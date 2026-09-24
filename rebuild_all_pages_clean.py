# rebuild_all_pages_clean.py
import os
import re

workspace = os.path.abspath(os.path.dirname(__file__))
index_path = os.path.join(workspace, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    full_text = f.read()

# Get strictly the first complete HTML document
base_text = full_text[:224808]

# Locate router block
pos1 = base_text.find('const routeMap = {')
pos2 = base_text.find('// Off-Canvas Drawer Data (100% complete business details)')
assert pos1 != -1 and pos2 != -1, "Failed to locate router boundaries"

clean_router = '''const routeMap = {
      'index.html': 'view-index',
      'index': 'view-index',
      '': 'view-index',
      '/': 'view-index',
      'about.html': 'view-about',
      'about': 'view-about',
      'about-us': 'view-about',
      'training.html': 'view-training',
      'training-schedule.html': 'view-training',
      'training-schedule': 'view-training',
      'training_schedule.php': 'view-training',
      'training_schedule': 'view-training',
      'training': 'view-training',
      'contact.html': 'view-contact',
      'contact': 'view-contact',
      'contact-us': 'view-contact',
      'soc.html': 'view-soc',
      'soc': 'view-soc',
      'soc-as-a-service': 'view-soc',
      'enterprises.html': 'view-enterprises',
      'enterprises': 'view-enterprises',
      'enterprise': 'view-enterprises',
      'skilling-enterprises': 'view-enterprises',
      'campus.html': 'view-campus',
      'campus': 'view-campus',
      'skilling-campus': 'view-campus',
      'cambridge.html': 'view-cambridge',
      'cambridge': 'view-cambridge',
      'cambridge-learning': 'view-cambridge',
      'isc2.html': 'view-isc2',
      'isc2': 'view-isc2',
      'isc2-credentials': 'view-isc2',
      'ec-council.html': 'view-ec-council',
      'ec-council': 'view-ec-council',
      'eccouncil': 'view-ec-council',
      'it-services.html': 'view-it-services',
      'it-services': 'view-it-services',
      'it': 'view-it-services',
      'offerings.html': 'view-soc',
      'offerings': 'view-soc',
      'our-offering': 'view-soc',
      'our-offerings': 'view-soc'
    };

    // Client-side router function (Direct 1-Click Navigation)
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
      if (pageName === 'training' || pageName === 'training-schedule' || pageName === 'training_schedule' || pageName === 'training-schedule.html' || pageName === 'training_schedule.php') pageName = 'training.html';
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

        try {
          window.history.replaceState({ page: path, anchor: hash || null }, '', window.location.href);
        } catch (_) {}

        routePage(null, path, hash || null, false);
      } catch (_) {
        routePage(null, 'index.html', null, false);
      }
    });

    function closeAllDrawers() {
      const b = document.getElementById('capabilityDrawerBackdrop');
      const d = document.getElementById('capabilityDrawer');
      if (b) b.classList.add('hidden');
      if (d) d.classList.add('translate-x-full');
      document.body.style.overflow = '';
      closeOfferingsDropdown();
    }

    // Mobile nav toggle with background scroll lock
    function toggleMobileNav() {
      const m = document.getElementById('mobileDrawer');
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

    // Attach scroll isolator to key scrollable overlay elements on load
    window.addEventListener('DOMContentLoaded', () => {
      isolateScrollElement(document.getElementById('offeringsDropdownPanel'));
      isolateScrollElement(document.getElementById('drawerBody'));
      isolateScrollElement(document.getElementById('policyModalBody'));
      isolateScrollElement(document.getElementById('mobileDrawer'));
    });

    '''

clean_master_text = base_text[:pos1] + clean_router + base_text[pos2:]

# Save master index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(clean_master_text)
print("[SUCCESS] Master index.html saved (length:", len(clean_master_text), ")")

# Standalone pages configuration
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
    ('offerings.html', 'view-soc')
]

for filename, active_view in pages_config:
    file_path = os.path.join(workspace, filename)
    # Remove 'active' from all views
    content = re.sub(r'class="page-view active', 'class="page-view', clean_master_text)
    # Add 'active' to the target view
    content = content.replace(f'id="{active_view}" class="page-view', f'id="{active_view}" class="page-view active')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated clean standalone page: {filename} (active: {active_view})")

print("\nAll 13 clean pages rebuilt successfully!")
