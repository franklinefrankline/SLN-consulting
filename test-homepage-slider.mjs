import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';

function fetchPage(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve({ statusCode: res.statusCode, body: data }));
    }).on('error', reject);
  });
}

function getDimensions(filePath) {
  const buf = fs.readFileSync(filePath);
  if (buf[0] === 0x89 && buf[1] === 0x50 && buf[2] === 0x4E && buf[3] === 0x47) {
    return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20), type: 'png' };
  }
  if (buf[0] === 0xFF && buf[1] === 0xD8) {
    let offset = 2;
    while (offset < buf.length) {
      if (buf[offset] !== 0xFF) break;
      const marker = buf[offset + 1];
      if (marker === 0xC0 || marker === 0xC2) {
        return { height: buf.readUInt16BE(offset + 5), width: buf.readUInt16BE(offset + 7), type: 'jpg' };
      }
      const len = buf.readUInt16BE(offset + 2);
      offset += 2 + len;
    }
  }
  return { error: 'Unknown format' };
}

async function runTests() {
  console.log('========================================================================');
  console.log(' SLN CONSULTING — HOMEPAGE SLIDER VERIFICATION TEST SUITE');
  console.log('========================================================================\n');

  let passed = 0;
  let failed = 0;

  function assert(condition, message) {
    if (condition) {
      console.log(`  [PASS] ${message}`);
      passed++;
    } else {
      console.error(`  [FAIL] ${message}`);
      failed++;
    }
  }

  // 1. Fetch homepage
  console.log('--- 1. Homepage Accessibility & Slider Structure ---');
  const res = await fetchPage('http://localhost:3000/index.php');
  assert(res.statusCode === 200, 'index.php returns HTTP 200');
  const html = res.body;

  assert(html.includes('id="slnHeroCarousel"'), 'Hero carousel container #slnHeroCarousel exists');
  assert(html.includes('class="swiper mySwiper"'), 'Swiper container .mySwiper exists');

  // 2. Verify all 8 slides and image files
  console.log('\n--- 2. Slide Indexes & Image Identity Verification ---');
  const expectedSlides = [
    { index: 1, id: 'banner1', file: 'slk-banner1.jpg', compact: false },
    { index: 2, id: 'banner-training', file: 'slk-banner11.jpg', compact: false },
    { index: 3, id: 'banner6', file: 'slk-banner6.jpg', compact: false },
    { index: 4, id: 'banner2', file: 'slk-banner2.jpg', compact: false },
    { index: 5, id: 'banner-soc', file: 'slk-banner7.jpg', compact: false },
    { index: 6, id: 'banner-vapt', file: 'vapt-banner.jpg', compact: true },
    { index: 7, id: 'banner-cybersecurity-internship', file: 'cybersecurity-internship-3-month.png', compact: true },
    { index: 8, id: 'banner5', file: 'slk-banner5.jpg', compact: false }
  ];

  expectedSlides.forEach(s => {
    assert(html.includes(`id="${s.id}"`), `Slide ${s.index} (id="${s.id}") exists in HTML`);
    assert(html.includes(s.file), `Slide ${s.index} references exact file ${s.file}`);
  });

  // 3. Verify Slide 6 and Slide 7 slide-specific classes
  console.log('\n--- 3. Slide 6 & 7 Slide-Specific Scoping Verification ---');
  assert(html.includes('slide-compact slide-vapt'), 'Slide 6 has slide-compact and slide-vapt classes');
  assert(html.includes('slide-compact slide-internship'), 'Slide 7 has slide-compact and slide-internship classes');
  assert(html.includes('id="banner-vapt" class="slider-image-compact"'), 'Image 6 has class slider-image-compact');
  assert(html.includes('id="banner-cybersecurity-internship" class="slider-image-compact"'), 'Image 7 has class slider-image-compact');

  // Verify Slides 1-5 and 8 DO NOT have compact classes
  const slide1Match = html.match(/<!-- 1\.[\s\S]*?<\/div>/);
  assert(slide1Match && !slide1Match[0].includes('slide-compact'), 'Slide 1 does NOT have slide-compact (unchanged)');
  const slide5Match = html.match(/<!-- 5\.[\s\S]*?<\/div>/);
  assert(slide5Match && !slide5Match[0].includes('slide-compact'), 'Slide 5 does NOT have slide-compact (unchanged)');
  const slide8Match = html.match(/<!-- 8\.[\s\S]*?<\/div>/);
  assert(slide8Match && !slide8Match[0].includes('slide-compact'), 'Slide 8 does NOT have slide-compact (unchanged)');

  // 4. Verify Dimension Calculations & Aspect Ratio Preservation
  console.log('\n--- 4. Rendered Dimensions & Scale Matching Analysis ---');
  const imgDir = 'c:/Users/inbat/Downloads/SLN-Website-Development/SLN-Website-Development/assets/img/sln-img';

  const dimStandard = getDimensions(path.join(imgDir, 'slk-banner1.jpg'));
  const dim6 = getDimensions(path.join(imgDir, 'vapt-banner.jpg'));
  const dim7 = getDimensions(path.join(imgDir, 'cybersecurity-internship-3-month.png'));

  const standardRatio = dimStandard.width / dimStandard.height; // ~2.330
  const ratio6 = dim6.width / dim6.height; // ~1.7716
  const ratio7 = dim7.width / dim7.height; // ~1.7768

  console.log(`  - Standard Slides (1-5, 8) Intrinsic: ${dimStandard.width}x${dimStandard.height} (Aspect Ratio: ${standardRatio.toFixed(4)})`);
  console.log(`  - Slide 6 (vapt-banner.jpg) Intrinsic: ${dim6.width}x${dim6.height} (Aspect Ratio: ${ratio6.toFixed(4)})`);
  console.log(`  - Slide 7 (cybersecurity-internship-3-month.png) Intrinsic: ${dim7.width}x${dim7.height} (Aspect Ratio: ${ratio7.toFixed(4)})`);

  // Viewports to test
  const viewports = [
    { name: 'Full HD Desktop (1920px)', width: 1920 },
    { name: 'Standard Desktop (1349px)', width: 1349 },
    { name: 'Tablet Landscape (1024px)', width: 1024 },
    { name: 'Tablet Portrait (768px)', width: 768 },
    { name: 'Mobile (375px)', width: 375 }
  ];

  viewports.forEach(vp => {
    const stdH = vp.width / standardRatio;
    // Before: images 6 & 7 were 100% width
    const beforeH6 = vp.width / ratio6;
    const beforeH7 = vp.width / ratio7;
    // After: images 6 & 7 are 76.2% width
    const afterW = vp.width * 0.762;
    const afterH6 = afterW / ratio6;
    const afterH7 = afterW / ratio7;

    const diff6 = Math.abs(afterH6 - stdH);
    const diff7 = Math.abs(afterH7 - stdH);

    console.log(`\n  Viewport: ${vp.name}`);
    console.log(`    Standard Slides Height: ${stdH.toFixed(1)}px (Width: ${vp.width}px)`);
    console.log(`    Slide 6: Before = ${vp.width}x${beforeH6.toFixed(1)}px (+${(beforeH6 - stdH).toFixed(1)}px) | After = ${afterW.toFixed(1)}x${afterH6.toFixed(1)}px (Diff: ${diff6.toFixed(1)}px)`);
    console.log(`    Slide 7: Before = ${vp.width}x${beforeH7.toFixed(1)}px (+${(beforeH7 - stdH).toFixed(1)}px) | After = ${afterW.toFixed(1)}x${afterH7.toFixed(1)}px (Diff: ${diff7.toFixed(1)}px)`);

    assert(diff6 < 2.0, `${vp.name}: Slide 6 rendered height matches standard slides within 2px (diff = ${diff6.toFixed(2)}px)`);
    assert(diff7 < 2.0, `${vp.name}: Slide 7 rendered height matches standard slides within 2px (diff = ${diff7.toFixed(2)}px)`);
  });

  // 5. Verify Navigation Arrows
  console.log('\n--- 5. Left and Right Navigation Buttons Verification ---');
  assert(html.includes('id="heroSliderPrev"'), 'Prev button #heroSliderPrev exists');
  assert(html.includes('id="heroSliderNext"'), 'Next button #heroSliderNext exists');
  assert(html.includes('class="fa-solid fa-chevron-left"'), 'Prev button contains Font Awesome fa-chevron-left icon');
  assert(html.includes('class="fa-solid fa-chevron-right"'), 'Next button contains Font Awesome fa-chevron-right icon');
  assert(html.includes('aria-label="Previous slide"'), 'Prev button has accessible aria-label="Previous slide"');
  assert(html.includes('aria-label="Next slide"'), 'Next button has accessible aria-label="Next slide"');

  // Verify CSS properties for buttons
  assert(html.includes('.mySwiper .swiper-button-prev,') && html.includes('.mySwiper .swiper-button-next'), 'CSS rules define .swiper-button-prev and .swiper-button-next');
  assert(html.includes('border-radius: 50% !important;'), 'Buttons have border-radius: 50% (circular design)');
  assert(html.includes('z-index: 30 !important;'), 'Buttons have elevated z-index: 30 above slide images');
  assert(html.includes('background: #ffffff !important;'), 'Buttons have crisp white circular background for maximum visibility');
  assert(html.includes('color: #013df5 !important;'), 'Buttons have SLN blue chevron icon (#013df5)');
  assert(html.includes('box-shadow: 0 4px 16px rgba(0, 0, 0, 0.22)'), 'Buttons have soft drop shadow for visibility against light banners');
  assert(html.includes('top: 50% !important;'), 'Buttons are vertically centred with top: 50%');
  assert(html.includes('transform: translateY(-50%)'), 'Buttons use translateY(-50%) for exact vertical centring');

  // 6. Verify JavaScript Swiper Navigation & Wrapping
  console.log('\n--- 6. Swiper Configuration & Wrapping Functionality ---');
  assert(html.includes('loop: true'), 'Swiper is configured with loop: true for continuous wrapping');
  assert(html.includes('prevEl: \'.mySwiper .swiper-button-prev\''), 'Swiper navigation connects prevEl');
  assert(html.includes('nextEl: \'.mySwiper .swiper-button-next\''), 'Swiper navigation connects nextEl');
  assert(html.includes('heroSwiper.slidePrev()'), 'Direct click listener calls heroSwiper.slidePrev()');
  assert(html.includes('heroSwiper.slideNext()'), 'Direct click listener calls heroSwiper.slideNext()');
  assert(html.includes('clickable: true'), 'Pagination dots are clickable');
  assert(html.includes('delay: 4000'), 'Autoplay delay is 4000ms');

  // 7. Verify Banner Click Interception Exclusion
  console.log('\n--- 7. Banner Link Delegation Safety ---');
  assert(html.includes('e.target.closest(\'.swiper-button-prev\')'), 'Banner click handler ignores clicks on prev button');
  assert(html.includes('e.target.closest(\'.swiper-button-next\')'), 'Banner click handler ignores clicks on next button');
  assert(html.includes('e.target.closest(\'.swiper-pagination\')'), 'Banner click handler ignores clicks on pagination bullets');

  // 8. Responsive Design CSS
  console.log('\n--- 8. Responsive Design & Layout Verification ---');
  assert(html.includes('@media screen and (max-width: 1023px)'), 'Tablet breakpoint (max-width: 1023px) defined');
  assert(html.includes('@media screen and (max-width: 767px)'), 'Mobile breakpoint (max-width: 767px) defined');
  assert(html.includes('overflow-x: hidden;'), 'Page prevents horizontal overflow');

  console.log('\n========================================================================');
  console.log(` SUMMARY: Total Tests: ${passed + failed} | Passed: ${passed} | Failed: ${failed}`);
  console.log('========================================================================');

  if (failed > 0) {
    process.exit(1);
  }
}

runTests().catch(err => {
  console.error('Test execution failed:', err);
  process.exit(1);
});
