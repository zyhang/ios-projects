# Gleem — 产品需求文档（PRD）

| 字段 | 值 |
|------|-----|
| **状态** | 已对齐（v1） |
| **权威源** | 本文 + 下方链接的专题文档 |
| **Agent 规则** | [`../../AGENTS.md`](../../AGENTS.md)（必须遵守；不替代本 PRD） |
| **文档语言** | **中文**（开发/协作） |
| **界面 / 商店用户可见文案** | **英文**（海外用户） |

**专题深挖**（各自主题内具规范效力，不得与本 PRD 冲突）：

| 文档 | 范围 |
|------|------|
| [naming.md](naming.md) | 应用名、副标题、商店行、品牌语气 |
| [commerce.md](commerce.md) | 免费 + IAP 解锁、Family Sharing、价格政策 |
| [rule-packs.md](rule-packs.md) | Core / Annoyances / Strict 规则包 |
| [blocklists.md](blocklists.md) | 混合策展名单、更新节奏、许可证 |
| [breakage-recovery.md](breakage-recovery.md) | 暂停、按站放行、报错 |
| [url-filter-spike.md](url-filter-spike.md) | 系统级 URL Filter spike 清单 |
| [work-order.md](work-order.md) | 设计先行顺序；spike 并行 |

线框 → [`../wireframes/`](../wireframes/) · 高保真 → [`../design/`](../design/)（**视觉重设计中**）  
v1 视觉归档（非权威）→ [`../archive/design-v1-2026-07-25/`](../archive/design-v1-2026-07-25/)

语言约定见 [`AGENTS.md`](../../AGENTS.md) 规则 0：**PRD/开发文档中文，界面文案英文**。

---

## 1. 一句话定义

**Gleem** — 面向海外用户的隐私优先广告与追踪拦截：Safari + 系统级全 App 拦截、策展规则包、一次解锁。浏览数据留在设备上。

| 字段 | 值 | 状态 |
|------|-----|------|
| **App 显示名** | Gleem | 已锁定 |
| **副标题** | Block Ads & Trackers | 已锁定 |
| 理想/立场文案 | 放商店描述、截图、应用内 About — **不**放副标题 | 见 [naming.md](naming.md) |

营销 one-liner（**英文**，面向用户）：

> Gleem — Block ads and trackers in Safari and across apps. One purchase. Privacy stays on your device.

---

## 2. 受众

- **主受众：** 使用 Apple 设备、重视隐私的用户（美国 / 欧盟 / 其他海外市场）
- 愿意为「开箱即用」的工具一次性付费
- 期望：无广告商交易、无可接受广告后门、名单持续维护

**不为**中国市场支付习惯或国内浏览器生态做优化。Agent/协作者规则：[`AGENTS.md`](../../AGENTS.md) 规则 1。

---

## 3. 隐私原则（产品需求）

与 Wipr 级工具同等信任标准。完整 Agent 规则：[`AGENTS.md`](../../AGENTS.md) 规则 2。

| 要求 | 说明 |
|------|------|
| 浏览留本地 | 访问过的站点/App、被拦截请求等不用于分析、画像或遥测上传 |
| 不采集 | 不收集个人数据与浏览行为（无广告 SDK、无第三方分析、无静默追踪） |
| 优先系统过滤 | Content Blocker、URL Filters — 由系统代为过滤；扩展不必读页面内容 |
| PIR / 基建 | 运营方**不得**得知用户查了什么；禁止可还原浏览历史的日志 |
| 可选报错 | 仅用户主动；字段最小化；不与浏览历史绑定 |
| 冲突处理 | **隐私 / 本地优先 > 功能炫技** |

---

## 4. 定位与已对齐决策

相对极简拦截器（如 Wipr）：同人群略扩——补对方不做或另收费的能力；**不做**正面堆功能的「更重版」。

