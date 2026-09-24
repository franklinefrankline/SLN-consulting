# build_enterprises_campus_system.py
import re
import os

view_enterprises_html = '''
  <!-- ==================== DETAIL VIEW: ENTERPRISES ==================== -->
  <main id="view-enterprises" class="page-view flex-1 bg-white dark:bg-[#111315]">
    <!-- Breadcrumb Area -->
    <div class="white-section border-b border-[var(--border-white)] dark:border-[#2C3136]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
        <nav class="flex items-center gap-2 text-xs font-medium text-[var(--text-white-body)]" aria-label="Breadcrumb">
          <a href="index.html" onclick="routePage(event, 'index.html')" class="hover:text-[var(--text-white-head)] transition">Home</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="hover:text-[var(--text-white-head)] transition">Our Offering</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <a href="offerings.html#skilling-solutions" onclick="routePage(event, 'offerings.html', 'skilling-solutions')" class="hover:text-[var(--text-white-head)] transition">Skilling Solutions</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <span class="text-[#D6A84F] font-semibold">Enterprises</span>
        </nav>
      </div>
    </div>

    <!-- Hero / Header Section -->
    <section class="white-section py-16 sm:py-20 border-b border-[var(--border-white)] dark:border-[#2C3136]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-center">
          <div class="lg:col-span-6 order-1 lg:order-2">
            <div class="rounded-2xl overflow-hidden shadow-subtle border border-[var(--border-white)] dark:border-[#34383D]">
              <img src="assets/training_classroom.jpg" alt="Enterprise Training &amp; Workshops" class="w-full h-80 object-cover">
            </div>
          </div>
          <div class="lg:col-span-6 order-2 lg:order-1 space-y-4">
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">02A &bull; CORPORATE LEARNING &amp; WORKSHOPS</span>
            <h1 class="font-display font-bold text-3xl sm:text-4xl text-[var(--text-white-head)]">Enterprises</h1>
            <p class="text-sm sm:text-base text-[var(--text-white-body)] leading-relaxed">
              Empowering modern enterprises with executive cybersecurity briefings, tailored technical workshops, mid &amp; senior leadership masterclasses, and hands-on onboarding programs for freshers.
            </p>
            <div class="pt-2 flex flex-wrap gap-3">
              <a href="#workshops-managers" class="px-5 py-2.5 rounded-xl bg-[#18202A] dark:bg-[#D6A84F] text-white dark:text-[#18202A] text-xs font-bold shadow-xs hover:opacity-90 transition">
                Workshops &amp; Webinars &darr;
              </a>
              <a href="#workshops-freshers" class="px-5 py-2.5 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#1E2226] text-xs font-semibold text-[var(--text-white-head)] hover:border-[#D6A84F] transition">
                Fresher Cybersecurity &darr;
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 1: Training Domains Grid (from source enterprises.php) -->
    <section class="charcoal-section py-16 sm:py-20 border-b border-[#3A4046]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-12">
          <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#D6A84F]">CORE PILLARS</span>
          <h2 class="font-display font-bold text-2xl sm:text-3xl text-white mt-2">Training</h2>
          <p class="text-xs sm:text-sm text-[#C9CDD2] mt-2">Specialized capability tracks delivered by certified industry practitioners.</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          <!-- 01 -->
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-center gap-4">
            <span class="w-10 h-10 rounded-full bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] font-mono font-bold text-xs flex items-center justify-center shrink-0">01</span>
            <div>
              <span class="text-sm font-semibold text-white">Cybersecurity &#10024;&#10024;</span>
            </div>
          </div>
          <!-- 02 -->
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-center gap-4">
            <span class="w-10 h-10 rounded-full bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] font-mono font-bold text-xs flex items-center justify-center shrink-0">02</span>
            <div>
              <span class="text-sm font-semibold text-white">Data Sciences</span>
            </div>
          </div>
          <!-- 03 -->
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-center gap-4">
            <span class="w-10 h-10 rounded-full bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] font-mono font-bold text-xs flex items-center justify-center shrink-0">03</span>
            <div>
              <span class="text-sm font-semibold text-white">Cloud Computing</span>
            </div>
          </div>
          <!-- 04 -->
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-center gap-4">
            <span class="w-10 h-10 rounded-full bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] font-mono font-bold text-xs flex items-center justify-center shrink-0">04</span>
            <div>
              <span class="text-sm font-semibold text-white">Network Management</span>
            </div>
          </div>
          <!-- 05 -->
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-center gap-4">
            <span class="w-10 h-10 rounded-full bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] font-mono font-bold text-xs flex items-center justify-center shrink-0">05</span>
            <div>
              <span class="text-sm font-semibold text-white">Artificial Intelligence</span>
            </div>
          </div>
          <!-- 06 -->
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-center gap-4">
            <span class="w-10 h-10 rounded-full bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] font-mono font-bold text-xs flex items-center justify-center shrink-0">06</span>
            <div>
              <span class="text-sm font-semibold text-white">Machine Language</span>
            </div>
          </div>
          <!-- 07 -->
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-center gap-4">
            <span class="w-10 h-10 rounded-full bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] font-mono font-bold text-xs flex items-center justify-center shrink-0">07</span>
            <div>
              <span class="text-sm font-semibold text-white">Soft Skills</span>
            </div>
          </div>
          <!-- 08 -->
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-center gap-4">
            <span class="w-10 h-10 rounded-full bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] font-mono font-bold text-xs flex items-center justify-center shrink-0">08</span>
            <div>
              <span class="text-sm font-semibold text-white">Soft Management Skills</span>
            </div>
          </div>
          <!-- 09 -->
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-center gap-4">
            <span class="w-10 h-10 rounded-full bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] font-mono font-bold text-xs flex items-center justify-center shrink-0">09</span>
            <div>
              <span class="text-sm font-semibold text-white">Leadership</span>
            </div>
          </div>
        </div>

        <div class="mt-8 text-center">
          <p class="text-xs sm:text-sm font-medium text-[#D6A84F]">
            &#10024;&#10024; All Cybersecurity training leads to attempting global certifications - ISACA, ISC2, EC-Council etc
          </p>
        </div>
      </div>
    </section>

    <!-- SECTION 2: WORKSHOPS & WEBINARS FOR MID & SENIOR MANAGERS -->
    <section id="workshops-managers" class="white-section py-16 sm:py-20 border-b border-[var(--border-white)] dark:border-[#2C3136]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl mb-10">
          <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">EXECUTIVE &amp; MANAGEMENT MODULES</span>
          <h2 class="font-display font-bold text-2xl sm:text-3xl text-[var(--text-white-head)] mt-2">
            WORKSHOPS &amp; WEBINARS FOR MID &amp; SENIOR MANAGERS
          </h2>
          <p class="text-xs sm:text-sm text-[var(--text-white-body)] mt-2">
            Targeted briefings and tactical sessions designed to address modern cyber threat landscapes, technology shifts, and corporate resilience.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Executive Session on Cybersecurity for C-Suite Leaders</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Cybersecurity Risks for Financial Organizations</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Cybersecurity Enterprise Awareness: Empowering Vigilance</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Critical IT &amp; Cybersecurity Infrastructure Review</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Artificial Intelligence (Ai) for Information Security Audit</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Threats and Vulnerability Management</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Data Security: Addressing Enterprise Concerns</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Cybersecurity in the Cloud: Ensuring Visibility &amp; Control</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Zero Trust: Disrupt, Destroy, Steal</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Blockchain Operational and Deployment Insights</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Metaverse Technologies and Enterprise Adoption</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Security Challenges: Disrupting Disruptors</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Blockchain: Transforming Business Processes</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Cybersecurity for Oil &amp; Gas: Redefining the Landscape</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Leadership Excellence: Mid &amp; Senior managers</span>
          </div>
          <div class="p-4 rounded-xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-2 shrink-0"></span>
            <span class="text-sm font-medium text-[var(--text-white-head)]">Resilience &amp; Building trusted security workforce</span>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: WORKSHOP IN CYBER SECURITY FOR FRESHERS -->
    <section id="workshops-freshers" class="charcoal-section py-16 sm:py-20 border-b border-[#3A4046]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl mb-10">
          <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#D6A84F]">ENTRY-LEVEL ONBOARDING</span>
          <h2 class="font-display font-bold text-2xl sm:text-3xl text-white mt-2">
            WORKSHOP IN CYBER SECURITY FOR FRESHERS
          </h2>
          <p class="text-xs sm:text-sm text-[#C9CDD2] mt-2">
            Comprehensive foundational programs designed to prepare incoming engineers for real-world enterprise cyber operations.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] flex flex-col justify-between">
            <div>
              <h3 class="font-display font-bold text-sm text-white mb-2">Cybersecurity awareness - essentials workshop.</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">Introduction to the key architectural and technological concepts of cybersecurity.</p>
            </div>
          </div>
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] flex flex-col justify-between">
            <div>
              <h3 class="font-display font-bold text-sm text-white mb-2">Security monitoring &amp; management</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">Tools, concepts and methods used to monitor and manage the network security infrastructure.</p>
            </div>
          </div>
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] flex flex-col justify-between">
            <div>
              <h3 class="font-display font-bold text-sm text-white mb-2">Network security concepts &amp; methodologies</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">Key cyber security threats, attack patterns and risks in the cyber world.</p>
            </div>
          </div>
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] flex flex-col justify-between">
            <div>
              <h3 class="font-display font-bold text-sm text-white mb-2">Essential tools for cyber investigation</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">Professional tools to investigate an accident, collect initial evidence and extract the required information for use by the incident response team.</p>
            </div>
          </div>
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] flex flex-col justify-between">
            <div>
              <h3 class="font-display font-bold text-sm text-white mb-2">Incident response principal tactics</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">Tools, skills and work methods utilised by an incident response team.</p>
            </div>
          </div>
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] flex flex-col justify-between">
            <div>
              <h3 class="font-display font-bold text-sm text-white mb-2">Cyber crisis management</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">Skills and concepts required for successful management of a major cyber incident, based on best practices and actual case studies.</p>
            </div>
          </div>
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] flex flex-col justify-between">
            <div>
              <h3 class="font-display font-bold text-sm text-white mb-2">Ethical hacking &amp; penetration testing principles</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">Principles, methodologies and tools for ethical hacking and penetration testing.</p>
            </div>
          </div>
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] flex flex-col justify-between">
            <div>
              <h3 class="font-display font-bold text-sm text-white mb-2">Secure software development a basic introduction</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">Principles for designing secure software architecture and developing secure code, utilising known practices and techniques.</p>
            </div>
          </div>
          <div class="p-5 rounded-xl bg-[#181C20] border border-[#34383D] flex flex-col justify-between">
            <div>
              <h3 class="font-display font-bold text-sm text-white mb-2">Overview of cyber basics</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">Internal processes, mechanisms and stages of malware execution; hands-on experience in collecting evidence and performing a forensic investigation.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Bottom Navigation: Back to All Offerings -->
    <div class="py-8 border-t border-[var(--border-white)] dark:border-[#2C3136] bg-slate-50/50 dark:bg-[#15181B]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-center">
        <a href="offerings.html#skilling-solutions" onclick="backToOfferings(event, 'card-skilling')" class="inline-flex items-center gap-2.5 px-6 py-3 rounded-xl bg-white dark:bg-[#202428] hover:bg-slate-100 dark:hover:bg-[#282D32] border border-[var(--border-white)] dark:border-[#3A4046] text-[#B08D57] dark:text-[#D6A84F] font-semibold text-xs tracking-wider uppercase transition shadow-xs group">
          <i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-0.5 transition-transform"></i>
          <span>Back to All Offerings</span>
        </a>
      </div>
    </div>

    <!-- Closing CTA Section -->
    <section class="py-14 sm:py-16 bg-[#F9F9F8] dark:bg-[#181C20] border-t border-[var(--border-white)] dark:border-[#2C3136]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-6">
        <div class="space-y-2 text-center md:text-left">
          <div class="flex items-center justify-center md:justify-start gap-2">
            <span class="w-8 h-0.5 bg-[#B08D57] dark:bg-[#D6A84F] inline-block"></span>
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">SCHEDULE AN ENTERPRISE WORKSHOP</span>
          </div>
          <h2 class="font-serif text-2xl sm:text-3xl lg:text-4xl font-bold text-[var(--text-white-head)] tracking-tight">
            Elevate Your Organizational Capabilities
          </h2>
        </div>
        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-sm shadow-md transition inline-flex items-center gap-2 shrink-0">
          <span>Enquire Now</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </section>
  </main>
'''

