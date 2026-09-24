import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 1. NEW HEADER HTML
# ==============================================================================
NEW_HEADER_HTML = '''  <!-- ==================== TWO-LEVEL EXACT REFERENCE HEADER ==================== -->
  <header class="sticky top-0 z-40 bg-white dark:bg-[#1B1E21] border-b border-slate-200 dark:border-[#2D3339] shadow-sm transition-colors duration-200">
    
    <!-- ROW 1 — TOP INFORMATION BAR (Dark Charcoal Bar) -->
    <div class="bg-[#181B1E] dark:bg-[#121417] border-b border-[#2C3136] dark:border-[#22262B] text-slate-300 transition-colors duration-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2 flex items-center justify-between gap-4 text-xs">
        
        <!-- Left: SLN CONSULTING | SOLUTIONS FOR SEAMLESS GROWTH | Location -->
        <div class="flex items-center gap-3 overflow-hidden whitespace-nowrap">
          <span class="font-display font-bold text-white tracking-tight uppercase text-xs">SLN CONSULTING</span>
          <span class="text-slate-600">|</span>
          <span class="font-mono text-[11px] text-slate-300 uppercase tracking-wider font-medium truncate">SOLUTIONS FOR SEAMLESS GROWTH</span>
          <span class="text-slate-600 hidden md:inline">|</span>
          <!-- Location -->
          <div class="hidden md:flex items-center gap-1.5 text-slate-300">
            <i data-lucide="map-pin" class="w-3.5 h-3.5 text-[#D6A84F] shrink-0"></i>
            <span class="truncate">Chennai - 600042, Tamil Nadu, India</span>
          </div>
        </div>

        <!-- Right: Phone | Email | Theme Toggle -->
        <div class="flex items-center gap-3.5 shrink-0">
          <a href="tel:+919940196195" class="flex items-center gap-1.5 text-xs text-slate-200 hover:text-white transition font-medium">
            <i data-lucide="phone" class="w-3.5 h-3.5 text-[#D6A84F] shrink-0"></i>
            <span>+91 9940196195</span>
          </a>
          <span class="text-slate-600 hidden sm:inline">|</span>
          <a href="mailto:srinivas.c@slnconsulting.co.in" class="hidden sm:flex items-center gap-1.5 text-xs text-slate-200 hover:text-white transition font-medium">
            <i data-lucide="mail" class="w-3.5 h-3.5 text-[#D6A84F] shrink-0"></i>
            <span class="truncate">srinivas.c@slnconsulting.co.in</span>
          </a>
          <span class="text-slate-600 hidden sm:inline">|</span>
          
          <!-- Pill Theme Toggle Switch -->
          <button onclick="toggleTheme()" id="headerThemeToggle" class="relative inline-flex h-6 w-11 shrink-0 items-center cursor-pointer rounded-full border border-slate-600 bg-slate-700/80 transition-colors duration-200 ease-in-out focus:outline-none" aria-label="Toggle Light and Dark Mode" title="Toggle Light/Dark Theme">
            <span class="inline-flex h-4 w-4 transform items-center justify-center rounded-full bg-white text-[#18202A] shadow transition duration-200 ease-in-out translate-x-1 dark:translate-x-6 dark:bg-[#D6A84F] dark:text-[#111315]">
              <i data-lucide="moon" class="w-2.5 h-2.5 block dark:hidden"></i>
              <i data-lucide="sun" class="w-2.5 h-2.5 hidden dark:block"></i>
            </span>
          </button>
        </div>

      </div>
    </div>

    <!-- ROW 2 — MAIN NAVIGATION -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center justify-between gap-4">
      
      <!-- Left: Official SLN Brand Logo -->
      <a href="index.html" onclick="routePage(event, 'index.html')" class="flex items-center shrink-0 group focus:outline-none py-0.5" aria-label="SLN Consulting Home">
        <div class="transition-transform group-hover:scale-[1.02] dark:bg-white dark:p-1.5 dark:rounded-lg dark:border dark:border-slate-700/60 dark:shadow-sm">
          <img src="assets/images/sln-consulting-logo.png" alt="SLN Consulting - Solutions for Seamless Growth" class="h-8 sm:h-9 md:h-10 w-auto object-contain block" style="max-height: 40px; width: auto;" />
        </div>
      </a>

      <!-- Center: Main Navigation Structure (10 Items) -->
      <nav class="hidden lg:flex items-center gap-3.5 xl:gap-5 text-xs xl:text-sm" aria-label="Main Navigation">
        
        <!-- 1. Home -->
        <a href="index.html" onclick="routePage(event, 'index.html')" class="nav-btn font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all whitespace-nowrap" data-route="index.html">Home</a>

        <!-- 2. About Us ▾ -->
        <div class="relative group/nav">
          <button type="button" class="nav-btn font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap" data-route="about.html">
            <span>About Us</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#18202A] dark:group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- About Us Dropdown Panel -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[240px] z-50 transition-all duration-150">
            <div class="bg-white dark:bg-[#181C20] rounded-xl border border-slate-200 dark:border-[#2C3136] shadow-xl py-2 overflow-hidden text-xs">
              <a href="about.html" onclick="routePage(event, 'about.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>About SLN</span>
              </a>
              <a href="about.html#leadership" onclick="routePage(event, 'about.html', 'leadership')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Our Leadership</span>
              </a>
              <a href="about.html#why-sln" onclick="routePage(event, 'about.html', 'why-sln')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Why SLN?</span>
              </a>
              <a href="about.html#partners" onclick="routePage(event, 'about.html', 'partners')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Partners &amp; Accreditations</span>
              </a>
              <a href="about.html#clients" onclick="routePage(event, 'about.html', 'clients')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Our Clients</span>
              </a>
              <a href="about.html#success-stories" onclick="routePage(event, 'about.html', 'success-stories')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Success Stories</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 3. Cybersecurity ▾ (Mega-Menu with 4 Strategic Categories) -->
        <div class="relative group/nav">
          <button type="button" class="nav-btn font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap" data-route="soc.html">
            <span>Cybersecurity</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#18202A] dark:group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Mega Dropdown Panel -->
          <div class="hidden group-hover/nav:block absolute top-full -left-20 xl:-left-12 pt-2 w-[760px] xl:w-[820px] z-50 transition-all duration-150">
            <div class="bg-white dark:bg-[#181C20] rounded-2xl border border-slate-200 dark:border-[#2C3136] shadow-2xl p-5 overflow-hidden text-xs">
              <div class="grid grid-cols-4 gap-4">
                
                <!-- Category 1: Offensive Security -->
                <div class="space-y-2">
                  <div class="flex items-center gap-1.5 pb-1 border-b border-slate-100 dark:border-[#282D32]">
                    <span class="w-1 h-3 bg-[#D6A84F] rounded-full inline-block"></span>
                    <span class="font-mono text-[11px] font-bold text-[#18202A] dark:text-white uppercase tracking-wider">Offensive Security</span>
                  </div>
                  <ul class="space-y-1 text-slate-600 dark:text-slate-300">
                    <li><a href="soc.html#vapt" onclick="routePage(event, 'soc.html', 'vapt')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Vulnerability Assessment &amp; Penetration Testing</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Web Application Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Mobile Application Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">API Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Network Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Cloud Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Security Assessment</a></li>
                  </ul>
                </div>

                <!-- Category 2: Security Operations -->
                <div class="space-y-2">
                  <div class="flex items-center gap-1.5 pb-1 border-b border-slate-100 dark:border-[#282D32]">
                    <span class="w-1 h-3 bg-[#D6A84F] rounded-full inline-block"></span>
                    <span class="font-mono text-[11px] font-bold text-[#18202A] dark:text-white uppercase tracking-wider">Security Operations</span>
                  </div>
                  <ul class="space-y-1 text-slate-600 dark:text-slate-300">
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] text-[#B08D57] dark:text-[#D6A84F] font-semibold transition">SOC-as-a-Service</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">24×7 Security Monitoring</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Threat Detection &amp; Response</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Incident Response</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Threat Intelligence</a></li>
                  </ul>
                </div>

                <!-- Category 3: Security Consulting -->
                <div class="space-y-2">
                  <div class="flex items-center gap-1.5 pb-1 border-b border-slate-100 dark:border-[#282D32]">
                    <span class="w-1 h-3 bg-[#D6A84F] rounded-full inline-block"></span>
                    <span class="font-mono text-[11px] font-bold text-[#18202A] dark:text-white uppercase tracking-wider">Security Consulting</span>
                  </div>
                  <ul class="space-y-1 text-slate-600 dark:text-slate-300">
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Cybersecurity Consulting</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Risk Assessment</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Security Strategy</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Security Compliance</a></li>
                    <li><a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">Security Awareness</a></li>
                  </ul>
                </div>

                <!-- Category 4: AI & Emerging Security -->
                <div class="space-y-2">
                  <div class="flex items-center gap-1.5 pb-1 border-b border-slate-100 dark:border-[#282D32]">
                    <span class="w-1 h-3 bg-[#D6A84F] rounded-full inline-block"></span>
                    <span class="font-mono text-[11px] font-bold text-[#18202A] dark:text-white uppercase tracking-wider">AI &amp; Emerging</span>
                  </div>
                  <ul class="space-y-1 text-slate-600 dark:text-slate-300">
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">AI Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">AI Testing</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">AI Governance</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-slate-50 dark:hover:bg-[#202428] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition">AI Risk &amp; Compliance</a></li>
                  </ul>
                </div>

              </div>
            </div>
          </div>
        </div>

        <!-- 4. IT Services ▾ -->
        <div class="relative group/nav">
          <button type="button" class="nav-btn font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap" data-route="it-services.html">
            <span>IT Services</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#18202A] dark:group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- IT Services Dropdown Panel -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[260px] z-50 transition-all duration-150">
            <div class="bg-white dark:bg-[#181C20] rounded-xl border border-slate-200 dark:border-[#2C3136] shadow-xl py-2 overflow-hidden text-xs">
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Website Development</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Application Development</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Cloud Solutions</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Network Solutions</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>IT Infrastructure &amp; Support</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Application Testing</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>IT Resource Management</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 5. Academia ▾ -->
        <div class="relative group/nav">
          <button type="button" class="nav-btn font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap" data-route="campus.html">
            <span>Academia</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#18202A] dark:group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Academia Dropdown Panel -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[270px] z-50 transition-all duration-150">
            <div class="bg-white dark:bg-[#181C20] rounded-xl border border-slate-200 dark:border-[#2C3136] shadow-xl py-2 overflow-hidden text-xs">
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Academic Partnerships</span>
              </a>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Cybersecurity Workshops</span>
              </a>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Faculty Development Programs</span>
              </a>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Student Skill Development</span>
              </a>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Cybersecurity Curriculum</span>
              </a>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Campus Cybersecurity Programs</span>
              </a>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Industry–Academia Engagement</span>
              </a>
              <a href="internships.html" onclick="routePage(event, 'internships.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-[#B08D57] dark:text-[#D6A84F] font-semibold transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>3-Month Cybersecurity Internship</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 6. Internships (Top-Level Primary Navigation Item) -->
        <a href="internships.html" onclick="routePage(event, 'internships.html')" class="nav-btn font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all whitespace-nowrap" data-route="internships.html">
          <span>Internships</span>
        </a>

        <!-- 7. Training & Certifications ▾ -->
        <div class="relative group/nav">
          <button type="button" class="nav-btn font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap" data-route="training.html">
            <span>Training &amp; Certifications</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#18202A] dark:group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Training Dropdown Panel -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[270px] z-50 transition-all duration-150">
            <div class="bg-white dark:bg-[#181C20] rounded-xl border border-slate-200 dark:border-[#2C3136] shadow-xl py-2 overflow-hidden text-xs">
              <a href="training.html" onclick="routePage(event, 'training.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Cybersecurity Training</span>
              </a>
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Corporate Training</span>
              </a>
              <a href="isc2.html" onclick="routePage(event, 'isc2.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>CISSP</span>
              </a>
              <a href="isc2.html" onclick="routePage(event, 'isc2.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>ISC2 Certifications</span>
              </a>
              <a href="ec-council.html" onclick="routePage(event, 'ec-council.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>EC-Council Certifications</span>
              </a>
              <a href="cambridge.html" onclick="routePage(event, 'cambridge.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Cambridge Learning</span>
              </a>
              <a href="training.html" onclick="routePage(event, 'training.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Professional Upskilling</span>
              </a>
              <a href="training.html" onclick="routePage(event, 'training.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Customized Training</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 8. Corporate ▾ -->
        <div class="relative group/nav">
          <button type="button" class="nav-btn font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap" data-route="enterprises.html">
            <span>Corporate</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#18202A] dark:group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Corporate Dropdown Panel -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[260px] z-50 transition-all duration-150">
            <div class="bg-white dark:bg-[#181C20] rounded-xl border border-slate-200 dark:border-[#2C3136] shadow-xl py-2 overflow-hidden text-xs">
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Cybersecurity Consulting</span>
              </a>
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Corporate Training</span>
              </a>
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Employee Cybersecurity Awareness</span>
              </a>
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Security Assessments</span>
              </a>
              <a href="soc.html" onclick="routePage(event, 'soc.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Managed Security Services</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Technology Solutions</span>
              </a>
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Enterprise Partnerships</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 9. Resources ▾ -->
        <div class="relative group/nav">
          <button type="button" class="nav-btn font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap" data-route="resources">
            <span>Resources</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#18202A] dark:group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Resources Dropdown Panel -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[220px] z-50 transition-all duration-150">
            <div class="bg-white dark:bg-[#181C20] rounded-xl border border-slate-200 dark:border-[#2C3136] shadow-xl py-2 overflow-hidden text-xs">
              <a href="training.html" onclick="routePage(event, 'training.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Insights</span>
              </a>
              <a href="training.html" onclick="routePage(event, 'training.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Events &amp; Workshops</span>
              </a>
              <a href="training-schedule.html" onclick="routePage(event, 'training-schedule.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Training Calendar</span>
              </a>
              <a href="about.html" onclick="routePage(event, 'about.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Case Studies</span>
              </a>
              <a href="index.html" onclick="routePage(event, 'index.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Gallery</span>
              </a>
              <a href="contact.html" onclick="routePage(event, 'contact.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Downloads</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 10. Contact ▾ -->
        <div class="relative group/nav">
          <button type="button" class="nav-btn font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap" data-route="contact.html">
            <span>Contact</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#18202A] dark:group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Contact Dropdown Panel -->
          <div class="hidden group-hover/nav:block absolute top-full right-0 pt-2 w-[200px] z-50 transition-all duration-150">
            <div class="bg-white dark:bg-[#181C20] rounded-xl border border-slate-200 dark:border-[#2C3136] shadow-xl py-2 overflow-hidden text-xs">
              <a href="contact.html" onclick="routePage(event, 'contact.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Contact Us</span>
              </a>
              <a href="contact.html" onclick="routePage(event, 'contact.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Enquire Now</span>
              </a>
              <a href="contact.html" onclick="routePage(event, 'contact.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] text-slate-700 dark:text-slate-200 hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] shrink-0"></span>
                <span>Partner With Us</span>
              </a>
            </div>
          </div>
        </div>

      </nav>

      <!-- Right Action CTA (Preserves Existing SLN Button UI) -->
      <div class="flex items-center gap-3 shrink-0">
        <!-- Theme Toggle Button -->
        <button onclick="toggleTheme()" class="p-2.5 rounded-xl border border-[var(--border-white)] bg-slate-50 dark:bg-[#202428] text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white transition shadow-xs focus:outline-none" aria-label="Toggle Theme">
          <i data-lucide="sun" class="w-4 h-4 hidden dark:block text-[#D6A84F]"></i>
          <i data-lucide="moon" class="w-4 h-4 block dark:hidden text-slate-700"></i>
        </button>

        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="hidden sm:inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-xs tracking-wide shadow-xs transition-all">
          <span>ENQUIRE NOW</span>
          <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
        </a>

        <!-- Mobile Menu Trigger -->
        <button onclick="toggleMobileNav()" class="lg:hidden p-2.5 rounded-xl border border-[var(--border-white)] bg-slate-50 dark:bg-[#202428] text-slate-700 dark:text-slate-200 focus:outline-none" aria-label="Toggle navigation" id="mobileMenuBtn">
          <i data-lucide="menu" class="w-5 h-5"></i>
        </button>
      </div>

    </div>

    <!-- Mobile Drawer Navigation (Matches Section 15 Structure & UI) -->
    <div id="mobileDrawer" class="hidden lg:hidden border-t border-[var(--border-white)] bg-white dark:bg-[#1B1E21] px-6 py-5 space-y-3 isolate-scroll max-h-[calc(100vh-80px)] overflow-y-auto custom-scrollbar shadow-xl">
      
      <!-- HOME -->
      <a href="index.html" onclick="routePage(event, 'index.html'); toggleMobileNav();" class="block w-full text-left text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] py-1 border-b border-[var(--border-white)]/40">HOME</a>

      <!-- ABOUT US + -->
      <div class="border-b border-[var(--border-white)]/40 pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileAboutMenu', 'mobileAboutChev')">
          <span class="text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">ABOUT US</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-500 hover:text-[var(--text-white-head)] hover:bg-slate-100 dark:hover:bg-[#24282C] focus:outline-none" aria-label="Toggle About Us submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileAboutChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileAboutMenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-slate-50 dark:bg-[#15181B] rounded-xl border border-[var(--border-white)] my-1 text-xs">
          <a href="about.html" onclick="routePage(event, 'about.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">About SLN</a>
          <a href="about.html#leadership" onclick="routePage(event, 'about.html', 'leadership'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Our Leadership</a>
          <a href="about.html#why-sln" onclick="routePage(event, 'about.html', 'why-sln'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Why SLN?</a>
          <a href="about.html#partners" onclick="routePage(event, 'about.html', 'partners'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Partners &amp; Accreditations</a>
          <a href="about.html#clients" onclick="routePage(event, 'about.html', 'clients'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Our Clients</a>
          <a href="about.html#success-stories" onclick="routePage(event, 'about.html', 'success-stories'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Success Stories</a>
        </div>
      </div>

      <!-- CYBERSECURITY + -->
      <div class="border-b border-[var(--border-white)]/40 pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileCyberMenu', 'mobileCyberChev')">
          <span class="text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">CYBERSECURITY</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-500 hover:text-[var(--text-white-head)] hover:bg-slate-100 dark:hover:bg-[#24282C] focus:outline-none" aria-label="Toggle Cybersecurity submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileCyberChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileCyberMenu" class="hidden pl-3 pr-2 py-1.5 space-y-2 bg-slate-50 dark:bg-[#15181B] rounded-xl border border-[var(--border-white)] my-1 text-xs">
          <div>
            <span class="font-mono text-[10px] font-bold uppercase text-[#B08D57] dark:text-[#D6A84F] block px-2 pt-1">Offensive Security</span>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">VAPT &amp; Pen Testing</a>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Web, Mobile &amp; API Security</a>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Cloud &amp; Network Security</a>
          </div>
          <div>
            <span class="font-mono text-[10px] font-bold uppercase text-[#B08D57] dark:text-[#D6A84F] block px-2 pt-1">Security Operations</span>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 text-[#B08D57] dark:text-[#D6A84F] font-semibold">SOC-as-a-Service (24×7)</a>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Threat Detection &amp; Response</a>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Incident Response &amp; Forensics</a>
          </div>
          <div>
            <span class="font-mono text-[10px] font-bold uppercase text-[#B08D57] dark:text-[#D6A84F] block px-2 pt-1">Security Consulting &amp; AI</span>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Cybersecurity Consulting &amp; Risk</a>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">AI Security &amp; Governance</a>
          </div>
        </div>
      </div>

      <!-- IT SERVICES + -->
      <div class="border-b border-[var(--border-white)]/40 pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileITMenu', 'mobileITChev')">
          <span class="text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">IT SERVICES</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-500 hover:text-[var(--text-white-head)] hover:bg-slate-100 dark:hover:bg-[#24282C] focus:outline-none" aria-label="Toggle IT Services submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileITChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileITMenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-slate-50 dark:bg-[#15181B] rounded-xl border border-[var(--border-white)] my-1 text-xs">
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Website Development</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Application Development</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Cloud Solutions</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Network Solutions</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">IT Infrastructure &amp; Support</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Application Testing</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">IT Resource Management</a>
        </div>
      </div>

      <!-- ACADEMIA + -->
      <div class="border-b border-[var(--border-white)]/40 pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileAcademiaMenu', 'mobileAcademiaChev')">
          <span class="text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">ACADEMIA</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-500 hover:text-[var(--text-white-head)] hover:bg-slate-100 dark:hover:bg-[#24282C] focus:outline-none" aria-label="Toggle Academia submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileAcademiaChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileAcademiaMenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-slate-50 dark:bg-[#15181B] rounded-xl border border-[var(--border-white)] my-1 text-xs">
          <a href="campus.html" onclick="routePage(event, 'campus.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Academic Partnerships</a>
          <a href="campus.html" onclick="routePage(event, 'campus.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Cybersecurity Workshops</a>
          <a href="campus.html" onclick="routePage(event, 'campus.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Faculty Development Programs</a>
          <a href="campus.html" onclick="routePage(event, 'campus.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Student Skill Development</a>
          <a href="campus.html" onclick="routePage(event, 'campus.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Campus Cybersecurity Programs</a>
          <a href="internships.html" onclick="routePage(event, 'internships.html'); toggleMobileNav();" class="block py-1.5 px-2 text-[#B08D57] dark:text-[#D6A84F] font-semibold">3-Month Cybersecurity Internship</a>
        </div>
      </div>

      <!-- INTERNSHIPS (Direct Link) -->
      <a href="internships.html" onclick="routePage(event, 'internships.html'); toggleMobileNav();" class="block w-full text-left text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] py-1 border-b border-[var(--border-white)]/40">INTERNSHIPS</a>

      <!-- TRAINING & CERTIFICATIONS + -->
      <div class="border-b border-[var(--border-white)]/40 pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileTrainingMenu', 'mobileTrainingChev')">
          <span class="text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">TRAINING &amp; CERTIFICATIONS</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-500 hover:text-[var(--text-white-head)] hover:bg-slate-100 dark:hover:bg-[#24282C] focus:outline-none" aria-label="Toggle Training submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileTrainingChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileTrainingMenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-slate-50 dark:bg-[#15181B] rounded-xl border border-[var(--border-white)] my-1 text-xs">
          <a href="training.html" onclick="routePage(event, 'training.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Cybersecurity Training</a>
          <a href="enterprises.html" onclick="routePage(event, 'enterprises.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Corporate Training</a>
          <a href="isc2.html" onclick="routePage(event, 'isc2.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">CISSP &amp; ISC2 Credentials</a>
          <a href="ec-council.html" onclick="routePage(event, 'ec-council.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">EC-Council Certifications</a>
          <a href="cambridge.html" onclick="routePage(event, 'cambridge.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Cambridge Learning</a>
          <a href="training.html" onclick="routePage(event, 'training.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Professional Upskilling</a>
        </div>
      </div>

      <!-- CORPORATE + -->
      <div class="border-b border-[var(--border-white)]/40 pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileCorporateMenu', 'mobileCorporateChev')">
          <span class="text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">CORPORATE</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-500 hover:text-[var(--text-white-head)] hover:bg-slate-100 dark:hover:bg-[#24282C] focus:outline-none" aria-label="Toggle Corporate submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileCorporateChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileCorporateMenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-slate-50 dark:bg-[#15181B] rounded-xl border border-[var(--border-white)] my-1 text-xs">
          <a href="enterprises.html" onclick="routePage(event, 'enterprises.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Cybersecurity Consulting</a>
          <a href="enterprises.html" onclick="routePage(event, 'enterprises.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Corporate Training</a>
          <a href="enterprises.html" onclick="routePage(event, 'enterprises.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Employee Awareness</a>
          <a href="enterprises.html" onclick="routePage(event, 'enterprises.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Security Assessments</a>
          <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Managed Security Services</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Enterprise Partnerships</a>
        </div>
      </div>

      <!-- RESOURCES + -->
      <div class="border-b border-[var(--border-white)]/40 pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileResourcesMenu', 'mobileResourcesChev')">
          <span class="text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] transition-colors">RESOURCES</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-500 hover:text-[var(--text-white-head)] hover:bg-slate-100 dark:hover:bg-[#24282C] focus:outline-none" aria-label="Toggle Resources submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileResourcesChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileResourcesMenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-slate-50 dark:bg-[#15181B] rounded-xl border border-[var(--border-white)] my-1 text-xs">
          <a href="training.html" onclick="routePage(event, 'training.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Insights</a>
          <a href="training.html" onclick="routePage(event, 'training.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Events &amp; Workshops</a>
          <a href="training-schedule.html" onclick="routePage(event, 'training-schedule.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Training Calendar</a>
          <a href="about.html" onclick="routePage(event, 'about.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Case Studies</a>
          <a href="index.html" onclick="routePage(event, 'index.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Gallery</a>
          <a href="contact.html" onclick="routePage(event, 'contact.html'); toggleMobileNav();" class="block py-1.5 px-2 hover:text-[#B08D57] dark:hover:text-[#D6A84F]">Downloads</a>
        </div>
      </div>

      <!-- CONTACT -->
      <a href="contact.html" onclick="routePage(event, 'contact.html'); toggleMobileNav();" class="block w-full text-left text-sm font-semibold text-[var(--text-white-head)] hover:text-[#B08D57] dark:hover:text-[#D6A84F] py-1 border-b border-[var(--border-white)]/40">CONTACT</a>

      <!-- ENQUIRE NOW -->
      <a href="contact.html" onclick="routePage(event, 'contact.html'); toggleMobileNav();" class="w-full mt-3 flex items-center justify-center gap-2 px-5 py-3 rounded-full bg-[#D6A84F] text-[#18202A] text-xs font-bold shadow-sm">
        <span>ENQUIRE NOW</span>
        <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
      </a>

    </div>
  </header>'''

