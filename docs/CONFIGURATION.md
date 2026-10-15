# Configuration pas à pas

Tout se règle à deux endroits : les **secrets et variables GitHub** (clés, choses privées) et le fichier
**`config/asset_sources.json`** (bibliothèques et licences, versionné dans le dépôt).

## 1. Secrets GitHub (*Settings → Secrets and variables → Actions → Secrets*)

| Secret | Obligatoire ? | Où l'obtenir |
|---|---|---|
| `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN` | pour publier | `tools/get_youtube_refresh_token.py` |
| `AZURE_SPEECH_KEY`, `AZURE_SPEECH_REGION` | recommandé (voix) | portal.azure.com → Azure AI Speech |
| `NOURY_ARTIFACT_KEY` | recommandé | une phrase secrète que tu inventes (20 caractères ou plus). Active les licences « sans redistribution » (BlendKit Royalty Free, Quaternius, Fab, CGTrader) en les gardant chiffrées |
| `POLYPIZZA_API_KEY` | optionnel | poly.pizza → compte → API → créer une application |
| `SKETCHFAB_API_TOKEN` | optionnel | sketchfab.com → Settings → Password & API |
| `BLENDKIT_API_KEY` | optionnel | blendkit.com → profil → onglet ADD-ON → Show API key |
| `FREESOUND_API_KEY` | optionnel | freesound.org/apiv2/apply |

Sans aucune clé, l'usine utilise déjà **Poly Haven, ambientCG et Objaverse** (modèles CC0).

## 2. Variables GitHub (*Settings → Secrets and variables → Actions → Variables*)

| Variable | Défaut | Effet |
|---|---|---|
| `NOURY_ALLOW_CCBY` | 0 | `1` = accepter CC-BY (≈ 200 fois plus de modèles Objaverse ; auteurs crédités automatiquement) |
| `NOURY_MODELS` | 1 | `0` = aucun modèle de bibliothèque (décors 100 % code) |
| `NOURY_MAX_DOWNLOADS` | 70 | nouveaux fichiers téléchargés au maximum par lancement |
| `NOURY_SAMPLES`, `NOURY_ENGINE`, `NOURY_MOTION_BLUR`, `YT_PRIVACY` | | voir README |

## 3. Le fichier `config/asset_sources.json`

- **`licences`** : `attribution` (CC-BY), `share_alike` (CC-BY-SA), `restricted` (licences sans redistribution).
  NC et ND restent toujours refusées.
- **`sources`** : `enabled: false` coupe une bibliothèque ; `max_per_family` fixe combien de modèles elle apporte
  par famille (arbre, maison, bateau…).
- **`packs`** : packs complets téléchargés par lien direct.

### Ajouter un pack Kenney (CC0)
1. Ouvre la page du pack, par exemple kenney.nl/assets/nature-kit, et vérifie la ligne *License : Creative Commons CC0*.
2. Clic droit sur le bouton *Download* → copier l'adresse du lien.
3. Dans `config/asset_sources.json`, colle-la dans `"url"` du pack *Kenney - Nature Kit* et mets `"enabled": true`.
4. Adapte `"families"` : des motifs de noms de fichiers (`*tree_oak*`) rangés par famille.
   Familles possibles : `tree, pine, palm, bush, mushroom, rock, house, village_prop, flower, boat, snowman`.

### Ajouter un pack Quaternius (licence QAL)
Même chose avec `"licence": "QAL"`. Le pack n'est utilisé que si `NOURY_ARTIFACT_KEY` existe ; seuls ses fichiers
`.glb` et `.blend` sont gardés, chiffrés.

### Déposer un modèle à la main
- CC0 ou CC-BY : copie le fichier dans `assets/manual/models/<famille>/` avec un `licence.txt`
  (ligne 1 : licence, ligne 2 : auteur).
- Licence sans redistribution (Fab, CGTrader, Quaternius) :
  `NOURY_ARTIFACT_KEY="ta phrase" bash tools/encrypt_asset.sh modele.glb assets/manual/models/<famille>/`,
  puis le `licence.txt`. **Ne commite jamais le fichier d'origine.**

## 4. Vérifier après un lancement
Télécharge l'artefact `credits-N` : `LICENCE_REPORT.md` (ce qui est autorisé, ce qui a été retiré et pourquoi)
et `CREDITS.md` (tout ce qui est dans la bibliothèque, plus les refus du lancement).
