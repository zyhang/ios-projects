# Stillwall 产品总纲领

> 内部代号 `Gleem`。品牌主名 **Stillwall**。  
> **App Store Name：** `Stillwall for Safari` · **Subtitle：** `Free Ad & Tracker Blocking`（见 D-108/D-109）。  
> 主屏显示名：`Stillwall`。  
> 本文是产品的**总纲领与功能说明**：后续设计稿、交互、工程实现与验收均以本文为准。若与归档方案或口头讨论冲突，以本文及后续已确认决策为准。

**文档状态：** 已确认（grilling 2026-07-27；2026-07-29：商店 Name/Subtitle 锁定）  
**适用范围：** v1（首个可上架 / TestFlight 目标版本）

---

## 1. 文档目的与使用方式

| 读者 | 用法 |
|------|------|
| 产品 / 设计 | 范围、优先级、页面结构、文案边界 |
| 工程 | 能力边界、平台约束、免费/Pro、本地数据与联网 |
| 测试 / 运营 | 成功标准、明确不做、对外承诺边界 |

**冲突处理：**

1. 本文已确认内容优先于竞品参考图与历史归档文档。  
2. 范围变更须先修订本文（或决策记录），再改设计与代码。  
3. 「已完成 / 已验证」仅用于真实实现或测试通过项；未交付能力不得写成既成事实。

---

## 2. 产品定位

**Stillwall 是 iOS 上以 Safari 为中心的广告与追踪拦截产品**，强调少步骤启用、默认可信、无需用户编写规则。

### 2.1 一句话

> Effortlessly block ads, trackers and annoyances in Safari—with powerful Pro tools when you need them.

### 2.2 核心能力方向（v1）

- Safari 广告拦截（Ads）
- 隐私：拦截广告追踪器（Privacy）
- 烦人项拦截（Annoyances，如 Cookie / 隐私弹层等）
- 地区广告规则（Regional Ad Blocking，按语言自动）
- YouTube & X（**仅 Safari 网页**）专项拦截（Pro）
- Battery Boost（Pro）
- Strict Mode（Pro）
- Tap to Block（Pro；在 Safari 中使用）— **扩展侧交互细节：TODO，后续完善**
- **按能力类别的独立开关**（Ads / Privacy / Annoyances / Regional 及各 Pro 能力；**无**全局一键总开关）
- **站点级放行 / 当前站临时关闭：仅在 Safari 扩展中配置**（不在主 App 做名单与定时暂停 UI）— **扩展 UI/流程：TODO，后续完善**
- 规则自动更新

### 2.3 产品理念

| 原则 | 含义 |
|------|------|
| 简单优先 | 目标用户应能一键或极少步骤完成启用并感到「已经在保护」 |
| 少负担 | **不做 Custom Rules 编辑器**；主 App 不堆站点名单与复杂暂停选项 |
| 平台分工 | 遵循 Safari / 扩展能力：Content Blocker 与 Web Extension 的站点相关控制放在 **Safari 扩展侧**；主 App 负责启用、状态、能力类别与订阅 |
| 默认真香 | 免费核心能力默认开启；用户不配置也能受益 |
| 诚实状态 | 未完成系统授权或扩展被关时，不得显示「保护中」 |
| 可恢复 | 误杀时：关闭相关**类别开关**（或 Strict），或在 **Safari 扩展**中放行站点；Help 指向该路径 |
| 性能友好 | **不做**主 App 全局总开关（一键全开/全关会重载整套 blocker，代价过高）；仅按类别开关驱动规则编译 |

---

## 3. 目标用户

**首要用户：** 希望用很少步骤，在 iPhone/iPad 的 **Safari** 上获得广告拦截、基础隐私保护，以及（可选升级后）YouTube/X 网页广告拦截等能力的普通人。

**不是首要用户：**

- 需要自建过滤规则、维护规则列表的高级玩家  
- 以系统级「全 App 去广告」为唯一诉求、且不愿使用 Safari 路径的用户（v1 不提供）  
- 期望原生 YouTube/X App 完全无广告的用户（v1 **不承诺**）

