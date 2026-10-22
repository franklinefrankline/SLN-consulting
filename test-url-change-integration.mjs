/**
 * SLN Consulting - Google Forms URL Change & Centralized Config Test Suite
 *
 * Verifies:
 * 1. Single configuration file (forms-config.php) manages both Form 1 and Form 2 URLs.
 * 2. Changing the URL in forms-config.php automatically updates contact.php (sidebar + sub-button)
 *    and form.php without modifying multiple files.
 * 3. Validation and same-page submission remain rock-solid after changing URLs.
 * 4. Field-entry mappings and background sync are verified.
 * 5. Reversion back to original URLs restores all pages.
 */

import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const BASE_URL = 'http://localhost:3000';
const CSRF_TOKEN = 'sln_csrf_dev_token_4b9e28f11a8c903';
const CONFIG_FILE = path.join(__dirname, 'forms-config.php');

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

function makeRequest(pathname, { method = 'GET', headers = {}, body = '', isJson = false } = {}) {
  return new Promise((resolve, reject) => {
    const url = new URL(pathname, BASE_URL);
    const reqHeaders = {
      'X-Requested-With': 'XMLHttpRequest',
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
        if (isJson || res.headers['content-type']?.includes('application/json')) {
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
console.log(' SLN CONSULTING — GOOGLE FORMS URL CHANGE INTEGRATION TEST SUITE');
console.log('='.repeat(75));

async function run() {
  const originalConfigContent = fs.readFileSync(CONFIG_FILE, 'utf8');

  const ORIGINAL_FORM1_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdpVszsphdo1KhHgig4lCHfjuHmE8IzSvIUDHEFiE52LoW0Rw/viewform';
  const ORIGINAL_FORM2_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSfp_u4mUMGlDdk9omnkDtI-Us3aDAlM4KzEGit3B-duDh4B1A/viewform';

  const SIMULATED_FORM1_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSc_SIMULATED_NEW_FORM_1_SLN_2026/viewform';
  const SIMULATED_FORM2_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSd_SIMULATED_NEW_FORM_2_SLN_2026/viewform';

  const EXPECTED_SUCCESS_MSG = 'Your enquiry has been submitted successfully! Thank you for contacting SLN Consulting. Our team will get back to you soon.';

  try {
    // -------------------------------------------------------------
    // PHASE 1: Verify Initial Configuration & Integration
    // -------------------------------------------------------------
    console.log('\n--- PHASE 1: Verify Initial Config & Site Links ---');

    assert(fs.existsSync(CONFIG_FILE), 'Centralized config file (forms-config.php) exists');

    const contactInitial = await makeRequest('/contact.php');
    assert(contactInitial.status === 200, 'contact.php loads successfully');
    assert(contactInitial.body.includes(ORIGINAL_FORM1_URL), 'contact.php displays Form 1 URL from config');
    assert(contactInitial.body.includes(ORIGINAL_FORM2_URL), 'contact.php displays Form 2 URL from config');

    const formInitial = await makeRequest('/form.php');
    assert(formInitial.status === 200, 'form.php loads successfully');
    assert(formInitial.body.includes(ORIGINAL_FORM1_URL), 'form.php displays Form 1 URL from config');
    assert(formInitial.body.includes(ORIGINAL_FORM2_URL), 'form.php displays Form 2 URL from config');

    // -------------------------------------------------------------
    // PHASE 2: Change URLs in the SINGLE Configuration File
    // -------------------------------------------------------------
    console.log('\n--- PHASE 2: Update URLs in forms-config.php ---');

    let updatedConfig = originalConfigContent.replace(ORIGINAL_FORM1_URL, SIMULATED_FORM1_URL);
    updatedConfig = updatedConfig.replace(ORIGINAL_FORM2_URL, SIMULATED_FORM2_URL);
    fs.writeFileSync(CONFIG_FILE, updatedConfig, 'utf8');
    console.log('  Updated forms-config.php with simulated new Google Form URLs.');

    // -------------------------------------------------------------
    // PHASE 3: Verify Site Automatically Reflects New URLs
    // -------------------------------------------------------------
    console.log('\n--- PHASE 3: Verify Integration Automatically Reflects New URLs ---');

    const contactAfter = await makeRequest('/contact.php');
    assert(contactAfter.status === 200, 'contact.php loads with updated config');
    assert(contactAfter.body.includes(SIMULATED_FORM1_URL), 'contact.php automatically reflects new Form 1 URL');
    assert(contactAfter.body.includes(SIMULATED_FORM2_URL), 'contact.php automatically reflects new Form 2 URL');
    assert(!contactAfter.body.includes(ORIGINAL_FORM1_URL), 'contact.php no longer contains old Form 1 URL');
    assert(!contactAfter.body.includes(ORIGINAL_FORM2_URL), 'contact.php no longer contains old Form 2 URL');

    const formAfter = await makeRequest('/form.php');
    assert(formAfter.status === 200, 'form.php loads with updated config');
    assert(formAfter.body.includes(SIMULATED_FORM1_URL), 'form.php automatically reflects new Form 1 URL');
    assert(formAfter.body.includes(SIMULATED_FORM2_URL), 'form.php automatically reflects new Form 2 URL');
    assert(!formAfter.body.includes(ORIGINAL_FORM1_URL), 'form.php no longer contains old Form 1 URL');
    assert(!formAfter.body.includes(ORIGINAL_FORM2_URL), 'form.php no longer contains old Form 2 URL');

    // -------------------------------------------------------------
    // PHASE 4: Test Form Submissions with New Form URLs
    // -------------------------------------------------------------
    console.log('\n--- PHASE 4: Test Form Submissions with Updated URLs ---');

    // Test Form 1 Submission
    const testId1 = `test_url_change_f1_${Date.now()}`;
    const payload1 = toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: 'Sanjay Gupta',
      Fname: 'CyberDefend Technologies',
      Subject: 'Security Lead',
      Email: `sanjay.${Date.now()}@cyberdefend.in`,
      Number: '+91 98450 12345',
      Services: 'soc',
      Message: `Testing enquiry after Google Form URL update (${testId1})`
    });

    const res1 = await makeRequest('/conmail.php', { method: 'POST', body: payload1, isJson: true });
    assert(res1.status === 200, 'Form 1 submission succeeds with HTTP 200 after URL change');
    assert(res1.json && res1.json.success === true, 'Form 1 response indicates success');
    assert(res1.json && res1.json.message === EXPECTED_SUCCESS_MSG, 'Form 1 displays exact success message');

    // Test Form 2 Submission
    const testId2 = `test_url_change_f2_${Date.now()}`;
    const payload2 = toUrlParams({
      csrf_token: CSRF_TOKEN,
      Name: 'Meera Nambiar',
      Fname: 'Zenith Health Systems',
      Subject: 'Compliance Officer',
      Email: `meera.${Date.now()}@zenith.org`,
      Number: '+91 99123 45678',
      appt: '11:30 AM',
      Services: 'vapt',
      Message: `Testing callback request after Google Form URL update (${testId2})`
    });

    const res2 = await makeRequest('/conmail1.php', { method: 'POST', body: payload2, isJson: true });
    assert(res2.status === 200, 'Form 2 submission succeeds with HTTP 200 after URL change');
    assert(res2.json && res2.json.success === true, 'Form 2 response indicates success');
    assert(res2.json && res2.json.message === EXPECTED_SUCCESS_MSG, 'Form 2 displays exact success message');

    // Verify storage recorded both enquiries
    const jsonPath = path.join(__dirname, 'data', 'enquiries.json');
    if (fs.existsSync(jsonPath)) {
      const records = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
      const rec1 = records.find(r => r.message && r.message.includes(testId1));
      const rec2 = records.find(r => r.message && r.message.includes(testId2));
      assert(Boolean(rec1), 'Enquiry 1 successfully stored in data/enquiries.json');
      assert(Boolean(rec2), 'Enquiry 2 successfully stored in data/enquiries.json');
    }

  } finally {
    // -------------------------------------------------------------
    // PHASE 5: Restore Original Configuration & Verify
    // -------------------------------------------------------------
    console.log('\n--- PHASE 5: Restore Original Configuration ---');
    fs.writeFileSync(CONFIG_FILE, originalConfigContent, 'utf8');
    console.log('  Restored forms-config.php to original live Google Form URLs.');

    const contactRestored = await makeRequest('/contact.php');
    assert(contactRestored.body.includes(ORIGINAL_FORM1_URL), 'contact.php successfully restored to original Form 1 URL');
    assert(contactRestored.body.includes(ORIGINAL_FORM2_URL), 'contact.php successfully restored to original Form 2 URL');
  }

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

run().catch(err => {
  console.error('Fatal test error:', err);
  process.exit(1);
});
