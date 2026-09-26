# OctoScript App Design Flow

The harness a person **or a coding agent** uses to build an OctoSense app and
publish it through the [OctoSense App Hub](https://github.com/OctoSense-org/OctoSense-App-Hub):
flows to follow step by step, the developer docs, an app template, and
`tools/octo`, a small CLI around the App Hub's real `card-host` and `hub`.

(Formerly *Octoscript-AppCard*. The runtime moved to
[OctoSense-AppCard](https://github.com/OctoSense-org/OctoSense-AppCard); the
system apps to [OctoSense-System-Apps](https://github.com/OctoSense-org/OctoSense-System-Apps).)

Agents: read [AGENTS.md](AGENTS.md) first.

## Five minutes

Needs Rust, Python 3.9+, a graphical session, and the App Hub checkout with its
sibling sources ([QUICKSTART §1](docs/QUICKSTART.md#1-prerequisites)).

```sh
(cd ../OctoSense-App-Hub && cargo build --release -p octosense-card-host -p octosense-app-hub)
tools/octo doctor                                        # finds hub and card-host
tools/octo new ~/apps/my-app --id my-notes --name "My Notes"
tools/octo run ~/apps/my-app/bundle --port 8141 --detach # a real window, remote-controllable
curl -s "127.0.0.1:8141/snap?q=Notes"                    # what is on screen
tools/octo shot 8141 ~/apps/my-app/bundle/screenshots/01-main.png
curl -s 127.0.0.1:8141/quit
tools/octo check ~/apps/my-app/bundle                    # hub stamp + the App Hub gate
tools/octo package-help                                  # the publish checklist
```

## Map

| Path | What |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Rules, definition of done and reporting for coding agents |
| [flows/](flows/README.md) | Step-by-step flows. [script-app](flows/script-app/FLOW.md): text brief → script app. [image-to-card](flows/image-to-card/FLOW.md): design image → card app. [kits/sketch](flows/kits/sketch/FLOW.md): Sketch → kit. Shared native testing: [core/NATIVE-INSTRUMENT.md](flows/core/NATIVE-INSTRUMENT.md) |
| [docs/QUICKSTART.md](docs/QUICKSTART.md) | The one path: build tools, create, run, edit, check, phone, publish |
| [docs/PUBLISHING.md](docs/PUBLISHING.md) | Publishing to the App Hub, step by step, with verified outputs and the checklist |
| [docs/SCRIPT-API.md](docs/SCRIPT-API.md) | The Splash language and every API a contained app may call |
| [docs/CAPABILITIES.md](docs/CAPABILITIES.md) | Each capability: what it unlocks, what the person sees, the rules |
| [docs/HOST-SERVICES.md](docs/HOST-SERVICES.md) | `host.request`, sheets, "secrets are the host's", adding a service |
| [docs/GLOSSARY.md](docs/GLOSSARY.md) | One meaning per term |
| [docs/NATIVE-WORKSPACE.md](docs/NATIVE-WORKSPACE.md), [docs/l0/](docs/l0/) | Sibling-source setup; L0 card examples |
| [templates/script-app/](templates/script-app/README.md) | Runnable template `tools/octo new` copies; [card-app](templates/card-app/README.md) points to the card path |
| [examples/](examples/README.md) | Worked example projects |
| [tools/octo](tools/octo) | `doctor`, `new`, `run`, `shot`, `check`, `package-help` |

## Where the other pieces live

| Piece | Repository |
| --- | --- |
| Runtime: Splash isolate, widgets, Card lowering | [OctoSense-AppCard](https://github.com/OctoSense-org/OctoSense-AppCard), [OctoSense-org/makepad](https://github.com/OctoSense-org/makepad) |
| Store, gate, catalog, `hub`, `card-host`, `appstore` | [OctoSense-App-Hub](https://github.com/OctoSense-org/OctoSense-App-Hub) |
| System apps (News, Photos, Maps, Camera, Mail) and the Mail host service | [OctoSense-System-Apps](https://github.com/OctoSense-org/OctoSense-System-Apps) |
| Shells that run apps | OctoSense ROM `home/` (phone launcher), OctoSense desktop shell |

## License

Apache-2.0; see [LICENSE](LICENSE) and [NOTICE](NOTICE).
