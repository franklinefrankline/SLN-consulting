# test_direct_offerings_navigation.py
import os
import sys
from playwright.sync_api import sync_playwright

workspace = os.path.abspath(os.path.dirname(__file__))
artifact_dir = r"C:\Users\dhushyanth\.gemini\antigravity-ide\brain\a3f0dbb1-0b11-4467-af7c-72b2b2558fa9"
os.makedirs(artifact_dir, exist_ok=True)

print("======================================================================")
print("TESTING DIRECT OFFERINGS NAVIGATION & REMOVAL OF ALL OFFERINGS PAGE")
print("======================================================================\n")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1400, 'height': 900})

    # Test 1: DOM Audit on index.html
    print("--- TEST 1: Audit DOM on index.html ---")
    index_url = f"file:///{workspace.replace('\\', '/')}/index.html"
    page.goto(index_url, wait_until='networkidle')
    page.wait_for_timeout(400)

    # Confirm view-offerings is absent
    has_view_offerings = page.evaluate("() => !!document.getElementById('view-offerings')")
    assert not has_view_offerings, "FAILED: view-offerings should NOT exist in the DOM!"
    print("[PASS] view-offerings overview page is completely removed from the DOM.")

    # Confirm no "Back to All Offerings" button on index.html
    body_text = page.locator('body').inner_text()
    assert "Back to All Offerings" not in body_text, "FAILED: 'Back to All Offerings' found on index.html"
    assert "Previous Service" not in body_text, "FAILED: 'Previous Service' found on index.html"
    assert "Next Service" not in body_text, "FAILED: 'Next Service' found on index.html"
    print("[PASS] Zero 'Back to All Offerings', 'Previous Service', or 'Next Service' text found.")

    # Test 2: Direct Loading of All Detail Pages
    print("\n--- TEST 2: Direct Loading of Standalone Offering Pages ---")
    offerings_pages = [
        ('soc.html', 'view-soc', 'SOC-As-A-Service'),
        ('enterprises.html', 'view-enterprises', 'Enterprises'),
        ('campus.html', 'view-campus', 'Campus'),
        ('cambridge.html', 'view-cambridge', 'Cambridge Learning & Global Certifications'),
        ('isc2.html', 'view-isc2', 'ISC2 Credentials'),
        ('ec-council.html', 'view-ec-council', 'EC-Council (ATC)'),
        ('it-services.html', 'view-it-services', 'IT Services (8 Pillars)')
    ]

    for filename, view_id, expected_title in offerings_pages:
        file_url = f"file:///{workspace.replace('\\', '/')}/{filename}"
        page.goto(file_url, wait_until='networkidle')
        page.wait_for_timeout(300)

        # Check view is active
        is_active = page.evaluate(f"document.getElementById('{view_id}').classList.contains('active')")
        assert is_active, f"FAILED: {view_id} is not active on {filename}"

        # Check title / heading is visible
        heading = page.locator(f"#{view_id} :is(h1, h2)").first.inner_text()
        assert any(word in heading for word in expected_title.split()[:2]), f"Expected '{expected_title}' in heading, got '{heading}'"

        # Check NO "Back to All Offerings" button
        page_text = page.locator(f"#{view_id}").inner_text()
        assert "Back to All Offerings" not in page_text, f"FAILED: 'Back to All Offerings' found on {filename}!"
        assert "Previous Service" not in page_text, f"FAILED: 'Previous Service' found on {filename}!"
        assert "Next Service" not in page_text, f"FAILED: 'Next Service' found on {filename}!"

        # Check CTA section and footer are present
        cta_btn = page.locator(f"#{view_id} a[href='contact.html']")
        assert cta_btn.count() >= 1, f"Missing contact CTA on {filename}"

        print(f"[PASS] {filename} loads directly, displays '{expected_title}', has NO back button, and ends with clean CTA.")

    # Test 3: Dropdown 1-Click Direct Navigation from index.html
    print("\n--- TEST 3: Dropdown 1-Click Direct Navigation ---")
    page.goto(index_url, wait_until='networkidle')
    page.wait_for_timeout(300)

    # Hover over Our Offering
    page.hover('#offeringsMenuRoot')
    page.wait_for_timeout(200)

    dropdown_panel = page.locator('#offeringsDropdownPanel')
    assert dropdown_panel.is_visible(), "Dropdown panel is not visible on hover!"
    print("[PASS] Desktop dropdown opens on hover.")

    # Click 01 SOC
    print("Testing click on 01 SOC-As-A-Service...")
    page.click('#offeringsDropdownPanel a[href="soc.html"]')
    page.wait_for_timeout(300)
    assert page.evaluate("document.getElementById('view-soc').classList.contains('active')"), "Failed to open SOC view"
    print("[PASS] 1-Click opened SOC-As-A-Service directly.")

    # From SOC, open dropdown and click 03 Cambridge
    page.hover('#offeringsMenuRoot')
    page.wait_for_timeout(200)
    page.click('#offeringsDropdownPanel a[href="cambridge.html"]')
    page.wait_for_timeout(300)
    assert page.evaluate("document.getElementById('view-cambridge').classList.contains('active')"), "Failed to open Cambridge view"
    print("[PASS] 1-Click opened Cambridge Learning directly.")

    # From Cambridge, open dropdown, hover Skilling, click Enterprises
    page.hover('#offeringsMenuRoot')
    page.wait_for_timeout(200)
    page.hover('#skillingDropdownItem')
    page.wait_for_timeout(200)
    page.click('#navLinkEnterprises')
    page.wait_for_timeout(300)
    assert page.evaluate("document.getElementById('view-enterprises').classList.contains('active')"), "Failed to open Enterprises view"
    print("[PASS] 1-Click opened Enterprises directly from nested submenu.")

    # From Enterprises, open dropdown, hover Skilling, click Campus
    page.hover('#offeringsMenuRoot')
    page.wait_for_timeout(200)
    page.hover('#skillingDropdownItem')
    page.wait_for_timeout(200)
    page.click('#navLinkCampus')
    page.wait_for_timeout(300)
    assert page.evaluate("document.getElementById('view-campus').classList.contains('active')"), "Failed to open Campus view"
    print("[PASS] 1-Click opened Campus directly from nested submenu.")

    # From Campus, click 04 ISC2
    page.hover('#offeringsMenuRoot')
    page.wait_for_timeout(200)
    page.click('#offeringsDropdownPanel a[href="isc2.html"]')
    page.wait_for_timeout(300)
    assert page.evaluate("document.getElementById('view-isc2').classList.contains('active')"), "Failed to open ISC2 view"
    print("[PASS] 1-Click opened ISC2 Credentials directly.")

    # From ISC2, click 05 EC-Council
    page.hover('#offeringsMenuRoot')
    page.wait_for_timeout(200)
    page.click('#offeringsDropdownPanel a[href="ec-council.html"]')
    page.wait_for_timeout(300)
    assert page.evaluate("document.getElementById('view-ec-council').classList.contains('active')"), "Failed to open EC-Council view"
    print("[PASS] 1-Click opened EC-Council directly.")

    # From EC-Council, click 06 IT Services
    page.hover('#offeringsMenuRoot')
    page.wait_for_timeout(200)
    page.click('#offeringsDropdownPanel a[href="it-services.html"]')
    page.wait_for_timeout(300)
    assert page.evaluate("document.getElementById('view-it-services').classList.contains('active')"), "Failed to open IT Services view"
    print("[PASS] 1-Click opened IT Services directly.")

    # Screenshot of direct detail page
    shot_soc = os.path.join(artifact_dir, "verification_direct_offering_detail.png")
    page.screenshot(path=shot_soc)
    print(f"[SCREENSHOT] Saved {shot_soc}")

    # Test 4: Mobile Drawer Navigation (375 x 812)
    print("\n--- TEST 4: Mobile Drawer Navigation (375 x 812) ---")
    page.close()
    page_m = browser.new_page(viewport={'width': 375, 'height': 812})
    page_m.goto(index_url, wait_until='networkidle')
    page_m.wait_for_timeout(300)

    # Open mobile menu
    page_m.click('button[onclick="toggleMobileNav()"]')
    page_m.wait_for_timeout(200)

    # Expand offerings
    page_m.click('div[onclick="toggleMobileOfferingsMenu(event)"]')
    page_m.wait_for_timeout(200)
    assert page_m.locator('#mobileOfferingsSubmenu').is_visible(), "Mobile offerings submenu not visible!"

    # Check zero overflow on mobile
    scroll_w = page_m.evaluate("document.documentElement.scrollWidth")
    inner_w = page_m.evaluate("window.innerWidth")
    assert scroll_w <= inner_w, f"Mobile page overflowed: scrollWidth={scroll_w} > innerWidth={inner_w}"
    print(f"[PASS] Zero horizontal overflow on mobile drawer (scrollWidth={scroll_w}px).")

    # Click 01 SOC on mobile
    page_m.click('#mobileOfferingsSubmenu a[href="soc.html"]')
    page_m.wait_for_timeout(300)
    assert page_m.evaluate("document.getElementById('view-soc').classList.contains('active')"), "Failed to open SOC on mobile"
    print("[PASS] Mobile direct navigation to SOC-As-A-Service succeeded.")

    shot_m = os.path.join(artifact_dir, "verification_direct_offering_mobile.png")
    page_m.screenshot(path=shot_m)
    print(f"[SCREENSHOT] Saved {shot_m}")

    browser.close()

print("\n======================================================================")
print("ALL DIRECT OFFERINGS NAVIGATION TESTS PASSED WITH 100% SUCCESS!")
print("======================================================================")
