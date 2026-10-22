<?php
/**
 * SLN Consulting - Secure Email Transport Helper with PHPMailer & Authenticated SMTP
 * 
 * Supports:
 *  1. PHPMailer with Authenticated SMTP (TLS/SSL) - Primary Transport
 *  2. Pure PHP Authenticated SMTP Socket Fallback (if PHPMailer is absent)
 *  3. Resend REST API (HTTPS fallback)
 *  4. SendGrid REST API (HTTPS fallback)
 *  5. Brevo REST API (HTTPS fallback)
 *
 * Security & Reliability Features:
 * - Credentials stored in server environment variables or protected config outside webroot
 * - Placeholders safely detected without false success or exposure
 * - Header injection and CRLF sanitization
 * - Sensitive credential redaction from system error logs
 * - Visitor email assigned to Reply-To, never as authenticated SMTP sender
 * - Enquiries routed to srinivas.c@slnconsulting.co.in
 */

// 1. Autoload PHPMailer
$autoloadCandidates = [
    __DIR__ . '/vendor/autoload.php',
    dirname(__DIR__) . '/vendor/autoload.php',
    __DIR__ . '/vendor/phpmailer/phpmailer/src/PHPMailer.php'
];

foreach ($autoloadCandidates as $candidate) {
    if (file_exists($candidate)) {
        require_once $candidate;
        break;
    }
}

// 2. Load Configuration from Protected Sources (Outside Webroot or Local Environment)
$GLOBALS['sln_custom_config'] = [];

function sln_load_configuration($dir = null) {
    $dir = $dir ?: __DIR__;
    $parentDir = dirname($dir);

    // List of candidate configuration paths (outside public webroot prioritized)
    $candidateFiles = [
        $parentDir . '/sln-smtp-config.php',
        $parentDir . '/.env',
        $parentDir . '/.env.local',
        $dir . '/sln-smtp-config.php',
        $dir . '/.env',
        $dir . '/.env.local'
    ];

    foreach ($candidateFiles as $file) {
        if (!file_exists($file) || !is_readable($file)) {
            continue;
        }

        // Dedicated PHP config file returning an associative array
        if (substr($file, -4) === '.php') {
            try {
                $phpConfig = include $file;
                if (is_array($phpConfig)) {
                    foreach ($phpConfig as $key => $val) {
                        $key = trim((string)$key);
                        $val = trim((string)$val);
                        $GLOBALS['sln_custom_config'][$key] = $val;
                        if (!array_key_exists($key, $_ENV) && getenv($key) === false) {
                            putenv("{$key}={$val}");
                            $_ENV[$key] = $val;
                            $_SERVER[$key] = $val;
                        }
                    }
                }
            } catch (\Throwable $e) {}
            continue;
        }

        // Standard .env file
        $lines = @file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
        if ($lines) {
            foreach ($lines as $line) {
                $line = trim($line);
                if ($line === '' || $line[0] === '#') continue;
                if (strpos($line, '=') !== false) {
                    list($key, $val) = explode('=', $line, 2);
                    $key = trim($key);
                    $val = trim($val, " \t\n\r\0\x0B\"'");
                    $GLOBALS['sln_custom_config'][$key] = $val;
                    if (!array_key_exists($key, $_ENV) && getenv($key) === false) {
                        putenv("{$key}={$val}");
                        $_ENV[$key] = $val;
                        $_SERVER[$key] = $val;
                    }
                }
            }
        }
    }
}

sln_load_configuration();

/**
 * Retrieve configuration value from environment or custom loaded config.
 */
function sln_get_env($key, $default = null) {
    if (isset($GLOBALS['sln_custom_config'][$key]) && $GLOBALS['sln_custom_config'][$key] !== '') {
        return $GLOBALS['sln_custom_config'][$key];
    }
    if (isset($_ENV[$key]) && $_ENV[$key] !== '') {
        return $_ENV[$key];
    }
    if (isset($_SERVER[$key]) && $_SERVER[$key] !== '') {
        return $_SERVER[$key];
    }
    $val = getenv($key);
    if ($val !== false && $val !== '') {
        return $val;
    }
    return $default;
}

/**
 * Check if a configuration string is a placeholder or unconfigured.
 */
