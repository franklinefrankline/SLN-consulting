import re

files = ['index.html', 'about.html', 'offerings.html', 'training.html', 'contact.html']

pattern = r'theme:\s*\{[\s\S]*?\}\s*\}\s*(?=\s*<\/script>)'

replacement = '''theme: {
        extend: {
          fontFamily: {
            display: ['"Outfit"', 'sans-serif'],
            serif: ['"Playfair Display"', 'Georgia', 'serif'],
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
          },
          boxShadow: {
            'subtle': '0 2px 14px -2px rgba(0, 0, 0, 0.08)',
            'drawer-depth': '-20px 0 50px rgba(0, 0, 0, 0.5)',
          }
        }
      }
    };'''

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(pattern, replacement, c)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Fixed {fn}")
