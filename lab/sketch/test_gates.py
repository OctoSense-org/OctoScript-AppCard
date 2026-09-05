#!/usr/bin/env python3
"""Test the validators, by handing them the failures they exist to catch.

A gate has no gate of its own. It produces a plausible number on every run, so a
wrong one is indistinguishable from a right one until someone opens the pixels —
and three of these shipped today already blind to the exact defect that
motivated them:

- `audit_theme` decided "this pack has no card colour" by testing whether the
  colour was black, and CaMo's card IS black. It skipped the pack it was written
  for; restoring the ink that made it unreadable at 1.14 would still have passed.
- `gate_ink` accepted on missing BANDS alone. Keeping one label column per row
  and deleting the other eleven scores 92% missing cells and passed.
- `regress_desktop` returned success no matter what moved, and a render that
  never happened did not fail it.

So each test below injects one deliberate defect and asserts the tool says so.
Run it after touching any of them:

    python3 test_gates.py
"""
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

FAILURES = []


def check(name, cond, detail=""):
    print(f"{'ok  ' if cond else 'FAIL'} {name}" + (f"  — {detail}" if detail and not cond else ""))
    if not cond:
        FAILURES.append(name)


# --- audit_theme -----------------------------------------------------------

BASE = """let l0_base     = argb(255, 10, 14, 20)
let l0_fill     = argb( 18, 255, 255, 255)
let l0_text     = argb(255, 255, 255, 255)
let l0_card_1 = 0
let l0_card_2 = 0
let l0_card_ink = argb(255, 255, 255, 255)
"""


def audit(palettes: dict):
    """Run the auditor over a synthetic pack set; return (exit code, output)."""
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d)
        (p / "_palette_dark.splash").write_text(BASE)
        for name, body in palettes.items():
            (p / f"_palette_{name}.splash").write_text(body)
        r = subprocess.run([sys.executable, str(HERE / "audit_theme.py"), "--dir", str(p)],
                           capture_output=True, text=True)
        return r.returncode, r.stdout


def test_audit():
    # The CaMo case: an opaque BLACK card carrying near-black ink. The colour
    # and "this pack states no card" are not the same thing.
    code, out = audit({"blackcard": BASE + """
let l0_base = argb(255, 255, 255, 255)
let l0_text = argb(255, 20, 20, 24)
let l0_card_1 = argb(255, 0, 0, 0)
let l0_card_2 = argb(255, 0, 0, 0)
let l0_card_ink = argb(255, 20, 20, 24)
"""})
    check("audit: a black card with near-black ink is unreadable",
          code == 1 and "FAIL" in out, out.strip())

    # A pack that states no card of its own must be skipped, not crash and not
    # be reported against the base's `= 0`.
    code, out = audit({"nocard": BASE})
    check("audit: a pack with no card of its own is not reported",
          code == 0 and "card" not in out, out.strip())

    # A low-alpha panel lift is the colour you SEE, not white-on-white.
    code, out = audit({"lift": BASE})
    check("audit: a translucent panel is composited, not read literally",
          "panel" not in out, out.strip())


# --- gate_ink --------------------------------------------------------------

def test_gate_ink():
    import numpy as np
    import gate_ink as G

    real = G.ink_grid
    ref = np.ones((G.ROWS, G.COLS), bool)

    def with_grids(ref_g, shot_g):
        G.ink_grid = lambda p: ((ref_g, float(ref_g.mean())) if p == "ref"
                                else (shot_g, float(shot_g.mean())))
        try:
            return G.compare("ref", "shot")
        finally:
            G.ink_grid = real

    # The label survives, every value beside it is gone. Bands all still inked.
    keeps_label = np.zeros((G.ROWS, G.COLS), bool)
    keeps_label[:, 0] = True
    r = with_grids(ref, keeps_label)
    check("gate_ink: a row that keeps its label and loses its values fails",
          not r["ok"], str(r))

    # Whole bands gone.
    lost_bands = ref.copy()
    lost_bands[20:] = False
    r = with_grids(ref, lost_bands)
    check("gate_ink: whole bands going bare fails", not r["ok"], str(r))

    # Identical content passes.
    r = with_grids(ref, ref.copy())
    check("gate_ink: an identical render passes", r["ok"], str(r))

    # One row of vertical drift is not a difference.
    drifted = np.zeros((G.ROWS, G.COLS), bool)
    drifted[1:] = ref[:-1]
    r = with_grids(ref, drifted)
    check("gate_ink: one row of drift is tolerated", r["ok"], str(r))


