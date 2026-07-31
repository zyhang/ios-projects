# Issue 005：跨页视觉与文案一致性（Hallmark 全局审计后续）

| 字段 | 内容 |
|------|------|
| 状态 | open（**文案表 + 导出资产已对齐**；待主 App 单一 string catalog） |
| 优先级 | P2（体验与调性；不阻塞 001/004 的 P0） |
| 类型 | ui / copy / docs-sync |
| 影响范围 | Welcome · Setup · Home · Upgrade ·（Large Type / Dark） |
| 相关文档 | `docs/design/design-system.md`；`docs/design/screens.md`；Hi-fi `phone-preview/*` |
| 创建日期 | 2026-07-31 |
| 审计 | Hallmark 全局 review · 设计稿 + issue 001–004 |
| 文案锁定 | **2026-07-31 产品已确认**（下列字符串为 v1 权威，不再「推荐/可选」） |

## 背景（审计结论摘要）

**设计理念（已统一，应守住）：**

> iOS Settings 式分组列表 + 系统灰分组底 + 单一森绿 `#2F6A58` + 系统绿开关 + 暖金仅 Pro + 少阴影 + 单主 CTA + 冷静诚实文案。

Hi-fi（Welcome / Setup / Home / Upgrade + Dark + Large Type）**整体同属一套人格**，不是四套模板换皮。主要问题是：

1. **实现**偏离（001–004 已覆盖的状态 pill、中文进度、深链硬错误、$9.99、Request Canceled）。  
2. **跨页文案与细节**在设计稿内部也有轻微漂移（本 issue）。  
3. **design-system** 个别段落仍残留「Home 要展示 On/Off pill」旧叙述（文档侧已在同批修订）。

本 issue **不**重复 001–004 的修复项；专注跨页一致性与品味级打磨。

## 问题现象

### A. 同一能力的副文案多套说法

| 能力 | Welcome | Home（标准） | Home Large Type | Upgrade |
|------|---------|--------------|-----------------|---------|
| Battery | Pro · Reduce wasteful browsing scripts | Reduce wasteful scripts | 同左 | Reduce wasteful browsing scripts |
| Tap | （列表下方） | Hide page elements in Safari | 同左 | Hide page elements in Safari |
| Privacy | Block trackers. We don’t collect history. | Block common advertising trackers | Block common trackers | — |

### B. Setup 设计稿措辞偏「两个扩展」

Hi-fi Setup 副文案 / 步骤 2 使用 *both extensions*，与产品真实形态（**6 Content Blockers + 1 Web Extension**）不符；实现版更诚实。以诚实版为权威（与 **003** 一致），设计导出应回对齐。

### C. Welcome 主 CTA（已锁定）

| 状态 | 文案 |
|------|------|
| **权威** | `Set Up in Safari` |
| 弃用 | `Set Up Safari Protection` · `Enable Safari Blocking` |

与 Home 中性人格一致：动作化，少安防腔。商店成片若仍含旧 CTA，重导出时改掉（见 screenshot-plan 备注）。

### D. Home Free / Pro 列表节奏（已锁定）

- Free 行：**无**领先图标  
- Pro 行：暖金 `PRO` badge  
- **Regional 与 YouTube & X 之间 +8pt** 额外间距  
- **禁止**「PRO FEATURES」等大写分区标题  

### E. 缺失画板

- 规则编译进度（**002**）· Open Settings 失败 hint（**003**）— 有文字规格即可  
- More / Help / Tap 说明 / 扩展 popup Hi-fi → **006**

## 期望结果

### 1. 文案锁定表（v1 源语言 en · **已确认**）

开发与文案**必须**以本表为准。Large Type **仅**可使用「短式」列。

| 行 | 主标题 | 副文案（标准） | 副文案（Large Type 短式） |
|----|--------|----------------|---------------------------|
| Ads | Ads | Reduce ads and visual clutter | Reduce ads and visual clutter |
| Privacy | Privacy | Block common advertising trackers | Block common trackers |
| Annoyances | Annoyances | Hide cookie banners and noisy prompts | Hide cookie banners and prompts |
| Regional | Regional Ad Blocking | Automatic by language | Automatic by language |
| YouTube & X | YouTube & X | Block YouTube & X ads in Safari | YouTube & X ads in Safari |
| Battery Boost | Battery Boost | Reduce wasteful browsing scripts | Reduce wasteful scripts |

**Battery 禁止：** 实机常见的 *Block mining & wasteful scripts* / *mining* 口径（不可验证、偏恐吓）；统一上表。  

~~Strict Mode / Tap to Block~~ | — | **v1 不做（D-317）** | — |

