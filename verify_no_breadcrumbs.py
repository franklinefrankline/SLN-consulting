import glob

html_files = sorted(glob.glob('*.html'))
found_any = False
for f in html_files:
    if f in ['gemini_reference_design.html', 'original_sln_enterprise_platform.html']:
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for i, line in enumerate(lines):
        if '&rsaquo;' in line or '›' in line or 'Home >' in line or 'Home ›' in line:
            print(f"[{f}] Line {i+1}: {line.strip()[:100]}")
            found_any = True

if not found_any:
    print("SUCCESS: Zero breadcrumb symbols or text found in any of the 14 production HTML files!")