function sln_is_placeholder($val) {
    if ($val === null || $val === false) return true;
    $val = trim((string)$val);
    if ($val === '') return true;
    if (preg_match('/^(YOUR_|REPLACE_|CHANGEME|<your|placeholder)/i', $val)) return true;
    if ($val === 'YOUR_SMTP_PASSWORD_HERE' || $val === 'YOUR_PLESK_MAILBOX_PASSWORD' || $val === 'YOUR_SMTP_HOST_HERE') return true;
    return false;
}

/**
 * Resilient HTTP POST JSON client
 */
function sln_http_post_json($url, array $headers, $payloadJson) {
    // 1. Native cURL extension
    if (function_exists('curl_init')) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [
            CURLOPT_POST           => true,
            CURLOPT_POSTFIELDS     => $payloadJson,
            CURLOPT_HTTPHEADER     => $headers,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_TIMEOUT        => 15,
            CURLOPT_SSL_VERIFYPEER => true
        ]);
        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $curlErr  = curl_error($ch);
        curl_close($ch);

        if ($curlErr) {
            return ['code' => 0, 'body' => '', 'error' => $curlErr];
        }
        return ['code' => $httpCode, 'body' => $response, 'error' => null];
    }

    // 2. Stream context with HTTPS
    if (in_array('https', stream_get_wrappers())) {
        $headerStr = implode("\r\n", $headers) . "\r\n";
        $opts = [
            'http' => [
                'method'        => 'POST',
                'header'        => $headerStr,
                'content'       => $payloadJson,
                'ignore_errors' => true,
                'timeout'       => 15
            ]
        ];
        $context = stream_context_create($opts);
        $response = @file_get_contents($url, false, $context);
        $httpCode = 0;
        if (isset($http_response_header) && is_array($http_response_header)) {
            if (preg_match('#HTTP/\S+\s+(\d+)#', $http_response_header[0], $matches)) {
                $httpCode = (int)$matches[1];
            }
        }
        if ($response !== false) {
            return ['code' => $httpCode, 'body' => $response, 'error' => null];
        }
    }

    // 3. CLI curl (available on Windows 10/11 & Linux servers)
    if (function_exists('shell_exec')) {
        $headerArgs = '';
        foreach ($headers as $h) {
            $headerArgs .= ' -H ' . escapeshellarg($h);
        }
        $tmpPayload = tempnam(sys_get_temp_dir(), 'sln_mail_');
        if ($tmpPayload) {
            file_put_contents($tmpPayload, $payloadJson);
            $cmd = 'curl -s -w "\n%{http_code}" -X POST ' . escapeshellarg($url) . $headerArgs . ' --data-binary ' . escapeshellarg('@' . $tmpPayload);
            $output = @shell_exec($cmd);
            @unlink($tmpPayload);

            if ($output !== null && $output !== false) {
                $output = trim($output);
                $lastNewline = strrpos($output, "\n");
                if ($lastNewline !== false) {
                    $body = substr($output, 0, $lastNewline);
                    $code = (int)trim(substr($output, $lastNewline + 1));
                } else {
                    $body = '';
                    $code = (int)$output;
                }
                return ['code' => $code, 'body' => $body, 'error' => null];
            }
        }
    }

    return ['code' => 0, 'body' => '', 'error' => 'No HTTP transport available.'];
}

/**
 * Send email via Resend API (HTTPS POST).
 */
function sln_send_via_resend($apiKey, $from, array $recipients, $subject, $htmlBody, $replyTo = '') {
    $url = 'https://api.resend.com/emails';
    $payload = [
        'from'    => $from,
        'to'      => array_values($recipients),
        'subject' => $subject,
        'html'    => $htmlBody,
    ];
    if (!empty($replyTo)) {
        $payload['reply_to'] = $replyTo;
    }

    $headers = [
        'Authorization: Bearer ' . $apiKey,
        'Content-Type: application/json',
        'User-Agent: SLN-Website/1.0'
    ];

    $res = sln_http_post_json($url, $headers, json_encode($payload));
    if ($res['error']) {
        return ['success' => false, 'error' => "Network error connecting to email provider: {$res['error']}"];
    }

    $httpCode = $res['code'];
    $json = json_decode($res['body'], true);
    if ($httpCode >= 200 && $httpCode < 300 && isset($json['id'])) {
        return ['success' => true, 'id' => $json['id']];
    }

    $errorMsg = $json['message'] ?? ($json['error']['message'] ?? "HTTP {$httpCode}: {$res['body']}");
    return ['success' => false, 'error' => "Email delivery service returned: {$errorMsg}"];
}

/**
 * Send email via SendGrid API (HTTPS POST).
 */
