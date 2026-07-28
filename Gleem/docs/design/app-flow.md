# App 完整流程

> **逻辑事实源（流程）。** 功能范围以 [产品总纲领](../product/product-charter.md) 为准；页面级摘要见 [user-flows.md](user-flows.md)、[screens.md](screens.md)。  
> UI 文案英文；本说明用中文。

---

## 1. 目标与原则

> 用户完成必要系统授权后，不需要持续管理 App；再次打开时，一眼确认状态即可离开。

| 原则 | 流程含义 |
|------|----------|
| 少步骤 | Welcome → 一次授权引导 → Home |
| 门禁诚实 | 未完成 Safari 拦截授权 **不得** 进入 Home |
| 先价值后付费 | 免费核心先生效；Pro 从能力行进入 |
| 平台分工 | **站点 Pause/Resume、Tap、Report 在 Safari 扩展 popup（仅 3 项）**；主 App 只有 **全局 On/Off** + 类别开关 |
| 假保护为零 | 扩展被关、全局关闭时，主 App 与扩展顶栏必须说真话 |

---

## 2. 全局状态机

### 2.1 应用根状态

```text
Cold Start
  → 首次？ → Welcome → Setup
  → 授权校验
        ├─ 未通过 → 模态 Setup（挡 Home）
        └─ 通过 → Home
              ├── 全局开关 On  → 按类别开关拦截
              ├── 全局开关 Off → 不拦截（状态 Off）
              ├── 系统关掉扩展 → 模态 Setup
              └── Pro 行（free）→ Upgrade
```

### 2.2 保护呈现状态（Home 顶部）

| 呈现状态 | 条件 | 用户理解 |
|----------|------|----------|
| `needsSetup` | Content Blocker 或 Web Extension 未开 | 门禁 / 模态 Setup |
| `protected` | 授权完成 + 全局开关 On | 保护中 |
| `off` | 授权完成 + 全局开关 Off | 保护已关闭 |
| `degraded` | 可选：无可用规则基线 | 需修复；不得假装正常 |

**已移除：** 主 App `paused` 定时暂停状态、Pause 时长（15m / 1h / Until resume）。

**本站 Pause（仅扩展）：** 见 [safari-extension.md](safari-extension.md)；与全局 Off 不同——全局关一切，本站 Pause 只放行当前 eTLD+1。

### 2.3 全局开关

| 字段 | 说明 |
|------|------|
| `protectionEnabled` | bool；默认 `true` |
| Off 时 | 所有类别拦截不生效 |
| On 时 | 按 Ads / Privacy / … 各自开关 |

### 2.4 订阅状态

| 状态 | 含义 |
|------|------|
| `free` / `trial` / `pro` / `expired` | 同前；Pro 能力仅 trial/pro 可开 |

---

## 3. 主流程

### 3.1 首次启动

```text
[Welcome] 长页卖点 → 主按钮 Enable Safari Blocking
    → [Setup] 一次叙事：Content Blocker + Web Extension
    → 检测通过 → Home（全局 On，免费类别默认 On）
```

主按钮 **不是** Start Free Trial。

### 3.2 再次启动

```text
已 onboarding → 检测授权 → 通过则 Home（protected 或 off）/ 失败则模态 Setup
```

### 3.3 Home 日常

```text
状态区：protected | off + 全局开关
能力列表：Ads … Tap to Block
More → 次级页

关全局 → off
开全局 → 按类别生效
点 Pro（free）→ Upgrade
点 Tap → 说明页（Safari 中使用；站点设置亦在扩展）
```

### 3.4 误杀 / 站点例外（不在主 App 名单）

```text
站点异常
  → 推荐：Safari → Stillwall 扩展 popup → Pause on this site
  → 备选：Home 关闭全局开关（或关 Strict / 相关类别）
  → 可选：扩展 Report issue 或 App Feedback
  → 恢复本站：扩展 Resume on this site
```

**主 App 无：** Allowed Sites 页、Pause sheet、15m/1h 选项。  
**扩展 popup 仅 3 项：** 见 [safari-extension.md](safari-extension.md)。

### 3.5 升级 / Feedback / 规则更新 / 扩展被关

与前版相同逻辑：Upgrade 非首次门禁；Feedback 可预览；规则静默更新；扩展被关 → 模态 Setup。

---

## 4. Home 能力列表

| 顺序 | 行 | 类型 | 说明 |
|------|-----|------|------|
| — | 全局保护 | Switch（状态区） | On/Off |
| 1–4 | Ads / Privacy / Annoyances / Regional | Switch | 免费，默认 On |
| 5–7 | YouTube & X / Battery / Strict | Switch | Pro |
| 8 | Tap to Block | 入口行 | Pro；说明在 Safari 使用 |

全局 Off 时：类别开关可仍显示，但拦截不生效；状态区强提示 Off。

---

## 5. 数据（流程相关）

| 数据 | 位置 |
|------|------|
| onboarding、全局开关、类别开关 | 本机 App Group |
| Tap 规则 | 本机（扩展读写） |
| 本站 Pause 集合（eTLD+1） | **扩展侧 / App Group**；主 App 无名单 UI |
| 订阅 | StoreKit（扩展只读权益） |

---

## 6. 错误与边界

| 场景 | 行为 |
|------|------|
| 授权不全 | 门禁 Setup；扩展 popup 示 Not enabled → Open Stillwall |
| 购买取消 | 保持 free |
| 规则更新失败 | 保留可用包；不假保护 |
| 用户找「放行某站」 | 扩展 **Pause on this site**；Help 指向扩展；无 App 内名单死路 |

---

## 7. 与设计交付

线框：Lunacy `Stillwall Wireframes v1`（主 App；已去掉 Pause/Allow 画板）。  
扩展：Lunacy 另开 SE01–SE03（待画）；规格 [safari-extension.md](safari-extension.md)。  
修订时同步 [user-flows.md](user-flows.md)、[screens.md](screens.md)、总纲领。
