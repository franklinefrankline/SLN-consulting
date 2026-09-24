import os
import sys
from playwright.sync_api import sync_playwright

workspace = os.path.abspath(os.path.dirname(__file__))

print("======================================================================")
print("TESTING ENTERPRISES & CAMPUS SEPARATION AND NESTED SUBMENU SYSTEM")
print("======================================================================\n")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1400, 'height': 900})

    # Test 1: Direct File Loading of enterprises.html
    print("--- TEST 1: Direct File Loading of enterprises.html ---")
    ent_url = f"file:///{workspace.replace('\\', '/')}/enterprises.html"
    page.goto(ent_url, wait_until='networkidle')
    page.wait_for_timeout(500)

    # Check that view-enterprises is active
    is_ent_active = page.evaluate("document.getElementById('view-enterprises').classList.contains('active')")
    assert is_ent_active, "FAILED: view-enterprises is not active on enterprises.html"
    print("[PASS] view-enterprises is active on enterprises.html direct load.")

    # Check images on enterprises.html
    img_status = page.evaluate("""() => {
      const imgs = Array.from(document.querySelectorAll('#view-enterprises img'));
      return imgs.map(i => ({ src: i.getAttribute('src'), nw: i.naturalWidth, ok: i.complete && i.naturalWidth > 0 }));
    }""")
    for img in img_status:
        assert img['ok'], f"Broken image in enterprises view: {img['src']}"
    print(f"[PASS] All {len(img_status)} images in view-enterprises load correctly.")

    # Check 9 Training domains
    training_domains = [
        "Cybersecurity", "Data Sciences", "Cloud Computing",
        "Network Management", "Artificial Intelligence", "Machine Language",
        "Soft Skills", "Soft Management Skills", "Leadership"
    ]
    ent_text = page.locator('#view-enterprises').inner_text()
    for td in training_domains:
        assert td in ent_text, f"Missing training domain: {td}"
    assert "All Cybersecurity training leads to attempting global certifications - ISACA, ISC2, EC-Council etc" in ent_text, "Missing certification footnote"
    print("[PASS] All 9 Training domains and certification footnote are present.")

    # Check 16 Mid/Senior manager workshops
    manager_workshops = [
        "Executive Session on Cybersecurity for C-Suite Leaders",
        "Cybersecurity Risks for Financial Organizations",
        "Cybersecurity Enterprise Awareness: Empowering Vigilance",
        "Critical IT & Cybersecurity Infrastructure Review",
        "Artificial Intelligence (Ai) for Information Security Audit",
        "Threats and Vulnerability Management",
        "Data Security: Addressing Enterprise Concerns",
        "Cybersecurity in the Cloud: Ensuring Visibility & Control",
        "Zero Trust: Disrupt, Destroy, Steal",
        "Blockchain Operational and Deployment Insights",
        "Metaverse Technologies and Enterprise Adoption",
        "Security Challenges: Disrupting Disruptors",
        "Blockchain: Transforming Business Processes",
        "Cybersecurity for Oil & Gas: Redefining the Landscape",
        "Leadership Excellence: Mid & Senior managers",
        "Resilience & Building trusted security workforce"
    ]
    for mw in manager_workshops:
        assert mw in ent_text, f"Missing manager workshop: {mw}"
    print("[PASS] All 16 Mid & Senior Manager workshops are present.")

    # Check 9 Fresher workshops
    fresher_workshops = [
        "Cybersecurity awareness - essentials workshop",
        "Security monitoring & management",
        "Network security concepts & methodologies",
        "Essential tools for cyber investigation",
        "Incident response principal tactics",
        "Cyber crisis management",
        "Ethical hacking & penetration testing principles",
        "Secure software development a basic introduction",
        "Overview of cyber basics"
    ]
    for fw in fresher_workshops:
        assert fw in ent_text, f"Missing fresher workshop: {fw}"
    print("[PASS] All 9 Fresher Cybersecurity workshop names are present.")

    # Check that explanatory descriptions are completely removed
    removed_ent_phrases = [
        "Introduction to the key architectural and technological concepts of cybersecurity",
        "Tools, concepts and methods used to monitor and manage the network security infrastructure",
        "Key cyber security threats, attack patterns and risks in the cyber world",
        "Professional tools to investigate an accident, collect initial evidence",
        "Tools, skills and work methods utilised by an incident response team",
        "Skills and concepts required for successful management of a major cyber incident",
        "Principles, methodologies and tools for ethical hacking and penetration testing",
        "Principles for designing secure software architecture and developing secure code",
        "Internal processes, mechanisms and stages of malware execution",
        "Targeted briefings and tactical sessions designed to address modern cyber threat landscapes"
    ]
    for rep in removed_ent_phrases:
        assert rep not in ent_text, f"Found explanatory text that should be removed: {rep}"
    print("[PASS] Verified that all explanatory/description paragraphs are removed from Enterprises cards.")

    # Check NO Back to All Offerings and NO Previous/Next
    back_btn = page.locator('#view-enterprises a:has-text("Back to All Offerings")')
    assert back_btn.count() == 0, "Found obsolete Back to All Offerings in view-enterprises"
    assert "Previous Service" not in ent_text, "Found forbidden Previous Service in view-enterprises"
    assert "Next Service" not in ent_text, "Found forbidden Next Service in view-enterprises"
    print("[PASS] Back to All Offerings is removed and Prev/Next are absent.")

    # Take screenshot of Enterprises
    page.screenshot(path="verification_enterprises_page.png")
    print("Saved verification_enterprises_page.png")

    # Test 2: Direct File Loading of campus.html
    print("\n--- TEST 2: Direct File Loading of campus.html ---")
    cam_url = f"file:///{workspace.replace('\\', '/')}/campus.html"
    page.goto(cam_url, wait_until='networkidle')
    page.wait_for_timeout(500)

    # Check that view-campus is active
    is_cam_active = page.evaluate("document.getElementById('view-campus').classList.contains('active')")
    assert is_cam_active, "FAILED: view-campus is not active on campus.html"
    print("[PASS] view-campus is active on campus.html direct load.")

    cam_text = page.locator('#view-campus').inner_text()
    assert "For Campus" in cam_text, "Missing heading 'For Campus'"
    assert "Defining Career path" in cam_text, "Missing 'Defining Career path'"

    # Check 6 Campus offerings
    campus_offerings = [
        "Seminars / Webinars Through Industry SMEs",
        "Hackathon Events",
        "Preparing Students For Corporate World",
        "Induction Training",
        "Soft Skills Training",
        "Faculty Training And Updation (TTT)"
    ]
    for co in campus_offerings:
        assert co in cam_text, f"Missing campus offering: {co}"
    print("[PASS] All 6 Campus offerings are present.")

    # Check that descriptions have been removed from the 6 cards
    removed_phrases = [
        "Direct engagement sessions with industry subject matter experts",
        "Collaborative technical challenges and competitive hackathons",
        "Comprehensive career grooming, resume workshops",
        "Pre-employment and corporate onboarding bootcamps",
        "Professional communication, cross-functional collaboration",
        "Train-The-Trainer (TTT) intensive workshops updating"
    ]
    for rp in removed_phrases:
        assert rp not in cam_text, f"Card still contains removed descriptive paragraph: {rp}"
    print("[PASS] Verified that all descriptive paragraphs inside the 6 Campus cards are removed.")

    # Check "Let's discuss" CTA
    lets_discuss = page.locator('#view-campus a:has-text("Let\'s discuss")')
    assert lets_discuss.count() >= 1, "Missing 'Let\\'s discuss' CTA on campus page"
    print("[PASS] 'Let\\'s discuss' CTA is present.")

    # Check separation
    assert "WORKSHOPS & WEBINARS FOR MID & SENIOR MANAGERS" not in cam_text, "Enterprise content leaked into Campus page!"
    assert "Defining Career Path" not in ent_text and "Defining Career path" not in ent_text, "Campus content leaked into Enterprise page!"
    print("[PASS] Content separation verified: Enterprises and Campus are strictly independent.")

    # Take screenshot of Campus
    page.screenshot(path="verification_campus_page.png")
    print("Saved verification_campus_page.png")

    # Test 3: Dropdown Navigation from index.html
    print("\n--- TEST 3: Dropdown Navigation from index.html ---")
    idx_url = f"file:///{workspace.replace('\\', '/')}/index.html"
    page.goto(idx_url, wait_until='networkidle')
    page.wait_for_timeout(500)

    # Hover over Our Offering
    page.hover('#offeringsNavBtn')
    page.wait_for_timeout(300)

    # Hover over Skilling Solutions to show nested submenu
    page.hover('#skillingNavMainLink')
    page.wait_for_timeout(300)

    # Screenshot open nested dropdown
    page.screenshot(path="verification_nested_skilling_dropdown_v2.png")
    print("Saved verification_nested_skilling_dropdown_v2.png")

    # Click Enterprises
    print("Clicking Enterprises in nested submenu...")
    page.click('#desktopSkillingSubmenu a[href="enterprises.html"]')
    page.wait_for_timeout(400)
    assert page.evaluate("document.getElementById('view-enterprises').classList.contains('active')"), "Failed to open view-enterprises on 1 click"
    print("[PASS] 1-Click navigation from dropdown to Enterprises succeeded.")

    # Verify no Back to All Offerings link exists on page
    assert page.locator('a:has-text("Back to All Offerings")').count() == 0, "Obsolete Back to All Offerings button found"
    print("[PASS] Verified zero 'Back to All Offerings' button on page.")

    # Hover again and click Campus
    print("Clicking Campus in nested submenu...")
    page.hover('#offeringsNavBtn')
    page.wait_for_timeout(300)
    page.hover('#skillingNavMainLink')
    page.wait_for_timeout(300)
    page.click('#desktopSkillingSubmenu a[href="campus.html"]')
    page.wait_for_timeout(400)
    assert page.evaluate("document.getElementById('view-campus').classList.contains('active')"), "Failed to open view-campus on 1 click"
    print("[PASS] 1-Click navigation from dropdown to Campus succeeded.")

    # Click Skilling Solutions to toggle submenu
    print("Testing click on Skilling Solutions to toggle nested items...")
    page.hover('#offeringsNavBtn')
    page.wait_for_timeout(300)
    page.click('#skillingNavMainLink')
    page.wait_for_timeout(300)
    assert page.locator('#desktopSkillingSubmenu').is_visible(), "Submenu not visible after toggle"
    print("[PASS] Skilling Solutions toggle expands nested Enterprises and Campus items.")

    # Test 4: Mobile Navigation & Drawer Submenu
    print("\n--- TEST 4: Mobile Navigation & Drawer Submenu ---")
    page.set_viewport_size({'width': 375, 'height': 812})
    page.goto(idx_url, wait_until='networkidle')
    page.wait_for_timeout(500)

    # Open mobile drawer
    page.click('#mobileMenuBtn')
    page.wait_for_timeout(300)

    # Toggle Our Offering
    page.click('#mobileOfferingsToggleBtn')
    page.wait_for_timeout(300)

    # Toggle Skilling submenu
    page.click('#mobileSkillingToggleBtn')
    page.wait_for_timeout(300)

    # Check horizontal overflow
    overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
    assert not overflow, "Mobile drawer has horizontal overflow!"
    print("[PASS] Zero horizontal overflow on mobile drawer with nested Skilling expanded.")

    page.screenshot(path="verification_mobile_nested_expanded_v2.png")
    print("Saved verification_mobile_nested_expanded_v2.png")

    # Click Enterprises in mobile drawer
    page.click('#mobileSkillingSubmenu a[href="enterprises.html"]')
    page.wait_for_timeout(400)
    assert page.evaluate("document.getElementById('view-enterprises').classList.contains('active')"), "Failed to open view-enterprises on mobile"
    print("[PASS] Mobile 1-click navigation to Enterprises succeeded.")

    browser.close()

print("\n======================================================================")
print("ALL ENTERPRISES & CAMPUS TESTS COMPLETED AND PASSED WITH 100% SUCCESS!")
print("======================================================================")