function sln_send_via_sendgrid($apiKey, $from, array $recipients, $subject, $htmlBody, $replyTo = '') {
    $url = 'https://api.sendgrid.com/v3/mail/send';
    
    $fromEmail = $from;
    $fromName = 'SLN Consulting';
    if (preg_match('/^(.*?)\s*<([^>]+)>$/', $from, $m)) {
        $fromName = trim($m[1], " '\"");
        $fromEmail = $m[2];
    }

    $toList = [];
    foreach ($recipients as $r) {
        $toList[] = ['email' => trim($r)];
    }

    $payload = [
        'personalizations' => [['to' => $toList]],
        'from'             => ['email' => $fromEmail, 'name' => $fromName],
        'subject'          => $subject,
        'content'          => [['type' => 'text/html', 'value' => $htmlBody]]
    ];
    if (!empty($replyTo)) {
        $payload['reply_to'] = ['email' => $replyTo];
    }

    $headers = [
        'Authorization: Bearer ' . $apiKey,
        'Content-Type: application/json',
        'User-Agent: SLN-Website/1.0'
    ];

    $res = sln_http_post_json($url, $headers, json_encode($payload));
    if ($res['error']) {
        return ['success' => false, 'error' => "Network error connecting to SendGrid: {$res['error']}"];
    }

    $httpCode = $res['code'];
    if ($httpCode >= 200 && $httpCode < 300) {
        return ['success' => true];
    }

    $json = json_decode($res['body'], true);
    $errorMsg = isset($json['errors'][0]['message']) ? $json['errors'][0]['message'] : "HTTP {$httpCode}: {$res['body']}";
    return ['success' => false, 'error' => "SendGrid API error: {$errorMsg}"];
}

/**
 * Send email via Brevo / Sendinblue API (HTTPS POST).
 */
function sln_send_via_brevo($apiKey, $from, array $recipients, $subject, $htmlBody, $replyTo = '') {
    $url = 'https://api.brevo.com/v3/smtp/email';
    
    $fromEmail = $from;
    $fromName = 'SLN Consulting';
    if (preg_match('/^(.*?)\s*<([^>]+)>$/', $from, $m)) {
        $fromName = trim($m[1], " '\"");
        $fromEmail = $m[2];
    }

    $toList = [];
    foreach ($recipients as $r) {
        $toList[] = ['email' => trim($r)];
    }

    $payload = [
        'sender'      => ['email' => $fromEmail, 'name' => $fromName],
        'to'          => $toList,
        'subject'     => $subject,
        'htmlContent' => $htmlBody,
    ];
    if (!empty($replyTo)) {
        $payload['replyTo'] = ['email' => $replyTo];
    }

    $headers = [
        'api-key: ' . $apiKey,
        'Content-Type: application/json',
        'Accept: application/json'
    ];

    $res = sln_http_post_json($url, $headers, json_encode($payload));
    if ($res['error']) {
        return ['success' => false, 'error' => "Network error connecting to Brevo: {$res['error']}"];
    }

    $httpCode = $res['code'];
    if ($httpCode >= 200 && $httpCode < 300) {
        return ['success' => true];
    }

    $json = json_decode($res['body'], true);
    $errorMsg = $json['message'] ?? "HTTP {$httpCode}: {$res['body']}";
    return ['success' => false, 'error' => "Brevo API error: {$errorMsg}"];
}

/**
 * Send email via PHPMailer with Authenticated SMTP.
 *
 * Implements:
 * - PHPMailer object with full TLS/SSL/SMTPS negotiation
 * - Authenticated SLN mailbox as the From sender
 * - Visitor email assigned as Reply-To
 * - Enquiry directed to srinivas.c@slnconsulting.co.in
 * - Credential and password protection in logs
 */
