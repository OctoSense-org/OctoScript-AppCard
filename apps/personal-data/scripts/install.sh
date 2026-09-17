#!/bin/sh
# Build the personal-data skill and install it into an octos profile.
#
#   bash scripts/install.sh --profile dev \
#       --mail-dir "$TMPDIR/octosense-native-mail/mail" \
#       --calendar http://127.0.0.1:8190 --calendar-token-file path/to/calendar.token
#
# Options: --profile <id> (default _main), --mail-dir <dir> (repeatable),
# --calendar <url>, --calendar-token-file <file>, --calendar-state-file <file>,
# --index-bodies, --locale <en|cn>, --stage-only <dir> (write the skill dir and stop).
set -eu
here=$(cd "$(dirname "$0")/.." && pwd)
profile=_main
locale=en
index_bodies=false
calendar=""
token_file=""
state_file=""
stage_only=""
mail_dirs=""
while [ $# -gt 0 ]; do
  case "$1" in
    --profile) profile=$2; shift 2 ;;
    --mail-dir) mail_dirs="$mail_dirs
$2"; shift 2 ;;
    --calendar) calendar=$2; shift 2 ;;
    --calendar-token-file) token_file=$2; shift 2 ;;
    --calendar-state-file) state_file=$2; shift 2 ;;
    --index-bodies) index_bodies=true; shift ;;
    --locale) locale=$2; shift 2 ;;
    --stage-only) stage_only=$2; shift 2 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done
[ -n "$mail_dirs" ] || mail_dirs="${TMPDIR:-/tmp}/octosense-native-mail/mail"

(cd "$here" && cargo build --release --quiet)

stage=${stage_only:-$(mktemp -d "${TMPDIR:-/tmp}/personal-data-skill.XXXXXX")/personal-data}
mkdir -p "$stage"
cp "$here/target/release/main" "$stage/main"
chmod 755 "$stage/main"
cp "$here/skill/manifest.json" "$here/skill/SKILL.md" "$stage/"

# Absolute paths: the skill runs with the agent session's cwd, not ours.
dirs_json=$(printf '%s\n' "$mail_dirs" | sed '/^$/d' | python3 -c 'import json,os,sys; print(json.dumps([os.path.abspath(l.rstrip("\n")) for l in sys.stdin]))')
cal_json='{}'
if [ -n "$state_file" ]; then
  cal_json=$(python3 -c 'import json,sys,os; print(json.dumps({"state_file": os.path.abspath(sys.argv[1])}))' "$state_file")
elif [ -n "$calendar" ]; then
  if [ -n "$token_file" ]; then
    cp "$token_file" "$stage/calendar.token"
    chmod 600 "$stage/calendar.token"
    cal_json=$(python3 -c 'import json,sys; print(json.dumps({"server": sys.argv[1], "token_file": "calendar.token", "timeout_secs": 2}))' "$calendar")
  else
    cal_json=$(python3 -c 'import json,sys; print(json.dumps({"server": sys.argv[1], "timeout_secs": 2}))' "$calendar")
  fi
fi
python3 - "$stage/config.json" "$locale" "$dirs_json" "$index_bodies" "$cal_json" <<'EOF'
import json, sys
path, locale, dirs, bodies, cal = sys.argv[1:]
json.dump({"locale": locale, "mail": {"dirs": json.loads(dirs), "index_bodies": bodies == "true"}, "calendar": json.loads(cal)}, open(path, "w"), indent=2)
EOF

echo "staged skill in $stage"
if [ -n "$stage_only" ]; then
  exit 0
fi
octos skills --profile "$profile" install "$stage" --force
octos skills --profile "$profile" info personal-data || true
