import os
import re

files = ['index.html', 'about.html', 'offerings.html', 'training.html', 'contact.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all img src
    img_matches = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', html, re.IGNORECASE)
    # Also find if src is before other attributes
    img_matches += re.findall(r'<img\s+src=["\']([^"\']+)["\']', html, re.IGNORECASE)
    # Background images
    bg_matches = re.findall(r'url\(["\']?([^"\'\)]+)["\']?\)', html, re.IGNORECASE)

    print(f"\n==================== {fn} ====================")
    unique_imgs = sorted(list(set(img_matches)))
    print(f"Total unique <img> sources: {len(unique_imgs)}")
    for src in unique_imgs:
        if src.startswith('http://') or src.startswith('https://'):
            print(f"  [EXTERNAL] {src}")
        elif src.startswith('data:'):
            print(f"  [DATA-URI]")
        else:
            exists = os.path.exists(src)
            print(f"  [LOCAL] exists={exists}: {src}")

    unique_bgs = sorted(list(set(bg_matches)))
    print(f"Total unique CSS urls: {len(unique_bgs)}")
    for bg in unique_bgs:
        if bg.startswith('http://') or bg.startswith('https://'):
            print(f"  [EXTERNAL BG] {bg}")
        elif bg.startswith('data:'):
            pass
        else:
            exists = os.path.exists(bg)
            print(f"  [LOCAL BG] exists={exists}: {bg}")
