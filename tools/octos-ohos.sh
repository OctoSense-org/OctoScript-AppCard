#!/usr/bin/env bash
# Studio RunItem: signed release app + embedded core, normal prompt generation.
# SDK/signing stay local. Request JSON carries test options, never bundled keys.
set -euo pipefail
umask 077
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SDK_ENV="${OCTOS_OHOS_SDK_ENV:-$HOME/ohos-sdk/env-deveco.sh}"
if [[ -f "$SDK_ENV" ]]; then source "$SDK_ENV"; fi
export DEVECO_HOME="${DEVECO_HOME:-/Applications/DevEco-Studio.app/Contents}"
export HDC="${HDC:-$DEVECO_HOME/sdk/default/openharmony/toolchains/hdc}"
export OCTOS_OHOS_ROOT="$ROOT"
export OCTOS_OHOS_REQUEST="${OCTOS_OHOS_REQUEST:-/tmp/octos-ohos-request.json}"
export RUSTFLAGS=''
python3 "$ROOT/tools/octos-ohos.py"
