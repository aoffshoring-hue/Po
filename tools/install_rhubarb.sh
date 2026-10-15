#!/usr/bin/env bash
# Installs Rhubarb Lip Sync (latest Linux release). Never fails the build:
# without Rhubarb the lip-sync falls back to the voice volume.
set -uo pipefail
DEST="$HOME/rhubarb"
if [ ! -x "$DEST/rhubarb" ]; then
  URL=$(curl -fsSL https://api.github.com/repos/DanielSWolf/rhubarb-lip-sync/releases/latest \
        | grep -o '"browser_download_url": *"[^"]*Linux[^"]*\.zip"' | head -n1 | cut -d'"' -f4)
  if [ -z "$URL" ]; then echo "Rhubarb: release not found, fallback to volume lip-sync"; exit 0; fi
  curl -fsSL "$URL" -o /tmp/rhubarb.zip && unzip -q -o /tmp/rhubarb.zip -d /tmp/rhubarb_x || exit 0
  BIN=$(find /tmp/rhubarb_x -type f -name rhubarb | head -n1)
  [ -z "$BIN" ] && { echo "Rhubarb binary not found in archive"; exit 0; }
  rm -rf "$DEST" && cp -r "$(dirname "$BIN")" "$DEST" && chmod +x "$DEST/rhubarb"
fi
sudo ln -sf "$DEST/rhubarb" /usr/local/bin/rhubarb
rhubarb --version || true
