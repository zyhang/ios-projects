# Issue 006：次级页与 Safari 扩展 Hi-fi 债（设计补齐）

| 字段 | 内容 |
|------|------|
| 状态 | **open**（规格/HTML 已齐 · **App 次级页+扩展 UI 待开发**；Lunacy 正式板可选） |
| 优先级 | **P1**（主路径后应实现；勿因标题含 Hi-fi 而只当设计债） |
| 类型 | ui / copy / docs-sync |
| 影响范围 | More · About · Feedback · Safari 扩展 popup（Help 见 **009**；**无** Tap · D-317） |
| 相关文档 | `docs/design/secondary-screens.md`；`docs/design/safari-extension.md`；`docs/engineering/ui-copy-en.md` |
| 创建日期 | 2026-07-31 |
| 来源 | Hallmark 全局审计 + 设计续作审计 |

## 问题现象

主路径 Hi-fi（Welcome / Setup / Home / Upgrade）已齐；下列仍 **缺 Hi-fi 画板** 或仅有线框/文字规格：

| 面 | 现状 |
|----|------|
| More（S06） | 列表结构在 screens；无 phone-preview 成片 |
| Help（S07） | 条目建议有；无高保真 |
| Tap to Block 说明（S05） | **v1 不做**（D-317） |
| Feedback / About（S09–S10） | 文字规格 |
| Safari 扩展 popup（SE01 **2 项**） | 规格已改 2 项；线框/mock 待去 Tap |

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

### 开发（**本 issue 主要关闭条件**）

权威：[`secondary-screens.md`](../../docs/design/secondary-screens.md) + [`ui-copy-en.md`](../../docs/engineering/ui-copy-en.md) + 预览 HTML。  
**不要**等 Lunacy 才开工；HTML 即可对稿。

| 屏 | 必须实现 |
|----|----------|
| **S06 More** | Help / Feedback / About / Privacy / Website / Restore / Manage（无账号、无 Allowed Sites） |
| **S05 Tap** | **不实现**（D-317 / **011**） |
| **S09 Feedback** | 类型 · 描述 · 可选域名 · **发送前预览** |
| **S10 About** | 版本 · 定位句 · Acknowledgements 入口 · Mac coming soon 可选 |
| **SE01 popup** | **仅 2 项**（Pause · Report）；顶栏 Protected / Paused / Off in app / Not enabled；无 IAP；**无** Tap |
| **Help** | 归 **009**（勿在本 issue 重复关） |

视觉：`surfaceGrouped` + r18 + 森绿主 CTA + PRO 仅暖金；与 **001** 一致：主 App 无保护 pill。

## 修改说明

| 角色 | 动作 |
|------|------|
| **开发** | 按上表实现次级页 + 扩展 popup；字符串走 `ui-copy-en` / 005 catalog |
| 设计 | 可选：Lunacy 正式板 → PNG（增强对稿，**非**开发开工阻塞） |
| 产品 | 关闭本 issue = **App 实现验收通过**（不是仅有 HTML） |

## 验收标准

### 规格 / 设计预览（已完成）

- [x] secondary-screens 规格 + secondary-preview HTML  
- [x] 扩展 3 项 / 无 IAP 写进规格  

### 开发实现（**未完成**）

- [ ] More 列表齐全且无违禁行  
- [ ] **无** Tap 说明页 / 扩展 Tap 槽（D-317）  
- [ ] Feedback 发送前预览  
- [ ] About 基础信息  
- [ ] 扩展 popup **2 项** + 四态（至少 Protected + Not enabled）  
- [ ] 无第二套主色/威胁仪表盘；无扩展内 IAP  

### 可选 · Lunacy 导出

- [ ] Wireframes 在 **Automation 已连接的 Lunacy 窗口**中打开后，导出 More / Help / Feedback / About / SE01 四态 → `docs/design/exports/secondary-preview/png/`  
- [ ] **勿**导出 S05 Tap 作权威（D-317）  
- 进度：2026-07-31 主路径已从 Hi-fi 导出；**次级/SE 因文档未切换 MCP 会话未导出**（见 `docs/design/exports/lunacy-export-log-2026-07-31.md`）  

## 附件

- 临时视觉：[`docs/design/exports/secondary-preview/index.html`](../../docs/design/exports/secondary-preview/index.html)  
- 既有 mock：`docs/design/extension-popup-mock.html`  

逻辑参考（已有）：

- `docs/design/safari-extension.md`  
- `docs/design/extension-wireframes-se.md`  
- `docs/engineering/ui-copy-en.md`  
