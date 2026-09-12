# Mate 70 Air nav validation — 2026-09-05

Signing is renewed for `dev.makepad.octos_app`. The development certificate and
profile expire September 20, 2026 UTC. The signed application installs on the
connected Huawei Mate 70 Air (SUP-AL90, OpenHarmony 6.1.1.120).

The final signed release is Studio **build 38**, with `app.debug: false`.
[Artifact metadata and SHA-256](nav-evidence/mate70-38-artifact.json).
The final run rechecked saved HOME/WORK after restart, all three travel modes,
the direct route, stop search/selection, waypoint totals, navigation views,
End returning to the plan with its stop retained, and subsequent stop removal.
The destination pin is fully visible and saved-place labels no longer clip.
[Direct route](nav-evidence/mate70-38-direct-route.png),
[Walk](nav-evidence/mate70-38-walk-route.png),
[Bike](nav-evidence/mate70-38-bike-route.png),
[Waypoint route](nav-evidence/mate70-38-waypoint-route.png),
[3D navigation](nav-evidence/mate70-38-navigation-3d.png).

The dedicated Studio bridge on port 8002 remains connected. Device applications
are launched by `RunItem` (`octos-nav-mate70`). Screenshots, widget queries,
clicks, text, gestures and build cleanup are scoped to the returned build ID.
No `ObserveMount` was sent, and the other debugger's port 8001 was untouched.

## Device functionality

Build 31 used optimized Rust and a release HAP (`app.debug: false`), a bundled
copy of the canonical nav ledger, and an isolated review user store. The actual
phone framebuffer is 1320 × 2523, at DPI 3.25. These are phone screenshots, not
desktop simulations. The latest performance follow-up is described below.

| Check | Observed result |
| --- | --- |
| Origin and destination editing | Studio input entered Saratoga High School and NVIDIA Santa Clara; Return closed each editor. |
| Drive / Walk / Bike | Selected controls changed and persisted. Walk showed 186 min / 15.5 km; Bike showed 62 min / 15.5 km in build 36. Drive restored 21 min / 15.5 km. [Bike](nav-evidence/mate70-36-bike-route.png) |
| Map and route drawing | Vector streets, labels, route ribbon and endpoint markers rendered. [Route](nav-evidence/mate70-31-drive-route.png) |
| Add / edit a stop and choose search result | Added a stop, searched Apple Park Cupertino and selected the Cupertino result. |
| Waypoint route consistency | 29 min / 18.9 km; legs 17 min / 10.5 km and 12 min / 8.4 km. [Route](nav-evidence/mate70-31-waypoint-route.png) |
| Failed route and recovery | Unqualified Apple Park resolved to South Africa and the route service rejected it. The error appeared; choosing the Cupertino search result restored the route. [Error](nav-evidence/mate70-31-route-error.png) |
| Start navigation | Follow view opened with the waypoint route and an explicit waiting-for-location banner. [Navigation](nav-evidence/mate70-31-navigation.png) |
| Zoom and recenter | Zoom in, zoom out and recenter accepted Studio clicks. [Zoom](nav-evidence/mate70-31-zoom-in.png) |
| 2D / 3D | Switching from tilted to flat updated the control and map. [Flat view](nav-evidence/mate70-31-2d.png) |
| End trip | A Studio swipe revealed End; End returned to the plan with its stop preserved. [Reveal](nav-evidence/mate70-31-end-revealed.png) |
| Remove stop | One click removed the waypoint and restored the direct route. [Removed](nav-evidence/mate70-31-stop-removed.png) |
| Saved places | Saved Saratoga High School as HOME in build 36; build 37 loaded it after restart and selecting HOME populated the origin. Saved NVIDIA Santa Clara as WORK and selected it as destination. [Saved places](nav-evidence/mate70-37-saved-places.png) |

Actual GPS movement and permission grant/revocation have not been validated on
the phone: the native permission result remained denied and no fix arrived.
Desktop coverage is in the earlier reports. No physical travel or simulated GPS
was used in this device run.
Native touch pan and two-finger pinch also remain unverified: this Studio bridge
injects mouse events, while the nav gesture branch consumes `TouchUpdate`.
A Studio mouse drag did not pan the navigation map. Button zoom/recenter and
the bottom-sheet swipe were tested separately; they are not pinch validation.
Unqualified place names can resolve far away; choosing a specific search result
is necessary. Long waypoint labels are clipped in the narrow field. Walk/Bike
remain estimates over driving geometry, not dedicated routes for those modes.

## Device fixes and checks

