import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import net from 'node:net';
import tls from 'node:tls';
import https from 'node:https';
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
            process.env[key] = val;
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

function loadFormsConfig() {
  loadDotEnv();
  const defaultForm1 = 'https://docs.google.com/forms/d/e/1FAIpQLSdpVszsphdo1KhHgig4lCHfjuHmE8IzSvIUDHEFiE52LoW0Rw/viewform';
  const defaultForm2 = 'https://docs.google.com/forms/d/e/1FAIpQLSfp_u4mUMGlDdk9omnkDtI-Us3aDAlM4KzEGit3B-duDh4B1A/viewform';

  let form1Url = process.env.GOOGLE_FORM_1_URL || defaultForm1;
  let form2Url = process.env.GOOGLE_FORM_2_URL || defaultForm2;
  let form1Submit = true;
  let form2Submit = true;

  const phpConfigPath = path.join(ROOT_DIR, 'forms-config.php');
  if (fs.existsSync(phpConfigPath)) {
    try {
      const phpContent = fs.readFileSync(phpConfigPath, 'utf8');

      // 1. Check $form1Url = '...'
      const f1VarMatch = phpContent.match(/\$form1Url\s*=\s*(?:getenv\([^)]*\)\s*\?:\s*)?['"]([^'"]+)['"]/);
      if (f1VarMatch && f1VarMatch[1]) {
        form1Url = f1VarMatch[1];
      }
      // 2. Check 'form1' => [ ... 'url' => '...' ]
      const f1UrlMatch = phpContent.match(/['"]form1['"][\s\S]*?['"]url['"]\s*=>\s*(?:getenv\([^)]*\)\s*\?:\s*)?['"]([^'"]+)['"]/);
      if (f1UrlMatch && f1UrlMatch[1] && !f1UrlMatch[1].startsWith('$')) {
        form1Url = f1UrlMatch[1];
      }

      // 3. Check $form2Url = '...'
      const f2VarMatch = phpContent.match(/\$form2Url\s*=\s*(?:getenv\([^)]*\)\s*\?:\s*)?['"]([^'"]+)['"]/);
      if (f2VarMatch && f2VarMatch[1]) {
        form2Url = f2VarMatch[1];
      }
      // 4. Check 'form2' => [ ... 'url' => '...' ]
      const f2UrlMatch = phpContent.match(/['"]form2['"][\s\S]*?['"]url['"]\s*=>\s*(?:getenv\([^)]*\)\s*\?:\s*)?['"]([^'"]+)['"]/);
      if (f2UrlMatch && f2UrlMatch[1] && !f2UrlMatch[1].startsWith('$')) {
        form2Url = f2UrlMatch[1];
      }
    } catch (e) {}
  }

  function deriveResponseUrl(u) {
    if (!u) return '';
    if (u.includes('/formResponse')) return u.split('?')[0];
    return u.replace(/(\/(viewform|edit|formResponse|prefill)[^\?]*)(\?.*)?$/, '/formResponse');
  }

  return {
    form1: {
      key: 'form1',
      name: 'Website Enquiry Form',
      url: form1Url,
      responseUrl: deriveResponseUrl(form1Url),
      submitDirect: form1Submit,
      entries: {
        name: 'entry.2005620554',
        organisation: 'entry.969435007',
        designation: 'entry.1065046570',
        email: 'entry.1166974658',
        phone: 'entry.839337160',
        service: 'entry.1230817807',
        message: 'entry.1984267215'
      },
      serviceOptions: serviceMap
    },
    form2: {
      key: 'form2',
      name: 'General Contact Form',
      url: form2Url,
      responseUrl: deriveResponseUrl(form2Url),
      submitDirect: form2Submit,
      entries: {
        name: 'entry.2005620554',
        organisation: 'entry.1045781291',
        designation: 'entry.1065046570',
        email: 'entry.1166974658',
        phone: 'entry.839337160',
        right_time_to_call_hour: 'entry.1007004095_hour',
        right_time_to_call_minute: 'entry.1007004095_minute',
        service: 'entry.660909226',
        message: 'entry.1789743'
      },
      serviceOptions: serviceMap
    }
  };
}

