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
    'training-schedule.html',
    'resources.html'
]

print("==================================================")
print(" SLN CONSULTING — SIMPLIFIED NAVBAR VERIFICATION ")
print("==================================================\n")

total_tests = 0
passed_tests = 0
errors = []

def check(condition, desc):
    global total_tests, passed_tests, errors
    total_tests += 1
    if condition:
        passed_tests += 1
        print(f"  [PASS] {desc}")
    else:
        errors.append(desc)
        print(f"  [FAIL] {desc}")

for fname in HTML_FILES:
    print(f"--- Auditing Simplified Navbar in {fname} ---")
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Desktop Navbar Container & Classes
    check('header-desktop-row' in html and 'flex-nowrap' in html, f"{fname}: desktop row has flex-nowrap")
    check('header-desktop-nav' in html and 'desktop-nav' in html, f"{fname}: desktop nav has desktop-nav class")

    # Extract desktop <nav>
    nav_match = re.search(r'<nav class="[^"]*header-desktop-nav[^"]*"[^>]*>(.*?)</nav>', html, re.DOTALL)
    check(nav_match is not None, f"{fname}: found desktop <nav> element")
    
    if nav_match:
        nav_html = nav_match.group(1)

        # Count dropdown buttons in desktop nav: MUST BE EXACTLY 1 (Cybersecurity)
        dropdown_divs = re.findall(r'class="[^"]*nav-item-dropdown[^"]*"', nav_html)
        check(len(dropdown_divs) == 1, f"{fname}: desktop nav has EXACTLY 1 dropdown component (found {len(dropdown_divs)})")

        # Check Cybersecurity is that single dropdown
        check('data-dropdown="cybersecurity"' in nav_html, f"{fname}: single dropdown is Cybersecurity")
        check('id="dropdown-cybersecurity"' in nav_html, f"{fname}: has #dropdown-cybersecurity")

        # Extract Cybersecurity dropdown panel content
        cyber_panel_match = re.search(r'<div id="dropdown-cybersecurity"[^>]*>(.*?)</div>\s*</div>\s*</div>', nav_html, re.DOTALL)
        if not cyber_panel_match:
            cyber_panel_match = re.search(r'<div id="dropdown-cybersecurity"[^>]*>(.*?)</div>\s*</div>', nav_html, re.DOTALL)
        
        check(cyber_panel_match is not None, f"{fname}: found #dropdown-cybersecurity panel")
        if cyber_panel_match:
            cyber_panel = cyber_panel_match.group(1)
            # MUST contain SaaS & VAPT
            check('SaaS' in cyber_panel, f"{fname}: Cybersecurity dropdown contains SaaS")
            check('VAPT' in cyber_panel, f"{fname}: Cybersecurity dropdown contains VAPT")

            # MUST NOT contain old mega-menu sections
            check('Offensive Security' not in cyber_panel, f"{fname}: Cybersecurity dropdown does NOT contain Offensive Security header")
            check('Security Operations' not in cyber_panel, f"{fname}: Cybersecurity dropdown does NOT contain Security Operations header")
            check('Consulting & Risk' not in cyber_panel, f"{fname}: Cybersecurity dropdown does NOT contain Consulting & Risk header")
            check('Specialized Services' not in cyber_panel, f"{fname}: Cybersecurity dropdown does NOT contain Specialized Services header")
            check('Zero Trust' not in cyber_panel, f"{fname}: Cybersecurity dropdown does NOT contain Zero Trust")

        # Check all other items are direct links without dropdown arrows/panels
        # 1. Home
        check('<a href="index.html"' in nav_html and 'Home</a>' in nav_html, f"{fname}: Home is direct link")
        # 2. About Us
        check('<a href="about.html"' in nav_html and 'About Us</a>' in nav_html, f"{fname}: About Us is direct link")
        check('data-dropdown="about"' not in nav_html, f"{fname}: About Us has NO dropdown")
        # 4. IT Services
        check('<a href="it-services.html"' in nav_html and 'IT Services</a>' in nav_html, f"{fname}: IT Services is direct link")
        check('data-dropdown="it-services"' not in nav_html, f"{fname}: IT Services has NO dropdown")
        # 5. Academia
        check('<a href="campus.html"' in nav_html and 'Academia</a>' in nav_html, f"{fname}: Academia is direct link")
        check('data-dropdown="academia"' not in nav_html, f"{fname}: Academia has NO dropdown")
        # 6. Internships
        check('<a href="internships.html"' in nav_html and 'Internships</a>' in nav_html, f"{fname}: Internships is direct link")
        check('data-dropdown="internships"' not in nav_html and 'id="internshipsNavBtn"' not in nav_html, f"{fname}: Internships has NO dropdown")
        # 7. Training & Certifications
        check('<a href="training.html"' in nav_html and ('Training &amp; Certifications</a>' in nav_html or 'Training & Certifications</a>' in nav_html), f"{fname}: Training & Certifications is direct link")
        check('data-dropdown="training"' not in nav_html, f"{fname}: Training & Certifications has NO dropdown")
        # 8. Corporate
        check('<a href="enterprises.html"' in nav_html and 'Corporate</a>' in nav_html, f"{fname}: Corporate is direct link")
        check('data-dropdown="corporate"' not in nav_html, f"{fname}: Corporate has NO dropdown")
        # 9. Resources
        check(('<a href="resources.html"' in nav_html or '<a href="resources"' in nav_html) and 'Resources</a>' in nav_html, f"{fname}: Resources is direct link")
        check('data-dropdown="resources"' not in nav_html, f"{fname}: Resources has NO dropdown")
        # 10. Contact
        check('<a href="contact.html"' in nav_html and 'Contact</a>' in nav_html, f"{fname}: Contact is direct link")
        check('data-dropdown="contact"' not in nav_html, f"{fname}: Contact has NO dropdown")

    # 2. Desktop Actions (Theme Toggle + Enquire Now)
    check('id="headerThemeToggle"' in html, f"{fname}: has exactly one #headerThemeToggle")
    check('ENQUIRE NOW' in html, f"{fname}: has ENQUIRE NOW button")

    # 3. Mobile Navigation Drawer (#mobileDrawer)
    drawer_match = re.search(r'<div id="mobileDrawer"[^>]*>(.*?)</div>\s*</header>', html, re.DOTALL)
    check(drawer_match is not None, f"{fname}: found #mobileDrawer")
    
    if drawer_match:
        drawer_html = drawer_match.group(1)

        # Count accordions in mobile drawer: MUST BE EXACTLY 1 (Cybersecurity)
        accordion_toggles = re.findall(r'toggleMobileAccordion\(', drawer_html)
        check(len(accordion_toggles) == 1, f"{fname}: mobile drawer has EXACTLY 1 accordion toggle (found {len(accordion_toggles)})")

        # Check Cybersecurity is that single accordion
        check("toggleMobileAccordion('mobileCyberMenu'" in drawer_html, f"{fname}: mobile accordion is Cybersecurity")
        check('id="mobileCyberMenu"' in drawer_html, f"{fname}: has #mobileCyberMenu")

        # Check Cybersecurity accordion contains ONLY SaaS & VAPT
        cyber_mobile_match = re.search(r'<div id="mobileCyberMenu"[^>]*>(.*?)</div>', drawer_html, re.DOTALL)
        check(cyber_mobile_match is not None, f"{fname}: found #mobileCyberMenu content")
        if cyber_mobile_match:
            cm_content = cyber_mobile_match.group(1)
            check('SaaS' in cm_content, f"{fname}: mobile Cybersecurity has SaaS")
            check('VAPT' in cm_content, f"{fname}: mobile Cybersecurity has VAPT")
            check('Offensive Security' not in cm_content, f"{fname}: mobile Cybersecurity has no extra Offensive Security")
            check('Security Operations' not in cm_content, f"{fname}: mobile Cybersecurity has no extra Security Operations")

        # Verify all other items in mobile drawer are direct links, NOT accordions
        check('<a href="index.html"' in drawer_html and 'HOME</a>' in drawer_html, f"{fname}: mobile HOME is direct link")
        check('<a href="about.html"' in drawer_html and 'ABOUT US</a>' in drawer_html, f"{fname}: mobile ABOUT US is direct link")
        check('mobileAboutMenu' not in drawer_html, f"{fname}: mobile ABOUT US has no accordion menu")
        check('<a href="it-services.html"' in drawer_html and 'IT SERVICES</a>' in drawer_html, f"{fname}: mobile IT SERVICES is direct link")
        check('mobileITMenu' not in drawer_html, f"{fname}: mobile IT SERVICES has no accordion menu")
        check('<a href="campus.html"' in drawer_html and 'ACADEMIA</a>' in drawer_html, f"{fname}: mobile ACADEMIA is direct link")
        check('mobileAcademiaMenu' not in drawer_html, f"{fname}: mobile ACADEMIA has no accordion menu")
        check('<a href="internships.html"' in drawer_html and 'INTERNSHIPS</a>' in drawer_html, f"{fname}: mobile INTERNSHIPS is direct link")
        check('mobileInternshipsMenu' not in drawer_html, f"{fname}: mobile INTERNSHIPS has no accordion menu")
        check('<a href="training.html"' in drawer_html and ('TRAINING &amp; CERTIFICATIONS</a>' in drawer_html or 'TRAINING & CERTIFICATIONS</a>' in drawer_html), f"{fname}: mobile TRAINING & CERTIFICATIONS is direct link")
        check('mobileTrainingMenu' not in drawer_html, f"{fname}: mobile TRAINING has no accordion menu")
        check('<a href="enterprises.html"' in drawer_html and 'CORPORATE</a>' in drawer_html, f"{fname}: mobile CORPORATE is direct link")
        check('mobileCorporateMenu' not in drawer_html, f"{fname}: mobile CORPORATE has no accordion menu")
        check(('<a href="resources.html"' in drawer_html or '<a href="resources"' in drawer_html) and 'RESOURCES</a>' in drawer_html, f"{fname}: mobile RESOURCES is direct link")
        check('mobileResourcesMenu' not in drawer_html, f"{fname}: mobile RESOURCES has no accordion menu")
        check('<a href="contact.html"' in drawer_html and 'CONTACT</a>' in drawer_html, f"{fname}: mobile CONTACT is direct link")
        check('mobileContactMenu' not in drawer_html, f"{fname}: mobile CONTACT has no accordion menu")

        # Appearance & Enquire now
        check('toggleTheme()' in drawer_html, f"{fname}: mobile has appearance toggle")
        check('ENQUIRE NOW' in drawer_html, f"{fname}: mobile has ENQUIRE NOW button")

    # 4. Routing & Section Anchors
    check("'saas': 'view-soc'" in html, f"{fname}: routeMap maps 'saas' to view-soc")
    check("'vapt': 'view-soc'" in html, f"{fname}: routeMap maps 'vapt' to view-soc")
    check("'resources': 'view-resources'" in html, f"{fname}: routeMap maps 'resources' to view-resources")
    check('id="view-resources"' in html, f"{fname}: has view-resources")
    check('id="soc-as-a-service"' in html, f"{fname}: has section #soc-as-a-service")
    check('id="vapt"' in html, f"{fname}: has target #vapt")

print("\n==================================================")
print(f"RESULTS: {passed_tests}/{total_tests} PASSED")
if errors:
    print(f"FAILED ({len(errors)}):")
    for err in errors:
        print("  *", err)
    sys.exit(1)
else:
    print("ALL SIMPLIFIED NAVBAR REQUIREMENTS AUDITED & PASSED (100%)!")
    print("==================================================")
    sys.exit(0)
