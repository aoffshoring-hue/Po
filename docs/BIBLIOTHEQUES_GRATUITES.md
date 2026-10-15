# Bibliothèques gratuites utilisées par l'usine

> Licences vérifiées site par site : **`LICENCES_PAR_SITE.md`**. Réglages et clés : **`CONFIGURATION.md`**.

À chaque épisode, `agents/agent_assets.py` complète automatiquement une bibliothèque de ressources libres
(`assets/library/`, gardée en cache entre les lancements GitHub). Si un site ne répond pas, l'usine continue
avec ses ressources construites par le code : **une bibliothèque en panne ne bloque jamais un épisode**.

## 1. Sources intégrées

| Site | Ce qu'il apporte | Licence | Clé | Statut |
|---|---|---|---|---|
| **Poly Haven** (polyhaven.com) | 4 ciels HDRI (jour, coucher de soleil, orage, nuit) pour l'éclairage + textures herbe, sable, roche | CC0 | aucune | ✅ automatique |
| **ambientCG** (ambientcg.com) | textures neige, enduit des murs, bois, terre, tuiles, pavés | CC0 | aucune | ✅ automatique |
| **Poly Pizza** (poly.pizza) | modèles 3D *low poly* stylisés (Quaternius, Kenney…) : arbres, sapins, palmiers, buissons, champignons, rochers | CC0 (CC-BY en option) | `POLYPIZZA_API_KEY` | ✅ avec clé gratuite |
| **Sketchfab** (sketchfab.com) | la plus grande bibliothèque de modèles 3D téléchargeables ; l'usine cherche des versions « low poly » et « stylized » : arbres, maisons, puits, étals, bateaux, bonhommes de neige… | CC0 (CC-BY en option) | `SKETCHFAB_API_TOKEN` | ✅ avec clé gratuite |
| **BlendKit** (blendkit.com, ex-BlenderKit) | modèles au format Blender natif (.blend), **gratuits uniquement** | CC0 et Royalty Free | `BLENDKIT_API_KEY` (+ `NOURY_ARTIFACT_KEY`) | ✅ avec clé gratuite |
| **Objaverse** (huggingface.co, allenai/objaverse) | 800 000 objets 3D venus de Sketchfab, chacun avec sa licence ; recherche par catégorie (arbre, bateau, banc, bonhomme de neige…) | CC0 (CC-BY en option) | aucune | ✅ automatique |
| **Packs par lien direct** (Kenney, Quaternius…) | packs complets triés par famille grâce à des motifs de noms de fichiers | selon le pack | aucune | ✅ à configurer (`config/asset_sources.json`) |
| **Freesound** (freesound.org) | vrais sons : oiseaux, vagues, vent, grillons, miaou, aboiements, hibou, pas (herbe, sable, neige), carillons, chute | CC0 (CC-BY en option) | `FREESOUND_API_KEY` | ✅ avec clé gratuite |

Poly Haven fournit aussi des modèles 3D, mais ils sont photoréalistes : ils jureraient avec le style cartoon.
L'usine ne prend donc chez Poly Haven que les ciels et les textures, et les textures sont **mélangées aux couleurs
cartoon** (le relief et le grain de la photo, avec la palette du dessin animé).

## 2. Les autres sites de la liste Similarweb

| Site | Pourquoi il n'est pas automatisé | Que faire |
|---|---|---|
| **Poliigon** | téléchargements liés à un compte, pas d'API publique pour un téléchargement automatique | possible à la main si la licence de l'élément le permet → dossier manuel |
| **textures.com** | système de crédits / abonnement, licence restrictive | déconseillé |
| **freepbr.com**, **3dtextures.me** | gratuits mais sans API | à la main → dossier manuel (vérifie la licence sur le site) |
| **free3d.com** | licence différente pour chaque modèle, souvent « usage personnel » | déconseillé pour une chaîne YouTube monétisée |
| **Kenney.nl** (CC0), **Quaternius.com** (licence QAL) | pas d'API, mais lien de téléchargement direct | section `packs` de `config/asset_sources.json` (voir `CONFIGURATION.md`) |
| **CGTrader**, **TurboSquid** (modèles gratuits) | pas d'API de téléchargement, licences propres à chaque site | à la main en vérifiant la licence → dossier manuel |

## 3. Le dossier manuel `assets/manual/`

