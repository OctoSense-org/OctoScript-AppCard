#!/usr/bin/env python3
"""Render the 15 fidelity screens ON DEVICE (OnePlus 6T), both rails.

L0: cards2/<n>.card through the SEED_L0 hook — the app assembles the kit,
fetches images over the reversed 8787 tunnel, and lays the card out live.
L3: frozen2/<n>.dsl through SEED_CARD_FILE — the pre-lowered widget dialect,
colours baked, straight onto the phone's Metal^H^H^H^H^H Vulkan surface.

Resume-safe: existing shots are skipped. Usage: render_device.py [l0|l3|all]
"""
import io
import pathlib
import subprocess
import sys
import time

from PIL import Image
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ADB = str(pathlib.Path.home() / "Library/Android/sdk/platform-tools/adb")
DEVICE = "bf0a4730"
PKG = "dev.makepad.octos_app"
REMOTE = f"/storage/emulated/0/Android/media/{PKG}/cards"
CROP_TOP, CROP_BOTTOM = 90, 195
NAMES = ["Stats_Cards", "Settings_Choose_Country", "Shop_View_12", "Social_Feed_1",
         "Social_Contacts_2", "Shop_View_18", "Email_Mail_View_1", "Chat_Doodle_Pad",
         "Alerts_View_2", "Navigation_View_9", "Onboarding_View_2", "Calendar_View_3",
         "Profile_View_6", "Calendar_View_4", "Photo_Gallery_Selection"]


def adb(*args):
    return subprocess.run([ADB, "-s", DEVICE, *args], capture_output=True)


def grab():
    shot = adb("exec-out", "screencap", "-p").stdout
    im = Image.open(io.BytesIO(shot)).convert("RGB")
    return im.crop((0, CROP_TOP, im.width, im.height - CROP_BOTTOM))


def differs(a, b):
    x = np.asarray(a.resize((90, 180)), dtype=np.int16)
    y = np.asarray(b.resize((90, 180)), dtype=np.int16)
    return float(np.abs(x - y).mean()) > 1.0


def settle(timeout=22):
    time.sleep(5)
    prev, stable = grab(), 0
    for _ in range(timeout):
        time.sleep(1)
        cur = grab()
        stable = 0 if differs(prev, cur) else stable + 1
        prev = cur
        if stable >= 2:
            return cur
    return prev


def render(local, extra_key, wait_marker):
    remote = f"{REMOTE}/{local.name}"
    adb("push", str(local), remote)
    adb("push", str(HERE / "xrail2" / "data.json"), f"{REMOTE}/data.json")
    adb("shell", "am", "force-stop", PKG)
    adb("logcat", "-c")
    adb("shell", "input", "keyevent", "KEYCODE_WAKEUP")
    adb("shell", f"am start -S -n {PKG}/.MakepadApp "
                 f"--es makepad.{extra_key} {remote} "
                 f"--es makepad.SEED_L0_DATA {REMOTE}/data.json "
                 f"--es makepad.SEED_L0_FILL_HEIGHT 812 "
                 f"--es makepad.DEV_GOAL_FILE /data/local/tmp/__no_dev_loop__")
    if wait_marker:
        for _ in range(25):
            time.sleep(1)
            log = adb("logcat", "-d").stdout.decode("utf-8", "replace")
            if wait_marker in log:
                break
            if "SEED_L0 realize failed" in log or "SEED_L0 read failed" in log:
                why = [l for l in log.splitlines() if "SEED_L0" in l][-1]
                return None, why[-140:]
    return settle(), None


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    adb("reverse", "tcp:8787", "tcp:8787")
    jobs = []
    if which in ("l0", "all"):
        jobs += [(HERE / "cards2" / f"{n}.card", "SEED_L0_FILE",
                  "SEED_L0 injected", HERE / "devl0" / f"{n}.png") for n in NAMES]
    if which in ("l3", "all"):
        jobs += [(HERE / "frozen2" / f"{n}.dsl", "SEED_CARD_FILE",
                  None, HERE / "devl3" / f"{n}.png") for n in NAMES]
    for src, key, marker, out in jobs:
        out.parent.mkdir(exist_ok=True)
        if out.exists():
            continue
        t0 = time.time()
        shot, err = render(src, key, marker)
        if shot is None:
            print(f"FAIL {out.parent.name}/{src.stem} {err}", flush=True)
            continue
        shot.save(out)
        print(f"{out.parent.name}/{src.stem} ok ({time.time() - t0:.0f}s)", flush=True)


if __name__ == "__main__":
    main()
