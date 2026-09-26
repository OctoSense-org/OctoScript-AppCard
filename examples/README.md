# Apps

Runnable apps built with the image-to-appcard pipeline live in `apps/<name>/`.
Each app owns its service code, reviewed card scenes, design source, launcher,
tests and fixture evidence. App runtime state and personal data stay ignored.

| App | Platform | Description |
| --- | --- | --- |
| [Aircon](aircon/README.md) | Native cards / WASM | One purchase-to-installation journey with 12 screen states and 14 extracted service-card variants. |
| [Mail](mail/README.md) | OctoSense system script app | Accounts, folders, reading and sending through the `mail` host service; the app never holds a socket or a password. |
| [School](school/README.md) | Native cards / WASM | School notice, calendar and payment journey. |
| [Health](health/README.md) | Native cards / WASM | Fictional health-check booking journey. |
| [Reunion](reunion/README.md) | Native cards / WASM | Reunion planning, RSVP and payment journey. |
| [personal-data](personal-data/README.md) | octos skill (macOS, Android later) | Read-only search over the Mail and Calendar apps' data for the octos agent: `mail_search`, `mail_read`, `calendar_query`, `contacts_lookup`. Phase 1 of the octos personal-memory ADR. Its Mail source reads the removed native Mail module's `mailbox-*.json`; it needs the mail host service's store instead. |
| [Calendar](calendar/README.md) | Native cards / browser preview + sync server | iOS-style calendar for two devices: 10 screens, 4 service cards, and a SQLite-backed operation-log server every client replays. |

## System script apps

`apps/<name>/script/` is an app as a contained script bundle (`manifest.json`,
`main.splash`, small artwork): what OctoSense ships as a first-party system app
(`os.<name>`, OctoSense ADR 0004) and what a contestant's or publisher's app
looks like. The OctoSense shells (the ROM's Home, the desktop shell) pin this
repository and choose which bundles to include; App Hub's Card runner runs each
in its own isolate under its manifest's policy. An app's `host-service/` is the
Rust service its script calls through `host.request` (Mail keeps accounts and
passwords there), and `native/` is the earlier native module, kept for
comparison.

| Script app | Id | Needs |
| --- | --- | --- |
| [News](news/script/main.splash) | `os.news` | `storage`, `net` (feed hosts), `images`, `web` |
| [Photos](photos/script/main.splash) | `os.photos` | `storage`; the shell mounts its sample library as `{{assets}}/photos` |
| [Maps](maps/script/main.splash) | `os.maps` | `storage`, `net` (map and route hosts), `location` |
| [Camera](camera/script/main.splash) | `os.camera` | `camera`, `microphone`, `library`, `storage` |
| [Mail](mail/script/main.splash) | `os.mail` | `storage`, `mail` (the [mail host service](mail/host-service)) |

All projects are siblings here; `personal-data` is a plain Rust skill rather than an AppCard journey. The repository root is
`Octosense-Service-AppCards/`; there is no nested `pipeline/` checkout.
Makepad and Octoscript live in the separate [native workspace](../docs/NATIVE-WORKSPACE.md).
[shared/](shared/README.md) contains common browser adapters and historical
cross-app verification artifacts, not another application.

Within an app, `cards/` holds full screen states. For example,
`aircon/cards/aircon-01` through `aircon-12` are twelve screens of **one Aircon
app**, not twelve apps. `service-cards/` holds smaller interactive panels
extracted from those screens—an order, installation appointment, calendar update
or payment panel—with their own data and actions. Their owner names identify
services within the journey, not additional app projects.

Each app keeps its design source, scenes, service code and
`image-to-appcard-flow.json` together. Run the shared pipeline from the repository
root, choosing an app explicitly:

```sh
bash tools/image-to-appcard-flow.sh plan \
  --project "$PWD/apps/aircon" \
  --manifest "$PWD/apps/aircon/image-to-appcard-flow.json"
```

For native UI tests, use [Makepad's built-in instrument](../lab/core/NATIVE-INSTRUMENT.md)
and hidden windows. Older Studio scripts and receipts are historical material;
moving them does not constitute a fresh native or image-parity acceptance.

`app/` remains the shared Android client. `a2app/apps/` and `a2app-l0/apps/`
contain agent specifications. Shared authoring and conversion tools remain in
`lab/`; app implementations belong here.