function fetchGoogleFormMetadata(viewformUrl) {
  return new Promise((resolve) => {
    if (!viewformUrl) return resolve({ fbzx: null, cookies: '' });
    try {
      const url = new URL(viewformUrl);
      const req = https.request({
        hostname: url.hostname,
        path: url.pathname + url.search,
        method: 'GET',
        headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        },
        timeout: 4000
      }, (res) => {
        let body = '';
        res.on('data', chunk => body += chunk);
        res.on('end', () => {
          const cookies = (res.headers['set-cookie'] || []).map(c => c.split(';')[0]).join('; ');
          const fbzxMatch = body.match(/name="fbzx"\s*value="([^"]+)"/i);
          resolve({
            fbzx: fbzxMatch ? fbzxMatch[1] : null,
            cookies
          });
        });
      });
      req.on('error', () => resolve({ fbzx: null, cookies: '' }));
      req.on('timeout', () => { req.destroy(); resolve({ fbzx: null, cookies: '' }); });
      req.end();
    } catch (e) {
      resolve({ fbzx: null, cookies: '' });
    }
  });
}

async function postToGoogleForms(formCfg, data) {
  if (!formCfg || !formCfg.responseUrl) {
    return { success: false, error: 'No Google Form response URL configured' };
  }

  // Fetch session metadata (fbzx + cookies) to ensure verified Google Forms acceptance
  let fbzx = null;
  let cookies = '';
  if (formCfg.url) {
    const meta = await fetchGoogleFormMetadata(formCfg.url);
    fbzx = meta.fbzx;
    cookies = meta.cookies;
  }

  const entries = formCfg.entries || {};
  const serviceOptions = formCfg.serviceOptions || {};
  const params = new URLSearchParams();

  for (const [fieldKey, entryId] of Object.entries(entries)) {
    if (!entryId) continue;
    if (fieldKey === 'service') {
      const rawService = data.service || '';
      params.append(entryId, serviceOptions[rawService] || rawService);
    } else if (fieldKey === 'organisation') {
      let org = data.organisation || '';
      if (formCfg.key === 'form2' || formCfg.name === 'General Contact Form') {
        // Google Form 2 Question 2 has an email validation rule in Google Forms
        const email = data.email || '';
        if (!org.includes('@') && email) {
          org = `${org} <${email}>`;
        }
      }
      params.append(entryId, org);
    } else if (fieldKey === 'right_time_to_call_hour') {
      const rawTime = data.right_time_to_call || data.appt || '';
      let hour = '10';
      const m = rawTime.match(/(\d{1,2}):?(\d{2})?\s*(AM|PM)?/i);
      if (m) {
        let h = parseInt(m[1], 10);
        const ampm = m[3] ? m[3].toUpperCase() : '';
        if (ampm === 'PM' && h < 12) h += 12;
        if (ampm === 'AM' && h === 12) h = 0;
        hour = String(h).padStart(2, '0');
      }
      params.append(entryId, hour);
    } else if (fieldKey === 'right_time_to_call_minute') {
      const rawTime = data.right_time_to_call || data.appt || '';
      let minute = '00';
      const m = rawTime.match(/(\d{1,2}):?(\d{2})?\s*(AM|PM)?/i);
      if (m && m[2]) {
        minute = String(parseInt(m[2], 10)).padStart(2, '0');
      }
      params.append(entryId, minute);
    } else if (data[fieldKey] !== undefined && data[fieldKey] !== null) {
      params.append(entryId, String(data[fieldKey]));
    }
  }

  params.append('fvv', '1');
  if (fbzx) {
    params.append('fbzx', fbzx);
  }
  params.append('pageHistory', '0');

  const postData = params.toString();
  const url = new URL(formCfg.responseUrl);

  const headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': Buffer.byteLength(postData),
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Origin': 'https://docs.google.com'
  };
  if (cookies) {
    headers['Cookie'] = cookies;
  }
  if (formCfg.url) {
    headers['Referer'] = formCfg.url;
  }

  return new Promise((resolve) => {
    const req = https.request({
      hostname: url.hostname,
      path: url.pathname,
      method: 'POST',
      headers,
      timeout: 10000
    }, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        const isSuccess = (res.statusCode >= 200 && res.statusCode < 400) &&
          (body.includes('Thanks for submitting your contact info!') ||
           body.includes('Your response has been recorded') ||
           body.includes('edit2='));
        resolve({
          success: isSuccess,
          statusCode: res.statusCode,
          message: isSuccess ? 'Google Form response recorded' : `HTTP ${res.statusCode}`
        });
      });
    });

    req.on('error', (err) => {
      resolve({ success: false, error: err.message });
    });
    req.on('timeout', () => {
      req.destroy();
      resolve({ success: false, error: 'Timeout after 10s' });
    });

    req.write(postData);
    req.end();
  });
}

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

