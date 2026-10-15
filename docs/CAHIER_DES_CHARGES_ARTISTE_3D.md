# Cahier des charges : personnages 3D « Yakine & Nour »

**Projet :** série d'animation 3D pour enfants de 3 à 7 ans, publiée sur YouTube.
**Production :** entièrement automatique (Blender piloté par scripts Python). Le modèle livré sera réutilisé
dans **tous les épisodes**. Il doit donc respecter **exactement** les noms et conventions ci-dessous.

*An English summary is available at the end of this document.*

---

## 1. Les personnages principaux

| | **Yakine** (fille, ~6 ans) | **Nour** (garçon, ~6 ans) |
|---|---|---|
| Caractère | curieuse, attentionnée, un peu pressée | joyeux, prudent, un peu peureux |
| Silhouette | légèrement plus petite (≈ 97 % de Nour) | silhouette ronde et douce |
| Peau | claire et chaude (RGB ≈ 0.97 / 0.76 / 0.62) | mate (RGB ≈ 0.80 / 0.56 / 0.40) |
| Cheveux | brun foncé, **deux chignons** sur les côtés, frange | brun très foncé, **cheveux bouclés** en volume |
| Yeux | iris marron | iris marron foncé |
| Tenue | robe **rose** (0.93 / 0.33 / 0.60), accents **jaunes**, collants violets, chaussures blanches | t-shirt **bleu** (0.16 / 0.48 / 0.92) à bande jaune, pantalon bleu marine, baskets jaunes |

Les couleurs sont des repères : l'artiste peut les ajuster pour un meilleur rendu, en gardant la dominante rose / bleu.

