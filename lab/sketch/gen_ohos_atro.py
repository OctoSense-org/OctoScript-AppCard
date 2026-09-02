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
    s = s.replace('t: "card"', 't: "column"')
    s = s.replace('t: "divider"', 't: "column"')
    s = s.replace('t: "grid"', 't: "column"')
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


def state_lets(card: str) -> str:
    out = []
    for m in re.finditer(r"state\s+(\w+)\s*{[^}]*initial:\s*(\"[^\"]*\"|[\d.]+|\.\w+)", card):
        v = m.group(2)
        if v.startswith("."):
            v = f'"{v[1:]}"'
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
        src = (f"{POLYFILL}\n{state_lets(card)}\n{base}\n{deltas[mood]}\n{ground}\n"
               f"{derive_color}\n{derive}\n{rescale}\n{kit}\n"
               f'{{t: "stack", fillw: 1, fillh: 1, c: [\n{tree},\n'
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
