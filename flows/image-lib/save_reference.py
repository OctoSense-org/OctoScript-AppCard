#!/usr/bin/env python3
"""Preserve an original PNG and declared, provider-neutral generation metadata."""
import argparse,hashlib,json,re,shutil
from pathlib import Path
from PIL import Image
from catalogue import HERE

def save(id,source,*,provider,model=None):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',id):raise ValueError('invalid design ID')
    if not provider.strip():raise ValueError('declare the actual image provider')
    dest=HERE/id;source=Path(source).resolve();target=dest/'reference.png'
    if target.exists():raise FileExistsError(f'{target}: retain the previous reference; use a new design ID')
    prompt=(dest/'image-prompt.md').read_bytes()
    with Image.open(source) as im:
        if im.format!='PNG':raise ValueError('provide the original PNG; do not rename another format')
        dimensions=list(im.size);im.verify()
    shutil.copy2(source,target)
    data={'provider':provider.strip(),'model':model or 'not recorded','prompt':'image-prompt.md',
          'image':'reference.png','image_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
          'prompt_sha256':hashlib.sha256(prompt).hexdigest(),
          'dimensions':dimensions,'requested_logical_artboard':[406,776],'original_filename':source.name}
    (dest/'generation.json').write_text(json.dumps(data,indent=2)+'\n');print(id)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('id');p.add_argument('source')
    p.add_argument('--provider',required=True,help='actual image generator or source; metadata only')
    p.add_argument('--model',help='actual model identifier when known; never inferred')
    a=p.parse_args();save(a.id,a.source,provider=a.provider,model=a.model)
