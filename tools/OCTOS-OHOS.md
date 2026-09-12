# Native Octos on HarmonyOS

Run `octos-mate70-generation` from the `app/makepad.splash` mount in a release
Makepad Studio. It builds a signed release HAP, replaces the installed Octos app
without clearing its data, and connects the phone to Studio for inspection.

The HarmonyOS transport links `octos-cli` into `libmakepad.so`. It boots the
core's `local_oup` runtime and uses its canonical embedded dispatcher through a
Tokio duplex pipe. The phone does not execute an ELF from its bundle and does
not need a development computer to serve Octos. The configured LLM provider
still runs remotely; provider prompt caching is not an on-device model KV cache.

## Local prerequisites

- A release Studio and its matching `cargo-makepad studio` bridge.
- DevEco Studio / OpenHarmony native SDK and HDC, and the Rust nightly
  `aarch64-unknown-linux-ohos` target.
- Device signing configured locally. Set `OCTOS_OHOS_SIGNING_CONFIG` to its
  JSON signing-config array. It is never checked into this repository.
- A connected device. Set `OCTOS_OHOS_DEVICE` when more than one is connected.
- Configure a model in the app. For local automation only, an optional private
  provisioning JSON file can supply the app's existing `llm_family`, `llm_model`
  and `llm_key` fields. Never put that file, raw build logs, signing profiles or
  keys in a review artifact or HAP resource.
  A self-hosted model can also supply `llm_base_url` (its HTTP(S) model endpoint)
  and `llm_api_type` (`openai`, `anthropic`, or `responses`). These populate the
  selected model's route, separate from the Octos core/server connection.
  Provisioning a built-in provider without these fields clears a prior custom
  route. The model endpoint must not contain credentials or query parameters.

`DEVECO_HOME`, `HDC` and `OCTOS_OHOS_SDK_ENV` override local SDK discovery.
The request file defaults to `/tmp/octos-ohos-request.json`; override it with
`OCTOS_OHOS_REQUEST`. Example with no credentials:

```json
{
  "prompt": "Weather in Tokyo. It is morning; I prefer Taskplan and a forecast-first page with airy spacing.",
  "studio_port": 8002,
  "evidence_dir": "/tmp/octos-ohos-generation"
}
```

Use the port of the running Studio. Before another launch, `ClearBuild` the
previous live build. After the first successful install, `"skip_build": true`
can launch more context prompts against that same package. After any runtime
source change, remove `skip_build` and rebuild through Studio. Omit `prompt`
for normal interactive use. Add `"standalone": true` to omit Studio connection
extras while launching through the same RunItem; use the device capture for
that final independent-launch check. Omit provisioning after onboarding; the app retains
its private settings across updates.

## Context and cache contract

The shared language, capability catalog, app requirements, exemplars and native
page compositions precede the request. Theme hints, preferences and supplied
time-of-day context follow `END REFERENCE`. Changing context therefore preserves
the complete reference prefix. The native kernel also omits the per-session
workspace hint from its system prefix. Neither operation forces a provider to
cache; only reported cache usage proves a hit. The cache is at the model
provider, not a KV tensor cache stored on the phone. Native composition uses
fast inference by default unless the saved model/gateway settings or the
per-turn Thinking control request reasoning. GLM receives an explicit disabled
setting in fast mode.

The LLM can select every admitted theme, including Atro, Camo and Taskplan,
compose semantic theme axes, and use the existing weather dashboard/forecast,
stock tiles/chart and news magazine/compact view compositions. A request does
not merely select a saved screenshot. The model emits a complete checked L0
card with its declared sources and controls, rendered by native widgets.

For context variation, compare morning planning, nighttime monitoring, and a
compact reading preference across weather, stock and news. Repeat comparable
requests in fresh sessions on the same provider/model. Preserve reported input,
output and cache-read counts, first visible text time, total turn time, repair
count and final render status. Label the initial request as *initial* unless
the provider's cache counters establish a cold request. Do not attribute faster
decoding or fewer output tokens to prefix caching.

## Device validation

When an authorized runtime upgrade changes the bundle fingerprint, an existing
card's receipt correctly refuses the new bundle. Set `"reapprove_cards": true`
in that deployment's private request to explicitly migrate it. The app archives
the previous receipt directory as `l0-approvals-before-studio-BUILD_ID` inside
its own storage before opening cards. Each card then goes through normal
admission under the new runtime. Old receipts are preserved; the renderer never
silently overwrites a mismatched pin. Remove the option for subsequent launches
and repeat native validation after the migration. This is host policy admission,
not a claim that a person has visually approved the generated design.

Require the native core version, a real submitted/completed generation turn,
and a rendered card. Use Studio `WidgetTreeDump`, `WidgetSnapshot` and
`WidgetQuery`, plus a device screenshot. Host-only inspection or an empty chat
is a failure. Verify content, bounds, visibility and controls; inspect the image
for font, palette, spacing and clipping. Keep raw private diagnostics under the
local evidence directory. Share only selected metrics, screenshots, structural
findings and source/build hashes.

`octos-generation-contract-tests` checks theme vocabulary and stable reference
prefixes. Device generation and visual inspection are separate checks; a passing
contract test does not establish a working phone deployment or a speedup.

`build-ohos-kernel.sh` is an optional CLI cross-build check. That standalone
executable is not the HarmonyOS application's runtime transport.

Capture one completed run with the existing bridge (no build is started):

```sh
python3 tools/octos-ohos-capture.py --build BUILD_ID --bridge-port BRIDGE_PORT \
  --name weather-morning --theme taskplan_light \
  --prompt 'Weather in Tokyo. Morning planning; Taskplan; forecast first.' \
  --output docs/reviews/my-phone-generation
```

The structural gate requires a completed turn, hidden loading overlay, inner
native widgets, the expected kit in realized source, and horizontal overflow
within 2 logical pixels. Vertical content outside the viewport is allowed for
scrolling cards. Inspect the screenshot and exercise controls separately;
`visual_review` deliberately remains pending until a reviewer does so.
`octos-generation-terminal-tests` exercises terminal completion and error
handling through Studio. The transport and provider crates also have CLI-only
release tests for lossless text delivery and GLM fast-mode serialization.
