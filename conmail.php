<?php
/**
 * SLN Consulting - Secure Contact Form Email Handler
 *
 * Implements:
 * - Anti-CSRF protection
 * - Honeypot spam bot trapping
 * - IP rate limiting
 * - Full field input validation (Name, Organisation, Designation, Email, Phone, Service, Message)
 * - Header injection prevention
 * - Preservation of user input on validation error
 * - Integration with existing mailer.php (sln_send_email)
 */

ini_set('display_errors', '0');
error_reporting(0);

require_once __DIR__ . '/security.php';
require_once __DIR__ . '/mailer.php';

sln_send_security_headers();
sln_start_session();

$isAjax = (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'xmlhttprequest')
    || (isset($_SERVER['HTTP_ACCEPT']) && strpos($_SERVER['HTTP_ACCEPT'], 'application/json') !== false);

function sln_respond_error($message, $isAjax, $formData = [], $httpCode = 400) {
    if (!empty($formData)) {
        $_SESSION['sln_form_data'] = $formData;
    }
    if ($isAjax) {
        http_response_code($httpCode);
        header('Content-Type: application/json; charset=UTF-8');
        echo json_encode([
            'success' => false,
            'status'  => 'error',
            'message' => $message
        ]);
        exit;
    }
    header('Location: contact.php?status=error&msg=' . urlencode($message) . '#contact-status');
    exit;
}

function sln_respond_success($message, $isAjax) {
    unset($_SESSION['sln_form_data']);
    if ($isAjax) {
        http_response_code(200);
        header('Content-Type: application/json; charset=UTF-8');
        echo json_encode([
            'success' => true,
            'status'  => 'success',
            'message' => $message
        ]);
        exit;
    }
    header('Location: contact.php?status=success#contact-status');
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    sln_respond_error('Invalid request method.', $isAjax, [], 405);
}

// 1. Rate Limiting Check
if (!sln_check_rate_limit(5, 300)) {
    sln_respond_error('Too many requests. Please wait a few minutes before submitting another enquiry.', $isAjax, $_POST, 429);
}

// 2. Honeypot Bot Trap Check
if (sln_is_honeypot_triggered()) {
    // Silently reject spam bot submission
    sln_respond_success('Your enquiry has been received.', $isAjax);
}

// 3. CSRF Verification
$submittedToken = $_POST['csrf_token'] ?? '';
if (!sln_verify_csrf_token($submittedToken)) {
    sln_respond_error('Security session expired. Please refresh the page and submit again.', $isAjax, $_POST, 403);
}

// 4. Input Validations
$rawName    = $_POST['Name'] ?? '';
$rawFname   = $_POST['Fname'] ?? '';
$rawSubject = $_POST['Subject'] ?? '';
$rawEmail   = $_POST['Email'] ?? '';
$rawNumber  = $_POST['Number'] ?? '';
$rawService = $_POST['Services'] ?? '';
$rawMessage = $_POST['Message'] ?? '';

// Validate Name
$vName = sln_validate_name($rawName);
if (!$vName['valid']) {
    sln_respond_error($vName['error'], $isAjax, $_POST);
}

// Validate Organisation
$vFname = sln_validate_organisation($rawFname);
if (!$vFname['valid']) {
    sln_respond_error($vFname['error'], $isAjax, $_POST);
}

// Validate Designation
$vSubject = sln_validate_designation($rawSubject);
if (!$vSubject['valid']) {
    sln_respond_error($vSubject['error'], $isAjax, $_POST);
}

// Validate Email
$vEmail = sln_validate_email($rawEmail);
if (!$vEmail['valid']) {
    sln_respond_error($vEmail['error'], $isAjax, $_POST);
}

// Validate Phone
$vNumber = sln_validate_phone($rawNumber);
if (!$vNumber['valid']) {
    sln_respond_error($vNumber['error'], $isAjax, $_POST);
}

// Validate Service (Required in Contact form)
$vService = sln_validate_service($rawService, true);
if (!$vService['valid']) {
    sln_respond_error($vService['error'], $isAjax, $_POST);
}

// Validate Message
$vMessage = sln_validate_message($rawMessage);
if (!$vMessage['valid']) {
    sln_respond_error($vMessage['error'], $isAjax, $_POST);
}

