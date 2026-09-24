# test_official_logo.py
import os
import sys
from playwright.sync_api import sync_playwright

workspace = os.path.abspath(os.path.dirname(__file__))
artifact_dir = r"C:\Users\dhushyanth\.gemini\antigravity-ide\brain\a3f0dbb1-0b11-4467-af7c-72b2b2558fa9"
os.makedirs(artifact_dir, exist_ok=True)

print("======================================================================")
print("TESTING OFFICIAL SLN CONSULTING LOGO INTEGRATION")
print("======================================================================\n")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    # 1. Desktop Test (1400 x 900)
    print("--- 1. DESKTOP VIEWPORT (1400 x 900) ---")
    page = browser.new_page(viewport={'width': 1400, 'height': 900})
    index_url = f"file:///{workspace.replace('\\', '/')}/index.html"
    page.goto(index_url, wait_until='networkidle')
    page.wait_for_timeout(400)

    # Header Logo Checks
    header_img = page.locator('header a[aria-label="SLN Consulting Home"] img')
    assert header_img.is_visible(), "FAILED: Header logo image is not visible!"
    
    header_img_src = header_img.get_attribute('src')
    assert "sln-consulting-logo.png" in header_img_src, f"FAILED: Unexpected src: {header_img_src}"
    
    header_box = header_img.bounding_box()
    print(f"Header logo bounding box: {header_box['width']:.1f}px x {header_box['height']:.1f}px")
    
    # Check natural dimensions to confirm image actually loaded
    natural_dims = page.evaluate("""() => {
        const img = document.querySelector('header a[aria-label="SLN Consulting Home"] img');
        return { naturalWidth: img.naturalWidth, naturalHeight: img.naturalHeight };
    }""")
    assert natural_dims['naturalWidth'] == 270, f"Expected naturalWidth 270, got {natural_dims['naturalWidth']}"
    assert natural_dims['naturalHeight'] == 90, f"Expected naturalHeight 90, got {natural_dims['naturalHeight']}"
    print(f"[PASS] Header logo natural dimensions: {natural_dims['naturalWidth']}x{natural_dims['naturalHeight']} (image loaded successfully).")

    # Verify aspect ratio preserved (approx 3.0)
    aspect_ratio = header_box['width'] / header_box['height']
    assert 2.8 <= aspect_ratio <= 3.2, f"FAILED: Aspect ratio distorted: {aspect_ratio:.2f}"
    print(f"[PASS] Header logo aspect ratio preserved: {aspect_ratio:.2f} (expected ~3.0)")

    # Verify no duplicate text beside the logo
    brand_link_text = page.locator('header a[aria-label="SLN Consulting Home"]').inner_text().strip()
    assert brand_link_text == "", f"FAILED: Found extra text beside header logo: '{brand_link_text}'"
    print("[PASS] No duplicate text beside header logo.")

    # Check header total height (Row 1 top bar ~40px + Row 2 nav bar ~88px = ~128px)
    header_elem = page.locator('header')
    header_box_total = header_elem.bounding_box()
    print(f"Header total height: {header_box_total['height']:.1f}px (remains compact and standard)")
    assert header_box_total['height'] <= 135, f"Header is too tall: {header_box_total['height']}px"

    # Footer Logo Checks
    footer_img = page.locator('footer a[aria-label="SLN Consulting Home"] img')
    assert footer_img.is_visible(), "FAILED: Footer logo image is not visible!"
    
    footer_box = footer_img.bounding_box()
    print(f"Footer logo bounding box: {footer_box['width']:.1f}px x {footer_box['height']:.1f}px")
    
    footer_natural = page.evaluate("""() => {
        const img = document.querySelector('footer a[aria-label="SLN Consulting Home"] img');
        return { naturalWidth: img.naturalWidth, naturalHeight: img.naturalHeight };
    }""")
    assert footer_natural['naturalWidth'] == 270
    assert footer_natural['naturalHeight'] == 90
    print(f"[PASS] Footer logo loaded successfully: {footer_natural['naturalWidth']}x{footer_natural['naturalHeight']}")

    footer_ratio = footer_box['width'] / footer_box['height']
    assert 2.8 <= footer_ratio <= 3.2, f"FAILED: Footer logo aspect ratio distorted: {footer_ratio:.2f}"
    print(f"[PASS] Footer logo aspect ratio preserved: {footer_ratio:.2f}")

    # Check clean white container in footer
    footer_container_bg = page.evaluate("""() => {
        const c = document.querySelector('footer a[aria-label="SLN Consulting Home"] div');
        return window.getComputedStyle(c).backgroundColor;
    }""")
    print(f"Footer container background: {footer_container_bg}")
    assert "255, 255, 255" in footer_container_bg or "rgb(255, 255, 255)" in footer_container_bg, f"Expected white container, got {footer_container_bg}"
    print("[PASS] Footer logo sits inside a clean white container.")

    # Capture Desktop Header screenshot
    desktop_header_shot = os.path.join(artifact_dir, "verification_logo_header_desktop_light.png")
    page.locator('header').screenshot(path=desktop_header_shot)
    print(f"[SCREENSHOT] Saved {desktop_header_shot}")

    # Scroll to footer and capture Footer screenshot
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(300)
    desktop_footer_shot = os.path.join(artifact_dir, "verification_logo_footer_desktop.png")
    page.locator('footer').screenshot(path=desktop_footer_shot)
    print(f"[SCREENSHOT] Saved {desktop_footer_shot}")

    # Dark Mode Desktop Header Test
    print("\n--- 2. DARK MODE DESKTOP TEST ---")
    page.evaluate("document.documentElement.classList.add('dark')")
    page.wait_for_timeout(200)
    desktop_header_dark_shot = os.path.join(artifact_dir, "verification_logo_header_desktop_dark.png")
    page.locator('header').screenshot(path=desktop_header_dark_shot)
    print(f"[SCREENSHOT] Saved {desktop_header_dark_shot}")

    # 3. Mobile Viewport Test (375 x 812)
    print("\n--- 3. MOBILE VIEWPORT (375 x 812) ---")
    page.close()
    page_mobile = browser.new_page(viewport={'width': 375, 'height': 812})
    page_mobile.goto(index_url, wait_until='networkidle')
    page_mobile.wait_for_timeout(400)

    # Check mobile header logo visibility & dimensions
    m_header_img = page_mobile.locator('header a[aria-label="SLN Consulting Home"] img')
    assert m_header_img.is_visible(), "FAILED: Mobile header logo is not visible!"
    m_box = m_header_img.bounding_box()
    print(f"Mobile header logo bounding box: {m_box['width']:.1f}px x {m_box['height']:.1f}px")
    assert m_box['width'] <= 130, f"Mobile logo too wide: {m_box['width']}"
    
    # Check no horizontal scrollbar on mobile
    scroll_w = page_mobile.evaluate("document.documentElement.scrollWidth")
    inner_w = page_mobile.evaluate("window.innerWidth")
    print(f"Mobile widths: scrollWidth={scroll_w}px, innerWidth={inner_w}px")
    assert scroll_w <= inner_w, f"FAILED: Mobile page has horizontal overflow: scrollWidth={scroll_w} > innerWidth={inner_w}"
    print("[PASS] Zero horizontal overflow on mobile.")

    mobile_header_shot = os.path.join(artifact_dir, "verification_logo_header_mobile.png")
    page_mobile.locator('header').screenshot(path=mobile_header_shot)
    print(f"[SCREENSHOT] Saved {mobile_header_shot}")

    # Check other pages (e.g. training.html, offerings.html, enterprises.html, campus.html)
    print("\n--- 4. CROSS-PAGE VERIFICATION ---")
    for test_page_name in ['training.html', 'offerings.html', 'enterprises.html', 'campus.html']:
        page_mobile.goto(f"file:///{workspace.replace('\\', '/')}/{test_page_name}", wait_until='networkidle')
        p_logo = page_mobile.locator('header a[aria-label="SLN Consulting Home"] img')
        assert p_logo.is_visible(), f"FAILED: Header logo missing on {test_page_name}"
        p_footer = page_mobile.locator('footer a[aria-label="SLN Consulting Home"] img')
        assert p_footer.is_visible(), f"FAILED: Footer logo missing on {test_page_name}"
        print(f"[PASS] Header and footer logos verified on {test_page_name}")

    browser.close()

print("\n======================================================================")
print("ALL OFFICIAL LOGO VERIFICATION TESTS PASSED SUCCESSFULLY!")
print("======================================================================")
