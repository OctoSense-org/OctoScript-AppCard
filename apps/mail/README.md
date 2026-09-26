# Mail

Mail is an OctoSense system app (`os.mail`, OctoSense ADR 0004): a contained
script app that reads and sends mail without ever holding a socket or a
password.

| Path | What it is |
| --- | --- |
| [`script/`](script/) | The app: `manifest.json` (`storage`, `mail`) and `main.splash`: accounts, folders, inbox, reader (formatted HTML) and composer. |
| [`host-service/`](host-service/) | `octosense-mail-service`, the `mail` host service the app calls through `host.request`. It signs in on the host's own sheet, reads over IMAP (folders, read flags) or POP3, sends over SMTP, keeps passwords in the keychain or behind an Android Keystore key, and rebuilds a message's HTML from the tags the app's `Html` view draws. |

Test the service from a shell workspace that links it (the OctoSense ROM's
`home/`): `cargo test -p octosense-mail-service`. The shells run the app with
`MAKEPAD_APP_CONFIG='{"mail_demo":true}'` for a demo mailbox (password `demo`).

The earlier native Mail module (`native/`), its AppCard scenes, design source
and evidence were removed when Mail became a script app; they remain in Git
history.
