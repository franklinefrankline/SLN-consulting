import os
import re

files = ['campus.html', 'index.html', 'about.html', 'offerings.html', 'training.html', 'contact.html', 'enterprises.html']

old_campus_section = '''    <!-- The 6 Campus Offerings Grid -->
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
    </section>'''

new_campus_section = '''    <!-- The 6 Campus Offerings Grid -->
    <section class="charcoal-section py-16 sm:py-20 border-b border-[#3A4046]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-12">
          <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#D6A84F]">CAMPUS SOLUTIONS</span>
          <h2 class="font-display font-bold text-2xl sm:text-3xl text-white mt-2">Defining Career Path</h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- 1 -->
          <div class="p-6 rounded-2xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex flex-col justify-between group">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-4">
                <i data-lucide="video" class="w-5 h-5"></i>
              </div>
              <h3 class="font-display font-bold text-base text-white">1. Seminars / Webinars Through Industry SMEs</h3>
            </div>
          </div>

          <!-- 2 -->
          <div class="p-6 rounded-2xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex flex-col justify-between group">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-4">
                <i data-lucide="code" class="w-5 h-5"></i>
              </div>
              <h3 class="font-display font-bold text-base text-white">2. Hackathon Events</h3>
            </div>
          </div>

          <!-- 3 -->
          <div class="p-6 rounded-2xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex flex-col justify-between group">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-4">
                <i data-lucide="briefcase" class="w-5 h-5"></i>
              </div>
              <h3 class="font-display font-bold text-base text-white">3. Preparing Students For Corporate World</h3>
            </div>
          </div>

          <!-- 4 -->
          <div class="p-6 rounded-2xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex flex-col justify-between group">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-4">
                <i data-lucide="award" class="w-5 h-5"></i>
              </div>
              <h3 class="font-display font-bold text-base text-white">4. Induction Training</h3>
            </div>
          </div>

          <!-- 5 -->
          <div class="p-6 rounded-2xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex flex-col justify-between group">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-4">
                <i data-lucide="message-square" class="w-5 h-5"></i>
              </div>
              <h3 class="font-display font-bold text-base text-white">5. Soft Skills Training</h3>
            </div>
          </div>

          <!-- 6 -->
          <div class="p-6 rounded-2xl bg-[#181C20] border border-[#34383D] hover:border-[#D6A84F]/50 transition-all flex flex-col justify-between group">
            <div>
              <div class="w-12 h-12 rounded-xl bg-[#D6A84F]/10 border border-[#D6A84F]/30 text-[#D6A84F] flex items-center justify-center mb-4">
                <i data-lucide="users" class="w-5 h-5"></i>
              </div>
              <h3 class="font-display font-bold text-base text-white">6. Faculty Training And Updation (TTT)</h3>
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
    </section>'''

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    if old_campus_section in c:
        c = c.replace(old_campus_section, new_campus_section)
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated campus section in {fn}")
    else:
        # Try regex replacement if whitespace differed
        pattern = r'<!-- The 6 Campus Offerings Grid -->[\s\S]*?</section>'
        # Only replace the one inside view-campus
        # Let's find view-campus
        pos = c.find('id="view-campus"')
        if pos != -1:
            end_pos = c.find('<!-- Bottom Navigation: Back to All Offerings -->', pos)
            if end_pos != -1:
                section_part = c[pos:end_pos]
                # Replace the offerings grid within section_part
                subbed_part = re.sub(
                    r'<!-- The 6 Campus Offerings Grid -->[\s\S]*?</section>',
                    new_campus_section,
                    section_part
                )
                c = c[:pos] + subbed_part + c[end_pos:]
                with open(fn, 'w', encoding='utf-8') as f:
                    f.write(c)
                print(f"Updated campus section via regex in {fn}")

print("Campus update complete!")
