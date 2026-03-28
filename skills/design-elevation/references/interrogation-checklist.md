# Design Interrogation Checklist

Before delivering ANY visual output, interrogate these dimensions. This is your internal quality gate—the user doesn't see this process, only the elevated result.

## Typography Interrogation

### Typeface Selection
- [ ] **Am I using defaults because they're there, or because they're right?**
  - PowerPoint's Calibri? Google's Roboto? Only if they serve the content.
  - Consider: Does this context demand serif authority? Sans-serif clarity? Monospace precision?

- [ ] **Does the typeface match the content's personality?**
  - Financial data → Clean, authoritative (Inter, SF Pro, Helvetica Neue)
  - Creative work → Distinctive but readable (Poppins, Space Grotesk, DM Sans)
  - Technical docs → Monospace for code, clear sans for text (JetBrains Mono, IBM Plex)

- [ ] **Am I pairing typefaces intentionally?**
  - Contrast works: Serif headers + sans body, Display title + text workhorse
  - Don't pair two similar sans-serifs or two similar serifs unless you know exactly why

### Hierarchy & Scale
- [ ] **Is the scale difference dramatic enough?**
  - Generic: H1 is 24pt, body is 18pt (1.33x difference)
  - Elevated: H1 is 48pt, body is 16pt (3x difference) - Creates clear hierarchy

- [ ] **Can I identify information priority in 2 seconds?**
  - Main point should be 2-3x larger than supporting text
  - Labels should be 0.75x body size or smaller
  - Scale creates hierarchy more effectively than color or bold

- [ ] **Am I using weight purposefully?**
  - Headers: 600-700 weight for presence without heaviness
  - Body: 400 for easy reading, 500 for slight emphasis
  - Labels/metadata: 300-400 for visual subordination
  - Avoid using both bold and large simultaneously (redundant)

### Spacing & Line Height
- [ ] **Is the line height comfortable?**
  - Tight: 1.2-1.3x for large headings (display text)
  - Standard: 1.5x for body copy (optimal readability)
  - Generous: 1.6-1.8x for long-form reading or emphasis
  - Never use default single spacing (1.0x) for body text

- [ ] **Does paragraph spacing create clear breaks?**
  - Between paragraphs: 0.75-1x line height
  - Between sections: 1.5-2x line height
  - White space is a design element, not empty space

## Color Interrogation

### Palette Selection
- [ ] **Is this a considered color system or random choices?**
  - Professional: 1 primary, 1-2 accents, neutrals for structure
  - Amateur: Multiple competing colors with no relationship

- [ ] **Do my colors reference professional standards?**
  - Stripe blues, Linear purples, Apple grays—study these palettes
  - Avoid pure black (#000000) and pure white on bright backgrounds
  - Use near-black (#1a1a1a) and off-white (#fafafa)

- [ ] **Am I using color functionally, not just decoratively?**
  - Primary: Brand identity, key actions, emphasis
  - Success/Error: Green (#10b981) / Red (#ef4444) with good contrast
  - Neutral hierarchy: Multiple grays (900, 700, 500, 300, 100) for depth

### Contrast & Readability
- [ ] **Is text readable in all contexts?**
  - Minimum 4.5:1 contrast for body text (WCAG AA standard)
  - 7:1 for optimal readability
  - Use contrast checkers, don't guess

- [ ] **Am I using subtle color differences intentionally?**
  - Background shifts (white to gray-50) create section separation
  - Tinted backgrounds (blue-50, purple-50) highlight key areas without screaming

## Layout Interrogation

### Structure & Grid
- [ ] **Is there an intentional underlying structure?**
  - Everything should align to a grid (even if invisible)
  - Use 8pt or 12pt spacing system for consistency
  - Misalignment should be a deliberate choice, not sloppiness

- [ ] **Am I using the full canvas thoughtfully?**
  - Margins matter: 48-64px minimum, 80-120px for breathing room
  - Don't cram content to fill space
  - Don't leave awkward gaps that suggest you didn't notice them

- [ ] **Does the layout guide the eye naturally?**
  - Z-pattern for web/documents (top left → top right → bottom left → bottom right)
  - F-pattern for dense information (scan left edge, horizontal passes)
  - Focal points should be obvious, not accidental

### Composition
- [ ] **Am I using proximity to show relationships?**
  - Related items should be closer together than unrelated items
  - Group spacing should be 2-3x tighter than separation spacing

- [ ] **Does visual weight create appropriate emphasis?**
  - Larger, bolder, brighter elements draw attention first
  - Use size, color, and position to direct focus deliberately

- [ ] **Am I leaving enough white space?**
  - Generous margins make everything feel premium
  - Dense layouts feel cheap, cramped, and hard to scan
  - White space is active design, not empty space to fill

## Information Architecture

### Hierarchy & Organization
- [ ] **Can someone understand the structure in 10 seconds?**
  - Main sections clearly differentiated from subsections
  - Supporting details visually subordinate to key points
  - Use size, weight, color, and space to create levels

- [ ] **Is the most important information the most prominent?**
  - Bury supporting details, elevate key insights
  - Lead with the answer, not the process

- [ ] **Am I using progressive disclosure appropriately?**
  - Overview → Detail → Supporting data (for presentations)
  - Summary → Sections → Appendix (for documents)
  - Don't front-load everything equally

## Format-Specific Interrogation

### Presentations (PPTX, Google Slides)
- [ ] **Is each slide doing one job well?**
  - One key point per slide, not multiple competing ideas
  - Use build animations to reveal information progressively
  - Supporting details can be in speaker notes, not cluttering slides

- [ ] **Am I using slide real estate effectively?**
  - Large, impactful visuals (not tiny centered images)
  - Generous margins (not content crammed edge-to-edge)
  - Asymmetric layouts (not everything centered)

### Spreadsheets (XLSX, Google Sheets)
- [ ] **Have I moved beyond default table styling?**
  - Custom header colors, not green/blue defaults
  - Subtle row banding (gray-50, not bright blue)
  - Cell borders used sparingly for structure, not everywhere

- [ ] **Is the data hierarchy clear?**
  - Headers bold, larger, colored background
  - Totals/summaries have visual weight (bold, borders, shading)
  - Input vs. calculated cells clearly differentiated

### HTML/Web (Artifacts, Pages)
- [ ] **Am I using modern layout techniques?**
  - Flexbox/Grid for structure, not floats
  - Responsive spacing (clamp, viewport units)
  - CSS custom properties for consistent theming

- [ ] **Does this feel hand-coded or templated?**
  - Custom spacing, not Bootstrap defaults
  - Intentional color palette, not theme colors
  - Typography hierarchy that shows craft

### Documents (PDFs, DOCX)
- [ ] **Is the document structure immediately clear?**
  - Headers guide navigation at a glance
  - Sections have clear visual separation
  - Supporting elements (footnotes, captions) visually subordinate

## The Final Gate

Before delivering, ask yourself:

**Would I show this to a design director without apologizing?**

If the answer is no, identify what's still generic and elevate it. If the answer is "it's good enough," remember: good enough is the enemy of distinctive.

**One more thing:** Don't apologize in advance or hedge your design choices when presenting to the user. Deliver with confidence. The design work happened internally; the user sees only the polished result.
