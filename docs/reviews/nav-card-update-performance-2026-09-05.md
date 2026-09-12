# Nav card update performance

Implemented and validated with release Studio RunItems on the debugger's own
persistent port-8002 bridge. Baseline build 19, optimized plan build 20, GPS
replay build 21, final desktop build 22, HarmonyOS package build 23. All queries,
input and stop requests were scoped to these builds; no mount observation was
sent. The other debugger's Studio and app were not controlled.

## Changes

- Cache immutable ledger syntax and validation by exact source, bounded to eight
  entries per thread and the existing maximum source size. Data, instance state,
  capability answers and durable approval records are not cached by this layer.
- Reuse a Cx-owned capability-probe VM with 64 compiled-expression slots and
  garbage collection. Probes execute on every call and no longer load the visual
  kit. Complete card evaluation still uses its own VM.
- Ledger taps apply state without generating a widget body that would be
  discarded. The draw path realizes/evaluates once; typing keeps its debounce.
  The legacy already-lowered-card path still requests an immediate body.
- Complete generated ledgers reuse one script body and reconcile their existing
  native View tree. Matching widgets survive; removed children are deleted even
  when a container becomes empty. Streaming scripts retain their existing path.
- Retained maps preserve user zoom when GPS changes and clear old route geometry
  when the route is removed or unavailable. GPS follow and live labels continue
  updating without regenerating the ledger card.

## Measurements

Same desktop release fixture, 398 × 850 logical viewport at DPI 2. Durations are
instrumented UI-thread phases, not frame presentation or handset measurements.
The table compares the same sequence: Walk, Drive, Add Stop. The initial Walk
preference save was slower in both runs and is excluded from the warmed rows.

| Phase/action | Before (build 19) | After (build 20) |
| --- | ---: | ---: |
| Card resolution following these taps | 19.7–20.3 ms | 3.3–3.6 ms |
| Source-query preparation within resolution | 16.6–17.1 ms | 2.0–2.2 ms |
| Ledger realization within resolution | 1.07–1.11 ms | 0.079–0.086 ms |
| Drive dispatch, including preference save | 14.99 ms | 5.79 ms |
| Add Stop dispatch | 7.74 ms | 0.79 ms |
| Widget evaluation/application after Add Stop | 1.33 ms | 0.98 ms |

Card resolution fell about 83% in these samples. Summing the measured Add Stop
dispatch, resolution and widget phases gives 29.37 ms before and 5.22 ms after.
That sum excludes event scheduling, layout, drawing and presentation; it is not
a measured tap-to-photon latency. Final build 22 repeated a 3.28 ms card resolve
and 0.83 ms widget application after selecting Walk while keeping the map zoom.

Cold startup still costs more: final build 22's seed resolution took 13.2 ms and
its first native widget evaluation took 14.8 ms. Preference persistence still
runs synchronously. Fetch-driven structural updates still use the existing
one-second epoch poll. Card state transitions still realize and evaluate once;
this change does not eliminate all DSL generation or port upstream's tile upload
budgets, retained draw submissions, label placement cache or archive workers.

## Validation

- All 283 `splash-ui-l0` tests passed in release, including approval/origin,
  parser diagnostics, profile limits, waypoint and new cache tests.
- The capability-probe test passed: repeated compiled calls read fresh values,
  expression churn stays within 64 bodies, and Cx instances own separate caches.
- Both native retention tests passed: map/group/label identity survives updates,
  labels receive new text, empty containers remove children, returning children
  get new identity, GPS changes preserve user zoom, and removing a route clears
  its geometry/progress state.
- Studio build 21 replayed 64 GPS fixes. Position and instructions advanced
  without card rebuilds between user actions. Verified 2D/3D switching, End,
  removing a waypoint, editing a destination, continued typing across result
  refreshes, and choosing the refreshed stable result key. Build 22 confirmed
  route loading, zoom, and mode changes after the last runtime edit.
- `git diff --check` passed for the touched runtime files.

Evidence: `nav-evidence/card-update-timings.jsonl`,
`nav-evidence/card-update-studio.jsonl`, `nav-evidence/card-update-*.log`, and the
`card-update-*.png` screenshots. Earlier full functional coverage and known
limitations are recorded in `nav-validation-2026-09-05.md`.

## Mate 70 Air

The connected device still identifies as SUP-AL90. Studio package build 23
completed successfully with the changes, producing:

`app/target/makepad-open-harmony/octos_app/entry/build/default/outputs/default/makepad-default-unsigned.hap`

SHA-256: `b0cdb460899fefc85c37820db52261d1299b3a2daa618e4ce9cf5a19680b7fb8`.

This packaging run was initially blocked by expired signing. Signing has since
been renewed for `dev.makepad.octos_app`; the signed release app is installed and
has been visually exercised on the phone. See
[the handset follow-up](nav-mate70-validation-2026-09-05.md) for device measurements
and remaining limits. The desktop timings above are not Mate 70 Air results.
