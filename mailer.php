<?php
/**
 * SLN Consulting - Secure Email Transport Helper
 * 
 * Compatible with Vercel Serverless (PHP runtime) and local PHP development.
 * Supports:
 *  1. Resend REST API (Recommended for Vercel)
 *  2. SendGrid REST API
 *  3. Brevo (Sendinblue) REST API
 *  4. Authenticated SMTP (TLS/SSL socket client without Composer dependencies)
 *
 * Keeps all credentials in environment variables.
 * Prevents raw PHP warnings and header injection.
 */

// Load .env or .env.local if present (useful for local development)
function sln_load_dotenv($dir = null) {
    $dir = $dir ?: __DIR__;
    $files = [$dir . '/.env', $dir . '/.env.local'];
    foreach ($files as $file) {
        if (file_exists($file) && is_readable($file)) {
            $lines = file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
            foreach ($lines as $line) {
                $line = trim($line);
                if ($line === '' || $line[0] === '#') continue;
                if (strpos($line, '=') !== false) {
                    list($key, $val) = explode('=', $line, 2);
                    $key = trim($key);
                    $val = trim($val, " \t\n\r\0\x0B\"'");
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
sln_load_dotenv();

/**
 * Retrieve configuration value from environment.
 */
function sln_get_env($key, $default = null) {
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
 * Resilient HTTP POST JSON client
 * Supports:
 * 1. Native PHP cURL extension (standard on Vercel Linux PHP runtime)
 * 2. PHP stream wrappers with openssl (file_get_contents)
 * 3. CLI curl fallback (Windows & Linux command line)
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

    return ['code' => 0, 'body' => '', 'error' => 'No HTTP transport (cURL extension, HTTPS stream wrapper, or CLI cURL) available.'];
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
 * Send email via Authenticated SMTP Socket (Pure PHP, zero external dependencies).
 */
function sln_send_via_smtp(array $config, array $recipients, $subject, $htmlBody, $replyTo = '', $replyToName = '') {
    $host   = $config['host'];
    $port   = (int)($config['port'] ?? 587);
    $user   = $config['user'];
    $pass   = $config['pass'];
    $from   = $config['from'];
    $secure = strtolower($config['secure'] ?? 'tls');

    $timeout = 15;
    $protocol = ($secure === 'ssl' || $port === 465) ? 'ssl://' : '';
    
    $socket = @stream_socket_client($protocol . $host . ':' . $port, $errno, $errstr, $timeout);
    if (!$socket) {
        return ['success' => false, 'error' => "Cannot connect to SMTP server ({$host}:{$port}): {$errstr}"];
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
        return ['success' => false, 'error' => "SMTP greeting failed: {$greet}"];
    }

    // 2. EHLO
    $helloHost = gethostname() ?: 'localhost';
    $ehlo = $sendCommand("EHLO {$helloHost}", 250);
    if (!$ehlo['ok']) {
        fclose($socket);
        return ['success' => false, 'error' => $ehlo['error']];
    }

    // 3. STARTTLS
    if ($secure === 'tls' || ($port === 587 && $protocol === '')) {
        $starttls = $sendCommand("STARTTLS", 220);
        if ($starttls['ok']) {
            $cryptoMethod = STREAM_CRYPTO_METHOD_TLS_CLIENT | STREAM_CRYPTO_METHOD_TLSv1_2_CLIENT;
            if (defined('STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT')) {
                $cryptoMethod |= STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT;
            }
            if (!@stream_socket_enable_crypto($socket, true, $cryptoMethod)) {
                fclose($socket);
                return ['success' => false, 'error' => "Failed to establish TLS encryption with SMTP server."];
            }
            // Repeat EHLO after TLS
            $ehlo2 = $sendCommand("EHLO {$helloHost}", 250);
            if (!$ehlo2['ok']) {
                fclose($socket);
                return ['success' => false, 'error' => $ehlo2['error']];
            }
        }
    }

    // 4. AUTH LOGIN
    $auth = $sendCommand("AUTH LOGIN", 334);
    if (!$auth['ok']) {
        fclose($socket);
        return ['success' => false, 'error' => $auth['error']];
    }

    $authUser = $sendCommand(base64_encode($user), 334);
    if (!$authUser['ok']) {
        fclose($socket);
        return ['success' => false, 'error' => "SMTP username rejected: " . $authUser['error']];
    }

    $authPass = $sendCommand(base64_encode($pass), 235);
    if (!$authPass['ok']) {
        fclose($socket);
        return ['success' => false, 'error' => "SMTP authentication failed: " . $authPass['error']];
    }

    // 5. MAIL FROM
    $cleanFrom = $from;
    if (preg_match('/<([^>]+)>/', $from, $m)) {
        $cleanFrom = $m[1];
    }
    $mailFrom = $sendCommand("MAIL FROM:<{$cleanFrom}>", 250);
    if (!$mailFrom['ok']) {
        fclose($socket);
        return ['success' => false, 'error' => $mailFrom['error']];
    }

    // 6. RCPT TO
    foreach ($recipients as $toEmail) {
        $toEmail = trim($toEmail);
        if (empty($toEmail)) continue;
        $rcpt = $sendCommand("RCPT TO:<{$toEmail}>", 250);
        if (!$rcpt['ok']) {
            fclose($socket);
            return ['success' => false, 'error' => "Recipient {$toEmail} rejected: " . $rcpt['error']];
        }
    }

    // 7. DATA
    $data = $sendCommand("DATA", 354);
    if (!$data['ok']) {
        fclose($socket);
        return ['success' => false, 'error' => $data['error']];
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
        return ['success' => false, 'error' => "Failed to deliver message data: {$dataRes}"];
    }

    // 9. QUIT
    fputs($socket, "QUIT\r\n");
    fclose($socket);

    return ['success' => true];
}

/**
 * Primary Email Dispatcher
 *
 * Checks configured environment variables and dispatches using the appropriate transport.
 * If no external email service is configured, returns a user-friendly error without PHP warnings.
 */
function sln_send_email($subject, $htmlContent, $replyToEmail, $replyToName = '') {
    // Sanitize subject and reply-to to prevent header injection
    $subject      = str_replace(["\r", "\n"], '', $subject);
    $replyToEmail = str_replace(["\r", "\n"], '', trim($replyToEmail));
    $replyToName  = str_replace(["\r", "\n"], '', trim($replyToName));

    // Default recipients as requested
    $recipientsRaw = sln_get_env('RECIPIENT_EMAIL', 'srinivas.c@slnconsulting.co.in,schakravarthy@hotmail.com');
    $recipients = array_filter(array_map('trim', explode(',', $recipientsRaw)));

    $defaultFrom = sln_get_env('MAIL_FROM', 'SLN Consulting <notifications@slnconsulting.co.in>');

    // 1. Resend API (Recommended for Vercel)
    $resendKey = sln_get_env('RESEND_API_KEY');
    if (!empty($resendKey)) {
        $from = $defaultFrom;
        // Resend free tier without custom domain uses onboarding@resend.dev
        if ($from === 'SLN Consulting <notifications@slnconsulting.co.in>' && !sln_get_env('MAIL_FROM')) {
            $from = 'SLN Consulting <onboarding@resend.dev>';
        }
        return sln_send_via_resend($resendKey, $from, $recipients, $subject, $htmlContent, $replyToEmail);
    }

    // 2. SendGrid API
    $sendgridKey = sln_get_env('SENDGRID_API_KEY');
    if (!empty($sendgridKey)) {
        return sln_send_via_sendgrid($sendgridKey, $defaultFrom, $recipients, $subject, $htmlContent, $replyToEmail);
    }

    // 3. Brevo API
    $brevoKey = sln_get_env('BREVO_API_KEY');
    if (!empty($brevoKey)) {
        return sln_send_via_brevo($brevoKey, $defaultFrom, $recipients, $subject, $htmlContent, $replyToEmail);
    }

    // 4. Authenticated SMTP
    $smtpHost = sln_get_env('SMTP_HOST');
    $smtpUser = sln_get_env('SMTP_USER');
    $smtpPass = sln_get_env('SMTP_PASS');
    if (!empty($smtpHost) && !empty($smtpUser) && !empty($smtpPass)) {
        $smtpConfig = [
            'host'   => $smtpHost,
            'port'   => sln_get_env('SMTP_PORT', '587'),
            'user'   => $smtpUser,
            'pass'   => $smtpPass,
            'from'   => sln_get_env('SMTP_FROM', $defaultFrom),
            'secure' => sln_get_env('SMTP_SECURE', 'tls')
        ];
        return sln_send_via_smtp($smtpConfig, $recipients, $subject, $htmlContent, $replyToEmail, $replyToName);
    }

    // 5. No mail provider configured
    return [
        'success' => false,
        'error'   => 'Email service configuration is pending. Please set RESEND_API_KEY or SMTP credentials in your environment variables. In the meantime, please contact us directly at srinivas.c@slnconsulting.co.in or +91 9940196195.'
    ];
}
