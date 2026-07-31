# UI 英文文案源（v1 · 工程实现）

> **单一事实源（App 内用户可见英文）。** 与 D-510、`issues/005`、`screens.md` 对齐。  
> 实现：建议 `Localizable.xcstrings` / String Catalog；本文件为仓库权威对照。  
> **本仓库当前无 Swift 源码**；接入主工程时以本文 + 产品总纲领为准。

**状态：** 2026-07-31 已按 Journey polish + 001–009 锁定  

---

## 1. Welcome（S01）

| Key | 文案 |
|-----|------|
| `welcome.title` | `A quieter Safari.` |
| `welcome.subtitle` | `Ads, trackers, and everyday annoyances stay out of your way.` |
| `welcome.cta` | **`Set Up in Safari`** |
| `welcome.footer` | `No account required · Core Safari protection is free` |

**弃用 CTA：** `Set Up Safari Protection` · `Enable Safari Blocking`

### Welcome 卖点行（营销可略软，边界须诚实）

| 标题 | 副文案 |
|------|--------|
| Safari ad blocking | Fewer ads and distractions |
| Privacy | Block trackers. We don’t collect history. |
| Annoyances | Quiet cookie banners and noisy prompts |
| Regional Ad Blocking | Automatic rules for your language |
| YouTube & X in Safari | Pro · Not the native apps |
| Battery Boost | Pro · Reduce wasteful browsing scripts |
| Strict Mode | Pro · Stronger blocking · Use with care |
| Tap to Block | Pro · Hide page elements in Safari |

Large Type 短式（可选）：Privacy 保留 trackers 语义，例如 `Block trackers · No history collected`（勿只剩 history 一句）。

---

## 2. Setup（S02）· issue 003

| Key | 文案 |
|-----|------|
| `setup.title` | `Enable Stillwall in Safari` |
| `setup.subtitle` | `Safari needs six Stillwall Content Blockers plus the Web Extension. Turn them all on, then allow website access.` |
| `setup.step1.title` | `Open Settings` |
| `setup.step1.detail` | `Apps → Safari → Extensions` |
| `setup.step2.title` | `Turn on Stillwall` |
| `setup.step2.detail` | `Enable all 6 Content Blockers and the Web Extension` |
| `setup.step3.title` | `Allow website access` |
| `setup.step3.detail` | `Choose Allow on All Websites` |
| `setup.cta` | `Open Settings` |
| `setup.return_hint` | `Come back when you’re done — Stillwall continues automatically.` |
| `setup.privacy_title` | `Private by design` |
| `setup.privacy_body` | `Your browsing stays on your device.` |
| `setup.deep_link_hint` | `If Settings didn’t open, go to: Settings → Apps → Safari → Extensions` |

**禁止：** *both extensions* · 未完成时顶 emblem 常驻「已完成」金勾 · 恐吓式红/橙错误作为默认深链失败态  

**可选增强：** step2 列出六类 CB 短名（Ads, Privacy, Annoyances, Social, Other, Security）+ Web Extension。

---

## 3. Home（S03）· issue 001 / 005

| Key | 文案 |
|-----|------|
| `home.hero_title` | `A quieter Safari, on your terms.` |
| `home.hero_subtitle` | `Choose what stays out of your way.` |

**禁止：** 顶部 On/Off pill · `Safari Protection` 状态标题 · 全局总开关  

### 能力行（标准 / Large Type 短式）

| 行 | 标准副文案 | Large Type 短式 |
|----|------------|-----------------|
| Ads | Reduce ads and visual clutter | Reduce ads and visual clutter |
| Privacy | Block common advertising trackers | Block common trackers |
| Annoyances | Hide cookie banners and noisy prompts | Hide cookie banners and prompts |
| Regional Ad Blocking | Automatic by language | Automatic by language |
| YouTube & X | Block YouTube & X ads in Safari | YouTube & X ads in Safari |
| Battery Boost | Reduce wasteful browsing scripts | Reduce wasteful scripts |
| Strict Mode | Stronger blocking · Use with care | Stronger blocking · Use with care |
| Tap to Block | Hide page elements in Safari | Hide page elements in Safari |

**Strict Large Type 禁止：** `May affect some sites`

Regional 与 YouTube & X 之间 **+8pt**；Free 行无领先图标；Pro 行暖金 `PRO` badge。

### 规则进度 · issue 002

| Key | 文案 |
|-----|------|
| `filter_progress.title` | `Updating filters` |
| `filter_progress.subtitle` | `Preparing blockers for Safari…` |
| `filter_progress.failed` | `Couldn’t update filters. Try again.` |

