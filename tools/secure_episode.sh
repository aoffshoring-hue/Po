#!/usr/bin/env bash
# Encrypts / decrypts export/episode.blend with NOURY_ARTIFACT_KEY (GitHub secret), so that the
# episode shared between machines (public artifact) never exposes royalty-free asset files.
#   bash tools/secure_episode.sh lock     -> episode.blend      => episode.blend.enc
#   bash tools/secure_episode.sh unlock   -> episode.blend.enc  => episode.blend
# Without NOURY_ARTIFACT_KEY nothing is done (only CC0 / CC-BY assets are used in that case).
set -euo pipefail
F=export/episode.blend
if [ -z "${NOURY_ARTIFACT_KEY:-}" ]; then echo "secure_episode: pas de clé, rien à faire"; exit 0; fi
case "${1:-}" in
  lock)
    [ -f "$F" ] || exit 0
    openssl enc -aes-256-cbc -pbkdf2 -salt -in "$F" -out "$F.enc" -pass env:NOURY_ARTIFACT_KEY
    rm -f "$F"; echo "secure_episode: episode.blend chiffré" ;;
  unlock)
    [ -f "$F.enc" ] || exit 0
    openssl enc -d -aes-256-cbc -pbkdf2 -in "$F.enc" -out "$F" -pass env:NOURY_ARTIFACT_KEY
    rm -f "$F.enc"; echo "secure_episode: episode.blend déchiffré" ;;
  *) echo "usage: secure_episode.sh lock|unlock"; exit 2 ;;
esac
