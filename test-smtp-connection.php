<?php
/**
 * SLN Consulting - Command-Line SMTP Diagnostic & Verification Tool
 *
 * Usage on Plesk Server via SSH / CLI:
 *   php test-smtp-connection.php
 *
 * Security: Web access is strictly prohibited (returns 403 Forbidden).
 */

if (php_sapi_name() !== 'cli') {
    http_response_code(403);
    echo "<h1>403 Forbidden</h1><p>This diagnostic script can only be run via command line (CLI).</p>";
    exit(1);
}

define('SLN_CONFIG_ALLOWED', true);

echo "===============================================================\n";
echo " SLN Consulting - PHPMailer Authenticated SMTP Verification\n";
echo "===============================================================\n\n";

// 1. Load mailer helper & dependencies
require_once __DIR__ . '/mailer.php';

// 2. Inspect PHPMailer Availability
echo "[1/5] Checking PHPMailer Library:\n";
$phpmailerLoaded = class_exists('\PHPMailer\PHPMailer\PHPMailer');
if ($phpmailerLoaded) {
    echo "  [OK] PHPMailer library loaded successfully.\n\n";
} else {
    echo "  [FAIL] PHPMailer library NOT found. Please verify vendor/autoload.php.\n\n";
    exit(1);
}

// 3. Inspect SMTP Configuration
echo "[2/5] Inspecting SMTP Configuration:\n";
$host    = sln_get_env('SMTP_HOST');
$port    = sln_get_env('SMTP_PORT', '465');
$user    = sln_get_env('SMTP_USER');
$pass    = sln_get_env('SMTP_PASS');
$secure  = sln_get_env('SMTP_SECURE', 'ssl');
$from    = sln_get_env('SMTP_FROM', sln_get_env('SMTP_USER', 'srinivas.c@slnconsulting.co.in'));
$toRaw   = sln_get_env('RECIPIENT_EMAIL', 'srinivas.c@slnconsulting.co.in');
$recipients = array_unique(array_filter(array_map('trim', explode(',', $toRaw))));

echo "  Host:   " . ($host ?: '[NOT SET]') . "\n";
echo "  Port:   " . $port . "\n";
echo "  Secure: " . $secure . "\n";
echo "  User:   " . ($user ?: '[NOT SET]') . "\n";
echo "  Pass:   " . (sln_is_placeholder($pass) ? '[PLACEHOLDER / NOT CONFIGURED]' : '[CONFIGURED - ' . strlen($pass) . ' chars]') . "\n";
echo "  From:   " . $from . "\n";
echo "  To:     " . implode(', ', $recipients) . "\n\n";

if (sln_is_placeholder($host) || sln_is_placeholder($user) || sln_is_placeholder($pass)) {
    echo "[!] Configuration Incomplete:\n";
    echo "    One or more required SMTP settings are missing or still set to placeholder values.\n";
    echo "    Please configure your real credentials in your server environment variables or in\n";
    echo "    sln-smtp-config.php outside the public webroot.\n\n";
    echo "    Status: SMTP is NOT connected yet. Placeholders are active.\n";
    exit(2);
}

// 4. Test Network Reachability & DNS
echo "[3/5] Testing Network Reachability to {$host}:{$port}...\n";
$resolvedIp = @gethostbyname($host);
if ($resolvedIp === $host && !filter_var($host, FILTER_VALIDATE_IP)) {
    echo "  [FAIL] DNS Resolution Error: Hostname '{$host}' cannot be resolved.\n";
    echo "         Diagnosis: No DNS A/CNAME record exists for '{$host}'.\n";
    echo "         Action Required: Verify SMTP host setting (e.g. smtpout.secureserver.net for GoDaddy).\n\n";
    exit(3);
}
echo "  [OK] Hostname '{$host}' resolved to IP: {$resolvedIp}\n";

$errno = 0;
$errstr = '';
$socket = @fsockopen($host, (int)$port, $errno, $errstr, 10);
if ($socket) {
    echo "  [OK] TCP connection to {$host}:{$port} established successfully.\n\n";
    fclose($socket);
} else {
    echo "  [FAIL] Unable to connect to {$host}:{$port} (Err {$errno}: {$errstr}).\n";
    echo "         Tip: Check firewall or try Port 465 (SMTPS) vs Port 587 (TLS).\n\n";
    exit(3);
}

// 5. Test Live Message Dispatch via PHPMailer
echo "[4/5] Attempting Authenticated SMTP Dispatch via PHPMailer...\n";
$testSubject = "[SLN Test] SMTP Verification - " . date('Y-m-d H:i:s');
$testBody = "<h3>SLN Consulting - SMTP Connectivity Test</h3><p>This is a verified test email sent via authenticated PHPMailer.</p><p>Timestamp: " . date('r') . "</p>";

$result = sln_send_via_phpmailer(
    [
        'host'   => $host,
        'port'   => $port,
        'user'   => $user,
        'pass'   => $pass,
        'secure' => $secure,
        'from'   => $from
    ],
    $recipients,
    $testSubject,
    $testBody,
    'noreply@dreamscreen.co.in',
    'SLN Verification Bot'
);

echo "[5/5] Result:\n";
if ($result['success']) {
    echo "  ===============================================================\n";
    echo "  [SUCCESS] Real test email was accepted by the SMTP mail server!\n";
    echo "  Recipients: " . implode(', ', $recipients) . "\n";
    echo "  Status: SMTP is VERIFIED and WORKING.\n";
    echo "  ===============================================================\n";
    exit(0);
} else {
    echo "  ===============================================================\n";
    echo "  [FAILED] SMTP server rejected the dispatch.\n";
    echo "  Error: " . ($result['error'] ?? 'Unknown error') . "\n";
    echo "  Status: SMTP is NOT working yet. Please verify mailbox credentials.\n";
    echo "  ===============================================================\n";
    exit(4);
}
