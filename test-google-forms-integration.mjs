import http from 'node:http';
import https from 'node:https';

function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    const client = url.startsWith('https:') ? https : http;
    client.get(url, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        const redirectUrl = new URL(res.headers.location, url).toString();
        return fetchUrl(redirectUrl).then(resolve).catch(reject);
      }
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve({ statusCode: res.statusCode, body: data, headers: res.headers }));
    }).on('error', reject);
  });
}

async function verifyGoogleFormsIntegration() {
  console.log('===============================================================');
  console.log('SLN Consulting - Google Forms Integration Automated Test Suite');
  console.log('===============================================================\n');

  let passed = 0;
  let failed = 0;

  function assert(condition, message) {
    if (condition) {
      console.log(`[PASS] ${message}`);
      passed++;
    } else {
      console.error(`[FAIL] ${message}`);
      failed++;
    }
  }

  // 1. Check form.php endpoint
  console.log('--- 1. Testing form.php Structure & Order ---');
  const formRes = await fetchUrl('http://localhost:3000/form.php');
  assert(formRes.statusCode === 200, 'form.php responds with HTTP 200');

  // Verify fields in exact order
  const fields = [
    { name: 'Name', label: 'Name *' },
    { name: 'Fname', label: 'Organisation Name *' },
    { name: 'Subject', label: 'Designation *' },
    { name: 'Email', label: 'Email *' },
    { name: 'Number', label: 'Phone *' },
    { name: 'appt', label: 'Right time to call' },
    { name: 'Services', label: 'Select Service (Optional)' },
    { name: 'Message', label: 'Please describe your requirements' }
  ];

  let lastIndex = -1;
  let orderCorrect = true;
  for (const f of fields) {
    const idx = formRes.body.indexOf(`name="${f.name}"`);
    if (idx === -1) {
      assert(false, `Field "${f.name}" (${f.label}) exists in form.php`);
      orderCorrect = false;
    } else if (idx < lastIndex) {
      assert(false, `Field "${f.name}" is out of order (pos ${idx} < last ${lastIndex})`);
      orderCorrect = false;
    }
    lastIndex = idx;
  }
  assert(orderCorrect, 'All 8 fields preserved in exact requested order');

  // Verify Form 1 URL & Form 2 URL in form.php
  const form1Url = 'https://docs.google.com/forms/d/e/1FAIpQLSdpVszsphdo1KhHgig4lCHfjuHmE8IzSvIUDHEFiE52LoW0Rw/viewform';
  const form2Url = 'https://docs.google.com/forms/d/e/1FAIpQLSfp_u4mUMGlDdk9omnkDtI-Us3aDAlM4KzEGit3B-duDh4B1A/viewform';

  assert(formRes.body.includes(form1Url), 'Form 1 published URL present in form.php');
  assert(formRes.body.includes(form2Url), 'Form 2 published URL present in form.php');
  assert(formRes.body.includes('General Contact Form'), '"General Contact Form" link text present in form.php');
  assert(formRes.body.includes('Website Enquiry Form'), '"Website Enquiry Form" link text present in form.php');
  assert(formRes.body.includes('target="_blank"'), 'Google Forms links open in a new tab (target="_blank")');
  assert(formRes.body.includes('rel="noopener noreferrer"'), 'Google Forms links include rel="noopener noreferrer"');

  // Check verified Google Form entry IDs
  const entryIds = [
    'entry.2005620554', // Name
    'entry.969435007',  // Organisation Name
    'entry.1065046570', // Designation
    'entry.1166974658', // Email
    'entry.839337160',  // Phone
    'entry.1230817807', // Service Required
    'entry.1984267215'  // Message
  ];
  let allEntriesPresent = true;
  for (const id of entryIds) {
    if (!formRes.body.includes(id)) {
      assert(false, `Entry ID ${id} present in form.php prefill handler`);
      allEntriesPresent = false;
    }
  }
  assert(allEntriesPresent, 'All 7 verified Google Form 1 entry IDs present in JavaScript');

  // 2. Check contact.php
  console.log('\n--- 2. Testing contact.php Structure & Link ---');
  const contactRes = await fetchUrl('http://localhost:3000/contact.php');
  assert(contactRes.statusCode === 200, 'contact.php responds with HTTP 200');
  assert(contactRes.body.includes(form2Url), 'Form 2 published URL present in contact.php');
  assert(contactRes.body.includes('General Contact Form'), '"General Contact Form" clearly labelled in contact.php');

  // 3. Live Google Forms Connectivity
  console.log('\n--- 3. Testing Published Google Forms Accessibility ---');
  const g1Res = await fetchUrl(form1Url);
  assert(g1Res.statusCode === 200 && g1Res.body.includes('SLN Consulting'), 'Form 1 (Website Enquiry Form) is accessible online and returns HTTP 200');

  const g2Res = await fetchUrl(form2Url);
  assert(g2Res.statusCode === 200 && g2Res.body.includes('SLN Consulting'), 'Form 2 (General Contact Form) is accessible online and returns HTTP 200');

  // Summary
  console.log(`\n===============================================================`);
  console.log(`Results: Total ${passed + failed} | Passed: ${passed} | Failed: ${failed}`);
  console.log(`===============================================================`);
  if (failed > 0) process.exit(1);
}

verifyGoogleFormsIntegration().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
