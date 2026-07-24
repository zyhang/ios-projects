# Information architecture — Gleem

Low-fidelity. English UI. **Minimal.** iPhone-first; Mac/iPad share the same hierarchy.

## Design principles (nav & chrome)

1. **No tab bar.** One primary surface (Home). Everything else is a **push** from a single secondary entry (Wipr-like **More** / overflow).  
2. **Home is almost empty when healthy** — one status line, optional quiet secondary facts, one primary action only when needed.  
3. **Lists update automatically** — never a manual “Update rules” control on Home (or elsewhere in v1 UI). Stale lists surface only as soft status/diagnostics copy if something is wrong.  
4. **Welcome is 3 pages, visual-first** — category → scope → trust; not a settings dump. See `docs/design/welcome.md`.  
5. **Copy & density** — short sentences, generous space, few buttons. Indie calm, not dashboard.

## Nav model (v1)

```
┌──────────────────────────────────────┐
│  Home  (root, always)                │
│    status · fix/unlock if needed     │
│    [More]  →  list of secondary      │
└──────────────────────────────────────┘
         │
         ▼ push
┌──────────────────────────────────────┐
│  More (plain list)                   │
│    Rule Packs                        │
│    Pause & Allowances                │
│    Report a Problem                  │
│    Help                              │
│    Privacy                           │
│    Acknowledgements                  │
│    Restore Purchase                  │
│    About Gleem                       │
└──────────────────────────────────────┘
```

| Entry | How |
|-------|-----|
| **Home** | Root. No tabs. |
| **More** | Toolbar trailing control, or quiet text button top-trailing (Wipr-style). Not a bottom tab. |
| Deep screens | Standard back-stack from More (or from Home CTAs into setup). |

**Mac:** single window; Home as main; More opens a list or sheet. Optional sidebar later is OK only if it still feels like “one app, one status”—not a multi-module IDE.

```
Gleem
├── Welcome (3 pages, first launch only)
├── Home
│   ├── One-sentence status
│   ├── Safari / Apps (minimal presence indicators — only if useful)
│   ├── Diagnostics line (only if misconfigured / paused / locked)
│   └── Single primary CTA when action required
│         (no “Update lists” button)
│
└── More → …
    ├── Rule Packs
    ├── Pause & Allowances
    ├── Report a Problem
    ├── Help
    ├── Privacy
    ├── Acknowledgements
    ├── Restore Purchase
    └── About Gleem
```

## Screen inventory (v1)

| ID | Screen | How opened |
|----|--------|------------|
| W1–W3 | Welcome pages | First launch |
| H1 | Home — Protected | Root |
| H2 | Home — Needs setup | Root |
| H3 | Home — Locked | Root |
| H4 | Home — Paused | Root |
| O2 | Enable Safari | Home CTA / Help |
| O3 | Enable app-wide | Home CTA / Help |
| O4 | Unlock | Home CTA / Welcome end |
| M0 | More list | Home → More |
| P1 | Rule Packs | More |
| R1 | Pause & Allowances | More / Home “Something broken?” |
| R2 | Allow website | R1 sheet |
| R3 | Report a Problem | More |
| S1 | Help hub | More |
| S2 | Privacy | More |
| S3 | About | More |
| S4 | Acknowledgements | More |

## What Home intentionally omits

- Manual list refresh  
- Block counts / graphs  
- Multi-button action rows when status is healthy  
- Bottom navigation  
