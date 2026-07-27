# Series Index

Lookup table for the 🎭 Character Voices system. `Voices data source` is the UUID you pass to
`notion-create-pages` (as `data_source_id`) and to `notion-query-data-sources`
(as `collection://<uuid>`).

Verified 2026-07-27.

| Series | Aliases Pavi uses | Series page | Voices database | Voices data source |
|---|---|---|---|---|
| Defiance of the Fall Voices | DotF, Defiance | `12a089eb3ccc801fb8e4f9495981d2b9` | `f5e62bcb28354746a26d35080e8411b8` | `4d8a97dc-0408-4da4-9963-d17e5bef0a63` |
| Daily Grind Voices | Daily Grind, DG | `12a089eb3ccc802fbaf2dac64b745281` | `41ab7bd50e004775950385146eaa3c3e` | `444f215a-e324-4e7f-ad78-43beddfd3d3c` |
| Kolya Petrov Voices | Kolya, Petrov | `12a089eb3ccc804099f7e515f1d23459` | `174089eb3ccc80cc89fbd268108af0ef` | `174089eb-3ccc-8142-bc72-000bab78a7c6` |
| Obelisk Voices | Obelisk | `12a089eb3ccc8056b285c0ca6ed1c04e` | `152089eb3ccc80818f44ee5df2a4132a` | `152089eb-3ccc-8126-a68b-000bb295a0f6` |
| Exlian Syndrome Voices | Exlian | `12a089eb3ccc806d95ead765b6fb727e` | `17a089eb3ccc80e7b698e063aaafc1de` | `17a089eb-3ccc-8109-92da-000b86fa7d82` |
| QiMC 2 Voices | QiMC, QiMC2, Fourth Law of Cultivation | `12a089eb3ccc808789bdd2b014bbe873` | `f2ac446c2f4f4dee83765b77311d88f1` | `b647c208-1b69-40a9-baef-9a142a57c6ea` |
| ASR Loremaster Voices | ASR, Loremaster | `12a089eb3ccc809da834ffedf75f8ccf` | `d38168117029442387bc9da7ce981323` | `0ced5f24-30d5-4be6-ad10-57453b29c483` |
| Dawn of Wizards Voices | DoW, Dawn of Wizards | `12a089eb3ccc80aa9dedcd56457e96a3` | `118089eb3ccc8065ad8dc9e88dccf615` | `118089eb-3ccc-8105-92c0-000b7da8f1cf` |
| ACA Voices | ACA | `12a089eb3ccc80b08be0fcd89c2002fa` | `efdd767825d8410b87ba3a7704f3719b` | `00197357-4d75-4f7b-82f6-5fa30a386873` |
| Apocalypse Summoner Voices | Apoc Summoner, AS | `12a089eb3ccc80b09554fc4d852a5614` | `f5903e4e42174e64baa6c0a46b6fc5bb` | `77539a8d-475e-48ba-9265-f20421fd9119` |
| Adventure Academy Voices | Adventure Academy, AA | `12a089eb3ccc80fca29ef6bd26d824e3` | **none — build one** | — |
| Skill Hunter Voices | Skill Hunter, SH | `1e3089eb3ccc80bcadbbf2ec00424ce4` | `1e3089eb3ccc8003a999c73f930a42f5` | `1e3089eb-3ccc-819f-bcd4-000b5b740e2f` |
| Demon Loan Voices | Demon Loan, DL | `35d089eb3ccc80e1a485f56e35fad8f4` | `35d089eb3ccc80c3b8aaebe35255a377` | `35d089eb-3ccc-80c5-816f-000b5e5dc900` |
| Loop Bound Voices | Loop Bound, LB, LB1/2/3 | `3aa089eb3ccc81cfb5ccf231b8f72ba3` | `89b2109df2594fe09cf495cb309f9cd5` | `b1c9c872-2e85-415a-8e1d-7306f902f11c` |

## Notes

- **Adventure Academy Voices** — parent row exists, page body is blank. First voice logged there
  needs the inline database created (see "Creating a new series," steps 3–5).
- **Loop Bound Voices** covers Loop Bound 1, 2, and 3.
- Series names follow the *series*, not the book. `QiMC 2` is the second QiMC series, not book two.
- Prefix `https://app.notion.com/p/` to any page/database ID above for a working URL.

## Parent system IDs

| Thing | ID |
|---|---|
| 🎭 Character Voices data source | `8e45d582-7f69-4275-90ff-f242ebe70cbc` |
| 🎧 Audiobook Projects data source | `28321020-d7f5-4619-aafd-28c3faccf815` |
| Relation property on Character Voices | `🎧 Audiobook Projects` |
| Relation property on Audiobook Projects | `Voice Database` |

## Zo audio hosting

| Thing | Value |
|---|---|
| Upload endpoint | `POST https://paviproczko.zo.space/api/voice-sample?name=<slug>` |
| Auth header | `x-voice-token: <token>` |
| Token file (on Zo) | `/home/workspace/.zo-app-data/voice-log/token.txt` |
| Playback URL | `https://paviproczko.zo.space/api/voice-sample/<slug>.m4a` |
| Storage dir (on Zo) | `/home/workspace/Audio/VoiceSamples/` |
| Size cap | 25 MB |

Rotate the token by writing a new value to the token file — the route reads it fresh on every
request, so no redeploy is needed.
