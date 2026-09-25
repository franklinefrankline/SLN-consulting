import subprocess
import time
import urllib.request
import json
import asyncio
import websockets
import sys

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BREAKPOINTS = [320, 360, 375, 390, 414, 768, 991, 1024, 1280, 1440]
PAGES_TO_TEST = ['index.html', 'about.html', 'soc.html', 'internships.html', 'campus.html', 'contact.html', 'training.html']

async def run_full_suite():
    print("=" * 60)
    print(" SLN CONSULTING — BOTH HEADERS FIXED CDP VERIFICATION")
    print("=" * 60)

    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--remote-debugging-port=9222",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--window-size=1280,800",
        "http://localhost:5500/index.html"
    ]
    proc = subprocess.Popen(cmd)
    time.sleep(2)
    
    passed = 0
    failed = 0
    errors = []

    def check(condition, desc):
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"  [PASS] {desc}")
        else:
            failed += 1
            errors.append(desc)
            print(f"  [FAIL] {desc}")

    try:
        req = urllib.request.urlopen("http://localhost:9222/json")
        targets = json.loads(req.read().decode('utf-8'))
        ws_url = [t['webSocketDebuggerUrl'] for t in targets if t.get('type') == 'page'][0]

        async with websockets.connect(ws_url) as ws:
            cur_id = 1
            async def send_cmd(method, params=None):
                nonlocal cur_id
                cmd_id = cur_id
                cur_id += 1
                msg = {"id": cmd_id, "method": method}
                if params: msg["params"] = params
                await ws.send(json.dumps(msg))
                while True:
                    raw = await ws.recv()
                    data = json.loads(raw)
                    if data.get("id") == cmd_id:
                        return data.get("result", {})

            await send_cmd("Page.enable")
            await send_cmd("Runtime.enable")
            await asyncio.sleep(1)

            # -------------------------------------------------------------
            # TEST SUITE 1: Desktop Fixed Headers & Scroll Tests
            # -------------------------------------------------------------
            print("\n--- Test Suite 1: Desktop Initial State (scrollY = 0) ---")
            r0 = await send_cmd("Runtime.evaluate", {
                "expression": """JSON.stringify({
                    topBarRect: document.querySelector('.top-utility-bar').getBoundingClientRect(),
                    headerRect: document.querySelector('header').getBoundingClientRect(),
                    heroRect: document.querySelector('#hero-section').getBoundingClientRect(),
                    topBarComp: {
                        position: window.getComputedStyle(document.querySelector('.top-utility-bar')).position,
                        zIndex: window.getComputedStyle(document.querySelector('.top-utility-bar')).zIndex
                    },
                    headerComp: {
                        position: window.getComputedStyle(document.querySelector('header')).position,
                        zIndex: window.getComputedStyle(document.querySelector('header')).zIndex
                    }
                })"""
            })
            d0 = json.loads(r0.get('result', {}).get('value'))
            check(d0['topBarRect']['top'] == 0, "Top utility bar is at y = 0")
            check(d0['topBarComp']['position'] == 'fixed', f"Top utility bar position is fixed (got {d0['topBarComp']['position']})")
            check(d0['topBarComp']['zIndex'] == '10002', f"Top utility bar z-index is 10002 (got {d0['topBarComp']['zIndex']})")

            check(d0['headerRect']['top'] == 33, f"Main navbar is fixed at y = 33 directly below utility bar (got {d0['headerRect']['top']})")
            check(d0['headerComp']['position'] == 'fixed', f"Main navbar position is fixed (got {d0['headerComp']['position']})")
            check(d0['headerComp']['zIndex'] == '10001', f"Main navbar z-index is 10001 (got {d0['headerComp']['zIndex']})")

            check(d0['heroRect']['top'] == 110, f"Hero content starts exactly at y = 110 below both headers (got {d0['heroRect']['top']})")

            # Section 13: Scroll down 200px
            print("\n--- Test Suite 1: Scroll to 200px ---")
            await send_cmd("Runtime.evaluate", { "expression": "window.scrollTo({top: 200, behavior: 'instant'});" })
            await asyncio.sleep(0.3)
            r200 = await send_cmd("Runtime.evaluate", {
                "expression": """JSON.stringify({
                    scrollY: window.scrollY,
                    topBarTop: document.querySelector('.top-utility-bar').getBoundingClientRect().top,
                    headerTop: document.querySelector('header').getBoundingClientRect().top,
                    heroTop: document.querySelector('#hero-section').getBoundingClientRect().top
                })"""
            })
            d200 = json.loads(r200.get('result', {}).get('value'))
            check(d200['scrollY'] == 200, "Scroll position is 200px")
            check(d200['topBarTop'] == 0, f"Top utility bar remains fixed at top: 0 (got {d200['topBarTop']})")
            check(d200['headerTop'] == 33, f"Main navbar remains fixed at top: 33 (got {d200['headerTop']})")
            check(d200['heroTop'] < 0, f"Hero moves underneath both fixed headers (got {d200['heroTop']})")

            # Section 13: Scroll down 500px
            print("\n--- Test Suite 1: Scroll to 500px ---")
            await send_cmd("Runtime.evaluate", { "expression": "window.scrollTo({top: 500, behavior: 'instant'});" })
            await asyncio.sleep(0.3)
            r500 = await send_cmd("Runtime.evaluate", {
                "expression": """JSON.stringify({
                    scrollY: window.scrollY,
                    topBarTop: document.querySelector('.top-utility-bar').getBoundingClientRect().top,
                    headerTop: document.querySelector('header').getBoundingClientRect().top
                })"""
            })
            d500 = json.loads(r500.get('result', {}).get('value'))
            check(d500['scrollY'] == 500, "Scroll position is 500px")
            check(d500['topBarTop'] == 0, "Both header sections remain fixed: utility bar at y = 0")
            check(d500['headerTop'] == 33, "Both header sections remain fixed: main navbar at y = 33")

            # Section 13: Scroll to middle (~2000px)
            print("\n--- Test Suite 1: Scroll to Middle (2000px) ---")
            await send_cmd("Runtime.evaluate", { "expression": "window.scrollTo({top: 2000, behavior: 'instant'});" })
            await asyncio.sleep(0.3)
            r2000 = await send_cmd("Runtime.evaluate", {
                "expression": """JSON.stringify({
                    topBarTop: document.querySelector('.top-utility-bar').getBoundingClientRect().top,
                    headerTop: document.querySelector('header').getBoundingClientRect().top
                })"""
            })
            d2000 = json.loads(r2000.get('result', {}).get('value'))
            check(d2000['topBarTop'] == 0, "Middle of page: utility bar remains fixed at y = 0")
            check(d2000['headerTop'] == 33, "Middle of page: main navbar remains fixed at y = 33")

            # Section 13: Scroll to bottom
            print("\n--- Test Suite 1: Scroll to Bottom ---")
            await send_cmd("Runtime.evaluate", { "expression": "window.scrollTo({top: document.body.scrollHeight, behavior: 'instant'});" })
            await asyncio.sleep(0.3)
            r_bot = await send_cmd("Runtime.evaluate", {
                "expression": """JSON.stringify({
                    scrollY: window.scrollY,
                    topBarTop: document.querySelector('.top-utility-bar').getBoundingClientRect().top,
                    headerTop: document.querySelector('header').getBoundingClientRect().top
                })"""
            })
            dbot = json.loads(r_bot.get('result', {}).get('value'))
            check(dbot['topBarTop'] == 0, f"Absolute bottom: utility bar remains fixed at y = 0 (scrollY = {dbot['scrollY']})")
            check(dbot['headerTop'] == 33, f"Absolute bottom: main navbar remains fixed at y = 33 (scrollY = {dbot['scrollY']})")

            # -------------------------------------------------------------
            # TEST SUITE 2: Section 7 Dropdown Compatibility
            # -------------------------------------------------------------
            print("\n--- Test Suite 2: Cybersecurity Dropdown at scroll 500px ---")
            await send_cmd("Runtime.evaluate", { "expression": "window.scrollTo({top: 500, behavior: 'instant'});" })
            await asyncio.sleep(0.3)
            r_drop = await send_cmd("Runtime.evaluate", {
                "expression": """(() => {
                    const btn = document.querySelector('button[data-route="soc.html"]');
                    btn.click();
                    const dropdown = document.getElementById('dropdown-cybersecurity');
                    const comp = window.getComputedStyle(dropdown);
                    const rect = dropdown.getBoundingClientRect();
                    const btnRect = btn.getBoundingClientRect();
                    return JSON.stringify({
                        dropdownDisplay: comp.display,
                        dropdownZIndex: comp.zIndex,
                        buttonBottom: btnRect.bottom,
                        dropdownTop: rect.top,
                        items: Array.from(dropdown.querySelectorAll('a')).map(a => a.innerText.trim())
                    });
                })()"""
            })
            dd = json.loads(r_drop.get('result', {}).get('value'))
            check(dd['dropdownDisplay'] == 'block', "Cybersecurity dropdown display is block")
            check(dd['dropdownZIndex'] == '10003', f"Cybersecurity dropdown z-index is 10003 (got {dd['dropdownZIndex']})")
            check(dd['dropdownTop'] >= dd['buttonBottom'], f"Dropdown appears below button ({dd['dropdownTop']} >= {dd['buttonBottom']})")
            check('SaaS' in dd['items'] and 'VAPT' in dd['items'], f"Dropdown contains SaaS and VAPT (got {dd['items']})")

            # -------------------------------------------------------------
            # TEST SUITE 3: Section 9 Responsive Breakpoints (320px to 1440px)
            # -------------------------------------------------------------
            print("\n--- Test Suite 3: Responsive Breakpoints Test ---")
            for bp in BREAKPOINTS:
                print(f">> Breakpoint: {bp}px")
                await send_cmd("Emulation.setDeviceMetricsOverride", {
                    "width": bp,
                    "height": 800,
                    "deviceScaleFactor": 1,
                    "mobile": bp < 992
                })
                await asyncio.sleep(0.3)
                
                # Check horizontal overflow
                r_ov = await send_cmd("Runtime.evaluate", {
                    "expression": """JSON.stringify({
                        scrollWidth: document.documentElement.scrollWidth,
                        innerWidth: window.innerWidth,
                        hasHorizontalOverflow: document.documentElement.scrollWidth > window.innerWidth
                    })"""
                })
                d_ov = json.loads(r_ov.get('result', {}).get('value'))
                check(not d_ov['hasHorizontalOverflow'], f"{bp}px: No horizontal overflow ({d_ov['scrollWidth']} <= {d_ov['innerWidth']})")

                # Scroll to 300px
                await send_cmd("Runtime.evaluate", { "expression": "window.scrollTo({top: 300, behavior: 'instant'});" })
                await asyncio.sleep(0.3)
                r_bp_s = await send_cmd("Runtime.evaluate", {
                    "expression": """JSON.stringify({
                        topBarTop: document.querySelector('.top-utility-bar').getBoundingClientRect().top,
                        headerTop: document.querySelector('header').getBoundingClientRect().top
                    })"""
                })
                d_bps = json.loads(r_bp_s.get('result', {}).get('value'))
                check(d_bps['topBarTop'] == 0, f"{bp}px: Utility bar remains fixed at y = 0 while scrolling")
                check(d_bps['headerTop'] == 33, f"{bp}px: Main navbar remains fixed at y = 33 while scrolling")

                # Mobile menu check (< 992px)
                if bp < 992:
                    await send_cmd("Runtime.evaluate", { "expression": "document.getElementById('mobileMenuBtn').click();" })
                    await asyncio.sleep(0.3) # Wait for animation
                    r_mob = await send_cmd("Runtime.evaluate", {
                        "expression": """(() => {
                            const btn = document.getElementById('mobileMenuBtn');
                            const drawer = document.getElementById('mobileDrawer');
                            const topBar = document.querySelector('.top-utility-bar');
                            const header = document.querySelector('header');
                            return JSON.stringify({
                                isOpen: !drawer.classList.contains('hidden'),
                                topBarTop: topBar.getBoundingClientRect().top,
                                drawerTop: Math.round(drawer.getBoundingClientRect().top),
                                headerBottom: Math.round(header.getBoundingClientRect().bottom)
                            });
                        })()"""
                    })
                    dm = json.loads(r_mob.get('result', {}).get('value'))
                    check(dm['isOpen'], f"{bp}px: Mobile hamburger opens drawer")
                    check(dm['topBarTop'] == 0, f"{bp}px: Mobile drawer does NOT move utility bar")
                    check(abs(dm['drawerTop'] - dm['headerBottom']) <= 1, f"{bp}px: Drawer appears directly below main navbar ({dm['drawerTop']} ~= {dm['headerBottom']})")

                    # Close menu
                    await send_cmd("Runtime.evaluate", { "expression": "document.getElementById('mobileMenuBtn').click();" })
                    await asyncio.sleep(0.1)

            # -------------------------------------------------------------
            # TEST SUITE 4: Multi-Page Test across 7 production pages
            # -------------------------------------------------------------
            print("\n--- Test Suite 4: Multi-Page Verification ---")
            for page in PAGES_TO_TEST:
                await send_cmd("Page.navigate", {"url": f"http://localhost:5500/{page}"})
                await asyncio.sleep(1)
                await send_cmd("Emulation.setDeviceMetricsOverride", { "width": 1280, "height": 800, "deviceScaleFactor": 1, "mobile": False })
                await asyncio.sleep(0.2)
                
                await send_cmd("Runtime.evaluate", { "expression": "window.scrollTo({top: 400, behavior: 'instant'});" })
                await asyncio.sleep(0.3)
                r_page = await send_cmd("Runtime.evaluate", {
                    "expression": """JSON.stringify({
                        topBarTop: document.querySelector('.top-utility-bar').getBoundingClientRect().top,
                        headerTop: document.querySelector('header').getBoundingClientRect().top
                    })"""
                })
                dp = json.loads(r_page.get('result', {}).get('value'))
                check(dp['topBarTop'] == 0, f"{page}: Utility bar remains fixed at y = 0")
                check(dp['headerTop'] == 33, f"{page}: Main navbar remains fixed at y = 33")

    finally:
        proc.terminate()

    print("\n" + "=" * 60)
    print(f"VERIFICATION RESULTS: {passed} PASSED, {failed} FAILED")
    print("=" * 60)
    if errors:
        for e in errors:
            print("  - ", e)
        sys.exit(1)
    else:
        print("ALL TESTS PASSED WITH 100% SUCCESS!")

asyncio.run(run_full_suite())
