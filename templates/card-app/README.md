# Card app template (pointer)

A **card app** is an L0 `page.card` with its `page.data.json` and `kit/`,
lowered to widgets by the host. It is produced, not hand-written: use the
[image-to-card flow](../../flows/image-to-card/FLOW.md) (or the
[Sketch kit flow](../../flows/kits/sketch/FLOW.md) for a kit), then publish it
with [docs/PUBLISHING.md](../../docs/PUBLISHING.md), where the bundle carries
`page.card` + `kit/` instead of `main.splash`.

The metadata scaffold for a card bundle (manifest, listing, icon, agent
instructions) is App Hub's
[`templates/app/`](https://github.com/OctoSense-org/OctoSense-App-Hub/tree/main/templates/app).
For an app with its own logic, state and requests, use
[../script-app](../script-app/README.md) instead.