**首发语言与市场：** 产品 UI 与商店文案以 **英文** 为主（具体国家列表可在发布计划中细化）。

---

## 4. 商业模式与权益

### 4.1 定价

| 项 | v1 决策 |
|----|---------|
| 形式 | 仅 **年订阅** |
| 价格 | **$14.99 / 年** |
| 试用 | **1 个月**免费试用 |
| 家庭共享 | **支持** Family Sharing |
| 月订阅 | 不做 |
| 终身买断 | 不做 |

### 4.2 免费 vs Pro

| 能力 | 层级 | 默认 | 说明 |
|------|------|------|------|
| Ads | 免费 | 开 | Safari 常见广告；**独立开关** |
| Privacy | 免费 | 开 | 广告追踪器；**独立开关** |
| Annoyances | 免费 | 开 | Cookie / 隐私提示等烦人项；**独立开关** |
| Regional Ad Blocking | 免费 | 开 | 按**系统语言**全自动，无手动选区负担；**独立开关** |
| 规则日更 / 后台更新 | 免费 | 自动 | 不单独做用户开关 |
| 站点放行 / 当前站控制 | 免费 | — | **仅 Safari 扩展 UI**；主 App **不**做 Allowed Sites 列表 |
| 多设备 | 免费权益 | — | 同一 **Apple ID** 下多台 iPhone/iPad；**无设备席位费** |
| Mac | 路线图 | — | **Coming soon**；不另售设备授权；**非 v1 交付** |
| YouTube & X Ad Block | **Pro** | 关（未订阅） | **一个合并开关**；仅 Safari 网页 |
| Battery Boost | **Pro** | 关（未订阅） | 见功能说明 |
| Strict Mode | **Pro** | **关** | 更激进；可能影响站点 |
| Tap to Block | **Pro** | — | Home 为**入口行**（说明如何在 Safari 使用） |
| ~~全局保护开关~~ | — | — | **v1 不做**（性能：整包重载代价过高；见 D-315） |

### 4.3 多设备与 Pro 的表述（防挖坑）

- **免费核心拦截**在完成系统授权后即可使用，不依赖试用或付费。  
- **同一 Apple ID** 登录的设备共享免费能力；**Pro 随 Apple 订阅 / 家庭共享**在同一 ID 体系下生效，不按台收费。  
- **不是**自建账号「买一次给任意设备」；无产品账号体系。  
- Mac 仅可在营销/路线中写 Coming soon，**不得**在 v1 写成已支持。

### 4.4 升级路径

- 首次启动 **不以**全屏付费墙作为进入 App 的条件。  
- 用户点击 Pro 能力（或升级入口）时进入升级页：卖点 + **1 个月试用** + **$14.99/年** + Family Sharing 说明。  
- 免费用户完整可用：Ads / Privacy / Annoyances / Regional 各类别开关 + Safari 扩展内站点控制。

---

## 5. 功能说明（总纲领级）

以下定义供设计与开发共用。实现细节（规则源、API）在工程文档细化，但**不得突破**本节边界。

### 5.1 Ads（免费）

- **做什么：** 拦截常见展示广告、明显广告位及相关请求，减少 Safari 内广告干扰。  
- **不做什么：** 不承诺「所有广告 100% 消失」；不覆盖系统内其他 App 的原生广告。

### 5.2 Privacy（免费）

- **做什么：** 拦截广告追踪器与常见跨站跟踪脚本，减轻「全网被广告跟」的感受。  
- **不做什么：** 不是 VPN；不隐藏 IP；不做完整反指纹产品。

### 5.3 Annoyances（免费）

- **做什么：** 拦截或抑制恼人的 Cookie 同意条、部分隐私提示、常见 newsletter / 干扰层等（以规则能力为限）。  
- **不做什么：** 不保证全部网站弹层消失。

### 5.4 Regional Ad Blocking（免费）

- **做什么：** 按用户**系统语言（及合理地区信号）自动**启用对应地区/语言的广告规则补充。  
- **不做什么：** 不提供「选国家当节点」式配置；v1 **无**地区设置页；用户零配置。

