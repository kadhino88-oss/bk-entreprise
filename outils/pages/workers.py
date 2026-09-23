# -*- coding: utf-8 -*-
"""Page Workers — une vraie expérience produit : concept, workflow, composition d'équipe
interactive et 17 Workers détaillés + Chloé. Portraits TOUJOURS petits et circulaires."""
from bk_build import page_hero, CTA_FINAL

PAGE  = "workers.html"
TITLE = "Agent IA pour PME à Genève — BK-AI-WORKERS | BK Entreprise"
DESC  = ("Agents IA pour PME à Genève : 17 Workers spécialisés orchestrés par Chloé. Vous donnez l'objectif, "
         "Chloé compose l'équipe, les Workers exécutent. Une offre de l'écosystème BK Entreprise.")
OG    = "images/agents-clean/01-chloe.jpg"

CHLOE = ("chloe", "Chloé", "Agent Maître",
         "Agent Maître · Orchestration &amp; stratégie", "images/agents-clean/01-chloe.jpg",
         ["Analyse d'objectif", "Composition d'équipe", "Répartition des tâches", "Contrôle qualité", "Arbitrage"],
         ["Traduire un objectif en missions concrètes", "Choisir les Workers utiles — et seulement eux",
          "Distribuer et séquencer le travail", "Vérifier le résultat avant livraison"],
         ["Tous les outils connectés de l'écosystème BK"])

