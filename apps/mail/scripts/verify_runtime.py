"""Exercise HTML, long readers, subject search and list virtualization on native Metal.

Only fictional mail is used. The owned hidden app exposes Makepad's built-in
HTTP instrument; WKWebView probes travel through /event, without Studio.
"""
from contextlib import ExitStack
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import tempfile
import time
from unittest.mock import patch

import run as app_run
from run import MailSession, launch_native
from common import ROOT, NATIVE_ROOT
from account import defaults, save_account
import mailbox
import sending
import attachments
from instrument import settled, read
from core.native_runtime import verify


def main():
    out = ROOT / 'evidence' / ('runtime-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
    out.mkdir(parents=True)
    process = instrument = None
    checks = []
    try:
        with tempfile.TemporaryDirectory() as temp, ExitStack() as stack:
            private = Path(temp) / 'mail'
            private.mkdir()
            stack.enter_context(patch.dict(os.environ, {'OCTOS_MAIL_CREDENTIALS': str(Path(temp) / 'account.json')}))
            for module in (app_run, mailbox, sending, attachments):
                stack.enter_context(patch.object(module, 'PRIVATE', private))
            save_account({**defaults('fixture@example.com'), 'password': 'fixture', 'sync_enabled': False})
            app = MailSession(live=False)
            base = app.state['mailbox']['messages'][0]
            rows = [{**deepcopy(base), 'id': f'fixture-{i}', 'subject': f'Runtime topic {i:03}', 'unread': False}
                    for i in range(150)]
            rows[0]['subject'] = 'HTML runtime fixture'
            rows[0]['html'] = ('<h1>HTML runtime fixture</h1><strong>Bold fixture</strong>'
                '<table><tr><td>Table fixture</td></tr></table>'
                '<script>window.emailScriptExecuted=true</script>'
                + ''.join(f'<p>HTML paragraph {i:03}: native WebView content.</p>' for i in range(180))
                + '<p>END OF HTML FIXTURE</p>')
            rows[-1].update(subject='Plain scroll fixture', html='',
                            body='\n\n'.join(f'Paragraph {i:03}: continuous native reader content.' for i in range(100)))
            app.state['mailbox'].update(messages=rows, available=150, has_more=False)
            process, instrument = launch_native(app, hidden=True)

            def pump(seconds=.8):
                end = time.monotonic() + seconds
                while time.monotonic() < end:
                    app.poll()
                    time.sleep(.05)
                return settled(poll=app.poll)

            def node(ident):
                meta = settled(poll=app.poll)
                return next(n for n in read(meta['mapping'])['elements'] if n['source_id'] == ident)

            def rectangle(ident):
                native = node(ident)['native_id']
                return next(w['r'] for w in instrument.get('/snap', q=native, all=1)['s'] if w['i'] == native)

            def click(ident):
                x, y, w, h = rectangle(ident)
                assert w > 0 and h > 0 and 0 <= y < 776, (ident, (x,y,w,h))
                instrument.get('/click', x=round(x+w/2), y=round(y+h/2), wait=1)
                pump()

            def probe(kind, name, **fields):
                result = out / (name + '.json')
                data = dict(kind=kind, result=str(result), **fields)
                instrument.get('/event', data=json.dumps(data))
                deadline = time.monotonic() + 15
                while not result.exists():
                    app.poll()
                    if time.monotonic() > deadline:
                        raise AssertionError('Native probe timed out: ' + name)
                    time.sleep(.05)
                return read(result)

            pump()
            (out / 'protocol.txt').write_text(instrument.get('/'))
            click('message_0_open_control')
            html_id = node('message_html')['native_id']
            pump(1)
            before = probe('webview_inspect', 'html-top', id=html_id, snapshot=str(out/'html.png'))
            assert before['tables'] == 1 and before['bold'] >= 1, before
            assert 'END OF HTML FIXTURE' in before['text'] and not before['emailScriptExecuted'], before
            assert before['scrollHeight'] > before['viewportHeight'] * 5, before
            after = probe('webview_inspect', 'html-bottom', id=html_id, scroll_y=100000)
            assert after['scrollY'] > 1000 and after['scrollY'] + after['viewportHeight'] >= after['scrollHeight'] - 3, after
            checks.append('Native WKWebView renders formatted full HTML, blocks mail scripts and scrolls to the end')
            click('back_control')
            assert probe('webview_lifecycle', 'webview-closed')['native_browsers'] == 0
            checks.append('Leaving the reader disposes its native WebView')
            instrument.get('/m', k='scroll', x=200, y=500, dy=9000, wait=1)
            pump(2)
            assert app.state['list_start'] > 40 and app.state['list_scroll'] > 5000, app.state['list_start']
            assert sum(n['source_id'].startswith('message_') and n['source_id'].endswith('_open_control')
                       for n in read(settled(poll=app.poll)['mapping'])['elements']) <= 60
            checks.append('A 150-message inbox scrolls beyond the initial window while mounting at most 60 rows')
            click('search_field_input')
            instrument.get('/t', t='Plain scroll fixture', wait=1)
            pump(1)
            assert app.state['query'] == 'Plain scroll fixture'
            click('message_0_open_control')
            assert app.state['selected'] == 'fixture-149'
            checks.append('The fixed subject search finds and opens a message beyond the initial list window')
            instrument.get('/m', k='scroll', x=200, y=500, dy=100000, wait=1)
            pump(1)
            # Container areas are clipped to the viewport; inspect the final text row.
            bottom = instrument.get('/snap', q='Paragraph 099')['s']
            assert any(88 <= w['r'][1] < 704 and w['r'][3] > 0 for w in bottom), bottom
            mailbox.atomic_json(out / 'plain-reader-bottom-snapshot.json', bottom)
            instrument.grab(out / 'plain-reader-bottom.png')
            checks.append('The full plain-text reader scrolls vertically without pagination')
            report = {'passed': True, 'checks': checks, 'runtime': verify(NATIVE_ROOT),
                      'native_pid': process.pid, 'hidden': True, 'instrument': 'Makepad HTTP /event; no Studio'}
            mailbox.atomic_json(out / 'report.json', report)
            mailbox.atomic_json(ROOT/'evidence/latest-runtime.json', {'directory': str(out.relative_to(ROOT)), **report})
    finally:
        if instrument:
            try:
                instrument.grab(out / 'exit.png', quit=True)
            except Exception:
                instrument.get('/quit')
        if process:
            process.wait(timeout=10)
    print(json.dumps({'passed': True, 'checks': checks, 'evidence': str(out)}, indent=2))


if __name__ == '__main__':
    main()
