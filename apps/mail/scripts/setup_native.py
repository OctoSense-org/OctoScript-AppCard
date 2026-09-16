"""Prepare pinned, patched native dependencies without changing shared submodules."""
from pathlib import Path
import hashlib
import json
import subprocess
from common import ROOT, PIPELINE, NATIVE_ROOT


def git(directory,*args,check=True):
    return subprocess.run(['git','-C',str(directory),*args],check=check,capture_output=True,text=True)


def main():
    source=ROOT/'native-support';manifest=json.loads((source/'manifest.json').read_text())
    if NATIVE_ROOT in (PIPELINE,ROOT):raise SystemExit('Choose a separate OCTOS_MAIL_NATIVE_ROOT; shared checkouts are not modified.')
    NATIVE_ROOT.mkdir(parents=True,exist_ok=True)
    for name,spec in manifest['repositories'].items():
        directory=NATIVE_ROOT/name
        if not (directory/'.git').exists():
            if directory.exists() and any(directory.iterdir()):raise SystemExit(f'{directory} is not an empty native checkout.')
            directory.mkdir(exist_ok=True)
            git(directory,'init','--quiet');git(directory,'remote','add','origin',spec['url'])
            local=PIPELINE/name
            available=local.exists() and git(local,'cat-file','-e',spec['revision']+'^{commit}',check=False).returncode==0
            fetch_source=str(local) if available else 'origin'
            git(directory,'fetch','--quiet','--no-tags','--depth','1',fetch_source,spec['revision'])
            git(directory,'checkout','--quiet','--detach','FETCH_HEAD')
        if git(directory,'rev-parse','HEAD').stdout.strip()!=spec['revision']:
            raise SystemExit(f'{directory} has another revision; keep it or select a new OCTOS_MAIL_NATIVE_ROOT.')
        if spec.get('patch'):
            patch=source/spec['patch']
            if hashlib.sha256(patch.read_bytes()).hexdigest()!=spec['patch_sha256']:raise SystemExit('Native patch integrity check failed.')
            applied=git(directory,'apply','--reverse','--check',str(patch),check=False).returncode==0
            if not applied:
                git(directory,'apply','--check',str(patch));git(directory,'apply',str(patch))
            for filename,digest in spec['files_after'].items():
                if hashlib.sha256((directory/filename).read_bytes()).hexdigest()!=digest:
                    raise SystemExit(f'{name}/{filename} differs from the supported source. Local edits were preserved.')
        print(f'{name}: {spec["revision"][:12]} ready',flush=True)
    receipt={'manifest_sha256':hashlib.sha256((source/'manifest.json').read_bytes()).hexdigest()}
    (NATIVE_ROOT/'ready.json').write_text(json.dumps(receipt,indent=2)+'\n')

if __name__=='__main__':main()
