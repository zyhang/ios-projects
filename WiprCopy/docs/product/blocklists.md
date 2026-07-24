# Blocklists (v1)

Status: **aligned** — hybrid curated model (grilling option C).

## Strategy

| Layer | Approach |
|-------|----------|
| Overall | **Curated hybrid**: reputable community lists + our selection, compiled and QA’d by us before ship/update |
| Core | High-quality baseline sources (ads, common trackers, miners, etc.) |
| Annoyances | Annoyance-oriented community sources where license allows |
| Strict | More aggressive sources / rules; higher breakage tolerance |
| Our layer | Exceptions, emergency fixes, product-specific patches on top of upstream |

Do **not** claim “million rules we invented.” Positioning: **carefully curated + continuously fixed**.

## Privacy

- Updates **download rule data only**.
- No upload of browsing history, visited apps, or which rules matched.
- Aligns with `AGENTS.md` rule 2.

## Cadence (working assumption)

- Automatic refresh on the order of **1–2× per week** under normal conditions.
- Hotfix path for severe breakage when needed.
- Diagnostics should surface “lists are stale” without collecting browse data.

## License & attribution

- Before shipping any upstream list: confirm license allows our distribution (in-app and/or remote update).
- English **Acknowledgements** (and privacy policy as needed) list sources.
- Keep a machine-readable manifest in-repo later (source URL, license, which pack).

## Pipeline (implementation intent)

1. Fetch upstream → 2. Filter/transform per pack → 3. Merge our patches → 4. Compile to Safari Content Blocker JSON and URL Filter datasets (Bloom/PIR inputs) → 5. QA sample → 6. Publish update.

Safari and system-wide should stay **semantically aligned** with the same pack toggles where technically possible.

## Non-goals (v1)

- In-app subscription to arbitrary list URLs
- User-edited rules
- Shipping unvetted full upstream dumps without compile/QA
