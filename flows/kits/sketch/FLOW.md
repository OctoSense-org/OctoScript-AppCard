# Flow: Sketch kit ingest

The contract every flow follows is in [flows/README.md](../../README.md). This
page is the step list for this flow; [README.md](README.md) explains the
importer, gates and repair loop in depth.

**This flow produces theme kits, not apps.** Its output is native L0
components and themes that other flows and Octoscript-Makepad consume. It has
no App Hub hand-off of its own.

## Use when

You hold a **licensed** Sketch design kit and want its screens reproduced as
native Makepad widgets, then promoted into a reusable L0 kit (tokens,
components, themes). Do not use it for a generated image (use
[image-to-card](../../image-to-card/FLOW.md)) or a text brief (use
[script-app](../../script-app/FLOW.md)).

## Inputs

| Input | Where it goes | Notes |
| --- | --- | --- |
| Kit archive (`.zip` containing a `.sketch`) | `flows/core/work/<kit>/source.zip` | Licensed to you; never committed (`work/` is ignored) |
| Kit configuration | `flows/core/kits/<kit>-native-all.json` | Copy [core/examples/sketch-kit.json](../../core/examples/sketch-kit.json); set `sketch_member`, `pages`, `screens`, `design_scale` |
| The design's exact fonts | `font_files` in the kit configuration | Local paths to fonts you may use |
| Reviewed semantic manifests | `flows/core/work/<kit>/native/semantics/<screen>.json` | One per screen, from the source review |

## Prerequisites

- macOS with Xcode command-line tools.
- **Sketch.app (paid) and a licensed kit.** Buying them is a **HUMAN** step.
  `SKETCHTOOL` must point at `Sketch.app/Contents/MacOS/sketchtool`.
- Python 3.12 with the Sketch environment:
  `python3.12 -m venv flows/kits/sketch/.venv && flows/kits/sketch/.venv/bin/pip install -r flows/kits/sketch/requirements.txt`.
- The shared native runtime beside this repository:
  `python3 tools/setup-native.py` (see [NATIVE-WORKSPACE.md](../../../docs/NATIVE-WORKSPACE.md)).
- Release Makepad Studio with a `splashref` mount on the prepared
  `octoscript-makepad` checkout, its matching `cargo-makepad`, and the
  persistent bridge, started as in [REPRODUCE.md](../../core/REPRODUCE.md).

Check, from the repository root (with `BEAUTY_STUDIO`, `BEAUTY_BRIDGE`,
`CARGO_MAKEPAD` and `SKETCHTOOL` exported and Studio plus the bridge running,
as in REPRODUCE.md):

```sh
export KIT=example-native-all
export BEAUTY_PYTHON="$PWD/flows/kits/sketch/.venv/bin/python"
python3 tools/setup-native.py --check >/dev/null \
  && test -x "$SKETCHTOOL" && test -x "$CARGO_MAKEPAD" \
  && curl -fsS "$BEAUTY_BRIDGE" | grep -q '"running": *true' \
  && "$BEAUTY_PYTHON" -c "import numpy, PIL, fontTools" \
  && echo "prerequisites: ok"
```

Pass when it prints `prerequisites: ok`. After the first import (step 3),
`bash tools/beauty-pipeline.sh --kit "$KIT" --stages doctor` is the full
preflight: it ends with `doctor: ready` or exits nonzero naming each missing
item (Sketch CLI, the prepared `makepad`/`octoscript`/`octoscript-makepad`
checkouts, the bridge, the imported kit source and image directory).

## Steps

`K` below stands for `bash tools/beauty-pipeline.sh --kit "$KIT"`, which runs
`flows/kits/sketch/run_kit.py` with `$BEAUTY_PYTHON`. Each stage exits nonzero
on failure; stop there.

