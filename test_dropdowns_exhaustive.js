const fs = require('fs');
const vm = require('vm');

console.log("==================================================");
console.log("  EXHAUSTIVE NAVBAR DROPDOWN VERIFICATION TEST    ");
console.log("==================================================\n");

let totalTests = 0;
let passedTests = 0;

function assert(desc, condition) {
  totalTests++;
  if (condition) {
    passedTests++;
    console.log(`  [PASS] ${desc}`);
  } else {
    console.error(`  [FAIL] ${desc}`);
    process.exitCode = 1;
  }
}

const HTML_FILES = [
  'index.html', 'about.html', 'soc.html', 'it-services.html',
  'campus.html', 'internships.html', 'training.html', 'training-schedule.html',
  'enterprises.html', 'contact.html', 'isc2.html', 'ec-council.html',
  'cambridge.html', 'offerings.html'
];

// 1. Static HTML & CSS checks across all 14 files
HTML_FILES.forEach(fname => {
  const content = fs.readFileSync(fname, 'utf-8');

  // Header positioning & z-index
  assert(`${fname}: header has z-[1000] or z-1000`, content.includes('z-[1000]') || content.includes('z-1000') || content.includes('z-index: 1000'));
  assert(`${fname}: header has overflow: visible !important`, content.includes('header {') && content.includes('overflow: visible !important'));
  assert(`${fname}: dropdown panel has position: absolute !important`, content.includes('.nav-dropdown-panel {') && content.includes('position: absolute !important'));
  assert(`${fname}: dropdown panel has z-index: 9999 !important`, content.includes('z-index: 9999 !important'));

  // No overflow-x: hidden on header
  assert(`${fname}: header does not have overflow-x: hidden`, !content.includes('body, header {\n      max-width: 100vw;\n      overflow-x: hidden;'));

  // Dropdown containers
  assert(`${fname}: has #dropdown-about`, content.includes('id="dropdown-about"'));
  assert(`${fname}: has #dropdown-cybersecurity`, content.includes('id="dropdown-cybersecurity"'));
  assert(`${fname}: has #dropdown-it-services`, content.includes('id="dropdown-it-services"'));
  assert(`${fname}: has #dropdown-academia`, content.includes('id="dropdown-academia"'));
  assert(`${fname}: has #internshipsDropdownPanel`, content.includes('id="internshipsDropdownPanel"'));
  assert(`${fname}: has #dropdown-training`, content.includes('id="dropdown-training"'));
  assert(`${fname}: has #dropdown-corporate`, content.includes('id="dropdown-corporate"'));
  assert(`${fname}: has #dropdown-resources`, content.includes('id="dropdown-resources"'));
  assert(`${fname}: has #dropdown-contact`, content.includes('id="dropdown-contact"'));

  // Internships behavior
  assert(`${fname}: Internships parent trigger is button`, content.includes('id="internshipsNavBtn"') && content.includes('<button type="button"'));
  assert(`${fname}: Internships parent has no href navigation`, !content.includes('href="internships.html" id="internshipsNavBtn"'));
  assert(`${fname}: Internships has Program link`, content.includes('Program') && content.includes('href="internships.html"'));
  assert(`${fname}: Internships has Pathways link`, content.includes('Pathways') && content.includes('href="internships.html#pathways"'));
  assert(`${fname}: Internships has Student Journey link`, content.includes('Student Journey') && content.includes('href="internships.html#student-journey"'));
  assert(`${fname}: Internships has Institutional Model link`, content.includes('Institutional Model') && content.includes('href="internships.html#institutional-model"'));

  // JS function definitions
  assert(`${fname}: defines toggleNavDropdown`, content.includes('function toggleNavDropdown('));
  assert(`${fname}: defines openNavDropdown`, content.includes('function openNavDropdown('));
  assert(`${fname}: defines closeAllNavDropdowns`, content.includes('function closeAllNavDropdowns('));
  assert(`${fname}: defines toggleInternshipsDropdown`, content.includes('function toggleInternshipsDropdown('));
  assert(`${fname}: defines openInternshipsDropdown`, content.includes('function openInternshipsDropdown('));
  assert(`${fname}: defines closeInternshipsDropdown`, content.includes('function closeInternshipsDropdown('));
});

