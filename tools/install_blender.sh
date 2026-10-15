#!/usr/bin/env bash
# Installs Blender (headless) into ~/blender and links it to /usr/local/bin/blender
set -euo pipefail
VER="${BLENDER_VERSION:-4.2.3}"
MAJOR="${VER%.*}"
DIR="$HOME/blender/blender-${VER}-linux-x64"
if [ ! -x "$DIR/blender" ]; then
  mkdir -p "$HOME/blender"
  wget -q --tries=3 "https://download.blender.org/release/Blender${MAJOR}/blender-${VER}-linux-x64.tar.xz" -O /tmp/blender.tar.xz
  tar -xf /tmp/blender.tar.xz -C "$HOME/blender"
fi
sudo ln -sf "$DIR/blender" /usr/local/bin/blender
blender --version | head -n 1