### 5.5 YouTube & X Ad Block（Pro，合并开关）

- **做什么：** 在 **Safari 网页版** YouTube 与 X 上提供专项广告/推广拦截增强。  
- **不做什么：** **不承诺**官方 YouTube / X 原生 App 去广告。对外文案须带 **in Safari**（或等价清晰限定）。

### 5.6 Battery Boost（Pro）

- **做什么：** 拦截加密挖矿脚本、明显不必要的耗电后台脚本等，以改善浏览能效。  
- **不做什么：** 不是 iOS 系统省电模式；不承诺具体续航百分比。

### 5.7 Strict Mode（Pro）

- **做什么：** 在用户已开启的拦截类别之上，**叠加**更激进的规则集。  
- **默认：** 关闭。  
- **风险：** 可能造成个别站点异常；恢复路径见 §5.9 / §5.10（关 Strict 或相关类别，或在 Safari 扩展中放行站点）。  
- **不做什么：** 不是自定义规则编辑器，不是开发者模式。

### 5.8 Tap to Block（Pro）

> **交互规格：** [design/safari-extension.md](../design/safari-extension.md)（popup 第 2 项；页内点选）。主 App 仅保留说明入口（S05）。

- **做什么：** 用户在 Safari 扩展中点 **Tap to Block**，在当前页点选元素进行屏蔽。  
- **Home 形态：** **入口行**——说明能力 + 如何在 Safari 打开扩展使用；不是仅一个无解释的 Switch。  
- **未订阅：** 扩展内不拉起 IAP；引导 **Open Stillwall** 至主 App 升级页。  
- **数据：** 用户点选产生的规则 **仅存本机**；无云同步；卸装/清数据可能丢失。  
- **与理念关系：** 允许「点一下屏蔽」的轻量个性化，**仍不提供**通用 Custom Rules 编辑器。  
- **待验证：** 点选交互与系统限制见 V-005。

### 5.9 无全局保护开关（主 App；v1 明确不做）

- **不提供** Home 顶部「一键开/关全部拦截」的全局 Switch。  
- **原因：** 全局切换会触发整套 Content Blocker / 规则管道重载，**性能代价过高**；细粒度类别开关更可控。  
- **用户如何停拦：**  
  1. 关闭相关**类别开关**（Ads / Privacy / … / Strict 等）；或  
  2. 在 **Safari 扩展**对本站 **Pause on this site**。  
- **不做**「暂停 15 分钟 / 1 小时 / 直到手动恢复」等定时 Pause UI（主 App）。  
- **Home：** 不展示保护中 / 已关闭状态；顶部仅用中性价值文案，类别开关直接表达用户选择。
- **扩展：** popup 仍不提供全局开关；当主 App 内**全部类别均为 Off** 时，顶栏显示 Off in app 并可引导回主 App。

### 5.10 站点放行与当前站控制（免费，仅 Safari 扩展）

> **交互规格：** [design/safari-extension.md](../design/safari-extension.md)。主 App **不做** Allowed Sites / 定时 Pause。

- **做什么：** 在扩展 popup 第 1 项对本站 **Pause on this site** / **Resume on this site**（同一槽位切换）。  
- **作用域：** eTLD+1（`www` 与裸域同一站）。  
- **持久化：** 直到用户 Resume（无时长选项）。  
- **主 App：** **不提供** Allowed Sites 列表页、不提供 App 内「Allow this site」管理、不提供定时 Pause。  
- **扩展 popup 常态仅 3 项：** ① Pause/Resume this site · ② Tap to Block · ③ Report issue（只读顶栏不算项）。  
- **Help / Tap 说明：** 指向 Safari 中打开 Stillwall 扩展；系统入口路径以 V-002 验证后文案为准。  
- **数据：** 扩展侧本地；不上传浏览历史。

### 5.11 规则更新（免费，自动）

- **做什么：** 定期/后台更新拦截规则，扩大覆盖、修复漏拦与误杀。  
- **原则：** 默认静默；失败时不得导致「界面显示保护中但规则已空/损坏」的假保护；不因普通更新失败阻断已有可用保护（内置基线规则策略由工程细化）。  
- **隐私：** 可联网下载规则包；**不上传**浏览历史。