# (id, nom, rôle court, rôle long, image, compétences, missions, outils)
WORKERS = [
 ("alex", "Alex", "Prospection", "Ventes · Prospection commerciale", "images/agents-clean/02-alex.jpg",
  ["Ciblage", "Prospection", "Relances", "Qualification"],
  ["Constituer des listes de prospects pertinents", "Rédiger et personnaliser les prises de contact",
   "Relancer au bon moment", "Qualifier les demandes entrantes"],
  ["HubSpot", "Pipedrive", "Salesforce"]),

 ("emma", "Emma", "Contenu", "Contenu · Réseaux sociaux", "images/agents-clean/03-emma.jpg",
  ["Rédaction", "Calendrier éditorial", "Formats courts", "Community management"],
  ["Produire des publications régulières", "Tenir un calendrier éditorial",
   "Adapter un message à chaque réseau", "Répondre aux commentaires et messages"],
  ["Instagram", "Facebook", "TikTok", "Slack"]),

 ("lea", "Léa", "Design", "Design · Branding", "images/agents-clean/04-lea.jpg",
  ["Direction artistique", "Déclinaisons", "Chartes graphiques", "Maquettes"],
  ["Décliner une identité sur tous les supports", "Préparer des visuels de campagne",
   "Maintenir la cohérence graphique", "Produire des maquettes à valider"],
  ["Figma", "Adobe Photoshop", "Adobe Illustrator"]),

 ("lucas", "Lucas", "Web &amp; dév.", "Web · Développement digital", "images/agents-clean/05-lucas.jpg",
  ["Intégration", "Front-end", "Performance", "Mise en ligne"],
  ["Construire et mettre à jour les pages", "Corriger les anomalies d'affichage",
   "Améliorer la vitesse de chargement", "Préparer les mises en ligne"],
  ["GitHub", "Vercel", "WordPress", "Webflow"]),

 ("maya", "Maya", "Marketing", "Marketing · Growth", "images/agents-clean/06-maya.jpg",
  ["Campagnes", "Audiences", "Acquisition", "Analyse de performance"],
  ["Cadrer et lancer une campagne", "Définir les audiences à toucher",
   "Suivre le coût par résultat", "Ajuster selon les performances réelles"],
  ["HubSpot", "Google Workspace"]),

 ("noah", "Noah", "Administration", "Administration · Organisation", "images/agents-clean/07-noah.jpg",
  ["Documents", "Agendas", "Procédures", "Classement"],
  ["Préparer et classer les documents courants", "Tenir les agendas et les échéances",
   "Mettre au propre les procédures internes", "Organiser les espaces de fichiers"],
  ["Microsoft 365", "Google Workspace", "Dropbox"]),

 ("sam", "Sam", "IT", "IT · Cybersécurité · Infrastructure", "images/agents-clean/08-sam.jpg",
  ["Sécurité", "Sauvegardes", "Accès", "Surveillance"],
  ["Vérifier sauvegardes et mises à jour", "Contrôler les accès et les droits",
   "Surveiller les incidents", "Documenter l'infrastructure"],
  ["Microsoft 365", "GitHub"]),

 ("seoya", "Séoya", "SEO &amp; rédaction", "SEO · Rédaction web", "images/agents-clean/09-seoya.jpg",
  ["Mots-clés", "Rédaction optimisée", "Balises &amp; structure", "Suivi de position"],
  ["Identifier les requêtes qui comptent pour votre activité", "Rédiger des pages pensées pour le référencement",
   "Structurer titres, balises et liens internes", "Suivre l'évolution des positions sur Google"],
  ["Google Workspace"]),

 ("nora", "Nora", "Support", "Support · Relation client", "images/agents-clean/01-nora.jpg",
  ["Réponses clients", "Suivi des demandes", "Documentation", "Satisfaction"],
  ["Répondre aux demandes courantes", "Suivre les tickets jusqu'à résolution",
   "Rédiger les réponses types", "Remonter les problèmes récurrents"],
  ["Zendesk", "Intercom", "Slack"]),

 ("sophie", "Sophie", "RH", "RH · Recrutement", "images/agents-clean/02-sophie.jpg",
  ["Annonces", "Tri de candidatures", "Entretiens", "Intégration"],
  ["Rédiger et diffuser les annonces", "Trier et classer les candidatures",
   "Préparer les trames d'entretien", "Organiser l'arrivée des nouveaux"],
  ["Microsoft 365", "Google Workspace"]),

 ("dario", "Dario", "Finance", "Finance · Contrôle", "images/agents-clean/03-dario.jpg",
  ["Devis", "Factures", "Suivi de budget", "Relances"],
  ["Préparer devis et factures", "Suivre les encaissements",
   "Contrôler un budget de projet", "Relancer les impayés"],
  ["Microsoft 365", "Google Workspace"]),

 ("ines", "Inès", "Data", "Data · Analytics", "images/agents-clean/04-ines.jpg",
  ["Tableaux de bord", "Indicateurs", "Rapports", "Nettoyage de données"],
  ["Construire un tableau de bord lisible", "Définir les indicateurs utiles",
   "Produire les rapports récurrents", "Fiabiliser les données sources"],
  ["Google Workspace", "Microsoft 365", "HubSpot"]),

 ("yanis", "Yanis", "Gestion de projet", "PMO · Gestion de projet", "images/agents-clean/05-yanis.jpg",
  ["Planning", "Jalons", "Coordination", "Suivi des risques"],
  ["Découper le projet en étapes", "Tenir le planning et les jalons",
   "Coordonner les intervenants", "Signaler les risques à temps"],
  ["Trello", "Asana", "Monday.com"]),

 ("clara", "Clara", "Juridique", "Juridique · Contrats · Documents", "images/agents-clean/06-clara.jpg",
  ["Contrats", "Mentions légales", "Conformité", "Modèles"],
  ["Préparer les contrats courants", "Tenir à jour mentions légales et CGV",
   "Vérifier la conformité des documents", "Maintenir une bibliothèque de modèles"],
  ["Microsoft 365", "Dropbox"]),

 ("amina", "Amina", "Veille", "Veille stratégique &amp; intelligence", "images/agents-clean/07-amina.jpg",
  ["Veille de marché", "Analyse concurrentielle", "Synthèses", "Sourcing"],
  ["Surveiller un marché ou un secteur", "Analyser ce que font les concurrents",
   "Produire des synthèses exploitables", "Trouver les sources fiables"],
  ["Google Workspace"]),

 ("thomas", "Thomas", "E-commerce", "E-commerce · Catalogue &amp; marketplace", "images/agents-clean/08-thomas.jpg",
  ["Catalogue", "Fiches produits", "Stocks", "Commandes"],
  ["Créer et enrichir les fiches produits", "Tenir le catalogue à jour",
   "Surveiller les stocks", "Suivre les commandes et les retours"],
  ["Shopify", "HubSpot"]),

 ("rayan", "Rayan", "Automatisation", "Automatisation · Intégrations", "images/agents-clean/09-rayan.jpg",
  ["Connecteurs", "Scénarios", "Synchronisation", "Maintenance des flux"],
  ["Relier deux outils qui ne se parlent pas", "Automatiser les tâches répétitives",
   "Synchroniser les données entre plateformes", "Surveiller les flux en place"],
  ["Slack", "Google Workspace", "Microsoft 365", "Salesforce"]),
]