function sln_send_via_phpmailer(array $config, array $recipients, $subject, $htmlBody, $replyTo = '', $replyToName = '') {
    // Autoload PHPMailer classes if not already declared
    if (!class_exists('\PHPMailer\PHPMailer\PHPMailer')) {
        $vendorPaths = [
            __DIR__ . '/vendor/autoload.php',
            dirname(__DIR__) . '/vendor/autoload.php',
            __DIR__ . '/vendor/phpmailer/phpmailer/src/PHPMailer.php'
        ];
        foreach ($vendorPaths as $p) {
            if (file_exists($p)) {
                require_once $p;
                break;
            }
        }
    }

    if (!class_exists('\PHPMailer\PHPMailer\PHPMailer')) {
        $logMsg = "[SLN PHPMailer Error] PHPMailer class is not loaded. Please verify vendor/autoload.php.";
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    }

    $mail = new \PHPMailer\PHPMailer\PHPMailer(true);

    try {
        // 1. SMTP Server Settings
        $mail->isSMTP();
        $mail->Host       = $config['host'];
        $mail->SMTPAuth   = true;
        $mail->Username   = $config['user'];
        $mail->Password   = $config['pass'];
        $mail->Timeout    = 15;
        $mail->CharSet    = 'UTF-8';

        // 2. Encryption and Port
        $port   = (int)($config['port'] ?? 465);
        $secure = strtolower((string)($config['secure'] ?? 'ssl'));

        if ($secure === 'ssl' || $secure === 'true' || $secure === '1' || $port === 465) {
            $mail->SMTPSecure = \PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_SMTPS;
            $mail->Port       = 465;
        } elseif ($secure === 'tls' || $port === 587) {
            $mail->SMTPSecure = \PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
            $mail->Port       = $port ?: 587;
        } else {
            $mail->SMTPSecure = false;
            $mail->SMTPAutoTLS = false;
            $mail->Port       = $port ?: 25;
        }

        // 3. Sender Identity (Authenticated SLN mailbox - Requirement 4)
        $fromEmail = $config['user'];
        $fromName  = 'SLN Consulting';
        if (!empty($config['from']) && preg_match('/^(.*?)\s*<([^>]+)>$/', $config['from'], $m)) {
            $fromName  = trim($m[1], " '\"");
            $fromEmail = trim($m[2]);
        } elseif (!empty($config['from']) && filter_var($config['from'], FILTER_VALIDATE_EMAIL)) {
            $fromEmail = $config['from'];
        }
        $mail->setFrom($fromEmail, $fromName);

        // 4. Reply-To (Visitor's submitted email and name - Requirement 5)
        if (!empty($replyTo) && filter_var($replyTo, FILTER_VALIDATE_EMAIL)) {
            $mail->addReplyTo($replyTo, $replyToName ?: $replyTo);
        }

        // 5. Recipients (Requirement 3: send to srinivas.c@slnconsulting.co.in)
        $validRecipients = [];
        foreach ($recipients as $toEmail) {
            $toEmail = trim($toEmail);
            if (!empty($toEmail) && filter_var($toEmail, FILTER_VALIDATE_EMAIL)) {
                $validRecipients[] = $toEmail;
            }
        }
        if (empty($validRecipients)) {
            $validRecipients[] = 'srinivas.c@slnconsulting.co.in';
        }
        foreach (array_unique($validRecipients) as $toEmail) {
            $mail->addAddress($toEmail);
        }

        // 6. Content
        $mail->isHTML(true);
        $mail->Subject = $subject;
        $mail->Body    = $htmlBody;
        $mail->AltBody = strip_tags(str_replace(['<br>', '<br/>', '<br />', '</p>'], "\n", $htmlBody));

        // 7. Dispatch
        $mail->send();

        error_log("[SLN SMTP Success] PHPMailer successfully accepted enquiry for delivery to: " . implode(', ', $validRecipients));
        return ['success' => true];
    } catch (\PHPMailer\PHPMailer\Exception $e) {
        $rawError = $e->getMessage();
        // Redact any password or sensitive token
        $sanitizedError = preg_replace('/Password:?\s*\S+/i', 'Password: [REDACTED]', $rawError);
        $logMsg = "[SLN PHPMailer Error] Email dispatch failed: {$sanitizedError}";
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    } catch (\Exception $e) {
        $logMsg = "[SLN PHPMailer Error] Unexpected error during dispatch: " . $e->getMessage();
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    }
}

/**
 * Fallback: Pure PHP Authenticated SMTP Socket Transport
 */
