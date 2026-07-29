# 设计原则与视觉规范（v1）

> **现行权威。** 视觉 token、组件与动效以本文 + Lunacy 高保真为准。  
> 范围与交互逻辑仍服从 [产品总纲领](../product/product-charter.md) 与 [决策记录](../decisions/decision-log.md)。  
> 页面结构见 [screens.md](screens.md)；流程见 [app-flow.md](app-flow.md)。

| 项 | 说明 |
|----|------|
| 视觉源 | Lunacy：`Depth Pass · Hi-fi P0` / 仓库 [Stillwall-HiFi-v1.free](Stillwall-HiFi-v1.free) |
| 线框 | [Stillwall-Wireframes-v1.free](Stillwall-Wireframes-v1.free)（结构，非视觉权威） |
| 对外品牌 | Stillwall（内部代号 Gleem） |
| App Store | Name `Stillwall for Safari` · Subtitle `Free Ad & Tracker Blocking` |
| 说明语言 | 中文；**用户可见 UI 字符串：英文** |
| 归档旧稿 | [archive/…/design-system.md](../archive/project-v1-2026-07-27/design/design-system.md) 勿作现行权威 |

---

## 1. 设计目标与人格

体验差异不来自更多卡片、图表或开关，而来自用户在几秒内确认：

1. 我现在是否受到保护。  
2. 如果没有生效，下一步该做什么。  
3. 如果页面异常，如何快速恢复。

> Stillwall should feel calm because it is working—not busy because it wants to prove it.

### 应呈现

- 安静、可信；原生 iOS 分组列表感  
- 现代但不追逐装饰潮流；轻量、反应迅速  
- 隐私透明，不制造恐惧  
- 默认设置经过判断，不把复杂度推给用户  

### 应避免

- 大面积盾牌、锁、雷达、警报符号  
- 威胁计数、「已阻止 N 个威胁」等不可验证数字  
- 密集 dashboard、环形图、霓虹/赛博安全风  
- 为展示动效而延迟状态反馈  
- 单屏多个竞争主按钮  

---

## 2. 一句话视觉定义

> **iOS Settings 式分组列表 + 系统灰分组底 + 单一森绿主色（`#2F6A58`）+ 系统绿开关 + 暖金 Pro 标记；少阴影、少装饰、单主 CTA、文案冷静诚实。**

HIG notes（稿内）：

> Brand `#2F6A58` identifies primary action and protection; warm gold is reserved for Pro.

---

## 3. 画板与布局

| 项 | 规范 |
|----|------|
| 参考画板 | **390 × 844**（iPhone 逻辑尺寸；设备圆角示意 47） |
| 内容水平 inset | **16** → 列表/按钮宽 **358** |
| 文案区 inset | 常 **20** 或 **32** |
| 导航 | **无 Tab Bar**；授权通过后 **Home 为根** |
| 列布局 | iPhone 单列；iPad 限制内容最大宽度，不拉成多列 dashboard |
| 结构 | 顶：中性价值文案 → 中：白卡片分组；Home 无状态控件，类别 Switch 在列表内 |
| 触控 | 可点目标 **≥ 44×44 pt**（稿中 More/Close 约 48×44） |

### 间距常用值

| Token 意图 | 值 |
|------------|-----|
| 行内 gap（文案 ↔ 控件） | **12** |
| 列表行 padding | **16** 水平；垂直 **8 / 10 / 12 / 14**（随双行内容） |
| Hero 内部 spacing | **10–12** |
| 卡片内 stack | **2–4**（标题与副文案） |
| 分隔线 | 高 **0.33**；色见 §4 |

---

## 4. 色彩（语义 Token）

实现时用语义名，禁止在业务视图里散落魔法色值。Hex 为 Light 默认；Dark 见对照表。

### 4.1 品牌与状态

