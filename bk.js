/* ============================================================
   BK ENTREPRISE — COMPORTEMENTS COMMUNS
   Header réactif · menu mobile · animations au scroll · parallaxe
   carousels · filtres · orbite Workers · constructeur de mission
   ============================================================ */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- 1. HEADER RÉACTIF AU SCROLL ---------- */
  function header() {
    var h = $('.hdr');
    if (!h) return;
    var tick = function () { h.classList.toggle('is-stuck', window.scrollY > 40); };
    tick();
    window.addEventListener('scroll', tick, { passive: true });
  }

  /* ---------- 2. MENU MOBILE ---------- */
  function mobileNav() {
    var burger = $('.hdr__burger'), nav = $('.mnav');
    if (!burger || !nav) return;

    var open = function (state) {
      nav.classList.toggle('is-open', state);
      document.body.classList.toggle('no-scroll', state);
      burger.setAttribute('aria-expanded', String(state));
      if (state) {
        $$('.mnav a', nav).forEach(function (a, i) {
          a.style.animationDelay = (0.05 + i * 0.045) + 's';
        });
      }
    };

    burger.addEventListener('click', function () {
      open(!nav.classList.contains('is-open'));
    });
    $$('.mnav a', nav).forEach(function (a) {
      a.addEventListener('click', function () { open(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') open(false);
    });
  }

  /* ---------- 3. APPARITION AU SCROLL ---------- */
  function reveal() {
    var els = $$('.rv, .step');
    if (!els.length) return;
    if (reduced || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ---------- 4. PARALLAXE DOUCE ---------- */
  function parallax() {
    var els = $$('[data-px]');
    if (!els.length || reduced) return;
    var raf = null;
    var run = function () {
      raf = null;
      var vh = window.innerHeight;
      els.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        var speed = parseFloat(el.getAttribute('data-px')) || 0.12;
        var offset = (r.top + r.height / 2 - vh / 2) * speed * -1;
        el.style.transform = 'translate3d(0,' + offset.toFixed(2) + 'px,0)';
      });
    };
    window.addEventListener('scroll', function () {
      if (!raf) raf = requestAnimationFrame(run);
    }, { passive: true });
    window.addEventListener('resize', run, { passive: true });
    run();
  }

  /* ---------- 5. CAROUSEL (flèches, molette, glisser, clavier) ---------- */
  function carousels() {
    $$('.car').forEach(function (car) {
      var track = $('.car__track', car);
      var prev  = $('[data-car="prev"]', car);
      var next  = $('[data-car="next"]', car);
      if (!track) return;

      var step = function () {
        var item = $('.car__item', track);
        return item ? item.getBoundingClientRect().width + 22 : 320;
      };
      var sync = function () {
        if (!prev || !next) return;
        var max = track.scrollWidth - track.clientWidth - 2;
        prev.disabled = track.scrollLeft <= 2;
        next.disabled = track.scrollLeft >= max;
      };

      if (prev) prev.addEventListener('click', function () { track.scrollBy({ left: -step(), behavior: 'smooth' }); });
      if (next) next.addEventListener('click', function () { track.scrollBy({ left:  step(), behavior: 'smooth' }); });
      track.addEventListener('scroll', sync, { passive: true });
      window.addEventListener('resize', sync, { passive: true });

      /* glisser à la souris */
      var down = false, startX = 0, startS = 0, moved = 0;
      track.addEventListener('pointerdown', function (e) {
        if (e.pointerType === 'touch') return;
        down = true; moved = 0;
        startX = e.clientX; startS = track.scrollLeft;
        track.classList.add('is-drag');
      });
      track.addEventListener('pointermove', function (e) {
        if (!down) return;
        var d = e.clientX - startX;
        moved = Math.abs(d);
        track.scrollLeft = startS - d;
      });
      ['pointerup', 'pointerleave', 'pointercancel'].forEach(function (ev) {
        track.addEventListener(ev, function () {
          if (!down) return;
          down = false;
          track.classList.remove('is-drag');
        });
      });
      /* évite d'ouvrir le lien après un vrai glissement */
      track.addEventListener('click', function (e) {
        if (moved > 8) { e.preventDefault(); e.stopPropagation(); }
        moved = 0;
      }, true);

      /* clavier */
      track.setAttribute('tabindex', '0');
      track.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') { e.preventDefault(); track.scrollBy({ left:  step(), behavior: 'smooth' }); }
        if (e.key === 'ArrowLeft')  { e.preventDefault(); track.scrollBy({ left: -step(), behavior: 'smooth' }); }
      });

      sync();
    });
  }

  /* ---------- 6. FILTRES (portfolio) ---------- */
  function filters() {
    var bar = $('[data-filter-bar]');
    if (!bar) return;
    var items = $$('[data-cat]');
    var btns = $$('button', bar);

    var apply = function (btn) {
      var f = btn.getAttribute('data-f');
      btns.forEach(function (b) { b.classList.toggle('is-on', b === btn); });
      items.forEach(function (it) {
        var show = (f === '*') || it.getAttribute('data-cat') === f;
        it.style.display = show ? '' : 'none';
        if (show) {
          it.classList.remove('is-in');
          requestAnimationFrame(function () { it.classList.add('is-in'); });
        }
      });
    };

    btns.forEach(function (btn) {
      btn.addEventListener('click', function () { apply(btn); });
    });

    /* lien profond : portfolio.html#identite active directement le filtre */
    var fromHash = function () {
      var h = decodeURIComponent(location.hash.slice(1));
      if (!h) return;
      var m = btns.filter(function (b) { return b.getAttribute('data-slug') === h; })[0];
      if (m) apply(m);
    };
    fromHash();
    window.addEventListener('hashchange', fromHash);
  }

  /* ---------- 7. ORBITE DES WORKERS ---------- */
  /* Le rayon doit être en pixels : un pourcentage dans translateY() se
     calculerait sur la hauteur du portrait, pas sur celle de l'anneau. */
  function orbit() {
    var rings = $$('.orbit__spin, .eco');
    if (!rings.length) return;

    var place = function () {
      rings.forEach(function (ring) {
        var sats = $$('.orbit__sat, .eco__tool', ring);
        if (!sats.length) return;
        var pct  = (parseFloat(ring.getAttribute('data-radius')) || 46) / 100;
        var box  = ring.getBoundingClientRect();
        /* on prend la plus petite dimension : sinon les pastilles sortent du cadre */
        var size = Math.min(box.width, box.height) || box.width;
        var rpx  = Math.round(size * pct);
        var off  = parseFloat(ring.getAttribute('data-offset')) || 0;
        sats.forEach(function (s, i) {
          s.style.setProperty('--a', ((360 / sats.length) * i + off) + 'deg');
          s.style.setProperty('--r', rpx + 'px');
        });
      });
    };

    place();
    window.addEventListener('resize', place, { passive: true });
    window.addEventListener('load', place);
  }

  /* ---------- 8. CONSTRUCTEUR DE MISSION (page Workers) ---------- */
  /* Chloé analyse l'objectif et compose l'équipe. Correspondances
     définies à partir des rôles réels des 17 Workers. */
  var MATCH = {
    boutique:  ['thomas', 'lucas', 'lea', 'maya', 'alex'],
    campagne:  ['maya', 'emma', 'lea', 'ines', 'alex'],
    reseaux:   ['emma', 'lea', 'seoya', 'ines'],
    projet:    ['yanis', 'noah', 'clara', 'dario'],
    automatiser:['rayan', 'sam', 'noah', 'ines'],
    site:      ['lucas', 'lea', 'seoya', 'sam'],
    recrutement:['sophie', 'noah', 'clara'],
    client:    ['nora', 'emma', 'alex']
  };

  function missionBuilder() {
    var root = $('[data-mission]');
    if (!root) return;
    var chips  = $$('[data-goal]', root);
    var out    = $('[data-mission-out]', root);
    var team   = $('[data-mission-team]', root);
    var verdict= $('[data-mission-verdict]', root);
    if (!out || !team) return;

    var pool = {};
    $$('[data-worker]', document).forEach(function (el) {
      pool[el.getAttribute('data-worker')] = {
        nom:  el.getAttribute('data-nom')  || '',
        role: el.getAttribute('data-role') || '',
        img:  el.getAttribute('data-img')  || ''
      };
    });

    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        chips.forEach(function (c) { c.classList.toggle('is-on', c === chip); });
        var key = chip.getAttribute('data-goal');
        var ids = MATCH[key] || [];

        team.innerHTML = '';
        ids.forEach(function (id, i) {
          var w = pool[id];
          if (!w) return;
          var card = document.createElement('a');
          card.className = 'wcard rv';
          card.href = 'workers.html#' + id;
          card.innerHTML =
            '<span class="pf pf--sm pf--ring"><img src="' + w.img + '" alt="' + w.nom + ' — ' + w.role + '" loading="lazy"></span>' +
            '<span><span class="wcard__n">' + w.nom + '</span>' +
            '<span class="wcard__r">' + w.role + '</span></span>';
          team.appendChild(card);
          setTimeout(function () { card.classList.add('is-in'); }, 90 + i * 85);
        });

        if (verdict) {
          verdict.textContent = ids.length
            ? 'Chloé a composé une équipe de ' + ids.length + ' Workers pour cet objectif.'
            : '';
        }
        out.hidden = false;
        out.setAttribute('aria-live', 'polite');
      });
    });
  }

  /* ---------- 9. PROFIL WORKER OUVERT PAR L'URL (?worker=alex) ---------- */
  function openWorkerFromUrl() {
    var id = new URLSearchParams(location.search).get('worker');
    if (!id) return;
    var el = document.getElementById(id);
    if (el) {
      setTimeout(function () {
        el.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'center' });
        el.classList.add('is-target');
      }, 240);
    }
  }

  /* ---------- 10. FORMULAIRE CONTACT — sujets cliquables ---------- */
  function contactChips() {
    var wrap = $('[data-subject-chips]');
    if (!wrap) return;
    var hidden = $('#sujet');
    $$('.chip', wrap).forEach(function (chip) {
      chip.addEventListener('click', function () {
        $$('.chip', wrap).forEach(function (c) { c.classList.toggle('is-on', c === chip); });
        if (hidden) hidden.value = chip.textContent.trim();
      });
    });
  }

  /* ---------- 11. VIDÉO : lecture uniquement quand visible ---------- */
  function smartVideo() {
    var vids = $$('video[data-auto]');
    if (!vids.length || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var v = en.target;
        if (en.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        else v.pause();
      });
    }, { threshold: 0.25 });
    vids.forEach(function (v) { io.observe(v); });
  }

  /* ---------- 12. ANCRES INTERNES ---------- */
  function anchors() {
    $$('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var id = a.getAttribute('href');
        if (id.length < 2) return;
        var t = document.querySelector(id);
        if (!t) return;
        e.preventDefault();
        t.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' });
      });
    });
  }

  /* ---------- 13. ANNÉE DU FOOTER ---------- */
  function year() {
    $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
  }

  /* ---------- INIT ---------- */
  function init() {
    header(); mobileNav(); reveal(); parallax(); carousels();
    filters(); orbit(); missionBuilder(); openWorkerFromUrl();
    contactChips(); smartVideo(); anchors(); year();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
