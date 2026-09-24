# -*- coding: utf-8 -*-
"""Page Contact — formulaire vivant, numéro suisse officiel, aucune trace de l'ancien numéro français."""
from bk_build import page_hero

PAGE  = "contact.html"
TITLE = "Contact — Agence digitale à Genève | BK Entreprise"
DESC  = ("Contactez BK Entreprise, agence digitale à Genève : création de site web, identité visuelle, "
         "communication, IT, conseil, événementiel ou agents IA. +41 79 934 99 46 — contact@bk-entreprise.com")
OG    = "images/project5.jpg"

SUJETS = ["Site web", "Design", "Communication", "IT",
          "Conseil", "Événementiel", "IA / Automatisation", "Autre"]


def body():
    chips = "".join('<button type="button" class="chip">%s</button>' % s for s in SUJETS)

    return page_hero(
        eyebrow="Parlons-en",
        title_html='Parlons de ce que vous <span class="it">voulez construire.</span>',
        lead=("Une idée, un besoin, un objectif : expliquez simplement ce que vous souhaitez "
              "construire, améliorer ou développer. On part de là."),
        cta1=("#formulaire", "Décrire mon projet"),
        cta2=("tel:+41799349946", "+41 79 934 99 46"),
    ) + f"""
<!-- ===== FORMULAIRE ===== -->
<section class="sec sec--night" id="formulaire" style="padding-top:clamp(56px,6vw,88px);">
  <div class="halo halo--gold" style="width:560px;height:560px;bottom:-220px;right:-180px;"></div>
  <div class="wrap">
    <div class="split split--wide" style="align-items:start;">

      <form class="rv" method="POST" action="https://formsubmit.co/contact@bk-entreprise.com">
        <input type="hidden" name="_next" value="https://www.bk-entreprise.com/merci.html">
        <input type="hidden" name="_subject" value="Nouvelle demande depuis bk-entreprise.com">
        <input type="hidden" name="_captcha" value="true">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
        <input type="hidden" name="sujet" id="sujet" value="">

        <span class="eyebrow">Votre projet porte sur</span>
        <div class="chips" data-subject-chips style="margin:16px 0 34px;">{chips}</div>

        <label class="field">
          <span>Nom et prénom</span>
          <input type="text" name="nom" required autocomplete="name" placeholder="Votre nom">
        </label>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
          <label class="field">
            <span>Email</span>
            <input type="email" name="email" required autocomplete="email" placeholder="vous@exemple.com">
          </label>
          <label class="field">
            <span>Téléphone <em style="text-transform:none;letter-spacing:0;opacity:.6;">(facultatif)</em></span>
            <input type="tel" name="telephone" autocomplete="tel" placeholder="+41 …">
          </label>
        </div>

        <label class="field">
          <span>Votre activité <em style="text-transform:none;letter-spacing:0;opacity:.6;">(facultatif)</em></span>
          <input type="text" name="activite" placeholder="Restaurant, commerce, association…">
        </label>

        <label class="field">
          <span>Décrivez votre projet</span>
          <textarea name="message" required
            placeholder="Votre objectif, ce qui existe déjà (site, logo, réseaux), et votre échéance si vous en avez une."></textarea>
        </label>

        <button class="btn btn--gold" type="submit" style="width:100%;justify-content:center;">
          Envoyer ma demande <span class="arr">↗</span>
        </button>
        <p style="margin-top:16px;font-size:13px;color:var(--tx-inv-muted);">
          Vos informations servent uniquement à répondre à votre demande.
        </p>
      </form>

      <aside class="rv rv--r rv-d1">
        <div class="card" style="background:rgba(255,255,255,.05);">
          <div class="card__i">☎</div>
          <div class="card__t">Par téléphone</div>
          <p class="card__d" style="font-size:1.15rem;margin-top:12px;">
            <a href="tel:+41799349946" style="color:var(--gold-strong);font-weight:600;">+41 79 934 99 46</a>
          </p>
        </div>

        <div class="card" style="background:rgba(255,255,255,.05);margin-top:20px;">
          <div class="card__i">✉</div>
          <div class="card__t">Par email</div>
          <p class="card__d" style="margin-top:12px;">
            <a href="mailto:contact@bk-entreprise.com" style="color:var(--gold-strong);font-weight:600;">contact@bk-entreprise.com</a>
          </p>
        </div>

        <div class="card" style="background:rgba(255,255,255,.05);margin-top:20px;">
          <div class="card__i">◎</div>
          <div class="card__t">Adresse</div>
          <p class="card__d" style="margin-top:12px;">
            Rue Joseph Pasquier 1<br>1203 Genève, Suisse
          </p>
        </div>

        <div class="card" style="background:rgba(255,255,255,.05);margin-top:20px;">
          <div class="card__i">◈</div>
          <div class="card__t">Réseaux</div>
          <div class="ftr__soc" style="margin-top:14px;">
            <a href="https://www.instagram.com/bk_entreprise7/" target="_blank" rel="noopener">Instagram</a>
            <a href="https://www.tiktok.com/@bkentreprise7" target="_blank" rel="noopener">TikTok</a>
            <a href="https://www.facebook.com/profile.php?id=61576414298574" target="_blank" rel="noopener">Facebook</a>
          </div>
        </div>

        <a class="card" href="portfolio.html" style="background:rgba(255,255,255,.05);margin-top:20px;display:block;">
          <div class="card__i">◎</div>
          <div class="card__t">Avant d'écrire</div>
          <p class="card__d" style="margin-top:12px;">
            Plus de 1000 créations graphiques et 100+ sites réalisés — voir des exemples concrets.
          </p>
          <span class="link-arrow" style="margin-top:14px;">Voir le portfolio ↗</span>
        </a>
      </aside>

    </div>
  </div>
</section>

<!-- ===== CE QUI SE PASSE ENSUITE ===== -->
<section class="sec sec--cream">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">Ce qui se passe ensuite</span>
      <h2 class="h-lg" style="margin-top:22px;">Trois étapes, <span class="it">sans engagement.</span></h2>
    </div>
    <div class="steps">
      <div class="step"><div class="step__n">01</div><div class="step__t">Échange</div><div class="step__d">Un appel ou un message suffit : on clarifie votre besoin, ce qui existe déjà (site, logo, réseaux) et votre échéance.</div></div>
      <div class="step"><div class="step__n">02</div><div class="step__t">Proposition</div><div class="step__d">Une direction claire, un périmètre écrit noir sur blanc et un budget réaliste — sans engagement de votre part à ce stade.</div></div>
      <div class="step"><div class="step__n">03</div><div class="step__t">Réalisation</div><div class="step__d">On construit par étapes, avec un point de validation avant de passer à la suivante.</div></div>
    </div>
  </div>
</section>
"""
