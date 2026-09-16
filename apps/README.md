# Standalone apps

Runnable apps built with the image-to-appcard pipeline live in `apps/<name>/`.
Each app owns its service code, reviewed card scenes, design source, launcher,
tests and fixture evidence. App runtime state and personal data stay ignored.

| App | Platform | Description |
| --- | --- | --- |
| [Mail](mail/README.md) | macOS, iOS-style UI | Gmail POP3 inbox, SMTP sending, IMAP folders/flags, native HTML reader and attachments. |

`app/` remains the shared Android client. `a2app/apps/` and `a2app-l0/apps/`
contain agent specifications. Shared authoring and conversion tools remain in
`lab/`; app implementations belong here.
