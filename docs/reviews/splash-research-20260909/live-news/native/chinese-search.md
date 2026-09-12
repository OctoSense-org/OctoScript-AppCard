# Chinese search and news-card routing

Validated in native Mac release build 37 through Makepad Studio on 2026-09-09
Los Angeles / 2026-09-10 UTC, using RTX PRO 6000.

The user's Chinese searches exposed two independent gaps. The news card sent
Chinese text directly to the English BBC/Guardian search indexes: both feeds
returned zero usable results for `加州高温` and `美国和伊朗最新情况`. Submitting
through the bottom composer then created a normal chat turn, replacing the news
screen with a prose response.

The Splash workflow now has a fixed conditional `research.query` step before
discovery. Queries containing non-ASCII letters are translated into bounded
English search terms by RTX. The model gets no tools; the host retains publisher
restrictions, freshness limits and source links. English queries skip this step.
A Chinese search uses two model calls when articles are found: query translation
and summary generation. The selected summary language remains the user's choice.
Translation failures stop the workflow and surface through the existing failure
state. They do not fall back to an ordinary chat answer.

The shell now offers composer input to the foreground live news ledger before
starting a chat turn. It locates that card's actual search controls and dispatches
through the same admission, event and user-input-origin checks as its Search
field. The current card stays live, with its chosen language and source bindings.
This only applies while the latest foreground message is a live news ledger.

## Verification

| Check | Observed result |
|---|---|
| CLI `美国伊朗最新冲突` | Translated to `US Iran conflict`; three articles, Chinese summaries, ready, 4.81 s |
| Card Search field with the same query | News cards visible in 5.05 s |
| Bottom composer `美国和伊朗最新情况` | News cards retained; two articles and explicit partial-coverage state |
| Bottom composer `美国伊朗最新冲突` | Three news cards visible in 4.73 s; window left on this result |

UI timings include submission, workflow, delivery, rendering and Studio polling;
they are individual observations on an open app. The card's displayed time is
only that dataset's pipeline duration (3.4 s on the final submission). Search
ranking remains lexical and broad queries may include indirect coverage.

[Final native screenshot](chinese-search.png). Private input/snapshot evidence is
in `/tmp/octos-live-news-native/iran-*-37.json`. The standalone evidence report
is [here](chinese-search-result.json), with article bodies redacted.

Sixteen standalone Rust tests and three L0 tests passed. Added coverage checks
that translation precedes discovery, a failed translation stops the workflow,
English queries skip translation, and Chinese field submissions retain user-input
origin and invalidate the news sources. Release Clippy passed for the standalone
tool. Both UI input paths were exercised in the newly rebuilt application.
