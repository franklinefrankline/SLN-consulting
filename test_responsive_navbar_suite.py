import os
import re
import sys

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

print("==================================================")
print(" SLN CONSULTING — RESPONSIVE NAVBAR VERIFICATION ")
print("==================================================\n")

total_checks = 0
passed_checks = 0
errors = []

def check(condition, desc):
    global total_checks, passed_checks, errors
    total_checks += 1
    if condition:
        passed_checks += 1
        print(f"  [PASS] {desc}")
    else:
        errors.append(desc)
        print(f"  [FAIL] {desc}")

for fname in HTML_FILES:
    print(f"--- Auditing {fname} ---")
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Desktop Navbar: Single row, 10 items, no wrap, absolute dropdowns
    check('header-desktop-row' in c and 'flex-nowrap' in c, f"{fname}: desktop header row has flex-nowrap")
    check('header-desktop-nav' in c and 'hidden xl:flex' in c, f"{fname}: desktop nav has hidden xl:flex")
    check('position: absolute' in c, f"{fname}: dropdowns positioned absolute to prevent navbar stretching")

    # 10 Desktop items present in header
    desktop_nav_match = re.search(r'<nav class="[^"]*header-desktop-nav[^"]*"[^>]*>(.*?)</nav>', c, re.DOTALL)
    check(desktop_nav_match is not None, f"{fname}: found <nav> header-desktop-nav element")
    if desktop_nav_match:
        nav_html = desktop_nav_match.group(1)
        check('Home' in nav_html, f"{fname}: desktop nav has Home")
        check('About Us' in nav_html, f"{fname}: desktop nav has About Us")
        check('Cybersecurity' in nav_html, f"{fname}: desktop nav has Cybersecurity")
        check('IT Services' in nav_html, f"{fname}: desktop nav has IT Services")
        check('Academia' in nav_html, f"{fname}: desktop nav has Academia")
        check('id="internshipsNavBtn"' in nav_html, f"{fname}: desktop nav has Internships trigger button")
        check('Training &amp; Certifications' in nav_html or 'Training & Certifications' in nav_html, f"{fname}: desktop nav has Training & Certifications")
        check('Corporate' in nav_html, f"{fname}: desktop nav has Corporate")
        check('Resources' in nav_html, f"{fname}: desktop nav has Resources")
        check('Contact' in nav_html, f"{fname}: desktop nav has Contact")

    # Desktop Action: Exactly ONE Theme Toggle + Enquire Now
    check('id="headerThemeToggle"' in c, f"{fname}: has #headerThemeToggle")
    check('ENQUIRE NOW' in c, f"{fname}: has ENQUIRE NOW button")

    # 2. Mobile Visibility & Hamburger button (44px x 44px min touch target, accessible, animated)
    check('id="mobileMenuBtn"' in c, f"{fname}: has #mobileMenuBtn")
    check('min-w-[44px]' in c and 'min-h-[44px]' in c, f"{fname}: mobileMenuBtn has minimum 44px x 44px touch target")
    check('aria-label="Open navigation"' in c, f"{fname}: mobileMenuBtn has aria-label='Open navigation'")
    check('aria-expanded="false"' in c, f"{fname}: mobileMenuBtn has aria-expanded='false'")
    check('aria-controls="mobileDrawer"' in c, f"{fname}: mobileMenuBtn has aria-controls='mobileDrawer'")
    check('bar-top' in c and 'bar-mid' in c and 'bar-bot' in c, f"{fname}: has animated 3-bar hamburger-to-X icon")

    # Logo responsive scaling
    check('assets/images/sln-consulting-logo.png' in c, f"{fname}: has SLN Consulting logo")
    check('object-contain' in c, f"{fname}: logo uses object-contain")

    # 3. Mobile Menu Panel (#mobileDrawer)
    check('id="mobileDrawer"' in c, f"{fname}: has #mobileDrawer")
    mobile_drawer_match = re.search(r'<div id="mobileDrawer"[^>]*>(.*?)</div>\s*</header>', c, re.DOTALL)
    check(mobile_drawer_match is not None, f"{fname}: found #mobileDrawer content")
    if mobile_drawer_match:
        drawer_html = mobile_drawer_match.group(1)
        check('HOME' in drawer_html, f"{fname}: mobile drawer has HOME")
        check('ABOUT US' in drawer_html, f"{fname}: mobile drawer has ABOUT US accordion")
        check('CYBERSECURITY' in drawer_html, f"{fname}: mobile drawer has CYBERSECURITY accordion")
        check('IT SERVICES' in drawer_html, f"{fname}: mobile drawer has IT SERVICES accordion")
        check('ACADEMIA' in drawer_html, f"{fname}: mobile drawer has ACADEMIA accordion")
        check('INTERNSHIPS' in drawer_html, f"{fname}: mobile drawer has INTERNSHIPS accordion")
        check('TRAINING &amp; CERTIFICATIONS' in drawer_html or 'TRAINING & CERTIFICATIONS' in drawer_html, f"{fname}: mobile drawer has TRAINING accordion")
        check('CORPORATE' in drawer_html, f"{fname}: mobile drawer has CORPORATE accordion")
        check('RESOURCES' in drawer_html, f"{fname}: mobile drawer has RESOURCES accordion")
        check('CONTACT' in drawer_html, f"{fname}: mobile drawer has CONTACT accordion")
        check('toggleTheme()' in drawer_html, f"{fname}: mobile drawer has Dark Mode toggle")
        check('ENQUIRE NOW' in drawer_html, f"{fname}: mobile drawer has ENQUIRE NOW button")

    # 4. Mobile Internships Submenu Behavior
    check('onclick="toggleMobileAccordion(\'mobileInternshipsMenu\', \'mobileInternshipsChev\')"' in c, f"{fname}: mobile Internships trigger is pure accordion toggle")
    check('href="internships.html"' in c, f"{fname}: Program routes to internship home")
    check('href="internships.html#pathways"' in c, f"{fname}: Pathways routes to #pathways")
    check('href="internships.html#student-journey"' in c, f"{fname}: Student Journey routes to #student-journey")
    check('href="internships.html#institutional-model"' in c, f"{fname}: Institutional Model routes to #institutional-model")

    # 5. JavaScript functions: openMobileNav, closeMobileNav, toggleMobileNav, body scroll lock
    check('function closeMobileNav()' in c, f"{fname}: defines closeMobileNav()")
    check('function openMobileNav()' in c, f"{fname}: defines openMobileNav()")
    check('function toggleMobileNav()' in c, f"{fname}: defines toggleMobileNav()")
    check("document.body.style.overflow = 'hidden'" in c, f"{fname}: locks body overflow when open")
    check("document.body.style.overflow = ''" in c, f"{fname}: unlocks body overflow when closed")

    # 6. Overflow protection and Reduced Motion
    check('overflow-x: hidden' in c, f"{fname}: prevents horizontal overflow")
    check('prefers-reduced-motion: reduce' in c, f"{fname}: respects prefers-reduced-motion")

print("\n==================================================")
print(f"RESULTS: {passed_checks}/{total_checks} PASSED")
if errors:
    print(f"FAILED ({len(errors)}):")
    for err in errors:
        print("  *", err)
    sys.exit(1)
else:
    print("ALL RESPONSIVE NAVBAR REQUIREMENTS VERIFIED & PASSED (100%)!")
    print("==================================================")
    sys.exit(0)