# ==============================================================================
# 2. NEW INTERNSHIPS VIEW HTML (Matches Section 9 & Existing SLN Theme)
# ==============================================================================
NEW_INTERNSHIPS_VIEW_HTML = '''  <!-- ==================== VIEW: INTERNSHIPS (internships.html) ==================== -->
  <main id="view-internships" class="page-view flex-1 bg-white dark:bg-[#111315]">
    
    <!-- Breadcrumb Area -->
    <div class="white-section border-b border-[var(--border-white)] dark:border-[#2C3136]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
        <nav class="flex items-center gap-2 text-xs font-medium text-[var(--text-white-body)]" aria-label="Breadcrumb">
          <a href="index.html" onclick="routePage(event, 'index.html')" class="hover:text-[var(--text-white-head)] transition">Home</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <a href="campus.html" onclick="routePage(event, 'campus.html')" class="hover:text-[var(--text-white-head)] transition">Academia</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <span class="text-[#D6A84F] font-semibold">Internships</span>
        </nav>
      </div>
    </div>

    <!-- Hero / Header Section -->
    <section class="white-section py-16 sm:py-20 border-b border-[var(--border-white)] dark:border-[#2C3136]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-center">
          
          <div class="lg:col-span-6 order-1 lg:order-2">
            <div class="rounded-2xl overflow-hidden shadow-subtle border border-[var(--border-white)] dark:border-[#34383D]">
              <img src="assets/training_classroom.jpg" alt="Cybersecurity Internship Classroom" class="w-full h-84 object-cover">
            </div>
          </div>

          <div class="lg:col-span-6 order-2 lg:order-1 space-y-4">
            <div class="flex items-center gap-2">
              <span class="w-5 h-0.5 bg-[#D6A84F] inline-block"></span>
              <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">ACADEMIC &amp; EARLY CAREER DEVELOPMENT</span>
            </div>
            <h1 class="font-display font-extrabold text-3xl sm:text-4xl lg:text-5xl text-[var(--text-white-head)] tracking-tight leading-[1.15]">
              Cybersecurity <span class="text-[#D6A84F]">Internship</span>
            </h1>
            <div class="inline-block px-3 py-1 rounded-lg bg-[#B08D57]/10 dark:bg-[#D6A84F]/10 border border-[#B08D57]/30 dark:border-[#D6A84F]/30">
              <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] tracking-wide">3-Month Industry Internship &bull; For 2027 Graduates</span>
            </div>
            <p class="text-sm sm:text-base text-[var(--text-white-body)] leading-relaxed">
              SLN Consulting's rigorous 3-month cybersecurity internship immerses emerging engineers in operational defense, vulnerability assessment, threat intelligence, and modern SOC workflows led by senior practitioners with 30+ years of enterprise experience.
            </p>
            <div class="pt-2 flex flex-wrap items-center gap-4">
              <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-xs tracking-wide shadow-md transition inline-flex items-center gap-2">
                <span>Apply / Enquire</span>
                <i data-lucide="arrow-right" class="w-4 h-4"></i>
              </a>
              <a href="#internship-structure" class="px-6 py-3.5 rounded-full border border-slate-300 dark:border-[#3A4046] text-slate-700 dark:text-slate-200 text-xs font-semibold hover:border-[#D6A84F] transition">
                View Curriculum
              </a>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- 3-Month Industry Internship Framework (CHARCOAL SECTION) -->
    <section id="internship-structure" class="charcoal-section py-16 sm:py-20 border-b border-[#3A4046]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-2xl mx-auto mb-14">
          <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#D6A84F]">STRUCTURED TIMELINE</span>
          <h2 class="font-display font-bold text-2xl sm:text-3xl text-white mt-1">3-Month Industry Internship Roadmap</h2>
          <p class="text-xs sm:text-sm text-[#C9CDD2] mt-1">Comprehensive theoretical grounding combined with intensive hands-on lab defense scenarios.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          
          <!-- Month 1 -->
          <div class="p-6 rounded-2xl charcoal-card border shadow-sm space-y-3 relative overflow-hidden">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-bold px-2.5 py-1 rounded bg-[#D6A84F]/15 text-[#D6A84F]">MONTH 01</span>
              <i data-lucide="shield" class="w-5 h-5 text-[#D6A84F]"></i>
            </div>
            <h3 class="font-display font-bold text-base text-white">Foundations &amp; Threat Modeling</h3>
            <p class="text-xs text-[#C9CDD2] leading-relaxed">
              Enterprise network protocols, TCP/IP deep-dive, Linux/Windows system administration, threat landscape overview, and foundational defense controls.
            </p>
            <ul class="text-xs text-slate-300 space-y-1.5 pt-2 border-t border-[#3A4046]">
              <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F]"></span>Network architecture &amp; packet inspection</li>
              <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F]"></span>Identity &amp; Access Management (IAM)</li>
              <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F]"></span>Security baseline compliance audits</li>
            </ul>
          </div>

          <!-- Month 2 -->
          <div class="p-6 rounded-2xl charcoal-card border shadow-sm space-y-3 relative overflow-hidden">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-bold px-2.5 py-1 rounded bg-[#D6A84F]/15 text-[#D6A84F]">MONTH 02</span>
              <i data-lucide="cpu" class="w-5 h-5 text-[#D6A84F]"></i>
            </div>
            <h3 class="font-display font-bold text-base text-white">Hands-on Security Tasks &amp; VAPT</h3>
            <p class="text-xs text-[#C9CDD2] leading-relaxed">
              Practical vulnerability assessment and penetration testing across web applications, API endpoints, SIEM log analysis, and incident triage.
            </p>
            <ul class="text-xs text-slate-300 space-y-1.5 pt-2 border-t border-[#3A4046]">
              <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F]"></span>OWASP Top 10 web vulnerabilities</li>
              <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F]"></span>SIEM event correlation &amp; alert triage</li>
              <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F]"></span>Vulnerability remediation reporting</li>
            </ul>
          </div>

          <!-- Month 3 -->
          <div class="p-6 rounded-2xl charcoal-card border shadow-sm space-y-3 relative overflow-hidden">
            <div class="flex items-center justify-between">
              <span class="font-mono text-xs font-bold px-2.5 py-1 rounded bg-[#D6A84F]/15 text-[#D6A84F]">MONTH 03</span>
              <i data-lucide="award" class="w-5 h-5 text-[#D6A84F]"></i>
            </div>
            <h3 class="font-display font-bold text-base text-white">Threat Hunting &amp; Placement Preparation</h3>
            <p class="text-xs text-[#C9CDD2] leading-relaxed">
              Incident response exercises, live capture-the-flag simulation, capstone project evaluation, mock technical interviews, and resume alignment.
            </p>
            <ul class="text-xs text-slate-300 space-y-1.5 pt-2 border-t border-[#3A4046]">
              <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F]"></span>Capstone cybersecurity project defense</li>
              <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F]"></span>Placement preparation &amp; interview drills</li>
              <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F]"></span>Internship Certificate &amp; performance record</li>
            </ul>
          </div>

        </div>

      </div>
    </section>

    <!-- Key Program Highlights (WHITE AREA) -->
    <section class="white-section py-16 sm:py-20 border-b border-[var(--border-white)] dark:border-[#2C3136]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-2xl mx-auto mb-12">
          <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">PROGRAM ADVANTAGES</span>
          <h2 class="font-display font-bold text-2xl sm:text-3xl text-[var(--text-white-head)] mt-1">Why Choose SLN Internship?</h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          
          <!-- Highlight 1: Hands-on Tasks -->
          <div class="p-6 rounded-2xl bg-white dark:bg-[#181C20] border border-[var(--border-white)] dark:border-[#34383D] shadow-sm space-y-2 hover:border-[#D6A84F]/50 transition">
            <div class="w-10 h-10 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-3">
              <i data-lucide="terminal" class="w-5 h-5"></i>
            </div>
            <h4 class="font-display font-bold text-base text-[var(--text-white-head)]">Hands-on Cybersecurity Tasks</h4>
            <p class="text-xs text-[var(--text-white-body)] leading-relaxed">
              Work on authentic scenarios: network traffic dissection, firewall config verification, simulated phishing analysis, and endpoint threat containment.
            </p>
          </div>

          <!-- Highlight 2: Internship Certificate -->
          <div class="p-6 rounded-2xl bg-white dark:bg-[#181C20] border border-[var(--border-white)] dark:border-[#34383D] shadow-sm space-y-2 hover:border-[#D6A84F]/50 transition">
            <div class="w-10 h-10 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-3">
              <i data-lucide="file-check" class="w-5 h-5"></i>
            </div>
            <h4 class="font-display font-bold text-base text-[var(--text-white-head)]">Internship Certificate</h4>
            <p class="text-xs text-[var(--text-white-body)] leading-relaxed">
              Receive an official, verifiable SLN Consulting Internship Certificate documenting your completed hours, tools mastered, and evaluation metrics.
            </p>
          </div>

          <!-- Highlight 3: Placement Preparation -->
          <div class="p-6 rounded-2xl bg-white dark:bg-[#181C20] border border-[var(--border-white)] dark:border-[#34383D] shadow-sm space-y-2 hover:border-[#D6A84F]/50 transition">
            <div class="w-10 h-10 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-3">
              <i data-lucide="briefcase" class="w-5 h-5"></i>
            </div>
            <h4 class="font-display font-bold text-base text-[var(--text-white-head)]">Placement Preparation</h4>
            <p class="text-xs text-[var(--text-white-body)] leading-relaxed">
              Direct role mapping for SOC Analyst (L1), Junior Security Engineer, and VAPT Associate roles with resume enhancement and interview coaching.
            </p>
          </div>

          <!-- Highlight 4: For 2027 Graduates -->
          <div class="p-6 rounded-2xl bg-white dark:bg-[#181C20] border border-[var(--border-white)] dark:border-[#34383D] shadow-sm space-y-2 hover:border-[#D6A84F]/50 transition">
            <div class="w-10 h-10 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-3">
              <i data-lucide="calendar" class="w-5 h-5"></i>
            </div>
            <h4 class="font-display font-bold text-base text-[var(--text-white-head)]">For 2027 Graduates</h4>
            <p class="text-xs text-[var(--text-white-body)] leading-relaxed">
              Designed specifically to fit the engineering academic calendar, giving pre-final year students a decisive industry edge ahead of campus recruitment drives.
            </p>
          </div>

          <!-- Highlight 5: Institutional Program -->
          <div class="p-6 rounded-2xl bg-white dark:bg-[#181C20] border border-[var(--border-white)] dark:border-[#34383D] shadow-sm space-y-2 hover:border-[#D6A84F]/50 transition">
            <div class="w-10 h-10 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-3">
              <i data-lucide="building" class="w-5 h-5"></i>
            </div>
            <h4 class="font-display font-bold text-base text-[var(--text-white-head)]">Institutional Internship Program</h4>
            <p class="text-xs text-[var(--text-white-body)] leading-relaxed">
              Dedicated institutional MoUs, cohort-based scheduling, campus bootcamps, and faculty coordination tailored for university departments.
            </p>
          </div>

          <!-- Highlight 6: Apply / Enquire -->
          <div class="p-6 rounded-2xl bg-white dark:bg-[#181C20] border border-[var(--border-white)] dark:border-[#34383D] shadow-sm space-y-2 hover:border-[#D6A84F]/50 transition">
            <div class="w-10 h-10 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-3">
              <i data-lucide="send" class="w-5 h-5"></i>
            </div>
            <h4 class="font-display font-bold text-base text-[var(--text-white-head)]">Apply / Enquire</h4>
            <p class="text-xs text-[var(--text-white-body)] leading-relaxed">
              Flexible batch options across weekday evenings and weekend cohorts. Individual candidates and institutional representatives are welcome to apply.
            </p>
          </div>

        </div>

        <!-- Banner CTA -->
        <div class="mt-12 p-8 rounded-3xl bg-[#181C20] border border-[#3A4046] shadow-xl text-white flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="space-y-1 text-center md:text-left">
            <span class="text-[10px] font-mono font-bold tracking-widest text-[#D6A84F] uppercase">ADMISSIONS OPEN FOR NEXT COHORT</span>
            <h3 class="text-xl sm:text-2xl font-bold font-display text-white">Ready to Launch Your Cybersecurity Career?</h3>
            <p class="text-xs text-slate-300">Enroll individually or connect with our academic team for institutional collaboration.</p>
          </div>
          <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#E5A83B] hover:bg-[#D6A84F] text-[#111315] font-bold text-xs tracking-wide shadow-md transition inline-flex items-center gap-2 shrink-0">
            <span>Apply Now</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </a>
        </div>

      </div>
    </section>

  </main>'''

