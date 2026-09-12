#!/usr/bin/env bash
# Called by the Studio weather/stock/news RunItems; builds and tests the real app.
set -euo pipefail
case "${1:-}" in
  weather|stock|news) export OCTOS_REVIEW_APP="$1" ;;
  *) echo "Usage: theme-apps-ohos.sh weather|stock|news [theme] [layout]" >&2; exit 2 ;;
esac
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export OCTOS_REVIEW_THEME="${2:-}"
case "$OCTOS_REVIEW_THEME" in
  ""|atro|atro_light|camo|camo_light|taskplan_light) ;;
  *) echo "Unknown review theme: $OCTOS_REVIEW_THEME" >&2; exit 2 ;;
esac
export OCTOS_REVIEW_EVIDENCE="$ROOT/docs/reviews/theme-phone-evidence/$OCTOS_REVIEW_APP"
if [ -n "$OCTOS_REVIEW_THEME" ]; then
  export OCTOS_REVIEW_EVIDENCE="$ROOT/docs/reviews/theme-phone-evidence/$OCTOS_REVIEW_APP-themes/$OCTOS_REVIEW_THEME"
fi
export OCTOS_REVIEW_LAYOUT="${3:-}"
case "$OCTOS_REVIEW_APP/$OCTOS_REVIEW_LAYOUT" in
  */|weather/dashboard|weather/forecast|stock/tiles|stock/chart|news/magazine|news/compact) ;;
  *) echo "Unknown app layout: $OCTOS_REVIEW_APP/$OCTOS_REVIEW_LAYOUT" >&2; exit 2 ;;
esac
if [ -n "$OCTOS_REVIEW_LAYOUT" ]; then
  export OCTOS_REVIEW_EVIDENCE="$ROOT/docs/reviews/theme-phone-evidence/structures/$OCTOS_REVIEW_APP/$OCTOS_REVIEW_LAYOUT"
fi
exec bash "$ROOT/tools/nav-ohos.sh"