- Added the shared plain TCP WebSocket transport to the HarmonyOS network
  backend. Studio commands and responses now traverse the phone's app socket.
- Added explicit, build-scoped Studio screenshot readback before EGL presentation.
- Replaced unsupported sandbox hard-link publication of approvals with a file
  lock and atomic rename. Existing approvals remain pinned and verified.
- Bundled nav seeding avoids privileged fixture transfers into a release app.
- Corrected cargo-makepad's hvigor argument boundaries: `--mode`, `-p`, and their
  values must be separate arguments. The launcher rejects debug HAPs.
- Reuses the existing HDC reverse port and checks HDC textual failures even
  when HDC returns exit status zero. Saves diagnostics for only the nav PID.
- Keeps the screen awake only for an explicit Studio review session.
- Preserves already-ready OpenGL shaders when polling compilation. The previous
  `take()` discarded `Ready`, causing the text helper to remain unavailable and
  request a full redraw forever. Build 34 traced these requests to
  `draw_text.rs:1711`; build 35 retained the shader and the screen settled.
- Clears the fullscreen pass dirty flag after drawing and makes decorative
  glass grain static, while retaining redraws for actual time-based shaders.
- Uses Label's layout area for widget queries, including vector-rendered text
  whose raster glyph area is empty.
- Resets layout and walk defaults when applying a complete generated View tree.
  Reused anonymous views had retained panel padding when they became simple
  columns, shrinking HOME to a single letter. Build 37 verified full HOME/WORK
  labels and aligned rows after saving and switching endpoints.
- Reserves 52 logical pixels above the route's northern endpoint when fitting
  the plan camera, accounting for its standing pin and a clear top margin.
  Build 38 verified the full destination pin above both direct and waypoint routes.

Two release approval tests passed (concurrent writers and restart/corruption).
The shared plain WebSocket round-trip integration test passed. The signed HAP
build and on-device bidirectional Studio interaction validate the OHOS backend.

## Performance follow-up

Build 31 instrumented samples across the interaction sequence:

| UI-thread phase | Samples | Median | Range |
| --- | ---: | ---: | ---: |
| Card render | 28 | 15.69 ms | 6.31–43.45 ms |
| Widget evaluation/application | 22 | 3.20 ms | 1.92–29.57 ms |
| Tap dispatch | 18 | 4.88 ms | 2.36–11.11 ms |

These mixed cold/warm phase samples are not frame presentation or tap-to-photon
latency. See [raw timings](nav-evidence/mate70-31-timings.json).

Further device profiling found a continuous redraw after each frame. Build 33
observed `redraw=true`, `next=0`, no dirty passes and no time-based shaders after
rendering. Build 34's caller trace identified `DrawText::slug_run_is_ready`:
OpenGL's compilation poll discarded completed shaders, leaving the text helper
permanently unready. Preserving `Ready` in the poll stopped this loop in build
35. The direct route and text still rendered correctly after the fix.

Comparable stationary navigation measurements used the same 18.9 km waypoint
route, flat view, zoom/recenter sequence and waiting-for-location state. No UI
input or screenshots occurred during either measurement window:

| Build | Window | Process CPU ticks | Ticks/second |
| --- | ---: | ---: | ---: |
| 31, before redraw fixes | 10.065 s | 774 | 76.90 |
| 36, after redraw fixes | 10.078 s | 198 | 19.65 |

This is a **74.45% reduction in process CPU work per second** in these samples,
not an FPS, battery-life or tap-latency result. See [before](nav-evidence/mate70-31-idle-cpu.json)
and [after](nav-evidence/mate70-36-idle-cpu.json). Idle CPU is reduced, not zero.
Per-thread attribution was unavailable because the device denied access to
`/proc/<pid>/task`.

The final build 38 repeated the stationary flat-view waypoint check after its
layout and pin-margin corrections: 200 CPU ticks in 10.070 s (19.86 ticks/s),
**74.17% below build 31**. [Final sample](nav-evidence/mate70-38-idle-cpu.json),
[measured screen](nav-evidence/mate70-38-navigation-idle.png).

Build 36's mixed interaction samples still included card-render work on the UI
thread: median 26.97 ms, range 4.76–64.27 ms; widget application median 3.77 ms;
tap dispatch median 11.50 ms. The render phase includes approval verification,
source resolution, realization, kit evaluation and DSL emission. It precedes
widget application and drawing. These samples have different action and cache
mixes from build 31 and do **not** demonstrate a tap-latency improvement. The
continuous shader redraw bug is fixed; synchronous card work and remote search,
route and tile loading remain sources of delay. [Phase samples](nav-evidence/mate70-36-timings.json)
