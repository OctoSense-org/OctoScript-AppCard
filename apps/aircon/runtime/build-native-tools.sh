#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
cd "$OCTOSENSE_WORKSPACE/makepad"
exec cargo build --release -p makepad-studio -p cargo-makepad
