# App Store 提审资料包（v1）

> **状态：** 基础资料已定稿（grilling 2026-07-28）。  
> **对外名：** Stillwall（暂用；[V-001](../decisions/decision-log.md) 商标/重名/域名未通过前可整包替换）。  
> **内部代号：** Gleem。  
> **权威产品范围：** [product-charter.md](../product/product-charter.md)。  
> **视觉：** [design-system.md](../design/design-system.md)。

| 项 | 值 |
|----|-----|
| 本包版本 | 2026-07-28 |
| 商店语言 | English (U.S.) only |
| 销售地区 | 全球可售（ASC 默认排除地区除外） |
| 下载价格 | **Free**（功能通过 IAP 升级） |
| 设备 | Universal：iPhone + iPad（最低 iOS/iPadOS 26） |

**上架前硬门禁（未完成不得点 Submit）：**

- [ ] V-001：商标 / App Store 重名 / 域名  
- [ ] V-003：StoreKit 试用 1 个月 + $14.99 年 + Family Sharing 在 ASC 配通  
- [ ] V-004：规则源许可与 About 归因  
- [ ] Privacy / Support URL **可公网访问**（host 替换占位域名）  
- [ ] 法务主体名写入 Copyright（替换 `<LEGAL_ENTITY_NAME>`）  
- [ ] Bundle ID 中 `<org>` 替换为真实团队段  
- [ ] 真机：Content Blocker + Web Extension 启用路径与截图一致（V-002）  

---

## 1. 身份与命名

| 字段 | 内容 | 限制 |
|------|------|------|
| **App Name** | `Stillwall` | ≤30；本轮权威名 |
| **Subtitle** | `Ad Block for Safari` | 19 字符 |
| **CFBundleDisplayName**（主屏） | `Stillwall` | 与商店名一致 |
| **SKU** | `stillwall-ios` | Connect 内部 |
| **Bundle ID（主 App）** | `com.<org>.stillwall` | 上架前替换 `<org>` |
| **Content Blocker** | `com.<org>.stillwall.blocker` | 建议 |
| **Web Extension** | `com.<org>.stillwall.extension` | 建议 |
| **Copyright** | `© 2026 <LEGAL_ENTITY_NAME>` | 与 ASC 卖方主体一致 |
| **Primary Category** | **Utilities** | 副类本轮不填 |
| **Age Rating** | 目标 **4+**；非 Made for Kids | 以 ASC 问卷生成为准 |

### 1.1 更名波及面（V-001 失败时）

需替换：App Name、Display Name、IAP 展示名、截图标题条中的品牌词、图标若含字标、隐私/Support 页标题、工程 Bundle 产品段（若已用 stillwall）。

---

## 2. 商店文案（English U.S.）

完整可复制文本见 [app-store-assets/copy/](app-store-assets/copy/)。

| 字段 | 内容 |
|------|------|
| **Promotional Text** | `Free Safari ad blocking. Pro adds YouTube & X in Safari, Tap to Block, and more.`（80 字符；可随时改） |
| **Keywords** | `adblock,blocker,tracker,privacy,cookie,ads,filter,browsing,annoyance,youtube`（76 字符） |
| **Description** | 见 `copy/description-en-US.txt` |
| **What’s New（1.0）** | 见 `copy/whats-new-1.0-en-US.txt` |

**Keywords 原则：** 核心意图优先；不重复 Name/Subtitle 已有词堆砌；不承诺全 App / 原生 YouTube 去广告。

---

## 3. 链接约定

| 用途 | URL 约定 | 本轮状态 |
|------|----------|----------|
| **Privacy Policy** | `https://<domain>/privacy` | 文案见 `copy/privacy-policy-en-US.md`；host 待 V-001 |
| **Support** | `https://<domain>/support` | 文案见 `copy/support-en-US.md` |
| **Marketing**（可选） | `https://<domain>/` 或 `/product` | **域名未定时 Connect 可先留空** |

提交前三条（Privacy 必填、Support 强烈建议）必须 **HTTPS 可打开**。

---

## 4. 订阅（In-App Purchase）

| 项 | 值 |
|----|-----|
| 类型 | Auto-Renewable Subscription |
| **Reference Name** | `pro_yearly_1499` |
| **Product ID** | `com.<org>.stillwall.pro.yearly`（建议） |
| **Display Name** | `Stillwall Pro (Yearly)` |
| 价格 | **$14.99 / year**（ASC 对应价位） |
| 试用 | **1 month** free |
| Family Sharing | **On** |
| 月订 / 终身 | **不做** |
| 付费墙句（App 内与商店一致） | `One month free, then $14.99/year` + Family Sharing |

**订阅说明（Description 与审核用，英文）：**

见 description 文末 Subscription 段；须符合 App Store 订阅披露要求（时长、价格、续订、取消方式）。

---

## 5. App Privacy（营养标签）

**口径 B（已锁定）：** 仅申报用户**主动** Feedback 相关数据。

| 数据类型（建议） | 联动用户 | 用途 | 追踪 |
|------------------|----------|------|------|
| Contact Info（若表单含邮箱）或 Other User Content（描述、可选域名） | Yes（用户填写） | Customer Support / App Functionality | **No** |
| 浏览历史 / 精确位置 / 广告数据 / 第三方分析 | — | **不收集** | — |

**不申报：** 分析、广告 SDK、崩溃第三方 SDK（D-603 / D-606）。

实现须与申报一致：Feedback 上自有后端时仅处理支持请求，不用于画像追踪。

---

## 6. 出口合规

- 仅使用 **豁免/标准加密**（HTTPS、系统 TLS、StoreKit）。  
- **无**自研非豁免加密。  
- Info.plist 常见：`ITSAppUsesNonExemptEncryption` = **NO**（以法务/账号实际问答为准）。

