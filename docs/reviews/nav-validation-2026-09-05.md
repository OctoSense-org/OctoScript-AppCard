# Nav validation — 2026-09-05

The canonical L0 nav card was exercised in Makepad Studio, and functional and
performance fixes were made. After renewing signing for `dev.makepad.octos_app`,
the signed release app was installed and visually exercised on the Mate 70 Air.
Device results and remaining limits are recorded in
[the handset follow-up](nav-mate70-validation-2026-09-05.md).

Studio used a dedicated persistent bridge on port 8002. Every app was launched
with `RunItem`; input, screenshots, widget queries, and build cleanup were scoped
to that run's returned build ID. Neither bridge sent `ObserveMount`. The other
debugger's Studio on port 8001 and its app were left alone. Final desktop build
16 remains available for review; final unsigned HarmonyOS packaging was build 17.

## Functional coverage

The target was [the shipping L0 exemplar](../../a2app-l0/apps/nav/exemplar.card),
rendered inside Octos, rather than the older L2 trip-planner example. Desktop
runs used a 398 × 850 logical viewport at 2× scale. GPS movement below is a
controlled replay, not physical travel. Saved-place tests used an isolated user
store at `/tmp/octos-nav-review-user.json`.

| Function | Result and evidence |
| --- | --- |
| Edit origin and destination; submit text | Passed in Studio. Commit closes the search panel. |
| Search and select a result | Passed. Five NVIDIA results with shared address labels remained distinct and selectable. [Screenshot](nav-evidence/search-results.png) |
| Named-origin route preview and GO | Passed. Saratoga High School → NVIDIA Santa Clara: 21 min, 15.5 km. [Screenshot](nav-evidence/direct-route.png) |
| Drive / Walk / Bike controls | Passed switching and persistence checks. Walk/Bike are duration estimates over driving geometry, not dedicated pedestrian/cycling routes. |
| Add, edit, and remove one stop | Passed. Apple Park changed the total to 29 min / 18.9 km, with 17 min / 10.5 km and 12 min / 8.4 km legs. One tap on the resting Remove control now removes it. [Via route](nav-evidence/waypoint-route.png), [removed](nav-evidence/stop-removed.png) |
| Start navigation through a stop | Passed. Follow map, remaining distance and instructions use the same waypoint route. [Screenshot](nav-evidence/drive-waiting-gps.png) |
| Current-location origin | Passed with replayed GPS, including a waypoint. Without GPS the card shows a waiting message and does not issue an invalid origin request. [With fix](nav-evidence/current-origin-waypoint.png), [without fix](nav-evidence/current-origin-waiting-gps.png) |
| GPS camera and instruction updates | Passed with the 64-fix replay. Following a stationary period, camera motion resumed; remaining distance changed from 18.9 to 18.5 km and the instruction advanced to South De Anza Boulevard. [Moving](nav-evidence/gps-replay-moving.png), [finished](nav-evidence/gps-replay-finished.png) |
| Zoom + / −, pan and recenter | Passed by Studio input and visual inspection. [Zoom in](nav-evidence/zoom-in.png), [zoom out](nav-evidence/zoom-out.png), [pan](nav-evidence/pan.png), [recenter](nav-evidence/recenter.png) |
| 2D / 3D | Passed both transitions. [Flat view](nav-evidence/flat-view.png) |
| Reveal End, then end trip | Passed. Returns to the plan and retains the selected stop. [Screenshot](nav-evidence/end-trip-revealed.png) |
| HOME / WORK save and reuse | Passed using the isolated store. Saved values survived subsequent app runs; selecting WORK recovered from the failed route in final build 16. |
| Rejected route and recovery | Passed in final build 16. Honolulu → Santa Clara receives a service rejection and now shows “No route found…” instead of staying pending. Selecting saved WORK then fetched a valid route and restored GO. [Before](nav-evidence/route-failure-before.png), [after](nav-evidence/route-failure-after.png) |

## Changes

- Search uses provider feature IDs, preserves distinct results that share an
  address, and removes actual duplicate features. Tap validation now uses the
  fetched rows that produced the displayed widgets.
- Map control helpers are defined before they are referenced by the kit.
- Source readiness is observed before guards are realized. A consumed fetch
  epoch no longer invalidates the same render again. Missing sourced state
  remains absent rather than becoming a false coordinate at zero.
- Unresolved and invalid waypoint coordinates do not issue route requests.
  Pending and failed route responses retain distinct lifecycle states.
- Current-location and named-origin waypoint branches pass the same waypoints
  to route totals, maps, progress and turn instructions. Destination submission
  clears the query. The Remove control has its own reachable tap target.
- Follow mode stops requesting frames when settled, wakes on changed GPS,
  finishes zoom/pan animations, and bounds interpolation after a long stationary
  interval. Missing GPS does not force a valid route preview to world zoom.
