#!/usr/bin/env bash
# Entry point for the beauty card pipeline (design kit -> judged live cards).
# Setup for both branches: flows/core/REPRODUCE.md.
#   tools/beauty-pipeline.sh --kit atro-native-all --stages beauty
#   tools/beauty-pipeline.sh --kit <name> --stages splash-makepad
#   tools/beauty-pipeline.sh --kit <name> --stages audit
#   tools/beauty-pipeline.sh --kit <name> --stages report
set -euo pipefail
if [[ "${1:-}" == "--image-to-appcard-flow" ]]; then
    shift
    ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    PYTHON="${BEAUTY_PYTHON:-$ROOT/flows/image-lib/.venv/bin/python}"
    if [[ ! -x "$PYTHON" ]]; then PYTHON=python3; fi
    exec "$PYTHON" "$ROOT/flows/image-to-card/flow.py" "$@"
fi
if [[ "${1:-}" == "--repair" ]]; then
    shift
    ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    PYTHON="${BEAUTY_PYTHON:-$ROOT/flows/kits/sketch/.venv/bin/python}"
    if [[ ! -x "$PYTHON" ]]; then PYTHON=python3; fi
    exec "$PYTHON" "$ROOT/flows/core/repair.py" "$@"
fi
if [[ "${1:-}" == "--ux-image" ]]; then
    shift
    ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    PYTHON="${BEAUTY_PYTHON:-$ROOT/flows/image-lib/.venv/bin/python}"
    if [[ ! -x "$PYTHON" ]]; then PYTHON=python3; fi
    exec "$PYTHON" "$ROOT/flows/image-lib/run.py" "$@"
fi
cd "$(dirname "${BASH_SOURCE[0]}")/../flows/kits/sketch"
PYTHON="${BEAUTY_PYTHON:-$PWD/.venv/bin/python}"
if [[ ! -x "$PYTHON" ]]; then PYTHON=python3; fi
exec "$PYTHON" run_kit.py "$@"
