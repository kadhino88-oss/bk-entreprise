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
    def __init__(self): super().__init__(); self.refs=[]; self.h1=0; self.canonical=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1': self.h1+=1
        if tag=='link' and 'canonical' in (a.get('rel') or '').split(): self.canonical+=1
        for k in ('src','href'):
            if a.get(k): self.refs.append(a[k])
for page in root.glob('*.html'):
    if page.name.startswith('google'): continue
    raw=page.read_text(encoding='utf-8')
    p=Links(); p.feed(raw)
    if p.h1 != 1: errors.append(f'{page.name}: nombre de H1 = {p.h1}')
    if p.canonical != 1: errors.append(f'{page.name}: canonical = {p.canonical}')
    if 'Rue Joseph Pasquier' in raw: errors.append(page.name+': ancienne adresse')
    for link in p.refs:
        url=urlsplit(link)
        if url.scheme or link.startswith(('#','//','mailto:','tel:','data:','/')): continue
        target=unquote(url.path)
        if target and not (root/target).exists(): errors.append(page.name+': lien/ressource absent '+target)
    for block in re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',raw,re.S|re.I):
        try: json.loads(block)
        except Exception as ex: errors.append(page.name+': schema JSON-LD invalide '+str(ex))
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
