#!/usr/bin/env python3
"""Resolve every name the assembled theme chain reads, before it is evaluated.

The theme is six files spliced into one program and handed to a VM that has no
error channel this side can read. A name the chain never bound does not stop the
render: it yields 0, and 0 is a legal fully transparent colour. So a missing
binding paints nothing and says nothing.

Worse, this VM binds a function's free names when the function is DEFINED. A
`let` written after the kit therefore creates a fresh binding that functions
defined earlier never see — a whole type-rescale block sat in the vendored kit
doing nothing for its entire life, and the only symptom was type that would not
change size.

Both are decidable without running anything:

    python3 lint_theme.py                      # every mood x its own axes
    python3 lint_theme.py --mood camo_light    # one

  UNBOUND   a name is read that nothing in the chain ever binds
  TOO LATE  a name is bound after a function that reads it — the binding is
            inert for that function, whatever it looks like

Deliberately not a parser for the whole language. It tracks `let`/`fn` bindings
and identifier reads in splice order, which is exactly the axis these two
failures live on.
"""
import argparse
import pathlib
import re
import sys

L0 = pathlib.Path.home() / "home/octos-one/splash-makepad/components/l0"

# Names the HOST injects rather than the chain binding: capabilities and VM
# builtins. Reading one is not a missing binding.
HOST_PROVIDED = {
    "argb", "nil", "true", "false", "mod", "sys",
    "fetch_num", "fetch_str", "fetch_fmt", "fetch_weekday", "geocode",
    "geocodenum", "moonphase", "moonnum", "daylight", "weekmin", "weekmax",
    "invoke", "sget", "crate_resource", "http_resource",
}
KEYWORDS = {"let", "fn", "if", "else", "return", "for", "in", "while", "and",
            "or", "not"}

IDENT = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\b")
LET = re.compile(r"^\s*let\s+([A-Za-z_][A-Za-z0-9_]*)\s*=")
FN = re.compile(r"^\s*fn\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(([^)]*)\)")


STRING = re.compile(r'"(?:[^"\\]|\\.)*"')
# A name is a READ only when it is neither a map key (`text:`) nor a member
# (`mod.math.round`). Counting those made every node literal in the kit look
# like a hundred missing bindings and buried the two real ones.
KEY_OR_MEMBER = re.compile(
    r'(?:\.\s*[A-Za-z_][A-Za-z0-9_]*)|(?:\b[A-Za-z_][A-Za-z0-9_]*\s*:)')


def readable(line: str) -> str:
    """The part of a line where an identifier would be a free-name READ."""
    line = STRING.sub(' "" ', line)
    return KEY_OR_MEMBER.sub(" ", line)


def strip_comments(src: str) -> str:
    return "\n".join(l.split("//")[0] for l in src.splitlines())


def scan(chain: list) -> list:
    """(file, lineno, kind, name) events in splice order."""
    events = []
    for fname, src in chain:
        in_fn, depth, fn_name, fn_params, fn_start = False, 0, "", set(), 0
        for i, line in enumerate(strip_comments(src).splitlines(), 1):
            m = FN.match(line)
            if m and not in_fn:
                in_fn, fn_name, fn_start = True, m.group(1), i
                fn_params = {p.strip() for p in m.group(2).split(",") if p.strip()}
                events.append((fname, i, "bindfn", fn_name))
                depth = line.count("{") - line.count("}")
                # a one-line fn body
                body = line[line.index("{") + 1:] if "{" in line else ""
                for name in IDENT.findall(readable(body)):
                    if name not in KEYWORDS and name not in fn_params:
                        events.append((fname, i, f"read@{fn_name}", name))
                if depth <= 0:
                    in_fn = False
                continue
            if in_fn:
                depth += line.count("{") - line.count("}")
                locals_here = LET.match(line)
                if locals_here:
                    fn_params.add(locals_here.group(1))
                for name in IDENT.findall(readable(line)):
                    if name not in KEYWORDS and name not in fn_params:
                        events.append((fname, fn_start, f"read@{fn_name}", name))
                if depth <= 0:
                    in_fn = False
                continue
            m = LET.match(line)
            if m:
                rhs = line.split("=", 1)[1]
                for name in IDENT.findall(readable(rhs)):
                    if name not in KEYWORDS:
                        events.append((fname, i, "read", name))
                events.append((fname, i, "bind", m.group(1)))
                continue
            for name in IDENT.findall(readable(line)):
                if name not in KEYWORDS:
                    events.append((fname, i, "read", name))
    return events


def lint(chain: list) -> list:
    """UNBOUND and TOO LATE findings for one assembled chain."""
    events = scan(chain)
    bound_at, bind_kind = {}, {}
    for i, (f, ln, kind, name) in enumerate(events):
        if kind in ("bind", "bindfn"):
            if name not in bound_at:
                bound_at[name], bind_kind[name] = i, kind

    out, seen = [], set()
    for i, (f, ln, kind, name) in enumerate(events):
        if kind in ("bind", "bindfn") or name in HOST_PROVIDED or (kind, name) in seen:
            continue
        first = bound_at.get(name)
        if first is None:
            out.append(("UNBOUND", f, ln, name, kind))
            seen.add((kind, name))
        elif first > i and bind_kind[name] == "bind":
            # A read before the binding, for a `let`. Asked on the device (the
            # boot selftest logs the answer): this VM resolves a FUNCTION call
            # by name when the call runs, so a function may call one defined
            # below it and the kit's three forward calls are fine. A `let` is
            # different — it is captured lexically, which is why a rescale block
            # appended behind the kit never reached the functions above it.
            # Reporting forward function calls made this tool cry wolf in every
            # mood and buried the one finding that was real.
            out.append(("TOO LATE", f, ln, name, kind))
            seen.add((kind, name))
    return out


def chain_for(mood: str, axes: list) -> list:
    files = ["_palette_dark.splash"]
    if mood != "dark":
        files.append(f"_palette_{mood}.splash")
    files += axes + ["_derive_color.splash", "_derive.splash", "_kit.splash"]
    out = []
    for f in files:
        p = L0 / f
        if p.exists():
            out.append((f, p.read_text()))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mood")
    p.add_argument("--axis", action="append", default=[],
                   help="an axis fragment file name, repeatable")
    a = p.parse_args()

    moods = [a.mood] if a.mood else sorted(
        f.stem.replace("_palette_", "") for f in L0.glob("_palette_*.splash"))
    bad = 0
    for mood in moods:
        found = lint(chain_for(mood, a.axis))
        for level, f, ln, name, kind in found:
            where = kind.split("@")[1] if "@" in kind else "top level"
            print(f"{level:9} {mood:<12} {name:<22} read in {where:<18} "
                  f"({f}:{ln})")
        bad += len(found)
    print(f"\n{bad} unresolved name(s) across {len(moods)} mood(s)" if bad
          else f"\nevery name resolves, in order, in all {len(moods)} moods")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
