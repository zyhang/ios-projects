# Welcome design — Gleem

Status: **aligned (design direction)**  
Scope: first-launch Welcome only (not Home, not Enable setup, not App Store listing).  
UI language: **English**. Audience: overseas privacy-conscious users (`AGENTS.md` rules 1–2).

Related: [wireframes/screens.md](../wireframes/screens.md) · [hi-fi.html](hi-fi.html) · [tokens.md](tokens.md)

---

## 1. Purpose

Welcome answers one question in ~30 seconds:

> **What is this, and is it worth continuing?**

It must establish:

1. **Category** — ad / tracker blocking (web feels quieter)  
2. **Scope / wedge** — Safari **and** other apps (primary differentiator vs Safari-only tools)  
3. **Trust** — browsing stays on device (required before system permissions and purchase)

It must **not**:

- Tell the full brand story  
- Teach full Settings paths  
- Explain rule packs, list pipelines, or URL Filter / PIR jargon  
- Open with a hard paywall before any value is understood  

---

## 2. Conclusions (best practice for Gleem)

| Conclusion | Rationale |
|------------|-----------|
| **3 pages is enough** | More pages usually restate “we’re good people” with low new information; 3 pages can cover category + scope + trust without fatigue. |
| **Visual-first, one line of copy** | Utility apps convert on glanceable metaphor, not essays. Matches minimal product tone (Wipr-class calm). |
| **Welcome ≠ setup wizard** | Enable Safari / URL Filter belongs in dedicated Enable screens after intent (and usually after unlock). Device-specific Settings copy changes by OS. |
| **Welcome ≠ About** | Independence, “no acceptable ads,” long privacy policy → About / store description. At most *implied* by art on the trust page. |
| **Slightly more than Wipr’s silence** | We are not the incumbent; we need one clear **Safari & apps** signal. We do **not** need three slogan pages. |
| **Skip allowed** | Reinstall / Family Sharing second device should not force a full pitch. |
| **Shown once** (until reset) | Ongoing state lives on Home (“You’re protected.” / “Safari blocking is off.”). |
| **Motion is supportive** | Slow loops that show state change; respect **Reduce Motion** (final calm frame only). |

### Success criteria (what users should leave knowing)

After Welcome, a user should be able to say:

1. It blocks ads / trackers so the web is quieter.  
2. It works in Safari **and** in apps.  
3. It doesn’t collect where they browse.  

Not required at this stage: pricing math, pack names, how to toggle extensions.

---

## 3. Design principles

1. **One idea per page** — no overlapping “trust” monologues across pages.  
2. **Hero visual / light animation carries meaning; headline confirms it.**  
3. **Headline ≤ ~5 words** (English). Prefer **no** body paragraph. Optional micro-line on W2 only, if needed.  
4. **Primary CTA only at the end** of the flow (`Get Started`). Intermediate pages: `Continue`.  
5. **No feature bullet lists** on Welcome.  
6. **No manual list-update messaging** (lists are automatic product-wide).  
7. **Paywall after Welcome** (Unlock sheet / Home locked) — not page 1 of Welcome.  
8. **Calm aesthetic** — warm paper canvas, accent green, no security-theater red, no VPN neon ([tokens.md](tokens.md)).

---

## 4. Recommended scheme: 3 pages

### Overview

| Page | Job | Visual intent | Headline (EN) | CTA |
|------|-----|---------------|---------------|-----|
| **W1** | Category / benefit | Page calms; ad/noise tiles dissolve | **Without the noise.** | Continue |
| **W2** | Scope / wedge | Safari (or browser) mark + app grid, quietly linked | **Safari & Apps.** | Continue |
| **W3** | Trust + next step | Data stays inside device; cloud rejected / no upload | **Stays on your device.** | **Get Started** |

Optional micro under W2 (only if needed): `One purchase. No subscription.` — makes clear one purchase covers Safari **and** apps, with no extra charge.

Page control: dots `● ○ ○` style; optional **Skip** on W1–W2 (lands on Home locked or last page — product choice; default recommendation: Skip → Home / unlock path without re-animating all pages).

### Why this order

1. **Noise first** — universal, emotional, category-clear.  
2. **Safari & apps second** — differentiator while attention is still high; not buried after three philosophy slides.  
3. **Privacy last before action** — sets trust immediately before unlock + system permissions; pairs with `Get Started`.

### What we explicitly dropped from earlier 4-page ideology

| Dropped as own page | Where it goes instead |
|--------------------|------------------------|
| Long “built for you / not advertisers” essay | About, store description; optional art detail on W3 |
| “No acceptable ads” lecture | About / listing |
| Feature bullets (packs, auto lists, not a VPN) | W2 visual implies apps; “not a VPN” on **Enable apps** screen; packs in More |
| Full setup steps | O2 / O3 Enable flows |

---

## 5. Page specs

### W1 — Without the noise.

| Item | Spec |
|------|------|
| **User takeaway** | This makes browsing calmer by removing ads/noise. |
| **Visual** | Stylized content page; ad/noise blocks fade or shrink away in a slow loop. Content lines remain. |
| **Motion** | 2.5–3.5s loop; ease-in-out; no jarring flashes. |
| **Copy** | Title only: `Without the noise.` |
| **Not on page** | Tracker jargon, battery claims, competitor names. |

