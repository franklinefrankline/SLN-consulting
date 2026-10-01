import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PORT = process.env.PORT || 3000;
const ROOT_DIR = __dirname;

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.htm': 'text/html; charset=utf-8',
  '.php': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.mjs': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.webp': 'image/webp',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.otf': 'font/otf',
  '.eot': 'application/vnd.ms-fontobject',
  '.pdf': 'application/pdf',
  '.mp4': 'video/mp4',
  '.zip': 'application/zip'
};

function renderPhpTemplate(filePath, queryParams = {}, depth = 0) {
  if (depth > 5) return '';
  if (!fs.existsSync(filePath)) return '';

  let content = fs.readFileSync(filePath, 'utf8');

  // Recursively process include / require statements
  // e.g. <?php include 'header.php'; ?> or <?php include "footer.php" ?>
  const includeRegex = /<\?php\s+(?:include|require|include_once|require_once)\s*\(?['"]([^'"]+)['"]\)?\s*;?\s*\?>/gi;
  content = content.replace(includeRegex, (match, includedRelPath) => {
    const includedAbsPath = path.resolve(path.dirname(filePath), includedRelPath);
    return renderPhpTemplate(includedAbsPath, queryParams, depth + 1);
  });

  // Handle contact/form status query parameter banner if present
  // Match the complete <div id="contact-status-container">...</div> block including any nested PHP ifs
  const statusContainerRegex = /<div id="contact-status-container">[\s\S]*?<\/div>\s*(?:<\?php\s*endif;\s*\?>\s*)?<\/div>/i;
  if (statusContainerRegex.test(content)) {
    if (queryParams.status) {
      const isSuccess = queryParams.status === 'success';
      const msg = queryParams.msg || (isSuccess ? 'Thank you! Your message has been sent successfully.' : 'Unable to send request at this time.');
      const bannerHtml = `<div id="contact-status-container">
        <div id="contact-status" class="alert ${isSuccess ? 'alert-success' : 'alert-danger'}" style="${isSuccess ? 'background-color: #ecfdf5; border: 1px solid #a7f3d0; color: #065f46;' : 'background-color: #fef2f2; border: 1px solid #fecaca; color: #991b1b;'} border-radius: 8px; padding: 14px 18px; font-size: 15px; margin-bottom: 20px;">
          <i class="fas ${isSuccess ? 'fa-check-circle' : 'fa-exclamation-circle'}" style="color: ${isSuccess ? '#059669' : '#dc2626'}; margin-right: 8px;"></i>
          ${isSuccess ? '<strong>Thank you!</strong> ' + msg : '<strong>Notice:</strong> ' + msg}
        </div>
      </div>`;
      content = content.replace(statusContainerRegex, bannerHtml);
    } else {
      content = content.replace(statusContainerRegex, '<div id="contact-status-container"></div>');
    }
  }

  // Strip any remaining PHP tags cleanly
  content = content.replace(/<\?php[\s\S]*?\?>/gi, '');

  return content;
}

const server = http.createServer((req, res) => {
  const parsedUrl = new URL(req.url, `http://${req.headers.host || 'localhost:' + PORT}`);
  let pathname = decodeURIComponent(parsedUrl.pathname);

  // Form submission handler simulation
  if (req.method === 'POST' && (pathname.endsWith('conmail.php') || pathname.endsWith('conmail1.php'))) {
    res.writeHead(302, { Location: '/contact.php?status=success' });
    return res.end();
  }

  // Normalize path
  if (pathname === '/' || pathname === '') {
    pathname = '/index.php';
  }

  let fullPath = path.join(ROOT_DIR, pathname);

  // If path doesn't exist, try appending .php or .html
  if (!fs.existsSync(fullPath)) {
    if (fs.existsSync(fullPath + '.php')) {
      fullPath = fullPath + '.php';
    } else if (fs.existsSync(fullPath + '.html')) {
      fullPath = fullPath + '.html';
    }
  }

  // If it's a directory, look for index.php or index.html
  if (fs.existsSync(fullPath) && fs.statSync(fullPath).isDirectory()) {
    const dirIndexPhp = path.join(fullPath, 'index.php');
    const dirIndexHtml = path.join(fullPath, 'index.html');
    if (fs.existsSync(dirIndexPhp)) {
      fullPath = dirIndexPhp;
    } else if (fs.existsSync(dirIndexHtml)) {
      fullPath = dirIndexHtml;
    }
  }

  // Check if file exists
  if (!fs.existsSync(fullPath) || fs.statSync(fullPath).isDirectory()) {
    const notFoundPage = path.join(ROOT_DIR, '404.html');
    res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
    if (fs.existsSync(notFoundPage)) {
      return res.end(fs.readFileSync(notFoundPage));
    }
    return res.end('<h1>404 Not Found</h1>');
  }

  const ext = path.extname(fullPath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';

  // Process PHP files as rendered HTML
  if (ext === '.php') {
    try {
      const queryParams = Object.fromEntries(parsedUrl.searchParams.entries());
      const renderedHtml = renderPhpTemplate(fullPath, queryParams);
      res.writeHead(200, {
        'Content-Type': 'text/html; charset=utf-8',
        'Cache-Control': 'no-cache'
      });
      return res.end(renderedHtml);
    } catch (err) {
      console.error('[Dev Server Error]', err);
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      return res.end('Server Error rendering PHP template');
    }
  }

  // Serve static files
  res.writeHead(200, { 'Content-Type': contentType });
  const readStream = fs.createReadStream(fullPath);
  readStream.pipe(res);
});

server.listen(PORT, () => {
  console.log(`[SLN Consulting] Development server running on: http://localhost:${PORT}`);
});
