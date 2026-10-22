<?php
/**
 * ====================================================================================
 * SLN CONSULTING — GOOGLE FORMS CENTRALIZED CONFIGURATION & INTEGRATION
 * ====================================================================================
 *
 * This is the SINGLE configuration file for all Google Form integrations across the
 * SLN Consulting website.
 *
 * Requirements:
 * 1. Form 1 is associated with the Website Enquiry Form (contact.php / conmail.php).
 * 2. Form 2 is associated with the General Contact Form link (sidebar & external links).
 * 3. When either URL changes here, the entire website updates automatically without
 *    needing changes across multiple files.
 * 4. When a Google Form is recreated, update its URL and its field-entry mappings below.
 *
 * ====================================================================================
 * HOW TO OBTAIN NEW ENTRY IDs WHEN A GOOGLE FORM IS RECREATED:
 * ====================================================================================
 * Option A (Recommended):
 *   1. Open the Google Form in your browser.
 *   2. Click the three dots (More) in the top-right -> "Get pre-filled link".
 *   3. Fill each field with its name (e.g. name="NAME_TEST", email="test@example.com").
 *   4. Click "Get link" and copy the generated link.
 *   5. Paste it in a text editor to see all the entry parameters:
 *      entry.2005620554=NAME_TEST&entry.1166974658=test%40example.com...
 *   6. Copy each entry ID (e.g. entry.2005620554) into the corresponding field below.
 *
 * Option B:
 *   Right-click each question on the Google Form -> "Inspect" and look for the <input>
 *   tag with name="entry.XXXXXXXXX".
 * ====================================================================================
 */

function sln_derive_response_url($url) {
    if (empty($url)) return '';
    if (strpos($url, '/formResponse') !== false) {
        return preg_replace('/\?.*$/', '', $url);
    }
    // Convert /viewform, /edit, /prefill, etc. to /formResponse
    $base = preg_replace('/(\/(viewform|edit|formResponse|prefill)[^\?]*)(\?.*)?$/', '/formResponse', $url);
    if ($base === $url) {
        $base = rtrim($url, '/') . '/formResponse';
    }
    return $base;
}

function sln_get_forms_config() {
    static $config = null;
    if ($config !== null) {
        return $config;
    }

    // Default configuration (can also be overridden via .env)
    $form1Url = getenv('GOOGLE_FORM_1_URL') ?: 'https://docs.google.com/forms/d/e/1FAIpQLSdpVszsphdo1KhHgig4lCHfjuHmE8IzSvIUDHEFiE52LoW0Rw/viewform';
    $form2Url = getenv('GOOGLE_FORM_2_URL') ?: 'https://docs.google.com/forms/d/e/1FAIpQLSfp_u4mUMGlDdk9omnkDtI-Us3aDAlM4KzEGit3B-duDh4B1A/viewform';

    $config = [
        /**
         * FORM 1: Website Enquiry Form
         * Associated with: contact.php "Send us a Message" & conmail.php
         */
        'form1' => [
            'key'           => 'form1',
            'name'          => 'Website Enquiry Form',
            // View URL shown to visitors and used for all links
            'url'           => $form1Url,
            // Direct submission responder URL
            'response_url'  => sln_derive_response_url($form1Url),
            // Background direct submission toggle
            'submit_direct' => true,
            // Field-entry mappings for Google Form 1:
            'entries'       => [
                'name'         => 'entry.2005620554', // Name *
                'organisation' => 'entry.969435007',  // Organisation Name *
                'designation'  => 'entry.1065046570', // Designation *
                'email'        => 'entry.1166974658', // Email *
                'phone'        => 'entry.839337160',  // Phone *
                'service'      => 'entry.1230817807', // Select Service *
                'message'      => 'entry.1984267215'  // Requirement / Message
            ],
            // Service dropdown code to Google Form exact option text
            'service_options' => [
                'soc'                      => 'SOC As A Service',
                'vapt'                     => 'VAPT',
                'cybersecurity_internship' => 'Cybersecurity Internship',
                'skilling'                 => 'Skilling',
                'cambridge'                => 'Cambridge Learning',
                'nure'                     => 'ISC2',
                'ec'                       => 'EC-Council',
                'it_services'              => 'IT Services'
            ]
        ],

        /**
         * FORM 2: General Contact Form
         * Associated with: General Contact Form link in contact.php, form.php & conmail1.php
         */
        'form2' => [
            'key'           => 'form2',
            'name'          => 'General Contact Form',
            // View URL shown to visitors and used for all links
            'url'           => $form2Url,
            // Direct submission responder URL
            'response_url'  => sln_derive_response_url($form2Url),
            // Background direct submission toggle
            'submit_direct' => true,
            // Field-entry mappings for Google Form 2:
            'entries'       => [
                'name'                      => 'entry.2005620554', // Name *
                'organisation'              => 'entry.1045781291', // Organisation Name *
                'designation'               => 'entry.1065046570', // Designation *
                'email'                     => 'entry.1166974658', // Email *
                'phone'                     => 'entry.839337160',  // Phone *
                'right_time_to_call_hour'   => 'entry.1007004095_hour',   // Time Hour
                'right_time_to_call_minute' => 'entry.1007004095_minute', // Time Minute
                'service'                   => 'entry.660909226',  // Select Service
                'message'                   => 'entry.1789743'     // Message
            ],
            // Service dropdown code to Google Form exact option text
            'service_options' => [
                'soc'                      => 'SOC As A Service',
                'vapt'                     => 'VAPT',
                'cybersecurity_internship' => 'Cybersecurity Internship',
                'skilling'                 => 'Skilling',
                'cambridge'                => 'Cambridge Learning',
                'nure'                     => 'ISC2',
                'ec'                       => 'EC-Council',
                'it_services'              => 'IT Services'
            ]
        ]
    ];

    return $config;
}

