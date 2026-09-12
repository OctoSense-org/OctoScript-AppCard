**Splash review follow-up — state origins, approvals and native rendering**

Closed the remaining implementation gaps from the [earlier fixes](splash-layers-fixes-2026-09-04.md). The fourth review layer is native widget rendering and interaction, as requested. Language capability levels remain L0/L1/L2; an L3 header is rejected.

| Gap | Implemented behavior |
| --- | --- |
| State provenance | State cells retain their origin through dispatch, component arguments, loops, captures, schema retention and pruning. Authored values in data slots and numeric text slots become missing, including their live bindings and expressions. Controls retain editable defaults. A native Field establishes user input; a Row carrying an authored value retains its authored origin. Literal assignments and resets revoke data eligibility. Pending captures stay missing until data arrives. |
| Complete-artifact approvals | BLAKE3 pins source, level, policy, profile code, assembled kit and the host runtime bundle. The build fingerprints local implementations/resources, patched Makepad/VM/capability code, lockfile and build configuration. Approvals persist in the host configuration directory and are checked before capability resolution/mounting and before session dispatch. Existing mismatches, corrupt records and storage failures fail closed. |
| Runtime replacement | The app locks compiled script sources before widget registration. File watching and Studio live edits cannot replace the approved runtime; manual layout refreshes still work. |
| Native validation | Built and drove the actual `octos-app` through Studio, including widget mounting, keyboard input, change/return callbacks, taps, resets and L1 arithmetic. |

The native typing test found an additional defect beyond the original target-expression probes: `agent.notify` serializes the target string inside an outer JSON object. The VM serializer emitted a single backslash and omitted escaping for several control characters, breaking quoted input at that second boundary. Both VM copies now escape backslashes and every JSON control character. The regression harness exercises the actual outer serializer as well as the emitted Field callback. The reference VM has its own serializer regression.

The native host also accepts empty text as an actual payload. It establishes the event origin from the realized control and declared event, and retains source captures on the first successful session render. A user confirming the same value as an authored default changes the origin and triggers a redraw.

Validation completed in release mode:

- **280 UI-core tests**, including origin propagation, pending/captured sources, reset behavior and source/level/kit/runtime approval changes.
- **48 renderer/translator tests**, including the reference VM's nested JSON escaping regression.
- **1 host persistence test**, compiling the real host module, covering restart, changed runtime and corrupt storage.
- **1 platform source-lock test**, covering rejected file changes and preserved manual layout refreshes.
- **77 headless observations**, all successful, with all boundary assertions and **16 app/reference comparisons** passing.
- Full native app release build and the interaction checks below. Diff whitespace checks passed across the parent and all affected submodules.

Native checks used upstream [Makepad `dev` at `a13034d`](https://github.com/makepad/makepad/commit/a13034d85d5564f95d1ce100fa6fd19827c73117), built in `/tmp/octos-makepad-dev-studio-20260904`. Studio hosted the app using `app/makepad.splash`. The final app binary and runtime-bundle hashes are recorded in [validation.json](splash-native-evidence/validation.json).

| Native observation | Evidence |
| --- | --- |
| Authored `1547` remains editable while its data display is missing | [Initial screenshot](splash-native-evidence/initial.png) |
| Typing `42 "x"` updates state through `on_change`; Return invokes the commit callback | [Quoted input](splash-native-evidence/quoted-input.png) |
| `x","e":"reset","v":"` stays text and does not trigger Reset | [Event-shaped input](splash-native-evidence/event-shaped-input.png) |
| Deleting all text clears the state and display | [Empty input](splash-native-evidence/empty-input.png) |
| Reset restores the default and masks it; the authored-value Row cannot upgrade its origin | [Reset](splash-native-evidence/reset.png) |
| A host value of 42 times 0.621371 renders 26.097582 | [L1 arithmetic](splash-native-evidence/l1-arithmetic.png) |
| Replacing that input with an authored numeric transition masks the result | [L1 authored replacement](splash-native-evidence/l1-authored-refused.png) |
| Restart reuses the identical approval, including unchanged file modification time | [Approval record comparison](splash-native-evidence/approval-restart.json) |
| A rebuild with changed runtime rejects the saved approval before rendering | Build 2 in the [selected bridge transcript](splash-native-evidence/transcript.json) |

Final L0 interactions used build 7, approval reuse used build 8, and L1 interactions used build 9. Earlier transcript entries preserve the discovered JSON defect and an initial test-driver packet framing error; the corrected driver wraps keyboard messages in `StudioToAppVec`. Final interactions use the corrected framing. All test app processes and Studio were closed after capture; the Studio checkout and release binaries remain available.

The [headless evidence](splash-layers-gaps-2026-09-04-evidence.json), [test logs](splash-native-evidence/validation.json) and [reproduction instructions](splash-layers-probes/README.md) accompany this report. Earlier review and fix evidence remain separate snapshots.

Approvals are admissions under the installed host L0/L1 policy, not signatures or claims of manual user review. Changed pins require host reapproval; the renderer never silently overwrites them. The host and approval storage are trusted. Origins trace inputs rather than proving factual truth: inline labels, authored vocabulary and formula choice retain the limits stated in §4. Native validation covers macOS ARM64/Metal with local fixtures; other operating systems and live capability providers were not exercised.
