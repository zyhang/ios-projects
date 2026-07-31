# Journey polish 评审报告（2026-07-31）

> **类型：** 用户旅程体验 / 文案 / 交互 / 视觉一致性 review（非改代码）  
> **镜头：** 首次安装的普通人（主）  
> **主轴：** 意图优先（charter · Hi-fi · D-510）；每条发现标 `intent` / `drift` / `store` / `intent-optional`  
> **触点：** 主 App + Safari 扩展 + App Store + Support/Privacy（不含官网 marketing redesign）  
> **深度：** 全路径均匀；Dark / Large Type 抽查主路径  
> **产出约定：** 本报告 + P0/P1 落 `issues/`；**不**重复开 001–006 同题  

---

## 0. 评审边界（已锁定）

| 项 | 值 |
|----|-----|
| 目标 | Journey polish（尊重已锁决策；顺带标上架硬伤） |
| 不做 | 默认改代码、推翻 charter 铁律、官网大改、无确认改 D-510 |
| 已有债 | 001–006 仍有效；本报告只**对照验收**，不重写同题 issue |
| 权威输入 | `product-charter` · `decision-log` · `app-flow` / `user-flows` / `screens` · `design-system` · Hi-fi `phone-preview` · App Store assets · Support/Privacy · `safari-extension` |

**人格锚点（应守住）：**

> iOS Settings 式分组列表 + 系统灰底 + 森绿 `#2F6A58` + 系统绿 Switch + 暖金仅 Pro + 少阴影 + 单主 CTA + 冷静诚实。  
> *Stillwall should feel calm because it is working—not busy because it wants to prove it.*

---

## 1. 总评（给产品的一页纸）

| 维度 | 分数（1–5） | 一句话 |
|------|-------------|--------|
| 产品模型清晰度 | **4.5** | 免费类别开关 + 扩展现场控制 + Pro 增强，边界清楚 |
| 主路径 Hi-fi 人格 | **4.5** | Welcome/Setup/Home/Upgrade 同属一套安静 Settings 气质 |
| 意图 vs 实现 | **2.5** | 001–004 显示实机严重漂移（状态 pill、$9.99、中文进度、硬错误） |
| 意图内部一致性 | **3.0** | D-510 已锁，但 Hi-fi 导出 / 商店截图 / Support **未回写** |
| 首次用户启用负担 | **3.0** | Setup 诚实度与 6 个 CB 认知成本是最大摩擦 |
| 误杀恢复可发现性 | **2.5** | 路径正确但藏在扩展；App Help/Support 规格或内容有误 |
| 付费墙诚实度（意图） | **4.5** | Hi-fi 定价/试用/Family 清楚；实现见 004 |
| 商店首印象 | **3.5** | 截图序列与调性好；像素内仍有旧 CTA；描述域名为占位 |
| 信任页（Support） | **1.5** | **与 D-316 直接冲突**（写 Home 显示 On） |

**结论：**  
v1 **产品意图与主路径设计人格已经立住**；当前最大风险不是「再做一个更炫的 Home」，而是：

1. **实现未跟上意图**（001–004，P0/P1 已开）  
2. **权威文案已锁，外围触点（Hi-fi 导出、商店成片、Support）仍在旧宇宙**  
3. **首次用户在 Setup 与「坏站怎么办」两处最容易流失或误解**

开发优先仍应：**001 + 004 → 002 + 003 → 005 文案源**；本轮新增 **007（Support 信任口径）** 与 **008（商店包装）** 应与上架并行，**009（Help/恢复路径可发现性）** 在主路径稳定后尽快补。

---

## 2. 旅程走查

### 2.1 商店首屏（App Store）

**用户目标：** 3 秒内判断「这是不是我想要的 Safari 去广告」。

| 观察 | 标签 | 说明 |
|------|------|------|
| Name / Subtitle 清晰 | — | `Stillwall for Safari` + `Free Ad & Tracker Blocking` 对首次用户诚实（D-108/109） |
| 截图 1 用中性 Home | — | 正确传达「类别可控、非恐吓仪表盘」；与 D-316 一致 |
| 截图 2 Welcome 像素 CTA 仍为 `Set Up Safari Protection` | `store` | 与 D-510 `Set Up in Safari` 冲突；框外标题 OK，**框内 UI 过期**（screenshot-plan 已备注，**成片未更新**） |
| Setup 成片同源 | `store` | 若仍含 *both extensions* / 预完成金勾，会在商店预演错误心智 |
| Description 结构好 | — | Free → Pro（in Safari）→ 隐私 → 订阅；无 VPN/全 App 夸大 |
| Description 尾部 `https://<domain>/…` | `store` | D-113 已定为 `yilinglabs.com`；占位符上架前必须替换 |
| 框外「annoyances blocked」略绝对 | `intent-optional` | 产品原则是「不承诺 100%」；可改为 *quieter* / *fewer* 语气，非必须 |

