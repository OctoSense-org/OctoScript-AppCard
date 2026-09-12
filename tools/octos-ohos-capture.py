"""Capture a completed native generation through an existing Studio bridge.

Raw device logs stay local. Only allowlisted timing/counter fields are exported.
This does not launch, build or provision the app.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import shutil
import urllib.request


def studio(port, kind, build, **fields):
    body = {'request': {kind: {'build_id': [build], **fields}},
            'response': kind, 'timeout': 20}
    request = urllib.request.Request(f'http://127.0.0.1:{port}',
                                    data=json.dumps(body).encode(),
                                    headers={'Content-Type': 'application/json'})
    return json.load(urllib.request.urlopen(request, timeout=25))


def metrics(log):
    rows, usage, seen = [], [], set()
    for line in log.splitlines():
        if 'generation-metric ' in line:
            try:
                raw = json.loads(line.split('generation-metric ', 1)[1])
            except json.JSONDecodeError:
                continue
            row = {k: v for k, v in raw.items() if k in {
                'event', 'turn_id', 'session_id', 'elapsed_ms', 'prompt_bytes',
                'transport', 'tokens_in', 'tokens_out', 'outcome', 'token_usage', 'code'}}
            key = json.dumps(row, sort_keys=True)
            if key not in seen:
                rows.append(row)
                seen.add(key)
        if 'A0AF00' in line and 'LLM response received' in line:
            counts = dict(re.findall(r'\b(input_tokens|output_tokens|cache_read_tokens|cache_write_tokens)=(\d+)', line))
            usage.append({k: int(v) for k, v in counts.items()})
    return rows, usage


def capture(args):
    out = args.output / args.name
    out.mkdir(parents=True, exist_ok=True)
    results = {}
    for kind in ['WidgetTreeDump', 'WidgetSnapshot', 'Screenshot']:
        results[kind] = studio(args.bridge_port, kind, args.build)
    results['WidgetQuery'] = studio(args.bridge_port, 'WidgetQuery', args.build, query='type:KitButton')
    for kind in ['WidgetTreeDump', 'WidgetSnapshot', 'WidgetQuery']:
        (out / (kind + '.json')).write_text(json.dumps(results[kind], ensure_ascii=False, indent=2) + '\n')
    shot = results['Screenshot']
    shutil.copy2(shot['path'], out / 'screen.png')
    widgets = results['WidgetSnapshot']['widgets']
    sources = [w.get('text', '') for w in widgets if w['id'] == 'splash_view']
    source = max(sources, key=len, default='')
    (out / 'native.splash').write_text(source)
    tree = results['WidgetTreeDump'].get('dump', '')
    nodes = tree.splitlines()[1:]
    counts = Counter(w['widget_type'] for w in widgets)
    log_path = args.logs / f'device-{args.build}.log'
    raw_log = log_path.read_text(errors='replace') if log_path.exists() else ''
    rows, usage = metrics(raw_log)
    submitted = {r['turn_id'] for r in rows if r['event'] == 'submitted'}
    finished = {r['turn_id'] for r in rows if r['event'] == 'completed'}
    completed = bool(submitted) and submitted == finished and not any(r['event'] == 'failed' for r in rows)
    loading = any(w['id'] == 'thinking_curtain' and w['visible'] and w['width'] > 0 for w in widgets)
    source_theme = f'\\"recipe_theme\\":\\"{args.theme}\\"' in source
    # Offscreen rows in a scrolling card are expected. Check horizontal bounds
    # only for nodes intersecting the current viewport. Logical-pixel tolerance.
    window = next(w for w in widgets if w['widget_type'] == 'Window')
    differences = []
    splash_index = next((int(n.split()[0]) for n in nodes if ' splash_view Splash ' in n), None)
    descendants = set()
    for node in nodes:
        parts = node.split()
        if len(parts) < 8:
            continue
        index, parent = int(parts[0]), int(parts[1])
        if parent == splash_index or parent in descendants:
            descendants.add(index)
            x, y, width, height = map(float, parts[-4:])
            if y < window['height'] and y + height > 0 and width > 0:
                overflow = max(0, -x, x + width - window['width'])
                if overflow > 2:
                    differences.append({'id': parts[2], 'widget_type': parts[3],
                                        'bounds': [x, y, width, height],
                                        'horizontal_overflow_px': overflow, 'tolerance_px': 2})
    checks = {'completed': completed, 'loading_overlay_hidden': not loading,
              'inner_native_widgets': len(descendants) > 3,
              'expected_kit_in_realized_source': source_theme,
              'no_horizontal_overflow': not differences}
    # The outer bounds can fit while a price wraps into "$ / 315. / 39".
    # Native label metrics have a 24px small-text allowance and up to
    # 2.25 * nominal font size plus 2px rounding. Multiple price lines exceed it.
    fonts = dict(re.findall(r'(\w+) := Label\{[^\n]*?font_size: ([\d.]+)', source))
    numeric_wraps = []
    for w in widgets:
        value = w.get('text', '').strip()
        if w['id'] not in fonts or not w['visible'] or not (0 <= w['y'] < window['height']):
            continue
        if re.fullmatch(r'[-+≈↑↓$€£¥\d.,%°\s]+', value) and any(c.isdigit() for c in value):
            limit = max(24.0, float(fonts[w['id']]) * 2.25 + 2.0)
            if w['height'] > limit:
                numeric_wraps.append({'id': w['id'], 'text': value, 'height': w['height'],
                                      'max_single_line_height': limit})
    checks['numeric_values_stay_on_one_line'] = not numeric_wraps
    report = {'name': args.name, 'build': args.build, 'prompt': args.prompt,
              'theme': args.theme, 'checks': checks, 'structural_pass': all(checks.values()),
              'native_descendants': len(descendants), 'widget_counts': counts,
              'screenshot': {'width': shot['width'], 'height': shot['height']},
              'metrics': rows, 'provider_iterations': usage,
              'repair_rounds': max(0, len(submitted) - 1),
              'generation_total_ms': sum(r.get('elapsed_ms', 0) or 0 for r in rows if r['event'] == 'completed'),
              'differences': differences + numeric_wraps, 'visual_review': 'pending'}
    (out / 'result.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['name', 'checks', 'native_descendants', 'metrics', 'provider_iterations']}))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', type=int, required=True)
    parser.add_argument('--name', required=True)
    parser.add_argument('--theme', required=True)
    parser.add_argument('--prompt', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--bridge-port', type=int, default=8169)
    parser.add_argument('--logs', type=Path, default=Path('/tmp/octos-ohos-generation'))
    raise SystemExit(capture(parser.parse_args()))