// 2. Interactive DOM & State Tests in Node VM
const htmlContent = fs.readFileSync('index.html', 'utf-8');
const scriptMatches = htmlContent.match(/<script[\s\S]*?>([\s\S]*?)<\/script>/gi);
let appScript = "";
for (const match of scriptMatches) {
  if (!match.includes('src=')) {
    appScript += match.replace(/<script[\s\S]*?>/i, '').replace(/<\/script>/i, '') + "\n";
  }
}

class MockClassList {
  constructor(initial = []) { this.classes = new Set(initial); }
  add(...c) { c.forEach(x => this.classes.add(x)); }
  remove(...c) { c.forEach(x => this.classes.delete(x)); }
  contains(c) { return this.classes.has(c); }
}

class MockElement {
  constructor(id = '', tag = 'div', classes = []) {
    this.id = id;
    this.tagName = tag.toUpperCase();
    this.classList = new MockClassList(classes);
    this.attributes = {};
    this.style = {};
  }
  getAttribute(n) { return this.attributes[n] || null; }
  setAttribute(n, v) { this.attributes[n] = String(v); }
  removeAttribute(n) { delete this.attributes[n]; }
  querySelector(sel) {
    if (sel.includes('.nav-dropdown-panel')) return this._panel || null;
    if (sel.includes('button')) return this._btn || null;
    if (sel.includes('.dropdown-chev')) return this._chev || null;
    return null;
  }
}

const registry = new Map();
function getEl(id, tag = 'div', classes = []) {
  if (!registry.has(id)) {
    registry.set(id, new MockElement(id, tag, classes));
  }
  return registry.get(id);
}

// Setup elements
getEl('policyModal', 'div', ['hidden']);
const keys = ['about', 'cybersecurity', 'it-services', 'academia', 'internships', 'training', 'corporate', 'resources', 'contact'];
const parents = {};
keys.forEach(k => {
  const parent = new MockElement(`parent-${k}`, 'div', ['nav-item-dropdown']);
  parent.attributes['data-dropdown'] = k;
  const panelId = k === 'internships' ? 'internshipsDropdownPanel' : `dropdown-${k}`;
  const btnId = k === 'internships' ? 'internshipsNavBtn' : `btn-${k}`;
  const chevId = k === 'internships' ? 'internshipsChevron' : `chev-${k}`;

  const panel = getEl(panelId, 'div', ['nav-dropdown-panel', 'hidden']);
  const btn = getEl(btnId, 'button');
  btn.setAttribute('aria-expanded', 'false');
  const chev = getEl(chevId, 'svg', ['dropdown-chev']);

  parent._panel = panel;
  parent._btn = btn;
  parent._chev = chev;
  parents[k] = parent;
});

const listeners = {};
const docListeners = {};
const mockDoc = {
  documentElement: new MockElement('html'),
  body: new MockElement('body'),
  getElementById: (id) => registry.get(id) || null,
  querySelector: (sel) => {
    for (const k of keys) {
      if (sel.includes(`data-dropdown="${k}"`)) return parents[k];
    }
    return null;
  },
  querySelectorAll: (sel) => {
    if (sel === '.nav-dropdown-panel') {
      return keys.map(k => k === 'internships' ? registry.get('internshipsDropdownPanel') : registry.get(`dropdown-${k}`));
    }
    if (sel === '.nav-item-dropdown') {
      return Object.values(parents);
    }
    return [];
  },
  addEventListener: (ev, fn) => {
    if (!docListeners[ev]) docListeners[ev] = [];
    docListeners[ev].push(fn);
  }
};

const mockWin = {
  document: mockDoc,
  localStorage: { getItem: () => null, setItem: () => {} },
  location: { protocol: 'https:', href: 'https://sln-consulting.vercel.app/index.html' },
  history: { pushState: () => {}, replaceState: () => {} },
  addEventListener: () => {}
};

