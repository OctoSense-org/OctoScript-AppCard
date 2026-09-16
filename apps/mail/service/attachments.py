"""Extract user-selected MIME files into private storage, then open a viewer."""
from pathlib import Path
import base64
import hashlib
import os
import re
import subprocess
import unicodedata
from account import account_id
from mailbox import PRIVATE

MAX_ATTACHMENT=40_000_000
SAFE_OPEN={'.pdf','.png','.jpg','.jpeg','.gif','.webp','.heic','.tif','.tiff','.bmp',
           '.txt','.csv','.md','.rtf','.doc','.docx','.xls','.xlsx','.ppt','.pptx',
           '.mp3','.wav','.m4a','.mp4','.mov','.ics','.vcf'}


def filename(value):
    name=unicodedata.normalize('NFC',value or 'attachment').replace('\\','/').split('/')[-1]
    name=re.sub(r'[\x00-\x1f\x7f:/]', '_',name).strip(' .')
    return name[:180] or 'attachment'


def materialize(account,message,index):
    item=message.get('attachment_items',[])[index]
    payload=base64.b64decode(item['data'],validate=True)
    if len(payload)>MAX_ATTACHMENT or len(payload)!=item['size']:raise ValueError('Attachment size is invalid.')
    digest=hashlib.sha256(payload).hexdigest()
    if digest!=item['sha256']:raise ValueError('Attachment failed its integrity check.')
    directory=PRIVATE/'attachments'/account_id(account)/hashlib.sha256(message['id'].encode()).hexdigest()/digest
    directory.mkdir(parents=True,exist_ok=True,mode=0o700)
    path=directory/filename(item['filename'])
    fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_TRUNC,0o600)
    os.fchmod(fd,0o600)
    with os.fdopen(fd,'wb') as stream:stream.write(payload)
    return path


def open_attachment(path):
    path=Path(path).resolve()
    if path.suffix.lower() in SAFE_OPEN:
        # Quick Look previews documents without executing a downloaded program.
        with open(os.devnull,'wb') as output:
            subprocess.Popen(['/usr/bin/qlmanage','-p',str(path)],stdout=output,stderr=output,start_new_session=True)
        return 'Opened in Quick Look'
    subprocess.run(['/usr/bin/open','-R',str(path)],check=True,capture_output=True)
    return 'Saved attachment and revealed it in Finder'
