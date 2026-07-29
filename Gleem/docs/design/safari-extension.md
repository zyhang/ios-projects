# Safari 扩展产品面（v1）

> **逻辑事实源（扩展侧）。** 范围与边界以 [产品总纲领](../product/product-charter.md) 为准；主 App 流程见 [app-flow.md](app-flow.md)。  
> **UI 文案：英文。** 本说明用中文。  
> **文档状态：** 已确认（2026-07-28：popup 固定 3 项）

---

## 1. 角色与原则

| 面 | 角色 |
|----|------|
| 主 App | 授权门禁、**类别开关**、只读状态、订阅、Help / Feedback 完整页（**无**全局总开关） |
| **Safari Web Extension popup** | **当前站点**情境：放行/恢复、Tap to Block、Report |

### 原则

1. **选项尽量少：常态固定 3 个可点项**（硬上限 5；v1 不凑满）。  
2. 扩展 = 浏览中 3–10 秒完成的动作，不是第二套 Home。  
3. **本站 Pause / Resume** 是站点控制的**唯一操作面**（主 App 无 Allowed Sites）。  
4. 状态必须诚实：扩展未开、主 App 全部类别 Off 时不得显示 Protected。  
5. 扩展内 **无 IAP、无订阅营销墙**（App Store 4.4）；未订阅点 Pro 能力 → 回主 App。  
6. 不做 Custom Rules 编辑器、不做定时 Pause 时长、不做 paywall bypass。

### 平台入口（文案约束）

- 用户从 **Safari 中的 Stillwall Web Extension** 打开 popup（具体系统入口随 iOS/iPadOS 版本变化）。  
- 主 App Help / Tap 说明须描述「在 Safari 中打开 Stillwall 扩展」，**不得**写死未经验证的图标位置（见决策 V-002）。  
- **Content Blocker 无独立 UI**；用户可点的菜单属于 Web Extension。

---

## 2. Popup 信息架构（固定 3 项）

### 2.1 常态布局

```text
┌────────────────────────────────┐
│  example.com                   │  ← 当前 host（只读，不算菜单项）
│  Protected                     │  ← 或 Paused / 其他状态文案
├────────────────────────────────┤
│  1  Pause on this site         │  ← 与 Resume 同一槽位切换
│  2  Tap to Block               │
│  3  Report issue               │
└────────────────────────────────┘
```

| # | 菜单项（英文） | ID | 层级 | 说明 |
|---|----------------|-----|------|------|
| 1 | **Pause on this site** / **Resume on this site** | E-01 | 免费 | 本站拦截开关；同一槽位按状态切换文案 |
| 2 | **Tap to Block** | E-02 | Pro | 进入页内点选；未订阅 → 引导 Open Stillwall |
| 3 | **Report issue** | E-03 | 免费 | 反馈；预填当前域名 |

**只读顶栏（不算第 4 项）：** 当前 host + 状态短语。

### 2.2 明确不放进 popup

| 不做 | 去哪 |
|------|------|
| 类别开关（Ads/…） | 主 App Home（**无**全局总开关） |
| Ads / Privacy / Annoyances / Regional / Strict / Battery 列表 | 主 App Home |
| Open Stillwall 常驻第 4 行 | 仅降级态 / 未订阅路径出现 |
| 定时 Pause（15m / 1h） | 不做 |
| 已放行站点完整名单 | v1 不做；Resume 只针对当前站 |
| 拦截数量 / Performance Insights | 不做 |
| 扩展内购买 / 试用 CTA 墙 | 主 App Upgrade |

---

## 3. 状态模型

### 3.1 Popup 呈现状态

| 状态 ID | 条件 | 顶栏状态文案（方向） | 三项如何表现 |
|---------|------|----------------------|--------------|
| `site_protected` | 授权可用 + 至少一个类别 On + 本站未 Pause | Protected | ① Pause on this site · ② Tap · ③ Report |
| `site_paused` | 授权可用 + 至少一个类别 On + 本站已 Pause | Paused | ① **Resume on this site** · ② Tap · ③ Report |
| `all_categories_off`（原 `global_off`） | 授权可用 + 主 App **全部类别 Off** | Off in app | ① 禁用或改为 **Open Stillwall**（仍只占槽 1）· ②③ 仍可点（Report 可用；Tap 可说明需先开保护） |
| `not_enabled` | CB 或 Web Extension 系统侧未开 / 不可用 | Not enabled | **整页降级**：主 CTA **Open Stillwall**（可视为仅 1 个操作，不展示完整 3 项） |
| `permission_needed` | Tap 等需要额外网站权限且未授 | Needs access | 引导系统授权；成功后回 `site_protected` / `site_paused` |

