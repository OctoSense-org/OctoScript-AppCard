# The beauty pipeline: a purchased design kit → judged live cards on three backends

Entry point: `tools/beauty-pipeline.sh` at the repo root (forwards here).
One command per stage. Input is a UI kit bought from UI8 (a `.zip` holding a
`.sketch`). Output is: a registered Splash theme pack, one validated L0 card
per screen, renders on desktop / Android / HarmonyOS, and a score plus a
fill-gate verdict per screen.

Two kits have been through it: Atro V2 (15 screens, the bring-up) and CaMo 2
(107 screens, one automated pass). Numbers from those runs are in
`xrail/*.jsonl`.

## Prerequisites

Run the preflight first; it checks everything below and names what is missing:

    python3 run_kit.py --kit <name> --stages doctor

- macOS host. Python 3 with `pillow` + `numpy`.
- Rust toolchain. Desktop and Android rails are **self-contained in this
  repo**: the language crates (`../../splash/`), the theme kit
  (`../../splash-makepad/`), the render binary (`../../app/`) and the LLM
  helper (`llm.py`, vendored) all live here. Only the HarmonyOS rail needs a
  sibling checkout of `Splash-OH` under `~/home/` — skip the `ohos` stage and
  nothing else changes.
- Desktop render binary: `cd ~/home/octos-one/app && cargo build -p octos-app`.
- `claude` CLI on PATH — the strict judge and the card author both run
  through `claude -p` (vision + text). Any account that can run it works.
- Android rail: a phone on `adb`, the octos APK installed
  (`tools/build-android.sh`). Set the serial in `kits/<name>.json`
  (`android_serial`) or env `ANDROID_SERIAL`.
- HarmonyOS rail: a phone on `hdc`, DevEco installed, a valid debug
  signature (14-day expiry — renew in DevEco with the phone attached, one
  click). Serial in `ohos_serial` / env `OHOS_SERIAL`; hdc path via env `HDC`
  if not at the default.

## Set up a new kit

1. Copy `kits/atro.json` to `kits/<name>.json`. Set:
   - `sketch`: path to the purchased `.zip` (or an unpacked `.sketch` dir)
   - `theme` / `theme_light` / `model`: the pack names the cards will declare
   - `screens`: artboard names to run (see step 3 to list them)
   - the `*_dir` keys: per-kit output directories (any names)
2. `python3 run_kit.py --kit <name> --stages unpack` — lands the sketch tree
   in `work/<name>_sketch/` and repoints the config. `work/` is gitignored:
   kit assets are purchased content and stay out of the repo.
3. `python3 run_kit.py --kit <name> --stages extract` — parses every artboard
   to `specs_dir` and renders design targets to `targets_dir`. List artboard
   names with `ls <specs_dir>` and put the app screens (skip styleguide /
   symbol pages) into `screens`. Duplicate Light/Dark names get `_2` suffixes.
4. `python3 run_kit.py --kit <name> --stages theme` — mints
   `_palette_<theme>.splash` + `_light` from the specs (spec2pack) and
   registers them across the catalog, app palette table and accent axes
   (register_pack; anchored edits, loud failure). Then rebuild the desktop
   binary and the APK — the stage prints the reminder.

## Run the loop

    python3 run_kit.py --kit <name> --stages doctor          # before anything
    python3 run_kit.py --kit <name> --stages author,desktop
    python3 run_kit.py --kit <name> --stages android
    python3 run_kit.py --kit <name> --stages ohos
    python3 run_kit.py --kit <name> --stages verify,regress  # after a change

- `author` — one L0 card per screen via `claude -p`, with a validate/repair
  loop against the real `realize()` gate. Resumes: existing cards are kept.
  Round 2 (`--rounds 2` or rerun after judging) feeds each screen's judge
  verdict and fill-gate note back into the prompt.
- `desktop` / `android` / `ohos` — render, fill-gate, strict-judge that rail.
  Every stage is resumable; `--stages status` shows freshness and medians.
- `doctor` — the preflight, and it now runs the VALIDATORS first: the gate
  self-tests, the theme-chain linter, and the vendored-theme comparison. A
  loop that trusts a gate it has not tested is measuring nothing.
- `verify` — content parity: two rails must resolve the same strings, in the
  same order, for one card. This is the only check here that does not look at
  pixels, and it is the one that catches a screen which looks composed and is
  missing its values. Needs the phone.
- `regress` — render the whole corpus and report which screens MOVED. Run it
  after touching the kit, the lowering or a palette: a fix proven on four
  screens has twice moved a hundred others.

Useful loops beyond the stages:

- `python3 fill_fix.py --kit <name>` — the measured stretch: re-renders
  gate-flagged screens with the dead-space ratio injected as `media_stretch`
  (media, paddings, type at half rate). No LLM. Run after `desktop`.
- Best-of across authoring rounds: keep each screen's higher-scoring card;
  a blind re-author of a whole kit has measurably regressed (CaMo: mean
  2.83 → 2.49) while best-of cannot.

## Reading the results

- `xrail/strict_<kit>_<rail>.jsonl` — per-screen `design_match` 1–10,
  verdict, one-line worst defect. Calibration: the same judge scores a
  pixel-perfect CSS render of these specs **7/10** — read every score
  against 7, not 10. CaMo landed at median 3 across all rails.