| 维度 | 决策 |
|------|------|
| 路线 | 同人群略扩：填补缺口 / 打包价值 |
| 主楔子 | **系统级全 App 拦截**（Filtr 级能力；Apple URL Filters） |
| 主赢法 | 系统级过滤**打进基础买断解锁** — 不为该项另设核心 IAP |
| 副楔子 | **内置规则包**（结构 B）：Core 常开 + Annoyances / Strict 可选；**不提供**自由自定义规则 |
| 定价叙事 | 「更便宜」仅作辅助；信任、完整性与维护优先 |
| 商业 | **免费下载 + 一次非消耗型 IAP 全解锁** + **Family Sharing**；见 [commerce.md](commerce.md) |
| 价格政策 | 略低于 Wipr 基础买断（目标约 ≤ $1）；上架前按现价校准；**不以**「便宜」作主卖点 |
| 名单 | 混合策展 **(C)**：社区源 + 自选，自有编译/QA/补丁；见 [blocklists.md](blocklists.md) |
| 破站自救 | 档位 **B**：全局暂停 + Safari 按站放行 + 系统 Filter 关闭指引 + 可选最小化报错；见 [breakage-recovery.md](breakage-recovery.md) |
| 命名方向 | 短工具感 + 常规英文词变体；避免 Wipr/Filtr 仿名与杀毒腔；见 [naming.md](naming.md) |
| 隐私 | 本地优先；不采集浏览；无广告商；无可接受广告 |
| 明确不做 | 以中文/区域深度当差异化；用户自写过滤规则；以低价当品牌主轴；后台浏览遥测；名单更新订阅制 |

---

## 5. MVP（v1 上架门槛）

**能力档 A** — 上线首日兑现主楔子。

### 5.1 范围内

| 领域 | 要求 |
|------|------|
| UI | **英文**界面 + 清晰隐私说明（不采集、本地优先） |
| Safari | Content Blocker，支持名单 / 规则包开关 |
| 系统级 | **URL Filter** 含在基础购买内（iOS / iPadOS / macOS 26+） |
| 规则包 | 结构 **B** — 见 §5.3 与 [rule-packs.md](rule-packs.md) |
| 状态 | 是否启用、名单新鲜度（软诊断）、常见错误配置 |
| 自救 | 档位 **B** — [breakage-recovery.md](breakage-recovery.md) |
| 名单 | 自动更新（技术需要时可有手动）— 只拉取规则；不上传浏览 |
| 平台 | **Universal**：iPhone + iPad + Mac 上架质量达标 |

### 5.2 后置（非 MVP）

- Safari Web Extension（Extra 级）
- 复杂远程报错后台、Live Help CMS
- 拦截统计、Vision Pro 打磨
- 强力按站微调、名单导入、正则编辑器
- 深色模式打磨（高保真以浅色优先）

### 5.3 规则包（v1）

| 包 | 作用 | 默认 | 用户可关？ |
|----|------|------|------------|
| **Core** | 基线广告、常见追踪、挖矿等 | **开** | 否（如有全局暂停则走暂停） |
| **Annoyances** | Cookie 墙、订阅弹窗、装 App 骚扰等（名单级） | **开** | 是 |
| **Strict** | 更激进；更容易破站 | **关** | 是 |

同一套包开关应尽量同时驱动 Safari 与系统级名单（一套心智模型）。v1 无自由自定义规则。详见 [rule-packs.md](rule-packs.md)。

### 5.4 名单

**混合策展 (C)：** 社区优质源 + 自选，经我们编译/QA。各包上游可不同；自有 exception 与热修。约每周 1–2 次刷新。许可证 + 英文 Acknowledgements。详见 [blocklists.md](blocklists.md)。

### 5.5 系统级后端（URL Filters）

**先 spike** — 在 Apple 路径跑通前，不锁定「Filtr 级」上架日期。清单：[url-filter-spike.md](url-filter-spike.md)。

