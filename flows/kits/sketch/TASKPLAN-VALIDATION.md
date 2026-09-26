> Historical five-screen L0 baseline (failed). For the completed 79-screen native design route, see [README.md](README.md) and the [native parity report](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/blob/cbbda4da0a9d0fbf13497335dd3342b71f35e71f/docs/reviews/taskplan-native-parity-2026-09-05.md). The standalone-window and reconstructed-reference limitations below describe this earlier run.

# Taskplan pipeline validation

Input: `taskplan-mobile-app-ui-kit_NTgxZDczMGNiYTliNGUxNTAwZTQyZjli.zip` from Downloads.
The provided archive and extracted assets remain in ignored `work/` directories.

The new `taskplan` config extracts the **Hifi Design** page: 79 artboards,
393×852 logical pixels, scale 1. It selects five representative screens for
native validation: Home, Project Details, Notifications, Profile and Login.
Taskplan ships a light design; `theme_modes: ["light"]` registers only that
measured palette. No fabricated dark palette is required.

## Reproduce

From the repository root:

```sh
python3 -m venv flows/kits/sketch/.venv
flows/kits/sketch/.venv/bin/pip install -r flows/kits/sketch/requirements.txt
```

Use the built release Studio and bridge from the upstream Makepad dev checkout.
The bridge must include the `WidgetSnapshot` forwarding fix in
`makepad/tools/cargo_makepad/src/studio.rs`; the tested dev revision silently
filtered that response. Rebuild the bridge after applying that fix. The native
runtime includes the full-label-area and composed View selected-state fixes.
Start Studio with a mount named `splashref` pointing to this checkout:

```sh
/path/to/makepad/target/release/makepad-studio --remote \
  --mounts=splashref:/absolute/path/to/octos-one/splash-makepad \
  --bind=127.0.0.1:8001
export CARGO_MAKEPAD=/path/to/makepad/target/release/cargo-makepad
```

Then run:

```sh
tools/beauty-pipeline.sh --kit taskplan --stages unpack,extract,theme
tools/beauty-pipeline.sh --kit taskplan --stages doctor,author,validate,splash-makepad,status
```

`validate` executes the real L0 realization, ordered theme assembly, checked
Splash VM and native dialect translation. `splash-makepad` repeats that gate,
builds the release `splash-beauty-host` **through Studio RunItem**, mounts every
card in a standalone native window, compares the portable/native text lists,
checks the capture dimensions, and captures pixels plus **WidgetTreeDump,
WidgetSnapshot and an exact WidgetQuery for every generated ID**. It compares
the measured structure against Sketch, then runs the fill and visual gates.
The stage exits nonzero on structural failure even when screenshots and visual
reviews are saved successfully. This runs before the Octos app/device rails.

A standalone window is necessary to preserve the design frame: Studio's
embedded pane controls its own size. It remains controlled and captured through
one persistent Studio bridge. The host confirms a successful mount; standalone
runs do not emit the embedded `AppStarted` event.

To exercise feedback:

```sh
flows/kits/sketch/.venv/bin/python flows/kits/sketch/author_cards.py --kit taskplan --round2
tools/beauty-pipeline.sh --kit taskplan --stages validate,splash-makepad,status
```

The feedback rail is configured per kit. The author reads the prior native
screenshot, its judge verdict, fill-gate finding and **per-element structural
report first**, including failures even when the vision score is high. Preserve a previous
round before requesting a rewrite if comparing author quality.

## What is checked

- Chained unpack/extract reloads the changed paths and uses one Python environment.
- Preflight checks only configured rails; phones and HarmonyOS are optional.
- Theme registration edits this checkout and handles the multiline catalog.
- Design scale controls measured type/radii and author instructions.
- Invalid new **or resumed** cards fail the author stage. Candidate files are
  validated before replacing existing cards; author failures preserve completed
  work and cause a nonzero stage result.
- Numeric state fixtures must match text in the design before the lab supplies
  them as host data; `.fixture-origin.json` records the admission.
