#!/usr/bin/env python3
"""Assemble the 15 L0 cards into self-contained Splash-OH sources.

The ArkUI backend evals plain splash and walks the returned node map — same
chain as the makepad host, minus the host: no argb builtin, no state runtime,
no gradient/texture/asymmetric-inset attrs, real-point font sizes. So each
card becomes ONE source: argb polyfill + state initials as lets + palette +
ground axis + derivation + a dialect-adapted kit + the lowered call tree,
wrapped in a tap-to-advance overlay.
"""
import json
import pathlib
import re
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
L0 = pathlib.Path.home() / "home/octos-one/splash-makepad/components/l0"
SPLASH = pathlib.Path.home() / "home/Splash"
OH = pathlib.Path.home() / "home/Splash-OH/crates/splash-oh-native"
NAMES = ["Stats_Cards", "Settings_Choose_Country", "Shop_View_12", "Social_Feed_1",
         "Social_Contacts_2", "Shop_View_18", "Email_Mail_View_1", "Chat_Doodle_Pad",
         "Alerts_View_2", "Navigation_View_9", "Onboarding_View_2", "Calendar_View_3",
         "Profile_View_6", "Calendar_View_4", "Photo_Gallery_Selection"]

POLYFILL = """fn argb(a, r, g, b) { return ((a * 256 + r) * 256 + g) * 256 + b }
"""

# Real points ≈ makepad units / 1.61 — the kit's scale is makepad-calibrated,
# ArkUI fp are true points, so sizes go back UP by the same factor.
FONT_VARS = ["font_caption", "font_row", "font_body", "font_value", "font_title"]


def adapt(kit: str) -> str:
    """The OH dialect: retag what the walk doesn't know, drop what it ignores,
    fold asymmetric insets into what it has."""
    s = kit
    # Retag everything the ArkUI walk does not know to its closest native:
    # boxes to column, decorated text to text. The data-viz tags never occur
    # in these cards but their kit fns exist, so map them too.
    for tag in ("card", "divider", "grid", "chip", "weathericon", "tempbar",
                "sunarc", "moonphase", "stockplot", "indicatorplot",
                "aqicontour", "satellite", "navmap", "map", "listitem"):
        s = s.replace(f't: "{tag}"', 't: "column"')
    s = s.replace('t: "eyebrow"', 't: "text"')
    # page insets: top/bottom pair -> symmetric pady; page columns gain the
    # spacing that panel margintop used to provide
    s = s.replace("padx: pad_page_x, padtop: pad_page_top, padbottom: pad_page_bot,",
                  "padx: pad_page_x, pady: 26, spacing: 12,")
    s = s.replace("padx: pad_page_x, padtop: pad_page_top, padbottom: pad_page_bot, c:",
                  "padx: pad_page_x, pady: 26, spacing: 12, c:")
    for key in ("bg2", "gradient_across", "texture_alpha", "texture_scale", "texture",
                "family", "tracking", "fitw", "fith", "inkdark", "lines",
                "margintop", "marginbottom", "marginx", "padtop", "padbottom"):
        s = re.sub(rf"\b{key}\s*:\s*[^,}}\n]+,?\s*", "", s)
    s = re.sub(r",\s*}", "}", s)
    s = re.sub(r"{\s*,", "{", s)
    return s


IMG_DIR = pathlib.Path("/private/tmp/claude-501/-Users-user-home-Splash/"
                       "df6c4ec5-2002-4e8f-84de-7d846576918e/scratchpad/atro/src/images")


def data_uri(url: str) -> str:
    """The tunnel URL becomes the file itself: ArkUI Image takes base64 data
    URIs, and a self-contained source beats a reverse-port dependency."""
    import base64
    name = url.rsplit("/", 1)[-1]
    p = IMG_DIR / name
    if not p.exists():
        return url
    mime = "image/png" if name.endswith(".png") else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()


def state_lets(card: str) -> str:
    out = []
    for m in re.finditer(r"state\s+(\w+)\s*{[^}]*initial:\s*(\"[^\"]*\"|[\d.]+|\.\w+)", card):
        v = m.group(2)
        if v.startswith("."):
            v = f'"{v[1:]}"'
        if v.startswith('"http://127.0.0.1:8787/'):
            v = '"' + data_uri(v.strip('"')) + '"'
        out.append(f"let {m.group(1)} = {v}")
    return "\n".join(out)


def lower(card_path: pathlib.Path) -> str:
    r = subprocess.run(
        ["cargo", "run", "-q", "-p", "splash-ui-l0", "--example", "lower_kit",
         "--", str(card_path), str(HERE / "xrail2" / "data.json")],
        capture_output=True, text=True, cwd=SPLASH)
    if r.returncode != 0:
        raise SystemExit(f"lower failed for {card_path.name}: {r.stderr[:300]}")
    return r.stdout


