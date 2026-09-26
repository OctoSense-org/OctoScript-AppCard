Generate exactly ONE polished mobile stock app UX mockup titled "Market tiles". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Two-column market tile grid with mini line charts inside each company card.. Palette: {"name": "Cobalt", "page": "F3F5FA", "panel": "FFFFFF", "ink": "172D56", "muted": "75829B", "tint": "DFE9FF", "accent": "2F61D5"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#f3f5fa"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Market tiles","size":30,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Design fixture · Prices are illustrative","size":13,"weight":400,"alignx":0,"color":"#75829b"}
{"id":"tile_0","t":"stack","x":24,"y":126,"w":171,"h":210,"radius":20,"bg":"#dfe9ff"}
{"id":"symbol_0","t":"text","x":40,"y":141,"w":139,"h":26.0,"text":"AAPL","size":20,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"price_0","t":"text","x":40,"y":180,"w":139,"h":32.5,"text":"$182.40","size":25,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"chart_0","t":"svg","x":40,"y":231,"w":139,"h":52,"graphic":"line"}
{"id":"gain_0","t":"text","x":40,"y":302,"w":139,"h":16.9,"text":"+1.24%","size":13,"weight":500,"alignx":0,"color":"#2f61d5"}
{"id":"tile_1","t":"stack","x":211,"y":126,"w":171,"h":210,"radius":20,"bg":"#ffffff"}
{"id":"symbol_1","t":"text","x":227,"y":141,"w":139,"h":26.0,"text":"NVDA","size":20,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"price_1","t":"text","x":227,"y":180,"w":139,"h":32.5,"text":"$124.80","size":25,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"chart_1","t":"svg","x":227,"y":231,"w":139,"h":52,"graphic":"line"}
{"id":"gain_1","t":"text","x":227,"y":302,"w":139,"h":16.9,"text":"+2.16%","size":13,"weight":500,"alignx":0,"color":"#2f61d5"}
{"id":"tile_2","t":"stack","x":24,"y":356,"w":171,"h":210,"radius":20,"bg":"#ffffff"}
{"id":"symbol_2","t":"text","x":40,"y":371,"w":139,"h":26.0,"text":"MSFT","size":20,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"price_2","t":"text","x":40,"y":410,"w":139,"h":32.5,"text":"$416.20","size":25,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"chart_2","t":"svg","x":40,"y":461,"w":139,"h":52,"graphic":"line"}
{"id":"gain_2","t":"text","x":40,"y":532,"w":139,"h":16.9,"text":"+0.83%","size":13,"weight":500,"alignx":0,"color":"#2f61d5"}
{"id":"tile_3","t":"stack","x":211,"y":356,"w":171,"h":210,"radius":20,"bg":"#ffffff"}
{"id":"symbol_3","t":"text","x":227,"y":371,"w":139,"h":26.0,"text":"GOOGL","size":20,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"price_3","t":"text","x":227,"y":410,"w":139,"h":32.5,"text":"$165.30","size":25,"weight":700,"alignx":0,"color":"#172d56"}
{"id":"chart_3","t":"svg","x":227,"y":461,"w":139,"h":52,"graphic":"line"}
{"id":"gain_3","t":"text","x":227,"y":532,"w":139,"h":16.9,"text":"+0.62%","size":13,"weight":500,"alignx":0,"color":"#2f61d5"}
{"id":"note","t":"text","x":24,"y":636,"w":358,"h":20.8,"text":"Four companies. One clear view.","size":16,"weight":500,"alignx":0,"color":"#75829b"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#2f61d5"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"View watchlist","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.

The background MUST be fully opaque from edge to edge. Every pixel must have alpha 255; no transparency, cutouts or checkerboards.