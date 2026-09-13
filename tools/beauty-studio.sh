#!/usr/bin/env bash
# Start the release Studio server with backing space for full artboard captures.
# Apps are subsequently built and launched through Studio RunItem.
set -euo pipefail
if [[ $# -lt 1 ]]; then
    echo 'Usage: beauty-studio.sh /path/to/target/release/makepad-studio [Studio arguments]' >&2
    exit 2
fi
studio_binary="$1"
shift
if [[ ! -x "$studio_binary" ]]; then
    echo "Studio release binary is missing: $studio_binary" >&2
    exit 1
fi
export MAKEPAD_RUNVIEW_MIN_ALLOC_WIDTH="${BEAUTY_CAPTURE_WIDTH_PX:-2048}"
export MAKEPAD_RUNVIEW_MIN_ALLOC_HEIGHT="${BEAUTY_CAPTURE_HEIGHT_PX:-4096}"
exec "$studio_binary" "$@"
