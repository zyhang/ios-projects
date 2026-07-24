# Screen wireframes — Gleem (v1)

ASCII = structure only. **Minimal chrome.** English UI.  
No tab bar. No manual list-update button.

---

## Visual density (all screens)

- Large breathing room; few elements above the fold  
- Prefer **one** primary button when action is required; zero when healthy  
- Secondary actions: text buttons or More  
- Typography-led; icon only when it earns its place  

---

## Welcome (3 pages) — visual-first

Canonical design doc: **[`docs/design/welcome.md`](../design/welcome.md)**.

First launch only. **3 pages.** Illustration / motion carries meaning; **one headline per page**.

| Page | Visual | Headline | CTA |
|------|--------|----------|-----|
| W1 | Ads/noise dissolve on a page | Without the noise. | Continue |
| W2 | Safari + app grid | Safari & Apps. | Continue |
| | | Optional micro: One purchase. No subscription. | |
| W3 | Data stays on device | Stays on your device. | Get Started |

```
┌─────────────────────────────────┐
│                                 │
│     [ hero art / motion ]       │
│                                 │
│        {one headline}           │
│                                 │
│           ○ ● ○                 │
│   ┌─────────────────────────┐   │
│   │   Continue / Get Started│   │
│   └─────────────────────────┘   │
└─────────────────────────────────┘
```

Notes: Welcome ≠ setup ≠ About. Skip optional. Reduce Motion → static calm frame. Full rules in `welcome.md`.

---

## Home (root — no tabs)

### Shared chrome

```
┌─────────────────────────────────┐
│  Gleem                    More  │  ← text or ••• ; NOT tab bar
│                                 │
│         (main content)          │
│                                 │
└─────────────────────────────────┘
```

### H1 — Protected (ideal default)

```
┌─────────────────────────────────┐
│  Gleem                    More  │
│                                 │
│                                 │
│                                 │
│       You’re protected.         │  ← one line, large
│                                 │
│         Safari · Apps           │  ← quiet meta, optional
│                                 │
│                                 │
│                                 │
│                                 │
│                                 │
│      Something broken?          │  ← text only, low contrast
│                                 │
└─────────────────────────────────┘
```

**No** “Update now”. **No** list age unless we later need a single soft diagnostic line (prefer silence).  
**No** primary button when healthy. Pause lives under More → Pause & Allowances (or long-press/menu if we add later—not required on H1).

Optional even quieter: drop “Safari · Apps” when both on; only show when partial.

### H2 — Needs setup

```
┌─────────────────────────────────┐
│  Gleem                    More  │
│                                 │
│                                 │
│     Safari blocking is off.     │
│                                 │
│   ┌─────────────────────────┐   │
│   │    Enable in Safari     │   │  sole primary
│   └─────────────────────────┘   │
│                                 │
│                                 │
└─────────────────────────────────┘
```

If both Safari and Apps off: one sentence that covers both, or prioritize Safari first then Apps on next visit—**one CTA at a time**.

### H3 — Locked

```
┌─────────────────────────────────┐
│  Gleem                    More  │
│                                 │
│                                 │
│     Unlock to protect           │
│     this device.                │
│                                 │
│   ┌─────────────────────────┐   │
│   │     Unlock Gleem        │   │
│   └─────────────────────────┘   │
│                                 │
│        Restore Purchase         │
│                                 │
└─────────────────────────────────┘
```

### H4 — Paused

```
┌─────────────────────────────────┐
│  Gleem                    More  │
│                                 │
│                                 │
│     Protection paused.          │
│                                 │
│   ┌─────────────────────────┐   │
│   │   Resume protection     │   │
│   └─────────────────────────┘   │
│                                 │
└─────────────────────────────────┘
```

### Home status copy (single sentence)

| State | Line |
|-------|------|
| All good | You’re protected. |
| Safari off | Safari blocking is off. |
| Apps off | App blocking is off. |
| Both off | Gleem isn’t enabled yet. |
| Paused | Protection paused. |
| Locked | Unlock to protect this device. |
| Rare: lists stuck | Protection on. Lists will refresh soon. *(no button)* |

---

## O4 — Unlock (sheet or full screen)

```
┌─────────────────────────────────┐
│                                 │
│     Unlock Gleem                │
│                                 │
│     Safari + apps.              │
│     Rule packs. List updates.   │
│     One purchase — no           │
│     subscription.               │
│                                 │
│   ┌─────────────────────────┐   │
│   │   Unlock — $X.XX        │   │
│   └─────────────────────────┘   │
│                                 │
│     Restore · Not now           │
│                                 │
│     Family Sharing ready.       │
└─────────────────────────────────┘
```

