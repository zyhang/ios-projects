# Gleem design tokens (v1 high-fi)

English product. Minimal, calm, indie utility — not security-theater red, not neon VPN.

## Color

| Token | Light | Usage |
|-------|--------|--------|
| `bg` | `#F4F2EE` | App canvas (warm paper, slight gleam) |
| `bg-elevated` | `#FFFFFF` | Cards, lists, sheets |
| `ink` | `#1A1917` | Primary text |
| `ink-secondary` | `#6B6860` | Meta, captions |
| `ink-tertiary` | `#9C9890` | Hints, “Something broken?” |
| `line` | `rgba(26,25,23,0.08)` | Separators |
| `accent` | `#2C6E5A` | Primary buttons, active toggle (deep calm green) |
| `accent-pressed` | `#245A4A` | Pressed primary |
| `accent-soft` | `rgba(44,110,90,0.12)` | Soft fills |
| `danger-soft` | not used on Home | Avoid alarm red on default states |

Dark mode: defer to v1.1 unless system requirement; high-fi set is **light-first**.

## Type

| Role | Size / weight | Notes |
|------|----------------|-------|
| Status (Home) | 28–34 / Semibold | One sentence, centered |
| Welcome title | 28–32 / Semibold | Short lines |
| Welcome body | 17 / Regular | Secondary ink |
| Nav title | 17 / Semibold | |
| Body | 17 / Regular | |
| Caption | 13–15 / Regular | Tertiary |
| Button | 17 / Semibold | |

Font stack in mockups: `-apple-system, SF Pro, system-ui, sans-serif`.

## Layout

- iPhone frame: 393 × 852 pt content area (mock)
- Side padding: 24–28 pt
- Primary button: full width, 52 pt height, 14 pt corner radius
- List rows: 52–56 pt min height
- Home healthy: vertical center bias for status line

## Motion (intent)

- Welcome: gentle page cross-fade or horizontal slide
- Home state change: fade status text only
- No confetti, no aggressive success animations
