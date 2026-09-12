Generate exactly ONE polished mobile stock app UX mockup titled "Market overview". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Market dashboard with three index summaries and a large market trend chart.. Palette: {"name": "Editorial", "page": "F4F2EB", "panel": "FCFBF7", "ink": "252922", "muted": "797E70", "tint": "E4E7D4", "accent": "536241"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#f4f2eb"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Market overview","size":30,"weight":700,"alignx":0,"color":"#252922"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Design fixture · Prices are illustrative","size":13,"weight":400,"alignx":0,"color":"#797e70"}
{"id":"index_0","t":"stack","x":24,"y":126,"w":114,"h":124,"radius":20,"bg":"#e4e7d4"}
{"id":"index_label_0","t":"text","x":36,"y":143,"w":90,"h":13.0,"text":"S&P 500","size":10,"weight":700,"alignx":0,"color":"#797e70"}
{"id":"index_value_0","t":"text","x":36,"y":180,"w":90,"h":28.6,"text":"5,420","size":22,"weight":700,"alignx":0,"color":"#252922"}
{"id":"index_gain_0","t":"text","x":36,"y":218,"w":90,"h":14.3,"text":"+0.82%","size":11,"weight":500,"alignx":0,"color":"#536241"}
{"id":"index_1","t":"stack","x":146,"y":126,"w":114,"h":124,"radius":20,"bg":"#fcfbf7"}
{"id":"index_label_1","t":"text","x":158,"y":143,"w":90,"h":13.0,"text":"NASDAQ","size":10,"weight":700,"alignx":0,"color":"#797e70"}
{"id":"index_value_1","t":"text","x":158,"y":180,"w":90,"h":28.6,"text":"17,132","size":22,"weight":700,"alignx":0,"color":"#252922"}
{"id":"index_gain_1","t":"text","x":158,"y":218,"w":90,"h":14.3,"text":"+0.82%","size":11,"weight":500,"alignx":0,"color":"#536241"}
{"id":"index_2","t":"stack","x":268,"y":126,"w":114,"h":124,"radius":20,"bg":"#fcfbf7"}
{"id":"index_label_2","t":"text","x":280,"y":143,"w":90,"h":13.0,"text":"DOW","size":10,"weight":700,"alignx":0,"color":"#797e70"}
{"id":"index_value_2","t":"text","x":280,"y":180,"w":90,"h":28.6,"text":"39,420","size":22,"weight":700,"alignx":0,"color":"#252922"}
{"id":"index_gain_2","t":"text","x":280,"y":218,"w":90,"h":14.3,"text":"+0.82%","size":11,"weight":500,"alignx":0,"color":"#536241"}
{"id":"trend_title","t":"text","x":24,"y":285,"w":250,"h":26.0,"text":"Market trend","size":20,"weight":700,"alignx":0,"color":"#252922"}
{"id":"trend","t":"stack","x":24,"y":332,"w":358,"h":212,"radius":20,"bg":"#fcfbf7"}
{"id":"market_chart","t":"svg","x":44,"y":355,"w":318,"h":162,"graphic":"line"}
{"id":"quote","t":"stack","x":24,"y":578,"w":358,"h":72,"radius":20,"bg":"#fcfbf7"}
{"id":"quote_symbol","t":"text","x":40,"y":590,"w":326,"h":20.8,"text":"AAPL","size":16,"weight":700,"alignx":0,"color":"#252922"}
{"id":"quote_name","t":"text","x":40,"y":618,"w":326,"h":14.3,"text":"Apple","size":11,"weight":400,"alignx":0,"color":"#797e70"}
{"id":"quote_price","t":"text","x":247,"y":588,"w":119,"h":23.4,"text":"182.40","size":18,"weight":700,"alignx":1,"color":"#252922"}
{"id":"quote_change","t":"text","x":247,"y":618,"w":119,"h":14.3,"text":"+1.24%","size":11,"weight":500,"alignx":1,"color":"#536241"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#536241"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"View watchlist","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.

The background MUST be fully opaque from edge to edge. Every pixel must have alpha 255; no transparency, cutouts or checkerboards.