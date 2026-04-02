# =========================================
# 🔄 Script optimisé : Mise à jour & Déploiement
# =========================================

Write-Host "=== MISE À JOUR AUTOMATIQUE DES IMAGES ET VIDÉOS ===`n"

# ========================
# 1️⃣ Images
# ========================
$images = Get-ChildItem "images" -File | Where-Object { $_.BaseName -match "^project\d*$" -or $_.BaseName -eq "project" }
$images = $images | Sort-Object LastWriteTime

$counter = 1

foreach ($img in $images) {
    $ext = $img.Extension
    $expectedName = "project$counter$ext"
    
    if ($img.Name -ne $expectedName) {
        # Utiliser un nom temporaire pour éviter les conflits
        $tempName = "temp_$counter$ext"
        Rename-Item $img.FullName "images\$tempName"
        Write-Host "$($img.Name) temporairement renommé en $tempName"
    }
    $counter++
}

# Renommer les fichiers temporaires en noms définitifs
$counter = 1
foreach ($img in Get-ChildItem "images" -File | Where-Object { $_.Name -match "^temp_\d+" } | Sort-Object Name) {
    $ext = $img.Extension
    $finalName = "project$counter$ext"
    Rename-Item $img.FullName "images\$finalName"
    Write-Host "$($img.Name) renommé en $finalName"
    $counter++
}

Write-Host "`n=== IMAGES ACTUELLES ==="
Get-ChildItem "images" -File | Sort-Object Name | Select-Object Name, Length | Format-Table

# ========================
# 2️⃣ Vidéos
# ========================
$videos = Get-ChildItem "videos" -File | Where-Object { $_.Extension -match "\.mp4|\.mov" }

foreach ($vid in $videos) {
    $newName = $vid.Name -replace "\.mp4\.mov$", ".mp4"
    if ($vid.Name -ne $newName) {
        Rename-Item $vid.FullName "videos\$newName"
        Write-Host "$($vid.Name) renommé en $newName"
    }
}

Write-Host "`n=== VIDEOS ACTUELLES ==="
Get-ChildItem "videos" -File | Sort-Object Name | Select-Object Name, Length | Format-Table

# ========================
# 3️⃣ Déploiement Vercel
# ========================
Write-Host "`n=== DEPLOIEMENT SUR VERCEL ==="

try {
    vercel --prod --force
    Write-Host "✅ Déploiement terminé avec succès !"
} catch {
    Write-Host "⚠️ Échec du déploiement automatique. Vérifie que Vercel CLI est installé et accessible."
}