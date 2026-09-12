# Splash research templates on RTX PRO 6000

Tested 2026-09-09 America/Los_Angeles (2026-09-10 UTC).

**Live news update:** the [real pipeline](live-news/README.md) now runs live feed
discovery and article downloads, followed by actual RTX summaries and translation.
Those measurements include the network and model steps.

**News summarization update:** the [follow-up digest experiment](news-digest/README.md)
includes a real RTX model call for summaries and translation. The original
news latency table below measures retrieval and assembly and does not include
that work.

The standalone Splash language is suitable for small deterministic research
workflows in Octos One. The experiment uses three reusable templates and real
deferred capability calls, with a Rust host executing independent tools
concurrently. The native app has not been wired to these datasets yet.

## Environment

- Model: `qwen3.8-27b`, Qwen3.8-27B-FP8 target with DFlash2 draft.
- GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition, 97,887 MiB reported.
- Serving: existing SGLang container, FlashInfer attention, FP8 KV, 262,144
  context, `max_running_requests=1`. See [runtime settings](rtx-runtime.json).
- Host: Mac runs the Splash VM, adapter futures and model client; inference
  runs on RTX. H100 was closed by the user and was not used for this experiment.
- Splash checkout: `de2233f2e18c07bee64cf469f68073c9a8c2b0b9`, using local path
  dependencies and the experiment's Cargo.lock. The wider working tree has
  unrelated changes; no Splash engine code was changed for this experiment.

RTX initially ran FreeToken. It was idle; that container was stopped and the
existing `octos-qwen-dflash2` container started. SGLang is left running, with the
Mac tunnel `http://127.0.0.1:30881/v1` now pointing at RTX. This reuses the Mac
launcher's default endpoint after H100 shutdown. No new native UI run is claimed.

## Model comparison

| Research dataset | Parallel tool loop | Splash template | Speedup | Model calls |
|---|---:|---:|---:|---|
| Weather | 2.834 s | 1.171 s | 2.42× | 2 → 1 |
| Stock | 3.558 s | 1.250 s | 2.85× | 2 → 1 |
| News | 5.695 s | 1.580 s | 3.60× | 3 → 1 |

Medians of three repetitions per arm. All 18 final runs passed data comparison.
The selector generated 26–35 tokens; the complete tool loops generated 293–478
tokens across their calls. The templates were already authored; their source
generation cost is not included or needed on each request.

[Final measurements](rtx-model.json) compare a model-driven tool loop with a
single model call selecting and parameterizing a named Splash template. Both
arms use the same resolved request inputs, fixture tool results and delays, a
maximum of three simultaneous tools, greedy sampling, and disabled thinking.
The baseline is allowed to batch tools, removes exhausted tool capabilities,
and uses structured JSON output. The template selector has one shared response
schema containing all three templates and input alternatives; the expected
template is not supplied through a per-case response grammar.

Three repetitions per case/arm alternate arm order. The final JSON instances
are compared recursively against the same expected data; numeric comparison
allows only a small floating-point tolerance. Model time, output tokens, tool
batch sizes and template execution traces are retained in the JSON.

The elapsed time is request-to-complete-research-dataset. It includes the model
requests, fixture tool waits, Splash subprocess startup and validation where
applicable. It excludes L0 generation, app reference prefill, UI transport and
rendering. These are short synthetic research requests, not the earlier full
weather/stock/news app-generation benchmarks. The serving configuration does
not expose cache counts in these responses, so no cache-hit percentage is
claimed. There is no explicit cache flush between repetitions.

The successful baseline batches are `[2]` for weather, `[3]` for stock and
`[1,3]` for news. Splash is therefore compared with a baseline that already
parallelizes independent tools. Its advantage is avoiding follow-up model calls
and model-generated copies of tool data. A known admitted template binding can
also skip the selector call; that is a possible integration optimization,
separate from the model-inclusive measurements.

Earlier diagnostic trials are preserved: an unchanged tool catalog led to
repeated calls ([initial trial](rtx-model-unpruned-tools.json)); removing exhausted
tools allowed news to pass, but weather/stock final output was malformed
([unconstrained output](rtx-model-unconstrained-output.json)). The
[diagnostic response](tool-loop-diagnostic.json) shows weather emitting both the
schema and a dataset. A [per-case binding-schema trial](rtx-model-specific-binding-schema.json)
was also replaced by the shared-schema comparison to avoid giving the selector
an answer hint. Only `rtx-model.json` is the final latency comparison. Failed
diagnostic rows omit elapsed time and must not be treated as zero-latency runs.

## Tool scheduling and live reads

The Rust experiment executes the same template with host concurrency 1 and 3.
There are two warmups and five measured runs per mode, alternating mode order.
All outputs were ready. [Fixture traces](fixtures.json) and
[live Open-Meteo weather traces](live-weather.json) preserve individual results.

| Data workload | Sequential | Parallel | Speedup |
|---|---:|---:|---:|
| Weather, fixture | 604 ms | 363 ms | 1.67× |
| Stock, fixture | 787 ms | 352 ms | 2.23× |
| News, fixture | 809 ms | 465 ms | 1.74× |
| Weather + air quality, actual HTTPS | 556 ms | 274 ms | 2.03× |

The live trial ran on the Mac without a model call. Network conditions vary.
Source URLs and timestamps are retained; the live source's `retrieved_at` uses
the server HTTP Date. `first_adapter_result_ms` is a host-observed tool result,
not a validated native UI publication.

## Validation and reproduction

Five Rust tests passed. They cover dependency ordering, out-of-order completion,
stable results, bounded concurrency, optional failures/timeouts/schema rejection,
required failure, cancellation, and denied tool/input/call-budget violations.
Release Clippy with warnings denied passed. Python syntax compilation passed;
the model experiment exercises the real API and the `--once` Splash path.

The [experiment README](../../../tools/splash-research/README.md) gives runnable
commands. The [design note](../../SPLASH-RESEARCH.md) explains the intended
UI-contract integration and remaining work. Template source sizes: weather
411 bytes, stock 747 bytes, news 700 bytes, excluding host contracts/adapters.

The experiment does not implement progressive native snapshots, arbitrary
research synthesis, production stock/news adapters, generic DAG scheduling or
durable restart. Fixed orchestration does not make live evidence or model
interpretation deterministic. In particular, a stock return since news needs
event timestamp alignment, ticker resolution and coverage rules beyond this
previous-session-close example.
