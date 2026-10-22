<?php
/**
 * SLN Consulting - Server-Side SMTP Configuration Template
 *
 * HOW TO USE FOR PLESK HOSTING:
 * -------------------------------------------------------------
 * 1. Copy this file OUTSIDE your public webroot (outside httpdocs).
 *    For example:
 *    Linux Plesk:   /var/www/vhosts/slnconsulting.co.in/sln-smtp-config.php
 *    Windows Plesk: C:\Inetpub\vhosts\slnconsulting.co.in\sln-smtp-config.php
 *
 * 2. Replace 'YOUR_SMTP_PASSWORD_HERE' with your actual mailbox password.
 * 3. mailer.php will automatically detect and load this file outside httpdocs.
 *
 * NOTE: If preferred, you can also define these directly in Plesk:
 * Domains -> slnconsulting.co.in -> PHP Settings -> Additional configuration directives:
 * putenv("SMTP_HOST=mail.slnconsulting.co.in");
 * putenv("SMTP_PORT=465");
 * putenv("SMTP_SECURE=ssl");
 * putenv("SMTP_USER=srinivas.c@slnconsulting.co.in");
 * putenv("SMTP_PASS=YOUR_REAL_PASSWORD");
 * putenv("RECIPIENT_EMAIL=srinivas.c@slnconsulting.co.in");
 */

if (!defined('SLN_CONFIG_ALLOWED') && basename($_SERVER['PHP_SELF'] ?? '') === basename(__FILE__)) {
    http_response_code(403);
    exit('Direct access not permitted.');
}

return [
    // GoDaddy Outgoing SMTP Server Hostname
    'SMTP_HOST'       => 'smtpout.secureserver.net',

    // SMTP Port: 465 for SSL/TLS (implicit SSL)
    'SMTP_PORT'       => 465,

    // Security protocol: 'ssl' (port 465)
    'SMTP_SECURE'     => 'ssl',

    // Authenticated Mailbox Username
    'SMTP_USER'       => 'srinivas.c@slnconsulting.co.in',

    // Authenticated Mailbox Password (Replace placeholder with your real GoDaddy mailbox password)
    'SMTP_PASS'       => 'YOUR_ACTUAL_GODADDY_MAILBOX_PASSWORD',

    // Authenticated Sender Address shown in From header
    'SMTP_FROM'       => 'srinivas.c@slnconsulting.co.in',

    // Admin mailbox that receives website enquiries
    'RECIPIENT_EMAIL' => 'srinivas.c@slnconsulting.co.in',
];
