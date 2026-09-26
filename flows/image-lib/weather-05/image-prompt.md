Generate exactly ONE polished mobile weather app UX mockup titled "The daily weather". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Editorial weather bulletin: oversized type without a hero box, thin information rows.. Palette: {"name": "Editorial", "page": "F4F2EB", "panel": "FCFBF7", "ink": "252922", "muted": "797E70", "tint": "E4E7D4", "accent": "536241"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#f4f2eb"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"The daily weather","size":30,"weight":700,"alignx":0,"color":"#252922"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Monday, September 7","size":13,"weight":400,"alignx":0,"color":"#797e70"}
{"id":"location","t":"text","x":24,"y":126,"w":358,"h":14.3,"text":"CUPERTINO, CALIFORNIA","size":11,"weight":700,"alignx":0,"color":"#797e70"}
{"id":"temperature","t":"text","x":19,"y":160,"w":300,"h":171.6,"text":"24°","size":132,"weight":500,"alignx":0,"color":"#252922"}
{"id":"weather_symbol","t":"svg","x":271,"y":216,"w":100,"h":85,"graphic":"cloud"}
{"id":"condition","t":"text","x":24,"y":332,"w":358,"h":31.2,"text":"A softer kind of sunshine.","size":24,"weight":700,"alignx":0,"color":"#252922"}
{"id":"range","t":"text","x":24,"y":377,"w":358,"h":18.2,"text":"High 27° / Low 17°","size":14,"weight":400,"alignx":0,"color":"#797e70"}
{"id":"forecast","t":"stack","x":24,"y":433,"w":358,"h":112,"radius":20,"bg":"#fcfbf7"}
{"id":"day_0","t":"stack","x":24.0,"y":433,"w":89.5,"h":112}
{"id":"day_label_0","t":"text","x":32.0,"y":446,"w":73.5,"h":15.6,"text":"Now","size":12,"weight":500,"alignx":0.5,"color":"#797e70"}
{"id":"day_icon_0","t":"svg","x":52.0,"y":472,"w":34,"h":28,"graphic":"cloud"}
{"id":"day_temp_0","t":"text","x":32.0,"y":511,"w":73.5,"h":22.1,"text":"24°","size":17,"weight":700,"alignx":0.5,"color":"#252922"}
{"id":"day_1","t":"stack","x":113.5,"y":433,"w":89.5,"h":112}
{"id":"day_label_1","t":"text","x":121.5,"y":446,"w":73.5,"h":15.6,"text":"Tue","size":12,"weight":500,"alignx":0.5,"color":"#797e70"}
{"id":"day_icon_1","t":"svg","x":141.5,"y":472,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_1","t":"text","x":121.5,"y":511,"w":73.5,"h":22.1,"text":"25°","size":17,"weight":700,"alignx":0.5,"color":"#252922"}
{"id":"day_2","t":"stack","x":203.0,"y":433,"w":89.5,"h":112}
{"id":"day_label_2","t":"text","x":211.0,"y":446,"w":73.5,"h":15.6,"text":"Wed","size":12,"weight":500,"alignx":0.5,"color":"#797e70"}
{"id":"day_icon_2","t":"svg","x":231.0,"y":472,"w":34,"h":28,"graphic":"cloud"}
{"id":"day_temp_2","t":"text","x":211.0,"y":511,"w":73.5,"h":22.1,"text":"23°","size":17,"weight":700,"alignx":0.5,"color":"#252922"}
{"id":"day_3","t":"stack","x":292.5,"y":433,"w":89.5,"h":112}
{"id":"day_label_3","t":"text","x":300.5,"y":446,"w":73.5,"h":15.6,"text":"Thu","size":12,"weight":500,"alignx":0.5,"color":"#797e70"}
{"id":"day_icon_3","t":"svg","x":320.5,"y":472,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_3","t":"text","x":300.5,"y":511,"w":73.5,"h":22.1,"text":"22°","size":17,"weight":700,"alignx":0.5,"color":"#252922"}
{"id":"humidity","t":"stack","x":24,"y":579,"w":171,"h":92,"radius":20,"bg":"#fcfbf7"}
{"id":"humidity_label","t":"text","x":40,"y":593,"w":139,"h":15.6,"text":"Humidity","size":12,"weight":500,"alignx":0,"color":"#797e70"}
{"id":"humidity_value","t":"text","x":40,"y":618,"w":139,"h":32.5,"text":"64%","size":25,"weight":700,"alignx":0,"color":"#252922"}
{"id":"wind","t":"stack","x":211,"y":579,"w":171,"h":92,"radius":20,"bg":"#fcfbf7"}
{"id":"wind_label","t":"text","x":227,"y":593,"w":139,"h":15.6,"text":"Wind","size":12,"weight":500,"alignx":0,"color":"#797e70"}
{"id":"wind_value","t":"text","x":227,"y":618,"w":139,"h":32.5,"text":"12 km/h","size":25,"weight":700,"alignx":0,"color":"#252922"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#536241"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"My cities","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.

The background MUST be fully opaque from edge to edge. Every pixel must have alpha 255; no transparency, cutouts or checkerboards.