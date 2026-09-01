#!/usr/bin/env python3
"""Instructed LLM composition: the card author sees the design, knows the pack.

This replaces the deterministic translator for the fidelity question. The
translator proved the LANGUAGE (150/150 validate, recall 83%) and scored 2/10 on
strict design likeness — its ceiling, not the language's: it never used Grid,
never centred a stack, never made a button a Chip. This author is INSTRUCTED:
it reads the target image and a measured digest, writes against the full
constructor list with the Atro pack available, and repairs against the checker's
own diagnostics.

Usage: author_cards.py [--only substr] [--round2]
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "style-factory"))
import batch_styles as B  # noqa: E402

SPLASH = pathlib.Path.home() / "home" / "Splash"
NAMES = ["Stats_Cards", "Settings_Choose_Country", "Shop_View_12", "Social_Feed_1",
         "Social_Contacts_2", "Shop_View_18", "Email_Mail_View_1", "Chat_Doodle_Pad",
         "Alerts_View_2", "Navigation_View_9", "Onboarding_View_2", "Calendar_View_3",
         "Profile_View_6", "Calendar_View_4", "Photo_Gallery_Selection"]

RULES = """You are writing a Splash L0 card. HARD RULES:
- Header lines first: `# level: L0` and `# model: atro-app`, then `theme atro` (dark screens) or `theme atro_light` (light screens). The pack carries the kit's palette, Montserrat, radii and depth — never write a colour, size or file path.
- Constructors (the ONLY ones): Surface(pad) Panel Card Col(align,gap,width) Row(width,align,gap) Grid(cols) Rule() Field(text,placeholder) Chip(text,active,tone,width) TextHero(text,value,unit) TextTitle(text,width) TextBody(text,width) TextRow(text,width) TextEyebrow(text) TextCaption(text,value,glyph,suffix,width) TextValue(value,unit,tint) TextStat(value,tint) Tile(label,value,unit) Thumb(src).
- Literal strings ARE allowed in text/placeholder/glyph args: TextTitle(text: "Savings"). Use the design's exact strings.
- Tokens start with a dot: width: .fill, align: .center, pad: .page.
- view root Surface(pad: .page) { ... } wraps everything. Views may be split: `view root ...` referencing `view sectionname Col(...) {...}` by bare name.
- IMAGES: ONLY urls that appear in the digest may be used — NEVER invent one. IMAGE lines are real photos; MEDIA lines are the design's own grey placeholder tiles (galleries, feed media, thumbnails) — bind them exactly the same way. Pattern: declare `state pN { shape: text, initial: "<the url>" }` then `Thumb(src: pN)` where the image sits. A photo GRID (gallery, mosaic, feed media) is `Grid(cols: 3) { Thumb(src: p1) Thumb(src: p2) ... }`. A full-bleed hero image screen uses `view root Photo(src: p1, pad: .page) { ... }` instead of Surface. Small round person photos may be Avatar initials instead.
- TYPE DISCIPLINE: TextHero is ONLY for the screen's one dominant number/word (a balance, a temperature). List items and names are TextRow; section headers are TextTitle; metadata is TextCaption. Never TextHero in a list.
- MODE: match the design exactly — a white/light screen is `theme atro_light`, a dark one `theme atro`. Do not invert.
- NO icons exist. For small marks you may use a unicode glyph inside TextCaption(glyph: "✓") — sparingly, monochrome symbols only, never emoji.
- NEW capabilities you MUST use where the design does: Avatar(text: "TC") — a tinted initials circle for every avatar/person slot (write the initials yourself from the name); Chip(text: "...", tone: .primary) for the screen's CTA/primary button (renders as a filled accent pill); Card { ... } for CONTENT cards — in this pack a Card takes the kit's signature indigo gradient automatically (use Card for credit cards, feature tiles, hero blocks; use Panel for plain sections).
- Composition tools you MUST use where the design does: a photo/media mosaic is Grid(cols: 2 or 3) of Thumb; a month calendar is Grid(cols: 7) of Tile(label: "1") cells; Grid(cols: N) for grids; Col(align: .center) for centered stacks; Chip(text: "...") for buttons/CTAs (they render as filled pills in this pack); Row { TextRow(text:.., width: .fill) TextValue(value: "..") } for label-left value-right rows; Rule() for dividers; Field(placeholder: "...") for inputs; Tile for small stat cells inside Grid.
- Reproduce the DESIGN: same sections in the same order, same alignment, same grouping into panels, exact text. Do not invent content. Skip status bars, keyboards and iPhone chrome.
Return ONLY the card source, no fences, no commentary."""


def digest(spec, budget=110):
    lines = []

    def walk(n, d):
        if len(lines) > budget:
            return
        t = n.get("text")
        ind = " " * d
        if t and (t.get("string") or "").strip():
            r = t.get("run") or {}
            lines.append(f"{ind}TEXT {n['x']:.0f},{n['y']:.0f} w{n['w']:.0f} "
                         f"size{(r.get('size') or 0)/2:.0f} align{r.get('align', 0)} "
                         f"\"{' '.join(t['string'].split())[:60]}\"")
        elif n.get("cls") == "bitmap":
            ref = (n.get("image") or "").split("/")[-1]
            url = f" url=http://127.0.0.1:8787/{ref}" if ref else ""
            lines.append(f"{ind}IMAGE {n['x']:.0f},{n['y']:.0f} {n['w']:.0f}x{n['h']:.0f}{url}")
        elif (n.get("cls") == "rectangle" and n.get("fill")
              and n["w"] > 80 and n["h"] > 80 and not n.get("children")
              and (200 <= int(n["fill"]["hex"][1:3], 16) <= 232
                   or int(n["fill"]["hex"][1:3], 16) < 50)
              and abs(int(n["fill"]["hex"][1:3], 16) - int(n["fill"]["hex"][5:7], 16)) < 30):
            # The kit's screen-mock grey: a PLACEHOLDER MEDIA TILE, which is a
            # design element in its own right — the gallery mosaic is 60 of
            # these, not photographs.
            ph = "_ph_dark.png" if int(n["fill"]["hex"][1:3], 16) < 50 else "_ph.png"
            lines.append(f"{ind}MEDIA {n['x']:.0f},{n['y']:.0f} {n['w']:.0f}x{n['h']:.0f} "
                         f"url=http://127.0.0.1:8787/{ph}")
        elif n.get("cls") == "rectangle" and n.get("radius", 0) >= 10 and n["w"] > 120:
            lines.append(f"{ind}PANEL {n['x']:.0f},{n['y']:.0f} {n['w']:.0f}x{n['h']:.0f} r{n['radius']:.0f}")
        name = (n.get("name") or "").lower()
        if "button" in name and n.get("cls") == "symbolInstance":
            lines.append(f"{ind}BUTTON {n['x']:.0f},{n['y']:.0f} w{n['w']:.0f}")
        for c in n.get("children", []):
            walk(c, d + 1)
    walk(spec, 0)
    return "\n".join(lines[:budget])


def validate(card_path):
    r = subprocess.run(
        ["cargo", "run", "-q", "-p", "splash-ui-l0", "--example", "l0validate",
         "--", str(card_path)],
        capture_output=True, text=True, cwd=SPLASH)
    try:
        d = json.loads(r.stdout)
        return d.get("ok", False), d.get("diagnostics", [])
    except Exception:
        return False, [r.stdout[:200] or r.stderr[:200]]


def author(name, round2_note=""):
    spec = json.loads((HERE / "specs" / f"{name}.json").read_text())
    target = HERE / "targets" / f"{name}.png"
    dig_file = HERE / "cards2" / f"{name}.digest.txt"
    dig_file.write_text(digest(spec))
    mode_hint = "light" if "light" in judge_mode(spec) else "dark"
    prompt = (f"Read {target} — a mobile app screen design to reproduce.\n"
              f"Read {dig_file} — the measured element digest (positions are @2x; "
              f"indentation = the design's own grouping).\n\n{RULES}\n\n"
              f"The screen reads as a {mode_hint} screen.\n{round2_note}")
    src = B.strip_fence(B.claude_text(prompt, timeout=600)).strip()
    card = HERE / "cards2" / f"{name}.card"
    card.write_text(src + "\n")
    ok, diags = validate(card)
    for attempt in range(2):
        if ok:
            break
        fix = B.strip_fence(B.claude_text(
            f"Read {card} — an L0 card that FAILED validation with:\n"
            + "\n".join(f"- {d}" for d in diags[:6])
            + f"\n\n{RULES}\n\nReturn the corrected FULL card source only.",
            timeout=600)).strip()
        card.write_text(fix + "\n")
        ok, diags = validate(card)
    return ok, diags


def judge_mode(spec):
    f = spec.get("fill")
    # crude: use the artboard's own background name/colour cues via children scan
    darks = lights = 0

    def walk(n):
        nonlocal darks, lights
        a = n.get("fill")
        if a and a["a"] > 0.9 and n["w"] * n["h"] > 200000:
            h = a["hex"].lstrip("#")
            lum = int(h[0:2], 16) + int(h[2:4], 16) + int(h[4:6], 16)
            if lum < 300:
                darks += 1
            elif lum > 600:
                lights += 1
        for c in n.get("children", []):
            walk(c)
    walk(spec)
    return "light" if lights >= darks else "dark"


def main():
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else ""
    (HERE / "cards2").mkdir(exist_ok=True)
    feedback = {}
    if "--round2" in sys.argv:
        for l in (HERE / "xrail" / "strict2.jsonl").open():
            r = json.loads(l)
            if r["design_match"] < 6:
                feedback[r["screen"]] = r.get("worst", "")
    for name in NAMES:
        if only and only not in name:
            continue
        if "--round2" in sys.argv and name not in feedback:
            continue
        note = (f"A previous attempt was rejected by a design reviewer for: "
                f"\"{feedback[name]}\" — fix exactly that.\n") if name in feedback else ""
        ok, diags = author(name, note)
        print(f"{name:<28} {'valid' if ok else 'INVALID: ' + str(diags[:1])[:80]}",
              flush=True)


if __name__ == "__main__":
    main()
