import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# EXACT NEW PREMIUM ENTERPRISE CYBERSECURITY DARK HEADER HTML
# ==============================================================================
PREMIUM_DARK_HEADER_HTML = '''  <!-- ==================== PREMIUM ENTERPRISE CYBERSECURITY DARK HEADER ==================== -->
  <header class="sticky top-0 z-40 bg-[#16191D] border-b border-white/[0.08] shadow-lg transition-colors duration-200">
    
    <!-- ROW 1 — TOP INFORMATION BAR (Dark Charcoal Bar) -->
    <div class="bg-[#111315] border-b border-white/[0.06] text-slate-300">
      <div class="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8 py-2 flex items-center justify-between gap-4 text-xs">
        
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

        <!-- Right: Phone | Email (Theme Toggle completely removed) -->
        <div class="flex items-center gap-4 shrink-0">
          <a href="tel:+919940196195" class="flex items-center gap-1.5 text-xs text-slate-300 hover:text-[#D6A84F] transition font-medium">
            <i data-lucide="phone" class="w-3.5 h-3.5 text-[#D6A84F] shrink-0"></i>
            <span>+91 9940196195</span>
          </a>
          <span class="text-slate-600 hidden sm:inline">|</span>
          <a href="mailto:srinivas.c@slnconsulting.co.in" class="hidden sm:flex items-center gap-1.5 text-xs text-slate-300 hover:text-[#D6A84F] transition font-medium">
            <i data-lucide="mail" class="w-3.5 h-3.5 text-[#D6A84F] shrink-0"></i>
            <span class="truncate">srinivas.c@slnconsulting.co.in</span>
          </a>
        </div>

      </div>
    </div>

    <!-- ROW 2 — MAIN NAVIGATION BAR (Seamless Dark Continuous Header) -->
    <div class="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8 h-[74px] flex items-center justify-between gap-3 xl:gap-6">
      
      <!-- Left: Logo (Transparent area, no white background, vertically centered) -->
      <a href="index.html" onclick="routePage(event, 'index.html')" class="flex items-center shrink-0 focus:outline-none transition-transform hover:opacity-95" aria-label="SLN Consulting Home">
        <img src="assets/images/sln-consulting-logo.png" alt="SLN Consulting - Solutions for Seamless Growth" class="h-10 sm:h-11 w-auto object-contain block" style="max-height: 44px; width: auto;" />
      </a>

      <!-- Center: Main Navigation (10 Items, single clean horizontal flex row, vertically centered) -->
      <nav class="hidden lg:flex items-center gap-2 xl:gap-3.5 2xl:gap-4.5 text-[12px] xl:text-[13px] 2xl:text-sm font-medium tracking-normal" aria-label="Main Navigation">
        
        <!-- 1. Home -->
        <a href="index.html" onclick="routePage(event, 'index.html')" class="nav-btn font-medium xl:font-semibold text-[#D6A84F] border-b-2 border-[#D6A84F] pb-1 transition-all whitespace-nowrap" data-route="index.html">Home</a>

        <!-- 2. About Us ▾ -->
        <div class="relative group/nav flex items-center h-full">
          <button type="button" class="nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap cursor-pointer" data-route="about.html">
            <span>About Us</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- About Us Dropdown Panel (Dark Theme) -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[240px] z-50 transition-all duration-150">
            <div class="bg-[#181C20] rounded-xl border border-[#2C3136] shadow-2xl py-2 overflow-hidden text-xs">
              <a href="about.html" onclick="routePage(event, 'about.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>About SLN</span>
              </a>
              <a href="about.html#leadership" onclick="routePage(event, 'about.html', 'leadership')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Our Leadership</span>
              </a>
              <a href="about.html#why-sln" onclick="routePage(event, 'about.html', 'why-sln')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Why SLN?</span>
              </a>
              <a href="about.html#partners" onclick="routePage(event, 'about.html', 'partners')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Partners &amp; Accreditations</span>
              </a>
              <a href="about.html#clients" onclick="routePage(event, 'about.html', 'clients')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Our Clients</span>
              </a>
              <a href="about.html#success-stories" onclick="routePage(event, 'about.html', 'success-stories')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Success Stories</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 3. Cybersecurity ▾ (Dark Mega-Menu with 4 Strategic Categories) -->
        <div class="relative group/nav flex items-center h-full">
          <button type="button" class="nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap cursor-pointer" data-route="soc.html">
            <span>Cybersecurity</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Mega Dropdown Panel (Dark Theme) -->
          <div class="hidden group-hover/nav:block absolute top-full -left-16 xl:-left-24 pt-2 w-[760px] xl:w-[820px] z-50 transition-all duration-150">
            <div class="bg-[#181C20] rounded-2xl border border-[#2C3136] shadow-2xl p-5 overflow-hidden text-xs">
              <div class="grid grid-cols-4 gap-4">
                
                <!-- Category 1: Offensive Security -->
                <div class="space-y-2">
                  <div class="flex items-center gap-1.5 pb-1 border-b border-[#282D32]">
                    <span class="w-1 h-3 bg-[#D6A84F] rounded-full inline-block"></span>
                    <span class="font-mono text-[10px] xl:text-[11px] font-bold text-white uppercase tracking-wider">Offensive Security</span>
                  </div>
                  <ul class="space-y-1 text-slate-300">
                    <li><a href="soc.html#vapt" onclick="routePage(event, 'soc.html', 'vapt')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Vulnerability Assessment &amp; Penetration Testing</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Web Application Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Mobile Application Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">API Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Network Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Cloud Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Security Assessment</a></li>
                  </ul>
                </div>

                <!-- Category 2: Security Operations -->
                <div class="space-y-2">
                  <div class="flex items-center gap-1.5 pb-1 border-b border-[#282D32]">
                    <span class="w-1 h-3 bg-[#D6A84F] rounded-full inline-block"></span>
                    <span class="font-mono text-[10px] xl:text-[11px] font-bold text-white uppercase tracking-wider">Security Operations</span>
                  </div>
                  <ul class="space-y-1 text-slate-300">
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] text-[#D6A84F] font-semibold transition">SOC-as-a-Service (24×7)</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">24×7 Security Monitoring</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Threat Detection &amp; Response</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Incident Response &amp; Forensics</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Threat Intelligence</a></li>
                  </ul>
                </div>

                <!-- Category 3: Security Consulting -->
                <div class="space-y-2">
                  <div class="flex items-center gap-1.5 pb-1 border-b border-[#282D32]">
                    <span class="w-1 h-3 bg-[#D6A84F] rounded-full inline-block"></span>
                    <span class="font-mono text-[10px] xl:text-[11px] font-bold text-white uppercase tracking-wider">Security Consulting</span>
                  </div>
                  <ul class="space-y-1 text-slate-300">
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Cybersecurity Consulting</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Risk Assessment</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Security Strategy</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Security Compliance</a></li>
                    <li><a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">Security Awareness</a></li>
                  </ul>
                </div>

                <!-- Category 4: AI & Emerging Security -->
                <div class="space-y-2">
                  <div class="flex items-center gap-1.5 pb-1 border-b border-[#282D32]">
                    <span class="w-1 h-3 bg-[#D6A84F] rounded-full inline-block"></span>
                    <span class="font-mono text-[10px] xl:text-[11px] font-bold text-white uppercase tracking-wider">AI &amp; Emerging</span>
                  </div>
                  <ul class="space-y-1 text-slate-300">
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">AI Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">AI Testing</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">AI Governance</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="block py-1 px-1.5 rounded hover:bg-[#22272B] hover:text-[#D6A84F] transition">AI Risk &amp; Compliance</a></li>
                  </ul>
                </div>

              </div>
            </div>
          </div>
        </div>

        <!-- 4. IT Services ▾ -->
        <div class="relative group/nav flex items-center h-full">
          <button type="button" class="nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap cursor-pointer" data-route="it-services.html">
            <span>IT Services</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- IT Services Dropdown Panel (Dark Theme) -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[260px] z-50 transition-all duration-150">
            <div class="bg-[#181C20] rounded-xl border border-[#2C3136] shadow-2xl py-2 overflow-hidden text-xs">
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Website Development</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Application Development</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Cloud Solutions</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Network Solutions</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>IT Infrastructure &amp; Support</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Application Testing</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>IT Resource Management</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 5. Academia ▾ -->
        <div class="relative group/nav flex items-center h-full">
          <button type="button" class="nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap cursor-pointer" data-route="campus.html">
            <span>Academia</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Academia Dropdown Panel (Dark Theme) -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[270px] z-50 transition-all duration-150">
            <div class="bg-[#181C20] rounded-xl border border-[#2C3136] shadow-2xl py-2 overflow-hidden text-xs">
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Academic Partnerships</span>
              </a>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Cybersecurity Workshops</span>
              </a>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Faculty Development Programs</span>
              </a>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Student Skill Development</span>
              </a>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Cybersecurity Curriculum</span>
              </a>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Campus Cybersecurity Programs</span>
              </a>
              <a href="campus.html" onclick="routePage(event, 'campus.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Industry–Academia Engagement</span>
              </a>
              <a href="internships.html" onclick="routePage(event, 'internships.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-[#D6A84F] font-semibold transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>3-Month Cybersecurity Internship</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 6. Internships (Top-Level Primary Navigation Item) -->
        <a href="internships.html" onclick="routePage(event, 'internships.html')" class="nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all whitespace-nowrap cursor-pointer" data-route="internships.html">
          <span>Internships</span>
        </a>

        <!-- 7. Training & Certifications ▾ -->
        <div class="relative group/nav flex items-center h-full">
          <button type="button" class="nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap cursor-pointer" data-route="training.html">
            <span>Training &amp; Certifications</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Training Dropdown Panel (Dark Theme) -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[270px] z-50 transition-all duration-150">
            <div class="bg-[#181C20] rounded-xl border border-[#2C3136] shadow-2xl py-2 overflow-hidden text-xs">
              <a href="training.html" onclick="routePage(event, 'training.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Cybersecurity Training</span>
              </a>
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Corporate Training</span>
              </a>
              <a href="isc2.html" onclick="routePage(event, 'isc2.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>CISSP</span>
              </a>
              <a href="isc2.html" onclick="routePage(event, 'isc2.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>ISC2 Certifications</span>
              </a>
              <a href="ec-council.html" onclick="routePage(event, 'ec-council.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>EC-Council Certifications</span>
              </a>
              <a href="cambridge.html" onclick="routePage(event, 'cambridge.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Cambridge Learning</span>
              </a>
              <a href="training.html" onclick="routePage(event, 'training.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Professional Upskilling</span>
              </a>
              <a href="training.html" onclick="routePage(event, 'training.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Customized Training</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 8. Corporate ▾ -->
        <div class="relative group/nav flex items-center h-full">
          <button type="button" class="nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap cursor-pointer" data-route="enterprises.html">
            <span>Corporate</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Corporate Dropdown Panel (Dark Theme) -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[260px] z-50 transition-all duration-150">
            <div class="bg-[#181C20] rounded-xl border border-[#2C3136] shadow-2xl py-2 overflow-hidden text-xs">
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Cybersecurity Consulting</span>
              </a>
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Corporate Training</span>
              </a>
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Employee Cybersecurity Awareness</span>
              </a>
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Security Assessments</span>
              </a>
              <a href="soc.html" onclick="routePage(event, 'soc.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Managed Security Services</span>
              </a>
              <a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Technology Solutions</span>
              </a>
              <a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Enterprise Partnerships</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 9. Resources ▾ -->
        <div class="relative group/nav flex items-center h-full">
          <button type="button" class="nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap cursor-pointer" data-route="resources">
            <span>Resources</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Resources Dropdown Panel (Dark Theme) -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[220px] z-50 transition-all duration-150">
            <div class="bg-[#181C20] rounded-xl border border-[#2C3136] shadow-2xl py-2 overflow-hidden text-xs">
              <a href="training.html" onclick="routePage(event, 'training.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Insights</span>
              </a>
              <a href="training.html" onclick="routePage(event, 'training.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Events &amp; Workshops</span>
              </a>
              <a href="training-schedule.html" onclick="routePage(event, 'training-schedule.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Training Calendar</span>
              </a>
              <a href="about.html" onclick="routePage(event, 'about.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Case Studies</span>
              </a>
              <a href="index.html" onclick="routePage(event, 'index.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Gallery</span>
              </a>
              <a href="contact.html" onclick="routePage(event, 'contact.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Downloads</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 10. Contact ▾ -->
        <div class="relative group/nav flex items-center h-full">
          <button type="button" class="nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap cursor-pointer" data-route="contact.html">
            <span>Contact</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Contact Dropdown Panel (Dark Theme) -->
          <div class="hidden group-hover/nav:block absolute top-full right-0 pt-2 w-[200px] z-50 transition-all duration-150">
            <div class="bg-[#181C20] rounded-xl border border-[#2C3136] shadow-2xl py-2 overflow-hidden text-xs">
              <a href="contact.html" onclick="routePage(event, 'contact.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Contact Us</span>
              </a>
              <a href="contact.html" onclick="routePage(event, 'contact.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Enquire Now</span>
              </a>
              <a href="contact.html" onclick="routePage(event, 'contact.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Partner With Us</span>
              </a>
            </div>
          </div>
        </div>

      </nav>

      <!-- Right Action CTA: ENQUIRE NOW (Theme toggle completely removed, perfectly aligned) -->
      <div class="flex items-center shrink-0">
        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="hidden sm:inline-flex items-center justify-center gap-2 px-5 py-2.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-xs tracking-wider shadow-md transition-all shrink-0">
          <span>ENQUIRE NOW</span>
          <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
        </a>

        <!-- Mobile Menu Trigger (No theme toggle on mobile) -->
        <button onclick="toggleMobileNav()" class="lg:hidden p-2 text-slate-300 hover:text-white focus:outline-none" aria-label="Toggle navigation" id="mobileMenuBtn">
          <i data-lucide="menu" class="w-6 h-6"></i>
        </button>
      </div>

    </div>

    <!-- Mobile Drawer Navigation (Matches Dark Theme & Section 15 Structure) -->
    <div id="mobileDrawer" class="hidden lg:hidden border-t border-[#2C3136] bg-[#181C20] px-6 py-5 space-y-3 isolate-scroll max-h-[calc(100vh-80px)] overflow-y-auto custom-scrollbar shadow-2xl text-white">
      
      <!-- HOME -->
      <a href="index.html" onclick="routePage(event, 'index.html'); toggleMobileNav();" class="block w-full text-left text-sm font-semibold text-white hover:text-[#D6A84F] py-1 border-b border-[#2C3136]">HOME</a>

      <!-- ABOUT US + -->
      <div class="border-b border-[#2C3136] pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileAboutMenu', 'mobileAboutChev')">
          <span class="text-sm font-semibold text-white hover:text-[#D6A84F] transition-colors">ABOUT US</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-400 hover:text-white focus:outline-none" aria-label="Toggle About Us submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileAboutChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileAboutMenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-[#14171A] rounded-xl border border-[#2C3136] my-1 text-xs">
          <a href="about.html" onclick="routePage(event, 'about.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">About SLN</a>
          <a href="about.html#leadership" onclick="routePage(event, 'about.html', 'leadership'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Our Leadership</a>
          <a href="about.html#why-sln" onclick="routePage(event, 'about.html', 'why-sln'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Why SLN?</a>
          <a href="about.html#partners" onclick="routePage(event, 'about.html', 'partners'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Partners &amp; Accreditations</a>
          <a href="about.html#clients" onclick="routePage(event, 'about.html', 'clients'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Our Clients</a>
          <a href="about.html#success-stories" onclick="routePage(event, 'about.html', 'success-stories'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Success Stories</a>
        </div>
      </div>

      <!-- CYBERSECURITY + -->
      <div class="border-b border-[#2C3136] pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileCyberMenu', 'mobileCyberChev')">
          <span class="text-sm font-semibold text-white hover:text-[#D6A84F] transition-colors">CYBERSECURITY</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-400 hover:text-white focus:outline-none" aria-label="Toggle Cybersecurity submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileCyberChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileCyberMenu" class="hidden pl-3 pr-2 py-1.5 space-y-2 bg-[#14171A] rounded-xl border border-[#2C3136] my-1 text-xs">
          <div>
            <span class="font-mono text-[10px] font-bold uppercase text-[#D6A84F] block px-2 pt-1">Offensive Security</span>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 text-slate-300 hover:text-[#D6A84F]">VAPT &amp; Pen Testing</a>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 text-slate-300 hover:text-[#D6A84F]">Web, Mobile &amp; API Security</a>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 text-slate-300 hover:text-[#D6A84F]">Cloud &amp; Network Security</a>
          </div>
          <div>
            <span class="font-mono text-[10px] font-bold uppercase text-[#D6A84F] block px-2 pt-1">Security Operations</span>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 text-[#D6A84F] font-semibold">SOC-as-a-Service (24×7)</a>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 text-slate-300 hover:text-[#D6A84F]">Threat Detection &amp; Response</a>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 text-slate-300 hover:text-[#D6A84F]">Incident Response &amp; Forensics</a>
          </div>
          <div>
            <span class="font-mono text-[10px] font-bold uppercase text-[#D6A84F] block px-2 pt-1">Security Consulting &amp; AI</span>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 text-slate-300 hover:text-[#D6A84F]">Cybersecurity Consulting &amp; Risk</a>
            <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1 px-2 text-slate-300 hover:text-[#D6A84F]">AI Security &amp; Governance</a>
          </div>
        </div>
      </div>

      <!-- IT SERVICES + -->
      <div class="border-b border-[#2C3136] pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileITMenu', 'mobileITChev')">
          <span class="text-sm font-semibold text-white hover:text-[#D6A84F] transition-colors">IT SERVICES</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-400 hover:text-white focus:outline-none" aria-label="Toggle IT Services submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileITChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileITMenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-[#14171A] rounded-xl border border-[#2C3136] my-1 text-xs">
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Website Development</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Application Development</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Cloud Solutions</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Network Solutions</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">IT Infrastructure &amp; Support</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Application Testing</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">IT Resource Management</a>
        </div>
      </div>

      <!-- ACADEMIA + -->
      <div class="border-b border-[#2C3136] pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileAcademiaMenu', 'mobileAcademiaChev')">
          <span class="text-sm font-semibold text-white hover:text-[#D6A84F] transition-colors">ACADEMIA</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-400 hover:text-white focus:outline-none" aria-label="Toggle Academia submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileAcademiaChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileAcademiaMenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-[#14171A] rounded-xl border border-[#2C3136] my-1 text-xs">
          <a href="campus.html" onclick="routePage(event, 'campus.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Academic Partnerships</a>
          <a href="campus.html" onclick="routePage(event, 'campus.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Cybersecurity Workshops</a>
          <a href="campus.html" onclick="routePage(event, 'campus.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Faculty Development Programs</a>
          <a href="campus.html" onclick="routePage(event, 'campus.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Student Skill Development</a>
          <a href="campus.html" onclick="routePage(event, 'campus.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Campus Cybersecurity Programs</a>
          <a href="internships.html" onclick="routePage(event, 'internships.html'); toggleMobileNav();" class="block py-1.5 px-2 text-[#D6A84F] font-semibold">3-Month Cybersecurity Internship</a>
        </div>
      </div>

      <!-- INTERNSHIPS (Direct Link) -->
      <a href="internships.html" onclick="routePage(event, 'internships.html'); toggleMobileNav();" class="block w-full text-left text-sm font-semibold text-white hover:text-[#D6A84F] py-1 border-b border-[#2C3136]">INTERNSHIPS</a>

      <!-- TRAINING & CERTIFICATIONS + -->
      <div class="border-b border-[#2C3136] pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileTrainingMenu', 'mobileTrainingChev')">
          <span class="text-sm font-semibold text-white hover:text-[#D6A84F] transition-colors">TRAINING &amp; CERTIFICATIONS</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-400 hover:text-white focus:outline-none" aria-label="Toggle Training submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileTrainingChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileTrainingMenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-[#14171A] rounded-xl border border-[#2C3136] my-1 text-xs">
          <a href="training.html" onclick="routePage(event, 'training.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Cybersecurity Training</a>
          <a href="enterprises.html" onclick="routePage(event, 'enterprises.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Corporate Training</a>
          <a href="isc2.html" onclick="routePage(event, 'isc2.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">CISSP &amp; ISC2 Credentials</a>
          <a href="ec-council.html" onclick="routePage(event, 'ec-council.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">EC-Council Certifications</a>
          <a href="cambridge.html" onclick="routePage(event, 'cambridge.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Cambridge Learning</a>
          <a href="training.html" onclick="routePage(event, 'training.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Professional Upskilling</a>
        </div>
      </div>

      <!-- CORPORATE + -->
      <div class="border-b border-[#2C3136] pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileCorporateMenu', 'mobileCorporateChev')">
          <span class="text-sm font-semibold text-white hover:text-[#D6A84F] transition-colors">CORPORATE</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-400 hover:text-white focus:outline-none" aria-label="Toggle Corporate submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileCorporateChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileCorporateMenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-[#14171A] rounded-xl border border-[#2C3136] my-1 text-xs">
          <a href="enterprises.html" onclick="routePage(event, 'enterprises.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Cybersecurity Consulting</a>
          <a href="enterprises.html" onclick="routePage(event, 'enterprises.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Corporate Training</a>
          <a href="enterprises.html" onclick="routePage(event, 'enterprises.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Employee Awareness</a>
          <a href="enterprises.html" onclick="routePage(event, 'enterprises.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Security Assessments</a>
          <a href="soc.html" onclick="routePage(event, 'soc.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Managed Security Services</a>
          <a href="it-services.html" onclick="routePage(event, 'it-services.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Enterprise Partnerships</a>
        </div>
      </div>

      <!-- RESOURCES + -->
      <div class="border-b border-[#2C3136] pb-1">
        <div class="flex items-center justify-between py-1 cursor-pointer" onclick="toggleMobileAccordion('mobileResourcesMenu', 'mobileResourcesChev')">
          <span class="text-sm font-semibold text-white hover:text-[#D6A84F] transition-colors">RESOURCES</span>
          <button type="button" class="p-1.5 rounded-lg text-slate-400 hover:text-white focus:outline-none" aria-label="Toggle Resources submenu">
            <svg class="w-4 h-4 transition-transform duration-200" id="mobileResourcesChev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
        <div id="mobileResourcesMenu" class="hidden pl-3 pr-2 py-1.5 space-y-1 bg-[#14171A] rounded-xl border border-[#2C3136] my-1 text-xs">
          <a href="training.html" onclick="routePage(event, 'training.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Insights</a>
          <a href="training.html" onclick="routePage(event, 'training.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Events &amp; Workshops</a>
          <a href="training-schedule.html" onclick="routePage(event, 'training-schedule.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Training Calendar</a>
          <a href="about.html" onclick="routePage(event, 'about.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Case Studies</a>
          <a href="index.html" onclick="routePage(event, 'index.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Gallery</a>
          <a href="contact.html" onclick="routePage(event, 'contact.html'); toggleMobileNav();" class="block py-1.5 px-2 text-slate-300 hover:text-[#D6A84F]">Downloads</a>
        </div>
      </div>

      <!-- CONTACT -->
      <a href="contact.html" onclick="routePage(event, 'contact.html'); toggleMobileNav();" class="block w-full text-left text-sm font-semibold text-white hover:text-[#D6A84F] py-1 border-b border-[#2C3136]">CONTACT</a>

      <!-- ENQUIRE NOW -->
      <a href="contact.html" onclick="routePage(event, 'contact.html'); toggleMobileNav();" class="w-full mt-3 flex items-center justify-center gap-2 px-5 py-3 rounded-full bg-[#D6A84F] text-[#18202A] text-xs font-bold shadow-md">
        <span>ENQUIRE NOW</span>
        <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
      </a>

    </div>
  </header>'''

