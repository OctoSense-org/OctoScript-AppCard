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
- Constructors (the ONLY ones): Surface(pad) Panel Card Col(align,gap,width) Row(width,align,gap) Grid(cols) Rule() Space() Field(text,placeholder) Chip(text,active,tone,width) Icon(name,size) TextHero(text,value,unit) TextTitle(text,width) TextBody(text,width) TextRow(text,width) TextEyebrow(text) TextCaption(text,value,glyph,suffix,width) TextValue(value,unit,tint) TextStat(value,tint) Tile(label,value,unit) Thumb(src,shape).
- Literal strings ARE allowed in text/placeholder/glyph args: TextTitle(text: "Savings"). Use the design's exact strings.
- Tokens start with a dot: width: .fill, align: .center, pad: .page.
- view root Surface(pad: .page) { ... } wraps everything. Views may be split: `view root ...` referencing `view sectionname Col(...) {...}` by bare name.
- IMAGES: ONLY urls that appear in the digest may be used — NEVER invent one. IMAGE lines are real photos; MEDIA lines are the design's own grey placeholder tiles (galleries, feed media, thumbnails) — bind them exactly the same way. Pattern: declare `state pN { shape: text, initial: "<the url>" }` then `Thumb(src: pN)` where the image sits. A photo GRID (gallery, mosaic, feed media) is `Grid(cols: 3) { Thumb(src: p1) Thumb(src: p2) ... }`. A full-bleed hero image screen uses `view root Photo(src: p1, pad: .page) { ... }` instead of Surface. Small round person photos may be Avatar initials instead.
- TYPE DISCIPLINE: TextHero is ONLY for the screen's one dominant number/word (a balance, a temperature). List items and names are TextRow; section headers are TextTitle; metadata is TextCaption. Never TextHero in a list.
- MODE: match the design exactly — a white/light screen is `theme atro_light`, a dark one `theme atro`. Do not invert.
- COLORED PAGE: when the page background is a strong colour (blue, violet, green...), add a ground axis after the theme: `theme atro ground navy` (dark-leaning colour) or `theme atro_light ground ivory` (light). Grounds: teal violet navy ivory sand terracotta wine forest slate paper cream midnight blush olive — pick the nearest to the design's page colour. The theme derives readable ink and panels on it automatically.
- ICONS: Icon(name: .bell) — a closed set of ~50 semantic names rendered in the theme's icon font: activity alert arrow_down arrow_left arrow_right arrow_up bell bookmark calendar camera chat check chevron_down chevron_left chevron_right chevron_up clock close cloud edit filter heart home image info location lock mail map menu mic minus moon more phone play plus refresh search send settings share star sun trash user users video wifi zap. UNDERSCORES, never hyphens. Sizes: size: .row (default, inline), .tile (small/dim), .hero (large). Put the icon the design shows: row chevrons, header bells, search glasses, tab icons.
- For rare marks with no Icon name you may use a unicode glyph inside TextCaption(glyph: "✓") — sparingly, monochrome symbols only, never emoji.
- NEW capabilities you MUST use where the design does: Avatar(text: "TC") — a tinted initials circle for every avatar/person slot (write the initials yourself from the name); Card { ... } for CONTENT cards — the pack's signature indigo gradient (credit cards, hero blocks). When the DESIGN's card is a different colour, name it: Card(tint: .green) { ... } — tint tokens: neutral green pink blue amber violet cyan red (soft pastel fill, ink stays dark). Use Panel for plain sections.
- BUTTONS: `tone: .primary` is ONLY for the screen's ONE dominant CTA (a big filled pill). Every in-row / in-card / repeated button (Follow, Add, View) is a plain compact Chip(text: "Follow") — small, never full-width, never primary.
- CARD GRIDS (contacts, products, features): Grid(cols: 2) { Panel { Col(align: .center, gap: 6) { Avatar(text: "IB") TextRow(text: "Isabelle Barker", width: .fit) TextCaption(text: "Kuala Lumpur", width: .fit) Chip(text: "Follow") } } ... } — one Panel per cell, contents centered.
- Composition tools you MUST use where the design does: Grid(cols: N) for grids; Col(align: .center) for centered stacks; Chip(text: "...") for buttons/CTAs (they render as filled pills in this pack); Row { TextRow(text:.., width: .fill) TextValue(value: "..") } for label-left value-right rows; Rule() for dividers; Field(placeholder: "...") for inputs; Tile for small stat cells inside Grid.
- FILL THE FRAME: the design is a full 375x812 phone screen and the card must own all of it — size media generously, keep lists complete. Space() is a flexible blank that absorbs leftover height, and it is ONLY for what the design shows: ONE before a bar/CTA the design pins at the screen floor, or one above AND below a centered hero on a sparse screen. A dense list/grid screen takes NO Space() at all — never put one between adjacent content sections; a giant vacuum in the middle of content is as wrong as dead space at the end.
- CENTERED HERO SCREENS (onboarding, empty states, success): view root Surface { <top bar if any> Space() Col(align: .center, gap: 10) { <art> <title> <body> } Space() Col(align: .center, width: .fill) { Chip(text: "<cta>", tone: .primary) } } — art, copy and CTA centered, CTA pinned to the bottom. INSIDE a centered Col every text takes width: .fit (a full-width text ignores centering).
- CALENDAR month grid: Grid(cols: 7) { Tile(label: "25", shape: .square) Tile(label: "27", glyph: "•", shape: .square) ... } — every day is one SQUARE Tile; a day with events carries glyph: "•" (or "••"). Weekday initials are a Grid(cols: 7) of TextEyebrow above.
- SECTION BANDS: a full-bleed dark strip with a title (month headers, dark app-bar bands over a light page) is Band(text: "April") — never a Card or Panel.
- CHAT MESSAGES: every message is Bubble(text: "...", side: .them) (left, gray) or Bubble(text: "...", side: .me) (right, accent). Never a Panel or bare text for a message.
- FAB: a round floating action button = Fab(name: .plus) written as a direct child of view root Surface — it renders pinned bottom-right over the page.
- SIZE HONESTY: digest positions and sizes are @2x pixels — HALVE them for screen points. An 88px-tall row is 44pt: ONE compact row. The sizeN on TEXT lines is already in points — never render text visibly larger than the digest says.
- MEDIA SIZES: photo/media grids use SQUARE cells — Thumb(src: pN, shape: .square) inside Grid(cols: 3). A LARGE media area (canvas, illustration panel, hero image, map — anything ≥ a third of the screen) is Thumb(src: pN, shape: .hero) — full-width tall panel. The bare Thumb default is a wide 16:9 list-row tile beside row text. A SMALL leading image in a list row (≤56px in the design) is Avatar initials, never a Thumb.
- APP BAR with a centered title: Row(width: .fill, align: .center) { Icon(name: .chevron_left) Col(width: .fill, align: .center) { TextTitle(text: "<title>", width: .fit) } Icon(name: .more) } — swap the two icons for what the design shows.
- PROPORTION: keep every element at the design's scale. A list row is ONE compact row (Avatar + name/subtitle + a trailing compact Chip or Icon) — an action button inside a row is never full-width. Nothing may eat several design-rows of height.
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
    spec = json.loads((HERE / "specs2" / f"{name}.json").read_text())
    target = HERE / "targets2" / f"{name}.png"
    dig_file = HERE / "cards2" / f"{name}.digest.txt"
    dig_file.write_text(digest(spec))
    mode_hint = "light" if "light" in judge_mode(spec) else "dark"
    hexc, ground = page_colour(spec)
    ground_note = (f"The page background is a COLOUR (#{hexc}) — you MUST write the "
                   f"theme line as `theme atro{'_light' if mode_hint == 'light' else ''} "
                   f"ground {ground}` so the page carries that colour.\n") if ground else ""
    notes = (f"The screen reads as a {mode_hint} screen.\n{limits(spec)}"
             f"{ground_note}{round2_note}")
    prompt = (f"Read {target} — a mobile app screen design to reproduce.\n"
              f"Read {dig_file} — the measured element digest (positions are @2x; "
              f"indentation = the design's own grouping).\n\n{RULES}\n\n{notes}")
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
            + f"\n\n{RULES}\n\n{notes}\n"
            + "Return the corrected FULL card source only — keep the theme "
            + "line's ground/axes exactly as they were.",
            timeout=600)).strip()
        card.write_text(fix + "\n")
        ok, diags = validate(card)
    return ok, diags


