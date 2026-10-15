# Ajouter des personnages, des lieux et des histoires

Yakine et Nour sont toujours présents. Chaque épisode fait appel, selon son histoire, à des **personnages
secondaires** et à plusieurs **lieux de tournage**. Tout est choisi automatiquement ; ce guide explique
comment enrichir la série.

## 1. La distribution actuelle (`agents/cast_library.py`)

| Clé | Nom à l'écran | Type | Rôles possibles |
|---|---|---|---|
| `Zahra` | Mamie Zahra | humaine (grand-mère) | ancienne du village, propriétaire, guide |
| `Ali` | Papi Ali | humain (grand-père) | ancien du village, propriétaire, guide |
| `Lina` | Lina | humaine (amie, 6 ans) | amie, propriétaire |
| `Mimi` | Mimi | chatte | animal perdu, compagnon |
| `Rocky` | Rocky | chien | animal perdu, compagnon |
| `Pompon` | Pompon | lapin | animal perdu, compagnon |
| `Piou` | Piou | oiseau | compagnon |
| `Hibou` | Grand Hibou | hibou | guide |

### Ajouter un personnage
Ajoute une entrée dans `CAST` :
```python
"Karim": {
    "key": "Karim", "name": "Monsieur Karim", "kind": "human", "f": False,
    "roles": ["owner", "mentor"],                 # rôles qu'il peut tenir dans les histoires
    "design": {"outfit_color": [0.95, 0.95, 0.93], "hair_color": [0.1, 0.07, 0.05],
               "skin_color": [0.8, 0.58, 0.42], "hair_style": "short", "beard": True,
               "adult": True, "height": 1.3},
    "voice": {"azure": "fr-FR-HenriNeural", "pitch": -4, "rate": -6, "gtts_shift": 0.92},
},
```
- **Humains** : `hair_style` = `short`, `curly`, `side_buns`, `ponytail`, `headscarf` (+ `scarf_color`),
  `cap` (+ `cap_color`). Options : `beard`, `glasses`, `skirt`, `adult`.
- **Animaux** : `"kind": "animal"`, `"species"` = `cat`, `dog`, `rabbit`, `bird` ou `owl`, avec
  `design = {"fur", "belly", "iris", "nose", "size"}`, plus `cry` (« Miaou ! ») et `sound`.
- **Version professionnelle** : dépose `assets/characters/karim.blend` (même convention que Yakine et Nour,
  voir le cahier des charges). Il remplacera automatiquement la version construite par le code.

## 2. Les lieux de tournage (`agents/agent_sets.py`)

| Clé | Lieu | Particularités |
|---|---|---|
| `meadow` | la prairie | collines, herbe, fleurs, arbres |
| `storm_meadow` | la prairie sous l'orage | ciel sombre, vent fort |
| `forest` | la forêt | arbres |
| `coast` | la plage | sable, mer, palmiers |
| `rocky_coast` | la côte rocheuse | rochers, vent, mer agitée |
| `magical_clearing` | la clairière magique | lumière violette, lucioles |
| `village` | le village | maisons blanches et ocre, toits de tuiles vertes, fontaine en zellige, guirlande |
| `village_night` | le village la nuit | lune, étoiles, lucioles, guirlande allumée |
| `garden` | le jardin | potager, clôture, tournesols |
| `night_forest` | la forêt de nuit | lune, étoiles, lucioles |
| `snowy_hill` | la colline enneigée | sol de neige, sapins enneigés, flocons qui tombent |
| `desert_oasis` | l'oasis | dunes, eau, palmiers, rochers |

Les décors sont enrichis automatiquement par la bibliothèque (voir `BIBLIOTHEQUES_GRATUITES.md`) :
ciel HDRI adapté (jour, coucher de soleil pour la magie, orage, nuit), textures et modèles 3D.

### Ajouter un lieu
Ajoute une entrée dans `LOCATIONS` en combinant les éléments existants :
```python
"beach_sunset": {"label": "la plage au coucher du soleil", "sky": [0.95, 0.55, 0.40],
                 "ground": [0.9, 0.72, 0.5], "wind": 0.3, "terrain": "coast", "water": True,
                 "props": ["palms"], "glow": True},
```
`terrain` : `meadow` ou `coast` · `props` : `trees`, `pines`, `palms`, `houses`, `garden`, `rocks`, `fireflies`
· options : `water`, `night`, `snow`, `glow` (lumière de coucher de soleil), `storm`.
Une **nouvelle famille d'objets** (par exemple une école) se construit dans `agents/blender/build_scene.py`,
dans sa propre collection `<nom>_set`, puis s'ajoute à la liste des props dans `noury_anim.py → apply_env`.

## 3. Les histoires (`agents/agent_director.py`)

Trois structures existent : `quest` (la quête magique), `lost` (l'animal perdu), `festival` (la fête du village).
Chaque scène indique :
- l'**action** des héros (`look_around`, `approach_seed`, `meet_guest`, `talk_together`, `brace_wind`,
  `help_friend`, `run_together`, `protect_seed`, `plant_seed`, `celebrate`) ;
- les **invités** présents : `G(rôle, place, attitude, émotion)`
  - places : `right`, `left`, `near`, `back`, `far`, `follow` (suit les héros quand ils marchent ou courent)
  - attitudes : `idle`, `sad`, `enter` (arrive en marchant), `follow`, `hide`, `talk`, `wave`, `cheer`
- jusqu'à **3 répliques**, dites par `Y` (Yakine), `N` (Nour) ou un rôle (`C`, `M`, `L`, `O`, `E`, `F`).

Pour tester une histoire précise : *Actions → Run workflow → template* = `quest`, `lost` ou `festival`.
Toute nouvelle histoire est vérifiée automatiquement : un personnage qui parle doit être présent dans la scène,
chaque lieu, action, place et attitude doit exister, sinon l'épisode s'arrête avant le rendu.
