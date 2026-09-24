import re

with open('offerings.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if '<img' in line:
        # print line and next 3 lines
        chunk = "".join(lines[max(0, idx-1):min(len(lines), idx+6)])
        print(f"--- Line {idx+1} ---")
        print(chunk.strip())
