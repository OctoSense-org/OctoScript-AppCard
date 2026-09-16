"""Gracefully close only this app's owned standalone native process/controller."""
import json
import os
import signal
import subprocess
import time
from common import ROOT
from instrument import Instrument


def stop(clear_build=True):
    process_file=ROOT/'runtime/app-process.json'
    if process_file.exists():
        pid=json.loads(process_file.read_text())['pid']
        command=subprocess.run(['ps','-p',str(pid),'-o','command='],capture_output=True,text=True).stdout
        if str(ROOT/'scripts/run.py') in command:
            try:os.kill(pid,signal.SIGTERM)
            except ProcessLookupError:pass
            deadline=time.monotonic()+6
            while time.monotonic()<deadline:
                try:os.kill(pid,0)
                except ProcessLookupError:break
                time.sleep(.1)
    remote=ROOT/'runtime/session/remote.json'
    if clear_build and remote.exists():
        meta=json.loads(remote.read_text())
        command=subprocess.run(['ps','-p',str(meta['pid']),'-o','command='],capture_output=True,text=True).stdout
        if 'beauty-host' in command:
            try:Instrument(meta['endpoint']).get('/quit')
            except Exception:os.kill(meta['pid'],signal.SIGTERM)


if __name__=='__main__':stop()
