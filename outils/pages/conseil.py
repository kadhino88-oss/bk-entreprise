# -*- coding: utf-8 -*-
"""Page Conseil — une expérience visuelle : Comprendre → Structurer → Décider → Construire → Accompagner."""
from bk_build import page_hero, CTA_FINAL, shot_class

PAGE  = "conseil.html"
TITLE = "Conseil & stratégie digitale à Genève — BK Entreprise"
DESC  = ("Diagnostic, positionnement, stratégie digitale, cadrage et accompagnement pour commerces, "
         "associations et PME à Genève, en Suisse romande et en Haute-Savoie : structurer une idée pour la faire avancer.")
OG    = "images/project15.jpg"

PARCOURS = [
 ("01", "Comprendre", "On part de votre activité réelle : ce que vous vendez, à qui, avec quels moyens, "
  "et ce qui bloque aujourd'hui. Pas de méthode plaquée sur un cas qui n'est pas le vôtre."),
 ("02", "Structurer", "Le besoin devient un périmètre : ce qui est prioritaire, ce qui peut attendre, "
  "ce qui n'a pas lieu d'être. C'est souvent l'étape qui fait gagner le plus de temps."),
 ("03", "Décider", "Des options claires, avec ce que chacune coûte et ce qu'elle apporte. "
  "Vous décidez avec les éléments en main — pas sur une intuition."),
 ("04", "Construire", "Le plan se traduit en réalisations concrètes : site, identité, contenus, "
  "outils, automatisations. Mobilisées seules ou ensemble."),
 ("05", "Accompagner", "Un projet vit après sa livraison. Suivi, ajustements et évolutions "
  "au rythme de votre activité."),
]

LEVIERS = [
 ("◎", "Diagnostic", "État des lieux de votre présence : site, image, réseaux, outils, visibilité."),
 ("◈", "Positionnement", "Clarifier l'offre, l'image et le message — pour qui, pourquoi, en quoi différent."),
 ("◇", "Stratégie digitale", "Relier présence digitale, contenus, outils et objectifs dans un même plan."),
 ("◆", "Cadrage de projet", "Périmètre, étapes, priorités et budget réaliste avant de lancer quoi que ce soit."),
 ("▲", "Organisation", "Qui fait quoi, avec quels outils, et ce qui peut être automatisé."),
 ("★", "Plan d'action", "Une feuille de route datée, avec des étapes que vous pouvez suivre."),
]


def body():
    project25_alt = "Market Les Saveurs d’Afrik — version premium"
    project25_class = shot_class(project25_alt)
    etapes = "".join(f"""
      <div class="flow__step rv rv-d{min(i,6)}">
        <div class="flow__i">{n}</div>
        <div>
          <div class="flow__t">{t}</div>
          <div class="flow__d">{d}</div>
        </div>
      </div>""" for i, (n, t, d) in enumerate(PARCOURS, 1))

    leviers = "".join(f"""
      <div class="card rv rv-d{(i % 3) + 1}">
        <div class="card__i">{ico}</div>
        <div class="card__t">{t}</div>
        <p class="card__d">{d}</p>
      </div>""" for i, (ico, t, d) in enumerate(LEVIERS))

    return page_hero(
        eyebrow="Conseil &amp; Stratégie",
        title_html='Structurer une idée pour <span class="it">la faire avancer.</span>',
        lead=("BK accompagne le positionnement, la stratégie digitale, la structuration d'un projet "
              "et la mise en cohérence des différents leviers."),
        cta1=("contact.html", "Parler de mon projet"),
        cta2=("#parcours", "Voir la démarche ↓"),
    ) + f"""
<!-- ===== LE PARCOURS ===== -->
<section class="sec sec--dark" id="parcours">
  <div class="halo halo--gold" style="width:560px;height:560px;top:-180px;left:-170px;"></div>
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">01 — La démarche</span>
      <h2 class="h-lg" style="margin-top:22px;">Comprendre, structurer, <span class="it">décider.</span></h2>
      <p class="lead">Cinq étapes, dans cet ordre. Chacune sert à rendre la suivante plus simple.</p>
    </div>
    <div class="flow">{etapes}</div>
  </div>
</section>

<!-- ===== LES LEVIERS ===== -->
<section class="sec sec--cream">
  <div class="halo halo--warm" style="width:480px;height:480px;bottom:-170px;right:-150px;"></div>
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">02 — Les leviers</span>
      <h2 class="h-lg" style="margin-top:22px;">Six angles pour <span class="it">y voir clair.</span></h2>
      <p class="lead">Selon la situation, on en active un seul — ou plusieurs ensemble.</p>
    </div>
    <div class="cards">{leviers}</div>
  </div>
</section>

<!-- ===== CE QUE ÇA CHANGE ===== -->
<section class="sec sec--night">
  <div class="wrap">
    <div class="split">
      <div class="rv">
        <span class="eyebrow">03 — Concrètement</span>
        <h2 class="h-md" style="margin-top:20px;">Le conseil ne s'arrête pas <span class="it">au document.</span></h2>
        <p class="lead" style="margin-top:20px;">
          Une recommandation qui reste dans un fichier ne change rien. Chez BK, le conseil débouche
          sur des réalisations : un site refondu, une identité clarifiée, des contenus produits,
          des outils reliés entre eux.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:32px;">
          <a class="btn btn--gold" href="contact.html">Demander un diagnostic <span class="arr">↗</span></a>
          <a class="btn btn--ghost" href="portfolio.html">Voir des projets aboutis</a>
        </div>
      </div>
      <div class="rv rv--r rv-d1" data-px="0.05">
        <div class="shot shot--4x3{project25_class}"><img src="images/project25.jpg" alt="{project25_alt}" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>
""" + CTA_FINAL
