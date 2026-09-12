# L0 app-card migration — 2026-09-09

All 11 registered app cards validate at L0. Unit conversion and saved-city
comparison now obtain their calculations from shared runtime capabilities.
Per-app `app.md` files remain developer documentation and are excluded from
both the combined and individual L0 generation prompts.

## Implementation

- `sys.convert` validates the unit pair and returns the input `amount` and
  converted `value`. The runtime owns all eight supported conversion pairs,
  including forward/reverse Celsius–Fahrenheit offsets. The card contains no
  coefficients or arithmetic.
- `sys.cities` returns temperatures and `feels_delta` in the requested unit.
  Differences are calculated before rounding; Fahrenheit differences use the
  scale without adding 32. Missing readings remain missing.
- Live `format: .ratio` bindings now retain runtime formatting. Numeric preset
  events preserve the control's declared value and type; text input such as
  `010` stays text.
- Initial connection and session-open notifications preserve a queued first
  reference. Explicit resumes and reconnects still invalidate cached state.
  Previously, startup could discard the reference record after submission and
  cause the second request to resend it.

The registered cards are weather, stock, news, activity, nav, chart, youtube,
convert, quake, weather-activity and city-picks. Their acceptance ceiling is L0;
the language's general L1 support remains independent of this app registry.

## Makepad Studio verification

Final validation used the persistent Studio bridge and release
`RunItem { mount: "octos", name: "octos-macos-mobile" }`, build **26**, at
440 × 841 logical pixels. Interaction used Studio `Click`, `TypeText` and
`Return`; screenshots and widget snapshots came from that same build. The
exploratory macOS native-click changes were removed.

| Native action | Observed result |
|---|---|
| Generate conversion for 20°C | Input 20; result 68.0°F |
| Swap | 20°F → −6.7°C |
| Select preset 10 | 10°F → −12.2°C |
| Swap again | 10°C → 50.0°F |
| Generate saved-city comparison | Live readings for Tokyo, San Francisco and Paris |
| Tap a city row | Absolute temperatures and feels-like differences switch to Fahrenheit; **zero additional weather fetches** |
| Add Vancouver | Fourth row loads live readings and persists to the dedicated test profile |

Only two model requests occurred: generating the converter and generating the
city card. All tested controls execute locally. Paris, added in an earlier
validation run, also survived the app restart.

![L0 converter](convert-celsius.png)

![L0 saved-city comparison after adding Vancouver](cities-added.png)

## Reference size and reuse

| Measurement | Submitted bytes |
|---|---:|
| Historical first prompt from the earlier cache review | 203,468 |
| First prompt after this migration | 150,698 |
| Next app request in the same session | **395** |

The first prompt is about **25.9% smaller**. These are UTF-8 message bytes,
including the request; the new stable reference prefix itself is 150,615 bytes.
The next app request reports `reference_cache_hit: true`, confirming reuse of
the accepted reference in conversation history. GPU KV eviction and cache-hit
rates are separate server measurements. This run is functional validation,
not a controlled before/after latency benchmark.

## Automated verification

All **296** targeted checks passed in release mode:

| Suite | Passed |
|---|---:|
| Shared unit calculations | 3 |
| L0 profile | 269 |
| Renderer, including one doctest | 11 |
| App migration and startup-race regression | 8 |
| Reference-cache behavior | 5 |

The checks cover all registered cards, prompt exclusion of prose specs,
conversion direction and offsets, unsupported/nonfinite values, live formatting,
numeric presets, missing weather values, cached-response reuse, and reference
invalidation on resume, reconnect, compaction and context pressure.

[Measurements and source hashes](measurements.json), [test commands and results](tests.json),
[temperature/cache checks](city-temperature-check.json),
[generated converter](convert.generated.card), and
[generated city card](city-picks.generated.card) accompany the native widget
snapshots in this directory. The earlier baseline is retained in
[the cache-speed review](../a2app-cache-speed/measurements.json).
