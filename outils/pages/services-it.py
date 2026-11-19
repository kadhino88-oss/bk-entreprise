# -*- coding: utf-8 -*-
"""Page IT & Digital — création web, développement, maintenance, IT, sécurité, IA, intégrations."""
from bk_build import page_hero, CTA_FINAL

PAGE  = "services-it.html"
TITLE = "Création site web Genève — IT & Digital | BK Entreprise"
DESC  = ("Création de site web à Genève, développement, maintenance, infrastructure, sécurité, "
         "agents IA pour PME et automatisation : la partie technique de vos projets, prise en charge par BK Entreprise.")
OG    = "images/project6.jpg"

CREATION = [
 ("◈", "Sites vitrines", "Présenter votre activité avec clarté : structure lisible, image soignée, chargement rapide."),
 ("◆", "Sites marchands &amp; boutiques en ligne", "Catalogue, paiement, livraison et suivi des commandes — pensés pour être tenus au quotidien."),
 ("▲", "Applications mobiles", "Prototypes et applications pour porter un service au-delà du site."),
 ("◎", "Refonte", "Repartir d'un site existant sans perdre son contenu ni son référencement."),
 ("★", "Optimisation", "Vitesse, affichage mobile et accessibilité — ce qui décide si un visiteur reste."),
 ("◇", "Référencement", "Structure, balises et contenus pour être trouvé sur les bons mots."),
]

IT = [
 ("◎", "Maintenance", "Mises à jour, correctifs et surveillance pour éviter les mauvaises surprises."),
 ("◈", "Hébergement &amp; domaines", "Mise en place et gestion du nom de domaine, de l'hébergement et des certificats."),
 ("▲", "Sécurité", "Sauvegardes, accès, certificats et bonnes pratiques contre les incidents courants."),
 ("◆", "Messagerie professionnelle", "Adresses à votre nom de domaine, configurées proprement."),
 ("★", "Assistance", "Un interlocuteur quand quelque chose ne fonctionne plus."),
 ("◇", "Postes &amp; outils", "Équipement, comptes et outils du quotidien mis en cohérence."),
]

IA = [
 ("Automatiser une tâche répétitive", "Relances, publications, mises à jour de fichiers, rapports récurrents."),
 ("Relier vos outils entre eux", "Vos applications se parlent au lieu de vous faire ressaisir les mêmes informations."),
 ("Mobiliser les Workers", "17 Workers spécialisés, orchestrés par Chloé, pour exécuter des missions précises."),
]


def cartes(items, start=0):
    return "".join(f"""
      <div class="card rv rv-d{(i % 3) + 1}">
        <div class="card__i">{ico}</div>
        <div class="card__t">{t}</div>
        <p class="card__d">{d}</p>
      </div>""" for i, (ico, t, d) in enumerate(items, start))


def body():
    ia_rows = "".join(f"""
      <div class="flow__step rv rv-d{i}">
        <div class="flow__i">{i}</div>
        <div><div class="flow__t">{t}</div><div class="flow__d">{d}</div></div>
      </div>""" for i, (t, d) in enumerate(IA, 1))

    return page_hero(
        eyebrow="IT &amp; Digital",
        title_html='La technique qui rend votre projet <span class="it">solide et utile.</span>',
        lead=("Création de sites, sites marchands, développement, maintenance, infrastructure, sécurité, IA et "
              "automatisation : tout ce qui fait qu'un projet digital fonctionne — et continue de fonctionner."),
        cta1=("contact.html", "Parler de mon projet"),
        cta2=("#creation", "Voir les prestations ↓"),
    ) + f"""
<!-- ===== CRÉATION WEB ===== -->
<section class="sec sec--cream" id="creation">
  <div class="halo halo--gold" style="width:540px;height:540px;top:-190px;right:-160px;"></div>
  <div class="wrap">
    <div class="split split--wide">
      <div class="rv">
        <span class="eyebrow">01 — Création web</span>
        <h2 class="h-md" style="margin-top:20px;">Créer une présence digitale qui travaille <span class="it">pour vous.</span></h2>
        <p class="lead" style="margin-top:20px;">
          Un site n'est pas une brochure en ligne : c'est un outil qui doit présenter votre activité,
          rassurer et déclencher un contact. C'est de là qu'on part.
        </p>
        <a class="link-arrow" style="margin-top:24px;" href="portfolio.html">Voir des réalisations <span class="arr">↗</span></a>
      </div>
      <div class="rv rv--r rv-d1" data-px="0.05">
        <div class="shot shot--4x3"><img src="images/project6.jpg" alt="BK Entreprise — solutions créatives" loading="lazy"></div>
      </div>
    </div>
    <div class="cards" style="margin-top:clamp(40px,5vw,66px);">{cartes(CREATION)}</div>
  </div>
</section>

<!-- ===== IT ===== -->
<section class="sec sec--night" id="it">
  <div class="halo halo--night" style="width:620px;height:620px;top:-220px;left:-190px;"></div>
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">02 — IT &amp; Infrastructure</span>
      <h2 class="h-lg" style="margin-top:22px;">Ce qu'on ne voit pas, mais qui <span class="it">tient tout.</span></h2>
      <p class="lead">Hébergement, maintenance, sécurité et outils du quotidien : la partie qui décide
      si votre projet tient dans la durée.</p>
    </div>
    <div class="cards">{cartes(IT)}</div>
  </div>
</section>

<!-- ===== IA & AUTOMATISATION ===== -->
<section class="sec sec--dark" id="ia">
  <div class="halo halo--gold" style="width:500px;height:500px;bottom:-180px;right:-150px;"></div>
  <div class="wrap">
    <div class="split">
      <div class="rv">
        <span class="eyebrow">03 — IA &amp; Automatisation</span>
        <h2 class="h-md" style="margin-top:20px;">Gagner du temps sur ce qui <span class="it">se répète.</span></h2>
        <p class="lead" style="margin-top:20px;">
          L'automatisation ne remplace pas votre métier : elle retire les tâches qui vous en éloignent.
          BK identifie celles qui s'y prêtent réellement, puis les met en place.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:32px;">
          <a class="btn btn--gold" href="workers.html">Découvrir les Workers <span class="arr">↗</span></a>
          <a class="btn btn--ghost" href="integrations.html">Voir les intégrations</a>
        </div>
      </div>
      <div class="rv rv--r rv-d1">
        <div class="flow">{ia_rows}</div>
      </div>
    </div>
  </div>
</section>

<!-- ===== MÉTHODE ===== -->
<section class="sec sec--sand">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">04 — Comment ça se passe</span>
      <h2 class="h-lg" style="margin-top:22px;">Une méthode <span class="it">sans surprise.</span></h2>
    </div>
    <div class="steps">
      <div class="step"><div class="step__n">01</div><div class="step__t">Cadrer</div><div class="step__d">Vos objectifs, vos contraintes et ce qui existe déjà.</div></div>
      <div class="step"><div class="step__n">02</div><div class="step__t">Concevoir</div><div class="step__d">Structure, contenus et direction visuelle, validés avant de coder.</div></div>
      <div class="step"><div class="step__n">03</div><div class="step__t">Développer</div><div class="step__d">Réalisation par étapes, avec des points de validation réguliers.</div></div>
      <div class="step"><div class="step__n">04</div><div class="step__t">Mettre en ligne</div><div class="step__d">Domaine, hébergement, sécurité et vérifications avant publication.</div></div>
      <div class="step"><div class="step__n">05</div><div class="step__t">Maintenir</div><div class="step__d">Suivi, mises à jour et évolutions une fois le site en service.</div></div>
    </div>
  </div>
</section>
""" + CTA_FINAL
