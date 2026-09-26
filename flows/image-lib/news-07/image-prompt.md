Generate exactly ONE polished mobile news app UX mockup titled "Listen today". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Audio-first news dashboard with large episode card and two upcoming episodes.. Palette: {"name": "Lavender", "page": "F4F0FA", "panel": "FFFFFF", "ink": "3A2A56", "muted": "8C7C9C", "tint": "E5DDF4", "accent": "7551A9"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#f4f0fa"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Listen today","size":30,"weight":700,"alignx":0,"color":"#3a2a56"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Independent stories. Fresh perspectives.","size":13,"weight":400,"alignx":0,"color":"#8c7c9c"}
{"id":"episode","t":"stack","x":24,"y":124,"w":358,"h":310,"radius":26,"bg":"#e5ddf4"}
{"id":"episode_tag","t":"text","x":44,"y":145,"w":318,"h":14.3,"text":"THE DAILY AUDIO","size":11,"weight":700,"alignx":0,"color":"#8c7c9c"}
{"id":"waveform","t":"svg","x":44,"y":197,"w":318,"h":74,"graphic":"wave"}
{"id":"episode_title","t":"text","x":44,"y":301,"w":318,"h":35.1,"text":"The world, in focus.","size":27,"weight":700,"alignx":0,"color":"#3a2a56"}
{"id":"episode_meta","t":"text","x":44,"y":346,"w":318,"h":18.2,"text":"A 12-minute morning briefing","size":14,"weight":400,"alignx":0,"color":"#8c7c9c"}
{"id":"play","t":"stack","x":44,"y":383,"w":180,"h":34}
{"id":"play_surface","t":"stack","x":44,"y":383,"w":180,"h":34,"radius":14,"bg":"#7551a9"}
{"id":"play_label","t":"text","x":52,"y":390.0,"w":164,"h":20,"text":"Play episode","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}
{"id":"up_next","t":"text","x":24,"y":462,"w":250,"h":26.0,"text":"Up next","size":20,"weight":700,"alignx":0,"color":"#3a2a56"}
{"id":"next","t":"stack","x":24,"y":505,"w":358,"h":112,"radius":20,"bg":"#ffffff"}
{"id":"next_tag","t":"text","x":44,"y":519,"w":260,"h":13.0,"text":"SCIENCE","size":10,"weight":700,"alignx":0,"color":"#8c7c9c"}
{"id":"next_title","t":"text","x":44,"y":541,"w":326,"h":24.7,"text":"The next chapter","size":19,"weight":700,"alignx":0,"color":"#3a2a56"}
{"id":"next_title2","t":"text","x":44,"y":566,"w":326,"h":24.7,"text":"of clean energy","size":19,"weight":700,"alignx":0,"color":"#3a2a56"}
{"id":"next_meta","t":"text","x":44,"y":593,"w":150,"h":13.0,"text":"4 min read","size":10,"weight":400,"alignx":0,"color":"#8c7c9c"}
{"id":"queue_note","t":"text","x":24,"y":659,"w":358,"h":16.9,"text":"New episodes every weekday.","size":13,"weight":400,"alignx":0,"color":"#8c7c9c"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#7551a9"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"Your reading list","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.

The background MUST be fully opaque from edge to edge. Paint the specified page background color across the entire canvas. Every pixel must have alpha 255; absolutely no transparency, cutouts or checkerboards.