// Clean and prepare values
$cleanName        = sln_clean_header_value($vName['value']);
$cleanFname       = $vFname['value'];
$cleanDesignation = sln_clean_header_value($vSubject['value']);
$cleanEmail       = sln_clean_header_value($vEmail['value']);
$cleanNumber      = $vNumber['value'];
$serviceName      = $vService['name'];
$cleanMessage     = $vMessage['value'];

// Contextually encoded values for HTML email
$safeName        = htmlspecialchars($cleanName, ENT_QUOTES, 'UTF-8');
$safeFname       = htmlspecialchars($cleanFname, ENT_QUOTES, 'UTF-8');
$safeDesignation = htmlspecialchars($cleanDesignation, ENT_QUOTES, 'UTF-8');
$safeEmail       = htmlspecialchars($cleanEmail, ENT_QUOTES, 'UTF-8');
$safeNumber      = htmlspecialchars($cleanNumber, ENT_QUOTES, 'UTF-8');
$safeServiceName = htmlspecialchars($serviceName, ENT_QUOTES, 'UTF-8');
$safeMessage     = !empty($cleanMessage) ? nl2br(htmlspecialchars($cleanMessage, ENT_QUOTES, 'UTF-8')) : '<em>No additional details provided.</em>';
$date            = date('F j, Y, g:i a');

$htmlBody = <<<HTML
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f8fafc; margin: 0; padding: 20px; }
    .card { max-width: 600px; margin: 0 auto; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .header { background: #013df5; color: #ffffff; padding: 22px 24px; text-align: center; }
    .header h2 { margin: 0; font-size: 21px; font-weight: 600; letter-spacing: 0.5px; }
    .body { padding: 24px; color: #334155; }
    table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    td { padding: 10px 8px; border-bottom: 1px solid #f1f5f9; font-size: 14.5px; }
    td.label { width: 35%; font-weight: 600; color: #64748b; }
    td.val { color: #0f172a; }
    .badge { display: inline-block; background: #d7f1fa; color: #013df5; padding: 4px 10px; border-radius: 4px; font-weight: 600; font-size: 13px; }
    .footer { background: #f8fafc; padding: 14px 24px; text-align: center; font-size: 12px; color: #94a3b8; border-top: 1px solid #e2e8f0; }
</style>
</head>
<body>
<div class="card">
    <div class="header">
        <h2>New Website Enquiry</h2>
    </div>
    <div class="body">
        <p style="font-size: 15px; margin-top: 0;">You have received a new contact enquiry through the SLN Consulting website:</p>
        <table>
            <tr><td class="label">Name:</td><td class="val"><strong>{$safeName}</strong></td></tr>
            <tr><td class="label">Organisation:</td><td class="val">{$safeFname}</td></tr>
            <tr><td class="label">Designation:</td><td class="val">{$safeDesignation}</td></tr>
            <tr><td class="label">Email:</td><td class="val"><a href="mailto:{$safeEmail}">{$safeEmail}</a></td></tr>
            <tr><td class="label">Phone:</td><td class="val"><a href="tel:{$safeNumber}">{$safeNumber}</a></td></tr>
            <tr><td class="label">Service Required:</td><td class="val"><span class="badge">{$safeServiceName}</span></td></tr>
            <tr><td class="label" style="vertical-align: top;">Requirement:</td><td class="val">{$safeMessage}</td></tr>
        </table>
    </div>
    <div class="footer">
        Received on {$date} | SLN Consulting Website
    </div>
</div>
</body>
</html>
HTML;

$emailSubject = "Enquiry: {$cleanName} - {$serviceName}";

// Dispatch via existing sln_send_email in mailer.php
$sendResult = sln_send_email($emailSubject, $htmlBody, $cleanEmail, $cleanName);

if ($sendResult['success']) {
    sln_respond_success('Your enquiry has been submitted successfully.', $isAjax);
} else {
    // Log technical failure securely without exposing secrets
    error_log("[SLN Contact Form Error] Email dispatch failed: " . ($sendResult['error'] ?? 'Unknown error'));
    sln_respond_error('Unable to send your enquiry. Please try again later.', $isAjax, $_POST, 500);
}
