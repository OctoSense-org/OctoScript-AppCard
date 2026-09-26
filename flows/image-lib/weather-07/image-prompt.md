Generate exactly ONE polished mobile weather app UX mockup titled "Rain watch". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Precipitation focus: wide radar-like vector rings, rain timeline, one humidity metric.. Palette: {"name": "Lavender", "page": "F4F0FA", "panel": "FFFFFF", "ink": "3A2A56", "muted": "8C7C9C", "tint": "E5DDF4", "accent": "7551A9"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#f4f0fa"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Rain watch","size":30,"weight":700,"alignx":0,"color":"#3a2a56"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Monday, September 7","size":13,"weight":400,"alignx":0,"color":"#8c7c9c"}
{"id":"location","t":"text","x":24,"y":120,"w":358,"h":22.1,"text":"Cupertino","size":17,"weight":700,"alignx":0,"color":"#3a2a56"}
{"id":"radar","t":"stack","x":24,"y":164,"w":358,"h":254,"radius":20,"bg":"#e5ddf4"}
{"id":"rain_radar","t":"svg","x":75,"y":180,"w":256,"h":220,"graphic":"radar"}
{"id":"rain_headline","t":"text","x":24,"y":449,"w":358,"h":36.4,"text":"Rain in 35 minutes","size":28,"weight":700,"alignx":0,"color":"#3a2a56"}
{"id":"rain_note","t":"text","x":24,"y":496,"w":358,"h":18.2,"text":"A short shower, then clearer skies.","size":14,"weight":400,"alignx":0,"color":"#8c7c9c"}
{"id":"chance","t":"stack","x":24,"y":550,"w":171,"h":92,"radius":20,"bg":"#ffffff"}
{"id":"chance_label","t":"text","x":40,"y":564,"w":139,"h":15.6,"text":"Rain chance","size":12,"weight":500,"alignx":0,"color":"#8c7c9c"}
{"id":"chance_value","t":"text","x":40,"y":589,"w":139,"h":32.5,"text":"80%","size":25,"weight":700,"alignx":0,"color":"#3a2a56"}
{"id":"humidity","t":"stack","x":211,"y":550,"w":171,"h":92,"radius":20,"bg":"#ffffff"}
{"id":"humidity_label","t":"text","x":227,"y":564,"w":139,"h":15.6,"text":"Humidity","size":12,"weight":500,"alignx":0,"color":"#8c7c9c"}
{"id":"humidity_value","t":"text","x":227,"y":589,"w":139,"h":32.5,"text":"64%","size":25,"weight":700,"alignx":0,"color":"#3a2a56"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#7551a9"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"My cities","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.

The background MUST be fully opaque from edge to edge. Every pixel must have alpha 255; no transparency, cutouts or checkerboards.