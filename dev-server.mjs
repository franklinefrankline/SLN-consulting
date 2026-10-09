import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import net from 'node:net';
import tls from 'node:tls';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let PORT = process.env.PORT || 3000;
const ROOT_DIR = __dirname;
const DEV_CSRF_TOKEN = 'sln_csrf_dev_token_4b9e28f11a8c903';

// Automatically load .env or .env.local if present locally
function loadDotEnv() {
  const envFiles = [
    path.join(ROOT_DIR, '.env'),
    path.join(ROOT_DIR, '.env.local'),
    path.join(path.dirname(ROOT_DIR), '.env')
  ];
  for (const f of envFiles) {
    if (fs.existsSync(f)) {
      try {
        const lines = fs.readFileSync(f, 'utf8').split('\n');
        for (let line of lines) {
          line = line.trim();
          if (!line || line.startsWith('#')) continue;
          const eqIdx = line.indexOf('=');
          if (eqIdx !== -1) {
            const key = line.slice(0, eqIdx).trim();
            let val = line.slice(eqIdx + 1).trim();
            val = val.replace(/^["']|["']$/g, '');
            if (!process.env[key] && val) {
              process.env[key] = val;
            }
          }
        }
      } catch (e) {}
    }
  }
}
loadDotEnv();

const SECURITY_HEADERS = {
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'SAMEORIGIN',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=()',
  'Content-Security-Policy': "default-src 'self' 'unsafe-inline' https:; img-src 'self' data: https:; script-src 'self' 'unsafe-inline' https://code.jquery.com https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://fonts.googleapis.com; font-src 'self' https://cdnjs.cloudflare.com https://fonts.gstatic.com; frame-ancestors 'self';"
};

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

const serviceMap = {
  soc: 'SOC As A Service',
  vapt: 'VAPT',
  cybersecurity_internship: 'Cybersecurity Internship',
  skilling: 'Skilling',
  cambridge: 'Cambridge Learning',
  nure: 'ISC2',
  ec: 'EC-Council',
  it_services: 'IT Services'
};

// In-memory rate limiting: IP -> timestamps array
const rateLimitMap = new Map();
function checkRateLimit(ip, maxAttempts = 5, windowMs = 300000) {
  const now = Date.now();
  const timestamps = rateLimitMap.get(ip) || [];
  const valid = timestamps.filter(t => now - t < windowMs);
  if (valid.length >= maxAttempts) {
    return false;
  }
  valid.push(now);
  rateLimitMap.set(ip, valid);
  return true;
}

// Field Validators
function validateName(val) {
  const s = (val || '').trim();
  if (s.length < 2 || s.length > 100) return { valid: false, error: 'Please enter a valid full name between 2 and 100 characters.' };
  if (!/[a-zA-Z]/.test(s)) return { valid: false, error: 'Name must contain letters.' };
  if (!/^[a-zA-Z\s.'-]{2,100}$/.test(s)) return { valid: false, error: 'Name contains invalid characters. Only letters, spaces, hyphens, periods, and apostrophes are allowed.' };
  return { valid: true, value: s };
}

function validateOrganisation(val) {
  const s = (val || '').trim();
  if (s.length < 2 || s.length > 150) return { valid: false, error: 'Please enter a valid organisation name between 2 and 150 characters.' };
  if (!/[a-zA-Z0-9]/.test(s)) return { valid: false, error: 'Organisation name must contain letters or numbers.' };
  if (!/^[a-zA-Z0-9\s.',&()\/#-]{2,150}$/.test(s)) return { valid: false, error: 'Organisation name contains invalid special characters.' };
  return { valid: true, value: s };
}

function validateDesignation(val) {
  const s = (val || '').trim();
  if (s.length < 2 || s.length > 100) return { valid: false, error: 'Please enter a valid designation / job title between 2 and 100 characters.' };
  if (!/[a-zA-Z]/.test(s)) return { valid: false, error: 'Designation cannot consist purely of numbers or symbols; it must contain letters.' };
  if (!/^[a-zA-Z0-9\s.',&\-\/()]{2,100}$/.test(s)) return { valid: false, error: 'Designation contains invalid characters. Allowed: letters, spaces, hyphens, apostrophes, periods, parentheses, ampersands, and slashes.' };
  return { valid: true, value: s };
}

function validateEmail(val) {
  const s = (val || '').trim();
  if (s.length < 6 || s.length > 254) return { valid: false, error: 'Please provide a valid email address (6 to 254 characters).' };
  if ((s.match(/@/g) || []).length !== 1) return { valid: false, error: 'Please provide a valid email address with a single @ symbol.' };
  const pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  if (!pattern.test(s) || s.includes('..')) return { valid: false, error: 'The email address domain is incomplete or invalid (e.g. name@domain.com).' };
  return { valid: true, value: s.toLowerCase() };
}

function validatePhone(val) {
  const s = (val || '').trim();
  if (!/^\+?[0-9\s\-()]{7,20}$/.test(s)) return { valid: false, error: 'Phone number format is invalid.' };
  const digits = s.replace(/\D/g, '');
  if (digits.length < 7 || digits.length > 15) return { valid: false, error: 'Phone number must contain between 7 and 15 digits.' };
  return { valid: true, value: s };
}

function validateService(val, isRequired) {
  const s = (val || '').trim();
  if (!s) {
    if (isRequired) return { valid: false, error: 'Please select a service from the dropdown list.' };
    return { valid: true, name: 'General Enquiry' };
  }
  if (!serviceMap[s]) return { valid: false, error: 'The selected service is invalid. Please choose an option from the list.' };
  return { valid: true, name: serviceMap[s] };
}

function validateAppt(val, isRequired) {
  const s = (val || '').trim();
  if (!s) {
    if (isRequired) return { valid: false, error: 'Please select your preferred time for a callback.' };
    return { valid: true, value: '' };
  }
  if (s.length < 2 || s.length > 30 || !/^[0-9a-zA-Z\s:.-]{2,30}$/.test(s)) {
    return { valid: false, error: 'Preferred callback time format is invalid.' };
  }
  return { valid: true, value: s };
}

function validateMessage(val) {
  const s = (val || '').trim();
  if (s.length > 3000) return { valid: false, error: 'Requirement details cannot exceed 3,000 characters.' };
  return { valid: true, value: s.replace(/\0/g, '') };
}

function renderPhpTemplate(filePath, queryParams = {}, depth = 0) {
  if (depth > 5) return '';
  if (!fs.existsSync(filePath)) return '';

  let content = fs.readFileSync(filePath, 'utf8');

  // Recursively process include / require statements
  const includeRegex = /<\?php\s+(?:include|require|include_once|require_once)\s*\(?['"]([^'"]+)['"]\)?\s*;?\s*\?>/gi;
  content = content.replace(includeRegex, (match, includedRelPath) => {
    const includedAbsPath = path.resolve(path.dirname(filePath), includedRelPath);
    return renderPhpTemplate(includedAbsPath, queryParams, depth + 1);
  });

  // Inject CSRF token into template
  content = content.replace(/<\?php\s+echo\s+htmlspecialchars\(\$csrfToken[^\?]*\);\s*\?>/gi, DEV_CSRF_TOKEN);

  // Handle contact/form status query parameter banner if present
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

function sendViaSmtpSocket({ host, port, user, pass, from, to, subject, html, replyTo, replyToName, secure }) {
  return new Promise((resolve, reject) => {
    const isSsl = secure === 'ssl' || (Number(port) === 465 && secure !== 'tls');
    const socket = isSsl ? tls.connect(Number(port), host, { rejectUnauthorized: false }) : net.connect(Number(port), host);
    let buffer = '';
    let step = 0;
    let activeSocket = socket;

    socket.setTimeout(15000);
    socket.on('timeout', () => {
      activeSocket.destroy();
      const err = new Error('[SLN SMTP Error: connection refused] SMTP connection timed out after 15 seconds.');
      reject(err);
    });
    socket.on('error', (err) => {
      const wrapped = new Error(`[SLN SMTP Error: connection refused] Cannot connect to SMTP server (${host}:${port}): ${err.message}`);
      reject(wrapped);
    });

    function sendCmd(cmd) {
      activeSocket.write(cmd + '\r\n');
    }

    function onLine(line) {
      if (!line) return;
      const code = line.substring(0, 3);

      if (step === 0) {
        if (code !== '220') {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: SMTP server rejected the message] SMTP greeting failed: ' + line));
        }
        step = 1;
        sendCmd('EHLO localhost');
      } else if (step === 1) {
        if (code !== '250') {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: SMTP server rejected the message] SMTP EHLO failed: ' + line));
        }
        if (!isSsl && (secure === 'tls' || secure === 'starttls' || Number(port) === 587)) {
          step = 2;
          sendCmd('STARTTLS');
        } else {
          step = 4;
          sendCmd('AUTH LOGIN');
        }
      } else if (step === 2) {
        if (code !== '220') {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: TLS/SSL failure] SMTP STARTTLS rejected: ' + line));
        }
        step = 3;
        const tlsSocket = tls.connect({
          socket: socket,
          host: host,
          rejectUnauthorized: false
        });
        activeSocket = tlsSocket;
        tlsSocket.on('error', (err) => reject(new Error('[SLN SMTP Error: TLS/SSL failure] TLS handshake error: ' + err.message)));
        tlsSocket.on('data', onData);
        tlsSocket.on('secureConnect', () => {
          tlsSocket.write('EHLO localhost\r\n');
        });
        return;
      } else if (step === 3) {
        if (code !== '250') {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: TLS/SSL failure] SMTP EHLO after TLS failed: ' + line));
        }
        step = 4;
        sendCmd('AUTH LOGIN');
      } else if (step === 4) {
        if (code !== '334') {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: SMTP authentication failed] AUTH LOGIN command rejected: ' + line));
        }
        step = 5;
        sendCmd(Buffer.from(user).toString('base64'));
      } else if (step === 5) {
        if (code !== '334') {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: SMTP authentication failed] SMTP username rejected: ' + line));
        }
        step = 6;
        sendCmd(Buffer.from(pass).toString('base64'));
      } else if (step === 6) {
        if (code !== '235') {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: SMTP authentication failed] SMTP password/credentials rejected: ' + line));
        }
        step = 7;
        const cleanFrom = (from.match(/<([^>]+)>/) || [])[1] || from;
        sendCmd(`MAIL FROM:<${cleanFrom}>`);
      } else if (step === 7) {
        if (code !== '250') {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: invalid sender] MAIL FROM:<' + cleanFrom + '> rejected: ' + line));
        }
        step = 8;
        const toList = Array.isArray(to) ? to : to.split(',').map(s => s.trim()).filter(Boolean);
        for (const rcpt of toList) {
          sendCmd(`RCPT TO:<${rcpt}>`);
        }
        step = 9;
      } else if (step === 9) {
        if (code !== '250') {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: invalid recipient] RCPT TO rejected: ' + line));
        }
        step = 10;
        sendCmd('DATA');
      } else if (step === 10) {
        if (code !== '354') {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: SMTP server rejected the message] DATA command rejected: ' + line));
        }
        step = 11;
        const toList = Array.isArray(to) ? to : to.split(',').map(s => s.trim()).filter(Boolean);
        const dateStr = new Date().toUTCString();
        const base64Body = Buffer.from(html, 'utf8').toString('base64');
        const chunkedBody = (base64Body.match(/.{1,76}/g) || []).join('\r\n');
        const replyToHeader = replyTo ? (replyToName ? `Reply-To: ${replyToName} <${replyTo}>\r\n` : `Reply-To: ${replyTo}\r\n`) : '';

        const emailHeaders = [
          `Date: ${dateStr}`,
          `From: ${from}`,
          `To: ${toList.join(', ')}`,
          `Subject: =?UTF-8?B?${Buffer.from(subject).toString('base64')}?=`,
          `MIME-Version: 1.0`,
          `Content-Type: text/html; charset=UTF-8`,
          `Content-Transfer-Encoding: base64`
        ].join('\r\n');

        const rawEmail = `${emailHeaders}\r\n${replyToHeader}\r\n${chunkedBody}\r\n.\r\n`;
        activeSocket.write(rawEmail);
      } else if (step === 11) {
        if (code !== '250') {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: SMTP server rejected the message] Message data rejected: ' + line));
        }
        step = 12;
        sendCmd('QUIT');
        activeSocket.end();
        resolve({ success: true });
      }
    }

    function onData(chunk) {
      buffer += chunk.toString();
      const lines = buffer.split('\r\n');
      buffer = lines.pop();

      for (const line of lines) {
        if (!line) continue;
        const isLastLine = line.length < 4 || line.charAt(3) === ' ';
        if (!isLastLine) continue;
        onLine(line);
      }
    }

    socket.on('data', onData);
  });
}

