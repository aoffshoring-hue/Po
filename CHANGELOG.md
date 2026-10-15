# Changelog

## v8 - plus de bibliothèques, licences vérifiées, configuration
- **Objaverse** (sans clé) : 800 000 objets Creative Commons, choisis par catégorie, licence lue objet par objet.
- **Packs par lien direct** : Kenney (CC0), Quaternius (licence QAL, chiffré), triés par familles de fichiers.
- **Formats** : import FBX et OBJ en plus de glTF et .blend.
- **`config/asset_sources.json`** : activer / couper chaque bibliothèque, quotas, règles de licence, packs.
- **`agents/licences.py`** : une seule règle de licence pour toutes les sources (CC0 toujours, CC-BY / CC-BY-SA en option,
  licences sans redistribution seulement chiffrées, NC / ND / inconnues toujours refusées).
- **`agent_licence_check.py`** : audit de toute la bibliothèque avant chaque épisode, avec retrait des éléments
  devenus interdits et rapport `LICENCE_REPORT.md`.
- **Dossier manuel** : `licence.txt` par dossier, fichiers chiffrés `.enc` (`tools/encrypt_asset.sh`) pour Fab, CGTrader…
- **Correction** : les sons Freesound CC-BY (licence donnée sous forme d'adresse web) étaient refusés à tort.
- **Docs** : `LICENCES_PAR_SITE.md` (vérification site par site) et `CONFIGURATION.md` (pas à pas).

## v7 - BlendKit et Sketchfab
- **BlendKit** (clé gratuite) : modèles Blender natifs, éléments gratuits seulement, licences CC0 et Royalty Free.
  Les fichiers Royalty Free sont chiffrés (cache, épisode partagé) car ils ne doivent jamais être redistribués.
- **Sketchfab** (clé gratuite) : recherche de modèles « low poly » / « stylized » téléchargeables, en glTF.
- **Nouveaux éléments de décor** : maisons au fond du village, puits / étals / bancs autour de la place,
  massifs de fleurs au jardin, bateaux sur l'eau, bonhommes de neige sur la colline.
- **Quotas par source** : chaque bibliothèque apporte sa part de modèles, pour plus de variété.
- **Filtre enfants** sur les titres (armes, horreur, contenu adulte refusés), modèles animés et trop lourds exclus.
- **Crédits exacts** : seuls les éléments CC-BY réellement présents dans l'épisode sont cités (`used_assets.json`,
  `sfx_used.json`), sans limite de nombre.

## v6 - bibliothèques libres
- **`agent_assets.py`** : bibliothèque de ressources libres, mise en cache entre les lancements.
  - **Poly Haven** (sans clé) : 4 ciels HDRI selon l'ambiance (jour, coucher de soleil pour la magie, orage, nuit)
    et textures herbe, sable, roche.
  - **ambientCG** (sans clé) : neige, enduit des murs, bois, terre, tuiles, pavés.
  - **Poly Pizza** (clé gratuite) : modèles 3D stylisés (arbres, sapins, palmiers, buissons, champignons, rochers),
    mélangés aux décors construits par le code.
  - **Freesound** (clé gratuite) : vrais sons (ambiances, animaux, pas selon le sol, carillons, chute, rafales).
  - **Dossier manuel** `assets/manual/` pour les sites sans API (Kenney, Quaternius, 3dtextures.me…), prioritaire.
- **Licences** : CC0 seulement par défaut ; CC-BY en option avec **crédits automatiques** dans la description YouTube.
- **Décors** : le ciel d'éclairage change avec le lieu ; sol de neige texturé ; murs, tuiles, bois, terre et pavés
  texturés en gardant les couleurs cartoon ; place pavée au village.
- **Rendu** : toutes les images sont empaquetées dans `episode.blend` (les 12 machines de rendu n'ont besoin de rien d'autre).
- **Correction** : la boucle des ambiances sonores réelles ne ralentit plus en fin de scène.

## v5 - personnages secondaires et nouveaux lieux
- 3 humains et 5 animaux, 3 structures d'histoires, 12 lieux, mise en scène des invités, une voix par personnage.

## v4 - image plus cinématographique
- Lumière HDRI, textures photo, principes d'animation, flou de mouvement, halo et vignettage.

## v3 - prêt pour les personnages professionnels
- Chargement automatique des personnages de l'artiste ; `pro_rig.py` pilote squelette et expressions.

## v2 - son et parole
- Voix Azure, musique par émotion, bruitages synchronisés, synchronisation labiale Rhubarb.

## v1 - version Blender
- Passage de Godot à Blender Cycles, rendu réparti sur 12 machines GitHub, publication YouTube.
