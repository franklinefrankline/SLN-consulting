import os
import sys
import json
import asyncio
import subprocess
import urllib.request
import websockets

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9223

async def main():
    cmd = [
        CHROME_PATH,
        f"--remote-debugging-port={PORT}",
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-extensions",
        "--user-data-dir=" + os.path.join(os.environ.get("TEMP", "C:\\temp"), "chrome_nav_test_suite")
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    await asyncio.sleep(2)

    try:
        tabs_url = f"http://127.0.0.1:{PORT}/json"
        req = urllib.request.urlopen(tabs_url)
        tabs = json.loads(req.read().decode())
        page_tabs = [t for t in tabs if t.get("type") == "page"]
        ws_url = page_tabs[0]["webSocketDebuggerUrl"]

        async with websockets.connect(ws_url) as ws:
            msg_id = 0

            async def send_cmd(method, params=None):
                nonlocal msg_id
                msg_id += 1
                payload = {"id": msg_id, "method": method, "params": params or {}}
                await ws.send(json.dumps(payload))
                while True:
                    resp = json.loads(await ws.recv())
                    if resp.get("id") == msg_id:
                        return resp.get("result", {})

            async def wait_event(event_name):
                while True:
                    resp = json.loads(await ws.recv())
                    if resp.get("method") == event_name:
                        return resp

            await send_cmd("Page.enable")
            await send_cmd("Runtime.enable")

            async def evaluate(expr):
                res = await send_cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True})
                return res.get("result", {}).get("value")

            # 1. Navigate to index.html
            print("1. Navigating to http://localhost:5500/index.html...")
            p = send_cmd("Page.navigate", {"url": "http://localhost:5500/index.html"})
            await p
            await wait_event("Page.loadEventFired")
            await asyncio.sleep(0.5)

            # Check initial state
            home_active = await evaluate("!!document.getElementById('view-index')?.classList.contains('active')")
            resources_active = await evaluate("!!document.getElementById('view-resources')?.classList.contains('active')")
            training_active = await evaluate("!!document.getElementById('view-training')?.classList.contains('active')")
            print(f"   Initial state -> Home active: {home_active}, Resources active: {resources_active}, Training active: {training_active}")
            assert home_active == True, "Home must be initially active"
            assert resources_active == False, "Resources must NOT be initially active"
            assert training_active == False, "Training must NOT be initially active"

            # Check Resources link attributes
            print("2. Checking Resources navbar link properties...")
            res_link = await evaluate("""
                (() => {
                    const link = Array.from(document.querySelectorAll('.desktop-nav a')).find(a => a.textContent.trim() === 'Resources');
                    return {
                        text: link ? link.textContent.trim() : null,
                        href: link ? link.getAttribute('href') : null,
                        dataRoute: link ? link.getAttribute('data-route') : null,
                        onclick: link ? link.getAttribute('onclick') : null,
                        hasDropdown: link ? !!link.closest('.group')?.querySelector('[id^="dropdown"]') : false
                    };
                })()
            """)
            print(f"   Resources link: {res_link}")
            assert res_link['text'] == 'Resources', "Resources link should exist"
            assert res_link['href'] == 'resources.html', "Resources href should be resources.html"
            assert res_link['dataRoute'] == 'resources.html', "data-route should be resources.html"
            assert 'resources.html' in res_link['onclick'], "onclick should route to resources.html"
            assert res_link['hasDropdown'] == False, "Resources must have NO dropdown"

            # Click Resources link
            print("3. Clicking 'Resources' link from main navbar...")
            await evaluate("""
                (() => {
                    const link = Array.from(document.querySelectorAll('.desktop-nav a')).find(a => a.textContent.trim() === 'Resources');
                    link.click();
                })()
            """)
            await asyncio.sleep(0.5)

            res_active_after = await evaluate("!!document.getElementById('view-resources')?.classList.contains('active')")
            train_active_after = await evaluate("!!document.getElementById('view-training')?.classList.contains('active')")
            res_display = await evaluate("window.getComputedStyle(document.getElementById('view-resources')).display")
            train_display = await evaluate("window.getComputedStyle(document.getElementById('view-training')).display")

            print(f"   After clicking Resources:")
            print(f"     view-resources active: {res_active_after} (display: {res_display})")
            print(f"     view-training active: {train_active_after} (display: {train_display})")
            assert res_active_after == True, "view-resources MUST be active after clicking Resources"
            assert train_active_after == False, "view-training MUST NOT be active after clicking Resources"
            assert res_display != 'none', "view-resources must be visible"
            assert train_display == 'none', "view-training must be hidden"

            # Check Resources page content
            print("4. Verifying dedicated Resources page content & design...")
            eyebrow = await evaluate("document.querySelector('#view-resources .font-mono')?.textContent?.trim()")
            hero_title = await evaluate("document.querySelector('#view-resources h1')?.textContent?.trim()")
            hero_desc = await evaluate("document.querySelector('#view-resources section#resources-hero p')?.textContent?.trim()")
            card_count = await evaluate("document.querySelectorAll('#view-resources .resource-card')?.length")
            card_titles = await evaluate("Array.from(document.querySelectorAll('#view-resources .resource-card h3')).map(h => h.textContent.trim())")
            print(f"   Eyebrow: '{eyebrow}'")
            print(f"   Hero Title: '{hero_title}'")
            print(f"   Hero Desc: '{hero_desc}'")
            print(f"   Card Titles ({card_count}): {card_titles}")

            assert "RESOURCES & INSIGHTS" in eyebrow, "Eyebrow must contain RESOURCES & INSIGHTS"
            assert "Knowledge for Secure, Smarter Growth" in hero_title, "Hero title must match"
            assert "SLN Consulting provides cybersecurity insights" in hero_desc, "Hero description must match"
            assert card_count == 6, f"Expected 6 resource cards, found {card_count}"
            expected_titles = [
                "Insights & Advisories",
                "Events & Workshops",
                "Case Studies",
                "Training Calendar",
                "Campus Skilling",
                "Downloads & Toolkits"
            ]
            for title in expected_titles:
                assert title in card_titles, f"Missing card title: {title}"

            # Test clicking Training & Certifications
            print("5. Clicking 'Training & Certifications'...")
            await evaluate("""
                (() => {
                    const link = Array.from(document.querySelectorAll('.desktop-nav a')).find(a => a.textContent.trim().includes('Training'));
                    link.click();
                })()
            """)
            await asyncio.sleep(0.5)

            train_active = await evaluate("!!document.getElementById('view-training')?.classList.contains('active')")
            res_active = await evaluate("!!document.getElementById('view-resources')?.classList.contains('active')")
            print(f"   After clicking Training -> view-training active: {train_active}, view-resources active: {res_active}")
            assert train_active == True, "Training page should be active"
            assert res_active == False, "Resources page should be hidden"

            # Test all required navbar links individually
            test_links = [
                ("Home", "view-index"),
                ("About Us", "view-about"),
                ("IT Services", "view-it-services"),
                ("Academia", "view-campus"),
                ("Internships", "view-internships"),
                ("Training & Certifications", "view-training"),
                ("Corporate", "view-enterprises"),
                ("Resources", "view-resources"),
                ("Contact", "view-contact"),
            ]

            print("6. Testing all navbar links individually...")
            for label, view_id in test_links:
                await evaluate(f"""
                    (() => {{
                        const link = Array.from(document.querySelectorAll('.desktop-nav a')).find(a => a.textContent.trim().includes('{label}'));
                        link.click();
                    }})()
                """)
                await asyncio.sleep(0.3)
                is_active = await evaluate(f"!!document.getElementById('{view_id}')?.classList.contains('active')")
                print(f"   Clicked '{label}' -> {view_id} active: {is_active}")
                assert is_active == True, f"Clicking {label} must activate {view_id}"

            # Test Cybersecurity dropdown
            print("7. Testing Cybersecurity dropdown menu (ONLY SaaS & VAPT)...")
            cyber_dropdown = await evaluate("""
                (() => {
                    const btn = Array.from(document.querySelectorAll('.desktop-nav button')).find(b => b.textContent.includes('Cybersecurity'));
                    const menu = document.getElementById('dropdown-cybersecurity');
                    const items = Array.from(menu.querySelectorAll('a')).map(a => a.textContent.trim());
                    return {
                        btnText: btn ? btn.textContent.trim() : null,
                        items: items
                    };
                })()
            """)
            print(f"   Dropdown items: {cyber_dropdown['items']}")
            assert 'SaaS' in cyber_dropdown['items'], "Should contain SaaS"
            assert 'VAPT' in cyber_dropdown['items'], "Should contain VAPT"
            assert len(cyber_dropdown['items']) == 2, f"Expected exactly 2 items, got {cyber_dropdown['items']}"

            # Test direct navigation to resources.html
            print("8. Testing direct page load of http://localhost:5500/resources.html...")
            p2 = send_cmd("Page.navigate", {"url": "http://localhost:5500/resources.html"})
            await p2
            await wait_event("Page.loadEventFired")
            await asyncio.sleep(0.5)

            res_active_direct = await evaluate("!!document.getElementById('view-resources')?.classList.contains('active')")
            train_active_direct = await evaluate("!!document.getElementById('view-training')?.classList.contains('active')")
            print(f"   Direct load resources.html -> view-resources active: {res_active_direct}, view-training active: {train_active_direct}")
            assert res_active_direct == True, "Direct load of resources.html must activate view-resources"
            assert train_active_direct == False, "Direct load of resources.html must NOT activate view-training"

            # Test header positioning and scrolling on resources.html
            print("9. Testing fixed header positioning and scrolling on resources.html...")
            header_check = await evaluate("""
                (() => {
                    const topBar = document.querySelector('.top-utility-bar');
                    const mainNav = document.querySelector('.main-navbar') || document.querySelector('header');
                    const styleTop = window.getComputedStyle(topBar);
                    const styleMain = window.getComputedStyle(mainNav);
                    return {
                        topBarPos: styleTop.position,
                        topBarTop: styleTop.top,
                        mainNavPos: styleMain.position,
                        mainNavTop: styleMain.top
                    };
                })()
            """)
            print(f"   Top utility bar: pos={header_check['topBarPos']}, top={header_check['topBarTop']}")
            print(f"   Main navbar: pos={header_check['mainNavPos']}, top={header_check['mainNavTop']}")
            assert header_check['topBarPos'] == 'fixed', "Top utility bar must be fixed"
            assert header_check['mainNavPos'] == 'fixed', "Main navbar must be fixed"

            # Scroll down 800px and check rects
            await evaluate("window.scrollTo(0, 800);")
            await asyncio.sleep(0.5)
            rect_check = await evaluate("""
                (() => {
                    const topBar = document.querySelector('.top-utility-bar');
                    const mainNav = document.querySelector('.main-navbar') || document.querySelector('header');
                    const rectTop = topBar.getBoundingClientRect();
                    const rectMain = mainNav.getBoundingClientRect();
                    return {
                        scrollY: window.scrollY,
                        topBarBoundingTop: rectTop.top,
                        mainNavBoundingTop: rectMain.top
                    };
                })()
            """)
            print(f"   After scrolling down (scrollY={rect_check['scrollY']}):")
            print(f"     Top utility bar bounding top: {rect_check['topBarBoundingTop']}")
            print(f"     Main navbar bounding top: {rect_check['mainNavBoundingTop']}")
            assert rect_check['topBarBoundingTop'] == 0, "Top utility bar must remain at top 0"
            assert abs(rect_check['mainNavBoundingTop'] - 33) <= 2, "Main navbar must remain at top ~33px"

            print("\n============================================================")
            print("ALL 9 TEST SUITES PASSED! 100% VERIFICATION SUCCESSFUL.")
            print("============================================================")

    finally:
        proc.kill()

if __name__ == "__main__":
    asyncio.run(main())
