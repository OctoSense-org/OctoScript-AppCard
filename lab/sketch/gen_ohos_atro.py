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
    # ArkUI has no asymmetric page inset, so the top/bottom pair folds into one
    # `pady`. Take it from the THEME (36/24 either side, averaged) rather than
    # the 26 this used to hardcode: 26 top and bottom is 20pt less page than the
    # desktop renders, on every screen, and it reads as the card sitting high in
    # a frame it does not fill.
    s = s.replace("padx: pad_page_x, padtop: pad_page_top, padbottom: pad_page_bot,",
                  "padx: pad_page_x, pady: (pad_page_top + pad_page_bot) / 2, spacing: 12,")
    s = s.replace("padx: pad_page_x, padtop: pad_page_top, padbottom: pad_page_bot, c:",
                  "padx: pad_page_x, pady: (pad_page_top + pad_page_bot) / 2, spacing: 12, c:")
    # bg2 + gradient_across stay: the ArkUI walk paints them as a real
    # linear gradient now (NODE_LINEAR_GRADIENT via the shim).
    for key in ("texture_alpha", "texture_scale", "texture",
                # fitw/fith stay: the ArkUI walk now reads them, and deleting
                # them is what flattened the seven-day list into one row.
                "family", "tracking", "inkdark", "lines",
                "margintop", "marginbottom", "marginx", "padtop", "padbottom"):
        s = re.sub(rf"\b{key}\s*:\s*[^,}}\n]+,?\s*", "", s)
    # A flexible blank grows along a ROW here (that is where the kit uses it);
    # `fillh` alone reads in ArkUI as "be page-tall" and stacks a list's rows
    # on top of each other.
    s = s.replace('fn l0_space() { return {t: "column", fillh: 1} }',
                  'fn l0_space() { return {t: "column", fillw: 1, w: 1} }')
    s = re.sub(r",\s*}", "}", s)
    s = re.sub(r"{\s*,", "{", s)
    # OH overrides, appended so the later definition wins: ArkUI stacks center
    # children by default and percent-fill has no meaning inside them — pages
    # and pin layers take the frame in vp, and ALIGNMENT does the pinning
    # (aligny on a fixed-height column justifies its children to top/center/end).
    s += """

// `align: .center` on a ROW centres its children along the row too.
//
// The shared kit reads it as cross-axis only, which on makepad still looks
// centred because a Label there defaults to Fill and three of them split the
// row into thirds. An ArkUI text node hugs its content instead, so the same
// row left-aligned: the three readings under a centred hero sat jammed against
// the page margin. Setting the main axis as well says what the card meant.
fn l0_aligned(node, how) {
    if how == "center" {
        node.alignx = 0.5
        if node.t == "row" { node.aligny = 0.5 }
    }
    if how == "end" {
        if node.t == "row" { node.aligny = 1.0 } else { node.alignx = 1.0 }
    }
    return node
}

// A weather icon, drawn.
//
// The shared kit returns {t: "weathericon", variant: <cond>} and leaves the
// drawing to a backend that has a vector for it. The ArkUI walk has no
// `variant` arm at all, so this retagged to a bare 34x34 column: the row kept
// a gap where the icon belonged and drew nothing, on every forecast row of
// every weather screen. The desktop rail draws all eight.
//
// The device already has a whole Font Awesome solid face registered for
// `icon: 1` (1966 codepoints, resources/rawfile/fonts/fa-solid-900.ttf), and
// `l0_icon` reaches it. So the condition WORD picks a glyph and the icon goes
// down the path that already works, which also means the card's ink plane
// recolours it like any other text.
fn _wx_glyph(cond) {
    if cond == "Clear" { return "" }
    if cond == "Mainly clear" { return "" }
    if cond == "Partly cloudy" { return "" }
    if cond == "Overcast" { return "" }
    if cond == "Fog" { return "" }
    if cond == "Drizzle" { return "" }
    if cond == "Freezing drizzle" { return "" }
    if cond == "Rain" { return "" }
    if cond == "Heavy rain" { return "" }
    if cond == "Freezing rain" { return "" }
    if cond == "Showers" { return "" }
    if cond == "Heavy showers" { return "" }
    if cond == "Snow" { return "" }
    if cond == "Heavy snow" { return "" }
    if cond == "Snow grains" { return "" }
    if cond == "Snow showers" { return "" }
    if cond == "Thunderstorm" { return "" }
    return ""
}
fn l0_weathericon(cond, size) {
    let g = _wx_glyph(cond)
    if size == "hero" { return {t: "text", text: g, icon: 1, size: font_title * 2.0,
                                color: l0_text, fitw: 1, fith: 1} }
    if size == "tile" { return {t: "text", text: g, icon: 1, size: font_caption * 1.4,
                                color: l0_dim, fitw: 1, fith: 1} }
    return {t: "text", text: g, icon: 1, size: font_value * 3.1,
            color: l0_text, fitw: 1, fith: 1}
}

fn l0_surface(kids) {
    // A scroll, not a fixed box: a card taller than the viewport was being
    // clamped to 830 and its lower sections squeezed out. ArkUI scrolls what
    // overflows; the page keeps the frame width and its own background.
    // `spread`: the desktop harness stretches a card to fill its design frame,
    // and nothing here did — a page shorter than the frame left the rest of the
    // screen blank (62% against the desktop's 88% on the weather card). The
    // leftover height goes into the gaps between sections instead. A page that
    // already overflows is unaffected.
    // NOT spread to fill the frame. The renderer has `spread` (ArkUI
    // SPACE_BETWEEN) and it works — measured here, it pushed the page's three
    // sections to the extremes, opened a void the height of the hero between
    // the readings and the forecast, and drove the stat tiles under the gesture
    // bar. The desktop rail's fill is a PROPORTIONAL stretch of paddings and
    // media, not a maximal spread, and nothing here implements that yet. A page
    // at its natural height reads better than one pulled apart, so the slack
    // stays at the bottom until the stretch exists.
    return {t: "scroll", w: 402, h: 830, bg: l0_base, align: 1, c: [
        {t: "column", w: 402, bg: l0_base,
         padx: pad_page_x, pady: (pad_page_top + pad_page_bot) / 2, spacing: 12, c: kids}
    ]}
}
fn l0_surface_layer(kids, y) {
    return {t: "column", w: 402, h: 830, aligny: y,
            padx: pad_page_x, pady: (pad_page_top + pad_page_bot) / 2, spacing: 12, c: kids}
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
         padx: pad_page_x, pady: (pad_page_top + pad_page_bot) / 2, c: [fab]}]}
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


def data_lets(snapshot: dict, card: str, live: bool = True) -> str:
    """Answer the card's `sys.*` calls — from the network, or from a snapshot.

    The lowering emits real calls (`sys.weather(sys.geocodenum("上海","lat"),
    .., "current.temperature_2m")`). With `live` the shims forward them to the
    device's own capabilities (`fetch_num`/`fetch_fmt`/`fetch_weekday`, which
    fetch and cache open-meteo just as the weather kit does), so the phone
    holds real data with no workstation in the loop. Without it they read a
    snapshot taken on the host — a fallback for capture runs with no network.

    Both forms keep the §4 boundary: the card names WHERE to look, never what
    was found.
    """
    import json as _json
    place = snapshot.get("place", {})
    lat, lon = place.get("lat", 0), place.get("lon", 0)
    if live:
        query = ("&current=temperature_2m,relative_humidity_2m,apparent_temperature,"
                 "weather_code,wind_speed_10m"
                 "&daily=weather_code,temperature_2m_max,temperature_2m_min,uv_index_max"
                 "&timezone=auto&forecast_days=7")
        news_url = "https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=10"
        return f"""
