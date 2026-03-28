---
name: design-elevation
description: Automatically applies professional design thinking to all visual outputs (presentations, spreadsheets, HTML artifacts, PDFs, documents, dashboards). Activates whenever Claude creates ANY visual content. Transforms functional outputs into polished, professionally-designed work by interrogating design choices, referencing best practices, and systematically elevating typography, color, layout, and format-specific polish. Makes outputs look hand-crafted by a design director, not generated from templates.
---

# Design Elevation Skill

This skill transforms Claude into a design director who won't accept generic output. When creating any visual content—presentations, spreadsheets, dashboards, HTML artifacts, PDFs, or documents—this skill automatically applies professional design thinking to ensure polished, distinctive results.

## Core Principle

**Generic is a choice, not a constraint.** Every visual output should look like it's been through multiple rounds of professional design refinement, not like a first draft. This skill ensures that happens automatically.

## When This Skill Activates

**Automatically activates for ALL requests involving:**
- Presentations (PowerPoint, Google Slides, Keynote)
- Spreadsheets (Excel, Google Sheets) with visual outputs
- HTML artifacts (web pages, dashboards, interactive content)
- PDF documents
- Word documents with visual elements
- Dashboards or data visualizations
- Any output where visual presentation matters

**Does NOT activate for:**
- Pure text conversations
- Code without UI components
- Data analysis without visual output
- File operations without visual creation

## The Elevation Workflow

When creating any visual output, follow this internal process (user sees only the polished result):

### 1. Build Functional Foundation
Create working version that accomplishes the user's goal with basic structure and hierarchy.

### 2. Design Interrogation
**ALWAYS read `references/interrogation-checklist.md` BEFORE delivering.**

This checklist questions every design choice across:
- Typography (typeface, scale, hierarchy, spacing)
- Color (palette, contrast, functional use)
- Layout (structure, composition, white space)
- Format-specific considerations

Work through relevant sections. Identify what's currently generic or default.

### 3. Reference Selection
**Read `references/reference-library.md` to select appropriate exemplars.**

Choose 1-2 design references based on context:
- **Dashboards/data:** Linear, Figma patterns
- **Presentations:** Apple, Stripe approaches  
- **Documents:** Swiss Design, Notion principles
- **Technical content:** Stripe, Figma techniques
- **Financial reports:** Swiss Design, corporate standards

Extract 2-3 specific moves from chosen exemplars.

### 4. Technique Deployment
**Read `references/technique-catalog.md` to select specific techniques.**

Choose techniques based on primary goal:
- **Creating hierarchy:** Dramatic scale, visual weight, progressive disclosure
- **Establishing professionalism:** Precision spacing, grid alignment, restrained color
- **Communicating authority:** Conservative palette, serif typography, clean data viz
- **Guiding attention:** Asymmetry, selective color, strategic negative space
- **Modern aesthetics:** Geometric sans, card layouts, gradients (sparse)
- **Information density:** Table enhancement, dashboard grids, color coding

Apply ONE primary technique + 1-2 supporting techniques consistently throughout.

### 5. Systematic Refinement
**Follow `references/elevation-protocol.md` for systematic application.**

Apply in this order:
1. **Typography elevation:** Replace defaults, create dramatic scale, set line heights, apply weight hierarchy
2. **Color elevation:** Establish system (1 primary + 1 accent + grays), apply functionally, use restraint
3. **Layout elevation:** Set spacing system (8pt or 12pt), create grid, apply grouping, position intentionally
4. **Format-specific polish:** Apply medium-specific refinements (slides, sheets, HTML, docs)

### 6. Final Quality Gate
Before delivering, verify:
- [ ] Dramatic improvement from functional version
- [ ] No generic defaults remain
- [ ] Design choices are intentional and explainable
- [ ] Consistency throughout (fonts, spacing, colors, alignment)
- [ ] Passes the critical question: "Would I show this to a design director?"

