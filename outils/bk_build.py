#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BK ENTREPRISE — générateur de pages.
Garantit un header, un footer et un <head> strictement identiques sur
toutes les pages. Les contenus propres à chaque page vivent dans
outils/pages/<nom>.py et les réalisations dans data-realisations.json.

Usage :  python3 outils/bk_build.py            (génère toutes les pages)
         python3 outils/bk_build.py contact    (une seule page)
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = [
    ("index.html",       "Accueil"),
    ("expertises.html",  "Expertises"),
    ("portfolio.html",   "Réalisations"),
    ("services-it.html", "IT &amp; Digital"),
    ("conseil.html",     "Conseil"),
    ("evenement.html",   "Événementiel"),
    ("workers.html",     "Workers"),
    ("integrations.html","Intégrations"),
    ("profil.html",      "Profil"),
    ("contact.html",     "Contact"),
]
# Navigation visible en haut (Accueil = logo, Contact = bouton)
NAV_TOP = [n for n in NAV if n[0] not in ("index.html", "contact.html")]


NOINDEX = {"merci.html"}   # pages de confirmation : utiles au visiteur, pas à Google

# Données réelles de l'entreprise (identiques au footer) — utilisées pour le
# balisage Schema.org / LocalBusiness, un signal de référencement local pour Google.
JSONLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "BK Entreprise",
  "image": "https://www.bk-entreprise.com/images/logo.png",
  "logo": "https://www.bk-entreprise.com/images/logo.png",
  "url": "https://www.bk-entreprise.com/",
  "telephone": "+41799349946",
  "email": "contact@bk-entreprise.com",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rue Joseph Pasquier 1",
    "postalCode": "1203",
    "addressLocality": "Genève",
    "addressCountry": "CH"
  },
  "areaServed": ["Genève", "Suisse romande", "Haute-Savoie"],
  "sameAs": [
    "https://www.instagram.com/bk_entreprise7/",
    "https://www.tiktok.com/@bkentreprise7",
    "https://www.facebook.com/profile.php?id=61576414298574"
  ],
  "description": "Agence digitale et créative à Genève : sites web, identités visuelles, communication, IT et agents IA pour commerces, restaurants, marques et associations."
}
</script>"""


def head(page, title, desc, og_image="images/project5.jpg"):
    robots = '\n<meta name="robots" content="noindex, follow">' if page in NOINDEX else ""
    jsonld = "" if page in NOINDEX else f"\n{JSONLD}"
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{robots}
<link rel="canonical" href="https://www.bk-entreprise.com/{page}">
<meta name="geo.region" content="CH-GE">
<meta name="geo.placename" content="Genève">

<meta property="og:type" content="website">
<meta property="og:site_name" content="BK Entreprise">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://www.bk-entreprise.com/{page}">
<meta property="og:image" content="https://www.bk-entreprise.com/{og_image}">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="images/logo.png">
<link rel="preload" href="fonts/inter-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/instrument-serif-latin-400-italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="bk.css">{jsonld}
</head>
<body>
"""


def header(page, light=True):
    """light=True : pages internes (hero sombre mais court).
    light=False : accueil, dont le hero vidéo occupe tout l'écran."""
    cls = "hdr hdr--light" if light else "hdr"
    cur = ' aria-current="page"'
    links = "".join(
        '\n      <a href="%s"%s>%s</a>' % (h, cur if h == page else "", t)
        for h, t in NAV_TOP
    )
    mob = "".join(
        '\n  <a href="%s"%s>%s <span>%02d</span></a>' % (h, cur if h == page else "", t, i)
        for i, (h, t) in enumerate(NAV, 1)
    )
    return f"""<!-- ===== HEADER COMMUN ===== -->
<header class="{cls}">
  <div class="wrap hdr__in">
    <a class="hdr__logo" href="index.html"><img src="images/logo.png" alt="BK Entreprise"></a>
    <nav class="hdr__nav" aria-label="Navigation principale">{links}
    </nav>
    <a class="btn btn--gold hdr__cta" href="contact.html">Parler à BK <span class="arr">↗</span></a>
    <button class="hdr__burger" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mnav"><span></span></button>
  </div>
</header>

<nav class="mnav" id="mnav" aria-label="Menu mobile">{mob}
  <a class="btn btn--gold mnav__cta" href="contact.html">Parler à BK ↗</a>
</nav>

<main>
"""