Tout ce que tu y déposes est **prioritaire** sur les téléchargements automatiques :

```
assets/manual/
├── textures/<usage>/    fichiers contenant color|diff|albedo, rough, normal|nor (jpg/png)
│                        usages : grass, sand, rock, snow, plaster, wood, soil, tiles, pebbles
├── hdri/<ambiance>/     un fichier .hdr ou .exr ; ambiances : day, sunset, storm, night
├── models/<famille>/    fichiers .glb ou .blend ; familles : tree, pine, palm, bush, mushroom, rock, house,
│                        village_prop, flower, boat, snowman
└── sounds/<son>/        fichiers .wav, .mp3, .ogg ; sons : amb_birds, amb_waves, amb_wind, amb_crickets,
                         meow, woof, chirp, hoot, step_grass, step_snow, step_sand, chime, thud, whoosh
```
Exemple : un pack de buissons Kenney → `assets/manual/models/bush/buisson_1.glb`, puis commit + push.
**Tu es responsable de la licence des fichiers déposés à la main.**

## 4. Obtenir les clés gratuites
1. **Poly Pizza** : crée un compte sur poly.pizza, ouvre les paramètres du compte, rubrique API, crée une application
   et copie la clé. Ajoute-la dans GitHub : *Settings → Secrets and variables → Actions → New repository secret*,
   nom `POLYPIZZA_API_KEY`.
2. **Freesound** : crée un compte sur freesound.org, puis demande une clé sur `freesound.org/apiv2/apply`
   (elle apparaît aussitôt). Secret GitHub : `FREESOUND_API_KEY`.
3. **Sketchfab** : compte gratuit sur sketchfab.com → *Settings → Password & API* → copie l'*API token*.
   Secret GitHub : `SKETCHFAB_API_TOKEN`.
4. **BlendKit** : compte gratuit sur blendkit.com → ton profil → onglet *ADD-ON* → *Show API key*.
   Secret GitHub : `BLENDKIT_API_KEY`. Seuls les éléments **gratuits** sont téléchargés (pas d'abonnement nécessaire).
5. **`NOURY_ARTIFACT_KEY`** (recommandé avec BlendKit) : une phrase secrète que tu inventes (au moins 20 caractères).
   Elle sert à chiffrer les fichiers « Royalty Free » (voir ci-dessous).

## 5. Licences
- Par défaut, **seules les ressources CC0** (domaine public) sont acceptées : aucune obligation de citer.
- Variable GitHub `NOURY_ALLOW_CCBY = 1` : accepte aussi les ressources **CC-BY**, plus nombreuses.
  Leurs auteurs sont alors **cités automatiquement** dans la description YouTube, comme l'exige cette licence.
- Les licences « NC » (pas d'usage commercial) et « ND » sont toujours refusées.
- **BlendKit « Royalty Free »** : autorisé dans des vidéos monétisées, sans citer l'auteur, mais **interdit de
  redistribuer le fichier lui-même**. Comme ton dépôt est public, l'usine ne les utilise que si `NOURY_ARTIFACT_KEY`
  existe : ils sont alors gardés **chiffrés** dans le cache, déchiffrés seulement pendant la construction de la scène,
  et l'épisode transmis aux 12 machines est chiffré lui aussi. Sans cette clé, seuls les modèles BlendKit CC0 sont pris.
- **Sketchfab CC-BY** : il faut citer l'auteur et Sketchfab ; c'est fait automatiquement, et uniquement pour les
  modèles réellement présents dans l'épisode (fichier `export/used_assets.json`).
- Tous les titres sont filtrés pour un public d'enfants (armes, horreur, contenu adulte… refusés).
- La liste complète de ce qui a été utilisé est dans `assets/library/CREDITS.md`, téléchargeable après chaque
  lancement dans l'artefact `credits-N`.

## 6. Réglages
| Variable GitHub | Défaut | Effet |
|---|---|---|
| `NOURY_ALLOW_CCBY` | 0 | `1` = accepter aussi les ressources CC-BY (crédits automatiques) |
| `NOURY_MODELS` | 1 | `0` = ne pas utiliser les modèles 3D de la bibliothèque (style 100 % code) |
| `NOURY_MAX_DOWNLOADS` | 70 | nombre maximal de nouveaux fichiers téléchargés par lancement |
