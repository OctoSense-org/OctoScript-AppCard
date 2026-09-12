# News summaries and translation through Splash

Follow-up: the [real news pipeline](../live-news/README.md) now performs live
RSS discovery and article downloads before the RTX model step. The measurements
in this document used fictional retrieval fixtures and remain historical.

2026-09-09 America/Los_Angeles / 2026-09-10 UTC. This extends the earlier
retrieval-only experiment with an actual model step on RTX PRO 6000.

The [news-digest template](../../../../tools/splash-research/templates/news-digest.splash)
runs a fixed sequence:

1. Search and obtain up to three article IDs.
2. Retrieve those articles concurrently.
3. Send successful articles to one bounded model capability, requesting summaries
   directly in the output language. Translation happens in that same response.
4. Validate the summaries and return them alongside the original article records.

The relevant Splash call is:

```splash
let resolved = try research.digest({articles: articles, language: request.language}).await() catch nil
```

`research.digest` is a registered host capability, implemented by the
[Rust model adapter](../../../../tools/splash-research/src/news_digest.rs).
It uses `qwen3.8-27b` with SGLang + DFlash2 through the RTX tunnel. The host fixes
the prompt, model, JSON output schema, 1,024-token output limit and 45-second
deadline. The model receives source text, title, language and article ID; it has
no tools. Original source URLs stay in the host dataset and are not generated
by the model.

The model returns `{language, items: [{id, summary}]}`. Validation requires the
requested language tag, bounded nonempty summaries, exact unique coverage of
the retrieved IDs, and no unexpected fields such as model-supplied URLs. A
coarse script check also rejects Chinese summaries with fewer than eight Han
characters, catching English-only text falsely labeled Chinese. That heuristic
is not a full language classifier or a semantic correctness check.

If no articles arrive, Splash skips the model call. If summarization fails,
times out, or produces rejected data, original articles remain available and the
dataset is partial. This is a batch of up to three articles because the current
RTX configuration permits only one running inference request; submitting three
model calls concurrently would queue them on the GPU. Retrieval remains parallel.

## Test scope

| Output language | Pipeline median | Model-call median | Pipeline range | Passed |
|---|---:|---:|---:|---:|
| English | 2.783 s | 2.317 s | 2.667–11.487 s | 3/3 |
| Simplified Chinese | 4.289 s | 3.823 s | 4.282–4.440 s | 3/3 |

All six final runs completed with one model call and three source-linked
summaries. The English 11.487-second outlier is retained. Its model phase took
approximately 11.02 seconds; server queueing and unrelated traffic were not
isolated, so the cause is not established. These are small-sample medians,
not a latency guarantee. English summary wording varied slightly across runs;
fixed orchestration does not imply byte-identical model output.

The model requests are real. Search/article tools use three explicitly fictional
[source articles](../../../../tools/splash-research/news-digest-fixtures.json),
including English and Spanish text. The English target therefore also tests
Spanish-to-English summarization; the Chinese target tests translation from both
source languages. This is not a live news feed or native app integration.

[Final measurements and outputs](rtx-results.json) contain three repetitions per
language in alternating order. Elapsed pipeline time includes fixture retrieval
delays, actual RTX summarization and validation. It excludes template selection,
UI generation, native rendering and subprocess startup before the internal
timer. The binding is already known in this experiment. Do not compare this
scope directly with the earlier 1.58-second selector-plus-retrieval news result,
which omitted summarization entirely.

No KV-cache hit rate is claimed: the server did not expose cached-token counts.
Diagnostic calls preceded the measured repetitions; no cache flush was applied.
Repeated latency on this small corpus does not establish production latency or
translation quality on arbitrary articles.

## Quality findings

The initial Chinese summary changed the source's water-loss quantity into a
water-loss rate. A generic prompt asking to preserve metric definitions did not
eliminate this. The experiment now supplies a small reviewed
[terminology glossary](../../../../tools/splash-research/news-digest-glossary.json)
for “water loss” and “library attendance.” This is a language/domain input, not
an additional model stage or a claim that an arbitrary glossary is complete.

A subsequent [diagnostic response](rtx-language-tag-diagnostic.json) returned
English summaries with a Chinese language tag. The prompt now names the output
language explicitly, and the runtime rejects this obvious mismatch. The
diagnostic's old `ready` status predates that check and is not an accepted final
result. Earlier [initial-prompt](rtx-results-initial-prompt.json) and
[metric-prompt](rtx-results-metric-prompt.json) trials are retained separately.

Review checks compare summaries against the supplied source text: bus quantities,
budget and conditional delivery; library pilot duration, budget and temporary
status; and water-loss comparison period and correlation/causation caveat.
Source IDs and provenance are retained separately. Structural validation does
not prove factual faithfulness, and this small manual review is not a general
translation evaluation or independent fact-check.

The final six outputs were reviewed against those fixture checks. Chinese
summaries used the approved quantity terms, converted the stated budgets to
1800 万美元, 24 万欧元 and 90 万美元 correctly where included, and preserved
the temporary library pilot and the water report's causation caveat. English
summaries preserved the key conditions and same-month comparison; some omitted
secondary details such as the water pilot's cost. This review checks faithful
condensation of the fictional source text, not whether the reported events
occurred. Minor wording roughness remains; no publication-quality claim is made.

## Reproduce

From the repository root, with the RTX endpoint already available:

```sh
cargo test --locked --manifest-path tools/splash-research/Cargo.toml --release
cargo build --locked --manifest-path tools/splash-research/Cargo.toml --release
tools/splash-research/target/release/octos-one-splash-research-experiment --news-digest zh-CN
python3 tools/splash-research/digest_bench.py --output /tmp/news-digest-results.json
```

Eight Rust tests pass, including dependency order, summary failure/timeout/schema
rejection preserving original articles, skipping inference when all reads fail,
duplicate/missing IDs, language-tag mismatches and English-only text under a
Chinese tag. Release Clippy with warnings denied and Python syntax checks pass.

The next native integration can show retrieved headlines while the digest is
running, then publish a validated summary snapshot under the same dataset ID.
That progressive publication is still proposed. An optional future summary
cache must include source content, output language, model, prompt and glossary
versions in its key so a language switch cannot reuse the wrong text.
