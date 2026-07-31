# Issue 006：次级页与 Safari 扩展 Hi-fi 债（设计补齐）

| 字段 | 内容 |
|------|------|
| 状态 | **partial**（规格 + 完整 HTML 预览已交付；Lunacy 正式画板仍待） |
| 优先级 | P2（不阻塞主路径 001–005 开发；上架前建议有线框/说明对齐） |
| 类型 | docs-sync / ui |
| 影响范围 | More · Help · About · Feedback · Tap to Block 说明 · Safari 扩展 popup |
| 相关文档 | `docs/design/screens.md` S05–S10；`docs/design/safari-extension.md`；`docs/design/extension-wireframes-se.md` |
| 创建日期 | 2026-07-31 |
| 来源 | Hallmark 全局审计后续（产品确认登记债项） |

## 问题现象

主路径 Hi-fi（Welcome / Setup / Home / Upgrade）已齐；下列仍 **缺 Hi-fi 画板** 或仅有线框/文字规格：

| 面 | 现状 |
|----|------|
| More（S06） | 列表结构在 screens；无 phone-preview 成片 |
| Help（S07） | 条目建议有；无高保真 |
| Tap to Block 说明（S05） | 文字规格；无高保真 |
| Feedback / About（S09–S10） | 文字规格 |
| Safari 扩展 popup（SE01–SE03） | 有线框 / mock HTML；**Lunacy Hi-fi 待画**（safari-extension.md） |

风险：实现时各自「自由发挥」，破坏主路径已统一的 quiet Settings 人格。

## 期望结果

### 设计（产品/设计）

**已交付（仓库内，可对稿）：**

1. 规格权威：[secondary-screens.md](../../docs/design/secondary-screens.md)  
2. HTML 预览：[exports/secondary-preview/index.html](../../docs/design/exports/secondary-preview/index.html)  
   - More · Help 列表 · Site broken 详情 · Tap · Feedback · About  
   - SE01 / a / b / c 四态  
   - Setup 名称清单（与 003 / D-511 共用预览）  

**仍待（Lunacy）：**

1. 在 `Stillwall-HiFi-v1.free` Depth Pass 补齐画板并导出 PNG（关闭本 issue 的正式条件）  
2. 视觉 **必须** 继承主路径 token；扩展 **无 IAP**（D-508）

### 开发（在 Hi-fi 未出前）

- 严格按 `screens.md` + `safari-extension.md` + `design-system.md` 实现，**不要**自创第二套风格。  
- 扩展顶栏状态文案诚实：Protected / Paused / Off in app 等（见扩展规格）。  
- 与主 App Home **001** 对齐：主 App 无保护 pill；扩展可表达站点状态。

## 修改说明

| 角色 | 动作 |
|------|------|
| 设计 | 补画板 → 导出 → 更新 `design/exports` 与 screens 链接 |
| 开发 | 次级页与扩展跟规格；Hi-fi 到达后做视觉 diff |
| 产品 | 本 issue 关闭条件：至少 More + SE01 + Tap 说明有可对稿图像 |

## 验收标准

- [x] More / Tap 说明 / SE01 有与主路径 token 一致的视觉稿或导出 — **HTML：** `docs/design/exports/secondary-preview/`  
- [ ] Lunacy Hi-fi 正式画板（仍建议补）  
- [x] 扩展 popup 固定 3 项、无 IAP、无类别列表（预览 + 规格）  
- [x] 文档索引链到 secondary-preview  

## 附件

- 临时视觉：[`docs/design/exports/secondary-preview/index.html`](../../docs/design/exports/secondary-preview/index.html)  
- 既有 mock：`docs/design/extension-popup-mock.html`  

逻辑参考（已有）：

- `docs/design/safari-extension.md`  
- `docs/design/extension-wireframes-se.md`  
- `docs/engineering/ui-copy-en.md`  
