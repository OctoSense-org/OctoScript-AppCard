# Generation prompt template — replace every bracketed value before submission

Generate one finished mobile app screen, front-facing and flat, with no device
frame, perspective, watermark, extra canvas or explanatory annotations. Use a
406 × 776 logical artboard and scale the entire canvas uniformly to your output
resolution. Keep all content inside the specified artboard.

App purpose: [purpose]. Screen/state: [screen name and initial state].

Typography: [actual supplied family], bundled files [filenames], weights
[weights]. Heading [size/line height], body [size/line height], caption
[size/line height]. Preserve exact capitalization, punctuation, units and
strings from the contract. Coordinates are logical pixels from the top left;
text rectangles are line boxes, not glyph outlines. Do not print font names,
element IDs or coordinates in the image.

Layout: [copy the exact contract hierarchy and x/y/width/height for each ID].
Spacing: [outer padding, section gaps, row gaps and alignment anchors].
Colors: [background, surface, text, muted text, accent and selected colors].
Effects: [radii, borders, shadows, blur and gradients with explicit values].
Controls: [native control intent, enabled/selected/value states and labels].

Numerical regions: [native chart type, source ID, samples, series names,
units, domains, axes, selected range and markers]. Use these values; do not
invent a decorative curve. If absent, state “No quantitative chart regions.”

Artwork: [isolated rectangle, subject, style, fit and cropping requirements].
Keep UI text and controls outside artwork so that it can become an isolated
asset. Simple icons: [named icons and vector geometry]. Do not replace UI
labels with raster artwork.

Render only the specified finished screen. The actual output will be measured
and reviewed against this contract; the prompt alone is not layout evidence.