| Token | Light | Dark | 用途 |
|-------|-------|------|------|
| `brandPrimary` | `#2F6A58` | `#2F6A58`（可保持） | 主按钮、保护语义、图标强调 |
| `brandSoft` | `#EAF3EF` | 深底上略提亮的绿灰 | Header emblem 底、轻量强调面 |
| `brandSoftAlt` | `#E9F2EE` / `#E5EFEB` / `#DDECE5` | 对应压暗 | 隐私条、Pro 行图标底、步骤附属 |
| `brandDeepText` | `#244F42` | 浅绿灰字 | 「Private by design」等品牌正文 |
| `protectionOn` | `#34C759` | `#34C759` | UISwitch On、状态 pill 圆点 |
| `protectionOnLabel` | `#248A3D` | 浅绿 | Status pill「On」文字 |
| `protectionOnPillBg` | `#34C759` @ ~14% | 同色低透明 | On 状态胶囊底 |
| `proBadgeBg` | `#FFF4D6` | `#3A301C` | PRO 徽标底 |
| `proBadgeBorder` | `#EAC97C` | `#8A6A2D` | PRO 边 0.75pt |
| `proBadgeText` | `#7A5316` | `#F4D58B` | PRO 字 |
| `link` | `#007AFF` | 系统 label / tint | Restore Purchases 等 |

**暖金仅用于 Pro。** 主 CTA 与保护状态只用森绿，不与 Pro 金混用。

### 4.2 表面与文字

| Token | Light | Dark | 用途 |
|-------|-------|------|------|
| `surfaceGrouped` | `#F2F2F7` | `#1C1C1E` | 页面分组灰底 |
| `surfaceElevated` | `#FFFFFF` | `#2C2C2E` | 列表卡、步骤卡、Offer 卡 |
| `textPrimary` | `#000000` | `#F5F5F7` | 标题、列表主文案 |
| `textSecondary` | `#3C3C43` @ **0.60–0.72** | `#A8A8AD`（常再 ×0.65） | 副标题、说明、footer |
| `separator` | `#3C3C43` @ ~15–25% | 同系半透明 | 行分隔 |
| `controlChrome` | `#787880` @ ~6–8% | 同系 | More 等弱按钮底 |
| `switchOffTrack` | 系统灰（约 `#E9E9EA`） | `#3A3A3C` | UISwitch Off |

### 4.3 画布 / 设计稿标注（非 App UI）

Lunacy 画布底 `#E8E6E1`；章节标题 `#1C1B19` 等——**不要**写进 App token。

### 4.4 对比与无障碍

- 支持 Light / Dark；对比目标 **WCAG AA**  
- 状态不得只靠颜色：On/Off 同时有 pill 文案 + Switch + 标题语义  
- Reduce Transparency 下边界仍可辨（依赖表面色差，非仅靠模糊）

---

## 5. 字体与字号

| 项 | 规范 |
|----|------|
| 设计稿 | Inter（Regular / SemiBold / Bold） |
| **实现** | **SF Pro / 系统字体 + Dynamic Type**；勿打包 Inter 作 UI 正文字体 |
| 标题 | 不用全大写装饰标题 |
| 数字 | 版本号等可读即可；需对齐时用法向等宽数字特性 |

### 字号阶梯（逻辑 pt，对齐 Dynamic Type 语义）

| 角色 | 字重 | 字号 | SwiftUI 建议 | 用途 |
|------|------|------|--------------|------|
| Large Title | Bold | 34 | `.largeTitle.weight(.bold)` 或自定义 | Home / Upgrade 主标题 |
| Title | Bold | 28–32 | `.title` / `.title2` | Welcome 口号、Setup 标题 |
| Price | Bold | 20 | `.title3.weight(.bold)` | 「1 month free」 |
| Body / Row | Regular | 17 | `.body` | 列表主标题、状态说明 |
| CTA | SemiBold | 17 | `.body.weight(.semibold)` | 主按钮文案 |
| Subhead | SemiBold / Regular | 15 | `.subheadline` | 隐私标题、Offer 副行 |
| Caption | Regular | 13 | `.footnote` / `.caption` | 行副文案、footer、法律字 |
| Badge | Bold | 10.5–11 | 固定小字 + 动态放大策略 | `PRO` |

副文案惯例：使用 `textSecondary`，**优先 opacity 0.65**，而不是另起一套硬编码灰。

---

## 6. 圆角与材质

| 元素 | 圆角 (pt) |
|------|-----------|
| 主列表卡 / 卖点区 / Setup 步骤卡 | **18** |
| 主按钮 CTA | **12** |
| More 弱按钮 | **14** |
| Offer / Pro benefits 卡 | **10** |
| Setup 步骤序号底 | **10** |
| Pro 行图标底 | **8** |
| Pro badge | **7** |
| Status pill | **20**（胶囊） |
| Header emblem（72×72） | **36**（正圆） |
| 隐私 reassurance 条 | **16** |

### 材质与阴影

