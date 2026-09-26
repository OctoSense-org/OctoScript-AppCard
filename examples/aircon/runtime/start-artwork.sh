#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
mkdir -p "$SERVICE_APP_ROOT/runtime/artwork"
if [[ ! -e "$SERVICE_APP_ROOT/runtime/artwork/ux-images" && ! -L "$SERVICE_APP_ROOT/runtime/artwork/ux-images" ]]; then
  ln -s ../../artwork "$SERVICE_APP_ROOT/runtime/artwork/ux-images"
fi
exec "$BEAUTY_PYTHON" -m http.server 8170 --bind 127.0.0.1 \
  --directory "$SERVICE_APP_ROOT/runtime/artwork"
