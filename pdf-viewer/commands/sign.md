---
description: Place a signature or initials image on a PDF
argument-hint: "[path-or-url] [signature-image-path]"
---

> If you need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

# Sign PDF

Add a visual signature or initials to a document — usually a publisher
narration agreement (Aethon, Podium, Recorded Books, Blackstone,
Audible) or a vendor/onboarding form.

> **Disclaimer:** This places your signature **image** on the page. It
> is **not** a certified or cryptographic digital signature. For a
> legally binding e-signature, use a dedicated signing service. If a
> publisher sends a DocuSign/Adobe Sign link, use that instead — this
> command is for PDFs they email you to sign and return.

## Workflow

1. **Get the signature image** — ask for the local PNG/JPG of Pavi's
   signature or initials. No stored path is configured yet, so ask each
   time (or drag-and-drop onto the viewer). Once he settles on a
   permanent location, note it here so future signings can skip this
   step.

2. **Open the PDF** — `display_pdf` (or reuse an existing `viewUUID`).
   Check the returned `formFields` for signature-type fields — they
   carry page and bounding-box coordinates.

3. **Locate the target** — use a signature field's coordinates if
   present. Otherwise ask: "Which page, and where — bottom-right of the
   last page?" Contracts usually sign on the final page; initials often
   go on each page.

4. **Place it** — `interact` -> `add_annotations`:
   ```json
   {"action": "add_annotations", "annotations": [
     {"id": "sig1", "type": "image", "page": 8,
      "imageUrl": "/path/to/pavi-signature.png",
      "x": 400, "y": 700, "width": 150}
   ]}
   ```
   Width/height auto-detect from the image if omitted.

5. **Verify** — follow with `get_screenshot` of that page, show Pavi,
   adjust position via `update_annotations` if needed. Add the date
   next to the signature with a `freetext` annotation if the contract
   has a date line.

6. **Initials on every page** — batch one `image` annotation per page
   in a single `add_annotations` call.

7. **Return it** — remind him to download the signed PDF from the
   viewer toolbar, then send it back to the publisher.

## Tips

- `imageUrl` accepts local file paths or HTTPS URLs (no data: URIs)
- Coordinate origin is top-left; a typical bottom-right signature on
  US Letter is around `x: 400, y: 700`
- Fill the text fields first with `/pdf-viewer:fill-form`, then sign
