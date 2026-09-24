import re
import os

files = ['index.html', 'about.html', 'offerings.html', 'training.html', 'contact.html']

with open('offerings.html', 'r', encoding='utf-8') as f:
    offerings_file_content = f.read()

# 1. Update Skilling detail view in offerings_file_content to include IDs for Enterprises and Campus
skilling_old_divs = '''            <div class="space-y-3 pt-1 text-xs text-[var(--text-white-body)]">
              <div class="p-3.5 rounded-xl border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]">
                <strong class="text-[var(--text-white-head)] block mb-0.5">Corporate Learning</strong>
                Workforce upskilling across Cybersecurity, Cloud, Network, AI &amp; ML, and Executive Leadership.
              </div>
              <div class="p-3.5 rounded-xl border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]">
                <strong class="text-[var(--text-white-head)] block mb-0.5">Academic Campus Programs</strong>
                SME webinars, student hackathons, corporate induction, career mapping, and faculty TTT workshops.
              </div>
            </div>'''

skilling_new_divs = '''            <div class="space-y-3 pt-1 text-xs text-[var(--text-white-body)]">
              <div id="skilling-enterprises" class="p-4 rounded-xl border border-[var(--border-white)] bg-white dark:bg-[#1B1E21] transition-all duration-300">
                <div class="flex items-center justify-between mb-1">
                  <strong class="text-[var(--text-white-head)] text-sm">Corporate Learning</strong>
                  <span class="text-[10px] font-mono uppercase tracking-wider px-2 py-0.5 rounded bg-[#B08D57]/15 dark:bg-[#D6A84F]/15 text-[#B08D57] dark:text-[#D6A84F] font-bold">Enterprises</span>
                </div>
                <p class="text-xs leading-relaxed text-[var(--text-white-body)]">
                  Workforce upskilling across Cybersecurity, Cloud, Network, AI &amp; ML, and Executive Leadership.
                </p>
              </div>
              <div id="skilling-campus" class="p-4 rounded-xl border border-[var(--border-white)] bg-white dark:bg-[#1B1E21] transition-all duration-300">
                <div class="flex items-center justify-between mb-1">
                  <strong class="text-[var(--text-white-head)] text-sm">Academic Campus Programs</strong>
                  <span class="text-[10px] font-mono uppercase tracking-wider px-2 py-0.5 rounded bg-[#B08D57]/15 dark:bg-[#D6A84F]/15 text-[#B08D57] dark:text-[#D6A84F] font-bold">Campus</span>
                </div>
                <p class="text-xs leading-relaxed text-[var(--text-white-body)]">
                  SME webinars, student hackathons, corporate induction, career mapping, and faculty TTT workshops.
                </p>
              </div>
            </div>'''

if skilling_old_divs in offerings_file_content:
    offerings_file_content = offerings_file_content.replace(skilling_old_divs, skilling_new_divs)
    print("Updated skilling section in offerings_file_content")
elif 'id="skilling-enterprises"' in offerings_file_content:
    print("Skilling section already contains skilling-enterprises")
else:
    print("Warning: skilling_old_divs not found directly in offerings.html")

# Extract all offerings views from offerings.html (Main showcase + 6 detail views)
m = re.search(r'(<!-- ==================== VIEW 3: MAIN OUR OFFERING SHOWCASE[\s\S]*?)(?=<!-- ==================== VIEW 4: TRAINING)', offerings_file_content)
if not m:
    m = re.search(r'(<!-- ==================== VIEW 3:[\s\S]*?)(?=<!-- ==================== VIEW 4: TRAINING)', offerings_file_content)

offerings_views_chunk = m.group(1).strip()
print(f"Extracted offerings views chunk, length: {len(offerings_views_chunk)}")

font_link_new = '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">'
tailwind_font_new = '''fontFamily: {
            display: ['"Outfit"', 'sans-serif'],
            serif: ['"Playfair Display"', 'Georgia', 'serif'],
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
          }'''

