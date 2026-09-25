import subprocess
import time
import urllib.request
import json
import asyncio
import websockets
import sys

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BREAKPOINTS = [320, 360, 375, 390, 414, 768, 991, 1024, 1280, 1440]

async def run_full_verification():
    print("=" * 60)
    print(" SLN CONSULTING — STICKY NAVBAR CDP VERIFICATION SUITE")
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
        ws_url = None
        for t in targets:
            if t.get('type') == 'page':
                ws_url = t.get('webSocketDebuggerUrl')
                break
        
        async with websockets.connect(ws_url) as ws:
            cur_id = 1
            async def send_cmd(method, params=None):
                nonlocal cur_id
                cmd_id = cur_id
                cur_id += 1
                msg = {"id": cmd_id, "method": method}
                if params:
                    msg["params"] = params
                await ws.send(json.dumps(msg))
                while True:
                    raw = await ws.recv()
                    data = json.loads(raw)
                    if data.get("id") == cmd_id:
                        return data.get("result", {})

            await send_cmd("Page.enable")
            await send_cmd("Runtime.enable")
            await asyncio.sleep(1)

            # TEST 1: Initial state at scroll 0 (Desktop 1280)
            print("\n--- Test 1: Desktop Initial State (scrollY = 0) ---")
            r0 = await send_cmd("Runtime.evaluate", {
                "expression": """JSON.stringify({
                    topBarRect: document.querySelector('.top-utility-bar').getBoundingClientRect(),
                    headerRect: document.querySelector('header').getBoundingClientRect(),
                    headerComp: {
                        position: window.getComputedStyle(document.querySelector('header')).position,
                        zIndex: window.getComputedStyle(document.querySelector('header')).zIndex
                    }
                })"""
            })
            d0 = json.loads(r0.get('result', {}).get('value'))
            check(d0['topBarRect']['top'] == 0, "Top utility bar is at y = 0")
            check(d0['headerRect']['top'] >= 30 and d0['headerRect']['top'] <= 40, f"Header is immediately below utility bar (y = {d0['headerRect']['top']})")
            check(d0['headerComp']['position'] == 'sticky', f"Header position is sticky (got {d0['headerComp']['position']})")
            check(d0['headerComp']['zIndex'] == '10000', f"Header z-index is 10000 (got {d0['headerComp']['zIndex']})")

            # TEST 2: Section 11 Scroll Test: 200px, 500px, middle (~2000px), bottom
            scroll_positions = [200, 500, 2000]
            for spos in scroll_positions:
                print(f"\n--- Test 2: Scroll to {spos}px ---")
                await send_cmd("Runtime.evaluate", {
                    "expression": f"window.scrollTo({{top: {spos}, behavior: 'instant'}});"
                })
                await asyncio.sleep(0.3)
                r_scroll = await send_cmd("Runtime.evaluate", {
                    "expression": """JSON.stringify({
                        scrollY: window.scrollY,
                        topBarTop: document.querySelector('.top-utility-bar').getBoundingClientRect().top,
                        headerTop: document.querySelector('header').getBoundingClientRect().top,
                        headerBottom: document.querySelector('header').getBoundingClientRect().bottom
                    })"""
                })
                ds = json.loads(r_scroll.get('result', {}).get('value'))
                check(ds['scrollY'] == spos, f"Scroll position is {spos}px")
                check(ds['headerTop'] == 0, f"Header remains exactly at top (y = 0) at scroll {spos}px")
                check(ds['topBarTop'] < 0, f"Top utility bar has scrolled away (y = {ds['topBarTop']})")

            # Scroll to absolute bottom
            print("\n--- Test 3: Scroll to Absolute Bottom ---")
            await send_cmd("Runtime.evaluate", {
                "expression": "window.scrollTo({top: document.body.scrollHeight, behavior: 'instant'});"
            })
            await asyncio.sleep(0.3)
            r_bot = await send_cmd("Runtime.evaluate", {
                "expression": """JSON.stringify({
                    scrollY: window.scrollY,
                    headerTop: document.querySelector('header').getBoundingClientRect().top
                })"""
            })
            db = json.loads(r_bot.get('result', {}).get('value'))
            check(db['headerTop'] == 0, f"Header remains at top: 0 at absolute page bottom (scrollY = {db['scrollY']})")

            # TEST 4: Dropdown Compatibility at scroll 500px
            print("\n--- Test 4: Cybersecurity Dropdown at scroll 500px ---")
            await send_cmd("Runtime.evaluate", {
                "expression": "window.scrollTo({top: 500, behavior: 'instant'});"
            })
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
                        dropdownVisibility: comp.visibility,
                        dropdownZIndex: comp.zIndex,
                        buttonBottom: btnRect.bottom,
                        dropdownTop: rect.top,
                        items: Array.from(dropdown.querySelectorAll('a')).map(a => a.innerText.trim())
                    });
                })()"""
            })
            dd = json.loads(r_drop.get('result', {}).get('value'))
            check(dd['dropdownDisplay'] == 'block', "Cybersecurity dropdown display is block")
            check(dd['dropdownZIndex'] == '10001', f"Cybersecurity dropdown z-index is 10001 (got {dd['dropdownZIndex']})")
            check(dd['dropdownTop'] >= dd['buttonBottom'], f"Dropdown appears below button ({dd['dropdownTop']} >= {dd['buttonBottom']})")
            check('SaaS' in dd['items'] and 'VAPT' in dd['items'], f"Dropdown contains SaaS and VAPT (got {dd['items']})")

            # TEST 5: Close dropdown and route to another page
            print("\n--- Test 5: In-Page Navigation / Page Switch ---")
            r_route = await send_cmd("Runtime.evaluate", {
                "expression": """(() => {
                    routePage(null, 'about.html');
                    const activeView = document.querySelector('.page-view.active');
                    const header = document.querySelector('header');
                    return JSON.stringify({
                        activeViewId: activeView ? activeView.id : null,
                        headerTop: header.getBoundingClientRect().top
                    });
                })()"""
            })
            dr = json.loads(r_route.get('result', {}).get('value'))
            check(dr['activeViewId'] == 'view-about', f"Successfully routed to view-about (got {dr['activeViewId']})")
            check(dr['headerTop'] == 0, f"Header is still at top (y = 0) on About page")

            # Reset back to Home
            await send_cmd("Runtime.evaluate", { "expression": "routePage(null, 'index.html');" })
            await asyncio.sleep(0.3)

            # TEST 6: Responsive Breakpoints Test
            print("\n--- Test 6: Responsive Breakpoints Test ---")
            for bp in BREAKPOINTS:
                print(f"\n>> Testing Breakpoint: {bp}px")
                await send_cmd("Emulation.setDeviceMetricsOverride", {
                    "width": bp,
                    "height": 800,
                    "deviceScaleFactor": 1,
                    "mobile": bp < 992
                })
                await asyncio.sleep(0.3)
                
                # Check horizontal overflow at scroll 0
                r_overflow = await send_cmd("Runtime.evaluate", {
                    "expression": """JSON.stringify({
                        scrollWidth: document.documentElement.scrollWidth,
                        innerWidth: window.innerWidth,
                        hasHorizontalOverflow: document.documentElement.scrollWidth > window.innerWidth
                    })"""
                })
                d_ov = json.loads(r_overflow.get('result', {}).get('value'))
                check(not d_ov['hasHorizontalOverflow'], f"{bp}px: No horizontal overflow (scrollWidth {d_ov['scrollWidth']} <= innerWidth {d_ov['innerWidth']})")
                
                # Scroll to 300px
                await send_cmd("Runtime.evaluate", {
                    "expression": "window.scrollTo({top: 300, behavior: 'instant'});"
                })
                await asyncio.sleep(0.3)
                
                r_bp_scroll = await send_cmd("Runtime.evaluate", {
                    "expression": """JSON.stringify({
                        headerTop: document.querySelector('header').getBoundingClientRect().top,
                        headerVisible: document.querySelector('header').getBoundingClientRect().height > 0
                    })"""
                })
                d_bps = json.loads(r_bp_scroll.get('result', {}).get('value'))
                check(d_bps['headerTop'] == 0, f"{bp}px: Navbar remains visible at top: 0 while scrolling at 300px")

                # Mobile-specific test (< 992px)
                if bp < 992:
                    # Open menu and wait for animation to complete
                    await send_cmd("Runtime.evaluate", {
                        "expression": "document.getElementById('mobileMenuBtn').click();"
                    })
                    await asyncio.sleep(0.3) # Wait for 0.22s CSS animation
                    
                    r_mob = await send_cmd("Runtime.evaluate", {
                        "expression": """(() => {
                            const btn = document.getElementById('mobileMenuBtn');
                            const drawer = document.getElementById('mobileDrawer');
                            if (!btn || !drawer) return JSON.stringify({ error: 'missing elements' });
                            
                            const isOpen = !drawer.classList.contains('hidden');
                            const drawerComp = window.getComputedStyle(drawer);
                            const drawerRect = drawer.getBoundingClientRect();
                            const headerRect = document.querySelector('header').getBoundingClientRect();
                            
                            return JSON.stringify({
                                isOpen: isOpen,
                                drawerZIndex: drawerComp.zIndex,
                                drawerTop: Math.round(drawerRect.top),
                                headerBottom: Math.round(headerRect.bottom)
                            });
                        })()"""
                    })
                    dm = json.loads(r_mob.get('result', {}).get('value'))
                    check(dm['isOpen'], f"{bp}px: Mobile hamburger opens drawer")
                    check(dm['drawerZIndex'] == '10002', f"{bp}px: Mobile drawer z-index is 10002 (got {dm['drawerZIndex']})")
                    check(abs(dm['drawerTop'] - dm['headerBottom']) <= 1, f"{bp}px: Drawer opens directly below navbar ({dm['drawerTop']} ~= {dm['headerBottom']})")

                    # Close menu
                    await send_cmd("Runtime.evaluate", {
                        "expression": "document.getElementById('mobileMenuBtn').click();"
                    })
                    await asyncio.sleep(0.1)
                    r_close = await send_cmd("Runtime.evaluate", {
                        "expression": "document.getElementById('mobileDrawer').classList.contains('hidden');"
                    })
                    is_closed = r_close.get('result', {}).get('value')
                    check(is_closed, f"{bp}px: Mobile hamburger closes drawer")

    finally:
        proc.terminate()

    print("\n" + "=" * 60)
    print(f"VERIFICATION RESULTS: {passed} PASSED, {failed} FAILED")
    print("=" * 60)
    if errors:
        print("FAILURES:")
        for e in errors:
            print("  - ", e)
        sys.exit(1)
    else:
        print("ALL TESTS PASSED WITH 100% SUCCESS!")

asyncio.run(run_full_verification())
