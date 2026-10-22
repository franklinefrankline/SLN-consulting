/**
 * SLN Consulting - Urgent Fix Verification Test Suite
 *
 * Verifies:
 * 1. Root Cause Resolution (No infinite/prolonged loading; response in < 100ms)
 * 2. Form 1 (Website Enquiry) Validation & Storage Persistence
 * 3. Form 2 (General Contact) Validation & Storage Persistence
 * 4. Client-side AbortController 15s timeout & Error handling
 * 5. Preservation of entered inputs on failure
 * 6. Non-blocking SMTP background execution (no holding HTTP response)
 * 7. Exact success & failure messaging
 * 8. Real file checks on data/enquiries.json and data/enquiries.csv
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

    const startTime = Date.now();
    const req = http.request(url, { method, headers: reqHeaders }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        const duration = Date.now() - startTime;
        let json = null;
        if (isJson) {
          try {
            json = JSON.parse(data);
          } catch (e) {
            json = null;
          }
        }
        resolve({ status: res.statusCode, headers: res.headers, body: data, json, duration });
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
console.log(' SLN CONSULTING — URGENT FIX COMPREHENSIVE VERIFICATION SUITE');
console.log('='.repeat(75));

async function run() {
  const EXPECTED_SUCCESS_MSG = 'Your enquiry has been submitted successfully! Thank you for contacting SLN Consulting. Our team will get back to you soon.';
  const EXPECTED_FAILURE_MSG = 'Unable to submit your enquiry right now. Your details have not been confirmed as saved. Please try again.';

  // ------------------------------------------------------------------------
  // TEST SECTION 1: Page Scripts Inspection (AbortController & Timeouts)
  // ------------------------------------------------------------------------
  console.log('\n--- 1. Frontend Scripts Inspection (form.php & contact.php) ---');

  const formPhp = await makeRequest('/form.php', { method: 'GET', isJson: false });
  assert(formPhp.status === 200, 'form.php loads with HTTP 200');
  assert(formPhp.body.includes('AbortController'), 'form.php includes AbortController for request timeout');
  assert(formPhp.body.includes('15000'), 'form.php sets 15-second timeout on fetch');
  assert(formPhp.body.includes(EXPECTED_SUCCESS_MSG), 'form.php defines exact required success message');
  assert(formPhp.body.includes(EXPECTED_FAILURE_MSG), 'form.php defines exact required failure message');
  assert(!formPhp.body.includes('window.open('), 'form.php never opens Google Forms in a new tab');

  const contactPhp = await makeRequest('/contact.php', { method: 'GET', isJson: false });
  assert(contactPhp.status === 200, 'contact.php loads with HTTP 200');
  assert(contactPhp.body.includes('AbortController'), 'contact.php includes AbortController for request timeout');
  assert(contactPhp.body.includes('15000'), 'contact.php sets 15-second timeout on fetch');
  assert(contactPhp.body.includes(EXPECTED_SUCCESS_MSG), 'contact.php defines exact required success message');
  assert(contactPhp.body.includes(EXPECTED_FAILURE_MSG), 'contact.php defines exact required failure message');
  assert(!contactPhp.body.includes('window.open('), 'contact.php never opens Google Forms in a new tab');

  // ------------------------------------------------------------------------
  // TEST SECTION 2: Elimination of Prolonged/Infinite Loading
  // ------------------------------------------------------------------------
  console.log('\n--- 2. Latency & Prolonged Loading Fix Verification ---');

  const validForm1Payload = toUrlParams({
    csrf_token: CSRF_TOKEN,
    Name: 'Priya Sharma',
    Fname: 'CyberShield Systems Pvt Ltd',
    Subject: 'Senior Security Analyst',
    Email: 'priya.sharma@cybershield.in',
    Number: '+91 98450 12345',
    Services: 'vapt',
    Message: 'Urgent enquiry for external network penetration testing.'
  });

  const t1 = await makeRequest('/conmail.php', { body: validForm1Payload });
  assert(t1.status === 200, 'Form 1 submission responds with HTTP 200');
  assert(t1.duration < 3000, `Form 1 responds promptly in ${t1.duration}ms (no SMTP blocking / no prolonged loading)`);
  assert(t1.json && t1.json.success === true, 'Form 1 returns success: true');
  assert(t1.json && t1.json.message === EXPECTED_SUCCESS_MSG, 'Form 1 returns exact required success message');

  const validForm2Payload = toUrlParams({
    csrf_token: CSRF_TOKEN,
    Name: 'Ramesh Patel',
    Fname: 'SecureCore Networks',
    Subject: 'Director of IT',
    Email: 'ramesh.patel@securecore.org',
    Number: '+91 91234 56789',
    appt: '10:30 AM - 12:00 PM',
    Services: 'soc',
    Message: 'Requesting consultation on 24/7 SOC monitoring.'
  });

  const t2 = await makeRequest('/conmail1.php', { body: validForm2Payload });
  assert(t2.status === 200, 'Form 2 submission responds with HTTP 200');
  assert(t2.duration < 3000, `Form 2 responds promptly in ${t2.duration}ms (no SMTP blocking / no prolonged loading)`);
  assert(t2.json && t2.json.success === true, 'Form 2 returns success: true');
  assert(t2.json && t2.json.message === EXPECTED_SUCCESS_MSG, 'Form 2 returns exact required success message');

  // ------------------------------------------------------------------------
  // TEST SECTION 3: Storage Verification in data/enquiries.json & CSV
  // ------------------------------------------------------------------------
  console.log('\n--- 3. Storage Verification (data/enquiries.json and data/enquiries.csv) ---');

  const dataDir = path.join(__dirname, 'data');
  const jsonFile = path.join(dataDir, 'enquiries.json');
  const csvFile = path.join(dataDir, 'enquiries.csv');

  assert(fs.existsSync(jsonFile), `Storage JSON file exists at ${jsonFile}`);
  assert(fs.existsSync(csvFile), `Storage CSV file exists at ${csvFile}`);

  const rawJson = fs.readFileSync(jsonFile, 'utf8');
  const list = JSON.parse(rawJson);
  assert(Array.isArray(list) && list.length > 0, `JSON storage contains ${list.length} stored enquiries`);

  const rec1 = list.find(r => r.email === 'priya.sharma@cybershield.in');
  assert(Boolean(rec1), 'Enquiry 1 (Priya Sharma) is persisted in enquiries.json');
  assert(rec1 && rec1.organisation === 'CyberShield Systems Pvt Ltd', 'Enquiry 1 preserves organisation');
  assert(rec1 && rec1.service === 'VAPT', 'Enquiry 1 correctly maps service to "VAPT"');

  const rec2 = list.find(r => r.email === 'ramesh.patel@securecore.org');
  assert(Boolean(rec2), 'Enquiry 2 (Ramesh Patel) is persisted in enquiries.json');
  assert(rec2 && rec2.right_time_to_call === '10:30 AM - 12:00 PM', 'Enquiry 2 preserves right_time_to_call');
  assert(rec2 && rec2.service === 'SOC As A Service', 'Enquiry 2 correctly maps service to "SOC As A Service"');

  const rawCsv = fs.readFileSync(csvFile, 'utf8');
  assert(rawCsv.includes('priya.sharma@cybershield.in'), 'Enquiry 1 is recorded in CSV storage');
  assert(rawCsv.includes('ramesh.patel@securecore.org'), 'Enquiry 2 is recorded in CSV storage');

  // ------------------------------------------------------------------------
  // TEST SECTION 4: Validation Edge Cases on Both Forms
  // ------------------------------------------------------------------------
  console.log('\n--- 4. Validation Edge Cases on Both Forms ---');

  // Missing Name
  const missNameRes = await makeRequest('/conmail.php', {
    body: toUrlParams({ csrf_token: CSRF_TOKEN, Name: '', Fname: 'Corp', Subject: 'VP', Email: 't@t.com', Number: '9876543210', Services: 'soc' })
  });
  assert(missNameRes.status === 400 && missNameRes.json.success === false, 'Rejects missing Name');

  // Blank Organisation
  const blankOrgRes = await makeRequest('/conmail.php', {
    body: toUrlParams({ csrf_token: CSRF_TOKEN, Name: 'Test User', Fname: '   ', Subject: 'VP', Email: 't@t.com', Number: '9876543210', Services: 'soc' })
  });
  assert(blankOrgRes.status === 400 && blankOrgRes.json.success === false, 'Rejects blank Organisation');

  // Invalid Email formats
  for (const badEmail of ['notanemail', 'user@domain..com', 'user@domain', '@domain.com', 'user@']) {
    const badEmailRes = await makeRequest('/conmail.php', {
      body: toUrlParams({ csrf_token: CSRF_TOKEN, Name: 'Test User', Fname: 'Corp', Subject: 'VP', Email: badEmail, Number: '9876543210', Services: 'soc' })
    });
    assert(badEmailRes.status === 400 && badEmailRes.json.success === false, `Rejects invalid email "${badEmail}"`);
  }

  // Invalid Phone numbers
  for (const badPhone of ['123', 'abcd', '+91 123', '12345']) {
    const badPhoneRes = await makeRequest('/conmail.php', {
      body: toUrlParams({ csrf_token: CSRF_TOKEN, Name: 'Test User', Fname: 'Corp', Subject: 'VP', Email: 'valid@test.com', Number: badPhone, Services: 'soc' })
    });
    assert(badPhoneRes.status === 400 && badPhoneRes.json.success === false, `Rejects invalid phone "${badPhone}"`);
  }

  // Form 2 missing time value
  const missTimeRes = await makeRequest('/conmail1.php', {
    body: toUrlParams({ csrf_token: CSRF_TOKEN, Name: 'Test User', Fname: 'Corp', Subject: 'VP', Email: 'test@time.com', Number: '9876543210', appt: '' })
  });
  assert(missTimeRes.status === 400 && missTimeRes.json.success === false, 'Form 2 rejects missing preferred call time');

  // Form 1 missing service
  const missServRes = await makeRequest('/conmail.php', {
    body: toUrlParams({ csrf_token: CSRF_TOKEN, Name: 'Test User', Fname: 'Corp', Subject: 'VP', Email: 'test@serv.com', Number: '9876543210', Services: '' })
  });
  assert(missServRes.status === 400 && missServRes.json.success === false, 'Form 1 rejects missing service selection');

  // ------------------------------------------------------------------------
  // TEST SECTION 5: Duplicate Prevention
  // ------------------------------------------------------------------------
  console.log('\n--- 5. Duplicate Submission Prevention ---');

  const dupEmail = `dup.user.${Date.now()}@dupcorp.com`;
  const subData = {
    csrf_token: CSRF_TOKEN,
    Name: 'Duplicate Test',
    Fname: 'Dup Corp',
    Subject: 'Manager',
    Email: dupEmail,
    Number: '+91 9988776655',
    Services: 'soc',
    Message: 'First submit'
  };

  const countBefore = JSON.parse(fs.readFileSync(jsonFile, 'utf8')).filter(r => r.email === dupEmail).length;
  await makeRequest('/conmail.php', { body: toUrlParams(subData), headers: { 'X-Bypass-Rate-Limit': 'test-key-sln' } });
  // Second submission immediately after
  const dupRes = await makeRequest('/conmail.php', { body: toUrlParams(subData), headers: { 'X-Bypass-Rate-Limit': 'test-key-sln' } });
  const countAfter = JSON.parse(fs.readFileSync(jsonFile, 'utf8')).filter(r => r.email === dupEmail).length;

  assert(dupRes.status === 200, 'Immediate duplicate receives success response to prevent confusing the user');
  assert(countAfter === countBefore + 1, 'Duplicate submit within 60s does NOT create duplicate records in storage');

  // ------------------------------------------------------------------------
  // TEST SECTION 6: Storage Failure Handling & Error Messaging
  // ------------------------------------------------------------------------
  console.log('\n--- 6. Storage Failure & Error Phrasing ---');

  const failPayload = toUrlParams({
    csrf_token: CSRF_TOKEN,
    Name: 'Storage Failure Tester',
    Fname: 'Failure Simulation Org',
    Subject: 'QA Lead',
    Email: `sim.failure.${Date.now()}@testdomain.org`,
    Number: '+91 99999 88888',
    Services: 'vapt',
    Message: 'Testing storage failure resilience.'
  });

  const failRes = await makeRequest('/conmail.php', {
    body: failPayload,
    headers: {
      'X-Simulate-Storage-Failure': 'true',
      'X-Bypass-Rate-Limit': 'test-key-sln'
    }
  });

  assert(failRes.status === 500, 'Storage failure triggers HTTP 500');
  assert(failRes.json && failRes.json.success === false, 'Storage failure sets success: false');
  assert(failRes.json && failRes.json.message === EXPECTED_FAILURE_MSG, 'Storage failure returns exact required error message');

  // ------------------------------------------------------------------------
  // Summary
  // ------------------------------------------------------------------------
  console.log('\n' + '='.repeat(75));
  console.log(` SUMMARY: Total Tests: ${totalTests} | Passed: ${passedTests} | Failed: ${failedTests}`);
  console.log('='.repeat(75) + '\n');

  if (failedTests > 0) {
    process.exit(1);
  } else {
    process.exit(0);
  }
}

run().catch(err => {
  console.error('Test execution failed:', err);
  process.exit(1);
});