def get_desktop_nav(target_file):
    is_active = (target_file == 'offerings.html')
    active_cls = "nav-btn text-sm font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all flex items-center gap-1.5 focus:outline-none"
    inactive_cls = "nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1.5 focus:outline-none"
    cls = active_cls if is_active else inactive_cls

    return f'''<!-- Our Offering Dropdown Menu -->
        <div class="relative group" id="offeringsMenuRoot">
          <div class="flex items-center">
            <a href="offerings.html" onclick="routePage(event, 'offerings.html'); closeOfferingsDropdown();" class="{cls}" data-route="offerings.html" id="offeringsNavBtn" aria-haspopup="true" aria-expanded="false">
              <span>Our Offering</span>
              <span class="inline-flex items-center ml-0.5 text-slate-400 group-hover:text-[#18202A] dark:group-hover:text-[#D6A84F] transition-colors cursor-pointer" onclick="toggleOfferingsDropdown(event)" aria-label="Toggle Our Offering dropdown" id="offeringsChevronWrap">
                <svg class="w-3.5 h-3.5 transition-transform duration-200 group-hover:rotate-180" id="offeringsChevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="6 9 12 15 18 9"></polyline>
                </svg>
              </span>
            </a>
          </div>

          <!-- Dropdown Panel (Compact, Clean, Professional, Solid Opaque) -->
          <div id="offeringsDropdownPanel" class="hidden group-hover:block absolute top-full left-0 pt-2 w-[360px] z-50 transition-all duration-150">
            <div class="bg-white dark:bg-[#181C20] rounded-xl border border-slate-200 dark:border-[#2C3136] shadow-xl py-2 overflow-hidden">
              <!-- 01 SOC -->
              <a href="offerings.html#soc-as-a-service" onclick="routePage(event, 'offerings.html', 'soc-as-a-service'); closeOfferingsDropdown();" class="flex items-center gap-2.5 px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/item">
                <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] w-5 shrink-0">01</span>
                <span class="text-slate-300 dark:text-[#3A4046] text-xs shrink-0">—</span>
                <span class="text-xs font-semibold text-slate-700 dark:text-slate-200 group-hover/item:text-[#B08D57] dark:group-hover/item:text-[#D6A84F] transition-colors truncate">SOC-As-A-Service</span>
              </a>

              <!-- 02 Skilling Solutions with Nested Submenu -->
              <div class="relative group/skilling" id="skillingDropdownItem">
                <div class="flex items-center justify-between px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/item cursor-pointer">
                  <a href="offerings.html#skilling-solutions" onclick="routePage(event, 'offerings.html', 'skilling-solutions'); closeOfferingsDropdown();" class="flex items-center gap-2.5 flex-1 min-w-0" id="skillingNavMainLink">
                    <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] w-5 shrink-0">02</span>
                    <span class="text-slate-300 dark:text-[#3A4046] text-xs shrink-0">—</span>
                    <span class="text-xs font-semibold text-slate-700 dark:text-slate-200 group-hover/item:text-[#B08D57] dark:group-hover/item:text-[#D6A84F] transition-colors truncate">Skilling Solutions</span>
                  </a>
                  <button type="button" onclick="toggleDesktopSkillingSubmenu(event)" class="ml-2 p-1 text-slate-400 group-hover/skilling:text-[#B08D57] dark:group-hover/skilling:text-[#D6A84F] hover:text-[#18202A] transition-colors focus:outline-none" aria-label="Toggle Skilling nested submenu" id="desktopSkillingChevronWrap">
                    <svg class="w-3.5 h-3.5 transition-transform duration-200 group-hover/skilling:rotate-180" id="desktopSkillingChevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                      <polyline points="6 9 12 15 18 9"></polyline>
                    </svg>
                  </button>
                </div>

                <!-- Nested Submenu for Enterprises and Campus -->
                <div id="desktopSkillingSubmenu" class="hidden group-hover/skilling:block pl-11 pr-4 py-1.5 space-y-1 bg-slate-50/80 dark:bg-[#14171A] border-y border-slate-100 dark:border-[#252A2F]">
                  <a href="offerings.html#skilling-enterprises" onclick="routePage(event, 'offerings.html', 'skilling-enterprises'); closeOfferingsDropdown();" class="flex items-center gap-2 py-1 px-2 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:text-[#B08D57] dark:hover:text-[#D6A84F] hover:bg-white dark:hover:bg-[#1E2226] rounded-md transition-colors" id="navLinkEnterprises">
                    <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                    <span>Enterprises</span>
                  </a>
                  <a href="offerings.html#skilling-campus" onclick="routePage(event, 'offerings.html', 'skilling-campus'); closeOfferingsDropdown();" class="flex items-center gap-2 py-1 px-2 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:text-[#B08D57] dark:hover:text-[#D6A84F] hover:bg-white dark:hover:bg-[#1E2226] rounded-md transition-colors" id="navLinkCampus">
                    <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                    <span>Campus</span>
                  </a>
                </div>
              </div>

              <!-- 03 Cambridge -->
              <a href="offerings.html#cambridge-learning" onclick="routePage(event, 'offerings.html', 'cambridge-learning'); closeOfferingsDropdown();" class="flex items-center gap-2.5 px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/item">
                <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] w-5 shrink-0">03</span>
                <span class="text-slate-300 dark:text-[#3A4046] text-xs shrink-0">—</span>
                <span class="text-xs font-semibold text-slate-700 dark:text-slate-200 group-hover/item:text-[#B08D57] dark:group-hover/item:text-[#D6A84F] transition-colors truncate">Cambridge Learning &amp; Global Certifications</span>
              </a>

              <!-- 04 ISC2 -->
              <a href="offerings.html#isc2" onclick="routePage(event, 'offerings.html', 'isc2'); closeOfferingsDropdown();" class="flex items-center gap-2.5 px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/item">
                <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] w-5 shrink-0">04</span>
                <span class="text-slate-300 dark:text-[#3A4046] text-xs shrink-0">—</span>
                <span class="text-xs font-semibold text-slate-700 dark:text-slate-200 group-hover/item:text-[#B08D57] dark:group-hover/item:text-[#D6A84F] transition-colors truncate">ISC2 Credentials</span>
              </a>

              <!-- 05 EC-Council -->
              <a href="offerings.html#ec-council" onclick="routePage(event, 'offerings.html', 'ec-council'); closeOfferingsDropdown();" class="flex items-center gap-2.5 px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/item">
                <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] w-5 shrink-0">05</span>
                <span class="text-slate-300 dark:text-[#3A4046] text-xs shrink-0">—</span>
                <span class="text-xs font-semibold text-slate-700 dark:text-slate-200 group-hover/item:text-[#B08D57] dark:group-hover/item:text-[#D6A84F] transition-colors truncate">EC-Council (ATC)</span>
              </a>

              <!-- 06 IT Services -->
              <a href="offerings.html#it-services" onclick="routePage(event, 'offerings.html', 'it-services'); closeOfferingsDropdown();" class="flex items-center gap-2.5 px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/item">
                <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] w-5 shrink-0">06</span>
                <span class="text-slate-300 dark:text-[#3A4046] text-xs shrink-0">—</span>
                <span class="text-xs font-semibold text-slate-700 dark:text-slate-200 group-hover/item:text-[#B08D57] dark:group-hover/item:text-[#D6A84F] transition-colors truncate">IT Services (8 Pillars)</span>
              </a>
            </div>
          </div>
        </div>'''