GROUNDS = {"teal": (20, 120, 110), "violet": (109, 74, 255), "indigo": (64, 72, 239), "navy": (28, 44, 120),
           "ivory": (248, 244, 232), "sand": (226, 204, 164),
           "terracotta": (196, 88, 58), "wine": (112, 28, 52),
           "forest": (34, 84, 48), "slate": (90, 100, 116), "paper": (244, 244, 240),
           "cream": (250, 242, 222), "midnight": (16, 18, 38),
           "blush": (242, 196, 204), "olive": (112, 112, 60)}


def page_colour(spec):
    """The artboard's dominant fill, and whether it is a CHROMATIC colour."""
    best = (0, None)

    def walk(n):
        nonlocal best
        area = n["w"] * n["h"]
        a = n.get("fill")
        if a and a.get("a", 0) > 0.9 and area > best[0] and area > 200000:
            best = (area, a["hex"].lstrip("#"))
        # A page painted by a GRADIENT fill: take its first stop — the vivid
        # blue Navigation page is exactly this, and the flat-fill walk saw
        # only the dark artboard behind it.
        g = n.get("gradient")
        if g and g.get("stops") and area >= best[0] and area > 200000:
            c = g["stops"][0].get("c") or {}
            if c.get("hex"):
                best = (area, c["hex"].lstrip("#"))
        for c in n.get("children", []):
            walk(c)
    walk(spec)
    if not best[1]:
        return None, None
    r, g, b = (int(best[1][i:i + 2], 16) for i in (0, 2, 4))
    if max(r, g, b) - min(r, g, b) < 40:
        return best[1], None
    tok = min(GROUNDS, key=lambda k: sum((a - b) ** 2 for a, b in zip(GROUNDS[k], (r, g, b))))
    return best[1], tok


