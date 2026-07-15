# News app

A polished, dark, **iOS-News-style top-stories app** for Hacker News. Use it for
headlines / what's happening / top news ("top news", "头条", "what's
happening"). Its canonical card is `exemplars/news-canonical.splash`.

## OUTPUT CONTRACT - FOLLOW EXACTLY

Your entire answer MUST be exactly one `runsplash` fenced code block. Its opening
line must be three backticks immediately followed by `runsplash`, with no leading
whitespace; its closing line must be exactly three backticks. Never emit a
`splash`, `rust`, `text`, or unlabeled fence, and never emit raw DSL, because
those render as source code instead of an interactive app. Do not write prose
before or after the fence.

For a News request, copy the complete interactive structure of
`exemplars/news-canonical.splash`. It is a known-good, template-based Splash app,
not merely visual inspiration. Preserve its state, `StoryRow` template,
list/detail helpers, eight live bindings, fixed shell, and interactions.

- The first executable line after `// name:` MUST be
  `let news_app = { detail: false selected: 0 }`; no comment may precede it.
- Define only the exemplar's `StoryRow` and `RowTap` style templates, then
  instantiate them for seven rows. Each `StoryRow` supplies its live `View` and
  `Label` children directly: nested overrides are ignored, while extra base
  `View`/`Label` prototypes leak defaults into unrelated widgets in this embedded
  renderer. Do not replace rows with a metrics table.
- Finish with one `SolidView` root using `width: Fill`, `height: 780`, and
  `flow: Overlay`. Keep the masthead, page title, 240dp lead card, and section
  label fixed; put only the seven story rows in a `ScrollYView` whose height is
  `Fill`. This preserves the old-template browsing density while keeping detail
  and Back visible at every feed offset.
- Use only `sys.news(NUMERIC_INDEX, "KEY")`. Never use path-style calls or keys
  such as `source`/`published`.
- Every story card has a transparent 72dp-wide, full-height `ButtonFlatter`
  aligned with its trailing chevron. This gives a generous action target while
  leaving the headline body available for vertical feed swipes. Never use a
  full-card button inside `ScrollYView`, because it captures drag gestures.
- Navigation is entirely Splash-local: `show_story(index)` opens detail and
  `show_list()` returns. Never use `agent.notify` or native host handlers.
- Detail keeps the selected story in the lead card and shows its live title,
  URL, author, points, and comment count. The dense story rows remain below under
  `TOP STORIES` and continue to open their corresponding details.
- Before emitting, verify the output contains `let StoryRow`, `let RowTap`,
  `height: 780`, `ScrollYView`, `fn show_story(i)`, `fn show_list()`,
  `sys.news(0, "title")`, and
  `sys.news(7, "title")`.

## LIVE DATA - MANDATORY

Every title, author, score, comment count, and URL comes from
`sys.news(index, "key")`; index 0 is the top story. Never invent story data.
Values may show `—` briefly before the live feed refreshes.

Keys: `title`, `author`, `points`, `url`, `comments`.

## UX STRUCTURE

Keep the complete generated block below 8,000 bytes so streaming remains
reliable.

1. **Masthead** - a full-width 44dp `ButtonFlatter` reading `TOP STORIES` over
   the restrained page title `Hacker News`. In detail it becomes
   `< Top Stories`, providing a large Back target.
2. **Lead card** - a prominent rounded card for index 0 with a 20pt wrapping
   title and live points/comments/author metadata. In detail it becomes the
   selected story and adds the live URL.
3. **Dense feed** - a `ScrollYView` holds seven `StoryRow` instances for indexes
   1..7. Each 136dp card has rank, 12pt wrapping title, 9pt metadata, chevron,
   and a transparent 72dp-wide, full-height trailing button. The headline body
   is the swipe surface. Never scroll the masthead or lead card with the feed.
4. **Detail continuity** - change only masthead, page title, lead content, and
   section heading. Keep the same feed below so users can continue browsing and
   switch stories without returning first.

Use a charcoal/black surface, restrained warm tint, orange accent, white primary
text, and muted gray metadata. Cards use an 8px radius and must not nest.

Widgets: GradientYView, SolidView, RoundedView, ScrollYView, View, Label,
ButtonFlatter.