mobile_direct_nav = '''<!-- Mobile Our Offering with Collapsible Submenu -->
      <div class="border-b border-[var(--border-white)]/40 pb-1">
        <div class="flex items-center justify-between py-1.5">
          <a href="offerings.html" onclick="routePage(event, 'offerings.html'); toggleMobileNav();" class="text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">Our Offering</a>
          <button type="button" onclick="toggleMobileOfferingsMenu(event)" class="p-1.5 rounded-lg text-slate-500 hover:text-[var(--text-white-head)] hover:bg-slate-100 dark:hover:bg-[#24282C] focus:outline-none" aria-label="Toggle Our Offering submenu" id="mobileOfferingsToggleBtn">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileOfferingsChevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileOfferingsSubmenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-slate-50 dark:bg-[#15181B] rounded-xl border border-[var(--border-white)] my-1">
          <!-- 01 SOC -->
          <a href="offerings.html#soc-as-a-service" onclick="routePage(event, 'offerings.html', 'soc-as-a-service'); toggleMobileNav();" class="flex items-center gap-2.5 py-2 px-2 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] rounded-lg transition-colors">
            <span class="font-mono text-[10px] text-[#B08D57] dark:text-[#D6A84F] font-bold w-5 shrink-0">01</span>
            <span class="text-slate-400 dark:text-slate-600 text-xs shrink-0">—</span>
            <span class="truncate">SOC-As-A-Service</span>
          </a>

          <!-- 02 Skilling Solutions with nested expansion -->
          <div>
            <div class="flex items-center justify-between py-1 px-2 rounded-lg hover:bg-slate-100 dark:hover:bg-[#202428]">
              <a href="offerings.html#skilling-solutions" onclick="routePage(event, 'offerings.html', 'skilling-solutions'); toggleMobileNav();" class="flex items-center gap-2.5 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors truncate flex-1 min-w-0">
                <span class="font-mono text-[10px] text-[#B08D57] dark:text-[#D6A84F] font-bold w-5 shrink-0">02</span>
                <span class="text-slate-400 dark:text-slate-600 text-xs shrink-0">—</span>
                <span class="truncate">Skilling Solutions</span>
              </a>
              <button type="button" onclick="toggleMobileSkillingSubmenu(event)" class="p-1 rounded text-slate-400 hover:text-[#B08D57] dark:hover:text-[#D6A84F] focus:outline-none" aria-label="Toggle Skilling nested submenu" id="mobileSkillingToggleBtn">
                <svg class="w-3.5 h-3.5 transition-transform duration-200" id="mobileSkillingChevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="6 9 12 15 18 9"></polyline>
                </svg>
              </button>
            </div>

            <!-- Nested Enterprises & Campus -->
            <div id="mobileSkillingSubmenu" class="hidden pl-8 pr-2 py-1 space-y-1 bg-white dark:bg-[#1B1E21] rounded-lg border border-[var(--border-white)] my-1">
              <a href="offerings.html#skilling-enterprises" onclick="routePage(event, 'offerings.html', 'skilling-enterprises'); toggleMobileNav();" class="flex items-center gap-2 py-1.5 px-2 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:text-[#B08D57] dark:hover:text-[#D6A84F] rounded-md transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Enterprises</span>
              </a>
              <a href="offerings.html#skilling-campus" onclick="routePage(event, 'offerings.html', 'skilling-campus'); toggleMobileNav();" class="flex items-center gap-2 py-1.5 px-2 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:text-[#B08D57] dark:hover:text-[#D6A84F] rounded-md transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Campus</span>
              </a>
            </div>
          </div>

          <!-- 03 Cambridge -->
          <a href="offerings.html#cambridge-learning" onclick="routePage(event, 'offerings.html', 'cambridge-learning'); toggleMobileNav();" class="flex items-center gap-2.5 py-2 px-2 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] rounded-lg transition-colors">
            <span class="font-mono text-[10px] text-[#B08D57] dark:text-[#D6A84F] font-bold w-5 shrink-0">03</span>
            <span class="text-slate-400 dark:text-slate-600 text-xs shrink-0">—</span>
            <span class="truncate">Cambridge Learning &amp; Global Certifications</span>
          </a>

          <!-- 04 ISC2 -->
          <a href="offerings.html#isc2" onclick="routePage(event, 'offerings.html', 'isc2'); toggleMobileNav();" class="flex items-center gap-2.5 py-2 px-2 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] rounded-lg transition-colors">
            <span class="font-mono text-[10px] text-[#B08D57] dark:text-[#D6A84F] font-bold w-5 shrink-0">04</span>
            <span class="text-slate-400 dark:text-slate-600 text-xs shrink-0">—</span>
            <span class="truncate">ISC2 Credentials</span>
          </a>

          <!-- 05 EC-Council -->
          <a href="offerings.html#ec-council" onclick="routePage(event, 'offerings.html', 'ec-council'); toggleMobileNav();" class="flex items-center gap-2.5 py-2 px-2 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] rounded-lg transition-colors">
            <span class="font-mono text-[10px] text-[#B08D57] dark:text-[#D6A84F] font-bold w-5 shrink-0">05</span>
            <span class="text-slate-400 dark:text-slate-600 text-xs shrink-0">—</span>
            <span class="truncate">EC-Council (ATC)</span>
          </a>

          <!-- 06 IT Services -->
          <a href="offerings.html#it-services" onclick="routePage(event, 'offerings.html', 'it-services'); toggleMobileNav();" class="flex items-center gap-2.5 py-2 px-2 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] rounded-lg transition-colors">
            <span class="font-mono text-[10px] text-[#B08D57] dark:text-[#D6A84F] font-bold w-5 shrink-0">06</span>
            <span class="text-slate-400 dark:text-slate-600 text-xs shrink-0">—</span>
            <span class="truncate">IT Services (8 Pillars)</span>
          </a>
        </div>
      </div>'''