### 3.2 本站 Pause 语义（已确认）

| 项 | 决策 |
|----|------|
| 作用 | 对当前站点**停止** Stillwall 拦截（Content Blocker + 相关扩展行为对该站不生效） |
| 作用域 | **eTLD+1**（`www.example.com` 与 `example.com` 视为同一站；工程实现须一致） |
| 持久化 | **直到用户 Resume**（非 session-only；无 15m/1h UI） |
| 与类别关系 | 全部类别 Off → 全部不拦；有类别 On + 本站 Pause → 仅该站不拦 |
| 存储 | 本机（扩展 / App Group）；**不上传**浏览历史；v1 **无云同步** |
| 主 App | **无**名单 UI；不在 Home 展示完整 allowlist |

### 3.3 与主 App 共享状态（逻辑字段）

| 字段 | 读/写 | 说明 |
|------|--------|------|
| `categories` / 派生 `anyCategoryEnabled` | 扩展只读 | 类别开关；**无**用户全局开关字段 |
| `sitePauseSet` | 扩展读写 | 已 Pause 的 eTLD+1 集合 |
| `subscription` | 扩展只读 | free / trial / pro / expired → 是否解锁 Tap |
| `tapRules` | 扩展读写 | 用户点选规则，仅本机 |
| 类别开关 / Strict 等 | 扩展不展示 | 由主 App 写入；拦截管道消费 |

实现细节（App Group、reload 规则）见后续工程文档；**不得**因同步延迟长期显示假 Protected。

---

## 4. 功能规格

### 4.1 E-01 Pause / Resume on this site（免费）

**Pause**

- 将当前站加入本站 Pause 集合并立即对该站停止拦截。  
- 顶栏变为 Paused；菜单项文案变为 **Resume on this site**。  
- 若页面仍异常，用户可手动刷新（Help 可一句提示 Reload if needed）。

**Resume**

- 从 Pause 集合移除当前站；恢复按已开启类别的拦截。  
- 顶栏变为 Protected。

**不做：** 选择时长、仅本次访问、批量管理多站列表（v1）。

### 4.2 E-02 Tap to Block（Pro）

**已订阅（trial / pro）**

1. 用户点 **Tap to Block**。  
2. 关闭或收起 popup → 进入**当前页**点选模式。  
3. 用户点页面元素 → 生成屏蔽规则（本机）并即时反馈。  
4. 提供退出点选模式（Done / 系统或页内明确出口）。  
5. 失败：无法选中或规则无效时提示，例如 *Couldn't block this element*（文案可微调）。  
6. **Undo：** v1 至少支持撤销**上一次**成功屏蔽，或退出点选前取消；细节实现可迭代，产品要求「点坏了能收回」。

**未订阅**

- 不进入点选。  
- 简短说明 + **Open Stillwall**（进主 App Upgrade / Tap 说明），**不在扩展内拉起 IAP**。

**不做：** CSS 选择器编辑器、规则列表大全、云同步。

### 4.3 E-03 Report issue（免费）

**目的：** 误杀、漏拦等主动反馈；域名预填降低摩擦。

**最小流程：**

1. 点 **Report issue**。  
2. 选择类型（建议固定少量）：  
   - Site broken  
   - Still seeing ads  
   - Other  
3. 域名：默认当前 eTLD+1 / host，**可编辑**。  
4. 可选短备注。  
5. **发送前预览**（对齐主 App Feedback / D-605）。  
6. 提交：用户主动；不静默上传浏览历史。

实现可选：扩展内轻量表单，或深链打开主 App Feedback 并带入 host + 类型。**产品要求路径短**；二选一由工程定，须在实现文档写死一种。

**不做：** 自动抓取完整 URL 路径与页面正文作为默认行为；扩展内客服聊天。

---

## 5. 关键用户流程

### 5.1 站点异常（误杀）

```text
Safari 页面异常
  → 打开 Stillwall 扩展 popup
  → Pause on this site
  → （如需）用户刷新页面
  → 可选 Report issue（Site broken）
```

### 5.2 恢复本站拦截

```text
popup（Paused）→ Resume on this site → 拦截恢复
```

### 5.3 Tap to Block

```text
popup → Tap to Block
  ├─ 未 Pro → 说明 + Open Stillwall
  └─ 已 Pro → 页内点选 → 屏蔽 / 失败提示 / 可撤销
```

### 5.4 扩展未启用

