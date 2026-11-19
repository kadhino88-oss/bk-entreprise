#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérificateur du site BK Entreprise.
Contrôle : liens internes (aucun 404), ancres, fichiers images et vidéos,
présence des 18 portraits, cohérence header/footer, absence de l'ancien
numéro français, et noms exacts des réalisations."""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = sorted(f for f in os.listdir(ROOT)
               if f.endswith(".html") and not f.startswith("google"))

ok, ko, warn = [], [], []


def rel(p):
    return os.path.join(ROOT, p)


def check():
    anchors = {}
    for p in PAGES:
        h = open(rel(p), encoding="utf-8").read()
        anchors[p] = set(re.findall(r'id="([^"]+)"', h))

    for p in PAGES:
        h = open(rel(p), encoding="utf-8").read()

        # --- liens internes ---
        for href in re.findall(r'href="([^"]+)"', h):
            if href.startswith(("http", "mailto:", "tel:", "#", "data:")):
                if href.startswith("#") and len(href) > 1:
                    if href[1:] not in anchors[p]:
                        ko.append(f"{p} → ancre introuvable {href}")
                continue
            page, _, frag = href.partition("#")
            if page and not os.path.exists(rel(page)):
                ko.append(f"{p} → LIEN MORT {page}")
            elif frag and page and frag not in anchors.get(page, set()):
                ko.append(f"{p} → ancre {frag} absente de {page}")

        # --- fichiers médias ---
        for src in re.findall(r'(?:src|poster)="([^"]+)"', h):
            if src.startswith(("http", "data:")):
                continue
            if not os.path.exists(rel(src)):
                ko.append(f"{p} → FICHIER MANQUANT {src}")

        # --- images sans alt ---
        for tag in re.findall(r'<img[^>]*>', h):
            if 'alt=' not in tag:
                warn.append(f"{p} → <img> sans attribut alt")

        # --- structure commune ---
        for must, label in [('class="hdr', "header"), ('class="ftr', "footer"),
                            ('src="bk.js"', "bk.js"), ('href="bk.css"', "bk.css"),
                            ('class="mnav"', "menu mobile")]:
            if must not in h:
                ko.append(f"{p} → {label} absent")

        # --- ancien numéro français ---
        if re.search(r'\+33[\s\d]', h):
            ko.append(f"{p} → ancien numéro français présent")
        # --- numéro suisse dans le footer ---
        if "+41 79 934 99 46" not in h:
            ko.append(f"{p} → numéro suisse absent")

    # --- les 18 portraits ---
    d = rel("images/agents-clean")
    noms = ["01-chloe", "02-alex", "03-emma", "04-lea", "05-lucas", "06-maya", "07-noah",
            "08-sam", "09-seoya", "01-nora", "02-sophie", "03-dario", "04-ines",
            "05-yanis", "06-clara", "07-amina", "08-thomas", "09-rayan"]
    manquants = [n for n in noms if not os.path.exists(os.path.join(d, n + ".jpg"))]
    if manquants:
        ko.append("portraits manquants : " + ", ".join(manquants))
    else:
        ok.append(f"18 portraits présents dans images/agents-clean/")

    # --- noms exacts des réalisations ---
    data = json.load(open(rel("data-realisations.json"), encoding="utf-8"))
    pf = open(rel("portfolio.html"), encoding="utf-8").read()
    abs_ = [r["titre"] for r in data["realisations"] if r["titre"] not in pf]
    if abs_:
        ko.append("noms de réalisations absents du portfolio : " + " | ".join(abs_))
    else:
        ok.append(f"{len(data['realisations'])} noms de réalisations exacts dans portfolio.html")

    # --- vidéos ---
    vids = [v["src"] for v in data["videos"]]
    perdues = [v for v in vids if not os.path.exists(rel(v))]
    if perdues:
        ko.append("vidéos manquantes : " + ", ".join(perdues))
    else:
        ok.append(f"{len(vids)} vidéos présentes")

    ok.append(f"{len(PAGES)} pages contrôlées : " + ", ".join(PAGES))


if __name__ == "__main__":
    check()
    print("\n=== ✅ CONFORME ===")
    for x in ok:
        print("  •", x)
    if warn:
        print("\n=== ⚠️  À SURVEILLER ===")
        for x in sorted(set(warn)):
            print("  •", x)
    if ko:
        print("\n=== ❌ PROBLÈMES ===")
        for x in sorted(set(ko)):
            print("  •", x)
        sys.exit(1)
    print("\n✅ Aucun lien mort, aucun fichier manquant.\n")