**Hallmark 视角：** 商店绿顶栏 + 设备居中是克制的 product-theater，没有假数据大数字——保持。不要为转化加威胁计数。

---

### 2.2 Welcome（S01）

**用户目标：** 决定要不要点主按钮去设 Safari。

| 观察 | 标签 | 说明 |
|------|------|------|
| 口号 *A quieter Safari.* 与 Home 同源 | — | 品牌句连贯，好 |
| 卖点列表：Free 与 Pro 分层清楚（Pro · / Not the native apps） | — | 诚实边界到位 |
| 主 CTA 导出仍为 `Set Up Safari Protection` | `intent`（资产未回写） | **权威是 D-510 `Set Up in Safari`**；工程与重导出必须改（005 已覆盖；资产仍旧） |
| Footer：No account · free core | — | 降低试用胁迫，符合 D-208 |
| 底栏遮住 Strict / Tap 下半 | `intent-optional` | 可滚动可接受；Large Type 更挤，确保可滚且 CTA 不挡最后可点卖点 |
| Large Type：Privacy 副文案变成 *No browsing history collected* | `intent-optional` | 丢掉「拦追踪」能力义；建议短式仍保留 trackers 语义（005 表可增 Welcome LT 行） |
| Dark：CTA 提亮绿 | — | 对比合理，人格保留 |

**品味判断：** Welcome 是成功的「安静卖货」——不是安全软件恐吓页。唯一必须修的是 **弃用 CTA 字符串在导出/商店中的幽灵残留**。

---

### 2.3 Setup（S02）— 最大体验瓶颈

**用户目标：** 搞懂系统要开什么，做完能回 App。

| 观察 | 标签 | 说明 |
|------|------|------|
| 三步结构清晰 | — | Open Settings → Turn on → Allow access，心智好 |
| 副文案 / 步骤 2：*both extensions* | `intent` | **与真实 6 CB + 1 Web Extension 不符**；首次用户按「两个开关」操作会失败 → 假「我装了但不拦」（003/005 已锁诚实版；**Hi-fi 未改**） |
| 顶 emblem 预挂金勾 | `intent` | 未完成即「已完成」暗示，违反诚实状态；design-system §7.7 已禁，导出仍有 |
| 深链失败橙错 | `drift` | 见 **003** |
| *Come back when you're done* | — | 降低焦虑，好 |
| Private by design 条 | — | 信任强化，好；视觉可作 002 进度条气质参考 |
| Large Type 仍 both extensions | `intent` | 与标准稿同病 |
| 认知负荷：系统里 6 个 Content Blocker 名 | `intent-optional` | 可在步骤 2 用一行微型列表点名 Ads/Privacy/… 或「全部 Stillwall 开头的开关」，减少漏开 |

**首次用户剧本（易失败）：**

```text
点 Open Settings → 深链失败或进错页 → 看到「两个扩展」文案
→ 只开了 Web Extension 或只开部分 CB → 回 App
→ 门禁仍挡 / 或进了 Home 但拦不全 → 「这 App 不行」
```

**优先级判断：** Setup 诚实文案 + 非恐吓失败态 = **启用漏斗 P0/P1**（003/005）；设计导出回写与 Support 对齐同步做。

---

### 2.4 首次进入 Home（S03）

**用户目标：** 感到「已经就绪」，并知道能调什么。

| 观察 | 标签 | 说明 |
|------|------|------|
| 中性 Value Hero 意图极强 | — | *A quieter Safari, on your terms.* 符合人格与 D-316 |
| 实机仍 On pill + Safari Protection | `drift` | **001**（P0） |
| Free 无图标 / Pro 暖金 badge / 无分区大写标题 | — | 克制、高级；+8pt Free→Pro 节奏（005）应守 |
| 全部 Off 仍同一页 | — | 正确；诚实态在扩展 `Off in app` |
| 规则进度中文 | `drift` | **002** |
| 无「站点放行」入口 | — | 符合 D-309；**但**首次用户不知道去 Safari 扩展（见 §2.6 / 009） |
| Dark / Large Type 抽查 | — | Dark 人格稳；**Large Type Strict 仍为 *May affect some sites***（D-510 否决，005） |

