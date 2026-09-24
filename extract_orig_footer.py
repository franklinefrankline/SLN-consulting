import json

with open(r'C:\Users\dhushyanth\.gemini\antigravity-ide\brain\b4b76897-4c86-4737-822d-bfa24e5768fc\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if 'Emergency SOC Dispatch' in line and '<footer' in line:
            data = json.loads(line)
            # Find the html content
            text = str(data)
            idx = text.find('<footer')
            if idx != -1:
                end_idx = text.find('</footer>', idx)
                if end_idx != -1:
                    full_footer = text[idx:end_idx+9]
                    # unescape
                    full_footer = full_footer.encode('utf-8').decode('unicode_escape')
                    with open('c:/Agen/SLN counsulting/scratch_orig_footer.html', 'w', encoding='utf-8') as out:
                        out.write(full_footer)
                    print('Wrote scratch_orig_footer.html, length:', len(full_footer))
                    break