clean_router_script = '''    // Map detail anchors to offering card IDs on the main showcase
    const cardIdByAnchor = {
      'soc-as-a-service': 'card-soc',
      'soc': 'card-soc',
      'skilling-solutions': 'card-skilling',
      'skilling': 'card-skilling',
      'skilling-enterprises': 'card-skilling',
      'skilling-enterprise': 'card-skilling',
      'skilling-campus': 'card-skilling',
      'cambridge-learning': 'card-cambridge',
      'cambridge': 'card-cambridge',
      'isc2': 'card-isc2',
      'isc2-credentials': 'card-isc2',
      'ec-council': 'card-ec-council',
      'eccouncil': 'card-ec-council',
      'it-services': 'card-it-services'
    };

    function toggleOfferingsDropdown(e) {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      const panel = document.getElementById('offeringsDropdownPanel');
      const chev = document.getElementById('offeringsChevron');
      if (!panel) return;
      const isOpen = panel.classList.contains('is-open');
      if (isOpen) {
        closeOfferingsDropdown();
      } else {
        panel.classList.remove('hidden');
        panel.classList.add('is-open');
        if (chev) chev.classList.add('rotate-180');
      }
    }

    function toggleDesktopSkillingSubmenu(e) {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      const sub = document.getElementById('desktopSkillingSubmenu');
      const chev = document.getElementById('desktopSkillingChevron');
      if (!sub) return;
      const isOpen = sub.classList.contains('is-open');
      if (isOpen) {
        sub.classList.remove('is-open');
        sub.classList.add('hidden');
        if (chev) chev.classList.remove('rotate-180');
      } else {
        sub.classList.add('is-open');
        sub.classList.remove('hidden');
        if (chev) chev.classList.add('rotate-180');
      }
    }

    function closeOfferingsDropdown() {
      const panel = document.getElementById('offeringsDropdownPanel');
      const chev = document.getElementById('offeringsChevron');
      if (panel) {
        panel.classList.remove('is-open');
        const root = document.getElementById('offeringsMenuRoot');
        const isHovered = (root && root.matches(':hover')) || panel.matches(':hover');
        if (!isHovered) {
          panel.classList.add('hidden');
        }
      }
      if (chev) chev.classList.remove('rotate-180');
      const deskSkilling = document.getElementById('desktopSkillingSubmenu');
      if (deskSkilling) {
        deskSkilling.classList.remove('is-open');
      }
    }

    function toggleMobileOfferingsMenu(e) {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      const sub = document.getElementById('mobileOfferingsSubmenu');
      const chev = document.getElementById('mobileOfferingsChevron');
      if (!sub) return;
      const isHidden = sub.classList.contains('hidden');
      if (isHidden) {
        sub.classList.remove('hidden');
        if (chev) chev.classList.add('rotate-180');
      } else {
        sub.classList.add('hidden');
        if (chev) chev.classList.remove('rotate-180');
      }
    }

    function toggleMobileSkillingSubmenu(e) {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      const sub = document.getElementById('mobileSkillingSubmenu');
      const chev = document.getElementById('mobileSkillingChevron');
      if (!sub) return;
      const isHidden = sub.classList.contains('hidden');
      if (isHidden) {
        sub.classList.remove('hidden');
        if (chev) chev.classList.add('rotate-180');
      } else {
        sub.classList.add('hidden');
        if (chev) chev.classList.remove('rotate-180');
      }
    }

    // Close desktop dropdown on outside click
    document.addEventListener('click', (e) => {
      const root = document.getElementById('offeringsMenuRoot');
      if (root && !root.contains(e.target)) {
        closeOfferingsDropdown();
      }
    });

    function openOfferingDetail(e, pageName, detailAnchor, cardId) {
      if (e && e.preventDefault) e.preventDefault();
      
      const curY = window.scrollY || window.pageYOffset || 0;
      window.lastOfferingsScrollY = curY;
      window.lastOfferingCardId = cardId || cardIdByAnchor[detailAnchor] || null;
      try {
        sessionStorage.setItem('sln_offerings_scroll', curY.toString());
        if (window.lastOfferingCardId) {
          sessionStorage.setItem('sln_last_offering', window.lastOfferingCardId);
        }
      } catch (_) {}

      routePage(e, pageName, detailAnchor);
    }

    function backToOfferings(e, fallbackCardId = null) {
      if (e && e.preventDefault) e.preventDefault();

      let targetCardId = fallbackCardId || window.lastOfferingCardId;
      if (!targetCardId) {
        try {
          targetCardId = sessionStorage.getItem('sln_last_offering');
        } catch (_) {}
      }

      let savedScroll = window.lastOfferingsScrollY;
      if (typeof savedScroll !== 'number') {
        try {
          const s = sessionStorage.getItem('sln_offerings_scroll');
          if (s) savedScroll = parseInt(s, 10);
        } catch (_) {}
      }

      closeAllDrawers();
      closeOfferingsDropdown();

      // Switch view to view-offerings
      document.querySelectorAll('.page-view').forEach(p => p.classList.remove('active'));
      const targetView = document.getElementById('view-offerings');
      if (targetView) {
        targetView.classList.add('active');
      }

      // Update Navigation Active State
      document.querySelectorAll('.nav-btn').forEach(btn => {
        const routeAttr = btn.getAttribute('data-route');
        if (routeAttr === 'offerings.html') {
          btn.className = 'nav-btn text-sm font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all flex items-center gap-1.5 focus:outline-none';
        } else {
          btn.className = 'nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1.5 focus:outline-none';
        }
      });

      // Update Browser History URL
      try {
        window.history.pushState({ page: 'offerings.html', anchor: null }, '', 'offerings.html');
      } catch (_) {}

      // Smoothly restore scroll position directly to the offering card
      setTimeout(() => {
        let restored = false;
        if (targetCardId) {
          const cardEl = document.getElementById(targetCardId);
          if (cardEl) {
            const yOffset = -90; // account for fixed header navbar
            const y = cardEl.getBoundingClientRect().top + window.pageYOffset + yOffset;
            window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' });
            restored = true;
          }
        }
        if (!restored && typeof savedScroll === 'number' && savedScroll > 50) {
          window.scrollTo({ top: savedScroll, behavior: 'smooth' });
        } else if (!restored) {
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      }, 50);

      if (window.lucide) {
        lucide.createIcons();
      }
    }

    // Comprehensive Route Mapping supporting files, clean URLs, and direct service anchors
    const routeMap = {
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
      'skilling-enterprises': 'view-skilling',
      'skilling-enterprise': 'view-skilling',
      'skilling-campus': 'view-skilling',
      'cambridge-learning': 'view-cambridge',
      'cambridge': 'view-cambridge',
      'isc2': 'view-isc2',
      'isc2-credentials': 'view-isc2',
      'ec-council': 'view-ec-council',
      'eccouncil': 'view-ec-council',
      'it-services': 'view-it-services'
    };

    // Client-side router function
    function routePage(e, pageName, anchorId = null, pushHistory = true) {
      closeAllDrawers();
      closeOfferingsDropdown();
      if (e && e.preventDefault) {
        e.preventDefault();
      }

      // Normalize route aliases
      if (pageName === 'our-offerings' || pageName === 'offerings' || pageName === 'our-offering' || pageName === 'offering' || pageName === 'offering.html') pageName = 'offerings.html';
      if (pageName === 'about-us' || pageName === 'about') pageName = 'about.html';
      if (pageName === 'contact-us' || pageName === 'contact') pageName = 'contact.html';
      if (pageName === 'training') pageName = 'training.html';
      if (pageName === '' || pageName === 'index' || pageName === '/') pageName = 'index.html';

      // Auto-save scroll position when leaving view-offerings for a detail view
      const currentOfferingsView = document.getElementById('view-offerings');
      if (currentOfferingsView && currentOfferingsView.classList.contains('active') && anchorId && cardIdByAnchor[anchorId]) {
        const curY = window.scrollY || window.pageYOffset || 0;
        window.lastOfferingsScrollY = curY;
        window.lastOfferingCardId = cardIdByAnchor[anchorId];
        try {
          sessionStorage.setItem('sln_offerings_scroll', curY.toString());
          sessionStorage.setItem('sln_last_offering', window.lastOfferingCardId);
        } catch (_) {}
      }

      // If anchorId maps to a detail view
      let viewId = 'view-index';
      if (anchorId && routeMap[anchorId]) {
        viewId = routeMap[anchorId];
      } else if (routeMap[pageName]) {
        viewId = routeMap[pageName];
      }

      // Switch active view
      document.querySelectorAll('.page-view').forEach(p => p.classList.remove('active'));
      const targetView = document.getElementById(viewId);
      if (targetView) {
        targetView.classList.add('active');
      }

      // Update Navigation Active State
      const isOfferingsGroup = (
        viewId === 'view-offerings' ||
        viewId === 'view-soc' ||
        viewId === 'view-skilling' ||
        viewId === 'view-cambridge' ||
        viewId === 'view-isc2' ||
        viewId === 'view-ec-council' ||
        viewId === 'view-it-services'
      );
      const activeRoute = isOfferingsGroup ? 'offerings.html' : pageName;
      document.querySelectorAll('.nav-btn').forEach(btn => {
        const routeAttr = btn.getAttribute('data-route');
        if (routeAttr === activeRoute || (activeRoute === 'index.html' && routeAttr === 'index.html')) {
          btn.className = 'nav-btn text-sm font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all flex items-center gap-1.5 focus:outline-none';
        } else {
          btn.className = 'nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1.5 focus:outline-none';
        }
      });

      // Update Browser History URL safely if pushHistory is requested
      if (pushHistory) {
        try {
          const newUrl = anchorId ? `${pageName}#${anchorId}` : pageName;
          window.history.pushState({ page: pageName, anchor: anchorId }, '', newUrl);
        } catch (err) {
          try {
            if (anchorId) window.location.hash = anchorId;
          } catch (_) {}
        }
      }

      // Handle targeted section scrolling for Enterprises and Campus
      if (anchorId === 'skilling-enterprises' || anchorId === 'skilling-enterprise' || anchorId === 'skilling-campus') {
        const targetSectionId = (anchorId === 'skilling-campus') ? 'skilling-campus' : 'skilling-enterprises';
        setTimeout(() => {
          const el = document.getElementById(targetSectionId);
          if (el) {
            const yOffset = -120;
            const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset;
            window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' });
            el.classList.add('ring-2', 'ring-[#B08D57]', 'dark:ring-[#D6A84F]');
            setTimeout(() => {
              el.classList.remove('ring-2', 'ring-[#B08D57]', 'dark:ring-[#D6A84F]');
            }, 2000);
          }
        }, 80);
      } else {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }

      if (window.lucide) {
        lucide.createIcons();
      }
    }

    // Handle Browser Back / Forward buttons
    window.addEventListener('popstate', (e) => {
      try {
        if (e.state && e.state.page) {
          routePage(null, e.state.page, e.state.anchor || null, false);
          return;
        }
        let path = window.location.pathname.split('/').pop() || 'index.html';
        let hash = window.location.hash.replace('#', '');
        if (path === 'our-offerings' || path === 'offerings' || path === 'our-offering' || path === 'offering') path = 'offerings.html';
        if (path === 'about-us' || path === 'about') path = 'about.html';
        if (path === 'contact-us' || path === 'contact') path = 'contact.html';
        if (path === 'training') path = 'training.html';
        if (path === '' || path === 'index') path = 'index.html';
        if (path === 'offerings.html' && (!hash || hash === '')) {
          backToOfferings(null);
          return;
        }
        routePage(null, path, hash || null, false);
      } catch (_) {}
    });

    // Initial page load router
    window.addEventListener('DOMContentLoaded', () => {
      try {
        let path = window.location.pathname.split('/').pop() || 'index.html';
        let hash = window.location.hash.replace('#', '');
        if (path === 'our-offerings' || path === 'offerings' || path === 'our-offering' || path === 'offering') path = 'offerings.html';
        if (path === 'about-us' || path === 'about') path = 'about.html';
        if (path === 'contact-us' || path === 'contact') path = 'contact.html';
        if (path === 'training') path = 'training.html';
        if (path === '' || path === 'index') path = 'index.html';

        try {
          window.history.replaceState({ page: path, anchor: hash || null }, '', window.location.href);
        } catch (_) {}

        routePage(null, path, hash || null, false);
      } catch (_) {
        routePage(null, 'index.html', null, false);
      }
    });

    function closeAllDrawers() {
      const b = document.getElementById('capabilityDrawerBackdrop');
      const d = document.getElementById('capabilityDrawer');
      if (b) b.classList.add('hidden');
      if (d) d.classList.add('translate-x-full');
      document.body.style.overflow = '';
      closeOfferingsDropdown();
    }'''