FOOTER = """</main>

<!-- ===== FOOTER COMMUN ===== -->
<footer class="ftr">
  <div class="wrap">
    <div class="ftr__top">
      <div class="ftr__brand">
        <img src="images/logo.png" alt="BK Entreprise">
        <p class="ftr__tag">Des idées aux résultats.</p>
        <div class="ftr__soc">
          <a href="https://www.instagram.com/bk_entreprise7/" target="_blank" rel="noopener">Instagram</a>
          <a href="https://www.tiktok.com/@bkentreprise7" target="_blank" rel="noopener">TikTok</a>
          <a href="https://www.facebook.com/profile.php?id=61576414298574" target="_blank" rel="noopener">Facebook</a>
        </div>
        <div class="ftr__contact">
          <a href="tel:+41799349946">+41 79 934 99 46</a><br>
          <a href="mailto:contact@bk-entreprise.com">contact@bk-entreprise.com</a><br>
          Rue Joseph Pasquier 1, 1203 Genève
        </div>
      </div>

      <div>
        <h4>Expertises</h4>
        <ul>
          <li><a href="services-it.html">Web &amp; Digital</a></li>
          <li><a href="expertises.html#design">Design &amp; Identité</a></li>
          <li><a href="expertises.html#communication">Communication</a></li>
          <li><a href="services-it.html#it">IT &amp; Technologie</a></li>
          <li><a href="workers.html">IA &amp; Automatisation</a></li>
          <li><a href="conseil.html">Conseil &amp; Stratégie</a></li>
        </ul>
      </div>

      <div>
        <h4>Réalisations</h4>
        <ul>
          <li><a href="portfolio.html">Tous les projets</a></li>
          <li><a href="evenement.html">Événementiel</a></li>
          <li><a href="portfolio.html#identite">Identité visuelle</a></li>
          <li><a href="portfolio.html#video">Contenus vidéo</a></li>
        </ul>
      </div>

      <div>
        <h4>Workers</h4>
        <ul>
          <li><a href="workers.html">Les 18 Workers</a></li>
          <li><a href="workers.html#chloe">Chloé — Agent Maître</a></li>
          <li><a href="workers.html#mission">Créer une mission</a></li>
          <li><a href="integrations.html">Intégrations</a></li>
        </ul>
      </div>

      <div>
        <h4>Entreprise</h4>
        <ul>
          <li><a href="profil.html">À propos</a></li>
          <li><a href="conseil.html">Conseil</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="index.html">Accueil</a></li>
        </ul>
      </div>
    </div>

    <div class="ftr__bot">
      <span>© <span data-year>2026</span> BK Entreprise — Tous droits réservés.</span>
      <em>Des idées aux résultats.</em>
      <a class="totop" href="#" aria-label="Revenir en haut">↑</a>
    </div>
  </div>
</footer>

<script src="bk.js"></script>
</body>
</html>
"""


def page_hero(eyebrow, title_html, lead, cta1=("contact.html", "Parler à BK"), cta2=None):
    """Hero commun aux pages internes — même ADN que la homepage, sans vidéo."""
    b2 = f'<a class="btn btn--ghost" href="{cta2[0]}">{cta2[1]}</a>' if cta2 else ""
    return f"""
<section class="sec sec--night" style="padding-top:clamp(140px,15vw,210px);">
  <div class="halo halo--gold" style="width:620px;height:620px;top:-220px;right:-180px;"></div>
  <div class="halo halo--night" style="width:520px;height:520px;bottom:-200px;left:-160px;"></div>
  <div class="wrap">
    <span class="eyebrow rv">{eyebrow}</span>
    <h1 class="h-xl rv rv-d1" style="margin-top:24px;max-width:18ch;">{title_html}</h1>
    <p class="lead rv rv-d2" style="margin-top:26px;">{lead}</p>
    <div class="rv rv-d3" style="display:flex;flex-wrap:wrap;gap:14px;margin-top:38px;">
      <a class="btn btn--gold" href="{cta1[0]}">{cta1[1]} <span class="arr">↗</span></a>
      {b2}
    </div>
  </div>
</section>
"""