### 5.12 开关与运行状态的逻辑关系

1. **未完成 Safari 拦截授权：** 不得进入 Home；以模态/引导完成授权（见流程）。  
2. **仅类别开关驱动拦截：** 无全局总开关；仅已开启的 Ads / Privacy / Annoyances / Regional / Pro 类别参与拦截。  
3. **工程派生值（不作为 Home 视觉状态）：**
   - `anyCategoryEnabled = true`：至少一个会参与拦截的类别开关为 On。
   - `anyCategoryEnabled = false`：所有类别开关均为 Off（无有效拦截）；用于规则管道与扩展顶栏诚实呈现。
   - Home 始终使用同一页面、同一中性标题，不切换 `On / Off` 版本。
4. **Strict Mode：** 叠加在当前已开启类别上，不替换 Ads/Privacy 等开关。  
5. **站点例外：** 仅扩展侧；主 App 不维护名单 UI。  
6. **YouTube & X / 扩展能力：** 依赖系统中 Content Blocker 与 Web Extension 处于可用状态；被系统关闭时必须可被发现并引导恢复。

---

## 6. 平台与技术边界

| 项 | v1 决策 |
|----|---------|
| 设备 | iPhone、iPad |
| 最低系统 | **iOS / iPadOS 26** |
| 浏览器 | **仅 Safari** |
| 拦截形态 | **Safari Content Blocker（必做）** + **Safari Web Extension（必做）** |
| Web Extension 用途 | YouTube & X 行为、**popup 3 项**（本站 Pause/Resume、Tap to Block、Report issue）等；规格见 [design/safari-extension.md](../design/safari-extension.md) |
| 主 App 职责 | 引导授权、能力类别开关、状态呈现、订阅、帮助/反馈/关于 |
| VPN | **不使用** |
| 系统级跨 App 过滤 | **v1 不做**；若未来做，走 **iOS 系统提供的 Filter 方案（非 VPN）** |
| Apple TV | 不做 |
| Mac 客户端 | 非 v1；Coming soon |
| 原生 YouTube / X App | 不承诺去广告 |

**架构暗示（非实现规格）：** 主 App（SwiftUI）负责状态、引导、类别开关与订阅；扩展共享最小必要状态（如 App Group）；站点例外优先落在扩展/Safari 侧能力，避免在主 App 重复造名单系统。

---

## 7. 信息架构与页面流程

### 7.1 总体结构

**不使用 Tab Bar。** 主界面为单 Home + 次级页。

```text
App
├── Welcome（首次）
├── Safari 授权引导（门禁；未完成则模态拦截）
├── Home
│   ├── 中性价值文案（无状态、无全局开关）
│   ├── 能力列表（类别开关 + Tap 入口行）
│   └── 其他入口
├── 升级 / 订阅页（从 Pro 能力进入）
└── 其他
    ├── Privacy Policy
    ├── Website
    ├── About
    ├── Feedback
    ├── Help（含：站点设置请在 Safari 扩展中完成）
    └── 订阅管理 / Restore 等
```

**主 App 不做：** Allowed Sites 页、Pause 时长 sheet、App 内网站名单管理。

### 7.2 首次启动

```text
首次启动
  → Welcome：1 个长页（顶标题/理念 · 中滚动卖点 · 底主按钮）
  → 开启 Safari 拦截（一次叙事：Content Blocker + Web Extension）
  → 校验授权
        · 是 → Home（默认免费类别开）
        · 否 → 不得进 Home；模态引导
```

**Welcome 内容原则：** 同前——禁止未交付能力；主 CTA 为启用 Safari，非强制试用。

### 7.3 Home

| 区域 | 要求 |
|------|------|
| 上：价值文案 | `A quieter Safari, on your terms.` + `Choose what stays out of your way.`；不随类别状态切换 |
| 中：能力列表 | 见下表（改顺序须先改本文）；**唯一**开/关入口 |
| 其他 | More |

**能力列表顺序（v1）：**

