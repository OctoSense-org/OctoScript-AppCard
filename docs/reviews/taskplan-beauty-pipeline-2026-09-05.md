# Taskplan beauty pipeline validation — 2026-09-05

The supplied Taskplan ZIP was imported and tested first through **splash-makepad**,
using the release native preview host launched and controlled by Makepad Studio.
The Octos app, Android and HarmonyOS rails were not used for this validation.

## Input and scope

- Archive SHA-256: `0cbca109074d6e75ca2600474b962640738893968dedc8f4e376c19ea0a37372`.
- Extracted 79 app artboards from **Hifi Design**, at 393×852 logical pixels (1×).
- Resolved all 1,597 symbol instances; no unresolved symbols or missing image assets.
- Authored and validated five representative cards: Home, Project Details,
  Notifications, Profile and Login.
- Registered the measured `taskplan_light` theme. The source did not require
  an invented dark variant.

## Repairs made

1. Unpack changed the on-disk config but chained extraction kept reading the ZIP
   as a directory. Stages now reload the config, preserve the original archive
   path for reconstruction, and use one Python environment.
2. Preflight used stale sibling paths and required phones for a desktop-only
   run. It now checks the configured rails and the local checkouts.
3. Theme registration assumed an obsolete one-line catalog and a second Splash
   checkout. It now updates the current catalog/app table with idempotent edits.
4. Theme/author measurements assumed 2× source coordinates. Taskplan now uses
   its actual 1× scale; text colors are read from the extractor's actual schema.
5. The author included off-artboard content and treated a translucent gradient
   as a solid colored ground. Those instructions now reflect the visible frame
   and opaque background evidence.
6. There was no native splash-makepad pipeline stage. The new stage runs checked
   realization, ordered theme assembly, portable evaluation, native widget
   construction, text parity, frame validation, screenshots, fill and vision
   judgments, with a comparison gallery.
7. Native evaluation rejected untyped padding/margin objects and invalid
   TextInput properties. Typed Inset values now preserve top/bottom overrides;
   unsupported show_bg/on_click properties are omitted from fields.
8. Material lowering restyled resolved L0 cards, changing avatar dimensions and
   discarding chip children. The L0 translator preserves their authored theme
   presentation and already calibrated point sizes.
9. HTTP image URLs were emitted as bundled file paths. Profile's image now
   loads through HTTP, with a successful image request required before capture.
10. `.on`/`.off` selected-state tokens were accepted but did not become Boolean
    arguments. The realized value now reaches the selected-chip lowering.
11. Authored numeric defaults could not act as host data. The lab admits only
    state values found literally in the design and records fixture provenance;
    Project Details' `80%` is now visible in the native screenshot.
12. Existing captures and scores were reused blindly. Captures now bind input,
    binary, theme, asset and PNG hashes; scores bind target/capture/prompt hashes.
    Missing/stale inputs fail, and status checks native capture hashes.
13. Failed author rewrites could overwrite valid cards. Candidates are validated
    before replacement. Timeouts are reported concisely, preserve prior cards,
    and do not discard other completed authoring work.
14. The initial widget dumps contained only Window → KeyboardView → Splash.
    The host now assigns deterministic generated IDs, deeply registers each
    replacement subtree and invalidates the cached widget index. This was tested
    across all five screens in one process, including repeated mounts.
15. The upstream dev bridge silently filtered WidgetSnapshot replies. Its
    forwarding and requesting-client filter now include that response, with a
    regression test. Label inspection now uses its complete layout area instead
    of the first glyph's drawing area. Composed native Views retain optional
    selection state, which the snapshot exposes and the gate checks.
16. Capture now saves WidgetTreeDump, WidgetSnapshot, an exact WidgetQuery per
    generated ID and native clipped-area measurements. The structural gate
    checks their agreement, hierarchy, content/state, dimensions, position,
    alignment, spacing, missing/unmapped elements and clipping. Host-only,
    missing, altered or stale inspection fails instead of accepting a screenshot.
17. Structural findings enter the repair round even when the visual score is
    high. The screenshot judge now focuses on typography, colors, imagery and
    effects; it cannot override structural rejection. The combined stage saves
    both reviews and returns a nonzero result when structure fails.
18. Startup reused Home's nonce-bound evidence paths, invalidating that screen
    on every cache run. Startup now writes separate bootstrap evidence, leaving
    the saved capture and its inspection bundle intact.

## Validation and evidence

- **333 Rust release tests passed**: 280 L0 core/profile, 52 portable
  renderer/backend tests and one Studio bridge snapshot regression.
- **24 Python regression tests passed** (13 pipeline and 11 structural), including chained config
  reload, scale invariance, fixture provenance, cache invalidation and failed
  rewrite preservation, host-only inspection, missing queries, native text and
  control-state loss, hierarchy changes, clipping, ambiguous mappings and
  structural repair selection despite a 10/10 visual score. The preflight's
  existing gate tests also passed.
