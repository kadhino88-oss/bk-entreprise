# -*- coding: utf-8 -*-
"""Accueil — centrée sur CE QU'ON FAIT, NOTRE EXPÉRIENCE et NOTRE FUTUR.
Volontairement sobre en images : ce n'est pas une galerie, le portfolio est là pour ça."""
from bk_build import CTA_FINAL, realisations, media_class

PAGE  = "index.html"
TITLE = "BK Entreprise — Agence digitale & créative à Genève"
DESC  = ("BK Entreprise conçoit sites, identités visuelles et communication pour commerces, "
         "restaurants et associations — et développe des agents IA pour les PME. Genève.")
OG    = "images/project5.jpg"
LIGHT_HEADER = False   # le hero vidéo est sombre : navigation en blanc

EXPERTISES = [
 ("01", "Web &amp; Digital", "Sites vitrines, boutiques en ligne et interfaces conçus pour présenter votre activité avec clarté.", "services-it.html"),
 ("02", "Design &amp; Identité", "Logos, chartes, affiches, menus et supports imprimés — une image cohérente et reconnaissable.", "expertises.html#design"),
 ("03", "Communication &amp; Réseaux", "Contenus, campagnes et gestion des réseaux, pensés autour de votre univers et de votre audience.", "expertises.html#communication"),
 ("04", "IT &amp; Technologie", "Hébergement, maintenance, sécurité et outils du quotidien : ce qui fait tenir un projet dans la durée.", "services-it.html#it"),
 ("05", "IA &amp; Automatisation", "BK-AI-WORKERS : 18 profils spécialisés qui transforment un objectif en missions exécutées.", "workers.html"),
 ("06", "Conseil &amp; Stratégie", "Diagnostic, positionnement et plan d'action pour décider avec une direction claire.", "conseil.html"),
 ("07", "Événementiel", "Affiches, univers visuel et communication pour donner à votre événement une image qui rassemble.", "evenement.html"),
]

# Preuves de travail — toutes les réalisations, pour qu'on puisse défiler dans l'ensemble.
# (Le détail de chaque projet reste sur la page Réalisations.)

SECTEURS = [
 ("Commerces &amp; épiceries", "Identité, boutique en ligne, catalogue produits."),
 ("Restaurants &amp; bars", "Logos, menus, cartes et supports de salle."),
 ("Marques &amp; indépendants", "Image de marque, visuels produit, réseaux sociaux."),
 ("Associations", "Affiches de collecte, événements et communication solidaire."),
]


