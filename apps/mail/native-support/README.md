# Native compatibility snapshot

`manifest.json` pins the three upstream repositories and hashes two cumulative
patches. `scripts/setup_native.py` fetches the pinned commits outside AppCards into
`octosense-org/.appcard-native/mail/`, verifies and applies the patches, then checks the resulting
source-file hashes. Re-running it accepts the same prepared source and preserves
unexpected local edits. It never resets the shared repositories.

- **makepad.patch:** compatible checked VM evaluation, text metrics/spacing and
  inspection, widget selection state, and macOS native WebView inspection.
- **splash-makepad.patch:** compatible VM/drawing APIs, platform Browser lowering
  and lifecycle, native scroll containers, selection/scroll preservation,
  app-owned scroll reports and request-supplied window title.
- **splash:** unmodified pinned L0 language profile.

These patches include the compatible runtime changes that the standalone host
needs, in addition to the mail-specific reader/scroll support. They deliberately
exclude Studio launcher changes, unrelated mount descriptors and service assets.
The checkout directories are `makepad`, `octoscript` and `octoscript-makepad`;
upstream crate names and patch identifiers remain unchanged. Two Cargo sibling
paths are adapted from `splash/` to `octoscript/` after patch verification. They can be removed
when equivalent upstream revisions are adopted and verified.