**intent-optional：**  
首次通过 Setup 进入 Home 时，**一次性**弱提示（非状态 pill）如 *Tip: to fix a broken site, use Pause in the Safari extension* —— 不破坏 D-316，但提升恢复路径发现。需产品点头后再锁文案。

---

### 2.5 Upgrade（S08）

| 观察 | 标签 | 说明 |
|------|------|------|
| 利益四行 + in Safari | — | 与 Home Pro 锁定表一致（意图） |
| $14.99 / 1 month free / Family / Cancel anytime | — | Hi-fi 正确 |
| 实机 $9.99 + Request Canceled | `drift` | **004** |
| 单主 CTA、无假倒计时 | — | 品味正确，保持 |
| 关闭 X 与 Restore 系统蓝 | — | 层级清楚 |

---

### 2.6 Safari 扩展（SE01–03）

| 观察 | 标签 | 说明 |
|------|------|------|
| 固定 3 项 IA | — | 符合 D-311；首次现场动作足够 |
| 状态：Protected / Paused / Off in app / Not enabled | — | 诚实状态放对地方（扩展而非 Home） |
| mock HTML 有四态 | — | 工程可参照；Hi-fi 仍债 **006** |
| 未订阅 Tap → Open Stillwall 无 IAP | — | 符合 4.4 / D-313 |
| 首次用户如何**找到**扩展 | `intent` + 规格债 | V-002 未验；Help 不得写死未验证路径；**Support 却写了过时/错误成功判据** |

**关键断裂：**  
产品把「坏站恢复」正确放在扩展，但 **Support 仍用「Home = On」当成功标准**，且 App Help 尚无高保真（006）。首次用户会用 Support/商店预期来理解 App——**信任页错了等于教坏用户**。

---

### 2.7 More / Help / Feedback / About（S06–S10）

| 观察 | 标签 | 说明 |
|------|------|------|
| screens 条目方向对 | — | Site broken → 扩展 Pause；YouTube Safari only |
| 缺 Hi-fi | — | **006** |
| 实现易自由发挥 | `drift` 风险 | 无画板时必须死跟 design-system token |
| Help 是恢复路径唯一 App 内入口 | `intent` | 内容必须与 charter 同步；见 **009** |

---

### 2.8 Support / Privacy（信任触点）

#### Support（严重）

| 现状文案（copy + website） | 问题 | 标签 |
|---------------------------|------|------|
| Follow **Set Up Safari Protection** | 弃用 CTA | `store` / 信任 |
| enable **both** Stillwall extensions | 与 6+1 不符 | `store` |
| Home should show protection **On** | **直接违反 D-316** | `store` **P0** |
| If Home does not show On… | 强化错误成功判据 | `store` **P0** |

站点异常、Report、YouTube Safari only、定价段落：**基本正确**，应保留并作为「好的一侧」。

#### Privacy

| 观察 | 标签 | 说明 |
|------|------|------|
| 政策正文与 charter §8 对齐 | — | 无账号、无浏览历史上传、本机规则等 |
| Live URL 已写 yilinglabs.com | — | 好 |
| ASC / description 仍 `<domain>` | `store` | 与 Privacy 正文不一致，上架前统一 |

---

## 3. 设计系统与 Hallmark 向检查

| 检查 | 结果 |
|------|------|
| 单一主色 + 暖金仅 Pro | 通过（意图） |
| 无威胁大数字 / 雷达仪表盘 | 通过（Hi-fi） |
| 单屏单主 CTA | 通过 |
| Home 无状态 pill（意图） | 通过；实现 **001** |
| Setup 预完成金勾 | **失败**（导出） |
| 跨页副文案单一源 | D-510 表已锁；导出/LT 未齐 **005** |
| 扩展与主 App 状态分工 | 模型正确；外围文案破坏模型 |
| 假 UI chrome / 玻璃拟态整页 | 无（好） |
| 对比 Dark CTA | 可接受；发布前抽查 AA |

**不要做的「优化」：**

