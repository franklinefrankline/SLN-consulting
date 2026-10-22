<?php
/**
 * Vendor Autoloader for SLN Consulting
 * Loads PHPMailer classes (Exception, PHPMailer, SMTP)
 */

$phpmailerSrc = __DIR__ . '/phpmailer/phpmailer/src';
if (file_exists($phpmailerSrc . '/PHPMailer.php')) {
    require_once $phpmailerSrc . '/Exception.php';
    require_once $phpmailerSrc . '/PHPMailer.php';
    require_once $phpmailerSrc . '/SMTP.php';
}
