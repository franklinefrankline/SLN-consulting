import https from 'node:https';

function postGoogleForm(actionUrl, formData) {
  return new Promise((resolve, reject) => {
    const postData = new URLSearchParams(formData).toString();
    const url = new URL(actionUrl);

    const options = {
      hostname: url.hostname,
      path: url.pathname,
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': Buffer.byteLength(postData),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
      }
    };

    const req = https.request(options, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        resolve({
          statusCode: res.statusCode,
          headers: res.headers,
          bodySnippet: body.slice(0, 1000)
        });
      });
    });

    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

async function testBoth() {
  console.log('=== SUBMITTING TO GOOGLE FORM 1 ===');
  const f1Action = 'https://docs.google.com/forms/d/e/1FAIpQLSdpVszsphdo1KhHgig4lCHfjuHmE8IzSvIUDHEFiE52LoW0Rw/formResponse';
  const data1 = {
    'entry.2005620554': 'Live Verification Test',
    'entry.969435007': 'SLN Verified Corp',
    'entry.1065046570': 'Lead Auditor',
    'entry.1166974658': 'srinivas.c@slnconsulting.co.in',
    'entry.839337160': '+91 98401 96195',
    'entry.1230817807': 'SOC As A Service',
    'entry.1984267215': 'Test from Antigravity diagnostic agent'
  };
  const res1 = await postGoogleForm(f1Action, data1);
  console.log('Form 1 HTTP Code:', res1.statusCode);
  console.log('Form 1 Body snippet:\n', res1.bodySnippet);
  const isRecorded1 = res1.bodySnippet.includes('freebirdFormviewerViewResponseConfirmationMessage') || res1.bodySnippet.includes('Your response has been recorded');
  console.log('Is Form 1 confirmed recorded in Google Forms?:', isRecorded1);

  console.log('\n=== SUBMITTING TO GOOGLE FORM 2 ===');
  const f2Action = 'https://docs.google.com/forms/d/e/1FAIpQLSfp_u4mUMGlDdk9omnkDtI-Us3aDAlM4KzEGit3B-duDh4B1A/formResponse';
  const data2 = {
    'entry.2005620554': 'Live Verification Test',
    'entry.1045781291': 'test@slnconsulting.co.in', // Notice: Form 2 requires email format for Organisation Name!
    'entry.1065046570': 'Security Architect',
    'entry.1166974658': 'srinivas.c@slnconsulting.co.in',
    'entry.839337160': '+91 98401 96195',
    'entry.1007004095_hour': '15',
    'entry.1007004095_minute': '00',
    'entry.660909226': 'SOC As A Service',
    'entry.1789743': 'Test callback enquiry'
  };
  const res2 = await postGoogleForm(f2Action, data2);
  console.log('Form 2 HTTP Code:', res2.statusCode);
  console.log('Form 2 Body snippet:\n', res2.bodySnippet);
  const isRecorded2 = res2.bodySnippet.includes('freebirdFormviewerViewResponseConfirmationMessage') || res2.bodySnippet.includes('Your response has been recorded');
  console.log('Is Form 2 confirmed recorded in Google Forms?:', isRecorded2);
}

testBoth().catch(console.error);
