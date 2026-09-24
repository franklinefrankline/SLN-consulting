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

        page.goto(url)
        page.wait_for_load_state('domcontentloaded')
        time.sleep(1)

        print("\n==================== TEST 1: ALL IMAGES LOAD LOCALLY (OFFLINE) ====================")
        imgs = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('img')).map(img => ({
                src: img.getAttribute('src'),
                alt: img.alt,
                w: img.naturalWidth,
                h: img.naturalHeight,
                complete: img.complete
            }));
        }""")
        print(f"Total img tags evaluated: {len(imgs)}")
        broken = [img for img in imgs if img['w'] == 0]
        assert len(broken) == 0, f"Found {len(broken)} broken images: {broken}"
        for img in imgs:
            assert not img['src'].startswith('http'), f"External image found: {img['src']}"
            assert img['src'].startswith('assets/'), f"Image not in assets/ directory: {img['src']}"
        print(f"[PASS] All {len(imgs)} images load locally with naturalWidth > 0 and correct relative paths.")

        print("\n==================== TEST 2: HEADER NAVIGATION & DROPDOWN ====================")
        nav_btn = page.locator('#offeringsNavBtn')
        assert nav_btn.is_visible(), "Header navigation button #offeringsNavBtn not visible!"
        nav_text = nav_btn.inner_text().strip()
        print(f"Nav button text: '{nav_text}'")
        assert "Our Offering" in nav_text, f"Expected 'Our Offering' in nav text, got: {nav_text}"
        assert "Our Offerings" not in nav_text, f"'Our Offerings' found in nav text: {nav_text}"
        
        chevron = page.locator('#offeringsChevron')
        assert chevron.is_visible(), "Dropdown chevron arrow not visible!"
        print("[PASS] Header says 'Our Offering' with visible chevron arrow.")

        print("\n==================== TEST 3: MAIN DROPDOWN & 6 OFFERINGS ====================")
        root = page.locator('#offeringsMenuRoot')
        panel = page.locator('#offeringsDropdownPanel')
        
        # Hover over root
        root.hover()
        time.sleep(0.4)
        assert panel.is_visible(), "Dropdown panel did not become visible on hover!"
        
        # Check SOC
        assert panel.locator('a:has-text("SOC-As-A-Service")').is_visible()
        # Check Skilling Solutions
        assert panel.locator('#skillingNavMainLink').is_visible()
        # Check Cambridge
        assert panel.locator('a:has-text("Cambridge Learning & Global Certifications")').is_visible()
        # Check ISC2
        assert panel.locator('a:has-text("ISC2 Credentials")').is_visible()
        # Check EC-Council
        assert panel.locator('a:has-text("EC-Council (ATC)")').is_visible()
        # Check IT Services
        assert panel.locator('a:has-text("IT Services (8 Pillars)")').is_visible()
        print("[PASS] Main dropdown contains all 6 offerings.")

        print("\n==================== TEST 4: NESTED SKILLING SOLUTIONS SUBMENU ====================")
        skilling_item = page.locator('#skillingDropdownItem')
        skilling_item.hover()
        time.sleep(0.3)
        
        desk_sub = page.locator('#desktopSkillingSubmenu')
        assert desk_sub.is_visible(), "Desktop Skilling nested submenu not visible on hover!"
        
        ent_link = desk_sub.locator('#navLinkEnterprises')
        camp_link = desk_sub.locator('#navLinkCampus')
        assert ent_link.is_visible(), "Enterprises link not visible in Skilling submenu!"
        assert camp_link.is_visible(), "Campus link not visible in Skilling submenu!"
        print(f"Nested links: '{ent_link.inner_text().strip()}' and '{camp_link.inner_text().strip()}'")
        print("[PASS] Skilling Solutions has nested Enterprises and Campus submenu.")

        print("\n==================== TEST 5: SKILLING NAVIGATION TARGETS ====================")
        # Click Enterprises directly while submenu is open
        ent_link.click()
        time.sleep(0.8)
        assert page.locator('#view-enterprises').is_visible(), "view-enterprises should be visible after Enterprises click!"
        ent_text = page.locator('#view-enterprises').inner_text()
        assert "WORKSHOPS & WEBINARS FOR MID & SENIOR MANAGERS" in ent_text, f"Expected workshops in enterprises, got: {ent_text[:100]}"
        print("[PASS] Enterprises navigates to dedicated Enterprises page with full executive workshops.")

        # Reopen dropdown and click Campus
        nav_btn.hover()
        time.sleep(0.4)
        skilling_item.hover()
        time.sleep(0.4)
        camp_link = page.locator('#desktopSkillingSubmenu #navLinkCampus')
        camp_link.click()
        time.sleep(0.8)
        assert page.locator('#view-campus').is_visible(), "view-campus should be visible after Campus click!"
        camp_text = page.locator('#view-campus').inner_text()
        assert "Defining Career path" in camp_text, f"Expected 'Defining Career path' in campus, got: {camp_text[:100]}"
        print("[PASS] Campus navigates to dedicated Campus page with 6 offerings.")

        # Reopen dropdown and click Skilling Solutions main link
        nav_btn.hover()
        time.sleep(0.4)
        main_skilling_link = page.locator('#skillingNavMainLink')
        main_skilling_link.click()
        time.sleep(0.8)
        assert page.locator('#view-skilling').is_visible()
        print("[PASS] Skilling Solutions itself remains clickable and opens main Skilling detail page.")

        print("\n==================== TEST 6: CLICKING 'OUR OFFERING' DIRECTLY ====================")
        # Click Our Offering main button text
        nav_btn.locator('span').first.click()
        time.sleep(0.6)
        assert page.locator('#view-offerings').is_visible(), "Main offerings overview page not visible!"
        label = page.locator('#view-offerings span.font-mono.tracking-widest').first.inner_text().strip()
        assert label == "OUR OFFERING", f"Expected 'OUR OFFERING', got '{label}'"
        print("[PASS] Clicking 'Our Offering' opens main overview page with label 'OUR OFFERING'.")

        print("\n==================== TEST 7: ALL DETAIL PAGES & BACK BUTTON ====================")
        offerings_checks = [
            ("SOC-As-A-Service", "view-soc", "card-soc"),
            ("Cambridge Learning & Global Certifications", "view-cambridge", "card-cambridge"),
            ("ISC2 Credentials", "view-isc2", "card-isc2"),
            ("EC-Council (ATC)", "view-ec-council", "card-ec-council"),
            ("IT Services (8 Pillars)", "view-it-services", "card-it-services"),
        ]
        
        for name, view_id, card_id in offerings_checks:
            root.hover()
            time.sleep(0.3)
            panel.locator(f'a:has-text("{name}")').click()
            time.sleep(0.6)
            assert page.locator(f'#{view_id}').is_visible(), f"Detail page #{view_id} not visible!"
            
            # Verify Back to All Offerings
            back_btn = page.locator(f'#{view_id} a:has-text("Back to All Offerings")')
            assert back_btn.count() == 1, f"Missing Back to All Offerings button in #{view_id}"
            
            # Verify NO Previous / Next Service
            assert page.locator(f'#{view_id} a:has-text("Previous Service")').count() == 0, f"Found Previous Service in #{view_id}"
            assert page.locator(f'#{view_id} a:has-text("Next Service")').count() == 0, f"Found Next Service in #{view_id}"

            # Click Back to All Offerings
            back_btn.click()
            time.sleep(0.6)
            assert page.locator('#view-offerings').is_visible(), f"Failed to return to view-offerings from #{view_id}"

        print("[PASS] All offerings detail pages work in 1 click, have 'Back to All Offerings', and have NO Previous/Next Service.")

        print("\n==================== TEST 8: MOBILE NAVIGATION & NESTED SKILLING ====================")
        page.set_viewport_size({'width': 375, 'height': 812})
        time.sleep(0.5)

        # Open mobile hamburger menu
        mob_btn = page.locator('#mobileMenuBtn')
        mob_btn.click()
        time.sleep(0.5)
        assert page.locator('#mobileDrawer').is_visible(), "Mobile drawer not visible!"

        # Toggle mobile offerings submenu
        mob_off_toggle = page.locator('#mobileOfferingsToggleBtn')
        mob_off_toggle.click()
        time.sleep(0.4)
        mob_off_sub = page.locator('#mobileOfferingsSubmenu')
        assert mob_off_sub.is_visible(), "Mobile offerings submenu not visible!"

        # Toggle mobile skilling nested submenu
        mob_skill_toggle = page.locator('#mobileSkillingToggleBtn')
        assert mob_skill_toggle.is_visible(), "Mobile Skilling toggle button not visible!"
        mob_skill_toggle.click()
        time.sleep(0.4)
        mob_skill_sub = page.locator('#mobileSkillingSubmenu')
        assert mob_skill_sub.is_visible(), "Mobile Skilling nested submenu not visible!"

        # Check Enterprises & Campus in mobile
        m_ent = mob_skill_sub.locator('a:has-text("Enterprises")')
        m_camp = mob_skill_sub.locator('a:has-text("Campus")')
        assert m_ent.is_visible(), "Mobile Enterprises link not visible!"
        assert m_camp.is_visible(), "Mobile Campus link not visible!"

        # Check horizontal overflow
        has_h_overflow = page.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth")
        assert not has_h_overflow, "Horizontal overflow detected on mobile!"
        print("[PASS] Mobile drawer, expandable Our Offering, and nested Skilling submenu work with zero horizontal overflow.")

        # Click Enterprises on mobile
        m_ent.click()
        time.sleep(0.6)
        assert page.locator('#view-enterprises').is_visible(), "view-enterprises not visible after mobile Enterprises click!"
        print("[PASS] Mobile Enterprises click works cleanly.")

        # Take screenshot of mobile view
        page.screenshot(path="verification_mobile_nested.png")

        # Set back to desktop and take screenshot of dropdown
        page.set_viewport_size({'width': 1280, 'height': 800})
        time.sleep(0.5)
        root.hover()
        time.sleep(0.3)
        skilling_item.hover()
        time.sleep(0.3)
        page.screenshot(path="verification_desktop_nested_dropdown.png")

        browser.close()

    print("\n==================== ALL VERIFICATION TESTS PASSED SUCCESSFULLY! ====================")

if __name__ == '__main__':
    run_tests()
