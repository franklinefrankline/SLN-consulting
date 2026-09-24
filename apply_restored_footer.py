import re

new_footer_html = '''  <!-- ==================== RESTORED 5-COLUMN COMPACT SLN CORPORATE FOOTER ==================== -->
  <footer class="bg-[#111315] text-[#AEB4BA] pt-10 pb-6 border-t border-[#1C2024]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
      
      <!-- 5-Column Navigation Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-12 gap-6 lg:gap-8 pb-6 border-b border-[#22262C] text-xs">
        
        <!-- Column 1: SLN Brand Area (lg:col-span-3) -->
        <div class="sm:col-span-2 lg:col-span-3 space-y-3">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl border border-[#D6A84F] bg-[#181C20] flex items-center justify-center shrink-0 shadow-sm">
              <span class="font-display font-extrabold text-[#D6A84F] text-sm tracking-tight">SLN</span>
            </div>
            <div class="flex flex-col">
              <span class="font-display font-bold text-base text-white tracking-tight leading-tight">SLN CONSULTING</span>
              <span class="text-[9px] font-mono text-[#D6A84F] uppercase tracking-wider font-semibold">SOLUTIONS FOR SEAMLESS GROWTH</span>
            </div>
          </div>
          
          <p class="text-slate-400 text-xs leading-relaxed max-w-sm">
            Enterprise technology integration, proactive cyber defense, and authorized workforce skilling frameworks.
          </p>

          <!-- Corporate Email Subscription Input -->
          <form onsubmit="handleEmailSubscribe(event)" class="relative flex items-center bg-[#181C20] border border-[#30363D] rounded-xl p-1 pl-3.5 max-w-sm focus-within:border-[#D6A84F] transition-colors">
            <i data-lucide="mail" class="w-4 h-4 text-slate-400 shrink-0 mr-2.5"></i>
            <input type="email" required placeholder="Enter your corporate email" class="bg-transparent text-xs text-white placeholder-slate-500 focus:outline-none w-full py-1.5" />
            <button type="submit" aria-label="Subscribe" class="w-8 h-8 rounded-lg bg-[#E5A83B] hover:bg-[#D6A84F] text-[#111315] flex items-center justify-center shrink-0 transition-colors shadow-sm">
              <i data-lucide="arrow-right" class="w-4 h-4"></i>
            </button>
          </form>

          <!-- 3 Small Value Indicators -->
          <div class="flex items-center gap-4 pt-0.5 text-xs">
            <div class="flex items-center gap-2">
              <i data-lucide="users" class="w-4 h-4 text-[#D6A84F]"></i>
              <div class="leading-tight">
                <span class="text-[11px] text-slate-200 block font-medium">People</span>
                <span class="text-[9px] text-slate-500 block">Driven</span>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="shield-check" class="w-4 h-4 text-[#D6A84F]"></i>
              <div class="leading-tight">
                <span class="text-[11px] text-slate-200 block font-medium">Security</span>
                <span class="text-[9px] text-slate-500 block">Focused</span>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="trending-up" class="w-4 h-4 text-[#D6A84F]"></i>
              <div class="leading-tight">
                <span class="text-[11px] text-slate-200 block font-medium">Growth</span>
                <span class="text-[9px] text-slate-500 block">Oriented</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Column 2: Our Offerings (lg:col-span-2) -->
        <div class="lg:col-span-2">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">OUR OFFERINGS</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F] mt-1.5 mb-3"></div>
          <ul class="space-y-2 text-xs">
            <li>
              <a href="offerings.html#soc-as-a-service" onclick="routePage(event, 'offerings.html', 'soc-as-a-service')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>SOC-As-A-Service</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="offerings.html#soc-as-a-service" onclick="routePage(event, 'offerings.html', 'soc-as-a-service')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Cyber Defense</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="offerings.html#skilling-solutions" onclick="routePage(event, 'offerings.html', 'skilling-solutions')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Skilling Solutions</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="offerings.html#it-services" onclick="routePage(event, 'offerings.html', 'it-services')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>IT Services</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="offerings.html#it-services" onclick="routePage(event, 'offerings.html', 'it-services')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Facility Management</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
          </ul>
        </div>

        <!-- Column 3: Quick Links (lg:col-span-2) -->
        <div class="lg:col-span-2">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">QUICK LINKS</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F] mt-1.5 mb-3"></div>
          <ul class="space-y-2 text-xs">
            <li>
              <a href="index.html" onclick="routePage(event, 'index.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Home</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="about.html" onclick="routePage(event, 'about.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>About Us</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Our Offerings</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="training.html" onclick="routePage(event, 'training.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Training</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="contact.html" onclick="routePage(event, 'contact.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Contact Us</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
          </ul>
        </div>

        <!-- Column 4: Learning Hub (lg:col-span-2) -->
        <div class="lg:col-span-2">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">LEARNING HUB</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F] mt-1.5 mb-3"></div>
          <ul class="space-y-2 text-xs">
            <li>
              <a href="training.html" onclick="routePage(event, 'training.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Training Overview</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="training.html#view-training" onclick="routePage(event, 'training.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Corporate Learning</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="training.html#view-training" onclick="routePage(event, 'training.html')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Campus Programs</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="offerings.html#cambridge-learning" onclick="routePage(event, 'offerings.html', 'cambridge-learning')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>Cambridge English</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
            <li>
              <a href="offerings.html#isc2" onclick="routePage(event, 'offerings.html', 'isc2')" class="group inline-flex items-center gap-2 text-slate-300 hover:text-[#D6A84F] transition-colors">
                <span>(ISC)&sup2; &amp; EC-Council</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#D6A84F] transition-transform duration-200 group-hover:translate-x-1"></i>
              </a>
            </li>
          </ul>
        </div>

        <!-- Column 5: Chennai Headquarters (lg:col-span-3) -->
        <div class="lg:col-span-3 space-y-2.5">
          <h4 class="font-mono text-xs uppercase font-bold text-white tracking-widest">CHENNAI HEADQUARTERS</h4>
          <div class="h-0.5 w-6 bg-[#D6A84F] mt-1.5 mb-3"></div>
          <ul class="space-y-2 text-xs">
            <li class="flex items-start gap-2 text-slate-300">
              <i data-lucide="map-pin" class="w-3.5 h-3.5 text-[#D6A84F] shrink-0 mt-0.5"></i>
              <span>Chennai - 600042, Tamil Nadu, India</span>
            </li>
            <li>
              <a href="tel:+919940196195" class="flex items-center gap-2 text-slate-300 hover:text-white transition font-medium">
                <i data-lucide="phone" class="w-3.5 h-3.5 text-[#D6A84F] shrink-0"></i>
                <span>+91 9940196195</span>
              </a>
            </li>
            <li>
              <a href="mailto:srinivas.c@slnconsulting.co.in" class="flex items-center gap-2 text-slate-300 hover:text-white transition">
                <i data-lucide="mail" class="w-3.5 h-3.5 text-[#D6A84F] shrink-0"></i>
                <span class="break-all sm:break-normal">srinivas.c@slnconsulting.co.in</span>
              </a>
            </li>
            <li class="flex items-center gap-2 text-slate-400">
              <i data-lucide="headphones" class="w-3.5 h-3.5 text-[#D6A84F] shrink-0"></i>
              <span>Mobile &amp; WhatsApp Support</span>
            </li>
            <li class="pt-1">
              <!-- Emergency SOC Dispatch button -->
              <a href="contact.html#soc-emergency" onclick="routePage(event, 'contact.html')" class="inline-flex items-center justify-between w-full px-3 py-2 rounded-xl bg-[#181C20] hover:bg-[#20252A] border border-[#D6A84F]/50 hover:border-[#D6A84F] transition-all group/soc shadow-sm">
                <div class="flex items-center gap-2">
                  <div class="w-5 h-5 rounded-md bg-[#2B1B1B] text-[#E05252] flex items-center justify-center shrink-0">
                    <i data-lucide="bell" class="w-3 h-3"></i>
                  </div>
                  <span class="text-xs font-semibold text-white">Emergency SOC Dispatch</span>
                </div>
                <i data-lucide="arrow-right" class="w-3 h-3 text-[#D6A84F] group-hover/soc:translate-x-1 transition-transform"></i>
              </a>
            </li>
          </ul>
        </div>

      </div>

      <!-- Bottom Bar: Copyright, Legal & Social -->
      <div class="pt-2 flex flex-col lg:flex-row items-center justify-between gap-4 text-xs text-slate-400">
        <!-- Left: Gold accent bar + Copyright -->
        <div class="flex items-center gap-2">
          <span class="w-1 h-3.5 bg-[#D6A84F] rounded-full inline-block"></span>
          <span>&copy; 2026 SLN Consulting. All Rights Reserved.</span>
        </div>

        <!-- Center: Policy links with vertical divider -->
        <div class="flex flex-wrap items-center justify-center gap-x-3 gap-y-1 text-[11px] text-slate-400">
          <button onclick="openPolicyModal('privacy')" class="hover:text-white transition">Privacy Policy</button>
          <span class="text-slate-600">|</span>
          <button onclick="openPolicyModal('terms')" class="hover:text-white transition">Terms of Service</button>
          <span class="text-slate-600">|</span>
          <button onclick="openPolicyModal('refund')" class="hover:text-white transition">Cancellation &amp; Refund</button>
          <span class="text-slate-600">|</span>
          <button onclick="openPolicyModal('shipping')" class="hover:text-white transition">Shipping &amp; Delivery</button>
          <span class="text-slate-600">|</span>
          <button onclick="openPolicyModal('cookie')" class="hover:text-white transition">Cookie Policy</button>
        </div>

        <!-- Right: Social icons (LinkedIn, GitHub, X, YouTube) + Chennai, India -->
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-2">
            <!-- LinkedIn -->
            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" class="w-7 h-7 rounded-lg bg-[#181C20] hover:bg-[#D6A84F] border border-[#2E353D] hover:border-[#D6A84F] flex items-center justify-center text-slate-200 hover:text-[#111315] transition-all shadow-sm" aria-label="LinkedIn" title="LinkedIn">
              <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24" aria-hidden="true">
                <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>
              </svg>
            </a>
            <!-- GitHub -->
            <a href="https://github.com" target="_blank" rel="noopener noreferrer" class="w-7 h-7 rounded-lg bg-[#181C20] hover:bg-[#D6A84F] border border-[#2E353D] hover:border-[#D6A84F] flex items-center justify-center text-slate-200 hover:text-[#111315] transition-all shadow-sm" aria-label="GitHub" title="GitHub">
              <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24" aria-hidden="true">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/>
              </svg>
            </a>
            <!-- Twitter / X -->
            <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" class="w-7 h-7 rounded-lg bg-[#181C20] hover:bg-[#D6A84F] border border-[#2E353D] hover:border-[#D6A84F] flex items-center justify-center text-slate-200 hover:text-[#111315] transition-all shadow-sm" aria-label="X (Twitter)" title="X (Twitter)">
              <svg class="w-3 h-3 fill-current" viewBox="0 0 24 24" aria-hidden="true">
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
              </svg>
            </a>
            <!-- YouTube -->
            <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" class="w-7 h-7 rounded-lg bg-[#181C20] hover:bg-[#D6A84F] border border-[#2E353D] hover:border-[#D6A84F] flex items-center justify-center text-slate-200 hover:text-[#111315] transition-all shadow-sm" aria-label="YouTube" title="YouTube">
              <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24" aria-hidden="true">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
              </svg>
            </a>
          </div>
          <span class="text-slate-600 hidden sm:inline">|</span>
          <span class="text-[11px] font-mono text-slate-400">Chennai, India</span>
        </div>
      </div>

    </div>
  </footer>'''

files = ['offerings.html', 'index.html', 'about.html', 'training.html', 'contact.html']

pattern_footer = r'(  <!-- ==================== (?:APPROVED|RESTORED).*?FOOTER ====================[\s\S]*?</footer>|  <footer[\s\S]*?</footer>)'

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    if re.search(pattern_footer, content):
        content = re.sub(pattern_footer, new_footer_html.strip(), content)
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated restored 5-column footer in {fn}")
    else:
        print(f"Error: footer pattern not found in {fn}")

print("All files updated with restored 5-column compact footer!")
