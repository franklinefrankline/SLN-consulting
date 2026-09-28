<?php
/**
 * SLN Consulting - Contact Form Email Handler
 */

// Suppress internal PHP warnings from reaching visitors
ini_set('display_errors', '0');
error_reporting(0);

require_once __DIR__ . '/mailer.php';

function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    // Strip CR and LF to prevent header injection
    $data = str_replace(["\r", "\n"], '', $data);
    return $data;
}

$isAjax = (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'xmlhttprequest')
    || (isset($_SERVER['HTTP_ACCEPT']) && strpos($_SERVER['HTTP_ACCEPT'], 'application/json') !== false);

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    if ($isAjax) {
        header('Content-Type: application/json; charset=UTF-8');
        echo json_encode(['status' => 'error', 'message' => 'Invalid request method.']);
        exit;
    }
    header('Location: contact.php');
    exit;
}

// Validate required fields
if (
    !empty($_POST['Name']) &&
    !empty($_POST['Fname']) &&
    !empty($_POST['Subject']) &&
    !empty($_POST['Email']) &&
    !empty($_POST['Number']) &&
    !empty($_POST['Services'])
) {
    $name    = test_input($_POST['Name']);
    $fname   = test_input($_POST['Fname']);
    $subject = test_input($_POST['Subject']);
    $email   = trim($_POST['Email']);
    $number  = test_input($_POST['Number']);
    $service = test_input($_POST['Services']);
    $text    = isset($_POST['Message']) ? trim($_POST['Message']) : '';

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errorMsg = 'Please provide a valid email address.';
        if ($isAjax) {
            header('Content-Type: application/json; charset=UTF-8');
            echo json_encode(['status' => 'error', 'message' => $errorMsg]);
            exit;
        }
        header('Location: contact.php?status=error&msg=' . urlencode($errorMsg) . '#contact-status');
        exit;
    }

    // Friendly service mapping including newly added VAPT and Cybersecurity Internship
    $serviceMap = [
        'soc'                      => 'SOC As A Service',
        'vapt'                     => 'VAPT',
        'cybersecurity_internship' => 'Cybersecurity Internship',
        'skilling'                 => 'Skilling',
        'cambridge'                => 'Cambridge',
        'nure'                     => 'ISC2',
        'ec'                       => 'EC-Council',
        'it_services'              => 'IT Services'
    ];
    $serviceName = $serviceMap[$service] ?? htmlspecialchars($service);

    // Build email HTML body
    $safeName    = htmlspecialchars($name);
    $safeFname   = htmlspecialchars($fname);
    $safeSubject = htmlspecialchars($subject);
    $safeEmail   = htmlspecialchars($email);
    $safeNumber  = htmlspecialchars($number);
    $safeMessage = !empty($text) ? nl2br(htmlspecialchars($text)) : '<em>No additional details provided.</em>';
    $date        = date('F j, Y, g:i a');

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
            <tr><td class="label">Designation:</td><td class="val">{$safeSubject}</td></tr>
            <tr><td class="label">Email:</td><td class="val"><a href="mailto:{$safeEmail}">{$safeEmail}</a></td></tr>
            <tr><td class="label">Phone:</td><td class="val"><a href="tel:{$safeNumber}">{$safeNumber}</a></td></tr>
            <tr><td class="label">Service Required:</td><td class="val"><span class="badge">{$serviceName}</span></td></tr>
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

    $emailSubject = "Enquiry: {$name} - {$serviceName}";

    $sendResult = sln_send_email($emailSubject, $htmlBody, $email, $name);

    if ($sendResult['success']) {
        if ($isAjax) {
            header('Content-Type: application/json; charset=UTF-8');
            echo json_encode([
                'status'  => 'success',
                'message' => 'Thank you! Your message has been sent successfully. We will get in touch shortly.'
            ]);
            exit;
        }
        header('Location: contact.php?status=success#contact-status');
        exit;
    } else {
        $errMsg = $sendResult['error'] ?? 'Unable to send message right now.';
        if ($isAjax) {
            header('Content-Type: application/json; charset=UTF-8');
            echo json_encode([
                'status'  => 'error',
                'message' => $errMsg
            ]);
            exit;
        }
        header('Location: contact.php?status=error&msg=' . urlencode($errMsg) . '#contact-status');
        exit;
    }
} else {
    $missingMsg = 'Please fill out all required fields marked with an asterisk (*).';
    if ($isAjax) {
        header('Content-Type: application/json; charset=UTF-8');
        echo json_encode(['status' => 'error', 'message' => $missingMsg]);
        exit;
    }
    header('Location: contact.php?status=error&msg=' . urlencode($missingMsg) . '#contact-status');
    exit;
}