### W2 — Safari & Apps.

| Item | Spec |
|------|------|
| **User takeaway** | Protection is not Safari-only; apps are included. |
| **Visual** | Two clear poles: browser/Safari metaphor + app icons grid; subtle link or shared “protected” cue between them. |
| **Motion** | Soft float or gentle link emphasis; avoid busy icon spam (4 app tiles max in mock). |
| **Copy** | Title: `Safari & Apps.` · Optional micro: `One purchase. No subscription.` |
| **Not on page** | URL Filter, VPN comparison paragraph, system version requirements (those belong in Help / Enable). |

### W3 — Stays on your device.

| Item | Spec |
|------|------|
| **User takeaway** | Gleem doesn’t harvest browsing; data stays local. |
| **Visual** | Device frame; activity dots stay inside; cloud muted or struck through. |
| **Motion** | Dots pulse in-place; no stream of particles leaving the device. |
| **Copy** | Title only: `Stays on your device.` |
| **CTA** | `Get Started` → Unlock (O4) or deferred Home locked (H3) per commerce flow. |
| **Footer** | Quiet `Privacy Policy` text link OK. |
| **Not on page** | PIR, Bloom filter, legal wall of text (link out only). |

---

## 6. Flow

```
First launch
  → W1 → W2 → W3
       ↘ Skip (optional) ──────────────┐
  → Get Started                        │
  → Unlock (O4)  [Not now → H3]        │
  → Enable Safari / Apps when ready    │
  → Home                               ←┘
```

Rules:

- Welcome **does not** embed full Enable tutorials.  
- Returning users: do not show Welcome again (unless debug / reset).  
- Purchase restore available from Unlock and More — not required on Welcome.

---

## 7. Content that must not appear on Welcome

- Rule pack names and toggles (Core / Annoyances / Strict)  
- Manual “update blocklist”  
- Multi-paragraph independence manifesto  
- Settings breadcrumb tutorials (`Settings → Apps → Safari → …`)  
- Pricing comparisons to Wipr in UI  
- Block counts / fake stats  
- Account signup  

---

## 8. Accessibility & platform

| Topic | Requirement |
|-------|-------------|
| **Reduce Motion** | No looping animation; show final “calm / protected / local” state. |
| **VoiceOver** | Each page: meaningful accessibility label combining title + short image description (e.g. “Illustration: ads fading from a webpage. Without the noise.”). |
| **Dynamic Type** | Title remains one short line; avoid multi-line essays that break layout. |
| **iPad / Mac** | Same 3 ideas and order; larger hero art, same copy. No extra Welcome pages for Mac. |

---

## 9. Implementation notes (product / eng)

- Prefer **vector / Lottie / SwiftUI canvas** over heavy video for size and Reduce Motion.  
- Art should feel **custom and calm**, not stock “shield VPN” clichés.  
- Keep illustration system consistent with [tokens.md](tokens.md) (warm paper, accent green).  
- Copy is **EN-first**; no CN-market onboarding patterns.

---

## 10. Open choices (minor)

| Topic | Default recommendation | Alternate |
|-------|------------------------|-----------|
| Skip control | Show Skip on W1–W2 | No Skip (force 3 pages once) |
| Micro line on W2 | `One purchase. No subscription.` | Omit; rely on Unlock sheet |
| Get Started target | Unlock sheet first | Home locked with Unlock CTA |
| Brand mark on W1 | Optional small Gleem wordmark above art | Title-only, no wordmark |

Resolve during hi-fi polish; none change the **3-page information architecture**.

---

## 11. Revision history

| Date | Change |
|------|--------|
| 2026-07-24 | Initial doc: 3-page visual-first Welcome; conclusions from design discussion; supersedes 4-page text-heavy ideology welcome as product direction. |
| 2026-07-24 | hi-fi.html synced to this spec: dropped the “Built for you.” page, reordered to noise → Safari & apps → on-device, moved `Get Started` / `One purchase. No subscription.` / Privacy Policy to W3, added Skip on W1–W2, pill-style page dots, and reworked hero art + choreographed motion (ads dissolve → content brightens; compass–app grid linked signal; in-device pulse with nothing leaving). Reduced-motion shows the final calm frame. |
| 2026-07-24 | Review fixes in hi-fi: page titles no longer forced uppercase (section-header selector scoped); W1 noise redrawn as a labeled popup + AD banners; W3 shows a dashed upload path into a struck cloud with the dot dissolving en route; W3 micro line renamed `One unlock.` → `One purchase. No subscription.` |
| 2026-07-24 | Copy per review: headline is `Safari & Apps.` (capital A); micro line `One purchase. No subscription.` moved from W3 to W2 — one purchase covers Safari **and** apps, no extra charge. W3 back to title only. |
| 2026-07-24 | Motion review (review-animations skill) fixes in hi-fi: deleted W2 ambient float (link endpoints detached from the floating poles); signal travel matched to the 24px link; W3 rise dot visible window widened (~26–68% of loop); buttons gained `:active` press feedback (`scale(0.97)`, 160ms ease-out). |