- L0 Card/Chip presentation bypasses Material semantic restyling. Child labels,
  avatar sizes and already calibrated point sizes survive the native translator.
- Native padding/margins use typed `Inset`, including top/bottom overrides.
- Empty field targets do not emit unsupported `on_click`; TextInput receives no
  unsupported `show_bg` property. HTTP images remain HTTP resources.
- Selected `.on`/`.off` tokens become Boolean values for Boolean arguments.
- Captures are bound to card/data/spec/theme/image/binary hashes and their PNG hash.
  Inspection, clipping and structural artifacts are also hashed; host-only or
  missing inspection cannot qualify for cache reuse. Scores are bound to
  target/capture/prompt hashes. Missing/stale captures fail.
- The image server binds the configured port and stops after the run; an occupied
  port is an error, preventing captures using a different kit's images.

## Structural gate

Each `*.structure.json` saves the Sketch object/instance hierarchy, generated
IDs, native hierarchy, per-element bounds/deltas, visibility, native text and
control state, mappings and unmapped elements. `*.widgets.json`,
`*.snapshot.json`, `*.queries.json` preserve all three Studio responses.
`*.layout.json` adds native `Area::clipped_rect` measurements, checked against
Studio bounds, to detect clipping by ancestors as well as artboard overflow.

All comparisons use logical points. Snapshot desktop coordinates are normalized
with its own Window origin. Sketch coordinates use `design_scale`. Defaults are
4 pt position/alignment/spacing, 6 pt dimensions, 2 pt clipping, and 1 pt for
agreement between inspection APIs. A kit may explicitly configure
`structure_tolerances`; the effective values are saved in each report.

Mapping uses exact text and image asset identity, duplicate document order when
multiplicities agree, and anchored descendant sets for containers. It never
chooses a mapping by nearest measured coordinates. Painted source elements that
cannot be matched (including unrepresented vector paths) remain failures, not
asserted absences or silent exemptions. Off-artboard/transparent layers and
nonpainting layout groups remain in the saved hierarchy with their eligibility.
Native TextInput bounds describe the whole control; placeholder text bounds are
not separately exposed by Studio, so those shape differences need review.

Run the structural gate independently with:

```sh
flows/kits/sketch/.venv/bin/python flows/kits/sketch/gate_structure.py --kit taskplan
```

Exit 1 means the design is not accepted or evidence is incomplete/stale. The
vision judge covers typography, colors, imagery and effects, and cannot override
a structural failure. The gallery links to both measured findings and snapshots.

## Boundaries

This is a prototype design-fidelity experiment. It does not add application
navigation, authentication or live task data. The native host deliberately has
no online source adapters; unsupported source-dependent cards fail checked
assembly instead of showing made-up data.

The design targets are reconstructed by the existing spec rasterizer, not
exported by Sketch itself. Proportional symbol resizing, unenforced mask paths,
rotations and font substitution remain approximation limits. All 1,597 symbol
instances resolved; extraction reported 599 scaled instances, 749 masks and
302 rotations. The rasterizer found no missing image assets.

A successful capture is not a design acceptance. Read the per-screen structural
report, judge verdict and fill findings; neither a nonempty tree nor matching text is
sufficient evidence of visual fidelity. The first complete native round scored
4, 4, 4, 3, 2 out of 10 and flagged all five screens for fill differences.
Its artifacts are preserved under `work/taskplan/round1/`.

Current artifacts: `work/taskplan/splash_makepad/` (PNG, portable/native JSON,
widget dumps, capture hashes, Studio transcript), `xrail/strict_taskplan_splash_makepad.jsonl`
and `xrail/fill_taskplan_splash_makepad.jsonl`.

The optional feedback pass hit 600-second author CLI timeouts for Project
Details and Login. Their prior valid cards were retained. A subsequent local
Login repair used the measured structural report and was validated before
publication; the pre-repair evidence is in `work/taskplan/inspection_round0/`.
The 80% fixture value and Profile
photo were subsequently verified in native captures after their pipeline fixes.
