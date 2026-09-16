#!/usr/bin/env python3
"""Mount each extracted App Card through the caller-owned Makepad Studio RunItem."""
import argparse
from datetime import datetime, timezone
import fcntl
import json
from pathlib import Path
import shutil
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'apps/aircon/scripts'), str(ROOT / 'lab/image-to-appcard'), str(ROOT / 'lab')]
import verify_standalone_cards as native
import studio
from core.gate_structure import parse_dump

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--flows', default='school,health,reunion')
parser.add_argument('--build-id', required=True, type=json.loads)
parser.add_argument('--cards', help='Comma-separated card IDs for a targeted repair check')
args = parser.parse_args()
selected = set(args.cards.split(',')) if args.cards else None
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:6]
output = ROOT / 'apps/shared/evidence/standalone' / stamp
output.mkdir(parents=True)
report = {'passed': False, 'build_id': args.build_id, 'scope': native.SCOPE, 'cards': []}
cards = []
for flow in args.flows.split(','):
    project = ROOT / 'apps' / flow
    native.require(project.resolve().parent == (ROOT / 'apps').resolve(), 'Invalid flow path')
    manifest = native.read(project / 'image-to-appcard-flow.json')
    exported = project / manifest['outputs']['cards']
    for original in native.read(exported / 'catalogue.json')['cards']:
        if selected is not None and original['id'] not in selected: continue
        card = {**original, 'source_surface': original['root']}
        folder = (exported / card['folder']).resolve()
        native.require(folder.is_relative_to(exported.resolve()), 'Export escapes project')
        contract, mapping = native.read(folder / 'contract.json'), native.read(folder / 'mapping.json')
        native.require(contract.get('standalone_service_card') is True, 'Expected a standalone card')
        native.require(contract['artboard'] == card['artboard'], 'Artboard mismatch')
        native.require(mapping['contract_sha256'] == native.sha(folder / 'contract.json'), 'Stale compiled card')
        native.require(len(mapping['elements']) == card['nodes'], 'Node count mismatch')
        roots = [element for element in mapping['elements'] if element['parent'] is None]
        native.require(len(roots) == 1 and roots[0]['source_id'] == card['root'], 'Export includes unrelated scene roots')
        hashes = native.manifest(folder)
        inputs = output / 'inputs' / card['id']
        shutil.copytree(folder, inputs)
        native.require(native.manifest(inputs) == hashes == native.manifest(folder), 'Source changed during staging')
        # Extracted packages keep their own compiled assets. Publish those exact bytes
        # to the local artwork server before asking Studio to load their native SVGs.
        gallery = ROOT / 'docs/reviews/theme-phone-evidence/ux-images' / card['id'] / 'assets'
        if (inputs / 'assets').exists():
            gallery.mkdir(parents=True, exist_ok=True)
            shutil.copytree(inputs / 'assets', gallery, dirs_exist_ok=True)
            native.require(native.manifest(gallery) == native.manifest(inputs / 'assets'), 'Published artwork differs from the standalone package')
        cards.append((card, folder, inputs, hashes))

native.require(bool(cards) and (selected is None or {card['id'] for card,_,_,_ in cards} == selected), 'Unknown card selection')

class FlowVerifier(native.Verifier):
    def settled(self, card, work):
        result = super().settled(card, work)
        # Layout output can arrive before Studio applies its asynchronous viewport
        # resize. Confirm the actual Window, rather than accepting stale dimensions.
        deadline = time.monotonic() + self.timeout
        while time.monotonic() < deadline:
            snapshot = self.ask('WidgetSnapshot')
            windows = [widget for widget in snapshot['widgets'] if widget['widget_type'] == 'Window']
            if len(windows) == 1 and native.delta([0,0,windows[0]['width'],windows[0]['height']], [0,0,*card['artboard']]) <= native.TOLERANCE:
                return result
            self.ask('RunViewResize', {'build_id': self.build, 'window_id':0, 'width':card['artboard'][0], 'height':card['artboard'][1], 'dpi':2.0}, False)
            time.sleep(.1)
        raise RuntimeError('Native Window resize did not settle')

with (ROOT / 'lab/image-to-appcard/.service-capture.lock').open('a') as lock:
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    verifier = FlowVerifier(output, args.build_id, studio, parse_dump, 45)
    try:
        builds = studio.request('ListBuilds', [], 'Builds')['builds']
        native.require(any(item['build_id'] == args.build_id and item.get('package') == studio.RUN_ITEM and item.get('mount') == studio.MOUNT for item in builds), 'Build is not the isolated Studio RunItem')
        native.write(output / 'builds.json', builds)
        native.write(output / 'runtime-hashes.json', native.runtime_manifest())
        for card, source, inputs, hashes in cards:
            work = output / '_runtime' / card['id']
            try:
                result = verifier.capture(card, inputs, work)
            except Exception as error:
                result = {'id': card['id'], 'passed': False, 'error': str(error)}
            destination = output / 'cards' / card['id']
            if work.exists(): shutil.copytree(work, destination)
            native.write(destination / 'result.json', result)
            native.write(destination / 'provenance.json', {'source': str(source.relative_to(ROOT)), 'sources': hashes, 'files': native.manifest(destination), 'build_id': args.build_id})
            native.require(native.manifest(source) == hashes, 'Export changed during capture')
            report['cards'].append(result)
            print(json.dumps({'id': card['id'], 'passed': result['passed']}), flush=True)
        report['passed'] = bool(report['cards']) and all(card['passed'] for card in report['cards'])
    finally:
        # Redirect all future host polling to an explicitly mutable parking request.
        if cards:
            card, _, inputs, _ = cards[0]
            try:
                verifier.mount(card, inputs, output / '_runtime/parking')
                verifier.settled(card, output / '_runtime/parking')
            except Exception as error:
                report['passed'] = False
                report['parking_error'] = str(error)
        report['completed_at'] = datetime.now(timezone.utc).isoformat()
        native.write(output / 'report.json', report)
        native.write(output / 'seal.json', {'files': {name: digest for name,digest in native.manifest(output).items() if not name.startswith('_runtime/')}, 'mutable': '_runtime'})
        native.write(ROOT / 'apps/shared/evidence/standalone-latest.json', {'directory': str(output.relative_to(ROOT)), 'passed': report['passed'], 'report_sha256': native.sha(output / 'report.json')})
print(json.dumps({'passed': report['passed'], 'report': str(output / 'report.json')}))
sys.exit(0 if report['passed'] else 1)
