#!/usr/bin/env bash
# Encrypts a model you downloaded by hand under a "no redistribution" licence
# (Quaternius QAL, Fab Standard, CGTrader / TurboSquid Royalty Free, BlendKit Royalty Free...)
# so that it can be committed to the PUBLIC repository without being redistributed.
#
#   NOURY_ARTIFACT_KEY="ta phrase secrète" bash tools/encrypt_asset.sh maison.glb assets/manual/models/house/
#
# Then create assets/manual/models/house/licence.txt with the licence on line 1 (e.g. "QAL" or "Royalty Free").
# Only self-contained files are accepted: .glb or .blend (textures packed inside).
set -euo pipefail
SRC="${1:?fichier .glb ou .blend}"
DEST="${2:?dossier de destination, ex. assets/manual/models/house/}"
[ -n "${NOURY_ARTIFACT_KEY:-}" ] || { echo "Définis NOURY_ARTIFACT_KEY (la même phrase que le secret GitHub)"; exit 1; }
case "${SRC,,}" in *.glb|*.blend) ;; *) echo "Seuls .glb et .blend sont acceptés"; exit 1 ;; esac
mkdir -p "$DEST"
OUT="$DEST/$(basename "$SRC").enc"
openssl enc -aes-256-cbc -pbkdf2 -salt -in "$SRC" -out "$OUT" -pass env:NOURY_ARTIFACT_KEY
echo "Chiffré : $OUT"
echo "N'oublie pas $DEST/licence.txt (ligne 1 = licence, ligne 2 = auteur). Ne commite JAMAIS le fichier d'origine."
