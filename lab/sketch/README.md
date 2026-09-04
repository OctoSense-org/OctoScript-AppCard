# The beauty pipeline: a purchased design kit → judged live cards on three backends

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
- Rust toolchain; these repos as siblings under `~/home/`:
  `Splash` (the language), `octos-one` (this repo, with `splash/` and
  `splash-makepad/` inside it), `Splash-OH` (the HarmonyOS app).
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

    python3 run_kit.py --kit <name> --stages author,desktop
    python3 run_kit.py --kit <name> --stages android
    python3 run_kit.py --kit <name> --stages ohos

- `author` — one L0 card per screen via `claude -p`, with a validate/repair
  loop against the real `realize()` gate. Resumes: existing cards are kept.
  Round 2 (`--rounds 2` or rerun after judging) feeds each screen's judge
  verdict and fill-gate note back into the prompt.
- `desktop` / `android` / `ohos` — render, fill-gate, strict-judge that rail.
  Every stage is resumable; `--stages status` shows freshness and medians.

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
- **Profile tests are the drift fence.** After any vocabulary change run
  `cargo test -p splash-ui-l0 --test profile` in `~/home/Splash`; the
  both-backends test fails the build for any constructor a backend cannot
  draw.

## Known limits (measured, not hidden)

- Strict design-match plateaus around median 3 (vs the 7 ceiling): the
  residual is LLM author underfill on dense screens, quantified per screen
  by the fill gate. More vocabulary has stopped helping; better authoring
  policy (gate-pointed repair, best-of) is the open lever.
- ArkUI rail renders without gradients (`bg2` dropped), in system type.
- Illustration artwork and masonry layouts are out of scope by design.