view_campus_html = '''
  <!-- ==================== DETAIL VIEW: CAMPUS ==================== -->
  <main id="view-campus" class="page-view flex-1 bg-white dark:bg-[#111315]">
    <!-- Breadcrumb Area -->
    <div class="white-section border-b border-[var(--border-white)] dark:border-[#2C3136]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
        <nav class="flex items-center gap-2 text-xs font-medium text-[var(--text-white-body)]" aria-label="Breadcrumb">
          <a href="index.html" onclick="routePage(event, 'index.html')" class="hover:text-[var(--text-white-head)] transition">Home</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="hover:text-[var(--text-white-head)] transition">Our Offering</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <a href="offerings.html#skilling-solutions" onclick="routePage(event, 'offerings.html', 'skilling-solutions')" class="hover:text-[var(--text-white-head)] transition">Skilling Solutions</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <span class="text-[#D6A84F] font-semibold">Campus</span>
        </nav>
      </div>
    </div>

    <!-- Hero / Header Section -->
    <section class="white-section py-16 sm:py-20 border-b border-[var(--border-white)] dark:border-[#2C3136]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-center">
          <div class="lg:col-span-6 order-1 lg:order-2">
            <div class="rounded-2xl overflow-hidden shadow-subtle border border-[var(--border-white)] dark:border-[#34383D]">
              <img src="assets/offering_skilling_classroom.jpg" alt="Academic Campus Programs" class="w-full h-80 object-cover">
            </div>
          </div>
          <div class="lg:col-span-6 order-2 lg:order-1 space-y-4">
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">02B &bull; ACADEMIC INSTITUTION ENABLEMENT</span>
            <h1 class="font-display font-bold text-3xl sm:text-4xl text-[var(--text-white-head)]">For Campus</h1>
            <div class="inline-block px-3 py-1 rounded-lg bg-[#B08D57]/10 dark:bg-[#D6A84F]/10 border border-[#B08D57]/30 dark:border-[#D6A84F]/30">
              <span class="font-mono text-xs font-bold text-[#B08D57] dark:text-[#D6A84F] tracking-wide">Defining Career path</span>
            </div>
            <p class="text-sm sm:text-base text-[var(--text-white-body)] leading-relaxed">
              Empowering universities, colleges, and academic institutions to bridge the gap between classroom theory and global industry requirements through certified student development and faculty enablement.
            </p>
            <div class="pt-2">
              <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-sm shadow-md transition inline-flex items-center gap-2">
                <span>Let's discuss</span>
                <i data-lucide="arrow-right" class="w-4 h-4"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- The 6 Campus Offerings Grid -->
    <section class="charcoal-section py-16 sm:py-20 border-b border-[#3A4046]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-12">
          <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#D6A84F]">CAMPUS SOLUTIONS</span>
          <h2 class="font-display font-bold text-2xl sm:text-3xl text-white mt-2">Defining Career path</h2>
          <p class="text-xs sm:text-sm text-[#C9CDD2] mt-2">Comprehensive university modules from pre-induction to faculty masterclasses.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- 1 -->
          <div class="p-6 rounded-2xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-4">
                <i data-lucide="video" class="w-5 h-5"></i>
              </div>
              <h3 class="font-display font-bold text-base text-white mb-2">1. Seminars / Webinars Through Industry SMEs</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">
                Direct engagement sessions with industry subject matter experts covering cutting-edge technological shifts, security trends, and real-world case studies.
              </p>
            </div>
          </div>

          <!-- 2 -->
          <div class="p-6 rounded-2xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-4">
                <i data-lucide="code" class="w-5 h-5"></i>
              </div>
              <h3 class="font-display font-bold text-base text-white mb-2">2. Hackathon Events</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">
                Collaborative technical challenges and competitive hackathons allowing students to solve live enterprise problems and build practical portfolios.
              </p>
            </div>
          </div>

          <!-- 3 -->
          <div class="p-6 rounded-2xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-4">
                <i data-lucide="briefcase" class="w-5 h-5"></i>
              </div>
              <h3 class="font-display font-bold text-base text-white mb-2">3. Preparing Students For Corporate World</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">
                Comprehensive career grooming, resume workshops, mock technical interviews, and industry etiquette training for graduating batches.
              </p>
            </div>
          </div>

          <!-- 4 -->
          <div class="p-6 rounded-2xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-4">
                <i data-lucide="award" class="w-5 h-5"></i>
              </div>
              <h3 class="font-display font-bold text-base text-white mb-2">4. Induction Training</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">
                Pre-employment and corporate onboarding bootcamps aligning collegiate knowledge with day-one workplace readiness and enterprise protocols.
              </p>
            </div>
          </div>

          <!-- 5 -->
          <div class="p-6 rounded-2xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-4">
                <i data-lucide="message-square" class="w-5 h-5"></i>
              </div>
              <h3 class="font-display font-bold text-base text-white mb-2">5. Soft Skills Training</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">
                Professional communication, cross-functional collaboration, presentation skills, and business articulation essentials.
              </p>
            </div>
          </div>

          <!-- 6 -->
          <div class="p-6 rounded-2xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-4">
                <i data-lucide="users" class="w-5 h-5"></i>
              </div>
              <h3 class="font-display font-bold text-base text-white mb-2">6. Faculty Training And Updation (TTT)</h3>
              <p class="text-xs text-[#C9CDD2] leading-relaxed">
                Train-The-Trainer (TTT) intensive workshops updating academic professors and instructors on latest industrial tools, curricula, and labs.
              </p>
            </div>
          </div>
        </div>

        <div class="mt-12 text-center">
          <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-sm shadow-md transition inline-flex items-center gap-2">
            <span>Let's discuss</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </a>
        </div>
      </div>
    </section>

    <!-- Bottom Navigation: Back to All Offerings -->
    <div class="py-8 border-t border-[var(--border-white)] dark:border-[#2C3136] bg-slate-50/50 dark:bg-[#15181B]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-center">
        <a href="offerings.html#skilling-solutions" onclick="backToOfferings(event, 'card-skilling')" class="inline-flex items-center gap-2.5 px-6 py-3 rounded-xl bg-white dark:bg-[#202428] hover:bg-slate-100 dark:hover:bg-[#282D32] border border-[var(--border-white)] dark:border-[#3A4046] text-[#B08D57] dark:text-[#D6A84F] font-semibold text-xs tracking-wider uppercase transition shadow-xs group">
          <i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-0.5 transition-transform"></i>
          <span>Back to All Offerings</span>
        </a>
      </div>
    </div>

    <!-- Closing CTA Section -->
    <section class="py-14 sm:py-16 bg-[#F9F9F8] dark:bg-[#181C20] border-t border-[var(--border-white)] dark:border-[#2C3136]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-6">
        <div class="space-y-2 text-center md:text-left">
          <div class="flex items-center justify-center md:justify-start gap-2">
            <span class="w-8 h-0.5 bg-[#B08D57] dark:bg-[#D6A84F] inline-block"></span>
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">PARTNER WITH SLN CONSULTING</span>
          </div>
          <h2 class="font-serif text-2xl sm:text-3xl lg:text-4xl font-bold text-[var(--text-white-head)] tracking-tight">
            Build Tomorrow’s Talent on Your Campus
          </h2>
        </div>
        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-sm shadow-md transition inline-flex items-center gap-2 shrink-0">
          <span>Let's discuss</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </section>
  </main>
'''

