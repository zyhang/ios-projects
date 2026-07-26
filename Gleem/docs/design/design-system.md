# 设计原则与视觉规范

## 1. 设计目标

Gleem 的体验差异不是增加更多卡片、图表或开关，而是让用户在几秒内确认三件事：

1. 我现在是否受到保护。
2. 如果没有生效，我下一步该做什么。
3. 如果页面异常，我如何快速恢复。

核心设计准则：

> Gleem should feel calm because it is working—not busy because it wants to prove it.

## 2. 品牌人格

### 2.1 应该呈现

- 安静而可信。
- 现代但不追逐装饰潮流。
- 原生、轻量、反应迅速。
- 隐私透明，但不制造恐惧。
- 默认设置经过判断，不把复杂度推给用户。

### 2.2 应该避免

- 大面积盾牌、锁、雷达和警报符号。
- 红色威胁计数、夸张风险评分。
- “已阻止 12,483 个威胁”等不可验证数字。
- 密集 dashboard、环形图和技术术语。
- 霓虹渐变、赛博安全风格或廉价 VPN 视觉。
- 为展示动效而延迟状态反馈。

## 3. 视觉语言

### 3.1 布局

- 首屏只保留一个主要状态、一条解释和一个主要动作。
- iPhone 使用单列布局。
- iPad 保持内容宽度上限，不把简单页面拉伸成多列 dashboard。
- 高级说明通过 sheet、详情页或 disclosure 渐进展示。
- 主要操作放在自然拇指区域，避免顶部小型关键按钮。

### 3.2 色彩

建议建立语义色，而不是直接在业务代码中使用具体色值：

| Token | 用途 |
| --- | --- |
| `protectionActive` | 已保护状态 |
| `attentionRequired` | 需要用户操作 |
| `protectionPaused` | 暂停状态 |
| `surfacePrimary` | 主背景 |
| `surfaceElevated` | 浮层或卡片 |
| `textPrimary` | 主要文字 |
| `textSecondary` | 补充说明 |
| `brandAccent` | 品牌强调色 |

要求：

- `All Quiet` 不依赖绿色单独表达，必须同时使用图形和文字。
- `One Quick Step` 使用温和琥珀色，不使用威胁式红色，除非确有不可恢复错误。
- 支持 Light、Dark、Increased Contrast。
- 颜色对比满足 WCAG AA 目标。

### 3.3 字体与图标

- 使用系统字体与 Dynamic Type。
- 标题不使用全大写。
- 数字与版本信息使用等宽数字特性时需保证可读性。
- 优先使用 SF Symbols。
- 不自行绘制与系统图标语义冲突的符号。

### 3.4 材质

- 使用 iOS 26 原生材质与容器层级。
- 透明和模糊只用于表达层级，不用于铺满所有内容。
- 保证 Reduce Transparency 开启时仍能看清边界。
- 不把 Liquid Glass 当成品牌本身；产品人格来自排版、留白和状态表达。

## 4. 核心组件

### 4.1 Protection Status

包含：

- 状态图形。
- `All Quiet / One Quick Step / Paused` 标题。
- 一句状态解释。
- 最多一个主要修复动作。
- 可选的次级详情入口。

状态组件不得展示无法从系统或本地状态验证的信息。

### 4.2 Feature Row

用于展示 Safari、YouTube & X、Annoyances、Pro 等能力。

每行最多包含：

- 功能名称。
- 当前状态。
- 简短说明。
- 必要时的 disclosure。

不要在同一行同时放置开关、按钮、徽标和详情链接。

### 4.3 Primary Action

- 单屏最多一个视觉主按钮。
- 按下必须立即有触觉或缩放反馈。
- 文案使用动作结果，如 `Enable in Settings`、`Resume Protection`。
- 不使用模糊的 `Continue`，除非上下文结果完全明确。

### 4.4 Paywall

- 只展示年订阅。
- 清楚区分永久免费 Safari 和 Pro 跨 App 能力。
- 展示 `$19.99/year`、7-day free trial、续费规则和 Family Sharing。
- 不用虚假“最受欢迎”标签，因为没有其他付费选项。
- TestFlight 预览必须标注不会产生真实收费。

### 4.5 Feedback Composer

- 两个入口：`Missed Ad`、`Site Broken`。
- 明确列出将要发送的域名、系统版本、App 版本、规则版本。
- 截图和说明为可选。
- 发送前可删除任意字段。

## 5. 动效原则

### 5.1 何时使用

只在以下场景使用动效：

- 保护状态从未启用切换为已保护。
- 暂停与恢复。
- 首次启用完成。
- 错误修复后状态确认。
- sheet、toast 等偶发界面。

高频列表导航和普通开关不添加装饰性动画。

### 5.2 时长与曲线

- 按压反馈：100–160ms。
- 小型状态过渡：150–250ms。
- sheet/modal：使用系统默认或 200–300ms。
- 常规 UI 动效不超过 300ms。
- 进入使用 ease-out，状态间移动使用 ease-in-out。
- 不使用 ease-in 作为交互进入曲线。
- SwiftUI 优先使用可中断的 system spring，bounce 保持克制。

### 5.3 细节

- 可点击元素按压缩放建议为 `0.97–0.98`。
- 元素进入不从 `scale(0)` 开始。
- 状态图标变换应保持空间连续，不突然替换成无关图形。
- 支持 Reduce Motion：移除位移动效，保留必要的透明度或颜色反馈。

## 6. 无障碍要求

首个 TestFlight 必须满足：

- VoiceOver 可完整完成启用、暂停、放行和反馈流程。
- Dynamic Type 至少测试到 Accessibility 级别。
- 支持 Voice Control 可识别名称。
- 不使用颜色作为唯一状态信号。
- 触控区域不小于 44×44pt。
- Reduce Motion 与 Reduce Transparency 下可用。
- iPad 横竖屏不截断关键动作。
- YouTube/X 权限说明使用直接语言，不诱导授权。

## 7. 文案原则

- 默认使用短句和普通词。
- 不使用 `VPN tunnel`、`PIR`、`Bloom filter` 等技术词解释主流程。
- 技术详情放在 Learn More。
- 不制造恐惧，例如避免 `You are exposed`、`Threats detected`。
- 对能力限制保持诚实，例如：
  - 推荐：`Blocks many third-party ads and trackers across apps.`
  - 禁止：`Blocks every ad in every app.`

## 8. 设计验收清单

- 用户不阅读帮助也能识别当前状态。
- 每个 `One Quick Step` 都有可执行修复动作。
- 同一屏没有多个竞争主按钮。
- 免费版与 Pro 边界在 paywall 前已经清楚。
- 没有不可验证的统计。
- Light/Dark、Dynamic Type、VoiceOver、Reduce Motion 均完成真机检查。
- 动效在慢速回放下没有跳帧、错误 origin 或内容重叠。
