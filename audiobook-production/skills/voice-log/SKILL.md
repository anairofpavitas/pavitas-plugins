---
name: voice-log
description: Log a new character voice into the right Notion series voice database, optionally capturing an audio sample straight off Pavi's studio mic. Use when Pavi says "new voice", "add a voice", "log a voice", "add a character voice", "record a sample for", or describes a character he's just built a voice for. Handles series routing, duplicate checks, mic capture via the Scarlett Solo, hosting on Zo, and writing the Notion row.
---

# Voice Log

Adds a character voice to Pavi's Notion voice-tracking system. One row per character, filed under the right book series.

## The system you're writing into

- Parent database: **🎭 Character Voices** — data source `8e45d582-7f69-4275-90ff-f242ebe70cbc`
  - `Series` (title), `🎧 Audiobook Projects` (relation → `28321020-d7f5-4619-aafd-28c3faccf815`)
- Each row's **page body** holds an inline database of that series' voices.
- Inline voice DB schema (identical everywhere):
  - `Name` (title) · `Dialect` (text) · `Features` (text) · `Sample` (file)
- Two views per DB: a table and a "Character Gallery" gallery using `Sample` as the cover.

**There is no Tags property. It was deleted on purpose. Never re-add it.**

See `references/series-index.md` for the series → data source lookup table.

## Flow

### 1. Route to a series

Match what Pavi said against `references/series-index.md`, including the aliases. If it's ambiguous between two series, ask — don't guess.

If the series isn't in the index, search the Character Voices data source for it before concluding it's new:

```
notion-query-data-sources
  data_source_urls: ["collection://8e45d582-7f69-4275-90ff-f242ebe70cbc"]
  query: SELECT url, "Series" FROM "collection://8e45d582-7f69-4275-90ff-f242ebe70cbc"
```

Then `notion-fetch` that series page and read the `data-source-url="collection://…"` off the `<database>` tag in its content.

### 2. Parse the description

Pavi describes voices in free prose. Split it:

- **`Dialect`** — only accent/regional/register information. "Light Boston," "RP," "Texas/Southern," "light Latin," "GenAm." Record it roughly as he says it; light cleanup only.
- **`Features`** — everything else. Age, gender, build, timbre, personality, role in the story, speech quirks (lisps, breathiness, vocal fry), reference points ("Billy from American Dad," "Alex Trebek").

**If he doesn't mention an accent, leave `Dialect` empty.** Do not write "Neutral" as a default and do not invent one. Sometimes he specifies, sometimes he doesn't — that's expected.

**Never edit `Dialect` on rows that already exist.** The historical values are inconsistent and he wants them left alone.

Confirm your parse back to him in one line before writing. Not a form — just: `Kessner — Dialect: light Boston · Features: gravelly bruiser, mid-50s, drops his R's.`

### 3. Duplicate check

Query the target data source for the character name before creating. If a row exists, ask whether to update it or create a second one (sometimes there are two Johnsons — see Obelisk).

### 4. Audio sample (optional but usually wanted)

Ask if he wants to record one. If yes, run the capture below. If he'd rather not, skip straight to step 5 and leave `Sample` empty — he can drag a file in later.

Three ways audio can arrive:
- **Mic capture** (default, described below)
- **He attaches a file to the chat** — read it from the uploads directory, then jump to the upload step
- **He points at a file on his Mac** — copy it to `/tmp/voicelog/` via osascript, then upload

#### 4a. Resolve the mic

All Mac commands run through `mcp__remote-devices__Control_your_Mac__osascript` wrapped in `do shell script "…"`. `ffmpeg` lives at `/opt/homebrew/bin/ffmpeg`.

```
export PATH=/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin
ffmpeg -hide_banner -f avfoundation -list_devices true -i '' 2>&1 \
  | sed -n '/audio devices/,$p' | grep -i 'Scarlett Solo' \
  | sed -E 's/.*\[([0-9]+)\].*/\1/' | head -1
```

Device indices shift between boots — always resolve by name, never hardcode. Scarlett Solo is the studio interface and the right default. Fall back to `MacBook Pro Microphone` only if he asks.

#### 4b. Record

Generate a slug first: `<character>-<series-abbrev>-<8 random hex>`, lowercase, `[a-z0-9-]` only. The random suffix keeps the public URL unguessable — don't skip it.

```
openssl rand -hex 4
```

**Open-ended (preferred).** Tell him you're rolling, then start it. He talks, then tells you he's done, and you stop it on the next turn.

```
mkdir -p /tmp/voicelog
nohup ffmpeg -hide_banner -loglevel error -y -f avfoundation -i ":$IDX" \
  -t 300 -ac 1 -ar 44100 /tmp/voicelog/<slug>.m4a > /tmp/voicelog/rec.log 2>&1 &
```

