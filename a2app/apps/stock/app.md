# Stock app

**One** dark, iOS-Stocks-style splash app that holds BOTH a top-gainers **list**
and a per-ticker **detail** view, with **client-side navigation** between them (no
LLM round-trip). Use it for any stock/market request ("top 10 stocks", "movers",
"best performers", "AAPL", "Tesla stock", "英伟达股价").

The client renders this app directly from a fixed TEMPLATE
(`exemplars/stock-movers.splash`) — you are **not** asked to generate it. The
template is the source of truth; this doc explains how it works.

## One card, two views, client-side navigation

The card is a **full-script** Splash body driven by one state key, `selected`:

```
let sel = "{{state.selected}}"
if sel == "0" || sel == "" { <LIST view> } else { <DETAIL view for `sel`> }
```

- `{{state.selected}}` is the app-side card state (default `"0"` when unset →
  the LIST shows first).
- **Tap a list row** → `agent.notify("set", {key: "selected", value:
  sys.movers(i, "symbol")})`. The app writes the state and re-renders → the `if`
  flips to the DETAIL branch for that ticker. **No LLM call.**
- **Detail back button** (`"‹ Movers"`) → `agent.notify("set", {key: "selected",
  value: ""})` → re-render → back to the LIST.

Because the detail branch uses the VM variable `sel` as the ticker, every detail
field is `sys.stock(sel, "…")` / `sys.stockbar(sel, i, 68, 114)` — the SAME view
serves every stock. The `else` branch is only evaluated once a row is tapped, so a
stock's data isn't fetched until you open it.

## LIVE DATA — MANDATORY (all fetched by splash code)

- LIST rows: `sys.movers(i, "field")` — Yahoo day_gainers, ONE fetch for all 10
  rows. Fields: `symbol`, `name`, `price`, `change`, `changepct`, `high`, `low`,
  `marketcap`, `vol`, `52wh`, `52wl`, `currency`, `exchange`.
- DETAIL: `sys.stock(sel, "key")` (`symbol`, `name`, `exchange`, `currency`,
  `price`, `prev`, `high`, `low`, `52wh`, `52wl`, `vol`, `change`, `changepct`)
  and the chart `sys.stockbar(sel, i, 68, 114)`. **Do NOT use `open`** (Yahoo
  omits it → `$—`). Nothing is hardcoded; the LLM never writes a number.

## Notes

- Full-script mode requires the body (after the stripped `// name:` line) to start
  with `let` — keep NO other leading comments.
- The default `{{state.selected}}` is `"0"`, so the LIST condition tests
  `sel == "0" || sel == ""`.
- Tappable rows: a transparent `Button` overlaid on each fixed-height row; the
  detail chart is a gridlined translucent-green area with a left Y-axis, a range
  selector, and a frosted stat grid (see the exemplar).
