# Issue 005：跨页视觉与文案一致性（Hallmark 全局审计后续）

| 字段 | 内容 |
|------|------|
| 状态 | open |
| 优先级 | P2（体验与调性；不阻塞 001/004 的 P0） |
| 类型 | ui / copy / docs-sync |
| 影响范围 | Welcome · Setup · Home · Upgrade ·（Large Type / Dark） |
| 相关文档 | `docs/design/design-system.md`；`docs/design/screens.md`；Hi-fi `phone-preview/*` |
| 创建日期 | 2026-07-31 |
| 审计 | Hallmark 全局 review · 设计稿 + issue 001–004 |

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
| Strict | （列表下方） | Stronger blocking · Use with care | **May affect some sites** | Stronger blocking · Use with care |
| Tap | （列表下方） | Hide page elements in Safari | 同左 | Hide page elements in Safari |
| Privacy | Block trackers. We don’t collect history. | Block common advertising trackers | Block common trackers | — |

Large Type 为省行高改写可以，但 **Strict 的「可能影响站点」** 与标准稿「更强拦截·慎用」语义重心不同，应锁定一版主句，Large Type 只做省略而非改意。

### B. Setup 设计稿措辞偏「两个扩展」

Hi-fi Setup 副文案 / 步骤 2 使用 *both extensions*，与产品真实形态（**6 Content Blockers + 1 Web Extension**）不符；实现版更诚实。以诚实版为权威（与 **003** 一致），设计导出应回对齐。

### C. Welcome 主 CTA 用词「Protection」与 Home 中性人格轻微拉扯

- Welcome CTA：`Set Up Safari Protection`  
- Home 价值句：`A quieter Safari, on your terms.`（刻意去「保护中」监控感）

品牌仍可用 Protection，但主路径 CTA 更宜动作化、少「安防产品腔」。

### D. Home Free / Pro 列表节奏

Hi-fi 正确：Free 行无领先图标（降噪），Pro 行暖金 `PRO` badge。  
可再提升一点「分区感」而不破坏安静：在首个 Pro 行前增加 **约 8pt 额外间距**（或 0.33 分隔已足够时保持现状）。**不要**加「PRO FEATURES」大写分区标题（廉价订阅模板感）。

### E. 缺失画板

- 规则编译进度（**002** 已补视觉规格）  
- Open Settings 失败 hint（**003**）  
- More / Help / Tap 说明 / 扩展 popup 仍无 Hi-fi（P2 文档债，本 issue 不强制出图）

## 期望结果

### 1. 文案锁定表（v1 源语言 en）

开发与文案以本表为准；Large Type 仅允许括号内「短式」。

| 行 | 主标题 | 副文案（标准） | 副文案（Large Type 可选短式） |
|----|--------|----------------|------------------------------|
| Ads | Ads | Reduce ads and visual clutter | （可同） |
| Privacy | Privacy | Block common advertising trackers | Block common trackers |
| Annoyances | Annoyances | Hide cookie banners and noisy prompts | Hide cookie banners and prompts |
| Regional | Regional Ad Blocking | Automatic by language | （可同） |
| YouTube & X | YouTube & X | Block YouTube & X ads in Safari | YouTube & X ads in Safari |
| Battery Boost | Battery Boost | Reduce wasteful browsing scripts | Reduce wasteful scripts |
| Strict Mode | Strict Mode | Stronger blocking · Use with care | Stronger blocking · Use with care（**不要**改成无关语义） |
| Tap to Block | Tap to Block | Hide page elements in Safari | （可同） |

**Upgrade 利益行**副文案与上表 Pro 四行对齐（Battery 用完整句 `Reduce wasteful browsing scripts`）。

**Welcome 卖点行**可保留略营销化写法，但 Pro 边界必须诚实：

- YouTube & X：须含 **in Safari** / **Not the native apps** 之一  
- 勿承诺未交付能力  

**Welcome 主 CTA（建议）：**

```text
Set Up in Safari
```

或保留 `Set Up Safari Protection` 若商店/截图已锁定——若改，需同步 App Store 截图计划。**推荐改为 `Set Up in Safari`**，与 quiet 人格一致。

**Setup 页（与 003 一致）：**

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

### 3. Home Pro 区微节奏（推荐）

- 在 **Regional** 与 **YouTube & X** 之间增加额外 **8pt** 间距（或保持单卡连续——二选一，全 App 统一）。  
- 推荐：**+8pt**，无分区标题。  

### 4. 顶图 emblem 语义

| 屏 | Emblem | 注意 |
|----|--------|------|
| Welcome | 圆 + shield-check | 价值「就绪」OK |
| Setup | 圆角方 + settings | **完成前无金勾**（见 003） |
| Home | 无大 emblem | 正确 |
| Upgrade | 无大 emblem | 正确 |

## 修改说明（给开发）

1. 建立单一文案源（`Localizable` / 常量表），Welcome / Home / Upgrade / Large Type 引用同一 key；短式用独立 key，禁止手写分叉。  
2. Setup 字符串按上表与 **003** 对齐；去掉 both extensions。  
3. Welcome CTA：按产品确认采用 `Set Up in Safari`（推荐）并回归测试截图。  
4. Home：Pro 区前 +8pt（若采用）；其余 token 对齐 design-system。  
5. 与 **001–004** 一起验收时做一次 **四屏连滑**（Welcome→Setup→Home→Upgrade），检查色、圆角、字体、按钮是否像同一产品。

### 文档

- `design-system.md` 已去除与 D-316 冲突的「Home 必须 On pill」叙述（同批）。  
- 设计文件 `Stillwall-HiFi-v1.free`：Setup 文案与 Welcome CTA 建议下次 Depth Pass 回写（工程可先按本文上线）。

## 验收标准

- [ ] Home / Upgrade /（Welcome Pro 相关）副文案符合锁定表；Large Type 不改变 Strict 语义  
- [ ] Setup 不再出现含糊的 both extensions；与 6 CB + Web Extension 一致  
- [ ] Welcome CTA 与产品确认的最终文案一致，且全项目无第三种说法  
- [ ] 主色 / 圆角 / 单主 CTA / PRO 仅暖金 四屏抽检通过  
- [ ] Home Free 行无多余领先图标；Pro 仅金 badge  
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
