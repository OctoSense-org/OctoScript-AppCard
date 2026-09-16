#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
cd "$APPCARD_ROOT"
exec bash tools/beauty-studio.sh "$BEAUTY_STUDIO_BIN" --remote \
  --mounts="splashref:$PWD/splash-makepad" --bind="$BEAUTY_STUDIO"