function sln_send_via_smtp(array $config, array $recipients, $subject, $htmlBody, $replyTo = '', $replyToName = '') {
    $host   = $config['host'];
    $port   = (int)($config['port'] ?? 465);
    $user   = $config['user'];
    $pass   = $config['pass'];
    $from   = $config['from'];
    $secure = strtolower($config['secure'] ?? 'ssl');

    $timeout = 15;
    $protocol = ($secure === 'ssl' || ($port === 465 && $secure !== 'tls')) ? 'ssl://' : '';
    
    $socket = @stream_socket_client($protocol . $host . ':' . $port, $errno, $errstr, $timeout);
    if (!$socket) {
        $logMsg = "[SLN SMTP Error: connection refused] Cannot connect to SMTP server ({$protocol}{$host}:{$port}) [Errno {$errno}]: {$errstr}";
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    }

    stream_set_timeout($socket, $timeout);

    $readResponse = function() use ($socket) {
        $response = '';
        while (!feof($socket)) {
            $line = fgets($socket, 512);
            if ($line === false) break;
            $response .= $line;
            if (isset($line[3]) && $line[3] === ' ') break;
        }
        return $response;
    };

    $sendCommand = function($cmd, $expectedCode) use ($socket, $readResponse) {
        fputs($socket, $cmd . "\r\n");
        $res = $readResponse();
        $code = substr(trim($res), 0, 3);
        if ($code !== (string)$expectedCode) {
            return ['ok' => false, 'error' => "SMTP Error [{$cmd}]: {$res}"];
        }
        return ['ok' => true, 'response' => $res];
    };

    // 1. Initial greeting
    $greet = $readResponse();
    if (substr(trim($greet), 0, 3) !== '220') {
        fclose($socket);
        $logMsg = "[SLN SMTP Error: SMTP server rejected the message] SMTP greeting failed: " . trim($greet);
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    }

    // 2. EHLO
    $helloHost = gethostname() ?: 'localhost';
    $ehlo = $sendCommand("EHLO {$helloHost}", 250);
    if (!$ehlo['ok']) {
        fclose($socket);
        $logMsg = "[SLN SMTP Error: SMTP server rejected the message] EHLO rejected: " . $ehlo['error'];
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    }

    // 3. STARTTLS
    $needsStarttls = ($protocol === '') && ($secure === 'tls' || $secure === 'starttls' || $port === 587);
    if ($needsStarttls) {
        $starttls = $sendCommand("STARTTLS", 220);
        if ($starttls['ok']) {
            $cryptoMethod = STREAM_CRYPTO_METHOD_TLS_CLIENT | STREAM_CRYPTO_METHOD_TLSv1_2_CLIENT;
            if (defined('STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT')) {
                $cryptoMethod |= STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT;
            }
            if (!@stream_socket_enable_crypto($socket, true, $cryptoMethod)) {
                fclose($socket);
                $logMsg = "[SLN SMTP Error: TLS/SSL failure] Failed to establish TLS encryption with SMTP server ({$host}:{$port}).";
                error_log($logMsg);
                return ['success' => false, 'error' => $logMsg];
            }
            // Repeat EHLO after TLS
            $ehlo2 = $sendCommand("EHLO {$helloHost}", 250);
            if (!$ehlo2['ok']) {
                fclose($socket);
                $logMsg = "[SLN SMTP Error: TLS/SSL failure] EHLO after STARTTLS failed: " . $ehlo2['error'];
                error_log($logMsg);
                return ['success' => false, 'error' => $logMsg];
            }
        } else {
            fclose($socket);
            $logMsg = "[SLN SMTP Error: TLS/SSL failure] STARTTLS rejected by SMTP server: " . $starttls['error'];
            error_log($logMsg);
            return ['success' => false, 'error' => $logMsg];
        }
    }

    // 4. AUTH LOGIN
    $auth = $sendCommand("AUTH LOGIN", 334);
    if (!$auth['ok']) {
        fclose($socket);
        $logMsg = "[SLN SMTP Error: SMTP authentication failed] AUTH LOGIN command rejected: " . $auth['error'];
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    }

    $authUser = $sendCommand(base64_encode($user), 334);
    if (!$authUser['ok']) {
        fclose($socket);
        $logMsg = "[SLN SMTP Error: SMTP authentication failed] SMTP username rejected: " . $authUser['error'];
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    }

    $authPass = $sendCommand(base64_encode($pass), 235);
    if (!$authPass['ok']) {
        fclose($socket);
        $logMsg = "[SLN SMTP Error: SMTP authentication failed] SMTP password/credentials rejected: " . $authPass['error'];
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    }

    // 5. MAIL FROM
    $cleanFrom = $from;
    if (preg_match('/<([^>]+)>/', $from, $m)) {
        $cleanFrom = $m[1];
    }
    $mailFrom = $sendCommand("MAIL FROM:<{$cleanFrom}>", 250);
    if (!$mailFrom['ok']) {
        fclose($socket);
        $logMsg = "[SLN SMTP Error: invalid sender] MAIL FROM:<{$cleanFrom}> rejected by server: " . $mailFrom['error'];
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    }

    // 6. RCPT TO
    $acceptedRcptCount = 0;
    foreach ($recipients as $toEmail) {
        $toEmail = trim($toEmail);
        if (empty($toEmail)) continue;
        $rcpt = $sendCommand("RCPT TO:<{$toEmail}>", 250);
        if (!$rcpt['ok']) {
            fclose($socket);
            $logMsg = "[SLN SMTP Error: invalid recipient] Recipient <{$toEmail}> rejected by server: " . $rcpt['error'];
            error_log($logMsg);
            return ['success' => false, 'error' => $logMsg];
        }
        $acceptedRcptCount++;
    }
    if ($acceptedRcptCount === 0) {
        fclose($socket);
        $logMsg = "[SLN SMTP Error: invalid recipient] No valid recipients provided.";
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    }

    // 7. DATA
    $data = $sendCommand("DATA", 354);
    if (!$data['ok']) {
        fclose($socket);
        $logMsg = "[SLN SMTP Error: SMTP server rejected the message] DATA command rejected: " . $data['error'];
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    }

    // 8. Headers & Body
    $headers = [];
    $headers[] = "Date: " . date('r');
    $headers[] = "From: {$from}";
    $headers[] = "To: " . implode(', ', $recipients);
    if (!empty($replyTo)) {
        $headers[] = !empty($replyToName) ? "Reply-To: {$replyToName} <{$replyTo}>" : "Reply-To: {$replyTo}";
    }
    $headers[] = "Subject: =?UTF-8?B?" . base64_encode($subject) . "?=";
    $headers[] = "MIME-Version: 1.0";
    $headers[] = "Content-Type: text/html; charset=UTF-8";
    $headers[] = "Content-Transfer-Encoding: base64";

    $messageContent = implode("\r\n", $headers) . "\r\n\r\n" . chunk_split(base64_encode($htmlBody)) . "\r\n.";

    fputs($socket, $messageContent . "\r\n");
    $dataRes = $readResponse();
    if (substr(trim($dataRes), 0, 3) !== '250') {
        fclose($socket);
        $logMsg = "[SLN SMTP Error: SMTP server rejected the message] Message data rejected by server: " . trim($dataRes);
        error_log($logMsg);
        return ['success' => false, 'error' => $logMsg];
    }

    // 9. QUIT
    fputs($socket, "QUIT\r\n");
    fclose($socket);

    error_log("[SLN SMTP Success] Email successfully accepted by SMTP server for delivery to: " . implode(', ', $recipients));
    return ['success' => true];
}

