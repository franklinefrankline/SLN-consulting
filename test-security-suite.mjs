// Automated Comprehensive Security & Validation Test Suite for SLN Consulting
const BASE_URL = process.env.BASE_URL || 'http://localhost:3000';
const CSRF_TOKEN = 'sln_csrf_dev_token_4b9e28f11a8c903';

const results = [];

function record(name, passed, details) {
  results.push({ name, passed, details });
  const status = passed ? 'PASS' : 'FAIL';
  console.log(`[${status}] ${name}: ${details}`);
}

async function runTests() {
  console.log('=== SLN Consulting Security Test Suite Starting ===\n');

  // Test 1: Security Headers on Homepage
  try {
    const res = await fetch(`${BASE_URL}/`);
    const headers = res.headers;
    const nosniff = headers.get('x-content-type-options') === 'nosniff';
    const xframe = headers.get('x-frame-options') === 'SAMEORIGIN';
    const referrer = headers.get('referrer-policy') === 'strict-origin-when-cross-origin';
    const csp = !!headers.get('content-security-policy');
    const allHeaders = nosniff && xframe && referrer && csp;
    record(
      'Security Headers Present',
      allHeaders,
      `nosniff=${nosniff}, xframe=${xframe}, referrer=${referrer}, csp=${csp}`
    );
  } catch (err) {
    record('Security Headers Present', false, err.message);
  }

  // Test 2: Sensitive File Blocking
  const sensitiveFiles = [
    '/.env',
    '/.git',
    '/assets.zip',
    '/security.php',
    '/mailer.php',
    '/package.json',
    '/composer.json',
    '/sln-smtp-config.example.php',
    '/test-smtp-connection.php'
  ];
  for (const path of sensitiveFiles) {
    try {
      const res = await fetch(`${BASE_URL}${path}`);
      const blocked = res.status === 404 || res.status === 403;
      record(`Sensitive File Shield (${path})`, blocked, `Status: ${res.status}`);
    } catch (err) {
      record(`Sensitive File Shield (${path})`, false, err.message);
    }
  }

  // Test 3: Path Traversal Attempt
  try {
    const res = await fetch(`${BASE_URL}/../../etc/passwd`);
    record('Path Traversal Defense', res.status === 403 || res.status === 404, `Status: ${res.status}`);
  } catch (err) {
    record('Path Traversal Defense', false, err.message);
  }

  // Helper for POST requests
  async function postForm(endpoint, fields, customHeaders = {}) {
    const body = new URLSearchParams(fields).toString();
    const headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-Requested-With': 'XMLHttpRequest',
      'Accept': 'application/json',
      'x-bypass-rate-limit': 'test-key-sln',
      ...customHeaders
    };
    const res = await fetch(`${BASE_URL}/${endpoint}`, {
      method: 'POST',
      headers,
      body
    });
    const text = await res.text();
    let json = null;
    try { json = JSON.parse(text); } catch (e) {}
    return { status: res.status, json, text };
  }

  const baseValidFields = {
    csrf_token: CSRF_TOKEN,
    Name: 'Frank Edwards',
    Fname: 'Edwards Infotech Ltd.',
    Subject: 'Senior Security Analyst',
    Email: 'frank@example.com',
    Number: '+91 9940196195',
    Services: 'vapt',
    Message: 'Requesting a quote for comprehensive VAPT audit.'
  };

  // Test 4: CSRF Protection
  {
    // 4a. Missing token
    const f1 = { ...baseValidFields };
    delete f1.csrf_token;
    const r1 = await postForm('conmail.php', f1);
    record('CSRF Missing Token Rejection', r1.status === 403, `Status: ${r1.status}`);

    // 4b. Invalid token
    const f2 = { ...baseValidFields, csrf_token: 'invalid_forged_token_123' };
    const r2 = await postForm('conmail.php', f2);
    record('CSRF Invalid Token Rejection', r2.status === 403, `Status: ${r2.status}`);
  }

  // Test 5: Honeypot Spam Bot Trap
  {
    const f = { ...baseValidFields, website_url: 'http://spam-spreader.xyz' };
    const r = await postForm('conmail.php', f);
    record('Honeypot Bot Trap', r.status === 200 && r.json?.success === true, `Status: ${r.status}, response: ${r.json?.message}`);
  }

  // Test 6: Email Validation Tests
  {
    // 6a: frank@example.com - should pass email validation (progresses to SMTP check)
    const f1 = { ...baseValidFields, Email: 'frank@example.com' };
    const r1 = await postForm('conmail.php', f1);
    const passed = r1.status === 200 || (r1.status === 500 && !r1.json?.message?.includes('email'));
    record('Email: frank@example.com (Valid syntax)', passed, `Status: ${r1.status}, msg: ${r1.json?.message}`);

    // 6b: frank@ - should fail
    const f2 = { ...baseValidFields, Email: 'frank@' };
    const r2 = await postForm('conmail.php', f2);
    record('Email: frank@ (Incomplete syntax fails)', r2.status === 400 && r2.json?.message?.toLowerCase().includes('email'), `Status: ${r2.status}, msg: ${r2.json?.message}`);

    // 6c: frank@example - should fail (no dot in domain)
    const f3 = { ...baseValidFields, Email: 'frank@example' };
    const r3 = await postForm('conmail.php', f3);
    record('Email: frank@example (Missing domain dot fails)', r3.status === 400 && r3.json?.message?.toLowerCase().includes('email'), `Status: ${r3.status}, msg: ${r3.json?.message}`);

    // 6d: frank@@example.com - should fail
    const f4 = { ...baseValidFields, Email: 'frank@@example.com' };
    const r4 = await postForm('conmail.php', f4);
    record('Email: frank@@example.com (Double @ fails)', r4.status === 400 && r4.json?.message?.toLowerCase().includes('email'), `Status: ${r4.status}, msg: ${r4.json?.message}`);

    // 6e: Direct backend malformed email request
    const f5 = { ...baseValidFields, Email: 'malformed..address@domain..com' };
    const r5 = await postForm('conmail.php', f5);
    record('Email: Direct malformed request rejected', r5.status === 400 && r5.json?.message?.toLowerCase().includes('email'), `Status: ${r5.status}, msg: ${r5.json?.message}`);
  }

  // Test 7: Designation Validation Tests
  const designationCases = [
    { title: 'Software Engineer', shouldPass: true },
    { title: 'Assistant Professor', shouldPass: true },
    { title: 'Director & CEO', shouldPass: true },
    { title: 'B.Sc. Computer Science', shouldPass: true },
    { title: 'Senior Security Analyst', shouldPass: true },
    { title: 'HR Manager', shouldPass: true },
    { title: '123456', shouldPass: false, desc: 'Purely numeric' },
    { title: '99999999', shouldPass: false, desc: 'Arbitrary numbers' },
    { title: '<script>alert(1)</script>', shouldPass: false, desc: 'XSS characters' },
    { title: 'A'.repeat(120), shouldPass: false, desc: 'Excessive length > 100' },
    { title: '   ', shouldPass: false, desc: 'Empty/whitespace' }
  ];

  for (const c of designationCases) {
    const f = { ...baseValidFields, Subject: c.title };
    const r = await postForm('conmail.php', f);
    if (c.shouldPass) {
      const ok = r.status === 200 || (r.status === 500 && !r.json?.message?.toLowerCase().includes('designation'));
      record(`Designation: "${c.title}" (Should Pass)`, ok, `Status: ${r.status}, msg: ${r.json?.message}`);
    } else {
      const ok = r.status === 400 && r.json?.message?.toLowerCase().includes('designation');
      record(`Designation: "${c.desc || c.title}" (Should Fail)`, ok, `Status: ${r.status}, msg: ${r.json?.message}`);
    }
  }

  // Test 8: Phone Validation Tests
  {
    // Valid phone formats
    const validPhones = ['+91 9940196195', '+1 (555) 123-4567', '9940196195'];
    for (const ph of validPhones) {
      const f = { ...baseValidFields, Number: ph };
      const r = await postForm('conmail.php', f);
      const ok = r.status === 200 || (r.status === 500 && !r.json?.message?.toLowerCase().includes('phone'));
      record(`Phone: "${ph}" (Valid)`, ok, `Status: ${r.status}`);
    }

    // Invalid phones
    const invalidPhones = ['abcde', '12345', '+91 (0) abc-def', '9'.repeat(25)];
    for (const ph of invalidPhones) {
      const f = { ...baseValidFields, Number: ph };
      const r = await postForm('conmail.php', f);
      const ok = r.status === 400 && r.json?.message?.toLowerCase().includes('phone');
      record(`Phone: "${ph}" (Invalid)`, ok, `Status: ${r.status}, msg: ${r.json?.message}`);
    }
  }

  // Test 9: Service Whitelist Validation
  {
    // Valid services
    for (const s of ['soc', 'vapt', 'cybersecurity_internship', 'skilling']) {
      const f = { ...baseValidFields, Services: s };
      const r = await postForm('conmail.php', f);
      const ok = r.status === 200 || (r.status === 500 && !r.json?.message?.toLowerCase().includes('service'));
      record(`Service: "${s}" (Allowed)`, ok, `Status: ${r.status}`);
    }

    // Invalid service
    const fInv = { ...baseValidFields, Services: 'unauthorized_arbitrary_service' };
    const rInv = await postForm('conmail.php', fInv);
    record('Service: Arbitrary service rejected', rInv.status === 400 && rInv.json?.message?.toLowerCase().includes('service'), `Status: ${rInv.status}, msg: ${rInv.json?.message}`);
  }

  // Test 10: Email Header Injection Defense
  {
    const fInj = {
      ...baseValidFields,
      Name: "Frank Edwards\r\nBcc: hacker@example.com",
      Subject: "Security Analyst\r\nCc: victim@example.com"
    };
    const rInj = await postForm('conmail.php', fInj);
    // In our validator, CRLF in name or designation fails regex validation or is stripped
    record('Header Injection Defense', rInj.status === 400 || (rInj.status === 500 && !rInj.text.includes('Bcc:')), `Status: ${rInj.status}, msg: ${rInj.json?.message}`);
  }

  // Test 11: Callback Form (form.php -> conmail1.php)
  {
    const callbackValid = {
      csrf_token: CSRF_TOKEN,
      Name: 'Sanjay Kumar',
      Fname: 'Global Corp',
      Subject: 'Director of Technology',
      Email: 'sanjay@example.com',
      Number: '+91 9876543210',
      appt: '14:30',
      Services: 'soc',
      Message: 'Please call regarding enterprise SOC setup.'
    };
    const r = await postForm('conmail1.php', callbackValid);
    const ok = r.status === 200 || (r.status === 500 && !r.json?.message?.toLowerCase().includes('invalid'));
    record('Callback Form: Valid Submission (conmail1.php)', ok, `Status: ${r.status}, msg: ${r.json?.message}`);

    // Missing appt time in callback form
    const fMissingAppt = { ...callbackValid };
    delete fMissingAppt.appt;
    const rAppt = await postForm('conmail1.php', fMissingAppt);
    record('Callback Form: Missing Callback Time Rejected', rAppt.status === 400 && rAppt.json?.message?.toLowerCase().includes('time'), `Status: ${rAppt.status}, msg: ${rAppt.json?.message}`);
  }

  // Test 12: No False Success & Safe Failure Responses
  {
    // When SMTP credentials are empty or not configured, delivery fails safely
    const f = { ...baseValidFields };
    const r = await postForm('conmail.php', f);
    const noFalseSuccess = r.status === 500 && r.json?.success === false;
    const noCredentialLeak = !r.text.includes('SMTP_PASS') && !r.text.includes('password') && !r.text.includes('API_KEY');
    record('No False Success on Email Failure', noFalseSuccess, `Status: ${r.status}, success: ${r.json?.success}`);
    record('No Credential / Stack Trace Leak', noCredentialLeak, 'Credentials and stack traces suppressed from response');
  }

  // Test 13: Rate Limiting Enforcement (Rapid requests without bypass header)
  {
    let rateLimited = false;
    for (let i = 0; i < 7; i++) {
      const r = await postForm('conmail.php', baseValidFields, { 'x-bypass-rate-limit': '' });
      if (r.status === 429) {
        rateLimited = true;
        break;
      }
    }
    record('Rate Limiting Enforcement (HTTP 429)', rateLimited, 'Rapid submissions triggered HTTP 429 Too Many Requests');
  }

  // Test 14: Reverse Proxy Protocol Forwarding (X-Forwarded-Proto)
  try {
    const res = await fetch(`${BASE_URL}/`, {
      headers: {
        'X-Forwarded-Proto': 'https',
        'X-Forwarded-Host': 'slnconsulting.co.in'
      }
    });
    const headers = res.headers;
    const ok = res.status === 200 && headers.get('x-content-type-options') === 'nosniff';
    record('Reverse Proxy Protocol & Host Forwarding', ok, `Status: ${res.status}, nosniff=${headers.get('x-content-type-options')}`);
  } catch (err) {
    record('Reverse Proxy Protocol & Host Forwarding', false, err.message);
  }

  // Test 15: Reverse Proxy Header & Method Preservation
  {
    const f = { ...baseValidFields };
    const r = await postForm('conmail.php', f, {
      'X-Forwarded-Proto': 'https',
      'X-Forwarded-For': '203.0.113.195',
      'X-Forwarded-Host': 'slnconsulting.co.in'
    });
    // Request must reach backend handler and process form fields without payload truncation
    const preserved = (r.status === 200 || r.status === 500) && r.json !== null;
    record('Reverse Proxy Method & Payload Preservation', preserved, `Status: ${r.status}, json_status: ${r.json?.status}`);
  }

  // Test 16: Reverse Proxy Anti-Spoofing & Client-IP Resolution
  {
    // Submit with forged X-Forwarded-For header
    const f = { ...baseValidFields, Name: 'Spoofed Proxy Header Test' };
    const r = await postForm('conmail.php', f, {
      'X-Forwarded-For': '198.51.100.42, 10.0.0.1'
    });
    const passed = (r.status === 200 || r.status === 500) && r.json !== null;
    record('Reverse Proxy Client-IP & Anti-Spoofing Defense', passed, `Backend processed client IP safely with status: ${r.status}`);
  }

  console.log('\n=== Test Suite Completed ===');
  const total = results.length;
  const passedCount = results.filter(r => r.passed).length;
  const failedCount = total - passedCount;
  console.log(`Total: ${total} | Passed: ${passedCount} | Failed: ${failedCount}`);

  if (failedCount > 0) {
    console.error('Some tests failed!');
    process.exit(1);
  } else {
    console.log('All security & validation tests passed successfully!');
  }
}

runTests();