- `xrail/fill_<kit>_<rail>.jsonl` — the fill gate: `missing` is the fraction
  of the frame the design fills and the render leaves as bare page
  (dead-space mask, no LLM). Flag threshold 0.18.
- `content_parity/` — the ordered strings each rail resolved. A structural
  difference is a defect; a numeric one is usually live data moving between
  the two renders, and the tool says which it saw.
- Side-by-side galleries: `scratchpad` builders exist in session history;
  any static page that pairs `targets_dir` and a shots dir works.

## Traps (each cost a debugging session; do not rediscover them)

- **The card author writes image URLs against `http://127.0.0.1:<img_port>`**
  and the renderer serves `img_dir` on that port. If a stale server from
  another kit holds the port, cards render black tiles. `lsof -ti tcp:8787 |
  xargs kill` then rerun; the render stage restarts it from the right dir.
- **Renders must postdate their cards.** The render stage skips existing
  PNGs; after re-authoring, delete the affected shots or the gallery/judge
  will read stale screens (this produced a fake all-reject OHOS round and a
  fake "squeezed" wave once each).
- **Judge on the rail's own pixels.** Never score one rail with another
  rail's captures.
- **OHOS capture**: one cold app launch per screen, advanced by a persisted
  counter; the harness reads the mounted index from hilog (`atroScreen(N)`)
  because the counter desyncs when a bad card crashes a launch. Reliable to
  ~15 screens per sitting; at 107 expect black-frame retries (built in) and
  rerun until `status` shows full coverage.
- **Type calibration**: makepad `font_size` is ~1.6× a real point. spec2pack
  bakes the 0.62 factor; if type looks 2–3× too big anywhere, this factor
  went missing, not the design.
- **register_pack edits by exact anchor.** If the catalog around an anchor
  changed, it exits loudly instead of guessing — do that edit by hand and
  rerun; never force it.
- **A gate has no gate of its own.** Three of these shipped blind to the exact
  defect they were written for: the theme auditor decided "this pack has no
  card colour" by testing whether the colour was black, and the pack that
  motivated it has a black card; the ink gate accepted a render that kept one
  label per row and lost every value beside it; the regression report returned
  success no matter what moved. `python3 test_gates.py` now breaks each of them
  on purpose. Run it after touching any gate.
- **A plausible number is not a measurement.** The fill gate scored an ArkUI
  card 98% while it showed seven forecast rows with no temperatures: it counts
  pixels that differ from the page background, and an opaque empty panel
  differs from the background. Ask what a gate is actually counting before
  believing a good score.
- **The harness lies before the code does.** In one session: a port that was
  open but serving another kit's images (a 50% fake regression), a baseline
  directory `fill_fix.py` also writes into (94 of 107 screens "moved",
  identical content at a different scale), a device capture that photographed
  the lock screen, and `snapshot_display` failing silently so `file recv`
  pulled the previous frame four times. When a result is dramatic, suspect the
  rig: a real regression from a scoped change is few and boring.
- **The theme VM binds `let` lexically and function calls by name.** A `let`
  appended behind the kit never reaches functions defined above it — a whole
  type-rescale block sat inert for its entire life that way. A function MAY
  call one defined below it (the device boot selftest logs which, so this stops
  being a matter of opinion). `python3 lint_theme.py` decides both statically.
- **An unbound name renders as transparent, not as an error.** 0 is a legal
  colour. `l0_accent` was unbound in six base moods and painted nothing,
  silently, until the linter was written. `doctor` runs it.
- **A miss is not a zero.** A fetch that fails must not return 0: a real 0°C
  and "no data" have to stay distinguishable, or the screen shows a number and
  the number is wrong. The OH shims answer `"--"` and log `net: MISS`.
- **Profile tests are the drift fence.** After any vocabulary change run
  `cargo test -p splash-ui-l0 --test profile` in `~/home/Splash`; the
  both-backends test fails the build for any constructor a backend cannot
  draw.

## Known limits (measured, not hidden)

- Strict design-match plateaus around median 3 (vs the 7 ceiling): the
  residual is LLM author underfill on dense screens, quantified per screen
  by the fill gate. More vocabulary has stopped helping; better authoring
  policy (gate-pointed repair, best-of) is the open lever.
- ArkUI rail: gradients, weather icons, device-assembled themes and live data
  all work now. What remains is frame FILL — the desktop harness stretches a
  card into its design frame and there is no equivalent here, so a page shorter
  than the frame leaves the slack at the bottom (~78% against the desktop's
  88% on the weather card). `spread` exists in the walk and is deliberately
  off: it pushes sections to the extremes and drives the last one under the
  gesture bar.
- Two rails still disagree about text width: a makepad Label defaults to Fill,
  an ArkUI text node hugs, so `Col(align: .center)` centres on one and does
  nothing on the other. Both are our own decisions, not toolkit defaults
  (`l0_widgets.rs`), and closing it is a corpus-wide pass.
- The contrast maths is not shared: `_derive_color.splash` uses a `pow(2.2)`
  approximation and `audit_theme.py` uses piecewise sRGB, so the runtime and
  the auditor disagree about the same pair. Fix before building anything new
  on top of either.
- Illustration artwork and masonry layouts are out of scope by design.
