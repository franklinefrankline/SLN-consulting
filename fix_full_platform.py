import re
import os

files = ['index.html', 'about.html', 'offerings.html', 'training.html', 'contact.html']

def build_header_and_slide1(target_file):
    is_offerings_active = (target_file == 'offerings.html')
    is_home_active = (target_file == 'index.html')
    is_about_active = (target_file == 'about.html')
    is_training_active = (target_file == 'training.html')
    is_contact_active = (target_file == 'contact.html')

    home_cls = "nav-btn text-sm font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all" if is_home_active else "nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all"
    about_cls = "nav-btn text-sm font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all" if is_about_active else "nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all"
    off_cls = "nav-btn text-sm font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all flex items-center gap-1.5 focus:outline-none" if is_offerings_active else "nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1.5 focus:outline-none"
    train_cls = "nav-btn text-sm font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all" if is_training_active else "nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all"
    contact_cls = "nav-btn text-sm font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all" if is_contact_active else "nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all"

    active_page_class = "page-view active flex-1 bg-white dark:bg-[#111315]" if is_home_active else "page-view flex-1 bg-white dark:bg-[#111315]"

    return f'''      <!-- Center: Main Navigation -->
      <nav class="hidden lg:flex items-center gap-8" aria-label="Main Navigation">
        <a href="index.html" onclick="routePage(event, 'index.html')" class="{home_cls}" data-route="index.html">Home</a>
        <a href="about.html" onclick="routePage(event, 'about.html')" class="{about_cls}" data-route="about.html">About Us</a>

        <!-- Our Offering Dropdown Menu -->
        <div class="relative group" id="offeringsMenuRoot">
          <div class="flex items-center">
            <a href="offerings.html" onclick="routePage(event, 'offerings.html'); closeOfferingsDropdown();" class="{off_cls}" data-route="offerings.html" id="offeringsNavBtn" aria-haspopup="true" aria-expanded="false">
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
        </div>

        <a href="training.html" onclick="routePage(event, 'training.html')" class="{train_cls}" data-route="training.html">Training</a>
        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="{contact_cls}" data-route="contact.html">Contact Us</a>
      </nav>

      <!-- Right Action CTA -->
      <div class="flex items-center gap-3">
        <!-- Theme Toggle Button -->
        <button onclick="toggleTheme()" class="p-2.5 rounded-xl border border-[var(--border-white)] bg-slate-50 dark:bg-[#202428] text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white transition shadow-xs focus:outline-none" aria-label="Toggle Theme">
          <i data-lucide="sun" class="w-4 h-4 hidden dark:block text-[#D6A84F]"></i>
          <i data-lucide="moon" class="w-4 h-4 block dark:hidden text-slate-700"></i>
        </button>

        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="hidden sm:inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-xs tracking-wide shadow-xs transition-all">
          <span>Enquire Now</span>
          <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
        </a>

        <button onclick="toggleMobileNav()" class="lg:hidden p-2.5 rounded-xl border border-[var(--border-white)] bg-slate-50 dark:bg-[#202428] text-slate-700 dark:text-slate-200 focus:outline-none" aria-label="Toggle navigation" id="mobileMenuBtn">
          <i data-lucide="menu" class="w-5 h-5"></i>
        </button>
      </div>

    </div>

    <!-- Mobile Drawer Navigation -->
    <div id="mobileDrawer" class="hidden lg:hidden border-t border-[var(--border-white)] bg-white dark:bg-[#1B1E21] px-6 py-5 space-y-3 isolate-scroll max-h-[calc(100vh-80px)] overflow-y-auto custom-scrollbar shadow-xl">
      <a href="index.html" onclick="routePage(event, 'index.html'); toggleMobileNav();" class="block w-full text-left text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] py-1 border-b border-[var(--border-white)]/40">Home</a>
      <a href="about.html" onclick="routePage(event, 'about.html'); toggleMobileNav();" class="block w-full text-left text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] py-1 border-b border-[var(--border-white)]/40">About Us</a>

      <!-- Mobile Our Offering with Collapsible Submenu -->
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
      </div>

      <a href="training.html" onclick="routePage(event, 'training.html'); toggleMobileNav();" class="block w-full text-left text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] py-1 border-b border-[var(--border-white)]/40">Training</a>
      <a href="contact.html" onclick="routePage(event, 'contact.html'); toggleMobileNav();" class="block w-full text-left text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] py-1 border-b border-[var(--border-white)]/40">Contact Us</a>
      <a href="contact.html" onclick="routePage(event, 'contact.html'); toggleMobileNav();" class="w-full mt-3 flex items-center justify-center gap-2 px-5 py-3 rounded-full bg-[#D6A84F] text-[#18202A] text-xs font-bold shadow-sm">
        <span>Enquire Now</span>
        <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
      </a>
    </div>
  </header>

  <!-- ==================== VIEW 1: HOME (index.html) ==================== -->
  <main id="view-index" class="{active_page_class}">
    
    <!-- Hero Carousel Banner Section -->
    <section class="relative border-b border-[var(--border-white)] bg-[#FDFDFC] dark:bg-[#15181B] overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16 lg:py-20">
        
        <div class="relative rounded-3xl overflow-hidden p-6 sm:p-10 lg:p-12 border border-[var(--border-white)] bg-white dark:bg-[#1B1E21] shadow-subtle min-h-[460px] sm:min-h-[500px]">
          
          <!-- Slide 1: Solutions for Seamless Growth -->
          <div class="hero-slide transition-opacity duration-700 ease-in-out opacity-100 flex items-center" data-index="0">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-center w-full">
              
              <div class="lg:col-span-6 space-y-5">
                <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F] block">SOLUTIONS FOR SEAMLESS GROWTH</span>
                <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold font-display text-[var(--text-white-head)] tracking-tight leading-[1.18]">
                  Enterprise Technology &amp; <br>Cybersecurity Solutions
                </h1>
                <p class="text-base sm:text-lg text-[var(--text-white-body)] leading-relaxed max-w-xl">
                  Established in 2022, SLN Consulting seamlessly integrates and optimizes systems to elevate operational efficiency and business resilience.
                </p>
                <div class="pt-2 flex items-center gap-4">
                  <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="px-7 py-3.5 rounded-xl bg-[#202428] hover:bg-[#282D32] dark:bg-[#24282C] dark:hover:bg-[#2D3237] text-white font-semibold text-xs shadow-sm transition inline-flex items-center gap-2 border border-[#3A4046]">
                    <span>Explore Offerings</span>
                    <i data-lucide="arrow-right" class="w-4 h-4 text-[#D6A84F]"></i>
                  </a>
                  <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-7 py-3.5 rounded-xl bg-white dark:bg-[#1B1E21] hover:bg-slate-50 dark:hover:bg-[#24282C] text-[var(--text-white-head)] border border-[var(--border-white)] font-semibold text-xs transition">
                    <span>Contact Us</span>
                  </a>
                </div>
              </div>

              <div class="lg:col-span-6">
                <div class="rounded-2xl overflow-hidden shadow-subtle border border-[var(--border-white)]">
                  <img 
                    src="assets/hero_offerings_office.jpg" 
                    alt="Corporate Business Consultants in Discussion" 
                    class="w-full h-80 sm:h-96 lg:h-[420px] object-cover"
                  >
                </div>
              </div>

            </div>
          </div>'''

# Execute synchronization on all files
for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace from <!-- Center: Main Navigation --> all the way to <!-- Slide 2: Workforce & Campus Development -->
    pattern_header = r'<!-- Center: Main Navigation -->[\s\S]*?(?=<!-- Slide 2: Workforce &amp; Campus Development -->|<!-- Slide 2: Workforce & Campus Development -->)'
    if re.search(pattern_header, content):
        content = re.sub(pattern_header, build_header_and_slide1(fn) + '\n\n          ', content)
        print(f"Replaced header and slide 1 in {fn}")
    else:
        print(f"Warning: pattern_header not found in {fn}")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print("Header & Slide 1 restoration completed.")
