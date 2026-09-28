<?php
// Vercel serverless entry point for SLN Consulting PHP application
$rootDir = dirname(__DIR__);
chdir($rootDir);

$requestUri = $_SERVER['REQUEST_URI'] ?? '/';
$path = parse_url($requestUri, PHP_URL_PATH);
$path = ltrim($path, '/');

// Default home page
if ($path === '' || $path === 'index.php') {
    require $rootDir . '/index.php';
    exit;
}

$targetFile = $rootDir . '/' . $path;

// If target PHP file exists
if (file_exists($targetFile) && !is_dir($targetFile) && pathinfo($targetFile, PATHINFO_EXTENSION) === 'php') {
    require $targetFile;
    exit;
}

// If requested without extension (e.g. /about-us -> /about-us.php)
if (file_exists($targetFile . '.php')) {
    require $targetFile . '.php';
    exit;
}

// If requesting an existing static file or HTML
if (file_exists($targetFile) && !is_dir($targetFile)) {
    $mime = mime_content_type($targetFile);
    if ($mime) {
        header("Content-Type: $mime");
    }
    readfile($targetFile);
    exit;
}

// 404 fallback
http_response_code(404);
if (file_exists($rootDir . '/404.html')) {
    require $rootDir . '/404.html';
} else {
    echo "<h1>404 Not Found</h1>";
}
