Generate exactly ONE polished mobile weather app UX mockup titled "Plan your week". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Weekly planner: compact current weather followed by a long five-day forecast list.. Palette: {"name": "Mint", "page": "EDF6F1", "panel": "FFFFFF", "ink": "173E34", "muted": "77968C", "tint": "D5EDE1", "accent": "22785D"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#edf6f1"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Plan your week","size":30,"weight":700,"alignx":0,"color":"#173e34"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Monday, September 7","size":13,"weight":400,"alignx":0,"color":"#77968c"}
{"id":"location","t":"text","x":24,"y":120,"w":250,"h":20.8,"text":"Cupertino","size":16,"weight":700,"alignx":0,"color":"#173e34"}
{"id":"temperature","t":"text","x":277,"y":110,"w":105,"h":62.4,"text":"24°","size":48,"weight":500,"alignx":1,"color":"#173e34"}
{"id":"forecast_title","t":"text","x":24,"y":181,"w":250,"h":26.0,"text":"Five-day outlook","size":20,"weight":700,"alignx":0,"color":"#173e34"}
{"id":"forecast","t":"stack","x":24,"y":227,"w":358,"h":320,"radius":20,"bg":"#ffffff"}
{"id":"day_0","t":"stack","x":24,"y":227,"w":358,"h":64}
{"id":"day_label_0","t":"text","x":42,"y":247,"w":120,"h":18.2,"text":"Monday","size":14,"weight":500,"alignx":0,"color":"#173e34"}
{"id":"day_icon_0","t":"svg","x":208,"y":243,"w":34,"h":28,"graphic":"cloud"}
{"id":"day_temp_0","t":"text","x":290,"y":244,"w":70,"h":27.3,"text":"24°","size":21,"weight":700,"alignx":1,"color":"#173e34"}
{"id":"day_1","t":"stack","x":24,"y":291,"w":358,"h":64}
{"id":"day_label_1","t":"text","x":42,"y":311,"w":120,"h":18.2,"text":"Tuesday","size":14,"weight":500,"alignx":0,"color":"#173e34"}
{"id":"day_icon_1","t":"svg","x":208,"y":307,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_1","t":"text","x":290,"y":308,"w":70,"h":27.3,"text":"25°","size":21,"weight":700,"alignx":1,"color":"#173e34"}
{"id":"day_2","t":"stack","x":24,"y":355,"w":358,"h":64}
{"id":"day_label_2","t":"text","x":42,"y":375,"w":120,"h":18.2,"text":"Wednesday","size":14,"weight":500,"alignx":0,"color":"#173e34"}
{"id":"day_icon_2","t":"svg","x":208,"y":371,"w":34,"h":28,"graphic":"cloud"}
{"id":"day_temp_2","t":"text","x":290,"y":372,"w":70,"h":27.3,"text":"23°","size":21,"weight":700,"alignx":1,"color":"#173e34"}
{"id":"day_3","t":"stack","x":24,"y":419,"w":358,"h":64}
{"id":"day_label_3","t":"text","x":42,"y":439,"w":120,"h":18.2,"text":"Thursday","size":14,"weight":500,"alignx":0,"color":"#173e34"}
{"id":"day_icon_3","t":"svg","x":208,"y":435,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_3","t":"text","x":290,"y":436,"w":70,"h":27.3,"text":"22°","size":21,"weight":700,"alignx":1,"color":"#173e34"}
{"id":"day_4","t":"stack","x":24,"y":483,"w":358,"h":64}
{"id":"day_label_4","t":"text","x":42,"y":503,"w":120,"h":18.2,"text":"Friday","size":14,"weight":500,"alignx":0,"color":"#173e34"}
{"id":"day_icon_4","t":"svg","x":208,"y":499,"w":34,"h":28,"graphic":"sun"}
{"id":"day_temp_4","t":"text","x":290,"y":500,"w":70,"h":27.3,"text":"24°","size":21,"weight":700,"alignx":1,"color":"#173e34"}
{"id":"note","t":"text","x":24,"y":592,"w":358,"h":23.4,"text":"Best day outside: Tuesday","size":18,"weight":700,"alignx":0,"color":"#173e34"}
{"id":"note_detail","t":"text","x":24,"y":627,"w":358,"h":16.9,"text":"Low wind and long sunny intervals.","size":13,"weight":400,"alignx":0,"color":"#77968c"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#22785d"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"My cities","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.

The background MUST be fully opaque from edge to edge. Every pixel must have alpha 255; no transparency, cutouts or checkerboards.