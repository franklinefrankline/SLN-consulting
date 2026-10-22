import tls from 'node:tls';
import fs from 'node:fs';

const envPath = 'c:/Users/inbat/Downloads/SLN-Website-Development/SLN-Website-Development/.env';
let env = {};
if (fs.existsSync(envPath)) {
  const lines = fs.readFileSync(envPath, 'utf8').split('\n');
  for (let l of lines) {
    l = l.trim();
    if (!l || l.startsWith('#')) continue;
    const [k, ...v] = l.split('=');
    env[k.trim()] = v.join('=').trim().replace(/^["']|["']$/g, '');
  }
}

const host = env.SMTP_HOST || 'smtpout.secureserver.net';
const port = Number(env.SMTP_PORT) || 465;
const user = env.SMTP_USER || 'srinivas.c@slnconsulting.co.in';
const pass = env.SMTP_PASS || '';
const from = env.SMTP_FROM || user;
const adminRecipient = env.RECIPIENT_EMAIL || user;
const testVisitorEmail = user; // Send visitor auto-reply to the same verified mailbox for testing
const testVisitorName = 'Test Visitor (Verification)';

console.log('===============================================================');
console.log('SLN Consulting - GoDaddy SMTP Verification & Dual Email Test');
console.log('===============================================================');
console.log(`SMTP Host:          ${host}`);
console.log(`SMTP Port:          ${port} (SSL/TLS)`);
console.log(`Authenticated User: ${user}`);
console.log(`Admin Mailbox:      ${adminRecipient}`);
console.log(`Test Visitor Email: ${testVisitorEmail}`);
console.log(`Password configured:${pass ? ' [YES - ' + pass.length + ' chars]' : ' [NO - EMPTY]'}\n`);

if (!pass) {
  console.log('[!] Notice: SMTP_PASS is empty in .env.');
  console.log('    Please edit .env and enter your valid GoDaddy mailbox password,');
  console.log('    then rerun this script to verify live email delivery.\n');
  process.exit(1);
}

function sendSmtpMessage({ toEmail, subject, htmlBody, replyToEmail, replyToName }) {
  return new Promise((resolve, reject) => {
    const socket = tls.connect(port, host, { rejectUnauthorized: true }, () => {});
    let buffer = '';
    let step = 0;

    socket.setTimeout(15000);
    socket.on('timeout', () => {
      socket.destroy();
      reject(new Error('SMTP connection timed out after 15 seconds.'));
    });
    socket.on('error', (err) => {
      reject(new Error('TLS socket error: ' + err.message));
    });

    socket.on('data', (chunk) => {
      buffer += chunk.toString();
      const lines = buffer.split('\r\n');
      buffer = lines.pop();

      for (const line of lines) {
        if (!line) continue;
        const code = line.substring(0, 3);
        const isLast = line.length < 4 || line.charAt(3) === ' ';
        if (!isLast) continue;

        if (step === 0 && code === '220') {
          step = 1;
          socket.write('EHLO localhost\r\n');
        } else if (step === 1 && code === '250') {
          step = 2;
          socket.write('AUTH LOGIN\r\n');
        } else if (step === 2 && code === '334') {
          step = 3;
          socket.write(Buffer.from(user).toString('base64') + '\r\n');
        } else if (step === 3 && code === '334') {
          step = 4;
          socket.write(Buffer.from(pass).toString('base64') + '\r\n');
        } else if (step === 4) {
          if (code === '235') {
            step = 5;
            socket.write(`MAIL FROM:<${user}>\r\n`);
          } else {
            socket.write('QUIT\r\n');
            return reject(new Error(`SMTP Authentication failed: ${line}`));
          }
        } else if (step === 5) {
          if (code === '250') {
            step = 6;
            socket.write(`RCPT TO:<${toEmail}>\r\n`);
          } else {
            socket.write('QUIT\r\n');
            return reject(new Error(`MAIL FROM rejected: ${line}`));
          }
        } else if (step === 6) {
          if (code === '250') {
            step = 7;
            socket.write('DATA\r\n');
          } else {
            socket.write('QUIT\r\n');
            return reject(new Error(`RCPT TO rejected: ${line}`));
          }
        } else if (step === 7) {
          if (code === '354') {
            const dateStr = new Date().toUTCString();
            const base64Body = Buffer.from(htmlBody, 'utf8').toString('base64');
            const chunkedBody = (base64Body.match(/.{1,76}/g) || []).join('\r\n');
            const replyToHeader = replyToEmail ? `Reply-To: ${replyToName ? `${replyToName} <${replyToEmail}>` : replyToEmail}\r\n` : '';
            const rawEmail = [
              `Date: ${dateStr}`,
              `From: SLN Consulting <${user}>`,
              `To: ${toEmail}`,
              replyToHeader + `Subject: =?UTF-8?B?${Buffer.from(subject).toString('base64')}?=`,
              `MIME-Version: 1.0`,
              `Content-Type: text/html; charset=UTF-8`,
              `Content-Transfer-Encoding: base64`,
              '',
              chunkedBody,
              '.'
            ].filter(Boolean).join('\r\n');

            step = 8;
            socket.write(rawEmail + '\r\n');
          } else {
            socket.write('QUIT\r\n');
            return reject(new Error(`DATA rejected: ${line}`));
          }
        } else if (step === 8) {
          if (code === '250') {
            step = 9;
            socket.write('QUIT\r\n');
            socket.end();
            return resolve({ success: true, response: line });
          } else {
            socket.write('QUIT\r\n');
            return reject(new Error(`Message data rejected: ${line}`));
          }
        }
      }
    });
  });
}

async function runDualTest() {
  const submissionDate = new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' });

  // 1. Test Admin Notification Email
  console.log('[1/2] Testing Admin Notification Email dispatch...');
  const adminSubject = `[SLN Test] Website Enquiry - ${testVisitorName}`;
  const adminHtml = `<h2>New Website Enquiry</h2>
<table>
  <tr><td><strong>Name:</strong></td><td>${testVisitorName}</td></tr>
  <tr><td><strong>Email:</strong></td><td>${testVisitorEmail}</td></tr>
  <tr><td><strong>Subject:</strong></td><td>VAPT Security Audit Enquiry</td></tr>
  <tr><td><strong>Date:</strong></td><td>${submissionDate}</td></tr>
  <tr><td><strong>Message:</strong></td><td>This is a verified test enquiry dispatching to admin.</td></tr>
</table>`;

  try {
    const res1 = await sendSmtpMessage({
      toEmail: adminRecipient,
      subject: adminSubject,
      htmlBody: adminHtml,
      replyToEmail: testVisitorEmail,
      replyToName: testVisitorName
    });
    console.log(`      [PASS] Admin Notification Email ACCEPTED by GoDaddy SMTP server!`);
    console.log(`      Server response: ${res1.response}`);
    console.log(`      Recipient: ${adminRecipient}\n`);
  } catch (err) {
    console.error(`      [FAIL] Admin Email Dispatch Failed: ${err.message}\n`);
    process.exit(1);
  }

  // 2. Test Visitor Acknowledgement Auto-Reply
  console.log('[2/2] Testing Visitor Automatic Acknowledgement Email dispatch...');
  const visitorSubject = "We Have Received Your Enquiry – SLN Consulting";
  const visitorHtml = `<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
  <p>Dear ${testVisitorName},</p>
  <p>Thank you for contacting SLN Consulting.</p>
  <p>We have successfully received your enquiry. Our team will review your message and get back to you as soon as possible.</p>
  <div style="background: #f8fafc; border-left: 4px solid #013df5; padding: 12px 16px; margin: 18px 0;">
    <h4 style="margin: 0 0 8px 0; color: #013df5;">Your Enquiry Details</h4>
    <p style="margin: 4px 0;"><strong>Subject:</strong> VAPT Security Audit Enquiry</p>
    <p style="margin: 4px 0;"><strong>Received on:</strong> ${submissionDate}</p>
  </div>
  <p>Thank you for your interest in SLN Consulting.</p>
  <p>Best regards,<br><strong>SLN Consulting Team</strong><br><a href="https://www.slnconsulting.co.in/">https://www.slnconsulting.co.in/</a></p>
</body>
</html>`;

  try {
    const res2 = await sendSmtpMessage({
      toEmail: testVisitorEmail,
      subject: visitorSubject,
      htmlBody: visitorHtml,
      replyToEmail: user,
      replyToName: 'SLN Consulting'
    });
    console.log(`      [PASS] Visitor Acknowledgement Email ACCEPTED by GoDaddy SMTP server!`);
    console.log(`      Server response: ${res2.response}`);
    console.log(`      Recipient: ${testVisitorEmail}\n`);

    console.log('===============================================================');
    console.log('[SUCCESS] Both email workflows verified and accepted by GoDaddy SMTP!');
    console.log('1. Admin Notification -> Delivered to ' + adminRecipient);
    console.log('2. Visitor Auto-Reply -> Delivered to ' + testVisitorEmail);
    console.log('Action: Please check your inbox and spam folder at ' + user);
    console.log('===============================================================\n');
  } catch (err) {
    console.error(`      [FAIL] Visitor Auto-Reply Dispatch Failed: ${err.message}\n`);
    process.exit(1);
  }
}

runDualTest();
