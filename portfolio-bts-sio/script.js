/* =============================================
   PORTFOLIO FANTAISIQUE — script.js
   ============================================= */

// ---- ÉTOILES CANVAS ----
(function() {
    const canvas = document.getElementById('star-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let stars = [];
    let w, h;

    function resize() {
        w = canvas.width  = window.innerWidth;
        h = canvas.height = document.documentElement.scrollHeight;
    }

    function rand(min, max) { return Math.random() * (max - min) + min; }

    function initStars() {
        stars = [];
        const count = Math.floor((w * h) / 4000);
        for (let i = 0; i < count; i++) {
            stars.push({
                x: rand(0, w),
                y: rand(0, h),
                r: rand(0.2, 1.4),
                a: rand(0.1, 0.9),
                speed: rand(0.0002, 0.001),
                phase: rand(0, Math.PI * 2),
                hue: Math.random() > 0.7 ? rand(190, 220) : rand(220, 260), // mostly cyan-blue, some indigo
            });
        }
    }

    let t = 0;
    function draw() {
        ctx.clearRect(0, 0, w, h);
        t += 0.01;
        stars.forEach(s => {
            const alpha = s.a * (0.5 + 0.5 * Math.sin(t * s.speed * 1000 + s.phase));
            ctx.beginPath();
            ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
            ctx.fillStyle = `hsla(${s.hue}, 80%, 80%, ${alpha})`;
            ctx.fill();
        });
        requestAnimationFrame(draw);
    }

    window.addEventListener('resize', () => {
        resize();
        initStars();
    });

    resize();
    initStars();
    draw();
})();

// ---- NAVBAR SCROLL ----
const navbar = document.getElementById('navbar');
if (navbar) {
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 40);
    }, { passive: true });
}

// ---- BURGER MENU ----
const burger = document.getElementById('navBurger');
const navLinks = document.getElementById('navLinks');
if (burger && navLinks) {
    burger.addEventListener('click', () => {
        burger.classList.toggle('active');
        navLinks.classList.toggle('open');
    });
    navLinks.querySelectorAll('.nav-link').forEach(l => {
        l.addEventListener('click', () => {
            burger.classList.remove('active');
            navLinks.classList.remove('open');
        });
    });
}

// ---- ANIMATE ON SCROLL ----
const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
        if (e.isIntersecting) {
            e.target.classList.add('visible');
        }
    });
}, { threshold: 0.08 });

document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));

// ---- FILTRES PROJETS ----
const filterBtns = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

if (filterBtns.length && projectCards.length) {
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filter = btn.dataset.filter;
            projectCards.forEach(card => {
                if (filter === 'all' || card.dataset.category === filter) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });
}

// ---- CONTACT FORM (EmailJS) ----
(function() {
  // ╔══════════════════════════════════════════════════╗
  // ║  CONFIGURATION EMAILJS — À REMPLIR APRÈS SIGNUP  ║
  // ╠══════════════════════════════════════════════════╣
  // ║  1. Crée un compte sur https://www.emailjs.com   ║
  // ║  2. Add a Service → Gmail → note le Service ID   ║
  // ║  3. Create Template → note le Template ID        ║
  // ║  4. Account → API Keys → copie la Public Key     ║
  // ╚══════════════════════════════════════════════════╝
  const EMAILJS_PUBLIC_KEY  = 'ZgtPi5Cnh6wf2q7dJ';   // ← remplace ici
  const EMAILJS_SERVICE_ID  = 'service_nxmv0ij';   // ← remplace ici
  const EMAILJS_TEMPLATE_ID = 'template_6zxi82l'; // ← remplace ici

  if (typeof emailjs === 'undefined') return;
  emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });

  const form = document.getElementById('contactForm');
  if (!form) return;

  // Feedback banner sous le bouton
  const feedback = document.createElement('p');
  feedback.style.cssText = 'margin-top:14px;font-size:.85rem;text-align:center;transition:opacity .3s;opacity:0;min-height:1.2em;';
  form.appendChild(feedback);

  const showFeedback = (msg, color) => {
    feedback.textContent = msg;
    feedback.style.color  = color;
    feedback.style.opacity = '1';
    setTimeout(() => { feedback.style.opacity = '0'; }, 4000);
  };

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const originalHTML = btn.innerHTML;

    // État chargement
    btn.disabled = true;
    btn.innerHTML = '<span>Envoi en cours…</span>';

    emailjs.sendForm(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, form)
      .then(() => {
        btn.innerHTML = '<span>Message envoyé ✦</span>';
        btn.style.background = 'linear-gradient(135deg,#2dd4bf,#6366f1)';
        showFeedback('✅ Ton message a bien été envoyé !', '#4ade80');
        form.reset();
        setTimeout(() => {
          btn.innerHTML = originalHTML;
          btn.style.background = '';
          btn.disabled = false;
        }, 3500);
      })
      .catch((err) => {
        console.error('EmailJS error:', err);
        btn.innerHTML = originalHTML;
        btn.style.background = '';
        btn.disabled = false;
        showFeedback('❌ Erreur d\'envoi. Réessaie ou contacte-moi par email directement.', '#f87171');
      });
  });
})();


// ---- CURSOR GLOW (subtil) ----
(function() {
    const glow = document.createElement('div');
    glow.style.cssText = `
        position: fixed;
        pointer-events: none;
        z-index: 9999;
        width: 300px;
        height: 300px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(139,92,246,0.06) 0%, transparent 70%);
        transform: translate(-50%, -50%);
        transition: left 0.12s ease, top 0.12s ease;
        will-change: left, top;
    `;
    document.body.appendChild(glow);

    window.addEventListener('mousemove', (e) => {
        glow.style.left = e.clientX + 'px';
        glow.style.top  = e.clientY + 'px';
    }, { passive: true });
})();
