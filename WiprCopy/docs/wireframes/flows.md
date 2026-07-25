# 关键流程 — Gleem

说明语言：中文 · 界面节点文案：英文（与线框一致）。

## F1 — 首次启动 → Home

```
Launch
  → W1 → W2 → W3 Welcome (visual-first; see docs/design/welcome.md)
  → Get Started → O4 Unlock (Not now → H3)
  → optional O2 / O3 from Home CTAs when ready
  → H1 or H2 or H3
```

Welcome **不是**完整技术设置。规格：`docs/design/welcome.md`。

## F2 — 回访启动（开心路径）

```
Launch → H1
  one sentence: You’re protected.
  (lists refresh in background — no UI control)
```

## F3 — 配置未就绪

```
Launch → H2
  one sentence names the issue
  one primary CTA → O2 or O3
```

名单过期：仅当诊断确实需要 — 状态下软文案，**后台自动重试**，无按钮。

## F4 — 破站

```
More → Pause & Allowances
  or Home quiet link “Something broken?”
→ Pause all  |  Allow website  |  Report
```

## F5 — 购买 / 恢复

```
H3 / O4 / end of Welcome → Unlock IAP
More → Restore Purchase
```

## F6 — 改规则包

```
More → Rule Packs → toggles → apply silently
(no extra confirm chrome unless reload fails)
```
