#!/usr/bin/env python3
"""Capture the kit's screens off the Mate 70 Air, one cold launch per screen.

The proven recipe: repeated in-process remounts exhaust ArkUI nodes and
event-thread mounts detach, so the app advances through a persisted counter
(Index.ets) — each launch shows the next screen. Every Nth rapid relaunch
renders black (period drifts with pacing), so a black capture retries when
the counter wraps around.

Prereqs: HAP freshly installed via build-atro.sh (uninstall first so the
counter starts at 0). Usage: capture_ohos.py [--kit atro]
"""
import os
import pathlib
import subprocess
import sys
import time

from PIL import Image
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import kitconf  # noqa: E402

HDC = os.environ.get(
    "HDC", str(pathlib.Path.home() / "ohos-sdk/ohos-base-deveco/21/toolchains/hdc"))
DEV = None  # set from kit config below
PKG = "com.example.myapplication"


def hdc(*a):
    return subprocess.run([HDC, "-t", DEV, *a], capture_output=True)


def main():
    kit = kitconf.load(sys.argv[sys.argv.index("--kit") + 1]
                       if "--kit" in sys.argv else "atro")
    global DEV
    DEV = os.environ.get("OHOS_SERIAL", kit["ohos_serial"])
    names = kit["screens"]
    out = kit["ohos_dir"]
    out.mkdir(exist_ok=True)
    n = len(names)
    need = {i for i in range(n) if not (out / f"{names[i]}.png").exists()}
    for _ in range(n * 3 + 40):
        if not need:
            break
        hdc("shell", "aa", "force-stop", PKG)
        time.sleep(1.0)
        hdc("shell", "hilog", "-r")
        hdc("shell", "aa", "start", "-a", "EntryAbility", "-b", PKG)
        time.sleep(6.5)
        # The counter on the phone is the only truth: a crashed or throttled
        # launch silently desyncs any local mirror, and 107 mislabeled
        # captures judge as 107 rejects. The app logs the index it mounted.
        log = hdc("shell", "hilog", "-x", "-T", "SplashOH").stdout.decode("utf-8", "replace")
        shown = None
        for line in reversed(log.splitlines()):
            if "atroScreen(" in line:
                shown = int(line.split("atroScreen(")[1].split(")")[0]) % n
                break
        if shown is None:
            print("no mount log; relaunching", flush=True)
            continue
        if shown not in need:
            continue
        hdc("shell", "snapshot_display", "-f", "/data/local/tmp/cap.jpeg")
        hdc("file", "recv", "/data/local/tmp/cap.jpeg", "/tmp/cap.jpeg")
        im = Image.open("/tmp/cap.jpeg").convert("RGB")
        if np.asarray(im.convert("L")).mean() > 2.0:
            im.crop((0, 112, im.width, im.height)).save(out / f"{names[shown]}.png")
            need.discard(shown)
            print(f"{shown:03d} {names[shown]} ok ({len(need)} left)", flush=True)
        else:
            print(f"{shown:03d} {names[shown]} black; retry on wrap", flush=True)
    if need:
        sys.exit(f"unfinished: {sorted(need)}")


if __name__ == "__main__":
    main()
