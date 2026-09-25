import os
import re

HTML_FILES = [
    'index.html',
    'about.html',
    'cambridge.html',
    'campus.html',
    'contact.html',
    'ec-council.html',
    'enterprises.html',
    'internships.html',
    'isc2.html',
    'it-services.html',
    'offerings.html',
    'soc.html',
    'training.html',
    'training-schedule.html'
]

REQUIRED_FUNCTIONS = [
    'showToast',
    'toggleTheme',
    'toggleMobileAccordion',
    'selectProposalTopic',
    'initInternshipInteractions',
    'handleInternshipEnquirySubmit',
    'toggleInternshipsDropdown',
    'openInternshipsDropdown',
    'closeInternshipsDropdown',
    'routePage',
    'closeAllDrawers',
    'toggleMobileNav',
    'isolateScrollElement',
    'openDrawer',
    'closeDrawer',
    'openPolicyModal',
    'closePolicyModal',
    'handleEmailSubscribe',
    'handleContactSubmit'
]

print("=== CHECKING ALL JAVASCRIPT FUNCTIONS ACROSS 14 HTML FILES ===")

all_ok = True
for fname in HTML_FILES:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    missing = []
    for fn in REQUIRED_FUNCTIONS:
        pattern = rf'function\s+{fn}\s*\('
        if not re.search(pattern, content):
            missing.append(fn)

    if missing:
        print(f"[FAIL] {fname} is missing functions: {missing}")
        all_ok = False
    else:
        print(f"[PASS] {fname} contains all {len(REQUIRED_FUNCTIONS)} required JS functions")

if all_ok:
    print("\nALL 14 HTML FILES HAVE 100% OF REQUIRED FUNCTIONS DEFINED!")
