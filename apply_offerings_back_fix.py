import re

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add IDs to 6 showcase sections in view-offerings
    card_replacements = [
        (
            r'<!-- 01 SOC-As-A-Service \(IMAGE LEFT, CONTENT RIGHT\) -->\s*<section class="py-14 sm:py-18 border-b border-\[var\(--border-white\)\] bg-white dark:bg-\[#111315\]">',
            '<!-- 01 SOC-As-A-Service (IMAGE LEFT, CONTENT RIGHT) -->\n    <section id="card-soc" class="py-14 sm:py-18 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">'
        ),
        (
            r'<!-- 02 Skilling Solutions \(CONTENT LEFT, IMAGE RIGHT\) -->\s*<section class="py-14 sm:py-18 border-b border-\[var\(--border-white\)\] bg-white dark:bg-\[#111315\]">',
            '<!-- 02 Skilling Solutions (CONTENT LEFT, IMAGE RIGHT) -->\n    <section id="card-skilling" class="py-14 sm:py-18 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">'
        ),
        (
            r'<!-- 03 Cambridge Learning & Global Certifications \(IMAGE LEFT, CONTENT RIGHT\) -->\s*<section class="py-14 sm:py-18 border-b border-\[var\(--border-white\)\] bg-white dark:bg-\[#111315\]">',
            '<!-- 03 Cambridge Learning & Global Certifications (IMAGE LEFT, CONTENT RIGHT) -->\n    <section id="card-cambridge" class="py-14 sm:py-18 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">'
        ),
        (
            r'<!-- 04 ISC2 Credentials \(CONTENT LEFT, IMAGE RIGHT\) -->\s*<section class="py-14 sm:py-18 border-b border-\[var\(--border-white\)\] bg-white dark:bg-\[#111315\]">',
            '<!-- 04 ISC2 Credentials (CONTENT LEFT, IMAGE RIGHT) -->\n    <section id="card-isc2" class="py-14 sm:py-18 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">'
        ),
        (
            r'<!-- 05 EC-Council \(ATC\) \(IMAGE LEFT, CONTENT RIGHT\) -->\s*<section class="py-14 sm:py-18 border-b border-\[var\(--border-white\)\] bg-white dark:bg-\[#111315\]">',
            '<!-- 05 EC-Council (ATC) (IMAGE LEFT, CONTENT RIGHT) -->\n    <section id="card-ec-council" class="py-14 sm:py-18 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">'
        ),
        (
            r'<!-- 06 IT Services \(8 Pillars\) \(CONTENT LEFT, IMAGE RIGHT\) -->\s*<section class="py-14 sm:py-18 border-b border-\[var\(--border-white\)\] bg-white dark:bg-\[#111315\]">',
            '<!-- 06 IT Services (8 Pillars) (CONTENT LEFT, IMAGE RIGHT) -->\n    <section id="card-it-services" class="py-14 sm:py-18 border-b border-[var(--border-white)] bg-white dark:bg-[#111315]">'
        ),
    ]

    for pat, rep in card_replacements:
        content = re.sub(pat, rep, content)

    # 2. Update arrow click handlers in view-offerings to openOfferingDetail
    arrow_replacements = [
        (
            r'onclick="routePage\(event,\s*\'offerings\.html\',\s*\'soc-as-a-service\'\)"',
            'onclick="openOfferingDetail(event, \'offerings.html\', \'soc-as-a-service\', \'card-soc\')"'
        ),
        (
            r'onclick="routePage\(event,\s*\'offerings\.html\',\s*\'skilling-solutions\'\)"',
            'onclick="openOfferingDetail(event, \'offerings.html\', \'skilling-solutions\', \'card-skilling\')"'
        ),
        (
            r'onclick="routePage\(event,\s*\'offerings\.html\',\s*\'cambridge-learning\'\)"',
            'onclick="openOfferingDetail(event, \'offerings.html\', \'cambridge-learning\', \'card-cambridge\')"'
        ),
        (
            r'onclick="routePage\(event,\s*\'offerings\.html\',\s*\'isc2\'\)"',
            'onclick="openOfferingDetail(event, \'offerings.html\', \'isc2\', \'card-isc2\')"'
        ),
        (
            r'onclick="routePage\(event,\s*\'offerings\.html\',\s*\'ec-council\'\)"',
            'onclick="openOfferingDetail(event, \'offerings.html\', \'ec-council\', \'card-ec-council\')"'
        ),
        (
            r'onclick="routePage\(event,\s*\'offerings\.html\',\s*\'it-services\'\)"',
            'onclick="openOfferingDetail(event, \'offerings.html\', \'it-services\', \'card-it-services\')"'
        ),
    ]

    for pat, rep in arrow_replacements:
        content = re.sub(pat, rep, content)

    # 3. Update Back to All Offerings buttons and breadcrumb links in each detail view
    detail_views_targets = [
        ('view-soc', 'card-soc', 'soc-as-a-service'),
        ('view-skilling', 'card-skilling', 'skilling-solutions'),
        ('view-cambridge', 'card-cambridge', 'cambridge-learning'),
        ('view-isc2', 'card-isc2', 'isc2'),
        ('view-ec-council', 'card-ec-council', 'ec-council'),
        ('view-it-services', 'card-it-services', 'it-services'),
    ]

    for view_id, card_id, anchor in detail_views_targets:
        # Find view boundaries
        v_start = content.find(f'id="{view_id}"')
        if v_start == -1:
            continue
        v_next = content.find('<main ', v_start + 10)
        if v_next == -1:
            v_next = content.find('<footer', v_start + 10)
        
        view_chunk = content[v_start:v_next]

        # In breadcrumb: replace <a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="hover:text-[var(--text-white-head)] transition">Our Offerings</a>
        # with onclick="backToOfferings(event, 'card_id')"
        view_chunk = re.sub(
            r'<a href="offerings\.html"\s+onclick="routePage\(event,\s*\'offerings\.html\'\)"\s+class="hover:text-\[var\(--text-white-head\)\] transition">Our Offerings</a>',
            f'<a href="offerings.html#{anchor}" onclick="backToOfferings(event, \'{card_id}\')" class="hover:text-[var(--text-white-head)] transition">Our Offerings</a>',
            view_chunk
        )

        # In Bottom Navigation: replace onclick="routePage(event, 'offerings.html')" with onclick="backToOfferings(event, 'card_id')"
        view_chunk = re.sub(
            r'(<!-- Bottom Navigation: Back to All Offerings -->[\s\S]*?<a href="offerings\.html)(?:#[^"]*)?("[\s\S]*?onclick=")(?:routePage|backToOfferings)\(event,\s*\'offerings\.html\'[^\)]*\)',
            rf'\g<1>#{anchor}\g<2>backToOfferings(event, \'{card_id}\')',
            view_chunk
        )

        content = content[:v_start] + view_chunk + content[v_next:]

    # 4. Insert or update openOfferingDetail and backToOfferings in script
    # Look for routePage definition
    if 'function backToOfferings' not in content:
        helper_code = '''    // Map detail anchors to offering card IDs on the main showcase
    const cardIdByAnchor = {
      'soc-as-a-service': 'card-soc',
      'soc': 'card-soc',
      'skilling-solutions': 'card-skilling',
      'skilling': 'card-skilling',
      'cambridge-learning': 'card-cambridge',
      'cambridge': 'card-cambridge',
      'isc2': 'card-isc2',
      'isc2-credentials': 'card-isc2',
      'ec-council': 'card-ec-council',
      'eccouncil': 'card-ec-council',
      'it-services': 'card-it-services'
    };

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
          btn.className = 'nav-btn text-sm font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all flex items-center gap-1.5 py-1 focus:outline-none';
        } else {
          btn.className = 'nav-btn text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-[#18202A] dark:hover:text-white border-b-2 border-transparent pb-1 transition-all flex items-center gap-1.5 py-1 focus:outline-none';
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

'''
        # Insert before routePage function
        content = content.replace('    // Client-side router function', helper_code + '    // Client-side router function')

    # Also update routePage to save scroll position when leaving view-offerings
    if 'currentOfferingsView.classList.contains(\'active\')' not in content:
        scroll_save_code = '''      // Auto-save scroll position when leaving view-offerings for a detail view
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

      // If anchorId maps to a detail view'''
        content = content.replace('      // If anchorId maps to a detail view', scroll_save_code)

    # In popstate listener, if popping to offerings.html with no anchor, restore scroll
    popstate_old = "if (path === '' || path === 'index') path = 'index.html';"
    popstate_new = """if (path === '' || path === 'index') path = 'index.html';
        if (path === 'offerings.html' && (!hash || hash === '')) {
          backToOfferings(null);
          return;
        }"""
    if 'backToOfferings(null)' not in content:
        content = content.replace(popstate_old, popstate_new)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename} successfully!")

files = ['offerings.html', 'index.html', 'about.html', 'training.html', 'contact.html']
for fn in files:
    update_file(fn)

print("All files updated with Back to All Offerings scroll restoration!")
