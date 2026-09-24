import os
import sys
from playwright.sync_api import sync_playwright

workspace = os.path.abspath(os.path.dirname(__file__))

print("======================================================================")
print("TESTING TRAINING SCHEDULE PAGE & TRAINING CALENDAR TABLE")
print("======================================================================\n")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1400, 'height': 900})

    # Test 1: Direct File Loading of training.html
    print("--- TEST 1: Direct File Loading of training.html ---")
    tr_url = f"file:///{workspace.replace('\\', '/')}/training.html"
    page.goto(tr_url, wait_until='networkidle')
    page.wait_for_timeout(500)

    # Check view-training is active
    is_tr_active = page.evaluate("document.getElementById('view-training').classList.contains('active')")
    assert is_tr_active, "FAILED: view-training is not active on training.html"
    print("[PASS] view-training is active on training.html direct load.")

    # Check "Training Calendar" heading
    cal_heading = page.locator('#training-calendar h2')
    assert cal_heading.is_visible(), "Training Calendar heading is not visible!"
    assert "Training Calendar" in cal_heading.inner_text(), f"Expected 'Training Calendar', got: {cal_heading.inner_text()}"
    print("[PASS] 'Training Calendar' heading is visible.")

    # Check Table is present
    table = page.locator('#training-calendar table')
    assert table.is_visible(), "Training Calendar table is not visible!"
    print("[PASS] Training Calendar table is present and visible.")

    # Check all 9 columns
    expected_cols = [
        "Month", "S.No.", "Certification", "OEM",
        "Date from", "Date to", "Timing", "Mode", "For Registration"
    ]
    th_elements = page.locator('#training-calendar table thead th')
    assert th_elements.count() == 9, f"Expected 9 columns, found {th_elements.count()}"
    for i, exp in enumerate(expected_cols):
        actual_col = th_elements.nth(i).inner_text().strip()
        assert exp.lower() == actual_col.lower(), f"Column {i} mismatch: expected '{exp}', got '{actual_col}'"
    print("[PASS] All 9 table columns verified: " + ", ".join(expected_cols))

    # Check row data
    row_text = page.locator('#training-calendar table tbody tr').inner_text()
    assert "Nov 2024" in row_text, "Missing 'Nov 2024'"
    assert "1" in row_text, "Missing '1'"
    assert "Certified Information Systems Security Professional (CISSP)" in row_text, "Missing CISSP certification name"
    assert "ISC2" in row_text, "Missing OEM 'ISC2'"
    assert "25-11-2024" in row_text, "Missing '25-11-2024'"
    assert "29-11-2024" in row_text, "Missing '29-11-2024'"
    assert "9 am–5 pm" in row_text or "9 am-5 pm" in row_text, "Missing '9 am–5 pm'"
    assert "Live Online" in row_text, "Missing 'Live Online'"
    assert "SLN Consulting Solution For Seamless Growth" in row_text, "Missing registration title"
    print("[PASS] Table row data verified exactly (Nov 2024, CISSP, ISC2, 25-11-2024 to 29-11-2024, 9 am–5 pm, Live Online, SLN Consulting Solution For Seamless Growth).")

    # Check registration link
    reg_link = page.locator('#training-calendar table tbody tr a[href="contact.html"]')
    assert reg_link.count() > 0, "Registration link to contact.html missing"
    print("[PASS] Registration area is clickable and links to existing contact route.")

    # Check images on training.html
    img_status = page.evaluate("""() => {
      const imgs = Array.from(document.querySelectorAll('#view-training img'));
      return imgs.map(i => ({ src: i.getAttribute('src'), nw: i.naturalWidth, ok: i.complete && i.naturalWidth > 0 }));
    }""")
    for img in img_status:
        assert img['ok'], f"Broken image in view-training: {img['src']}"
    print(f"[PASS] All {len(img_status)} images in view-training load properly.")

    # Screenshot desktop training calendar
    page.screenshot(path="verification_training_calendar_desktop.png")
    print("Saved verification_training_calendar_desktop.png")

    # Test 2: Navigation to Training from Header
    print("\n--- TEST 2: Navigation to Training from Header on index.html ---")
    idx_url = f"file:///{workspace.replace('\\', '/')}/index.html"
    page.goto(idx_url, wait_until='networkidle')
    page.wait_for_timeout(500)

    # Click Training in main nav
    page.click('nav a[data-route="training.html"]')
    page.wait_for_timeout(400)
    assert page.evaluate("document.getElementById('view-training').classList.contains('active')"), "Failed to open view-training on clicking Training in nav"
    assert page.locator('#training-calendar').is_visible(), "Training calendar section missing after nav click"
    print("[PASS] 1-Click navigation from Header 'Training' opens Training Schedule and Calendar.")

    # Test 3: Direct File Loading of training-schedule.html
    print("\n--- TEST 3: Direct File Loading of training-schedule.html ---")
    sched_url = f"file:///{workspace.replace('\\', '/')}/training-schedule.html"
    page.goto(sched_url, wait_until='networkidle')
    page.wait_for_timeout(500)
    assert page.evaluate("document.getElementById('view-training').classList.contains('active')"), "Failed to open view-training on training-schedule.html"
    assert page.locator('#training-calendar table').is_visible(), "Table not visible on training-schedule.html"
    print("[PASS] Direct load of training-schedule.html opens Training Calendar.")

    # Test 4: Mobile Responsiveness (375px)
    print("\n--- TEST 4: Mobile Responsiveness at 375px ---")
    page.set_viewport_size({'width': 375, 'height': 812})
    page.goto(tr_url, wait_until='networkidle')
    page.wait_for_timeout(500)

    # Check horizontal page overflow
    page_overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
    assert not page_overflow, "Horizontal overflow detected on mobile page body!"
    print("[PASS] Zero horizontal overflow on mobile viewport; table container safely scrolls internally.")

    # Check table container scrollable
    can_scroll = page.evaluate("""() => {
      const el = document.querySelector('#training-calendar .overflow-x-auto');
      return el.scrollWidth > el.clientWidth;
    }""")
    assert can_scroll, "Table should be horizontally scrollable on mobile"
    print("[PASS] Table container correctly supports smooth internal horizontal scrolling on mobile.")

    # Screenshot mobile training calendar
    page.screenshot(path="verification_training_calendar_mobile.png")
    print("Saved verification_training_calendar_mobile.png")

    browser.close()

print("\n======================================================================")
print("ALL TRAINING CALENDAR TESTS COMPLETED AND PASSED WITH 100% SUCCESS!")
print("======================================================================")