---

## 7. 图标

| 项 | 说明 |
|----|------|
| 方向 | 品牌绿底 `#2F6A58` + 浅绿圆盘 `#EAF3EF` + 深绿 shield-check |
| 主文件 | [app-store-assets/icon/AppIcon-1024.png](app-store-assets/icon/AppIcon-1024.png) |
| 备选 | `AppIcon-1024-alt-soft.png`（浅绿底） |
| 旧版备份 | `AppIcon-1024-prev.png` |
| 尺寸 | 另含 20…180、512 等常用 PNG；`AppIcon-size-preview.png` 小尺寸检视 |
| 规范 | 1024×1024、RGB、**无透明**、**不要**自带圆角（系统遮罩） |

**Apple craft 优化（2026-07-28）：** 去掉同心装饰环（小尺寸失效）；顶光渐变材质；圆盘轻阴影与高光；盾形比例与更粗对勾；4× 超采样再缩放。

---

## 8. 截图

### 8.1 序列（浅色主套，带短英文标题条）

| # | 画面 | 标题条建议 |
|---|------|------------|
| 1 | Home · On | `All quiet in Safari` |
| 2 | Welcome | `A quieter Safari` |
| 3 | Setup | `Enable in a few steps` |
| 4 | Home 能力列表 | `Block ads, trackers, annoyances` |
| 5 | Upgrade | `Pro tools when you need them` |
| 6（可选） | Home · Off | `One switch. Full control` |

源 UI：[design/exports/phone-preview/](../design/exports/phone-preview/)。

### 8.2 尺寸义务

| 设备 | 要求 |
|------|------|
| **iPhone 6.7" / 6.9"** | 首发必交（以 ASC 当前必填槽为准） |
| **iPad 13"** | Universal 必交最小套（可用同序列适配） |
| Dark / Large Type | 可选，不占首发主套 |

### 8.3 不做

- App Preview 视频（v1）  
- 夸大「全网/全 App 去广告」、原生 YouTube/X App 无广告画面  

合成带标题条的最终 JPG/PNG 可后续用脚本从 phone-preview 生成；清单见 [screenshot-plan.md](app-store-assets/screenshot-plan.md)。

---

## 9. App Review 备注（模板）

见 [copy/review-notes-en-US.txt](app-store-assets/copy/review-notes-en-US.txt)。

要点：

1. No account / login.  
2. Free path validates blocking after Safari extensions enabled.  
3. Step-by-step: Settings → Safari → Extensions → enable Stillwall (Content Blocker + Web Extension).  
4. Safari only; not a VPN; not system-wide blocking.  
5. Pro optional; sandbox subscription OK to skip for core review.  

**Demo account：** N/A — No account required.

---

## 10. 版本与构建

| 项 | 建议 |
|----|------|
| Version | `1.0.0` |
| What’s New | 首发功能列表（英文） |
| 构建 | Xcode Archive → Upload → 选构建提审 |

---

## 11. 规则源与第三方内容（V-004）

- 上架前完成许可证与归因核对。  
- About → Acknowledgements 列出规则源。  
- 商店 Description **不**点名未授权列表品牌。  
- Review Notes 可写：filter lists are licensed; attributions available in-app.

---

## 12. Connect 填写检查清单

### 12.1 App Information

- [ ] Name / Subtitle / Category / Content Rights  
- [ ] Age Rating 问卷 → 4+ 目标  
- [ ] Privacy Policy URL 可访问  

### 12.2 Pricing

- [ ] Free  
- [ ] 销售地区：全球（按策略）  

### 12.3 In-App Purchases

- [ ] `pro_yearly_1499` 年订 + 1 月试用 + Family Sharing  
- [ ] 订阅本地化英文 Display Name / Description  
- [ ] 审核截图（付费墙）可选附上  

### 12.4 App Privacy

- [ ] 按 §5 申报 Feedback 相关；无追踪  
- [ ] 无分析/广告 SDK  

### 12.5 Version

- [ ] 描述 / 关键词 / 促销文本  
- [ ] 截图 iPhone（+ iPad）  
- [ ] 无 Preview 视频  
- [ ] Review Notes  
- [ ] 构建号  

### 12.6 工程

- [ ] Bundle IDs / App Groups 与扩展一致  
- [ ] 加密合规声明  
- [ ] 图标 Asset 使用 1024 主图  

---

## 13. 文件索引

| 路径 | 说明 |
|------|------|
| [app-store-submission.md](app-store-submission.md) | 本总览 |
| [app-store-assets/copy/](app-store-assets/copy/) | 可复制商店文案 |
| [app-store-assets/icon/](app-store-assets/icon/) | App Icon PNG |
| [app-store-assets/screenshots/iphone-6.7/](app-store-assets/screenshots/iphone-6.7/) | 商店成片 iPhone（带标题条） |
| [app-store-assets/screenshots/ipad-13/](app-store-assets/screenshots/ipad-13/) | 商店成片 iPad |
| [app-store-assets/screenshot-plan.md](app-store-assets/screenshot-plan.md) | 截图规格与标题 |
| [app-store-assets/site/](app-store-assets/site/) | Privacy / Support 静态站（可部署） |
| [app-store-assets/asc-field-checklist.md](app-store-assets/asc-field-checklist.md) | ASC 字段速填表 |
| [grilling-decisions-2026-07-28.md](grilling-decisions-2026-07-28.md) | 决策记录摘要 |

---

## 14. 明确禁止写进商店的内容

- 原生 YouTube / X App 去广告承诺  
- 系统级 / 全 App / VPN 拦截  
- 不可验证的威胁计数或「省电 XX%」验收式数字  
- Custom Rules 编辑器、Mac 已交付、Apple TV  
- 首次强制付费才能用免费拦截  
