# Product overview

## Name

| Field | Value |
|-------|--------|
| **Name** | **Gleem** |
| **Subtitle** | **Block Ads & Trackers** (locked) |

## One-liner

**Gleem** — Privacy-first ad & tracker blocking for overseas users: Safari + system-wide app blocking, curated rule packs, one unlock. Browsing stays on device.

## Audience

- Primary: privacy-conscious users on Apple devices (US / EU / other overseas markets)
- Willing to pay once for a tool that “just works”
- Expect no ad deals, no “acceptable ads,” ongoing blocklist maintenance

**Not** optimized for Chinese market payment habits or domestic browser usage patterns. See `AGENTS.md` rule 1.

## Privacy principles (non-negotiable)

Same trust bar as Wipr-class tools. See `AGENTS.md` rule 2.

- **Browsing stays local.** Visited sites/apps and blocked requests are not uploaded for analytics, profiling, or “product improvement” telemetry.
- **The app does not collect** personal data or browsing behavior (no ad SDKs, no third-party analytics, no silent tracking).
- Prefer system APIs where the **OS filters on our behalf** and extensions need not read page content (Safari Content Blockers, URL Filters).
- Where infrastructure is required (e.g. URL Filters + PIR), use privacy-preserving paths so operators **cannot learn** what the user looked up; never log reconstructable browsing history.
- Optional issue reports only when the user initiates them; minimize fields; no binding to browsing history.
- When privacy conflicts with a feature: **privacy wins** (e.g. no block stats that require reading browsing data unless a fully on-device, zero-upload design exists).

## Positioning (vs. minimal blockers like Wipr)

| Dimension | Decision |
|-----------|----------|
| Path | Same audience, slight expansion—fill gaps / pack-in value, not a heavier feature dump |
| Primary wedge | **System-wide app blocking** (Filtr-class; Apple URL Filters) |
| Win condition | System-wide filtering **included in base paid unlock**—not a core separate IAP |
| Secondary wedge | **Built-in rule packs** (presets on/off); **no** freeform custom rules |
| Pricing story | “Cheaper” is secondary; trust, completeness, and maintenance come first |
| Privacy | Local-first; no browsing collection; no ad deals; no “acceptable ads” |
| Commerce | **Free download + one non-consumable IAP** (all features) + **Family Sharing**; price **slightly under Wipr base** (≤~$1); system-wide in that IAP; do not lead with “cheap” |
| Explicit non-goals | Regional/Chinese depth as differentiator; user-written filter rules; race-to-bottom pricing as brand; background browsing telemetry; list-update paywall subscription |

## MVP (v1 ship bar)

**Capability: A** — deliver the primary wedge on day one.

| In v1 | Deferred |
|-------|----------|
| English UI + clear privacy copy (no collection, local-first) | Safari Web Extension (Extra-class) |
| Safari Content Blocker (lists / rule-pack toggles) | Advanced remote issue backend, Live Help |
| System-wide **URL Filter** (included in base purchase) | Block statistics, Vision Pro polish |
| Rule packs (structure **B**) — see below | Per-site tweaks, import lists, regex editor |
| Status: enabled?, list freshness, common misconfig diagnostics | — |
| Breakage recovery **B**: global pause, per-site allow (Safari), filter disable guidance, optional report | Live Help CMS |
| List auto/manual update (rules fetch only; no browse upload) | — |

### Rule packs (v1)

| Pack | Role | Default |
|------|------|---------|
| **Core** | Baseline ads, common trackers, miners, etc. | **On** — not user-removable (pause-all is separate if needed) |
| **Annoyances** | Cookie walls, newsletter prompts, “get the app” nags (list-level) | **On** |
| **Strict** | More aggressive; higher break risk | **Off** |

Same pack toggles should drive Safari and system-wide lists where applicable (one mental model). No freeform custom rules in v1.

### Blocklists

**Hybrid curated (C):** community sources + our selection, compiled/QA’d by us. Packs may use different upstream mixes; we own exceptions and hotfixes. Refresh ~1–2× weekly. Licenses + English acknowledgements required. Details: [blocklists.md](blocklists.md).

**Platform:** Universal — **iPhone + iPad + Mac** all supported at ship (team can hold Mac quality).

### System-wide backend (URL Filters)

**Decision: spike first (option 5).** Do not lock a hard store launch date on “Filtr-class” until the Apple sample path works.

| Default target | Fallback if spike/ops too heavy |
|----------------|----------------------------------|
| Self-hosted **PIR** + on-device Bloom prefilter pipeline; we control lists and availability | Keep system-wide in v1 but **smaller list / lower refresh cadence**; still included in base purchase |

Privacy bar unchanged: operators must not learn what the user looked up; no reconstructable browse logs.

**Spike success criteria (minimum):**

1. Enable filter on iPhone and Mac; block known test URLs system-wide  
2. Prefilter refresh works on a schedule  
3. App process cannot read full user browse URLs via this path  
4. Coexists with VPN / Private Relay on the primary path  
5. Privacy copy can honestly state what is blocked and what we never see  

## Technical constraints

- **Safari**: Content Blocker; Web Extension if deeper rules are needed
- **System-wide**: URL Filters on iOS / iPadOS / macOS 26+ (not a VPN; works alongside VPN / Private Relay)
- Independent developer model: ongoing lists, no advertiser relationships
- List updates fetch rules only; no browse-behavior upload

## Work order

**Design-first** (team preference): **name → wireframes → visuals**, then full engineering. URL Filter spike should run **in parallel or immediately after** naming/wireframes start—not deferred until after polish. See [work-order.md](work-order.md).

## Design assets

- Wireframes → [`../wireframes/`](../wireframes/)
- High-fidelity → [`../design/`](../design/)
