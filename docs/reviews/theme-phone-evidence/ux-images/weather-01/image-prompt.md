Generate exactly ONE polished mobile weather app UX mockup titled "Cupertino". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Calm sage dashboard: big hero, four-column forecast, two metrics.. Palette: {"name": "Sage", "page": "F5F6F0", "panel": "FFFFFF", "ink": "19372D", "muted": "718078", "tint": "E3EDE3", "accent": "285F49"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#f5f6f0"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Cupertino","size":30,"weight":700,"alignx":0,"color":"#19372d"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Monday, September 7","size":13,"weight":400,"alignx":0,"color":"#718078"}
{"id":"units","t":"stack","x":330,"y":34,"w":52,"h":44}
{"id":"units_surface","t":"stack","x":330,"y":34,"w":52,"h":44,"radius":14,"bg":"#ffffff"}
{"id":"units_label","t":"text","x":338,"y":46.0,"w":36,"h":20,"text":"°C","size":14,"weight":500,"alignx":0.5,"color":"#19372d"}
{"id":"current","t":"stack","x":24,"y":118,"w":358,"h":240,"radius":26,"bg":"#e3ede3"}
{"id":"current_kicker","t":"text","x":48,"y":144,"w":240,"h":15.6,"text":"CURRENT WEATHER","size":12,"weight":700,"alignx":0,"color":"#718078"}
{"id":"temperature","t":"text","x":46,"y":183,"w":213,"h":122.2,"text":"24°","size":94,"weight":500,"alignx":0,"color":"#19372d"}
{"id":"weather_symbol","t":"svg","x":250,"y":186,"w":102,"h":96,"graphic":"cloud"}
{"id":"condition","t":"text","x":48,"y":294,"w":250,"h":24.7,"text":"Partly cloudy","size":19,"weight":500,"alignx":0,"color":"#19372d"}
{"id":"range","t":"text","x":48,"y":323,"w":220,"h":16.9,"text":"H 27° · L 17°","size":13,"weight":400,"alignx":0,"color":"#718078"}
{"id":"forecast_title","t":"text","x":24,"y":384,"w":250,"h":26.0,"text":"This week","size":20,"weight":700,"alignx":0,"color":"#19372d"}
{"id":"forecast_title_detail","t":"text","x":270,"y":389,"w":112,"h":14.3,"text":"4-day outlook","size":11,"weight":400,"alignx":1,"color":"#718078"}
{"id":"forecast","t":"stack","x":24,"y":422,"w":358,"h":112,"radius":20,"bg":"#ffffff"}
{"id":"day_0","t":"stack","x":24.0,"y":422,"w":89.5,"h":112}
{"id":"day_label_0","t":"text","x":32.0,"y":435,"w":73.5,"h":15.6,"text":"Now","size":12,"weight":500,"alignx":0.5,"color":"#718078"}
{"id":"day_icon_0","t":"svg","x":52.0,"y":461,"w":34,"h":28,"graphic":"cloud"}
{"id":"day_temp_0","t":"text","x":32.0,"y":500,"w":73.5,"h":22.1,"text":"24°","size":17,"weight":700,"alignx":0.5,"color":"#19372d"}
{"id":"day_1","t":"stack","x":113.5,"y":422,"w":89.5,"h":112}
{"id":"day_label_1","t":"text","x":121.5,"y":435,"w":73.5,"h":15.6,"text":"Tue","size":12,"weight":500,"alignx":0.5,"color":"#718078"}
{"id":"day_icon_1","t":"svg","x":141.5,"y":461,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_1","t":"text","x":121.5,"y":500,"w":73.5,"h":22.1,"text":"25°","size":17,"weight":700,"alignx":0.5,"color":"#19372d"}
{"id":"day_2","t":"stack","x":203.0,"y":422,"w":89.5,"h":112}
{"id":"day_label_2","t":"text","x":211.0,"y":435,"w":73.5,"h":15.6,"text":"Wed","size":12,"weight":500,"alignx":0.5,"color":"#718078"}
{"id":"day_icon_2","t":"svg","x":231.0,"y":461,"w":34,"h":28,"graphic":"cloud"}
{"id":"day_temp_2","t":"text","x":211.0,"y":500,"w":73.5,"h":22.1,"text":"23°","size":17,"weight":700,"alignx":0.5,"color":"#19372d"}
{"id":"day_3","t":"stack","x":292.5,"y":422,"w":89.5,"h":112}
{"id":"day_label_3","t":"text","x":300.5,"y":435,"w":73.5,"h":15.6,"text":"Thu","size":12,"weight":500,"alignx":0.5,"color":"#718078"}
{"id":"day_icon_3","t":"svg","x":320.5,"y":461,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_3","t":"text","x":300.5,"y":500,"w":73.5,"h":22.1,"text":"22°","size":17,"weight":700,"alignx":0.5,"color":"#19372d"}
{"id":"details_title","t":"text","x":24,"y":570,"w":250,"h":26.0,"text":"Details","size":20,"weight":700,"alignx":0,"color":"#19372d"}
{"id":"humidity","t":"stack","x":24,"y":610,"w":171,"h":86,"radius":20,"bg":"#ffffff"}
{"id":"humidity_label","t":"text","x":40,"y":624,"w":139,"h":15.6,"text":"Humidity","size":12,"weight":500,"alignx":0,"color":"#718078"}
{"id":"humidity_value","t":"text","x":40,"y":649,"w":139,"h":32.5,"text":"64%","size":25,"weight":700,"alignx":0,"color":"#19372d"}
{"id":"wind","t":"stack","x":211,"y":610,"w":171,"h":86,"radius":20,"bg":"#ffffff"}
{"id":"wind_label","t":"text","x":227,"y":624,"w":139,"h":15.6,"text":"Wind","size":12,"weight":500,"alignx":0,"color":"#718078"}
{"id":"wind_value","t":"text","x":227,"y":649,"w":139,"h":32.5,"text":"12 km/h","size":25,"weight":700,"alignx":0,"color":"#19372d"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#285f49"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"My cities","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.