files = ['index.html', 'about.html', 'offerings.html', 'training.html', 'contact.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update links in desktop dropdown to enterprises.html and campus.html
    # In desktop skilling submenu
    content = re.sub(
        r'<a\s+href="[^"]*#skilling-enterprises"[^>]*onclick="routePage\(event,\s*\'offerings\.html\',\s*\'skilling-enterprises\'\)[^>]*>(\s*<span[^>]*></span>\s*<span[^>]*>Enterprises</span>\s*)</a>',
        r'<a href="enterprises.html" onclick="routePage(event, \'enterprises.html\'); closeOfferingsDropdown();" class="flex items-center gap-2 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/sub">\1</a>',
        content
    )
    content = re.sub(
        r'<a\s+href="[^"]*#skilling-campus"[^>]*onclick="routePage\(event,\s*\'offerings\.html\',\s*\'skilling-campus\'\)[^>]*>(\s*<span[^>]*></span>\s*<span[^>]*>Campus</span>\s*)</a>',
        r'<a href="campus.html" onclick="routePage(event, \'campus.html\'); closeOfferingsDropdown();" class="flex items-center gap-2 px-4 py-2 hover:bg-slate-50 dark:hover:bg-[#202428] transition-colors group/sub">\1</a>',
        content
    )

    # In mobile skilling submenu
    content = re.sub(
        r'<a\s+href="[^"]*#skilling-enterprises"[^>]*onclick="routePage\(event,\s*\'offerings\.html\',\s*\'skilling-enterprises\'\)[^>]*>(\s*&bull;\s*Enterprises\s*)</a>',
        r'<a href="enterprises.html" onclick="routePage(event, \'enterprises.html\'); closeAllDrawers();" class="block py-1.5 px-2 text-xs text-slate-600 dark:text-slate-300 hover:text-[#B08D57] dark:hover:text-[#D6A84F] font-medium rounded hover:bg-slate-100 dark:hover:bg-[#1E2226]">\1</a>',
        content
    )
    content = re.sub(
        r'<a\s+href="[^"]*#skilling-campus"[^>]*onclick="routePage\(event,\s*\'offerings\.html\',\s*\'skilling-campus\'\)[^>]*>(\s*&bull;\s*Campus\s*)</a>',
        r'<a href="campus.html" onclick="routePage(event, \'campus.html\'); closeAllDrawers();" class="block py-1.5 px-2 text-xs text-slate-600 dark:text-slate-300 hover:text-[#B08D57] dark:hover:text-[#D6A84F] font-medium rounded hover:bg-slate-100 dark:hover:bg-[#1E2226]">\1</a>',
        content
    )

    # 2. Update view-skilling action buttons to link to dedicated pages
    content = re.sub(
        r'<button\s+onclick="openDrawer\(\'corporate-workshops\'\)"[^>]*>Corporate Workshops &rarr;</button>',
        r'<a href="enterprises.html" onclick="routePage(event, \'enterprises.html\')" class="px-4 py-2 rounded-xl border border-[var(--border-white)] bg-white dark:bg-[#24282C] text-xs font-semibold hover:border-[#202428] transition">Enterprises Workshops &rarr;</a>',
        content
    )
    content = re.sub(
        r'<button\s+onclick="openDrawer\(\'campus-workshops\'\)"[^>]*>Campus Programs &rarr;</button>',
        r'<a href="campus.html" onclick="routePage(event, \'campus.html\')" class="px-4 py-2 rounded-xl border border-[var(--border-white)] bg-white dark:bg-[#24282C] text-xs font-semibold hover:border-[#202428] transition">Campus Programs &rarr;</a>',
        content
    )

    # 3. Add view-enterprises and view-campus if not already present
    # Remove existing view-enterprises / view-campus if any was partially added
    content = re.sub(r'<!-- ==================== DETAIL VIEW: ENTERPRISES ==================== -->.*?<!-- ==================== DETAIL VIEW: CAMPUS ==================== -->.*?</main>', '', content, flags=re.DOTALL)
    content = re.sub(r'<main id="view-enterprises".*?</main>', '', content, flags=re.DOTALL)
    content = re.sub(r'<main id="view-campus".*?</main>', '', content, flags=re.DOTALL)

    # Insert after </main> of view-skilling
    skilling_end = '</main>\n\n  <!-- ==================== DETAIL VIEW 3: CAMBRIDGE LEARNING'
    if '</main>\n\n  <!-- ==================== DETAIL VIEW 3: CAMBRIDGE' in content:
        content = content.replace(
            '</main>\n\n  <!-- ==================== DETAIL VIEW 3: CAMBRIDGE',
            f'</main>\n{view_enterprises_html}\n{view_campus_html}\n\n  <!-- ==================== DETAIL VIEW 3: CAMBRIDGE'
        )
    elif 'id="view-skilling"' in content:
        # Fallback find end of view-skilling
        pos = content.find('id="view-skilling"')
        main_end = content.find('</main>', pos)
        if main_end != -1:
            main_end += len('</main>')
            content = content[:main_end] + f'\n{view_enterprises_html}\n{view_campus_html}' + content[main_end:]

    # 4. Update routeMap in script
    # Ensure enterprises and campus are in routeMap
    if "'enterprises.html': 'view-enterprises'" not in content:
        content = content.replace(
            "'skilling-solutions': 'view-skilling',",
            "'skilling-solutions': 'view-skilling',\n      'enterprises.html': 'view-enterprises',\n      'enterprises': 'view-enterprises',\n      'enterprise': 'view-enterprises',\n      'skilling-enterprises': 'view-enterprises',\n      'skilling-enterprise': 'view-enterprises',\n      'campus.html': 'view-campus',\n      'campus': 'view-campus',\n      'skilling-campus': 'view-campus',"
        )

    # Update isOfferingsGroup
    if "viewId === 'view-enterprises'" not in content:
        content = content.replace(
            "viewId === 'view-skilling' ||",
            "viewId === 'view-skilling' ||\n        viewId === 'view-enterprises' ||\n        viewId === 'view-campus' ||"
        )

    # Update cardIdByAnchor
    if "'enterprises': 'card-skilling'" not in content:
        content = content.replace(
            "'skilling': 'card-skilling',",
            "'skilling': 'card-skilling',\n      'enterprises': 'card-skilling',\n      'campus': 'card-skilling',\n      'skilling-enterprises': 'card-skilling',\n      'skilling-campus': 'card-skilling',"
        )

    # Update initial route detection
    if "path.includes('enterprises.html')" not in content:
        content = content.replace(
            "else if (path.includes('contact.html')) initialPage = 'contact.html';",
            "else if (path.includes('contact.html')) initialPage = 'contact.html';\n      else if (path.includes('enterprises.html')) initialPage = 'enterprises.html';\n      else if (path.includes('campus.html')) initialPage = 'campus.html';"
        )

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {fn}")

# Now generate dedicated enterprises.html and campus.html
with open('offerings.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# For enterprises.html:
ent_html = base_html
# Make view-enterprises active, remove active from view-offerings
ent_html = ent_html.replace('id="view-offerings" class="page-view active flex-1 bg-white dark:bg-[#111315]"', 'id="view-offerings" class="page-view flex-1 bg-white dark:bg-[#111315]"')
ent_html = ent_html.replace('id="view-enterprises" class="page-view flex-1 bg-white dark:bg-[#111315]"', 'id="view-enterprises" class="page-view active flex-1 bg-white dark:bg-[#111315]"')
# Update title tag
ent_html = re.sub(r'<title>.*?</title>', '<title>Enterprises | Skilling Solutions | SLN Consulting</title>', ent_html)
with open('enterprises.html', 'w', encoding='utf-8') as f:
    f.write(ent_html)
print("Created enterprises.html")

# For campus.html:
cam_html = base_html
# Make view-campus active, remove active from view-offerings
cam_html = cam_html.replace('id="view-offerings" class="page-view active flex-1 bg-white dark:bg-[#111315]"', 'id="view-offerings" class="page-view flex-1 bg-white dark:bg-[#111315]"')
cam_html = cam_html.replace('id="view-campus" class="page-view flex-1 bg-white dark:bg-[#111315]"', 'id="view-campus" class="page-view active flex-1 bg-white dark:bg-[#111315]"')
# Update title tag
cam_html = re.sub(r'<title>.*?</title>', '<title>Campus Programs | Skilling Solutions | SLN Consulting</title>', cam_html)
with open('campus.html', 'w', encoding='utf-8') as f:
    f.write(cam_html)
print("Created campus.html")

print("All platform files synchronized successfully!")
