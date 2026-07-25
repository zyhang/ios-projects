# Welcome 设计 — Gleem

> **归档（design-v1-2026-07-25）**：非现行权威。重设计工作区见 [`docs/design/`](../../design/)。

状态：**已封存（v1）**  
范围：仅首次启动 Welcome（非 Home、非 Enable 设置、非 App Store listing）。  
界面语言：**英文**。受众：海外重视隐私用户（`AGENTS.md` 规则 0–2）。  
说明语言：**中文**。

相关：[wireframes/screens.md](../../wireframes/screens.md) · [hi-fi.html](hi-fi.html) · [tokens.md](tokens.md)

---

## 1. 目的

Welcome 在约 30 秒内回答一个问题：

> **这是什么，值不值得继续？**

必须建立：

1. **品类** — 广告/追踪拦截（网页更安静）  
2. **范围 / 楔子** — Safari **以及** 其他 App（相对纯 Safari 工具的主差异）  
3. **信任** — 浏览留在设备（在系统权限与购买之前必需）  

必须**不要**：

- 讲完整品牌故事  
- 教完整 Settings 路径  
- 解释规则包、名单管线或 URL Filter / PIR 黑话  
- 在理解价值前就硬付费墙  

---

## 2. 结论（Gleem 最佳实践）

| 结论 | 理由 |
|------|------|
| **3 页足够** | 更多页往往重复「我们人很好」而信息增量低；3 页可覆盖品类 + 范围 + 信任而不疲劳。 |
| **视觉优先，一行文案** | 工具类靠可一眼读懂的隐喻转化，不是长文。契合极简产品语气（Wipr 级冷静）。 |
| **Welcome ≠ 设置向导** | 启用 Safari / URL Filter 放在意图明确后的独立 Enable 页（通常也在解锁后）。设备相关 Settings 文案随系统变。 |
| **Welcome ≠ About** | 独立、无可接受广告、长隐私政策 → About / 商店描述。最多由信任页插画**暗示**。 |
| **比 Wipr 的沉默略多一点** | 我们不是 incumbent；需要一次清晰的 **Safari & apps** 信号。不需要三页口号。 |
| **允许 Skip** | 重装 / Family Sharing 第二台设备不应强制完整推销。 |
| **只展示一次**（直到重置） | 持续状态在 Home（`You're protected.` / `Safari blocking is off.`）。 |
| **动效辅助** | 慢循环展示状态变化；尊重 **Reduce Motion**（仅最终平静帧）。 |

### 成功标准（用户离开时应知道）

Welcome 结束后，用户应能说出：

1. 它拦截广告/追踪，让网页更安静。  
2. 它在 Safari **和** App 里都工作。  
3. 它不收集他们去哪浏览。  

此阶段不要求：价格算术、包名、如何开关扩展。

---

## 3. 设计原则

1. **每页一个主意** — 不要跨页重复「信任」长独白。  
2. **主视觉 / 轻动效承载含义；标题确认它。**  
3. **标题 ≤ 约 5 个英文词**。优先**没有**正文段。W2 仅在需要时可选 micro 行。  
4. **主 CTA 仅在流程末尾**（`Get Started`）。中间页：`Continue`。  
5. Welcome **无**功能 bullet 列表。  
6. **无**手动更新名单相关文案（产品全局自动）。  
7. **付费墙在 Welcome 之后**（Unlock sheet / Home locked）— 不是 Welcome 第 1 页。  
8. **冷静审美** — 暖纸画布、 accent 绿、无杀毒红、无 VPN 霓虹（[tokens.md](tokens.md)）。  

---

## 4. 推荐方案：3 页

### 总览

| 页 | 任务 | 视觉意图 | 标题（EN） | CTA（EN） |
|----|------|----------|------------|-----------|
| **W1** | 品类 / 收益 | 页面变安静；广告/噪音块缓慢消散 | **Without the noise.** | Continue |
| **W2** | 范围 / 楔子 | Safari（或浏览器）标记 + App 格子，安静相连 | **Safari & Apps.** | Continue |
| **W3** | 信任 + 下一步 | 数据留在设备内；云被弱化/拒绝上传 | **Stays on your device.** | **Get Started** |

W2 下可选 micro（仅在需要时）：`One purchase. No subscription.` — 明确一次购买覆盖 Safari **和** apps，无额外收费。

页指示：圆点 `● ○ ○` 风格；W1–W2 可选 **Skip**（落到 Home locked 或末页 — 产品选择；默认建议：Skip → Home / 解锁路径，不再播完全部动画）。

### 为何此顺序

1. **噪音优先** — 通用、情绪化、品类清晰。  
2. **Safari & apps 第二** — 注意力仍高时抛出差异点；不埋在三页哲学之后。  
3. **隐私在行动前最后** — 解锁 + 系统权限前建立信任；与 `Get Started` 配对。  

### 相对早期 4 页理念明确删掉的

| 不再单独成页 | 改放何处 |
|--------------|----------|
| 长「为你而建 / 不为广告商」essay | About、商店描述；W3 可选插画细节 |
| 「无可接受广告」说教 | About / listing |
| 功能 bullet（包、自动名单、非 VPN） | W2 视觉暗示 apps；「非 VPN」在 **Enable apps**；包在 More |
| 完整设置步骤 | O2 / O3 Enable 流程 |

---