- 给 Home 加回 On/Off 证明「在工作」  
- 商店截图加「已拦截 12,847 威胁」  
- Welcome 主 CTA 改成 Start Free Trial  
- 扩展塞第 4 个常驻 Open Stillwall / 类别列表  

---

## 4. 发现清单（排序）

### 4.1 已有 issue（对照，不新建）

| ID | 主题 | 本轮结论 |
|----|------|----------|
| **001** | Home 中性 Hero | 仍 P0；Hi-fi 目标正确，实现未达标 |
| **002** | 进度条文案/气质 | 仍 P1；规格已 Hallmark 化 |
| **003** | Setup 深链 + 诚实三步 | 仍 P1；Hi-fi 仍 both extensions / 金勾 |
| **004** | $14.99 + 取消静默 | 仍 P0/P1 |
| **005** | 跨页文案锁 + 导出回写 | 仍 P2 体验；**阻塞商店像素一致性** 时上浮 |
| **006** | 次级页 + 扩展 Hi-fi | 仍 P2；扩展实现前至少要有 SE01 可对稿 |

### 4.2 本轮新建（见 issues）

| ID | 优先级 | 标签 | 摘要 |
|----|--------|------|------|
| **007** | **P0** | `store` | Support（md + website + site 包）废除「Home = On / both extensions / 旧 CTA」；对齐 D-316/D-510 |
| **008** | **P1** | `store` | 商店包装：截图 Welcome CTA、description/review-notes 域名占位 → yilinglabs.com；Setup 成片诚实文案 |
| **009** | **P1** | `intent` | App 内 Help（及可选首次提示）写清恢复路径；禁止写 Home 保护 On；与 T-EXT-07 / V-002 协同 |

### 4.3 仅报告、不单独开 issue（intent-optional）

| 项 | 建议 | 是否动锁 |
|----|------|----------|
| 商店框外 *annoyances blocked* | 可略软化为 fewer / quieter | 可选 |
| Welcome LT Privacy 短式 | 保留 trackers 语义 | 可并入 005 表 |
| Setup 步骤 2 点名 6 个 CB | 降低漏开 | 可选增强 003 |
| 首次进 Home 一次性扩展 Pause tip | 提升可发现性 | 可选；与 009 相关 |
| Battery 文案 *wasteful scripts* | 已够诚实；勿加假续航 % | 保持 |

---

## 5. 建议开发 / 上架顺序

```text
1. 001 Home 中性 Hero + 004 定价/取消     ← 产品正确性
2. 007 Support 信任口径                  ← 对外别教错用户（可并行文案）
3. 002 进度条 + 003 Setup 体验
4. 005 单一文案源（含工程）
5. 008 重导出商店截图 + 换域名 URL
6. 009 Help 文案实现 / 规格钉死
7. 006 次级 + 扩展 Hi-fi（扩展开发前）
```

---

## 6. 模拟用户一句话验收（首发前）

以**第一次装 App 的普通人**过一遍，应全部为「是」：

1. 商店是否让我明白：**只做 Safari、核心免费、Pro 可选**？  
2. Welcome 是否**不逼我试用**就能去设置？  
3. Setup 是否说清楚：**要开很多个 Stillwall 开关 + 网站访问**，而不是含糊「两个扩展」？  
4. 进 Home 后是否看到**可控类别**，而不是假的「全绿 On 监控台」？  
5. 点 Pro 是否看到 **$14.99 / 年 + 试用**，取消购买是否**不吓人**？  
6. 某网站坏了，Support/Help 是否告诉我去 **Safari 扩展 Pause**，而不是「看 Home 是不是 On」？  
7. Privacy 是否与行为一致：**不收集浏览历史、无账号**？  

当前：**意图层 1–5、7 基本可答是；6 为否（Support）；2–5 的实现层仍否（001–004）。**

---

## 7. 文档与资产索引

| 用途 | 路径 |
|------|------|
| 本报告 | `docs/design/journey-polish-review-2026-07-31.md` |
| Hi-fi 导出 | `docs/design/exports/phone-preview/` |
| 商店截图 | `docs/release/app-store-assets/screenshots/` |
| Support 源 | `docs/release/app-store-assets/copy/support-en-US.md` · `website/support/index.html` |
| 文案锁 | `issues/005-cross-screen-consistency/` · D-510 |

---

## 8. 修订

| 日期 | 说明 |
|------|------|
| 2026-07-31 | grilling 锁定 B/3/A/2/C/2/B/1 后执行；新建 007–009 |