# ==============================================================================
# 3. NEW FOOTER HTML (Matches Section 17 & 18-21 Exactly)
# ==============================================================================
NEW_FOOTER_HTML = '''  <!-- ==================== SLN CORPORATE FOOTER (RESTRUCTURED PER REQUIREMENTS) ==================== -->
  <footer class="bg-[#111315] text-[#AEB4BA] pt-12 pb-8 border-t border-[#1C2024]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      
      <!-- Top Brand Row: Logo, Tagline, Description & Corporate Inquiries -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 pb-8 border-b border-[#22262C]">
        
        <!-- Company Area -->
        <div class="lg:col-span-7 space-y-3.5">
          <a href="index.html" onclick="routePage(event, 'index.html')" class="inline-block group focus:outline-none" aria-label="SLN Consulting Home">
            <div class="inline-flex items-center justify-center bg-white px-3.5 py-2 rounded-xl shadow-sm border border-slate-200/50 group-hover:shadow-md transition-all">
              <img src="assets/images/sln-consulting-logo.png" alt="SLN Consulting - Solutions for Seamless Growth" class="h-9 w-auto object-contain block" style="max-height: 40px; width: auto;" />
            </div>
          </a>
          
          <div class="font-display font-bold text-sm text-[#D6A84F] tracking-wide">
            Enterprise Technology &amp; Cybersecurity Solutions
          </div>
          
          <p class="text-slate-400 text-xs leading-relaxed max-w-xl">
            Established in 2022 by industry veterans each possessing over three decades of executive experience, SLN Consulting delivers integrated corporate solutions across proactive cyber defense, authorized certifications ((ISC)², EC-Council, Cambridge), academic institution enablement, and enterprise technology services.
          </p>

          <!-- Core Trust Indicators -->
          <div class="flex flex-wrap items-center gap-4 pt-1 text-xs">
            <div class="flex items-center gap-2">
              <i data-lucide="shield-check" class="w-4 h-4 text-[#D6A84F]"></i>
              <span class="text-slate-300 text-xs">Security Focused</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="award" class="w-4 h-4 text-[#D6A84F]"></i>
              <span class="text-slate-300 text-xs">Authorized Training Partner</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="users" class="w-4 h-4 text-[#D6A84F]"></i>
              <span class="text-slate-300 text-xs">Enterprise &amp; Campus Enablement</span>
            </div>
          </div>
        </div>

        <!-- Corporate Inquiries / Subscription -->
        <div class="lg:col-span-5 space-y-3 flex flex-col justify-center">
          <span class="font-mono text-xs uppercase font-bold text-white tracking-widest block">CORPORATE COMMUNICATIONS</span>
          <p class="text-slate-400 text-xs">Receive executive cybersecurity advisories, training calendars, and corporate skilling bulletins.</p>
          <form onsubmit="handleEmailSubscribe(event)" class="relative flex items-center bg-[#181C20] border border-[#30363D] rounded-xl p-1 pl-3.5 focus-within:border-[#D6A84F] transition-colors">
            <i data-lucide="mail" class="w-4 h-4 text-slate-400 shrink-0 mr-2.5"></i>
            <input type="email" required placeholder="Enter corporate email address" class="bg-transparent text-xs text-white placeholder-slate-500 focus:outline-none w-full py-1.5" />
            <button type="submit" aria-label="Subscribe" class="px-4 py-2 rounded-lg bg-[#E5A83B] hover:bg-[#D6A84F] text-[#111315] font-bold text-xs flex items-center justify-center shrink-0 transition-colors shadow-sm gap-1.5">
              <span>Subscribe</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
          </form>
        </div>

      </div>

      <!-- 7-Section Grid (Matches Section 17 Exactly) -->
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-6 text-xs pb-8 border-b border-[#22262C]">
        
        <!-- 1. COMPANY -->
        <div class="space-y-3">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">COMPANY</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F]"></div>
          <ul class="space-y-2 text-xs">
            <li><a href="about.html" onclick="routePage(event, 'about.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">About SLN</a></li>
            <li><a href="about.html#leadership" onclick="routePage(event, 'about.html', 'leadership')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Our Leadership</a></li>
            <li><a href="about.html#why-sln" onclick="routePage(event, 'about.html', 'why-sln')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Why SLN?</a></li>
            <li><a href="about.html#partners" onclick="routePage(event, 'about.html', 'partners')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Partners &amp; Accreditations</a></li>
            <li><a href="about.html#clients" onclick="routePage(event, 'about.html', 'clients')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Our Clients</a></li>
            <li><a href="about.html#success-stories" onclick="routePage(event, 'about.html', 'success-stories')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Success Stories</a></li>
          </ul>
        </div>

        <!-- 2. CYBERSECURITY -->
        <div class="space-y-3">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">CYBERSECURITY</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F]"></div>
          <ul class="space-y-2 text-xs">
            <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Offensive Security</a></li>
            <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Security Operations</a></li>
            <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Security Consulting</a></li>
            <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">AI &amp; Emerging Security</a></li>
            <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">SOC-as-a-Service</a></li>
            <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Security Assessments</a></li>
          </ul>
        </div>

        <!-- 3. IT & CORPORATE -->
        <div class="space-y-3">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">IT &amp; CORPORATE</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F]"></div>
          <ul class="space-y-2 text-xs">
            <li><a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">IT Services</a></li>
            <li><a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Website Development</a></li>
            <li><a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Application Development</a></li>
            <li><a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Cloud Solutions</a></li>
            <li><a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Corporate</a></li>
            <li><a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Enterprise Partnerships</a></li>
            <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Managed Security Services</a></li>
          </ul>
        </div>

        <!-- 4. ACADEMIA & INTERNSHIPS -->
        <div class="space-y-3">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">ACADEMIA &amp; INTERNSHIPS</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F]"></div>
          <ul class="space-y-2 text-xs">
            <li><a href="campus.html" onclick="routePage(event, 'campus.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Academia</a></li>
            <li><a href="campus.html" onclick="routePage(event, 'campus.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Academic Partnerships</a></li>
            <li><a href="campus.html" onclick="routePage(event, 'campus.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Student Skill Development</a></li>
            <li><a href="campus.html" onclick="routePage(event, 'campus.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Campus Cybersecurity</a></li>
            <li><a href="internships.html" onclick="routePage(event, 'internships.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Cybersecurity Internship</a></li>
            <li><a href="internships.html" onclick="routePage(event, 'internships.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">3-Month Internship</a></li>
            <li><a href="internships.html" onclick="routePage(event, 'internships.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Placement Preparation</a></li>
          </ul>
        </div>

        <!-- 5. TRAINING & CERTIFICATIONS -->
        <div class="space-y-3">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">TRAINING &amp; CERTIFICATIONS</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F]"></div>
          <ul class="space-y-2 text-xs">
            <li><a href="training.html" onclick="routePage(event, 'training.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Cybersecurity Training</a></li>
            <li><a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Corporate Training</a></li>
            <li><a href="isc2.html" onclick="routePage(event, 'isc2.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">CISSP</a></li>
            <li><a href="isc2.html" onclick="routePage(event, 'isc2.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">ISC2</a></li>
            <li><a href="ec-council.html" onclick="routePage(event, 'ec-council.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">EC-Council</a></li>
            <li><a href="cambridge.html" onclick="routePage(event, 'cambridge.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Cambridge Learning</a></li>
            <li><a href="training.html" onclick="routePage(event, 'training.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Professional Upskilling</a></li>
          </ul>
        </div>

        <!-- 6. RESOURCES -->
        <div class="space-y-3">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">RESOURCES</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F]"></div>
          <ul class="space-y-2 text-xs">
            <li><a href="training.html" onclick="routePage(event, 'training.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Insights</a></li>
            <li><a href="training.html" onclick="routePage(event, 'training.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Events &amp; Workshops</a></li>
            <li><a href="training-schedule.html" onclick="routePage(event, 'training-schedule.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Training Calendar</a></li>
            <li><a href="about.html" onclick="routePage(event, 'about.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Case Studies</a></li>
            <li><a href="index.html" onclick="routePage(event, 'index.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Gallery</a></li>
            <li><a href="contact.html" onclick="routePage(event, 'contact.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Downloads</a></li>
          </ul>
        </div>

        <!-- 7. CONTACT -->
        <div class="space-y-3">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">CONTACT</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F]"></div>
          <ul class="space-y-2 text-xs">
            <li><a href="contact.html" onclick="routePage(event, 'contact.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Contact Us</a></li>
            <li><a href="contact.html" onclick="routePage(event, 'contact.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Enquire Now</a></li>
            <li><a href="contact.html" onclick="routePage(event, 'contact.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Partner With Us</a></li>
            <li class="pt-1.5 border-t border-[#22262C]">
              <a href="mailto:srinivas.c@slnconsulting.co.in" class="text-slate-300 hover:text-[#D6A84F] transition-colors flex items-center gap-1.5 break-all">
                <i data-lucide="mail" class="w-3.5 h-3.5 text-[#D6A84F] shrink-0"></i>
                <span class="truncate">Email Us</span>
              </a>
            </li>
            <li>
              <a href="tel:+919940196195" class="text-slate-300 hover:text-[#D6A84F] transition-colors flex items-center gap-1.5 font-medium">
                <i data-lucide="phone" class="w-3.5 h-3.5 text-[#D6A84F] shrink-0"></i>
                <span>+91 9940196195</span>
              </a>
            </li>
            <li>
              <div class="text-slate-400 flex items-start gap-1.5 leading-snug">
                <i data-lucide="map-pin" class="w-3.5 h-3.5 text-[#D6A84F] shrink-0 mt-0.5"></i>
                <span>Chennai - 600042, Tamil Nadu, India</span>
              </div>
            </li>
          </ul>
        </div>

      </div>

      <!-- Bottom Bar: Copyright, Legal Policies & Social Links (Matches Section 20) -->
      <div class="pt-2 flex flex-col lg:flex-row items-center justify-between gap-4 text-xs text-slate-400">
        
        <!-- Left: Gold accent bar + Copyright -->
        <div class="flex items-center gap-2">
          <span class="w-1 h-3.5 bg-[#D6A84F] rounded-full inline-block"></span>
          <span>&copy; 2026 SLN Consulting. All Rights Reserved.</span>
        </div>

        <!-- Center: Policy Links (Privacy Policy | Terms & Conditions | Cookie Policy | Disclaimer) -->
        <div class="flex flex-wrap items-center justify-center gap-x-3 gap-y-1 text-[11px] text-slate-400">
          <button onclick="openPolicyModal('privacy')" class="hover:text-white transition cursor-pointer">Privacy Policy</button>
          <span class="text-slate-600">|</span>
          <button onclick="openPolicyModal('terms')" class="hover:text-white transition cursor-pointer">Terms &amp; Conditions</button>
          <span class="text-slate-600">|</span>
          <button onclick="openPolicyModal('cookie')" class="hover:text-white transition cursor-pointer">Cookie Policy</button>
          <span class="text-slate-600">|</span>
          <button onclick="openPolicyModal('disclaimer')" class="hover:text-white transition cursor-pointer">Disclaimer</button>
        </div>

        <!-- Right: Professional Presence (Preserves Verified Company Links) -->
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-2">
            <!-- LinkedIn -->
            <a href="https://www.linkedin.com/company/sln-consulting" target="_blank" rel="noopener noreferrer" class="w-7 h-7 rounded-lg bg-[#181C20] hover:bg-[#D6A84F] border border-[#2E353D] hover:border-[#D6A84F] flex items-center justify-center text-slate-200 hover:text-[#111315] transition-all shadow-sm" aria-label="SLN Consulting LinkedIn" title="SLN Consulting LinkedIn">
              <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24" aria-hidden="true">
                <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>
              </svg>
            </a>
            <!-- Email -->
            <a href="mailto:srinivas.c@slnconsulting.co.in" class="w-7 h-7 rounded-lg bg-[#181C20] hover:bg-[#D6A84F] border border-[#2E353D] hover:border-[#D6A84F] flex items-center justify-center text-slate-200 hover:text-[#111315] transition-all shadow-sm" aria-label="SLN Consulting Email" title="SLN Consulting Email">
              <i data-lucide="mail" class="w-3.5 h-3.5"></i>
            </a>
            <!-- Phone -->
            <a href="tel:+919940196195" class="w-7 h-7 rounded-lg bg-[#181C20] hover:bg-[#D6A84F] border border-[#2E353D] hover:border-[#D6A84F] flex items-center justify-center text-slate-200 hover:text-[#111315] transition-all shadow-sm" aria-label="SLN Consulting Phone" title="SLN Consulting Phone">
              <i data-lucide="phone" class="w-3.5 h-3.5"></i>
            </a>
          </div>
          <span class="text-slate-600 hidden sm:inline">|</span>
          <span class="text-[11px] font-mono text-slate-400">Chennai, India</span>
        </div>

      </div>

    </div>
  </footer>'''