1. Ads  
2. Privacy  
3. Annoyances  
4. Regional Ad Blocking  
5. YouTube & X（Pro）  
6. Battery Boost（Pro）  
7. Strict Mode（Pro）  
8. Tap to Block（Pro，**入口行**）

未订阅时 Pro 行 → 升级页。  
扩展或 Content Blocker 被关：不得显示保护中；模态拉回授权。

### 7.4 其他

至少包含：Privacy Policy、Website、About、Feedback、Help。  
Feedback：用户主动；可选手动附域名；发送前预览。

---

## 8. 隐私与数据

| 项 | 决策 |
|----|------|
| 账号 | **无**产品账号 |
| 浏览历史 / 访问 URL | **不收集、不上传**（Feedback 用户可选域名除外） |
| 第三方分析 / 广告 SDK | **不使用** |
| 规则更新 | 允许联网下载；不上传访问记录 |
| 类别开关 / Tap 规则 | **仅本机** |
| 站点例外 | 扩展侧本地；主 App 不维护名单库 |
| 订阅 | StoreKit；依赖 Apple ID |
| 崩溃统计 | v1 不接第三方崩溃 SDK |

**对外信任句方向：**

> We don’t collect your browsing history. No account required.

---

## 9. v1 明确不做

| 不做 | 说明 |
|------|------|
| **主 App 内 Allowed Sites / 网站名单管理** | 站点控制在 Safari 扩展 |
| **主 App 定时 Pause（15m / 1h / Until resume）** | 需要临时放行时用扩展 Pause 本站，或关闭相关类别开关 |
| **主 App 全局保护总开关** | 性能：整包 blocker 重载代价过高；仅保留类别级开关（D-315） |
| Custom Rules 编辑器 | 与简单理念冲突 |
| 系统级 / 全 App 广告拦截 | 含 VPN；v1 仅 Safari |
| Apple TV 客户端 | — |
| Mac 客户端交付 | 仅 Coming soon |
| 原生 YouTube / X App 无广告承诺 | — |
| 云同步规则 / 名单 | 无账号 |
| 第三方分析与广告 SDK | — |
| 月订阅、终身买断 | — |
| 首次强制付费墙才能用免费拦截 | — |
| Performance Insights 看板 | — |
| 多 Tab Dashboard | — |
| 「2.0× / 省电 XX%」作验收事实 | — |

---

## 10. 成功标准（v1）

### 10.1 体验

1. 新用户能以较少步骤完成 Safari 授权并进入 Home，默认免费类别已开启。
2. 默认开启 Ads/Privacy/Annoyances/Regional 后，预定站点上广告与追踪明显改善。  
3. 用户能用 **各类别开关** 关闭/打开对应拦截；站点例外路径在 Help 中可找到（Safari 扩展），**不**要求主 App 内名单；**无**全局总开关。

### 10.2 商业

4. Pro 入口清晰；试用 1 个月、$14.99/年、Family Sharing 表述正确。  
5. 未订阅用户完整可用全部免费能力。

### 10.3 信任

6. 行为与 Privacy Policy 及 §8 一致。

### 10.4 工程底线

7. 规则可更新；失败不造成假保护。  
8. 系统关闭扩展/Content Blocker 时能发现并引导，不显示虚假「保护中」。

---

## 11. 统一术语

| 术语 | 含义 |
|------|------|
| 主 App | 用户打开的 SwiftUI 应用 |
| Content Blocker | Safari 内容拦截扩展（声明式规则） |
| Web Extension | Safari 网页扩展（YouTube/X、Tap to Block、站点控制等） |
| Safari 保护 | 上述扩展共同提供的 Safari 内拦截能力 |
| 类别开关 | 主 App Home 能力列表中的 Ads / Privacy / … 独立开关（**无**全局总开关） |
| Pro | 订阅解锁的能力集合 |
| 站点放行 | 在 **Safari 扩展**中对站点停止拦截；非主 App 功能 |
| 规则包 | 经更新通道下发的拦截规则集合 |
| 门禁 | 未完成必要授权则不可进入 Home |

---

## 12. 关联文档

