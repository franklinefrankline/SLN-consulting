import re
import os

files = ['enterprises.html', 'index.html', 'about.html', 'offerings.html', 'training.html', 'contact.html', 'campus.html']

old_freshers_grid_pattern = r'<!-- SECTION 3: WORKSHOP IN CYBER SECURITY FOR FRESHERS -->[\s\S]*?</section>'

new_freshers_grid = '''    <!-- SECTION 3: WORKSHOP IN CYBER SECURITY FOR FRESHERS -->
    <section id="workshops-freshers" class="charcoal-section py-16 sm:py-20 border-b border-[#3A4046]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl mb-10">
          <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#D6A84F]">ENTRY-LEVEL ONBOARDING</span>
          <h2 class="font-display font-bold text-2xl sm:text-3xl text-white mt-2">
            WORKSHOP IN CYBER SECURITY FOR FRESHERS
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div class="p-4 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-1.5 shrink-0"></span>
            <h3 class="font-display font-bold text-sm text-white">Cybersecurity awareness - essentials workshop</h3>
          </div>
          <div class="p-4 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-1.5 shrink-0"></span>
            <h3 class="font-display font-bold text-sm text-white">Security monitoring &amp; management</h3>
          </div>
          <div class="p-4 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-1.5 shrink-0"></span>
            <h3 class="font-display font-bold text-sm text-white">Network security concepts &amp; methodologies</h3>
          </div>
          <div class="p-4 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-1.5 shrink-0"></span>
            <h3 class="font-display font-bold text-sm text-white">Essential tools for cyber investigation</h3>
          </div>
          <div class="p-4 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-1.5 shrink-0"></span>
            <h3 class="font-display font-bold text-sm text-white">Incident response principal tactics</h3>
          </div>
          <div class="p-4 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-1.5 shrink-0"></span>
            <h3 class="font-display font-bold text-sm text-white">Cyber crisis management</h3>
          </div>
          <div class="p-4 rounded-xl border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-1.5 shrink-0"></span>
            <h3 class="font-display font-bold text-sm text-white">Ethical hacking &amp; penetration testing principles</h3>
          </div>
          <div class="p-4 rounded-xl border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-1.5 shrink-0"></span>
            <h3 class="font-display font-bold text-sm text-white">Secure software development a basic introduction</h3>
          </div>
          <div class="p-4 rounded-xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex items-start gap-3">
            <span class="w-2 h-2 rounded-full bg-[#B08D57] dark:bg-[#D6A84F] mt-1.5 shrink-0"></span>
            <h3 class="font-display font-bold text-sm text-white">Overview of cyber basics</h3>
          </div>
        </div>
      </div>
    </section>'''

# Also remove explanatory paragraph under SECTION 2 heading
old_managers_header = '''        <div class="max-w-3xl mb-10">
          <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">EXECUTIVE &amp; MANAGEMENT MODULES</span>
          <h2 class="font-display font-bold text-2xl sm:text-3xl text-[var(--text-white-head)] mt-2">
            WORKSHOPS &amp; WEBINARS FOR MID &amp; SENIOR MANAGERS
          </h2>
          <p class="text-xs sm:text-sm text-[var(--text-white-body)] mt-2">
            Targeted briefings and tactical sessions designed to address modern cyber threat landscapes, technology shifts, and corporate resilience.
          </p>
        </div>'''

new_managers_header = '''        <div class="max-w-3xl mb-10">
          <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#B08D57] dark:text-[#D6A84F]">EXECUTIVE &amp; MANAGEMENT MODULES</span>
          <h2 class="font-display font-bold text-2xl sm:text-3xl text-[var(--text-white-head)] mt-2">
            WORKSHOPS &amp; WEBINARS FOR MID &amp; SENIOR MANAGERS
          </h2>
        </div>'''

# Also remove explanatory paragraph in Training header if present
old_training_header = '''        <div class="text-center max-w-3xl mx-auto mb-12">
          <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#D6A84F]">CORE PILLARS</span>
          <h2 class="font-display font-bold text-2xl sm:text-3xl text-white mt-2">Training</h2>
          <p class="text-xs sm:text-sm text-[#C9CDD2] mt-2">Specialized capability tracks delivered by certified industry practitioners.</p>
        </div>'''

new_training_header = '''        <div class="text-center max-w-3xl mx-auto mb-12">
          <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#D6A84F]">CORE PILLARS</span>
          <h2 class="font-display font-bold text-2xl sm:text-3xl text-white mt-2">Training</h2>
        </div>'''

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace freshers section inside view-enterprises
    pos_ent = c.find('id="view-enterprises"')
    if pos_ent != -1:
        end_ent = c.find('</main>', pos_ent)
        if end_ent != -1:
            ent_part = c[pos_ent:end_ent]

            # Replace managers header
            if old_managers_header in ent_part:
                ent_part = ent_part.replace(old_managers_header, new_managers_header)
            
            # Replace training header
            if old_training_header in ent_part:
                ent_part = ent_part.replace(old_training_header, new_training_header)

            # Replace freshers section
            ent_part = re.sub(old_freshers_grid_pattern, new_freshers_grid, ent_part)

            c = c[:pos_ent] + ent_part + c[end_ent:]
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Updated view-enterprises in {fn}")

print("Simplification of Enterprises page complete!")
