# RTX PRO 6000: native Mac A2App cache comparison

2026-09-09. The same Mac weather → stock → news sequence was repeated against
the NVIDIA RTX PRO 6000 Blackwell Server Edition (97,887 MiB), using the
existing Qwen3.8-27B-FP8 + DFlash2 SGLang container. Both arms used the same
release app binary as the final [H100 trial](../README.md). Reference reuse
was disabled for the baseline and enabled for the optimized run; both arms
contained the earlier streaming and document-evaluation fixes.

Across five follow-ups, median submission-to-card time fell from **36.32 s
to 11.45 s (68.5%)**. Weighted server KV reuse rose from **48.49% to 99.64%**.
All six requests in each arm loaded native cards and populated primary data
in one model call each.

| Follow-up request | Reuse off: card appears | Reuse on: card appears | Reuse on: primary data ready | Off: KV reuse | On: KV reuse |
|---|---:|---:|---:|---:|---:|
| AAPL stock | 29.77 s | 11.45 s | 11.52 s | 60.48% | 99.66% |
| Technology news | 33.98 s | 10.22 s | 10.63 s | 71.99% | 99.55% |
| San Francisco weather | 47.33 s | 12.04 s | 13.70 s | 0.00% | 99.61% |
| NVDA stock | 36.32 s | 11.73 s | 12.10 s | 72.11% | 99.75% |
| News requested as business | 41.79 s | 10.26 s | 10.33 s | 19.44% | 99.64% |

Median first text fell from **24.43 s to 0.84 s**. Uncached input across the
five follow-ups fell from 415,391 to 1,556 tokens. The baseline compacted
twice in six requests; the optimized conversation had zero compactions
through a seventh request used for chart interaction checks.

The existing client optimization worked without further application changes.
After the initial full reference, each optimized submission contained
573–607 bytes of request/theme guidance instead of approximately 203 KB.
Wire inspection confirmed one complete reference remained in conversation
history. The full history still travels to the provider; SGLang reuses its
cached prefix on the GPU. This distinguishes client reference reuse from
server KV reuse.

## Comparison with H100

| Optimized follow-ups | H100, earlier trial | RTX PRO 6000 |
|---|---:|---:|
| Median card appears | 6.76 s | 11.45 s |
| Median first text | 0.78 s | 0.84 s |
| Weighted KV reuse | 99.78% | 99.64% |

RTX's median card time was 1.69× H100's in these runs. First-text latency was
close after prefix reuse; most remaining elapsed time was between first text
and completion of the roughly 1,600–2,000-token card response. This is a
comparison of the deployed configurations: H100 uses FA3 attention and RTX
uses FlashInfer, with GPU-specific kernel differences. It does not isolate
hardware throughput. Generated outputs also differed slightly despite the
same prompts and temperature zero.

Both used SGLang `0.0.0.dev1+g5f55db35e`, a 262,144-token context,
`fp8_e4m3` KV cache, radix caching enabled, eight DFlash draft tokens,
`mem_fraction_static=0.75`, and one maximum running request. Target revision
was `017b9c7af6b5689d5dd426a76e0bc077eb5ca20a`; draft revision was
`50307d4c4cde6860d4eee73e2547cd786fe8e8a4`.

## Local chart cache

After generating AAPL again, native clicks selected 1W → 1D → 1W. Binding
updates were observed in **186, 212 and 173 ms**. All three actions made
**zero LLM requests**. The first two selections each issued one chart-data
request; returning to 1W issued **zero new data requests**. The final chart
remained populated. These measurements include Studio polling and indicate
binding updates, not network completion for an uncached range.

## Method and limits

The client was the Apple M3 Max MacBook with 128 GiB RAM and macOS 26.5,
running a 440 × 841 native window. The persistent Makepad Studio bridge
launched `octos-macos-mobile` and drove the real composer with `Click`,
`TypeText` and `Return`. Measured builds were 9 and 10. WidgetTreeDump,
WidgetSnapshot, generation lifecycle logs and screenshots verified the
mounted cards, hidden generation overlay and non-placeholder primary values.
A transparent local proxy recorded streaming usage from the RTX SSH tunnel.

Each arm used a fresh dedicated app/core profile and the sequence Tokyo →
AAPL → technology news → San Francisco → NVDA → business news. The initial
Tokyo request is excluded from comparative metrics: its baseline card took
28.51 s and optimized card took 12.01 s, with different server cache warmth.
There was one sequence per arm and no forced KV eviction between arms, so
the optimized arm could also benefit from prefixes cached during the first.
These are running-app generation/load times, not application startup or a
cold-GPU benchmark. The prior H100 baseline also preceded renderer fixes;
the two RTX arms share those fixes.

Cache percentages use `cached_tokens / prompt_tokens`, weighted by input
tokens over the five follow-ups. Cache reporting was enabled in both
measured arms. The installed SGLang implementation returns null cache
details when its cached count is zero (`UsageProcessor._details_if_cached`),
so those nulls count as zero. An exploratory run before enabling reporting
was excluded.

Primary-data readiness checks the main temperature, price or headline. It
does not wait for every image or optional stock field; satellite imagery
and stock volume, market cap and P/E were still absent in the captures.
The business request still used Hacker News, so it does not demonstrate
business-specific coverage. RTX news captures rendered light; earlier H100
captures rendered dark for the same “Atro light” wording. Category and exact
theme correctness are outside the load checks.

## Evidence and restoration

[Measurements](measurements.json) contain all twelve measured requests,
cache usage, request hashes, submitted bytes, reference counts, runtime
settings, context-ledger summaries, the extra AAPL request and chart actions.
Captures: [weather](weather.png), [stock](stock.png), [news](news.png),
[stock range cache](stock-range-cache.png). PNG data was recompressed
losslessly with identical decoded bytes. Native trees are included alongside
the first three captures. The private harness and wire traces remain in
`/tmp/octos-a2app-speed-20260909`.

The release binary SHA-256 was
`5260febc9d672cdf3e9593ea53030ba72baa65e96304ac7ecd6f91dcbc525463`,
matching the final H100 trial. Studio reused this binary with `skip_build`
because no source changes were made. Reproduction uses a fresh `state_dir`,
the RTX SGLang `model_base_url`, and `disable_reference_cache: true` for the
baseline; omit the disable flag for the optimized arm. Rebuild through the
Studio RunItem after any source changes.

RTX was initially idle with `octos-qwen-freetoken` running. That service was
temporarily stopped and the existing `octos-qwen-dflash2` container started.
Its launcher temporarily gained `--enable-cache-report` so native requests
could report their cache counts. No inference kernel settings were changed.
After testing, the launcher was restored byte-for-byte, DFlash2 stopped,
and FreeToken restarted and checked for health. These native measurements
therefore describe SGLang + DFlash2, not FreeToken.

The Mac was returned to its direct H100 connection in Studio build 11, with
a live Tokyo weather card verified. The temporary RTX request observer was
stopped. Restoration details are recorded in `measurements.json`.
