import re
import os

calendar_section_html = '''    <!-- ==================== TRAINING CALENDAR TABLE SECTION ==================== -->
    <section id="training-calendar" class="white-section py-16 sm:py-20 border-b border-[var(--border-white)] dark:border-[#2C3136]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Section Header -->
        <div class="text-center max-w-3xl mx-auto mb-10">
          <div class="inline-flex items-center gap-2 mb-2">
            <span class="w-6 h-0.5 bg-[#B08D57] dark:bg-[#D6A84F] inline-block"></span>
            <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">SCHEDULE &amp; BATCHES</span>
            <span class="w-6 h-0.5 bg-[#B08D57] dark:bg-[#D6A84F] inline-block"></span>
          </div>
          <h2 class="text-3xl sm:text-4xl font-extrabold font-display text-[var(--text-white-head)] tracking-tight">
            Training Calendar
          </h2>
          <p class="text-xs sm:text-sm text-[var(--text-white-body)] mt-2 max-w-xl mx-auto">
            Official upcoming certification batches, scheduled dates, and authorized enrollment details.
          </p>
        </div>

        <!-- Responsive Table Container -->
        <div class="rounded-2xl border border-[var(--border-white)] dark:border-[#34383D] bg-white dark:bg-[#181C20] shadow-xl overflow-hidden">
          <div class="overflow-x-auto custom-scrollbar">
            <table class="w-full text-left border-collapse min-w-[900px]">
              <thead>
                <tr class="bg-slate-50 dark:bg-[#14171A] border-b border-[var(--border-white)] dark:border-[#2C3136] text-[11px] font-mono uppercase font-bold text-slate-600 dark:text-slate-300 tracking-wider">
                  <th scope="col" class="py-4 px-5">Month</th>
                  <th scope="col" class="py-4 px-4 text-center">S.No.</th>
                  <th scope="col" class="py-4 px-6 min-w-[280px]">Certification</th>
                  <th scope="col" class="py-4 px-4 text-center">OEM</th>
                  <th scope="col" class="py-4 px-5">Date from</th>
                  <th scope="col" class="py-4 px-5">Date to</th>
                  <th scope="col" class="py-4 px-5">Timing</th>
                  <th scope="col" class="py-4 px-5">Mode</th>
                  <th scope="col" class="py-4 px-6 min-w-[240px]">For Registration</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-[var(--border-white)] dark:divide-[#24282D] text-xs sm:text-sm text-[var(--text-white-body)]">
                <!-- Row 1: CISSP -->
                <tr class="hover:bg-slate-50/75 dark:hover:bg-[#1E2227] transition-colors">
                  <!-- Month -->
                  <td class="py-5 px-5 font-semibold text-[var(--text-white-head)] whitespace-nowrap">
                    Nov 2024
                  </td>

                  <!-- S.No. -->
                  <td class="py-5 px-4 font-mono font-bold text-[#B08D57] dark:text-[#D6A84F] text-center">
                    1
                  </td>

                  <!-- Certification -->
                  <td class="py-5 px-6 font-semibold text-[var(--text-white-head)] leading-snug">
                    Certified Information Systems Security Professional (CISSP)
                  </td>

                  <!-- OEM -->
                  <td class="py-5 px-4 text-center">
                    <span class="inline-block px-2.5 py-1 rounded-md bg-[#B08D57]/10 dark:bg-[#D6A84F]/10 border border-[#B08D57]/30 dark:border-[#D6A84F]/30 text-[#B08D57] dark:text-[#D6A84F] font-mono font-bold text-xs">
                      ISC2
                    </span>
                  </td>

                  <!-- Date from -->
                  <td class="py-5 px-5 font-mono text-xs text-slate-700 dark:text-slate-300 whitespace-nowrap">
                    25-11-2024
                  </td>

                  <!-- Date to -->
                  <td class="py-5 px-5 font-mono text-xs text-slate-700 dark:text-slate-300 whitespace-nowrap">
                    29-11-2024
                  </td>

                  <!-- Timing -->
                  <td class="py-5 px-5 font-mono text-xs text-slate-700 dark:text-slate-300 whitespace-nowrap">
                    9 am–5 pm
                  </td>

                  <!-- Mode -->
                  <td class="py-5 px-5 whitespace-nowrap">
                    <div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 font-semibold text-xs border border-emerald-500/20">
                      <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                      <span>Live Online</span>
                    </div>
                  </td>

                  <!-- For Registration -->
                  <td class="py-5 px-6">
                    <a href="contact.html" onclick="routePage(event, 'contact.html')" class="group/reg inline-flex items-center gap-1.5 text-xs font-semibold text-[#B08D57] dark:text-[#D6A84F] hover:underline" title="Register with SLN Consulting">
                      <span>SLN Consulting Solution For Seamless Growth</span>
                      <i data-lucide="arrow-right" class="w-3.5 h-3.5 transition-transform group-hover/reg:translate-x-0.5"></i>
                    </a>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Table Note / Advisory Strip -->
        <div class="mt-6 flex flex-col sm:flex-row items-center justify-between gap-4 p-4 rounded-xl bg-slate-50 dark:bg-[#181C20] border border-[var(--border-white)] dark:border-[#2C3136] text-xs text-slate-500 dark:text-slate-400">
          <div class="flex items-center gap-2">
            <i data-lucide="calendar" class="w-4 h-4 text-[#D6A84F] shrink-0"></i>
            <span>Need a custom corporate batch or academic schedule? We offer on-demand instructor-led dates.</span>
          </div>
          <a href="contact.html" onclick="routePage(event, 'contact.html')" class="font-bold text-[#B08D57] dark:text-[#D6A84F] hover:underline shrink-0">
            Request Custom Dates &rarr;
          </a>
        </div>

      </div>
    </section>
'''

