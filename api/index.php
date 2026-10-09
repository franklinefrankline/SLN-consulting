<?php
// Vercel serverless entry point for SLN Consulting PHP application
$rootDir = dirname(__DIR__);
chdir($rootDir);

require_once $rootDir . '/security.php';
sln_send_security_headers();

$requestUri = $_SERVER['REQUEST_URI'] ?? '/';
$path = parse_url($requestUri, PHP_URL_PATH);
$path = ltrim($path, '/');

// Default home page
if ($path === '' || $path === 'index.php') {
    require $rootDir . '/index.php';
    exit;
}

// 1. Strict Path Traversal and Sensitive File Shield
$cleanPath = str_replace(["\0", "\\"], ['', '/'], $path);
$pathSegments = explode('/', $cleanPath);

foreach ($pathSegments as $segment) {
    // Block directory traversal attempts
    if ($segment === '..' || $segment === '.') {
        http_response_code(403);
        echo "<h1>403 Forbidden</h1>";
        exit;
    }
    // Block access to hidden files and directories (.env, .git, .vercel, etc.)
    if (strpos($segment, '.') === 0) {
        http_response_code(404);
        require $rootDir . '/404.html';
        exit;
    }
}

// Block direct access to internal server scripts, archives, and configuration files
$forbiddenPatterns = [
    '/\.env/i',
    '/\.git/i',
    '/\.zip$/i',
    '/\.mjs$/i',
    '/\.json$/i',
    '/\.log$/i',
    '/\.md$/i',
    '/^security\.php$/i',
    '/^mailer\.php$/i'
];
foreach ($forbiddenPatterns as $pattern) {
    if (preg_match($pattern, $cleanPath)) {
        http_response_code(404);
        require $rootDir . '/404.html';
        exit;
    }
}

$targetFile = $rootDir . '/' . $cleanPath;
$realTarget = realpath($targetFile);
$realRoot   = realpath($rootDir);

// Ensure target file is strictly inside the root directory
if ($realTarget && strpos($realTarget, $realRoot) !== 0) {
    http_response_code(403);
    echo "<h1>403 Forbidden</h1>";
    exit;
}

// If target PHP file exists
if ($realTarget && is_file($realTarget) && pathinfo($realTarget, PATHINFO_EXTENSION) === 'php') {
    require $realTarget;
    exit;
}

// If requested without extension (e.g. /about-us -> /about-us.php)
$phpCandidate = realpath($targetFile . '.php');
if ($phpCandidate && is_file($phpCandidate) && strpos($phpCandidate, $realRoot) === 0) {
    require $phpCandidate;
    exit;
}

// If requesting an existing static file or HTML (whitelist allowed extensions)
$allowedStaticExts = ['html', 'htm', 'css', 'js', 'png', 'jpg', 'jpeg', 'gif', 'svg', 'ico', 'webp', 'woff', 'woff2', 'ttf', 'otf', 'pdf', 'mp4'];
if ($realTarget && is_file($realTarget)) {
    $ext = strtolower(pathinfo($realTarget, PATHINFO_EXTENSION));
    if (in_array($ext, $allowedStaticExts, true)) {
        $mime = mime_content_type($realTarget);
        if ($mime) {
            header("Content-Type: $mime");
        }
        readfile($realTarget);
        exit;
    }
}

// 404 fallback
http_response_code(404);
if (file_exists($rootDir . '/404.html')) {
    require $rootDir . '/404.html';
} else {
    echo "<h1>404 Not Found</h1>";
}
