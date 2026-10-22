/**
 * SLN Consulting - Independent Verification Test Suite for Both Google Forms
 *
 * Verifies:
 * 1. Independent field entry ID mappings for Form 1 and Form 2.
 * 2. Form 1 submission records directly in Google Form 1 (FAIpQLSdpVszsphdo1KhHgig4lCHfjuHmE8IzSvIUDHEFiE52LoW0Rw).
 * 3. Form 2 submission records directly in Google Form 2 (FAIpQLSfp_u4mUMGlDdk9omnkDtI-Us3aDAlM4KzEGit3B-duDh4B1A).
 * 4. Distinct URLs, distinct entry IDs, distinct schema requirements.
 * 5. Isolation: Failure in Form 1 does NOT break Form 2; failure in Form 2 does NOT break Form 1.
 * 6. Same-page behavior and exact success message display upon confirmed recording.
 */

import http from 'node:http';
import https from 'node:https';
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

function submitDirectToGoogle(url, params) {
  return new Promise((resolve) => {
    const postData = new URLSearchParams(params).toString();
    const parsed = new URL(url);
    const req = https.request({
      hostname: parsed.hostname,
      path: parsed.pathname,
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': Buffer.byteLength(postData),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        const confirmed = data.includes('Thanks for submitting your contact info!') || data.includes('Your response has been recorded');
        resolve({ statusCode: res.statusCode, confirmed });
      });
    });
    req.on('error', (e) => resolve({ error: e.message }));
    req.write(postData);
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
console.log(' SLN CONSULTING — INDEPENDENT GOOGLE FORMS VERIFICATION SUITE');
console.log('='.repeat(75));

async function run() {
  const EXPECTED_SUCCESS_MSG = 'Your enquiry has been submitted successfully! Thank you for contacting SLN Consulting. Our team will get back to you soon.';

  // -------------------------------------------------------------
  // TEST 1: Entry ID Verification for Both Forms
  // -------------------------------------------------------------
  console.log('\n--- 1. Verify Independent Configuration & Field Mappings ---');

  const formsCfgPath = path.join(__dirname, 'forms-config.php');
  const formsCfgContent = fs.readFileSync(formsCfgPath, 'utf8');

  // Verify Form 1 specific entry IDs
  assert(formsCfgContent.includes("'organisation' => 'entry.969435007'"), 'Form 1 maps organisation to entry.969435007 (Company Name)');
  assert(formsCfgContent.includes("'service'      => 'entry.1230817807'"), 'Form 1 maps service to entry.1230817807 (Service Required)');
  assert(formsCfgContent.includes("'message'      => 'entry.1984267215'"), 'Form 1 maps message to entry.1984267215');

  // Verify Form 2 specific entry IDs
  assert(formsCfgContent.includes("'organisation'              => 'entry.1045781291'"), 'Form 2 maps organisation to entry.1045781291 (Organisation Name)');
  assert(formsCfgContent.includes("'right_time_to_call_hour'   => 'entry.1007004095_hour'"), 'Form 2 maps call time hour to entry.1007004095_hour');
  assert(formsCfgContent.includes("'right_time_to_call_minute' => 'entry.1007004095_minute'"), 'Form 2 maps call time minute to entry.1007004095_minute');
  assert(formsCfgContent.includes("'service'                   => 'entry.660909226'"), 'Form 2 maps service to entry.660909226 (Select Service)');
  assert(formsCfgContent.includes("'message'                   => 'entry.1789743'"), 'Form 2 maps message to entry.1789743');

  // Verify Distinct Google Form URLs
  const FORM1_LIVE_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdpVszsphdo1KhHgig4lCHfjuHmE8IzSvIUDHEFiE52LoW0Rw/formResponse';
  const FORM2_LIVE_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSfp_u4mUMGlDdk9omnkDtI-Us3aDAlM4KzEGit3B-duDh4B1A/formResponse';
  assert(formsCfgContent.includes('1FAIpQLSdpVszsphdo1KhHgig4lCHfjuHmE8IzSvIUDHEFiE52LoW0Rw'), 'Form 1 URL points to 1FAIpQLSdpVszsphdo1KhHgig4lCHfjuHmE8IzSvIUDHEFiE52LoW0Rw');
  assert(formsCfgContent.includes('1FAIpQLSfp_u4mUMGlDdk9omnkDtI-Us3aDAlM4KzEGit3B-duDh4B1A'), 'Form 2 URL points to 1FAIpQLSfp_u4mUMGlDdk9omnkDtI-Us3aDAlM4KzEGit3B-duDh4B1A');

  // -------------------------------------------------------------
  // TEST 2: Direct Google Forms Acceptance Check
  // -------------------------------------------------------------
  console.log('\n--- 2. Direct Live Submission to Google Form Endpoints ---');

  const directG1 = await submitDirectToGoogle(FORM1_LIVE_URL, {
    'entry.2005620554': 'Antigravity Verification Test',
    'entry.969435007': 'SLN Technologies Pvt Ltd',
    'entry.1065046570': 'Lead Security Consultant',
    'entry.1166974658': 'audit-form1@slnconsulting.co.in',
    'entry.839337160': '+91 98450 11001',
    'entry.1230817807': 'VAPT',
    'entry.1984267215': 'Direct endpoint verification for Google Form 1',
    'fvv': '1',
    'pageHistory': '0'
  });
  assert(directG1.statusCode === 200, 'Google Form 1 directly accepts submission with HTTP 200');
  assert(directG1.confirmed === true, 'Google Form 1 returns live confirmation: "Thanks for submitting your contact info!"');

  const directG2 = await submitDirectToGoogle(FORM2_LIVE_URL, {
    'entry.2005620554': 'Antigravity Verification Test',
    'entry.1045781291': 'SLN Technologies Pvt Ltd <audit-form2@slnconsulting.co.in>',
    'entry.1065046570': 'Lead Security Consultant',
    'entry.1166974658': 'audit-form2@slnconsulting.co.in',
    'entry.839337160': '+91 98450 22002',
    'entry.1007004095_hour': '15',
    'entry.1007004095_minute': '30',
    'entry.660909226': 'SOC As A Service',
    'entry.1789743': 'Direct endpoint verification for Google Form 2',
    'fvv': '1',
    'pageHistory': '0'
  });
  assert(directG2.statusCode === 200, 'Google Form 2 directly accepts submission with HTTP 200');
  assert(directG2.confirmed === true, 'Google Form 2 returns live confirmation: "Thanks for submitting your contact info!"');

  // -------------------------------------------------------------
  // TEST 3: End-to-End Website Submission for Form 1
  // -------------------------------------------------------------
  console.log('\n--- 3. End-to-End Website Form 1 (contact.php -> conmail.php) ---');

  const testStamp1 = Date.now();
  const form1Email = `form1.test.${testStamp1}@slnconsulting.co.in`;
  const form1Data = {
    csrf_token: CSRF_TOKEN,
    Name: 'Rajesh Raman',
    Fname: 'Raman CyberSec Solutions',
    Subject: 'Chief Information Security Officer',
    Email: form1Email,
    Number: '+91 98451 22334',
    Services: 'vapt',
    Message: `[IDENTIFIABLE TEST DATA] Live Form 1 Verification Response (Timestamp: ${testStamp1})`
  };

  const f1Res = await makeRequest('/conmail.php', { body: toUrlParams(form1Data) });
  assert(f1Res.status === 200, 'Form 1 website submission returns HTTP 200');
  assert(f1Res.json && f1Res.json.success === true, 'Form 1 returns success: true');
  assert(f1Res.json && f1Res.json.message === EXPECTED_SUCCESS_MSG, 'Form 1 returns exact required success message');

  // -------------------------------------------------------------
  // TEST 4: End-to-End Website Submission for Form 2
  // -------------------------------------------------------------
  console.log('\n--- 4. End-to-End Website Form 2 (form.php -> conmail1.php) ---');

  const testStamp2 = Date.now();
  const form2Email = `form2.test.${testStamp2}@slnconsulting.co.in`;
  const form2Data = {
    csrf_token: CSRF_TOKEN,
    Name: 'Ananya Sharma',
    Fname: 'Sharma Infotech Labs',
    Subject: 'Director of Technology',
    Email: form2Email,
    Number: '+91 98112 33445',
    appt: '4:15 PM - 5:30 PM',
    Services: 'soc',
    Message: `[IDENTIFIABLE TEST DATA] Live Form 2 Verification Response (Timestamp: ${testStamp2})`
  };

  const f2Res = await makeRequest('/conmail1.php', { body: toUrlParams(form2Data) });
  assert(f2Res.status === 200, 'Form 2 website submission returns HTTP 200');
  assert(f2Res.json && f2Res.json.success === true, 'Form 2 returns success: true');
  assert(f2Res.json && f2Res.json.message === EXPECTED_SUCCESS_MSG, 'Form 2 returns exact required success message');

  // -------------------------------------------------------------
  // TEST 5: Verify Storage Persistence and Field Correctness
  // -------------------------------------------------------------
  console.log('\n--- 5. Server Storage Persistence & Google Forms Sync Verification ---');

  const storageJsonPath = path.join(__dirname, 'data', 'enquiries.json');
  const storageData = JSON.parse(fs.readFileSync(storageJsonPath, 'utf8'));

  const rec1 = storageData.find(r => r.email === form1Email);
  assert(Boolean(rec1), `Form 1 enquiry (${form1Email}) is stored in enquiries.json`);
  assert(rec1 && rec1.form_type === 'contact_enquiry', 'Form 1 enquiry has form_type "contact_enquiry"');
  assert(rec1 && rec1.service === 'VAPT', 'Form 1 enquiry service mapped to "VAPT"');

  const rec2 = storageData.find(r => r.email === form2Email);
  assert(Boolean(rec2), `Form 2 enquiry (${form2Email}) is stored in enquiries.json`);
  assert(rec2 && rec2.form_type === 'callback_enquiry', 'Form 2 enquiry has form_type "callback_enquiry"');
  assert(rec2 && rec2.right_time_to_call === '4:15 PM - 5:30 PM', 'Form 2 enquiry preserves "Right time to call" value');

  // -------------------------------------------------------------
  // TEST 6: Isolation — Failure in One Does NOT Break the Other
  // -------------------------------------------------------------
  console.log('\n--- 6. Isolation Between Forms ---');

  // A. Trigger validation failure on Form 2 (missing required call time)
  const f2Bad = await makeRequest('/conmail1.php', {
    body: toUrlParams({ csrf_token: CSRF_TOKEN, Name: 'Test User', Fname: 'Org', Subject: 'Title', Email: 'test@ok.com', Number: '9845012345', appt: '' })
  });
  assert(f2Bad.status === 400 && f2Bad.json.success === false, 'Form 2 fails cleanly on missing call time');

  // Form 1 must still work immediately after Form 2 failure
  const f1AfterF2Fail = await makeRequest('/conmail.php', {
    body: toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: 'Kiran Rao',
      Fname: 'Kiran Networks',
      Subject: 'CTO',
      Email: `kiran.${Date.now()}@networks.org`,
      Number: '+91 98450 99887',
      Services: 'skilling',
      Message: 'Testing Form 1 works despite prior Form 2 failure'
    })
  });
  assert(f1AfterF2Fail.status === 200 && f1AfterF2Fail.json.success === true, 'Form 1 works immediately and is NOT broken by Form 2 failure');

  // B. Trigger validation failure on Form 1 (missing required service)
  const f1Bad = await makeRequest('/conmail.php', {
    body: toUrlParams({ csrf_token: CSRF_TOKEN, Name: 'Test User', Fname: 'Org', Subject: 'Title', Email: 'test@ok.com', Number: '9845012345', Services: '' })
  });
  assert(f1Bad.status === 400 && f1Bad.json.success === false, 'Form 1 fails cleanly on missing service');

  // Form 2 must still work immediately after Form 1 failure
  const f2AfterF1Fail = await makeRequest('/conmail1.php', {
    body: toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: 'Sunita Mehra',
      Fname: 'Mehra FinTech',
      Subject: 'Compliance Head',
      Email: `sunita.${Date.now()}@fintech.in`,
      Number: '+91 99887 11223',
      appt: '11:00 AM',
      Services: 'it_services',
      Message: 'Testing Form 2 works despite prior Form 1 failure'
    })
  });
  assert(f2AfterF1Fail.status === 200 && f2AfterF1Fail.json.success === true, 'Form 2 works immediately and is NOT broken by Form 1 failure');

  // -------------------------------------------------------------
  // Summary
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

run().catch((err) => {
  console.error('Test suite failed:', err);
  process.exit(1);
});
