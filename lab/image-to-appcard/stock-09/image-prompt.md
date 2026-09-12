Generate exactly ONE polished mobile stock app UX mockup titled "Holdings". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: Ledger-inspired holdings layout: large total, column headings and separated rows.. Palette: {"name": "Mint", "page": "EDF6F1", "panel": "FFFFFF", "ink": "173E34", "muted": "77968C", "tint": "D5EDE1", "accent": "22785D"}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
{"id":"page","t":"stack","x":0,"y":0,"w":406,"h":776,"bg":"#edf6f1"}
{"id":"heading","t":"text","x":24,"y":32,"w":290,"h":39.0,"text":"Holdings","size":30,"weight":700,"alignx":0,"color":"#173e34"}
{"id":"subtitle","t":"text","x":24,"y":76,"w":350,"h":16.9,"text":"Design fixture · Prices are illustrative","size":13,"weight":400,"alignx":0,"color":"#77968c"}
{"id":"balance_label","t":"text","x":24,"y":130,"w":358,"h":14.3,"text":"TOTAL HOLDINGS","size":11,"weight":700,"alignx":0,"color":"#77968c"}
{"id":"balance","t":"text","x":24,"y":166,"w":358,"h":57.2,"text":"$42,860.24","size":44,"weight":700,"alignx":0,"color":"#173e34"}
{"id":"asset_header","t":"text","x":24,"y":265,"w":180,"h":14.3,"text":"ASSET","size":11,"weight":700,"alignx":0,"color":"#77968c"}
{"id":"value_header","t":"text","x":210,"y":265,"w":172,"h":14.3,"text":"VALUE / CHANGE","size":11,"weight":700,"alignx":1,"color":"#77968c"}
{"id":"holding_0","t":"stack","x":24,"y":309,"w":358,"h":72,"radius":20,"bg":"#ffffff"}
{"id":"holding_0_symbol","t":"text","x":40,"y":321,"w":326,"h":20.8,"text":"AAPL","size":16,"weight":700,"alignx":0,"color":"#173e34"}
{"id":"holding_0_name","t":"text","x":40,"y":349,"w":326,"h":14.3,"text":"Apple","size":11,"weight":400,"alignx":0,"color":"#77968c"}
{"id":"holding_0_price","t":"text","x":247,"y":319,"w":119,"h":23.4,"text":"182.40","size":18,"weight":700,"alignx":1,"color":"#173e34"}
{"id":"holding_0_change","t":"text","x":247,"y":349,"w":119,"h":14.3,"text":"+1.24%","size":11,"weight":500,"alignx":1,"color":"#22785d"}
{"id":"holding_1","t":"stack","x":24,"y":396,"w":358,"h":72,"radius":20,"bg":"#ffffff"}
{"id":"holding_1_symbol","t":"text","x":40,"y":408,"w":326,"h":20.8,"text":"NVDA","size":16,"weight":700,"alignx":0,"color":"#173e34"}
{"id":"holding_1_name","t":"text","x":40,"y":436,"w":326,"h":14.3,"text":"NVIDIA","size":11,"weight":400,"alignx":0,"color":"#77968c"}
{"id":"holding_1_price","t":"text","x":247,"y":406,"w":119,"h":23.4,"text":"124.80","size":18,"weight":700,"alignx":1,"color":"#173e34"}
{"id":"holding_1_change","t":"text","x":247,"y":436,"w":119,"h":14.3,"text":"+2.16%","size":11,"weight":500,"alignx":1,"color":"#22785d"}
{"id":"holding_2","t":"stack","x":24,"y":483,"w":358,"h":72,"radius":20,"bg":"#ffffff"}
{"id":"holding_2_symbol","t":"text","x":40,"y":495,"w":326,"h":20.8,"text":"MSFT","size":16,"weight":700,"alignx":0,"color":"#173e34"}
{"id":"holding_2_name","t":"text","x":40,"y":523,"w":326,"h":14.3,"text":"Microsoft","size":11,"weight":400,"alignx":0,"color":"#77968c"}
{"id":"holding_2_price","t":"text","x":247,"y":493,"w":119,"h":23.4,"text":"416.20","size":18,"weight":700,"alignx":1,"color":"#173e34"}
{"id":"holding_2_change","t":"text","x":247,"y":523,"w":119,"h":14.3,"text":"+0.83%","size":11,"weight":500,"alignx":1,"color":"#22785d"}
{"id":"holding_3","t":"stack","x":24,"y":570,"w":358,"h":72,"radius":20,"bg":"#ffffff"}
{"id":"holding_3_symbol","t":"text","x":40,"y":582,"w":326,"h":20.8,"text":"GOOGL","size":16,"weight":700,"alignx":0,"color":"#173e34"}
{"id":"holding_3_name","t":"text","x":40,"y":610,"w":326,"h":14.3,"text":"Alphabet","size":11,"weight":400,"alignx":0,"color":"#77968c"}
{"id":"holding_3_price","t":"text","x":247,"y":580,"w":119,"h":23.4,"text":"165.30","size":18,"weight":700,"alignx":1,"color":"#173e34"}
{"id":"holding_3_change","t":"text","x":247,"y":610,"w":119,"h":14.3,"text":"+0.62%","size":11,"weight":500,"alignx":1,"color":"#22785d"}
{"id":"primary","t":"stack","x":24,"y":708,"w":358,"h":44}
{"id":"primary_surface","t":"stack","x":24,"y":708,"w":358,"h":44,"radius":14,"bg":"#22785d"}
{"id":"primary_label","t":"text","x":32,"y":720.0,"w":342,"h":20,"text":"View watchlist","size":14,"weight":500,"alignx":0.5,"color":"#ffffff"}

Render only this single finished app screen. Fit every element within the artboard.

The background MUST be fully opaque from edge to edge. Paint the specified page background color across the entire canvas. Every pixel must have alpha 255; absolutely no transparency, cutouts or checkerboards.