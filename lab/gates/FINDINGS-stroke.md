# `sdf.stroke` — a sharper diagnosis, and still unfixed (2026-08-31)

Timeboxed investigation of step 3. Not fixed, but the previous description of
the fault was wrong in a way that mattered, and the next attempt should not
start where this one did.

## What was believed

> `border_size` applies and insets the box, only `sdf.stroke` is missing.

True as far as it went, and it pointed at the SDF maths. It isn't the maths.

## What the probes actually show

All against a `RoundedShadowView` panel with a deliberately unmissable border —
6px, opaque red — rendered on desktop and counted by pixel.

| probe | red pixels |
|---|---|
| `border: 6`, `l0_stroke: #ff0000ff` through the normal path | **0** |
| `sdf.stroke(vec4(1,0,0,1) 6.0)`, unconditional, branch removed | **0** |
| `sdf.stroke_keep(...)` and `sdf.glow_keep(...)` | **0** |
| `abs(self.shape)` replaced by an explicit `if` branch | **0** |
| `self.result = red` forced at the top of `stroke_keep` | **6506** |

The last row is the finding. 6506 pixels is a **border-shaped band** — roughly
the panel perimeter times six — not a filled panel and not nothing.

So, established:

1. `stroke_keep` **is invoked**, once per pixel of the panel quad.
2. Its mutation of `self.result` **does persist** to the returned colour.
3. The band **geometry is right** — `f` is non-zero exactly where a border
   belongs, so `calc_blur`, `self.shape`, `scale_factor` and `aa` are all fine.
4. Passing a **colour** produces nothing — instance, `vec4(...)` literal, and
   `#f00` alike.

The fault is therefore in the COLOUR reaching the stroke, not in the signed
distance field. That is a different bug in a different place from the one that
was being looked for.

## What was tried and did not work

Inlining `stroke_keep`'s body directly into `view_ui.rs`'s `pixel` fn — reading
the `stroke_color` local that the gradient-mix code above it already reads
successfully — also produced 0. Which is odd, because that local demonstrably
holds a colour two lines earlier.

## Where to start next

Not in `sdf.rs`. Compare how `color` (an instance that arrives) and the stroke's
`color` argument are translated into the Metal shader — dump the generated
shader source for `RoundedShadowView` and diff the two paths. The argument is
being lost between the call site and the function body, and the generated source
will say so directly rather than by inference.

Cost so far: five rebuild-and-render cycles. Every one of them was cheap and
each removed a hypothesis; the reason to stop is the timebox, not a dead end.
53 of 100 style recipes want a stroke, though only 3 are blocked by it alone —
see the cluster table in the plan.
