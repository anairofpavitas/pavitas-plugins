# Technique Catalog

Organized by *what you're trying to achieve*, not by medium. Each technique includes specific implementation details, not vague principles.

## Creating Clear Hierarchy

### Dramatic Scale Differences
**What it achieves:** Instantly communicates information priority

**Specific moves:**
- Headers 3-4x body size, not 1.5x (48pt vs 16pt, not 24pt vs 18pt)
- Key numbers 5-10x larger than labels (72pt vs 12pt)
- Section titles 2x subsection titles minimum

**When to use:** Dashboards, presentations, documents where scanning is critical

**Example implementation:**
```
Hero title: 64pt, 700 weight
Section header: 32pt, 600 weight  
Subsection: 20pt, 600 weight
Body: 16pt, 400 weight
Caption: 12pt, 400 weight
```

### Visual Weight Through Contrast
**What it achieves:** Directs attention without size changes

**Specific moves:**
- Bold + dark for primary (700 weight, gray-900)
- Medium + mid-tone for secondary (500 weight, gray-600)
- Light + pale for tertiary (400 weight, gray-400)
- Use only one emphasis per element (not bold + large + colored)

**When to use:** Dense information where size variations aren't practical

### Progressive Information Disclosure
**What it achieves:** Prevents cognitive overload

**Specific moves:**
- Lead with conclusion/insight (large, prominent)
- Supporting data below fold or in appendix
- Use expandable sections in digital formats
- "Show more" patterns for optional details

**When to use:** Complex reports, dashboards with multiple data layers, presentations

## Establishing Professional Polish

### Precision Spacing Systems
**What it achieves:** Creates rhythm and prevents haphazard layouts

**Specific moves:**
- 8pt spacing scale: 8, 16, 24, 32, 48, 64, 96 (or 12pt: 12, 24, 36, 48, 72)
- Component internal padding: 16-24px
- Between related items: 16-24px
- Between sections: 48-64px
- Page margins: 48-96px (more = more premium)

**Implementation:**
```
Tight: 8-16px (related items)
Standard: 24-32px (component separation)
Generous: 48-64px (section breaks)
Expansive: 96-120px (premium breathing room)
```

### Subtle Grid Alignment
**What it achieves:** Feels ordered without looking rigid

**Specific moves:**
- Everything aligns to 8px or 12px grid (even if invisible)
- Break grid intentionally for emphasis, never accidentally
- Left-align text blocks for readability (centered is for special occasions)
- Use column grids for multi-element layouts (2-column, 3-column, 12-column)

### Color as Structure
**What it achieves:** Organization without lines everywhere

**Specific moves:**
- Background shifts define sections (white → gray-50 → white)
- Tinted cards for grouping (blue-50 background, blue-600 accent)
- Color blocks for categorical separation (not random colors)
- Avoid using borders when color contrast can work

**Example palette:**
```
Primary: #2563eb (blue-600)
Primary light: #eff6ff (blue-50)
Success: #10b981 (green-500)
Error: #ef4444 (red-500)
Gray scale: #f9fafb, #e5e7eb, #9ca3af, #4b5563, #1f2937
```

## Communicating Authority & Trust

### Restrained Color Palette
**What it achieves:** Looks serious, not playful

