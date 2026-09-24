with open('c:/Agen/SLN counsulting/offerings.html', 'r', encoding='utf-8') as f:
    c = f.read()

assert '01' in c and 'SOC-As-A-Service' in c
assert '02' in c and 'Skilling Solutions' in c
assert '03' in c and 'Cambridge Learning' in c
assert '04' in c and 'ISC2 Credentials' in c
assert '05' in c and 'EC-Council (ATC)' in c
assert '06' in c and 'IT Services (8 Pillars)' in c

assert 'id="view-soc"' in c, "view-soc missing!"
assert 'id="view-skilling"' in c, "view-skilling missing!"
assert 'id="view-cambridge"' in c, "view-cambridge missing!"
assert 'id="view-isc2"' in c, "view-isc2 missing!"
assert 'id="view-ec-council"' in c, "view-ec-council missing!"
assert 'id="view-it-services"' in c, "view-it-services missing!"

# Check view-cambridge doesn't have EC-Council or ISC2
cambridge_match = c.split('id="view-cambridge"')[1].split('</main>')[0]
assert 'EC-Council' not in cambridge_match, 'EC-Council found in view-cambridge!'
assert 'ISC2' not in cambridge_match, 'ISC2 found in view-cambridge!'
assert 'CISSP' not in cambridge_match, 'CISSP found in view-cambridge!'
assert 'CEH' not in cambridge_match, 'CEH found in view-cambridge!'

# Check view-isc2 doesn't have Cambridge or EC-Council
isc2_match = c.split('id="view-isc2"')[1].split('</main>')[0]
assert 'Cambridge' not in isc2_match, 'Cambridge found in view-isc2!'
assert 'EC-Council' not in isc2_match, 'EC-Council found in view-isc2!'
assert 'CEH' not in isc2_match, 'CEH found in view-isc2!'
assert 'CISSP' in isc2_match, 'CISSP missing from view-isc2!'

# Check view-ec-council doesn't have Cambridge or ISC2
ecc_match = c.split('id="view-ec-council"')[1].split('</main>')[0]
assert 'Cambridge' not in ecc_match, 'Cambridge found in view-ec-council!'
assert 'ISC2' not in ecc_match, 'ISC2 found in view-ec-council!'
assert 'CISSP' not in ecc_match, 'CISSP found in view-ec-council!'
assert 'CEH' in ecc_match, 'CEH missing from view-ec-council!'

# Check Previous / Next service removed
assert 'PREVIOUS SERVICE' not in c, 'PREVIOUS SERVICE still in offerings.html!'
assert 'NEXT SERVICE' not in c, 'NEXT SERVICE still in offerings.html!'
assert 'Previous Service' not in c, 'Previous Service still in offerings.html!'
assert 'Next Service' not in c, 'Next Service still in offerings.html!'

print('ALL ASSERTIONS PASSED FOR offerings.html!')
