# -*- coding: utf-8 -*-
"""Page Intégrations — BK-AI-WORKERS au centre, les outils autour. Chaque outil a sa propre description.
Liste alignée sur le vrai catalogue de connecteurs (core/runtime/controlled-connectors/
CONTROLLED-CONNECTOR-CATALOG.json) : 35 outils nommés individuellement + 7 connecteurs génériques
par catégorie (calendrier, CRM, réseaux sociaux, analytics, design, supervision, RH) pour les outils
non listés un par un = 42 connecteurs réels au total. Aucun chiffre inventé."""
from bk_build import page_hero, CTA_FINAL

PAGE  = "integrations.html"
TITLE = "Intégrations — BK Entreprise"
DESC  = ("Plus de 40 connecteurs réels — Gmail, Outlook, Slack, Shopify, Stripe, HubSpot, Salesforce, "
         "Instagram, Figma et bien d'autres — reliés à l'écosystème BK et à vos Workers.")
OG    = "images/project5.jpg"

# (clé, nom, catégorie, couleur, initiales, description PROPRE à chaque outil, site officiel)
TOOLS = [
 ("gmail",      "Gmail",              "Email",          "#EA4335", "Gm", "Lecture, recherche et brouillons de messages — sans jamais envoyer sans votre accord.", "https://mail.google.com"),
 ("outlook",    "Outlook",            "Email",          "#0078D4", "Ol", "Messagerie professionnelle Microsoft, reliée à vos échanges et à vos suivis clients.", "https://outlook.com"),
 ("outlook_cal","Outlook Calendrier", "Agenda",         "#0078D4", "Oc", "Rendez-vous et disponibilités synchronisés avec le reste de votre organisation.", "https://outlook.com/calendar"),
 ("salesforce", "Salesforce",         "CRM",            "#00A1E0", "Sf", "Le CRM des structures qui ont besoin de processus commerciaux détaillés.", "https://salesforce.com"),
 ("hubspot",    "HubSpot",            "CRM",            "#FF7A59", "Hs", "Contacts, opportunités et campagnes marketing suivis dans un même outil.", "https://hubspot.com"),
 ("pipedrive",  "Pipedrive",          "CRM",            "#017737", "Pd", "Un pipeline commercial visuel, pensé pour les équipes de vente réduites.", "https://pipedrive.com"),
 ("linkedin",   "LinkedIn",           "Réseaux sociaux","#0A66C2", "Li", "Présence professionnelle, publications et prospection B2B.", "https://linkedin.com"),
 ("instagram",  "Instagram",          "Réseaux sociaux","#C13584", "Ig", "Publications, stories et messages — la vitrine visuelle de votre activité.", "https://instagram.com"),
 ("facebook",   "Facebook",           "Réseaux sociaux","#1877F2", "Fb", "Page pro, événements et communauté locale au même endroit.", "https://facebook.com"),
 ("tiktok",     "TikTok",             "Réseaux sociaux","#000000", "Tk", "Formats courts et portée organique, pour toucher une audience plus jeune.", "https://tiktok.com"),
 ("x",          "X (Twitter)",        "Réseaux sociaux","#000000", "X",  "Actualité, veille et prise de parole publique en temps réel.", "https://x.com"),
 ("wordpress",  "WordPress",          "Site web",       "#21759B", "Wp", "Le CMS le plus répandu — contenus et pages gérés en autonomie une fois livrés.", "https://wordpress.org"),
 ("webflow",    "Webflow",            "Site web",       "#146EF5", "Wf", "Sites sur-mesure avec une interface visuelle propre pour les mises à jour.", "https://webflow.com"),
 ("shopify",    "Shopify",            "E-commerce",     "#95BF47", "Sh", "Boutique en ligne complète : catalogue, paiement, commandes et livraison.", "https://shopify.com"),
 ("woocommerce","WooCommerce",        "E-commerce",     "#96588A", "Wc", "E-commerce sur WordPress, pour garder tout au même endroit.", "https://woocommerce.com"),
 ("stripe",     "Stripe",             "Paiement",       "#635BFF", "St", "Paiements en ligne sécurisés, abonnements et facturation automatisée.", "https://stripe.com"),
 ("paypal",     "PayPal",             "Paiement",       "#003087", "Pp", "Un moyen de paiement que vos clients connaissent déjà et utilisent en confiance.", "https://paypal.com"),
 ("quickbooks", "QuickBooks",         "Comptabilité",   "#2CA01C", "Qb", "Comptabilité et facturation, avec vos données commerciales déjà à jour.", "https://quickbooks.intuit.com"),
 ("xero",       "Xero",               "Comptabilité",   "#13B5EA", "Xe", "Une alternative comptable complète pour les structures en croissance.", "https://xero.com"),
 ("slack",      "Slack",              "Communication",  "#4A154B", "Sl", "Les échanges d'équipe au même endroit, avec des notifications qui remontent là où vous travaillez.", "https://slack.com"),
 ("teams",      "Microsoft Teams",    "Communication",  "#6264A7", "Te", "Réunions, chat et fichiers d'équipe dans l'environnement Microsoft.", "https://teams.microsoft.com"),
 ("whatsapp",   "WhatsApp Business",  "Communication",  "#25D366", "Wa", "Le canal que vos clients utilisent déjà pour vous écrire directement.", "https://business.whatsapp.com"),
 ("gdrive",     "Google Drive",       "Fichiers",       "#4285F4", "Gd", "Fichiers partagés et organisés, accessibles à toute l'équipe.", "https://drive.google.com"),
 ("dropbox",    "Dropbox",            "Fichiers",       "#0061FF", "Db", "Fichiers partagés et versions conservées — utile quand les livrables circulent beaucoup.", "https://dropbox.com"),
 ("onedrive",   "OneDrive",           "Fichiers",       "#0078D4", "Od", "Stockage Microsoft relié directement à Outlook et Teams.", "https://onedrive.live.com"),
 ("gsc",        "Google Search Console","Analytics",    "#4285F4", "Gs", "Suivi de votre visibilité réelle sur Google : requêtes, positions, erreurs d'indexation.", "https://search.google.com/search-console"),
 ("gads",       "Google Ads",         "Publicité",      "#4285F4", "Ga", "Campagnes de recherche et de visibilité, pour apparaître au bon moment.", "https://ads.google.com"),
 ("metaads",    "Meta Ads",           "Publicité",      "#0866FF", "Ma", "Campagnes Facebook et Instagram, ciblées sur votre audience réelle.", "https://www.facebook.com/business/ads"),
 ("asana",      "Asana",              "Gestion",        "#F06A6A", "As", "Tâches, responsables et échéances pour les projets qui impliquent plusieurs personnes.", "https://asana.com"),
 ("trello",     "Trello",             "Gestion",        "#0079BF", "Tr", "Des tableaux simples pour suivre l'avancement sans alourdir l'organisation.", "https://trello.com"),
 ("monday",     "Monday.com",         "Gestion",        "#FF3D57", "Mo", "Une vue d'ensemble des chantiers en cours, lisible par toute l'équipe.", "https://monday.com"),
 ("zendesk",    "Zendesk",            "Support",        "#03363D", "Zd", "Tickets et demandes clients centralisés, avec suivi des délais de réponse.", "https://zendesk.com"),
 ("intercom",   "Intercom",           "Support",        "#1F8DED", "Ic", "Messagerie client sur votre site, avec historique et réponses automatisées.", "https://intercom.com"),
 ("canva",      "Canva",              "Design",         "#00C4CC", "Cv", "Visuels rapides et cohérents pour les contenus du quotidien.", "https://canva.com"),
 ("figma",      "Figma",              "Design",         "#F24E1E", "Fi", "Maquettes et chartes graphiques partagées, commentées et validées avant production.", "https://figma.com"),
]