def limits(spec):
    """Per-screen measured caps, stated as hard limits in the prompt."""
    tsizes, squares, buttons = [], [], []

    def walk(n):
        t = n.get("text")
        if t and (t.get("string") or "").strip():
            r = t.get("run") or {}
            if r.get("size"):
                tsizes.append(r["size"] / 2)
        w, h = n.get("w", 0), n.get("h", 0)
        if 40 <= w <= 160 and abs(w - h) < 6 and n.get("cls") in ("oval", "bitmap"):
            squares.append(w / 2)
        if "button" in (n.get("name") or "").lower() and h > 0:
            buttons.append((w / 2, h / 2))
        for c in n.get("children", []):
            walk(c)
    walk(spec)
    out = []
    if tsizes:
        out.append(f"the LARGEST text is {max(tsizes):.0f}pt — nothing may render bigger")
    if squares:
        out.append(f"avatars/round images are ~{sorted(squares)[len(squares) // 2]:.0f}pt")
    if buttons:
        w, h = max(buttons, key=lambda b: b[0])
        out.append(f"buttons are ~{h:.0f}pt tall (widest {w:.0f}pt)")
    if not out:
        return ""
    return "MEASURED LIMITS for THIS screen: " + "; ".join(out) + ".\n"


def judge_mode(spec):
    # The single LARGEST opaque fill is the artboard background, and it alone
    # decides. Counting big fills inverted every dark screen full of light
    # cards: one dark background, five white panels, verdict "light".
    best = (0, "dark")

    def walk(n):
        nonlocal best
        a = n.get("fill")
        if a and a.get("a", 0) > 0.9:
            area = n["w"] * n["h"]
            if area > best[0] and area > 200000:
                h = a["hex"].lstrip("#")
                lum = int(h[0:2], 16) + int(h[2:4], 16) + int(h[4:6], 16)
                best = (area, "dark" if lum < 384 else "light")
        for c in n.get("children", []):
            walk(c)
    walk(spec)
    return best[1]


def main():
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else ""
    (HERE / "cards2").mkdir(exist_ok=True)
    feedback = {}
    if "--round2" in sys.argv:
        for l in (HERE / "xrail" / "strict_live4.jsonl").open():
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
