# update_mobile_drawer_and_resync.py
import os
import re

workspace = os.path.abspath(os.path.dirname(__file__))
index_path = os.path.join(workspace, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Exact mobile block replacement
old_pattern = re.compile(
    r'<!-- Mobile Our Offering with Collapsible Submenu -->.*?<a href="training\.html"',
    re.DOTALL
)

new_mobile_block = '''<!-- Mobile Our Offering with Collapsible Submenu -->
      <div class="border-b border-[var(--border-white)]/40 pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileOfferingsMenu(event)">
          <span class="text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">Our Offering</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-500 hover:text-[var(--text-white-head)] hover:bg-slate-100 dark:hover:bg-[#24282C] focus:outline-none" aria-label="Toggle Our Offering submenu" id="mobileOfferingsToggleBtn">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileOfferingsChevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>

        <!-- Mobile Submenu (Direct 1-Click Access) -->
        <div id="mobileOfferingsSubmenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-slate-50 dark:bg-[#15181B] rounded-xl border border-[var(--border-white)] my-1">
          <!-- 01 SOC -->
          <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="flex items-center gap-2.5 py-2 px-2 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] rounded-lg transition-colors">
            <span class="font-mono text-[10px] text-[#B08D57] dark:text-[#D6A84F] font-bold w-5 shrink-0">01</span>
            <span class="text-slate-400 dark:text-slate-600 text-xs shrink-0">—</span>
            <span class="truncate">SOC-As-A-Service</span>
          </a>

          <!-- 02 Skilling Solutions with nested expansion -->
          <div>
            <div class="flex items-center justify-between py-1 px-2 rounded-lg hover:bg-slate-100 dark:hover:bg-[#202428] cursor-pointer" onclick="toggleMobileSkillingSubmenu(event)">
              <div class="flex items-center gap-2.5 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors truncate flex-1 min-w-0">
                <span class="font-mono text-[10px] text-[#B08D57] dark:text-[#D6A84F] font-bold w-5 shrink-0">02</span>
                <span class="text-slate-400 dark:text-slate-600 text-xs shrink-0">—</span>
                <span class="truncate">Skilling Solutions</span>
              </div>
              <button type="button" class="p-1 rounded text-slate-400 hover:text-[#B08D57] dark:hover:text-[#D6A84F] focus:outline-none" aria-label="Toggle Skilling nested submenu" id="mobileSkillingToggleBtn">
                <svg class="w-3.5 h-3.5 transition-transform duration-200" id="mobileSkillingChevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="6 9 12 15 18 9"></polyline>
                </svg>
              </button>
            </div>

            <!-- Nested Enterprises & Campus -->
            <div id="mobileSkillingSubmenu" class="hidden pl-8 pr-2 py-1 space-y-1 bg-white dark:bg-[#1B1E21] rounded-lg border border-[var(--border-white)] my-1">
              <a href="enterprises.html" id="mobileNavLinkEnterprises" onclick="routePage(event, 'enterprises.html'); toggleMobileNav();" class="flex items-center gap-2 px-2 py-1.5 hover:bg-slate-50 dark:hover:bg-[#202428] text-xs font-medium text-slate-700 dark:text-slate-200 transition-colors group/sub">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Enterprises</span>
              </a>
              <a href="campus.html" id="mobileNavLinkCampus" onclick="routePage(event, 'campus.html'); toggleMobileNav();" class="flex items-center gap-2 px-2 py-1.5 hover:bg-slate-50 dark:hover:bg-[#202428] text-xs font-medium text-slate-700 dark:text-slate-200 transition-colors group/sub">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Campus</span>
              </a>
            </div>
          </div>

          <!-- 03 Cambridge -->
          <a href="cambridge.html" onclick="routePage(event, 'cambridge.html'); toggleMobileNav();" class="flex items-center gap-2.5 py-2 px-2 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] rounded-lg transition-colors">
            <span class="font-mono text-[10px] text-[#B08D57] dark:text-[#D6A84F] font-bold w-5 shrink-0">03</span>
            <span class="text-slate-400 dark:text-slate-600 text-xs shrink-0">—</span>
            <span class="truncate">Cambridge Learning &amp; Global Certifications</span>
          </a>

          <!-- 04 ISC2 -->
          <a href="isc2.html" onclick="routePage(event, 'isc2.html'); toggleMobileNav();" class="flex items-center gap-2.5 py-2 px-2 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] rounded-lg transition-colors">
            <span class="font-mono text-[10px] text-[#B08D57] dark:text-[#D6A84F] font-bold w-5 shrink-0">04</span>
            <span class="text-slate-400 dark:text-slate-600 text-xs shrink-0">—</span>
            <span class="truncate">ISC2 Credentials</span>
          </a>

          <!-- 05 EC-Council -->
          <a href="ec-council.html" onclick="routePage(event, 'ec-council.html'); toggleMobileNav();" class="flex items-center gap-2.5 py-2 px-2 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] rounded-lg transition-colors">
            <span class="font-mono text-[10px] text-[#B08D57] dark:text-[#D6A84F] font-bold w-5 shrink-0">05</span>
            <span class="text-slate-400 dark:text-slate-600 text-xs shrink-0">—</span>
            <span class="truncate">EC-Council (ATC)</span>
          </a>

          <!-- 06 IT Services -->
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="flex items-center gap-2.5 py-2 px-2 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] rounded-lg transition-colors">
            <span class="font-mono text-[10px] text-[#B08D57] dark:text-[#D6A84F] font-bold w-5 shrink-0">06</span>
            <span class="text-slate-400 dark:text-slate-600 text-xs shrink-0">—</span>
            <span class="truncate">IT Services (8 Pillars)</span>
          </a>
        </div>
      </div>

      <a href="training.html"'''

assert old_pattern.search(text), "Failed to match old mobile block"
text = old_pattern.sub(new_mobile_block, text)

# Save master
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated index.html mobile block successfully.")

# Resync across all 13 pages
pages_config = [
    ('index.html', 'view-index'),
    ('about.html', 'view-about'),
    ('soc.html', 'view-soc'),
    ('enterprises.html', 'view-enterprises'),
    ('campus.html', 'view-campus'),
    ('cambridge.html', 'view-cambridge'),
    ('isc2.html', 'view-isc2'),
    ('ec-council.html', 'view-ec-council'),
    ('it-services.html', 'view-it-services'),
    ('training.html', 'view-training'),
    ('training-schedule.html', 'view-training'),
    ('contact.html', 'view-contact'),
    ('offerings.html', 'view-soc')
]

for filename, active_view in pages_config:
    file_path = os.path.join(workspace, filename)
    content = re.sub(r'class="page-view active', 'class="page-view', text)
    content = content.replace(f'id="{active_view}" class="page-view', f'id="{active_view}" class="page-view active')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Resynced {filename} (active: {active_view})")

print("Done resyncing all pages with updated mobile drawer!")
