Generate exactly ONE polished mobile stock app UX mockup titled "Portfolio". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Portfolio overview with large balance, area chart and two stock rows.. Palette: {"name": "Sage", "page": "F5F6F0", "panel": "FFFFFF", "ink": "19372D", "muted": "718078", "tint": "E3EDE3", "accent": "285F49"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#f5f6f0"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Portfolio","size":30,"weight":700,"alignx":0,"color":"#19372d"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Design fixture · Prices are illustrative","size":13,"weight":400,"alignx":0,"color":"#718078"}
{"id":"portfolio","t":"stack","x":24,"y":119,"w":358,"h":290,"radius":20,"bg":"#e3ede3"}
{"id":"balance_label","t":"text","x":44,"y":140,"w":318,"h":14.3,"text":"TOTAL VALUE","size":11,"weight":700,"alignx":0,"color":"#718078"}
{"id":"balance","t":"text","x":44,"y":174,"w":318,"h":55.9,"text":"$42,860.24","size":43,"weight":700,"alignx":0,"color":"#19372d"}
{"id":"gain","t":"text","x":44,"y":238,"w":318,"h":16.9,"text":"+$842.16  (2.01%) today","size":13,"weight":500,"alignx":0,"color":"#285f49"}
{"id":"portfolio_chart","t":"svg","x":44,"y":284,"w":318,"h":96,"graphic":"line"}
{"id":"watchlist_title","t":"text","x":24,"y":438,"w":250,"h":26.0,"text":"Watchlist","size":20,"weight":700,"alignx":0,"color":"#19372d"}
{"id":"quote_0","t":"stack","x":24,"y":480,"w":358,"h":72,"radius":20,"bg":"#ffffff"}
{"id":"quote_0_symbol","t":"text","x":40,"y":492,"w":326,"h":20.8,"text":"AAPL","size":16,"weight":700,"alignx":0,"color":"#19372d"}
{"id":"quote_0_name","t":"text","x":40,"y":520,"w":326,"h":14.3,"text":"Apple","size":11,"weight":400,"alignx":0,"color":"#718078"}
{"id":"quote_0_price","t":"text","x":247,"y":490,"w":119,"h":23.4,"text":"182.40","size":18,"weight":700,"alignx":1,"color":"#19372d"}
{"id":"quote_0_change","t":"text","x":247,"y":520,"w":119,"h":14.3,"text":"+1.24%","size":11,"weight":500,"alignx":1,"color":"#285f49"}
{"id":"quote_1","t":"stack","x":24,"y":571,"w":358,"h":72,"radius":20,"bg":"#ffffff"}
{"id":"quote_1_symbol","t":"text","x":40,"y":583,"w":326,"h":20.8,"text":"NVDA","size":16,"weight":700,"alignx":0,"color":"#19372d"}
{"id":"quote_1_name","t":"text","x":40,"y":611,"w":326,"h":14.3,"text":"NVIDIA","size":11,"weight":400,"alignx":0,"color":"#718078"}
{"id":"quote_1_price","t":"text","x":247,"y":581,"w":119,"h":23.4,"text":"124.80","size":18,"weight":700,"alignx":1,"color":"#19372d"}
{"id":"quote_1_change","t":"text","x":247,"y":611,"w":119,"h":14.3,"text":"+2.16%","size":11,"weight":500,"alignx":1,"color":"#285f49"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#285f49"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"View watchlist","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.
