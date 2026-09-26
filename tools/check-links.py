#!/usr/bin/env python3
"""Check that relative links in tracked Markdown files point at existing files.

Recorded evidence (rounds/, evidence/) is skipped. External URLs and anchors
are not fetched. Targets listed in .github/link-check-pending.txt (one per
line, `#` comments) are reported but do not fail: they are files another
branch adds.
"""
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'!?\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
FENCE = re.compile(r'```.*?```', re.S)
SKIP = ('/rounds/', '/evidence/')


def pending():
    path = ROOT / '.github/link-check-pending.txt'
    if not path.exists():
        return set()
    lines = (line.split('#', 1)[0].strip() for line in path.read_text().splitlines())
    return {line for line in lines if line}


def main():
    allowed = pending()
    files = subprocess.check_output(['git', '-C', str(ROOT), 'ls-files', '*.md'], text=True).splitlines()
    broken, waiting = [], []
    for name in files:
        if any(part in '/' + name for part in SKIP):
            continue
        path = ROOT / name
        text = FENCE.sub('', path.read_text(errors='replace'))
        for number, line in enumerate(text.splitlines(), 1):
            for match in LINK.finditer(line):
                target = match.group(1)
                if re.match(r'^[a-z][a-z0-9+.-]*:', target) or target.startswith(('#', '<')):
                    continue
                target = unquote(target.split('#', 1)[0])
                if not target or (path.parent / target).exists():
                    continue
                resolved = (path.parent / target).resolve()
                try:
                    relative = str(resolved.relative_to(ROOT))
                except ValueError:
                    relative = str(resolved)
                entry = f'{name}:{number}: {match.group(1)}'
                (waiting if relative in allowed or name in allowed else broken).append(entry)
    for entry in waiting:
        print('pending ', entry)
    for entry in broken:
        print('BROKEN  ', entry)
    print(f'{len(broken)} broken, {len(waiting)} pending', file=sys.stderr)
    return 1 if broken else 0


if __name__ == '__main__':
    sys.exit(main())
