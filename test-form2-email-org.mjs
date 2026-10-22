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
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Origin': 'https://docs.google.com',
        'Referer': actionUrl.replace('/formResponse', '/viewform')
      }
    };

    const req = https.request(options, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        resolve({
          statusCode: res.statusCode,
          headers: res.headers,
          body: body
        });
      });
    });

    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

async function testForm2() {
  const f2Action = 'https://docs.google.com/forms/d/e/1FAIpQLSfp_u4mUMGlDdk9omnkDtI-Us3aDAlM4KzEGit3B-duDh4B1A/formResponse';
  const data = {
    'fvv': '1',
    'draftResponse': '[]',
    'pageHistory': '0',
    'fbzx': '',
    'entry.2005620554': 'Antigravity Test',
    'entry.1045781291': 'contact@company.com', // email format
    'entry.1065046570': 'Consultant',
    'entry.1166974658': 'visitor@example.com',
    'entry.839337160': '+91 9988776655',
    'entry.1007004095_hour': '16',
    'entry.1007004095_minute': '45',
    'entry.660909226': 'SOC As A Service',
    'entry.1789743': 'Testing if Form 2 accepts with email org'
  };

  const res = await postGoogleForm(f2Action, data);
  console.log('Form 2 (with email in org) HTTP status:', res.statusCode);
  const vhw8k = res.body.match(/<div class="vHW8K">([\s\S]*?)<\/div>/);
  console.log('Confirmation message:', vhw8k ? vhw8k[1] : 'None');
}

testForm2().catch(console.error);
