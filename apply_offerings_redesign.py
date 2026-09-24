import re

# Read current offerings.html
with open('offerings.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Google Fonts and Tailwind config for Playfair Display
font_link_old = r'<link href="https://fonts\.googleapis\.com/css2\?family=Outfit:wght@500;600;700;800&family=Plus\+Jakarta\+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">'
font_link_new = '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">'
content = re.sub(font_link_old, font_link_new, content)

tailwind_font_old = r'fontFamily:\s*\{\s*display:\s*\[\'"Outfit"\',\s*\'sans-serif\'\],\s*sans:\s*\[\'"Plus Jakarta Sans"\',\s*\'sans-serif\'\],\s*\}'
tailwind_font_new = '''fontFamily: {
            display: ['"Outfit"', 'sans-serif'],
            serif: ['"Playfair Display"', 'Georgia', 'serif'],
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
          }'''
content = re.sub(tailwind_font_old, tailwind_font_new, content)

# 2. Update Header Navigation: "Our Offerings" must NOT have a dropdown in header
# Replace desktop #servicesMenuRoot with direct link
nav_dropdown_pattern = r'<!-- Our Offerings Dropdown -->\s*<div class="relative" id="servicesMenuRoot">[\s\S]*?</div>\s*</div>'
desktop_direct_nav = '''<a href="offerings.html" onclick="routePage(event, 'offerings.html')" class="nav-btn text-sm font-semibold text-[#18202A] dark:text-[#D6A84F] border-b-2 border-[#18202A] dark:border-[#D6A84F] pb-1 transition-all" data-route="offerings.html">Our Offerings</a>'''
content = re.sub(nav_dropdown_pattern, desktop_direct_nav, content)

# Replace mobile offerings collapsible menu with direct link
mobile_offerings_pattern = r'<!-- Mobile Our Offerings with Collapsible Submenu -->\s*<div>[\s\S]*?</div>\s*</div>'
mobile_direct_nav = '''<a href="offerings.html" onclick="routePage(event, 'offerings.html'); toggleMobileNav();" class="block w-full text-left text-sm font-semibold text-[var(--text-white-head)] py-1.5">Our Offerings</a>'''
content = re.sub(mobile_offerings_pattern, mobile_direct_nav, content)

print("Updated header and fonts.")
with open('offerings.html', 'w', encoding='utf-8') as f:
    f.write(content)
