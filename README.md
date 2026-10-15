# Noury Blender Factory

Usine automatique de dessins animés **Yakine & Nour** : 3 épisodes de 4 minutes par jour,
rendus avec **Blender (Cycles)** en 1920×1080, puis publiés sur YouTube, sans aucun clic.
Yakine et Nour sont les héros ; selon l'histoire, des **personnages secondaires** (Mamie Zahra, Papi Ali, Lina,
Mimi la chatte, Rocky le chien, Pompon le lapin, Piou l'oiseau, le Grand Hibou) et **12 lieux de tournage**
entrent en scène. Les décors et les sons sont enrichis par des **bibliothèques libres** (Poly Haven, ambientCG,
Poly Pizza, Sketchfab, BlendKit, Objaverse, packs Kenney / Quaternius, Freesound),
dont les licences sont vérifiées automatiquement.

## Installation (une seule fois)
1. Supprimer les anciens fichiers du dépôt, puis copier tout le contenu de ce dossier à la racine du dépôt.
   Commit + push.
2. Le dépôt doit être **public** (minutes GitHub Actions gratuites et 12 machines en parallèle).
3. YouTube : suivre les étapes en tête de `tools/get_youtube_refresh_token.py` sur ton PC, puis créer les
   secrets `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN`
   (Settings → Secrets and variables → Actions). Mettre l'écran de consentement OAuth en **"In production"**.
4. Premier test : Actions → *Noury Blender Factory* → Run workflow → quality = `preview`.
   Sans secrets YouTube, la vidéo est seulement disponible en artefact (`noury-episode-N`).

Ensuite tout est automatique : 03:00, 11:00 et 18:00 UTC.

## Secrets optionnels (fortement recommandés)
| Secret | Où l'obtenir | Ce que ça change |
|---|---|---|
| `AZURE_SPEECH_KEY` + `AZURE_SPEECH_REGION` | portal.azure.com → *Azure AI Speech* | voix naturelles (sinon gTTS, robotique) |
| `POLYPIZZA_API_KEY` | compte gratuit sur poly.pizza | arbres, buissons, rochers… en 3D stylisée |
| `FREESOUND_API_KEY` | compte gratuit, puis freesound.org/apiv2/apply | vrais sons (animaux, vagues, pas, oiseaux) |
| `SKETCHFAB_API_TOKEN` | compte gratuit sketchfab.com → Settings → Password & API | maisons, puits, bateaux, fleurs, arbres stylisés |
| `BLENDKIT_API_KEY` | compte gratuit blendkit.com → profil → ADD-ON | modèles Blender natifs gratuits |
| `NOURY_ARTIFACT_KEY` | phrase secrète que tu inventes | permet les licences « sans redistribution » (BlendKit Royalty Free, Quaternius, Fab, CGTrader), fichiers gardés chiffrés |

Poly Haven, ambientCG et Objaverse fonctionnent **sans clé**.
Configuration complète : `docs/CONFIGURATION.md` · licences site par site : `docs/LICENCES_PAR_SITE.md`.

## Fonctionnement
```
prepare (1 machine)   histoire + distribution + lieux → bibliothèque libre → voix → musique → bruitages
                      → lip-sync → expressions → episode.blend (tout est empaqueté dedans)
render  (12 machines) chaque machine rend 480 images (20 s de film) → segment vidéo
finalize (1 machine)  assemblage → titre + FIN → mixage audio → contrôle qualité → miniature
                      → description avec crédits → YouTube
```
Si une étape essentielle échoue, rien n'est publié. Une bibliothèque en ligne indisponible ne bloque jamais l'épisode.

## Fichiers clés
| Fichier | Rôle |
|---|---|
| `agents/agent_director.py` | nouvel épisode à chaque lancement : structure d'histoire, invités, lieux, dialogues |
| `agents/cast_library.py` | personnages (apparence, voix, rôles possibles) |
| `agents/agent_sets.py` | lieux de tournage |
| `config/asset_sources.json` | bibliothèques activées, quotas, règles de licence, packs |
| `agents/agent_assets.py` | bibliothèque libre : Poly Haven, ambientCG, Poly Pizza, Sketchfab, BlendKit, Objaverse, packs, Freesound, dossier manuel |
| `agents/licences.py` + `agents/agent_licence_check.py` | règles de licence et audit avant chaque épisode |
| `agents/blender/build_scene.py` | construit décors, personnages, animaux, objet magique, lumières |
| `agents/blender/noury_anim.py` | animation image par image : poses, invités, regards, expressions, parole, caméra, ciel |
| `agents/blender/pro_rig.py` | pilote les personnages livrés par un artiste (squelette + expressions) |
| `docs/BIBLIOTHEQUES_GRATUITES.md` | sources, clés, licences, dossier manuel |
| `docs/AJOUTER_PERSONNAGES_ET_LIEUX.md` | ajouter un personnage, un lieu ou une histoire |
| `docs/CAHIER_DES_CHARGES_ARTISTE_3D.md` | à envoyer à un artiste 3D |

## Réglages (Settings → Variables → Actions)
| Variable | Défaut | Effet |
|---|---|---|
| `NOURY_SAMPLES` | 32 | qualité Cycles (plus = plus beau, plus lent) |
| `NOURY_ENGINE` | CYCLES | `EEVEE` seulement sur une machine avec carte graphique |
| `NOURY_MOTION_BLUR` | 1 | flou de mouvement ; mettre `0` si le rendu échoue |
| `NOURY_ALLOW_CCBY` | 0 | `1` = accepter aussi les ressources CC-BY (crédits automatiques) |
| `NOURY_MODELS` | 1 | `0` = ne pas utiliser les modèles 3D de la bibliothèque |
| `YT_PRIVACY` | public | `unlisted` ou `private` pour vérifier avant publication |

## Personnages professionnels
1. Envoyer `docs/CAHIER_DES_CHARGES_ARTISTE_3D.md` à un artiste 3D.
2. Vérifier sa livraison : `blender -b yakine.blend --python tools/check_character.py -- Yakine`
3. Déposer `yakine.blend` / `nour.blend` dans `assets/characters/` : l'usine les utilise automatiquement.

## Ordinateur avec carte graphique (option la plus rapide)
```
NOURY_ENGINE=EEVEE python agents/agent_supervisor.py all
NOURY_GPU=1 python agents/agent_supervisor.py all      # Cycles sur GPU
```
