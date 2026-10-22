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
          bodySnippet: body.slice(0, 500)
        });
      });
    });

    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

async function testSubmissions() {
  console.log('Testing Form 1 (7 fields: Full Name, Company, Designation, Email, Phone, Service, Message)...');
  const form1Action = 'https://docs.google.com/forms/d/e/1FAIpQLSdpVszsphdo1KhHgig4lCHfjuHmE8IzSvIUDHEFiE52LoW0Rw/formResponse';
  const data1 = {
    'entry.2005620554': 'Test SLN Visitor',
    'entry.969435007': 'SLN Test Company',
    'entry.1065046570': 'Security Engineer',
    'entry.1166974658': 'test@slnconsulting.co.in',
    'entry.839337160': '+91 9940196195',
    'entry.1230817807': 'VAPT',
    'entry.1984267215': 'Test enquiry submission from automated diagnostic tool.'
  };
  const res1 = await postGoogleForm(form1Action, data1);
  console.log(`Form 1 Response Status: ${res1.statusCode}`);
  const success1 = res1.statusCode === 200 || (res1.statusCode >= 300 && res1.statusCode < 400);
  console.log(`Form 1 Success: ${success1}`);
  if (res1.bodySnippet.includes('response has been recorded') || res1.bodySnippet.includes('freebirdFormviewerViewResponseConfirmationMessage')) {
    console.log('Form 1 confirmed response recorded in HTML!');
  }

  console.log('\nTesting Form 2 (8 fields: Name, Org, Designation, Email, Phone, Right time to call, Select Service, Message)...');
  const form2Action = 'https://docs.google.com/forms/d/e/1FAIpQLSfp_u4mUMGlDdk9omnkDtI-Us3aDAlM4KzEGit3B-duDh4B1A/formResponse';
  // Google Forms Time field: entry.1007004095_hour and entry.1007004095_minute
  const data2 = {
    'entry.2005620554': 'Test SLN Visitor',
    'entry.1045781291': 'SLN Test Organisation',
    'entry.1065046570': 'Security Analyst',
    'entry.1166974658': 'test@slnconsulting.co.in',
    'entry.839337160': '+91 9940196195',
    'entry.1007004095_hour': '14',
    'entry.1007004095_minute': '30',
    'entry.660909226': 'SOC As A Service',
    'entry.1789743': 'Test callback request from automated diagnostic tool.'
  };
  const res2 = await postGoogleForm(form2Action, data2);
  console.log(`Form 2 Response Status: ${res2.statusCode}`);
  const success2 = res2.statusCode === 200 || (res2.statusCode >= 300 && res2.statusCode < 400);
  console.log(`Form 2 Success: ${success2}`);
  if (res2.bodySnippet.includes('response has been recorded') || res2.bodySnippet.includes('freebirdFormviewerViewResponseConfirmationMessage')) {
    console.log('Form 2 confirmed response recorded in HTML!');
  }
}

testSubmissions();
