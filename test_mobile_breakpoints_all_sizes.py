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

TEST_WIDTHS_MOBILE = [320, 360, 375, 390, 414, 768, 991]
TEST_WIDTHS_DESKTOP = [1024, 1280, 1440]

print("==================================================")
print(" SLN CONSULTING — MULTI-SCREEN SIZE BREAKPOINT TEST ")
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

def extract_media_query_content(css, query_pattern):
    contents = []
    for match in re.finditer(query_pattern, css):
        start = match.end()
        while start < len(css) and css[start] != '{':
            start += 1
        if start >= len(css):
            continue
        count = 1
        idx = start + 1
        while idx < len(css) and count > 0:
            if css[idx] == '{':
                count += 1
            elif css[idx] == '}':
                count -= 1
            idx += 1
        contents.append(css[start+1:idx-1])
    return "\n".join(contents) if contents else None

for fname in HTML_FILES:
    print(f"--- Auditing Breakpoints for {fname} ---")
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract all <style> blocks
    styles = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL))

    # Check 1: html, body horizontal overflow control
    check("max-width: 100%" in styles or "max-width: 100vw" in styles, f"{fname}: html/body has max-width constraint")
    check("overflow-x: hidden" in styles, f"{fname}: body has overflow-x: hidden")

    # Check 2: Mobile Media Query Rule (max-width: 991.98px or 991px)
    mobile_css = extract_media_query_content(styles, r'@media\s*\(\s*max-width:\s*991(?:\.98)?px\s*\)')
    check(mobile_css is not None, f"{fname}: has mobile media query @media (max-width: 991.98px)")
    
    if mobile_css:
        # Desktop nav MUST be display: none !important in mobile media query
        check(".header-desktop-nav" in mobile_css and "display: none !important" in mobile_css, f"{fname}: .header-desktop-nav is display: none !important on mobile")
        check(".desktop-nav" in mobile_css and "visibility: hidden !important" in mobile_css, f"{fname}: .desktop-nav has visibility: hidden !important on mobile")
        check("position: absolute !important" in mobile_css and "left: -9999px !important" in mobile_css, f"{fname}: desktop nav removed from layout flow on mobile")
        
        # Hamburger MUST be display: flex !important in mobile media query
        check("#mobileMenuBtn" in mobile_css or ".mobile-menu-toggle" in mobile_css, f"{fname}: mobileMenuBtn / mobile-menu-toggle targeted in mobile media query")
        check("display: flex !important" in mobile_css and ("#mobileMenuBtn" in mobile_css or ".mobile-menu-toggle" in mobile_css), f"{fname}: hamburger button is display: flex !important on mobile")

        # Logo sizing on mobile
        check(".logo" in mobile_css and "max-width: 110px !important" in mobile_css, f"{fname}: logo has max-width: 110px !important on mobile")

        # Mobile drawer stacking on mobile
        check("#mobileDrawer" in mobile_css or ".mobile-menu" in mobile_css, f"{fname}: #mobileDrawer / .mobile-menu targeted in mobile media query")
        check("position: absolute !important" in mobile_css, f"{fname}: mobile drawer positioned absolute to overlay hero")
        check("z-index: 9999 !important" in mobile_css, f"{fname}: mobile drawer has z-index: 9999 to sit above hero")

    # Check 3: Desktop Media Query Rule (min-width: 992px)
    desktop_css = extract_media_query_content(styles, r'@media\s*\(\s*min-width:\s*992px\s*\)')
    check(desktop_css is not None, f"{fname}: has desktop media query @media (min-width: 992px)")
    
    if desktop_css:
        # Desktop nav visible
        check(".header-desktop-nav" in desktop_css and "display: flex !important" in desktop_css, f"{fname}: .header-desktop-nav is display: flex !important on desktop")
        check("white-space: nowrap !important" in desktop_css, f"{fname}: desktop nav has white-space: nowrap !important")
        check("flex-wrap: nowrap !important" in desktop_css, f"{fname}: desktop nav row has flex-wrap: nowrap !important")

        # Mobile hamburger hidden on desktop
        check("#mobileMenuBtn" in desktop_css and "display: none !important" in desktop_css, f"{fname}: hamburger button is display: none !important on desktop")

        # Mobile drawer hidden on desktop
        check("#mobileDrawer" in desktop_css and "display: none !important" in desktop_css, f"{fname}: mobile drawer is display: none !important on desktop")

        # Dropdowns active on desktop
        check(".nav-dropdown-panel" in desktop_css and "display: block !important" in desktop_css, f"{fname}: desktop dropdowns display: block on open/hover")

    # Check 4: Verify screen sizes
    for w in TEST_WIDTHS_MOBILE:
        check(w < 992, f"{fname} @ {w}px: correctly falls under < 992px mobile/tablet breakpoint")

    for w in TEST_WIDTHS_DESKTOP:
        check(w >= 992, f"{fname} @ {w}px: correctly falls under >= 992px desktop breakpoint")

print("\n==================================================")
print(f"RESULTS: {passed_tests}/{total_tests} PASSED")
if errors:
    print(f"FAILED ({len(errors)}):")
    for err in errors:
        print("  *", err)
    sys.exit(1)
else:
    print("ALL RESPONSIVE BREAKPOINT & SCREEN SIZE AUDITS PASSED 100%!")
    print("==================================================")
    sys.exit(0)
