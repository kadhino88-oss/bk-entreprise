# -*- coding: utf-8 -*-
"""Page Intégrations — BK-AI-WORKERS au centre, les outils autour. Chaque outil a sa propre description."""
from bk_build import page_hero, CTA_FINAL

PAGE  = "integrations.html"
TITLE = "Intégrations — BK Entreprise"
DESC  = ("Google Workspace, Microsoft 365, Slack, Trello, Asana, Monday, Figma, HubSpot, Pipedrive, "
         "Intercom, Zendesk, Dropbox, Salesforce : vos outils reliés à l'écosystème BK.")
OG    = "images/project5.jpg"

# (clé, nom, catégorie, couleur, initiales, description PROPRE à chaque outil, site officiel)
TOOLS = [
 ("google",    "Google Workspace", "Bureautique",   "#1A73E8", "G",  "Gmail, Agenda, Drive et Docs : la base du quotidien, reliée à vos projets et à vos échanges clients.", "https://workspace.google.com"),
 ("microsoft", "Microsoft 365",    "Bureautique",   "#0078D4", "Ms", "Outlook, Teams, Calendar et OneDrive — l'environnement déjà en place dans la plupart des PME.", "https://www.microsoft.com/microsoft-365"),
 ("slack",     "Slack",            "Communication", "#4A154B", "Sl", "Les échanges d'équipe au même endroit, avec des notifications qui remontent là où vous travaillez.", "https://slack.com"),
 ("trello",    "Trello",           "Gestion",       "#0079BF", "Tr", "Des tableaux simples pour suivre l'avancement sans alourdir l'organisation.", "https://trello.com"),
 ("asana",     "Asana",            "Gestion",       "#F06A6A", "As", "Tâches, responsables et échéances pour les projets qui impliquent plusieurs personnes.", "https://asana.com"),
 ("monday",    "Monday.com",       "Gestion",       "#FF3D57", "Mo", "Une vue d'ensemble des chantiers en cours, lisible par toute l'équipe.", "https://monday.com"),
 ("figma",     "Figma",            "Design",        "#F24E1E", "Fi", "Maquettes et chartes graphiques partagées, commentées et validées avant production.", "https://figma.com"),
 ("hubspot",   "HubSpot",          "CRM",           "#FF7A59", "Hs", "Contacts, opportunités et campagnes marketing suivis dans un même outil.", "https://hubspot.com"),
 ("pipedrive", "Pipedrive",        "CRM",           "#017737", "Pd", "Un pipeline commercial visuel, pensé pour les équipes de vente réduites.", "https://pipedrive.com"),
 ("intercom",  "Intercom",         "Support",       "#1F8DED", "Ic", "Messagerie client sur votre site, avec historique et réponses automatisées.", "https://intercom.com"),
 ("zendesk",   "Zendesk",          "Support",       "#03363D", "Zd", "Tickets et demandes clients centralisés, avec suivi des délais de réponse.", "https://zendesk.com"),
 ("dropbox",   "Dropbox",          "Fichiers",      "#0061FF", "Db", "Fichiers partagés et versions conservées — utile quand les livrables circulent beaucoup.", "https://dropbox.com"),
 ("salesforce","Salesforce",       "CRM",           "#00A1E0", "Sf", "Le CRM des structures qui ont besoin de processus commerciaux détaillés.", "https://salesforce.com"),
]

USAGES = [
 ("01", "Vos outils restent les vôtres", "BK ne vous demande pas de tout changer. On part de ce que vous utilisez déjà et on le relie au reste."),
 ("02", "Les informations circulent", "Un devis signé, une demande client, une publication programmée : l'information passe d'un outil à l'autre sans ressaisie."),
 ("03", "Les Workers s'y branchent", "Quand c'est pertinent, un Worker travaille directement dans vos outils plutôt que dans une interface de plus."),
]


