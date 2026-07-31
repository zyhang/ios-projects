# 页面说明（v1）

> 供线框 / 高保真 / 实现对照。逻辑见 [app-flow.md](app-flow.md)；范围见 [产品总纲领](../product/product-charter.md)。  
> 视觉 token 与组件规格见 [design-system.md](design-system.md)。  
> **界面文案：英文。**

---

## 约定

| 项 | 说明 |
|----|------|
| 导航 | 无 Tab；Home 为根（授权通过后） |
| 主 App 不做 | Allowed Sites 页、Pause 时长 sheet、App 内网站名单 |
| 站点控制 | Safari 扩展 popup（**固定 3 项**） |
| Pro 行 | 未订阅 → Upgrade |
| 扩展规格 | [safari-extension.md](safari-extension.md) |

---

## S01 — Welcome

| 项 | 说明 |
|----|------|
| 布局 | 单长页：顶标题/理念 · 中滚动卖点 · 底主按钮 |
| 主 CTA | **Set Up in Safari** → S02（**D-510 锁定**；弃用 *Set Up Safari Protection* / *Enable Safari Blocking*） |
| 禁止 | 主 CTA 为强制 Free Trial；未交付能力卖点 |

卖点池：Safari Ad Blocking、Privacy、Annoyances、Regional、YouTube & X（Pro/in Safari）、Battery/Tap（Pro）、Daily updates、Devices（Mac coming soon）。  
跨页副文案锁定（含 Strict Large Type）见 `issues/005-cross-screen-consistency`（**D-510**）。

---

## S02 — Setup（Safari Protection）

| 项 | 说明 |
|----|------|
| 目的 | 一次说清并完成 Content Blocker + Web Extension |
| 门禁 | 未完成不得进 Home；运行时丢失则模态 |
| 认知减负 | **[setup-first-run.md](setup-first-run.md)**（step2 名称清单） |

结构：标题、说明、**三步**列表、主按钮 Open Settings、手动路径 hint、等待权限提示。

| # | 步骤 | 要点 |
|---|------|------|
| 1 | Open Settings | Apps → Safari → Extensions |
| 2 | Turn on Stillwall | **6** 个 Content Blockers（Ads, Privacy, Annoyances, Social, Other, Security）+ Stillwall Web Extension 全开；**下方静态名称清单**（见 setup-first-run） |
| 3 | Allow website access | Web Extension → **Allow All Websites** |

深链：优先尝试打开系统 Extensions；失败时展示**指导性**手动路径（非恐吓式硬错误）。详见 `issues/003-setup-open-settings`。

---

## S03 — Home

| 项 | 说明 |
|----|------|
| 目的 | 中性价值文案 + **能力类别开关** + More（**无**全局总开关、无 On/Off 页面变体） |

### 顶部文案

```text
A quieter Safari, on your terms.
Choose what stays out of your way.
```

文案不随类别开关状态切换。**不做：** Home On/Off 变体、保护状态 pill、全局总开关、Pause 按钮、Allowed Sites 入口、15m/1h/Until resume。

### 能力列表（顺序固定）

| # | 行 | 控件 | 默认 |
|---|-----|------|------|
| 1 | Ads | Switch | On |
| 2 | Privacy | Switch | On |
| 3 | Annoyances | Switch | On |
| 4 | Regional Ad Blocking | Switch | On（副文案：auto by language） |
| 5 | YouTube & X | Switch · Pro | Off |
| 6 | Battery Boost | Switch · Pro | Off |
| 7 | Strict Mode | Switch · Pro | Off |
| 8 | Tap to Block | Chevron 行 · Pro | → S05 |

全部类别 Off 时列表与顶部文案均保持不变，仅无拦截生效；Safari 扩展顶栏负责诚实显示 `Off in app`。

规则重编译时可用底部非阻塞进度（**英文**）：`Updating filters` / `Preparing blockers for Safari…`（见 `issues/002-filter-progress-copy`）。

### 其他

右上角 More → S06。

---

## S04 — （已移除）

原 Allowed Sites / empty **不再作为主 App 页面**。  
站点放行在 **Safari 扩展** 中完成；线框中相关画板删除或标为 obsolete。

