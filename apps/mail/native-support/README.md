# Shared native runtime

Mail consumes the AppCards root `native-runtime.lock.json`, which pins
[Octoscript-Makepad](https://github.com/OctoSense-org/Octoscript-Makepad).
That framework owns `runtime.json` and the exact Makepad and Octoscript sources.
HTML/WebView support, scrolling, state restoration and native inspection are
maintained in those repositories. This directory no longer distributes patches.

Run `python3 apps/mail/scripts/setup_native.py` from the AppCards root.
See [the shared workspace guide](../../../docs/NATIVE-WORKSPACE.md) for setup,
source verification and preservation of local edits.
