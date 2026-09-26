# Historical Aircon native runtime

These scripts and receipts preserve the original Studio-based run. Use
[Makepad’s built-in instrument](../../../flows/core/NATIVE-INSTRUMENT.md) for new
native tests. This repository move does not renew the historical acceptance.

# Native runtime

The isolated Makepad Studio uses `127.0.0.1:8012`. Its persistent matching
`cargo-makepad` bridge listens on `http://127.0.0.1:8182`. Local generated
artwork is served at port 8170 from the pipeline's published review directory. Studio on
port 8001 belongs to another task and is not controlled by this workspace.

Run each service in its own terminal:

```sh
bash runtime/start-studio.sh
bash runtime/start-bridge.sh
bash runtime/start-artwork.sh
```

Source `runtime/env.sh` from bash before running pipeline commands. Launch the
native UI only through the configured Studio `RunItem` named
`octos-ux-image-studio`, mount `splashref`. `studio.py --launch` implements this.
The RunItem builds `splash-makepad/apps/kit-host` binary `beauty-host` in release
mode with opt-level 3 and LTO disabled for fast review iterations, and consumes
`flows/image-lib/current-request.json`. Rebuild infrastructure binaries
with `bash runtime/build-native-tools.sh`; the native application itself is
always built by its Studio RunItem.

Image mapping/compilation may run in parallel. Native capture jobs must be
serialized: the host consumes one current request at a time. The controller
must also be paused during immutable per-frame capture.

Native evidence comes from Makepad Studio `WidgetTreeDump`, exact ID
`WidgetQuery`, `WidgetSnapshot`, layout inspection, `Screenshot` and actual
`Click` events. Disabled controls must emit no activation and remain disabled
in a fresh native snapshot. Label geometry is the allocated native walk Area;
text layout is recorded separately. Screenshot capture preserves the full
Studio backing image and a hash-bound receipt for the exact viewport crop
(406 × 776 logical pixels at DPI 2 for image-derived scenes), without resizing.
No OS screenshot mechanism is used.

The host polls changed requests every 250 ms and logs native kit actions to
the request's `actions` file. A service state controller can consume these
actions and remount the appropriate L0 card without rebuilding the host.

The published parent repository pins an older Makepad missing APIs its own
Splash runtime consumes. This reproduction uses Makepad revision
`38f4d3bc28938dfc8d8afe05082e84e599c0575d`, the last parent before Studio was
removed, with the narrow adapters recorded in `compatible-makepad.patch` and
`compatible-splash-makepad.patch`. These retain bounded checked evaluation,
native selection state, actual Label/backdrop measurements, and native text
tracking. The generated UI explicitly returns its root View. The bridge
forwards and scopes WidgetSnapshot responses. No wire protocol changes are
made. Native text tracking uses logical pixels and converts to ems for shaping,
including cached layouts, wrapping and ellipsis.

`infrastructure.json` records actual revisions, binary hashes, active patches
and test results. Earlier pin experiments and their failed rounds remain as
historical diagnostics; their patches are not the active reproduction.
Optional physics PGO is disabled via `RUSTFLAGS=""` because its relative profile
path does not resolve inside dependency builds.

After native runtime code changes, clear the old Studio build and launch a new
RunItem before taking evidence. Do not inspect an old build after changing code.
Original images and archived capture rounds remain immutable.
