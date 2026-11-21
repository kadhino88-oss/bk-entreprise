# -*- coding: utf-8 -*-
"""Page Contact — demandes envoyées à la boîte Gmail de BK Entreprise."""
from html import escape

from bk_build import page_hero

PAGE = "contact.html"
TITLE = "Contact — Création de site web à Genève | BK Entreprise"
DESC = ("Parlez à BK Entreprise de votre site web, refonte, application, référencement SEO, "
        "CRO ou automatisation IA à Genève. Projets à distance en Suisse et en France.")
OG = "images/apercu-tresorsbyninel.jpg"

PRESTATIONS = [
    ("BK CLIENTS+", "Site vitrine et visibilité locale"),
    ("Diagnostic gratuit", "Échange initial de 15 minutes"),
    ("Site web", "Création ou refonte"),
    ("Application", "Web ou mobile"),
    ("Référencement SEO", "Visibilité sur Google"),
    ("IA / Automatisation", "Tâches et outils métier"),
    ("Design", "Logo et identité visuelle"),
    ("Communication", "Contenus et supports"),
    ("IT", "Assistance et infrastructure"),
    ("Conseil", "Cadrage et stratégie"),
    ("Événementiel", "Communication événementielle"),
    ("Autre", "À préciser ensemble"),
]

BUDGETS = [
    ("À définir ensemble", ""),
    ("Moins de 1 500 CHF", ""),
    ("1 500 à 3 000 CHF", ""),
    ("3 000 à 6 000 CHF", ""),
    ("Plus de 6 000 CHF", ""),
]

ORIGINES = [
    ("Recherche Google", ""),
    ("Google Maps", ""),
    ("Recommandation", ""),
    ("Instagram / Facebook / TikTok", ""),
    ("Chat ou moteur IA", ""),
    ("Autre", ""),
]


def radio_cards(name, prefix, choices, required=False, currency=False):
    cards = []
    for index, (label, detail) in enumerate(choices):
        field_id = f"{prefix}-{index}"
        value = escape(label, quote=True)
        visible = escape(label)
        required_attr = " required" if required else ""
        input_currency_attr = ""
        text_currency_attr = ""
        if currency and "CHF" in label:
            template = escape(label.replace("CHF", "{c}"), quote=True)
            input_currency_attr = f' data-cur-tpl="{template}"'
            text_currency_attr = f' data-cur-tpl="{template}"'
        subline = f"<small>{escape(detail)}</small>" if detail else ""
        cards.append(
            f'<label class="contact-option" for="{field_id}">'
            f'<input type="radio" id="{field_id}" name="{name}" value="{value}"'
            f'{required_attr}{input_currency_attr}>'
            f'<span><strong{text_currency_attr}>{visible}</strong>{subline}</span>'
            "</label>"
        )
    return "".join(cards)