def body():
    # anneau : 7 outils à l'extérieur, 6 à l'intérieur
    ext, inte = TOOLS[:7], TOOLS[7:]

    def ring(items, radius, cls=""):
        pastilles = "".join(f"""
        <div class="eco__tool"><a href="{url}" target="_blank" rel="noopener" title="{nom} — {cat}">
          <span class="eco__ico" style="background:{col};color:#fff;">{ini}</span>{nom}</a></div>"""
            for _, nom, cat, col, ini, _, url in items)
        return f'<div class="eco__ring {cls}" data-radius="{radius}" style="{cls}"></div>{pastilles}'

    ext_html = "".join(f"""
      <div class="eco__tool"><a href="{url}" target="_blank" rel="noopener" title="{nom} — {cat}">
        <span class="eco__ico" style="background:{col};color:#fff;">{ini}</span>{nom}</a></div>"""
        for _, nom, cat, col, ini, _, url in ext)

    cartes = "".join(f"""
      <a class="tool rv rv-d{(i % 3) + 1}" id="{k}" href="{url}" target="_blank" rel="noopener">
        <span class="eco__ico" style="background:{col};color:#fff;width:34px;height:34px;border-radius:9px;font-size:12px;">{ini}</span>
        <span><span class="tool__n">{nom}</span><span class="tool__c">{cat}</span>
        <span class="tool__c" style="display:block;margin-top:7px;line-height:1.5;">{desc}</span></span>
      </a>""" for i, (k, nom, cat, col, ini, desc, url) in enumerate(TOOLS))

    usages = "".join(f"""
      <div class="flow__step rv rv-d{i}">
        <div class="flow__i">{n}</div>
        <div><div class="flow__t">{t}</div><div class="flow__d">{d}</div></div>
      </div>""" for i, (n, t, d) in enumerate(USAGES, 1))

    return page_hero(
        eyebrow="Outils &amp; connecteurs",
        title_html='Vos outils. <span class="it">Un même écosystème.</span>',
        lead=("Collaboration, gestion de projet, design, CRM, support, fichiers et suites bureautiques : "
              "BK relie les plateformes que vous utilisez déjà à vos processus et, si utile, à vos Workers."),
        cta1=("contact.html", "Parler de mes outils"),
        cta2=("#ecosysteme", "Voir l'écosystème ↓"),
    ) + f"""
<!-- ===== ÉCOSYSTÈME : BK-AI-WORKERS AU CENTRE ===== -->
<section class="sec sec--night" id="ecosysteme">
  <div class="halo halo--gold" style="width:640px;height:640px;top:50%;left:50%;transform:translate(-50%,-50%);opacity:.45;"></div>
  <div class="wrap">
    <div class="sec-head rv" style="text-align:center;margin-inline:auto;">
      <span class="eyebrow" style="justify-content:center;">01 — L'écosystème</span>
      <h2 class="h-lg" style="margin-top:22px;">Au centre, <span class="it">vos Workers.</span></h2>
      <p class="lead" style="margin-inline:auto;">Autour, les outils dans lesquels votre équipe travaille déjà.</p>
    </div>

    <div class="eco rv rv--z rv-d1" data-radius="40">
      <div class="eco__ring" style="inset:8%;"></div>
      <div class="eco__ring" style="inset:26%;"></div>
      <div class="eco__core">
        <b>BK-AI-<br>WORKERS</b>
        <small>17 Workers</small>
      </div>
      {ext_html}
    </div>

    <p class="lead rv rv-d2" style="text-align:center;margin:44px auto 0;font-size:14.5px;">
      Cette liste n'est pas exhaustive : d'autres outils peuvent être étudiés selon votre environnement.
    </p>
  </div>
</section>

<!-- ===== LISTE COMPLÈTE ===== -->
<section class="sec sec--dark">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">02 — Les plateformes</span>
      <h2 class="h-lg" style="margin-top:22px;">Treize outils, <span class="it">treize usages.</span></h2>
      <p class="lead">Chaque plateforme répond à un besoin précis — cliquez pour ouvrir son site officiel.</p>
    </div>
    <div class="tools">{cartes}</div>
  </div>
</section>

<!-- ===== COMMENT ÇA MARCHE ===== -->
<section class="sec sec--cream">
  <div class="halo halo--warm" style="width:480px;height:480px;bottom:-170px;left:-150px;"></div>
  <div class="wrap">
    <div class="split">
      <div class="rv">
        <span class="eyebrow">03 — En pratique</span>
        <h2 class="h-md" style="margin-top:20px;">Relier, pas <span class="it">remplacer.</span></h2>
        <p class="lead" style="margin-top:20px;">
          Changer d'outils coûte cher en temps et en habitudes. L'intégration consiste à faire
          communiquer ceux que vous avez, pour que l'information cesse d'être ressaisie.
        </p>
        <a class="btn btn--ink" style="margin-top:30px;" href="workers.html">Découvrir les Workers <span class="arr">↗</span></a>
      </div>
      <div class="rv rv--r rv-d1" style="--line-dark:var(--line);--tx-inv-muted:var(--tx-muted);">
        <div class="flow">{usages}</div>
      </div>
    </div>
  </div>
</section>
""" + CTA_FINAL
