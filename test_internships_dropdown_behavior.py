# -*- coding: utf-8 -*-
"""
test_internships_dropdown_behavior.py
Verification test for the pure dropdown behavior of the Internships navbar item.
"""

import os
import glob
import re

HTML_FILES = [
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

def run_tests():
    total_checks = 0
    passed_checks = 0
    errors = []

    def check(condition, desc):
        nonlocal total_checks, passed_checks
        total_checks += 1
        if condition:
            passed_checks += 1
            print(f"  [PASS] {desc}")
        else:
            errors.append(desc)
            print(f"  [FAIL] {desc}")

    print("=== TESTING INTERNSHIPS NAVBAR PURE DROPDOWN BEHAVIOR ===")

    for fname in HTML_FILES:
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()

        # 1. Trigger is a button, not an <a> tag
        check('<button type="button"' in c and 'id="internshipsNavBtn"' in c, f"{fname}: trigger is a <button>")
        check('href="internships.html"' not in c.split('id="internshipsNavBtn"')[0][-100:], f"{fname}: trigger has no href")
        check('onclick="toggleInternshipsDropdown(event)"' in c, f"{fname}: trigger has toggleInternshipsDropdown(event)")
        check('aria-haspopup="true"' in c, f"{fname}: trigger has aria-haspopup='true'")
        check('aria-expanded="false"' in c, f"{fname}: trigger has aria-expanded='false'")

        # 2. Dropdown panel
        check('id="internshipsDropdownPanel"' in c, f"{fname}: has #internshipsDropdownPanel")
        check('href="internships.html#program"' in c, f"{fname}: has link to #program")
        check('href="internships.html#pathways"' in c, f"{fname}: has link to #pathways")
        check('href="internships.html#journey"' in c, f"{fname}: has link to #journey")
        check('href="internships.html#institutional-model"' in c, f"{fname}: has link to #institutional-model")

        # 3. Dropdown items close dropdown on click
        check('closeInternshipsDropdown()' in c, f"{fname}: dropdown links close the dropdown on click")

        # 4. JS functions
        check('function toggleInternshipsDropdown' in c, f"{fname}: JS defines toggleInternshipsDropdown")
        check('function openInternshipsDropdown' in c, f"{fname}: JS defines openInternshipsDropdown")
        check('function closeInternshipsDropdown' in c, f"{fname}: JS defines closeInternshipsDropdown")

        # 5. CSS animation
        check('internshipDropdownFade' in c, f"{fname}: CSS has internshipDropdownFade animation")

    print("\n==================================================")
    print(f"TEST RESULTS: {passed_checks}/{total_checks} PASSED")
    if errors:
        print(f"FAILED ({len(errors)}):")
        for e in errors:
            print("  *", e)
    else:
        print("ALL INTERNSHIPS NAVBAR BEHAVIOR CHECKS PASSED PERFECTLY!")
    print("==================================================")

if __name__ == '__main__':
    run_tests()