- Studio built from official Makepad `dev`, revision
  `a13034d85d5564f95d1ce100fa6fd19827c73117` plus the bridge snapshot forwarding
  fix; runtime uses this repository's Makepad fork and its checked evaluator.
- The first full native round rendered all five screens with matching text lists
  and 786×1704 pixel captures. Its design scores were **4, 4, 4, 3, 2 / 10**.
- Profile's HTTP image and Project Details' 80% fixture were separately verified
  in fresh native runs after their repairs.
- Home completed a feedback rewrite. Project Details and Login's optional author
  requests timed out after 600 seconds; their valid cards were preserved.
  Login subsequently received a local repair using measured structural findings.

## Structural measurements

Tolerance values are saved in every report: **4 pt** for position, alignment and
spacing, **6 pt** for dimensions, **2 pt** for clipping, and **1 pt** for agreement
between inspection APIs. Snapshot desktop coordinates are normalized using the
reported Window origin; W3 and Query already use window-local logical points.
Sketch geometry is divided by the kit's explicit scale of 1.

The extractor preserves Sketch object IDs. Reports retain the full instance-qualified
source hierarchy and generated/native hierarchies. Mapping uses exact content,
image asset identity, duplicate document order when counts agree, and anchored
descendant sets for containers. It does not remap by nearest measured position.
Unmatched painted elements are marked **missing or unmapped**, which fails the
gate without falsely claiming that every unmatched vector subpath is absent.
TextInput inspection exposes the whole control's bounds and current value;
its placeholder glyph bounds are not separately available.

The first complete inspected round had **374/374 generated nodes**, compared
with the three-node host-only dumps found by the side review. A subsequent
Login repair adds four containers. All captured native text and composed-control
selected values are checked against the generated manifest. Native clipped areas
also detect ancestor clipping, independently of the screenshot review.

The measured Login repair moved its heading from y=55 to y=166 (Sketch y=166),
Email from y=118 to y=301 (Sketch y=302), Password from y=197 to y=399
(Sketch y=400), and the social separator from y=327 to y=622 (Sketch y=622).
It also restored the missing sentence-ending period. The card's large gap
arguments account for the existing theme's `air_factor=0.62`. This is a partial
repair: type sizes, field styling, logos and footer placement still differ.

Final structural results:

| Screen | Inspected generated nodes | Mapped Sketch elements | Failed element/relation checks | Gate |
| --- | ---: | ---: | ---: | --- |
| Home | 95 | 44 | 140 | FAIL |
| Project Details | 88 | 44 | 102 | FAIL |
| Notifications | 96 | 50 | 112 | FAIL |
| Profile | 61 | 21 | 80 | FAIL |
| Login | 38 | 18 | 57 | FAIL |

Inspection passes for **378/378 nodes**. All five structural gates fail, as they
should for these reproductions. The counts include unresolved source mappings,
which remain conservative failures; they are not a claim that that many visible
widgets are absent. The repair adds mappings and relations, so raw failure counts
are not directly comparable to a previous card with fewer mapped elements.

The final visual scores are **4, 3, 4, 4, 3 / 10**, all **rework**. The combined
pipeline returns **exit 1** after saving both reviews. This is a functioning
rejection gate, not a successful design acceptance.

The final capture used Studio build **19**. A separate warm run, build **20**,
reused **all five** complete capture/inspection bundles. PNG SHA-256 values and
nanosecond modification timestamps remained identical; visual judgments were
also reused. The manifest and `validation/cache-verification.json` record the
proof. No structural failures were removed or relaxed to obtain cache reuse.

[Comparison gallery](../../lab/sketch/work/taskplan/splash_makepad/gallery.html) ·
[Per-element reports](../../lab/sketch/work/taskplan/splash_makepad/) ·
[Validation manifest](../../lab/sketch/work/taskplan/validation/manifest.json).

Local artifacts are in [the Taskplan work directory](../../lab/sketch/work/taskplan/).
The initial complete round is preserved in `round1/`; the current captures,
portable/native reports, hashes and Studio transcript are in `splash_makepad/`.
Test logs and the input manifest are in `validation/`.

## Interpretation

Pipeline execution and visual acceptance are separate results. The remaining
fidelity differences include typeface substitution, role-based spacing and
control styling, and design details outside the current L0 vocabulary. Targets
are reconstructed from specs, with symbol resize, mask and rotation limitations;
they are not authoritative Sketch exports. No claim of pixel equivalence or
complete task-app behavior is made.

[Reproduction instructions](../../lab/sketch/TASKPLAN-VALIDATION.md).
