# -*- coding: utf-8 -*-
"""Page Merci — confirmation après la validation du formulaire de contact."""

PAGE = "merci.html"
TITLE = "Merci pour votre demande | BK Entreprise"
DESC = ("Votre demande a été transmise à BK Entreprise. Nous vous recontacterons à l’adresse "
        "e-mail indiquée dans le formulaire.")
OG = "images/project5.jpg"


def body():
    return """
<section class="sec sec--night" style="min-height:78svh;display:flex;align-items:center;padding-top:clamp(140px,15vw,200px);">
  <div class="halo halo--gold" style="width:620px;height:620px;top:50%;left:50%;transform:translate(-50%,-50%);"></div>
  <div class="wrap" style="max-width:920px;text-align:center;">
    <div class="rv" style="width:78px;height:78px;border-radius:50%;margin:0 auto 30px;display:grid;place-items:center;background:linear-gradient(135deg,var(--gold-strong),var(--gold));color:#1B1405;font-size:34px;">✓</div>
    <span class="eyebrow rv rv-d1" style="justify-content:center;">Demande transmise</span>
    <h1 class="h-xl rv rv-d2" style="margin:22px auto 0;max-width:18ch;">Votre demande <span class="it">est bien envoyée.</span></h1>
    <p class="lead rv rv-d3" style="margin:26px auto 0;">Merci pour votre message. BK Entreprise va prendre connaissance de votre projet et vous recontacter à l’adresse e-mail indiquée dans le formulaire.</p>

    <div class="steps rv rv-d4" style="margin-top:40px;text-align:left;">
      <div class="step"><div class="step__n">01</div><div class="step__t">Nous lisons votre demande</div><div class="step__d">La prestation choisie, votre objectif et les informations transmises nous aident à comprendre votre besoin.</div></div>
      <div class="step"><div class="step__n">02</div><div class="step__t">Nous précisons le projet</div><div class="step__d">Si nécessaire, nous vous posons quelques questions avant de préparer une proposition adaptée.</div></div>
      <div class="step"><div class="step__n">03</div><div class="step__t">Vous décidez</div><div class="step__d">Le périmètre, le calendrier et le prix sont précisés avant tout engagement.</div></div>
    </div>

    <p class="lead rv rv-d5" style="margin:34px auto 0;font-size:15px;">Une précision à ajouter ou une demande urgente ? Écrivez à <a href="mailto:contact@bk-entreprise.com" style="color:var(--gold-strong);font-weight:600;">contact@bk-entreprise.com</a> ou appelez le <a href="tel:+41799349946" style="color:var(--gold-strong);font-weight:600;">+41 79 934 99 46</a>.</p>
    <div class="rv rv-d5" style="display:flex;flex-wrap:wrap;gap:14px;justify-content:center;margin-top:34px;">
      <a class="btn btn--gold" href="portfolio.html">Découvrir nos réalisations <span class="arr">↗</span></a>
      <a class="btn btn--ghost" href="index.html">Retour à l’accueil</a>
    </div>
  </div>
</section>
"""