# Connecteurs génériques (par catégorie, sans produit unique imposé) — comptent dans le total réel
# mais ne sont pas des marques individuelles : présentés à part pour rester honnêtes sur ce qu'ils sont.
GENERIQUES = [
 "Agenda (autre que Outlook)", "CRM (autre que Salesforce/HubSpot/Pipedrive)", "Réseaux sociaux (autre plateforme)",
 "Web Analytics (autre qu'un outil listé)", "Design (autre que Canva/Figma)", "Supervision &amp; monitoring", "RH &amp; recrutement",
]

# Sélection pour l'anneau visuel — les marques les plus reconnues, un représentant par grande
# famille d'usage (le reste de la liste, complète, est juste en dessous).
RING_KEYS = {"gmail", "outlook", "slack", "teams", "gdrive", "dropbox", "shopify", "stripe",
             "hubspot", "salesforce", "instagram", "figma"}

USAGES = [
 ("01", "Vos outils restent les vôtres", "BK ne vous demande pas de tout changer. On part de ce que vous utilisez déjà et on le relie au reste."),
 ("02", "Les informations circulent", "Un devis signé, une demande client, une publication programmée : l'information passe d'un outil à l'autre sans ressaisie."),
 ("03", "Les Workers s'y branchent", "Quand c'est pertinent, un Worker travaille directement dans vos outils plutôt que dans une interface de plus."),
]


