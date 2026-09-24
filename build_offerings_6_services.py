import re

# Read current offerings.html
with open('c:/Agen/SLN counsulting/offerings.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. BUILD THE 6-OFFERING MAIN SHOWCASE
showcase_html = '''  <!-- ==================== VIEW 3: MAIN OUR OFFERINGS SHOWCASE (offerings.html) ==================== -->
  <main id="view-offerings" class="page-view active flex-1 bg-white dark:bg-[#111315]">
    
    <!-- 1. HERO SECTION (Clean composition matching reference) -->
    <section class="py-12 sm:py-16 lg:py-20 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">
          
          <!-- Left: Label + Heading -->
          <div class="lg:col-span-6 space-y-4">
            <div class="flex items-center gap-3">
              <span class="w-8 h-0.5 bg-[#B08D57] dark:bg-[#D6A84F] inline-block"></span>
              <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">OUR OFFERINGS</span>
            </div>
            <h1 class="font-serif text-4xl sm:text-5xl lg:text-6xl font-bold text-[var(--text-white-head)] tracking-tight leading-[1.12]">
              Capabilities<br>That Create Impact
            </h1>
          </div>

          <!-- Right: Corporate Office Image -->
          <div class="lg:col-span-6">
            <div class="rounded-2xl overflow-hidden shadow-subtle border border-[var(--border-white)] bg-slate-100 dark:bg-[#202428]">
              <img 
                src="assets/hero_offerings_office.jpg" 
                alt="SLN Consulting Corporate Headquarters" 
                class="w-full h-64 sm:h-72 lg:h-84 object-cover"
              >
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- 2. ALTERNATING 6 OFFERINGS (NO GRID) -->
    
    <!-- 01 SOC-As-A-Service (IMAGE LEFT, CONTENT RIGHT) -->
    <section class="py-14 sm:py-18 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-14 items-center">
          
          <!-- Image Left (7 cols on lg) -->
          <div class="lg:col-span-7">
            <div class="rounded-xl overflow-hidden shadow-sm border border-[var(--border-white)] bg-slate-100 dark:bg-[#202428] cursor-pointer group" onclick="routePage(event, 'offerings.html', 'soc-as-a-service')">
              <img 
                src="assets/soc_operations_center.jpg" 
                alt="SOC-As-A-Service Security Operations Center" 
                class="w-full h-64 sm:h-80 lg:h-[350px] object-cover group-hover:scale-102 transition-transform duration-500"
              >
            </div>
          </div>

          <!-- Content Right (5 cols on lg) -->
          <div class="lg:col-span-5 flex items-center justify-between gap-4">
            <div class="space-y-3">
              <div class="flex items-center gap-3">
                <span class="text-xs font-mono font-bold text-[#B08D57] dark:text-[#D6A84F]">01</span>
                <span class="w-10 h-0.5 bg-[#B08D57] dark:bg-[#D6A84F] inline-block"></span>
              </div>
              <h2 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-[var(--text-white-head)] tracking-tight">
                SOC-As-A-Service
              </h2>
            </div>
            <a href="offerings.html#soc-as-a-service" onclick="routePage(event, 'offerings.html', 'soc-as-a-service')" class="w-12 h-12 sm:w-14 sm:h-14 rounded-full border border-[#B08D57] dark:border-[#D6A84F] text-[#B08D57] dark:text-[#D6A84F] hover:bg-[#B08D57] hover:text-white dark:hover:bg-[#D6A84F] dark:hover:text-[#18202A] flex items-center justify-center transition-all duration-300 shadow-sm shrink-0 group" aria-label="Open SOC-As-A-Service Details">
              <i data-lucide="arrow-right" class="w-5 h-5 sm:w-6 sm:h-6 group-hover:translate-x-0.5 transition-transform"></i>
            </a>
          </div>

        </div>
      </div>
    </section>

    <!-- 02 Skilling Solutions (CONTENT LEFT, IMAGE RIGHT) -->
    <section class="py-14 sm:py-18 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-14 items-center">
          
          <!-- Content Left (5 cols on lg) -->
          <div class="lg:col-span-5 order-2 lg:order-1 flex items-center justify-between gap-4">
            <div class="space-y-3">
              <div class="flex items-center gap-3">
                <span class="text-xs font-mono font-bold text-[#B08D57] dark:text-[#D6A84F]">02</span>
                <span class="w-10 h-0.5 bg-[#B08D57] dark:bg-[#D6A84F] inline-block"></span>
              </div>
              <h2 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-[var(--text-white-head)] tracking-tight">
                Skilling Solutions
              </h2>
            </div>
            <a href="offerings.html#skilling-solutions" onclick="routePage(event, 'offerings.html', 'skilling-solutions')" class="w-12 h-12 sm:w-14 sm:h-14 rounded-full border border-[#B08D57] dark:border-[#D6A84F] text-[#B08D57] dark:text-[#D6A84F] hover:bg-[#B08D57] hover:text-white dark:hover:bg-[#D6A84F] dark:hover:text-[#18202A] flex items-center justify-center transition-all duration-300 shadow-sm shrink-0 group" aria-label="Open Skilling Solutions Details">
              <i data-lucide="arrow-right" class="w-5 h-5 sm:w-6 sm:h-6 group-hover:translate-x-0.5 transition-transform"></i>
            </a>
          </div>

          <!-- Image Right (7 cols on lg) -->
          <div class="lg:col-span-7 order-1 lg:order-2">
            <div class="rounded-xl overflow-hidden shadow-sm border border-[var(--border-white)] bg-slate-100 dark:bg-[#202428] cursor-pointer group" onclick="routePage(event, 'offerings.html', 'skilling-solutions')">
              <img 
                src="assets/offering_skilling_classroom.jpg" 
                alt="Skilling Solutions Corporate Training" 
                class="w-full h-64 sm:h-80 lg:h-[350px] object-cover group-hover:scale-102 transition-transform duration-500"
              >
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- 03 Cambridge Learning & Global Certifications (IMAGE LEFT, CONTENT RIGHT) -->
    <section class="py-14 sm:py-18 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-14 items-center">
          
          <!-- Image Left (7 cols on lg) -->
          <div class="lg:col-span-7">
            <div class="rounded-xl overflow-hidden shadow-sm border border-[var(--border-white)] bg-slate-100 dark:bg-[#202428] cursor-pointer group" onclick="routePage(event, 'offerings.html', 'cambridge-learning')">
              <img 
                src="assets/offering_cambridge_certifications.jpg" 
                alt="Cambridge Learning and Global Certifications" 
                class="w-full h-64 sm:h-80 lg:h-[350px] object-cover group-hover:scale-102 transition-transform duration-500"
              >
            </div>
          </div>

          <!-- Content Right (5 cols on lg) -->
          <div class="lg:col-span-5 flex items-center justify-between gap-4">
            <div class="space-y-3">
              <div class="flex items-center gap-3">
                <span class="text-xs font-mono font-bold text-[#B08D57] dark:text-[#D6A84F]">03</span>
                <span class="w-10 h-0.5 bg-[#B08D57] dark:bg-[#D6A84F] inline-block"></span>
              </div>
              <h2 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-[var(--text-white-head)] tracking-tight leading-[1.15]">
                Cambridge Learning<br>&amp; Global Certifications
              </h2>
            </div>
            <a href="offerings.html#cambridge-learning" onclick="routePage(event, 'offerings.html', 'cambridge-learning')" class="w-12 h-12 sm:w-14 sm:h-14 rounded-full border border-[#B08D57] dark:border-[#D6A84F] text-[#B08D57] dark:text-[#D6A84F] hover:bg-[#B08D57] hover:text-white dark:hover:bg-[#D6A84F] dark:hover:text-[#18202A] flex items-center justify-center transition-all duration-300 shadow-sm shrink-0 group" aria-label="Open Cambridge Learning & Global Certifications Details">
              <i data-lucide="arrow-right" class="w-5 h-5 sm:w-6 sm:h-6 group-hover:translate-x-0.5 transition-transform"></i>
            </a>
          </div>

        </div>
      </div>
    </section>

    <!-- 04 ISC2 Credentials (CONTENT LEFT, IMAGE RIGHT) -->
    <section class="py-14 sm:py-18 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-14 items-center">
          
          <!-- Content Left (5 cols on lg) -->
          <div class="lg:col-span-5 order-2 lg:order-1 flex items-center justify-between gap-4">
            <div class="space-y-3">
              <div class="flex items-center gap-3">
                <span class="text-xs font-mono font-bold text-[#B08D57] dark:text-[#D6A84F]">04</span>
                <span class="w-10 h-0.5 bg-[#B08D57] dark:bg-[#D6A84F] inline-block"></span>
              </div>
              <h2 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-[var(--text-white-head)] tracking-tight">
                ISC2 Credentials
              </h2>
            </div>
            <a href="offerings.html#isc2" onclick="routePage(event, 'offerings.html', 'isc2')" class="w-12 h-12 sm:w-14 sm:h-14 rounded-full border border-[#B08D57] dark:border-[#D6A84F] text-[#B08D57] dark:text-[#D6A84F] hover:bg-[#B08D57] hover:text-white dark:hover:bg-[#D6A84F] dark:hover:text-[#18202A] flex items-center justify-center transition-all duration-300 shadow-sm shrink-0 group" aria-label="Open ISC2 Credentials Details">
              <i data-lucide="arrow-right" class="w-5 h-5 sm:w-6 sm:h-6 group-hover:translate-x-0.5 transition-transform"></i>
            </a>
          </div>

          <!-- Image Right (7 cols on lg) -->
          <div class="lg:col-span-7 order-1 lg:order-2">
            <div class="rounded-xl overflow-hidden shadow-sm border border-[var(--border-white)] bg-slate-100 dark:bg-[#202428] cursor-pointer group" onclick="routePage(event, 'offerings.html', 'isc2')">
              <img 
                src="assets/offering_isc2_credentials.jpg" 
                alt="ISC2 Professional Cybersecurity Credentials" 
                class="w-full h-64 sm:h-80 lg:h-[350px] object-cover group-hover:scale-102 transition-transform duration-500"
              >
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- 05 EC-Council (ATC) (IMAGE LEFT, CONTENT RIGHT) -->
    <section class="py-14 sm:py-18 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-14 items-center">
          
          <!-- Image Left (7 cols on lg) -->
          <div class="lg:col-span-7">
            <div class="rounded-xl overflow-hidden shadow-sm border border-[var(--border-white)] bg-slate-100 dark:bg-[#202428] cursor-pointer group" onclick="routePage(event, 'offerings.html', 'ec-council')">
              <img 
                src="assets/offering_eccouncil_atc.jpg" 
                alt="EC-Council Authorised Training Centre Lab" 
                class="w-full h-64 sm:h-80 lg:h-[350px] object-cover group-hover:scale-102 transition-transform duration-500"
              >
            </div>
          </div>

          <!-- Content Right (5 cols on lg) -->
          <div class="lg:col-span-5 flex items-center justify-between gap-4">
            <div class="space-y-3">
              <div class="flex items-center gap-3">
                <span class="text-xs font-mono font-bold text-[#B08D57] dark:text-[#D6A84F]">05</span>
                <span class="w-10 h-0.5 bg-[#B08D57] dark:bg-[#D6A84F] inline-block"></span>
              </div>
              <h2 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-[var(--text-white-head)] tracking-tight">
                EC-Council (ATC)
              </h2>
            </div>
            <a href="offerings.html#ec-council" onclick="routePage(event, 'offerings.html', 'ec-council')" class="w-12 h-12 sm:w-14 sm:h-14 rounded-full border border-[#B08D57] dark:border-[#D6A84F] text-[#B08D57] dark:text-[#D6A84F] hover:bg-[#B08D57] hover:text-white dark:hover:bg-[#D6A84F] dark:hover:text-[#18202A] flex items-center justify-center transition-all duration-300 shadow-sm shrink-0 group" aria-label="Open EC-Council (ATC) Details">
              <i data-lucide="arrow-right" class="w-5 h-5 sm:w-6 sm:h-6 group-hover:translate-x-0.5 transition-transform"></i>
            </a>
          </div>

        </div>
      </div>
    </section>

    <!-- 06 IT Services (8 Pillars) (CONTENT LEFT, IMAGE RIGHT) -->
    <section class="py-14 sm:py-18 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-14 items-center">
          
          <!-- Content Left (5 cols on lg) -->
          <div class="lg:col-span-5 order-2 lg:order-1 flex items-center justify-between gap-4">
            <div class="space-y-3">
              <div class="flex items-center gap-3">
                <span class="text-xs font-mono font-bold text-[#B08D57] dark:text-[#D6A84F]">06</span>
                <span class="w-10 h-0.5 bg-[#B08D57] dark:bg-[#D6A84F] inline-block"></span>
              </div>
              <h2 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-[var(--text-white-head)] tracking-tight">
                IT Services (8 Pillars)
              </h2>
            </div>
            <a href="offerings.html#it-services" onclick="routePage(event, 'offerings.html', 'it-services')" class="w-12 h-12 sm:w-14 sm:h-14 rounded-full border border-[#B08D57] dark:border-[#D6A84F] text-[#B08D57] dark:text-[#D6A84F] hover:bg-[#B08D57] hover:text-white dark:hover:bg-[#D6A84F] dark:hover:text-[#18202A] flex items-center justify-center transition-all duration-300 shadow-sm shrink-0 group" aria-label="Open IT Services (8 Pillars) Details">
              <i data-lucide="arrow-right" class="w-5 h-5 sm:w-6 sm:h-6 group-hover:translate-x-0.5 transition-transform"></i>
            </a>
          </div>

          <!-- Image Right (7 cols on lg) -->
          <div class="lg:col-span-7 order-1 lg:order-2">
            <div class="rounded-xl overflow-hidden shadow-sm border border-[var(--border-white)] bg-slate-100 dark:bg-[#202428] cursor-pointer group" onclick="routePage(event, 'offerings.html', 'it-services')">
              <img 
                src="assets/offering_it_datacenter.jpg" 
                alt="IT Services 8 Strategic Pillars Data Center" 
                class="w-full h-64 sm:h-80 lg:h-[350px] object-cover group-hover:scale-102 transition-transform duration-500"
              >
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- 3. CTA SECTION (MATCHING REFERENCE EXACTLY) -->
    <section class="py-14 sm:py-16 bg-[#F9F9F8] dark:bg-[#181C20] border-t border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-6">
        <div class="space-y-2 text-center md:text-left">
          <div class="flex items-center justify-center md:justify-start gap-2">
            <span class="w-8 h-0.5 bg-[#B08D57] dark:bg-[#D6A84F] inline-block"></span>
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">READY TO MOVE FORWARD?</span>
          </div>
          <h2 class="font-serif text-2xl sm:text-3xl lg:text-4xl font-bold text-[var(--text-white-head)] tracking-tight">
            Let’s Build a Safer, Smarter Tomorrow
          </h2>
        </div>
        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-sm shadow-md transition inline-flex items-center gap-2 shrink-0">
          <span>Enquire Now</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </section>

  </main>'''

# 2. DETAIL VIEWS WITH ZERO PREVIOUS/NEXT, CLEAN BACK TO ALL OFFERINGS, AND CTA
detail_views_html = '''
  <!-- ==================== DETAIL VIEW 1: SOC-AS-A-SERVICE ==================== -->
  <main id="view-soc" class="page-view flex-1 bg-white dark:bg-[#111315]">
    <!-- Breadcrumb Area -->
    <div class="white-section border-b border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
        <nav class="flex items-center gap-2 text-xs font-medium text-[var(--text-white-body)]" aria-label="Breadcrumb">
          <a href="index.html" onclick="routePage(event, 'index.html')" class="hover:text-[var(--text-white-head)] transition">Home</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="hover:text-[var(--text-white-head)] transition">Our Offerings</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <span class="text-[#D6A84F] font-semibold">SOC-As-A-Service</span>
        </nav>
      </div>
    </div>

    <section id="soc-as-a-service" class="charcoal-section bg-[#181C20] text-white py-12 sm:py-16 border-b border-[#2C3136]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        
        <!-- Header Row -->
        <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-2">
          <div class="space-y-2 max-w-2xl">
            <div class="flex items-center gap-2">
              <span class="w-6 h-0.5 bg-[#D6A84F] inline-block"></span>
              <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#D6A84F]">01 &bull; DEFENSIVE OPERATIONS</span>
            </div>
            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold font-display text-white tracking-tight">
              SOC-As-A-Service
            </h1>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed pt-1">
              Delivering continuous security operations, threat detection, and defensive posture management through six core capabilities.
            </p>
          </div>

          <div class="inline-flex items-center gap-2.5 px-4 py-2 rounded-full bg-[#202428] border border-[#3A4046] text-xs font-mono text-slate-300 shadow-sm shrink-0 self-start lg:self-end">
            <i data-lucide="shield-check" class="w-4 h-4 text-[#D6A84F]"></i>
            <span>Monitor &bull; Detect &bull; Respond &bull; Stay Ahead</span>
          </div>
        </div>

        <!-- Two-Column Layout -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
          <div class="lg:col-span-5 flex flex-col">
            <div class="relative rounded-3xl overflow-hidden shadow-2xl border border-[#3A4046] bg-[#202428] h-full min-h-[340px] sm:min-h-[400px] flex-1 group">
              <img 
                src="assets/soc_operations_center.jpg" 
                alt="SLN Consulting Enterprise Security Operations Center" 
                class="w-full h-full object-cover group-hover:scale-102 transition-transform duration-500"
              >
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-5 sm:p-6">
                <div class="bg-[#181C20]/90 backdrop-blur-xs px-4 py-2 rounded-xl border border-white/10 text-white flex items-center gap-2.5">
                  <span class="w-4 h-0.5 bg-[#D6A84F] inline-block"></span>
                  <div>
                    <span class="text-[9px] font-mono text-[#D6A84F] uppercase tracking-wider block font-bold">PROACTIVE SECURITY</span>
                    <span class="text-[11px] font-medium text-slate-200">FOR A STRONGER TOMORROW</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Six Capability Cards -->
          <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-4">
            
            <div onclick="openDrawer('soc-technical')" class="p-5 rounded-2xl bg-[#202428] border border-[#34383D] hover:border-[#D6A84F]/50 shadow-lg cursor-pointer group transition-all duration-200 hover:-translate-y-0.5 flex items-center justify-between gap-4">
              <div class="flex items-center gap-3.5">
                <div class="w-10 h-10 rounded-xl bg-[#282D32] border border-[#3A4046] flex items-center justify-center text-[#D6A84F] group-hover:scale-105 transition-transform shrink-0">
                  <i data-lucide="shield-check" class="w-5 h-5"></i>
                </div>
                <div>
                  <h3 class="font-display font-bold text-xs sm:text-sm text-white group-hover:text-[#D6A84F] transition-colors leading-snug">Managed Detection &amp; Response</h3>
                </div>
              </div>
              <div class="w-8 h-8 rounded-full bg-[#282D32] border border-[#3A4046] flex items-center justify-center text-[#D6A84F] group-hover:bg-[#D6A84F] group-hover:text-[#111315] group-hover:translate-x-1 transition-all shrink-0">
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </div>
            </div>

            <div onclick="openDrawer('soc-technical')" class="p-5 rounded-2xl bg-[#202428] border border-[#34383D] hover:border-[#D6A84F]/50 shadow-lg cursor-pointer group transition-all duration-200 hover:-translate-y-0.5 flex items-center justify-between gap-4">
              <div class="flex items-center gap-3.5">
                <div class="w-10 h-10 rounded-xl bg-[#282D32] border border-[#3A4046] flex items-center justify-center text-[#D6A84F] group-hover:scale-105 transition-transform shrink-0">
                  <i data-lucide="bar-chart-2" class="w-5 h-5"></i>
                </div>
                <div>
                  <h3 class="font-display font-bold text-xs sm:text-sm text-white group-hover:text-[#D6A84F] transition-colors leading-snug">SIEM &amp; Log Management</h3>
                </div>
              </div>
              <div class="w-8 h-8 rounded-full bg-[#282D32] border border-[#3A4046] flex items-center justify-center text-[#D6A84F] group-hover:bg-[#D6A84F] group-hover:text-[#111315] group-hover:translate-x-1 transition-all shrink-0">
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </div>
            </div>

            <div onclick="openDrawer('soc-technical')" class="p-5 rounded-2xl bg-[#202428] border border-[#34383D] hover:border-[#D6A84F]/50 shadow-lg cursor-pointer group transition-all duration-200 hover:-translate-y-0.5 flex items-center justify-between gap-4">
              <div class="flex items-center gap-3.5">
                <div class="w-10 h-10 rounded-xl bg-[#282D32] border border-[#3A4046] flex items-center justify-center text-[#D6A84F] group-hover:scale-105 transition-transform shrink-0">
                  <i data-lucide="network" class="w-5 h-5"></i>
                </div>
                <div>
                  <h3 class="font-display font-bold text-xs sm:text-sm text-white group-hover:text-[#D6A84F] transition-colors leading-snug">Threat Intelligence</h3>
                </div>
              </div>
              <div class="w-8 h-8 rounded-full bg-[#282D32] border border-[#3A4046] flex items-center justify-center text-[#D6A84F] group-hover:bg-[#D6A84F] group-hover:text-[#111315] group-hover:translate-x-1 transition-all shrink-0">
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </div>
            </div>

            <div onclick="openDrawer('soc-technical')" class="p-5 rounded-2xl bg-[#202428] border border-[#34383D] hover:border-[#D6A84F]/50 shadow-lg cursor-pointer group transition-all duration-200 hover:-translate-y-0.5 flex items-center justify-between gap-4">
              <div class="flex items-center gap-3.5">
                <div class="w-10 h-10 rounded-xl bg-[#282D32] border border-[#3A4046] flex items-center justify-center text-[#D6A84F] group-hover:scale-105 transition-transform shrink-0">
                  <i data-lucide="file-search" class="w-5 h-5"></i>
                </div>
                <div>
                  <h3 class="font-display font-bold text-xs sm:text-sm text-white group-hover:text-[#D6A84F] transition-colors leading-snug">Incident Response &amp; Forensics</h3>
                </div>
              </div>
              <div class="w-8 h-8 rounded-full bg-[#282D32] border border-[#3A4046] flex items-center justify-center text-[#D6A84F] group-hover:bg-[#D6A84F] group-hover:text-[#111315] group-hover:translate-x-1 transition-all shrink-0">
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </div>
            </div>

            <div onclick="openDrawer('soc-technical')" class="p-5 rounded-2xl bg-[#202428] border border-[#34383D] hover:border-[#D6A84F]/50 shadow-lg cursor-pointer group transition-all duration-200 hover:-translate-y-0.5 flex items-center justify-between gap-4">
              <div class="flex items-center gap-3.5">
                <div class="w-10 h-10 rounded-xl bg-[#282D32] border border-[#3A4046] flex items-center justify-center text-[#D6A84F] group-hover:scale-105 transition-transform shrink-0">
                  <i data-lucide="clipboard-check" class="w-5 h-5"></i>
                </div>
                <div>
                  <h3 class="font-display font-bold text-xs sm:text-sm text-white group-hover:text-[#D6A84F] transition-colors leading-snug">VAPT &amp; Security Testing</h3>
                </div>
              </div>
              <div class="w-8 h-8 rounded-full bg-[#282D32] border border-[#3A4046] flex items-center justify-center text-[#D6A84F] group-hover:bg-[#D6A84F] group-hover:text-[#111315] group-hover:translate-x-1 transition-all shrink-0">
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </div>
            </div>

            <div onclick="openDrawer('soc-technical')" class="p-5 rounded-2xl bg-[#202428] border border-[#34383D] hover:border-[#D6A84F]/50 shadow-lg cursor-pointer group transition-all duration-200 hover:-translate-y-0.5 flex items-center justify-between gap-4">
              <div class="flex items-center gap-3.5">
                <div class="w-10 h-10 rounded-xl bg-[#282D32] border border-[#3A4046] flex items-center justify-center text-[#D6A84F] group-hover:scale-105 transition-transform shrink-0">
                  <i data-lucide="crosshair" class="w-5 h-5"></i>
                </div>
                <div>
                  <h3 class="font-display font-bold text-xs sm:text-sm text-white group-hover:text-[#D6A84F] transition-colors leading-snug">Red Teaming &amp; Threat Hunting</h3>
                </div>
              </div>
              <div class="w-8 h-8 rounded-full bg-[#282D32] border border-[#3A4046] flex items-center justify-center text-[#D6A84F] group-hover:bg-[#D6A84F] group-hover:text-[#111315] group-hover:translate-x-1 transition-all shrink-0">
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- Bottom Navigation: Back to All Offerings -->
    <div class="py-8 border-t border-[var(--border-white)] dark:border-[#2C3136] bg-slate-50/50 dark:bg-[#15181B]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-center">
        <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="inline-flex items-center gap-2.5 px-6 py-3 rounded-xl bg-white dark:bg-[#202428] hover:bg-slate-100 dark:hover:bg-[#282D32] border border-[var(--border-white)] dark:border-[#3A4046] text-[#B08D57] dark:text-[#D6A84F] font-semibold text-xs tracking-wider uppercase transition shadow-xs group">
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
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">READY TO MOVE FORWARD?</span>
          </div>
          <h2 class="font-serif text-2xl sm:text-3xl lg:text-4xl font-bold text-[var(--text-white-head)] tracking-tight">
            Let’s Build a Safer, Smarter Tomorrow
          </h2>
        </div>
        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-sm shadow-md transition inline-flex items-center gap-2 shrink-0">
          <span>Enquire Now</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </section>
  </main>

  <!-- ==================== DETAIL VIEW 2: SKILLING SOLUTIONS ==================== -->
  <main id="view-skilling" class="page-view flex-1 bg-white dark:bg-[#111315]">
    <!-- Breadcrumb Area -->
    <div class="white-section border-b border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
        <nav class="flex items-center gap-2 text-xs font-medium text-[var(--text-white-body)]" aria-label="Breadcrumb">
          <a href="index.html" onclick="routePage(event, 'index.html')" class="hover:text-[var(--text-white-head)] transition">Home</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="hover:text-[var(--text-white-head)] transition">Our Offerings</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <span class="text-[#D6A84F] font-semibold">Skilling Solutions</span>
        </nav>
      </div>
    </div>

    <section id="skilling-solutions" class="white-section py-18 sm:py-24 border-b border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-center">
          <div class="lg:col-span-6 order-1 lg:order-2">
            <div class="rounded-2xl overflow-hidden shadow-subtle border border-[var(--border-white)]">
              <img src="assets/offering_skilling_classroom.jpg" alt="Workforce &amp; Academic Skilling" class="w-full h-80 object-cover">
            </div>
          </div>
          <div class="lg:col-span-6 order-2 lg:order-1 space-y-4">
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">02 &bull; TALENT ENABLEMENT</span>
            <h2 class="font-display font-bold text-2xl sm:text-3xl text-[var(--text-white-head)]">Skilling Solutions</h2>
            <p class="text-xs sm:text-sm text-[var(--text-white-body)] leading-relaxed">
              Bridging enterprise technical excellence and university career readiness across two specialized divisions:
            </p>
            <div class="space-y-3 pt-1 text-xs text-[var(--text-white-body)]">
              <div class="p-3.5 rounded-xl border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]">
                <strong class="text-[var(--text-white-head)] block mb-0.5">Corporate Learning</strong>
                Workforce upskilling across Cybersecurity, Cloud, Network, AI &amp; ML, and Executive Leadership.
              </div>
              <div class="p-3.5 rounded-xl border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]">
                <strong class="text-[var(--text-white-head)] block mb-0.5">Academic Campus Programs</strong>
                SME webinars, student hackathons, corporate induction, career mapping, and faculty TTT workshops.
              </div>
            </div>
            <div class="pt-2 flex flex-wrap gap-3">
              <button onclick="openDrawer('corporate-workshops')" class="px-4 py-2 rounded-xl border border-[var(--border-white)] bg-white dark:bg-[#24282C] text-xs font-semibold hover:border-[#202428] transition">Corporate Workshops &rarr;</button>
              <button onclick="openDrawer('campus-workshops')" class="px-4 py-2 rounded-xl border border-[var(--border-white)] bg-white dark:bg-[#24282C] text-xs font-semibold hover:border-[#202428] transition">Campus Programs &rarr;</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Subsidiary Highlight: CYBERNXTGEN -->
    <section class="charcoal-section py-16 sm:py-20 border-b border-[#3A4046]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          <div class="lg:col-span-8 space-y-3">
            <span class="text-[10px] font-mono font-bold uppercase tracking-widest text-[#D6A84F]">SLN ECOSYSTEM SUBSIDIARY</span>
            <h3 class="font-display font-bold text-2xl sm:text-3xl text-white">CYBERNXTGEN</h3>
            <span class="text-xs font-mono text-[#D6A84F] block font-semibold">Cybersecurity Skilling &bull; Upskilling &bull; Reskilling</span>
            <p class="text-xs sm:text-sm text-[#C9CDD2] leading-relaxed max-w-2xl">
              CYBERNXTGEN is a subsidiary of SLN Consulting focused specifically on skilling, upskilling, and reskilling the global workforce in cybersecurity. Designed to bridge the global security talent shortage with hands-on, job-ready capabilities.
            </p>
          </div>
          <div class="lg:col-span-4 flex justify-start lg:justify-end">
            <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-6 py-3 rounded-xl bg-[#282D32] hover:bg-[#343A40] text-white font-semibold text-xs border border-[#3A4046] shadow-sm transition">
              Inquire About Cyber Programs
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Bottom Navigation: Back to All Offerings -->
    <div class="py-8 border-t border-[var(--border-white)] dark:border-[#2C3136] bg-slate-50/50 dark:bg-[#15181B]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-center">
        <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="inline-flex items-center gap-2.5 px-6 py-3 rounded-xl bg-white dark:bg-[#202428] hover:bg-slate-100 dark:hover:bg-[#282D32] border border-[var(--border-white)] dark:border-[#3A4046] text-[#B08D57] dark:text-[#D6A84F] font-semibold text-xs tracking-wider uppercase transition shadow-xs group">
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
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">READY TO MOVE FORWARD?</span>
          </div>
          <h2 class="font-serif text-2xl sm:text-3xl lg:text-4xl font-bold text-[var(--text-white-head)] tracking-tight">
            Let’s Build a Safer, Smarter Tomorrow
          </h2>
        </div>
        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-sm shadow-md transition inline-flex items-center gap-2 shrink-0">
          <span>Enquire Now</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </section>
  </main>

  <!-- ==================== DETAIL VIEW 3: CAMBRIDGE LEARNING & GLOBAL CERTIFICATIONS (CAMBRIDGE ONLY) ==================== -->
  <main id="view-cambridge" class="page-view flex-1 bg-white dark:bg-[#111315]">
    <!-- Breadcrumb Area -->
    <div class="white-section border-b border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
        <nav class="flex items-center gap-2 text-xs font-medium text-[var(--text-white-body)]" aria-label="Breadcrumb">
          <a href="index.html" onclick="routePage(event, 'index.html')" class="hover:text-[var(--text-white-head)] transition">Home</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="hover:text-[var(--text-white-head)] transition">Our Offerings</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <span class="text-[#D6A84F] font-semibold">Cambridge Learning &amp; Global Certifications</span>
        </nav>
      </div>
    </div>

    <section id="cambridge-learning" class="charcoal-section py-18 sm:py-24 border-b border-[#3A4046]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-center">
          <div class="lg:col-span-6">
            <div class="rounded-2xl overflow-hidden border border-[#3A4046] shadow-xl">
              <img src="assets/offering_cambridge_certifications.jpg" alt="Cambridge Learning Assessment" class="w-full h-80 object-cover">
            </div>
          </div>
          <div class="lg:col-span-6 space-y-4">
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#D6A84F]">03 &bull; GLOBAL COMMUNICATION</span>
            <h2 class="font-display font-bold text-2xl sm:text-3xl text-white">Cambridge Learning &amp; Global Certifications</h2>
            <p class="text-xs sm:text-sm text-[#C9CDD2] leading-relaxed">
              Assessment and language competency solutions delivered through SLN's relationship as Authorised Distributor for <strong>Cambridge University Press &amp; Assessment</strong>.
            </p>
            <div class="grid grid-cols-2 gap-2 text-xs text-white pt-1">
              <div class="p-2.5 rounded-lg charcoal-card border border-[#3A4046]">English for Academic Ability</div>
              <div class="p-2.5 rounded-lg charcoal-card border border-[#3A4046]">English as a Skill</div>
              <div class="p-2.5 rounded-lg charcoal-card border border-[#3A4046]">English for Employability</div>
              <div class="p-2.5 rounded-lg charcoal-card border border-[#3A4046]">English for International Mobility</div>
            </div>
            <div class="pt-2">
              <button onclick="openDrawer('cambridge')" class="px-5 py-2.5 rounded-xl bg-[#282D32] hover:bg-[#343A40] text-white text-xs font-semibold border border-[#3A4046] shadow-sm transition inline-flex items-center gap-2">
                <span>View CEFR Objectives</span>
                <i data-lucide="sliders" class="w-3.5 h-3.5 text-[#D6A84F]"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Bottom Navigation: Back to All Offerings -->
    <div class="py-8 border-t border-[var(--border-white)] dark:border-[#2C3136] bg-slate-50/50 dark:bg-[#15181B]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-center">
        <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="inline-flex items-center gap-2.5 px-6 py-3 rounded-xl bg-white dark:bg-[#202428] hover:bg-slate-100 dark:hover:bg-[#282D32] border border-[var(--border-white)] dark:border-[#3A4046] text-[#B08D57] dark:text-[#D6A84F] font-semibold text-xs tracking-wider uppercase transition shadow-xs group">
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
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">READY TO MOVE FORWARD?</span>
          </div>
          <h2 class="font-serif text-2xl sm:text-3xl lg:text-4xl font-bold text-[var(--text-white-head)] tracking-tight">
            Let’s Build a Safer, Smarter Tomorrow
          </h2>
        </div>
        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-sm shadow-md transition inline-flex items-center gap-2 shrink-0">
          <span>Enquire Now</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </section>
  </main>

  <!-- ==================== DETAIL VIEW 4: ISC2 CREDENTIALS (DEDICATED ISC2 ONLY) ==================== -->
  <main id="view-isc2" class="page-view flex-1 bg-white dark:bg-[#111315]">
    <!-- Breadcrumb Area -->
    <div class="white-section border-b border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
        <nav class="flex items-center gap-2 text-xs font-medium text-[var(--text-white-body)]" aria-label="Breadcrumb">
          <a href="index.html" onclick="routePage(event, 'index.html')" class="hover:text-[var(--text-white-head)] transition">Home</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="hover:text-[var(--text-white-head)] transition">Our Offerings</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <span class="text-[#D6A84F] font-semibold">ISC2 Credentials</span>
        </nav>
      </div>
    </div>

    <section id="isc2" class="white-section py-18 sm:py-24 border-b border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-center">
          <div class="lg:col-span-6 order-1 lg:order-2">
            <div class="rounded-2xl overflow-hidden shadow-subtle border border-[var(--border-white)]">
              <img src="assets/offering_isc2_credentials.jpg" alt="ISC2 Professional Cybersecurity Lab" class="w-full h-80 object-cover">
            </div>
          </div>
          <div class="lg:col-span-6 order-2 lg:order-1 space-y-4">
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">04 &bull; (ISC)&sup2; CREDENTIAL TRACKS</span>
            <h2 class="font-display font-bold text-2xl sm:text-3xl text-[var(--text-white-head)]">ISC2 Credentials</h2>
            <p class="text-xs sm:text-sm text-[var(--text-white-body)] leading-relaxed">
              Authorized candidate training and preparation as an Official Training Partner of (ISC)&sup2;:
            </p>
            <div class="grid grid-cols-2 gap-2 text-xs pt-1">
              <div class="p-3 rounded-lg border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]">
                <strong class="text-[var(--text-white-head)] block">CC</strong>
                <span class="text-[var(--text-white-body)] text-[11px]">Certified in Cybersecurity</span>
              </div>
              <div class="p-3 rounded-lg border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]">
                <strong class="text-[var(--text-white-head)] block">CCSP</strong>
                <span class="text-[var(--text-white-body)] text-[11px]">Cloud Security Professional</span>
              </div>
              <div class="p-3 rounded-lg border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]">
                <strong class="text-[var(--text-white-head)] block">CSSLP</strong>
                <span class="text-[var(--text-white-body)] text-[11px]">Secure Software Lifecycle</span>
              </div>
              <div class="p-3 rounded-lg border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]">
                <strong class="text-[var(--text-white-head)] block">CISSP</strong>
                <span class="text-[var(--text-white-body)] text-[11px]">Information Systems Security</span>
              </div>
            </div>
            <div class="pt-2">
              <button onclick="openDrawer('certs')" class="px-5 py-2.5 rounded-xl bg-[#202428] hover:bg-[#282D32] dark:bg-[#24282C] dark:hover:bg-[#2D3237] text-white text-xs font-semibold shadow-sm transition inline-flex items-center gap-2 border border-[#3A4046]">
                <span>View Credential Specifications</span>
                <i data-lucide="sliders" class="w-3.5 h-3.5 text-[#D6A84F]"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Bottom Navigation: Back to All Offerings -->
    <div class="py-8 border-t border-[var(--border-white)] dark:border-[#2C3136] bg-slate-50/50 dark:bg-[#15181B]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-center">
        <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="inline-flex items-center gap-2.5 px-6 py-3 rounded-xl bg-white dark:bg-[#202428] hover:bg-slate-100 dark:hover:bg-[#282D32] border border-[var(--border-white)] dark:border-[#3A4046] text-[#B08D57] dark:text-[#D6A84F] font-semibold text-xs tracking-wider uppercase transition shadow-xs group">
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
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">READY TO MOVE FORWARD?</span>
          </div>
          <h2 class="font-serif text-2xl sm:text-3xl lg:text-4xl font-bold text-[var(--text-white-head)] tracking-tight">
            Let’s Build a Safer, Smarter Tomorrow
          </h2>
        </div>
        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-sm shadow-md transition inline-flex items-center gap-2 shrink-0">
          <span>Enquire Now</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </section>
  </main>

  <!-- ==================== DETAIL VIEW 5: EC-COUNCIL (ATC) (DEDICATED EC-COUNCIL ONLY) ==================== -->
  <main id="view-ec-council" class="page-view flex-1 bg-white dark:bg-[#111315]">
    <!-- Breadcrumb Area -->
    <div class="white-section border-b border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
        <nav class="flex items-center gap-2 text-xs font-medium text-[var(--text-white-body)]" aria-label="Breadcrumb">
          <a href="index.html" onclick="routePage(event, 'index.html')" class="hover:text-[var(--text-white-head)] transition">Home</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="hover:text-[var(--text-white-head)] transition">Our Offerings</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <span class="text-[#D6A84F] font-semibold">EC-Council (ATC)</span>
        </nav>
      </div>
    </div>

    <section id="ec-council" class="charcoal-section py-18 sm:py-24 border-b border-[#3A4046]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-center">
          <div class="lg:col-span-6">
            <div class="rounded-2xl overflow-hidden border border-[#3A4046] shadow-xl">
              <img src="assets/offering_eccouncil_atc.jpg" alt="EC Council Ethical Hacking Training" class="w-full h-80 object-cover">
            </div>
          </div>
          <div class="lg:col-span-6 space-y-4">
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#D6A84F]">05 &bull; EC-COUNCIL ACCREDITATION</span>
            <h2 class="font-display font-bold text-2xl sm:text-3xl text-white">EC-COUNCIL (ATC)</h2>
            <p class="text-xs sm:text-sm text-[#C9CDD2] leading-relaxed">
              Official training and lab preparation delivered through SLN Consulting's Authorised Training Centre (ATC) relationship with EC-Council across 8 programs:
            </p>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs pt-1">
              <div class="p-2.5 rounded-lg charcoal-card border border-[#3A4046]"><strong class="text-white block">CEH</strong><span class="text-[10px] text-[#C9CDD2]">Ethical Hacker</span></div>
              <div class="p-2.5 rounded-lg charcoal-card border border-[#3A4046]"><strong class="text-white block">CND</strong><span class="text-[10px] text-[#C9CDD2]">Defender</span></div>
              <div class="p-2.5 rounded-lg charcoal-card border border-[#3A4046]"><strong class="text-white block">CHFI</strong><span class="text-[10px] text-[#C9CDD2]">Forensics</span></div>
              <div class="p-2.5 rounded-lg charcoal-card border border-[#3A4046]"><strong class="text-white block">CPENT</strong><span class="text-[10px] text-[#C9CDD2]">Pen Test</span></div>
              <div class="p-2.5 rounded-lg charcoal-card border border-[#3A4046]"><strong class="text-white block">CASE</strong><span class="text-[10px] text-[#C9CDD2]">App Sec</span></div>
              <div class="p-2.5 rounded-lg charcoal-card border border-[#3A4046]"><strong class="text-white block">CCSE</strong><span class="text-[10px] text-[#C9CDD2]">Cloud Sec</span></div>
              <div class="p-2.5 rounded-lg charcoal-card border border-[#3A4046]"><strong class="text-white block">CTIA</strong><span class="text-[10px] text-[#C9CDD2]">Threat Intel</span></div>
              <div class="p-2.5 rounded-lg charcoal-card border border-[#3A4046]"><strong class="text-white block">CSA</strong><span class="text-[10px] text-[#C9CDD2]">SOC Analyst</span></div>
            </div>
            <div class="pt-2">
              <button onclick="openDrawer('certs')" class="px-5 py-2.5 rounded-xl bg-[#282D32] hover:bg-[#343A40] text-white text-xs font-semibold border border-[#3A4046] shadow-sm transition inline-flex items-center gap-2">
                <span>View EC-Council Specs</span>
                <i data-lucide="sliders" class="w-3.5 h-3.5 text-[#D6A84F]"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Bottom Navigation: Back to All Offerings -->
    <div class="py-8 border-t border-[var(--border-white)] dark:border-[#2C3136] bg-slate-50/50 dark:bg-[#15181B]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-center">
        <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="inline-flex items-center gap-2.5 px-6 py-3 rounded-xl bg-white dark:bg-[#202428] hover:bg-slate-100 dark:hover:bg-[#282D32] border border-[var(--border-white)] dark:border-[#3A4046] text-[#B08D57] dark:text-[#D6A84F] font-semibold text-xs tracking-wider uppercase transition shadow-xs group">
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
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">READY TO MOVE FORWARD?</span>
          </div>
          <h2 class="font-serif text-2xl sm:text-3xl lg:text-4xl font-bold text-[var(--text-white-head)] tracking-tight">
            Let’s Build a Safer, Smarter Tomorrow
          </h2>
        </div>
        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-sm shadow-md transition inline-flex items-center gap-2 shrink-0">
          <span>Enquire Now</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </section>
  </main>

  <!-- ==================== DETAIL VIEW 6: IT SERVICES (8 PILLARS) ==================== -->
  <main id="view-it-services" class="page-view flex-1 bg-white dark:bg-[#111315]">
    <!-- Breadcrumb Area -->
    <div class="white-section border-b border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
        <nav class="flex items-center gap-2 text-xs font-medium text-[var(--text-white-body)]" aria-label="Breadcrumb">
          <a href="index.html" onclick="routePage(event, 'index.html')" class="hover:text-[var(--text-white-head)] transition">Home</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="hover:text-[var(--text-white-head)] transition">Our Offerings</a>
          <span class="text-slate-400 dark:text-slate-600">&rsaquo;</span>
          <span class="text-[#D6A84F] font-semibold">IT Services (8 Pillars)</span>
        </nav>
      </div>
    </div>

    <section id="it-services" class="white-section py-18 sm:py-24 border-b border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-center">
          <div class="lg:col-span-6 order-1 lg:order-2">
            <div class="rounded-2xl overflow-hidden shadow-subtle border border-[var(--border-white)]">
              <img src="assets/offering_it_datacenter.jpg" alt="Enterprise IT Architecture" class="w-full h-80 object-cover">
            </div>
          </div>
          <div class="lg:col-span-6 order-2 lg:order-1 space-y-4">
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">06 &bull; ENTERPRISE IT ENABLEMENT</span>
            <h2 class="font-display font-bold text-2xl sm:text-3xl text-[var(--text-white-head)]">IT Services</h2>
            <p class="text-xs sm:text-sm text-[var(--text-white-body)] leading-relaxed">
              Eight strategic IT pillars supporting organizations with infrastructure, development, testing, and operational requirements:
            </p>
            <div class="grid grid-cols-2 gap-2 text-xs text-[var(--text-white-body)] pt-1">
              <div class="p-2.5 rounded-lg border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]"><strong class="text-[var(--text-white-head)] block">1. Website Creation</strong>Hosting, SSL &amp; UI/UX</div>
              <div class="p-2.5 rounded-lg border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]"><strong class="text-[var(--text-white-head)] block">2. App Development</strong>Mobile &amp; Web Platforms</div>
              <div class="p-2.5 rounded-lg border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]"><strong class="text-[var(--text-white-head)] block">3. Facility Management</strong>I-FMS &amp; Data Center Ops</div>
              <div class="p-2.5 rounded-lg border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]"><strong class="text-[var(--text-white-head)] block">4. Cloud Computing</strong>IaaS, PaaS, SaaS</div>
              <div class="p-2.5 rounded-lg border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]"><strong class="text-[var(--text-white-head)] block">5. Network Solutions</strong>Firewalls &amp; IDS/IPS</div>
              <div class="p-2.5 rounded-lg border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]"><strong class="text-[var(--text-white-head)] block">6. Cyber Consulting</strong>Policy &amp; Compliance</div>
              <div class="p-2.5 rounded-lg border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]"><strong class="text-[var(--text-white-head)] block">7. App Testing</strong>Functional &amp; CI/CD QA</div>
              <div class="p-2.5 rounded-lg border border-[var(--border-white)] bg-white dark:bg-[#1B1E21]"><strong class="text-[var(--text-white-head)] block">8. Resource Planning</strong>Allocation &amp; Cost Control</div>
            </div>
            <div class="pt-2">
              <button onclick="openDrawer('tech-services')" class="px-5 py-2.5 rounded-xl bg-[#202428] hover:bg-[#282D32] dark:bg-[#24282C] dark:hover:bg-[#2D3237] text-white text-xs font-semibold shadow-sm transition inline-flex items-center gap-2 border border-[#3A4046]">
                <span>View Full IT Specifications</span>
                <i data-lucide="sliders" class="w-3.5 h-3.5 text-[#D6A84F]"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Bottom Navigation: Back to All Offerings -->
    <div class="py-8 border-t border-[var(--border-white)] dark:border-[#2C3136] bg-slate-50/50 dark:bg-[#15181B]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-center">
        <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="inline-flex items-center gap-2.5 px-6 py-3 rounded-xl bg-white dark:bg-[#202428] hover:bg-slate-100 dark:hover:bg-[#282D32] border border-[var(--border-white)] dark:border-[#3A4046] text-[#B08D57] dark:text-[#D6A84F] font-semibold text-xs tracking-wider uppercase transition shadow-xs group">
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
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">READY TO MOVE FORWARD?</span>
          </div>
          <h2 class="font-serif text-2xl sm:text-3xl lg:text-4xl font-bold text-[var(--text-white-head)] tracking-tight">
            Let’s Build a Safer, Smarter Tomorrow
          </h2>
        </div>
        <a href="contact.html" onclick="routePage(event, 'contact.html')" class="px-8 py-3.5 rounded-full bg-[#D6A84F] hover:bg-[#C2943F] text-[#18202A] font-bold text-sm shadow-md transition inline-flex items-center gap-2 shrink-0">
          <span>Enquire Now</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </section>
  </main>'''

full_offerings_block = showcase_html + "\n\n" + detail_views_html

# Replace from VIEW 3 to VIEW 4 in offerings.html
pattern = r'(  <!-- ==================== VIEW 3: MAIN OUR OFFERINGS SHOWCASE[\s\S]*?)(  <!-- ==================== VIEW 4: TRAINING)'
if not re.search(pattern, html):
    # Try finding with <main id="view-offerings"
    pattern = r'(  <!-- ==================== VIEW 3:.*?)(  <!-- ==================== VIEW 4: TRAINING)'

new_html = re.sub(pattern, full_offerings_block + "\n\n\\2", html)

# 3. UPDATE ROUTER MAP AND ROUTER LOGIC
new_router = '''    // Comprehensive Route Mapping supporting files, clean URLs, and direct service anchors
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
      'training.html': 'view-training',
      'training': 'view-training',
      'contact.html': 'view-contact',
      'contact': 'view-contact',
      'contact-us': 'view-contact',
      'soc-as-a-service': 'view-soc',
      'soc': 'view-soc',
      'skilling-solutions': 'view-skilling',
      'skilling': 'view-skilling',
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
      if (e && e.preventDefault) {
        e.preventDefault();
      }

      // Normalize route aliases
      if (pageName === 'our-offerings' || pageName === 'offerings') pageName = 'offerings.html';
      if (pageName === 'about-us' || pageName === 'about') pageName = 'about.html';
      if (pageName === 'contact-us' || pageName === 'contact') pageName = 'contact.html';
      if (pageName === 'training') pageName = 'training.html';
      if (pageName === '' || pageName === 'index' || pageName === '/') pageName = 'index.html';

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
          btn.className = 'nav-btn text-sm font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all flex items-center gap-1.5 py-1 focus:outline-none';
        } else {
          btn.className = 'nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1.5 py-1 focus:outline-none';
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

      window.scrollTo({ top: 0, behavior: 'smooth' });

      if (window.lucide) {
        lucide.createIcons();
      }
    }'''

router_pattern = r'    // Comprehensive Route Mapping supporting files[\s\S]*?window\.scrollTo\(\{ top: 0, behavior: \'smooth\' \}\;\s*if \(window\.lucide\) \{\s*lucide\.createIcons\(\)\;\s*\}\s*\}'
new_html = re.sub(router_pattern, new_router, new_html)

with open('c:/Agen/SLN counsulting/offerings.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("offerings.html updated successfully with 6 offerings & independent detail pages!")