// --- live data: the device fetches, exactly as the weather kit does ---
let _NEWS = "{news_url}"

// The coordinate is resolved ON THE DEVICE from the name the card states, and
// the data URL is built from what comes back.
//
// It used to be written in here from a snapshot taken on the workstation, and
// when a regeneration ran without one the pair silently defaulted to 0,0 — so
// the phone fetched the Gulf of Guinea while the card said 上海, and a week of
// ocean weather (every day 24.5°-25.4°) looked entirely plausible on screen.
// Nothing about that is visible in a screenshot; only the URL says it.
fn _wx(lat, lon) {{
    return "https://api.open-meteo.com/v1/forecast?latitude=" + lat
         + "&longitude=" + lon + "{query}"
}}
fn sys_geocodenum(name, which) {{
    if which == "lat" {{ return geocodenum(name, "lat") }}
    return geocodenum(name, "lon")
}}
// Day 0 is "Now", as the makepad rail's own `sys.weather` answers it. The
// content-parity check found this: same card, same fixture, one rail said
// "Sat" where the other said "Now", and no pixel gate can see a divergence
// like that because both screens look entirely correct.
fn sys_dayname(lat, lon, i) {{
    if i == 0 {{ return "Now" }}
    return fetch_weekday(_wx(lat, lon), "daily.time", i)
}}
// A miss is NOT zero. `return 0` here made a failed fetch indistinguishable
// from a real 0 degrees, a real 0% humidity, a real 0 UV — the screen showed a
// number, the number was wrong, and nothing anywhere said so. "--" is what
// `net.rs::fetch_fmt` already answers for an absent field, so a miss now reads
// as a miss on the screen and in the empty-value count.
fn sys_weather(lat, lon, path) {{
    let v = fetch_num(_wx(lat, lon), path, -1)
    if v == nil {{ return "--" }}
    // Rounded, because the makepad rail's `sys.weather` rounds and one card
    // must read the same on both. Raw API values put "30.2 °" beside the other
    // rail's "30 °" on every temperature of every weather screen.
    return mod.math.round(v)
}}
// A WMO code is a NUMBER; every consumer of it wants a word. Without this the
// forecast rows carried "51" and the headline condition line read "3".
fn _wmo(c) {{
    if c == "--" {{ return "Unknown" }}
    if c == 0 {{ return "Clear" }}
    if c == 1 {{ return "Mainly clear" }}
    if c == 2 {{ return "Partly cloudy" }}
    if c == 3 {{ return "Overcast" }}
    if c == 45 {{ return "Fog" }}
    if c == 48 {{ return "Fog" }}
    if c == 51 {{ return "Drizzle" }}
    if c == 53 {{ return "Drizzle" }}
    if c == 55 {{ return "Drizzle" }}
    if c == 56 {{ return "Freezing drizzle" }}
    if c == 57 {{ return "Freezing drizzle" }}
    if c == 61 {{ return "Rain" }}
    if c == 63 {{ return "Rain" }}
    if c == 65 {{ return "Heavy rain" }}
    if c == 66 {{ return "Freezing rain" }}
    if c == 67 {{ return "Freezing rain" }}
    if c == 71 {{ return "Snow" }}
    if c == 73 {{ return "Snow" }}
    if c == 75 {{ return "Heavy snow" }}
    if c == 77 {{ return "Snow grains" }}
    if c == 80 {{ return "Showers" }}
    if c == 81 {{ return "Showers" }}
    if c == 82 {{ return "Heavy showers" }}
    if c == 85 {{ return "Snow showers" }}
    if c == 86 {{ return "Snow showers" }}
    if c == 95 {{ return "Thunderstorm" }}
    if c == 96 {{ return "Thunderstorm" }}
    if c == 99 {{ return "Thunderstorm" }}
    return "Unknown"
}}
fn sys_weathercond(lat, lon, path) {{ return _wmo(sys_weather(lat, lon, path)) }}
fn sys_weatherword(lat, lon, path) {{ return _wmo(sys_weather(lat, lon, path)) }}
// The lowering emits `sys.news(<index>, "<field>")` — the story's index first.
// Reading that first argument as a COUNT left the real index nil, and every
// headline on the page fetched nothing.
//
// Two of the six field names the card may ask for are not the names the API
// answers to. Forwarding them verbatim returned nil, and a nil in a text slot
// is a node that draws nothing — so the comment count was absent from every
// row while the row itself looked complete.
fn _news_field(f) {{
    if f == "comments" {{ return "num_comments" }}
    if f == "id" {{ return "objectID" }}
    return f
}}
fn sys_news(i, field) {{ return fetch_str(_NEWS, "hits#" + _news_field(field), i) }}
"""
    now = snapshot.get("now", {})
    week = snapshot.get("week", {}).get("days", [])
    top = snapshot.get("top", [])
    unrolled = "\n".join(
        f'    if path == "daily.temperature_2m_max.{i}" {{ return _hi[{i}] }}\n'
        f'    if path == "daily.temperature_2m_min.{i}" {{ return _lo[{i}] }}\n'
        f'    if path == "daily.weather_code.{i}" {{ return _cond[{i}] }}'
        for i in range(7))
    return f"""
// --- snapshot fallback: real values, taken once on the host ---
let _hi = {_json.dumps([d.get("hi", 0) for d in week])}
let _lo = {_json.dumps([d.get("lo", 0) for d in week])}
let _dayname = {_json.dumps([d.get("dayname", "") for d in week])}
let _cond = {_json.dumps([d.get("cond", "") for d in week])}
let _news = {_json.dumps(top, ensure_ascii=False)}
fn sys_geocodenum(name, which) {{
    if which == "lat" {{ return {lat} }}
    return {lon}
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
{unrolled}
    return 0
}}
fn sys_weathercond(lat, lon, path) {{ return sys_weather(lat, lon, path) }}
fn sys_weatherword(lat, lon, path) {{ return sys_weather(lat, lon, path) }}
fn sys_news(i, field) {{ return _news[i][field] }}
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
