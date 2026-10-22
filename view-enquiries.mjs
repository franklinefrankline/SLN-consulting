#!/usr/bin/env node
/**
 * SLN Consulting - Admin Enquiry Inspector CLI
 *
 * Usage:
 *   node view-enquiries.mjs            - View summary and recent enquiries
 *   node view-enquiries.mjs --all      - View all enquiries
 *   node view-enquiries.mjs SLN-XXX    - View full details of a specific enquiry
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Look for data dir in current dir or child SLN-Website-Development dir
const possibleDataDirs = [
  path.join(__dirname, 'data'),
  path.join(__dirname, 'SLN-Website-Development', 'data')
];

let dataDir = possibleDataDirs.find(d => fs.existsSync(d)) || path.join(__dirname, 'data');
const jsonFile = path.join(dataDir, 'enquiries.json');
const csvFile = path.join(dataDir, 'enquiries.csv');

console.log('='.repeat(70));
console.log(' SLN CONSULTING — ENQUIRY STORAGE VIEWER');
console.log('='.repeat(70));
console.log(`Storage Location: ${jsonFile}`);
console.log(`CSV Export:       ${csvFile}\n`);

if (!fs.existsSync(jsonFile)) {
  console.log('No enquiries recorded yet (enquiries.json not found).');
  process.exit(0);
}

let enquiries = [];
try {
  const content = fs.readFileSync(jsonFile, 'utf8');
  enquiries = JSON.parse(content);
} catch (e) {
  console.error(`Error parsing ${jsonFile}:`, e.message);
  process.exit(1);
}

if (!Array.isArray(enquiries) || enquiries.length === 0) {
  console.log('No enquiries found in storage.');
  process.exit(0);
}

const args = process.argv.slice(2);
const specificId = args.find(a => a.startsWith('SLN-'));
const showAll = args.includes('--all');

if (specificId) {
  const item = enquiries.find(e => e.id === specificId);
  if (!item) {
    console.log(`Enquiry with ID ${specificId} not found.`);
  } else {
    console.log(`DETAILS FOR ENQUIRY: ${item.id}`);
    console.log('-'.repeat(50));
    console.log(`Form Type:     ${item.form_type}`);
    console.log(`Date:          ${item.date || item.timestamp}`);
    console.log(`Name:          ${item.name}`);
    console.log(`Organisation:  ${item.organisation}`);
    console.log(`Designation:   ${item.designation}`);
    console.log(`Email:         ${item.email}`);
    console.log(`Phone:         ${item.phone}`);
    if (item.right_time_to_call) {
      console.log(`Call Time:     ${item.right_time_to_call}`);
    }
    console.log(`Service:       ${item.service}`);
    console.log(`Client IP:     ${item.ip}`);
    console.log(`Email Status:  ${item.email_status}`);
    if (item.email_error) {
      console.log(`Email Error:   ${item.email_error}`);
    }
    console.log(`Message:\n${item.message || '(None)'}`);
    console.log('-'.repeat(50));
  }
  process.exit(0);
}

// Summary stats
const total = enquiries.length;
const contactCount = enquiries.filter(e => e.form_type === 'contact_enquiry').length;
const callbackCount = enquiries.filter(e => e.form_type === 'callback_enquiry').length;
const emailSentCount = enquiries.filter(e => e.email_status === 'sent').length;

console.log(`Total Enquiries:       ${total}`);
console.log(`Contact Enquiries:     ${contactCount}`);
console.log(`Callback Enquiries:    ${callbackCount}`);
console.log(`Email Dispatched:      ${emailSentCount}`);
console.log('-'.repeat(70));

const displayList = showAll ? enquiries : enquiries.slice(-10);
console.log(`Showing ${displayList.length} of ${total} records:`);
console.log('');

displayList.forEach((e, idx) => {
  const num = showAll ? (idx + 1) : (total - displayList.length + idx + 1);
  const timeInfo = e.right_time_to_call ? ` | Call: ${e.right_time_to_call}` : '';
  console.log(`[#${num}] ${e.id} (${e.date || e.timestamp})`);
  console.log(`     Type: ${e.form_type} | Status: ${e.email_status}`);
  console.log(`     Client: ${e.name} <${e.email}> | Phone: ${e.phone}`);
  console.log(`     Org: ${e.organisation} | Desig: ${e.designation}`);
  console.log(`     Service: ${e.service}${timeInfo}`);
  console.log('');
});

console.log('To view full details of a specific enquiry:');
console.log('  node view-enquiries.mjs SLN-XXXXXXXX-XXXXXX-XXXXXX\n');