const sandbox = {
  window: mockWin,
  document: mockDoc,
  localStorage: mockWin.localStorage,
  setTimeout: () => {},
  console: console,
  tailwind: { config: {} }
};

vm.createContext(sandbox);
vm.runInContext(appScript, sandbox);

console.log("\n--- Testing JavaScript Dropdown State Machine ---");

// Test 1: open About Us dropdown
sandbox.toggleNavDropdown({ preventDefault: () => {}, stopPropagation: () => {} }, 'about');
const aboutPanel = registry.get('dropdown-about');
const aboutBtn = parents['about']._btn;
assert("Clicking 'About Us' opens about dropdown", aboutPanel.classList.contains('is-open') && !aboutPanel.classList.contains('hidden'));
assert("Clicking 'About Us' sets aria-expanded='true'", aboutBtn.getAttribute('aria-expanded') === 'true');

// Test 2: Clicking another dropdown ('cybersecurity') closes 'about' and opens 'cybersecurity'
sandbox.toggleNavDropdown({ preventDefault: () => {}, stopPropagation: () => {} }, 'cybersecurity');
const cyberPanel = registry.get('dropdown-cybersecurity');
assert("Opening 'Cybersecurity' closes 'About Us'", !aboutPanel.classList.contains('is-open') && aboutPanel.classList.contains('hidden'));
assert("Opening 'Cybersecurity' sets 'About Us' aria-expanded='false'", aboutBtn.getAttribute('aria-expanded') === 'false');
assert("Opening 'Cybersecurity' opens cybersecurity panel", cyberPanel.classList.contains('is-open') && !cyberPanel.classList.contains('hidden'));

// Test 3: Clicking same dropdown ('cybersecurity') toggles it closed
sandbox.toggleNavDropdown({ preventDefault: () => {}, stopPropagation: () => {} }, 'cybersecurity');
assert("Clicking 'Cybersecurity' again closes it", !cyberPanel.classList.contains('is-open') && cyberPanel.classList.contains('hidden'));

// Test 4: Internships dropdown opens/closes properly
sandbox.toggleInternshipsDropdown({ preventDefault: () => {}, stopPropagation: () => {} });
const internPanel = registry.get('internshipsDropdownPanel');
const internBtn = registry.get('internshipsNavBtn');
assert("toggleInternshipsDropdown opens internships panel", internPanel.classList.contains('is-open') && !internPanel.classList.contains('hidden'));
assert("toggleInternshipsDropdown sets aria-expanded='true'", internBtn.getAttribute('aria-expanded') === 'true');

// Test 5: Pressing Escape closes open dropdowns
if (docListeners['keydown']) {
  docListeners['keydown'].forEach(fn => fn({ key: 'Escape' }));
}
assert("Pressing Escape closes open dropdowns", !internPanel.classList.contains('is-open') && internPanel.classList.contains('hidden'));
assert("Pressing Escape resets aria-expanded to 'false'", internBtn.getAttribute('aria-expanded') === 'false');

// Test 6: Clicking outside closes open dropdowns
sandbox.toggleNavDropdown({ preventDefault: () => {}, stopPropagation: () => {} }, 'training');
const trainingPanel = registry.get('dropdown-training');
assert("Opening 'Training' dropdown succeeds", trainingPanel.classList.contains('is-open'));

if (docListeners['click']) {
  // Simulate click on outside element (not inside .nav-item-dropdown)
  const outsideTarget = { closest: (sel) => null };
  docListeners['click'].forEach(fn => fn({ target: outsideTarget }));
}
assert("Clicking outside closes 'Training' dropdown", !trainingPanel.classList.contains('is-open') && trainingPanel.classList.contains('hidden'));

console.log("\n==================================================");
console.log(`EXHAUSTIVE TEST RESULTS: ${passedTests}/${totalTests} PASSED`);
if (process.exitCode) {
  console.log("SOME CHECKS FAILED!");
} else {
  console.log("ALL EXHAUSTIVE NAVBAR DROPDOWN CHECKS PASSED (100%)!");
}
console.log("==================================================");
