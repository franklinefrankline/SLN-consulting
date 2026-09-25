# -*- coding: utf-8 -*-
"""
test_internships_redesign.py
Automated verification suite validating all 21 requirements of the Internship Redesign prompt.
"""

import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.chdir(os.path.dirname(os.path.abspath(__file__)))

ALL_HTML_FILES = [
    'index.html',
    'about.html',
    'soc.html',
    'enterprises.html',
    'campus.html',
    'internships.html',
    'cambridge.html',
    'isc2.html',
    'ec-council.html',
    'it-services.html',
    'training.html',
    'training-schedule.html',
    'contact.html',
    'offerings.html'
]

def run_tests():
    total_checks = 0
    passed_checks = 0
    errors = []

    def check(condition, message):
        nonlocal total_checks, passed_checks
        total_checks += 1
        if condition:
            passed_checks += 1
            print(f"  [PASS] {message}")
        else:
            errors.append(message)
            print(f"  [FAIL] {message}")

    print("==================================================")
    print("SLN CONSULTING INTERNSHIP REDESIGN VERIFICATION")
    print("==================================================\n")

    # 1. CHECK ALL 14 FILES FOR CONSISTENCY & DROPDOWN
    print("--- 1. Testing Internships Dropdown in All 14 HTML Files ---")
    for fname in ALL_HTML_FILES:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()

        check('id="internshipsNavRoot"' in content, f"{fname} has desktop Internships dropdown root")
        check('id="mobileInternshipsMenu"' in content, f"{fname} has mobile Internships accordion")
        check('href="internships.html#program"' in content, f"{fname} links to #program in dropdown")
        check('href="internships.html#pathways"' in content, f"{fname} links to #pathways in dropdown")
        check('href="internships.html#journey"' in content, f"{fname} links to #journey in dropdown")
        check('href="internships.html#institutional-model"' in content, f"{fname} links to #institutional-model in dropdown")
        check('View Internship Program' in content, f"{fname} has 'View Internship Program' action link")

    # 2. CHECK VIEW-INTERNSHIPS SECTION CONTENT
    print("\n--- 2. Testing View Internships Sections & Content ---")
    with open('internships.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # SECTION 1: HERO
    check('id="internship-hero"' in content, "Hero section has #internship-hero")
    check('3-Month Industry-Aligned' in content and 'Cybersecurity Internship' in content, "Hero has correct main heading")
    check('Structured industry exposure for 2027 graduating students' in content, "Hero has short description")
    check('Discuss Institutional Partnership' in content, "Hero has 'Discuss Institutional Partnership' CTA")
    check('View Program Structure' in content, "Hero has 'View Program Structure' CTA")
    check('assets/internship_hero_cybersecurity.jpg' in content, "Hero uses assets/internship_hero_cybersecurity.jpg")
    check('PROGRAM CONSOLE' in content and 'Cohort 2027' in content, "Hero has Program Console header")
    check('AI-SOC Analyst' in content or 'AI-SOC' in content, "Hero Program Console shows AI-SOC")
    check('01 Foundation' in content and '02 Practice' in content and '03 Project' in content, "Hero console shows 3-month nodes")
    check('Unusual Sign-in Pattern' in content or 'Unusual sign-in' in content, "Hero console has guided alert scenario")
    check('data-count="3"' in content, "Metric strip has count-up for 3 Months")
    check('data-count="7"' in content, "Metric strip has count-up for 7 Pathways")
    check('data-count="400"' in content, "Metric strip has count-up for 400+ Tasks")

    # SECTION 2: PROGRAM
    check('id="program"' in content, "Program section has id='program'")
    check('Three Months.' in content and 'Real Industry Exposure.' in content, "Program has heading 'Three Months. Real Industry Exposure.'")
    check('Structured Industry Exposure' in content, "Program has Value Card 1")
    check('Multiple Specialization Pathways' in content, "Program has Value Card 2")
    check('Practical Learning' in content, "Program has Value Card 3")
    check('Final-Year Project Enablement' in content, "Program has Value Card 4")
    check('Verifiable Credentials' in content, "Program has Value Card 5")
    check('Low-Friction Delivery' in content, "Program has Value Card 6")

    # SECTION 2B: PROGRAM AT A GLANCE
    check('id="glance"' in content, "Program at a Glance has id='glance'")
    check('The Program at a Glance' in content, "Glance has heading")
    check('Knowledge Checks' in content, "Glance has Knowledge Checks indicator")

    # SECTION 3: PATHWAYS
    check('id="pathways"' in content, "Pathways section has id='pathways'")
    check('Seven Cybersecurity Specialization Pathways' in content, "Pathways has heading")
    check('Common Foundation' in content, "Pathways has Common Foundation origin card")
    check('assets/internship_pathway_soc.jpg' in content, "Pathways has SOC image")
    check('assets/internship_pathway_vapt.jpg' in content, "Pathways has VAPT image")
    check('assets/internship_pathway_grc.jpg' in content, "Pathways has GRC image")
    check('assets/internship_pathway_cloud.jpg' in content, "Pathways has Cloud image")
    check('assets/internship_pathway_identity.jpg' in content, "Pathways has Identity image")
    check('Security Operations' in content, "Pathways has Security Operations family")
    check('Offensive Security' in content, "Pathways has Offensive Security family")
    check('Governance, Risk & Privacy' in content or 'Governance, Risk &amp; Privacy' in content, "Pathways has GRC family")
    check('Cloud Security' in content, "Pathways has Cloud Security family")
    check('Identity Security' in content, "Pathways has Identity Security family")

    # SECTION 4: STUDENT JOURNEY
    check('id="journey"' in content, "Student Journey has id='journey'")
    check('Three Months. One Structured Journey.' in content, "Journey has heading")
    check('MONTH 01' in content and 'Foundation + Orientation' in content, "Journey has Month 01")
    check('MONTH 02' in content and 'Domain Practice' in content, "Journey has Month 02")
    check('MONTH 03' in content and 'Project + Career Readiness' in content, "Journey has Month 03")
    check('assets/internship_journey_foundation.jpg' in content, "Journey has Month 01 image")
    check('assets/internship_journey_domain.jpg' in content, "Journey has Month 02 image")
    check('assets/internship_journey_project.jpg' in content, "Journey has Month 03 image")

    # SECTION 5: LEARNING MODEL
    check('id="learning-model"' in content, "Learning Model has id='learning-model'")
    check('From Knowledge to Demonstrable Practice' in content, "Learning Model has heading")
    check('Knowledge' in content and 'Skill' in content and 'Task' in content and 'Evidence' in content and 'Career Ready' in content, "Learning Model has 5-stage flow")
    check('LIVE LEARNING' in content, "Learning Model has Live Learning pillar")
    check('PRACTICAL EXPOSURE' in content, "Learning Model has Practical Exposure pillar")
    check('PROJECT ENABLEMENT' in content, "Learning Model has Project Enablement pillar")

    # SECTION 6: FINAL-YEAR PROJECTS
    check('id="projects"' in content, "Projects section has id='projects'")
    check('Helping Students Connect Industry Tasks to Final-Year Projects' in content, "Projects has heading")
    check('Problem Identification' in content and 'Domain Selection' in content and 'Technical Exploration' in content, "Projects has process steps")
    check('Project enablement' in content and 'not project completion' in content, "Projects has scope note")

    # SECTION 7: CREDENTIALS
    check('id="credentials"' in content, "Credentials has id='credentials'")
    check('Recognition Built Into the Journey' in content, "Credentials has heading")
    check('assets/internship_credentials_badge.jpg' in content, "Credentials has real certificate image")
    check('Foundation Certificate' in content, "Credentials has Foundation Certificate")
    check('Core Domain Certificate' in content, "Credentials has Core Domain Certificate")
    check('Placement Prep Access' in content or 'Placement Preparation Program' in content, "Credentials has Placement Prep")

    # SECTION 8: INSTITUTIONAL MODEL
    check('id="institutional-model"' in content, "Institutional Model has id='institutional-model'")
    check('Simple for the Institution. Structured for the Student.' in content, "Institutional Model has heading")
    check('assets/internship_institutional_campus.jpg' in content, "Institutional Model has campus meeting photo")
    check('The Institution' in content and '4 Responsibilities' in content, "Institutional Model has 4 responsibilities for institution")
    check('The Program Provider' in content or 'SLN Consulting (Program Provider)' in content, "Institutional Model has provider role")
    check('8 Responsibilities' in content, "Institutional Model has 8 responsibilities for provider")

    # SECTION 9: GOVERNANCE
    check('id="governance"' in content, "Governance has id='governance'")
    check('Program Governance & Institutional Visibility' in content or 'Program Governance &amp; Visibility' in content or 'Program Governance' in content, "Governance has heading")
    check('Enrollment' in content and 'Participation' in content and 'Assessment Status' in content, "Governance has reporting indicator bars")

    # SECTION 10: ENGAGEMENT
    check('id="engagement"' in content, "Engagement has id='engagement'")
    check('Institutional Engagement' in content, "Engagement has heading")
    check('Request Institutional Proposal' in content, "Engagement has Proposal CTA")

    # SECTION 11: FAQ
    check('id="faq"' in content, "FAQ has id='faq'")
    check('Frequently Asked Questions' in content, "FAQ has heading")
    check('Does this replace our academic curriculum?' in content, "FAQ has Question 1")
    check('Is the program only theoretical?' in content, "FAQ has Question 2")
    check('Does every student follow all seven pathways?' in content, "FAQ has Question 3")
    check('Can the institution evaluate the internship?' in content, "FAQ has Question 4")
    check('Will this create significant additional workload?' in content, "FAQ has Question 5")
    check('Does the program guarantee employment?' in content, "FAQ has Question 6")

    # SECTION 13: CONTACT / ENQUIRY
    check('id="contact"' in content, "Contact has id='contact'")
    check('Ready to Build Industry-Ready Cybersecurity Skills?' in content, "Contact has heading")
    check('id="internshipEnquiryForm"' in content, "Contact has #internshipEnquiryForm")
    check('handleInternshipEnquirySubmit(event)' in content, "Form has handleInternshipEnquirySubmit(event)")
    check('Discuss Institutional Partnership' in content, "Form has topic radio")

    # ROUTING & SCRIPTS
    check('function initInternshipInteractions' in content, "Script contains initInternshipInteractions()")
    check('function handleInternshipEnquirySubmit' in content, "Script contains handleInternshipEnquirySubmit()")
    check("'program': 'view-internships'" in content, "Router routeMap maps 'program' to view-internships")
    check("'pathways': 'view-internships'" in content, "Router routeMap maps 'pathways' to view-internships")
    check("'journey': 'view-internships'" in content, "Router routeMap maps 'journey' to view-internships")
    check("'institutional-model': 'view-internships'" in content, "Router routeMap maps 'institutional-model' to view-internships")

    print("\n==================================================")
    print(f"INTERNSHIP REDESIGN TEST RESULTS: {passed_checks}/{total_checks} PASSED")
    if errors:
        print(f"FAILED CHECKS ({len(errors)}):")
        for err in errors:
            print(f"  - {err}")
    else:
        print("ALL INTERNSHIP REDESIGN REQUIREMENTS VERIFIED & PASSED!")
    print("==================================================")

if __name__ == '__main__':
    run_tests()
