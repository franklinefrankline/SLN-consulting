from playwright.sync_api import sync_playwright
import time

offerings_to_test = [
    {
        'index': 1,
        'title': '01 SOC-As-A-Service',
        'card_id': 'card-soc',
        'view_id': 'view-soc',
        'arrow_selector': '#card-soc a[aria-label*="SOC"]',
    },
    {
        'index': 2,
        'title': '02 Skilling Solutions',
        'card_id': 'card-skilling',
        'view_id': 'view-skilling',
        'arrow_selector': '#card-skilling a[aria-label*="Skilling"]',
    },
    {
        'index': 3,
        'title': '03 Cambridge Learning',
        'card_id': 'card-cambridge',
        'view_id': 'view-cambridge',
        'arrow_selector': '#card-cambridge a[aria-label*="Cambridge"]',
    },
    {
        'index': 4,
        'title': '04 ISC2 Credentials',
        'card_id': 'card-isc2',
        'view_id': 'view-isc2',
        'arrow_selector': '#card-isc2 a[aria-label*="ISC2"]',
    },
    {
        'index': 5,
        'title': '05 EC-Council ATC',
        'card_id': 'card-ec-council',
        'view_id': 'view-ec-council',
        'arrow_selector': '#card-ec-council a[aria-label*="EC-Council"]',
    },
    {
        'index': 6,
        'title': '06 IT Services',
        'card_id': 'card-it-services',
        'view_id': 'view-it-services',
        'arrow_selector': '#card-it-services a[aria-label*="IT Services"]',
    }
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1400, 'height': 900})
    
    print("\n=======================================================")
    print("STARTING TEST: ALL 6 OFFERINGS BACK BUTTON & SCROLL RESTORATION")
    print("=======================================================\n")
    
    for item in offerings_to_test:
        idx = item['index']
        name = item['title']
        cid = item['card_id']
        vid = item['view_id']
        arrow_sel = item['arrow_selector']
        
        print(f"\n--- TESTING {name} ---")
        
        # 1. Start at main offerings page
        import os
        file_url = 'file:///' + os.path.abspath('offerings.html').replace('\\', '/')
        page.goto(file_url, wait_until='domcontentloaded')
        page.wait_for_timeout(300)
        
        # 2. Scroll to the card
        card = page.locator(f'#{cid}')
        card.scroll_into_view_if_needed()
        page.wait_for_timeout(400)
        
        pre_click_scroll = page.evaluate("() => window.scrollY")
        print(f"[{name}] Scrolled on main page to scrollY = {pre_click_scroll}")
        
        # 3. Click offering arrow
        arrow = page.locator(arrow_sel)
        arrow.click()
        page.wait_for_timeout(500)
        
        # 4. Verify detail view is active
        detail_view = page.locator(f'#{vid}')
        assert 'active' in (detail_view.get_attribute('class') or ''), f"{vid} is not active!"
        print(f"[{name}] Successfully entered detail view {vid}")
        
        # 5. Check Back to All Offerings button exists and is visible
        back_btn = page.locator(f'#{vid} a:has-text("Back to All Offerings")')
        assert back_btn.count() > 0, f"Back button missing on {vid}!"
        back_btn.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        assert back_btn.is_visible(), f"Back button is not visible on {vid}!"
        print(f"[{name}] 'Back to All Offerings' button is present and visible!")
        
        # 6. Click Back to All Offerings
        back_btn.click()
        page.wait_for_timeout(800)
        
        # 7. Verify main offerings page is active
        main_view = page.locator('#view-offerings')
        assert 'active' in (main_view.get_attribute('class') or ''), "view-offerings is not active after click!"
        
        # 8. Check restored scroll position
        post_click_scroll = page.evaluate("() => window.scrollY")
        card_rect_top = page.evaluate(f"() => document.getElementById('{cid}').getBoundingClientRect().top")
        print(f"[{name}] Returned to main page. scrollY = {post_click_scroll}. Card rect top = {card_rect_top}")
        
        # Verify it did NOT scroll to top (0) for items below the hero
        if idx > 1:
            assert post_click_scroll > 100, f"[{name}] FAILED: Returned to top of page (scrollY={post_click_scroll}) instead of restoring card position!"
        # Verify card is nicely in viewport
        assert -150 <= card_rect_top <= 300, f"[{name}] FAILED: Card is not centered/visible in viewport! rect top: {card_rect_top}"
        
        print(f"[{name}] PASS: Scroll position perfectly restored to {name} (card rect top={card_rect_top})!")
        
        # Save verification screenshot for Skilling Solutions
        if cid == 'card-skilling':
            page.screenshot(path='skilling_scroll_restored_verification.png')
            print("Saved skilling_scroll_restored_verification.png!")
            
    print("\n=======================================================")
    print("ALL 6 OFFERINGS PASSED SCROLL RESTORATION & BACK BUTTON TESTS!")
    print("=======================================================\n")
    browser.close()
