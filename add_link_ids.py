import os
import re

files = ['index.html', 'about.html', 'offerings.html', 'training.html', 'contact.html', 'enterprises.html', 'campus.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # Add id="navLinkEnterprises" if not present
    c = re.sub(
        r'<a\s+href="enterprises\.html"(?![^>]*id="navLinkEnterprises")',
        '<a href="enterprises.html" id="navLinkEnterprises"',
        c
    )

    # Add id="navLinkCampus" if not present
    c = re.sub(
        r'<a\s+href="campus\.html"(?![^>]*id="navLinkCampus")',
        '<a href="campus.html" id="navLinkCampus"',
        c
    )

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)

print("Added IDs to all nav links.")
