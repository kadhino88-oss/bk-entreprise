# -*- coding: utf-8 -*-
"""Page Événementiel — les réalisations événementielles réelles, en carousel."""
from bk_build import page_hero, CTA_FINAL, media_class

PAGE  = "evenement.html"
TITLE = "Événementiel — BK Entreprise"
DESC  = ("Affiches, flyers, univers visuels et communication pour vos événements : "
         "soirées, galas de charité, tournois et initiatives associatives.")
OG    = "images/project7.jpg"

# Réalisations événementielles réelles — noms exacts
EVENTS = [
 ("images/project7.jpg",  "Zouglou Live — Garba Party", "Soirée",
  "Un visuel qui porte l'énergie du rendez-vous : couleurs chaudes, typographie vivante, "
  "informations pratiques lisibles au premier coup d'œil."),
 ("images/project17.jpg", "Association Cœur d’Or Dalet — Dîner Gala de Charité", "Gala",
  "Une direction artistique plus solennelle, adaptée à un dîner de gala, sans perdre la chaleur "
  "de l'événement associatif."),
 ("images/project18.jpg", "Association Akouani", "Associatif",
  "Un visuel construit autour de l'humain et du lien, pour porter une vision associative."),
 ("images/project20.jpg", "Savoyard Cup — Soccer", "Sport",
  "Un écusson dans les codes du football : or, relief et lisibilité même en petit format."),
 ("images/project9.png",  "Association des Ivoiriens de Haute-Savoie — Un don, une goutte d’espoir", "Solidarité",
  "Une affiche de collecte qui explique la cause, montre son impact et donne les moyens d'agir."),
 ("images/project14.png", "Ô Saveurs d’Afrique — Noël solidaire", "Solidarité",
  "Un flyer de repas solidaire : message clair, ambiance de fête et informations essentielles."),
]

PRESTATIONS = [
 ("◎", "Organisation", "Cadrage de l'événement, rétroplanning et points de passage."),
 ("◈", "Coordination", "Suivi des prestataires, des supports et des échéances."),
 ("◆", "Affiches &amp; flyers", "Supports imprimés pensés pour être lisibles de loin comme de près."),
 ("▲", "Univers visuel", "Une direction cohérente déclinée sur tous les supports."),
 ("★", "Promotion digitale", "Déclinaisons pour Instagram, Facebook et TikTok."),
 ("◇", "Contenus sur place", "Photo et vidéo pour faire vivre l'événement après sa fin."),
]


def body():
    cards = "".join(f"""
        <a class="car__item" href="portfolio.html">
          <div class="car__media{media_class(t)}"><img src="{img}" alt="{t}" loading="lazy"></div>
          <div class="car__cap"><div class="car__cat">{cat}</div><div class="car__t">{t}</div></div>
        </a>""" for img, t, cat, _ in EVENTS)

    details = "".join(f"""
      <div class="card rv rv-d{(i % 3) + 1}">
        <div class="card__i">{ico}</div>
        <div class="card__t">{t}</div>
        <p class="card__d">{d}</p>
      </div>""" for i, (ico, t, d) in enumerate(PRESTATIONS))

    focus = "".join(f"""
      <div class="xp__row rv rv-d{(i % 5) + 1}" style="cursor:default;">
        <span class="xp__n">{i + 1:02d}</span>
        <span><span class="xp__t" style="font-size:clamp(1.05rem,1.8vw,1.35rem);">{t}</span>
        <span class="xp__d">{d}</span></span>
        <span></span>
      </div>""" for i, (_, t, _, d) in enumerate(EVENTS))

    return page_hero(
        eyebrow="Événementiel",
        title_html='Donner à votre événement une image <span class="it">qui rassemble.</span>',
        lead=("Création de supports visuels, coordination et communication pour présenter, "
              "promouvoir et accompagner vos événements — avant, pendant et après."),
        cta1=("contact.html", "Parler de mon événement"),
        cta2=("#realisations", "Voir les réalisations ↓"),
    ) + f"""
<!-- ===== CAROUSEL DES ÉVÉNEMENTS ===== -->
<section class="sec" id="realisations">
  <div class="wrap">
    <div class="sec-head rv" style="max-width:none;display:flex;flex-wrap:wrap;gap:24px;align-items:flex-end;justify-content:space-between;">
      <div style="max-width:640px;">
        <span class="eyebrow">01 — Réalisations événementielles</span>
        <h2 class="h-lg" style="margin-top:22px;">Des événements qui ont <span class="it">leur image.</span></h2>
      </div>
      <div class="car__nav" style="margin-bottom:6px;">
        <button class="car__btn" data-car="prev" aria-label="Événement précédent">←</button>
        <button class="car__btn" data-car="next" aria-label="Événement suivant">→</button>
      </div>
    </div>

    <div class="car rv rv-d1">
      <div class="car__track" role="list" aria-label="Réalisations événementielles">{cards}
      </div>
    </div>
  </div>
</section>

<!-- ===== CE QUE BK PREND EN CHARGE ===== -->
<section class="sec sec--night">
  <div class="halo halo--gold" style="width:540px;height:540px;top:-190px;right:-160px;"></div>
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">02 — Prestations</span>
      <h2 class="h-lg" style="margin-top:22px;">De l'affiche à la <span class="it">présence terrain.</span></h2>
      <p class="lead">Selon l'événement, BK intervient sur un seul volet ou sur l'ensemble.</p>
    </div>
    <div class="cards">{details}</div>
  </div>
</section>

<!-- ===== DÉTAIL DE CHAQUE PROJET ===== -->
<section class="sec sec--cream">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">03 — Le détail</span>
      <h2 class="h-lg" style="margin-top:22px;">Chaque événement a <span class="it">sa contrainte.</span></h2>
    </div>
    <div class="xp">{focus}</div>
  </div>
</section>
""" + CTA_FINAL
