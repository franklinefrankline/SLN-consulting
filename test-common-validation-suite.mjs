/**
 * SLN Consulting - Comprehensive Common Validation & Same-Page Submission Test Suite
 *
 * Verifies both forms (contact.php -> conmail.php and form.php -> conmail1.php)
 * against all required validation rules, storage recording, error handling,
 * and same-page behavior.
 */

import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const BASE_URL = 'http://localhost:3000';
const CSRF_TOKEN = 'sln_csrf_dev_token_4b9e28f11a8c903';

let totalTests = 0;
let passedTests = 0;
let failedTests = 0;

function assert(condition, message) {
  totalTests++;
  if (condition) {
    passedTests++;
    console.log(`  [PASS] ${message}`);
  } else {
    failedTests++;
    console.error(`  [FAIL] ${message}`);
  }
}

function makeRequest(pathname, { method = 'POST', headers = {}, body = '', isJson = true } = {}) {
  return new Promise((resolve, reject) => {
    const url = new URL(pathname, BASE_URL);
    const reqHeaders = {
      'X-Requested-With': 'XMLHttpRequest',
      'Accept': 'application/json',
      'X-Bypass-Rate-Limit': 'test-key-sln',
      ...headers
    };

    if (method === 'POST' && !reqHeaders['Content-Type']) {
      reqHeaders['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';
    }

    const req = http.request(url, { method, headers: reqHeaders }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        let json = null;
        if (isJson) {
          try {
            json = JSON.parse(data);
          } catch (e) {
            json = null;
          }
        }
        resolve({ status: res.statusCode, headers: res.headers, body: data, json });
      });
    });

    req.on('error', reject);
    if (body) req.write(body);
    req.end();
  });
}

function toUrlParams(obj) {
  const params = new URLSearchParams();
  for (const [k, v] of Object.entries(obj)) {
    if (v !== undefined && v !== null) {
      params.append(k, v);
    }
  }
  return params.toString();
}

console.log('='.repeat(75));
console.log(' SLN CONSULTING — COMMON VALIDATION & SAME-PAGE SUBMISSION SUITE');
console.log('='.repeat(75));

