# -*- coding: utf-8 -*-
"""Page Merci — confirmation après envoi du formulaire de contact."""
from bk_build import page_hero

PAGE  = "merci.html"
TITLE = "Merci — votre demande est bien partie | BK Entreprise"
DESC  = "Votre demande a bien été transmise à BK Entreprise. Réponse sous 24 à 48 heures ouvrées."
OG    = "images/project5.jpg"


def body():
    return """
<section class="sec sec--night" style="min-height:82svh;display:flex;align-items:center;padding-top:clamp(140px,15vw,200px);">
  <div class="halo halo--gold" style="width:620px;height:620px;top:50%;left:50%;transform:translate(-50%,-50%);"></div>
  <div class="wrap" style="text-align:center;">
    <div class="rv" style="width:78px;height:78px;border-radius:50%;margin:0 auto 30px;display:grid;place-items:center;
         background:linear-gradient(135deg,var(--gold-strong),var(--gold));color:#1B1405;font-size:34px;">✓</div>
    <span class="eyebrow rv rv-d1" style="justify-content:center;">Demande envoyée</span>
    <h1 class="h-xl rv rv-d2" style="margin-top:22px;max-width:16ch;margin-inline:auto;">
      Merci, c'est <span class="it">bien parti.</span>
    </h1>
    <p class="lead rv rv-d3" style="margin:26px auto 0;">
      Votre message a été transmis. Vous recevrez une réponse sous 24 à 48 heures ouvrées,
      à l'adresse que vous avez indiquée.
    </p>
    <div class="rv rv-d4" style="display:flex;flex-wrap:wrap;gap:14px;justify-content:center;margin-top:40px;">
      <a class="btn btn--gold" href="index.html">Retour à l'accueil <span class="arr">↗</span></a>
      <a class="btn btn--ghost" href="portfolio.html">Voir les réalisations</a>
    </div>
    <p class="lead rv rv-d5" style="margin:40px auto 0;font-size:14.5px;">
      Une urgence ? <a href="tel:+41799349946" style="color:var(--gold-strong);font-weight:600;">+41 79 934 99 46</a>
    </p>
  </div>
</section>

<section class="sec sec--cream">
  <div class="wrap">
    <div class="sec-head rv" style="text-align:center;margin-inline:auto;">
      <span class="eyebrow" style="justify-content:center;">En attendant</span>
      <h2 class="h-md" style="margin-top:20px;">Il y a de quoi <span class="it">regarder.</span></h2>
    </div>
    <div class="cards">
      <a class="card rv"><div class="card__i">◈</div><div class="card__t">Les réalisations</div>
        <p class="card__d">Plus de 500 créations : identités, affiches, menus et contenus vidéo.</p>
        <span class="link-arrow" style="margin-top:16px;">Voir ↗</span></a>
      <a class="card rv rv-d1" href="workers.html"><div class="card__i">◆</div><div class="card__t">Les Workers</div>
        <p class="card__d">17 Workers IA orchestrés par Chloé pour exécuter vos missions.</p>
        <span class="link-arrow" style="margin-top:16px;">Découvrir ↗</span></a>
      <a class="card rv rv-d2" href="profil.html"><div class="card__i">★</div><div class="card__t">Le profil</div>
        <p class="card__d">Qui est derrière BK Entreprise, et comment le projet s'est construit.</p>
        <span class="link-arrow" style="margin-top:16px;">Lire ↗</span></a>
    </div>
  </div>
</section>
""".replace('<a class="card rv"><div class="card__i">◈',
            '<a class="card rv" href="portfolio.html"><div class="card__i">◈')
