import urllib.request
import time

URLS = [
    'https://sln-consulting.vercel.app/',
    'https://sln-consulting.vercel.app/about.html',
    'https://sln-consulting.vercel.app/soc.html',
    'https://sln-consulting.vercel.app/it-services.html',
    'https://sln-consulting.vercel.app/campus.html',
    'https://sln-consulting.vercel.app/internships.html',
    'https://sln-consulting.vercel.app/training.html',
    'https://sln-consulting.vercel.app/training-schedule.html',
    'https://sln-consulting.vercel.app/enterprises.html',
    'https://sln-consulting.vercel.app/contact.html',
    'https://sln-consulting.vercel.app/isc2.html',
    'https://sln-council.vercel.app/', # skip if not needed
    'https://sln-consulting.vercel.app/ec-council.html',
    'https://sln-consulting.vercel.app/cambridge.html',
    'https://sln-consulting.vercel.app/offerings.html'
]

print("Verifying live Vercel deployment...")
for attempt in range(1, 10):
    try:
        req = urllib.request.Request(
            'https://sln-consulting.vercel.app/',
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8')
            has_mega_grid = 'mega-menu-grid' in content
            has_w880 = 'w-[880px]' in content
            has_minmax = 'minmax(0, 1fr)' in content

            print(f"Attempt {attempt}: mega-menu-grid={has_mega_grid}, w-[880px]={has_w880}, minmax={has_minmax}")
            if has_mega_grid and has_w880 and has_minmax:
                print("SUCCESS: Vercel has deployed the updated build!")
                break
    except Exception as e:
        print(f"Attempt {attempt} error: {e}")
    time.sleep(4)

print("\nVerifying all live routes return 200 OK:")
routes = [
    '/',
    '/about.html',
    '/soc.html',
    '/it-services.html',
    '/campus.html',
    '/internships.html',
    '/training.html',
    '/training-schedule.html',
    '/enterprises.html',
    '/contact.html',
    '/isc2.html',
    '/ec-council.html',
    '/cambridge.html',
    '/offerings.html'
]

all_ok = True
for r in routes:
    url = f"https://sln-consulting.vercel.app{r}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            code = resp.getcode()
            print(f"  [PASS] {url} -> {code}")
    except Exception as e:
        print(f"  [FAIL] {url} -> {e}")
        all_ok = False

if all_ok:
    print("\nALL 14 LIVE ROUTES ARE FUNCTIONING WITH 200 OK!")