/**
 * Convenience Getters for Template Links
 */
function sln_get_form1_url() {
    $cfg = sln_get_forms_config();
    return $cfg['form1']['url'] ?? '';
}

function sln_get_form2_url() {
    $cfg = sln_get_forms_config();
    return $cfg['form2']['url'] ?? '';
}

function sln_fetch_gform_session_meta($viewUrl) {
    $meta = ['fbzx' => null, 'cookies' => ''];
    if (empty($viewUrl)) return $meta;

    if (function_exists('curl_init')) {
        $ch = curl_init($viewUrl);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, true);
        curl_setopt($ch, CURLOPT_TIMEOUT, 4);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
        $raw = curl_exec($ch);
        $headerSize = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
        $headers = substr($raw, 0, $headerSize);
        $body = substr($raw, $headerSize);
        curl_close($ch);

        if (preg_match_all('/^Set-Cookie:\s*([^;\r\n]+)/mi', $headers, $matches)) {
            $meta['cookies'] = implode('; ', $matches[1]);
        }
        if (preg_match('/name="fbzx"\s*value="([^"]+)"/i', $body, $fbzxMatch)) {
            $meta['fbzx'] = $fbzxMatch[1];
        }
    }
    return $meta;
}

/**
 * Dispatch an enquiry directly to Google Forms in the background.
 *
 * @param string $formKey 'form1' or 'form2'
 * @param array $data Input fields (name, organisation, designation, email, phone, service, message, appt)
 * @return array ['success' => bool, 'http_code' => int, 'message' => string]
 */
