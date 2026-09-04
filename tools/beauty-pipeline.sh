#!/usr/bin/env bash
# Entry point for the beauty card pipeline (design kit -> judged live cards).
# Docs: lab/sketch/README.md. Everything forwards to run_kit.py:
#   tools/beauty-pipeline.sh --kit camo --stages doctor
#   tools/beauty-pipeline.sh --kit <name> --stages unpack,extract,theme
#   tools/beauty-pipeline.sh --kit <name> --stages author,desktop,android,ohos
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/../lab/sketch"
exec python3 run_kit.py "$@"
