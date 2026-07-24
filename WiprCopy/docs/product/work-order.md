# Preferred work order

Status: **aligned** with team habit.

## Sequence

1. **Name / brand** — product name, one-liner, tone ✅ (Gleem / Block Ads & Trackers)  
2. **Wireframes** — IA, key flows (`docs/wireframes/`) ✅ first pass  
3. **Visual design** — high-fi, icon direction (`docs/design/`) ✅ hi-fi HTML + tokens (icon TBD)  
4. **Engineering** — app shell, IAP, blockers, lists, URL Filter  
5. **URL Filter spike** — may start in parallel with (2)–(3); **must pass before** marketing “system-wide” as shipped  

## Why this order

- Matches how this team prefers to work (identity and UX first).  
- Design still bound by locked product decisions in `AGENTS.md` / `overview.md` (privacy, packs, recovery, commerce).  
- Technical risk on URL Filters is real: do not let polish replace the spike; run it alongside design so launch isn’t blocked at the end.

## Design constraints (do not drift)

- English-first, overseas users (`AGENTS.md` rule 1)  
- Privacy-local, no browse collection (`AGENTS.md` rule 2)  
- Main status: protection on/off, list freshness, misconfig  
- Rule packs: Core / Annoyances / Strict  
- Recovery: pause, per-site allow, report  
- Unlock: free app + one IAP for everything including system-wide  
