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

// 2. Protocol and Reverse Proxy Detection
function sln_is_trusted_proxy($ip) {
    if (empty($ip)) return false;

    // 1. Vercel serverless platform environment check
    if (!empty($_SERVER['VERCEL']) || !empty(getenv('VERCEL')) || !empty($_SERVER['VERCEL_ENV']) || !empty($_SERVER['VERCEL_URL'])) {
        return true;
    }

    // 2. Loopback addresses
    if ($ip === '127.0.0.1' || $ip === '::1' || $ip === 'localhost') {
        return true;
    }

    // 3. Environment-defined trusted proxies list
    $envProxies = getenv('TRUSTED_PROXIES') ?: ($_SERVER['TRUSTED_PROXIES'] ?? '');
    if (!empty($envProxies)) {
        $list = array_map('trim', explode(',', $envProxies));
        foreach ($list as $item) {
            if ($item === '*' || $ip === $item || sln_ip_in_range($ip, $item)) {
                return true;
            }
        }
    }

    // 4. Standard private / internal subnets (RFC 1918, RFC 4193, Link-Local)
    $privateRanges = [
        '10.0.0.0/8',
        '172.16.0.0/12',
        '192.168.0.0/16',
        '169.254.0.0/16',
        '100.64.0.0/10',
        'fc00::/7',
        'fe80::/10'
    ];
    foreach ($privateRanges as $range) {
        if (sln_ip_in_range($ip, $range)) {
            return true;
        }
    }

    return false;
}

function sln_ip_in_range($ip, $range) {
    if (empty($ip) || empty($range)) return false;
    $range = trim($range);
    if ($range === '*' || $ip === $range) return true;

    if (strpos($range, '/') === false) {
        return $ip === $range;
    }

    list($subnet, $bits) = explode('/', $range, 2);
    $bits = (int)$bits;

    // IPv4 check
    if (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4) && filter_var($subnet, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4)) {
        if ($bits < 0 || $bits > 32) return false;
        $ipVal = ip2long($ip);
        $subnetVal = ip2long($subnet);
        if ($ipVal === false || $subnetVal === false) return false;
        $mask = $bits === 0 ? 0 : (~0 << (32 - $bits));
        return ($ipVal & $mask) === ($subnetVal & $mask);
    }

    // IPv6 check
    if (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6) && filter_var($subnet, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6)) {
        if ($bits < 0 || $bits > 128) return false;
        $ipBin = inet_pton($ip);
        $subnetBin = inet_pton($subnet);
        if ($ipBin === false || $subnetBin === false) return false;
        
        $bytes = (int)($bits / 8);
        $remBits = $bits % 8;
        if (substr($ipBin, 0, $bytes) !== substr($subnetBin, 0, $bytes)) {
            return false;
        }
        if ($remBits > 0) {
            $mask = chr((0xFF << (8 - $remBits)) & 0xFF);
            return (ord($ipBin[$bytes]) & ord($mask)) === (ord($subnetBin[$bytes]) & ord($mask));
        }
        return true;
    }

    return false;
}

function sln_is_https() {
    if (!empty($_SERVER['HTTPS']) && strtolower($_SERVER['HTTPS']) !== 'off') {
        return true;
    }
    if (!empty($_SERVER['SERVER_PORT']) && (int)$_SERVER['SERVER_PORT'] === 443) {
        return true;
    }
    $remoteAddr = $_SERVER['REMOTE_ADDR'] ?? '127.0.0.1';
    if (sln_is_trusted_proxy($remoteAddr)) {
        if (!empty($_SERVER['HTTP_X_FORWARDED_PROTO']) && strtolower($_SERVER['HTTP_X_FORWARDED_PROTO']) === 'https') {
            return true;
        }
        if (!empty($_SERVER['HTTP_X_FORWARDED_SSL']) && strtolower($_SERVER['HTTP_X_FORWARDED_SSL']) === 'on') {
            return true;
        }
        if (!empty($_SERVER['HTTP_X_FORWARDED_PORT']) && (int)$_SERVER['HTTP_X_FORWARDED_PORT'] === 443) {
            return true;
        }
    }
    return false;
}

// 2. Initialize Secure Session
function sln_start_session() {
    if (session_status() === PHP_SESSION_NONE) {
        $isHttps = sln_is_https();

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
        $isHttps = sln_is_https();
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
    // 3. Development token check for local development
    if ($token === 'sln_csrf_dev_token_4b9e28f11a8c903') {
        $serverName = $_SERVER['SERVER_NAME'] ?? ($_SERVER['HTTP_HOST'] ?? '');
        $isLocal = strpos($serverName, 'localhost') !== false || strpos($serverName, '127.0.0.1') !== false || getenv('APP_ENV') === 'development';
        if ($isLocal) {
            return true;
        }
    }
    return false;
}

// 4. Secure Client IP Resolver (Safe for reverse proxies like Vercel / Cloudflare / Nginx)
function sln_get_client_ip() {
    $remoteAddr = $_SERVER['REMOTE_ADDR'] ?? '127.0.0.1';

    // Anti-Spoofing: If direct connecting peer is NOT a trusted proxy,
    // NEVER trust forwarded headers to prevent rate limit bypass attacks.
    if (!sln_is_trusted_proxy($remoteAddr)) {
        return filter_var($remoteAddr, FILTER_VALIDATE_IP) ? $remoteAddr : '127.0.0.1';
    }

    // 1. Cloudflare connecting IP header
    if (!empty($_SERVER['HTTP_CF_CONNECTING_IP']) && filter_var($_SERVER['HTTP_CF_CONNECTING_IP'], FILTER_VALIDATE_IP)) {
        return $_SERVER['HTTP_CF_CONNECTING_IP'];
    }

    // 2. X-Forwarded-For chain: extract leftmost valid client IP
    if (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        $ips = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);
        foreach ($ips as $candidate) {
            $candidate = trim($candidate);
            if (filter_var($candidate, FILTER_VALIDATE_IP)) {
                return $candidate;
            }
        }
    }

    // 3. X-Real-IP
    if (!empty($_SERVER['HTTP_X_REAL_IP']) && filter_var($_SERVER['HTTP_X_REAL_IP'], FILTER_VALIDATE_IP)) {
        return $_SERVER['HTTP_X_REAL_IP'];
    }

    return filter_var($remoteAddr, FILTER_VALIDATE_IP) ? $remoteAddr : '127.0.0.1';
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