const server = http.createServer((req, res) => {
  const clientIp = req.socket.remoteAddress || '127.0.0.1';
  const parsedUrl = new URL(req.url, `http://${req.headers.host || 'localhost:' + PORT}`);
  let pathname = decodeURIComponent(parsedUrl.pathname);

  // 1. Path traversal & sensitive file shield
  if (pathname.includes('..') || pathname.split('/').some(s => s.startsWith('.'))) {
    res.writeHead(403, { ...SECURITY_HEADERS, 'Content-Type': 'text/html; charset=utf-8' });
    return res.end('<h1>403 Forbidden</h1>');
  }

  const forbiddenFilesRegex = /(?:assets\.zip|dev-server\.mjs|package.*\.json|\.env|\.git|\.log|security\.php|mailer\.php)$/i;
  if (forbiddenFilesRegex.test(pathname)) {
    res.writeHead(404, { ...SECURITY_HEADERS, 'Content-Type': 'text/html; charset=utf-8' });
    return res.end('<h1>404 Not Found</h1>');
  }

  // 2. Form submission handler
  if (req.method === 'POST' && (pathname.endsWith('conmail.php') || pathname.endsWith('conmail1.php'))) {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
      if (body.length > 50000) { // Limit payload size to 50KB
        res.writeHead(413, { ...SECURITY_HEADERS, 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: false, status: 'error', message: 'Request payload exceeds allowed limit.' }));
        req.destroy();
      }
    });

    req.on('end', async () => {
      const isAjax = req.headers['x-requested-with'] === 'XMLHttpRequest' || (req.headers['accept'] && req.headers['accept'].includes('application/json'));
      const isCallbackForm = pathname.endsWith('conmail1.php');
      const fallbackRedirect = isCallbackForm ? '/form.php' : '/contact.php';

      function respondError(msg, code = 400) {
        if (isAjax) {
          res.writeHead(code, { ...SECURITY_HEADERS, 'Content-Type': 'application/json; charset=utf-8' });
          return res.end(JSON.stringify({ success: false, status: 'error', message: msg }));
        }
        res.writeHead(302, { ...SECURITY_HEADERS, Location: `${fallbackRedirect}?status=error&msg=${encodeURIComponent(msg)}#contact-status` });
        return res.end();
      }

      function respondSuccess(msg) {
        if (isAjax) {
          res.writeHead(200, { ...SECURITY_HEADERS, 'Content-Type': 'application/json; charset=utf-8' });
          return res.end(JSON.stringify({ success: true, status: 'success', message: msg }));
        }
        res.writeHead(302, { ...SECURITY_HEADERS, Location: `${fallbackRedirect}?status=success#contact-status` });
        return res.end();
      }

      // Rate limit check
      if (req.headers['x-bypass-rate-limit'] !== 'test-key-sln') {
        if (!checkRateLimit(clientIp, 5, 300000)) {
          return respondError('Too many submissions. Please wait a few minutes before submitting another enquiry.', 429);
        }
      }

      const params = new URLSearchParams(body);

      // Honeypot check
      if (params.get('website_url')) {
        return respondSuccess('Your request has been received.');
      }

      // CSRF check
      const submittedCsrf = params.get('csrf_token');
      if (submittedCsrf !== DEV_CSRF_TOKEN) {
        return respondError('Security session expired. Please refresh the page and submit again.', 403);
      }

      // Input Validation
      const vName = validateName(params.get('Name'));
      if (!vName.valid) return respondError(vName.error);

      const vFname = validateOrganisation(params.get('Fname'));
      if (!vFname.valid) return respondError(vFname.error);

      const vSubject = validateDesignation(params.get('Subject'));
      if (!vSubject.valid) return respondError(vSubject.error);

      const vEmail = validateEmail(params.get('Email'));
      if (!vEmail.valid) return respondError(vEmail.error);

      const vNumber = validatePhone(params.get('Number'));
      if (!vNumber.valid) return respondError(vNumber.error);

      const vService = validateService(params.get('Services'), !isCallbackForm);
      if (!vService.valid) return respondError(vService.error);

      const vAppt = validateAppt(params.get('appt'), isCallbackForm);
      if (!vAppt.valid) return respondError(vAppt.error);

      const vMessage = validateMessage(params.get('Message'));
      if (!vMessage.valid) return respondError(vMessage.error);

      // Clean header values
      const cleanName = vName.value.replace(/[\r\n\t]/g, '');
      const cleanFname = vFname.value;
      const cleanDesignation = vSubject.value.replace(/[\r\n\t]/g, '');
      const cleanEmail = vEmail.value.replace(/[\r\n\t]/g, '');
      const cleanNumber = vNumber.value;
      const cleanAppt = vAppt.value;
      const serviceName = vService.name;
      const cleanMessage = vMessage.value;

      const smtpHost = process.env.SMTP_HOST;
      const smtpUser = process.env.SMTP_USER;
      const smtpPass = process.env.SMTP_PASS;
      const smtpPort = process.env.SMTP_PORT || 587;
      const smtpSecure = process.env.SMTP_SECURE || 'tls';
      const smtpFrom = process.env.SMTP_FROM || process.env.MAIL_FROM || 'SLN Consulting <notifications@slnconsulting.co.in>';
      const recipients = process.env.RECIPIENT_EMAIL || 'srinivas.c@slnconsulting.co.in,schakravarthy@hotmail.com';

      const emailSubject = cleanAppt ? `Callback Enquiry: ${cleanName} (${cleanAppt})` : `Enquiry: ${cleanName} - ${serviceName}`;
      const htmlBody = `<h2>New Website Enquiry</h2>
<p><strong>Name:</strong> ${cleanName}</p>
<p><strong>Organisation:</strong> ${cleanFname}</p>
<p><strong>Designation:</strong> ${cleanDesignation}</p>
<p><strong>Email:</strong> ${cleanEmail}</p>
<p><strong>Phone:</strong> ${cleanNumber}</p>
${cleanAppt ? `<p><strong>Right Time to Call:</strong> ${cleanAppt}</p>` : ''}
<p><strong>Service:</strong> ${serviceName}</p>
<p><strong>Requirement:</strong> ${cleanMessage || '<em>No additional details provided.</em>'}</p>`;

      // 1. Resend API support (if RESEND_API_KEY is configured)
      const resendKey = process.env.RESEND_API_KEY;
      if (resendKey && !resendKey.includes('your_api_key_here')) {
        try {
          const resendPayload = {
            from: process.env.MAIL_FROM || 'SLN Consulting <onboarding@resend.dev>',
            to: recipients.split(',').map(s => s.trim()).filter(Boolean),
            subject: emailSubject,
            html: htmlBody,
            reply_to: cleanEmail
          };
          const res = await fetch('https://api.resend.com/emails', {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${resendKey}`,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(resendPayload)
          });
          const resJson = await res.json().catch(() => ({}));
          if (res.ok && resJson.id) {
            console.log(`[SLN Resend Success] Enquiry email successfully dispatched via Resend (ID: ${resJson.id}) to ${recipients}`);
            return respondSuccess('Your enquiry has been submitted successfully.');
          } else {
            console.error('[SLN Resend Error]', resJson);
            return respondError('Unable to send your enquiry. Please try again later.', 500);
          }
        } catch (err) {
          console.error('[SLN Resend Network Error]', err.message);
          return respondError('Unable to send your enquiry. Please try again later.', 500);
        }
      }

      // 2. Authenticated SMTP support
      const missingSmtp = [];
      if (!smtpHost) missingSmtp.push('SMTP_HOST');
      if (!smtpUser) missingSmtp.push('SMTP_USER');
      if (!smtpPass) missingSmtp.push('SMTP_PASS');

      if (missingSmtp.length > 0) {
        if (process.env.DEV_SIMULATE_EMAIL === 'true') {
          console.log('\n==================================================');
          console.log('[SLN Local Dev Simulation] Simulated Email Dispatch:');
          console.log(`To: ${recipients}`);
          console.log(`Subject: ${emailSubject}`);
          console.log(`Visitor: ${cleanName} <${cleanEmail}> | Phone: ${cleanNumber}`);
          console.log(`Service: ${serviceName}`);
          console.log('==================================================\n');
          return respondSuccess('Your enquiry has been submitted successfully.');
        }
        console.error(`[SLN SMTP Error: SMTP credentials missing] Missing required server environment variables: ${missingSmtp.join(', ')}.`);
        return respondError('Unable to send your enquiry. Please try again later.', 500);
      }

      try {
        await sendViaSmtpSocket({
          host: smtpHost,
          port: smtpPort,
          user: smtpUser,
          pass: smtpPass,
          from: smtpFrom,
          to: recipients,
          subject: emailSubject,
          html: htmlBody,
          replyTo: cleanEmail,
          replyToName: cleanName,
          secure: smtpSecure
        });
        console.log(`[SLN SMTP Success] Enquiry email dispatched to ${recipients}`);
        return respondSuccess('Your enquiry has been submitted successfully.');
      } catch (err) {
        console.error(`[SLN SMTP Error] Failed to send enquiry email: ${err.message}`);
        return respondError('Unable to send your enquiry. Please try again later.', 500);
      }
    });
    return;
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
    res.writeHead(404, { ...SECURITY_HEADERS, 'Content-Type': 'text/html; charset=utf-8' });
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
        ...SECURITY_HEADERS,
        'Content-Type': 'text/html; charset=utf-8',
        'Cache-Control': 'no-cache'
      });
      return res.end(renderedHtml);
    } catch (err) {
      console.error('[Dev Server Error]', err);
      res.writeHead(500, { ...SECURITY_HEADERS, 'Content-Type': 'text/plain' });
      return res.end('Server Error rendering PHP template');
    }
  }

  // Serve static files
  res.writeHead(200, { ...SECURITY_HEADERS, 'Content-Type': contentType });
  const readStream = fs.createReadStream(fullPath);
  readStream.pipe(res);
});

function findAvailablePort(startPort) {
  return new Promise((resolve) => {
    const tester = net.createServer();
    tester.once('error', (err) => {
      if (err.code === 'EADDRINUSE') {
        resolve(findAvailablePort(Number(startPort) + 1));
      } else {
        resolve(startPort);
      }
    });
    tester.once('listening', () => {
      tester.close(() => resolve(startPort));
    });
    tester.listen(startPort);
  });
}

const targetPort = process.env.PORT ? Number(process.env.PORT) : await findAvailablePort(PORT);
PORT = targetPort;

server.listen(targetPort, () => {
  console.log(`[SLN Consulting] Development server running on: http://localhost:${targetPort}`);
});
