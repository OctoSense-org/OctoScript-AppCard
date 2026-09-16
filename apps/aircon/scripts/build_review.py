#!/usr/bin/env python3
"""Regenerate the local native-review manifest; never fabricates capture evidence."""

from datetime import datetime, timezone
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / 'review'


def read_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return None


def artifact(path, label):
    return {'label': label, 'url': '../' + path.relative_to(ROOT).as_posix(),
            'available': path.is_file()}


def build():
    REVIEW.mkdir(parents=True, exist_ok=True)
    flow = read_json(ROOT / 'source/flow.json') or {}
    states = {int(s['id']): s for s in flow.get('states', [])}
    directories = {int(p.name.removeprefix('aircon-')): p
                   for p in (ROOT / 'cards').glob('aircon-*')
                   if p.is_dir() and re.fullmatch(r'aircon-\d+', p.name)}
    rows = []
    for number in sorted(set(states) | set(directories)):
        state = states.get(number, {})
        directory = directories.get(number, ROOT / 'cards' / f'aircon-{number:02d}')
        latest = read_json(directory / 'latest.json')
        run = read_json(directory / 'pipeline-run.json')
        round_id = str((latest or {}).get('round', ''))
        round_dir = directory / 'rounds' / round_id if re.fullmatch(r'\d{1,8}', round_id) else None
        reference = directory / 'reference.png'
        native = round_dir / 'native.png' if round_dir else None
        row = {
            'number': number, 'id': directory.name,
            'title': state.get('title', f'界面 {number:02d}'),
            'description': state.get('description', ''),
            'surface': state.get('surface', ''), 'branch': bool(state.get('branch')),
            'base': '../' + directory.relative_to(ROOT).as_posix() + '/',
            'reference': '../' + reference.relative_to(ROOT).as_posix() if reference.is_file() else None,
            'native': '../' + native.relative_to(ROOT).as_posix() if native and native.is_file() else None,
            'latest': latest, 'run': run,
            'gate': read_json(round_dir / 'gate.json') if round_dir else None,
            'files': {
                'card': artifact(directory / 'page.card', '.card 源码'),
                'kit': artifact(directory / 'kit/native/light/kit.json', '组件 kit'),
                'components': artifact(directory / 'kit/native/light/components.l0', '原生组件'),
                'actions': artifact(directory / 'service-actions.json', '服务动作'),
                'mapped': artifact(directory / 'mapped.json', '组件树'),
                'run': artifact(directory / 'pipeline-run.json', 'Pipeline'),
                'data': artifact(ROOT / 'service/fixtures' / f'{number:02d}.view.json', '服务状态'),
            },
        }
        if round_dir:
            for key, name, label in [
                ('gate', 'gate.json', '验收 gate'), ('tree', 'tree.json', 'Studio 控件树'),
                ('provenance', 'provenance.json', '截图来源'),
                ('interactions', 'interactions.json', '原生输入证据'),
            ]:
                row['files'][key] = artifact(round_dir / name, label)
        rows.append(row)
    manifest = {
        'schema_version': 1, 'title': '空调到家 · 原生卡片评审',
        'built_at': datetime.now(timezone.utc).isoformat(), 'rows': rows,
        'note': 'Only latest.json selects a native capture. Missing or failed evidence is never replaced with reference imagery.',
    }
    payload = json.dumps(manifest, ensure_ascii=False, indent=2)
    (REVIEW / 'manifest.json').write_text(payload + '\n')
    (REVIEW / 'manifest.js').write_text('window.REVIEW_MANIFEST = ' + payload.replace('<', '\\u003c') + ';\n')
    print(json.dumps({'review': str(REVIEW / 'index.html'), 'frames': len(rows),
                      'native_captures': sum(bool(r['native']) for r in rows)}, ensure_ascii=False))


if __name__ == '__main__':
    build()