| 默认目标 | Spike/运维过重时的回退 |
|----------|------------------------|
| 自建 **PIR** + 设备端 Bloom 预过滤；名单与可用性自控 | v1 仍保留系统级，但**缩小名单 / 降低刷新频率**；仍含在基础购买内 |

**不得**砍掉主楔子，也不得把系统级降为单独核心 IAP。

Spike 最低成功标准：

1. iPhone 与 Mac 上启用 Filter；系统级拦截已知测试 URL  
2. 预过滤按计划刷新  
3. App 进程无法通过该路径读取用户完整浏览 URL  
4. 主路径可与 VPN / Private Relay 并存  
5. 隐私文案可诚实说明拦截什么、我们永远看不到什么  

### 5.6 商业（v1）

| 项 | 决策 |
|----|------|
| 商店形态 | 免费下载 + **一个**非消耗型 IAP 解锁全部能力 |
| 解锁包含 | Safari + 系统级 + 规则包 + 持续名单更新 |
| Family Sharing | 是（在解锁 IAP 上开启） |
| v1 不做 | 付费下载为主；免费 Safari / 付费系统级拆分；名单更新订阅制 |

详见 [commerce.md](commerce.md)。

---

## 6. 技术约束

| 层 | 约束 |
|----|------|
| Safari | Content Blocker；更深层规则若需要再考虑 Web Extension |
| 系统级 | iOS / iPadOS / macOS 26+ 的 **URL Filters**（非 VPN；可与 VPN / Private Relay 并存） |
| 商业模式 | 独立开发者；持续名单；无广告商关系；无可接受广告后门 |
| 遥测 | 默认关 / 优先不做；名单更新只拉规则 — 永不上传浏览行为 |
| 架构偏好 | 系统负责过滤；App/扩展不为统计或调试去读页面内容 |

---

## 7. UX 产品约束（v1）

对线框与高保真具规范效力（不得漂移）：

| 约束 | 说明 |
|------|------|
| 导航 | **无 Tab**；Home 为根 + **More** push（Wipr 风格） |
| 健康态 Home | 一句状态文案（英文）；几乎无按钮 |
| 名单更新 | 自动；Home（及 v1 UI）**无**手动 Update 控件 |
| Welcome | 3 页、视觉优先（内容结构见线框；视觉稿在 [`../design/`](../design/) 重设计中；v1 见 [归档 welcome](../archive/design-v1-2026-07-25/welcome.md)） |
| 自救 | 从 Home / More 1–2 次点按可达 |
| 文案密度 | 短英文、大留白、少控件 |

屏幕清单与流程：[`../wireframes/`](../wireframes/)。

---

## 8. 开工顺序

**设计先行**（团队习惯）：名称 → 线框 → 视觉 → 完整工程。  
URL Filter spike 与设计**并行**；营销宣称「system-wide」前**必须**通过 spike。

详见 [work-order.md](work-order.md)。

---

## 9. 范围外（摘要）

- 以中文 / 区域深度作为产品差异化  
- 用户自写过滤规则、EasyList 导入 UI、元素选择器（v1）  
- 以大幅低价 /「比 Wipr 便宜」作品牌主轴  
- 后台采集浏览数据  
- 仅为系统级设第二付费 SKU  
- 必须订阅才能更新名单  

---

## 10. 文档地图（Agent / 协作者）

| 需要 | 阅读 |
|------|------|
| 硬性规则（语言、受众、隐私） | [`AGENTS.md`](../../AGENTS.md) |
| 产品决策与 MVP（本 PRD） | **本文** |
| 商业 / 包 / 名单 / 自救 | 文首专题表 |
| UI 结构 | [`../wireframes/`](../wireframes/) |
| 视觉 / Welcome | [`../design/`](../design/)（重设计中） |
| 旧视觉归档 | [`../archive/design-v1-2026-07-25/`](../archive/design-v1-2026-07-25/) |

决策冲突时：**`AGENTS.md` 规则 0–2 > 本 PRD > 专题文档 > 线框/设计**。线框与高保真不得与本文已对齐决策冲突。
