#!/usr/bin/env python3
"""Capture the 15 Atro screens off the Mate 70 Air, tap-advancing between them.

Each generated screen carries an invisible tap strip whose route is the next
index; a uitest click fires it. The click point probes center then top, since
the stack's alignment decides where the strip landed.
"""
import io
import pathlib
import subprocess
import time

from PIL import Image
import numpy as np

HDC = str(pathlib.Path.home() / "ohos-sdk/ohos-base-deveco/21/toolchains/hdc")
DEV = "5ZGYD25B13020968"
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "devoh"
NAMES = ["Stats_Cards", "Settings_Choose_Country", "Shop_View_12", "Social_Feed_1",
         "Social_Contacts_2", "Shop_View_18", "Email_Mail_View_1", "Chat_Doodle_Pad",
         "Alerts_View_2", "Navigation_View_9", "Onboarding_View_2", "Calendar_View_3",
         "Profile_View_6", "Calendar_View_4", "Photo_Gallery_Selection"]


def hdc(*args):
    return subprocess.run([HDC, "-t", DEV, *args], capture_output=True)


def grab():
    hdc("shell", "snapshot_display", "-f", "/data/local/tmp/cap.jpeg")
    hdc("file", "recv", "/data/local/tmp/cap.jpeg", "/tmp/mate_cap.jpeg")
    im = Image.open("/tmp/mate_cap.jpeg").convert("RGB")
    return im.crop((0, 112, im.width, im.height))  # status bar off


def sig(im):
    return np.asarray(im.resize((60, 120)), dtype=np.int16)


def advance(prev):
    for x, y in ((660, 1490), (660, 700), (660, 2200)):
        hdc("shell", "uitest", "uiInput", "click", str(x), str(y))
        time.sleep(2.2)
        cur = grab()
        if float(np.abs(sig(cur) - sig(prev)).mean()) > 1.2:
            return cur
    return None


def main():
    OUT.mkdir(exist_ok=True)
    time.sleep(2)
    shot = grab()
    for i, name in enumerate(NAMES):
        shot.save(OUT / f"{name}.png")
        print(f"{i:02d} {name} saved", flush=True)
        if i + 1 < len(NAMES):
            nxt = advance(shot)
            if nxt is None:
                print(f"ADVANCE FAILED after {name}", flush=True)
                return
            shot = nxt


if __name__ == "__main__":
    main()