- 层级靠 **`surfaceGrouped` + `surfaceElevated`**，不是大阴影卡片  
- 阴影几乎只用于 **UISwitch 拇指**（约 radius 3, y:1, black 19%）  
- 透明/模糊仅表达层级（如 Welcome 底栏 fade）；不把整页做成 glass 品牌  
- 产品人格来自排版、留白与状态，不来自 Liquid Glass 装饰  

---

## 7. 核心组件

### 7.1 Value Hero（Home）

| 区 | 内容 |
|----|------|
| 左列 | 34 Bold `A quieter Safari, on your terms.` → 17 Regular `Choose what stays out of your way.` |
| 右 | **无状态、无控件**（**无**全局 Toggle） |
| 右上 | **More**（`•••`），独占 ≥44×44 |

文案固定，不随类别状态变化。**不做：** Home On/Off 变体、状态 pill、全局总开关、Pause 按钮、Allowed Sites 入口、15m/1h 定时（见 D-309 / D-310 / D-315 / D-316）。

### 7.2 Feature Row（能力列表）

白卡 `cornerRadius 18`，行分隔 0.33pt。顺序固定（改前先改总纲领）：

1. Ads  
2. Privacy  
3. Annoyances  
4. Regional Ad Blocking（副文案：Automatic by language）  
5. YouTube & X · Pro  
6. Battery Boost · Pro  
7. Strict Mode · Pro  
8. Tap to Block · Pro（Chevron 行 → 说明页）  

| 规则 | 说明 |
|------|------|
| 主/副文案 | 17 + 13 @ secondary |
| Free 行 | 右侧 Switch；默认 On |
| Pro 行 | 左 **PRO badge** + 文案 + Switch（默认 Off）或 Chevron |
| 全部类别 Off | 列表仍可见；选择保留；无拦截生效 |
| Locked Pro | **禁止乐观切换** → 进 Upgrade；取消后控件原样 |
| 密度 | 同一行不堆开关 + 按钮 + 徽标 + 多链接 |

### 7.3 Primary Button

- 尺寸 **358 × 50**（水平 inset 16），圆角 **12**  
- 底 `brandPrimary`，字白 SemiBold 17  
- **单屏最多一个**视觉主按钮  
- 文案用动作结果：`Set Up Safari Protection` / `Open Settings` / `Start 1 Month Free Trial`  
- 避免模糊 `Continue`（除非结果已完全明确）  

### 7.4 Pro Badge

- 约 **40 × 22**，圆角 7，边 0.75  
- 字 `PRO` Bold ~10.5  
- 色见 §4.1；**暖金只服务 Pro**

### 7.5 Icon treatment

| 场景 | 规格 |
|------|------|
| Welcome / Setup emblem | 72 圆，`brandSoft` 底 + `brandPrimary` 图标 |
| Paywall / 列表小图标 | 30×30，圆角 8，`#E5EFEB` 类底 |
| Setup 步骤 | 40×40，圆角 10，中性灰绿底 |

