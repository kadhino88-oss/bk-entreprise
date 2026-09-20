#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fabrique les portraits circulaires des Workers à partir des posters d'origine.
Détecte le visage, cadre carré avec de la marge au-dessus de la tête
(jamais de tête coupée), et exporte en 640x640.
"""
import cv2, os, sys, json

SRC = "/root/.claude/uploads/55ef1ace-adc2-5434-af6d-0f8159ac00d5"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images/agents-clean")

# fichier source -> (slug de sortie, prénom)
MAP = [
 ("e489a698-image.png", "01-chloe",  "Chloé"),
 ("da8d08a3-image.png", "02-sophie", "Sophie"),
 ("cae93269-image.png", "09-seoya",  "Séoya"),
 ("4b92d9d2-image.png", "05-yanis",  "Yanis"),
 ("53057df9-image.png", "04-ines",   "Inès"),
 ("6c367f82-image.png", "03-dario",  "Dario"),
 ("1f8f046d-image.png", "06-clara",  "Clara"),
 ("3b80f0ac-image.png", "02-alex",   "Alex"),
 ("c191356b-image.png", "03-emma",   "Emma"),
 ("3d4517d5-image.png", "05-lucas",  "Lucas"),
 ("8d2021ea-image.png", "06-maya",   "Maya"),
 ("848119f2-image.png", "04-lea",    "Léa"),          # variante beige
 ("0d20bf84-image.png", "07-noah",   "Noah"),
 ("8cf6cb73-image.png", "08-sam",    "Sam"),
 ("62a973c7-image.png", "09-rayan",  "Rayan"),
 ("e3b8b517-image.png", "08-thomas", "Thomas"),
 ("6bd85c2d-image.png", "07-amina",  "Amina"),
 ("d5bdb385-image.png", "01-nora",   "Nora"),
 ("6b7f5f5e-image.png", "04-lea-variante-creme", "Léa (variante crème)"),
]

# Cadrages validés à l'œil quand la détection automatique se trompait
# (elle accrochait un logo BK ou un visage d'arrière-plan).
# Fractions de la largeur/hauteur de l'affiche : (x, y, largeur du visage)
MANUEL = {
 "01-chloe": (0.452, 0.086, 0.114),
 "01-nora":  (0.469, 0.092, 0.134),
 "04-lea":   (0.399, 0.068, 0.146),
 "06-clara": (0.409, 0.074, 0.131),
 "06-maya":  (0.440, 0.125, 0.125),
 "08-sam":   (0.420, 0.075, 0.135),
 "09-seoya": (0.475, 0.076, 0.155),
}

TAILLE = 640
casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
os.makedirs(OUT, exist_ok=True)
rapport = []

for fichier, slug, nom in MAP:
    p = os.path.join(SRC, fichier)
    if not os.path.exists(p):
        rapport.append((nom, slug, "SOURCE INTROUVABLE", None)); continue
    img = cv2.imread(p)
    if img is None:
        rapport.append((nom, slug, "LECTURE IMPOSSIBLE", None)); continue
    H, W = img.shape[:2]
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if slug in MANUEL:
        fx, fy, fw = MANUEL[slug]
        x, y, w, h = int(fx*W), int(fy*H), int(fw*W), int(fw*W)
        faces = [(x, y, w, h)]
    else:
        faces = []
    for sf, mn in (() if slug in MANUEL else ((1.05, 6), (1.08, 4), (1.15, 3))):
        faces = casc.detectMultiScale(gris, scaleFactor=sf, minNeighbors=mn,
                                      minSize=(int(W*0.04), int(W*0.04)))
        if len(faces): break
    if not len(faces):
        rapport.append((nom, slug, "AUCUN VISAGE DÉTECTÉ", None)); continue

    # le plus grand visage, et parmi eux le plus haut dans l'image
    faces = sorted(faces, key=lambda f: -f[2]*f[3])[:3]
    x, y, w, h = sorted(faces, key=lambda f: f[1])[0]

    cx = x + w/2
    cy = y + h/2
    # cadre : 3.0x la largeur du visage -> visage + cou + épaules, avec de l'air
    cote = int(max(w, h) * 3.0)
    # on remonte légèrement le centre pour garder de la marge au-dessus du crâne
    cy = cy - h * 0.18

    x0 = int(cx - cote/2); y0 = int(cy - cote/2)
    x1 = x0 + cote;        y1 = y0 + cote

    # si le cadre dépasse, on complète par réplication au lieu de rogner le visage
    pl = max(0, -x0); pt = max(0, -y0)
    pr = max(0, x1 - W); pb = max(0, y1 - H)
    if pl or pt or pr or pb:
        img = cv2.copyMakeBorder(img, pt, pb, pl, pr, cv2.BORDER_REPLICATE)
        x0 += pl; x1 += pl; y0 += pt; y1 += pt

    crop = img[y0:y1, x0:x1]
    crop = cv2.resize(crop, (TAILLE, TAILLE), interpolation=cv2.INTER_LANCZOS4)
    dest = os.path.join(OUT, slug + ".jpg")
    cv2.imwrite(dest, crop, [cv2.IMWRITE_JPEG_QUALITY, 92])

    # marge au-dessus du crâne, en % de la hauteur du cadre
    marge = (y - y0) / cote * 100
    rapport.append((nom, slug, "ok", round(marge, 1)))

print(f"{'Worker':<22}{'fichier':<26}{'état':<24}{'marge au-dessus du visage'}")
print("-"*92)
for nom, slug, etat, marge in rapport:
    m = f"{marge} %" if marge is not None else "—"
    print(f"{nom:<22}{slug+'.jpg':<26}{etat:<24}{m}")
