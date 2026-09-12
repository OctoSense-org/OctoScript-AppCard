# Twenty-intent native composition study

This experiment turns an intent into a bounded source plan, runs real independent
reads through the Splash VM, synthesizes a shared dataset, and renders a native
L0 card. It supports five presentation families: travel, outdoor activity, city
comparison, daily briefing, and market research.

See the [20-case gallery](../../../docs/reviews/app-composition-20260910/gallery.html)
and [measurements and findings](../../../docs/reviews/app-composition-20260910/README.md).
The documented content errors are intentional experiment findings, not approved
recommendations. This runner is separate from the normal Octos chat composer.

## Run

Requires Python 3.9+, the local Rust workspace, and the RTX endpoint at
`http://127.0.0.1:30881/v1` serving `qwen3.8-27b`. No H100 is used.

```sh
cargo build --release --locked --manifest-path tools/splash-research/Cargo.toml --bins

# All 20 real intents; generate a fresh L0 view and retrieve sources concurrently.
python3 tools/splash-research/composition/run.py --out /tmp/compositions-generated

# All 20 intents with reusable L0 views and host-owned comparisons.
python3 tools/splash-research/composition/run.py \
  --templates-only --out /tmp/compositions-template

# A new intent through the same bounded workflow; output ID is custom.
python3 tools/splash-research/composition/run.py --templates-only \
  --out /tmp/my-composition \
  --intent "What do you recommend for a Beijing tour this week based on weather?"
```

`--ids 01,07,18` selects cases; `--resume` keeps completed results. Preserve an
output directory before rerunning: a repeated case replaces its result files.
Failed attempts produce `failure.json` and are not counted as completed results.

## The DSL boundary

The executable [composition.splash](../templates/composition.splash) issues every
admitted fetch before its first await, joins results in request order, then calls
one synthesis capability. The host starts at most four I/O jobs concurrently.
It admits 1–8 exact source requests, bounds response sizes, and permits only
specific HTTPS source hosts. A job cannot substitute a model-generated URL.
The Rust VM rejects unknown replies and outputs that violate the result schema.

```splash
use mod.composition
use mod.std.array
let tasks = []
for job in request.jobs {
    array.push(tasks, composition.fetch(job))
}
let evidence = []
for task in tasks {
    array.push(evidence, task.await())
}
let answer = composition.synthesize({
    intent: request.intent, plan: request.plan, evidence: evidence
}).await()
{answer: answer, evidence: evidence}
```

This is a standalone research program. The host installs `mod.composition`; an
L0 renderer alone does not provide network tools. The generated UI remains L0,
using the supplied `sys.dataset` fields and existing theme roles.

Reusable L0 templates are in [templates/composition](../templates/composition).
The exported files bind dataset ID `composition`. `cards.template(id, plan)`
instantiates the same family with a caller-owned dataset ID. They contain no
source values, complete embedded apps, arbitrary code, or model tool loops.

`decisions.py` computes calendar comparisons, rain ordering, daylight duration,
and air-quality constraints. An outdoor plan with unhealthy forecast daily maxima
on every day uses a conservative deterministic indoor plan. Other compositions
still use the LLM for prose, including Chinese synthesis. Source-ID enums enforce
valid references; they do not establish factual faithfulness.

## Native Mac review

Use the existing persistent Studio bridge at `127.0.0.1:8170`, connected to Studio
at port 8001. The `octos` mount points to `app/`, whose `makepad.splash` defines
`octos-macos-composition`. Follow [aichat/AGENTS.md](../../../aichat/AGENTS.md).
The request seed is `/tmp/octos-macos-composition-request.json`; it must already
contain the local launcher configuration, as prepared in this experiment.

```sh
# --build asks Studio to perform the release build; subsequent runs reuse it.
python3 tools/splash-research/composition/review.py \
  --out /tmp/my-composition --ids custom --build
```

The reviewer clears the preceding build, launches a fresh RunItem, verifies title
and content bindings, captures Plan, clicks Evidence and captures it, then returns
to Plan. It records launch-to-visible time separately from research/generation.
It never claims a mount or discovers runnables. The native binding reads a bounded,
host-selected `OCTOS_DATASET_FILE` snapshot; the card selects an ID and approved
fields, never a filesystem path. This study does not publish partial results into
an already running composition or add a generic search UI.

## Checks and export

```sh
python3 -m unittest discover -s tools/splash-research/composition -p 'test_*.py' -v
cargo test --release --locked --manifest-path tools/splash-research/Cargo.toml
```

For the export layout, place the generated run under `/tmp/study/` and template
run under `/tmp/study/template-run/`, each with a native review, then run:

```sh
python3 tools/splash-research/composition/report.py \
  --input /tmp/study --out /tmp/study-gallery
```

The gallery works from local disk, includes both variants and evidence screenshots,
and links each L0 card, dataset and trace. Export removes news excerpt text from
the trace and recompresses PNGs losslessly. `findings.json` records this dated
experiment's manual review; update it when exporting a different experiment.
