#!/usr/bin/env python3
"""Stage 1: generate mockups. Free rein, no format constraints.

Constraining generation is what kills the taste — every measurement in this
project points the same way, and the constraint belongs downstream on the
translation, not here. So the prompts name a subject and a design school and
otherwise get out of the way.

This stage was reported blocked for most of a session on a bad check: the key
was on disk the whole time and `api.openai.com` answers directly. No proxy is
involved. Worth stating because the belief cost more than the work.

Usage:  e0_generate.py [--n 12] [--out e0]
"""
import base64
import concurrent.futures as cf
import json
import os
import pathlib
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
KEY_FILE = os.environ.get("OAI_KEY_FILE", "")
URL = "https://api.openai.com/v1/images/generations"

# Subject × school. The subjects are the card domains the corpus actually has;
# the schools are deliberately far apart, because E0 measures whether a judge
# can rank them and a set that all looks alike would answer nothing.
SUBJECTS = [
    ("weather", "a phone weather screen: one city, the current temperature very "
                "large, condition, and a short forecast list"),
    ("news", "a phone news screen: one lead story, then a list of headlines"),
    ("stock", "a phone stock screen: one ticker, the price large, the day's "
              "change, and a few figures"),
    ("transit", "a phone transit screen: the next departure large, then the "
                "following departures as rows"),
]
SCHOOLS = [
    ("editorial", "editorial print design — a serif display face, generous "
                  "margins, one dominant element, restrained palette"),
    ("bauhaus", "Bauhaus — primary colours, hard geometry, a strict grid, "
                "heavy sans type"),
    ("terracotta", "warm earth tones, a single saturated ground carrying the "
                   "whole screen, light type over it"),
    ("brutalist", "brutalist web — monospace, hairline rules, near-monochrome, "
                  "deliberately plain"),
]

PROMPT = ("A UI design mockup, {subject}. Design direction: {school}. "
          "Portrait phone screen, filling the frame edge to edge. "
          "Realistic plausible content, not lorem ipsum. No device frame, no "
          "hand, no desk — the screen only.")


def key():
    if KEY_FILE:
        return pathlib.Path(KEY_FILE).read_text().strip()
    return os.environ["OPENAI_API_KEY"]


def gen(spec, out_dir):
    (name, subject), (school, style) = spec
    dst = out_dir / f"{name}-{school}-mockup.png"
    if dst.exists():
        return dst.name, "cached"
    body = {"model": "gpt-image-2",
            "prompt": PROMPT.format(subject=subject, school=style),
            "size": "1024x1536", "quality": "medium"}
    req = urllib.request.Request(
        URL, data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key()}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            d = json.load(r)
        dst.write_bytes(base64.b64decode(d["data"][0]["b64_json"]))
        return dst.name, "ok"
    except Exception as e:
        detail = e.read().decode()[:110] if hasattr(e, "read") else str(e)[:110]
        return dst.name, f"FAILED {detail}"


def main():
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 12
    out = HERE / (sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "e0")
    out.mkdir(exist_ok=True)
    plan = [(SUBJECTS[i % len(SUBJECTS)], SCHOOLS[(i // len(SUBJECTS)) % len(SCHOOLS)])
            for i in range(n)]
    print(f"{n} mockups -> {out}\n")
    with cf.ThreadPoolExecutor(4) as ex:
        for i, (nm, status) in enumerate(ex.map(lambda s: gen(s, out), plan), 1):
            print(f"  [{i}/{n}] {nm:<34} {status}", flush=True)
    have = len([p for p in out.glob("*mockup*.png")])
    print(f"\n{have} mockups on disk")


if __name__ == "__main__":
    main()
