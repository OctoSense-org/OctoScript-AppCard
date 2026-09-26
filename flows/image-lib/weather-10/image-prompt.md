Generate exactly ONE polished mobile weather app UX mockup titled "Outside today". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Outdoor activity dashboard: large comfort score, condition chips, sunrise and sunset tiles.. Palette: {"name": "Electric", "page": "171C1C", "panel": "252D2C", "ink": "F3F7E9", "muted": "A0AFA9", "tint": "384F43", "accent": "D2EF82"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#171c1c"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Outside today","size":30,"weight":700,"alignx":0,"color":"#f3f7e9"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Monday, September 7","size":13,"weight":400,"alignx":0,"color":"#a0afa9"}
{"id":"comfort","t":"stack","x":24,"y":121,"w":358,"h":283,"radius":28,"bg":"#384f43"}
{"id":"comfort_kicker","t":"text","x":44,"y":141,"w":316,"h":15.6,"text":"OUTDOOR COMFORT","size":12,"weight":700,"alignx":0,"color":"#a0afa9"}
{"id":"comfort_score","t":"text","x":44,"y":187,"w":214,"h":145.6,"text":"86","size":112,"weight":500,"alignx":0,"color":"#f3f7e9"}
{"id":"weather_symbol","t":"svg","x":266,"y":215,"w":86,"h":75,"graphic":"sun"}
{"id":"comfort_label","t":"text","x":44,"y":345,"w":318,"h":26.0,"text":"A great day to get outside.","size":20,"weight":700,"alignx":0,"color":"#f3f7e9"}
{"id":"sunrise","t":"stack","x":24,"y":438,"w":171,"h":92,"radius":20,"bg":"#252d2c"}
{"id":"sunrise_label","t":"text","x":40,"y":452,"w":139,"h":15.6,"text":"Sunrise","size":12,"weight":500,"alignx":0,"color":"#a0afa9"}
{"id":"sunrise_value","t":"text","x":40,"y":477,"w":139,"h":32.5,"text":"6:42 AM","size":25,"weight":700,"alignx":0,"color":"#f3f7e9"}
{"id":"sunset","t":"stack","x":211,"y":438,"w":171,"h":92,"radius":20,"bg":"#252d2c"}
{"id":"sunset_label","t":"text","x":227,"y":452,"w":139,"h":15.6,"text":"Sunset","size":12,"weight":500,"alignx":0,"color":"#a0afa9"}
{"id":"sunset_value","t":"text","x":227,"y":477,"w":139,"h":32.5,"text":"7:28 PM","size":25,"weight":700,"alignx":0,"color":"#f3f7e9"}
{"id":"activity","t":"text","x":24,"y":574,"w":358,"h":31.2,"text":"Try a late afternoon walk.","size":24,"weight":700,"alignx":0,"color":"#f3f7e9"}
{"id":"activity_detail","t":"text","x":24,"y":620,"w":358,"h":16.9,"text":"24° and a gentle breeze in Cupertino.","size":13,"weight":400,"alignx":0,"color":"#a0afa9"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#d2ef82"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"My cities","size":14,"weight":500,"alignx":0.5,"color":"#171c1c"}

Render only this single finished app screen. Fit every element within the artboard.

The background MUST be fully opaque from edge to edge. Every pixel must have alpha 255; no transparency, cutouts or checkerboards.