### Personnages secondaires (optionnel, même convention)
Les personnages humains secondaires peuvent être commandés plus tard avec **exactement la même convention**
(noms d'os, shape keys, orientation). Leur nom de fichier et de collection est leur clé :
`Zahra` (Mamie Zahra, grand-mère, foulard rose, lunettes, robe verte), `Ali` (Papi Ali, grand-père, barbe grise,
djellaba beige, calotte blanche, babouches jaunes), `Lina` (amie, ~6 ans, queue-de-cheval, robe jaune).
Les animaux (chat, chien, lapin, oiseau, hibou) restent construits par le code.

## 2. Style visuel
- Cartoon 3D pour enfants : formes **rondes et douces**, aucun angle agressif.
- Tête volumineuse (≈ 1/3 de la hauteur pour les enfants), **grands yeux expressifs**, petit nez, joues rondes.
- Mains simplifiées à 4 doigts acceptées.
- Lisible de loin : silhouettes très différentes entre les personnages.
- Pas de copie d'un personnage existant (Pixar, Disney, etc.) : le design doit être **original**.

## 3. Livrables
1. `yakine.blend` et `nour.blend` (un personnage par fichier), compatibles **Blender 4.2 LTS**.
2. Toutes les textures **empaquetées** dans le fichier (*File → External Data → Pack Resources*).
3. Une planche de présentation (*turnaround* : face, profil, dos, 3/4) en PNG.
4. Une planche des expressions et des formes de bouche en PNG.
5. Une cession écrite des droits d'utilisation **commerciale** (YouTube, produits dérivés).

## 4. Conventions techniques (obligatoires)

### 4.1 Échelle, orientation, origine
- Échelle de scène stylisée, en **unités Blender** (ce ne sont pas des tailles réelles d'enfant) :
  - **Nour** : sommet de la tête (cheveux compris) à **1,75**, centre de la tête à **1,35**, base du cou à **1,02** ;
  - **Yakine** : les mêmes valeurs × 0,97 (chignons non compris).
- Les cadrages automatiques des caméras reposent sur ces hauteurs : elles doivent être respectées à ±5 %.
- Le personnage **regarde vers −Y** (vue de face Blender = numpad 1).
- Origine de l'armature : **au sol, entre les pieds** (0, 0, 0).
- Pose de repos : **A-pose** (bras à ~45°). Transformations appliquées (rotation 0, échelle 1).

### 4.2 Organisation du fichier
```
Collection  "Yakine"                 (ou "Nour", "Zahra", ...)
├── Armature  "Yakine_rig"
├── Mesh      "Yakine_body"          corps + vêtements (peut être découpé en plusieurs meshes)
├── Mesh      "Yakine_face"          porte les shape keys du visage
├── Mesh      "Yakine_eye_L" / "Yakine_eye_R"
└── Mesh      "Yakine_hair"
```
Tous les meshes sont parentés à l'armature (*Armature Deform*).

### 4.3 Os de l'armature (noms exacts)
Squelette humanoïde compatible avec le reciblage d'animations capturées (Mixamo ou équivalent) :
```
root
└── hips
    ├── spine ── chest ── neck ── head
    │                │             ├── eye_L, eye_R        (rotation = direction du regard)
    │                │             ├── jaw                 (ouverture de la mâchoire)
    │                │             └── hair_01 … hair_06   (mèches / chignons, mouvement secondaire)
    │                ├── shoulder_L ── upperarm_L ── forearm_L ── hand_L ── doigts
    │                └── shoulder_R ── upperarm_R ── forearm_R ── hand_R ── doigts
    ├── thigh_L ── shin_L ── foot_L ── toe_L
    └── thigh_R ── shin_R ── foot_R ── toe_R
```
- Doigts : `thumb_01_L`, `thumb_02_L`, `index_01_L`, `index_02_L`, `middle_01_L`, …, `pinky_02_L` (idem `_R`).
- **Pas de contraintes ni de drivers cachés** : les scripts animent directement la rotation des os.
- Un contrôle IK des pieds et des mains est apprécié, mais **optionnel**.

### 4.4 Shape keys du visage (sur `<Nom>_face`, noms exacts, valeurs 0 → 1)
**Expressions**

| Nom | Description |
|---|---|
| `smile` | grand sourire, joues relevées |
| `frown` | coins de la bouche vers le bas, tristesse |
| `brow_up` | deux sourcils levés (surprise, émerveillement) |
| `brow_down` | sourcils froncés (détermination, colère légère) |
| `brow_worried` | intérieur des sourcils levé (peur, inquiétude) |
| `eyes_wide` | yeux grand ouverts |
| `squint` | yeux plissés (rire, joie) |
| `blink_L`, `blink_R` | fermeture complète de chaque œil |
| `cheeks_puff` | joues gonflées |
| `pout` | moue boudeuse |

**Formes de bouche pour la parole** (standard Rhubarb / Hanna-Barbera)

| Nom | Son | Description |
|---|---|---|
| `vis_A` | M, B, P | lèvres fermées avec légère pression |
| `vis_B` | K, S, T, « i » | bouche entrouverte, dents serrées |
| `vis_C` | « è », « a » court | bouche ouverte |
| `vis_D` | « a » long | bouche grande ouverte |
| `vis_E` | « o » | bouche légèrement arrondie |
| `vis_F` | « ou », W | lèvres en cul-de-poule |
| `vis_G` | F, V | dents du haut sur la lèvre du bas |
| `vis_H` | L | bouche ouverte, langue relevée |

La position de repos (bouche fermée détendue) est la forme de base (*Basis*).
Les expressions et les formes de bouche doivent **pouvoir se combiner** (exemple : `smile` 0,6 + `vis_C` 1,0) sans déformation.

### 4.5 Matériaux
- **Principled BSDF** uniquement, sans nodes de moteurs externes.
- Rendu correct en **Cycles et EEVEE**.
- Peau avec léger *subsurface*. Yeux avec cornée brillante et reflets.
- Cheveux : géométrie (*cards* ou volumes sculptés), **pas de particules de poils**, pour garder un rendu rapide.

### 4.6 Budget
- Environ **30 000 à 60 000 triangles** par personnage, sans subdivision. Un modificateur *Subdivision* (niveau 1 au rendu) est accepté.
- Textures : 2K maximum.

## 5. Recette (critères d'acceptation)
La livraison est validée quand :
1. Le script `tools/check_character.py` ne signale **aucune erreur** :
   `blender -b yakine.blend --python tools/check_character.py -- Yakine`
2. Les 19 shape keys et tous les os listés existent avec les noms exacts.
3. Une animation de marche Mixamo se recible sans déformation majeure.
4. Les combinaisons d'expressions testées (joie qui parle, peur qui parle, clignement pendant un sourire) ne présentent pas de défaut visible.

## 6. Étapes proposées
1. Croquis et proposition de design → validation.
2. Modèle sculpté + couleurs → validation (rendu de face, profil, 3/4).
3. Rig + shape keys → validation par le script de contrôle.
4. Livraison finale + cession de droits.

---

## English summary
Two original stylised 3D kids characters (≈ 6 years old) for an automated Blender pipeline, Blender 4.2 LTS.
Optional later: secondary humans (`Zahra`, `Ali`, `Lina`) with the same convention.
- **Scale & orientation:** stylised Blender units: Nour top of head (with hair) 1.75, head centre 1.35, neck base 1.02;
  Yakine = same × 0.97, facing −Y, rig origin at the feet, A-pose, transforms applied.
- **Naming (mandatory):** collection `Yakine`, armature `Yakine_rig`, meshes `Yakine_body`, `Yakine_face`,
  `Yakine_eye_L/R`, `Yakine_hair` (same pattern for every character).
- **Bones:** see 4.3 (humanoid, retargetable from Mixamo; eye_L/eye_R and jaw bones; hair_01…06; no hidden drivers).
- **Shape keys on `<Name>_face`:** `smile, frown, brow_up, brow_down, brow_worried, eyes_wide, squint, blink_L, blink_R,
  cheeks_puff, pout`, plus Rhubarb visemes `vis_A … vis_H`. They must combine cleanly.
- **Materials:** Principled BSDF only, packed textures (2K max), geometry hair (no particle hair), 30–60k tris.
- **Acceptance:** `tools/check_character.py` passes with no errors, and a Mixamo walk retargets cleanly.
- **Rights:** full commercial usage rights (YouTube and merchandise), original design.
