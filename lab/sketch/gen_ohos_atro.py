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

import sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import kitconf
L0 = pathlib.Path.home() / "home/octos-one/splash-makepad/components/l0"
SPLASH = pathlib.Path(__file__).resolve().parents[2] / "splash"
OH = pathlib.Path.home() / "home/Splash-OH/crates/splash-oh-native"
KIT = kitconf.load(sys.argv[sys.argv.index("--kit") + 1]
                   if "--kit" in sys.argv else "atro")
NAMES = KIT["screens"]

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
    # OH overrides, appended so the later definition wins: ArkUI stacks center
    # children by default and percent-fill has no meaning inside them — pages
    # and pin layers take the frame in vp, and ALIGNMENT does the pinning
    # (aligny on a fixed-height column justifies its children to top/center/end).
    s += """

fn l0_surface(kids) {
    return {t: "column", w: 402, h: 830, bg: l0_base,
            padx: pad_page_x, pady: 26, spacing: 12, c: kids}
}
fn l0_surface_layer(kids, y) {
    return {t: "column", w: 402, h: 830, aligny: y,
            padx: pad_page_x, pady: 26, spacing: 12, c: kids}
}
fn l0_surface_pin2(top, bottom) {
    return {t: "stack", w: 402, h: 830, align: 1, bg: l0_base,
            c: [l0_surface_layer(top, 0), l0_surface_layer(bottom, 1)]}
}
fn l0_surface_pin3(top, mid, bottom) {
    return {t: "stack", w: 402, h: 830, align: 1, bg: l0_base,
            c: [l0_surface_layer(top, 0), l0_surface_layer(mid, 0.5),
                l0_surface_layer(bottom, 1)]}
}
fn l0_surface_fab(page, fab) {
    return {t: "stack", w: 402, h: 830, align: 1, c: [page,
        {t: "column", w: 402, h: 830, alignx: 1, aligny: 1,
         padx: pad_page_x, pady: 26, c: [fab]}]}
}
"""
    return s


IMG_DIR = None  # resolved from the kit config in main()


def data_uri(url: str) -> str:
    """The tunnel URL becomes the file itself: ArkUI Image takes base64 data
    URIs, and a self-contained source beats a reverse-port dependency."""
    import base64
    name = url.rsplit("/", 1)[-1]
    p = pathlib.Path(KIT["img_dir"]) / name
    if not p.exists():
        return url
    mime = "image/png" if name.endswith(".png") else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()


def data_lets(snapshot: dict, card: str) -> str:
    """Answer the card's live `sys.*` calls from a REAL data snapshot.

    The lowering emits actual calls (`sys.weather(sys.geocodenum("上海",
    "lat"), .., "current.temperature_2m")`), not variable reads — binding the
    source names as lets does nothing. The ArkUI assembler has no runtime to
    execute those calls, so unanswered ones render `[Error:WrongValue]`.
    These shims give the same tree the numbers the phone runtime would have
    fetched: one snapshot, taken live, keyed by the open-meteo field path the
    lowering asks for.
    """
    import json as _json
    now = snapshot.get("now", {})
    week = snapshot.get("week", {}).get("days", [])
    top = snapshot.get("top", [])
    place = snapshot.get("place", {})
    hi = _json.dumps([d.get("hi", 0) for d in week])
    lo = _json.dumps([d.get("lo", 0) for d in week])
    names = _json.dumps([d.get("dayname", "") for d in week])
    conds = _json.dumps([d.get("cond", "") for d in week])
    unrolled = "\n".join(
        f'    if path == "daily.temperature_2m_max.{i}" {{ return _hi[{i}] }}\n'
        f'    if path == "daily.temperature_2m_min.{i}" {{ return _lo[{i}] }}\n'
        f'    if path == "daily.weather_code.{i}" {{ return _cond[{i}] }}'
        for i in range(7))
    return f"""
// --- live-data shims: a snapshot answers what the runtime would fetch ---
let _hi = {hi}
let _lo = {lo}
let _dayname = {names}
let _cond = {conds}
let _news = {_json.dumps(top, ensure_ascii=False)}
fn sys_geocodenum(name, which) {{
    if which == "lat" {{ return {place.get("lat", 0)} }}
    return {place.get("lon", 0)}
}}
fn sys_dayname(lat, lon, i) {{ return _dayname[i] }}
fn sys_weather(lat, lon, path) {{
    if path == "current.temperature_2m" {{ return {now.get("temp", 0)} }}
    if path == "current.apparent_temperature" {{ return {now.get("feels", 0)} }}
    if path == "current.relative_humidity_2m" {{ return {now.get("humidity", 0)} }}
    if path == "current.wind_speed_10m" {{ return {now.get("wind", 0)} }}
    if path == "current.uv_index" {{ return {now.get("uv", 0)} }}
    if path == "daily.uv_index_max.0" {{ return {now.get("uv", 0)} }}
    if path == "current.weather_code" {{ return "{now.get("cond", "")}" }}
    let d0 = ""
{unrolled}
    return 0
}}
fn sys_news(count, field, i) {{ return _news[i][field] }}
fn sys_weathercond(lat, lon, path) {{ return sys_weather(lat, lon, path) }}
fn sys_weatherword(lat, lon, path) {{ return sys_weather(lat, lon, path) }}
"""


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