# ==============================================================================
# 4. UPDATED JAVASCRIPT ROUTER AND HELPERS
# ==============================================================================
UPDATED_SCRIPT_HTML = '''  <!-- ==================== ROUTER & INTERACTIVE LOGIC ==================== -->
  <script>
    // Initialize Lucide Icons
    if (window.lucide) {
      lucide.createIcons();
    }

    // Theme Switcher Functionality
    function toggleTheme() {
      if (document.documentElement.classList.contains('dark')) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('sln_theme', 'light');
      } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('sln_theme', 'dark');
      }
      if (window.lucide) lucide.createIcons();
    }

    // Mobile Accordion Toggle
    function toggleMobileAccordion(menuId, chevId) {
      const menu = document.getElementById(menuId);
      const chev = document.getElementById(chevId);
      if (!menu) return;
      const isHidden = menu.classList.contains('hidden');
      if (isHidden) {
        menu.classList.remove('hidden');
        if (chev) chev.classList.add('rotate-180');
      } else {
        menu.classList.add('hidden');
        if (chev) chev.classList.remove('rotate-180');
      }
    }

    // Comprehensive Route Mapping supporting all pages and anchor aliases
    const routeMap = {
      // Home
      'index.html': 'view-index',
      'index': 'view-index',
      '': 'view-index',
      '/': 'view-index',

      // About
      'about.html': 'view-about',
      'about': 'view-about',
      'about-us': 'view-about',
      'about-sln': 'view-about',
      'leadership': 'view-about',
      'why-sln': 'view-about',
      'partners': 'view-about',
      'clients': 'view-about',
      'success-stories': 'view-about',

      // Cybersecurity
      'soc.html': 'view-soc',
      'soc': 'view-soc',
      'soc-as-a-service': 'view-soc',
      'cybersecurity': 'view-soc',
      'offensive-security': 'view-soc',
      'security-operations': 'view-soc',
      'security-consulting': 'view-soc',
      'ai-security': 'view-soc',
      'vapt': 'view-soc',
      'security-assessments': 'view-soc',
      'managed-detection-response': 'view-soc',

      // IT Services
      'it-services.html': 'view-it-services',
      'it-services': 'view-it-services',
      'it': 'view-it-services',
      'website-development': 'view-it-services',
      'app-development': 'view-it-services',
      'cloud-solutions': 'view-it-services',
      'network-solutions': 'view-it-services',
      'it-infrastructure': 'view-it-services',
      'application-testing': 'view-it-services',
      'it-resource-management': 'view-it-services',

      // Academia
      'campus.html': 'view-campus',
      'campus': 'view-campus',
      'academia': 'view-campus',
      'academic-partnerships': 'view-campus',
      'cybersecurity-workshops': 'view-campus',
      'faculty-development': 'view-campus',
      'student-skill-development': 'view-campus',
      'cybersecurity-curriculum': 'view-campus',
      'campus-cybersecurity': 'view-campus',

      // Internships
      'internships.html': 'view-internships',
      'internships': 'view-internships',
      'internship': 'view-internships',
      'cybersecurity-internship': 'view-internships',
      '3-month-internship': 'view-internships',

      // Training & Certifications
      'training.html': 'view-training',
      'training': 'view-training',
      'training-schedule.html': 'view-training',
      'training-schedule': 'view-training',
      'training_schedule.php': 'view-training',
      'training_schedule': 'view-training',
      'certifications': 'view-training',
      'training-and-certifications': 'view-training',
      'cambridge.html': 'view-cambridge',
      'cambridge': 'view-cambridge',
      'cambridge-learning': 'view-cambridge',
      'isc2.html': 'view-isc2',
      'isc2': 'view-isc2',
      'isc2-credentials': 'view-isc2',
      'cissp': 'view-isc2',
      'ec-council.html': 'view-ec-council',
      'ec-council': 'view-ec-council',
      'eccouncil': 'view-ec-council',

      // Corporate
      'enterprises.html': 'view-enterprises',
      'enterprises': 'view-enterprises',
      'enterprise': 'view-enterprises',
      'corporate': 'view-enterprises',
      'skilling-enterprises': 'view-enterprises',
      'corporate-training': 'view-enterprises',
      'employee-awareness': 'view-enterprises',

      // Resources
      'resources': 'view-training',
      'training-calendar': 'view-training',
      'events-workshops': 'view-training',
      'insights': 'view-about',
      'case-stories': 'view-about',

      // Contact
      'contact.html': 'view-contact',
      'contact': 'view-contact',
      'contact-us': 'view-contact',
      'enquire-now': 'view-contact',
      'partner-with-us': 'view-contact',

      // Legacy fallback
      'offerings.html': 'view-soc',
      'offerings': 'view-soc',
      'our-offering': 'view-soc',
      'our-offerings': 'view-soc'
    };

    // Client-side router function (Direct 1-Click Navigation)
    function routePage(e, pageName, anchorId = null, pushHistory = true) {
      closeAllDrawers();
      if (e && e.preventDefault) {
        e.preventDefault();
      }

      // Normalize aliases
      let cleanPath = (pageName || '').split('#')[0].split('/').pop();
      if (!cleanPath && anchorId && routeMap[anchorId]) {
        cleanPath = anchorId;
      }
      if (cleanPath === '' || cleanPath === 'index' || cleanPath === '/') cleanPath = 'index.html';
      if (cleanPath === 'about-us' || cleanPath === 'about') cleanPath = 'about.html';
      if (cleanPath === 'contact-us' || cleanPath === 'contact') cleanPath = 'contact.html';
      if (cleanPath === 'training' || cleanPath === 'training-schedule' || cleanPath === 'training-schedule.html') cleanPath = 'training.html';
      if (cleanPath === 'enterprises' || cleanPath === 'enterprise' || cleanPath === 'corporate') cleanPath = 'enterprises.html';
      if (cleanPath === 'campus' || cleanPath === 'academia') cleanPath = 'campus.html';
      if (cleanPath === 'internships' || cleanPath === 'internship') cleanPath = 'internships.html';
      if (cleanPath === 'soc' || cleanPath === 'soc-as-a-service' || cleanPath === 'cybersecurity') cleanPath = 'soc.html';
      if (cleanPath === 'it' || cleanPath === 'it-services') cleanPath = 'it-services.html';
      if (cleanPath === 'offerings' || cleanPath === 'offerings.html' || cleanPath === 'our-offering') cleanPath = 'soc.html';

      let viewId = 'view-index';
      if (anchorId && routeMap[anchorId]) {
        viewId = routeMap[anchorId];
      } else if (routeMap[cleanPath]) {
        viewId = routeMap[cleanPath];
      }

      // Switch active view
      document.querySelectorAll('.page-view').forEach(p => p.classList.remove('active'));
      const targetView = document.getElementById(viewId);
      if (targetView) {
        targetView.classList.add('active');
      }

      // Update Navigation Active State
      document.querySelectorAll('.nav-btn').forEach(btn => {
        const routeAttr = btn.getAttribute('data-route') || '';
        let isMatching = false;
        if (viewId === 'view-index' && routeAttr === 'index.html') isMatching = true;
        else if (viewId === 'view-about' && routeAttr === 'about.html') isMatching = true;
        else if (viewId === 'view-soc' && routeAttr === 'soc.html') isMatching = true;
        else if (viewId === 'view-it-services' && routeAttr === 'it-services.html') isMatching = true;
        else if (viewId === 'view-campus' && routeAttr === 'campus.html') isMatching = true;
        else if (viewId === 'view-internships' && routeAttr === 'internships.html') isMatching = true;
        else if ((viewId === 'view-training' || viewId === 'view-cambridge' || viewId === 'view-isc2' || viewId === 'view-ec-council') && routeAttr === 'training.html') isMatching = true;
        else if (viewId === 'view-enterprises' && routeAttr === 'enterprises.html') isMatching = true;
        else if (viewId === 'view-contact' && routeAttr === 'contact.html') isMatching = true;

        if (isMatching) {
          btn.className = 'nav-btn font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap';
        } else {
          btn.className = 'nav-btn font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap';
        }
      });

      // Update Browser History URL
      if (pushHistory) {
        try {
          const newUrl = anchorId ? `${cleanPath}#${anchorId}` : cleanPath;
          window.history.pushState({ page: cleanPath, anchor: anchorId }, '', newUrl);
        } catch (_) {}
      }

      // Smooth scroll to target or top
      if (anchorId) {
        const targetEl = document.getElementById(anchorId);
        if (targetEl) {
          const yOffset = -90;
          const y = targetEl.getBoundingClientRect().top + window.pageYOffset + yOffset;
          window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' });
        } else {
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
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
        routePage(null, path, hash || null, false);
      } catch (_) {}
    });

    // Initial page load router
    window.addEventListener('DOMContentLoaded', () => {
      try {
        let path = window.location.pathname.split('/').pop() || 'index.html';
        let hash = window.location.hash.replace('#', '');
        try {
          window.history.replaceState({ page: path, anchor: hash || null }, '', window.location.href);
        } catch (_) {}
        routePage(null, path, hash || null, false);
      } catch (_) {
        routePage(null, 'index.html', null, false);
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeAllDrawers();
        closePolicyModal();
      }
    });

    function closeAllDrawers() {
      const b = document.getElementById('capabilityDrawerBackdrop');
      const d = document.getElementById('capabilityDrawer');
      if (b) b.classList.add('hidden');
      if (d) d.classList.add('translate-x-full');
      document.body.style.overflow = '';
    }

    // Mobile nav toggle with background scroll lock
    function toggleMobileNav() {
      const m = document.getElementById('mobileDrawer');
      if (!m) return;
      const isHidden = m.classList.toggle('hidden');
      if (!isHidden) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = '';
      }
    }

    // Isolate wheel scrolling on specific scrollable containers
    function isolateScrollElement(el) {
      if (!el) return;
      el.addEventListener('wheel', function(e) {
        const delta = e.deltaY;
        const up = delta < 0;
        const scrollHeight = el.scrollHeight;
        const height = el.clientHeight;
        const scrollTop = el.scrollTop;

        if (scrollHeight <= height) {
          e.preventDefault();
          return;
        }

        if (!up && delta > scrollHeight - height - scrollTop) {
          el.scrollTop = scrollHeight;
          e.preventDefault();
        } else if (up && -delta > scrollTop) {
          el.scrollTop = 0;
          e.preventDefault();
        }
      }, { passive: false });
    }

    window.addEventListener('DOMContentLoaded', () => {
      isolateScrollElement(document.getElementById('drawerBody'));
      isolateScrollElement(document.getElementById('policyModalBody'));
      isolateScrollElement(document.getElementById('mobileDrawer'));
    });

    // Off-Canvas Drawer Data
    const drawerCatalog = {
      'cyber-defense': {
        title: "Cyber Defense — Core Capabilities",
        content: `
          <p class="text-[#C9CDD2] mb-4">Core cybersecurity capabilities delivered under SLN Consulting's Cyber Defense &amp; SOC-As-A-Service framework:</p>
          <div class="space-y-3">
            <div class="p-3.5 rounded-xl bg-[#282D32] border border-[#3A4046]">
              <span class="font-bold text-white block">1. Managed Detection &amp; Response (MDR)</span>
              <p class="text-[#C9CDD2] mt-1 text-xs">Security monitoring, detection and response capabilities for organizational environments.</p>
            </div>
            <div class="p-3.5 rounded-xl bg-[#282D32] border border-[#3A4046]">
              <span class="font-bold text-white block">2. SIEM &amp; Log Management</span>
              <p class="text-[#C9CDD2] mt-1 text-xs">Centralized security information and event management with log collection and analysis.</p>
            </div>
            <div class="p-3.5 rounded-xl bg-[#282D32] border border-[#3A4046]">
              <span class="font-bold text-white block">3. Threat Intelligence</span>
              <p class="text-[#C9CDD2] mt-1 text-xs">Security intelligence to help identify and understand relevant cyber threats.</p>
            </div>
            <div class="p-3.5 rounded-xl bg-[#282D32] border border-[#3A4046]">
              <span class="font-bold text-white block">4. Incident Response &amp; Forensics</span>
              <p class="text-[#C9CDD2] mt-1 text-xs">Investigation and response support for security incidents and digital evidence.</p>
            </div>
            <div class="p-3.5 rounded-xl bg-[#282D32] border border-[#3A4046]">
              <span class="font-bold text-white block">5. VAPT &amp; Security Testing</span>
              <p class="text-[#C9CDD2] mt-1 text-xs">Vulnerability assessment and penetration testing across relevant security environments.</p>
            </div>
            <div class="p-3.5 rounded-xl bg-[#282D32] border border-[#3A4046]">
              <span class="font-bold text-white block">6. Red Teaming &amp; Threat Hunting</span>
              <p class="text-[#C9CDD2] mt-1 text-xs">Proactive security assessment and threat-hunting activities to identify potential weaknesses.</p>
            </div>
          </div>
        `
      }
    };

    function openDrawer(key) {
      const data = drawerCatalog[key];
      if (!data) return;
      document.getElementById('drawerTitle').innerText = data.title;
      document.getElementById('drawerBody').innerHTML = data.content;
      document.getElementById('capabilityDrawerBackdrop').classList.remove('hidden');
      document.getElementById('capabilityDrawer').classList.remove('translate-x-full');
      document.body.style.overflow = 'hidden';
      if (window.lucide) lucide.createIcons();
    }

    function closeDrawer() {
      document.getElementById('capabilityDrawerBackdrop').classList.add('hidden');
      document.getElementById('capabilityDrawer').classList.add('translate-x-full');
      document.body.style.overflow = '';
    }

    // Policy Modals Handlers
    const policyDocs = {
      privacy: {
        title: "Privacy Policy",
        body: "SLN Consulting maintains strict confidentiality regarding client organizational data, candidate training profiles, and credential examination registrations. Information collected is used solely to execute authorized consulting, skilling programs, and IT services in compliance with legal standards."
      },
      terms: {
        title: "Terms & Conditions",
        body: "Engagement with SLN Consulting's managed SOC, certification training, and IT facilities is governed by formal statements of work (SOWs) and organizational agreements. Curriculum materials and partner courseware are protected intellectual property."
      },
      cookie: {
        title: "Cookie Policy",
        body: "This website uses strictly operational cookies to support responsive page navigation and inquiry workflows without cross-site tracking."
      },
      disclaimer: {
        title: "Disclaimer",
        body: "All certification trademarks ((ISC)², EC-Council, Cambridge Assessment) belong to their respective owners. SLN Consulting operates as an authorized training center and partner adhering to official delivery standards."
      }
    };

    function openPolicyModal(type) {
      const p = policyDocs[type];
      if (!p) return;
      document.getElementById('policyModalTitle').innerText = p.title;
      document.getElementById('policyModalBody').innerHTML = `<p>${p.body}</p>`;
      document.getElementById('policyModal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
      if (window.lucide) lucide.createIcons();
    }

    function closePolicyModal() {
      document.getElementById('policyModal').classList.add('hidden');
      document.body.style.overflow = '';
    }

    // Form Handlers
    function handleEmailSubscribe(e) {
      e.preventDefault();
      const toast = document.getElementById('toast');
      const toastMsg = document.getElementById('toastMsg');
      if (toastMsg) toastMsg.innerText = "Thank you. Your corporate email has been registered.";
      toast.classList.remove('hidden');
      toast.classList.add('flex');
      e.target.reset();
      if (window.lucide) lucide.createIcons();
      setTimeout(() => {
        toast.classList.add('hidden');
        toast.classList.remove('flex');
      }, 4000);
    }

    function handleContactSubmit(e) {
      e.preventDefault();
      const toast = document.getElementById('toast');
      toast.classList.remove('hidden');
      toast.classList.add('flex');
      e.target.reset();
      if (window.lucide) lucide.createIcons();
      setTimeout(() => {
        toast.classList.add('hidden');
        toast.classList.remove('flex');
      }, 4000);
    }
  </script>'''

