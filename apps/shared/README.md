# Shared app support

Browser rendering, font metrics and wizard adapters used by the School, Health
and Reunion apps. This directory is not an app.

`flows-history.md`, the verification receipts and `evidence/` preserve the
earlier cross-app review. Absolute paths in those receipts record their original
execution locations; the apps now live at `apps/<name>/`.

`verify-standalone.py` is a historical Studio verifier. New native verification
must use [Makepad's built-in instrument](../../lab/core/NATIVE-INSTRUMENT.md),
with hidden windows for automation. Mail's `scripts/verify_completion.py` is a
working example.
