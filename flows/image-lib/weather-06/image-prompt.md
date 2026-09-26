Generate exactly ONE polished mobile weather app UX mockup titled "Your cities". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: City collection: one featured city and three independent location cards.. Palette: {"name": "Denim", "page": "EAF0F4", "panel": "F8FBFD", "ink": "213B50", "muted": "72899A", "tint": "CFDFE8", "accent": "355F7A"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#eaf0f4"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Your cities","size":30,"weight":700,"alignx":0,"color":"#213b50"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Monday, September 7","size":13,"weight":400,"alignx":0,"color":"#72899a"}
{"id":"featured","t":"stack","x":24,"y":118,"w":358,"h":182,"radius":20,"bg":"#cfdfe8"}
{"id":"location","t":"text","x":44,"y":140,"w":220,"h":31.2,"text":"Cupertino","size":24,"weight":700,"alignx":0,"color":"#213b50"}
{"id":"condition","t":"text","x":44,"y":182,"w":220,"h":18.2,"text":"Partly cloudy","size":14,"weight":400,"alignx":0,"color":"#72899a"}
{"id":"temperature","t":"text","x":255,"y":144,"w":108,"h":78.0,"text":"24°","size":60,"weight":500,"alignx":0,"color":"#213b50"}
{"id":"weather_symbol","t":"svg","x":282,"y":226,"w":54,"h":46,"graphic":"cloud"}
{"id":"city_0","t":"stack","x":24,"y":324,"w":358,"h":98,"radius":20,"bg":"#f8fbfd"}
{"id":"city_name_0","t":"text","x":44,"y":342,"w":235,"h":27.3,"text":"San Francisco","size":21,"weight":700,"alignx":0,"color":"#213b50"}
{"id":"city_note_0","t":"text","x":44,"y":378,"w":235,"h":15.6,"text":"Coastal clouds","size":12,"weight":400,"alignx":0,"color":"#72899a"}
{"id":"city_temp_0","t":"text","x":285,"y":349,"w":76,"h":39.0,"text":"19°","size":30,"weight":500,"alignx":1,"color":"#213b50"}
{"id":"city_1","t":"stack","x":24,"y":440,"w":358,"h":98,"radius":20,"bg":"#f8fbfd"}
{"id":"city_name_1","t":"text","x":44,"y":458,"w":235,"h":27.3,"text":"Tokyo","size":21,"weight":700,"alignx":0,"color":"#213b50"}
{"id":"city_note_1","t":"text","x":44,"y":494,"w":235,"h":15.6,"text":"Light rain","size":12,"weight":400,"alignx":0,"color":"#72899a"}
{"id":"city_temp_1","t":"text","x":285,"y":465,"w":76,"h":39.0,"text":"28°","size":30,"weight":500,"alignx":1,"color":"#213b50"}
{"id":"city_2","t":"stack","x":24,"y":556,"w":358,"h":98,"radius":20,"bg":"#f8fbfd"}
{"id":"city_name_2","t":"text","x":44,"y":574,"w":235,"h":27.3,"text":"Copenhagen","size":21,"weight":700,"alignx":0,"color":"#213b50"}
{"id":"city_note_2","t":"text","x":44,"y":610,"w":235,"h":15.6,"text":"Clear skies","size":12,"weight":400,"alignx":0,"color":"#72899a"}
{"id":"city_temp_2","t":"text","x":285,"y":581,"w":76,"h":39.0,"text":"16°","size":30,"weight":500,"alignx":1,"color":"#213b50"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#355f7a"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"Add a city","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.

The background MUST be fully opaque from edge to edge. Every pixel must have alpha 255; no transparency, cutouts or checkerboards.