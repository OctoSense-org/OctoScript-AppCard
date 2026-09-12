# Octos on Mate 70 Air — 8 September 2026

The signed release app was updated on the connected Mate 70 Air (SUP-AL90).
It runs Octos **2.0.3-rc.11**, based on upstream revision
`02e773eab26a13fe525c3d1b5b1a4da541c63cfb`, with the mobile compatibility and
cache-prefix changes in this working tree. The core runs inside the native app
through canonical OUP; it does not require a Mac-hosted Octos server.

[Open the six-variation gallery](index.html). Every screenshot is the native
Makepad implementation on the phone. Rejected captures remain beside their
replacements with `superseded_by` in `result.json`.

[Fresh cache and theme verification](kv-theme-verification/README.md) repeats
four generations on the unchanged final build. It confirms 99.92% cache reuse
for identical input and measures 15.0 → 11.3 s to first text and 35.8 → 33.0 s
to completion with inference settings held fixed. It also records native layout
differences and the limits of the speed and variety claims.

## Generation and KV reuse

The shared language, all app references, native page compositions and theme
vocabulary precede the varying context. Preferences and supplied time of day
are appended after that reference. The provider-normalized system/tool hash
was identical across all seven benchmark contexts; see
[the fingerprints](provider-prefix-proof.json). KV reuse occurs at the model
provider. The phone caches rendering state and resources separately.

The same Taskplan weather prompt measured **88.2 s to first text / 105.3 s to
completion** with provider-default inference, versus **10.8 s / 30.2 s** for
its fast-mode repeat. The repeat reused **73,088 of 73,102 input tokens**.
This is an observed comparison, not an isolated cache benchmark: fast inference,
output length, automatic repair, provider load and network timing also matter.
The initial fast-mode request with zero cache reads reached text in 10.6 s,
but required one repair and took 53.9 s overall.

| Benchmark context | First text | Total including repairs | Repairs | Cached input |
|---|---:|---:|---:|---:|
| Weather / Taskplan morning | 10.6 s | 53.9 s | 1 | 49.4% across both turns |
| Weather / Camo night | 11.1 s | 55.2 s | 1 | 92.2% across both turns |
| News / Atro light magazine | 11.9 s | 30.1 s | 0 | 86.8% |
| News / Taskplan compact | 13.6 s | 28.7 s | 0 | 86.8% |
| Stock / Atro dark chart | 11.1 s | 30.5 s | 0 | 99.9% |
| Stock / Camo light tiles | 12.4 s | 33.8 s | 0 | 86.7% |
| Identical Taskplan weather repeat | 10.8 s | 30.2 s | 0 | 99.98% |

Median total time was **30.5 s**. These seven runs used one installed fast-mode
package, before the subsequent visual repairs. Their measurements are preserved
in [benchmark.json](benchmark.json) and [baseline.json](baseline.json).
The gallery shows replacement captures where QA required a repair; each has its
own timing and build ID. Editing the shared reference invalidates that prefix,
so a subsequent first request can report zero cache reads.

## Changes and validation

- Linked the current core into HarmonyOS. Executing a bundled binary was denied
  by the app sandbox; the native library uses the canonical embedded OUP path.
  The mobile configuration skips desktop HTTP bearer/keychain initialization.
- Preserved the static prompt prefix across contexts, exposed all 11 theme IDs
  and six weather/news/stock page compositions, and enabled fast inference by
  default when saved model/gateway preferences do not override it. Explicit
  GLM thinking-disable settings now reach the provider.
- Applied backpressure to streamed text instead of dropping fragments. Handled
  canonical v2 completion/error events so a finished card clears the spinner.
  Carried full provider token usage through the core completion path.
- Cached unchanged L0 validation results, preserving revalidation whenever the
  source changes and reducing redundant parsing and diagnostic output.
- Repaired selected Taskplan button ink, cramped news metadata guidance,
  wrapped stock-price guidance, and native chart axis colors on light themes.
- Fixed retained native Image widgets failing to reload after `src` changes.
  On the phone the initial unresolved satellite URL failed; the later correct
  NASA URL now decodes and displays. See the
  [scrolled satellite capture](weather-taskplan-final/satellite-scroll.png).

Studio WidgetTreeDump, WidgetQuery and WidgetSnapshot record hierarchy, bounds,
text, visibility and control state. Captures require a completed turn, hidden
loading overlay, inner native widgets, the expected kit identity, horizontal
bounds within **2 logical pixels**, and no wrapped numeric values. The numeric
height allowance is `max(24, 2.25 * nominal_font_size + 2)` logical pixels,
accounting for measured native small-font metrics and rounding. Vertical content
outside a scrolling viewport is expected. Screenshot review remains a separate
step: it caught problems that the original bounds-only gate did not.

Observed interactions: weather's native + button opens the city input; the news
AI button adds a topic row, fetched headline and Remove control; the stock range
bar changes its selected index from 1M to 1W. The stock graph is the native
**StockPlot** backed by PlotView and Yahoo series data, with **KitTabBar** controls.
Weather/news use native labels, images and **KitButton** compositions retaining
Taskplan/Atro/Camo source-component identities and fonts.

Checks passed: stable-prefix/theme-vocabulary contract; two terminal lifecycle
regressions; three rendering regressions (validation invalidation, selected ink,
plot axis ink); lossless transport under a slow consumer; 60 provider tests.
The final Image change was validated by the native URL-change/decode sequence
and screenshot on the phone. Provider data can omit financial fields, which
remain dashes; the news feed has no image URL, so its lead is typographic.

A final launch with no Studio connection also completed through the embedded
core: **12.0 s to first text, 35.6 s to completion**, zero reported cache reads,
and no repair turn. The [full phone capture](standalone-run/screen.jpeg) shows
Tokyo's populated forecast and current conditions with the loading overlay
cleared; sunrise/sunset values were still unavailable. See
[standalone verification](standalone-run/verification.json). An earlier run
auto-locked during streaming and resumed UI delivery after foregrounding;
its suspended time is excluded from the speed comparison. Studio review mode
keeps the screen awake; normal use retains the phone's screen timeout.

The Camo weather screenshot has a repeated condition label, a minor remaining
content-layout issue. These captures establish tested theme variation and native
behavior at this phone size, not acceptance of every future generated layout.

## Reproduce

Follow [the generic deployment instructions](../../../tools/OCTOS-OHOS.md).
Prompts are in [contexts.json](contexts.json); repair prompts are saved in the
individual results. Builds and launches use Studio RunItem. The report includes
no provider keys, signing material or raw device/build logs.

Generate the gallery with:

```sh
python3 tools/octos-ohos-gallery.py docs/reviews/mate70-generation-20260908
```

[Installed build hashes](installed-build.json) and
[source hashes](source-hashes.json) identify the reviewed implementation.
Z.ai documents [automatic cache recognition and usage counters](https://docs.z.ai/guides/capabilities/cache)
and [per-turn thinking controls](https://docs.z.ai/guides/capabilities/thinking-mode).
