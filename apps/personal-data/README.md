# personal-data — an octos skill over the Mail and Calendar apps

Phase 1 of the octos ADR *Personal memory — three tiers by trust, one index*
(`docs/adr/personal-memory-tiers.md` in octos-org/octos): make the apps' data
searchable by the agent **without touching the kernel**. A plugin skill reads
the Mail module's private `mailbox-*.json` and the Calendar sync server's
`/v1/state`, keeps a small SQLite FTS5 index next to its binary, and answers
five tools over the octos skill protocol (`./main <tool>` with JSON on stdin,
`{success, output}` on stdout).

| Tool | What it answers |
| --- | --- |
| `mail_search` | matching or latest messages (folder, sender, date, unread/flagged filters) with ids |
| `mail_read` | one message's headers and body text, read live from the Mail app |
| `calendar_query` | events by words, date range (`from`/`to`/`days`) and calendar; next 14 days by default |
| `contacts_lookup` | a person across mail senders, calendar events and shared calendars |
| `personal_data_status` | which sources are indexed, row counts, refresh times |

Every result starts with a banner marking the content as untrusted personal
data. Nothing is written back and nothing leaves the device.

## Index

- `<skill dir>/state/index.sqlite`: mail headers + preview (bodies only when
  `mail.index_bodies` is on), events with wall-clock day columns, calendars.
  150 messages + 6 events → ~270 KB; each call answers in under 10 ms.
- Refresh is lazy: on every call the skill compares each mailbox file's
  mtime+size and the calendar server's `seq` with what the index recorded and
  re-ingests only what changed. If the calendar server is down the cached
  index is used and the answer says so.
- English FTS5 (`unicode61`) with prefix matching; queries containing CJK
  fall back to substring search over the bilingual title/location fields.
- Date filters compare the event's own wall-clock day (its `+08:00` etc.), so
  "what's on the 24th" means the calendar's 24th, not the Mac's time zone.

## Build, test, install

```sh
cd apps/personal-data
cargo test --release              # 5 unit + 9 protocol tests over fixtures
bash scripts/install.sh --profile dev \
  --mail-dir "$TMPDIR/octosense-native-mail/mail" \
  --calendar http://127.0.0.1:8190 \
  --calendar-token-file ../calendar/runtime/calendar.token
```

`install.sh` builds the release binary, stages `main`, `manifest.json`,
`SKILL.md`, `config.json` and the token copy into a temporary directory and runs
`octos skills --profile <id> install <dir> --force`, which places it under
`~/.octos/profiles/<id>/data/skills/personal-data/`. A running `octos serve`
picks up the new skill through the `profile/skills/install` RPC or on restart.

Manual protocol check without octos:

```sh
PERSONAL_DATA_CONFIG=~/.octos/profiles/dev/data/skills/personal-data/config.json \
  sh -c 'echo "{\"query\":\"dentist\"}" | ~/.octos/profiles/dev/data/skills/personal-data/main calendar_query'
```

## Configuration (`config.json` next to the binary)

```json
{
  "locale": "en",
  "mail": {"dirs": ["/var/folders/…/T/octosense-native-mail/mail"], "index_bodies": false},
  "calendar": {"server": "http://127.0.0.1:8190", "token_file": "calendar.token", "timeout_secs": 2}
}
```

`calendar.state_file` (a saved `/v1/state` document) replaces `server` for
offline use and tests. The kernel runs skill binaries with a filtered
environment and the session workspace as the working directory, which is why
configuration and state live beside the binary rather than in env vars or cwd.

## Privacy

- `account.json` (credentials) is never read.
- Bodies are not indexed unless opted in; `mail_read` reads them on demand.
- The index file is created with the user's umask inside the profile's data
  dir; delete `state/` to purge it.

## Next phases

Phase 2 moves the index into the kernel (`Document` records beside episodes,
`memory/ingest`, `memory_search`/`memory_load`, persisted HNSW with int8
MRL-256 vectors), phase 3 indexes the memory bank and promotes distilled facts
with provenance, phase 4 syncs derived records across devices. See the ADR.
