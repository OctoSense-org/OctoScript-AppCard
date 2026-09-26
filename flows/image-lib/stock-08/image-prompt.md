Generate exactly ONE polished mobile stock app UX mockup titled "Compare". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Two-security comparison: paired quote cards, dual line chart and metric grid.. Palette: {"name": "Clay", "page": "F4EEE8", "panel": "FFFCF8", "ink": "42352D", "muted": "988679", "tint": "E9D6C7", "accent": "996343"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#f4eee8"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Compare","size":30,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Design fixture · Prices are illustrative","size":13,"weight":400,"alignx":0,"color":"#988679"}
{"id":"compare_0","t":"stack","x":24,"y":127,"w":171,"h":142,"radius":20,"bg":"#e9d6c7"}
{"id":"symbol_0","t":"text","x":40,"y":145,"w":139,"h":24.7,"text":"AAPL","size":19,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"price_0","t":"text","x":40,"y":187,"w":139,"h":33.8,"text":"$182.40","size":26,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"change_0","t":"text","x":40,"y":235,"w":139,"h":15.6,"text":"+1.24%","size":12,"weight":500,"alignx":0,"color":"#996343"}
{"id":"compare_1","t":"stack","x":211,"y":127,"w":171,"h":142,"radius":20,"bg":"#fffcf8"}
{"id":"symbol_1","t":"text","x":227,"y":145,"w":139,"h":24.7,"text":"NVDA","size":19,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"price_1","t":"text","x":227,"y":187,"w":139,"h":33.8,"text":"$124.80","size":26,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"change_1","t":"text","x":227,"y":235,"w":139,"h":15.6,"text":"+2.16%","size":12,"weight":500,"alignx":0,"color":"#996343"}
{"id":"performance_title","t":"text","x":24,"y":302,"w":250,"h":26.0,"text":"Relative performance","size":20,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"comparison","t":"stack","x":24,"y":348,"w":358,"h":204,"radius":20,"bg":"#fffcf8"}
{"id":"comparison_chart","t":"svg","x":44,"y":370,"w":318,"h":158,"graphic":"compare"}
{"id":"apple_return","t":"stack","x":24,"y":584,"w":171,"h":92,"radius":20,"bg":"#fffcf8"}
{"id":"apple_return_label","t":"text","x":40,"y":598,"w":139,"h":15.6,"text":"Apple / 1 month","size":12,"weight":500,"alignx":0,"color":"#988679"}
{"id":"apple_return_value","t":"text","x":40,"y":623,"w":139,"h":32.5,"text":"+4.2%","size":25,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"nvidia_return","t":"stack","x":211,"y":584,"w":171,"h":92,"radius":20,"bg":"#fffcf8"}
{"id":"nvidia_return_label","t":"text","x":227,"y":598,"w":139,"h":15.6,"text":"NVIDIA / 1 month","size":12,"weight":500,"alignx":0,"color":"#988679"}
{"id":"nvidia_return_value","t":"text","x":227,"y":623,"w":139,"h":32.5,"text":"+8.6%","size":25,"weight":700,"alignx":0,"color":"#42352d"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#996343"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"View watchlist","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.

The background MUST be fully opaque from edge to edge. Paint the specified page background color across the entire canvas. Every pixel must have alpha 255; absolutely no transparency, cutouts or checkerboards.