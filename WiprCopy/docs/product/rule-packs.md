# Rule packs (v1)

Status: **aligned** (grilling: structure B).

## Principles

- Default experience works with zero configuration.
- Users choose among **curated packs** only — no custom rules, no list import, no regex UI.
- Toggles are local preferences; never uploaded with browsing data.
- Prefer one set of pack switches for **Safari** and **system-wide** URL Filter outputs.

## Packs

| Pack | Purpose | Default | User can disable? |
|------|---------|---------|-------------------|
| **Core** | Ads, common trackers, crypto miners, baseline junk | On | No (use global pause if we offer it) |
| **Annoyances** | Cookie nags, newsletter modals, app install banners, etc. (where list-level blocking works) | On | Yes |
| **Strict** | More aggressive blocking; may break more sites/apps | Off | Yes (off by default) |

## Non-goals (v1)

- Per-site allow/block UI beyond what OS/Safari already forces us to support for breakage
- EasyList file import / community subscription URLs in-app
- Element picker / cosmetic editor
- Separate “power user” rule language

## Copy direction (EN)

- Core: always-on protection (explain, don’t present as a scary toggle).
- Annoyances: “Fewer pop-ups and nags.”
- Strict: “More blocking — may break some sites. You can turn it off anytime.”
