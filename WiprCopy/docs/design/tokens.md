# Gleem design tokens（v1 高保真）

产品界面英文。极简、冷静、indie 工具感 — 非杀毒红、非 VPN 霓虹。  
说明语言：中文。

## 颜色

| Token | Light | 用途 |
|-------|--------|------|
| `bg` | `#F4F2EE` | App 画布（暖纸色，轻微 gleam） |
| `bg-elevated` | `#FFFFFF` | 卡片、列表、sheet |
| `ink` | `#1A1917` | 主文案 |
| `ink-secondary` | `#6B6860` | 次要、说明 |
| `ink-tertiary` | `#9C9890` | 提示、“Something broken?” |
| `line` | `rgba(26,25,23,0.08)` | 分隔线 |
| `accent` | `#2C6E5A` | 主按钮、开关开（沉静绿） |
| `accent-pressed` | `#245A4A` | 主按钮按下 |
| `accent-soft` | `rgba(44,110,90,0.12)` | 软底 |
| `danger-soft` | 默认 Home 不用 | 避免默认态警报红 |

深色模式：推迟到 v1.1，除非系统强制；本套高保真 **浅色优先**。

## 字体

| 角色 | 字号 / 字重 | 备注 |
|------|-------------|------|
| Status（Home） | 28–34 / Semibold | 一句状态，居中 |
| Welcome 标题 | 28–32 / Semibold | 短行 |
| Welcome 正文 | 17 / Regular | 次要 ink |
| 导航标题 | 17 / Semibold | |
| 正文 | 17 / Regular | |
| Caption | 13–15 / Regular | 三级 |
| 按钮 | 17 / Semibold | |

Mock 字体栈：`-apple-system, SF Pro, system-ui, sans-serif`。

## 布局

- iPhone 框：393 × 852 pt 内容区（mock）
- 左右边距：24–28 pt
- 主按钮：全宽、高 52 pt、圆角 14 pt
- 列表行：最小高 52–56 pt
- 健康 Home：状态句垂直居中偏向

## 动效（意图）

- Welcome：轻柔页交叉淡入或横向滑动
- Home 状态变化：仅状态文字淡入淡出
- 无礼花、无激进成功动画
