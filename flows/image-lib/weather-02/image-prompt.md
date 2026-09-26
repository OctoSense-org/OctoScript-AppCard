Generate exactly ONE polished mobile weather app UX mockup titled "Evening forecast". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Dark split hero with the temperature on the left and an icon on the right; stacked daily forecast.. Palette: {"name": "Midnight", "page": "111827", "panel": "1C293C", "ink": "F2F5FC", "muted": "9AACC5", "tint": "253C58", "accent": "92C9ED"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#111827"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Evening forecast","size":30,"weight":700,"alignx":0,"color":"#f2f5fc"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Monday, September 7","size":13,"weight":400,"alignx":0,"color":"#9aacc5"}
{"id":"location","t":"text","x":24,"y":123,"w":300,"h":15.6,"text":"CUPERTINO","size":12,"weight":700,"alignx":0,"color":"#9aacc5"}
{"id":"temperature","t":"text","x":24,"y":154,"w":240,"h":122.2,"text":"24°","size":94,"weight":500,"alignx":0,"color":"#f2f5fc"}
{"id":"weather_symbol","t":"svg","x":268,"y":165,"w":106,"h":96,"graphic":"moon"}
{"id":"condition","t":"text","x":24,"y":276,"w":350,"h":23.4,"text":"A calm, clear evening","size":18,"weight":500,"alignx":0,"color":"#f2f5fc"}
{"id":"forecast_title","t":"text","x":24,"y":321,"w":250,"h":26.0,"text":"Next few days","size":20,"weight":700,"alignx":0,"color":"#f2f5fc"}
{"id":"forecast","t":"stack","x":24,"y":365,"w":358,"h":256,"radius":20,"bg":"#1c293c"}
{"id":"day_0","t":"stack","x":24,"y":365,"w":358,"h":64}
{"id":"day_label_0","t":"text","x":42,"y":385,"w":120,"h":18.2,"text":"Now","size":14,"weight":500,"alignx":0,"color":"#f2f5fc"}
{"id":"day_icon_0","t":"svg","x":208,"y":381,"w":34,"h":28,"graphic":"cloud"}
{"id":"day_temp_0","t":"text","x":290,"y":382,"w":70,"h":27.3,"text":"24°","size":21,"weight":700,"alignx":1,"color":"#f2f5fc"}
{"id":"day_1","t":"stack","x":24,"y":429,"w":358,"h":64}
{"id":"day_label_1","t":"text","x":42,"y":449,"w":120,"h":18.2,"text":"Tue","size":14,"weight":500,"alignx":0,"color":"#f2f5fc"}
{"id":"day_icon_1","t":"svg","x":208,"y":445,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_1","t":"text","x":290,"y":446,"w":70,"h":27.3,"text":"25°","size":21,"weight":700,"alignx":1,"color":"#f2f5fc"}
{"id":"day_2","t":"stack","x":24,"y":493,"w":358,"h":64}
{"id":"day_label_2","t":"text","x":42,"y":513,"w":120,"h":18.2,"text":"Wed","size":14,"weight":500,"alignx":0,"color":"#f2f5fc"}
{"id":"day_icon_2","t":"svg","x":208,"y":509,"w":34,"h":28,"graphic":"cloud"}
{"id":"day_temp_2","t":"text","x":290,"y":510,"w":70,"h":27.3,"text":"23°","size":21,"weight":700,"alignx":1,"color":"#f2f5fc"}
{"id":"day_3","t":"stack","x":24,"y":557,"w":358,"h":64}
{"id":"day_label_3","t":"text","x":42,"y":577,"w":120,"h":18.2,"text":"Thu","size":14,"weight":500,"alignx":0,"color":"#f2f5fc"}
{"id":"day_icon_3","t":"svg","x":208,"y":573,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_3","t":"text","x":290,"y":574,"w":70,"h":27.3,"text":"22°","size":21,"weight":700,"alignx":1,"color":"#f2f5fc"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#92c9ed"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"My cities","size":14,"weight":500,"alignx":0.5,"color":"#111827"}

Render only this single finished app screen. Fit every element within the artboard.
