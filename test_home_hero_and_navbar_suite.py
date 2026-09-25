# -*- coding: utf-8 -*-
"""
test_home_hero_and_navbar_suite.py
Verification suite validating the complete Home Page visual update,
strict single-row desktop navbar, and Internships dropdown navigation behavior
across all 14 production HTML files.
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
    print("HOME PAGE HERO & SINGLE-ROW NAVBAR VERIFICATION")
    print("==================================================\n")

    for fname in ALL_HTML_FILES:
        print(f"--- Checking {fname} ---")
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. HOME HERO VERIFICATION
        check('id="hero-section"' in content, f"{fname} has #hero-section")
        check('EMPOWERING A SECURE TOMORROW' in content, f"{fname} has hero eyebrow badge")
        check("Let's Build" in content and "a Safer, Smarter Tomorrow" in content, f"{fname} has hero main heading")
        check("Tell us what your organization or institution needs" in content, f"{fname} has hero supporting description")
        check("GET IN TOUCH" in content, f"{fname} has 'GET IN TOUCH' button")
        check("Our Services" in content, f"{fname} has 'Our Services' button")
        check("assets/home_hero_cybersecurity_office.jpg" in content, f"{fname} uses assets/home_hero_cybersecurity_office.jpg")
        check("object-cover" in content and "home-hero-image" in content, f"{fname} has home-hero-image with object-fit: cover")
        check("10+" in content and "Years of Experience" in content, f"{fname} has 10+ Years stat")
        check("500+" in content and "Happy Clients" in content, f"{fname} has 500+ Clients stat")
        check("50+" in content and "Training Programs" in content, f"{fname} has 50+ Programs stat")
        check("100+" in content and "Corporate Collaborations" in content, f"{fname} has 100+ Collaborations stat")

        # 2. STRICT SINGLE ROW NAVBAR VERIFICATION
        check("header-desktop-row" in content, f"{fname} has header-desktop-row class")
        check("header-desktop-nav" in content, f"{fname} has header-desktop-nav class")
        check("flex-nowrap" in content, f"{fname} has flex-nowrap rule on desktop nav row")
        check("navbar-container" in content and "max-w-[1440px]" in content, f"{fname} has container navbar-container max-w-[1440px]")
        check("hidden xl:flex" in content, f"{fname} switches to desktop nav at xl breakpoint")
        check("xl:hidden" in content and "mobileMenuBtn" in content, f"{fname} switches to mobile hamburger below xl")

        # 3. INTERNSHIPS DROPDOWN BEHAVIOR VERIFICATION
        check('id="internshipsNavBtn"' in content and '<button type="button"' in content, f"{fname} has button trigger for Internships")
        check('onclick="toggleInternshipsDropdown(event)"' in content, f"{fname} has toggleInternshipsDropdown handler")
        check('href="internships.html"' in content, f"{fname} Program item routes to main Internship Home Page")
        check('href="internships.html#pathways"' in content, f"{fname} Pathways item routes to #pathways")
        check('href="internships.html#student-journey"' in content, f"{fname} Student Journey item routes to #student-journey")
        check('href="internships.html#institutional-model"' in content, f"{fname} Institutional Model item routes to #institutional-model")

        # 4. REDUCED MOTION & ACCESSIBILITY
        check('prefers-reduced-motion: reduce' in content, f"{fname} supports prefers-reduced-motion")

    print("\n==================================================")
    print(f"RESULTS: {passed_checks}/{total_checks} PASSED")
    if errors:
        print(f"FAILED ({len(errors)}):")
        for err in errors:
            print("  *", err)
        return False
    else:
        print("ALL HOME HERO & SINGLE-ROW NAVBAR CHECKS PASSED PERFECTLY!")
        print("==================================================")
        return True

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
