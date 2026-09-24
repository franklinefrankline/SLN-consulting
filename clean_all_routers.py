import os
import re

files = ['index.html', 'about.html', 'offerings.html', 'training.html', 'contact.html', 'enterprises.html', 'campus.html']

clean_route_map = '''    const routeMap = {
      'index.html': 'view-index',
      'index': 'view-index',
      '': 'view-index',
      '/': 'view-index',
      'about.html': 'view-about',
      'about': 'view-about',
      'about-us': 'view-about',
      'offerings.html': 'view-offerings',
      'offerings': 'view-offerings',
      'our-offerings': 'view-offerings',
      'our-offering': 'view-offerings',
      'offering': 'view-offerings',
      'offering.html': 'view-offerings',
      'training.html': 'view-training',
      'training': 'view-training',
      'contact.html': 'view-contact',
      'contact': 'view-contact',
      'contact-us': 'view-contact',
      'soc-as-a-service': 'view-soc',
      'soc': 'view-soc',
      'skilling-solutions': 'view-skilling',
      'skilling': 'view-skilling',
      'enterprises.html': 'view-enterprises',
      'enterprises': 'view-enterprises',
      'enterprise': 'view-enterprises',
      'skilling-enterprises': 'view-enterprises',
      'skilling-enterprise': 'view-enterprises',
      'campus.html': 'view-campus',
      'campus': 'view-campus',
      'skilling-campus': 'view-campus',
      'cambridge-learning': 'view-cambridge',
      'cambridge': 'view-cambridge',
      'isc2': 'view-isc2',
      'isc2-credentials': 'view-isc2',
      'ec-council': 'view-ec-council',
      'eccouncil': 'view-ec-council',
      'it-services': 'view-it-services'
    };'''

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace routeMap
    c = re.sub(r'const routeMap = \{.*?\};', clean_route_map, c, flags=re.DOTALL)

    # In popstate and DOMContentLoaded:
    # Ensure aliases for enterprises and campus are recognized
    if "if (path === 'enterprises' || path === 'enterprise') path = 'enterprises.html';" not in c:
        c = c.replace(
            "if (path === 'training') path = 'training.html';",
            "if (path === 'training') path = 'training.html';\n        if (path === 'enterprises' || path === 'enterprise') path = 'enterprises.html';\n        if (path === 'campus') path = 'campus.html';"
        )

    # In routePage:
    # Clean up scrolling: just smooth scroll to top 0
    c = re.sub(
        r'// Handle targeted section scrolling for Enterprises and Campus\s+if \(anchorId === \'skilling-enterprises\'[\s\S]*?window\.scrollTo\(\{ top: 0, behavior: \'smooth\' \}\);\s+\}',
        'window.scrollTo({ top: 0, behavior: "smooth" });',
        c
    )

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Cleaned and synchronized router in {fn}")

print("Done cleaning all files.")
