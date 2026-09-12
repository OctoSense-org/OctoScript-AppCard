# Oil brief design revision

The oil example now opens with two readable news stories and a compact market
summary. A light theme, shorter headlines, clear source dates and selected tabs
replace the large dark cards. Headlines, Markets and Sources each fit within the
440 × 841 native window.

| Previous design | Revised design |
|---|---|
| ![Previous oil app](../cases/18/template/screen.png) | ![Revised oil brief](headlines.png) |

[Markets](markets.png) · [Sources](sources.png) · [Native interaction results](review.json)

This is an editorial revision of the saved case 18 dataset, retrieved September
10, 2026 at 09:02 UTC. It makes no new retrieval or generation-time claim. The
original 40-app measurements and screenshots remain the experiment record.
The Goldman story now points to the Invezz URL in the original news evidence,
instead of the unrelated MSN story. Dates use the saved feed timestamps.

The reusable [news-market L0 template](../../../../tools/splash-research/templates/composition/news-market.card)
uses the existing `sys.dataset` contract. Set its dataset ID when instantiating:

- `title` and `subtitle`: short masthead and explicit edition date.
- `pick2` and `pick3`: lead and outlook articles, including source labels and URLs.
- `metric1/2_label`: symbol and daily change; `metric1/2_value`: currency and price.
- `pick1_source`: quote session, currency and change basis.
- `pick1_title/body` and `summary`: market comparison and context.
- `coverage`, `as_of` and `evidence_title/body`: readable source notes.

All article content remains in the data; the card contains layout and navigation.
This additional template is available for reuse; the existing market template
and automatic composition routing have not been replaced.

Validation: both L0 cards passed the release checker. Makepad Studio build 104
rendered the saved dataset; Headlines → Markets → Sources → Headlines passed.
All three native screenshots were visually inspected. No native code or model
server was needed for this revision.
