#!/usr/bin/env python3
"""Extract real advance widths from the fonts embedded in the shared WASM runtime."""
import hashlib
import json
from pathlib import Path
from fontTools.ttLib import TTFont

root = Path(__file__).resolve().parents[2]
metrics, sources = {}, {}
for weight in ('Regular', 'Medium', 'Bold'):
    path = root / f'apps/aircon/wizard/wasm-host/resources/service/NotoSansSC-{weight}.ttf'
    font = TTFont(path)
    em, cmap, widths = font['head'].unitsPerEm, font.getBestCmap(), font['hmtx'].metrics
    metrics[weight] = {
        'advance': {str(code): round(widths[glyph][0] / em, 6) for code, glyph in cmap.items() if code < 0x3000},
        'default': 1,
    }
    sources[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
destination = Path(__file__).with_name('font-metrics.mjs')
destination.write_text('/** Advance widths from embedded Noto Sans SC, in em units. */\n'
                       + '// Source SHA256: ' + json.dumps(sources, separators=(',', ':')) + '\n'
                       + 'export default ' + json.dumps(metrics, separators=(',', ':')) + ';\n')
