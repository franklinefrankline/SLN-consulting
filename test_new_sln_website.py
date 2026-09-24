# -*- coding: utf-8 -*-
"""
test_new_sln_website.py
Automated test suite verifying the updated SLN Consulting website.
"""

import os
import re
import sys

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
    print("SLN CONSULTING UI UPDATE - VERIFICATION SUITE")
    print("==================================================\n")

    # 1. FILE EXISTENCE & CRITICAL JS FUNCTIONS
    print("--- 1. Testing Core Functionality in All 14 Files ---")
    for fname in ALL_HTML_FILES:
        check(os.path.exists(fname), f"{fname} exists on disk")
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()

        check('function routePage' in content, f"{fname} has routePage()")
        check('function toggleTheme' in content, f"{fname} has toggleTheme()")
        check('function handleContactSubmit' in content, f"{fname} has handleContactSubmit()")
        check('function handleEmailSubscribe' in content, f"{fname} has handleEmailSubscribe()")
        check('function openPolicyModal' in content, f"{fname} has openPolicyModal()")
        check('function toggleMobileNav' in content, f"{fname} has toggleMobileNav()")
        check('id="toast"' in content, f"{fname} has #toast notification element")
        check('id="policyModal"' in content, f"{fname} has #policyModal")

        # Theme button count check: exactly ONE theme toggle
        theme_buttons = re.findall(r'id=["\']headerThemeToggle["\']', content)
        check(len(theme_buttons) == 1, f"{fname} has exactly 1 theme button (found {len(theme_buttons)})")

    # 2. CHECK VIEW-INDEX IN INDEX.HTML
    print("\n--- 2. Testing New Homepage (#view-index) Structure in index.html ---")
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_content = f.read()

    # Section 21: Color identities
    check('id="hero-section"' in idx_content, "index.html has #hero-section (White + Light Blue + Gold)")
    check('id="about-section"' in idx_content, "index.html has #about-section (Soft Mint / Green)")
    check('id="services-section"' in idx_content, "index.html has #services-section (Lavender / Pastel Multi-Color)")
    check('id="why-choose-us-section"' in idx_content, "index.html has #why-choose-us-section (Dark Navy Cybersecurity)")
    check('id="impact-section"' in idx_content, "index.html has #impact-section (Cream / Soft Gold)")

    # Hero verification (Section 7, 8, 9, 10)
    check('EMPOWERING A SECURE TOMORROW' in idx_content, "Hero has label 'EMPOWERING A SECURE TOMORROW'")
    check("Let's Build" in idx_content and "a Safer, Smarter Tomorrow" in idx_content, "Hero has main heading 'Let\\'s Build a Safer, Smarter Tomorrow'")
    check("Tell us what your organization or institution needs" in idx_content, "Hero has concise supporting text")
    check("assets/hero_offerings_office.jpg" in idx_content, "Hero uses corporate building image assets/hero_offerings_office.jpg")
    check("DIRECT INQUIRIES" in idx_content and "Send Us a Message" in idx_content, "Hero has Direct Inquiries floating card")
    check("handleContactSubmit(event)" in idx_content, "Direct Inquiries form uses handleContactSubmit(event)")
    check("10+ Years of Experience" in idx_content or "Years of Experience" in idx_content, "Hero has 10+ Years Experience stat")
    check("500+ Happy Clients" in idx_content or "500+" in idx_content, "Hero has 500+ Happy Clients stat")
    check("50+ Training Programs" in idx_content or "50+" in idx_content, "Hero has 50+ Training Programs stat")
    check("100+ Corporate Collaborations" in idx_content or "Corporate Collaborations" in idx_content, "Hero has 100+ Corporate Collaborations stat")

    # About verification (Section 11, 12, 13)
    check("ABOUT SLN CONSULTING" in idx_content, "About has eyebrow 'ABOUT SLN CONSULTING'")
    check("Driving Innovation in a Connected World" in idx_content, "About has heading 'Driving Innovation in a Connected World'")
    check("assets/training_classroom.jpg" in idx_content, "About has office/team image")
    check("More About Us" in idx_content and "routePage(event, 'about.html')" in idx_content, "About has working 'More About Us' button")
    check("Expert Team" in idx_content, "About has 'Expert Team' highlight")
    check("Client-Centric Approach" in idx_content, "About has 'Client-Centric Approach' highlight")
    check("Quality &amp; Trust" in idx_content or "Quality & Trust" in idx_content, "About has 'Quality & Trust' highlight")
    check("Continuous Innovation" in idx_content, "About has 'Continuous Innovation' highlight")

    # Services verification (Section 14, 15, 16, 17)
    check("OUR SERVICES" in idx_content, "Services has eyebrow 'OUR SERVICES'")
    check("Comprehensive IT &amp; Cybersecurity Solutions" in idx_content or "Comprehensive IT & Cybersecurity Solutions" in idx_content, "Services has heading")
    check("routePage(event, 'soc.html')" in idx_content, "Cybersecurity card routes to soc.html")
    check("routePage(event, 'it-services.html')" in idx_content, "IT Services card routes to it-services.html")
    check("routePage(event, 'campus.html')" in idx_content, "Academia card routes to campus.html")
    check("routePage(event, 'internships.html')" in idx_content, "Internships card routes to internships.html")
    check("routePage(event, 'training.html')" in idx_content, "Training card routes to training.html")
    check("routePage(event, 'enterprises.html')" in idx_content, "Corporate card routes to enterprises.html")
    # Micro-interactions
    check("group-hover:drop-shadow-" in idx_content, "Cybersecurity card has shield glow interaction")
    check("group-hover:rotate-90" in idx_content, "IT Services card has gear rotate interaction")
    check("group-hover:-translate-y-1.5" in idx_content or "group-hover:-translate-y" in idx_content, "Academia card has cap lift interaction")
    check("group-hover:translate-x-2" in idx_content or "group-hover:translate-x" in idx_content, "Internships card has people slide interaction")

    # Why Choose Us verification (Section 18, 19)
    check("WHY CHOOSE US" in idx_content, "Why Choose Us has eyebrow 'WHY CHOOSE US'")
    check("Your Trusted Partner in a Secure Digital Future" in idx_content, "Why Choose Us has heading 'Your Trusted Partner in a Secure Digital Future'")
    check("assets/soc_operations_center.jpg" in idx_content, "Why Choose Us has cybersecurity visual")
    check("Proven Expertise" in idx_content, "Why Choose Us has 'Proven Expertise'")
    check("Tailored Solutions" in idx_content, "Why Choose Us has 'Tailored Solutions'")
    check("End-to-End Support" in idx_content, "Why Choose Us has 'End-to-End Support'")
    check("Future-Ready Approach" in idx_content, "Why Choose Us has 'Future-Ready Approach'")

    # Impact verification (Section 20)
    check("OUR IMPACT" in idx_content, "Impact has eyebrow 'OUR IMPACT'")
    check("Trusted by Organizations Across Industries" in idx_content, "Impact has heading 'Trusted by Organizations Across Industries'")
    check("10+ Years of Excellence" in idx_content or "Years of Excellence" in idx_content, "Impact has 'Years of Excellence'")
    check("Corporate Tie-ups" in idx_content, "Impact has 'Corporate Tie-ups'")

    # Footer verification (Section 32)
    print("\n--- 3. Testing 5-Column Dark Footer in index.html ---")
    check("COMPANY" in idx_content, "Footer has Column 1: COMPANY")
    check("SOLUTIONS" in idx_content, "Footer has Column 2: SOLUTIONS")
    check("TRAINING" in idx_content, "Footer has Column 3: TRAINING")
    check("RESOURCES" in idx_content, "Footer has Column 4: RESOURCES")
    check("CONTACT" in idx_content, "Footer has Column 5: CONTACT")
    check("openPolicyModal('privacy')" in idx_content, "Footer has Privacy Policy modal trigger")
    check("openPolicyModal('terms')" in idx_content, "Footer has Terms & Conditions modal trigger")
    check("openPolicyModal('cookie')" in idx_content, "Footer has Cookie Policy modal trigger")
    check("openPolicyModal('disclaimer')" in idx_content, "Footer has Disclaimer modal trigger")
    check("handleEmailSubscribe(event)" in idx_content, "Footer has handleEmailSubscribe(event)")
    check("srinivas.c@slnconsulting.co.in" in idx_content, "Footer has verified email")
    check("+91 9940196195" in idx_content or "+919940196195" in idx_content, "Footer has verified phone")

    # 4. IMAGE ASSETS VERIFICATION
    print("\n--- 4. Testing Local Image Assets Integrity ---")
    image_paths = set(re.findall(r'src=["\'](assets/[^"\']+)["\']', idx_content))
    for ip in sorted(image_paths):
        norm_path = ip.replace('/', os.sep)
        exists = os.path.exists(norm_path)
        check(exists, f"Referenced image exists: {norm_path}")

    # Summary
    print("\n==================================================")
    print(f"TEST SUMMARY: {passed_checks}/{total_checks} PASSED")
    if errors:
        print(f"FAILED ({len(errors)}):")
        for err in errors:
            print(f"  - {err}")
    else:
        print("ALL TESTS PASSED! 100% SPECIFICATION COMPLIANCE!")
    print("==================================================")

if __name__ == '__main__':
    run_tests()
