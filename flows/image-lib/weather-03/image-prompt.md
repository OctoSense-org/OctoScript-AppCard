Generate exactly ONE polished mobile weather app UX mockup titled "Hour by hour". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Cobalt hourly timeline: compact summary, wide temperature chart, bottom metric tiles.. Palette: {"name": "Cobalt", "page": "F3F5FA", "panel": "FFFFFF", "ink": "172D56", "muted": "75829B", "tint": "DFE9FF", "accent": "2F61D5"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#f3f5fa"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Hour by hour","size":30,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Monday, September 7","size":13,"weight":400,"alignx":0,"color":"#75829b"}
{"id":"current","t":"stack","x":24,"y":116,"w":358,"h":112,"radius":20,"bg":"#dfe9ff"}
{"id":"temperature","t":"text","x":44,"y":131,"w":150,"h":75.4,"text":"24°","size":58,"weight":500,"alignx":0,"color":"#172d56"}
{"id":"condition","t":"text","x":199,"y":145,"w":170,"h":20.8,"text":"Partly cloudy","size":16,"weight":500,"alignx":0,"color":"#172d56"}
{"id":"location","t":"text","x":199,"y":178,"w":150,"h":15.6,"text":"Cupertino","size":12,"weight":400,"alignx":0,"color":"#75829b"}
{"id":"hourly_title","t":"text","x":24,"y":264,"w":250,"h":26.0,"text":"Temperature trend","size":20,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"hourly_title_detail","t":"text","x":270,"y":269,"w":112,"h":14.3,"text":"Next 12 hours","size":11,"weight":400,"alignx":1,"color":"#75829b"}
{"id":"timeline","t":"stack","x":24,"y":308,"w":358,"h":216,"radius":20,"bg":"#ffffff"}
{"id":"temperature_chart","t":"svg","x":44,"y":326,"w":318,"h":146,"graphic":"line"}
{"id":"hour_0","t":"text","x":44,"y":488,"w":70,"h":14.3,"text":"12 PM","size":11,"weight":400,"alignx":0,"color":"#75829b"}
{"id":"hour_1","t":"text","x":124,"y":488,"w":70,"h":14.3,"text":"3 PM","size":11,"weight":400,"alignx":0,"color":"#75829b"}
{"id":"hour_2","t":"text","x":204,"y":488,"w":70,"h":14.3,"text":"6 PM","size":11,"weight":400,"alignx":0,"color":"#75829b"}
{"id":"hour_3","t":"text","x":284,"y":488,"w":70,"h":14.3,"text":"9 PM","size":11,"weight":400,"alignx":0,"color":"#75829b"}
{"id":"humidity","t":"stack","x":24,"y":555,"w":171,"h":92,"radius":20,"bg":"#ffffff"}
{"id":"humidity_label","t":"text","x":40,"y":569,"w":139,"h":15.6,"text":"Humidity","size":12,"weight":500,"alignx":0,"color":"#75829b"}
{"id":"humidity_value","t":"text","x":40,"y":594,"w":139,"h":32.5,"text":"64%","size":25,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"wind","t":"stack","x":211,"y":555,"w":171,"h":92,"radius":20,"bg":"#ffffff"}
{"id":"wind_label","t":"text","x":227,"y":569,"w":139,"h":15.6,"text":"Wind","size":12,"weight":500,"alignx":0,"color":"#75829b"}
{"id":"wind_value","t":"text","x":227,"y":594,"w":139,"h":32.5,"text":"12 km/h","size":25,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#2f61d5"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"My cities","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.
