# -*- coding: utf-8 -*-
"""Page Réalisations — les 23 créations avec leurs noms exacts + les 8 vidéos."""
from bk_build import page_hero, CTA_FINAL, realisations, media_class

PAGE  = "portfolio.html"
TITLE = "Réalisations — BK Entreprise, Genève"
DESC  = ("Les créations de BK Entreprise : identités visuelles, affiches et flyers événementiels, "
         "menus, supports imprimés et contenus vidéo pour commerces, restaurants et associations.")
OG    = "images/project6.jpg"

# Ordre d'affichage des filtres
CATS = ["Identité", "Communication", "Événementiel", "Associatif",
        "Restauration", "Beauté", "Sport", "Édition"]


def body():
    data = realisations()
    items = data["realisations"]
    videos = data["videos"]

    # --- barre de filtres ---
    def slug(c):
        import unicodedata
        s = unicodedata.normalize("NFKD", c).encode("ascii", "ignore").decode().lower()
        return s.replace(" ", "-")

    chips = ['<button class="chip is-on" data-f="*" data-slug="tout">Tout <span style="opacity:.6">%d</span></button>' % len(items)]
    ancres = ['<span id="creations-liste"></span>']
    for c in CATS:
        n = sum(1 for i in items if i["cat"] == c)
        if n:
            chips.append('<button class="chip" data-f="%s" data-slug="%s">%s <span style="opacity:.6">%d</span></button>'
                         % (c, slug(c), c, n))
            # ancre profonde : portfolio.html#identite active le filtre Identité
            ancres.append('<span id="%s" style="display:block;height:0;scroll-margin-top:120px;"></span>' % slug(c))
    filtre = "".join(ancres) + '<div class="chips" data-filter-bar>%s</div>' % "".join(chips)

    # --- grille des réalisations ---
    cards = []
    for k, it in enumerate(items):
        delay = " rv-d%d" % ((k % 3) + 1)
        cards.append(f"""
      <figure class="car__item rv{delay}" data-cat="{it['cat']}" style="flex:none;width:auto;">
        <div class="car__media{media_class(it['titre'])}" style="aspect-ratio:4/5;">
          <img src="{it['img']}" alt="{it['titre']} — réalisation BK Entreprise" loading="lazy">
        </div>
        <figcaption class="car__cap">
          <div class="car__cat">{it['cat']}</div>
          <div class="car__t">{it['titre']}</div>
        </figcaption>
      </figure>""")
    grille = "".join(cards)

    # --- vidéos ---
    vids = []
    for k, v in enumerate(videos):
        poster = ' poster="images/hero-poster.jpg"' if "hero" in v["src"] else ""
        vids.append(f"""
        <figure class="shot shot--16x9 rv rv-d{(k % 3) + 1}" style="margin:0;">
          <video src="{v['src']}"{poster} controls preload="metadata" playsinline
                 aria-label="{v['titre']} — BK Entreprise"></video>
        </figure>""")
    videos_html = "".join(vids)

    return page_hero(
        eyebrow="Réalisations",
        title_html='Des créations qui parlent <span class="it">d\'elles-mêmes.</span>',
        lead=("Identités visuelles, affiches et flyers, menus, supports imprimés et contenus vidéo — "
              "réalisés pour des commerces, des restaurants, des associations et des événements."),
        cta1=("contact.html", "Démarrer un projet"),
        cta2=("#creations", "Voir les créations ↓"),
    ) + f"""
<!-- ===== GRILLE DES 23 CRÉATIONS ===== -->
<section class="sec" id="creations">
  <div class="wrap">
    <div class="sec-head rv" style="max-width:none;display:flex;flex-wrap:wrap;gap:24px;align-items:flex-end;justify-content:space-between;">
      <div style="max-width:620px;">
        <span class="eyebrow">01 — Créations</span>
        <h2 class="h-lg" style="margin-top:22px;">Chaque projet porte <span class="it">son vrai nom.</span></h2>
      </div>
    </div>

    <div class="rv rv-d1" style="margin-bottom:36px;--tx-inv:var(--tx);--line-dark:var(--line);">
      {filtre}
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:22px;">{grille}
    </div>
  </div>
</section>

<!-- ===== CONTENUS VIDÉO ===== -->
<section class="sec sec--night" id="video">
  <div class="halo halo--warm" style="width:520px;height:520px;top:-160px;right:-160px;"></div>
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">02 — Contenus vidéo</span>
      <h2 class="h-lg" style="margin-top:22px;">L'image <span class="it">en mouvement.</span></h2>
      <p class="lead">Montages, présentations et formats courts produits pour les réseaux et les campagnes.</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px;">{videos_html}
    </div>
  </div>
</section>
""" + CTA_FINAL
