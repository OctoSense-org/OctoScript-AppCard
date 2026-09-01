#!/usr/bin/env python3
"""Generate STYLE ELEMENTS separately — heroes, textures, icon sheets.

A whole-screen mockup bakes its art into a picture of a layout, so the art
cannot be reused and the layout cannot be trusted. Elements separate the two:
the app owns the layout, and these are the pieces a theme drops into it.

The families are not symmetric, and the asymmetry is the point:

  hero      full colour. It IS the image — a photograph or a painted backdrop —
            so it carries its own palette and the scrim is what makes text
            readable over it.

  texture   GREYSCALE and seamless. A texture with baked colour is another
            disconnected knob: it would fight whatever accent the card names,
            exactly the way `l0_accent` fought nothing because nothing read it.
            Generated as luminance only, applied as an alpha the palette tints.

  icons     monochrome silhouettes on a flat ground, one drawing idiom per
            sheet, sliced into cells. Same reason as texture — an icon that
            arrives pre-coloured cannot follow `l0_text`.

  gradient  NOT generated. A gradient is four numbers and an angle; as an image
            it cannot rescale, cannot recolour, and cannot follow the accent.
            `gradients.py` derives them from the palette instead.

Usage:  gen_assets.py [--family hero|texture|icons|all] [--n 4] [--out assets]
"""
import base64
import concurrent.futures as cf
import json
import os
import pathlib
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
URL = "https://api.openai.com/v1/images/generations"
MODEL = "gpt-image-2"

# Backdrops for the domains the corpus actually has. No text, no UI, no device —
# anything the model draws that looks like a control is something the renderer
# will draw again on top of it.
HEROES = [
    ("weather-alpine", "a cold alpine valley under high cloud, blue hour"),
    ("weather-coast", "a warm coastline at golden hour, long shadows"),
    ("news-city", "a dense city skyline at dusk, muted and grey"),
    ("stock-abstract", "an abstract dark field of soft vertical light streaks"),
    ("transit-tunnel", "a train platform at night, wet concrete, sodium light"),
    ("activity-market", "a sunlit market street, shallow depth of field"),
]

# Surface grain. Named by MATERIAL rather than by mood, because a material is
# reusable across moods and a mood is not.
TEXTURES = [
    ("paper-laid", "laid paper fibre, fine horizontal chain lines"),
    ("concrete", "smooth poured concrete, faint pitting and drift"),
    ("linen", "woven linen weave, even and regular"),
    ("noise-fine", "fine analogue film grain, uniform"),
    ("halftone", "a regular halftone dot screen at 45 degrees"),
    ("deco-fan", "an art deco sunburst fan motif, radiating thin lines"),
]

# One idiom per sheet, so the whole set matches. Mixed idioms are what makes a
# generated icon set read as generated.
ICON_SETS = [
    ("line", "thin uniform stroke line icons, rounded caps, no fill"),
    ("solid", "solid filled silhouette icons, no stroke"),
    ("deco", "art deco geometric icons, symmetric, stepped forms"),
]
ICON_GLYPHS = ("sun, cloud, rain, snow, wind, moon, thermometer, umbrella, "
               "arrow up, arrow down, clock, location pin")

PROMPTS = {
    "hero": (
        "{desc}. A photographic backdrop for a phone screen. Portrait, filling "
        "the frame. NO text, NO user interface, NO logos, NO people in focus, no "
        "device frame. Leave the upper third relatively uncluttered so a title "
        "can sit over it."),
    "texture": (
        "A seamless tiling texture: {desc}. GREYSCALE ONLY — no colour, no hue, "
        "pure luminance. Even overall value, no vignette, no lighting gradient, "
        "no focal point. It must tile edge to edge without a visible seam. Flat "
        "and subtle, as a surface grain, not as a picture."),
    "icons": (
        "A sheet of {desc}, arranged in a strict 4 by 3 grid on a plain white "
        "background, generous even margins around each cell. The twelve icons "
        "are: {glyphs}. PURE BLACK icons on PURE WHITE, no colour, no grey fills, "
        "no shadows, no labels, no text, no grid lines or frames. Every icon the "
        "same visual weight and the same optical size."),
}
SIZES = {"hero": "1024x1536", "texture": "1024x1024", "icons": "1024x1024"}


def key():
    p = os.environ.get("OAI_KEY_FILE")
    if p:
        return pathlib.Path(p).read_text().strip()
    return os.environ["OPENAI_API_KEY"]


def gen(family, name, prompt, out_dir):
    dst = out_dir / family / f"{name}.png"
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        return f"{family}/{name}", "cached"
    body = {"model": MODEL, "prompt": prompt, "size": SIZES[family],
            "quality": "medium"}
    req = urllib.request.Request(
        URL, data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key()}",
                 "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            d = json.load(r)
        dst.write_bytes(base64.b64decode(d["data"][0]["b64_json"]))
        return f"{family}/{name}", "ok"
    except Exception as e:
        detail = e.read().decode()[:120] if hasattr(e, "read") else str(e)[:120]
        return f"{family}/{name}", f"FAILED {detail}"


def plan_for(family, n):
    if family == "hero":
        return [("hero", nm, PROMPTS["hero"].format(desc=d))
                for nm, d in HEROES[:n]]
    if family == "texture":
        return [("texture", nm, PROMPTS["texture"].format(desc=d))
                for nm, d in TEXTURES[:n]]
    if family == "icons":
        return [("icons", nm, PROMPTS["icons"].format(desc=d, glyphs=ICON_GLYPHS))
                for nm, d in ICON_SETS[:n]]
    return []


def main():
    family = sys.argv[sys.argv.index("--family") + 1] if "--family" in sys.argv else "all"
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 4
    out = HERE / (sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "assets")
    fams = ["hero", "texture", "icons"] if family == "all" else [family]
    plan = [job for f in fams for job in plan_for(f, n)]
    print(f"{len(plan)} elements -> {out}\n")
    with cf.ThreadPoolExecutor(4) as ex:
        for i, (nm, status) in enumerate(
                ex.map(lambda j: gen(j[0], j[1], j[2], out), plan), 1):
            print(f"  [{i}/{len(plan)}] {nm:<26} {status}", flush=True)


if __name__ == "__main__":
    main()
