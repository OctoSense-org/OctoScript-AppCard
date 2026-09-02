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
import pathlib
import subprocess
import sys
import time

from PIL import Image
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import kitconf  # noqa: E402

HDC = str(pathlib.Path.home() / "ohos-sdk/ohos-base-deveco/21/toolchains/hdc")
DEV = "5ZGYD25B13020968"
PKG = "com.example.myapplication"


def hdc(*a):
    return subprocess.run([HDC, "-t", DEV, *a], capture_output=True)


def main():
    kit = kitconf.load(sys.argv[sys.argv.index("--kit") + 1]
                       if "--kit" in sys.argv else "atro")
    names = kit["screens"]
    out = kit["ohos_dir"]
    out.mkdir(exist_ok=True)
    n = len(names)
    k = 0  # fresh install starts the persisted counter at 0
    need = set(range(n))
    for _ in range(n * 6):
        if not need:
            break
        hdc("shell", "aa", "force-stop", PKG)
        time.sleep(1.2)
        hdc("shell", "aa", "start", "-a", "EntryAbility", "-b", PKG)
        shown, k = k, (k + 1) % n
        if shown not in need:
            time.sleep(1.2)
            continue
        time.sleep(7.0)
        hdc("shell", "snapshot_display", "-f", "/data/local/tmp/cap.jpeg")
        hdc("file", "recv", "/data/local/tmp/cap.jpeg", "/tmp/cap.jpeg")
        im = Image.open("/tmp/cap.jpeg").convert("RGB")
        if np.asarray(im.convert("L")).mean() > 2.0:
            im.crop((0, 112, im.width, im.height)).save(out / f"{names[shown]}.png")
            need.discard(shown)
            print(f"{shown:02d} {names[shown]} ok", flush=True)
        else:
            print(f"{shown:02d} {names[shown]} black; retry on wrap", flush=True)
    if need:
        sys.exit(f"unfinished: {sorted(need)}")


if __name__ == "__main__":
    main()
