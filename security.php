<?php
/**
 * SLN Consulting - Security Helper & Input Validation Suite
 *
 * Implements:
 * 1. Security Headers (nosniff, frame protection, referrer policy, CSP)
 * 2. Secure Session Initialization
 * 3. Anti-CSRF Token Generation and Verification
 * 4. Bot Honeypot Trap Detection
 * 5. IP-based Submission Rate Limiting
 * 6. Strict Input Validation (Email, Designation, Name, Organisation, Phone, Service, Message)
 * 7. Email Header Injection Prevention
 */

// 1. Send Security Headers
function sln_send_security_headers() {
    if (headers_sent()) return;

    header("X-Content-Type-Options: nosniff");
    header("X-Frame-Options: SAMEORIGIN");
    header("Referrer-Policy: strict-origin-when-cross-origin");
    header("Permissions-Policy: camera=(), microphone=(), geolocation=()");
    header("Content-Security-Policy: default-src 'self' 'unsafe-inline' https:; img-src 'self' data: https:; script-src 'self' 'unsafe-inline' https://code.jquery.com https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://fonts.googleapis.com; font-src 'self' https://cdnjs.cloudflare.com https://fonts.gstatic.com; frame-ancestors 'self';");
}

// 2. Initialize Secure Session
function sln_start_session() {
    if (session_status() === PHP_SESSION_NONE) {
        $isHttps = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off')
            || (!empty($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https');

        @ini_set('session.cookie_httponly', '1');
        @ini_set('session.use_only_cookies', '1');
        @ini_set('session.cookie_samesite', 'Lax');
        if ($isHttps) {
            @ini_set('session.cookie_secure', '1');
        }

        @session_start();
    }
}

// 3. CSRF Protection
function sln_get_csrf_token() {
    sln_start_session();
    if (empty($_SESSION['sln_csrf_token']) || !is_string($_SESSION['sln_csrf_token'])) {
        // Reuse cookie token if valid 64-char hex string
        if (!empty($_COOKIE['sln_csrf_token']) && is_string($_COOKIE['sln_csrf_token']) && preg_match('/^[a-f0-9]{64}$/i', $_COOKIE['sln_csrf_token'])) {
            $_SESSION['sln_csrf_token'] = $_COOKIE['sln_csrf_token'];
        } else {
            try {
                $_SESSION['sln_csrf_token'] = bin2hex(random_bytes(32));
            } catch (\Exception $e) {
                $_SESSION['sln_csrf_token'] = bin2hex(openssl_random_pseudo_bytes(32));
            }
        }
    }
    
    // Set double-submit cookie for stateless/serverless Lambda environments (Vercel)
    if (!headers_sent() && empty($_COOKIE['sln_csrf_token'])) {
        $isHttps = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off')
            || (!empty($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https');
        @setcookie('sln_csrf_token', $_SESSION['sln_csrf_token'], [
            'expires'  => time() + 7200,
            'path'     => '/',
            'httponly' => true,
            'samesite' => 'Lax',
            'secure'   => $isHttps,
        ]);
    }
    return $_SESSION['sln_csrf_token'];
}

function sln_verify_csrf_token($token) {
    if (empty($token) || !is_string($token)) {
        return false;
    }
    sln_start_session();
    
    // 1. Primary check: session-stored token
    if (!empty($_SESSION['sln_csrf_token']) && hash_equals($_SESSION['sln_csrf_token'], $token)) {
        return true;
    }
    // 2. Serverless fallback: double-submit cookie check (protects stateless multi-instance environments like Vercel Lambda)
    if (!empty($_COOKIE['sln_csrf_token']) && hash_equals($_COOKIE['sln_csrf_token'], $token)) {
        return true;
    }
    return false;
}

// 4. Client IP Resolver (Safe for reverse proxies like Vercel / Cloudflare)
function sln_get_client_ip() {
    if (!empty($_SERVER['HTTP_CF_CONNECTING_IP']) && filter_var($_SERVER['HTTP_CF_CONNECTING_IP'], FILTER_VALIDATE_IP)) {
        return $_SERVER['HTTP_CF_CONNECTING_IP'];
    }
    if (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        $ips = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);
        $candidate = trim($ips[0]);
        if (filter_var($candidate, FILTER_VALIDATE_IP)) {
            return $candidate;
        }
    }
    if (!empty($_SERVER['HTTP_X_REAL_IP']) && filter_var($_SERVER['HTTP_X_REAL_IP'], FILTER_VALIDATE_IP)) {
        return $_SERVER['HTTP_X_REAL_IP'];
    }
    return $_SERVER['REMOTE_ADDR'] ?? '127.0.0.1';
}

// 5. Honeypot Bot Trap Check
function sln_is_honeypot_triggered() {
    if (!empty($_POST['website_url'])) {
        return true;
    }
    return false;
}

// 6. Rate Limiting (File-based token bucket per IP)
function sln_check_rate_limit($maxAttempts = 5, $windowSeconds = 300) {
    $ip = sln_get_client_ip();
    // Clean IP for file naming
    $ipHash = md5($ip);
    $tmpDir = sys_get_temp_dir();
    $rateFile = $tmpDir . DIRECTORY_SEPARATOR . 'sln_rate_' . $ipHash . '.json';

    $now = time();
    $attempts = [];

    if (file_exists($rateFile)) {
        $data = @json_decode(@file_get_contents($rateFile), true);
        if (is_array($data)) {
            // Keep only attempts within the sliding window
            foreach ($data as $timestamp) {
                if ($now - $timestamp < $windowSeconds) {
                    $attempts[] = $timestamp;
                }
            }
        }
    }

    if (count($attempts) >= $maxAttempts) {
        return false; // Rate limit exceeded
    }

    $attempts[] = $now;
    @file_put_contents($rateFile, json_encode($attempts), LOCK_EX);
    return true;
}

// 6. Header Injection Cleaner
function sln_clean_header_value($str) {
    if (!is_string($str)) return '';
    return preg_replace('/[\r\n\t\x00-\x1f]/', '', trim($str));
}

// 7. Whitelisted Services
function sln_get_allowed_services() {
    return [
        'soc'                      => 'SOC As A Service',
        'vapt'                     => 'VAPT',
        'cybersecurity_internship' => 'Cybersecurity Internship',
        'skilling'                 => 'Skilling',
        'cambridge'                => 'Cambridge Learning',
        'nure'                     => 'ISC2',
        'ec'                       => 'EC-Council',
        'it_services'              => 'IT Services'
    ];
}

function sln_get_service_name($key) {
    $services = sln_get_allowed_services();
    return $services[$key] ?? null;
}

// 8. Field Validators

/**
 * Validate Name:
 * - 2 to 100 characters
 * - Must contain letters
 * - Allows letters, spaces, hyphens, apostrophes, periods
 */
function sln_validate_name($name) {
    $name = trim($name ?? '');
    if (strlen($name) < 2 || strlen($name) > 100) {
        return ['valid' => false, 'error' => 'Please enter a valid full name between 2 and 100 characters.'];
    }
    if (!preg_match('/[a-zA-Z]/', $name)) {
        return ['valid' => false, 'error' => 'Name must contain letters.'];
    }
    if (!preg_match('/^[a-zA-Z\s.\'-]{2,100}$/', $name)) {
        return ['valid' => false, 'error' => 'Name contains invalid characters. Only letters, spaces, hyphens, periods, and apostrophes are allowed.'];
    }
    return ['valid' => true, 'value' => $name];
}

/**
 * Validate Organisation:
 * - 2 to 150 characters
 * - Must contain alphanumeric characters
 * - Allows letters, numbers, spaces, and standard corporate punctuation
 */
function sln_validate_organisation($org) {
    $org = trim($org ?? '');
    if (strlen($org) < 2 || strlen($org) > 150) {
        return ['valid' => false, 'error' => 'Please enter a valid organisation name between 2 and 150 characters.'];
    }
    if (!preg_match('/[a-zA-Z0-9]/', $org)) {
        return ['valid' => false, 'error' => 'Organisation name must contain letters or numbers.'];
    }
    if (!preg_match('/^[a-zA-Z0-9\s.\',&()\/#-]{2,150}$/', $org)) {
        return ['valid' => false, 'error' => 'Organisation name contains invalid special characters.'];
    }
    return ['valid' => true, 'value' => $org];
}

/**
 * Validate Designation:
 * - 2 to 100 characters
 * - Must contain letters
 * - Accepts legitimate professional titles (e.g. Software Engineer, Director & CEO, B.Sc. Computer Science)
 * - Rejects purely numeric entries or arbitrary strings of numbers
 */
function sln_validate_designation($designation) {
    $designation = trim($designation ?? '');
    if (strlen($designation) < 2 || strlen($designation) > 100) {
        return ['valid' => false, 'error' => 'Please enter a valid designation / job title between 2 and 100 characters.'];
    }
    if (!preg_match('/[a-zA-Z]/', $designation)) {
        return ['valid' => false, 'error' => 'Designation cannot consist purely of numbers or symbols; it must contain letters.'];
    }
    if (!preg_match('/^[a-zA-Z0-9\s.\',&\-\/()]{2,100}$/', $designation)) {
        return ['valid' => false, 'error' => 'Designation contains invalid characters. Allowed: letters, spaces, hyphens, apostrophes, periods, parentheses, ampersands, and slashes.'];
    }
    return ['valid' => true, 'value' => $designation];
}

/**
 * Validate Email:
 * - Length: 6 to 254 characters (RFC 5321)
 * - PHP filter_var(FILTER_VALIDATE_EMAIL)
 * - Enforces valid domain structure with dot and TLD of >= 2 chars
 * - Rejects double dots, multiple @, or missing domain
 */
function sln_validate_email($email) {
    $email = trim($email ?? '');
    $len = strlen($email);
    if ($len < 6 || $len > 254) {
        return ['valid' => false, 'error' => 'Please provide a valid email address (6 to 254 characters).'];
    }
    if (substr_count($email, '@') !== 1) {
        return ['valid' => false, 'error' => 'Please provide a valid email address with a single @ symbol.'];
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return ['valid' => false, 'error' => 'The email address format is invalid.'];
    }
    // Strict domain check: must have a dot and valid TLD
    if (!preg_match('/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/', $email)) {
        return ['valid' => false, 'error' => 'The email address domain is incomplete or invalid (e.g., name@domain.com).'];
    }
    if (strpos($email, '..') !== false) {
        return ['valid' => false, 'error' => 'The email address contains consecutive dots.'];
    }
    return ['valid' => true, 'value' => strtolower($email)];
}

/**
 * Validate Phone:
 * - Length: 7 to 20 characters
 * - Digit count: 7 to 15 digits (E.164 compliant)
 * - Supports domestic and international numbers with +, spaces, hyphens, and brackets
 */
function sln_validate_phone($phone) {
    $phone = trim($phone ?? '');
    if (strlen($phone) < 7 || strlen($phone) > 20) {
        return ['valid' => false, 'error' => 'Please provide a valid phone number (7 to 20 characters).'];
    }
    if (!preg_match('/^\+?[0-9\s\-()]{7,20}$/', $phone)) {
        return ['valid' => false, 'error' => 'Phone number contains invalid characters. Only digits, +, spaces, hyphens, and parentheses are allowed.'];
    }
    $digits = preg_replace('/\D/', '', $phone);
    $digitCount = strlen($digits);
    if ($digitCount < 7 || $digitCount > 15) {
        return ['valid' => false, 'error' => 'Phone number must contain between 7 and 15 digits.'];
    }
    return ['valid' => true, 'value' => $phone];
}

/**
 * Validate Selected Service:
 * - Must match allowed server whitelist
 */
function sln_validate_service($service, $required = true) {
    $service = trim($service ?? '');
    $allowed = sln_get_allowed_services();

    if (empty($service)) {
        if ($required) {
            return ['valid' => false, 'error' => 'Please select a service from the dropdown list.'];
        }
        return ['valid' => true, 'key' => '', 'name' => 'General Enquiry'];
    }

    if (!array_key_exists($service, $allowed)) {
        return ['valid' => false, 'error' => 'The selected service is invalid. Please choose an option from the list.'];
    }

    return ['valid' => true, 'key' => $service, 'name' => $allowed[$service]];
}

/**
 * Validate Preferred Time (appt):
 * - Optional or required based on parameter
 * - 2 to 30 characters
 */
function sln_validate_appt($appt, $required = false) {
    $appt = trim($appt ?? '');
    if (empty($appt)) {
        if ($required) {
            return ['valid' => false, 'error' => 'Please select your preferred time for a callback.'];
        }
        return ['valid' => true, 'value' => ''];
    }
    if (strlen($appt) < 2 || strlen($appt) > 30) {
        return ['valid' => false, 'error' => 'Preferred callback time format is invalid.'];
    }
    if (!preg_match('/^[0-9a-zA-Z\s:.-]{2,30}$/', $appt)) {
        return ['valid' => false, 'error' => 'Preferred time contains invalid characters.'];
    }
    return ['valid' => true, 'value' => $appt];
}

/**
 * Validate Requirement / Message:
 * - Optional
 * - Max length: 3000 characters
 */
function sln_validate_message($message) {
    $message = trim($message ?? '');
    if (strlen($message) > 3000) {
        return ['valid' => false, 'error' => 'Requirement details cannot exceed 3,000 characters.'];
    }
    // Remove null bytes
    $message = str_replace("\0", '', $message);
    return ['valid' => true, 'value' => $message];
}