files = ['training.html', 'index.html', 'about.html', 'offerings.html', 'contact.html', 'enterprises.html', 'campus.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # Find view-training
    pos_tr = c.find('id="view-training"')
    if pos_tr != -1:
        end_tr = c.find('</main>', pos_tr)
        if end_tr != -1:
            tr_part = c[pos_tr:end_tr]

            # Remove existing calendar section if any
            tr_part = re.sub(r'<!-- ==================== TRAINING CALENDAR TABLE SECTION ==================== -->[\s\S]*?</section>', '', tr_part)

            # Insert right after the hero section: <!-- ==================== TRAINING CATEGORIES
            if '<!-- ==================== TRAINING CATEGORIES' in tr_part:
                tr_part = tr_part.replace(
                    '<!-- ==================== TRAINING CATEGORIES',
                    calendar_section_html + '\n    <!-- ==================== TRAINING CATEGORIES'
                )
            else:
                # Insert before closing CTA
                cta_marker = '<!-- ==================== CTA SECTION'
                if cta_marker in tr_part:
                    tr_part = tr_part.replace(cta_marker, calendar_section_html + '\n    ' + cta_marker)
                else:
                    tr_part = tr_part + '\n' + calendar_section_html

            c = c[:pos_tr] + tr_part + c[end_tr:]

    # Add training-schedule routes in routeMap
    if "'training-schedule.html': 'view-training'" not in c:
        c = c.replace(
            "'training.html': 'view-training',",
            "'training.html': 'view-training',\n      'training-schedule.html': 'view-training',\n      'training-schedule': 'view-training',\n      'training_schedule.php': 'view-training',\n      'training_schedule': 'view-training',"
        )

    # In popstate and DOMContentLoaded:
    if "path === 'training-schedule.html'" not in c:
        c = c.replace(
            "if (path === 'training') path = 'training.html';",
            "if (path === 'training' || path === 'training-schedule' || path === 'training_schedule' || path === 'training-schedule.html' || path === 'training_schedule.php') path = 'training.html';"
        )

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated Training Calendar in {fn}")

# Also create dedicated training-schedule.html as an identical copy of training.html
with open('training.html', 'r', encoding='utf-8') as f:
    sched_content = f.read()

# Update title tag in training-schedule.html
sched_content = re.sub(r'<title>.*?</title>', '<title>Training Schedule & Calendar | SLN Consulting</title>', sched_content)

with open('training-schedule.html', 'w', encoding='utf-8') as f:
    f.write(sched_content)
print("Created training-schedule.html")

print("Training Calendar implementation complete!")
