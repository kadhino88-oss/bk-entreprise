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
  "et ce qui bloque aujourd'hui. Pas de méthode plaquée sur un cas qui n'est pas le vôtre.",
  "Concrètement, un échange direct (appel ou visite) suffit souvent à cette étape : vos chiffres "
  "s'ils existent, vos retours clients, le temps que vous passez sur les tâches qui ne rapportent pas, "
  "l'image que vous donnez aujourd'hui face à celle que vous voulez donner. Aucun questionnaire "
  "générique — les questions changent selon que vous êtes un commerce, une association ou une TPE en "
  "création."),
 ("02", "Structurer", "Le besoin devient un périmètre : ce qui est prioritaire, ce qui peut attendre, "
  "ce qui n'a pas lieu d'être. C'est souvent l'étape qui fait gagner le plus de temps.",
  "Le résultat est écrit noir sur blanc : un périmètre daté, avec ce qui entre dans le projet et ce qui "
  "en sort explicitement — pour éviter qu'un projet grossisse en cours de route sans que personne ne "
  "l'ait décidé. Les risques connus (délai serré, budget contraint, dépendance à un tiers) sont "
  "nommés avant de commencer, pas découverts en chemin."),
 ("03", "Décider", "Des options claires, avec ce que chacune coûte et ce qu'elle apporte. "
  "Vous décidez avec les éléments en main — pas sur une intuition.",
  "En pratique, deux ou trois options sont posées côte à côte : ce que chacune implique en budget, "
  "en délai et en résultat attendu. Pas de recommandation unique imposée d'en haut — l'idée est que "
  "vous compreniez le compromis derrière chaque choix, pour trancher en connaissance de cause plutôt "
  "que de faire confiance à l'aveugle."),
 ("04", "Construire", "Le plan se traduit en réalisations concrètes : site, identité, contenus, "
  "outils, automatisations. Mobilisées seules ou ensemble.",
  "Chaque chantier a un responsable identifié (BK ou vous), un jalon et un point de validation avant "
  "de passer au suivant. Vous voyez l'avancement au fur et à mesure — pas seulement un livrable final "
  "après plusieurs semaines de silence."),
 ("05", "Accompagner", "Un projet vit après sa livraison. Suivi, ajustements et évolutions "
  "au rythme de votre activité.",
  "Une fois en ligne ou en place, un projet continue de rencontrer la réalité : des retours clients, "
  "une saison qui change la donne, un concurrent qui bouge. Le suivi consiste à ajuster ce qui doit "
  "l'être, au rythme réel de votre activité — pas selon un calendrier de maintenance figé à l'avance."),
]

LEVIERS = [
 ("◎", "Diagnostic", "État des lieux de votre présence : site, image, réseaux, outils, visibilité.",
  "Le diagnostic passe en revue ce qui existe déjà — votre site s'il y en a un, votre fiche Google, "
  "vos réseaux, vos outils du quotidien — et ce qui manque. Le rendu est un constat lisible, pas un "
  "audit de 40 pages que personne ne lit : ce qui fonctionne, ce qui freine, et par quoi commencer."),
 ("◈", "Positionnement", "Clarifier l'offre, l'image et le message — pour qui, pourquoi, en quoi différent.",
  "Trois questions structurent ce travail : à qui vous adressez-vous précisément, qu'est-ce qui vous "
  "distingue de la structure équivalente à côté, et ce message est-il le même partout où l'on vous "
  "trouve (site, réseaux, devanture, bouche-à-oreille) ? La plupart des flous viennent d'un "
  "positionnement jamais formulé clairement."),
 ("◇", "Stratégie digitale", "Relier présence digitale, contenus, outils et objectifs dans un même plan.",
  "Plutôt que d'être présent partout sans priorité, la stratégie choisit les canaux qui comptent "
  "réellement pour votre activité et votre budget, et fixe ce que chacun doit produire comme résultat "
  "— visibilité, contact, vente — pour que chaque action se juge sur un objectif clair."),
 ("◆", "Cadrage de projet", "Périmètre, étapes, priorités et budget réaliste avant de lancer quoi que ce soit.",
  "Le livrable est un cahier des charges concret : ce qui est inclus, un calendrier par étapes et une "
  "enveloppe budgétaire réaliste — pour que le prestataire (BK ou un autre) sache exactement ce qu'il "
  "doit produire, et que vous puissiez comparer des devis sur la même base."),
 ("▲", "Organisation", "Qui fait quoi, avec quels outils, et ce qui peut être automatisé.",
  "On regarde les tâches répétitives qui prennent du temps sans valeur ajoutée — relances, rappels, "
  "mises à jour de fichiers, publications — et ce qui peut être repris par un outil ou un Worker IA, "
  "pour que votre temps aille vers ce qui compte réellement."),
 ("★", "Plan d'action", "Une feuille de route datée, avec des étapes que vous pouvez suivre.",
  "Le format reste simple à utiliser au quotidien : des étapes datées, un responsable par étape, et "
  "des points de passage pour vérifier que le projet avance comme prévu — sans jargon de gestion de "
  "projet inutile pour une petite structure."),
]


def body():
    conseil_img_alt = "Chez Édouard — Le 225 — Logo créé par BK Entreprise"
    conseil_img_class = shot_class(conseil_img_alt)
    etapes = "".join(f"""
      <div class="flow__step rv rv-d{min(i,6)}">
        <div class="flow__i">{n}</div>
        <div>
          <div class="flow__t">{t}</div>
          <div class="flow__d">{d}</div>
          <details class="detail-toggle">
            <summary>En savoir plus <span class="arr">↗</span></summary>
            <p class="detail-more">{plus}</p>
          </details>
        </div>
      </div>""" for i, (n, t, d, plus) in enumerate(PARCOURS, 1))

    leviers = "".join(f"""
      <div class="card rv rv-d{(i % 3) + 1}">
        <div class="card__i">{ico}</div>
        <div class="card__t">{t}</div>
        <p class="card__d">{d}</p>
        <details class="detail-toggle">
          <summary>En savoir plus <span class="arr">↗</span></summary>
          <p class="detail-more">{plus}</p>
        </details>
      </div>""" for i, (ico, t, d, plus) in enumerate(LEVIERS))

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
        <div class="shot shot--4x3{conseil_img_class}"><img src="images/project22.png" alt="{conseil_img_alt}" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>
""" + CTA_FINAL
