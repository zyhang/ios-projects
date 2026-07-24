# Breakage recovery (v1)

Status: **aligned** — tier B.

## Goal

Zero-config by default, but users must **self-rescue** when something breaks—without custom filter rules.

## In v1

| Capability | Notes |
|------------|--------|
| **Global pause** | Temporarily disable blocking (Safari lists and/or system-wide filter as implemented) with clear “you’re unprotected” state |
| **Per-site allow (Safari)** | Temporary and/or permanent allow for a site that is broken |
| **System-wide guidance** | Status / help explains how to disable URL Filter if an app breaks; be honest if per-app allow isn’t available via API |
| **Optional report** | User-initiated only; minimal fields; anonymous OK; if a URL is included, only the one the user confirms |

## Privacy

- No silent upload of browse history or “sites you visited.”
- Report payload minimized; not tied to background telemetry.
- Aligns with `AGENTS.md` rule 2.

## Out of v1 (candidate later)

- Live Help / remote “known issues” CMS (tier C)
- Element picker, custom rules
- Rich per-app allowlist if OS doesn’t support it cleanly

## UX principles (EN product)

- Recovery actions obvious from the main status surface within one or two taps.
- Prefer plain language: “Pause protection,” “Allow this website,” “Report a problem.”
- Never require an account to report.
