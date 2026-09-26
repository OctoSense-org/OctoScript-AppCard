#!/usr/bin/env python3
"""Export this flow using the reusable pipeline, retaining artwork in this project."""
import json
import hashlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT.parents[1] / 'flows'
sys.path.insert(0, str(PIPELINE / 'image-lib'))
import compile as compiler
compiler.GALLERY = ROOT / 'artwork'
sys.path.insert(0, str(PIPELINE / 'image-to-card'))
import atlas
import extract
import bundle

manifest = ROOT / 'image-to-appcard-flow.json'
intake = atlas.intake(manifest, ROOT, ROOT / 'pipeline-output/intake')
result = {'intake': {'fingerprint': intake['input_fingerprint'], 'scenes': len(intake['scenes']),
                     'actual_size': intake['generation']['actual_size'],
                     'requested_size_matches_actual': intake['generation']['requested_size_matches_actual']}}
if not (ROOT / 'service-cards').exists():
    result['extract'] = extract.extract(manifest, ROOT, ROOT / 'service-cards')
else:
    catalogue = json.loads((ROOT / 'service-cards/catalogue.json').read_text())
    for card in catalogue['cards']:
        mapped = json.loads((ROOT / 'service-cards' / card['folder'] / 'mapped.json').read_text())
        source = mapped['changes'][0]
        current = hashlib.sha256((ROOT / source['source']).read_bytes()).hexdigest()
        if current != source['source_sha256']:
            raise RuntimeError('Standalone source changed: retain the old extraction and select a new output directory')
    result['extract'] = {'retained': True, 'output': 'service-cards'}
result['bundle'] = bundle.export_bundle(ROOT, manifest, ROOT / 'wizard/card-bundle')
print(json.dumps(result, ensure_ascii=False, indent=2))