# --- content_parity --------------------------------------------------------

def test_content_parity():
    import content_parity as C

    # Holes are positions, not absences: a rail that dropped index 2 must show
    # a gap THERE rather than a shorter list that diffs against everything.
    parsed = C.parse("content[0]: a\nnoise\ncontent[2]: c\n")
    check("content: a missing index is a hole at that position",
          parsed == ["a", "\x00MISSING", "c"], str(parsed))

    # A log line with a prefix in front of the marker still parses.
    parsed = C.parse("09-04 12:00 I A0/tag: content[0]: hello\n")
    check("content: a log prefix does not hide the entry",
          parsed == ["hello"], str(parsed))

    check("content: an empty resolve is recorded, not skipped",
          C.parse("content[0]: \ncontent[1]: x") == ["", "x"])


# --- lint_theme ------------------------------------------------------------

def test_lint():
    import lint_theme as L

    # A name nothing binds. Reads 0 at runtime, and 0 is a legal transparent
    # colour, so this is invisible everywhere except here.
    chain = [("p.splash", "let a = 1\n"),
             ("k.splash", "fn f() { return ghost }\n")]
    found = L.lint(chain)
    check("lint: a name nothing binds is reported",
          any(lv == "UNBOUND" and n == "ghost" for lv, _, _, n, _ in found),
          str(found))

    # A `let` written after a function that reads it. The function keeps the
    # earlier binding — this is how a whole rescale block came to be inert.
    chain = [("k.splash", "let size = 10\nfn f() { return size }\nlet size = 20\n")]
    found = L.lint(chain)
    check("lint: a let that lands after its reader is not reported when an "
          "earlier binding exists", not found, str(found))

    chain = [("k.splash", "fn f() { return size }\nlet size = 20\n")]
    found = L.lint(chain)
    check("lint: a let bound only AFTER its reader is reported",
          any(lv == "TOO LATE" and n == "size" for lv, _, _, n, _ in found),
          str(found))

    # A forward function CALL is legal: the device selftest reports that this
    # VM resolves a call by name when it runs. Reporting these made the tool
    # cry wolf in every mood.
    chain = [("k.splash", "fn early() { return later() }\nfn later() { return 7 }\n")]
    found = L.lint(chain)
    check("lint: a forward function call is not reported",
          not any(n == "later" for _, _, _, n, _ in found), str(found))

    # The real chain must be clean.
    import subprocess
    r = subprocess.run([sys.executable, str(HERE / "lint_theme.py")],
                       capture_output=True, text=True)
    check("lint: the shipped chain resolves in every mood",
          r.returncode == 0, r.stdout.strip()[-300:])


# --- regress_desktop -------------------------------------------------------

def test_regress():
    """Run the comparison for real, against directories built by hand.

    This test used to grep the source for the strings "missing" and "return 1".
    Changing `if missing:` to `if False:` satisfied it — so the one test written
    to prove a gate breaks on purpose broke nothing, which is the same failure
    it was written about.
    """
    import numpy as np
    from PIL import Image
    import regress_desktop as R

    def png(path, shade):
        Image.fromarray(np.full((409, 188), shade, np.uint8)).save(path)

    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d)
        cards, base, out = p / "cards", p / "base", p / "out"
        for x in (cards, base, out):
            x.mkdir()
        for name in ("a", "b"):
            (cards / f"{name}.card").write_text("# level: L0\n")
            png(base / f"{name}.png", 40)
            png(out / f"{name}.png", 40)

        argv = sys.argv[:]
        sys.argv = ["regress_desktop.py", "--against", str(base), "--out", str(out)]
        try:
            moved, missing = R.compare_dirs(sorted(cards.glob("*.card")), base, out)
            check("regress: identical renders report no movement",
                  not moved and not missing, f"{moved} {missing}")

            png(out / "b.png", 200)
            moved, missing = R.compare_dirs(sorted(cards.glob("*.card")), base, out)
            check("regress: a screen that changed is reported",
                  [n for _, n in moved] == ["b"], f"{moved}")

            (out / "a.png").unlink()
            moved, missing = R.compare_dirs(sorted(cards.glob("*.card")), base, out)
            check("regress: a render that did not happen is reported",
                  missing == ["a"], f"{missing}")
        finally:
            sys.argv = argv


if __name__ == "__main__":
    test_audit()
    test_gate_ink()
    test_content_parity()
    test_lint()
    test_regress()
    print(f"\n{len(FAILURES)} failing" if FAILURES else "\nall gates catch what they exist for")
    sys.exit(1 if FAILURES else 0)