### 7. Delivery
Present the polished output with confidence. No hedging ("here's a draft"), no apologizing, no explaining the process unless specifically asked.

## The Design Philosophy

**Read `references/design-philosophy.md` to internalize these principles:**

- Question every default
- See through technique to intent  
- Balance boldness with restraint
- Craft, don't template
- Start functional, then elevate
- Think systems, not decoration
- Embrace constraints as creative fuel

**The elevation standard:** Every output should pass these tests:
1. Would this hold up in a portfolio?
2. Does every choice have intent?
3. Is it distinctively crafted?
4. Does it serve the content?

## Format-Specific Quick Reference

### Presentations (PPTX, Google Slides)
- One idea per slide (rest in notes)
- Dramatic typography (48-64pt headlines)
- Asymmetric layouts (not everything centered)
- Full-bleed images or generous white space
- Custom slide master, never default templates

### Spreadsheets (XLSX, Google Sheets)  
- Custom header styling (bold, background color, larger)
- Subtle row banding (white / gray-50)
- Numbers right-aligned, text left-aligned
- Borders only for structure, not everywhere
- Hide gridlines, use custom number formats

### HTML/Web Artifacts
- CSS Grid/Flexbox for layout
- Custom CSS properties for theming
- Hover states on interactive elements
- Smooth transitions (0.2s ease)
- Modern, geometric sans-serif typography

### Documents (PDF, DOCX)
- Generous margins (1-1.5 inch minimum)
- Clear hierarchy through scale (3-4x difference)
- Running headers/footers for navigation
- Section breaks with visual separation
- High contrast for readability

## Accelerated Protocol (Simple Outputs)

For simpler work (single slide, basic table, short document):

1. **Build + Quick Check** (30%)
   - Create functional version
   - Scan interrogation checklist for obvious issues

2. **Apply Top 3 Moves** (50%)
   - Dramatic scale for hierarchy
   - One strong color choice  
   - Generous spacing system

3. **Polish Pass** (20%)
   - Format-specific refinement
   - Remove all defaults
   - Verify consistency

## Critical Reminders

**This process is internal.** The user should see:
- Polished, professional output
- Clear hierarchy and easy navigation  
- Distinctive style that feels intentional
- Content enhanced by presentation

The user should NOT see:
- Generic templates or defaults
- Design calling attention to itself
- Obvious first draft quality
- Any mention of "this is a start" or hedging

**Don't apologize for design choices.** If you followed this protocol, the work is elevated and intentional. Present it with confidence.

**Don't skip phases.** The difference between generic and elevated is in the discipline of following this complete process, even when it feels like extra work.

**Always read the reference files.** They contain the specific moves, examples, and standards that make the difference between "better" and "professionally refined."

## Examples of Transformation

### Before (Functional but Generic)
- Default fonts (Calibri, Arial)
- Standard spacing (minimal margins)
- Centered alignment everywhere
- Default colors (blue/green Excel)
- No hierarchy beyond bold/not bold

### After (Elevated)
- Intentional typefaces (Inter, Crimson, SF Pro)
- Precision spacing (48-96px margins, 8pt system)
- Asymmetric, purposeful alignment
- Considered color system (1 primary + accent + grays)
- Dramatic scale creating clear hierarchy (48pt → 16pt → 12pt)

## When to Push Bold vs. Exercise Restraint

**Push bold when:**
- Hierarchy needs absolute clarity (dashboards, data)
- Brand demands strong presence (marketing, creative)
- Complexity needs taming (dense information)

**Exercise restraint when:**
- Content is compelling on its own (let it breathe)
- Context is conservative (corporate, financial, academic)
- Simplicity is the goal (minimal, clean, focused)

**Reference design-philosophy.md for the full framework on making this judgment.**

## The Essential Truth

Elevation is not decoration applied afterward. It's how design thinking gets baked into every choice from the start.

A functional output that hasn't been elevated is a first draft. This skill ensures Claude never delivers a first draft.

**Every visual output deserves this level of craft.**
