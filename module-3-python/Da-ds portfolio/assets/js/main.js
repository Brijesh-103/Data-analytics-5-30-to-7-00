/* ============================================================
   main.js — Portfolio Interactivity
   Features: Dark Mode, Hamburger, Scroll Reveal, Typewriter,
             Active Nav, Skill Bars, Back To Top, Loading,
             Contact Form, Counter Animation
   ============================================================ */

// ─────────────── 1. THEME (Dark Mode) ───────────────
const html = document.documentElement;
const darkToggle = document.getElementById('darkToggle');
const darkIcon   = document.getElementById('darkIcon');

function applyTheme(dark) {
  if (dark) {
    html.classList.add('dark');
    darkIcon.textContent = '☀️';
    localStorage.setItem('theme', 'dark');
  } else {
    html.classList.remove('dark');
    darkIcon.textContent = '🌙';
    localStorage.setItem('theme', 'light');
  }
}

// Init theme from localStorage
const savedTheme = localStorage.getItem('theme');
applyTheme(savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches));

darkToggle.addEventListener('click', () => {
  applyTheme(!html.classList.contains('dark'));
});

// ─────────────── 2. LOADING SCREEN ───────────────
const loader = document.getElementById('loader');
window.addEventListener('load', () => {
  setTimeout(() => loader.classList.add('hidden'), 500);
});

// ─────────────── 3. NAVBAR SCROLL SHADOW ───────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 10);
}, { passive: true });

// ─────────────── 4. HAMBURGER MENU ───────────────
const hamburger   = document.getElementById('hamburger');
const mobileMenu  = document.getElementById('mobileMenu');

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('open');
  mobileMenu.classList.toggle('open');
});

// Close mobile menu on link click
mobileMenu.querySelectorAll('.mobile-nav-link').forEach(link => {
  link.addEventListener('click', () => {
    hamburger.classList.remove('open');
    mobileMenu.classList.remove('open');
  });
});

// ─────────────── 5. SMOOTH SCROLL ───────────────
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      const offset = 72; // navbar height
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

// ─────────────── 6. ACTIVE NAV HIGHLIGHT ───────────────
const sections  = document.querySelectorAll('section[id]');
const navLinks  = document.querySelectorAll('.nav-link');

const navObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(l => l.classList.remove('active'));
      const active = document.querySelector(`.nav-link[href="#${entry.target.id}"]`);
      if (active) active.classList.add('active');
    }
  });
}, { rootMargin: '-50% 0px -50% 0px' });

sections.forEach(s => navObserver.observe(s));

// ─────────────── 7. SCROLL REVEAL ───────────────
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal, .reveal-scale').forEach(el => {
  revealObserver.observe(el);
});

// ─────────────── 8. SKILL BARS ───────────────
const skillBarObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.skill-level-fill').forEach(fill => {
        fill.style.width = fill.dataset.level + '%';
      });
      skillBarObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.3 });

const skillsSection = document.getElementById('skills');
if (skillsSection) skillBarObserver.observe(skillsSection);

// ─────────────── 9. TYPEWRITER EFFECT ───────────────
const titles = [
  'Data Analyst',
  'Data Scientist',
  'BI Developer',
  'ML Enthusiast',
  'Python Developer',
];
let tIdx = 0, cIdx = 0, deleting = false;
const typeEl = document.getElementById('typewriter');

function typeLoop() {
  if (!typeEl) return;
  const current = titles[tIdx];
  if (!deleting) {
    typeEl.textContent = current.slice(0, ++cIdx);
    if (cIdx === current.length) { deleting = true; setTimeout(typeLoop, 2000); return; }
    setTimeout(typeLoop, 80);
  } else {
    typeEl.textContent = current.slice(0, --cIdx);
    if (cIdx === 0) {
      deleting = false;
      tIdx = (tIdx + 1) % titles.length;
      setTimeout(typeLoop, 400);
      return;
    }
    setTimeout(typeLoop, 45);
  }
}
typeLoop();

// ─────────────── 10. COUNTER ANIMATION ───────────────
function animateCounter(el, target, suffix = '') {
  let start = 0;
  const duration = 1800;
  const step = (timestamp) => {
    if (!start) start = timestamp;
    const progress = Math.min((timestamp - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
    el.textContent = Math.floor(eased * target) + suffix;
    if (progress < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('[data-count]').forEach(el => {
        animateCounter(el, +el.dataset.count, el.dataset.suffix || '');
      });
      counterObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.4 });

document.querySelectorAll('.stats-group').forEach(g => counterObserver.observe(g));

// ─────────────── 11. BACK TO TOP ───────────────
const backToTop = document.getElementById('backToTop');
window.addEventListener('scroll', () => {
  backToTop.classList.toggle('visible', window.scrollY > 350);
}, { passive: true });
backToTop.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// ─────────────── 12. CONTACT FORM ───────────────
const contactForm = document.getElementById('contactForm');
const formSuccess = document.getElementById('formSuccess');

if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = contactForm.querySelector('button[type="submit"]');
    btn.disabled = true;
    btn.textContent = 'Sending…';
    // Simulate send (no backend — visual only)
    setTimeout(() => {
      contactForm.reset();
      formSuccess.classList.add('show');
      btn.disabled = false;
      btn.textContent = 'Send Message';
      setTimeout(() => formSuccess.classList.remove('show'), 5000);
    }, 1200);
  });
}

// ─────────────── 13. GALLERY LIGHTBOX (simple) ───────────────
const galleryItems = document.querySelectorAll('.gallery-item img');
galleryItems.forEach(img => {
  img.style.cursor = 'zoom-in';
  img.addEventListener('click', () => {
    const overlay = document.createElement('div');
    overlay.style.cssText = `
      position:fixed;inset:0;z-index:9998;background:rgba(0,0,0,0.88);
      display:flex;align-items:center;justify-content:center;cursor:zoom-out;
      animation:fadeIn 0.2s ease;
    `;
    const bigImg = document.createElement('img');
    bigImg.src = img.src;
    bigImg.style.cssText = `
      max-width:92vw;max-height:88vh;border-radius:12px;
      box-shadow:0 20px 80px rgba(0,0,0,0.6);
    `;
    overlay.appendChild(bigImg);
    overlay.addEventListener('click', () => overlay.remove());
    document.body.appendChild(overlay);
  });
});
