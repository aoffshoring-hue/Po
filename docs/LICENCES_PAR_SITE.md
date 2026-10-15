# Licences et usage commercial, site par site

Vérifié en octobre 2026 sur les pages officielles des sites. Les licences peuvent changer : relis la page « licence »
d'un site avant de l'activer, et garde le rapport `LICENCE_REPORT.md` de chaque lancement.
*Ce document est une aide, pas un avis juridique.*

Le cas de ta chaîne : **vidéos YouTube monétisées, pour enfants, dépôt GitHub public**. Trois questions comptent :
1. **Usage commercial** autorisé ? (une chaîne monétisée est un usage commercial)
2. **Crédit** obligatoire ? (l'usine l'ajoute alors à la description YouTube)
3. **Redistribution** autorisée ? (un dépôt public, son cache et ses artefacts pourraient exposer les fichiers :
   si elle est interdite, l'usine garde les fichiers **chiffrés**)

## 1. Sites intégrés automatiquement

| Site | Licence | Commercial | Crédit | Redistribution des fichiers | Intégration |
|---|---|---|---|---|---|
| **Poly Haven** — polyhaven.com/license | CC0 (toutes les ressources) | ✅ | non | ✅ | auto, sans clé |
| **ambientCG** — ambientcg.com | CC0 (toutes les ressources) | ✅ | non | ✅ | auto, sans clé |
| **Poly Pizza** — poly.pizza | par modèle : CC0 ou CC-BY | ✅ | si CC-BY | ✅ (CC) | auto, clé gratuite |
| **Sketchfab** — sketchfab.com | par modèle : CC0, CC-BY, CC-BY-SA, CC-BY-NC, CC-BY-ND… | ✅ seulement CC0 / BY / BY-SA | si BY (auteur + Sketchfab) | ✅ (CC) | auto, clé gratuite |
| **Objaverse** — huggingface.co/datasets/allenai/objaverse | jeu de données ODC-By ; chaque objet garde sa licence (≈ 721 000 CC-BY, 3 500 CC0, le reste NC ou SA) | ✅ seulement CC0 / BY | si BY | ✅ (CC) | auto, **sans clé** |
| **BlendKit** — blendkit.com/docs/licenses | CC0 ou **Royalty Free** | ✅ (rendus et animations vendables) | non | ❌ pour Royalty Free | auto, clé gratuite ; Royalty Free **chiffré** |
| **Kenney** — kenney.nl | CC0 (indiqué sur chaque page de pack) | ✅ | non | ✅ | pack par lien direct |
| **Quaternius** — quaternius.com/license.html | **QAL** (licence propre, plus CC0) : usage commercial libre, vidéos comprises | ✅ | non | ❌ | pack par lien direct, **chiffré** |
| **Freesound** — freesound.org | par son : CC0, CC-BY, CC-BY-NC | ✅ seulement CC0 / BY | si BY | ✅ (CC) | auto, clé gratuite |

> **Note Quaternius / Poly Pizza** : d'anciens modèles Quaternius ont été publiés en CC0 et apparaissent ainsi sur
> Poly Pizza. Une renonciation CC0 ne peut pas être retirée pour les copies déjà publiées sous CC0 ; les nouveaux packs
> téléchargés sur quaternius.com relèvent en revanche de la licence QAL. L'usine applique la licence affichée par la
> source d'où vient chaque fichier.

## 2. Sites utilisables à la main (dossier `assets/manual/`)

| Site | Licence | Commercial | Crédit | Redistribution | Pourquoi pas automatique |
|---|---|---|---|---|---|
| **cgbookcase** — cgbookcase.com | CC0 | ✅ | non | ✅ | pas d'API |
| **Blend Swap** — blendswap.com | par modèle : CC0, CC-BY, CC-BY-SA, CC-BY-NC | ✅ seulement CC0 / BY | si BY | selon licence | vérifie chaque fichier |
| **Fab** (Epic, ex-Unreal Marketplace) — fab.com/eula | Standard (gratuit ou payant) ou CC-BY | ✅ les vidéos rendues peuvent être diffusées librement | non (Standard) | ❌ (Standard) | pas d'API publique → **chiffrer** |
| **CGTrader** (modèles gratuits) — help.cgtrader.com | Royalty Free | ✅ dans des images animées rendues | non | ❌ | pas d'API → **chiffrer** |

Pour les licences sans redistribution (Fab Standard, CGTrader Royalty Free, Quaternius QAL), utilise
`tools/encrypt_asset.sh` : seul le fichier chiffré est déposé dans le dépôt public, accompagné d'un `licence.txt`.

## 3. Sites écartés

| Site | Raison |
|---|---|
| **ShareTextures** | licence CC0 « personnalisée » qui **interdit les téléchargements automatisés** et la redistribution : utilisable uniquement à la main, et jamais dans un dépôt public |
| **Smithsonian 3D** | CC0 et API officielle, mais ce sont des scans de musée réalistes : hors style cartoon |
| **Thingiverse** | conçu pour l'impression 3D, beaucoup de licences NC |
| **Openverse** | moteur de recherche qui agrège des contenus CC ; il ne garantit pas l'exactitude des licences. Freesound couvre déjà les sons |
| **TurboSquid, textures.com, free3d** | licences non vérifiées dans cette version : non intégrés |

## 4. Règles appliquées par l'usine (`agents/licences.py`)

| Licence | Décision |
|---|---|
| CC0 / domaine public | ✅ toujours |
| CC-BY | ✅ si `attribution` est activé → auteur, source et lien ajoutés à la description YouTube |
| CC-BY-SA | ❌ par défaut (la vidéo pourrait devoir être publiée sous la même licence) ; activable |
| Royalty Free, QAL, Fab Standard | ✅ seulement avec le secret `NOURY_ARTIFACT_KEY` : fichiers chiffrés, jamais exposés |
| CC-BY-NC, CC-BY-ND, Sampling+, licence inconnue | ❌ **toujours** |

En plus des licences : filtre enfants sur les titres (armes, horreur, contenu adulte…), modèles animés,
trop lourds ou à accès restreint par âge exclus.

## 5. Contrôles automatiques
1. **Au téléchargement** : chaque ressource passe par la même règle ; les refus sont listés dans `CREDITS.md`.
2. **Avant chaque construction de scène** (`agent_licence_check.py`) : toute la bibliothèque en cache est revérifiée
   avec la configuration actuelle. Si tu durcis la règle, les éléments devenus interdits sont retirés aussitôt.
   Un fichier restreint non chiffré est supprimé.
3. **Dans la description YouTube** : seuls les éléments CC-BY réellement présents dans l'épisode sont crédités.
4. **Rapports** : `LICENCE_REPORT.md` et `CREDITS.md`, dans l'artefact `credits-N` de chaque lancement.
