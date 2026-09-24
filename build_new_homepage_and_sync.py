# -*- coding: utf-8 -*-
"""
build_new_homepage_and_sync.py

This script:
1. Updates Header (dark, 10 menu items, transparent logo, single theme toggle immediately before Enquire Now).
2. Updates #view-index Homepage:
   - Hero section (White + Light Blue + Gold) with Direct Inquiries floating form & 4 stats cards
   - About section (Soft Mint / Green) with More About Us button & 4 highlight cards
   - Services section (Soft Lavender / Pastel Multi-Color) with 6 visual interactive service cards
   - Why Choose Us section (Dark Navy / Blue / Purple Cybersecurity) with SOC visual & 4 cards
   - Impact section (Cream / Soft Gold) with 4 metric cards
3. Updates Footer:
   - Dark 5-column footer (Company, Solutions, Training, Resources, Contact)
   - Working subscription form & legal modals & social links
4. Synchronizes across all 14 HTML files, preserving existing file-specific active views!
"""

import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 1. HEADER HTML
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

        <!-- Right: Phone | Email -->
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
                <div>
                  <div class="font-mono text-[10px] font-bold uppercase text-[#D6A84F] tracking-wider mb-2 pb-1 border-b border-[#2C3136] flex items-center gap-1.5">
                    <i data-lucide="shield" class="w-3.5 h-3.5 text-[#D6A84F]"></i>
                    <span>Offensive Security</span>
                  </div>
                  <ul class="space-y-1.5">
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Vulnerability Assessment &amp; Pen Testing</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Web Application Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Mobile Application Security</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Cloud Security Assessment</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">API Security Testing</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Network Penetration Testing</a></li>
                  </ul>
                </div>

                <!-- Category 2: Security Operations & Defense -->
                <div>
                  <div class="font-mono text-[10px] font-bold uppercase text-[#D6A84F] tracking-wider mb-2 pb-1 border-b border-[#2C3136] flex items-center gap-1.5">
                    <i data-lucide="activity" class="w-3.5 h-3.5 text-[#D6A84F]"></i>
                    <span>Security Operations</span>
                  </div>
                  <ul class="space-y-1.5">
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-[#D6A84F] font-semibold hover:underline block py-0.5">SOC-as-a-Service (24×7)</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Threat Detection &amp; Response</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">SIEM Implementation &amp; Mgmt</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Incident Response &amp; Forensics</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Threat Intelligence &amp; Hunting</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Continuous Monitoring</a></li>
                  </ul>
                </div>

                <!-- Category 3: Security Consulting & Governance -->
                <div>
                  <div class="font-mono text-[10px] font-bold uppercase text-[#D6A84F] tracking-wider mb-2 pb-1 border-b border-[#2C3136] flex items-center gap-1.5">
                    <i data-lucide="file-check" class="w-3.5 h-3.5 text-[#D6A84F]"></i>
                    <span>Consulting &amp; Risk</span>
                  </div>
                  <ul class="space-y-1.5">
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Cybersecurity Consulting</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Risk Assessment &amp; Governance</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Compliance (ISO, DPDP, CERT-In)</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Security Architecture Design</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Virtual CISO (vCISO)</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Supply Chain Security</a></li>
                  </ul>
                </div>

                <!-- Category 4: AI & Emerging Tech Security -->
                <div>
                  <div class="font-mono text-[10px] font-bold uppercase text-[#D6A84F] tracking-wider mb-2 pb-1 border-b border-[#2C3136] flex items-center gap-1.5">
                    <i data-lucide="cpu" class="w-3.5 h-3.5 text-[#D6A84F]"></i>
                    <span>AI &amp; Emerging Tech</span>
                  </div>
                  <ul class="space-y-1.5">
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">AI Security &amp; Safety</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Securing LLMs &amp; GenAI</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">AI Governance &amp; Ethics</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">Model Vulnerability Testing</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block py-0.5">AI Defense Frameworks</a></li>
                    <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-[#D6A84F] font-semibold hover:underline block py-0.5">View All Cybersecurity &rarr;</a></li>
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
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[240px] z-50 transition-all duration-150">
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
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[260px] z-50 transition-all duration-150">
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
                <span>Campus Cybersecurity Programs</span>
              </a>
              <div class="border-t border-[#2C3136] my-1"></div>
              <a href="internships.html" onclick="routePage(event, 'internships.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-[#D6A84F] font-semibold transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>3-Month Cybersecurity Internship</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 6. Internships (Direct Link) -->
        <a href="internships.html" onclick="routePage(event, 'internships.html')" class="nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all whitespace-nowrap" data-route="internships.html">Internships</a>

        <!-- 7. Training & Certifications ▾ -->
        <div class="relative group/nav flex items-center h-full">
          <button type="button" class="nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap cursor-pointer" data-route="training.html">
            <span>Training &amp; Certifications</span>
            <svg class="w-3 h-3 text-slate-400 group-hover/nav:text-[#D6A84F] transition-transform duration-200 group-hover/nav:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <!-- Training Dropdown Panel (Dark Theme) -->
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[260px] z-50 transition-all duration-150">
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
                <span>CISSP &amp; ISC2 Credentials</span>
              </a>
              <a href="ec-council.html" onclick="routePage(event, 'ec-council.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>EC-Council Certifications</span>
              </a>
              <a href="cambridge.html" onclick="routePage(event, 'cambridge.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Cambridge English Learning</span>
              </a>
              <a href="training.html" onclick="routePage(event, 'training.html')" class="flex items-center gap-2.5 px-4 py-2 hover:bg-[#22272B] text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span class="w-1.5 h-1.5 rounded-full bg-[#D6A84F] shrink-0"></span>
                <span>Professional Upskilling</span>
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
          <div class="hidden group-hover/nav:block absolute top-full left-0 pt-2 w-[240px] z-50 transition-all duration-150">
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
                <span>Employee Awareness</span>
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
                <span>Enterprise Partnerships</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 9. Resources ▾ -->
        <div class="relative group/nav flex items-center h-full">
          <button type="button" class="nav-btn font-medium xl:font-semibold text-slate-300 hover:text-[#D6A84F] border-b-2 border-transparent pb-1 transition-all flex items-center gap-1 focus:outline-none whitespace-nowrap cursor-pointer" data-route="training.html">
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

      <!-- Right Action CTA: EXACTLY ONE THEME TOGGLE + ENQUIRE NOW -->
      <div class="flex items-center gap-2.5 sm:gap-3 shrink-0">
        
        <!-- Exactly ONE Theme Button (LIGHT <-> DARK) immediately before Enquire Now -->
        <button 
          type="button" 
          onclick="toggleTheme()" 
          id="headerThemeToggle" 
          aria-label="Toggle Light and Dark Mode" 
          title="Toggle Light and Dark Mode" 
          class="px-2.5 py-1.5 sm:px-3 sm:py-2 rounded-xl border border-white/15 bg-white/5 hover:bg-white/10 text-slate-200 hover:text-[#D6A84F] transition-all flex items-center gap-1.5 text-xs font-semibold shrink-0 cursor-pointer"
        >
          <i data-lucide="sun" class="w-3.5 h-3.5 hidden dark:inline-block text-[#D6A84F]"></i>
          <i data-lucide="moon" class="w-3.5 h-3.5 inline-block dark:hidden text-slate-300"></i>
          <span class="text-[11px] font-mono tracking-wider"><span class="dark:hidden">DARK</span><span class="hidden dark:inline">LIGHT</span></span>
        </button>

        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="hidden sm:inline-flex items-center justify-center gap-2 px-5 py-2.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-xs tracking-wider shadow-md transition-all shrink-0 cursor-pointer">
          <span>ENQUIRE NOW</span>
          <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
        </a>

        <!-- Mobile Menu Trigger -->
        <button onclick="toggleMobileNav()" class="lg:hidden p-2 text-slate-300 hover:text-white focus:outline-none cursor-pointer" aria-label="Toggle navigation" id="mobileMenuBtn">
          <i data-lucide="menu" class="w-6 h-6"></i>
        </button>
      </div>

    </div>

    <!-- Mobile Drawer Navigation -->
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
      <a href="contact.html" onclick="routePage(event, 'contact.html'); toggleMobileNav();" class="w-full mt-3 flex items-center justify-center gap-2 px-5 py-3 rounded-full bg-[#D6A84F] text-[#18202A] text-xs font-bold shadow-md cursor-pointer">
        <span>ENQUIRE NOW</span>
        <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
      </a>

    </div>
  </header>'''

# ==============================================================================
# 2. FOOTER HTML (5 Concise Columns: Company, Solutions, Training, Resources, Contact)
# ==============================================================================
PREMIUM_DARK_FOOTER_HTML = '''  <!-- ==================== PREMIUM 5-COLUMN DARK FOOTER ==================== -->
  <footer class="bg-[#0D1117] text-slate-300 pt-12 pb-8 border-t border-[#1C2028]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      
      <!-- Top Brand Row: Logo, Tagline, Description & Corporate Communications -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 pb-8 border-b border-[#21262D]">
        
        <!-- Company Area -->
        <div class="lg:col-span-7 space-y-3.5">
          <a href="index.html" onclick="routePage(event, 'index.html')" class="inline-block group focus:outline-none" aria-label="SLN Consulting Home">
            <img src="assets/images/sln-consulting-logo.png" alt="SLN Consulting - Solutions for Seamless Growth" class="h-10 w-auto object-contain block" style="max-height: 44px; width: auto;" />
          </a>
          
          <div class="font-display font-bold text-sm text-[#D6A84F] tracking-wide">
            SLN CONSULTING &bull; Solutions for Seamless Growth
          </div>
          
          <p class="text-slate-400 text-xs leading-relaxed max-w-xl">
            Established in 2022 by industry leaders with over three decades of consulting and enterprise technology experience, SLN Consulting delivers proactive cyber defense, authorized certification pathways ((ISC)², EC-Council, Cambridge), institutional academic skilling, and enterprise IT services.
          </p>

          <!-- Core Trust Indicators -->
          <div class="flex flex-wrap items-center gap-4 pt-1 text-xs">
            <div class="flex items-center gap-2">
              <i data-lucide="shield-check" class="w-4 h-4 text-[#D6A84F]"></i>
              <span class="text-slate-300 text-xs">Security &amp; Compliance Focused</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="award" class="w-4 h-4 text-[#D6A84F]"></i>
              <span class="text-slate-300 text-xs">Authorized Partner &amp; ATC</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="users" class="w-4 h-4 text-[#D6A84F]"></i>
              <span class="text-slate-300 text-xs">Enterprise &amp; Campus Enablement</span>
            </div>
          </div>
        </div>

        <!-- Corporate Communications / Subscription -->
        <div class="lg:col-span-5 space-y-3 flex flex-col justify-center">
          <span class="font-mono text-xs uppercase font-bold text-white tracking-widest block">CORPORATE COMMUNICATIONS</span>
          <p class="text-slate-400 text-xs">Receive executive cybersecurity advisories, training schedules, and institutional skilling bulletins.</p>
          <form onsubmit="handleEmailSubscribe(event)" class="relative flex items-center bg-[#161B22] border border-[#30363D] rounded-xl p-1 pl-3.5 focus-within:border-[#D6A84F] transition-colors">
            <i data-lucide="mail" class="w-4 h-4 text-slate-400 shrink-0 mr-2.5"></i>
            <input type="email" required placeholder="Enter corporate email address" class="bg-transparent text-xs text-white placeholder-slate-500 focus:outline-none w-full py-1.5" />
            <button type="submit" aria-label="Subscribe" class="px-4 py-2 rounded-lg bg-[#D6A84F] hover:bg-[#C2943F] text-[#111315] font-bold text-xs flex items-center justify-center shrink-0 transition-colors shadow-sm gap-1.5 cursor-pointer">
              <span>Subscribe</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
          </form>
        </div>

      </div>

      <!-- 5-Column Grid (Section 32 requirement: Company, Solutions, Training, Resources, Contact) -->
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-6 text-xs pb-8 border-b border-[#21262D]">
        
        <!-- Column 1: COMPANY -->
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

        <!-- Column 2: SOLUTIONS -->
        <div class="space-y-3">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">SOLUTIONS</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F]"></div>
          <ul class="space-y-2 text-xs">
            <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Offensive Security &amp; VAPT</a></li>
            <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">24×7 SOC Operations</a></li>
            <li><a href="soc.html" onclick="routePage(event, 'soc.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Security Consulting &amp; Risk</a></li>
            <li><a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">IT Infrastructure &amp; Cloud</a></li>
            <li><a href="it-services.html" onclick="routePage(event, 'it-services.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Web &amp; Application Dev</a></li>
            <li><a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Enterprise Solutions</a></li>
          </ul>
        </div>

        <!-- Column 3: TRAINING -->
        <div class="space-y-3">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">TRAINING</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F]"></div>
          <ul class="space-y-2 text-xs">
            <li><a href="training.html" onclick="routePage(event, 'training.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Cybersecurity Training</a></li>
            <li><a href="enterprises.html" onclick="routePage(event, 'enterprises.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Corporate Upskilling</a></li>
            <li><a href="isc2.html" onclick="routePage(event, 'isc2.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">CISSP &amp; (ISC)² Certs</a></li>
            <li><a href="ec-council.html" onclick="routePage(event, 'ec-council.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">EC-Council Certifications</a></li>
            <li><a href="cambridge.html" onclick="routePage(event, 'cambridge.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Cambridge English Learning</a></li>
            <li><a href="internships.html" onclick="routePage(event, 'internships.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">3-Month Internship</a></li>
          </ul>
        </div>

        <!-- Column 4: RESOURCES -->
        <div class="space-y-3">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">RESOURCES</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F]"></div>
          <ul class="space-y-2 text-xs">
            <li><a href="training.html" onclick="routePage(event, 'training.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Insights &amp; Advisories</a></li>
            <li><a href="training.html" onclick="routePage(event, 'training.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Events &amp; Workshops</a></li>
            <li><a href="training-schedule.html" onclick="routePage(event, 'training-schedule.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Training Calendar</a></li>
            <li><a href="about.html" onclick="routePage(event, 'about.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Case Studies</a></li>
            <li><a href="campus.html" onclick="routePage(event, 'campus.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Campus Skilling</a></li>
            <li><a href="contact.html" onclick="routePage(event, 'contact.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Downloads</a></li>
          </ul>
        </div>

        <!-- Column 5: CONTACT -->
        <div class="space-y-3">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">CONTACT</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F]"></div>
          <ul class="space-y-2 text-xs">
            <li><a href="contact.html" onclick="routePage(event, 'contact.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Contact Us</a></li>
            <li><a href="contact.html" onclick="routePage(event, 'contact.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Enquire Now</a></li>
            <li><a href="contact.html" onclick="routePage(event, 'contact.html')" class="text-slate-300 hover:text-[#D6A84F] transition-colors block">Partner With Us</a></li>
            <li class="pt-1.5 border-t border-[#21262D]">
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

      <!-- Bottom Bar: Copyright, Legal Policies & Social Links -->
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

        <!-- Right: Professional Social Links -->
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-2">
            <!-- LinkedIn -->
            <a href="https://www.linkedin.com/company/sln-consulting" target="_blank" rel="noopener noreferrer" class="w-7 h-7 rounded-lg bg-[#161B22] hover:bg-[#D6A84F] border border-[#30363D] hover:border-[#D6A84F] flex items-center justify-center text-slate-200 hover:text-[#111315] transition-all shadow-sm" aria-label="SLN Consulting LinkedIn" title="SLN Consulting LinkedIn">
              <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24" aria-hidden="true">
                <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>
              </svg>
            </a>
            <!-- Email -->
            <a href="mailto:srinivas.c@slnconsulting.co.in" class="w-7 h-7 rounded-lg bg-[#161B22] hover:bg-[#D6A84F] border border-[#30363D] hover:border-[#D6A84F] flex items-center justify-center text-slate-200 hover:text-[#111315] transition-all shadow-sm" aria-label="SLN Consulting Email" title="SLN Consulting Email">
              <i data-lucide="mail" class="w-3.5 h-3.5"></i>
            </a>
            <!-- Phone -->
            <a href="tel:+919940196195" class="w-7 h-7 rounded-lg bg-[#161B22] hover:bg-[#D6A84F] border border-[#30363D] hover:border-[#D6A84F] flex items-center justify-center text-slate-200 hover:text-[#111315] transition-all shadow-sm" aria-label="SLN Consulting Phone" title="SLN Consulting Phone">
              <i data-lucide="phone" class="w-3.5 h-3.5"></i>
            </a>
          </div>
          <span class="text-slate-600 hidden sm:inline">|</span>
          <span class="text-[11px] font-mono text-slate-400">Chennai, India</span>
        </div>

      </div>

    </div>
  </footer>'''

from scratch_generate_homepage import NEW_VIEW_INDEX_HTML

ALL_HTML_FILES = [
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

def update_file(filename):
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return False
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace <header>...</header>
    header_regex = r'<header\b[^>]*>.*?</header>'
    if not re.search(header_regex, content, re.DOTALL):
        print(f"Error: Could not find <header> in {filename}")
        return False
    content = re.sub(header_regex, PREMIUM_DARK_HEADER_HTML.strip(), content, count=1, flags=re.DOTALL)

    # 2. Replace <footer>...</footer>
    footer_regex = r'<footer\b[^>]*>.*?</footer>'
    if not re.search(footer_regex, content, re.DOTALL):
        print(f"Error: Could not find <footer> in {filename}")
        return False
    content = re.sub(footer_regex, PREMIUM_DARK_FOOTER_HTML.strip(), content, count=1, flags=re.DOTALL)

    # 3. Replace <main id="view-index" ...>...</main>
    # In index.html, it should be active.
    # In other files, if index.html is loaded, it's active. If about.html is loaded, view-about is active, and view-index is not active.
    view_index_regex = r'<main[^>]*id=["\']view-index["\'].*?</main>'
    if re.search(view_index_regex, content, re.DOTALL):
        if filename == 'index.html':
            replacement_view = NEW_VIEW_INDEX_HTML.strip()
        else:
            # Keep inactive for standalone files whose default view is their specific page
            replacement_view = NEW_VIEW_INDEX_HTML.strip().replace('page-view active', 'page-view')
        content = re.sub(view_index_regex, replacement_view, content, count=1, flags=re.DOTALL)
    else:
        print(f"Warning: view-index not found in {filename}")

    # Ensure single theme toggle button in HTML
    theme_btn_count = len(re.findall(r'id=["\']headerThemeToggle["\']', content))
    if theme_btn_count != 1:
        print(f"Warning: {filename} has {theme_btn_count} theme toggles")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully updated {filename} (length: {len(content)})")
    return True

def main():
    print("Starting update across all 14 HTML files...")
    success_count = 0
    for fname in ALL_HTML_FILES:
        if update_file(fname):
            success_count += 1
    print(f"\nCompleted! {success_count}/{len(ALL_HTML_FILES)} files updated successfully.")

if __name__ == '__main__':
    main()
