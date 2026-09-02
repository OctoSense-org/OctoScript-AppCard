#!/usr/bin/env python3
"""Mint a theme PACK (dark + light mood deltas) from a kit's specs.

The measured recipe that produced the Atro pack, scripted: cluster screens by
page luminance, take the dominant ground/ink/accent per mode, panel lift from
the E4 ratios, type scale from the text runs (makepad calibration 0.62 baked
in), radius from the panel median, gradient from the most-reused two-stop
fill. Writes `_palette_<theme>.splash` and `_palette_<theme>_light.splash`
into splash-makepad's l0 components, in the same token surface as the Atro
pack — register with register_pack.py afterwards.

Usage: spec2pack.py --kit <name>
"""
import collections
import json
import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import kitconf  # noqa: E402

MK = pathlib.Path.home() / "home/octos-one/splash-makepad/components/l0"


def rgb(hexs):
    h = hexs.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(c):
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def sat(c):
    return max(c) - min(c)


def harvest(spec, acc):
    def walk(n):
        f = n.get("fill")
        area = n.get("w", 0) * n.get("h", 0)
        if f and f.get("a", 1) > 0.9 and area > 200000:
            acc["grounds"].append((area, rgb(f["hex"])))
        if f and f.get("a", 1) > 0.9 and sat(rgb(f["hex"])) > 60 and 400 < area < 400000:
            acc["accents"].append(rgb(f["hex"]))
        g = n.get("gradient")
        if g and g.get("stops") and len(g["stops"]) >= 2 and area > 20000:
            stops = tuple(g["stops"][i]["c"]["hex"] for i in (0, -1))
            acc["grads"][stops] += 1
        t = n.get("text")
        if t and (t.get("string") or "").strip():
            r = t.get("run") or {}
            if r.get("size"):
                acc["sizes"].append(r["size"] / 2)
            if r.get("color"):
                acc["inks"].append(rgb(r["color"]))
        if (n.get("cls") == "rectangle" and n.get("radius", 0) > 0
                and n.get("w", 0) > 120):
            acc["radii"].append(n["radius"] / 2)
        for c in n.get("children", []):
            walk(c)
    walk(spec)


def med_rgb(colors):
    if not colors:
        return (128, 128, 128)
    return tuple(int(statistics.median(c[i] for c in colors)) for i in range(3))


def delta(theme, mode, ground, ink, accent, sizes, radii, grad, family="geometric"):
    g, base2 = ground, tuple(min(255, c + (14 if lum(ground) < 128 else -8)) for c in ground)
    lift = 1 if lum(ground) < 128 else -1
    step = lambda k: tuple(max(0, min(255, c + lift * k)) for c in g)
    p50 = statistics.median(sizes) if sizes else 11
    base = max(6, round(p50 * 0.62))
    rad = statistics.median(radii) if radii else 12
    lines = [
        f"// The {theme} pack ({mode} mode), minted by lab/sketch/spec2pack.py.",
        f"let l0_base     = argb(255, {g[0]}, {g[1]}, {g[2]})",
        f"let l0_base_2   = argb(255, {base2[0]}, {base2[1]}, {base2[2]})",
        f"let l0_sheet    = argb(255, {', '.join(map(str, step(8)))})",
        f"let l0_fill     = argb(255, {', '.join(map(str, step(12)))})",
        f"let l0_hairline = argb(255, {', '.join(map(str, step(33)))})",
        f"let l0_stroke   = argb(255, {', '.join(map(str, step(43)))})",
        f"let l0_active   = argb(255, {accent[0]}, {accent[1]}, {accent[2]})",
        f"let l0_bar_rail = argb(255, {', '.join(map(str, step(38)))})",
        f"let l0_text     = argb(255, {ink[0]}, {ink[1]}, {ink[2]})",
        f"let l0_soft     = argb(255, {', '.join(str(min(255, max(0, int(i + (g_ - i) * 0.1)))) for i, g_ in zip(ink, g))})",
        f"let l0_dim      = argb(255, {', '.join(str(min(255, max(0, int(i + (g_ - i) * 0.33)))) for i, g_ in zip(ink, g))})",
        "let icon_mono   = 1",
        f"let l0_accent   = argb(255, {accent[0]}, {accent[1]}, {accent[2]})",
        "let l0_bar      = l0_accent",
        "let l0_go       = l0_accent",
        f"let l0_scrim_top = argb(60, {g[0]}, {g[1]}, {g[2]})",
        f"let l0_scrim     = argb(242, {g[0]}, {g[1]}, {g[2]})",
        "",
        f"// measured type: p50 {p50:.0f}pt -> makepad base {base} (x0.62 calibration)",
        f"let font_base     = {base}",
        "let font_step     = 1",
        "let hero_factor   = 1.45",
        f"let radius_factor = {min(1.4, max(0.4, rad / 14)):.2f}",
        f'let l0_family         = "{family}"',
        f'let l0_display_family = "{family}"',
    ]
    if grad:
        c1, c2 = rgb(grad[0]), rgb(grad[1])
        lines += [
            "",
            "// the kit's most-reused two-stop gradient — content cards take it",
            f"let l0_card_1 = argb(255, {c1[0]}, {c1[1]}, {c1[2]})",
            f"let l0_card_2 = argb(255, {c2[0]}, {c2[1]}, {c2[2]})",
        ]
    return "\n".join(lines) + "\n"


def main():
    kit = kitconf.load(sys.argv[sys.argv.index("--kit") + 1])
    dark = collections.defaultdict(list) | {"grads": collections.Counter()}
    light = collections.defaultdict(list) | {"grads": collections.Counter()}
    for p in sorted(kit["specs_dir"].glob("*.json")):
        spec = json.loads(p.read_text())
        acc = collections.defaultdict(list) | {"grads": collections.Counter()}
        harvest(spec, acc)
        page = max(acc["grounds"], default=(0, (255, 255, 255)))[1]
        dst = dark if lum(page) < 128 else light
        for k in ("grounds", "accents", "sizes", "inks", "radii"):
            dst[k].extend(acc[k])
        dst["grads"].update(acc["grads"])

    out = {}
    for mode, acc, name in (("dark", dark, kit["theme"]),
                            ("light", light, kit["theme_light"])):
        if not acc["grounds"]:
            print(f"{mode}: no screens in this mode; skipping")
            continue
        ground = med_rgb([g for _, g in acc["grounds"]])
        ink = med_rgb([i for i in acc["inks"]
                       if abs(lum(i) - lum(ground)) > 80]) if acc["inks"] else (
            (255, 255, 255) if lum(ground) < 128 else (20, 20, 24))
        accent = med_rgb([a for a in acc["accents"] if sat(a) > 80] or acc["accents"])
        grad = acc["grads"].most_common(1)[0][0] if acc["grads"] else None
        src = delta(name, mode, ground, ink, accent, acc["sizes"], acc["radii"], grad)
        path = MK / f"_palette_{name}.splash"
        path.write_text(src)
        out[mode] = path
        print(f"{mode}: {path.name}  ground {ground} ink {ink} accent {accent}")
    if len(out) < 2:
        sys.exit("a pack needs both moods — check the kit's specs")


if __name__ == "__main__":
    main()