---

## S05 — Tap to Block（说明）

| 项 | 说明 |
|----|------|
| 内容 | 1–3 步：在 Safari 打开 Stillwall 扩展 → 点 **Tap to Block** → 点选页面元素 |
| 补充 | 一句：To pause blocking on a site, use **Pause on this site** in the extension |
| 未订阅 | 预览 + Upgrade CTA |

---

## S06 — More

Help · Feedback · About · Privacy Policy · Website · Restore · Manage Subscription。  
无账号、无 Allowed Sites 行。

---

## S07 — Help

> **权威英文正文：** [engineering/ui-copy-en.md](../engineering/ui-copy-en.md) §7 · issue **009**。

| 条目标题 | 语义要点 |
|----------|----------|
| How to enable protection | `Set Up in Safari`；**6 CB + Web Extension** + Allow All Websites；Home **无** On badge |
| Site broken? | 优先扩展 **Pause on this site**；备选关类别/Strict；Resume 恢复 |
| How to open the extension | 中性「在 Safari 打开 Stillwall 扩展」；**勿**写死未验证图标路径（V-002） |
| YouTube & X | Safari websites only |
| Tap to Block | 扩展第 2 项；Pro；规则本机 |
| Send feedback | App Feedback 或扩展 **Report issue** |

**禁止：** Home shows On · `Set Up Safari Protection` · *both extensions* 作为唯一描述  

---

## S08 — Upgrade / Paywall

利益：YouTube & X in Safari、Battery Boost、Strict Mode、Tap to Block。  
价格：`One month free, then $14.99/year` + Family Sharing（优先 StoreKit 本地化价；**不得**展示 $9.99）。  
主按钮：Start 1 Month Free Trial。  
用户**取消**系统购买表：不展示错误（勿露出 `Request Canceled`）。  
非首次进 Home 门禁。详见 `issues/004-pro-pricing-and-cancel-ux`。

---

## Safari 扩展页面（SE）

> 完整规格：[safari-extension.md](safari-extension.md)。Lunacy 待画。

### SE01 — Extension popup（常态）

| 项 | 说明 |
|----|------|
| 顶栏 | 当前 host + 状态（Protected / Paused / …），只读 |
| **仅 3 个可点项** | ① Pause on this site **或** Resume on this site · ② Tap to Block · ③ Report issue |
| 禁止 | 全局开关、类别列表、第 4 个常驻项、IAP |

变体：

| ID | 场景 |
|----|------|
| SE01 | Protected → 槽 1 = Pause on this site |
| SE01a | Paused → 槽 1 = Resume on this site |
| SE01b | Not enabled → 降级单 CTA：Open Stillwall |

### SE02 — Tap to Block（页内点选）

Pro；从 SE01 槽 2 进入。失败提示、可撤销上一次。未订阅不进入本页，走 Open Stillwall。

### SE03 — Report issue

类型：Site broken / Still seeing ads / Other；域名预填可编辑；发送前预览。

---

## S09 — Feedback

类型 · 描述 · 可选附域名 · 发送前预览 · Send。

---

## S10 — About

App 版本 · 规则包版本 · 定位句 · Acknowledgements · Mac coming soon（可选）。

---

## 屏幕优先级

| 优先级 | 屏幕 |
|--------|------|
| P0 | S01、S02、S03、S08 |
| P1 | S05、S06、S07、S09、S10 |
| — | S04 主 App 页面取消 |

---

## 设计稿检查清单

- [x] 无 Tab Bar  
- [x] Welcome CTA ≠ 强制试用  
- [x] Setup 门禁  
- [x] Home：**仅类别开关**（无全局总开关），无 Pause/Allow 入口  
- [x] 能力顺序：Ads → Privacy → Annoyances → Regional → YT&X → Battery → Strict → Tap  
- [x] Tap 为入口行  
- [x] YouTube/X 含 in Safari  
- [x] 无 Custom Rules / 全 App 拦截卖点  
- [x] $14.99/年 · 1 月试用 · Family Sharing  
- [x] 站点名单不在主 App  
- [x] 视觉规范文档：[design-system.md](design-system.md)（对齐 Depth Pass · Hi-fi P0）