# Outils qui possèdent une fiche sur integrations.html (les autres restent de simples étiquettes)
INTEGRATIONS = {
 "Google Workspace": "google", "Microsoft 365": "microsoft", "Slack": "slack",
 "Trello": "trello", "Asana": "asana", "Monday.com": "monday", "Figma": "figma",
 "HubSpot": "hubspot", "Pipedrive": "pipedrive", "Intercom": "intercom",
 "Zendesk": "zendesk", "Dropbox": "dropbox", "Salesforce": "salesforce",
}

OBJECTIFS = [
 ("boutique",    "Lancer une boutique"),
 ("campagne",    "Créer une campagne"),
 ("reseaux",     "Améliorer mes réseaux sociaux"),
 ("projet",      "Organiser un projet"),
 ("automatiser", "Automatiser une tâche"),
 ("site",        "Refondre mon site"),
 ("recrutement", "Recruter quelqu'un"),
 ("client",      "Mieux suivre mes clients"),
]

ETAPES = [
 ("Objectif du client", "Vous décrivez ce que vous voulez obtenir, dans vos mots."),
 ("Chloé analyse",      "Elle traduit l'objectif en besoins réels et repère ce qui manque."),
 ("Chloé sélectionne",  "Elle choisit les Workers utiles — et laisse les autres de côté."),
 ("Équipe créée",       "L'équipe est constituée pour cette mission précise."),
 ("Tâches distribuées", "Chaque Worker reçoit un périmètre clair et des priorités."),
 ("Les Workers travaillent", "L'exécution démarre, dans vos outils quand c'est possible."),
 ("Chloé contrôle",     "Elle vérifie la cohérence et la qualité de ce qui a été produit."),
 ("Résultat final",     "Vous recevez un livrable exploitable, pas un brouillon."),
]