Stop it cleanly (SIGINT finalizes the container — `kill -9` corrupts it):

```
pkill -INT -f '<slug>.m4a'; sleep 2
ffprobe -v error -show_entries format=duration -of csv=p=0 /tmp/voicelog/<slug>.m4a
```

**Timed.** When he wants it hands-off. Warn him it starts immediately, then:

```
ffmpeg -hide_banner -loglevel error -y -f avfoundation -i ":$IDX" \
  -t 20 -ac 1 -ar 44100 /tmp/voicelog/<slug>.m4a
```

Check the duration afterward. If it's near-zero or the file is tiny, the capture failed — say so and retry rather than uploading silence.

#### 4c. Host it on Zo

Get the upload token (never hardcode it into a message):

```
mcp__Zo_Computer__bash: cat /home/workspace/.zo-app-data/voice-log/token.txt
```

Upload from the Mac — this keeps the binary out of the conversation entirely:

```
curl -sS -X POST \
  -H "x-voice-token: <token>" -H 'Content-Type: audio/mp4' \
  --data-binary @/tmp/voicelog/<slug>.m4a \
  "https://paviproczko.zo.space/api/voice-sample?name=<slug>"
```

Returns `{"ok":true,"filename":"…","bytes":…,"url":"https://paviproczko.zo.space/api/voice-sample/<slug>.m4a"}`.

Files land in `/home/workspace/Audio/VoiceSamples/` on Zo and **must stay there** — the Notion `Sample` property links to that URL rather than hosting a copy. Deleting the Zo file breaks the sample. Max 25 MB.

### 5. Write the Notion row

Create the row first (the `Sample` file property will not accept a file reference at creation time):

```
notion-create-pages
  parent: {type: "data_source_id", data_source_id: "<series voices uuid>"}
  pages: [{properties: {Name: "…", Dialect: "…", Features: "…"}}]
```

Then set the sample:

```
notion-update-page
  page_id: <new row id>
  command: update_properties
  properties: {"Sample": ["https://paviproczko.zo.space/api/voice-sample/<slug>.m4a"]}
```

Then drop a durable, Notion-hosted copy in the row's page body, so the clip survives even if Zo changes:

```
notion-create-attachment
  filename: <slug>.m4a
  source_url: https://paviproczko.zo.space/api/voice-sample/<slug>.m4a
→ returns file-upload://<id>

notion-update-page
  page_id: <new row id>
  command: insert_content
  content: <audio src="file-upload://<id>"></audio>
```

**Known limitation:** the `Sample` file property rejects `file-upload://` references — it only takes external URLs. That's why the property links to Zo and the page body carries the hosted copy. Don't waste turns retrying the upload-ID form.

Clean up `/tmp/voicelog/` on the Mac when you're done.

### 6. Report

One line: character name, series, whether a sample landed, and a link to the row. Don't restate the description back at him.

## Creating a new series

When the series genuinely doesn't exist yet:

1. Find the matching book(s) in Audiobook Projects:
   ```
   SELECT url, "Project name", "Status" FROM "collection://28321020-d7f5-4619-aafd-28c3faccf815"
   WHERE "Project name" LIKE '%<series>%'
   ```
2. Create the parent row. **Name it for the series, not a single book** — "Loop Bound Voices," not "Loop Bound 2 Voices" — and relate it to every book in the series:
   ```
   notion-create-pages
     parent: {type: "data_source_id", data_source_id: "8e45d582-7f69-4275-90ff-f242ebe70cbc"}
     pages: [{properties: {Series: "<X> Voices", "🎧 Audiobook Projects": [<book page urls>]}}]
   ```
3. Create the inline database in that page:
   ```
   notion-create-database
     parent: {type: "page_id", page_id: "<new series page id>"}
     title: "<X> Voices"
     schema: CREATE TABLE ("Name" TITLE, "Sample" FILES, "Features" RICH_TEXT, "Dialect" RICH_TEXT)
   ```
4. Make it inline: `notion-update-data-source` with `is_inline: true`
5. Add the gallery:
   ```
   notion-create-view
     database_id: <new db id>
     data_source_id: <new ds uuid>
     name: "Character Gallery"
     type: gallery
     configure: SHOW "Name", "Dialect", "Features", "Sample"; COVER "Sample"
   ```
6. Tell Pavi to add the new series to `references/series-index.md` — this skill file is read-only at run time.

**Adventure Academy Voices** has a parent row but no inline database. Build one with the steps above the first time a voice gets logged there.

## Don'ts

- Don't add a Tags property. Ever.
- Don't normalize or "fix" `Dialect` values on existing rows.
- Don't invent a dialect he didn't give you.
- Don't delete files from `/home/workspace/Audio/VoiceSamples/` on Zo.
- Don't put the upload token in a message to Pavi.
