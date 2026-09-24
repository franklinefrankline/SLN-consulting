import re

with open('offerings.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'<main id="view-offerings"[\s\S]*?</main>', content)
block = m.group(0)

def extract_section(sec_id):
    pattern = rf'(<section id="{sec_id}"[\s\S]*?</section>)'
    sm = re.search(pattern, block)
    return sm.group(1) if sm else ""

soc_sec = extract_section('soc-as-a-service')
skilling_sec = extract_section('skilling-solutions')
cambridge_sec = extract_section('cambridge-learning')
isc2_sec = extract_section('isc2')
eccouncil_sec = extract_section('ec-council')
it_sec = extract_section('it-services')

print(f"soc_sec length: {len(soc_sec)}")
print(f"skilling_sec length: {len(skilling_sec)}")
print(f"cambridge_sec length: {len(cambridge_sec)}")
print(f"isc2_sec length: {len(isc2_sec)}")
print(f"eccouncil_sec length: {len(eccouncil_sec)}")
print(f"it_sec length: {len(it_sec)}")