function sln_submit_to_google_form($formKey, array $data) {
    $config = sln_get_forms_config();
    if (!isset($config[$formKey])) {
        return ['success' => false, 'http_code' => 0, 'message' => "Unknown form configuration: {$formKey}"];
    }

    $formCfg = $config[$formKey];
    if (empty($formCfg['submit_direct'])) {
        return ['success' => false, 'http_code' => 0, 'skipped' => true, 'message' => 'Direct Google Forms submission disabled'];
    }

    $responseUrl = !empty($formCfg['response_url']) ? $formCfg['response_url'] : sln_derive_response_url($formCfg['url']);
    if (empty($responseUrl)) {
        return ['success' => false, 'http_code' => 0, 'message' => 'No response URL configured'];
    }

    // Acquire session metadata (fbzx + cookies) to ensure genuine session verification
    $viewUrl = $formCfg['url'] ?? '';
    $sessionMeta = sln_fetch_gform_session_meta($viewUrl);

    $entries = $formCfg['entries'] ?? [];
    $serviceOptions = $formCfg['service_options'] ?? [];

    $postFields = [];
    foreach ($entries as $fieldKey => $entryParam) {
        if (empty($entryParam)) continue;

        if ($fieldKey === 'service') {
            $rawService = $data['service'] ?? '';
            // If passed code e.g. 'soc', map to text; otherwise keep as is
            $postFields[$entryParam] = $serviceOptions[$rawService] ?? $rawService;
        } elseif ($fieldKey === 'organisation') {
            $org = $data['organisation'] ?? '';
            if ($formKey === 'form2') {
                // Google Form 2 Question 2 has an email validation rule in Google Forms
                $email = $data['email'] ?? '';
                if (strpos($org, '@') === false && !empty($email)) {
                    $org = "{$org} <{$email}>";
                }
            }
            $postFields[$entryParam] = $org;
        } elseif ($fieldKey === 'right_time_to_call_hour') {
            $rawTime = $data['right_time_to_call'] ?? ($data['appt'] ?? '');
            $hour = '10';
            if (preg_match('/(\d{1,2}):?(\d{2})?\s*(AM|PM)?/i', $rawTime, $m)) {
                $h = (int)$m[1];
                $ampm = strtoupper($m[3] ?? '');
                if ($ampm === 'PM' && $h < 12) $h += 12;
                if ($ampm === 'AM' && $h === 12) $h = 0;
                $hour = sprintf('%02d', $h);
            }
            $postFields[$entryParam] = $hour;
        } elseif ($fieldKey === 'right_time_to_call_minute') {
            $rawTime = $data['right_time_to_call'] ?? ($data['appt'] ?? '');
            $minute = '00';
            if (preg_match('/(\d{1,2}):?(\d{2})?\s*(AM|PM)?/i', $rawTime, $m)) {
                $min = isset($m[2]) && $m[2] !== '' ? (int)$m[2] : 0;
                $minute = sprintf('%02d', $min);
            }
            $postFields[$entryParam] = $minute;
        } elseif (isset($data[$fieldKey])) {
            $postFields[$entryParam] = (string)$data[$fieldKey];
        }
    }

    $postFields['fvv'] = '1';
    if (!empty($sessionMeta['fbzx'])) {
        $postFields['fbzx'] = $sessionMeta['fbzx'];
    }
    $postFields['pageHistory'] = '0';

    $payload = http_build_query($postFields);

    // Attempt HTTP POST using cURL if available, else stream context
    if (function_exists('curl_init')) {
        $ch = curl_init($responseUrl);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_TIMEOUT, 10);
        curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');

        $headers = ['Content-Type: application/x-www-form-urlencoded', 'Origin: https://docs.google.com'];
        if (!empty($viewUrl)) {
            $headers[] = 'Referer: ' . $viewUrl;
        }
        if (!empty($sessionMeta['cookies'])) {
            $headers[] = 'Cookie: ' . $sessionMeta['cookies'];
        }
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

        $responseBody = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $curlError = curl_error($ch);
        curl_close($ch);

        $isSuccess = ($httpCode >= 200 && $httpCode < 400) && (
            strpos($responseBody, 'Thanks for submitting your contact info!') !== false ||
            strpos($responseBody, 'Your response has been recorded') !== false ||
            strpos($responseBody, 'edit2=') !== false
        );
        return [
            'success'   => $isSuccess,
            'http_code' => $httpCode,
            'message'   => $isSuccess ? 'Google Form response recorded' : "Google Form HTTP {$httpCode}: {$curlError}"
        ];
    } else {
        $headerStr = "Content-Type: application/x-www-form-urlencoded\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\r\n";
        if (!empty($viewUrl)) {
            $headerStr .= "Referer: {$viewUrl}\r\n";
        }
        if (!empty($sessionMeta['cookies'])) {
            $headerStr .= "Cookie: {$sessionMeta['cookies']}\r\n";
        }

        $opts = [
            'http' => [
                'method'  => 'POST',
                'header'  => $headerStr,
                'content' => $payload,
                'timeout' => 10,
                'ignore_errors' => true
            ]
        ];
        $context = stream_context_create($opts);
        $responseBody = @file_get_contents($responseUrl, false, $context);
        $httpCode = 200;
        if (isset($http_response_header) && is_array($http_response_header)) {
            if (preg_match('#HTTP/\S+\s+(\d+)#', $http_response_header[0], $matches)) {
                $httpCode = (int)$matches[1];
            }
        }
        $isSuccess = ($httpCode >= 200 && $httpCode < 400) && (
            strpos($responseBody, 'Thanks for submitting your contact info!') !== false ||
            strpos($responseBody, 'Your response has been recorded') !== false ||
            strpos($responseBody, 'edit2=') !== false
        );
        return [
            'success'   => $isSuccess,
            'http_code' => $httpCode,
            'message'   => $isSuccess ? 'Google Form response recorded' : "Google Form HTTP {$httpCode}"
        ];
    }
}

return sln_get_forms_config();
