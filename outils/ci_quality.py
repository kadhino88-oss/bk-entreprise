#!/usr/bin/env python3
"""BK Entreprise: tests statiques des pages déployables."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json, re, sys, xml.etree.ElementTree as ET
root = Path(__file__).resolve().parents[1]
required = ['index.html', 'contact.html', 'tarifs.html', 'bk-clients-plus.html',
            'mentions-legales.html', 'politique-de-confidentialite.html',
            'conditions-utilisation.html']
errors=[]
for f in required:
    if not (root / f).is_file(): errors.append(f+' absent')
class Links(HTMLParser):
    def __init__(self): super().__init__(); self.refs=[]; self.hrefs=[]; self.locales=[]; self.h1=0; self.canonical=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1': self.h1+=1
        if tag=='link' and 'canonical' in (a.get('rel') or '').split(): self.canonical+=1
        if tag=='meta' and a.get('property')=='og:locale': self.locales.append(a.get('content'))
        if tag=='a' and a.get('href'): self.hrefs.append(a['href'])
        for k in ('src','href'):
            if a.get(k): self.refs.append(a[k])
service_pages={'services-it.html','referencement-seo-geneve.html',
               'automatisation-ia-geneve.html','creation-application-geneve.html'}
service_nodes=[]
for page in root.glob('*.html'):
    if page.name.startswith('google'): continue
    raw=page.read_text(encoding='utf-8')
    p=Links(); p.feed(raw)
    if p.h1 != 1: errors.append(f'{page.name}: nombre de H1 = {p.h1}')
    if p.canonical != 1: errors.append(f'{page.name}: canonical = {p.canonical}')
    if p.locales != ['fr_CH']: errors.append(f'{page.name}: og:locale doit être fr_CH')
    legal={Path(urlsplit(h).path).name for h in p.hrefs}
    for name in ('mentions-legales.html','politique-de-confidentialite.html','conditions-utilisation.html'):
        if name not in legal: errors.append(f'{page.name}: lien légal absent {name}')
    if 'Rue Joseph Pasquier' in raw: errors.append(page.name+': ancienne adresse')
    for link in p.refs:
        url=urlsplit(link)
        if url.scheme or link.startswith(('#','//','mailto:','tel:','data:','/')): continue
        target=unquote(url.path)
        if target and not (root/target).exists(): errors.append(page.name+': lien/ressource absent '+target)
    for block in re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',raw,re.S|re.I):
        try:
            schema=json.loads(block)
            nodes=schema.get('@graph',[schema]) if isinstance(schema,dict) else []
            for node in nodes:
                if not isinstance(node,dict): continue
                if node.get('@type')=='ProfessionalService': errors.append(page.name+': ancien type ProfessionalService')
                if node.get('@type')=='Service':
                    service_nodes.append(page.name)
                    if node.get('provider',{}).get('@id')!='https://www.bk-entreprise.com/#organization':
                        errors.append(page.name+': fournisseur Service incohérent')
        except Exception as ex: errors.append(page.name+': schema JSON-LD invalide '+str(ex))
if set(service_nodes)!=service_pages or len(service_nodes)!=len(service_pages):
    errors.append('schema Service absent ou dupliqué sur les pages offre')
contact=(root/'contact.html').read_text(encoding='utf-8')
contact_source=(root/'outils'/'pages'/'contact.py').read_text(encoding='utf-8')
for label,text in (('contact.html',contact),('contact.py',contact_source)):
    if 'formsubmit.co/bkentreprise88@gmail.com' not in text: errors.append(label+': destinataire Gmail incorrect')
    if 'formsubmit.co/contact@bk-entreprise.com' in text: errors.append(label+': ancien destinataire du formulaire')
for field in ('sujet','budget','origine_declaree'):
    if f'name="{field}"' not in contact: errors.append('contact.html: champ absent '+field)
    if f'radio_cards("{field}"' not in contact_source: errors.append('contact.py: générateur de champ absent '+field)
if 'https://www.bk-entreprise.com/merci.html' not in contact: errors.append('contact.html: redirection Merci absente')
if 'noindex, follow' not in (root/'merci.html').read_text(encoding='utf-8'):
    errors.append('merci.html: la confirmation doit rester noindex')
llms=root/'llms.txt'
if not llms.is_file(): errors.append('llms.txt absent')
else:
    for path in re.findall(r'https://www\.bk-entreprise\.com/([\w-]+\.html)',llms.read_text(encoding='utf-8')):
        if not (root/path).is_file(): errors.append('llms.txt: page absente '+path)
robots=(root/'robots.txt').read_text(encoding='utf-8')
if 'User-agent: OAI-SearchBot' not in robots or 'Sitemap: https://www.bk-entreprise.com/sitemap.xml' not in robots:
    errors.append('robots.txt: OAI-SearchBot ou sitemap non déclaré')
for name in ('data-realisations.json','data-tarifs.json'):
    try: json.loads((root/name).read_text(encoding='utf-8'))
    except Exception as ex: errors.append(name+': JSON invalide '+str(ex))
try:
    tree=ET.parse(root/'sitemap.xml')
    for loc in tree.findall('.//{*}loc'):
        url=urlsplit(loc.text or '')
        target=(root/'index.html') if url.path in ('','/') else root/url.path.lstrip('/')
        if not target.exists(): errors.append('sitemap: URL sans fichier '+url.path)
except Exception as ex: errors.append('sitemap.xml: '+str(ex))
if errors:
    print('ECHEC ('+str(len(errors))+'):\n'+'\n'.join(errors)); sys.exit(1)
print('OK — liens locaux, ressources, SEO, JSON-LD et sitemap vérifiés.')
