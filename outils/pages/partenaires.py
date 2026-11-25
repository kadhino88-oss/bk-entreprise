# -*- coding: utf-8 -*-
from bk_build import page_hero

PAGE = "partenaires.html"
TITLE = "Partenaires et collaborations professionnelles | BK Entreprise Genève"
DESC = "Collaborations entre professionnels du web, du design, du SEO, du CRO et de l’automatisation IA à Genève et à distance."


def body():
    return page_hero(
        eyebrow="Espace partenaires · Genève et à distance",
        title_html='Des compétences complémentaires, <span class="it">des projets mieux menés</span>',
        lead="BK Entreprise échange avec les indépendants, agences et spécialistes qui souhaitent collaborer sur des projets web, SEO, CRO et automatisation IA.",
        cta1=("#collaboration", "Présenter mon expertise"),
        cta2=("contact.html?prestation=Autre&amp;pack=Partenariat#formulaire", "Proposer un partenariat"),
    ) + """
<section class="sec sec--cream" id="collaboration"><div class="wrap"><span class="eyebrow">Comment collaborer</span><h2 class="h-lg" style="margin-top:20px">Un cadre clair <span class="it">pour chaque mission</span></h2><div class="growth-grid"><article class="card"><h3 class="card__t">Expertise complémentaire</h3><p class="card__d">Design, rédaction, développement, SEO ou automatisation. Présentez vos compétences et vos disponibilités.</p></article><article class="card"><h3 class="card__t">Projets en commun</h3><p class="card__d">Les rôles, livrables, délais et budgets sont cadrés ensemble avant chaque mission.</p></article><article class="card"><h3 class="card__t">Recommandations</h3><p class="card__d">Les conditions d’une éventuelle rémunération sont discutées et formalisées avant la mission.</p></article></div></div></section>
<section class="sec sec--night"><div class="wrap"><span class="eyebrow">Premier échange</span><h2 class="h-lg" style="margin-top:20px">Parlez-nous de votre <span class="it">proposition</span></h2><p class="lead" style="margin-top:18px">Indiquez votre spécialité, votre zone, vos disponibilités et le type de partenariat envisagé.</p><a class="btn btn--gold" style="margin-top:26px" href="contact.html?prestation=Autre&amp;pack=Partenariat#formulaire">Présenter mon projet</a></div></section>
"""
