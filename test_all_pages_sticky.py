import subprocess
import time
import urllib.request
import json
import asyncio
import websockets
import sys

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PAGES_TO_TEST = ['index.html', 'about.html', 'soc.html', 'internships.html', 'campus.html', 'contact.html', 'training.html']

async def run_multi_page_test():
    print("=" * 60)
    print(" TESTING STICKY NAVBAR ACROSS MULTIPLE PRODUCTION PAGES")
    print("=" * 60)

    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--remote-debugging-port=9222",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--window-size=1280,800"
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

            for page in PAGES_TO_TEST:
                print(f"\n--- Testing Page: {page} ---")
                await send_cmd("Page.navigate", {"url": f"http://localhost:5500/{page}"})
                await asyncio.sleep(1.5)

                # Reset to desktop view
                await send_cmd("Emulation.setDeviceMetricsOverride", {
                    "width": 1280,
                    "height": 800,
                    "deviceScaleFactor": 1,
                    "mobile": False
                })
                await asyncio.sleep(0.3)

                # Initial state check
                r0 = await send_cmd("Runtime.evaluate", {
                    "expression": """(() => {
                        const topBar = document.querySelector('.top-utility-bar');
                        const header = document.querySelector('header');
                        if (!topBar || !header) return JSON.stringify({ error: 'not found' });
                        return JSON.stringify({
                            topBarRect: topBar.getBoundingClientRect(),
                            headerRect: header.getBoundingClientRect(),
                            headerComp: {
                                position: window.getComputedStyle(header).position,
                                zIndex: window.getComputedStyle(header).zIndex
                            }
                        });
                    })()"""
                })
                val0 = r0.get('result', {}).get('value')
                if not val0:
                    print(f"Failed to evaluate on {page}: {r0}")
                    continue
                d0 = json.loads(val0)
                check(d0['topBarRect']['top'] == 0, f"{page}: Top utility bar at y = 0")
                check(d0['headerComp']['position'] == 'sticky', f"{page}: Header position is sticky")
                check(d0['headerComp']['zIndex'] == '10000', f"{page}: Header z-index is 10000")

                # Scroll to 600px
                await send_cmd("Runtime.evaluate", {
                    "expression": "window.scrollTo({top: 600, behavior: 'instant'});"
                })
                await asyncio.sleep(0.3)
                r600 = await send_cmd("Runtime.evaluate", {
                    "expression": """JSON.stringify({
                        scrollY: window.scrollY,
                        headerTop: document.querySelector('header').getBoundingClientRect().top,
                        topBarTop: document.querySelector('.top-utility-bar').getBoundingClientRect().top
                    })"""
                })
                d600 = json.loads(r600.get('result', {}).get('value'))
                check(d600['headerTop'] == 0, f"{page}: Header remains at top: 0 at scroll 600px")
                check(d600['topBarTop'] < 0, f"{page}: Top utility bar scrolled away")

                # Dropdown at scroll 600px
                rdrop = await send_cmd("Runtime.evaluate", {
                    "expression": """(() => {
                        const btn = document.querySelector('button[data-route="soc.html"]');
                        btn.click();
                        const dd = document.getElementById('dropdown-cybersecurity');
                        const comp = window.getComputedStyle(dd);
                        return JSON.stringify({
                            display: comp.display,
                            zIndex: comp.zIndex
                        });
                    })()"""
                })
                dd = json.loads(rdrop.get('result', {}).get('value'))
                check(dd['display'] == 'block', f"{page}: Dropdown opens at scroll 600")
                check(dd['zIndex'] == '10001', f"{page}: Dropdown z-index is 10001")

                # Mobile test (375px)
                await send_cmd("Emulation.setDeviceMetricsOverride", {
                    "width": 375,
                    "height": 800,
                    "deviceScaleFactor": 1,
                    "mobile": True
                })
                await asyncio.sleep(0.3)
                await send_cmd("Runtime.evaluate", {
                    "expression": "window.scrollTo({top: 350, behavior: 'instant'});"
                })
                await asyncio.sleep(0.3)
                rmob = await send_cmd("Runtime.evaluate", {
                    "expression": """(() => {
                        const h = document.querySelector('header');
                        const btn = document.getElementById('mobileMenuBtn');
                        const drawer = document.getElementById('mobileDrawer');
                        btn.click();
                        const isOpen = !drawer.classList.contains('hidden');
                        const drawerComp = window.getComputedStyle(drawer);
                        return JSON.stringify({
                            headerTop: h.getBoundingClientRect().top,
                            isOpen: isOpen,
                            drawerZIndex: drawerComp.zIndex
                        });
                    })()"""
                })
                dm = json.loads(rmob.get('result', {}).get('value'))
                check(dm['headerTop'] == 0, f"{page}: Mobile header at top: 0 while scrolling")
                check(dm['isOpen'], f"{page}: Mobile drawer opened")
                check(dm['drawerZIndex'] == '10002', f"{page}: Mobile drawer z-index is 10002")

    finally:
        proc.terminate()

    print("\n" + "=" * 60)
    print(f"MULTI-PAGE RESULTS: {passed} PASSED, {failed} FAILED")
    print("=" * 60)
    if errors:
        sys.exit(1)

asyncio.run(run_multi_page_test())
