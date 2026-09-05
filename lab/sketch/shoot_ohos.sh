#!/usr/bin/env bash
# Capture the first N device-assembled screens off the Mate 70 Air, in order.
#
#   shoot_ohos.sh <out-dir> [count]
#
# The exhibit advances through a PERSISTED counter — one screen per cold start,
# because repeated in-process remounts exhaust ArkUI nodes — and that counter
# wraps at 15 while the themed screens occupy the first few slots. Waiting for
# the wanted index to come round took twelve relaunches for one screenshot, and
# a mirror counter kept on the host silently desynchronised whenever a launch
# wedged, which mislabelled a whole run.
#
# So: clear the app's data once, which resets the counter to 0, then take the
# screens in launch order and CONFIRM each against the index the app logged.
set -uo pipefail
# hdc lives in the DevEco toolchains, not on a login PATH. Without this every
# command below fails silently and the run reports four captures it never took.
source ~/ohos-sdk/env-deveco.sh >/dev/null 2>&1
export PATH="$HOME/ohos-sdk/ohos-base-deveco/21/toolchains:$PATH"
command -v hdc >/dev/null || { echo "hdc not found — check ~/ohos-sdk/env-deveco.sh"; exit 1; }
DEV="${DEVICE:-5ZGYD25B13020968}"
PKG=com.example.myapplication
OUT="${1:?usage: shoot_ohos.sh <out-dir> [count]}"
N="${2:-4}"
SETTLE="${SETTLE:-14}"
mkdir -p "$OUT"

hdc -t "$DEV" shell aa force-stop $PKG >/dev/null 2>&1
hdc -t "$DEV" shell bm clean -n $PKG -d >/dev/null 2>&1   # counter -> 0
hdc -t "$DEV" shell power-shell wakeup >/dev/null 2>&1

for ((i = 0; i < N; i++)); do
  hdc -t "$DEV" shell aa force-stop $PKG >/dev/null 2>&1
  hdc -t "$DEV" shell hilog -r >/dev/null 2>&1
  # Wake and unlock EVERY time, not once at the start. A sweep runs longer
  # than the display timeout, and a slept screen captures pure black — which
  # reads exactly like the known "every Nth relaunch renders black" fault and
  # sent a whole round of debugging at the app instead of at the phone.
  hdc -t "$DEV" shell power-shell wakeup >/dev/null 2>&1
  hdc -t "$DEV" shell uinput -T -m 660 2400 660 900 300 >/dev/null 2>&1
  hdc -t "$DEV" shell aa start -a EntryAbility -b $PKG >/dev/null 2>&1
  sleep "$SETTLE"
  # The app's own idea of which screen it mounted. Never the host's count.
  log=$(hdc -t "$DEV" shell hilog -x 2>/dev/null)
  idx=$(echo "$log" | grep -o "atroScreen([0-9]*)" | tail -1 | tr -dc 0-9)
  # Values that failed to arrive. The walk counts text nodes that resolved to
  # nothing, which is the one thing a screenshot cannot tell you: the page
  # still has its panels, rows and labels, and simply no numbers.
  empty=$(echo "$log" | grep -o "[0-9]* text node(s) resolved to nothing" | tail -1 | tr -dc 0-9)
  # And what it actually asked the network for. A screen of plausible numbers
  # fetched from the wrong coordinate looks exactly like a correct one.
  echo "$log" | grep -o "net: GET [^ ]*" | sed 's/^net: /    /' | sort -u
  # Remove the remote file FIRST. `snapshot_display` fails silently often
  # enough that leaving the previous capture in place means `file recv` pulls
  # it again — a whole run of four came back byte-identical, all of them the
  # frame from the run before, with the phone's own clock in the corner as the
  # only tell.
  hdc -t "$DEV" shell rm -f /data/local/tmp/s.jpeg >/dev/null 2>&1
  hdc -t "$DEV" shell snapshot_display -f /data/local/tmp/s.jpeg >/dev/null 2>&1
  if ! hdc -t "$DEV" shell ls /data/local/tmp/s.jpeg 2>/dev/null | grep -q s.jpeg; then
    echo "shot $((i + 1))/$N -> CAPTURE FAILED (no file on device)"
    continue
  fi
  hdc -t "$DEV" file recv /data/local/tmp/s.jpeg "$OUT/oh_${idx:-unknown}.jpeg" >/dev/null 2>&1
  # A capture with no dynamic range is a slept screen or a failed mount. Say so
  # here; a blank frame that reaches a comparison page reads as a design.
  note=$(python3 - "$OUT/oh_${idx:-unknown}.jpeg" <<'PY' 2>/dev/null
import sys
from PIL import Image
import numpy as np
a = np.asarray(Image.open(sys.argv[1]).convert("L"), dtype=float)
print("  BLANK" if a.std() < 4 else "")
PY
)
  echo "shot $((i + 1))/$N -> oh_${idx:-unknown}.jpeg${note}${empty:+  ${empty} EMPTY VALUES}"
  # Pace the relaunches. Enough force-stop/start churn puts this app into a
  # state where it mounts and paints NOTHING — every screen black, surviving a
  # reinstall and even a `bm uninstall`. Only `hdc shell reboot` clears it.
  # Two seconds between launches has been enough to stay out of it.
  sleep 2
done
