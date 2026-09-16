#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
APP_MAIL_PIPELINE="${OCTOS_APPCARD_PIPELINE:-$(cd ../.. && pwd)}"
APP_MAIL_PYTHON="${OCTOS_MAIL_PYTHON:-$APP_MAIL_PIPELINE/lab/image-to-appcard/.venv/bin/python}"
if [[ ! -x "$APP_MAIL_PYTHON" ]]; then
  echo 'Set up the pipeline Python environment as described in apps/mail/README.md.' >&2
  exit 1
fi
exec "$APP_MAIL_PYTHON" scripts/run.py --background "$@"