/**
 * Dedicated SMTP Enquiry Dispatcher
 */
function sln_send_enquiry_smtp($subject, $htmlContent, $replyToEmail, $replyToName = '') {
    $recipientsRaw = sln_get_env('RECIPIENT_EMAIL', 'srinivas.c@slnconsulting.co.in');
    $recipients = array_unique(array_filter(array_map('trim', explode(',', $recipientsRaw))));
    if (empty($recipients)) {
        $recipients = ['srinivas.c@slnconsulting.co.in'];
    }

    $defaultFrom = sln_get_env('SMTP_FROM', sln_get_env('SMTP_USER', 'srinivas.c@slnconsulting.co.in'));

    $smtpHost = sln_get_env('SMTP_HOST');
    $smtpUser = sln_get_env('SMTP_USER');
    $smtpPass = sln_get_env('SMTP_PASS');

    $missingCredentials = [];
    if (sln_is_placeholder($smtpHost)) $missingCredentials[] = 'SMTP_HOST';
    if (sln_is_placeholder($smtpUser)) $missingCredentials[] = 'SMTP_USER';
    if (sln_is_placeholder($smtpPass)) $missingCredentials[] = 'SMTP_PASS';

    if (!empty($missingCredentials)) {
        $logMsg = "[SLN SMTP Error: SMTP credentials missing] Cannot dispatch enquiry via SMTP. Missing or unconfigured placeholder server variables: " . implode(', ', $missingCredentials) . ".";
        error_log($logMsg);
        return [
            'success' => false,
            'error'   => $logMsg
        ];
    }

    $smtpConfig = [
        'host'   => $smtpHost,
        'port'   => sln_get_env('SMTP_PORT', '465'),
        'user'   => $smtpUser,
        'pass'   => $smtpPass,
        'from'   => $defaultFrom,
        'secure' => sln_get_env('SMTP_SECURE', 'ssl')
    ];

    if (class_exists('\PHPMailer\PHPMailer\PHPMailer') || file_exists(__DIR__ . '/vendor/autoload.php')) {
        return sln_send_via_phpmailer($smtpConfig, $recipients, $subject, $htmlContent, $replyToEmail, $replyToName);
    }

    return sln_send_via_smtp($smtpConfig, $recipients, $subject, $htmlContent, $replyToEmail, $replyToName);
}