def emit_themed(name, card_path, snapshot, out_dir):
    """Device-assembled form: the card's own source plus its lowered tree.

    The phone splices palette -> delta -> axes -> derivations -> kit itself
    (crates/splash-oh-native/src/theme.rs), so nothing here bakes a colour.
    Only the live-data shims travel with the tree, because the ArkUI path has
    no data runtime.
    """
    card = card_path.read_text()
    tree = lower(card_path).strip()
    # lower_kit ends with a bare `node` line — the makepad host's way of
    # yielding the value it just built. Inside a map literal it is a stray
    # token, and the ArkUI walk reports "unknown node type".
    # lower_kit emits a STATEMENT form: `let node = <expr>` … trailing `node`
    # (the makepad host binds then yields). Inside a map literal only the
    # expression is legal, so strip both ends.
    if tree.endswith("\nnode"):
        tree = tree[: -len("\nnode")].rstrip()
    tree = "\n".join(l for l in tree.splitlines() if not l.startswith("//"))
    tree = tree.lstrip()
    if tree.startswith("let node ="):
        tree = tree[len("let node ="):].lstrip()
    for fn in ("geocodenum", "weathercond", "weatherword", "weather", "dayname", "news"):
        tree = tree.replace(f"sys.{fn}(", f"sys_{fn}(")
    # NO self-rebinding lets (`let font_body = font_body * 1.61`): this VM
    # takes the name as unbound at that point and the whole source evaluates
    # to nothing. The device path rescales inside the kit instead, so the
    # tree file carries data shims and the tree only.
    wrapper = '{t: "stack", w: 402, h: 830, align: 1, c: [\n' + tree + "\n]}\n"
    body = data_lets(snapshot, card) + "\n" + state_lets(card) + "\n" + wrapper
    (out_dir / f"{name}.card.txt").write_text(card)
    (out_dir / f"{name}.tree.splash").write_text(body)
    return card, body


def main():
    base = (L0 / "_palette_dark.splash").read_text()
    deltas = {KIT["theme"]: (L0 / f"_palette_{KIT['theme']}.splash").read_text(),
              KIT["theme_light"]: (L0 / f"_palette_{KIT['theme_light']}.splash").read_text()}
    derive_color = (L0 / "_derive_color.splash").read_text()
    derive = (L0 / "_derive.splash").read_text()
    kit = adapt((L0 / "_kit.splash").read_text())
    rescale = "\n".join(f"let {v} = {v} * 1.61" for v in FONT_VARS)

    out_dir = OH / "assets" / "atro"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for i, name in enumerate(NAMES):
        card_path = KIT["cards_dir"] / f"{name}.card"
        card = card_path.read_text()
        mood = (KIT["theme_light"] if f"theme {KIT['theme_light']}" in card
                else KIT["theme"])
        ground = ""
        g = re.search(r"ground:\s*\.(\w+)", card)
        if g:
            ground = (L0 / f"_axis_ground_{g.group(1)}.splash").read_text()
        tree = lower(card_path).strip()
        # `sys.x(` -> `sys_x(`: the shims above answer them from the snapshot.
        # Only names that have a shim; a blanket rewrite renamed calls
        # (sys.weathercond) onto functions that did not exist.
        for _fn in ("geocodenum", "weathercond", "weatherword", "weather",
                    "dayname", "news"):
            tree = tree.replace(f"sys.{_fn}(", f"sys_{_fn}(")
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
               f'{{t: "stack", w: 402, h: 830, align: 1, c: [\n{tree},\n'
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
