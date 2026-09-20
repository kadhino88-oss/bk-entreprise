# -*- coding: utf-8 -*-
"""Page Profil — Vision → Parcours → Compétences → Projets → Écosystème → Aujourd'hui.
Informations issues des documents professionnels de Kader présents dans le projet.
Aucune donnée inventée, et rien qui relève de la recherche d'emploi."""
from bk_build import page_hero, CTA_FINAL

PAGE  = "profil.html"
TITLE = "Profil — Qui est derrière BK Entreprise"
DESC  = ("Christ Kader Berté, fondateur de BK Entreprise : concepteur digital et développeur web, "
         "basé à Genève. Sites, identités visuelles, e-commerce et agents IA.")
OG    = "images/project5.jpg"

COMPETENCES = [
 ("Développement web",     ["HTML5", "CSS3", "JavaScript", "WordPress", "Webflow"]),
 ("E-commerce",            ["Shopify", "Boutiques sur mesure", "Catalogue et paiement"]),
 ("Design &amp; identité", ["Adobe Photoshop", "Adobe Illustrator", "Logos et chartes", "Supports imprimés"]),
 ("Communication",         ["Community management", "Contenus réseaux", "Visuels de campagne"]),
 ("IA générative",         ["Conception d'agents", "Automatisation", "Intégration d'outils"]),
 ("Gestion de projet",     ["Analyse du besoin", "Cahier des charges", "Suivi et livraison"]),
]

PROJETS = [
 ("Market Les Saveurs d’Afrik", "Boutique Shopify sur mesure", "images/project25.jpg",
  "Identité visuelle complète et boutique en ligne pour une épicerie africaine, de la version "
  "première du logo à sa déclinaison premium."),
 ("Trésor by Ninel", "Identité et visuels produit", "images/project11.jpg",
  "Coffret beauté, visuels publicitaires et déclinaisons réseaux pour une marque de soins."),
 ("Restaurant Le Baron", "Identité et supports", "images/project19.jpg",
  "Logo, menu bar et menu restaurant pour un établissement de cuisine africaine."),
]

PARCOURS = [
 ("Vision", "Réunir au même endroit ce qu'une petite structure doit habituellement aller chercher "
  "chez trois prestataires différents : le site, l'image et la communication. Une seule "
  "interlocution, une seule cohérence."),
 ("Parcours", "Créateur de sites internet et d'applications mobiles, avec des bases solides en "
  "informatique et une pratique quotidienne des outils d'IA générative pour concevoir, "
  "documenter et produire plus vite."),
 ("Aujourd'hui", "BK Entreprise est installée à Genève et travaille avec des commerces, des "
  "restaurants, des marques et des associations en Suisse romande et en Haute-Savoie."),
]


