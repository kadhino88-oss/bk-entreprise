/* ============================================================
   BK ENTREPRISE — COMPORTEMENTS COMMUNS
   Header réactif · menu mobile · animations au scroll · devise selon le pays
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

  /* ---------- 5. CAROUSEL (flèches, molette, glisser, clavier) ---------- */
  function carousels() {
    $$('.car').forEach(function (car) {
      var track = $('.car__track', car);
      if (!track) return;
      // Les boutons ← → sont dans un bandeau AU-DESSUS du carousel (frère, pas enfant,
      // du .car) : on cherche donc dans la section entière, pas seulement dans .car.
      var scope = car.closest('.sec') || car.parentElement || car;
      var prev  = $('[data-car="prev"]', scope);
      var next  = $('[data-car="next"]', scope);

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
    var params = new URLSearchParams(location.search);
    var selected = params.get('prestation');
    if (selected) {
      $$('input[type="radio"][name="sujet"]').forEach(function (radio) {
        if (radio.value === selected) radio.checked = true;
      });
    }
    var campaign = ['utm_source', 'utm_medium', 'utm_campaign'].map(function (key) {
      var value = params.get(key);
      return value ? key + '=' + value.replace(/[^a-zA-Z0-9_. -]/g, '').slice(0, 80) : '';
    }).filter(Boolean).join('; ');
    var source = $('#source-campagne');
    if (source && campaign) source.value = campaign;
    if (campaign) {
      $$('a[href^="contact.html"]').forEach(function (link) {
        var target = new URL(link.getAttribute('href'), location.href);
        ['utm_source', 'utm_medium', 'utm_campaign'].forEach(function (key) {
          var value = params.get(key);
          if (value) target.searchParams.set(key, value.replace(/[^a-zA-Z0-9_. -]/g, '').slice(0, 80));
        });
        link.href = target.pathname + target.search + target.hash;
      });
    }
    var pack = (params.get('pack') || '').replace(/[^\wÀ-ÿ’' .,-]/g, '').slice(0, 80);
    var packField = $('#pack-demande'), packNote = $('#pack-notice');
    if (pack && packField) {
      packField.value = pack;
      if (packNote) { packNote.textContent = 'Offre sélectionnée : ' + pack; packNote.hidden = false; }
    }
    var page = $('#page-demande');
    if (page) page.value = location.pathname;
  }

  /* ---------- 11. VIDÉO : lecture uniquement quand visible ---------- */
  function smartVideo() {
    var vids = $$('video[data-auto]');
    if (!vids.length) return;
    if (reduced) { vids.forEach(function (v) { v.pause(); }); return; }
    if (!('IntersectionObserver' in window)) return;
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

  function contactValidation() {
    var form = $('.contact-form');
    if (!form) return;
    var feedback = $('#contact-feedback');
    form.addEventListener('invalid', function () {
      if (feedback) feedback.textContent = 'La demande n’a pas encore été envoyée. Complétez les champs obligatoires : prestation, nom, e-mail et description du projet.';
    }, true);
    form.addEventListener('submit', function () {
      if (feedback) feedback.textContent = 'Ouverture de la vérification anti-spam. Terminez cette étape pour poursuivre l’envoi.';
    });
  }

  /* ---------- 14. DEVISE SELON LE PAYS ---------- */
  /* Le pays vient de /api/region (en-tête géographique de Vercel, non conservé).
     Repli : région de la langue du navigateur. Par défaut : CHF.
     Test : ?devise=EUR  ou  ?pays=FR */
  var EURO = 'AT BE HR CY EE FI FR DE GR IE IT LV LT LU MT NL PT SK SI ES MC SM VA AD ME BG'.split(' ');
  var OTHER = { CH: 'CHF', LI: 'CHF', GB: 'GBP', US: 'USD', CA: 'CAD', AU: 'AUD', MA: 'MAD',
                SN: 'XOF', CI: 'XOF', BJ: 'XOF', BF: 'XOF', ML: 'XOF', NE: 'XOF', TG: 'XOF', GW: 'XOF',
                CM: 'XAF', GA: 'XAF', CG: 'XAF', TD: 'XAF', CF: 'XAF', GQ: 'XAF' };
  /* Tranches de budget par devise : mêmes paliers, ordre de grandeur adapté. */
  var TIERS = { CHF: [1500, 3000, 6000], EUR: [1500, 3000, 6000], USD: [1500, 3000, 6000],
                GBP: [1500, 3000, 6000], CAD: [2000, 4000, 8000], AUD: [2000, 4000, 8000],
                MAD: [15000, 30000, 60000], XOF: [900000, 1800000, 3600000], XAF: [900000, 1800000, 3600000] };

  function currencyFor(country) {
    country = (country || '').toUpperCase();
    if (EURO.indexOf(country) > -1) return 'EUR';
    return OTHER[country] || (country ? 'USD' : 'CHF');
  }
  function fmt(n) { try { return n.toLocaleString('fr-FR'); } catch (e) { return String(n); } }

  /* Taux indicatifs depuis le franc suisse (prix de base, hors taxes) : à valider et à mettre à jour. */
  var RATES = { CHF: 1, EUR: 1.07, USD: 1.2, GBP: 0.92, CAD: 1.7, AUD: 1.85, MAD: 11.5, XOF: 700, XAF: 700 };
  function roundPrice(n) {
    var step = n < 100 ? 5 : n < 1000 ? 10 : n < 10000 ? 50 : n < 100000 ? 500 : 5000;
    return Math.round(n / step) * step;
  }

  function applyCurrency(cur) {
    if (!TIERS[cur]) cur = 'USD';
    document.documentElement.setAttribute('data-currency', cur);
    $$('[data-cur]').forEach(function (el) { el.textContent = cur; });
    var rate = RATES[cur] || 1;
    $$('[data-price]').forEach(function (el) {
      var base = parseFloat(el.getAttribute('data-price'));
      if (!isFinite(base)) return;
      var fixed = parseFloat(el.getAttribute('data-price-' + cur.toLowerCase()));
      el.textContent = fmt(isFinite(fixed) ? fixed : roundPrice(base * rate)) + ' ' + cur;
    });
    var t = TIERS[cur];
    $$('[data-cur-tpl]').forEach(function (el) {
      var txt = el.getAttribute('data-cur-tpl')
        .replace(/1[\s\u00a0\u202f]?500/, fmt(t[0]))
        .replace(/3[\s\u00a0\u202f]?000/, fmt(t[1]))
        .replace(/6[\s\u00a0\u202f]?000/, fmt(t[2]))
        .replace('{c}', cur);
      if (el.tagName === 'INPUT') el.value = txt; else el.textContent = txt;
    });
    var hid = $('#devise-visiteur');
    if (hid) hid.value = cur;
  }

  function currency() {
    if (!$('[data-cur]') && !$('[data-cur-tpl]') && !$('[data-price]')) return;
    var params = new URLSearchParams(location.search);
    var forced = (params.get('devise') || '').toUpperCase();
    if (forced && TIERS[forced]) { applyCurrency(forced); return; }
    var cached = null;
    try { cached = sessionStorage.getItem('bk-devise'); } catch (e) {}
    if (cached && TIERS[cached]) { applyCurrency(cached); return; }

    var finished = false;
    var done = function (country) {
      if (finished) return;
      finished = true;
      var cur = currencyFor(country);
      applyCurrency(cur);
      try { sessionStorage.setItem('bk-devise', cur); } catch (e) {}
    };
    var fromLang = function () {
      var m = /[-_]([A-Za-z]{2})\b/.exec(navigator.language || '');
      return m ? m[1] : '';
    };
    var pays = (params.get('pays') || '').toUpperCase();
    if (pays) { done(pays); return; }
    if (!window.fetch) { done(fromLang()); return; }
    var timer = setTimeout(function () { done(fromLang()); }, 1800);
    fetch('/api/region', { cache: 'no-store' })
      .then(function (r) { return r.ok ? r.json() : {}; })
      .then(function (d) { clearTimeout(timer); done((d && d.country) || fromLang()); })
      .catch(function () { clearTimeout(timer); done(fromLang()); });
  }

  /* Pré-sélection du diagnostic ou du pack depuis les boutons du site. */
  function bkPrefillSubject() {
    var selected = new URLSearchParams(window.location.search).get('prestation');
    if (!selected) return;
    // Le formulaire actuel utilise des boutons radio, les anciennes versions des chips.
    $$('input[type="radio"][name="sujet"]').forEach(function(el) {
      if (el.value === selected) {
        el.checked = true;
        el.dispatchEvent(new Event('change', { bubbles: true }));
      }
    });
    $$('[data-subject-chips] .chip').forEach(function(chip) {
      if (chip.textContent.trim() === selected) chip.click();
    });
    var chosen = $('#pack-demande');
    if (chosen) chosen.value = selected;
  }

  /* ---------- INIT ---------- */
  function init() {
    header(); mobileNav(); reveal(); carousels();
    filters(); orbit(); missionBuilder(); openWorkerFromUrl();
    contactChips(); bkPrefillSubject(); contactValidation(); smartVideo(); anchors(); year(); currency();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
