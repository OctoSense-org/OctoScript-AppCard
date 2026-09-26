Generate exactly ONE polished mobile weather app UX mockup titled "Conditions". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Compact utility layout: horizontal conditions, a two-column metric grid, short outlook.. Palette: {"name": "Clay", "page": "F4EEE8", "panel": "FFFCF8", "ink": "42352D", "muted": "988679", "tint": "E9D6C7", "accent": "996343"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#f4eee8"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Conditions","size":30,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Monday, September 7","size":13,"weight":400,"alignx":0,"color":"#988679"}
{"id":"current","t":"stack","x":24,"y":118,"w":358,"h":120,"radius":20,"bg":"#e9d6c7"}
{"id":"weather_symbol","t":"svg","x":42,"y":151,"w":70,"h":56,"graphic":"cloud"}
{"id":"temperature","t":"text","x":131,"y":131,"w":126,"h":72.8,"text":"24°","size":56,"weight":500,"alignx":0,"color":"#42352d"}
{"id":"location","t":"text","x":264,"y":146,"w":105,"h":18.2,"text":"Cupertino","size":14,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"condition","t":"text","x":264,"y":181,"w":105,"h":15.6,"text":"Cloudy","size":12,"weight":400,"alignx":0,"color":"#988679"}
{"id":"metric_0","t":"stack","x":24,"y":272,"w":171,"h":92,"radius":20,"bg":"#fffcf8"}
{"id":"metric_0_label","t":"text","x":40,"y":286,"w":139,"h":15.6,"text":"Humidity","size":12,"weight":500,"alignx":0,"color":"#988679"}
{"id":"metric_0_value","t":"text","x":40,"y":311,"w":139,"h":32.5,"text":"64%","size":25,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"metric_1","t":"stack","x":211,"y":272,"w":171,"h":92,"radius":20,"bg":"#fffcf8"}
{"id":"metric_1_label","t":"text","x":227,"y":286,"w":139,"h":15.6,"text":"Wind","size":12,"weight":500,"alignx":0,"color":"#988679"}
{"id":"metric_1_value","t":"text","x":227,"y":311,"w":139,"h":32.5,"text":"12 km/h","size":25,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"metric_2","t":"stack","x":24,"y":382,"w":171,"h":92,"radius":20,"bg":"#fffcf8"}
{"id":"metric_2_label","t":"text","x":40,"y":396,"w":139,"h":15.6,"text":"Feels like","size":12,"weight":500,"alignx":0,"color":"#988679"}
{"id":"metric_2_value","t":"text","x":40,"y":421,"w":139,"h":32.5,"text":"25°","size":25,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"metric_3","t":"stack","x":211,"y":382,"w":171,"h":92,"radius":20,"bg":"#fffcf8"}
{"id":"metric_3_label","t":"text","x":227,"y":396,"w":139,"h":15.6,"text":"UV index","size":12,"weight":500,"alignx":0,"color":"#988679"}
{"id":"metric_3_value","t":"text","x":227,"y":421,"w":139,"h":32.5,"text":"4","size":25,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"forecast_title","t":"text","x":24,"y":520,"w":250,"h":26.0,"text":"Today into tomorrow","size":20,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"forecast","t":"stack","x":24,"y":564,"w":358,"h":112,"radius":20,"bg":"#fffcf8"}
{"id":"day_0","t":"stack","x":24.0,"y":564,"w":89.5,"h":112}
{"id":"day_label_0","t":"text","x":32.0,"y":577,"w":73.5,"h":15.6,"text":"Now","size":12,"weight":500,"alignx":0.5,"color":"#988679"}
{"id":"day_icon_0","t":"svg","x":52.0,"y":603,"w":34,"h":28,"graphic":"cloud"}
{"id":"day_temp_0","t":"text","x":32.0,"y":642,"w":73.5,"h":22.1,"text":"24°","size":17,"weight":700,"alignx":0.5,"color":"#42352d"}
{"id":"day_1","t":"stack","x":113.5,"y":564,"w":89.5,"h":112}
{"id":"day_label_1","t":"text","x":121.5,"y":577,"w":73.5,"h":15.6,"text":"Tue","size":12,"weight":500,"alignx":0.5,"color":"#988679"}
{"id":"day_icon_1","t":"svg","x":141.5,"y":603,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_1","t":"text","x":121.5,"y":642,"w":73.5,"h":22.1,"text":"25°","size":17,"weight":700,"alignx":0.5,"color":"#42352d"}
{"id":"day_2","t":"stack","x":203.0,"y":564,"w":89.5,"h":112}
{"id":"day_label_2","t":"text","x":211.0,"y":577,"w":73.5,"h":15.6,"text":"Wed","size":12,"weight":500,"alignx":0.5,"color":"#988679"}
{"id":"day_icon_2","t":"svg","x":231.0,"y":603,"w":34,"h":28,"graphic":"cloud"}
{"id":"day_temp_2","t":"text","x":211.0,"y":642,"w":73.5,"h":22.1,"text":"23°","size":17,"weight":700,"alignx":0.5,"color":"#42352d"}
{"id":"day_3","t":"stack","x":292.5,"y":564,"w":89.5,"h":112}
{"id":"day_label_3","t":"text","x":300.5,"y":577,"w":73.5,"h":15.6,"text":"Thu","size":12,"weight":500,"alignx":0.5,"color":"#988679"}
{"id":"day_icon_3","t":"svg","x":320.5,"y":603,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_3","t":"text","x":300.5,"y":642,"w":73.5,"h":22.1,"text":"22°","size":17,"weight":700,"alignx":0.5,"color":"#42352d"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#996343"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"My cities","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.

The background MUST be fully opaque from edge to edge. Every pixel must have alpha 255; no transparency, cutouts or checkerboards.