**Upgrade 利益行**副文案 = 上表 Pro **两行**标准列（YouTube & X + Battery only）。

**Welcome 卖点行**可略营销化，但 Pro 边界必须诚实：

- YouTube & X：须含 **in Safari** 或 **Not the native apps**  
- 勿承诺未交付能力  

**Welcome 主 CTA（已锁定）：**

```text
Set Up in Safari
```

**Setup 页（与 003 一致 · 已锁定）：**

```text
Title: Enable Stillwall in Safari
Subtitle: Safari needs six Stillwall Content Blockers plus the Web Extension. Turn them all on, then allow website access.
Step2 subtitle: Enable all 6 Content Blockers and the Web Extension
```

### 2. 视觉一致性检查表（实现对照 Hi-fi）

| 检查项 | 标准 |
|--------|------|
| 页面底 | `surfaceGrouped` `#F2F2F7` / Dark `#1C1C1E` |
| 主卡 | `surfaceElevated` r**18** |
| 主 CTA | `#2F6A58`（Dark 可用略提亮绿以保证对比），h**50** r**12**，单屏一个 |
| Switch On | 系统绿 |
| PRO badge | 暖金系，**仅** Pro 权益 |
| 图标井 | Welcome/Upgrade/Setup 步骤用软底图标；**Home Free 行不加**领先图标 |
| 链接触控 | Restore 等用系统蓝；主行动用森绿 |
| 无 | 多主按钮、霓虹、威胁大数字、玻璃拟态整页 |

### 3. Home Pro 区微节奏（已锁定）

Regional 与 YouTube & X 之间 **+8pt**，无分区标题。

### 4. 顶图 emblem 语义

| 屏 | Emblem | 注意 |
|----|--------|------|
| Welcome | 圆 + shield-check | 价值「就绪」OK |
| Setup | 圆角方 + settings | **完成前无金勾**（见 003） |
| Home | 无大 emblem | 正确 |
| Upgrade | 无大 emblem | 正确 |

## 修改说明（给开发）

1. 建立单一文案源（`Localizable` / 常量表），**以仓库** [`docs/engineering/ui-copy-en.md`](../../docs/engineering/ui-copy-en.md) **为权威表**（含 Welcome/Setup/Home/Upgrade/**Setup D-511 清单**/Help/扩展）。  
2. Welcome / Home / Upgrade / Large Type 引用同一 key；短式用独立 `*.large` key，禁止手写分叉。  
3. Setup 字符串按锁定块与 **003** 对齐（含 D-511 checklist keys）；去掉 both extensions。  
4. Welcome CTA **固定** `Set Up in Safari`。  
5. Home：Pro 区前 **+8pt**；其余 token 对齐 design-system。  
6. **无** Strict/Tap（D-317 / **011**）。  
7. 与 **001–004** 一起验收时做 **四屏连滑**（Welcome→Setup→Home→Upgrade）。  

### 文档

- `design-system.md` / `screens.md` / `app-flow.md` 已同步权威 CTA。  
- Lunacy `Stillwall-HiFi-v1.free`：下次 Depth Pass 回写 Welcome CTA、Setup 诚实文案、D-317 范围（工程可先按本文上线）。

## 验收标准

- [ ] 工程存在单一 string catalog，且与 `ui-copy-en.md` 主路径 key 对齐  
- [ ] Home / Upgrade 副文案符合锁定表（**仅** YT&X + Battery 为 Pro 行）  
- [ ] Battery 副文案为 *Reduce wasteful browsing scripts*（**禁止** *mining* / *Block mining…*）  
- [ ] **无**用户可见 Strict Mode / Tap to Block（D-317 / **011**）  
- [ ] Setup 不再出现 both extensions；与 6 CB + Web Extension 一致（清单实现见 **003**）  
- [ ] Welcome CTA **仅** `Set Up in Safari`，全项目无第三种主 CTA 说法  
- [ ] 主色 / 圆角 / 单主 CTA / PRO 仅暖金 四屏抽检通过  
- [ ] Home Free 行无多余领先图标；Pro 区前 +8pt；Pro 仅金 badge  
- [ ] 与 001 完成后的 Home 连看：无状态 pill、中性 hero、安静列表

## 附件

| 文件 | 说明 |
|------|------|
| `after/welcome.png` | Hi-fi Welcome |
| `after/setup.png` | Hi-fi Setup（文案以本 issue 诚实版为准，稿面可能仍写 both） |
| `after/home.png` | Hi-fi Home |
| `after/upgrade.png` | Hi-fi Upgrade |
| `after/home-dark.png` | Home Dark |
| `after/home-large-type.png` | Home Large Type（注意副文案分叉） |
