"""Read-only live Gmail checks; emits counts only and keeps content private."""
from datetime import datetime,timezone
import json
import common
from account import load_account
from mailbox import PRIVATE,atomic_json
import attachments
import gmail_sync
import sending


def main():
    account=load_account()
    if account['host']!='pop.gmail.com':raise SystemExit('This verifier requires the configured Gmail account.')
    services={'checked_at':datetime.now(timezone.utc).isoformat(),'server_mutations':0,'external_messages_sent':0}
    content={'server_mutations':0,'viewer_opened':False}
    try:
        services['smtp_auth_noop']=sending.smtp_test(account)
        box=json.loads((PRIVATE/'mailbox.json').read_text())
        gmail_sync.headers(account,box['messages'])
        rows,folders=gmail_sync.pull(account,box['messages'])
        services.update(imap_login=True,cached_messages=len(rows),identified=sum(bool(m.get('message_id')) for m in rows),
                        remote_state_count=sum(bool(m.get('server_state')) for m in rows),folder_count=len(folders))
        atomic_json(PRIVATE/'completion-readonly.json',{'mailbox':box,'folders':folders})
        folder=next(f for f in folders if f['special']=='\\Sent')
        page=gmail_sync.fetch_folder(account,folder,limit=1)
        content.update(sent_folder_downloaded=len(page['messages']),sent_folder_more=page['more'])
        message=next((m for m in rows if m.get('attachments')),None)
        if message:
            decoded=gmail_sync.hydrate(account,message)
            content['real_attachments_decoded']=len(decoded['attachment_items'])
            if decoded['attachment_items']:
                path=attachments.materialize(account,decoded,0)
                content.update(real_attachment_extracted=path.exists(),attachment_bytes=path.stat().st_size)
            atomic_json(PRIVATE/'completion-attachment.json',decoded)
    except Exception as error:
        services['failure_type']=type(error).__name__
    atomic_json(common.ROOT/'evidence/mail-services-readonly.json',services)
    atomic_json(common.ROOT/'evidence/mail-content-readonly.json',content)
    print(json.dumps({'services':services,'content':content}))
    if services.get('failure_type'):raise SystemExit(1)

if __name__=='__main__':main()
