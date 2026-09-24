# apply_remove_all_offerings.py
import os
import re

workspace = os.path.abspath(os.path.dirname(__file__))
index_path = os.path.join(workspace, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove <main id="view-offerings"> ... </main>
v_start = text.find('<main id="view-offerings"')
if v_start != -1:
    v_end = text.find('</main>', v_start)
    if v_end != -1:
        text = text[:v_start] + text[v_end + 7:]
        print("[1] Successfully removed <main id='view-offerings'> overview view.")

# 2. Remove all "<!-- Bottom Navigation: Back to All Offerings -->" blocks
bottom_nav_regex = re.compile(r'\s*<!-- Bottom Navigation: Back to All Offerings -->\s*<div class="py-8[^>]*>.*?</div>\s*</div>', re.DOTALL)
bottom_count = len(bottom_nav_regex.findall(text))
text = bottom_nav_regex.sub('', text)
print(f"[2] Successfully removed {bottom_count} 'Back to All Offerings' bottom navigation blocks.")

# 3. Clean Breadcrumbs in all detail views
breadcrumb_old_patterns = [
    (r'<a href="offerings\.html#[^"]*" onclick="backToOfferings\([^)]*\)" class="[^"]*">Our Offering</a>',
     r'<span class="text-slate-500 dark:text-slate-400">Our Offering</span>'),
    (r'<a href="offerings\.html" onclick="routePage\(event, \'offerings\.html\'\)" class="[^"]*">Our Offering</a>',
     r'<span class="text-slate-500 dark:text-slate-400">Skilling Solutions</span>'),
    (r'<a href="offerings\.html#skilling-solutions"[^>]*>Skilling Solutions</a>',
     r'<span class="text-slate-500 dark:text-slate-400">Skilling Solutions</span>')
]

for pat, rep in breadcrumb_old_patterns:
    c = len(re.findall(pat, text))
    text = re.sub(pat, rep, text)
    print(f"[3] Cleaned {c} breadcrumb links matching pattern '{pat[:40]}...'")

# 4. Update Desktop Header Dropdown and Nav Button
desktop_dropdown_old = re.search(r'<!-- Our Offering Dropdown Menu -->.*?</nav>', text, re.DOTALL)
if desktop_dropdown_old:
    desktop_dropdown_new = '''<!-- Our Offering Dropdown Menu -->
        <div class="relative group" id="offeringsMenuRoot">
          <div class="flex items-center">
            <button type="button" onclick="toggleOfferingsDropdown(event)" class="nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1.5 focus:outline-none" data-route="offerings" id="offeringsNavBtn" aria-haspopup="true" aria-expanded="false">
              <span>Our Offering</span>
              <span class="inline-flex items-center ml-0.5 text-slate-400 group-hover:text-[#18202A] dark:group-hover:text-[#D6A84F] transition-colors cursor-pointer" id="offeringsChevronWrap">
                <svg class="w-3.5 h-3.5 transition-transform duration-200 group-hover:rotate-180" id="offeringsChevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="6 9 12 15 18 9"></polyline>
                </svg>
              </span>
            </button>
          </div>

          <!-- Dropdown Panel (Solid Opaque, Direct 1-Click Access) -->
          <div id="offeringsDropdownPanel" class="hidden group-hover:block absolute top-full left-0 pt-2 w-[360px] z-50 transition-all duration-150">
            <div class="bg-white dark:bg-[#181C20] rounded-xl border border-slate-200 dark:border-[#2C3136] shadow-xl py-2 overflow-hidden">
              <!-- 01 SOC -->
              <a href="soc.html" onclick="routePage(event, 'soc.html'); closeOfferingsDropdown();" class="flex items-center gap-2.5 px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/item">
                <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] w-5 shrink-0">01</span>
                <span class="text-slate-300 dark:text-[#3A4046] text-xs shrink-0">—</span>
                <span class="text-xs font-semibold text-slate-700 dark:text-slate-200 group-hover/item:text-[#B08D57] dark:group-hover/item:text-[#D6A84F] transition-colors truncate">SOC-As-A-Service</span>
              </a>

              <!-- 02 Skilling Solutions with Nested Submenu -->
              <div class="relative group/skilling" id="skillingDropdownItem">
                <div class="flex items-center justify-between px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/item cursor-pointer" onclick="toggleDesktopSkillingSubmenu(event)">
                  <div class="flex items-center gap-2.5 flex-1 min-w-0" id="skillingNavMainLink">
                    <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] w-5 shrink-0">02</span>
                    <span class="text-slate-300 dark:text-[#3A4046] text-xs shrink-0">—</span>
                    <span class="text-xs font-semibold text-slate-700 dark:text-slate-200 group-hover/item:text-[#B08D57] dark:group-hover/item:text-[#D6A84F] transition-colors truncate">Skilling Solutions</span>
                  </div>
                  <button type="button" class="ml-2 p-1 text-slate-400 group-hover/skilling:text-[#B08D57] dark:group-hover/skilling:text-[#D6A84F] hover:text-[#18202A] transition-colors focus:outline-none" aria-label="Toggle Skilling nested submenu" id="desktopSkillingChevronWrap">
                    <svg class="w-3.5 h-3.5 transition-transform duration-200 group-hover/skilling:rotate-180" id="desktopSkillingChevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                      <polyline points="6 9 12 15 18 9"></polyline>
                    </svg>
                  </button>
                </div>

                <!-- Nested Submenu for Enterprises and Campus -->
                <div id="desktopSkillingSubmenu" class="hidden group-hover/skilling:block pl-11 pr-4 py-1.5 space-y-1 bg-slate-50/80 dark:bg-[#14171A] border-y border-slate-100 dark:border-[#252A2F]">
                  <a href="enterprises.html" id="navLinkEnterprises" onclick="routePage(event, 'enterprises.html'); closeOfferingsDropdown();" class="flex items-center gap-2 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/sub">
                    <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                    <span class="text-xs font-medium text-slate-700 dark:text-slate-200 group-hover/sub:text-[#B08D57] dark:group-hover/sub:text-[#D6A84F]">Enterprises</span>
                  </a>
                  <a href="campus.html" id="navLinkCampus" onclick="routePage(event, 'campus.html'); closeOfferingsDropdown();" class="flex items-center gap-2 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/sub">
                    <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                    <span class="text-xs font-medium text-slate-700 dark:text-slate-200 group-hover/sub:text-[#B08D57] dark:group-hover/sub:text-[#D6A84F]">Campus</span>
                  </a>
                </div>
              </div>

              <!-- 03 Cambridge -->
              <a href="cambridge.html" onclick="routePage(event, 'cambridge.html'); closeOfferingsDropdown();" class="flex items-center gap-2.5 px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/item">
                <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] w-5 shrink-0">03</span>
                <span class="text-slate-300 dark:text-[#3A4046] text-xs shrink-0">—</span>
                <span class="text-xs font-semibold text-slate-700 dark:text-slate-200 group-hover/item:text-[#B08D57] dark:group-hover/item:text-[#D6A84F] transition-colors truncate">Cambridge Learning &amp; Global Certifications</span>
              </a>

              <!-- 04 ISC2 -->
              <a href="isc2.html" onclick="routePage(event, 'isc2.html'); closeOfferingsDropdown();" class="flex items-center gap-2.5 px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/item">
                <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] w-5 shrink-0">04</span>
                <span class="text-slate-300 dark:text-[#3A4046] text-xs shrink-0">—</span>
                <span class="text-xs font-semibold text-slate-700 dark:text-slate-200 group-hover/item:text-[#B08D57] dark:group-hover/item:text-[#D6A84F] transition-colors truncate">ISC2 Credentials</span>
              </a>

              <!-- 05 EC-Council -->
              <a href="ec-council.html" onclick="routePage(event, 'ec-council.html'); closeOfferingsDropdown();" class="flex items-center gap-2.5 px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/item">
                <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] w-5 shrink-0">05</span>
                <span class="text-slate-300 dark:text-[#3A4046] text-xs shrink-0">—</span>
                <span class="text-xs font-semibold text-slate-700 dark:text-slate-200 group-hover/item:text-[#B08D57] dark:group-hover/item:text-[#D6A84F] transition-colors truncate">EC-Council (ATC)</span>
              </a>

              <!-- 06 IT Services -->
              <a href="it-services.html" onclick="routePage(event, 'it-services.html'); closeOfferingsDropdown();" class="flex items-center gap-2.5 px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/item">
                <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] w-5 shrink-0">06</span>
                <span class="text-slate-300 dark:text-[#3A4046] text-xs shrink-0">—</span>
                <span class="text-xs font-semibold text-slate-700 dark:text-slate-200 group-hover/item:text-[#B08D57] dark:group-hover/item:text-[#D6A84F] transition-colors truncate">IT Services (8 Pillars)</span>
              </a>
            </div>
          </div>
        </div>

        <a href="training.html" onclick="routePage(event, 'training.html')" class="nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all" data-route="training.html">Training</a>
        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all" data-route="contact.html">Contact Us</a>
      </nav>'''
    text = text[:desktop_dropdown_old.start()] + desktop_dropdown_new + text[desktop_dropdown_old.end():]
    print("[4] Updated desktop header dropdown.")

# 5. Update Mobile Drawer Offerings Menu
mobile_sub_start = text.find('id="mobileOfferingsSubmenu"')
if mobile_sub_start != -1:
    m_box_start = text.rfind('<div>', 0, mobile_sub_start)
    m_training_link = text.find('href="training.html"', mobile_sub_start)
    m_box_end = text.rfind('<a', 0, m_training_link)

    mobile_drawer_new = '''<div>
        <div class="flex items-center justify-between py-2 px-3 rounded-lg text-sm font-semibold text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-[#202428] cursor-pointer" onclick="toggleMobileOfferingsMenu(event)">
          <span>Our Offering</span>
          <button type="button" class="p-1 rounded-lg text-slate-400 focus:outline-none" aria-label="Toggle offerings menu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileOfferingsChevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>

        <!-- Mobile Submenu -->
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
      </div>\n\n      '''
    text = text[:m_box_start] + mobile_drawer_new + text[m_box_end:]
    print("[5] Successfully updated mobile drawer offerings menu.")
else:
    print("[5] WARNING: mobileOfferingsSubmenu not found!")

# 6. Update Footer Links
footer_c2_old = re.search(r'<!-- Column 2: Our Offering \(lg:col-span-2\) -->.*?<!-- Column 3: Quick Links', text, re.DOTALL)
if footer_c2_old:
    footer_c2_new = '''<!-- Column 2: Our Offering (lg:col-span-2) -->
        <div class="lg:col-span-2">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">OUR OFFERING</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F] mt-1.5 mb-3"></div>
          <ul class="space-y-2 text-xs">
            <li>
              <a href="soc.html" onclick="routePage(event, 'soc.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>SOC-As-A-Service</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Enterprises</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Campus</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>IT Services</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Facility Management</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
          </ul>
        </div>\n\n        <!-- Column 3: Quick Links'''
    text = text[:footer_c2_old.start()] + footer_c2_new + text[footer_c2_old.end() - len('<!-- Column 3: Quick Links'):]
    print("[6] Updated footer column 2 offerings links.")

# Update Quick Links: change offerings.html link to soc.html
text = text.replace(
    '<li><a href="offerings.html" onclick="routePage(event, \'offerings.html\')" class="text-slate-300 hover:text-[#D6A84F] transition-colors">Our Offering</a></li>',
    '<li><a href="soc.html" onclick="routePage(event, \'soc.html\')" class="text-slate-300 hover:text-[#D6A84F] transition-colors">Our Offering</a></li>'
)

# Update Learning Hub links: cambridge.html and isc2.html
text = re.sub(
    r'<a href="offerings\.html#cambridge-learning"[^>]*><span>Cambridge English</span>.*?</a>',
    r'<a href="cambridge.html" onclick="routePage(event, \'cambridge.html\')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors"><span>Cambridge English</span><i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i></a>',
    text
)
text = re.sub(
    r'<a href="offerings\.html#isc2"[^>]*><span>\(ISC\)&sup2; &amp; EC-Council</span>.*?</a>',
    r'<a href="isc2.html" onclick="routePage(event, \'isc2.html\')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors"><span>(ISC)&sup2; &amp; EC-Council</span><i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i></a>',
    text
)

# 7. Update Home view CTAs
text = text.replace(
    '<a href="offerings.html" onclick="routePage(event, \'offerings.html\')" class="px-7 py-3.5 rounded-xl bg-[#202428] hover:bg-[#282D32] dark:bg-[#24282C] dark:hover:bg-[#2D3237] text-white font-semibold text-xs shadow-sm transition inline-flex items-center gap-2 border border-[#3A4046]">\n                    <span>Explore Offerings</span>',
    '<a href="soc.html" onclick="routePage(event, \'soc.html\')" class="px-7 py-3.5 rounded-xl bg-[#202428] hover:bg-[#282D32] dark:bg-[#24282C] dark:hover:bg-[#2D3237] text-white font-semibold text-xs shadow-sm transition inline-flex items-center gap-2 border border-[#3A4046]">\n                    <span>Explore Offerings</span>'
)
text = text.replace(
    '<a href="offerings.html" onclick="routePage(event, \'offerings.html\')" class="px-7 py-3.5 rounded-xl bg-[#202428] hover:bg-[#282D32] dark:bg-[#24282C] dark:hover:bg-[#2D3237] text-white font-semibold text-xs shadow-sm transition inline-flex items-center gap-2 border border-[#3A4046]">\n                    <span>View Certifications</span>',
    '<a href="isc2.html" onclick="routePage(event, \'isc2.html\')" class="px-7 py-3.5 rounded-xl bg-[#202428] hover:bg-[#282D32] dark:bg-[#24282C] dark:hover:bg-[#2D3237] text-white font-semibold text-xs shadow-sm transition inline-flex items-center gap-2 border border-[#3A4046]">\n                    <span>View Certifications</span>'
)

# 8. Update Router Script: remove scroll restoration, remove backToOfferings, remove openOfferingDetail
router_old = re.search(r'// === SINGLE-PAGE ROUTING SYSTEM ===.*?function openPolicyModal', text, re.DOTALL)
if router_old:
    router_new = '''// === SINGLE-PAGE ROUTING SYSTEM ===
    const routeMap = {
      'index.html': 'view-index',
      'about.html': 'view-about',
      'training.html': 'view-training',
      'training-schedule.html': 'view-training',
      'training_schedule.php': 'view-training',
      'contact.html': 'view-contact',
      'soc.html': 'view-soc',
      'soc': 'view-soc',
      'soc-as-a-service': 'view-soc',
      'enterprises.html': 'view-enterprises',
      'enterprises': 'view-enterprises',
      'campus.html': 'view-campus',
      'campus': 'view-campus',
      'cambridge.html': 'view-cambridge',
      'cambridge': 'view-cambridge',
      'cambridge-learning': 'view-cambridge',
      'isc2.html': 'view-isc2',
      'isc2': 'view-isc2',
      'ec-council.html': 'view-ec-council',
      'ec-council': 'view-ec-council',
      'eccouncil': 'view-ec-council',
      'it-services.html': 'view-it-services',
      'it-services': 'view-it-services',
      'offerings.html': 'view-soc',
      'offerings': 'view-soc'
    };

    // Client-side router function
    function routePage(e, pageName, anchorId = null, pushHistory = true) {
      closeAllDrawers();
      closeOfferingsDropdown();
      if (e && e.preventDefault) {
        e.preventDefault();
      }

      // Normalize route aliases
      if (pageName === 'our-offerings' || pageName === 'offerings' || pageName === 'our-offering' || pageName === 'offering' || pageName === 'offerings.html' || pageName === 'offering.html') pageName = 'soc.html';
      if (pageName === 'about-us' || pageName === 'about') pageName = 'about.html';
      if (pageName === 'contact-us' || pageName === 'contact') pageName = 'contact.html';
      if (pageName === 'training' || pageName === 'training-schedule' || pageName === 'training_schedule' || pageName === 'training_schedule.php') pageName = 'training.html';
      if (pageName === 'enterprises' || pageName === 'enterprise') pageName = 'enterprises.html';
      if (pageName === 'campus') pageName = 'campus.html';
      if (pageName === 'soc' || pageName === 'soc-as-a-service') pageName = 'soc.html';
      if (pageName === 'cambridge' || pageName === 'cambridge-learning') pageName = 'cambridge.html';
      if (pageName === 'isc2' || pageName === 'isc2-credentials') pageName = 'isc2.html';
      if (pageName === 'ec-council' || pageName === 'eccouncil') pageName = 'ec-council.html';
      if (pageName === 'it-services' || pageName === 'it') pageName = 'it-services.html';
      if (pageName === '' || pageName === 'index' || pageName === '/') pageName = 'index.html';

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
        viewId === 'view-soc' ||
        viewId === 'view-enterprises' ||
        viewId === 'view-campus' ||
        viewId === 'view-cambridge' ||
        viewId === 'view-isc2' ||
        viewId === 'view-ec-council' ||
        viewId === 'view-it-services'
      );
      document.querySelectorAll('.nav-btn').forEach(btn => {
        const routeAttr = btn.getAttribute('data-route');
        if ((isOfferingsGroup && routeAttr === 'offerings') || (routeAttr === pageName) || (pageName === 'index.html' && routeAttr === 'index.html')) {
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

      window.scrollTo({ top: 0, behavior: "smooth" });

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
        if (path === 'our-offerings' || path === 'offerings' || path === 'our-offering' || path === 'offering' || path === 'offerings.html') path = 'soc.html';
        if (path === 'about-us' || path === 'about') path = 'about.html';
        if (path === 'contact-us' || path === 'contact') path = 'contact.html';
        if (path === 'training' || path === 'training-schedule' || path === 'training_schedule' || path === 'training-schedule.html' || path === 'training_schedule.php') path = 'training.html';
        if (path === 'enterprises' || path === 'enterprise') path = 'enterprises.html';
        if (path === 'campus') path = 'campus.html';
        if (path === 'soc' || path === 'soc-as-a-service') path = 'soc.html';
        if (path === 'cambridge' || path === 'cambridge-learning') path = 'cambridge.html';
        if (path === 'isc2' || path === 'isc2-credentials') path = 'isc2.html';
        if (path === 'ec-council' || path === 'eccouncil') path = 'ec-council.html';
        if (path === 'it-services' || path === 'it') path = 'it-services.html';
        if (path === '' || path === 'index') path = 'index.html';
        routePage(null, path, hash || null, false);
      } catch (_) {}
    });

    // Initial page load router
    window.addEventListener('DOMContentLoaded', () => {
      try {
        let path = window.location.pathname.split('/').pop() || 'index.html';
        let hash = window.location.hash.replace('#', '');
        if (path === 'our-offerings' || path === 'offerings' || path === 'our-offering' || path === 'offering' || path === 'offerings.html') path = 'soc.html';
        if (path === 'about-us' || path === 'about') path = 'about.html';
        if (path === 'contact-us' || path === 'contact') path = 'contact.html';
        if (path === 'training' || path === 'training-schedule' || path === 'training_schedule' || path === 'training-schedule.html' || path === 'training_schedule.php') path = 'training.html';
        if (path === 'enterprises' || path === 'enterprise') path = 'enterprises.html';
        if (path === 'campus') path = 'campus.html';
        if (path === 'soc' || path === 'soc-as-a-service') path = 'soc.html';
        if (path === 'cambridge' || path === 'cambridge-learning') path = 'cambridge.html';
        if (path === 'isc2' || path === 'isc2-credentials') path = 'isc2.html';
        if (path === 'ec-council' || path === 'eccouncil') path = 'ec-council.html';
        if (path === 'it-services' || path === 'it') path = 'it-services.html';
        if (path === '' || path === 'index') path = 'index.html';
        routePage(null, path, hash || null, false);
      } catch (_) {}
    });

    // Policy Modals Handlers
    function openPolicyModal'''
    text = text[:router_old.start()] + router_new + text[router_old.end() - len('function openPolicyModal'):]
    print("[8] Updated router script with clean direct routing and zero scroll-restoration / backToOfferings code.")

# Save master index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("[SUCCESS] Master index.html saved.")

# 9. Generate standalone HTML files for each page
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
    ('offerings.html', 'view-soc') # Fallback alias
]

for filename, active_view in pages_config:
    file_path = os.path.join(workspace, filename)
    file_content = re.sub(r'class="page-view active', 'class="page-view', text)
    file_content = file_content.replace(f'id="{active_view}" class="page-view', f'id="{active_view}" class="page-view active')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(file_content)
    print(f"Generated standalone page: {filename} (active: {active_view})")

print("\n=======================================================")
print("ALL OFFERINGS PAGE REMOVAL AND DIRECT NAVIGATION COMPLETE!")
print("=======================================================")
