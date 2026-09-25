import urllib.request
import time
import sys

URL = 'https://sln-consulting.vercel.app/'

print("Checking live Vercel deployment status...")

routes = [
    '/',
    '/resources.html',
    '/resources',
    '/about.html',
    '/about',
    '/soc.html',
    '/it-services.html',
    '/campus.html',
    '/internships.html',
    '/training.html',
    '/training',
    '/training-schedule.html',
    '/enterprises.html',
    '/contact.html',
    '/isc2.html',
    '/ec-council.html',
    '/cambridge.html',
    '/offerings.html'
]

print("\nVerifying all live routes return 200 OK:")
all_ok = True
for r in routes:
    url = f"https://sln-consulting.vercel.app{r}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            code = resp.getcode()
            print(f"  [PASS] {url} -> {code}")
    except Exception as e:
        print(f"  [FAIL] {url} -> {e}")
        all_ok = False

if all_ok:
    print("\nALL LIVE ROUTES ARE FUNCTIONING WITH 200 OK!")
else:
    print("\nSOME ROUTES FAILED.")
