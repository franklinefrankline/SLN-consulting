import os
import re
import glob
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def test_all():
    print("=" * 70)
    print("TESTING NEW NAVIGATION STRUCTURE & FOOTER ACROSS ALL PAGES")
    print("=" * 70)

    expected_files = {
        'index.html': 'view-index',
        'about.html': 'view-about',
        'soc.html': 'view-soc',
        'enterprises.html': 'view-enterprises',
        'campus.html': 'view-campus',
        'internships.html': 'view-internships',
        'cambridge.html': 'view-cambridge',
        'isc2.html': 'view-isc2',
        'ec-council.html': 'view-ec-council',
        'it-services.html': 'view-it-services',
        'training.html': 'view-training',
        'training-schedule.html': 'view-training',
        'contact.html': 'view-contact',
        'offerings.html': 'view-soc',
    }

    all_passed = True

    # 1. Test each file
    print("\n[CHECK 1: FILE EXISTENCE & ACTIVE VIEW INTEGRITY]")
    for fname, exp_view in expected_files.items():
        if not os.path.exists(fname):
            print(f"  ❌ Missing file: {fname}")
            all_passed = False
            continue

        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()

        active_matches = re.findall(r'<main[^>]+id="([^"]+)"[^>]*class="[^"]*active[^"]*"', content)
        if len(active_matches) == 1 and active_matches[0] == exp_view:
            print(f"  ✅ {fname:22} -> Correct single active view: #{exp_view}")
        else:
            print(f"  ❌ {fname:22} -> Expected #{exp_view}, found active: {active_matches}")
            all_passed = False

    # 2. Test Header items in index.html
    print("\n[CHECK 2: NEW HEADER STRUCTURE & DROPDOWN CONTENTS]")
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    header_m = re.search(r'<header[\s\S]*?<\/header>', html)
    assert header_m, "Header not found in index.html"
    header = header_m.group(0)

    req_nav_items = [
        'Home',
        'About Us',
        'Cybersecurity',
        'IT Services',
        'Academia',
        'Internships',
        'Training &amp; Certifications',
        'Corporate',
        'Resources',
        'Contact',
        'ENQUIRE NOW'
    ]

    for item in req_nav_items:
        clean_name = item.replace('&amp;', '&')
        if item in header or clean_name in header:
            print(f"  ✅ Header Nav Item present: '{clean_name}'")
        else:
            print(f"  ❌ Header Nav Item MISSING: '{clean_name}'")
            all_passed = False

    # Check Dropdown Contents
    dropdown_checks = [
        ("About Us", ["About SLN", "Our Leadership", "Why SLN?", "Partners & Accreditations", "Our Clients", "Success Stories"]),
        ("Cybersecurity", ["Offensive Security", "Vulnerability Assessment", "SOC-as-a-Service", "24×7 Security Monitoring", "Security Consulting", "AI & Emerging", "AI Security"]),
        ("IT Services", ["Website Development", "Application Development", "Cloud Solutions", "Network Solutions", "IT Infrastructure", "Application Testing", "IT Resource Management"]),
        ("Academia", ["Academic Partnerships", "Cybersecurity Workshops", "Faculty Development", "Student Skill Development", "Cybersecurity Curriculum", "Campus Cybersecurity", "Industry–Academia", "3-Month Cybersecurity Internship"]),
        ("Training & Certifications", ["Cybersecurity Training", "Corporate Training", "CISSP", "ISC2 Certifications", "EC-Council Certifications", "Cambridge Learning", "Professional Upskilling", "Customized Training"]),
        ("Corporate", ["Cybersecurity Consulting", "Corporate Training", "Employee Cybersecurity Awareness", "Security Assessments", "Managed Security Services", "Technology Solutions", "Enterprise Partnerships"]),
        ("Resources", ["Insights", "Events & Workshops", "Training Calendar", "Case Studies", "Gallery", "Downloads"]),
        ("Contact", ["Contact Us", "Enquire Now", "Partner With Us"])
    ]

    print("\n[CHECK 3: DROPDOWN CONTENTS VERIFICATION]")
    for section_name, items in dropdown_checks:
        missing = [it for it in items if it not in header and it.replace('&', '&amp;') not in header]
        if not missing:
            print(f"  ✅ Dropdown '{section_name}': All {len(items)} items verified.")
        else:
            print(f"  ❌ Dropdown '{section_name}': Missing items: {missing}")
            all_passed = False

    # Check Mobile Drawer
    print("\n[CHECK 4: MOBILE ACCORDION STRUCTURE]")
    drawer_m = re.search(r'id="mobileDrawer"[\s\S]*?<\/header>', html)
    assert drawer_m, "Mobile drawer not found"
    drawer = drawer_m.group(0)
    for m_item in ['HOME', 'ABOUT US', 'CYBERSECURITY', 'IT SERVICES', 'ACADEMIA', 'INTERNSHIPS', 'TRAINING &amp; CERTIFICATIONS', 'CORPORATE', 'RESOURCES', 'CONTACT', 'ENQUIRE NOW']:
        c_item = m_item.replace('&amp;', '&')
        if m_item in drawer or c_item in drawer:
            print(f"  ✅ Mobile Drawer item verified: '{c_item}'")
        else:
            print(f"  ❌ Mobile Drawer item MISSING: '{c_item}'")
            all_passed = False

    # Check Footer
    print("\n[CHECK 5: FOOTER SECTIONS (7-SECTION ENTERPRISE ARCHITECTURE)]")
    footer_m = re.search(r'<footer[\s\S]*?<\/footer>', html)
    assert footer_m, "Footer not found"
    footer = footer_m.group(0)

    footer_sections = [
        "COMPANY",
        "CYBERSECURITY",
        "IT &amp; CORPORATE",
        "ACADEMIA &amp; INTERNSHIPS",
        "TRAINING &amp; CERTIFICATIONS",
        "RESOURCES",
        "CONTACT"
    ]

    for fs in footer_sections:
        c_fs = fs.replace('&amp;', '&')
        if fs in footer or c_fs in footer:
            print(f"  ✅ Footer Section present: '{c_fs}'")
        else:
            print(f"  ❌ Footer Section MISSING: '{c_fs}'")
            all_passed = False

    # Check Footer Bottom Bar
    footer_legal = [
        "Privacy Policy",
        "Terms &amp; Conditions",
        "Cookie Policy",
        "Disclaimer",
        "2026 SLN Consulting"
    ]
    print("\n[CHECK 6: FOOTER LEGAL & BOTTOM BAR]")
    for fl in footer_legal:
        c_fl = fl.replace('&amp;', '&')
        if fl in footer or c_fl in footer:
            print(f"  ✅ Footer Legal link present: '{c_fl}'")
        else:
            print(f"  ❌ Footer Legal link MISSING: '{c_fl}'")
            all_passed = False

    # Check Internships View
    print("\n[CHECK 7: NEW INTERNSHIPS VIEW CONTENT]")
    int_view_m = re.search(r'<main id="view-internships"[\s\S]*?<\/main>', html)
    assert int_view_m, "view-internships not found in index.html"
    int_view = int_view_m.group(0)

    int_requirements = [
        "Cybersecurity Internship",
        "3-Month Industry Internship",
        "Hands-on Cybersecurity Tasks",
        "Internship Certificate",
        "Placement Preparation",
        "For 2027 Graduates",
        "Institutional Internship Program",
        "Apply / Enquire"
    ]

    for req in int_requirements:
        if req in int_view:
            print(f"  ✅ Internships requirement verified: '{req}'")
        else:
            print(f"  ❌ Internships requirement MISSING: '{req}'")
            all_passed = False

    # Check Images and Links
    print("\n[CHECK 8: OFFLINE ASSETS & IMAGES INTEGRITY]")
    all_imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    broken_imgs = [img for img in set(all_imgs) if not os.path.exists(img)]
    if not broken_imgs:
        print(f"  ✅ All {len(set(all_imgs))} referenced images exist locally on disk.")
    else:
        print(f"  ❌ Missing images: {broken_imgs}")
        all_passed = False

    print("\n" + "=" * 70)
    if all_passed:
        print("🎉 ALL VERIFICATION CHECKS PASSED PERFECTLY!")
    else:
        print("⚠️ SOME VERIFICATION CHECKS FAILED. SEE DETAILS ABOVE.")
    print("=" * 70)

if __name__ == '__main__':
    test_all()
