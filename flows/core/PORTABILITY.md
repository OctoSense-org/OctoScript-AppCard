# Reproduction update validation — 2026-09-08

Both native branches now have [generic setup and input examples](REPRODUCE.md),
with a [provider-neutral reviewer contract](MODEL-REVIEW.md). The image intake
records the declared generator/model, exact prompt and original PNG hashes;
it does not call a provider. Both branches accept the configured local Studio
bridge. Native Sketch capture and preflight default to external review; the
legacy provider CLI requires explicit selection. Personal device identifiers
are no longer built-in defaults.

`review.py` prepares frozen screenshot pairs and unresolved Sketch semantic
templates. Submission requires an explicit reviewer, written decision, all
four visual criteria and current image hashes. It preserves prior receipts
and leaves acceptance to the existing measured and visual gates. It does not
approve a template or make a visual judgment.

Validation completed:

- **250 tests passed** in fresh Python 3.12 environments installed from the
  declared requirements: 187 Sketch, 41 image and 22 shared tests. Separate
  environments resolve the branches' differing NumPy requirements. Coverage
  includes missing prompts, provider provenance, bridge configuration,
  reviewer selection, stale/modified packets and incomplete decisions.
- The source-review and screenshot-pair commands ran against an existing
  Taskplan screen and Weather 11. All resulting templates remain unreviewed;
  no real approval was created by this smoke test.
- **31 fresh native image captures** through the configured Studio bridge
  passed structural, semantic and freshness gates. Existing visual approvals
  remained valid because their source/native image hashes matched. This run
  did not create new visual judgments. One initial capture failed before its
  app socket was ready; rerunning it without launching again succeeded. The
  failure and recovery are retained in the run history.
- Browser verification opened all 31 comparison dialogs, checked 62 served
  image hashes and 373 artifact links, and found no browser script errors.
- The new public guides/examples use generic paths and contain no credential
  values. JSON examples parse and local documentation links resolve.
  Workspace and native repository whitespace checks pass.
- The temporary validation Studio, capture host and bridge were stopped;
  the pre-existing Studio, bridge and comparison server remain available.

The local machine-readable record is
[`qa-work/portability/validation.json`](qa-work/portability/validation.json).
Historical migration evidence remains unchanged. The previous 475-screen
Sketch migration was not recaptured for this documentation/intake update.

This checks fresh dependency installation and the existing native corpus in
the current compatible workspace. It is not a full clean-clone run with a new
licensed kit, a new image generator or another vision reviewer. The exact
native changes and compatible Studio revision must accompany a reproduction.
New designs still require explicit semantic interpretation, repair and visual
QA; no comparative benchmark establishes equal results with another reviewer.
Phone behavior, responsive layouts and complete app workflows remain separate
validation scopes.