def body():
    xp = "".join(f"""
      <a class="xp__row rv{' rv-d' + str(i) if i else ''}" href="{lien}">
        <span class="xp__n">{n}</span>
        <span><span class="xp__t">{t}</span><span class="xp__d">{d}</span></span>
        <span class="xp__go" aria-hidden="true">↗</span>
      </a>""" for i, (n, t, d, lien) in enumerate(EXPERTISES))

    preuves = "".join(f"""
        <a class="car__item" href="portfolio.html#creations">
          <div class="car__media{media_class(it['titre'])}"><img src="{it['img']}" alt="{it['titre']} — réalisation BK Entreprise" loading="lazy"></div>
          <div class="car__cap"><div class="car__cat">{it['cat']}</div><div class="car__t">{it['titre']}</div></div>
        </a>""" for it in realisations()["realisations"])

    detail = "".join(f"""
      <div class="flow__step rv rv-d{i}" style="border-color:var(--line);background:#fff;">
        <div class="flow__i">{i}</div>
        <div><div class="flow__t">{t}</div>
        <div class="flow__d" style="color:var(--tx-muted);">{d}</div></div>
      </div>""" for i, (t, d) in enumerate(SECTEURS, 1))

    return f"""
<!-- ========== HERO ========== -->
<section class="hero">
  <video class="hero__video" src="videos/hero-video.mp4" poster="images/hero-poster.jpg"
         autoplay muted loop playsinline preload="auto" aria-hidden="true"></video>
  <div class="hero__veil"></div>
  <div class="hero__grain"></div>

  <div class="wrap">
    <span class="eyebrow rv">BK Entreprise · Genève</span>
    <h1 class="h-xl hero__title rv rv-d1">Votre partenaire <span class="it">digital, créatif</span> et stratégique.</h1>
    <p class="hero__sub rv rv-d2">
      Nous concevons des sites, des identités visuelles et de la communication pour les commerces,
      les restaurants, les marques et les associations — et nous développons des agents IA
      pour alléger le travail des petites structures.
    </p>
    <div class="hero__cta rv rv-d3">
      <a class="btn btn--gold" href="contact.html">Démarrer un projet <span class="arr">↗</span></a>
      <a class="btn btn--ghost" href="#faire">Ce que nous faisons ↓</a>
    </div>

    <div class="hero__stats rv rv-d4">
      <div class="stat"><div class="stat__n">500+</div><div class="stat__l">Créations livrées</div></div>
      <div class="stat"><div class="stat__n">99%</div><div class="stat__l">Clients satisfaits</div></div>
      <div class="stat"><div class="stat__n">7</div><div class="stat__l">Expertises</div></div>
      <div class="stat"><div class="stat__n">2024</div><div class="stat__l">Année de création</div></div>
    </div>
  </div>

  <div class="scrollcue"><span>Scroll</span><i></i></div>
</section>

<!-- ========== CE QUE NOUS FAISONS ========== -->
<section class="sec sec--cream" id="faire">
  <div class="halo halo--gold" style="width:520px;height:520px;top:-180px;right:-160px;"></div>
  <div class="wrap">
    <div class="sec-head rv" style="max-width:780px;">
      <span class="eyebrow">Ce que nous faisons</span>
      <h2 class="h-lg">Une seule maison pour <span class="it">tout ce qui se voit</span> de votre activité.</h2>
      <p class="lead">
        La plupart des petites structures doivent aller chercher leur site chez l'un, leur logo chez
        l'autre et leurs réseaux chez un troisième. BK Entreprise réunit ces métiers au même endroit :
        une seule interlocution, une seule cohérence, et des décisions qui ne se contredisent pas.
      </p>
    </div>
  </div>
</section>

<!-- ========== LES EXPERTISES ========== -->
<section class="sec sec--night">
  <div class="halo halo--night" style="width:660px;height:660px;top:-220px;left:-200px;"></div>
  <div class="halo halo--warm" style="width:400px;height:400px;bottom:-140px;right:-120px;"></div>
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">01 — Nos expertises</span>
      <h2 class="h-lg">Sept métiers, <span class="it">mobilisables séparément.</span></h2>
      <p class="lead">Chacun existe seul. Ensemble, ils évitent les allers-retours entre prestataires.</p>
    </div>
    <div class="xp">{xp}</div>
  </div>
</section>

<!-- ========== NOTRE EXPÉRIENCE ========== -->
<section class="sec">
  <div class="wrap">
    <div class="sec-head rv" style="max-width:820px;">
      <span class="eyebrow">02 — Notre expérience</span>
      <h2 class="h-lg">Ce que nous avons <span class="it">déjà fait.</span></h2>
      <p class="lead">
        BK Entreprise travaille depuis 2024 avec des structures qui n'ont pas de service
        communication interne : un commerçant, un restaurateur, une marque qui démarre,
        une association qui organise un événement. Le point commun : il faut que ce soit
        clair, rapide à comprendre, et utilisable tout de suite.
      </p>
    </div>

    <div class="rv rv-d1" style="margin-bottom:clamp(40px,5vw,64px);">
      <div class="flow" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;">{detail}</div>
    </div>

    <div style="display:flex;flex-wrap:wrap;gap:24px;align-items:flex-end;justify-content:space-between;margin-bottom:26px;">
      <p class="lead rv" style="margin:0;max-width:52ch;">Quelques projets, à titre d'exemple.</p>
      <div class="car__nav">
        <button class="car__btn" data-car="prev" aria-label="Projet précédent">←</button>
        <button class="car__btn" data-car="next" aria-label="Projet suivant">→</button>
      </div>
    </div>

    <div class="car rv rv-d1">
      <div class="car__track" role="list" aria-label="Quelques réalisations">{preuves}
      </div>
    </div>

    <div class="rv rv-d2" style="margin-top:26px;">
      <a class="link-arrow" href="portfolio.html">Voir toutes les réalisations <span class="arr">↗</span></a>
    </div>
  </div>
</section>

<!-- ========== NOTRE FUTUR ========== -->
<section class="sec sec--night">
  <div class="halo halo--gold" style="width:600px;height:600px;top:50%;left:50%;transform:translate(-50%,-50%);opacity:.45;"></div>
  <div class="wrap">
    <div class="sec-head rv" style="max-width:820px;">
      <span class="eyebrow">03 — Notre futur</span>
      <h2 class="h-lg">Là où BK <span class="it">va maintenant.</span></h2>
      <p class="lead">
        Une petite structure passe un temps considérable sur des tâches qui ne font pas avancer
        son métier : relances, publications, mises à jour, documents à reprendre. C'est le terrain
        de <strong>BK-AI-WORKERS</strong> — 18 profils spécialisés, orchestrés par Chloé, qui
        exécutent ces missions dans vos outils existants.
      </p>
      <p class="lead" style="margin-top:16px;">
        L'offre est disponible dès aujourd'hui et travaille déjà pour plusieurs PME — sur des
        missions concrètes, dans leurs outils existants.
      </p>
    </div>

    <div class="orbit rv rv--z rv-d1">
      <div class="orbit__ring"></div>
      <div class="orbit__ring orbit__ring--2"></div>

      <div class="orbit__spin" data-radius="46">
        <div class="orbit__sat"><a href="workers.html#alex"   title="Alex — Prospection commerciale"><span class="pf pf--sm pf--ring"><img src="images/agents-clean/02-alex.jpg"   alt="Alex — prospection commerciale" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#emma"   title="Emma — Contenu et réseaux sociaux"><span class="pf pf--sm pf--ring"><img src="images/agents-clean/03-emma.jpg"   alt="Emma — contenu et réseaux sociaux" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#lea"    title="Léa — Design et branding"><span class="pf pf--sm pf--ring"><img src="images/agents-clean/04-lea.jpg"    alt="Léa — design et branding" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#lucas"  title="Lucas — Web et développement"><span class="pf pf--sm pf--ring"><img src="images/agents-clean/05-lucas.jpg"  alt="Lucas — web et développement" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#maya"   title="Maya — Marketing et growth"><span class="pf pf--sm pf--ring"><img src="images/agents-clean/06-maya.jpg"   alt="Maya — marketing et growth" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#noah"   title="Noah — Administration et organisation"><span class="pf pf--sm pf--ring"><img src="images/agents-clean/07-noah.jpg"   alt="Noah — administration et organisation" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#sam"    title="Sam — IT et cybersécurité"><span class="pf pf--sm pf--ring"><img src="images/agents-clean/08-sam.jpg"    alt="Sam — IT et cybersécurité" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#seoya"  title="Séoya — SEO et rédaction web"><span class="pf pf--sm pf--ring"><img src="images/agents-clean/09-seoya.jpg"  alt="Séoya — SEO et rédaction web" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#thomas" title="Thomas — E-commerce et marketplace"><span class="pf pf--sm pf--ring"><img src="images/agents-clean/08-thomas.jpg" alt="Thomas — e-commerce et marketplace" loading="lazy"></span></a></div>
      </div>

      <div class="orbit__spin orbit__spin--slow" data-radius="54" data-offset="22">
        <div class="orbit__sat"><a href="workers.html#nora"   title="Nora — Support et relation client"><span class="pf pf--xs pf--ring"><img src="images/agents-clean/01-nora.jpg"   alt="Nora — support et relation client" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#sophie" title="Sophie — RH et recrutement"><span class="pf pf--xs pf--ring"><img src="images/agents-clean/02-sophie.jpg" alt="Sophie — RH et recrutement" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#dario"  title="Dario — Finance et contrôle"><span class="pf pf--xs pf--ring"><img src="images/agents-clean/03-dario.jpg"  alt="Dario — finance et contrôle" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#ines"   title="Inès — Data et analytics"><span class="pf pf--xs pf--ring"><img src="images/agents-clean/04-ines.jpg"   alt="Inès — data et analytics" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#yanis"  title="Yanis — Gestion de projet"><span class="pf pf--xs pf--ring"><img src="images/agents-clean/05-yanis.jpg"  alt="Yanis — gestion de projet" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#clara"  title="Clara — Juridique et contrats"><span class="pf pf--xs pf--ring"><img src="images/agents-clean/06-clara.jpg"  alt="Clara — juridique et contrats" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#amina"  title="Amina — Veille stratégique"><span class="pf pf--xs pf--ring"><img src="images/agents-clean/07-amina.jpg"  alt="Amina — veille stratégique" loading="lazy"></span></a></div>
        <div class="orbit__sat"><a href="workers.html#rayan"  title="Rayan — Automatisation et intégrations"><span class="pf pf--xs pf--ring"><img src="images/agents-clean/09-rayan.jpg"  alt="Rayan — automatisation et intégrations" loading="lazy"></span></a></div>
      </div>

      <div class="orbit__core">
        <a href="workers.html#chloe" title="Chloé — Agent Maître">
          <span class="pf pf--lg pf--gold"><img src="images/agents-clean/01-chloe.jpg" alt="Chloé — Agent Maître, orchestration et stratégie"></span>
        </a>
        <div class="orbit__name">Chloé</div>
        <div class="orbit__role">Agent Maître · Orchestration</div>
      </div>
    </div>

    <div class="rv rv-d2" style="display:flex;flex-wrap:wrap;gap:14px;justify-content:center;margin-top:52px;">
      <a class="btn btn--gold" href="workers.html">Découvrir les Workers <span class="arr">↗</span></a>
      <a class="btn btn--ghost" href="integrations.html">Les outils connectés</a>
    </div>
  </div>
</section>

<!-- ========== NOTRE FAÇON DE TRAVAILLER ========== -->
<section class="sec sec--sand">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">04 — Notre façon de travailler</span>
      <h2 class="h-lg" style="margin-top:22px;">De l'idée au <span class="it">résultat.</span></h2>
    </div>
    <div class="steps">
      <div class="step"><div class="step__n">01</div><div class="step__t">Comprendre</div><div class="step__d">Votre activité, vos contraintes et ce dont vous avez réellement besoin.</div></div>
      <div class="step"><div class="step__n">02</div><div class="step__t">Concevoir</div><div class="step__d">Une direction claire : structure, image, message et priorités.</div></div>
      <div class="step"><div class="step__n">03</div><div class="step__t">Construire</div><div class="step__d">Site, supports, contenus ou outils — réalisés et testés.</div></div>
      <div class="step"><div class="step__n">04</div><div class="step__t">Connecter</div><div class="step__d">Vos outils, vos processus et, si utile, vos Workers IA.</div></div>
      <div class="step"><div class="step__n">05</div><div class="step__t">Accompagner</div><div class="step__d">Suivi, ajustements et évolutions dans la durée.</div></div>
    </div>
  </div>
</section>
""" + CTA_FINAL
