---
name: business-documentation
description: Generate consistent, professionally formatted business documents for Pavitas Productions audiobook narration services. Creates invoices, contracts, and other business documents with brand-consistent design. Use when creating invoices or any business documents that need brand colors, logos, and consistent formatting.
---

# Business Documentation - Pavitas Productions

## Company Information
- **Business Name:** Pavitas Productions, LLC
- **Owner:** Pavi Proczko
- **Address:** 4429 N Monitor Ave, Chicago, IL 60630
- **Phone:** (312) 909-1896
- **Email:** pavi@paviproczko.com
- **EIN:** 88-2914799 (include only if specifically requested)

## Brand Assets

### Logos
**Badge format (circular "P ◉ P"):**
- `logo-badge-color.png` - Default for most uses
- `logo-badge-black.png`, `logo-badge-white.png` - For different backgrounds
- `logo-badge-color-bg.png` - With background

**Wordmark format (horizontal text):**
- `logo-wordmark-color.png` - Default for headers
- `logo-wordmark-black.png`, `logo-wordmark-white.png` - For different backgrounds
- `logo-wordmark-color-bg.png` - With background

**Usage:** Use color badge or wordmark consistently across all documents. Badge for compact spaces, wordmark for full branding.

### Brand Colors
**Primary:** #394851 (slate), #f7f4eb (cream), #c7bca2 (beige)
**Accent:** #666441 (olive), #793e2d (terracotta), #62403d (chocolate)

## Client Details

No client data is stored in this skill. For every document, confirm with Pavi: client legal name, billing address, payment terms (default Net 30 if unspecified), and any delivery or formatting requirements. For prior-project context, check the Audiobook Projects DB (IDs in `pavitas-core:workspace-context`) — but billing details still get confirmed, never assumed from old records.

## Invoice Requirements

**Critical:** Apply `pavitas-core:output-quality` (visual half) for consistent, elevated formatting.

**Logo placement:**
- **Header:** Use color wordmark logo in the centered header section
- **Top right corner:** Place color badge logo for consistent branding

**Default settings:**
- **Invoice date:** Defaults to today's date (invoice creation date)
- **Due date:** Defaults to 30 days from invoice date
- **Payment methods:** Leave blank unless user specifies (project-specific)

**Invoice structure:**
- Header with wordmark logo (centered)
- Badge logo (top right corner)
- Invoice number format: User-specified or PP-YYYY-MM-### (e.g., PP-2024-11-001)
- Bill To section with client info confirmed for this document
- Service table: Description | Quantity (FH) | Rate (PFH) | Amount
- Payment terms as confirmed (default: Net 30)
- Payment methods: Only include if user specifies for this project
- Footer: "Thank you for your business!"

**Rate:** $350/PFH unless Pavi states otherwise — flag deviations (`pavitas-core:safety-rails`, Biz Mode).

**Output:** .docx format by default. Filename: Invoice_[ClientName]_[ProjectName]_[Date].docx

**Before generating:** Confirm client name, project, finished hours, and rate if not provided.

## Usage

**Creating invoices:**
"Create an invoice for [Client] for [X] hours on [Project]"

**Design changes:**
Update this skill document to apply changes to all future documents.
