# Key flows — Gleem

## F1 — First launch → Home

```
Launch
  → W1 → W2 → W3 Welcome (visual-first; see docs/design/welcome.md)
  → Get Started → O4 Unlock (Not now → H3)
  → optional O2 / O3 from Home CTAs when ready
  → H1 or H2 or H3
```

Welcome is **not** full technical setup. Spec: `docs/design/welcome.md`.

## F2 — Return launch (happy path)

```
Launch → H1
  one sentence: You’re protected.
  (lists refresh in background — no UI control)
```

## F3 — Misconfigured

```
Launch → H2
  one sentence names the issue
  one primary CTA → O2 or O3
```

List staleness: only if diagnostics truly needs it — soft line under status, **auto-retry in background**, no button.

## F4 — Breakage

```
More → Pause & Allowances
  or Home quiet link “Something broken?”
→ Pause all  |  Allow website  |  Report
```

## F5 — Purchase / restore

```
H3 / O4 / end of Welcome → Unlock IAP
More → Restore Purchase
```

## F6 — Pack change

```
More → Rule Packs → toggles → apply silently
(no extra confirm chrome unless reload fails)
```