/**
 * Generic Mail Dispatcher to arbitrary recipient(s)
 */
function sln_send_message_to(array $recipients, $subject, $htmlContent, $replyToEmail = '', $replyToName = '') {
    // Sanitize subject and reply-to to prevent header injection
    $subject      = preg_replace('/[\r\n\t\x00-\x1f]/', '', $subject);
    $replyToEmail = preg_replace('/[\r\n\t\x00-\x1f]/', '', trim($replyToEmail));
    $replyToName  = preg_replace('/[\r\n\t\x00-\x1f]/', '', trim($replyToName));

    $validRecipients = [];
    foreach ($recipients as $toEmail) {
        $toEmail = trim($toEmail);
        if (!empty($toEmail) && filter_var($toEmail, FILTER_VALIDATE_EMAIL)) {
            $validRecipients[] = $toEmail;
        }
    }
    $validRecipients = array_unique($validRecipients);
    if (empty($validRecipients)) {
        return ['success' => false, 'error' => 'No valid recipients provided.'];
    }

    $defaultFrom = sln_get_env('SMTP_FROM', sln_get_env('SMTP_USER', 'srinivas.c@slnconsulting.co.in'));

    // 1. Authenticated SMTP with PHPMailer / Pure PHP Socket
    $smtpHost   = sln_get_env('SMTP_HOST');
    $smtpUser   = sln_get_env('SMTP_USER');
    $smtpPass   = sln_get_env('SMTP_PASS');
    $smtpPort   = sln_get_env('SMTP_PORT', '465');
    $smtpSecure = sln_get_env('SMTP_SECURE', 'ssl');

    $missingSmtp = [];
    if (sln_is_placeholder($smtpHost)) $missingSmtp[] = 'SMTP_HOST';
    if (sln_is_placeholder($smtpUser)) $missingSmtp[] = 'SMTP_USER';
    if (sln_is_placeholder($smtpPass)) $missingSmtp[] = 'SMTP_PASS';

    if (empty($missingSmtp)) {
        $smtpConfig = [
            'host'   => $smtpHost,
            'port'   => $smtpPort,
            'user'   => $smtpUser,
            'pass'   => $smtpPass,
            'from'   => $defaultFrom,
            'secure' => $smtpSecure
        ];

        // Prefer PHPMailer
        if (class_exists('\PHPMailer\PHPMailer\PHPMailer') || file_exists(__DIR__ . '/vendor/autoload.php')) {
            return sln_send_via_phpmailer($smtpConfig, $validRecipients, $subject, $htmlContent, $replyToEmail, $replyToName);
        }
        return sln_send_via_smtp($smtpConfig, $validRecipients, $subject, $htmlContent, $replyToEmail, $replyToName);
    }

    // 2. Resend API
    $resendKey = sln_get_env('RESEND_API_KEY');
    if (!empty($resendKey) && !sln_is_placeholder($resendKey)) {
        $from = $defaultFrom;
        if ($from === 'SLN Consulting <notifications@slnconsulting.co.in>' && !sln_get_env('MAIL_FROM')) {
            $from = 'SLN Consulting <onboarding@resend.dev>';
        }
        return sln_send_via_resend($resendKey, $from, $validRecipients, $subject, $htmlContent, $replyToEmail);
    }

    // 3. SendGrid API
    $sendgridKey = sln_get_env('SENDGRID_API_KEY');
    if (!empty($sendgridKey) && !sln_is_placeholder($sendgridKey)) {
        return sln_send_via_sendgrid($sendgridKey, $defaultFrom, $validRecipients, $subject, $htmlContent, $replyToEmail);
    }

    // 4. Brevo API
    $brevoKey = sln_get_env('BREVO_API_KEY');
    if (!empty($brevoKey) && !sln_is_placeholder($brevoKey)) {
        return sln_send_via_brevo($brevoKey, $defaultFrom, $validRecipients, $subject, $htmlContent, $replyToEmail);
    }

    // 5. No mail provider configured
    $missingList = implode(', ', $missingSmtp);
    $logMsg = "[SLN SMTP Error: SMTP credentials missing] Server environment variables are missing or unconfigured placeholders: {$missingList}. Email cannot be delivered.";
    error_log($logMsg);

    return [
        'success' => false,
        'error'   => $logMsg
    ];
}