视觉：底部品牌软提示条（`brandSoft`），非中文、非告警橙。

---

## 4. Upgrade（S08）· issue 004

| Key | 文案 |
|-----|------|
| `upgrade.title` | `Unlock Stillwall Pro` |
| `upgrade.subtitle` | `Stronger blocking and finer control — all in Safari.` |
| `upgrade.offer_title` | `1 month free` |
| `upgrade.offer_detail` | `Then $14.99/year · Family Sharing included` |
| `upgrade.offer_cancel` | `Cancel anytime in Apple subscriptions.` |
| `upgrade.cta` | `Start 1 Month Free Trial` |
| `upgrade.restore` | `Restore Purchases` |
| `upgrade.legal` | `Payment is charged to your Apple ID after the trial. Terms · Privacy` |

利益行副文案 = §3 Pro 四行**标准**列（Battery 用完整句）。

**StoreKit：** 价格优先 Product 本地化；fallback **$14.99** 不得 $9.99。  
**取消购买：** 静默，勿展示 `Request Canceled` / 原始 `localizedDescription`。

---

## 5. Tap to Block 说明（S05）

```text
Title: Tap to Block
Body steps:
1. In Safari, open the Stillwall extension.
2. Tap Tap to Block.
3. Select page elements to hide.

Footer: To pause blocking on a site, use Pause on this site in the extension.
Free CTA: Unlock with Stillwall Pro → Upgrade
```

---

## 6. More（S06）

行（顺序建议）：

`Help` · `Feedback` · `About` · `Privacy Policy` · `Website` · `Restore Purchases` · `Manage Subscription`

无账号行、无 Allowed Sites。

---

## 7. Help（S07）· issue 009

### How to enable protection

```text
1. Open Stillwall and tap Set Up in Safari.
2. In Settings, turn on all Stillwall Content Blockers and the Stillwall Web Extension.
3. Allow website access (Allow All Websites).
4. Return to Stillwall. Home shows category controls—not an On/Off protection badge.
```

### Site broken?

```text
Open the Stillwall extension in Safari and choose Pause on this site.
Or turn off the related category switches (or Strict Mode) in the app.
When you’re ready, choose Resume on this site in the extension.
```

### How to open the extension

```text
In Safari, open the Stillwall extension from the browser’s extensions controls.
Exact placement can vary by iOS version—follow the path shown during Setup if needed.
```

### YouTube & X

```text
Pro blocking works on YouTube and X websites in Safari only—not the native apps.
```

### Tap to Block

```text
With Stillwall Pro, open the extension → Tap to Block, then select elements on the page.
Rules stay on this device.
```

### Send feedback

```text
Use Feedback in the app, or Report issue in the Safari extension (domain prefilled).
```

**可选（产品确认后）：** 首次进 Home 一次性 tip：  
`Tip: If a site looks wrong, open the Stillwall extension in Safari and choose Pause on this site.`

---

## 8. Feedback / About（S09–S10）

| 屏 | 要点 |
|----|------|
| Feedback | 类型 · 描述 · 可选域名 · 发送前预览 · Send |
| About | 版本 · 规则包版本 · 定位句 · Acknowledgements · Mac coming soon（可选） |

信任句方向：`We don’t collect your browsing history. No account required.`

---

## 9. Safari 扩展 popup（SE）

| 状态 / 项 | 文案 |
|-----------|------|
| Protected | `Protected` |
| Paused | `Paused` |
| Off in app | `Off in app` |
| Not enabled | `Not enabled` |
| E-01 | `Pause on this site` / `Resume on this site` |
| E-02 | `Tap to Block` |
| E-03 | `Report issue` |
| Not enabled CTA | `Open Stillwall` |

无扩展内 IAP。

---

## 10. 实现检查清单（对接 001–005 实机漂移）

| Issue | 代码动作 |
|-------|----------|
| **001** | 删除 Home 状态 pill / Safari Protection 标题；固定 §3 hero |
| **002** | 进度条改 §3 filter_progress；去掉中文硬编码 |
| **003** | Setup 用 §2；深链失败 → hint 非 error |
| **004** | ASC/StoreKit $14.99；cancel 静默 |
| **005** | 全表单 key 引用；Strict LT 不另写 |
| **009** | Help 用 §7 |

工程接入后：真机对照 `issues/*/before` 与 Hi-fi `docs/design/exports/phone-preview/` 做四屏连滑验收。
