#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
cd "$APPCARD_ROOT"
exec "$BEAUTY_PYTHON" lab/core/studio_bridge.py --binary "$CARGO_MAKEPAD" \
  --studio "$BEAUTY_STUDIO" --port 8182 --log "$SERVICE_APP_ROOT/runtime/studio.jsonl"