# ==============================================================================
# 5. SCRIPT TO APPLY TO ALL PRODUCTION HTML FILES
# ==============================================================================
def update_html_file(file_path, active_view_id):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace <header ...> ... </header>
    header_regex = re.compile(r'<!-- ==================== TWO-LEVEL EXACT REFERENCE HEADER ==================== -->[\s\S]*?<\/header>', re.DOTALL)
    if header_regex.search(content):
        content = header_regex.sub(NEW_HEADER_HTML, content)
    else:
        # Fallback to <header ...> </header>
        content = re.sub(r'<header[\s\S]*?<\/header>', NEW_HEADER_HTML, content, count=1)

    # 2. Insert or replace #view-internships
    if 'id="view-internships"' not in content:
        # Insert after view-campus
        campus_end = content.find('</main>', content.find('id="view-campus"'))
        if campus_end != -1:
            campus_end += 7
            content = content[:campus_end] + "\n\n" + NEW_INTERNSHIPS_VIEW_HTML + content[campus_end:]
    else:
        # Replace existing view-internships
        v_start = content.find('<!-- ==================== VIEW: INTERNSHIPS')
        if v_start != -1:
            v_end = content.find('</main>', v_start)
            if v_end != -1:
                v_end += 7
                content = content[:v_start] + NEW_INTERNSHIPS_VIEW_HTML + content[v_end:]

    # 3. Replace Footer
    footer_regex = re.compile(r'(<!-- ==================== RESTORED 5-COLUMN COMPACT SLN CORPORATE FOOTER ==================== -->[\s\S]*?<\/footer>|<!-- ==================== SLN CORPORATE FOOTER[\s\S]*?<\/footer>|<footer[\s\S]*?<\/footer>)', re.DOTALL)
    if footer_regex.search(content):
        content = footer_regex.sub(NEW_FOOTER_HTML, content)

    # 4. Replace <script> router block
    script_regex = re.compile(r'<!-- ==================== ROUTER & INTERACTIVE LOGIC ==================== -->[\s\S]*?<\/script>', re.DOTALL)
    if script_regex.search(content):
        content = script_regex.sub(UPDATED_SCRIPT_HTML, content)

    # 5. Set correct active view for this specific file
    # Remove all active classes from <main ... class="page-view ...">
    content = re.sub(r'(<main[^>]+class=["\'][^"\']*)active([^"\']*["\'])', r'\1\2', content)
    content = re.sub(r'class=["\']page-view\s+flex-1', 'class="page-view flex-1', content)
    
    # Add active class to target active_view_id
    target_pattern = f'id="{active_view_id}" class="page-view '
    if target_pattern in content:
        content = content.replace(target_pattern, f'id="{active_view_id}" class="page-view active ')
    else:
        # Try without trailing space
        target_pattern2 = f'id="{active_view_id}" class="page-view'
        content = content.replace(target_pattern2, f'id="{active_view_id}" class="page-view active')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path} successfully (Active: #{active_view_id}).")

def main():
    workspace = os.path.dirname(os.path.abspath(__file__))
    os.chdir(workspace)

    file_mapping = {
        'index.html': 'view-index',
        'about.html': 'view-about',
        'soc.html': 'view-soc',
        'enterprises.html': 'view-enterprises',
        'campus.html': 'view-campus',
        'cambridge.html': 'view-cambridge',
        'isc2.html': 'view-isc2',
        'ec-council.html': 'view-ec-council',
        'it-services.html': 'view-it-services',
        'training.html': 'view-training',
        'training-schedule.html': 'view-training',
        'contact.html': 'view-contact',
        'offerings.html': 'view-soc',
    }

    # First update index.html
    update_html_file('index.html', 'view-index')

    # Create internships.html from index.html if it doesn't exist
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_content = f.read()
    with open('internships.html', 'w', encoding='utf-8') as f:
        f.write(idx_content)

    file_mapping['internships.html'] = 'view-internships'

    # Update all files
    for fn, act in file_mapping.items():
        update_html_file(fn, act)

    print("\nAll 14 production HTML files updated with new Navigation, Internships View, and new Footer!")

if __name__ == '__main__':
    main()
