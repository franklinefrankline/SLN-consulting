<?php
/**
 * SLN Consulting - Secure Server-Side Storage Engine
 *
 * Reliably stores enquiry records in protected server storage (JSON and CSV).
 * Prevents direct public access via .htaccess and directory protection.
 */

function sln_get_storage_dir() {
    // Vercel serverless functions have a read-only filesystem outside /tmp
    if (!empty($_SERVER['VERCEL']) || !empty(getenv('VERCEL')) || !empty($_SERVER['VERCEL_ENV']) || !empty($_SERVER['VERCEL_URL'])) {
        $dir = sys_get_temp_dir() . '/sln_data';
    } else {
        $dir = __DIR__ . '/data';
    }
    if (!is_dir($dir)) {
        @mkdir($dir, 0755, true);
        $htaccess = $dir . '/.htaccess';
        if (!file_exists($htaccess)) {
            @file_put_contents($htaccess, "Order deny,allow\nDeny from all\n");
        }
        $indexHtml = $dir . '/index.html';
        if (!file_exists($indexHtml)) {
            @file_put_contents($indexHtml, "<!DOCTYPE html><html><head><title>403 Forbidden</title></head><body><h1>403 Forbidden</h1></body></html>");
        }
    }
    return $dir;
}

function sln_store_enquiry(array $data) {
    $dir = sln_get_storage_dir();
    $jsonFile = $dir . '/enquiries.json';
    $csvFile = $dir . '/enquiries.csv';

    $enquiryId = 'SLN-' . date('Ymd-His') . '-' . substr(md5(uniqid(mt_rand(), true)), 0, 6);
    $isoTimestamp = date('c');
    $displayDate = date('Y-m-d H:i:s T');

    $record = array_merge([
        'id'                 => $enquiryId,
        'timestamp'          => $isoTimestamp,
        'date'               => $displayDate,
        'form_type'          => 'unknown',
        'name'               => '',
        'organisation'       => '',
        'designation'        => '',
        'email'              => '',
        'phone'              => '',
        'right_time_to_call' => '',
        'service'            => '',
        'message'            => '',
        'ip'                 => '',
        'email_status'       => 'pending',
        'email_error'        => null,
        'google_forms_note'  => 'Enquiry saved in primary server storage; Google Forms direct sync not reliable for this schema.'
    ], $data);

    // 1. Append to JSON file with lock
    $existing = [];
    if (file_exists($jsonFile)) {
        $content = @file_get_contents($jsonFile);
        if ($content !== false) {
            $parsed = @json_decode($content, true);
            if (is_array($parsed)) {
                $existing = $parsed;
            }
        }
    }
    $existing[] = $record;
    $jsonResult = @file_put_contents($jsonFile, json_encode($existing, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES), LOCK_EX);

    // 2. Append to CSV file
    $csvExists = file_exists($csvFile) && filesize($csvFile) > 0;
    $csvHandle = @fopen($csvFile, 'a');
    if ($csvHandle) {
        if (!$csvExists) {
            fputcsv($csvHandle, [
                'ID',
                'Timestamp',
                'Date',
                'Form Type',
                'Name',
                'Organisation',
                'Designation',
                'Email',
                'Phone',
                'Right Time to Call',
                'Service',
                'Message',
                'Client IP',
                'Email Status'
            ]);
        }
        fputcsv($csvHandle, [
            $record['id'],
            $record['timestamp'],
            $record['date'],
            $record['form_type'],
            $record['name'],
            $record['organisation'],
            $record['designation'],
            $record['email'],
            $record['phone'],
            $record['right_time_to_call'],
            $record['service'],
            str_replace(["\r", "\n"], ' ', $record['message']),
            $record['ip'],
            $record['email_status']
        ]);
        fclose($csvHandle);
    }

    if ($jsonResult === false && !$csvHandle) {
        error_log("[SLN Storage Error] Could not write to {$jsonFile} or {$csvFile}");
        return ['success' => false, 'error' => 'Storage write failure.'];
    }

    return ['success' => true, 'id' => $enquiryId, 'record' => $record];
}

function sln_update_enquiry_email_status($enquiryId, $status, $errorMsg = null) {
    $dir = sln_get_storage_dir();
    $jsonFile = $dir . '/enquiries.json';
    if (!file_exists($jsonFile)) return false;

    $content = @file_get_contents($jsonFile);
    if ($content === false) return false;

    $records = @json_decode($content, true);
    if (!is_array($records)) return false;

    $updated = false;
    foreach ($records as &$item) {
        if (isset($item['id']) && $item['id'] === $enquiryId) {
            $item['email_status'] = $status;
            if ($errorMsg !== null) {
                $item['email_error'] = $errorMsg;
            }
            $updated = true;
            break;
        }
    }
    unset($item);

    if ($updated) {
        @file_put_contents($jsonFile, json_encode($records, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES), LOCK_EX);
    }
    return $updated;
}

function sln_update_enquiry_google_form_status($enquiryId, $status) {
    $dir = sln_get_storage_dir();
    $jsonFile = $dir . '/enquiries.json';
    if (!file_exists($jsonFile)) return false;

    $content = @file_get_contents($jsonFile);
    if ($content === false) return false;

    $records = @json_decode($content, true);
    if (!is_array($records)) return false;

    $updated = false;
    foreach ($records as &$item) {
        if (isset($item['id']) && $item['id'] === $enquiryId) {
            $item['google_form_status'] = $status;
            $updated = true;
            break;
        }
    }
    unset($item);

    if ($updated) {
        @file_put_contents($jsonFile, json_encode($records, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES), LOCK_EX);
    }
    return $updated;
}

function sln_get_all_enquiries() {
    $dir = sln_get_storage_dir();
    $jsonFile = $dir . '/enquiries.json';
    if (!file_exists($jsonFile)) return [];
    $content = @file_get_contents($jsonFile);
    if ($content === false) return [];
    $data = @json_decode($content, true);
    return is_array($data) ? $data : [];
}
