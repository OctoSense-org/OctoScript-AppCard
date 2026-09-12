# Native semantic L0 theme kits — 2026-09-06

All 475 source artboards across five themes pass the current release Studio structural, native composition, semantic component and visual gates. The generated kits contain 1,784 dedicated semantic widget instances.

[Open the comparison index](../../lab/sketch/work/l0-themes/index.html).

| Kit | Cards | Mapped native elements | Semantic instances | Added native controls |
| --- | ---: | ---: | ---: | ---: |
| Taskplan | 79 | 13,158 | 289 | 17 |
| Atro | 150 | 26,953 | 377 | 213 |
| Camo | 246 | 30,173 | 1,118 | 244 |

## Component replacement

| Native widget | Taskplan | Atro | Camo |
| --- | ---: | ---: | ---: |
| `KitButton` | 166 | 279 | 844 |
| `KitFormField` | 85 | 48 | 72 |
| `KitTabBar` | 21 | 50 | 26 |
| `KitBottomNavigation` | 0 | 0 | 74 |
| `TaskplanProjectCard` | 17 | 0 | 0 |
| `CamoTrackRow` | 0 | 0 | 102 |

The six Rust widget types in `splash-widgets::kit` replace recognized complete View compositions. They retain native Button, TextInput and RadioButton children, forward native actions and expose component activation, named row actions, value changes, selection and content setters. Ordinary layout containers remain Views.

Shared L0 definitions own every child and expose named properties through one `instance`. Checked `part` bindings preserve original Sketch IDs and placements. Public defaults live in each theme’s `roles.l0`; `$kit.instances` and `$kit.placements` supply the source-linked host bindings. Unknown parts, mismatched roots, missing controls and invalid selection indices fail.

Transparent native controls fill formerly passive Atro tabs and project/track-row actions. The offline audit permits only those explicitly mapped additions and otherwise requires every original source property and child to match (geometry rounding below 1e-8 pt only).

## Validation and repairs

- All 475 cards passed the offline source-property/hierarchy audit and fresh Studio WidgetTreeDump, WidgetQuery and WidgetSnapshot inspection.
- The kit gate verifies the actual native type at every semantic boundary; a generic View with the same ID fails. Missing or host-only inspection fails.
- Studio first checks enabled/selected state for every semantic component against its native controls, then probes every visible navigation item, exclusive radio state, component actions, representative fields/buttons and project/row title setters. Fully clipped controls are recorded without claiming click coverage. Click points exclude later native controls, including floating buttons. Covered regions and actual receiving controls are recorded; fully covered controls do not claim click coverage. Source state is restored afterward.
- Navigation validation found and repaired stale selection backgrounds: source surfaces now expose dynamic color instances. Active/inactive background and underline samples must match within 3/255 per color channel. The gate uses the initial screenshot’s source-state palette to account for modal scrims and rejects inconsistent sample colors.
- Disabled navigation items now retain their source paint and no longer define the normal inactive palette.
- Empty optional bindings no longer make wrappers report disabled. Added Atro radios now start with the inferred source selection; their initial checked state must match the group index.
- Tab underlines now follow the selected item. Elevation layers are kept separate from state backgrounds, and pixel probes check both background and indicator colors. Component probe failures are collected across the kit before the run fails.
- A negative L0 state initializer was being discarded, changing no selection (-1) into index 0. Signed numeric initialization and selection reconciliation are repaired and covered by regression tests.
- Core L0: [287 tests passed](../../lab/sketch/work/l0-themes/validation/l0-tests.log). Native library/integration: [54 tests passed](../../lab/sketch/work/l0-themes/validation/native-tests.log). Python pipeline: [155 tests passed](../../lab/sketch/work/l0-themes/validation/pipeline-tests.log).
- Structural tolerances remain position/alignment/spacing 4 pt, dimensions 6 pt, clipping 2 pt and inspection agreement 1 pt. Visual minimum remains 9/10; only identical screenshot pairs reuse an existing review. Changed pairs require fresh inspection.

| Kit | Studio builds | Passing behavior observations | Surface color samples | Byte-identical prior screenshots |
| --- | --- | ---: | ---: | ---: |
| Taskplan | [106] | 485 | 290 | 79/79 |
| Atro | [105] | 726 | 118 | 136/150 |
| Camo | [104] | 1900 | 36 | 246/246 |

## Theme libraries

| Theme | Tokens | Primitive variants | Shared compositions |
| --- | ---: | ---: | ---: |
| `taskplan_light` | 148 | 224 | 235 |
| `atro` | 330 | 447 | 195 |
| `atro_light` | 330 | 447 | 207 |
| `camo` | 290 | 452 | 263 |
| `camo_light` | 290 | 452 | 271 |

## Artifacts and scope

Cards, host data and Sketch maps: `lab/sketch/work/{taskplan,atro,camo}/native/l0/`. Screenshots, per-element differences, `.semantic-interactions.json`, repair findings and galleries: the adjacent `l0-captures/` directories. Theme libraries: `splash-makepad/components/l0/native/<theme>/`.

This validates reusable native components and parity at the source artboard sizes in the file-backed splash-makepad host. Page layouts retain source geometry; responsive layouts and complete navigation/submission/playback workflows require separate work. Component actions are available for application consumers. Setter probes prove data propagation; long replacement titles can exceed source text allocations, so arbitrary-copy layout requires separate placement/overflow validation. Project progress artwork and member images remain source assets; changing `progress_text` does not recompute a chart. The separate main application backend is unchanged.

See [the native L0 authoring contract](../../splash-makepad/docs/native-l0-kits.md) and [the beauty loop](../../lab/sketch/README.md).
