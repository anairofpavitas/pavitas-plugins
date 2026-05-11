# Companion integration

Pocket-hunt supports three companion states, with a fourth for mixed combinations:

1. **Solo** — user is alone
2. **Human companion** — partner, friend, family member
3. **Non-human companion** — one or more dogs
4. **Mixed** — human companion + dogs

Ask at intake which state applies. Mid-hunt, the user can add or remove companions; accept and adapt.

---

## The presence ethic

When any companion is present, the framing shifts. Pocket-hunt is **structured permission to be a little weird together** — not permission to drift into your phone while ignoring them. Between clues, the user looks up. Shows what they found. Asks what the companion's noticing. The hunt is the trellis; the togetherness is the plant.

This is encoded in the phone-away ethic (top of SKILL.md). When clues are sent, phones go away. The user returns when they have something to share — which is usually the moment of looking up at the companion.

If the user reports back two clues in a row without mentioning the companion, gently surface them in the next clue: *"Before the next clue, take a moment with [companion] — show them what you've gathered so far, ask what they've been noticing."*

This is not a nag. It's one sentence in the clue text, woven in. Don't make it into a separate meta-message.

---

## Solo

The simplest state. No special handling beyond the default flow.

Seed prompts: use solo patterns from `seed-prompts.md`.
Closing: standard debrief.

---

## Human companion (engaged)

The companion is participating actively. Conversation seeds work. They're contributing finds or observations. Their photos can join the album (with their consent at closing).

**Engagement check.** At intake, ask:
- Is the companion playing?
- Are they bringing their own quest, or improvising, or just doing what you're doing?
- If they don't have their own quest but want input — solicit something from them ("what's a color you've been drawn to lately? a texture? a thing you're missing in your life?"). Use it as a seed input.

**Three sub-states for human engagement:**

### (a) Companion has their own quest
They're looking for something specific. Use their target as one of the seeds. Example: companion is hunting for vintage frames → one of the three seeds becomes "frame-adjacent" (rectangular silhouettes, gilded surfaces, frame-shop aesthetics). Their hunt and yours can converge in the same shops.

### (b) Companion wants in but has no quest
Ask them for one input — a color, a feeling, a craving, something they've been thinking about. Use it as a seed. They participate as a second player who can call out finds or photograph alongside.

### (c) Companion is along for the walk, not playing
Don't pull them into mechanics. Solo seed prompts, no conversation seeds. The presence ethic still applies — look up between clues, talk to them — but the hunt structure stays the user's alone.

If the user's not sure which state the companion is in, suggest asking. One sentence: *"Want to be in on this, or just along for the walk?"*

---

## Conversation seeds

When the human companion is engaged (states a or b), seed prompts can use the conversation format. See `seed-prompts.md` "Companion conversation prompts" section.

**Critical:** conversation prompts are read silently by the user. They direct attention internally; the output is what surfaces in natural conversation. The user never reads the prompt aloud — that's the failure mode (reading "find something that reminds you of our first date" at the companion is awkward and breaks the spell).

Example of right vs. wrong:

❌ User reads aloud: *"Claude says, 'find something that reminds you of our first date.'"*
✅ User reads silently, looks around, sees an old movie poster: *"This reminds me of our first date — remember when we got stuck waiting for that movie that turned out to be sold out?"*

The conversation is the seed. Whatever the talk surfaces becomes the anchor for subsequent clues.

If the user is uncertain how to handle a conversation prompt naturally, the prompt itself can include a one-line "how to bring this into conversation" note. Don't over-coach.

---

## Non-human companion (dogs)

Dogs participate by being there. They can't talk, but they shape the hunt in real ways:

- **Pace** — dogs dictate stopping, sniffing, lingering. Clue stretches are shorter. Don't generate clues that require fast walking through interesting smells.
- **Photos** — bias toward dog-centric photo prompts. *"The dog's best calm moment. The dog's most curious sniff. The dog choosing a direction at a fork."*
- **Training context** — dogs benefit from structured calm-time and training reps in environments with stimulus. Clues can integrate training beats explicitly: *"Find a bench with moderate foot traffic. Sit with the dogs for 3–5 minutes. Practice watch-me as people pass. Photograph the calmest moment."*
- **Found objects** — dogs love walks where the human is paying attention to *the path with them*. Found-object hunts (sticks, stones, leaves) pair beautifully with sniff-walks.
- **Environment** — dogs change the venue calculus. Cafes need patios. Shops may or may not be dog-friendly; check before sending them to interiors.

**Pavi-specific defaults** (dogs are Jimothy and Linen, both male):

- Tuesdays and Fridays the dogs are at Camp-Run-A-Pup (7am–7pm) — they're not pocket-hunt companions on those days
- The dogs will probably want a water stop every 20–30 min in warm weather
- Reactive moments are normal — clue mechanics should never put the dogs in unavoidable close contact with other dogs

**Dog-centric clue beats** to rotate through:

- **Sniff break observation.** *"When the dogs pick their next major sniff point, sit with them for 2 minutes. Notice what they notice. Photograph what they're investigating."*
- **Choice point.** *"At the next intersection, let the dogs choose the direction. Go where they go. The next clue happens wherever you end up."*
- **Stranger training.** *"Find a bench in moderate foot traffic. Practice calm sits. Photograph successful moments. Reset and try again if it's not working."*
- **Pace match.** *"Match the pace of the slower dog for the next 5 minutes. Don't rush them. What do you notice at their pace that you'd miss at yours?"*
- **The dog's seed.** *"Watch the dogs for the next 2 minutes. What's something only a dog would notice on this block? Find it from their height. That's a seed."*

---

## Mixed companions

Human + dogs. Some specific considerations:

- The human is the conversation partner. Dogs are presence/pace/training context.
- Conversation seeds still work, adapted to dog-walk pacing.
- The human may be more focused on the dogs than the hunt — accept this. Don't pressure them into clue-engagement.
- Shared photos: dogs and companion alike welcome in the album with companion consent at closing.

If the human companion isn't engaged with the hunt, treat as solo-with-dogs but keep the presence ethic active. They're still there.

---

## Companion consent at closing

Before generating any output that includes the companion's photos or words, ask explicitly. The companion's contributions are theirs. *"Want to include [companion]'s photos and any of their quotes in the output? Or keep this just yours?"*

If they're not in the chat to consent themselves, default to including only what the user (you) have personally shared. Don't compile around the companion without their say.

For dogs: photos of them are at the user's discretion. They can't consent. Treat them like any other photo the user has taken — theirs to include or not.
