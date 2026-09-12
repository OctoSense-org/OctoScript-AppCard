# H100 latency optimization — 9 September 2026 UTC

The active Qwen3.8-27B-FP8 + DFlash2 server now uses Hopper-specific FP8
matrix kernels. Median warm weather-card completion fell from **8.340 s
to 6.644 s**, a **20.3% latency reduction**. The hardware
reports H100 80GB HBM3; no H200 was tested.

| Measurement | Original Triton path | Hopper DeepGEMM / swapAB |
|---|---:|---:|
| Warm repetitions | 4 | 3 |
| Completion median | 8.340 s | 6.644 s |
| Completion range | 8.218–8.543 s | 6.618–6.729 s |
| First content median | 0.987 s | 0.927 s |
| Decode estimate | 242.5 tokens/s | 312.4 tokens/s |

These fresh baseline and candidate samples use the same normal SSH route.
The earlier H100 result was 8.432 s; the fresh baseline above is the primary
comparison. Decode is `(output_tokens - 1) / (completion - first_content)`.

## What changed

- Enable DeepGEMM instead of the launcher's inherited disabled setting.
- Select `--fp8-gemm-backend flashinfer_deepgemm`. In the pinned SGLang source,
  this uses Hopper swapAB for token batches below 32 and DeepGEMM for larger
  prefill batches. DFlash2 verifies eight draft tokens per step.
- Compile actual kernel shapes on demand, with a persistent SGLang kernel cache.
  Disable the initial bulk precompile across unused batch sizes. First use of
  a new shape can still compile; this is not eliminated inference work.
- Enable `--enable-cache-report`, exposing real `cached_tokens` in API usage.
  This improves observability; cache reuse was already working before the change.

The target and draft revision pins, FP8 target weights and KV, BF16 draft,
FA3 attention, 262,144-token context limit, 0.75 memory fraction, block size 8,
single-request concurrency and fixed greedy payload are unchanged.
The new container is active with `unless-stopped`; the original container is
retained stopped for rollback.

## Validation and limits

The workload contains 78,528 input tokens, 62 tool definitions, and the complete
app context. Every full card contains 1,787 output tokens. All **18** full-card
observations across the baseline, kernel and transport tests have identical
payload hashes and byte-identical output. The short 50-token control also
matches the original server. Each measured request accounts for exactly one
server request; no overlapping traffic was counted.

Warm runs reuse 78,464 input tokens (99.92%); only 64 input tokens require new
prefill. The candidate's first app request took 12.200 s
with all 78,528 prompt tokens uncached. The next took 11.187 s
with 12,992 uncached tokens. Both are excluded from the warm median. The first
app request followed startup and a short control, and can include new-shape
compilation. It is not a measurement from a completely empty compiler cache.

An interleaved transport test produced 6.623 s
with normal SSH and 6.751 s with SSH compression,
three warm repetitions each. Compression showed no benefit and was not adopted.
Three requests made locally on the GPU host took 6.279 s
median, with 0.608 s to first content. That diagnostic
removes the client network route; it is not a replacement for the matched-route
baseline comparison.

This validates one fixed weather final-generation workload, not every theme,
app, sampling mode or concurrent load. Complete L0 output and parity checks
do not replace native structural/visual QA. The Mate 70 Air was disconnected
during this round, so the prior phone captures and 12.355–14.088 s timings
predate this optimization. No new phone speedup is claimed.

## Reproduce

Use the pinned [configuration](configuration.json) and
[generic launcher recipe](../../../../lab/demo/H200-DFLASH2.md).
Keep the request private and repeat it against each arm with
`benchmark_qwen_cards.py --arm dflash2 --repeats 5 --max-tokens 8192`.
Choose fully warm samples using the uncached-token counter, rather than
averaging cold and partial-cache samples into the warm result. Preserve the
same model pins, payload hash, route and sampling. Warm actual kernel shapes
and persist the compiled cache; confirm the runtime and process environment
match [runtime.json](runtime.json). Environment overrides take precedence.

Raw prompts, generated app text, credentials and machine connection details
are excluded. [Summary](summary.json), [baseline](baseline.json),
[kernel trial](swapab.json), [transport](transport.json),
[server-local diagnostic](server-local.json), [short control](control.json).

The kernel dispatch is verified against the
[pinned SGLang implementation](https://github.com/sgl-project/sglang/blob/5f55db35e926d50676f75b812640ea2410b0fe0e/python/sglang/srt/layers/quantization/fp8_utils.py).