---

## O2 — Enable Safari (minimal steps)

```
┌─────────────────────────────────┐
│  ←                              │
│                                 │
│     Enable in Safari            │
│                                 │
│     Settings → Apps → Safari    │
│     → Extensions → Gleem        │
│                                 │
│   ┌─────────────────────────┐   │
│   │    Open Settings        │   │
│   └─────────────────────────┘   │
│                                 │
│     Done?  [ Continue ]         │
│                                 │
└─────────────────────────────────┘
```

Collapse multi-step into one short instruction block + Open Settings.

---

## O3 — Enable app-wide

```
┌─────────────────────────────────┐
│  ←                              │
│                                 │
│     Enable for apps             │
│                                 │
│     Not a VPN. We don’t see     │
│     your traffic. Works with    │
│     VPNs & Private Relay.       │
│                                 │
│   ┌─────────────────────────┐   │
│   │    Enable               │   │
│   └─────────────────────────┘   │
│                                 │
│     Skip for now                │
│                                 │
└─────────────────────────────────┘
```

---

## M0 — More (list only)

```
┌─────────────────────────────────┐
│  ←  More                        │
│                                 │
│  Rule Packs                  ›  │
│  Pause & Allowances          ›  │
│  Report a Problem            ›  │
│  Help                        ›  │
│                                 │
│  Privacy                     ›  │
│  Acknowledgements            ›  │
│  Restore Purchase            ›  │
│  About Gleem                 ›  │
│                                 │
└─────────────────────────────────┘
```

Grouped with one quiet separator. No icons required in v1 wireframe.

---

## P1 — Rule Packs

```
┌─────────────────────────────────┐
│  ←  Rule Packs                  │
│                                 │
│  Core                      On   │  not a user toggle
│  Essentials. Always on.         │
│                                 │
│  Annoyances              [ ON ] │
│  Nags, banners, sign-up walls   │
│                                 │
│  Strict                 [ OFF ] │
│  Stronger. May break sites.     │
│                                 │
│  Applies to Safari and apps.    │
└─────────────────────────────────┘
```

---

## R1 — Pause & Allowances

```
┌─────────────────────────────────┐
│  ←  Pause & Allowances          │
│                                 │
│  Pause protection        [  ]   │
│                                 │
│  Allowed websites               │
│  example.com                 ✕  │
│  [ Allow a website ]            │
│                                 │
│  App blocking                   │
│  How to turn off app filter  ›  │
│                                 │
└─────────────────────────────────┘
```

---

## R2 — Allow website

```
┌─────────────────────────────────┐
│  Allow website                  │
│  [ domain                     ] │
│  Until I remove it              │
│  [ Allow ]                      │
└─────────────────────────────────┘
```

Keep duration options minimal (one default is enough for v1 if we want even less UI).

---

## R3 — Report

```
┌─────────────────────────────────┐
│  ←  Report                      │
│                                 │
│  Only what you send below.      │
│                                 │
│  What happened?                 │
│  ┌───────────────────────────┐  │
│  │                           │  │
│  └───────────────────────────┘  │
│  Site or app (optional)         │
│  [                           ]  │
│  Email (optional)               │
│  [                           ]  │
│                                 │
│  [ Send ]                       │
└─────────────────────────────────┘
```

---

## S1 — Help

```
┌─────────────────────────────────┐
│  ←  Help                        │
│                                 │
│  Enable Safari               ›  │
│  Enable app blocking         ›  │
│  Pause or allow a site       ›  │
│  Family Sharing              ›  │
│                                 │
└─────────────────────────────────┘
```

Short list; each row opens a sparse step page (same style as O2/O3).

---

## S2 — Privacy

```
┌─────────────────────────────────┐
│  ←  Privacy                     │
│                                 │
│  We don’t collect your          │
│  browsing.                      │
│                                 │
│  Lists update in the            │
│  background without uploading   │
│  where you go.                  │
│                                 │
│  [ Privacy Policy ]             │
└─────────────────────────────────┘
```

---

## S3 — About

```
┌─────────────────────────────────┐
│  ←  About                       │
│                                 │
│  Gleem                          │
│  Block Ads & Trackers           │
│  1.0                            │
│                                 │
│  Independent. On-device.         │
│  No one pays to be unblocked.   │
│                                 │
│  Acknowledgements            ›  │
│  Contact                     ›  │
└─────────────────────────────────┘
```

---

## Mac

- Same root Home + More (menu bar or toolbar trailing).  
- No multi-tab utility window.  
- Welcome can be a simple multi-step panel once.