| 文档 | 内容 | 状态 |
|------|------|------|
| 本文 | 总纲领与功能说明（范围真相源） | 已确认 |
| [decisions/decision-log.md](../decisions/decision-log.md) | 已确认 / 待验证 / 暂缓决策 | 已建立 |
| [design/app-flow.md](../design/app-flow.md) | 完整流程与状态机 | 已建立 |
| [design/user-flows.md](../design/user-flows.md) | IA 与关键用户流程 | 已建立 |
| [design/screens.md](../design/screens.md) | 分屏说明（主 App + SE 扩展） | 已建立 |
| [design/safari-extension.md](../design/safari-extension.md) | Safari 扩展 popup / 状态 / 3 项规格 | **已建立** |
| Lunacy 高保真 / 线框 | 见 `docs/design/*.free` | 以仓库文件为准；扩展画板待补 |
| `docs/engineering/*` | Targets、规则管道、StoreKit | 待建 |

---

## 13. 修订记录

| 日期 | 说明 |
|------|------|
| 2026-07-27 | 首版总纲领：基于产品 grilling 共享理解落稿 |
| 2026-07-27 | 关联决策记录与 design 流程/页面文档 |
| 2026-07-27 | **当时方案（后被 D-315 替代）**：主 App 仅全局 On/Off；移除 App 内 Pause 时长与 Allowed Sites；站点控制归 Safari 扩展 |
| 2026-07-27 | 标记 **Safari 扩展侧工作为 TODO**（§14），主 App 文档与线框优先 |
| 2026-07-28 | **扩展 popup 固定 3 项**；规格见 [safari-extension.md](../design/safari-extension.md)；§5.8–5.10 / §14 收敛 |
| 2026-07-29 | App Store Name `Stillwall for Safari` · Subtitle `Free Ad & Tracker Blocking`（D-108/D-109） |
| 2026-07-29 | **移除主 App 全局保护开关**（D-315，当时保留的只读状态区后被 D-316 替代）：恢复路径 = 关类别 / 扩展 Pause |
| 2026-07-29 | **合并 Home On/Off**（D-316）：Home 使用中性价值文案；全部类别 Off 不形成独立页面 |

---

## 14. Safari 扩展侧：规格与剩余工作

**产品规格（已确认）：** [design/safari-extension.md](../design/safari-extension.md)

| 常态菜单（仅 3 项） | 说明 |
|--------------------|------|
| Pause / Resume on this site | 免费；eTLD+1；持久至 Resume |
| Tap to Block | Pro；页内点选 |
| Report issue | 免费；预填域名 |

| ID | 事项 | 状态 | 备注 |
|----|------|------|------|
| T-EXT-01 | 扩展 popup / 菜单 IA | **已确认** | 固定 3 项；见专项文档 |
| T-EXT-02 | 当前站 Pause / Resume | **已确认（产品）** | 实现与 CB 同步待工程 |
| T-EXT-03 | Tap to Block 扩展内流程 | 产品已定骨架 | 点选/撤销/失败；**V-005** |
| T-EXT-04 | YouTube & X 扩展侧行为与权限 | TODO | 与 Content Blocker 分工；**无** popup 第四项 |
| T-EXT-05 | 扩展线框 / 高保真 | **线框已画** | Lunacy `Stillwall-Wireframes-v1.free` ROW 4；蓝图见 [extension-wireframes-se.md](../design/extension-wireframes-se.md) |
| T-EXT-06 | 扩展 ↔ 主 App 状态同步（App Group 等） | schema 已定 | [engineering/safari-extension.md](../engineering/safari-extension.md)；代码待做 |
| T-EXT-07 | Help「去 Safari 扩展」完整引导 | TODO | 依赖 **V-002** 系统路径 |

**已决边界（摘要）：**

- 主 App：中性 Home + 类别开关 + 订阅 + 引导门禁（**无**全局总开关、无 On/Off 状态区）。
- 扩展 popup：仅 3 项；无全局开关、无类别列表、无 IAP。  
- 不做：主 App 全局总开关、主 App 定时 Pause、主 App Allowed Sites、paywall bypass。
