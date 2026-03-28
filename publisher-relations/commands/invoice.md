---
description: Generate a branded invoice for a publisher using stored profiles and project data from Notion.
---

# Invoice Generator

Quick path to invoice creation. Uses stored publisher profiles and the business-documentation skill.

## Usage Examples

- "Invoice Blackstone for 18.5 finished hours on DotF 17"
- "Generate invoice for Portal Books, Exlian 5"
- "Create invoice for Audible, 12.3 FH"

## Execution

1. **Identify publisher** from input
2. **Load publisher profile**:
   - Billing contact and address
   - Payment terms
   - Any special requirements (PO numbers, etc.)
3. **Get project details** from Notion or from input:
   - Book title and number
   - Author name
   - Finished hours (actual, from delivered audio)
4. **Calculate total**: FH × PFH rate (default $350, check stored rate for publisher)
5. **Generate invoice** using business-documentation skill:
   - Pavitas Productions LLC branding
   - Logo placement
   - Professional PDF output
   - Consistent formatting via design-elevation skill
6. **Present for review** — Biz Mode, never finalize without approval

## Publisher Rate Reference

Check stored profiles first. If no stored rate, default to $350 PFH and flag for confirmation.

## Rules
- Always present draft for review
- If calculated amount seems unusual (< $1,000 or > $10,000), double-check the inputs
- Include payment terms on the invoice
- Sequential invoice numbering if Pavi has a system, otherwise date-based
