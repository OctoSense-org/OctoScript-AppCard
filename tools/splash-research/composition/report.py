#!/usr/bin/env python3
"""Export measurements and losslessly compressed native screenshots for review."""
import argparse
import json
from pathlib import Path
import shutil
import statistics
import struct
import zlib


def public(value):
    if isinstance(value, dict):
        return {k: public(v) for k, v in value.items() if k not in ['excerpt', 'previous_view']}
    if isinstance(value, list):
        return [public(v) for v in value]
    return value


def compress_png(source, target):
    """Recompress PNG IDAT only. Pixel/filter bytes and all other chunks stay exact."""
    raw = source.read_bytes()
    assert raw[:8] == b'\x89PNG\r\n\x1a\n'
    chunks = []; offset = 8
    while offset < len(raw):
        length = struct.unpack('>I', raw[offset:offset+4])[0]
        chunks.append((raw[offset+4:offset+8], raw[offset+8:offset+8+length]))
        offset += length + 12
    decoded = zlib.decompress(b''.join(data for kind, data in chunks if kind == b'IDAT'))
    encoded = zlib.compress(decoded, 9)
    assert zlib.decompress(encoded) == decoded
    output = bytearray(raw[:8]); written = False
    for kind, data in chunks:
        if kind == b'IDAT':
            if written:
                continue
            data = encoded; written = True
        output.extend(struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind+data)))
    target.write_bytes(output)


def metrics(r):
    fetches = [t for t in r['workflow']['trace'] if t['tool'] == 'composition.fetch']
    ui = r.get('initial_ui') or r['ui']
    return {'prepare_s': r['generation_and_research_s'], 'plan_s': r['plan_call']['elapsed_s'],
        'layout_s': sum(a['timing']['elapsed_s'] for a in r['ui_generation']),
        'template_ms': r['template_instantiation_s'] * 1000,
        'research_s': max(t['end_s'] for t in fetches) - min(t['start_s'] for t in fetches),
        'synthesis_s': sum(c['elapsed_s'] for c in r['workflow']['model_calls']),
        'display_s': ui['launch_to_visible_s'], 'source_status': r['dataset_status'],
        'repairs': max(0, len(r['ui_generation'])-1), 'fallback': r['ui_fallback'],
        'plan_tab': r['ui']['plan_tab'], 'evidence_tab': r['ui']['evidence_tab'],
        'ui_error': r['ui']['error']}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--input', type=Path, required=True); ap.add_argument('--out', type=Path, required=True); args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    findings = json.loads((Path(__file__).parent / 'findings.json').read_text())
    shutil.copyfile(Path(__file__).parent / 'findings.json', args.out / 'findings.json')
    rows = []
    for i in range(1, 21):
        cid = f'{i:02}'
        row = {'id': cid, 'content_review': findings['template_needs_content_review'].get(cid),
            'baseline_finding': findings['baseline_findings'].get(cid)}
        for mode, parent in [('generated', args.input), ('template', args.input / 'template-run')]:
            source = parent / cid; target = args.out / 'cases' / cid / mode; target.mkdir(parents=True, exist_ok=True)
            r = json.loads((source / 'result.json').read_text())
            row.update(intent=r['case']['intent'], family=r['plan']['family'])
            row[mode] = metrics(r)
            row[mode]['title'] = r['plan']['title']
            row[mode]['card_kib'] = (source / 'app.card').stat().st_size / 1024
            (target / 'result.json').write_text(json.dumps(public(r), ensure_ascii=False, indent=2))
            for name in ['app.card', 'dataset.json', 'data.json']:
                shutil.copyfile(source / name, target / name)
            if (source / 'failure.json').exists():
                shutil.copyfile(source / 'failure.json', target / 'prior-failure.json')
            for name in ['screen.png', 'evidence.png']:
                compress_png(source / name, target / name)
        rows.append(row)
    summary = {}
    for mode in ['generated', 'template']:
        summary[mode] = {key: {'median': statistics.median(r[mode][key] for r in rows),
            'p95': sorted(r[mode][key] for r in rows)[18], 'min': min(r[mode][key] for r in rows), 'max': max(r[mode][key] for r in rows)}
            for key in ['prepare_s', 'plan_s', 'layout_s', 'research_s', 'synthesis_s', 'display_s', 'template_ms', 'card_kib']}
    payload = {'summary': summary, 'cases': rows}
    (args.out / 'results.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    html = (Path(__file__).parent / 'gallery.html').read_text()
    (args.out / 'gallery.html').write_text(html.replace('__RESULTS_JSON__', json.dumps(payload, ensure_ascii=False).replace('<', '\\u003c')))
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main()
