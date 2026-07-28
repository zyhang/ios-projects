# Gleem 项目文档

> 内部代号 `Gleem`。对外产品名暂用 `Stillwall`（以[产品总纲领](product/product-charter.md)为准，上架前可调整）。

## 状态

**全应用重构进行中。** 现行范围与功能以产品总纲领为准；流程与页面说明已按总纲领重建。

| 项 | 位置 |
|----|------|
| **产品总纲领** | [product/product-charter.md](product/product-charter.md) |
| **决策记录** | [decisions/decision-log.md](decisions/decision-log.md) |
| **设计（流程/页面）** | [design/](design/) |
| **历史全量归档** | [archive/project-v1-2026-07-27](archive/project-v1-2026-07-27/)（勿作现行权威） |

## 文档目的

本目录是产品、设计、研发、规则、隐私、测试、发布和运营的统一事实来源。除 Apple API、代码标识符、产品文案等专用名词外，文档统一使用中文。

**冲突优先级：**

1. [产品总纲领](product/product-charter.md)  
2. [决策记录](decisions/decision-log.md)中「已确认」项  
3. 各专业目录详细设计  
4. 归档与未确认讨论  

## 文档导航

### 产品

- [产品总纲领与功能说明](product/product-charter.md)：定位、Free/Pro、功能边界、流程纲要、隐私、成功标准、明确不做  

### 决策

- [决策记录](decisions/decision-log.md)：D-1xx～D-6xx、待验证与暂缓项  

### 设计

- [设计目录说明](design/README.md)  
- [App 完整流程](design/app-flow.md)：状态机、门禁、主路径、错误边界  
- [信息架构与用户流程](design/user-flows.md)  
- [页面说明](design/screens.md)：Welcome / Setup / Home / More 等（主 App）+ SE 扩展页  
- [Safari 扩展产品面](design/safari-extension.md)：**popup 固定 3 项**（Pause/Resume · Tap · Report）  
- [扩展线框蓝图 SE](design/extension-wireframes-se.md) · [Popup mock HTML](design/extension-popup-mock.html)  
- [设计原则与视觉规范](design/design-system.md)：色板、字号、组件、动效、SwiftUI 映射（对齐 Lunacy Hi-fi P0）  
- **扩展剩余工作：** Lunacy 入库（T-EXT-05）、Tap 真机（V-005）、Help 路径（T-EXT-07 / V-002）  

### 质量

- [Safari 测试站点清单](quality/safari-test-sites.md)：欧美 / 日韩 / 澳高频站、能力 ID 映射、发版最小回归套件  

### 工程

- [engineering/](engineering/)：[ios-client.md](engineering/ios-client.md) · [safari-extension.md](engineering/safari-extension.md)（App Group schema、CB/WE、实现顺序）  
- 规则 / 隐私 / 发布 / 运营：待按总纲领继续重建。  

### 其他

- 实现不得突破总纲领第 5–9 节。  

### 归档

- [项目文档 v1 归档](archive/project-v1-2026-07-27/README.md)  

## 统一术语（摘要）

详见[总纲领 §11](product/product-charter.md)。

| 术语 | 含义 |
|------|------|
| Content Blocker | Safari 声明式内容拦截 |
| Web Extension | Safari 网页扩展（YouTube/X、Tap to Block 等） |
| Pro | $14.99/年 · 1 个月试用 · Family Sharing |
| 门禁 | 未完成 Safari 授权不得进入 Home |

## 维护规则

- 范围变化先更新总纲领与决策记录，再改设计与代码。  
- 「已完成」「已验证」仅用于真实运行或测试通过的内容。  
- 未完成的 entitlement、商标、许可证保持「待验证」。  
- 文档中不写密钥、Token、证书、真实用户数据。  
- 公开文案不承诺原生 YouTube/X App 去广告；不写 v1 未交付能力。  