TOKENS = ["l0_base", "l0_base_2", "l0_fill", "l0_sheet", "l0_hairline",
          "l0_stroke", "l0_active", "l0_bar_rail", "l0_text", "l0_soft",
          "l0_dim", "l0_accent", "l0_bar", "l0_go", "l0_scrim_top", "l0_scrim",
          "l0_card_1", "l0_card_2", "l0_grad_across", "l0_texture_a"]


def flatten_palette(parts: str) -> str:
    """Evaluate the derivation host-side and rebind every colour token as a
    literal — the device VM lacks some math builtin, and a nil seed-derived
    colour un-paints the whole screen while the layout stays live."""
    # Top-level lets are not in scope inside a bare trailing map literal —
    # only inside fns — so the probe returns its tree from one.
    # Dialect rules, measured: the final value must be a MAP LITERAL, and
    # top-level lets resolve only inside fn bodies — so the rows come from a
    # fn and the root is a literal that calls it.
    probe_kids = ",\n".join(
        f'    atok("{t}", {t})' for t in TOKENS)
    probe = (f"{parts}\n"
             'fn atok(s, c) { return {t: "text", text: s, color: c} }\n'
             "fn arows() {\n"
             "  return [\n" + probe_kids + "\n]\n"
             "}\n"
             '{t: "column", c: arows()}\n')
    tmp = pathlib.Path("/tmp/_flattenaprobe.splash")
    tmp.write_text(probe)
    r = subprocess.run(
        ["cargo", "run", "-q", "-p", "splash-oh-native", "--example", "evalnode",
         "--", str(tmp)],
        capture_output=True, text=True,
        cwd=pathlib.Path.home() / "home/Splash-OH")
    out = {}
    for line in r.stdout.splitlines():
        if line.startswith("TOKEN "):
            _, name, hexv = line.split()
            out[name] = int(hexv, 16)
    missing = [t for t in TOKENS if t not in out]
    if missing:
        raise SystemExit(f"flatten failed, missing {missing}: {r.stdout[:300]}")
    return "\n".join(f"let {t} = {v}" for t, v in out.items())


def main():
    base = (L0 / "_palette_dark.splash").read_text()
    deltas = {"atro": (L0 / "_palette_atro.splash").read_text(),
              "atro_light": (L0 / "_palette_atro_light.splash").read_text()}
    derive_color = (L0 / "_derive_color.splash").read_text()
    derive = (L0 / "_derive.splash").read_text()
    kit = adapt((L0 / "_kit.splash").read_text())
    rescale = "\n".join(f"let {v} = {v} * 1.61" for v in FONT_VARS)

    out_dir = OH / "assets" / "atro"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for i, name in enumerate(NAMES):
        card_path = HERE / "cards2" / f"{name}.card"
        card = card_path.read_text()
        mood = "atro_light" if "theme atro_light" in card else "atro"
        ground = ""
        g = re.search(r"ground:\s*\.(\w+)", card)
        if g:
            ground = (L0 / f"_axis_ground_{g.group(1)}.splash").read_text()
        tree = lower(card_path).strip()
        tree = re.sub(r"l0_hero\(([^,]+), (\d+(?:\.\d+)?)\)",
                      lambda m: f"l0_hero({m.group(1)}, {float(m.group(2)) * 1.61:.1f})",
                      tree)
        nxt = f"atro/{(i + 1) % len(NAMES)}"
        # ArkUI measures an unconstrained slot to its content, and percent
        # sizing inside it collapses to zero — the catalog kit pins the page
        # in vp for the same reason. 402x830 is this display's near-full frame.
        chain = (f"{POLYFILL}\n{base}\n{deltas[mood]}\n{ground}\n"
                 f"{derive_color}\n{derive}")
        flat = flatten_palette(chain)
        src = (f"{POLYFILL}\n{state_lets(card)}\n{chain}\n{flat}\n{rescale}\n{kit}\n"
               f'{{t: "stack", w: 402, h: 830, c: [\n{tree},\n'
               f'  {{t: "column", h: 34, fillw: 1, tapto: {json.dumps(nxt)}}}\n]}}\n')
        (out_dir / f"{name}.splash").write_text(src)
        rows.append(f'    ("{name}", include_str!("../assets/atro/{name}.splash")),')
        print(f"{name}: {len(src) // 1000}KB mood={mood}{' +ground' if ground else ''}")

    gen = (OH / "src" / "atro_screens.rs")
    gen.write_text(
        "// GENERATED by octos-one/lab/sketch/gen_ohos_atro.py — do not edit.\n"
        "/// The 15 Atro fidelity screens, assembled for the ArkUI walk.\n"
        "pub const ATRO_SCREENS: &[(&str, &str)] = &[\n" + "\n".join(rows) + "\n];\n")
    print(f"wrote {gen}")


if __name__ == "__main__":
    main()