**开源图标库（Hi-fi 现行）：[Lucide](https://lucide.dev) v0.469（ISC 许可）**  
线宽约 1.75–2.0，圆角端点；颜色随语义（`#2F6A58` / `#4A504D` / Dark `#67C7A5` / Pro 金 `#7A5316`）。

| 语义 | Lucide 名称 | 出现位置 |
|------|-------------|----------|
| Welcome Header | `shield-check` · **正圆** · 底 `#EAF3EF` | Welcome 顶 emblem（价值：保护就绪） |
| Setup Header | `settings` · **圆角方 r18** · 底 `#EEF0EF` · 角标 `check` 金 | Setup 顶 emblem（动作：去系统设置） |
| 保护（列表/其它） | `shield` / `shield-check` | 卖点与 Pro 行 |
| 广告拦截 | `megaphone-off` | Welcome 卖点 Ads |
| 隐私 | `eye-off` | Welcome Privacy |
| 烦人项 | `bell-off` | Welcome Annoyances |
| 地区规则 | `languages` | Welcome Regional |
| YouTube & X | `play`（填充三角） | Welcome / Upgrade |
| Battery Boost | `battery-medium` | Welcome / Upgrade |
| Strict Mode | `shield-check` | Welcome / Upgrade |
| Tap to Block | `mouse-pointer-click` | Welcome / Upgrade |
| Daily updates | `refresh-cw` | Welcome |
| Open Settings | `settings` | Setup 步骤 1 |
| 开启扩展 | `puzzle` | Setup 步骤 2 |
| 网站访问 | `globe` | Setup 步骤 3 |
| Private by design | `lock` | Setup 安心条 |
| Setup badge | `sliders-horizontal` | Setup 角标 |

**实现：** 优先 **SF Symbols** 中语义等价符号（如 `shield`、`eye.slash`、`bell.slash`、`globe`、`battery.100`、`arrow.triangle.2.circlepath`）；无 SF 等价时再打包 Lucide SVG。不绘制与系统语义冲突的自定义符号；避免夸张安全插画。

### 7.6 Welcome

- 顶：emblem + 口号（如 *A quieter Safari.*）+ 一句价值  
- 中：白卡可滚动卖点列表（行高约 70）  
- 底：固定主 CTA + fade；footer：*No account required · Core Safari protection is free*  
- 主 CTA **不得**强制 Free Trial  

### 7.7 Setup（门禁）

- 标题 + 说明 + 三步权限列表 + **Open Settings**  
- 等待回跳提示 + `Private by design` 安心条  
- 未完成授权 **不得进 Home**  

### 7.8 Upgrade / Paywall

- 标题 *Unlock Stillwall Pro* + 一句价值  
- 白卡利益列表（小图标）  
- Offer：*1 month free* → *Then $14.99/year · Family Sharing included*  
- 主 CTA *Start 1 Month Free Trial*  
- 系统蓝 *Restore Purchases* + 法律小字  
- 购买：CTA → `Processing…`（disabled）；取消静默；失败 **inline** 于 CTA 下  
- Restore：`Restoring…`；成功 inline「Pro restored」；**无**独立交易页  
- 非首次进 Home 门禁  

### 7.9 More / 次级页

Help · Feedback · About · Privacy Policy · Website · Restore · Manage Subscription。  
无账号体系行；无 Allowed Sites 行。

---

## 8. 动效

| 场景 | 规范 |
|------|------|
| 按钮按压 | scale **0.98** / **140ms** |
| 状态文案切换 | crossfade **180ms** |
| Switch / 系统导航 | 跟系统 |
| 常规 UI | ≤ 300ms；进入 ease-out；状态间 ease-in-out |
| sheet | 系统默认或 200–300ms |
| Reduce Motion | 去掉位移与缩放；保留约 **160ms** 透明度变化 |

**使用动效：** 保护状态切换、首次启用完成、错误修复确认、sheet/toast。  
**不使用装饰动效：** 高频列表滚动、普通开关旁加戏。

---

## 9. 文案原则

- 短句、普通词；不写 `VPN tunnel`、过滤器内部实现名解释主流程  
- 不恐吓（避免 *You are exposed* / *Threats detected*）  
- 能力边界诚实：YouTube & X **仅 Safari**；不承诺原生 App  
- 状态与能力用英文 UI；技术细节进 Learn More / Help  

---

## 10. 无障碍验收（TestFlight 底线）

- VoiceOver 可完成启用、开关、升级、反馈主路径  
- Dynamic Type：至少测到较大辅助级别；**行高随文字增高，滚动而非裁切**（稿含 Large Type 画板）  
- 触控 ≥ 44×44；颜色不是唯一状态信号  
- Reduce Motion / Reduce Transparency 可用  
- Light + Dark 主路径过一遍  

---

## 11. SwiftUI 实现映射

> 仓库当前 **尚无** iOS client 源码；本节为落地约定，供脚手架与 PR 对照。

### 11.1 建议文件结构

```text
Stillwall/
  DesignSystem/
    Color+Stillwall.swift      // 语义色
    Font+Stillwall.swift       // 动态字体角色（可选）
    Radius.swift
    Spacing.swift
    Motion.swift
  Components/
    PrimaryButton.swift
    ProBadge.swift
    FeatureRow.swift
    ProtectionHero.swift
    GroupedCard.swift
```

### 11.2 色表示例约定

```swift
// Color+Stillwall.swift — 语义 API，Light/Dark 用 Asset Catalog 或 adaptive init
enum StillwallColor {
    static let brandPrimary = Color("BrandPrimary")       // #2F6A58
    static let brandSoft = Color("BrandSoft")             // #EAF3EF
    static let protectionOn = Color("ProtectionOn")       // #34C759 / system green OK
    static let proBadgeBackground = Color("ProBadgeBg")
    static let proBadgeBorder = Color("ProBadgeBorder")
    static let proBadgeText = Color("ProBadgeText")
    static let surfaceGrouped = Color(.systemGroupedBackground) // 对齐 #F2F2F7 / #1C1C1E
    static let surfaceElevated = Color(.secondarySystemGroupedBackground) // 或 #FFFFFF / #2C2C2E
    static let textPrimary = Color.primary
    static let textSecondary = Color.secondary            // 校验是否接近稿中 0.65
    static let link = Color.accentColor                   // 系统蓝
}
```

优先系统语义色（`systemGroupedBackground` 等）对齐 iOS 列表；**品牌绿与 Pro 金必须进 Asset Catalog**，保证 Dark 可独立调。

### 11.3 组件 ↔ API

| 组件 | SwiftUI 方向 |
|------|----------------|
| 能力（类别）开关 | `Toggle` + `.labelsHidden()`；样式跟系统；**无** Hero 全局 Toggle |
| 主按钮 | 自定义 `ButtonStyle`：高 50、圆角 12、`brandPrimary`、按压 0.98/140ms |
| 列表卡 | `List` inset grouped **或** 自定义 `VStack` + 白底圆角 18（与稿一致时优先可控自定义） |
| More | `toolbar` / 右上按钮，命中区 ≥44 |
| Pro 锁定 | 拦截 `Toggle` 变更 → sheet/navigation 到 Upgrade；dismiss 后值不变 |
| Dynamic Type | 避免固定死行高；`fixedSize`/`lineLimit` 慎用 |

### 11.4 实现对照清单

| # | 检查项 | 设计源 | 代码状态 |
|---|--------|--------|----------|
| 1 | 无 Tab Bar | screens / 本稿 | **无 client 代码** |
| 2 | `brandPrimary` = `#2F6A58` | Lunacy Hi-fi | 未实现 |
| 3 | Pro 仅暖金徽标 | 本稿 §4 / §7.4 | 未实现 |
| 4 | 主按钮 50h / r12 / 单主 CTA | 本稿 §7.3 | 未实现 |
| 5 | 列表卡 r18、inset 16 | 本稿 §3 / §6 | 未实现 |
| 6 | Home Hero（只读）+ 类别列表 + More 44×44 | HIG notes | 未实现 |
| 7 | 能力行顺序与 Free/Pro 默认 | 总纲领 + screens | 未实现 |
| 8 | Locked Pro 不乐观切换 | HIG notes | 未实现 |
| 9 | 定价文案 $14.99/年 · 1 month free | 总纲领 §4 | 未实现 |
| 10 | 按压 0.98/140ms；Reduce Motion | 本稿 §8 | 未实现 |
| 11 | Light / Dark / Large Type | Lunacy 变体画板 | 未实现 |
| 12 | SF 系统字体，非 Inter 打包 | 本稿 §5 | 未实现 |

**结论（2026-07-27）：** `Gleem` 仓库目前仅有 `docs/`，**无 Swift / Xcode 工程可 diff**。视觉规范以本文 + Lunacy 为准；工程脚手架落地后，须按 §11.4 逐项勾选，不得从归档 v1 文档带回 Pause、App 内 Allowlist、$19.99/7-day 等旧决策。

---

## 12. 设计验收清单

- [ ] 用户不读帮助也能识别 On / Off  
- [ ] 单屏无多个竞争主按钮  
- [ ] Welcome CTA ≠ 强制试用  
- [ ] Setup 门禁完整  
- [ ] Home：仅类别开关（无全局总开关）；无 Pause / App 内 Allowed Sites  
- [ ] Free/Pro 边界在 paywall 前可读  
- [ ] 无不可验证威胁统计  
- [ ] Light / Dark、Dynamic Type、VoiceOver、Reduce Motion 真机或模拟器过主路径  
- [ ] 文案与总纲领一致（Safari-only YouTube/X、$14.99、Family Sharing）  

---

## 13. 变更规则

1. **产品范围**变更 → 先改总纲领 / 决策记录，再改本文与稿。  
2. **视觉 token** 变更 → 先改 Lunacy Hi-fi 与本文，再改代码 Asset。  
3. 与线框冲突时：**Hi-fi + 本文** 优先于线框；与总纲领冲突时：**总纲领** 优先。  
4. 旧归档 design-system 仅供追溯。  
