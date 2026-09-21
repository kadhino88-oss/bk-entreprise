# -*- coding: utf-8 -*-
"""Page Expertises — les 7 domaines, chacun avec une vraie section visuelle."""
from bk_build import page_hero, CTA_FINAL, shot_class

PAGE  = "expertises.html"
TITLE = "Identité visuelle & expertises digitales à Genève | BK Entreprise"
DESC  = ("Identité visuelle, création de site web, communication, IT, IA & automatisation, conseil et "
         "événementiel : les sept expertises de BK Entreprise à Genève, mobilisables seules ou combinées.")
OG    = "images/project8.jpg"

# (ancre, numéro, titre, accroche, texte, [prestations], image, légende image, lien, libellé lien)
XP = [
 ("web", "01", "Web &amp; Digital", "Créer une présence qui travaille <span class=\"it\">pour vous.</span>",
  "Sites vitrines, boutiques en ligne, interfaces et expériences digitales conçues pour présenter "
  "votre activité avec clarté et donner une vraie place à votre image.",
  ["Sites vitrines et institutionnels", "Boutiques e-commerce", "Applications et prototypes mobiles",
   "Refonte et modernisation", "Optimisation et performance"],
  "images/project5.jpg", "Création digitale BK Entreprise", "services-it.html", "Découvrir le web &amp; digital"),

 ("design", "02", "Design &amp; Identité", "Donner une identité reconnaissable à <span class=\"it\">votre activité.</span>",
  "Logos, supports, visuels et directions graphiques pensés pour construire une image cohérente, "
  "lisible et mémorable — du premier croquis au fichier prêt à imprimer.",
  ["Logos et chartes graphiques", "Affiches, flyers et menus", "Supports imprimés et cartes de visite",
   "Déclinaisons réseaux sociaux", "Direction artistique"],
  "images/project19.jpg", "Restaurant Le Baron — logo créé par BK Entreprise", "portfolio.html#identite", "Voir les créations"),

 ("communication", "03", "Communication &amp; Contenu", "Faire circuler votre image et <span class=\"it\">vos messages.</span>",
  "Réseaux sociaux, contenus, campagnes et présence digitale : une communication construite autour "
  "de votre univers et de votre audience réelle.",
  ["Gestion des réseaux sociaux", "Contenus photo et vidéo", "Visuels de campagne",
   "Publications et calendriers éditoriaux", "Publicité en ligne"],
  "images/project21.png", "Trésors by Ninel — visuel publicitaire", "portfolio.html#video", "Voir les contenus"),

 ("it", "04", "IT &amp; Technologie", "Des fondations <span class=\"it\">solides et utiles.</span>",
  "Outils, infrastructure, maintenance et sécurité : la partie moins visible d'un projet digital, "
  "celle qui décide s'il tient dans la durée.",
  ["Maintenance et mises à jour", "Hébergement et noms de domaine", "Sécurité et sauvegardes",
   "Messagerie professionnelle", "Assistance et dépannage"],
  "images/project6.jpg", "BK Entreprise — solutions créatives", "services-it.html#it", "Découvrir l'IT"),

 ("ia", "05", "IA &amp; Automatisation", "Une équipe IA qui <span class=\"it\">exécute.</span>",
  "BK-AI-WORKERS est une offre de l'écosystème BK : 18 profils spécialisés, orchestrés par Chloé, "
  "qui transforment un objectif en missions réellement exécutées — sans remplacer le reste de BK.",
  ["Les 18 Workers spécialisés", "Composition d'équipe par objectif", "Automatisation de tâches répétitives",
   "Connexion à vos outils existants", "Suivi et contrôle des missions"],
  "images/agents-clean/01-chloe.jpg", "Chloé — Agent Maître de BK-AI-WORKERS", "workers.html", "Découvrir les Workers"),

 ("conseil", "06", "Conseil &amp; Stratégie", "Une direction <span class=\"it\">claire.</span>",
  "Diagnostic, positionnement, cadrage et plan d'action : structurer une idée pour qu'elle avance, "
  "et relier présence digitale, contenus, outils et objectifs.",
  ["Diagnostic et état des lieux", "Positionnement et message", "Stratégie digitale",
   "Cadrage de projet", "Accompagnement dans la durée"],
  "images/project15.jpg", "Market Les Saveurs d'Afrik — identité", "conseil.html", "Découvrir le conseil"),

 ("evenement", "07", "Événementiel", "Une image <span class=\"it\">qui rassemble.</span>",
  "Organisation, coordination, supports et communication : donner à votre événement un univers "
  "visuel identifiable, avant, pendant et après.",
  ["Affiches et flyers d'événement", "Univers visuel complet", "Promotion sur les réseaux",
   "Supports sur place", "Contenus après l'événement"],
  "images/project7.jpg", "Zouglou Live — Garba Party", "evenement.html", "Découvrir l'événementiel"),
]


def body():
    out = []
    for k, (anc, num, titre, accroche, texte, presta, img, alt, lien, libelle) in enumerate(XP):
        dark = k % 2 == 1
        sec = "sec--night" if dark else ("sec--cream" if k % 4 == 0 else "")
        rev = "direction:rtl;" if k % 2 else ""
        li = "".join(
            '<li style="display:flex;gap:11px;align-items:flex-start;margin-bottom:11px;font-size:15.5px;">'
            '<span style="color:var(--gold);flex-shrink:0;">—</span><span>%s</span></li>' % p
            for p in presta
        )
        halo = ('<div class="halo halo--gold" style="width:520px;height:520px;top:-180px;%s:-160px;"></div>'
                % ("left" if k % 2 else "right"))
        out.append(f"""
<section class="sec {sec}" id="{anc}">
  {halo}
  <div class="wrap">
    <div class="split split--wide" style="{rev}">
      <div style="direction:ltr;">
        <span class="eyebrow rv">{num} — {titre}</span>
        <h2 class="h-md rv rv-d1" style="margin-top:20px;">{accroche}</h2>
        <p class="lead rv rv-d2" style="margin-top:20px;">{texte}</p>
        <ul class="rv rv-d3" style="margin-top:26px;">{li}</ul>
        <a class="link-arrow rv rv-d4" style="margin-top:24px;" href="{lien}">{libelle} <span class="arr">↗</span></a>
      </div>
      <div class="rv rv--r rv-d2" style="direction:ltr;" data-px="0.05">
        <div class="shot shot--4x3{shot_class(alt)}"><img src="{img}" alt="{alt}" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>""")

    return page_hero(
        eyebrow="Notre savoir-faire",
        title_html='Des expertises qui <span class="it">travaillent ensemble.</span>',
        lead=("BK Entreprise rassemble Web &amp; Digital, design, communication, IT, IA, conseil, "
              "stratégie et événementiel. Chaque domaine peut être mobilisé seul ou combiné aux autres."),
        cta1=("contact.html", "Parler à BK"),
        cta2=("#web", "Explorer les 7 expertises ↓"),
    ) + "".join(out) + CTA_FINAL
