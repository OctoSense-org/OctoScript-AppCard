#!/usr/bin/env bash
# Source from bash, then run the image-to-AppCard pipeline from its root.
SERVICE_APP_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
APPCARD_ROOT="$(cd "$SERVICE_APP_ROOT/../.." && pwd)"
export SERVICE_APP_ROOT APPCARD_ROOT
OCTOSENSE_WORKSPACE="$(PYTHONPATH="$APPCARD_ROOT/lab" python3 -c 'from core.native_paths import WORKSPACE; print(WORKSPACE)')"
export OCTOSENSE_WORKSPACE
export BEAUTY_PYTHON="$APPCARD_ROOT/lab/image-to-appcard/.venv/bin/python"
export BEAUTY_STUDIO="127.0.0.1:8012"
export BEAUTY_BRIDGE="http://127.0.0.1:8182"
export BEAUTY_STUDIO_BIN="$OCTOSENSE_WORKSPACE/makepad/target/release/makepad-studio"
export CARGO_MAKEPAD="$OCTOSENSE_WORKSPACE/makepad/target/release/cargo-makepad"
# The pinned Makepad profile-use flag is relative to individual crate roots.
# Disable that optional physics PGO profile for this portable UI reproduction.
export RUSTFLAGS=""
