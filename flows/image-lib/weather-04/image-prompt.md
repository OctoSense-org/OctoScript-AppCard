Generate exactly ONE polished mobile weather app UX mockup titled "Weather at a glance". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Warm apricot bento: asymmetrical large weather card and stacked mini metrics.. Palette: {"name": "Apricot", "page": "FBF4EC", "panel": "FFFFFF", "ink": "482F28", "muted": "987D70", "tint": "F6D8BE", "accent": "A34E2F"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#fbf4ec"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Weather at a glance","size":30,"weight":700,"alignx":0,"color":"#482f28"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Monday, September 7","size":13,"weight":400,"alignx":0,"color":"#987d70"}
{"id":"current","t":"stack","x":24,"y":122,"w":216,"h":288,"radius":24,"bg":"#f6d8be"}
{"id":"location","t":"text","x":44,"y":143,"w":178,"h":23.4,"text":"Cupertino","size":18,"weight":700,"alignx":0,"color":"#482f28"}
{"id":"temperature","t":"text","x":44,"y":176,"w":180,"h":98.8,"text":"24°","size":76,"weight":500,"alignx":0,"color":"#482f28"}
{"id":"weather_symbol","t":"svg","x":94,"y":280,"w":86,"h":70,"graphic":"cloud"}
{"id":"condition","t":"text","x":44,"y":364,"w":174,"h":20.8,"text":"Partly cloudy","size":16,"weight":500,"alignx":0,"color":"#482f28"}
{"id":"humidity","t":"stack","x":256,"y":122,"w":126,"h":132,"radius":20,"bg":"#ffffff"}
{"id":"humidity_label","t":"text","x":272,"y":136,"w":94,"h":15.6,"text":"Humidity","size":12,"weight":500,"alignx":0,"color":"#987d70"}
{"id":"humidity_value","t":"text","x":272,"y":161,"w":94,"h":32.5,"text":"64%","size":25,"weight":700,"alignx":0,"color":"#482f28"}
{"id":"wind","t":"stack","x":256,"y":270,"w":126,"h":140,"radius":20,"bg":"#ffffff"}
{"id":"wind_label","t":"text","x":272,"y":284,"w":94,"h":15.6,"text":"Wind","size":12,"weight":500,"alignx":0,"color":"#987d70"}
{"id":"wind_value","t":"text","x":272,"y":309,"w":94,"h":32.5,"text":"12 km/h","size":25,"weight":700,"alignx":0,"color":"#482f28"}
{"id":"forecast_title","t":"text","x":24,"y":444,"w":250,"h":26.0,"text":"The week ahead","size":20,"weight":700,"alignx":0,"color":"#482f28"}
{"id":"forecast","t":"stack","x":24,"y":488,"w":358,"h":112,"radius":20,"bg":"#ffffff"}
{"id":"day_0","t":"stack","x":24.0,"y":488,"w":89.5,"h":112}
{"id":"day_label_0","t":"text","x":32.0,"y":501,"w":73.5,"h":15.6,"text":"Now","size":12,"weight":500,"alignx":0.5,"color":"#987d70"}
{"id":"day_icon_0","t":"svg","x":52.0,"y":527,"w":34,"h":28,"graphic":"cloud"}
{"id":"day_temp_0","t":"text","x":32.0,"y":566,"w":73.5,"h":22.1,"text":"24°","size":17,"weight":700,"alignx":0.5,"color":"#482f28"}
{"id":"day_1","t":"stack","x":113.5,"y":488,"w":89.5,"h":112}
{"id":"day_label_1","t":"text","x":121.5,"y":501,"w":73.5,"h":15.6,"text":"Tue","size":12,"weight":500,"alignx":0.5,"color":"#987d70"}
{"id":"day_icon_1","t":"svg","x":141.5,"y":527,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_1","t":"text","x":121.5,"y":566,"w":73.5,"h":22.1,"text":"25°","size":17,"weight":700,"alignx":0.5,"color":"#482f28"}
{"id":"day_2","t":"stack","x":203.0,"y":488,"w":89.5,"h":112}
{"id":"day_label_2","t":"text","x":211.0,"y":501,"w":73.5,"h":15.6,"text":"Wed","size":12,"weight":500,"alignx":0.5,"color":"#987d70"}
{"id":"day_icon_2","t":"svg","x":231.0,"y":527,"w":34,"h":28,"graphic":"cloud"}
{"id":"day_temp_2","t":"text","x":211.0,"y":566,"w":73.5,"h":22.1,"text":"23°","size":17,"weight":700,"alignx":0.5,"color":"#482f28"}
{"id":"day_3","t":"stack","x":292.5,"y":488,"w":89.5,"h":112}
{"id":"day_label_3","t":"text","x":300.5,"y":501,"w":73.5,"h":15.6,"text":"Thu","size":12,"weight":500,"alignx":0.5,"color":"#987d70"}
{"id":"day_icon_3","t":"svg","x":320.5,"y":527,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_3","t":"text","x":300.5,"y":566,"w":73.5,"h":22.1,"text":"22°","size":17,"weight":700,"alignx":0.5,"color":"#482f28"}
{"id":"note","t":"text","x":24,"y":644,"w":358,"h":19.5,"text":"A little sunshine, a slower day.","size":15,"weight":400,"alignx":0,"color":"#987d70"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#a34e2f"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"My cities","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.
