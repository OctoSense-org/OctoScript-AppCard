# Qwen3.8-27B + DFlash2 GPU validation — 8 September 2026

The RTX PRO 6000 Blackwell 96GB runs the pinned Qwen FP8 target and real
DFlash2 draft. The other supplied host is an **H100 80GB, not an H200**. It
reports CUDA error 802 and an unfinished GPU fabric; Fabric Manager cannot
query an NVSwitch. That host needs its GPU fabric initialized before inference.

## Matched inference result

Same 78,528-token final-generation request from the phone, temperature zero,
thinking disabled, concurrency one, same model revisions, FP8 weights/KV,
FlashInfer, and one GPU. Three warmed runs per arm:

| Metric | Target only | DFlash2 |
|---|---:|---:|
| Median completion | 44.208 s | 11.543 s |
| Median first content | 1.044 s | 0.979 s |
| Estimated decode rate | 41.4 tokens/s | 168.4 tokens/s |
| Output tokens | 1,787 | 1,787 |

Completion is **3.83× faster (73.9% shorter)**. All eight full-card outputs
(three baseline, five DFlash2) have the same hash, as does the short greedy
control. This establishes parity for these tested requests, not every prompt.
DFlash2 cold completion was 27.563 s. The first partial-cache reuse took
14.810 s; both are reported separately and excluded from the warm comparison.
Fully warm requests reused 78,464 of 78,528 prompt tokens (99.92%).

The replay measures the final inference request after the phone's initial tool
turn. Native end-to-end timing includes that turn and is reported separately.
Cache counters come from SGLang request histogram deltas: this runtime does not
fill OpenAI `prompt_tokens_details` unless cache reporting is enabled. Zero
cache fields in the phone provider log therefore do not mean zero reuse.

## Native phone validation

All four final-runtime captures pass the structural gate (inner widgets,
expected kit contracts, hidden loader, bounds within 2 logical pixels, and
unwrapped numeric labels). Screenshot review remains a separate result:

| Phone run | First text | End-to-end completion | Inner widgets | Visual result |
|---|---:|---:|---:|---|
| Weather / Taskplan | 7.324 s | 18.334 s | 126 | Pass for viewport |
| Stock / Camo light | 5.048 s | 15.998 s | 63 | Pass for viewport; some provider fields unavailable |
| News / Atro magazine | 7.950 s | 19.919 s | 111 | Not accepted: narrow, uneven cards; missing imagery |
| News / Atro wide rows | 5.196 s | 15.034 s | 128 | Not accepted: unwanted routing prose above card |

Weather repeated in 18.009 s on the same final runtime. The final standalone
launch (Studio display/keep-awake extras removed) completed in 17.453 s. Physical touch opened
its native `KitFormField`. Stock's native `KitTabBar` changed selected index
from 1 to 0, and realized `StockPlot` changed its range to `1d`. Studio mouse
clicks did not activate these phone controls; physical HDC touches were used,
with Studio snapshots to verify the resulting native state. This input-path
limitation remains separate from the working inspection path.

The initial target-only phone run completed in 68.083 s, but Studio rejected it
because a generated `# model: weather` header did not activate native kit
composition. The host now uses the language header parser for model/ledger
identity. The next attempt correctly failed because an old receipt pinned the
previous runtime. Explicit migration archived those receipts and re-admitted
cards through current policy. These earlier failures remain in the evidence.
The 68.083 s versus 18.334 s phone observations also differ in prefix state and
runtime fixes; use the matched inference A/B above for the measured speedup.

No whole-pipeline visual reliability claim follows from this benchmark. In
particular, the news variants are not visually accepted.

## Changes and reproduction

- Pinned the actual SGLang container/source and both model checkpoints.
- Resolve pinned local snapshots before SGLang's speculative-alias lookup.
- Explicit BF16 draft override prevents inheriting target FP8 quantization.
- Added a private-request replay helper with payload/output hashes, SSE timing,
  cache deltas, and detection of overlapping requests.
- Added optional OpenAI-compatible model routes to phone provisioning.
- Native kit composition accepts checked app-model headers.
- Explicit runtime receipt migration preserves previous records.

Open the [capture gallery](index.html).

See [generic launch instructions](../../../lab/demo/H200-DFLASH2.md),
[server configuration](server-config.json), [actual runtime](server-runtime.json),
[benchmark summary](benchmark-summary.json), and individual
[baseline](baseline.json) / [DFlash2](dflash2.json) observations.

Request bodies, keys, profiles and raw device logs remain outside the repository.
The server binds loopback. The current phone test route uses HDC reverse through
an SSH tunnel; it requires the USB/Mac relay. The embedded Octos core remains on
the phone. GPU serving is configured to restart with Docker.

This is a single-user, thinking-disabled test. Concurrent serving, thinking mode,
and a broad held-out design corpus have not been validated here.