CTA_FINAL = """
<section class="sec sec--sand">
  <div class="halo halo--gold" style="width:560px;height:560px;top:-200px;left:50%;transform:translateX(-50%);"></div>
  <div class="wrap" style="text-align:center;">
    <span class="eyebrow rv" style="justify-content:center;">BK Entreprise</span>
    <h2 class="h-lg rv rv-d1" style="margin-top:22px;max-width:16ch;margin-inline:auto;">Un besoin <span class="it">précis ?</span></h2>
    <p class="lead rv rv-d2" style="margin:22px auto 0;">
      Décrivez votre objectif, votre activité ou votre projet. BK peut intervenir sur
      une expertise seule ou réunir plusieurs compétences.
    </p>
    <div class="rv rv-d3" style="display:flex;flex-wrap:wrap;gap:14px;justify-content:center;margin-top:38px;">
      <a class="btn btn--gold" href="contact.html">Parler de mon projet <span class="arr">↗</span></a>
      <a class="btn btn--ghost" href="portfolio.html">Voir les réalisations</a>
    </div>
  </div>
</section>
"""


def realisations():
    with open(os.path.join(ROOT, "data-realisations.json"), encoding="utf-8") as f:
        return json.load(f)


# Réalisations dont le visuel est un logo, un écusson, une affiche ou tout visuel avec du
# texte/contenu jusqu'aux bords : object-fit:contain (via --contain) pour ne JAMAIS rien couper.
LOGO_TITLES = {
    "DK Tendance",
    "Abiba Hair",
    # Nom de marque seul (sans suffixe "— Logo" / "— identité" / "— version premium"...)
    # pour matcher toutes les reformulations d'une page à l'autre.
    "Market Les Saveurs d’Afrik",
    "Market Les Saveurs d’Afrik — Logo",
    "Market Les Saveurs d’Afrik — Version premium",
    "AIHS",
    "AIHS — Association des Ivoiriens de Haute-Savoie",
    "AIHS — Logo officiel",
    "Restaurant Le Baron",
    "Chez Édouard — Le 225 — Logo",
    "Savoyard Cup — Soccer",
    # Affiches/visuels portrait (posters) écrasés dans des cadres 4:3 ou 4:5 — texte coupé sinon.
    "BK Entreprise — Solutions créatives",
    "Trésors by Ninel",
    "Trésor by Ninel",
    "Zouglou Live — Garba Party",
}


def _norm(s):
    """Normalise apostrophes et casse pour que la comparaison de titres ne rate rien
    (les libellés diffèrent légèrement d'une page à l'autre : majuscule/minuscule, etc.)."""
    return s.replace("’", "'").lower()


def _is_logo(texte):
    t = _norm(texte)
    return any(_norm(lt) in t or t in _norm(lt) for lt in LOGO_TITLES)


def media_class(titre):
    """Classe additionnelle à ajouter à .car__media pour ce titre, si c'est un logo/écusson.
    Comparaison souple (sous-chaîne, apostrophes normalisées) pour couvrir les titres
    raccourcis ou réécrits d'une page à l'autre."""
    return " car__media--contain" if _is_logo(titre) else ""


def shot_class(texte):
    """Équivalent de media_class() pour les visuels affichés via .shot (pas .car__media)."""
    return " shot--contain" if _is_logo(texte) else ""


def build(page, title, desc, body, og="images/project5.jpg", light=True):
    html = head(page, title, desc, og) + header(page, light) + body + FOOTER
    path = os.path.join(ROOT, page)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path, len(html)


if __name__ == "__main__":
    import importlib.util
    only = sys.argv[1:] or None
    pdir = os.path.join(ROOT, "outils", "pages")
    names = sorted(f[:-3] for f in os.listdir(pdir) if f.endswith(".py"))
    for n in names:
        if only and n not in only:
            continue
        spec = importlib.util.spec_from_file_location(n, os.path.join(pdir, n + ".py"))
        mod = importlib.util.module_from_spec(spec)
        sys.modules[n] = mod
        spec.loader.exec_module(mod)
        p, size = build(mod.PAGE, mod.TITLE, mod.DESC, mod.body(),
                        getattr(mod, "OG", "images/project5.jpg"),
                        getattr(mod, "LIGHT_HEADER", True))
        print(f"  ✓ {os.path.basename(p):<22} {size/1024:6.1f} Ko")