```text
打开 popup → Not enabled → Open Stillwall
  → 主 App 门禁 / Setup 引导系统设置
```

### 5.5 主 App 全部类别 Off

```text
popup 顶栏 Off in app
  → 槽 1 引导 Open Stillwall 打开保护
  → 或用户自行打开主 App 类别开关
```

---

## 6. 与主 App 职责对照

| 能力 | 主 App | 扩展 popup |
|------|--------|------------|
| 类别开关（**无**全局总开关） | ✅ 唯一控制面 | 只读 / 引导回 App |
| 本站 Pause / Resume | ❌ | ✅ 唯一操作面 |
| Tap 说明页 | ✅（S05） | ❌ 说明可极短 |
| Tap 点选 | ❌ | ✅ |
| Report / Feedback | ✅ 完整（More） | ✅ 三项之一（预填域名） |
| 订阅 | ✅ | 仅 Open Stillwall |
| YouTube & X 开关 | ✅ | ❌（脚本侧行为，无单独菜单项） |

---

## 7. 文案方向（英文）

| 场景 | 文案方向 |
|------|----------|
| 顶栏保护中 | Protected |
| 顶栏本站暂停 | Paused |
| 顶栏全部类别 Off | Off in app |
| 顶栏未启用 | Not enabled |
| 槽 1 保护中 | Pause on this site |
| 槽 1 已暂停 | Resume on this site |
| 槽 2 | Tap to Block |
| 槽 3 | Report issue |
| 降级主按钮 | Open Stillwall |
| Tap 未订阅 | 短说明 + Open Stillwall |
| Tap 失败 | Couldn't block this element |

最终文案可在线框中微调，**三项标签语义不得扩成更多主操作**。

---

## 8. 线框 / 页面 ID

| ID | 内容 | 状态 |
|----|------|------|
| **SE01** | Popup 常态（3 项 + 顶栏） | **Lunacy 已画** |
| **SE01a** | Popup · Paused（槽 1 = Resume） | **Lunacy 已画** |
| **SE01b** | Popup · 降级 Not enabled | **Lunacy 已画** |
| **SE01c** | Popup · Off in app | **Lunacy 已画** |
| **SE02** | Tap 点选模式（页内） | **Lunacy 已画** |
| **SE03** | Report issue 流程 | **Lunacy 已画** |

| 交付物 | 路径 |
|--------|------|
| 线框蓝图（尺寸/组件） | [extension-wireframes-se.md](extension-wireframes-se.md) |
| 浏览器可预览 mock | [extension-popup-mock.html](extension-popup-mock.html) |
| 工程 schema / Targets | [../engineering/safari-extension.md](../engineering/safari-extension.md) |

Lunacy：建议单独页「Safari Extension v1」；入库后更新 T-EXT-05。

主 App 相关：

| ID | 关联 |
|----|------|
| S05 | Tap 说明：三步指向扩展三项中的 Tap |
| S07 Help | Site broken → 扩展 Pause；含如何打开扩展（V-002 验证后补截图级步骤） |

---

## 9. 验收要点

1. 常态 popup **可见可点主操作 ≤ 3**（Pause/Resume · Tap · Report）。  
2. 误杀站可仅用 **Pause on this site** 恢复可用性（对照 [safari-test-sites](../quality/safari-test-sites.md) 购物/新闻站）。  
3. Paused 后再 **Resume** 恢复拦截。  
4. 全部类别 Off / 扩展未开时**不**显示 Protected。  
5. 未订阅点 Tap **不**在扩展内购买；能到达主 App。  
6. Report 预填域名、发送前可预览、无静默浏览历史上传。  
7. YouTube/X 无第四个菜单项；行为由 Home 开关 + 扩展脚本完成。

---

## 10. 关联文档

| 文档 | 关系 |
|------|------|
| [产品总纲领](../product/product-charter.md) §5.8–5.10、§14 | 范围与 TODO 收敛 |
| [decision-log](../decisions/decision-log.md) | D-309、D-310、D-311 等 |
| [app-flow.md](app-flow.md) | 主 App 状态机；扩展补充见本文 |
| [user-flows.md](user-flows.md) | 用户意图入口 |
| [screens.md](screens.md) | SE01–SE03 |
| [safari-test-sites.md](../quality/safari-test-sites.md) | 误杀回归 |

---

## 11. 修订记录

| 日期 | 说明 |
|------|------|
| 2026-07-28 | 初版：popup 固定 3 项；Pause 持久 eTLD+1；Tap / Report；降级态 |
| 2026-07-28 | 链路线框蓝图、HTML mock、engineering/safari-extension |