// In-memory deduplication map: key -> timestamp
const submissionDedupMap = new Map();

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

// Robust Body Parser supporting both URL-encoded and multipart/form-data
function parseRequestBody(body, contentType = '') {
  const map = new Map();
  if (contentType.includes('multipart/form-data') || body.startsWith('------') || body.includes('Content-Disposition: form-data;')) {
    let boundary = '';
    const boundaryMatch = contentType.match(/boundary=([^\s;]+)/i);
    if (boundaryMatch) {
      boundary = boundaryMatch[1];
    } else {
      const match = body.match(/^--([^\r\n]+)/);
      if (match) boundary = match[1];
    }
    if (boundary) {
      const parts = body.split('--' + boundary);
      for (const part of parts) {
        if (!part || part.trim() === '--') continue;
        const headerEnd = part.indexOf('\r\n\r\n') !== -1 ? part.indexOf('\r\n\r\n') : part.indexOf('\n\n');
        if (headerEnd === -1) continue;
        const headerText = part.slice(0, headerEnd);
        const delimiterLength = part.indexOf('\r\n\r\n') !== -1 ? 4 : 2;
        let value = part.slice(headerEnd + delimiterLength);
        value = value.replace(/\r?\n$/, '');
        const nameMatch = headerText.match(/name="([^"]+)"/i);
        if (nameMatch) {
          map.set(nameMatch[1], value);
        }
      }
    }
  } else {
    const sp = new URLSearchParams(body);
    for (const [k, v] of sp.entries()) {
      map.set(k, v);
    }
  }
  return {
    get(key) { return map.has(key) ? map.get(key) : null; },
    has(key) { return map.has(key); },
    entries() { return map.entries(); }
  };
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

  // Inject Google Form URLs from centralized forms-config.php
  const formsConfig = loadFormsConfig();
  content = content.replace(/<\?php\s+echo\s+htmlspecialchars\(\s*sln_get_form1_url\(\)[^\)]*\);\s*\?>/gi, formsConfig.form1.url);
  content = content.replace(/<\?php\s+echo\s+htmlspecialchars\(\s*sln_get_form2_url\(\)[^\)]*\);\s*\?>/gi, formsConfig.form2.url);
  // Also update any static URLs that may be present
  content = content.replace(/https:\/\/docs\.google\.com\/forms\/d\/e\/1FAIpQLSdpVszsphdo1KhHgig4lCHfjuHmE8IzSvIUDHEFiE52LoW0Rw\/viewform/g, formsConfig.form1.url);
  content = content.replace(/https:\/\/docs\.google\.com\/forms\/d\/e\/1FAIpQLSfp_u4mUMGlDdk9omnkDtI-Us3aDAlM4KzEGit3B-duDh4B1A\/viewform/g, formsConfig.form2.url);

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
    const isSsl = secure === 'ssl' || secure === 'true' || secure === true || (Number(port) === 465 && secure !== 'tls');
    const toList = Array.isArray(to) ? to : to.split(',').map(s => s.trim()).filter(Boolean);
    let rcptIdx = 0;
    const socket = isSsl ? tls.connect(Number(port), host, { rejectUnauthorized: true }) : net.connect(Number(port), host);
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
          rejectUnauthorized: true
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
        if (toList.length === 0) {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: invalid recipient] No valid recipients provided.'));
        }
        step = 8;
        rcptIdx = 0;
        sendCmd(`RCPT TO:<${toList[rcptIdx]}>`);
      } else if (step === 8) {
        if (code !== '250') {
          activeSocket.destroy();
          return reject(new Error('[SLN SMTP Error: invalid recipient] RCPT TO:<' + toList[rcptIdx] + '> rejected: ' + line));
        }
        rcptIdx++;
        if (rcptIdx < toList.length) {
          sendCmd(`RCPT TO:<${toList[rcptIdx]}>`);
        } else {
          step = 10;
          sendCmd('DATA');
        }
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

// Trusted Reverse Proxy Client IP resolution
function isTrustedProxy(ip) {
  if (!ip) return false;
  const clean = ip.replace(/^::ffff:/, '');
  if (clean === '127.0.0.1' || clean === '::1' || clean === 'localhost') return true;
  if (process.env.TRUST_PROXY === 'true' || process.env.TRUST_PROXY === '1') return true;
  if (process.env.TRUSTED_PROXIES) {
    const list = process.env.TRUSTED_PROXIES.split(',').map(s => s.trim());
    if (list.includes('*') || list.includes(clean)) return true;
  }
  // Standard private / local subnets (RFC 1918)
  if (clean.startsWith('10.') || clean.startsWith('192.168.') || /^172\.(1[6-9]|2[0-9]|3[0-1])\./.test(clean)) return true;
  return false;
}

function resolveClientIp(req) {
  const socketIp = (req.socket.remoteAddress || '127.0.0.1').replace(/^::ffff:/, '');
  if (!isTrustedProxy(socketIp)) {
    return socketIp;
  }
  if (req.headers['cf-connecting-ip']) {
    return req.headers['cf-connecting-ip'].trim();
  }
  if (req.headers['x-forwarded-for']) {
    const ips = req.headers['x-forwarded-for'].split(',');
    for (let candidate of ips) {
      candidate = candidate.trim().replace(/^::ffff:/, '');
      if (candidate) return candidate;
    }
  }
  if (req.headers['x-real-ip']) {
    return req.headers['x-real-ip'].trim().replace(/^::ffff:/, '');
  }
  return socketIp;
}

function saveEnquiryLocally(record) {
  const dataDir = path.join(ROOT_DIR, 'data');
  if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
    try {
      fs.writeFileSync(path.join(dataDir, '.htaccess'), "Order deny,allow\nDeny from all\n");
      fs.writeFileSync(path.join(dataDir, 'index.html'), "<!DOCTYPE html><html><head><title>403 Forbidden</title></head><body><h1>403 Forbidden</h1></body></html>");
    } catch (e) {}
  }

  const jsonFile = path.join(dataDir, 'enquiries.json');
  const csvFile = path.join(dataDir, 'enquiries.csv');

  let list = [];
  if (fs.existsSync(jsonFile)) {
    try {
      list = JSON.parse(fs.readFileSync(jsonFile, 'utf8'));
      if (!Array.isArray(list)) list = [];
    } catch (e) {
      list = [];
    }
  }
  list.push(record);
  fs.writeFileSync(jsonFile, JSON.stringify(list, null, 2), 'utf8');

  // CSV
  const csvExists = fs.existsSync(csvFile) && fs.statSync(csvFile).size > 0;
  let csvRow = '';
  if (!csvExists) {
    csvRow += 'ID,Timestamp,Date,Form Type,Name,Organisation,Designation,Email,Phone,Right Time to Call,Service,Message,Client IP,Email Status\n';
  }
  function escapeCsv(val) {
    if (val === null || val === undefined) return '""';
    const s = String(val).replace(/[\r\n]+/g, ' ').replace(/"/g, '""');
    return `"${s}"`;
  }
  csvRow += [
    record.id,
    record.timestamp,
    record.date,
    record.form_type,
    record.name,
    record.organisation,
    record.designation,
    record.email,
    record.phone,
    record.right_time_to_call || '',
    record.service,
    record.message,
    record.ip,
    record.email_status
  ].map(escapeCsv).join(',') + '\n';

  fs.appendFileSync(csvFile, csvRow, 'utf8');
  return true;
}

const server = http.createServer((req, res) => {
  const clientIp = resolveClientIp(req);
  const parsedUrl = new URL(req.url, `http://${req.headers.host || 'localhost:' + PORT}`);
  let pathname = decodeURIComponent(parsedUrl.pathname);

  // 1. Path traversal & sensitive file shield
  if (pathname.includes('..') || pathname.split('/').some(s => s.startsWith('.'))) {
    res.writeHead(403, { ...SECURITY_HEADERS, 'Content-Type': 'text/html; charset=utf-8' });
    return res.end('<h1>403 Forbidden</h1>');
  }

  const forbiddenFilesRegex = /(?:assets\.zip|dev-server\.mjs|package.*\.json|composer.*|\.env|\.git|\.log|security\.php|mailer\.php|storage\.php|.*smtp.*\.php|^\/vendor|^\/data)/i;
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

      const contentType = req.headers['content-type'] || '';
      const params = parseRequestBody(body, contentType);

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

      // Check for duplicate submission within 60s
      const subKey = `${clientIp}:${cleanEmail}:${cleanName}:${cleanMessage}`;
      const lastSubTime = submissionDedupMap.get(subKey);
      if (lastSubTime && (Date.now() - lastSubTime < 60000)) {
        return respondSuccess('Your enquiry has been submitted successfully! Thank you for contacting SLN Consulting. Our team will get back to you soon.');
      }
      submissionDedupMap.set(subKey, Date.now());

      // Check for simulated storage failure
      if (req.headers['x-simulate-storage-failure'] === 'true') {
        return respondError('Unable to submit your enquiry right now. Your details have not been confirmed as saved. Please try again.', 500);
      }

      // Generate unique Enquiry ID and record
      const enquiryId = `SLN-${new Date().toISOString().replace(/\D/g, '').slice(0, 14)}-${Math.random().toString(36).slice(2, 8).toUpperCase()}`;
      const nowIso = new Date().toISOString();
      const nowDisplay = new Date().toUTCString();

      const enquiryRecord = {
        id: enquiryId,
        timestamp: nowIso,
        date: nowDisplay,
        form_type: isCallbackForm ? 'callback_enquiry' : 'contact_enquiry',
        name: cleanName,
        organisation: cleanFname,
        designation: cleanDesignation,
        email: cleanEmail,
        phone: cleanNumber,
        right_time_to_call: cleanAppt || '',
        service: serviceName,
        message: cleanMessage,
        ip: clientIp,
        email_status: 'pending'
      };

      try {
        saveEnquiryLocally(enquiryRecord);
        console.log(`[SLN Storage Success] Saved enquiry ${enquiryId} to data/enquiries.json and data/enquiries.csv`);
      } catch (storeErr) {
        console.error(`[SLN Storage Error] Failed to store enquiry: ${storeErr.message}`);
        return respondError('Unable to submit your enquiry right now. Your details have not been confirmed as saved. Please try again.', 500);
      }

      // 1. Google Forms Forwarding (direct verification)
      let gRes = { success: true };
      const formsConfigSub = loadFormsConfig();
      const targetFormCfg = isCallbackForm ? formsConfigSub.form2 : formsConfigSub.form1;

      if (targetFormCfg && targetFormCfg.submitDirect) {
        try {
          gRes = await postToGoogleForms(targetFormCfg, {
            name: cleanName,
            organisation: cleanFname,
            designation: cleanDesignation,
            email: cleanEmail,
            phone: cleanNumber,
            right_time_to_call: cleanAppt,
            appt: cleanAppt,
            service: params.get('Services') || '',
            message: cleanMessage
          });

          if (gRes.success) {
            console.log(`[SLN Google Forms Success] Enquiry ${enquiryId} recorded on ${targetFormCfg.name}`);
            enquiryRecord.google_form_status = 'success';
          } else {
            console.warn(`[SLN Google Forms Warning] Forwarding for ${enquiryId} to ${targetFormCfg.name}:`, gRes.error || gRes.message);
            enquiryRecord.google_form_status = 'failed: ' + (gRes.error || gRes.message);
          }
        } catch (e) {
          console.warn(`[SLN Google Forms Error] Network error forwarding ${enquiryId}:`, e.message);
          enquiryRecord.google_form_status = 'error: ' + e.message;
          gRes = { success: false, error: e.message };
        }
      }

      if (!gRes.success) {
        return respondError('Unable to submit your enquiry right now. Your details have not been confirmed as saved. Please try again.', 502);
      }

      // Respond success only after confirmed recording
      respondSuccess('Your enquiry has been submitted successfully! Thank you for contacting SLN Consulting. Our team will get back to you soon.');

      // Background task: Admin Email (non-blocking)
      setImmediate(async () => {

        // 2. Email Notifications (Resend / SMTP)
        loadDotEnv();
        const smtpHost = process.env.SMTP_HOST;
        const smtpUser = process.env.SMTP_USER;
        const smtpPass = process.env.SMTP_PASS;
        const smtpPort = process.env.SMTP_PORT || 465;
        const smtpSecure = process.env.SMTP_SECURE || (Number(smtpPort) === 465 ? 'ssl' : 'tls');
        const smtpFrom = process.env.SMTP_FROM || process.env.SMTP_USER || 'srinivas.c@slnconsulting.co.in';
        const recipients = process.env.RECIPIENT_EMAIL || 'srinivas.c@slnconsulting.co.in';

        const emailSubject = cleanAppt ? `Callback Enquiry [${enquiryId}]: ${cleanName} (${cleanAppt})` : `Enquiry [${enquiryId}]: ${cleanName} - ${serviceName}`;
        const htmlBody = `<h2>New Website Enquiry</h2>
<p><strong>Enquiry Reference:</strong> ${enquiryId}</p>
<p><strong>Name:</strong> ${cleanName}</p>
<p><strong>Organisation:</strong> ${cleanFname}</p>
<p><strong>Designation:</strong> ${cleanDesignation}</p>
<p><strong>Email:</strong> ${cleanEmail}</p>
<p><strong>Phone:</strong> ${cleanNumber}</p>
${cleanAppt ? `<p><strong>Right Time to Call:</strong> ${cleanAppt}</p>` : ''}
<p><strong>Service:</strong> ${serviceName}</p>
<p><strong>Requirement:</strong> ${cleanMessage || '<em>No additional details provided.</em>'}</p>`;

        // Resend API (if configured)
        const resendKey = process.env.RESEND_API_KEY;
        if (resendKey && !resendKey.includes('your_api_key_here')) {
          try {
            const res = await fetch('https://api.resend.com/emails', {
              method: 'POST',
              headers: {
                'Authorization': `Bearer ${resendKey}`,
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                from: process.env.MAIL_FROM || 'SLN Consulting <onboarding@resend.dev>',
                to: recipients.split(',').map(s => s.trim()).filter(Boolean),
                subject: emailSubject,
                html: htmlBody,
                reply_to: cleanEmail
              })
            });
            const resJson = await res.json().catch(() => ({}));
            if (res.ok && resJson.id) {
              console.log(`[SLN Resend Success] Email dispatched (ID: ${resJson.id}) to ${recipients}`);
              enquiryRecord.email_status = 'sent';
            }
          } catch (err) {
            console.warn('[SLN Resend Warning]', err.message);
          }
        }

        // Authenticated SMTP (if configured)
        const isPlaceholder = (val) => !val || /^(YOUR_|REPLACE_|CHANGEME|<your|placeholder)/i.test(val.trim());
        const hasSmtp = smtpHost && !isPlaceholder(smtpHost) && smtpUser && !isPlaceholder(smtpUser) && smtpPass && !isPlaceholder(smtpPass);

        if (hasSmtp) {
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
            enquiryRecord.email_status = 'sent';

            // Visitor auto-reply
            const visitorSubject = "We Have Received Your Enquiry – SLN Consulting";
            const enquiryDetailsSubject = cleanAppt ? `Callback Request: ${serviceName} (Preferred Time: ${cleanAppt})` : (serviceName !== 'General Enquiry' ? `Enquiry regarding ${serviceName}` : (cleanDesignation || 'Website Enquiry'));
            const visitorHtmlBody = `<h2>SLN Consulting</h2>
<p>Dear ${cleanName},</p>
<p>Thank you for contacting SLN Consulting.</p>
<p>We have successfully received your enquiry. Our team will review your message and get back to you as soon as possible.</p>
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #013df5; padding: 14px 18px; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0; color: #013df5;">Your Enquiry Details</h3>
  <p style="margin: 6px 0;"><strong>Enquiry Reference:</strong> ${enquiryId}</p>
  <p style="margin: 6px 0;"><strong>Subject:</strong> ${enquiryDetailsSubject}</p>
  <p style="margin: 6px 0;"><strong>Received on:</strong> ${nowDisplay}</p>
</div>
<p>Thank you for your interest in SLN Consulting.</p>
<p>Best regards,<br><strong>SLN Consulting Team</strong><br><a href="https://www.slnconsulting.co.in/">https://www.slnconsulting.co.in/</a></p>`;

            try {
              await sendViaSmtpSocket({
                host: smtpHost,
                port: smtpPort,
                user: smtpUser,
                pass: smtpPass,
                from: smtpFrom,
                to: cleanEmail,
                subject: visitorSubject,
                html: visitorHtmlBody,
                replyTo: smtpFrom,
                replyToName: 'SLN Consulting',
                secure: smtpSecure
              });
              console.log(`[SLN Auto-Reply Success] Visitor acknowledgement sent to ${cleanEmail}`);
            } catch (autoErr) {
              console.warn(`[SLN Auto-Reply Warning] Visitor auto-reply failed: ${autoErr.message}`);
            }
          } catch (err) {
            console.warn(`[SLN Email Warning] Stored enquiry ${enquiryId}, but admin notification email failed: ${err.message}`);
            enquiryRecord.email_status = 'failed: ' + err.message;
          }
        }
      });
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
