import os
import sys
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from playwright.sync_api import sync_playwright

def run_tests():
    file_path = os.path.abspath('index.html').replace('\\', '/')
    url = f'file:///{file_path}'
    print(f"Testing URL: {url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()

        # Load page
        page.goto(url)
        page.wait_for_load_state('domcontentloaded')
        time.sleep(1)

        print("\n--- TEST 1: Header Navigation Label and Dropdown Arrow ---")
        nav_btn = page.locator('#offeringsNavBtn')
        assert nav_btn.is_visible(), "Header navigation button #offeringsNavBtn not visible!"
        nav_text = nav_btn.inner_text().strip()
        print(f"Nav button text: '{nav_text}'")
        assert "Our Offering" in nav_text, f"Expected 'Our Offering' in nav text, got: {nav_text}"
        assert "Our Offerings" not in nav_text, f"'Our Offerings' found in nav text: {nav_text}"
        
        chevron = page.locator('#offeringsChevron')
        assert chevron.is_visible(), "Dropdown chevron arrow not visible!"
        print("[PASS] Header says 'Our Offering' and dropdown arrow is visible.")

        print("\n--- TEST 2: Dropdown Opens on Hover and Content Verification ---")
        root = page.locator('#offeringsMenuRoot')
        panel = page.locator('#offeringsDropdownPanel')
        
        # Hover over root
        root.hover()
        time.sleep(0.5)
        assert panel.is_visible(), "Dropdown panel did not become visible on hover!"
        
        # Check all 6 items
        items = panel.locator('a').all()
        assert len(items) == 6, f"Expected 6 items in dropdown, found {len(items)}"
        
        expected_items = [
            ("01", "SOC-As-A-Service"),
            ("02", "Skilling Solutions"),
            ("03", "Cambridge Learning & Global Certifications"),
            ("04", "ISC2 Credentials"),
            ("05", "EC-Council (ATC)"),
            ("06", "IT Services (8 Pillars)")
        ]
        
        for idx, (num, title) in enumerate(expected_items):
            item_text = items[idx].inner_text().strip()
            print(f"Dropdown item {idx+1}: {item_text}")
            assert num in item_text, f"Missing number {num} in '{item_text}'"
            assert title in item_text, f"Missing title {title} in '{item_text}'"
        print("[PASS] Dropdown opens on hover and contains all 6 items exactly.")

        print("\n--- TEST 3: Click 'Our Offering' Text directly opens Main Overview Page in 1 Click ---")
        # Ensure we are on home first
        assert page.locator('#view-index').is_visible()
        # Click the text of the link
        nav_btn.locator('span').first.click()
        time.sleep(0.5)
        assert page.locator('#view-offerings').is_visible(), "Main offerings page view-offerings not visible after clicking Our Offering!"
        assert not page.locator('#view-index').is_visible(), "Home view should not be visible!"
        print("[PASS] Clicking 'Our Offering' opens main overview page directly in 1 click without redirecting through home.")

        print("\n--- TEST 4: Main Page says 'OUR OFFERING' (not 'OUR OFFERINGS') ---")
        label = page.locator('#view-offerings span.font-mono.tracking-widest').first.inner_text().strip()
        print(f"Main page badge label: '{label}'")
        assert label == "OUR OFFERING", f"Expected 'OUR OFFERING', got '{label}'"
        print("[PASS] Main overview page label is exactly 'OUR OFFERING'.")

        print("\n--- TEST 5: Verify All Six Offering Cards on Main Page ---")
        cards = ['card-soc', 'card-skilling', 'card-cambridge', 'card-isc2', 'card-ec-council', 'card-it-services']
        for c in cards:
            assert page.locator(f'#{c}').count() == 1, f"Card #{c} missing!"
        print("[PASS] All 6 offering sections exist on main overview page.")

        print("\n--- TEST 6: Dropdown Items open Detail Pages in 1 Click ---")
        test_routes = [
            ("SOC-As-A-Service", "#view-soc"),
            ("Skilling Solutions", "#view-skilling"),
            ("Cambridge Learning & Global Certifications", "#view-cambridge"),
            ("ISC2 Credentials", "#view-isc2"),
            ("EC-Council (ATC)", "#view-ec-council"),
            ("IT Services (8 Pillars)", "#view-it-services")
        ]
        
        for name, view_selector in test_routes:
            # Hover to open dropdown
            root.hover()
            time.sleep(0.3)
            # Click dropdown item
            item = panel.locator(f"text={name}").first
            item.click()
            time.sleep(0.5)
            assert page.locator(view_selector).is_visible(), f"{view_selector} not visible after clicking {name}!"
            assert not page.locator('#view-index').is_visible(), "Home view should not be visible!"
            print(f"  [PASS] Dropdown '{name}' directly opened {view_selector}")

        print("\n--- TEST 7: Detail Page 'Back to All Offerings' & Scroll Restoration ---")
        # Go to main offerings page
        nav_btn.locator('span').first.click()
        time.sleep(0.5)
        assert page.locator('#view-offerings').is_visible()

        # Scroll to Cambridge card
        cambridge_card = page.locator('#card-cambridge')
        cambridge_card.scroll_into_view_if_needed()
        time.sleep(0.5)
        scrollY_before = page.evaluate("window.scrollY")
        print(f"Scroll position before clicking Cambridge: {scrollY_before}")
        assert scrollY_before > 300, "Page should have scrolled down to Cambridge!"

        # Click Cambridge arrow to open detail page
        cambridge_card.locator('a').first.click()
        time.sleep(0.5)
        assert page.locator('#view-cambridge').is_visible(), "Cambridge detail view not visible!"

        # Verify Back to All Offerings button exists
        back_btn = page.locator('#view-cambridge a:has-text("Back to All Offerings")')
        assert back_btn.is_visible(), "'Back to All Offerings' button not visible!"

        # Verify NO Previous Service / Next Service buttons
        assert page.locator('#view-cambridge a:has-text("Previous Service")').count() == 0, "Found Previous Service!"
        assert page.locator('#view-cambridge a:has-text("Next Service")').count() == 0, "Found Next Service!"
        print("[PASS] 'Back to All Offerings' exists and no Previous/Next service buttons exist.")

        # Click Back to All Offerings
        back_btn.click()
        time.sleep(1.0)
        assert page.locator('#view-offerings').is_visible(), "Not returned to view-offerings!"
        scrollY_after = page.evaluate("window.scrollY")
        print(f"Scroll position after clicking Back to All Offerings: {scrollY_after}")
        diff = abs(scrollY_after - scrollY_before)
        print(f"Scroll position delta: {diff}px")
        assert diff < 200, f"Scroll position was not restored to Cambridge card! Delta: {diff}px"
        print("[PASS] Scroll position was accurately restored to the Cambridge card position!")

        print("\n--- TEST 8: Mobile Dropdown / Expandable Navigation ---")
        # Switch to mobile viewport
        page.set_viewport_size({'width': 375, 'height': 812})
        time.sleep(0.5)

        # Open mobile drawer
        menu_toggle = page.locator('button[aria-label="Toggle mobile menu"]')
        menu_toggle.click()
        time.sleep(0.5)
        drawer = page.locator('#mobileDrawer')
        assert drawer.is_visible(), "Mobile drawer did not open!"

        # Check mobile 'Our Offering' item
        mob_label = drawer.locator('text=Our Offering').first
        assert mob_label.is_visible(), "Mobile 'Our Offering' text not visible!"

        # Expand submenu
        mob_chev_btn = page.locator('#mobileOfferingsToggleBtn')
        mob_sub = page.locator('#mobileOfferingsSubmenu')
        assert not mob_sub.is_visible(), "Mobile submenu should initially be hidden!"
        mob_chev_btn.click()
        time.sleep(0.3)
        assert mob_sub.is_visible(), "Mobile submenu did not expand!"

        # Check all 6 items on mobile
        mob_items = mob_sub.locator('a').all()
        assert len(mob_items) == 6, f"Expected 6 items in mobile submenu, found {len(mob_items)}"
        
        # Check horizontal overflow
        has_h_overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
        assert not has_h_overflow, "Horizontal overflow detected on mobile!"
        print("[PASS] Mobile expandable menu works smoothly without horizontal overflow.")

        # Click a mobile item, e.g. Skilling Solutions
        mob_sub.locator('text=Skilling Solutions').click()
        time.sleep(0.5)
        assert page.locator('#view-skilling').is_visible(), "Mobile navigation did not open Skilling Solutions detail!"
        print("[PASS] Mobile item opens detail view in 1 click.")

        # Take verification screenshot
        page.screenshot(path="verification_mobile_detail.png")

        # Switch back to desktop and take screenshot of dropdown open
        page.set_viewport_size({'width': 1280, 'height': 800})
        time.sleep(0.5)
        page.locator('#offeringsNavBtn').locator('span').first.click()
        time.sleep(0.5)
        page.locator('#offeringsMenuRoot').hover()
        time.sleep(0.5)
        page.screenshot(path="verification_desktop_dropdown.png")
        print("[PASS] Screenshots captured.")

        browser.close()

    print("\n==========================================")
    print("ALL 12 VERIFICATION TESTS PASSED PERFECTLY!")
    print("==========================================")

if __name__ == '__main__':
    run_tests()