# Image Replacements (Map external unsplash images to local existing assets)
img_replacements = [
    ('https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=80', 'assets/training_desk.jpg'),
    ('https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=1200&q=80', 'assets/training_classroom.jpg'),
    ('https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1200&q=80', 'assets/soc_operations_center.jpg'),
    ('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80', 'assets/hero_offerings_office.jpg'),
    ('https://images.unsplash.com/photo-1524178232363-1fb2b075b655?auto=format&fit=crop&w=1200&q=80', 'assets/training_classroom.jpg'),
    ('https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=1200&q=80', 'assets/training_desk.jpg'),
    ('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=900&q=80', 'assets/hero_offerings_office.jpg'),
]

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update font link
    content = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?family=Outfit:wght@500;600;700;800[\s\S]*?rel="stylesheet">', font_link_new, content)

    # 2. Update tailwind fontFamily
    content = re.sub(r'fontFamily:\s*\{\s*display:\s*\[[\s\S]*?\}\s*\}', tailwind_font_new + '\n        }', content)

    # 3. Update desktop header nav for Our Offering Dropdown with nested Skilling
    content = re.sub(r'<!-- Our Offerings? Dropdown Menu? -->\s*<div class="relative group" id="offeringsMenuRoot">[\s\S]*?</div>\s*</div>\s*</div>\s*</div>', get_desktop_nav(fn), content)
    content = re.sub(r'<!-- Our Offerings? Dropdown Menu? -->\s*<div class="relative group" id="offeringsMenuRoot">[\s\S]*?</div>\s*</div>\s*</div>', get_desktop_nav(fn), content)
    content = re.sub(r'<a href="offerings\.html"[^>]*class="[^"]*"[^>]*data-route="offerings\.html">Our Offerings?</a>', get_desktop_nav(fn), content)

    # 4. Update mobile drawer nav with nested Skilling Solutions
    content = re.sub(r'<!-- Mobile Our Offering with Collapsible Submenu -->[\s\S]*?</div>\s*</div>\s*(?=<a href="training\.html")', mobile_direct_nav + '\n\n      ', content)

    # 5. Sync the offerings views into this file
    if fn != 'offerings.html':
        pattern_existing = r'<!-- ==================== VIEW 3:[\s\S]*?(?=<!-- ==================== VIEW 4: TRAINING)'
        if re.search(pattern_existing, content):
            content = re.sub(pattern_existing, offerings_views_chunk + '\n\n  ', content)
            print(f"Synced offerings views into {fn}")
        else:
            print(f"Warning: could not find offerings views block in {fn}")
    else:
        # Also ensure offerings.html itself has the skilling section updated
        if skilling_old_divs in content:
            content = content.replace(skilling_old_divs, skilling_new_divs)

    # 6. Replace all external unsplash images with local assets
    for old_src, new_src in img_replacements:
        content = content.replace(old_src, new_src)

    # 7. Update router block
    pattern_router = r'// Map detail anchors to offering card IDs[\s\S]*?(?=// Mobile nav toggle)'
    if not re.search(pattern_router, content):
        pattern_router = r'// Comprehensive Route Mapping supporting files[\s\S]*?(?=// Mobile nav toggle)'
    if not re.search(pattern_router, content):
        pattern_router = r'// Map URL / filename to view ID[\s\S]*?(?=// Mobile nav toggle)'
    if re.search(pattern_router, content):
        content = re.sub(pattern_router, clean_router_script.strip() + '\n\n    ', content)
        print(f"Updated router script in {fn}")
    else:
        print(f"Warning: could not find router block in {fn}")

    # 8. Ensure active views are correct per file in static HTML
    expected_active = {
        'index.html': 'view-index',
        'about.html': 'view-about',
        'offerings.html': 'view-offerings',
        'training.html': 'view-training',
        'contact.html': 'view-contact'
    }[fn]
    all_views = ['view-index', 'view-about', 'view-offerings', 'view-soc', 'view-skilling', 'view-cambridge', 'view-isc2', 'view-ec-council', 'view-it-services', 'view-training', 'view-contact']
    for vid in all_views:
        content = re.sub(rf'<main id="{vid}" class="page-view\s+active\s+flex-1', f'<main id="{vid}" class="page-view flex-1', content)
    content = re.sub(rf'<main id="{expected_active}" class="page-view flex-1', f'<main id="{expected_active}" class="page-view active flex-1', content)

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully processed {fn}")

print("Platform sync completed successfully!")
