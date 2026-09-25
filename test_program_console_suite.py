# -*- coding: utf-8 -*-
"""
test_program_console_suite.py
Validates the Program Console and Evidence of Practice Badge implementation
against all 17 requirements of the prompt across all 14 HTML files.
"""

import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ALL_HTML_FILES = [
    'index.html',
    'about.html',
    'soc.html',
    'enterprises.html',
    'campus.html',
    'internships.html',
    'cambridge.html',
    'isc2.html',
    'ec-council.html',
    'it-services.html',
    'training.html',
    'training-schedule.html',
    'contact.html',
    'offerings.html'
]

REQUIRED_SELECTORS = [
    '.internship-program-console',
    '.internship-console-header',
    '.internship-console-cohort',
    '.internship-console-pathway',
    '.internship-console-stages',
    '.internship-console-stage',
    '.internship-console-task',
    '.internship-console-metrics',
    '.internship-evidence-badge'
]

REQUIRED_STRINGS = [
    'PROGRAM CONSOLE',
    'Cohort 2027',
    'Selected Pathway:',
    'AI-SOC',
    '01 Foundation',
    '(Month 01)',
    '02 Practice',
    '(Month 02)',
    '03 Project',
    '(Month 03)',
    'TASK SCENARIO: ALERT TRIAGE',
    'Unusual Sign-in Pattern',
    'GUIDED',
    'Review',
    'Live Mentor Sessions / Week',
    'Recording Access',
    'EVIDENCE OF PRACTICE',
    'Task → Evidence → Readiness'
]

def run_tests():
    total_checks = 0
    passed_checks = 0
    errors = []

    def check(condition, message):
        nonlocal total_checks, passed_checks
        total_checks += 1
        if condition:
            passed_checks += 1
            print(f"  [PASS] {message}")
        else:
            errors.append(message)
            print(f"  [FAIL] {message}")

    print("==================================================")
    print("TESTING PROGRAM CONSOLE & EVIDENCE BADGE SUITE")
    print("==================================================\n")

    for fname in ALL_HTML_FILES:
        print(f"--- Checking {fname} ---")
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Component classes in HTML/CSS
        for sel in REQUIRED_SELECTORS:
            check(sel.lstrip('.') in content, f"{fname} contains {sel}")

        # 2. Required text content
        for s in REQUIRED_STRINGS:
            # Normalize arrows
            normalized_s = s.replace('→', '&rarr;')
            found = (s in content) or (normalized_s in content)
            check(found, f"{fname} contains '{s}'")

        # 3. CSS animation rules
        check('.internship-program-console' in content and 'background:' in content, f"{fname} defines .internship-program-console CSS")
        check('internship-pulse-dot' in content, f"{fname} has internship-pulse-dot")
        check('internship-alert-pulse' in content, f"{fname} has internship-alert-pulse")
        check('console-animate-fade-right' in content, f"{fname} has console-animate-fade-right")
        check('badge-animate-fade-down' in content, f"{fname} has badge-animate-fade-down")
        check('console-stagger-item' in content, f"{fname} has console-stagger-item")
        check('prefers-reduced-motion: reduce' in content, f"{fname} has prefers-reduced-motion accessibility")

        # 4. JS interaction / scroll observer
        check('IntersectionObserver' in content and 'internship-program-console' in content, f"{fname} has scroll reveal observer")

    print("\n==================================================")
    print(f"RESULTS: {passed_checks}/{total_checks} PASSED")
    if errors:
        print(f"FAILED CHECKS ({len(errors)}):")
        for err in errors:
            print(f" - {err}")
        return False
    else:
        print("ALL PROGRAM CONSOLE VERIFICATIONS PASSED PERFECTLY!")
        print("==================================================")
        return True

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
