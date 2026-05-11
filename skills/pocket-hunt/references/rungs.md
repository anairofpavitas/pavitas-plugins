# Rungs: commitment levels

Pocket-hunt has four rungs. The user picks one at intake. They can promote, demote, or skip rungs at any point.

The rungs are not a sequence. They're a menu of commitment levels for the same core skill. Each rung adapts the verbs, the seeds, the clue mechanics, and the closing.

---

## Rung 1 — Notice

**Pure presence. No acquisition. No capture. No output.**

The walk is the practice. Seeds are themes you carry in your attention. Clues are noticing prompts — *"for the next 5 minutes, count the shades of green you see"* or *"find three doors that look like they've been repainted multiple times."*

- **Verbs:** notice, spot, watch, listen, hear, smell
- **Seeds:** themed (color, sound, texture, shape, mood)
- **Photos:** none expected
- **Closing:** *"How was it?"* — no artifact, no summary unless requested

**When to recommend:** the user is in a low-energy state, just needs a walk, doesn't have a project in mind, doesn't want to spend money, is in a shop-sparse area, has limited time.

**Companion notes:** seed prompts in companion mode become conversation seeds — see `seed-prompts.md`.

---

## Rung 2 — Notice + capture

**Presence with photos. No acquisition required.**

Same as Rung 1, but each seed gets photographed. Subsequent clues can reference the photos ("the texture you photographed for seed 2"). Optional journal writing is invited but never required — user writes in their own journal off-app, not in chat.

- **Verbs:** notice, photograph, jot (optional)
- **Seeds:** themed, photographed
- **Photos:** central, required for seeds, optional for clue finds
- **Closing:** ask if user wants something generated from photos (collage, social post, journal pages, etc.) — no default output forced. Exit cleanly if declined.

**When to recommend:** the user wants a tangible record but no shopping pressure. Good for residential walks, parks, neighborhoods with limited commercial activity. Good for pure-presence walks with a slightly higher commitment ceiling.

**Companion notes:** companion photos can join the album if the companion consents. Their consent is asked at the end, not assumed.

---

## Rung 3 — Single-find acquisition

**Find or buy one thing per clue.**

Standard pocket-hunt. Each clue identifies a venue (via a small mechanic) and a thing to acquire. The thing connects to a seed where it can. Budget is set at intake.

- **Verbs:** find, get, buy, pocket, collect, forage
- **Seeds:** themed, photographed (carried over from rung 2 default)
- **Photos:** optional during finds, expected for seeds
- **Closing:** brief recap of what was acquired, optional output generation, debrief

**Found-object variant:** in shop-sparse environments, "buy" becomes "forage." Same structure, foraged inputs (leaves, bark, stones, fallen flowers, feathers). See `environment-context.md`.

**When to recommend:** the user wants a small acquisition outcome but doesn't have a multi-item project in mind. Good for "I need to come home with something" walks. Good for travel hunts where the destination is the main acquisition.

---

## Rung 4 — Combinatorial acquisition

**Find multiple things that combine into a project at home.**

Project shapes (pick one at intake or let it emerge):

- **Gift bag for a person** — 5–7 small items for one recipient. Combines into a presentation at home.
- **Craft materials** — 3–6 components for an at-home making project. Substrate, binder, tool, treasure, contrast material, finish, salvage.
- **Outfit assembly** — 3–5 pieces that combine with what you're wearing into a finished or partial outfit. Anchor, head, feet, layer, finisher, or enhancement.
- **Vignette / shelf moment** — 3–5 objects that compose into a small visual arrangement at home. Centerpiece, vessel, scent, scatter, weird object.
- **Sensory pairing** — a meal/snack/drink composition. Hero ingredient, contrast, garnish, vessel.

The find isn't the project — the **assembly is**. Clue language reflects this: each find is a *role*, and Claude tracks which roles are filled.

- **Verbs:** find, get, buy, gather, combine
- **Seeds:** themed, photographed
- **Photos:** expected for seeds; finds can be photographed for the inventory
- **Closing:** offer assembly guidance — "you've gathered X, Y, Z, here's how they could combine" — plus optional output generation, plus debrief

**When to recommend:** the user has a clear creative or social goal and at least 90 minutes. Best with shop-rich environments or wider travel. Foraged combinatorial works for nature-craft projects (botanical arrangements, found-object assemblages).

---

## Promoting / demoting between rungs

The user can promote upward (rung 2 → 3, rung 3 → 4) or demote downward (rung 4 → 3, rung 3 → 2, rung 3 → 1) at any point. Some rules:

- **Promoting mid-hunt:** convert current seeds and finds into the higher rung's structure. Example: rung 2 → rung 3 means the next clue introduces an acquisition verb; existing photos become inventory anchors.
- **Demoting mid-hunt:** keep what's been found, simplify the next clue. Demoting to rung 1 is a "we're done acquiring, let's just walk" pivot — accept and shift to noticing clues.
- **Skipping rungs:** the user can go straight from rung 1 to rung 4. Don't make them ladder through intermediate levels.

Never frame demotion as failure. It's a pivot, not a quit.

---

## Path-aware clue convention

Any clue can use path-aware mechanics — instructions for what to notice or do on the way between two points, in addition to the destination action. This is especially useful in:

- Travel hunts (the route is the hunt)
- Wider-range hunts (long walks/rides between venues)
- Shop-sparse environments (the path matters more than the venue)

**Example:**

> **Clue 4 · The yarn.** Head to the yarn shop on Damen. On the way, count signs that include a word from your color seed. Pick the third yarn you see in the shop that has that color — even if it's not your first instinct. Photograph it before buying.

Two beats: the path observation, the destination action. The path observation usually folds into the seeds. The destination action is the find.

Not every clue needs a path beat. Use it when there's meaningful distance, when the noticing earns the walk, when the user is in travel-hunt mode.

---

## Adapting rung to environment

Rungs aren't environment-agnostic. Some pairings:

- **Rung 1 + residential / park:** noticing prompts skew toward nature, architecture, sounds, weather. Strong default.
- **Rung 2 + residential / park:** capture-rich; photo album of nature and street life. Strong default.
- **Rung 3 + residential / park:** found-object mode is the natural fit. Acquisition becomes foraging.
- **Rung 4 + residential / park:** found-object combinatorial — botanical arrangement, nature assemblage, pressed-flower-and-leaf project.
- **Rung 1 + commercial:** unusual but valid. The noticing is more textured.
- **Rung 2 + commercial:** photo album of shop windows, signs, urban texture.
- **Rung 3 + commercial:** standard shop acquisition.
- **Rung 4 + commercial:** standard combinatorial. The richest combinatorial space.
- **Rung 4 + travel hunt:** the destination provides the final pieces; the route gathers contributing finds.

See `environment-context.md` for fuller treatment.
