#!/usr/bin/env python3
"""Render the authored cards. Theme comes from the card itself now — the pack
is real language, so no override splice, which is itself the proof of step 1."""
import json, os, pathlib, sys, time
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "gates"))
os.environ["GATE_WINDOW"] = "375x812"
import shoot
shoot.SIZE = "375x812"
OUT = HERE / "xrail2"; OUT.mkdir(exist_ok=True)
# The kit's own photos, served to the cards. Cards carry the URLs as demo-data
# state initials — the sanctioned slot — and the renderer fetches them like any
# data image. Start the server if it is not already up.
import socket, subprocess
IMG = pathlib.Path("/private/tmp/claude-501/-Users-yuechen-home-Splash/"
                   "df6c4ec5-2002-4e8f-84de-7d846576918e/scratchpad/atro/src/images")
s = socket.socket()
if s.connect_ex(("127.0.0.1", 8787)) != 0:
    subprocess.Popen(["python3", "-m", "http.server", "8787"], cwd=IMG,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
s.close()
DATA = OUT / "data.json"; DATA.write_text(json.dumps({"env": {"locale": {}}}))
for card in sorted((HERE / "cards2").glob("*.card")):
    png = OUT / f"{card.stem}.png"
    if png.exists(): continue
    ok = shoot.shoot(card, png, None, data=DATA)
    print(card.stem, "ok" if ok else "FAILED", flush=True)