## 5. 分页规格

### W1 — Without the noise.

| 项 | 规格 |
|----|------|
| **用户带走** | 这通过去掉广告/噪音让浏览更安静。 |
| **视觉** | 风格化内容页；广告/噪音块在慢循环中淡出或缩小。内容行保留。 |
| **动效** | 2.5–3.5s 循环；ease-in-out；无刺眼闪烁。 |
| **文案** | 仅标题：`Without the noise.` |
| **不出现** | Tracker 黑话、续航声称、竞品名。 |

### W2 — Safari & Apps.

| 项 | 规格 |
|----|------|
| **用户带走** | 保护不限于 Safari；App 也包含。 |
| **视觉** | 两极清晰：浏览器/Safari 隐喻 + App 图标格；两者间有细微「受保护」连接。 |
| **动效** | 轻浮或连接强调；避免图标轰炸（mock 最多 4 个 App 块）。 |
| **文案** | 标题：`Safari & Apps.` · 可选 micro：`One purchase. No subscription.` |
| **不出现** | URL Filter、VPN 对比长文、系统版本要求（放 Help / Enable）。 |

### W3 — Stays on your device.

| 项 | 规格 |
|----|------|
| **用户带走** | Gleem 不收割浏览；数据留本地。 |
| **视觉** | 设备框；活动点留在内部；云弱化或划掉。 |
| **动效** | 点在原处脉冲；无粒子流离开设备。 |
| **文案** | 仅标题：`Stays on your device.` |
| **CTA** | `Get Started` → Unlock（O4）或延后 Home locked（H3），按商业流程。 |
| **页脚** | 安静 `Privacy Policy` 文字链可。 |
| **不出现** | PIR、Bloom filter、法律长墙（仅链出）。 |

---

## 6. 流程

```
First launch
  → W1 → W2 → W3
       ↘ Skip (optional) ──────────────┐
  → Get Started                        │
  → Unlock (O4)  [Not now → H3]        │
  → Enable Safari / Apps when ready    │
  → Home                               ←┘
```

规则：

- Welcome **不**内嵌完整 Enable 教程。  
- 回访用户：不再展示 Welcome（除非 debug / 重置）。  
- 购买恢复在 Unlock 与 More — Welcome 上不强制。  

---

## 7. Welcome 上不得出现的内容

- 规则包名与开关（Core / Annoyances / Strict）  
- 手动 “update blocklist”  
- 多段独立宣言  
- Settings 面包屑教程（`Settings → Apps → Safari → …`）  
- UI 内与 Wipr 比价  
- 拦截次数 / 假数据  
- 账号注册  

---

## 8. 无障碍与平台

| 主题 | 要求 |
|------|------|
| **Reduce Motion** | 无循环动画；展示最终「平静 / 受保护 / 本地」状态。 |
| **VoiceOver** | 每页：有意义的无障碍标签 = 标题 + 短图像描述（如 “Illustration: ads fading from a webpage. Without the noise.”）。 |
| **Dynamic Type** | 标题保持短一行；避免打乱布局的长文。 |
| **iPad / Mac** | 同样 3 个主意与顺序；更大 hero，同样英文文案。不为 Mac 加额外 Welcome 页。 |

---

## 9. 实现备注（产品 / 工程）

- 优先 **矢量 / Lottie / SwiftUI canvas**，而非重视频（体积 + Reduce Motion）。  
- 艺术应 **定制且冷静**，非库存「盾牌 VPN」陈词滥调。  
- 插画体系与 [tokens.md](tokens.md) 一致（暖纸、 accent 绿）。  
- 界面文案 **EN-first**；无中文市场 onboarding 模式。  

---

## 10. 未决小选择

| 主题 | 默认建议 | 备选 |
|------|----------|------|
| Skip 控件 | W1–W2 显示 Skip | 无 Skip（强制看完 3 页一次） |
| W2 micro 行 | `One purchase. No subscription.` | 省略；依赖 Unlock sheet |
| Get Started 目标 | 先 Unlock sheet | Home locked + Unlock CTA |
| W1 品牌标 | 插画上可选小 Gleem wordmark | 仅标题，无 wordmark |

高保真打磨时解决；均不改变 **3 页信息架构**。

---

## 11. 修订历史

| 日期 | 变更 |
|------|------|
| 2026-07-24 | 初稿：3 页视觉优先 Welcome；来自设计讨论的结论；取代 4 页偏文案的理念向。 |
| 2026-07-24 | hi-fi.html 同步：去掉 “Built for you.” 页，顺序改为噪音 → Safari & apps → on-device；Get Started / One purchase / Privacy Policy 等到位；Skip；pill 圆点；hero 与编排动效；Reduce Motion 最终帧。 |
| 2026-07-24 | 评审修复：标题不再强制大写；W1 噪音改为带标签弹窗 + AD 横幅；W3 虚线上传路径与划掉的云；micro 文案调整。 |
| 2026-07-24 | 文案：标题 `Safari & Apps.`；micro `One purchase. No subscription.` 移到 W2。 |
| 2026-07-24 | 动效评审：删 W2 环境漂浮；信号路径对齐 24px 链接；W3 上升点可见窗口加宽；按钮 `:active` 反馈。 |
| 2026-07-25 | 说明改中文；用户可见文案仍为英文（语言约定 `AGENTS.md` 规则 0）。 |