def body():
    ring_items = [t for t in TOOLS if t[0] in RING_KEYS]

    ext_html = "".join(f"""
      <div class="eco__tool"><a href="{url}" target="_blank" rel="noopener" title="{nom} — {cat}">
        <span class="eco__ico" style="background:{col};color:#fff;">{ini}</span>{nom}</a></div>"""
        for _, nom, cat, col, ini, _, url in ring_items)

    cartes = "".join(f"""
      <a class="tool rv rv-d{(i % 3) + 1}" id="{k}" href="{url}" target="_blank" rel="noopener">
        <span class="eco__ico" style="background:{col};color:#fff;width:34px;height:34px;border-radius:9px;font-size:12px;">{ini}</span>
        <span><span class="tool__n">{nom}</span><span class="tool__c">{cat}</span>
        <span class="tool__c" style="display:block;margin-top:7px;line-height:1.5;">{desc}</span></span>
      </a>""" for i, (k, nom, cat, col, ini, desc, url) in enumerate(TOOLS))

    generiques = "".join(f'<span class="tag" style="opacity:.75;">{g}</span>' for g in GENERIQUES)

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
      <p class="lead" style="margin-inline:auto;">Autour, un aperçu des outils dans lesquels votre équipe travaille déjà — la liste complète est juste en dessous.</p>
    </div>

    <div class="eco rv rv--z rv-d1" data-radius="40">
      <div class="eco__ring" style="inset:8%;"></div>
      <div class="eco__ring" style="inset:26%;"></div>
      <a class="eco__core" href="https://bk-ai-workers.com" target="_blank" rel="noopener" title="Ouvrir BK-AI-WORKERS">
        <b>BK-AI-<br>WORKERS</b>
        <small>17 Workers</small>
      </a>
      {ext_html}
    </div>

    <p class="lead rv rv-d2" style="text-align:center;margin:44px auto 0;font-size:14.5px;">
      42 connecteurs réels au total : 35 outils nommés individuellement ci-dessous, plus 7 connecteurs
      génériques par catégorie pour les plateformes non listées une à une.
    </p>
  </div>
</section>

<!-- ===== LISTE COMPLÈTE ===== -->
<section class="sec sec--dark">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">02 — Les plateformes</span>
      <h2 class="h-lg" style="margin-top:22px;">35 outils nommés, <span class="it">35 usages précis.</span></h2>
      <p class="lead">Chaque plateforme répond à un besoin précis — cliquez pour ouvrir son site officiel.</p>
    </div>
    <div class="tools">{cartes}</div>

    <div class="rv rv-d1" style="margin-top:32px;padding-top:28px;border-top:1px solid var(--line-dark);">
      <div class="eyebrow" style="font-size:11px;">+ 7 connecteurs génériques par catégorie</div>
      <p class="lead" style="margin-top:12px;font-size:14px;">
        Pour les outils qui ne figurent pas encore individuellement dans la liste ci-dessus, un
        connecteur générique existe par catégorie — sans imposer une marque en particulier.
      </p>
      <div class="chips" style="margin-top:14px;">{generiques}</div>
    </div>
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