def body():
    # --- pastilles d'objectif ---
    chips = "".join('<button type="button" class="chip" data-goal="%s">%s</button>' % (k, t)
                    for k, t in OBJECTIFS)

    # --- données des Workers lues par bk.js ---
    pool = "".join(
        '\n  <template data-worker="%s" data-nom="%s" data-role="%s" data-img="%s"></template>'
        % (wid, nom, court, img) for wid, nom, court, _, img, _, _, _ in WORKERS)

    # --- grille des 18 ---
    grille = "".join(f"""
      <a class="wcard rv rv-d{(i % 6) + 1}" href="#{wid}">
        <span class="pf pf--sm pf--ring"><img src="{img}" alt="{nom} — {long}" loading="lazy"></span>
        <span class="wcard__txt"><span class="wcard__n">{nom}</span><span class="wcard__r">{court}</span></span>
      </a>""" for i, (wid, nom, court, long, img, _, _, _) in enumerate(WORKERS))

    # --- workflow ---
    flux = "".join(f"""
      <div class="flow__step rv rv-d{min(i,6)}">
        <div class="flow__i">{i}</div>
        <div><div class="flow__t">{t}</div><div class="flow__d">{d}</div></div>
      </div>""" for i, (t, d) in enumerate(ETAPES, 1))

    # --- fiches détaillées ---
    def fiche(wid, nom, court, long, img, comp, miss, outils, maitre=False):
        pills = "".join('<span class="chip" style="pointer-events:none;font-size:12.5px;padding:7px 13px;">%s</span>' % c for c in comp)
        lis = "".join('<li style="display:flex;gap:11px;align-items:flex-start;margin-bottom:10px;font-size:15px;">'
                      '<span style="color:var(--gold);flex-shrink:0;">—</span><span>%s</span></li>' % m for m in miss)
        # Seuls les outils réellement présents sur la page Intégrations deviennent des liens.
        parts = []
        for o in outils:
            cible = INTEGRATIONS.get(o)
            if cible:
                parts.append('<a class="chip" href="integrations.html#%s" style="font-size:12.5px;padding:7px 13px;">%s</a>' % (cible, o))
            else:
                parts.append('<span class="chip" style="pointer-events:none;font-size:12.5px;padding:7px 13px;opacity:.72;">%s</span>' % o)
        tools = "".join(parts)
        ring = "pf--gold" if maitre else "pf--ring"
        return f"""
      <article class="card rv" id="{wid}" style="scroll-margin-top:110px;">
        <div style="display:flex;gap:18px;align-items:center;">
          <span class="pf pf--md {ring}"><img src="{img}" alt="{nom} — {long}" loading="lazy"></span>
          <div>
            <div class="card__t" style="font-size:1.32rem;">{nom}</div>
            <div class="wcard__r" style="font-size:13px;margin-top:4px;">{long}</div>
          </div>
        </div>

        <div style="margin-top:22px;">
          <div class="eyebrow" style="font-size:11px;">Compétences</div>
          <div class="chips" style="margin-top:12px;">{pills}</div>
        </div>

        <div style="margin-top:22px;">
          <div class="eyebrow" style="font-size:11px;">Missions types</div>
          <ul style="margin-top:12px;">{lis}</ul>
        </div>

        <div style="margin-top:22px;">
          <div class="eyebrow" style="font-size:11px;">Outils &amp; intégrations</div>
          <div class="chips" style="margin-top:12px;">{tools}</div>
        </div>

        <a class="btn btn--gold" style="margin-top:26px;width:100%;justify-content:center;"
           href="#mission">Recruter {nom} <span class="arr">↗</span></a>
      </article>"""

    fiches = "".join(fiche(*w) for w in WORKERS)
    fiche_chloe = fiche(*CHLOE, maitre=True)

    return page_hero(
        eyebrow="BK-AI-WORKERS",
        title_html='Votre objectif. <span class="it">Une équipe IA.</span>',
        lead=("17 Workers spécialisés, orchestrés par Chloé. Vous donnez l'objectif, elle compose "
              "l'équipe, les Workers exécutent — et vous obtenez un résultat exploitable. "
              "BK-AI-WORKERS est une offre de l'écosystème BK Entreprise."),
        cta1=("#mission", "Créer ma première mission"),
        cta2=("#equipe", "Voir les 17 Workers ↓"),
    ) + f"""{pool}

<!-- ===== LE CONCEPT ===== -->
<section class="sec sec--cream">
  <div class="halo halo--gold" style="width:540px;height:540px;top:-190px;right:-160px;"></div>
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">01 — Le concept</span>
      <h2 class="h-lg" style="margin-top:22px;">Quatre temps, <span class="it">un résultat.</span></h2>
    </div>
    <div class="steps">
      <div class="step"><div class="step__n">01</div><div class="step__t">Vous donnez l'objectif</div><div class="step__d">Dans vos mots, sans jargon technique.</div></div>
      <div class="step"><div class="step__n">02</div><div class="step__t">Chloé construit l'équipe</div><div class="step__d">Elle choisit les profils réellement utiles.</div></div>
      <div class="step"><div class="step__n">03</div><div class="step__t">Vos Workers exécutent</div><div class="step__d">Chacun sur son périmètre, en parallèle.</div></div>
      <div class="step"><div class="step__n">04</div><div class="step__t">Vous obtenez le résultat</div><div class="step__d">Contrôlé par Chloé avant de vous parvenir.</div></div>
    </div>
  </div>
</section>

<!-- ===== INTERFACE : COMPOSER UNE MISSION ===== -->
<section class="sec sec--night" id="mission" data-mission>
  <div class="halo halo--gold" style="width:600px;height:600px;top:-200px;left:-180px;"></div>
  <div class="wrap">
    <div class="sec-head rv" style="text-align:center;margin-inline:auto;">
      <span class="eyebrow" style="justify-content:center;">02 — Composer une mission</span>
      <h2 class="h-lg" style="margin-top:22px;">Que souhaitez-vous accomplir <span class="it">aujourd'hui ?</span></h2>
      <p class="lead" style="margin-inline:auto;">Choisissez un objectif : Chloé compose l'équipe sous vos yeux.</p>
    </div>

    <div class="chips rv rv-d1" style="justify-content:center;max-width:860px;margin:0 auto;">{chips}</div>

    <div hidden data-mission-out style="margin-top:46px;">
      <div style="display:flex;align-items:center;justify-content:center;gap:16px;margin-bottom:28px;">
        <span class="pf pf--sm pf--gold"><img src="{CHLOE[4]}" alt="Chloé — Agent Maître"></span>
        <p class="lead" data-mission-verdict style="margin:0;text-align:left;"></p>
      </div>
      <div class="wgrid" data-mission-team style="max-width:880px;margin:0 auto;"></div>
      <div style="text-align:center;margin-top:34px;">
        <a class="btn btn--gold" href="contact.html">Lancer cette mission <span class="arr">↗</span></a>
      </div>
    </div>
  </div>
</section>

<!-- ===== LE WORKFLOW ===== -->
<section class="sec sec--dark">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">03 — Le déroulé</span>
      <h2 class="h-lg" style="margin-top:22px;">De l'objectif au <span class="it">livrable.</span></h2>
      <p class="lead">Huit étapes, toujours dans le même ordre — c'est ce qui rend le résultat prévisible.</p>
    </div>
    <div class="flow">{flux}</div>
  </div>
</section>

<!-- ===== CHLOÉ ===== -->
<section class="sec sec--night" id="chloe-section">
  <div class="halo halo--gold" style="width:520px;height:520px;top:-170px;right:-150px;"></div>
  <div class="wrap">
    <div class="split split--wide" style="align-items:start;">
      <div class="rv">
        <span class="eyebrow">04 — L'Agent Maître</span>
        <h2 class="h-md" style="margin-top:20px;">Chloé n'est pas un Worker <span class="it">comme les autres.</span></h2>
        <p class="lead" style="margin-top:20px;">
          Elle ne produit pas : elle comprend, décide et contrôle. C'est elle qui traduit votre
          objectif en missions, choisit qui intervient, répartit le travail et vérifie le résultat
          avant qu'il ne vous parvienne.
        </p>
        <p class="lead" style="margin-top:16px;">
          Sans elle, 17 profils isolés. Avec elle, une équipe.
        </p>
      </div>
      <div class="rv rv--r rv-d1">{fiche_chloe}</div>
    </div>
  </div>
</section>

<!-- ===== LES 17 WORKERS ===== -->
<section class="sec sec--cream" id="equipe">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">05 — L'équipe</span>
      <h2 class="h-lg" style="margin-top:22px;">Dix-sept spécialistes, <span class="it">un seul chef d'orchestre.</span></h2>
      <p class="lead">Cliquez sur un profil pour voir ses compétences, ses missions et ses outils.</p>
    </div>
    <div class="wgrid rv rv-d1">{grille}</div>
  </div>
</section>

<!-- ===== FICHES DÉTAILLÉES ===== -->
<section class="sec sec--dark" id="profils">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">06 — Les profils</span>
      <h2 class="h-lg" style="margin-top:22px;">Chaque Worker a <span class="it">son terrain.</span></h2>
    </div>
    <div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(320px,1fr));">{fiches}</div>
  </div>
</section>

<!-- ===== PLACE DANS L'ÉCOSYSTÈME ===== -->
<section class="sec sec--sand">
  <div class="wrap">
    <div class="split">
      <div class="rv">
        <span class="eyebrow">07 — Et le reste de BK ?</span>
        <h2 class="h-md" style="margin-top:20px;">Une branche, <span class="it">pas le tronc.</span></h2>
        <p class="lead" style="margin-top:20px;">
          BK-AI-WORKERS est une offre parmi d'autres. La création web, le design, la communication,
          l'IT, le conseil et l'événementiel continuent d'exister par eux-mêmes — les Workers
          viennent s'y ajouter quand ils apportent quelque chose.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:30px;">
          <a class="btn btn--ink" href="expertises.html">Voir toutes les expertises <span class="arr">↗</span></a>
          <a class="btn btn--ghost" href="integrations.html">Les intégrations</a>
        </div>
      </div>
      <div class="rv rv--r rv-d1" data-px="0.05">
        <div class="shot shot--4x3"><img src="images/project5.jpg" alt="BK Entreprise — donnez vie à vos idées" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>
""" + CTA_FINAL