- Prefetching covers up to 1.6 km ahead of measured route progress and respects
  the shared request limit. Plan mode relies on visible tiles. It previously
  scanned and populated the entire route corridor.
- GPS epoch movement accumulates relative to the last published position, so
  repeated small movements eventually cross the threshold. Each changed valid
  fix can wake the camera independently of that threshold.
- HarmonyOS now has foreground location permission/request wiring, an ArkTS
  location callback into the Rust GPS store, and explicit Studio/review launch
  parameters. These paths compile; runtime lifecycle behavior awaits device
  validation.

## Performance evidence

Builds 13 and 14 used the same release configuration, viewport, waypoint route
and GPS replay. Build 13 temporarily restored continuous follow frames and the
old full-route prefetch for comparison. The optimized gate is restored in the
final source. Samples were collected during the initial stationary period;
the first `top` sample is excluded because it reports no interval CPU usage.

| Desktop process measurement | Baseline, build 13 | Optimized, build 14 |
| --- | --- | --- |
| CPU, two interval samples | 7.9%, 8.4% | 4.1%, 4.8% |
| Memory reported by macOS `top` | 1185 M, 1228 M | 1029 M, 1029 M |

Mean sampled CPU decreased about 45%. These are short desktop measurements,
not a device benchmark or a long-duration leak test. Memory remains high and
needs further profiling on the handset; the cache capacity was not blindly
reduced because active map geometry shares cache-owned resources.

The replay produced no card resolves after the initial route became available
until an explicit UI action. Four initial resolves in build 14 took
20, 27, 26 and 26 ms. The map and live text continued updating during movement.
Raw samples: [before](nav-evidence/perf-before.txt),
[after](nav-evidence/perf-after.txt). Older exploratory `idle-*` files are not
the comparison used above.

## Automated validation

| Check | Result |
| --- | --- |
| L0 profile integration suite | 266 passed |
| L0 waypoint lowering regression | 1 passed |
| Search identity, unresolved waypoints, rejected-route lifecycle | 3 passed |
| GPS cumulative movement / invalid fix regression | 1 passed |
| Map control helper resolution | 1 passed |
| Canonical exemplar matches tested fixture | 1 passed |
| HarmonyOS Rust + ArkTS release packaging | Passed; build 17 exited 0 |
| Shell syntax and whitespace checks | Passed |

The broader workspace suites are **not clean**. An earlier app L0 run had
42 passing tests, 6 failures and 2 ignored tests. The nav exemplar drift failure
was fixed and its targeted rerun passes. Five other failures remain in theme
expectations, helper coverage, missing-capability display and watchlist removal.
The broader widget suite had 97 passes and two widget-tree observation/patch
failures. Those cases are outside the nav changes and are recorded rather than
reported as passing; they were not established against a clean baseline.

Logs are under [nav-evidence](nav-evidence/), including
[L0 tests](nav-evidence/l0-tests.txt), [route/search tests](nav-evidence/search-tests.txt),
[broader app failures](nav-evidence/broader-app-tests.txt),
[broader widget failures](nav-evidence/broader-widget-tests.txt),
[Studio events](nav-evidence/studio-events.jsonl), and
[OHOS build output](nav-evidence/ohos-build.log).

## Mate 70 Air status and remaining validation

HDC confirms authorized device `5ZGYD25B13020968`, model `SUP-AL90`, product
`HUAWEI Mate 70 Air`, running `OpenHarmony-6.1.1.120`. The Octos leaf signing
certificate expires `2026-08-14 23:52:41 UTC`; signed packaging failed at SignHap
with the expired-certificate error. Another local current profile belongs to
`com.example.myapplication` and was not reused.

The final unsigned HAP is
`app/target/makepad-open-harmony/octos_app/entry/build/default/outputs/default/makepad-default-unsigned.hap`
(78,571,644 bytes). Its SHA-256 and device/build metadata are recorded in
[validation-metadata.json](nav-evidence/validation-metadata.json).

Renew automatic signing in DevEco for `dev.makepad.octos_app` on this device,
or supply a current signing configuration through `OCTOS_NAV_SIGNING_CONFIG`.
The prepared `octos-nav-mate70` Studio RunItem builds, signs, installs that bundle
and attaches its own build ID through the persistent bridge. Its device file
transfer and launch path still require runtime verification after signing.

Pending on the physical device: installation/startup, permission grant and
denial, live location, background/foreground resume, touch/pinch/IME behavior,
screen fit, sustained navigation memory and frame timing. Arbitrary multi-stop
lists, dedicated walking/cycling geometry, route-deviation rerouting and
destination-arrival behavior were not validated. The desktop End reveal also
scrolls the surrounding card slightly; this needs checking with physical touch.