| # | Command | Pass when | Human? |
| --- | --- | --- | --- |
| 1 | Buy Sketch and the kit; place the archive at `flows/core/work/<kit>/source.zip` | the file exists and its license allows your use | **HUMAN**: purchase and license |
| 2 | `cp flows/core/examples/sketch-kit.json flows/core/kits/$KIT.json` and edit `source_archive`, `sketch_member`, `pages`, `screens`, `design_scale` and `font_files` | the file is valid JSON naming your archive | |
| 3 | `K --stages extract`, then `K --stages doctor` | extract exits 0 and `work/<kit>/native/` holds the imported tree and reference exports; doctor ends with `doctor: ready` | |
| 4 | Per screen: `"$BEAUTY_PYTHON" flows/core/review.py prepare-source --kit "$KIT" --screen <Screen> --out flows/core/work/<kit>/source-review/<Screen>` | a source-review template exists per screen | |
| 5 | Review each source image and tree, including anonymous numerical regions; install the reviewed manifest as `work/<kit>/native/semantics/<Screen>.json` | every region has a reviewed role, source IDs and paint owner | **HUMAN**: semantic review |
| 6 | `K --stages extract,promote` (lowers the reviewed mappings, then `promote_l0.py` and `export_app_recipes.py`) | exit 0; L0 kit cards written under the kit's `work/` | |
| 7 | `K --stages splash-makepad` (release Studio capture, structure and visual gates) | exit 0; captures and `pipeline-run.json` under the kit's captures directory | |
| 8 | Per screen: `"$BEAUTY_PYTHON" flows/core/review.py prepare --kit "$KIT" --screen <Screen> --out flows/core/work/<kit>/visual-review/<Screen>`; fill `decision.json`; `"$BEAUTY_PYTHON" flows/core/review.py submit --packet <packet> --decision <packet>/decision.json` | the submit command accepts the decision | **HUMAN**: visual review |
| 9 | `K --stages audit` | exit 0: structural, semantic, L0 and visual gates pass on saved evidence | |
| 10 | `K --stages report` | exit 0; gallery, composition and repair feedback refreshed | |

On a failed gate, read the per-element `.structure.json`, `.composition.json`,
`.kit.json` and `repair-feedback.json` beside the captures, repair the importer,
mapping, component or asset, and repeat from step 6. `K --stages beauty` runs one
import plus native validation cycle; `K --stages status` (the default) prints
artifact freshness. Never edit recorded rounds to pass a gate.

## Outputs

| Path | What |
| --- | --- |
| `flows/core/work/<kit>/native/` | Imported tree, reference exports, reviewed semantics (ignored; licensed material) |
| L0 kit cards and captures under the kit's `work/` directories | Native components, per-screen captures and gate reports |
| `$OCTOSENSE_WORKSPACE/octoscript-makepad/components/l0/native/<theme>/kit.json` | The promoted theme kit read by `export_app_recipes.py` |
| App recipes from `export_app_recipes.py` | Source-backed component styles for app composition |

## Hand-off

A theme kit is not published to App Hub. Hand it to the runtime:

1. Commit the promoted kit to **Octoscript-Makepad** (`components/l0/native/<theme>/`)
   through that repository's review, with the kit's license terms. Purchased
   source files, exports and captures stay in ignored `work/` directories and
   are never committed here or there.
2. Bump `native-runtime.lock.json` here to the Octoscript-Makepad release that
   contains the kit (`python3 tools/setup-native.py --update`, then
   `--check`).
3. Apps then select the theme through the other flows. An app built on it
   follows that flow's hand-off to App Hub.

## Limits

- Needs paid Sketch.app and a licensed kit; neither can be supplied by an
  agent. Redistribution follows the kit's license, not this repository's.
- Reproduces fixed artboards. Responsive reflow and complete application
  workflows need their own implementation and evidence.
- The older theme/LLM L0 and desktop/device rails in `run_kit.py` are not
  maintained; the kit-specific legacy migration adapters are not in this
  repository (see [OLD-KIT-MIGRATION.md](../../core/OLD-KIT-MIGRATION.md)).
- A passing gate is not visual approval; step 8 is.