def body():
    comps = "".join(f"""
      <div class="card rv rv-d{(i % 3) + 1}">
        <div class="card__t">{t}</div>
        <ul style="margin-top:14px;">{"".join(
          '<li style="display:flex;gap:10px;align-items:flex-start;margin-bottom:8px;font-size:14.5px;color:var(--tx-muted);">'
          '<span style="color:var(--gold);">—</span><span>%s</span></li>' % x for x in xs)}</ul>
      </div>""" for i, (t, xs) in enumerate(COMPETENCES))

    projets = "".join(f"""
        <a class="car__item" href="portfolio.html">
          <div class="car__media"><img src="{img}" alt="{t}" loading="lazy"></div>
          <div class="car__cap"><div class="car__cat">{st}</div><div class="car__t">{t}</div></div>
        </a>""" for t, st, img, _ in PROJETS)

    parcours = "".join(f"""
      <div class="flow__step rv rv-d{i}">
        <div class="flow__i">{i}</div>
        <div><div class="flow__t">{t}</div><div class="flow__d">{d}</div></div>
      </div>""" for i, (t, d) in enumerate(PARCOURS, 1))

    return page_hero(
        eyebrow="À propos",
        title_html='Qui est derrière <span class="it">BK Entreprise ?</span>',
        lead=("BK Entreprise réunit création, technologie, communication, stratégie et intelligence. "
              "L'objectif : passer de l'idée à une réalisation concrète, avec plusieurs expertises "
              "au même endroit."),
        cta1=("contact.html", "Me contacter"),
        cta2=("#parcours", "Le parcours ↓"),
    ) + f"""
<!-- ===== LE FONDATEUR ===== -->
<section class="sec sec--cream">
  <div class="halo halo--gold" style="width:540px;height:540px;top:-180px;right:-160px;"></div>
  <div class="wrap">
    <div class="split split--wide">
      <div class="rv">
        <span class="eyebrow">Le fondateur</span>
        <h2 class="h-md" style="margin-top:20px;">Christ Kader <span class="it">Berté</span></h2>
        <p class="lead" style="margin-top:8px;font-size:1.05rem;color:var(--gold-deep);font-weight:600;">
          Fondateur &amp; concepteur digital · Genève
        </p>
        <p class="lead" style="margin-top:20px;">
          Concepteur digital et développeur web, je conçois des sites internet et des applications
          mobiles pour des indépendants, des commerces et des PME. J'utilise l'IA générative au
          quotidien pour concevoir, documenter et produire plus vite — sans jamais remplacer
          le travail de compréhension du besoin.
        </p>
        <p class="lead" style="margin-top:16px;">
          Je prends le projet de bout en bout : analyse du besoin, cahier des charges, création,
          développement, mise en ligne et suivi.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:32px;">
          <a class="btn btn--ink" href="contact.html">Parler de votre projet <span class="arr">↗</span></a>
          <a class="btn btn--ghost" href="portfolio.html">Voir les réalisations</a>
        </div>
      </div>
      <div class="rv rv--r rv-d1" data-px="0.05">
        <div class="shot shot--4x3"><img src="images/project5.jpg" alt="BK Entreprise — donnez vie à vos idées" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>

<!-- ===== PARCOURS ===== -->
<section class="sec sec--night" id="parcours">
  <div class="halo halo--night" style="width:600px;height:600px;top:-210px;left:-180px;"></div>
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">01 — Parcours</span>
      <h2 class="h-lg" style="margin-top:22px;">D'une idée à <span class="it">une structure.</span></h2>
    </div>
    <div class="flow">{parcours}</div>
  </div>
</section>

<!-- ===== COMPÉTENCES ===== -->
<section class="sec">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">02 — Compétences</span>
      <h2 class="h-lg" style="margin-top:22px;">Ce que je sais <span class="it">faire moi-même.</span></h2>
      <p class="lead">Pas une liste d'intentions : les outils réellement utilisés sur les projets livrés.</p>
    </div>
    <div class="cards">{comps}</div>
  </div>
</section>

<!-- ===== PROJETS ===== -->
<section class="sec sec--dark">
  <div class="wrap">
    <div class="sec-head rv" style="max-width:none;display:flex;flex-wrap:wrap;gap:24px;align-items:flex-end;justify-content:space-between;">
      <div style="max-width:620px;">
        <span class="eyebrow">03 — Projets</span>
        <h2 class="h-lg" style="margin-top:22px;">Quelques clients <span class="it">accompagnés.</span></h2>
      </div>
      <div class="car__nav" style="margin-bottom:6px;">
        <button class="car__btn" data-car="prev" aria-label="Projet précédent">←</button>
        <button class="car__btn" data-car="next" aria-label="Projet suivant">→</button>
      </div>
    </div>
    <div class="car rv rv-d1">
      <div class="car__track" role="list" aria-label="Projets accompagnés">{projets}
      </div>
    </div>
  </div>
</section>

<!-- ===== L'ÉCOSYSTÈME ===== -->
<section class="sec sec--cream">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">04 — L'écosystème BK</span>
      <h2 class="h-lg" style="margin-top:22px;">Une maison mère, <span class="it">plusieurs branches.</span></h2>
    </div>
    <div class="cards">
      <div class="card rv"><div class="card__i">◈</div><div class="card__t">Création</div>
        <p class="card__d">Web, design, contenus et identité visuelle.</p>
        <a class="link-arrow" style="margin-top:16px;" href="expertises.html">Voir les expertises ↗</a></div>
      <div class="card rv rv-d1"><div class="card__i">◆</div><div class="card__t">Technologie</div>
        <p class="card__d">IT, outils, intégrations, IA et automatisation.</p>
        <a class="link-arrow" style="margin-top:16px;" href="services-it.html">Voir l'IT ↗</a></div>
      <div class="card rv rv-d2"><div class="card__i">★</div><div class="card__t">Accompagnement</div>
        <p class="card__d">Conseil, stratégie et évolution du projet dans la durée.</p>
        <a class="link-arrow" style="margin-top:16px;" href="conseil.html">Voir le conseil ↗</a></div>
    </div>
  </div>
</section>

<!-- ===== MON HISTOIRE ===== -->
<section class="sec sec--night" id="mon-histoire">
  <div class="halo halo--gold" style="width:600px;height:600px;top:-200px;left:-180px;"></div>
  <div class="halo halo--warm" style="width:420px;height:420px;bottom:-150px;right:-130px;"></div>
  <div class="wrap">
    <div class="sec-head rv" style="max-width:820px;">
      <span class="eyebrow">05 — Mon histoire</span>
      <h2 class="h-lg" style="margin-top:22px;">D'où vient <span class="it">BK Entreprise.</span></h2>
    </div>

    <div style="max-width:820px;">

      <div class="flow__step rv" style="display:block;padding:clamp(26px,3vw,38px);">
        <div class="eyebrow" style="font-size:11px;">Le point de départ</div>
        <p class="lead" style="margin-top:14px;color:var(--tx-inv-muted);">
          J'ai commencé par apprendre à construire : des sites web, puis des applications mobiles.
          Pas dans une école — en cherchant, en cassant des choses et en recommençant jusqu'à ce
          qu'elles fonctionnent. C'est de là que vient ma façon de travailler : comprendre comment
          une chose marche avant de promettre qu'elle marchera.
        </p>
      </div>

      <div class="flow__step rv rv-d1" style="display:block;padding:clamp(26px,3vw,38px);margin-top:16px;">
        <div class="eyebrow" style="font-size:11px;">La création de BK — 2024</div>
        <p class="lead" style="margin-top:14px;color:var(--tx-inv-muted);">
          Autour de moi, les mêmes situations revenaient : un commerçant avec un beau produit et
          aucune image, un restaurant sans carte présentable, une association qui n'arrivait pas à
          remplir sa salle. Chacun devait démarcher trois prestataires différents, avec trois
          factures et trois directions qui ne se parlaient pas.
        </p>
        <p class="lead" style="margin-top:14px;color:var(--tx-inv-muted);">
          BK Entreprise est née de ce constat : réunir la création, la technique et la communication
          au même endroit, pour que les décisions restent cohérentes entre elles.
        </p>
      </div>

      <div class="flow__step rv rv-d2" style="display:block;padding:clamp(26px,3vw,38px);margin-top:16px;">
        <div class="eyebrow" style="font-size:11px;">Ce qui a été construit</div>
        <p class="lead" style="margin-top:14px;color:var(--tx-inv-muted);">
          Depuis, ce sont des identités de marque complètes — logos, chartes, supports imprimés —,
          des sites vitrines et des boutiques en ligne, des campagnes et de la gestion de réseaux
          sociaux. Des épiceries, des restaurants, des marques de beauté, des salons, des clubs
          sportifs et des associations. <a href="portfolio.html" style="color:var(--gold-strong);font-weight:600;">23 créations</a>
          sont présentées sur ce site, chacune sous son vrai nom.
        </p>
        <p class="lead" style="margin-top:14px;color:var(--tx-inv-muted);">
          Sur chaque projet, je prends la relation client de bout en bout : analyse du besoin,
          cahier des charges, réalisation, livraison et suivi.
        </p>
      </div>

      <div class="flow__step rv rv-d3" style="display:block;padding:clamp(26px,3vw,38px);margin-top:16px;">
        <div class="eyebrow" style="font-size:11px;">L'outil qui a tout accéléré</div>
        <p class="lead" style="margin-top:14px;color:var(--tx-inv-muted);">
          J'ai intégré très tôt l'IA générative dans ma façon de produire : concevoir, documenter,
          écrire et fiabiliser du code plus vite. Ce n'est pas un gadget de communication — c'est
          ce qui permet à une structure de ma taille de livrer le travail d'une équipe.
        </p>
      </div>

      <div class="flow__step rv rv-d4" style="display:block;padding:clamp(26px,3vw,38px);margin-top:16px;border-color:var(--gold);background:rgba(214,168,79,.08);">
        <div class="eyebrow" style="font-size:11px;">L'ambition</div>
        <p class="lead" style="margin-top:14px;color:var(--tx-inv-muted);">
          L'étape suivante est <a href="workers.html" style="color:var(--gold-strong);font-weight:600;">BK-AI-WORKERS</a> :
          accompagner les PME dans la mise en place et le pilotage d'agents IA, pour leur retirer les
          tâches répétitives qui les éloignent de leur métier.
        </p>
        <p class="lead" style="margin-top:14px;color:var(--tx-inv-muted);">
          Je construis cette offre en l'utilisant d'abord sur mes propres projets. Ce qui sera proposé
          aux clients est ce qui aura déjà fait ses preuves en interne — c'est la seule façon
          honnête de vendre un outil auquel on croit.
        </p>
      </div>

      <div class="flow__step rv rv-d5" style="display:block;padding:clamp(26px,3vw,38px);margin-top:16px;">
        <div class="eyebrow" style="font-size:11px;">Aujourd'hui</div>
        <p class="lead" style="margin-top:14px;color:var(--tx-inv-muted);">
          BK Entreprise est installée à Genève et travaille des deux côtés de la frontière,
          en Suisse romande et en Haute-Savoie. La porte est ouverte : un projet, une idée,
          ou simplement une question.
        </p>
        <a class="btn btn--gold" style="margin-top:24px;" href="contact.html">Me parler de votre projet <span class="arr">↗</span></a>
      </div>

    </div>
  </div>
</section>
""" + CTA_FINAL