async function runSuite() {
  const EXPECTED_SUCCESS_MSG = 'Your enquiry has been submitted successfully! Thank you for contacting SLN Consulting. Our team will get back to you soon.';

  // -------------------------------------------------------------
  // SUITE 1: Page Integrity & Frontend Script Checks
  // -------------------------------------------------------------
  console.log('\n--- SUITE 1: Frontend Script & Page Inspection ---');

  const contactHtml = await makeRequest('/contact.php', { method: 'GET', isJson: false });
  assert(contactHtml.status === 200, 'contact.php loads successfully with HTTP 200');
  assert(!contactHtml.body.includes('window.open('), 'contact.php has NO window.open (no redirect / no new tab)');
  assert(contactHtml.body.includes(EXPECTED_SUCCESS_MSG), 'contact.php contains exact required success message');
  assert(contactHtml.body.includes('markInvalid('), 'contact.php implements field-level invalid markers');
  assert(contactHtml.body.includes('clearFieldErrors()'), 'contact.php implements real-time field error clearing');

  const formHtml = await makeRequest('/form.php', { method: 'GET', isJson: false });
  assert(formHtml.status === 200, 'form.php loads successfully with HTTP 200');
  assert(!formHtml.body.includes('window.open('), 'form.php has NO window.open (no redirect / no new tab)');
  assert(formHtml.body.includes(EXPECTED_SUCCESS_MSG), 'form.php contains exact required success message');
  assert(formHtml.body.includes('markInvalid('), 'form.php implements field-level invalid markers');
  assert(formHtml.body.includes('clearFieldErrors()'), 'form.php implements real-time field error clearing');

  // -------------------------------------------------------------
  // SUITE 2: Form 1 (contact.php -> conmail.php) Validation Rules
  // -------------------------------------------------------------
  console.log('\n--- SUITE 2: Form 1 (conmail.php) Validation Tests ---');

  // 2.1 Empty Name
  {
    const payload = toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: '   ',
      Fname: 'Tech Enterprises',
      Subject: 'Security Officer',
      Email: 'valid@example.com',
      Number: '+91 9876543210',
      Services: 'soc',
      Message: 'Looking for SOC'
    });
    const res = await makeRequest('/conmail.php', { body: payload });
    assert(res.status === 400 && res.json && res.json.success === false, 'Form 1 rejects empty / whitespace Name');
  }

  // 2.2 Empty Organisation Name
  {
    const payload = toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: 'John Doe',
      Fname: '',
      Subject: 'Security Officer',
      Email: 'valid@example.com',
      Number: '+91 9876543210',
      Services: 'soc',
      Message: 'Looking for SOC'
    });
    const res = await makeRequest('/conmail.php', { body: payload });
    assert(res.status === 400 && res.json && res.json.success === false, 'Form 1 rejects blank Organisation Name');
  }

  // 2.3 Organisation Name is NOT checked as an email (accepts normal corporate names)
  {
    const payload = toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: 'John Doe',
      Fname: 'Acme Systems & Solutions Ltd.',
      Subject: 'Director',
      Email: 'john@acme.com',
      Number: '+91 9876543210',
      Services: 'soc',
      Message: 'Test'
    });
    const res = await makeRequest('/conmail.php', {
      body: payload,
      headers: { 'X-Bypass-Rate-Limit': 'test-key-sln' }
    });
    assert(res.status === 200 && res.json && res.json.success === true, 'Form 1 accepts corporate Organisation without email regex');
  }

  // 2.4 Empty / Invalid Designation
  {
    const payload = toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: 'John Doe',
      Fname: 'Tech Enterprises',
      Subject: '   ',
      Email: 'valid@example.com',
      Number: '+91 9876543210',
      Services: 'soc',
      Message: 'Test'
    });
    const res = await makeRequest('/conmail.php', { body: payload });
    assert(res.status === 400 && res.json && res.json.success === false, 'Form 1 rejects blank Designation');
  }

  // 2.5 Invalid Email Formats
  const invalidEmails = ['plainaddress', 'missingdomain@', '@nodomain.com', 'user@domain..com', 'user@@domain.com'];
  for (const badEmail of invalidEmails) {
    const payload = toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: 'John Doe',
      Fname: 'Tech Enterprises',
      Subject: 'Director',
      Email: badEmail,
      Number: '+91 9876543210',
      Services: 'soc',
      Message: 'Test'
    });
    const res = await makeRequest('/conmail.php', { body: payload });
    assert(res.status === 400 && res.json && res.json.success === false, `Form 1 rejects invalid email: "${badEmail}"`);
  }

  // 2.6 Invalid Phone Numbers
  const invalidPhones = ['123', 'phone123', '12345', 'abcdefghijk'];
  for (const badPhone of invalidPhones) {
    const payload = toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: 'John Doe',
      Fname: 'Tech Enterprises',
      Subject: 'Director',
      Email: 'valid@example.com',
      Number: badPhone,
      Services: 'soc',
      Message: 'Test'
    });
    const res = await makeRequest('/conmail.php', { body: payload });
    assert(res.status === 400 && res.json && res.json.success === false, `Form 1 rejects invalid phone: "${badPhone}"`);
  }

  // 2.7 Missing Service (required on Form 1)
  {
    const payload = toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: 'John Doe',
      Fname: 'Tech Enterprises',
      Subject: 'Director',
      Email: 'valid@example.com',
      Number: '+91 9876543210',
      Services: '',
      Message: 'Test'
    });
    const res = await makeRequest('/conmail.php', { body: payload });
    assert(res.status === 400 && res.json && res.json.success === false, 'Form 1 rejects missing Service dropdown selection');
  }

  // -------------------------------------------------------------
  // SUITE 3: Form 2 (form.php -> conmail1.php) Validation Rules
  // -------------------------------------------------------------
  console.log('\n--- SUITE 3: Form 2 (conmail1.php) Validation Tests ---');

  // 3.1 Empty Name on Form 2
  {
    const payload = toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: '',
      Fname: 'Global Finance Corp',
      Subject: 'VP of IT',
      Email: 'finance@example.com',
      Number: '+91 9811223344',
      appt: '2:30 PM',
      Services: 'vapt',
      Message: 'Need security assessment'
    });
    const res = await makeRequest('/conmail1.php', { body: payload });
    assert(res.status === 400 && res.json && res.json.success === false, 'Form 2 rejects blank Name');
  }

  // 3.2 Missing Preferred Call Time on Form 2 (required on this form)
  {
    const payload = toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: 'Alice Morgan',
      Fname: 'Global Finance Corp',
      Subject: 'VP of IT',
      Email: 'alice@finance.com',
      Number: '+91 9811223344',
      appt: '',
      Services: 'vapt',
      Message: 'Need assessment'
    });
    const res = await makeRequest('/conmail1.php', { body: payload });
    assert(res.status === 400 && res.json && res.json.success === false, 'Form 2 rejects missing "Right time to call" value');
  }

  // 3.3 Optional Service on Form 2 (allowed to be empty, falls back gracefully)
  {
    const uniqueEmail = `alice.opt.${Date.now()}@finance.com`;
    const payload = toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: 'Alice Morgan',
      Fname: 'Global Finance Corp',
      Subject: 'VP of IT',
      Email: uniqueEmail,
      Number: '+91 9811223344',
      appt: '3:00 PM - 5:00 PM',
      Services: '', // optional on form.php
      Message: 'Inquiry regarding general cybersecurity consulting'
    });
    const res = await makeRequest('/conmail1.php', {
      body: payload,
      headers: { 'X-Bypass-Rate-Limit': 'test-key-sln' }
    });
    assert(res.status === 200 && res.json && res.json.success === true, 'Form 2 allows optional Service and succeeds');
  }

  // -------------------------------------------------------------
  // SUITE 4: Successful Submission & Storage Verification
  // -------------------------------------------------------------
  console.log('\n--- SUITE 4: Storage Recording & Success Messages ---');

  const testIdContact = `test_contact_${Date.now()}`;
  const payloadValid1 = toUrlParams({
    csrf_token: CSRF_TOKEN,
    Name: 'Rajesh Kumar',
    Fname: 'Apex Infosec Pvt Ltd',
    Subject: 'Chief Technology Officer',
    Email: `rajesh.${Date.now()}@apexinfosec.com`,
    Number: '+91 98230 12345',
    Services: 'vapt',
    Message: `Comprehensive penetration testing for web app (${testIdContact})`
  });

  const resValid1 = await makeRequest('/conmail.php', {
    body: payloadValid1,
    headers: { 'X-Bypass-Rate-Limit': 'test-key-sln' }
  });

  assert(resValid1.status === 200, 'Valid Form 1 returns HTTP 200');
  assert(resValid1.json && resValid1.json.success === true, 'Valid Form 1 returns success: true');
  assert(resValid1.json && resValid1.json.message === EXPECTED_SUCCESS_MSG, 'Valid Form 1 returns exact required success message');

  const testIdCallback = `test_callback_${Date.now()}`;
  const payloadValid2 = toUrlParams({
    csrf_token: CSRF_TOKEN,
    Name: 'Deepa Sharma',
    Fname: 'Kavach Solutions India',
    Subject: 'Head of Compliance',
    Email: `deepa.${Date.now()}@kavach.in`,
    Number: '+91 99887 76655',
    appt: '10:00 AM - 12:00 PM',
    Services: 'soc',
    Message: `Interested in SOC as a Service deployment (${testIdCallback})`
  });

  const resValid2 = await makeRequest('/conmail1.php', {
    body: payloadValid2,
    headers: { 'X-Bypass-Rate-Limit': 'test-key-sln' }
  });

  assert(resValid2.status === 200, 'Valid Form 2 returns HTTP 200');
  assert(resValid2.json && resValid2.json.success === true, 'Valid Form 2 returns success: true');
  assert(resValid2.json && resValid2.json.message === EXPECTED_SUCCESS_MSG, 'Valid Form 2 returns exact required success message');

  // Verify server-side storage in data/enquiries.json and data/enquiries.csv
  const possibleJsonPaths = [
    path.join(__dirname, 'data', 'enquiries.json'),
    path.join(__dirname, 'SLN-Website-Development', 'data', 'enquiries.json')
  ];
  const jsonPath = possibleJsonPaths.find(p => fs.existsSync(p));

  assert(Boolean(jsonPath), `enquiries.json exists in server storage (${jsonPath})`);

  if (jsonPath) {
    const rawData = fs.readFileSync(jsonPath, 'utf8');
    const storedEnquiries = JSON.parse(rawData);
    assert(Array.isArray(storedEnquiries), 'enquiries.json is a valid JSON array');

    const rec1 = storedEnquiries.find(e => e.message && e.message.includes(testIdContact));
    assert(Boolean(rec1), 'Form 1 enquiry successfully recorded in enquiries.json');
    if (rec1) {
      assert(rec1.name === 'Rajesh Kumar', 'Form 1 record preserves Name');
      assert(rec1.organisation === 'Apex Infosec Pvt Ltd', 'Form 1 record preserves Organisation');
      assert(rec1.designation === 'Chief Technology Officer', 'Form 1 record preserves Designation');
      assert(rec1.service === 'VAPT', 'Form 1 record maps Service to "VAPT"');
    }

    const rec2 = storedEnquiries.find(e => e.message && e.message.includes(testIdCallback));
    assert(Boolean(rec2), 'Form 2 enquiry successfully recorded in enquiries.json');
    if (rec2) {
      assert(rec2.name === 'Deepa Sharma', 'Form 2 record preserves Name');
      assert(rec2.right_time_to_call === '10:00 AM - 12:00 PM', 'Form 2 record preserves "Right time to call"');
      assert(rec2.service === 'SOC As A Service', 'Form 2 record maps Service to "SOC As A Service"');
    }
  }

  // -------------------------------------------------------------
  // SUITE 5: Duplicate Submission Handling
  // -------------------------------------------------------------
  console.log('\n--- SUITE 5: Duplicate Submission & Rate Handling ---');

  const dupPayload = toUrlParams({
    csrf_token: CSRF_TOKEN,
    Name: 'Pooja Reddy',
    Fname: 'CyberShield Systems',
    Subject: 'IT Manager',
    Email: 'pooja@cybershield.in',
    Number: '+91 97654 32100',
    Services: 'skilling',
    Message: 'Enquiry for team skilling workshops'
  });

  const firstSub = await makeRequest('/conmail.php', { body: dupPayload, headers: { 'X-Bypass-Rate-Limit': 'test-key-sln' } });
  assert(firstSub.status === 200, 'Initial submission succeeds');

  const dupSub = await makeRequest('/conmail.php', { body: dupPayload });
  assert(dupSub.status === 200 && dupSub.json && dupSub.json.success === true, 'Immediate duplicate submission is safely handled and returns success');

  // -------------------------------------------------------------
  // SUITE 6: Simulated Storage Failure Error Handling
  // -------------------------------------------------------------
  console.log('\n--- SUITE 6: Storage Failure Resilience ---');

  const failPayload = toUrlParams({
    csrf_token: CSRF_TOKEN,
    Name: 'Test Failure',
    Fname: 'Test Corp',
    Subject: 'Tester',
    Email: 'failtest@example.com',
    Number: '+91 9876543210',
    Services: 'soc',
    Message: 'Testing storage failure resilience'
  });

  const failRes = await makeRequest('/conmail.php', {
    body: failPayload,
    headers: {
      'X-Simulate-Storage-Failure': 'true',
      'X-Bypass-Rate-Limit': 'test-key-sln'
    }
  });

  assert(failRes.status === 500 && failRes.json && failRes.json.success === false, 'Storage failure triggers HTTP 500 with helpful error');
  assert(failRes.json && (failRes.json.message.includes('not been confirmed as saved') || failRes.json.message.includes('Unable to submit your enquiry')), 'Storage failure does NOT claim false success');

  // -------------------------------------------------------------
  // Final Results
  // -------------------------------------------------------------
  console.log('\n' + '='.repeat(75));
  console.log(` SUMMARY: Total Tests: ${totalTests} | Passed: ${passedTests} | Failed: ${failedTests}`);
  console.log('='.repeat(75) + '\n');

  if (failedTests > 0) {
    process.exit(1);
  } else {
    process.exit(0);
  }
}

runSuite().catch(err => {
  console.error('Fatal suite error:', err);
  process.exit(1);
});
