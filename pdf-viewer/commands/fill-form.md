---
description: Fill PDF form fields interactively with live visual feedback
argument-hint: "[path-or-url]"
---

> If you need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

# Fill Form

Help Pavi complete a fillable PDF in the live viewer — typically a
contractor tax form (W-9), a publisher vendor-setup or direct-deposit
form, or onboarding paperwork. Unlike headless form tools, this gives
**direct visual feedback** on every field as it's filled, with easy
undo/edit in the viewer.

## Context you can reuse

Recurring fields on Pavi's forms:
- **Name / business name** — Pavlo (Paul) Proczko / Pavitas Productions LLC
- **Federal tax classification** — LLC (confirm the sub-election box with
  him if the form asks S/C/P)
- **Email** — pavi@paviproczko.com

Never guess sensitive values — **EIN/SSN, address, and bank/routing
numbers must come from Pavi.** Ask; don't infer.

## Why use this instead of programmatic form filling

- **Visual confirmation** — Pavi sees each value land in the right box
- **Unnamed/unlabeled fields** — W-9s and vendor forms are full of
  fields named `f1_1`, `Text7`, or nothing. The real label is printed
  **next to** the box on the page, not in the metadata. `get_screenshot`
  to see what each field is, then fill by name.
- **Easy correction** — he can edit or clear any field directly, or ask
  you to `fill_form` again

## Two approaches

### User-driven (simple, well-labeled forms)

Call `display_pdf` with `elicit_form_inputs: true`. The server detects
fields and prompts Pavi to enter values **before** the viewer opens.

### AI-assisted (complex forms, unnamed fields, or when you have context)

1. `display_pdf` (without elicit) — inspect returned `formFields`
2. If field names are cryptic, `interact` -> `get_screenshot` of each
   page with fields; read the visual labels next to each box
3. For each field, either fill from the context above or ask Pavi
   (describing the field by its visual label)
4. `interact` -> `fill_form` with `fields: [{name, value}, ...]`
5. `interact` -> `get_screenshot` of each filled page
6. Show him, confirm or edit

## Example

> **Pavi:** Help me fill out this W-9 for Aethon
>
> *You:* `display_pdf` -> formFields: `f1_1`, `f1_2`, `f1_3`, `c1_1`, ...
>
> *You:* `get_screenshot` page 1 -> `f1_1` is "Name", `f1_2` is
> "Business name", `c1_*` are the tax-classification checkboxes
>
> *You:* "I'll put Paul Proczko as the name, Pavitas Productions LLC as
> the business name, and check LLC. What's the EIN and the address you
> want on this one?"
>
> *After answers:* `fill_form` + `get_screenshot`
>
> *You:* "Filled [screenshot]. Signature and date lines are blank — want
> to sign it now with `/pdf-viewer:sign`?"

## Notes

- Signature fields are separate — fill text first, then `/pdf-viewer:sign`
- Checkbox/radio values are `true`/`false` or the option string
- Pavi can always drag & edit fields directly in the viewer
