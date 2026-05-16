# PNP Partners — Brand Guidelines

**Version 1.0 · May 2026**

---

## 1. The mark

The PNP Partners mark is a single brass dot. It is a perfect circle.
No stem. No leaf. No outline. No ornament.

The dot is a private reference to the Korean persimmon (감) — a symbol of patience and ripening. Most viewers will not catch this. That is fine. The dot's only job is to be *the* dot, the way Target's bullseye or Nike's swoosh are theirs.

**Files:**
- `logos/pnp-mark.svg` — mark only
- `logos/pnp-logo-horizontal.svg` — dot + wordmark, side by side
- `logos/pnp-logo-horizontal-inverse.svg` — for use on navy
- `logos/pnp-logo-stacked.svg` — dot above wordmark, with tagline
- `logos/pnp-logo-korean.svg` — PNP 파트너스 variant
- `logos/pnp-app-icon.svg` — navy-backed square for app icons / social avatars

---

## 2. Color

| Role | Name | HEX | RGB | Notes |
|------|------|-----|-----|-------|
| Primary | Navy | `#0F2C59` | 15 44 89 | Wordmarks, headers, dark surfaces |
| Accent | Brass | `#B8893D` | 184 137 61 | The dot. Used sparingly elsewhere. |
| Tertiary | Champagne | `#E8D9B5` | 232 217 181 | Quiet accent on navy surfaces only |
| Surface | Bone | `#FAF8F4` | 250 248 244 | Page background. Warmer than #FFF. |
| Body text | Ink | `#1A1A1A` | 26 26 26 | Not pure black |
| Secondary text | Slate | `#6B7280` | 107 114 128 | Captions, metadata |

Navy and brass do almost all the work. Resist the urge to introduce a fifth color. If a context demands more contrast, reach for white space — not new pigment.

---

## 3. Typography

| Role | Family | Weights | Use |
|------|--------|---------|-----|
| Display | Fraunces | 600 | Headlines, the wordmark, editorial pull-quotes |
| Body | Inter | 400 / 500 / 600 | All body copy, UI, navigation, captions |
| Korean display | Noto Serif KR | 600 / 700 | Korean headlines |
| Korean body | Noto Sans KR | 400 / 500 | Korean body copy |

Three families is the ceiling. Never four.

**Display tracking:** -2.5% (tightens the wordmark).
**Body line height:** 1.65.

---

## 4. Construction & clear space

All measurements are expressed in units of `x`, where `x` = the diameter of the dot.

- **Clear space:** reserve a margin of at least `0.75x` on all sides of the mark.
- **Minimum size:** never below 16px digital or 5mm print. Below that, the form breaks at anti-aliased edges.
- **Wordmark spacing:** in horizontal lockup, the gap between dot and the letter "P" is `0.5x`. The cap-height of "P" equals `x`.
- **Alignment:** the dot's center aligns to the optical center of the wordmark — not the cap line, not the baseline.

---

## 5. Don't

- Don't stretch, squish, or distort the dot. It is a perfect circle.
- Don't recolor it outside the brand palette.
- Don't add shadows, bevels, glows, or 3D effects.
- Don't apply gradients to the dot.
- Don't use the dot as an outline or stroke only.
- Don't redraw the shape (no persimmon leaves, no stems, no faces).
- Don't pair with another logo at the same scale. The dot leads.

---

## 6. Voice & tone

Speak like a senior consultant who has been in the room and seen the failure mode. Direct, considered, sparing.

**Do**
- Say less. Land harder.
- Use specifics: numbers, durations, named firms.
- Frame outcomes the CEO actually loses sleep over.
- Write the way you would brief a board.
- Treat Korean and English as equals, not translations.

**Don't**
- "Holistic," "synergy," "tailored solutions."
- Hedged claims. Marketing bombast.
- Three adjectives where one verb would do.
- Promise outcomes you can't measure.
- Translate Korean copy. Write it.

---

## 7. Asset inventory

```
brand/
├── brand-sheet.html              · the living style guide
├── BRAND-GUIDELINES.md           · this document
├── colors.css                    · CSS variables for web
├── logos/
│   ├── pnp-mark.svg              · the dot, alone
│   ├── pnp-logo-horizontal.svg
│   ├── pnp-logo-horizontal-inverse.svg
│   ├── pnp-logo-stacked.svg
│   ├── pnp-logo-korean.svg
│   └── pnp-app-icon.svg
└── favicons/
    ├── favicon.svg               · scalable, modern browsers
    ├── favicon.ico               · 16/32/48 multi-size
    ├── favicon-16.png
    ├── favicon-32.png
    ├── favicon-48.png
    ├── favicon-192.png
    ├── favicon-512.png
    ├── apple-touch-icon.png      · 180px, navy background
    └── og-icon-512.png           · for Open Graph / social cards
```

---

## 8. HTML integration snippet

Drop this into your site's `<head>`:

```html
<link rel="icon" type="image/svg+xml" href="/brand/favicons/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/brand/favicons/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/brand/favicons/favicon-16.png">
<link rel="apple-touch-icon" href="/brand/favicons/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0F2C59">
```