def body():
    prestation_cards = radio_cards("sujet", "sujet", PRESTATIONS, required=True)
    budget_cards = radio_cards("budget", "budget", BUDGETS, currency=True)
    origin_cards = radio_cards("origine_declaree", "origine_declaree", ORIGINES)

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
  <div class="wrap">
    <div class="split split--wide" style="align-items:start;">
      <form class="rv contact-form" method="POST" action="https://formsubmit.co/bkentreprise88@gmail.com">
        <input type="hidden" name="_next" value="https://www.bk-entreprise.com/merci.html">
        <input type="hidden" name="_subject" value="Nouvelle demande depuis bk-entreprise.com">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="true">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">

        <fieldset class="contact-choices" id="prestations">
          <legend>1. Quelle prestation vous intéresse ? *</legend>
          <div class="contact-options">{prestation_cards}</div>
        </fieldset>
        <p id="pack-notice" class="contact-required" style="color:var(--gold-strong);font-weight:500;" hidden></p>

        <fieldset class="contact-choices">
          <legend>2. Quel budget envisagez-vous ? (facultatif)</legend>
          <p class="contact-required" style="margin:-8px 0 16px;">
            <a href="tarifs.html" style="color:var(--gold-strong);text-decoration:underline;text-underline-offset:3px;">Consulter la grille tarifaire</a>
          </p>
          <div class="contact-options">{budget_cards}</div>
        </fieldset>
        <label class="field contact-budget">
          <span>Ou indiquez votre montant en <span data-cur>CHF</span> (facultatif)</span>
          <input type="number" name="budget_libre" min="0" step="1" inputmode="numeric" placeholder="Ex. 2500">
          <small>Une indication pour cadrer le projet, pas un engagement.</small>
        </label>

        <fieldset class="contact-choices">
          <legend>3. Comment nous avez-vous connu ? (facultatif)</legend>
          <div class="contact-options">{origin_cards}</div>
        </fieldset>

        <h2 class="h-md contact-details-title">4. Votre projet et vos coordonnées</h2>
        <p class="contact-required">* Champs obligatoires : prestation, nom, e-mail et description du projet.</p>

        <label class="field">
          <span>Nom et prénom *</span>
          <input type="text" name="nom" required autocomplete="name" placeholder="Votre nom">
        </label>

        <div class="contact-row">
          <label class="field">
            <span>E-mail *</span>
            <input type="email" name="email" required autocomplete="email" placeholder="vous@exemple.com">
          </label>
          <label class="field">
            <span>Téléphone <em style="text-transform:none;letter-spacing:0;opacity:.6;">(facultatif)</em></span>
            <input type="tel" name="telephone" autocomplete="tel" placeholder="+41 …">
          </label>
        </div>

        <label class="field">
          <span>Votre activité et votre ville ou pays <em style="text-transform:none;letter-spacing:0;opacity:.6;">(facultatif)</em></span>
          <input type="text" name="activite" placeholder="Ex. boutique à Genève, entreprise à Lyon…">
        </label>

        <label class="field">
          <span>Décrivez votre projet *</span>
          <textarea name="message" required placeholder="Votre objectif, ce qui existe déjà (site, logo, réseaux), et votre échéance si vous en avez une."></textarea>
        </label>

        <label class="field">
          <span>Votre site actuel (facultatif)</span>
          <input type="url" name="site_actuel" placeholder="https://votre-site.ch" autocomplete="url">
        </label>

        <input type="hidden" name="devise" id="devise-visiteur" value="CHF">
        <input type="hidden" name="offre_choisie" id="pack-demande" value="">
        <input type="hidden" name="page_demande" id="page-demande" value="contact.html">
        <input type="hidden" name="source_campagne" id="source-campagne" value="directe ou non renseignée">

        <p style="margin:16px 0;">Après l’envoi, terminez la vérification anti-spam pour transmettre votre demande. En cas de difficulté, <a href="mailto:contact@bk-entreprise.com">écrivez-nous directement</a> ou appelez le <a href="tel:+41799349946">+41 79 934 99 46</a>.</p>
        <p id="contact-feedback" role="status" aria-live="polite" style="margin:16px 0;color:#f2cd7d"></p>
        <button class="btn btn--gold" type="submit" style="width:100%;justify-content:center;">
          Demander ma proposition <span class="arr">↗</span>
        </button>
        <p style="margin-top:16px;font-size:13px;color:var(--tx-inv-muted);">
          Vos informations et l’origine déclarée de votre demande servent à traiter votre projet et comprendre comment vous nous avez trouvé. <a href="politique-de-confidentialite.html">Politique de confidentialité</a>.
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
          <div class="card__t">Zone d’intervention</div>
          <p class="card__d" style="margin-top:12px;">Genève et communes voisines chez les clients · prestations numériques à distance en Suisse et en France.</p>
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
          <div class="card__t">Avant d’écrire</div>
          <p class="card__d" style="margin-top:12px;">Découvrez des exemples de sites, de design et de projets réalisés.</p>
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
      <div class="step"><div class="step__n">01</div><div class="step__t">Échange</div><div class="step__d">Un appel ou un message suffit : on clarifie votre besoin, ce qui existe déjà et votre échéance.</div></div>
      <div class="step"><div class="step__n">02</div><div class="step__t">Proposition</div><div class="step__d">Une direction claire, un périmètre écrit et un budget réaliste, sans engagement à ce stade.</div></div>
      <div class="step"><div class="step__n">03</div><div class="step__t">Réalisation</div><div class="step__d">On construit par étapes, avec un point de validation avant de passer à la suivante.</div></div>
    </div>
  </div>
</section>
"""
