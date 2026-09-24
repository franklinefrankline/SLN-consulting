from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    
    print("Navigating to http://localhost:8080/offerings.html ...")
    page.goto('http://localhost:8080/offerings.html', wait_until='networkidle')
    page.wait_for_timeout(1000)

    # 1. Main showcase active
    assert page.locator('#view-offerings').is_visible(), "view-offerings is not visible!"

    # 2. Check 6 offerings titles & numbering on showcase
    body_text = page.locator('#view-offerings').inner_text()
    assert "01" in body_text and "SOC-As-A-Service" in body_text, "01 SOC-As-A-Service missing from showcase!"
    assert "02" in body_text and "Skilling Solutions" in body_text, "02 Skilling Solutions missing from showcase!"
    assert "03" in body_text and "Cambridge Learning" in body_text, "03 Cambridge missing from showcase!"
    assert "04" in body_text and "ISC2 Credentials" in body_text, "04 ISC2 Credentials missing from showcase!"
    assert "05" in body_text and "EC-Council (ATC)" in body_text, "05 EC-Council (ATC) missing from showcase!"
    assert "06" in body_text and "IT Services (8 Pillars)" in body_text, "06 IT Services missing from showcase!"
    print("[OK] All 6 offerings present on main showcase!")

    # 3. Check NO dropdown under Our Offerings
    assert page.locator('#servicesMenuRoot').count() == 0, "Dropdown menu root found!"
    assert page.locator('#servicesDropdownPanel').count() == 0 or not page.locator('#servicesDropdownPanel').is_visible(), "Dropdown panel found!"
    print("[OK] Header has direct link with NO dropdown!")

    # 4. Check NO Previous / Next Service anywhere
    full_text = page.locator('body').inner_text()
    assert "PREVIOUS SERVICE" not in full_text, "PREVIOUS SERVICE text found!"
    assert "NEXT SERVICE" not in full_text, "NEXT SERVICE text found!"
    print("[OK] Previous / Next Service elements completely removed!")

    # 5. Screenshot Main Showcase Full Page
    page.screenshot(path='C:/Users/dhushyanth/.gemini/antigravity-ide/brain/b4b76897-4c86-4737-822d-bfa24e5768fc/showcase_6_offerings_full.png', full_page=True)
    print("[OK] Main Showcase screenshot saved!")

    # 6. Test 01 Arrow -> SOC-As-A-Service
    print("Testing Arrow 01 (SOC-As-A-Service)...")
    arrow_soc = page.locator('a[aria-label="Open SOC-As-A-Service Details"]')
    arrow_soc.click()
    page.wait_for_timeout(500)
    assert page.locator('#view-soc').is_visible(), "view-soc not visible after clicking arrow 01!"
    print("[OK] Arrow 01 routes to view-soc!")
    
    # Back to All Offerings
    back_btn = page.locator('#view-soc a:has-text("Back to All Offerings")')
    back_btn.click()
    page.wait_for_timeout(500)
    assert page.locator('#view-offerings').is_visible(), "Back to All Offerings failed from view-soc!"
    print("[OK] Back to All Offerings works from view-soc!")

    # 7. Test 02 Arrow -> Skilling Solutions
    print("Testing Arrow 02 (Skilling Solutions)...")
    arrow_skilling = page.locator('a[aria-label="Open Skilling Solutions Details"]')
    arrow_skilling.click()
    page.wait_for_timeout(500)
    assert page.locator('#view-skilling').is_visible(), "view-skilling not visible after clicking arrow 02!"
    print("[OK] Arrow 02 routes to view-skilling!")
    
    # Back to All Offerings
    back_btn = page.locator('#view-skilling a:has-text("Back to All Offerings")')
    back_btn.click()
    page.wait_for_timeout(500)
    assert page.locator('#view-offerings').is_visible(), "Back to All Offerings failed from view-skilling!"
    print("[OK] Back to All Offerings works from view-skilling!")

    # 8. Test 03 Arrow -> Cambridge Learning
    print("Testing Arrow 03 (Cambridge Learning)...")
    arrow_cambridge = page.locator('a[aria-label="Open Cambridge Learning & Global Certifications Details"]')
    arrow_cambridge.click()
    page.wait_for_timeout(500)
    assert page.locator('#view-cambridge').is_visible(), "view-cambridge not visible after clicking arrow 03!"
    cambridge_text = page.locator('#view-cambridge').inner_text()
    assert "EC-Council" not in cambridge_text, "EC-Council found in view-cambridge!"
    assert "ISC2" not in cambridge_text, "ISC2 found in view-cambridge!"
    assert "CISSP" not in cambridge_text, "CISSP found in view-cambridge!"
    assert "CEH" not in cambridge_text, "CEH found in view-cambridge!"
    page.screenshot(path='C:/Users/dhushyanth/.gemini/antigravity-ide/brain/b4b76897-4c86-4737-822d-bfa24e5768fc/cambridge_detail_preview.png')
    print("[OK] Arrow 03 routes to isolated view-cambridge (no EC-Council/ISC2)!")
    
    # Back to All Offerings
    back_btn = page.locator('#view-cambridge a:has-text("Back to All Offerings")')
    back_btn.click()
    page.wait_for_timeout(500)
    assert page.locator('#view-offerings').is_visible(), "Back to All Offerings failed from view-cambridge!"
    print("[OK] Back to All Offerings works from view-cambridge!")

    # 9. Test 04 Arrow -> ISC2 Credentials
    print("Testing Arrow 04 (ISC2 Credentials)...")
    arrow_isc2 = page.locator('a[aria-label="Open ISC2 Credentials Details"]')
    arrow_isc2.click()
    page.wait_for_timeout(500)
    assert page.locator('#view-isc2').is_visible(), "view-isc2 not visible after clicking arrow 04!"
    isc2_text = page.locator('#view-isc2').inner_text()
    assert "Cambridge" not in isc2_text, "Cambridge found in view-isc2!"
    assert "EC-Council" not in isc2_text, "EC-Council found in view-isc2!"
    assert "CISSP" in isc2_text, "CISSP missing from view-isc2!"
    page.screenshot(path='C:/Users/dhushyanth/.gemini/antigravity-ide/brain/b4b76897-4c86-4737-822d-bfa24e5768fc/isc2_detail_preview.png')
    print("[OK] Arrow 04 routes to isolated view-isc2!")
    
    # Back to All Offerings
    back_btn = page.locator('#view-isc2 a:has-text("Back to All Offerings")')
    back_btn.click()
    page.wait_for_timeout(500)
    assert page.locator('#view-offerings').is_visible(), "Back to All Offerings failed from view-isc2!"
    print("[OK] Back to All Offerings works from view-isc2!")

    # 10. Test 05 Arrow -> EC-Council (ATC)
    print("Testing Arrow 05 (EC-Council ATC)...")
    arrow_ecc = page.locator('a[aria-label="Open EC-Council (ATC) Details"]')
    arrow_ecc.click()
    page.wait_for_timeout(500)
    assert page.locator('#view-ec-council').is_visible(), "view-ec-council not visible after clicking arrow 05!"
    ecc_text = page.locator('#view-ec-council').inner_text()
    assert "Cambridge" not in ecc_text, "Cambridge found in view-ec-council!"
    assert "ISC2" not in ecc_text, "ISC2 found in view-ec-council!"
    assert "CEH" in ecc_text, "CEH missing from view-ec-council!"
    page.screenshot(path='C:/Users/dhushyanth/.gemini/antigravity-ide/brain/b4b76897-4c86-4737-822d-bfa24e5768fc/eccouncil_detail_preview.png')
    print("[OK] Arrow 05 routes to isolated view-ec-council!")
    
    # Back to All Offerings
    back_btn = page.locator('#view-ec-council a:has-text("Back to All Offerings")')
    back_btn.click()
    page.wait_for_timeout(500)
    assert page.locator('#view-offerings').is_visible(), "Back to All Offerings failed from view-ec-council!"
    print("[OK] Back to All Offerings works from view-ec-council!")

    # 11. Test 06 Arrow -> IT Services (8 Pillars)
    print("Testing Arrow 06 (IT Services)...")
    arrow_it = page.locator('a[aria-label="Open IT Services (8 Pillars) Details"]')
    arrow_it.click()
    page.wait_for_timeout(500)
    assert page.locator('#view-it-services').is_visible(), "view-it-services not visible after clicking arrow 06!"
    it_text = page.locator('#view-it-services').inner_text()
    assert "Website Creation" in it_text, "Website Creation missing from IT Services!"
    assert "Resource Planning" in it_text, "Resource Planning missing from IT Services!"
    page.screenshot(path='C:/Users/dhushyanth/.gemini/antigravity-ide/brain/b4b76897-4c86-4737-822d-bfa24e5768fc/itservices_detail_preview.png')
    print("[OK] Arrow 06 routes to isolated view-it-services!")
    
    # Back to All Offerings
    back_btn = page.locator('#view-it-services a:has-text("Back to All Offerings")')
    back_btn.click()
    page.wait_for_timeout(500)
    assert page.locator('#view-offerings').is_visible(), "Back to All Offerings failed from view-it-services!"
    print("[OK] Back to All Offerings works from view-it-services!")

    browser.close()
    print("\n=========================================")
    print("ALL TESTS PASSED WITH 100% SUCCESS!")
    print("=========================================")
