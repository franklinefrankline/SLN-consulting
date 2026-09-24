import re

with open('offerings.html', 'r', encoding='utf-8') as f:
    orig_content = f.read()

# 1. Main Showcase View (Exact match to approved reference design)
main_showcase_view = '''  <!-- ==================== VIEW 3: MAIN OUR OFFERINGS SHOWCASE (offerings.html) ==================== -->
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

    <!-- 2. ALTERNATING OFFERINGS (NO GRID) -->
    
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

    <!-- 04 IT Services (8 Pillars) (CONTENT LEFT, IMAGE RIGHT) -->
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

# 2. Extract detail sections from orig_content
def extract_section(sec_id):
    pattern = rf'(<section id="{sec_id}"[\s\S]*?</section>)'
    sm = re.search(pattern, orig_content)
    return sm.group(1) if sm else ""

soc_sec = extract_section('soc-as-a-service')
skilling_sec = extract_section('skilling-solutions')
cambridge_sec = extract_section('cambridge-learning')
isc2_sec = extract_section('isc2')
eccouncil_sec = extract_section('ec-council')
it_sec = extract_section('it-services')

# Detail View 1: SOC-As-A-Service
detail_soc = f'''  <!-- ==================== DETAIL VIEW 1: SOC-AS-A-SERVICE ==================== -->
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

    {soc_sec}
  </main>'''

# Detail View 2: Skilling Solutions
detail_skilling = f'''  <!-- ==================== DETAIL VIEW 2: SKILLING SOLUTIONS ==================== -->
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

    {skilling_sec}

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

    <!-- Service Navigation Bar -->
    <div class="white-section py-8 border-b border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-semibold">
        <a href="offerings.html#soc-as-a-service" onclick="routePage(event, 'offerings.html', 'soc-as-a-service')" class="flex items-center gap-3 group text-[var(--text-white-body)] hover:text-[var(--text-white-head)] transition">
          <div class="w-9 h-9 rounded-full bg-slate-100 dark:bg-[#202428] border border-[var(--border-white)] flex items-center justify-center text-[#D6A84F] group-hover:border-[#D6A84F] transition-colors shrink-0">
            <i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-0.5 transition-transform"></i>
          </div>
          <div class="text-left">
            <span class="text-[10px] font-mono text-slate-400 block uppercase tracking-wider">PREVIOUS SERVICE</span>
            <span class="text-xs font-bold text-[var(--text-white-head)] group-hover:text-[#D6A84F] transition-colors">SOC-As-A-Service</span>
          </div>
        </a>

        <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-slate-100 dark:bg-[#202428] hover:bg-slate-200 dark:hover:bg-[#282D32] border border-[var(--border-white)] text-[#D6A84F] transition shadow-xs font-mono text-xs uppercase tracking-wider">
          <i data-lucide="layout-grid" class="w-4 h-4 text-[#D6A84F]"></i>
          <span>Back to All Offerings</span>
        </a>

        <a href="offerings.html#cambridge-learning" onclick="routePage(event, 'offerings.html', 'cambridge-learning')" class="flex items-center gap-3 group text-[var(--text-white-body)] hover:text-[var(--text-white-head)] transition">
          <div class="text-right">
            <span class="text-[10px] font-mono text-slate-400 block uppercase tracking-wider">NEXT SERVICE</span>
            <span class="text-xs font-bold text-[var(--text-white-head)] group-hover:text-[#D6A84F] transition-colors">Cambridge Learning</span>
          </div>
          <div class="w-9 h-9 rounded-full bg-slate-100 dark:bg-[#202428] border border-[var(--border-white)] flex items-center justify-center text-[#D6A84F] group-hover:border-[#D6A84F] transition-colors shrink-0">
            <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-0.5 transition-transform"></i>
          </div>
        </a>
      </div>
    </div>
  </main>'''

# Detail View 3: Cambridge Learning & Global Certifications
detail_cambridge = f'''  <!-- ==================== DETAIL VIEW 3: CAMBRIDGE LEARNING & GLOBAL CERTIFICATIONS ==================== -->
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

    {cambridge_sec}
    {eccouncil_sec}
    {isc2_sec}

    <!-- Service Navigation Bar -->
    <div class="white-section py-8 border-b border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-semibold">
        <a href="offerings.html#skilling-solutions" onclick="routePage(event, 'offerings.html', 'skilling-solutions')" class="flex items-center gap-3 group text-[var(--text-white-body)] hover:text-[var(--text-white-head)] transition">
          <div class="w-9 h-9 rounded-full bg-slate-100 dark:bg-[#202428] border border-[var(--border-white)] flex items-center justify-center text-[#D6A84F] group-hover:border-[#D6A84F] transition-colors shrink-0">
            <i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-0.5 transition-transform"></i>
          </div>
          <div class="text-left">
            <span class="text-[10px] font-mono text-slate-400 block uppercase tracking-wider">PREVIOUS SERVICE</span>
            <span class="text-xs font-bold text-[var(--text-white-head)] group-hover:text-[#D6A84F] transition-colors">Skilling Solutions</span>
          </div>
        </a>

        <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-slate-100 dark:bg-[#202428] hover:bg-slate-200 dark:hover:bg-[#282D32] border border-[var(--border-white)] text-[#D6A84F] transition shadow-xs font-mono text-xs uppercase tracking-wider">
          <i data-lucide="layout-grid" class="w-4 h-4 text-[#D6A84F]"></i>
          <span>Back to All Offerings</span>
        </a>

        <a href="offerings.html#it-services" onclick="routePage(event, 'offerings.html', 'it-services')" class="flex items-center gap-3 group text-[var(--text-white-body)] hover:text-[var(--text-white-head)] transition">
          <div class="text-right">
            <span class="text-[10px] font-mono text-slate-400 block uppercase tracking-wider">NEXT SERVICE</span>
            <span class="text-xs font-bold text-[var(--text-white-head)] group-hover:text-[#D6A84F] transition-colors">IT Services (8 Pillars)</span>
          </div>
          <div class="w-9 h-9 rounded-full bg-slate-100 dark:bg-[#202428] border border-[var(--border-white)] flex items-center justify-center text-[#D6A84F] group-hover:border-[#D6A84F] transition-colors shrink-0">
            <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-0.5 transition-transform"></i>
          </div>
        </a>
      </div>
    </div>
  </main>'''

# Detail View 4: IT Services (8 Pillars)
detail_it = f'''  <!-- ==================== DETAIL VIEW 4: IT SERVICES (8 PILLARS) ==================== -->
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

    {it_sec}

    <!-- Service Navigation Bar -->
    <div class="white-section py-8 border-b border-[var(--border-white)]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-semibold">
        <a href="offerings.html#cambridge-learning" onclick="routePage(event, 'offerings.html', 'cambridge-learning')" class="flex items-center gap-3 group text-[var(--text-white-body)] hover:text-[var(--text-white-head)] transition">
          <div class="w-9 h-9 rounded-full bg-slate-100 dark:bg-[#202428] border border-[var(--border-white)] flex items-center justify-center text-[#D6A84F] group-hover:border-[#D6A84F] transition-colors shrink-0">
            <i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-0.5 transition-transform"></i>
          </div>
          <div class="text-left">
            <span class="text-[10px] font-mono text-slate-400 block uppercase tracking-wider">PREVIOUS SERVICE</span>
            <span class="text-xs font-bold text-[var(--text-white-head)] group-hover:text-[#D6A84F] transition-colors">Cambridge Learning</span>
          </div>
        </a>

        <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-slate-100 dark:bg-[#202428] hover:bg-slate-200 dark:hover:bg-[#282D32] border border-[var(--border-white)] text-[#D6A84F] transition shadow-xs font-mono text-xs uppercase tracking-wider">
          <i data-lucide="layout-grid" class="w-4 h-4 text-[#D6A84F]"></i>
          <span>Back to All Offerings</span>
        </a>

        <a href="offerings.html#soc-as-a-service" onclick="routePage(event, 'offerings.html', 'soc-as-a-service')" class="flex items-center gap-3 group text-[var(--text-white-body)] hover:text-[var(--text-white-head)] transition">
          <div class="text-right">
            <span class="text-[10px] font-mono text-slate-400 block uppercase tracking-wider">NEXT SERVICE</span>
            <span class="text-xs font-bold text-[var(--text-white-head)] group-hover:text-[#D6A84F] transition-colors">SOC-As-A-Service</span>
          </div>
          <div class="w-9 h-9 rounded-full bg-slate-100 dark:bg-[#202428] border border-[var(--border-white)] flex items-center justify-center text-[#D6A84F] group-hover:border-[#D6A84F] transition-colors shrink-0">
            <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-0.5 transition-transform"></i>
          </div>
        </a>
      </div>
    </div>
  </main>'''

all_offerings_blocks = f"{main_showcase_view}\n\n{detail_soc}\n\n{detail_skilling}\n\n{detail_cambridge}\n\n{detail_it}"

# Replace existing view-offerings in orig_content
pattern_existing_view = r'<main id="view-offerings"[\s\S]*?</main>'
new_content = re.sub(pattern_existing_view, all_offerings_blocks, orig_content, count=1)

with open('offerings.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully updated offerings.html with main showcase and detail pages!")
