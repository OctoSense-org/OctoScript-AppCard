# Upstream Makepad map comparison

Inspected `makepad/makepad` branch `work` at commit
`a75fe914ffaf4d6b4db956731c08e41d6d4aef75` on 2026-09-05. This is a source
comparison; the upstream app was not built or benchmarked. Studio sessions and
the other debugger's app were not touched.

The relevant app is `apps/route`. Its UI declares a persistent native MapView.
`apply_nav_tick` calls `set_puck`, `set_center`, `set_rotation`, and
`set_route_progress`, then updates existing banner labels. Live GPS arrives via
`Event::LocationUpdate`; simulation has a separate frame loop. These operations
do not traverse our L0 → kit evaluator → generated widget DSL pipeline.
[App source](https://github.com/makepad/makepad/blob/a75fe914ffaf4d6b4db956731c08e41d6d4aef75/apps/route/src/main.rs#L1644)

| Area | Upstream mechanism | Current Octos nav |
| --- | --- | --- |
| State updates | Existing widget references and Rust setters | Live follow already updates in place; card state changes still regenerate widget code |
| Tile rendering | Retained draw lists for each tile and cartographic pass; camera changes refresh uniforms | Retained geometry, but fill/stroke draw submissions are generated again |
| Labels | Cached placement moves with camera transforms; replacement waits for settling and has a time budget | Candidate cache is cloned, sorted and collision-tested during nav drawing |
| Ready tiles | Worker results enter a pending queue; insertion is limited per frame | Worker result queue drains directly into geometry creation |
| Memory | Byte budgets for resident tiles, pending buffers, uploads and archives; CPU staging released after GPU upload | Shared cache capped primarily at 640 tiles; no equivalent byte accounting/staging-release policy in the map |
| Local source I/O | Configured `.mkmap` archive uses worker reads | Legacy JSON cache reads synchronously before dispatching parsing to workers |

The retained drawing code checks a signature for each tile/pass. When it is
unchanged, `refresh` updates uniforms on existing draw calls. Geometry changes,
LOD transitions and other signature changes trigger recording again. This is
stronger reuse than retaining vertex geometry alone.
[Tile draw implementation](https://github.com/makepad/makepad/blob/a75fe914ffaf4d6b4db956731c08e41d6d4aef75/widgets/src/map/tile_draw.rs#L541)

The newer renderer also limits uploads using counts and bytes, retains label
placements while the camera moves, and disposes of uploaded CPU staging on a
worker. These are mechanisms to examine for our remaining frame stalls and
memory use; they are not evidence of a measured speedup on our app or handset.
[Renderer](https://github.com/makepad/makepad/blob/a75fe914ffaf4d6b4db956731c08e41d6d4aef75/widgets/src/map/view.rs#L7294)

The archive source sends local file reads through a worker queue and returns
completions to the UI. Upstream's legacy `request_tile` JSON fallback still uses
`fs::read_to_string` synchronously, so simply copying that fallback does not fix
our I/O path.
[Archive reader](https://github.com/makepad/makepad/blob/a75fe914ffaf4d6b4db956731c08e41d6d4aef75/widgets/src/map/archive.rs#L176),
[legacy fallback](https://github.com/makepad/makepad/blob/a75fe914ffaf4d6b4db956731c08e41d6d4aef75/widgets/src/map/view.rs#L9177)

The first application-level change should keep L0 authoring while maintaining
a persistent native map and updating its properties. Reuse parsed/evaluated
card state and rebuild structure only when required. Separately, port upload
budgets, byte accounting, staging release and retained drawing with their
required draw/platform support. Replacing only `map/view.rs` is not a complete
port: upstream also changes tile formats, archive loading, task queues and draw
list behavior.

The previously measured 20–36 ms timer measures our card-generation work before
final widget parsing/drawing. The upstream application avoids that work in its
navigation update path. Individual costs inside our timer still require
instrumentation; this comparison does not assign timings to them.
