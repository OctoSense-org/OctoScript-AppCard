# Splash research experiment

Three small workflow templates executed by the standalone Splash VM, with a
bounded Rust host dispatching external tool promises concurrently. See the
[design](../../docs/SPLASH-RESEARCH.md) and
[measurements](../../docs/reviews/splash-research-20260909/README.md).

The [20-intent composition study](composition/README.md) adds live weather, AQI,
places, quotes and news-excerpt composition, five reusable L0 templates, and a
bounded native dataset snapshot binding. Its gallery and timings are separate
from the original three-workflow benchmark below.

`--live-news` runs the complete news pipeline against live BBC and Guardian RSS
feeds and article pages, then summarizes directly in English or Simplified
Chinese on RTX PRO 6000. Each run downloads fresh source data; it never substitutes
fixtures. See the [live results](../../docs/reviews/splash-research-20260909/live-news/README.md).

```sh
cargo build --locked --manifest-path tools/splash-research/Cargo.toml --release
tools/splash-research/target/release/octos-one-splash-research-experiment --live-news zh-CN technology
python3 tools/splash-research/digest_bench.py --live --topic technology --output /tmp/live-news.json
```

The live command accepts `en|zh-CN`, an optional topic or quoted search query
(1–160 characters), and an optional model base URL (default `http://127.0.0.1:30881/v1`). The
RTX tunnel must be running. Discovery reads both topic feeds concurrently,
filters to the preceding 72 hours using RSS publication timestamps, removes
duplicate URLs/titles, and selects up to three articles with both publishers
represented when available. Named topics are `technology`, `world` and `business`.
Other queries use two concurrent Bing News RSS searches restricted to BBC and
The Guardian. Only supported publisher article URLs are fetched, ranked by query
terms in the headline and search position before recency. This is limited publisher
coverage, without semantic grouping of articles covering the same event.

Queries containing non-ASCII letters first pass through a fixed RTX query
translation capability in the Splash template. It produces English search terms;
the UI keeps the user's original query. English queries skip that model call.
Chinese searches therefore use up to two model calls: query translation, then
article summarization. A failed translation stops the workflow explicitly.

The native Mac app now connects the [L0 news card](live-news.card) to this workflow
through the localhost [news bridge](news_server.py). Use the Studio runnable
`octos-macos-news`; see [launch instructions and UI evidence](../../docs/reviews/splash-research-20260909/live-news/native/README.md).
The app accepts typed searches, English/Chinese summaries, and source article
navigation. Both the card's Search field and the bottom composer submit to the
foreground live news card. Results are cached for 60 seconds per query/language; identical
in-flight requests are coalesced. The CLI itself still performs fresh requests.

Splash starts all article reads before awaiting their results, then invokes one
model call. The host extracts publisher article paragraphs, caps evidence at
6,000 UTF-8 bytes per article on paragraph boundaries, and retains the URL,
publication/retrieval times, evidence hash and truncation flag. Source text stays
inside the workflow; CLI reports contain summaries and provenance without
duplicating article text. Feed failures, missing/unsupported article bodies,
and model failures produce explicit partial results. Check `output.status` and
the trace, even when the process exits successfully. Empty discovery skips
inference. Each HTTP response is capped at 2 MiB and has a 15-second timeout.

The [news-digest template](templates/news-digest.splash) adds one
real model call after parallel retrieval. It summarizes directly in English or
Simplified Chinese, translating source text as needed in that same call. The
test corpus contains English and Spanish fictional articles. Source IDs and
original provenance stay in the dataset; model output supplies summaries only.

From the repository root:

```sh
cargo test --locked --manifest-path tools/splash-research/Cargo.toml --release
cargo run --locked --manifest-path tools/splash-research/Cargo.toml --release > /tmp/splash-fixtures.json
cargo run --locked --manifest-path tools/splash-research/Cargo.toml --release -- --live-weather > /tmp/splash-live.json
python3 tools/splash-research/model_bench.py \
  --base-url http://127.0.0.1:30881/v1 --model qwen3.8-27b \
  --fixture-results /tmp/splash-fixtures.json \
  --output /tmp/splash-model.json
cargo run --locked --manifest-path tools/splash-research/Cargo.toml --release -- --news-digest zh-CN
python3 tools/splash-research/digest_bench.py --output /tmp/splash-digest.json
```

The default Rust benchmark uses fixture data with controlled asynchronous
delays. `--live-weather` uses real, bounded Open-Meteo HTTPS reads. The Python
benchmark uses a real model, the same fixture tools in both arms, and the built
Rust executable for the template arm. It allows the tool loop to issue parallel
calls, removes exhausted tools, and constrains final JSON against a schema.
It requires no Python packages. The model endpoint must already be reachable.

`--once CASE INPUT_JSON_FILE` runs one built-in template against its exact
fixture parameters. It refuses other inputs rather than returning synthetic
data for a different request. This command supports the model benchmark; it is
not a production arbitrary-location/symbol query service.

`mod.research` is a host-defined facade in this experiment. Templates use real
Splash syntax and capability APIs. They are research programs, separate from
L0 UI cards; loading them into a UI renderer would not install their tools.

The host owns tool policies, JSON schemas, concurrency, cancellation and final
validation. The digest model has a fixed prompt, a 1,024-token output budget,
a 45-second deadline and no tools. The workflow skips it when no articles were
retrieved; a failed summary leaves the original articles available with partial
status. Target-language tags, article coverage and schemas are checked; a coarse
script check also rejects English-only summaries tagged Chinese. A small
host-provided glossary controls the tested Chinese terminology. However,
those checks alone do not prove factual faithfulness or translation quality.

The original three-workflow benchmark does not implement native dataset bindings or partial UI publication,
cross-source fact-checking, durable workflows, a generic DAG scheduler, or
production stock retrieval. Live news has adapter-owned schemas and source
validation; other fixture schemas demonstrate the executable boundary. The
publisher-specific extraction rules cover supported page layouts and report
unsupported/blocked pages instead of summarizing their headline alone.
