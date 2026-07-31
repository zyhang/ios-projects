# design

流程、信息架构、页面说明与**视觉规范**。Lunacy 产出在本目录登记。

**说明用中文；用户可见界面字符串用英文。**

## 权威关系

| 优先级 | 文档 |
|--------|------|
| 1 | [产品总纲领](../product/product-charter.md) |
| 2 | [决策记录](../decisions/decision-log.md) |
| 3 | 本目录流程、页面与 [视觉规范](design-system.md) |
| — | [历史归档](../archive/project-v1-2026-07-27/) 勿作现行权威 |

**视觉冲突：** [design-system.md](design-system.md) + Lunacy Hi-fi 优先于线框；与总纲领冲突时以总纲领为准。

## 索引

| 文件 | 说明 | 状态 |
|------|------|------|
| [app-flow.md](app-flow.md) | App 完整流程、状态机、门禁、错误边界 | 已建立 |
| [user-flows.md](user-flows.md) | 信息架构与关键用户流程摘要 | 已建立 |
| [screens.md](screens.md) | 分屏说明（主 App S0x + 扩展 SE0x） | 已建立 |
| [safari-extension.md](safari-extension.md) | **Safari 扩展 popup：固定 3 项、状态、流程** | **已确认** |
| [extension-wireframes-se.md](extension-wireframes-se.md) | SE01–SE03 线框尺寸/组件蓝图 | **已确认** |
| [extension-popup-mock.html](extension-popup-mock.html) | Popup 四态浏览器预览 mock | 已建立 |
| [design-system.md](design-system.md) | 设计原则、色板、字号、组件、动效、SwiftUI 映射 | **已建立（Hi-fi P0）** |
| [journey-polish-review-2026-07-31.md](journey-polish-review-2026-07-31.md) | 全漏斗 Journey polish 评审（文案/交互/视觉/商店/信任页） | **2026-07-31** |
| [exports/phone-preview/](exports/phone-preview/) | 主路径 Hi-fi PNG（含 D-510 CTA/Setup 修正） | 现行预览 |
| [exports/secondary-preview/](exports/secondary-preview/) | More / Help / Tap / SE 临时 HTML（006） | 工程可对稿 |
| [Stillwall-Wireframes-v1.free](Stillwall-Wireframes-v1.free) | 主 App 线框 | 已保存 |
| [Stillwall-HiFi-v1.free](Stillwall-HiFi-v1.free) | 高保真 P0 | 以仓库文件为准 |

### Lunacy

| 内容 | 说明 |
|------|------|
| 线框 | `Stillwall Wireframes v1` / 仓库 `.free`（主 App） |
| 高保真 | `Depth Pass · Hi-fi P0`（主路径；含 Light / Dark / Large Type；勿与线框混文件） |
| 扩展画板 | **已画** `Stillwall-Wireframes-v1.free` · ROW 4（SE01–SE03）；蓝图 [extension-wireframes-se.md](extension-wireframes-se.md) |
| 视觉 token | 见 [design-system.md](design-system.md) |

### Safari 扩展侧

| 项 | 状态 |
|----|------|
| 产品规格 | [safari-extension.md](safari-extension.md) **已确认**（3 项） |
| 剩余工程/线框 | 总纲领 §14 · decision-log T-EXT-03～07 |

## 硬约束

- 无 Tab；授权门禁；主 App 为**单一中性 Home + 类别开关**（**无** Home On/Off 变体、全局总开关、定时 Pause、App 内 Allowed Sites）
- Free/Pro 与开关顺序固定（改前先改总纲领）  
- 无 Custom Rules、无系统级全 App 拦截卖点、无 paywall bypass  
- YouTube/X 仅 Safari；Mac 仅 Coming soon  
- 扩展 popup **仅 3 项**：Pause/Resume · Tap to Block · Report issue  