/**
 * Primary Email Dispatcher to SLN Admin Mailbox
 */
function sln_send_email($subject, $htmlContent, $replyToEmail, $replyToName = '') {
    $recipientsRaw = sln_get_env('RECIPIENT_EMAIL', 'srinivas.c@slnconsulting.co.in');
    $recipients = array_unique(array_filter(array_map('trim', explode(',', $recipientsRaw))));
    if (empty($recipients)) {
        $recipients = ['srinivas.c@slnconsulting.co.in'];
    }
    return sln_send_message_to($recipients, $subject, $htmlContent, $replyToEmail, $replyToName);
}

/**
 * Automatic Visitor Acknowledgement Email Dispatcher
 */
function sln_send_visitor_acknowledgement($visitorEmail, $visitorName, $subjectText, $submissionDate = null) {
    $visitorEmail = trim((string)$visitorEmail);
    if (!filter_var($visitorEmail, FILTER_VALIDATE_EMAIL)) {
        return ['success' => false, 'error' => 'Invalid visitor email address for acknowledgement.'];
    }

    $submissionDate = $submissionDate ?: date('F j, Y, g:i a');
    $visitorName = trim((string)$visitorName) ?: 'Valued Visitor';
    $subjectText = trim((string)$subjectText) ?: 'Website Enquiry';

    $safeVisitorName = htmlspecialchars($visitorName, ENT_QUOTES, 'UTF-8');
    $safeSubject     = htmlspecialchars($subjectText, ENT_QUOTES, 'UTF-8');
    $safeDate        = htmlspecialchars($submissionDate, ENT_QUOTES, 'UTF-8');
    $currentYear     = date('Y');

    $htmlBody = <<<HTML
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f8fafc; margin: 0; padding: 20px; }
    .card { max-width: 600px; margin: 0 auto; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .header { background: #013df5; color: #ffffff; padding: 22px 24px; text-align: center; }
    .header h2 { margin: 0; font-size: 20px; font-weight: 600; letter-spacing: 0.5px; }
    .body { padding: 26px 28px; color: #334155; line-height: 1.6; font-size: 15px; }
    .details-box { background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #013df5; border-radius: 6px; padding: 14px 18px; margin: 20px 0; }
    .details-box h3 { margin: 0 0 10px 0; font-size: 14.5px; color: #013df5; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
    .details-box p { margin: 6px 0; font-size: 14.5px; }
    .details-box strong { color: #0f172a; }
    .footer { background: #f8fafc; padding: 16px 24px; text-align: center; font-size: 12.5px; color: #64748b; border-top: 1px solid #e2e8f0; }
    .footer a { color: #013df5; text-decoration: none; font-weight: 500; }
</style>
</head>
<body>
<div class="card">
    <div class="header">
        <h2>SLN Consulting</h2>
    </div>
    <div class="body">
        <p>Dear {$safeVisitorName},</p>
        <p>Thank you for contacting SLN Consulting.</p>
        <p>We have successfully received your enquiry. Our team will review your message and get back to you as soon as possible.</p>
        <div class="details-box">
            <h3>Your Enquiry Details</h3>
            <p><strong>Subject:</strong> {$safeSubject}</p>
            <p><strong>Received on:</strong> {$safeDate}</p>
        </div>
        <p>Thank you for your interest in SLN Consulting.</p>
        <p style="margin-bottom: 0;">Best regards,<br><strong>SLN Consulting Team</strong><br><a href="https://www.slnconsulting.co.in/">https://www.slnconsulting.co.in/</a></p>
    </div>
    <div class="footer">
        &copy; {$currentYear} SLN Consulting. All rights reserved.
    </div>
</div>
</body>
</html>
HTML;

    $subject = "We Have Received Your Enquiry – SLN Consulting";
    $fromEmail = sln_get_env('SMTP_USER', 'srinivas.c@slnconsulting.co.in');

    return sln_send_message_to(
        [$visitorEmail],
        $subject,
        $htmlBody,
        $fromEmail,
        'SLN Consulting'
    );
}