def update_header_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace header block
    header_regex = re.compile(r'<!-- ==================== (TWO-LEVEL EXACT REFERENCE HEADER|PREMIUM ENTERPRISE CYBERSECURITY DARK HEADER)[\s\S]*?<\/header>', re.DOTALL)
    if header_regex.search(content):
        content = header_regex.sub(PREMIUM_DARK_HEADER_HTML, content)
    else:
        content = re.sub(r'<header[\s\S]*?<\/header>', PREMIUM_DARK_HEADER_HTML, content, count=1)

    # In router script, update routePage active state colors to gold on dark navbar
    old_active_btn_js = "btn.className = 'nav-btn font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap';"
    new_active_btn_js = "btn.className = 'nav-btn font-medium xl:font-semibold text-[#D6A84F] border-b-2 border-[#D6A84F] pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap';"
    if old_active_btn_js in content:
        content = content.replace(old_active_btn_js, new_active_btn_js)

    old_inactive_btn_js = "btn.className = 'nav-btn font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap';"
    new_inactive_btn_js = "btn.className = 'nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap';"
    if old_inactive_btn_js in content:
        content = content.replace(old_inactive_btn_js, new_inactive_btn_js)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated dark header in {file_path}")

def main():
    files = [
        'index.html',
        'about.html',
        'soc.html',
        'enterprises.html',
        'campus.html',
        'internships.html',
        'cambridge.html',
        'isc2.html',
        'ec-council.html',
        'it-services.html',
        'training.html',
        'training-schedule.html',
        'contact.html',
        'offerings.html'
    ]

    for f in files:
        if os.path.exists(f):
            update_header_in_file(f)

    print("\nAll 14 production files updated with the new Dark Navbar!")

if __name__ == '__main__':
    main()
