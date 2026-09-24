# update_logo.py
import os
import re

workspace = os.path.abspath(os.path.dirname(__file__))

new_header_brand = '''      <!-- Left: Official SLN Consulting Brand Logo -->
      <a href="index.html" onclick="routePage(event, 'index.html')" class="flex items-center shrink-0 group focus:outline-none py-0.5" aria-label="SLN Consulting Home">
        <div class="transition-transform group-hover:scale-[1.02] dark:bg-white dark:p-1.5 dark:rounded-lg dark:border dark:border-slate-700/60 dark:shadow-sm">
          <img src="assets/images/sln-consulting-logo.png" alt="SLN Consulting - Solutions for Seamless Growth" class="h-8 sm:h-9 md:h-10 lg:h-11 w-auto object-contain block" style="max-height: 44px; width: auto;" />
        </div>
      </a>'''

new_footer_brand = '''          <a href="index.html" onclick="routePage(event, 'index.html')" class="inline-block group focus:outline-none" aria-label="SLN Consulting Home">
            <div class="inline-flex items-center justify-center bg-white px-3.5 py-2 rounded-xl shadow-sm border border-slate-200/50 group-hover:shadow-md transition-all">
              <img src="assets/images/sln-consulting-logo.png" alt="SLN Consulting - Solutions for Seamless Growth" class="h-8 sm:h-9 md:h-10 w-auto object-contain block" style="max-height: 40px; width: auto;" />
            </div>
          </a>'''

html_files = [
    'index.html',
    'about.html',
    'offerings.html',
    'training.html',
    'training-schedule.html',
    'contact.html',
    'enterprises.html',
    'campus.html'
]

for hf in html_files:
    file_path = os.path.join(workspace, hf)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    header_pattern = re.compile(r'<!-- Left: (?:SLN Logo Badge \+ Name \+ Tagline|Official SLN Consulting Brand Logo) -->.*?</a>\n\n            ', re.DOTALL)
    footer_pattern = re.compile(r'<!-- Column 1: SLN Brand Area \(lg:col-span-3\) -->\s*<div class="sm:col-span-2 lg:col-span-3 space-y-3">\s*(?:<div class="flex items-center gap-3">.*?</div>\s*</div>|<a href="index\.html".*?</a>)\s*<p class="text-slate-400', re.DOTALL)

    h_match = header_pattern.search(content)
    f_match = footer_pattern.search(content)

    if h_match and f_match:
        content = header_pattern.sub(new_header_brand + '\n\n            ', content, count=1)
        replacement_footer = f'<!-- Column 1: SLN Brand Area (lg:col-span-3) -->\n        <div class="sm:col-span-2 lg:col-span-3 space-y-3">\n{new_footer_brand}\n          \n          <p class="text-slate-400'
        content = footer_pattern.sub(replacement_footer, content, count=1)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[SUCCESS] Updated {hf}")
    else:
        print(f"[FAIL] {hf}: h_match={bool(h_match)}, f_match={bool(f_match)}")

print("\nDone updating logo across files.")
