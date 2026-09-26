#!/usr/bin/env python3
"""Inventory lab storage or remove only explicitly recognized rebuildable caches.

`clean` previews by default. Stop import jobs before `clean --exports --apply`.
Source documents, final assets, captures, review rounds and environments are
never cleanup candidates. This is not an evidence-retention or Git-history tool.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess

LAB = Path(__file__).resolve().parent
ENVIRONMENTS = {'.venv', '.deps', 'node_modules', 'target', '.git'}


def files_under(path):
    if path.is_symlink():
        raise ValueError('refusing symlink: ' + str(path))
    if path.is_file():
        yield path
        return
    for base, dirs, files in os.walk(path, followlinks=False):
        for name in dirs + files:
            child = Path(base) / name
            if child.is_symlink():
                raise ValueError('refusing symlink inside cleanup candidate: ' + str(child))
        for name in files:
            yield Path(base) / name


def usage(path):
    count = size = allocated = 0
    for p in files_under(path):
        stat = p.stat()
        count += 1
        size += stat.st_size
        allocated += getattr(stat, 'st_blocks', (stat.st_size + 511) // 512) * 512
    return {'files': count, 'bytes': size, 'allocated_bytes': allocated}


def tracked_files(lab):
    result = subprocess.check_output(
        ['git', '-C', str(lab), 'ls-files', '-z', '--full-name'], text=True)
    root = Path(subprocess.check_output(
        ['git', '-C', str(lab), 'rev-parse', '--show-toplevel'], text=True).strip())
    return {root / name for name in result.split('\0') if name}


def candidates(lab, exports=False):
    selected = []
    for base, dirs, files in os.walk(lab, followlinks=False):
        dirs[:] = [name for name in dirs if name not in ENVIRONMENTS
                   and not (Path(base) / name).is_symlink()]
        if '__pycache__' in dirs:
            selected.append((Path(base) / '__pycache__', 'python-bytecode'))
            dirs.remove('__pycache__')
        if '.DS_Store' in files:
            selected.append((Path(base) / '.DS_Store', 'finder-metadata'))
        # These trees are handled separately with their source prerequisites.
        if 'graphic-export-cache' in dirs:
            dirs.remove('graphic-export-cache')
    if exports:
        for cache in sorted((lab / 'core/work').glob('*/native*/graphic-export-cache')):
            if any(parent.is_symlink() for parent in (cache, *cache.parents)
                   if parent == lab or lab in parent.parents):
                raise ValueError('refusing linked export cache: ' + str(cache))
            if not all((cache.parent / name).is_file() for name in
                       ('source.sketch', 'resolved.sketch', 'source-cache.json')):
                raise ValueError('export cache lacks its retained source documents: ' + str(cache))
            selected.append((cache, 'sketch-export-cache'))
    return sorted(selected)


def clean(lab, *, exports=False, apply=False):
    tracked = tracked_files(lab)
    rows = []
    # Validate every candidate before removing the first one.
    for path, kind in candidates(lab, exports):
        if any(p == path or path in p.parents for p in tracked):
            raise ValueError('refusing tracked cleanup candidate: ' + str(path))
        rows.append({'path': path.relative_to(lab).as_posix(), 'kind': kind, **usage(path)})
    result = {'mode': 'apply' if apply else 'preview', 'candidates': rows,
              'files': sum(row['files'] for row in rows),
              'bytes': sum(row['bytes'] for row in rows),
              'allocated_bytes': sum(row['allocated_bytes'] for row in rows)}
    if apply:
        for row in rows:
            path = lab / row['path']
            if path.is_symlink():
                raise ValueError('cleanup candidate became a symlink: ' + str(path))
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
    return result


def inventory(lab):
    rows = []
    for path in sorted(lab.iterdir()):
        if not path.is_dir() or path.is_symlink():
            continue
        # Inventory follows neither environment executables nor other symlinks.
        count = size = allocated = 0
        for base, dirs, files in os.walk(path, followlinks=False):
            dirs[:] = [n for n in dirs if not (Path(base) / n).is_symlink()]
            for name in files:
                p = Path(base) / name
                if p.is_symlink():
                    continue
                stat = p.stat()
                count += 1
                size += stat.st_size
                allocated += getattr(stat, 'st_blocks', (stat.st_size + 511) // 512) * 512
        rows.append({'path': path.name, 'files': count, 'bytes': size, 'allocated_bytes': allocated})
    return {'directories': rows, 'bytes': sum(r['bytes'] for r in rows),
            'allocated_bytes': sum(r['allocated_bytes'] for r in rows)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('inventory', 'clean'))
    parser.add_argument('--exports', action='store_true', help='include rebuildable Sketch export caches')
    parser.add_argument('--apply', action='store_true', help='remove recognized caches after validation')
    parser.add_argument('--report', type=Path, help='save the detailed JSON locally')
    args = parser.parse_args()
    if args.action == 'inventory' and (args.exports or args.apply):
        parser.error('--exports and --apply apply only to clean')
    result = inventory(LAB) if args.action == 'inventory' else clean(LAB, exports=args.exports, apply=args.apply)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2) + '\n')
        print(json.dumps({k: v for k, v in result.items() if k not in ('candidates', 'directories')}))
    else:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