**Specific moves:**
- Navy/charcoal primary (#1e293b, #1f2937)
- Single accent color, used sparingly (#2563eb, #7c3aed)
- Grays for most UI elements
- Avoid bright, saturated colors unless representing data

**When to use:** Financial reports, B2B presentations, corporate documents

### Serif Typography for Credibility
**What it achieves:** Establishes traditional authority

**Specific moves:**
- Headers in serif (Georgia, Crimson, Lora, Merriweather)
- Body in clean sans-serif for readability
- Or all serif for traditional documents (legal, academic)

**When NOT to use:** Tech products, creative work, modern startups

### Data Visualization Best Practices
**What it achieves:** Trustworthy, readable charts

**Specific moves:**
- Remove gridlines (or make them subtle gray-200)
- Direct label data points (not just legend)
- Use color purposefully (not Excel rainbow defaults)
- Clean axes (no unnecessary decimals)
- Clear titles that state the insight, not just topic

**Bad:** "Q3 Sales" (what about them?)
**Good:** "Q3 Sales Exceeded Target by 23%"

## Guiding Attention & Focus

### Asymmetric Emphasis
**What it achieves:** Breaks visual monotony, creates interest

**Specific moves:**
- Hero content on left 60%, supporting on right 40%
- Large image with small text overlay (not centered)
- Off-center focal points with generous white space

**Example layout:**
```
|============================|============|
| Main Content               | Sidebar    |
| (60% width)                | (40%)      |
|============================|============|
```

### Selective Color Usage
**What it achieves:** Directs eye to priority elements

**Specific moves:**
- Mostly grayscale with one accent color for CTAs/key points
- Color saturation for primary actions (bright blue button)
- Desaturated for secondary actions (gray outline)
- Reserve bright colors for <10% of interface

**Color attention hierarchy:**
1. Bright saturated accent (use sparingly)
2. Strong contrast text (black on white)
3. Medium contrast (gray-700 on white)
4. Low contrast (gray-400 on white) for de-emphasized

### Strategic Use of Negative Space
**What it achieves:** Creates focus through isolation

**Specific moves:**
- Surround key elements with generous margins (48-96px minimum)
- Don't fill space just because it's there
- Use white space to create visual groupings
- Empty space makes everything else feel more important

## Creating Modern, Tech-Forward Aesthetics

### Geometric Sans-Serif Typography
**What it achieves:** Clean, contemporary feel

**Specific moves:**
- Inter, SF Pro, Helvetica Neue for UI
- Space Grotesk, Poppins, DM Sans for more personality
- Medium-high x-height for screen readability
- Avoid condensed fonts (feel cramped on screens)

### Gradient Accents (Used Sparingly)
**What it achieves:** Modern polish without looking dated

**Specific moves:**
- Subtle gradients in backgrounds (not 1990s rainbow)
- Two close colors (blue-500 to purple-600)
- 120-180 degree angles (not 90 degree splits)
- Use for cards, headers, hero sections—not everywhere

**Example:**
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Card-Based Layouts
**What it achieves:** Clear separation, modern structure

**Specific moves:**
- Subtle shadows (0 1px 3px rgba(0,0,0,0.1))
- Rounded corners (4-8px, not 20px)
- Padding: 24-32px internal
- Hover states (subtle lift: shadow increase)

### Monospace for Technical Content
**What it achieves:** Signals code, data, precision

**Specific moves:**
- JetBrains Mono, Fira Code, IBM Plex Mono
- For code blocks, API endpoints, configuration
- Use sparingly outside technical contexts

## Building Information-Dense Displays

### Table Enhancement Techniques
**What it achieves:** Makes spreadsheets readable, not overwhelming

**Specific moves:**
- Header row: Bold, colored background (not bright blue—use gray-100), 12pt
- Data rows: Subtle banding (alternate white/#fafafa), 11pt
- Borders: Only where structure demands (header bottom, section breaks)
- Alignment: Numbers right-aligned, text left-aligned
- Highlight totals: Bold, top border, slightly larger

**Specific implementation:**
```
Headers: 12pt, 600 weight, #f3f4f6 background, #1f2937 text
Data: 11pt, 400 weight, alternate row #ffffff/#fafafa
Totals: 11pt, 700 weight, top border 2px #d1d5db
```

### Dashboard Grid Systems
**What it achieves:** Organized complexity

**Specific moves:**
- 12-column grid for flexibility
- Card-based modules (each card = one metric/chart)
- Larger cards for primary metrics (span 6-8 columns)
- Smaller cards for supporting data (span 3-4 columns)
- Consistent card heights within rows

### Color-Coded Categories
**What it achieves:** Quick pattern recognition

**Specific moves:**
- 5-7 distinct colors maximum for categories
- Use tints of same hue for related categories
- Reserve red/green for universal meanings (danger/success)
- Test for color blindness accessibility

**Accessible palette:**
```
Blue: #2563eb, Orange: #ea580c, Green: #059669
Purple: #7c3aed, Teal: #0891b2, Pink: #db2777
```

## Creating Presentation Impact

### One Idea Per Slide
**What it achieves:** Clarity and memorability

**Specific moves:**
- Single statement headline (large, 48-64pt)
- One supporting visual or 3-5 bullets maximum
- Rest goes in speaker notes
- Build animations reveal points sequentially

### Image-Dominant Layouts
**What it achieves:** Emotional connection, visual interest

**Specific moves:**
- Full-bleed images (edge to edge, no borders)
- Dark overlay (40-60% opacity) for text readability
- White text on dark overlay, not colored
- Keep text to one side (not centered)

### Data Visualization on Dark
**What it achieves:** Modern, focused presentation

**Specific moves:**
- Dark navy/charcoal background (#1e293b, #0f172a)
- White/light gray text (#f8fafc, #e2e8f0)
- Bright accent colors pop on dark (cyan, yellow, magenta)
- Generous padding (all elements float in space)

## Format-Specific Techniques

### PowerPoint/Google Slides Elevation
- Custom slide master (not default templates)
- Consistent header positioning (top 10% of slide)
- Footer with minimal info (page numbers, not clutter)
- Slide transitions: None or subtle fade (not dramatic)

### Excel/Google Sheets Elevation
- Custom number formats ($#,##0 not general)
- Conditional formatting (subtle color scales, not traffic lights)
- Sparklines for inline trends (in cells alongside data)
- Hide gridlines (View → Gridlines off)

### HTML/CSS Elevation
- CSS Grid for layout (not floats or tables)
- CSS custom properties for theming
```css
:root {
  --color-primary: #2563eb;
  --spacing-lg: 48px;
  --font-display: 'Inter', sans-serif;
}
```
- Hover states for interactive elements
- Smooth transitions (transition: all 0.2s ease)

### PDF Document Elevation
- Generous margins (1-1.5 inch minimum)
- Running headers/footers for navigation
- Page numbers in consistent position
- High-contrast for print readability

## The Anti-Patterns (What NOT to Do)

### Avoid These Generic Moves
- ❌ Centered alignment for everything (lazy, not intentional)
- ❌ Rainbow color schemes (no relationship between colors)
- ❌ Clip art or generic stock photos (instantly dated)
- ❌ Multiple competing fonts (more than 2 is usually chaos)
- ❌ Decorative borders everywhere (visual noise)
- ❌ Bright saturated backgrounds (#00FFFF, #FF00FF)
- ❌ Comic Sans, Papyrus, or other overused novelty fonts
- ❌ Text effects (shadows, bevels, glows) from 2003
- ❌ Every element the same visual weight (no hierarchy)
- ❌ Cramming content to avoid white space

## Deployment Strategy

**Start with one strong move, then support it:**

1. Identify the main job (hierarchy? professionalism? attention?)
2. Pick ONE primary technique from above
3. Add 1-2 supporting techniques
4. Apply consistently throughout
5. Review against interrogation checklist

**Don't use every technique at once.** The art is in selective deployment.
