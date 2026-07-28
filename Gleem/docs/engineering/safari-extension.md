# Safari 扩展工程规格（v1）

> **工程事实源（扩展 + 与主 App 共享状态）。** 产品行为以 [design/safari-extension.md](../design/safari-extension.md) 与 [产品总纲领](../product/product-charter.md) 为准。  
> 本文不替代 Xcode 工程；实现不得突破产品 3 项 popup 与隐私边界。

**文档状态：** 初版（2026-07-28）

---

## 1. Targets 与职责

| Target | 类型 | 职责 |
|--------|------|------|
| **Stillwall**（主 App） | iOS App | 引导、全局/类别开关、订阅、Help/Feedback、规则更新编排、扩展状态检测 |
| **Stillwall Content Blocker** | Safari Content Blocker Extension | 声明式 JSON 规则；**无 UI** |
| **Stillwall Web Extension** | Safari Web Extension | **popup 3 项**、Tap 点选、Report 入口、YouTube/X 页面逻辑（无 popup 第四项） |

最低系统：**iOS / iPadOS 26**。  
**不做 v1：** VPN、URL Filter Provider、Mac target 交付。

```text
                    ┌─────────────────────┐
                    │     Main App        │
                    │  StoreKit / UI      │
                    │  RuleUpdater        │
                    └─────────┬───────────┘
                              │ App Group
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
     Content Blocker    Web Extension    (shared files)
     (rules JSON)       popup + scripts  config + tap rules
```

---

## 2. App Group 与配置 schema

### 2.1 约定

| 项 | 决策 |
|----|------|
| App Group ID | 工程创建时锁定，形如 `group.<team>.stillwall`（以最终 Bundle 为准） |
| 配置文件 | 建议单一 JSON：`SharedConfig/v1/config.json`（原子写） |
| 禁止 | UI/扩展直接散落魔法 UserDefaults key 字符串；经 `SharedConfigStore` 读写 |
| 隐私 | **不**存完整浏览 URL path/query 作为默认；Pause 仅 **eTLD+1**；Feedback 仅用户主动提交的域名 |

### 2.2 `SharedConfig`（逻辑 schema）

```json
{
  "schemaVersion": 1,
  "protectionEnabled": true,
  "categories": {
    "ads": true,
    "privacy": true,
    "annoyances": true,
    "regional": true,
    "youtubeAndX": false,
    "batteryBoost": false,
    "strictMode": false
  },
  "pausedRegistrableDomains": [],
  "activeRuleVersion": null,
  "subscription": {
    "tier": "free",
    "expiresAt": null
  }
}
```

| 字段 | 写者 | 读者 | 说明 |
|------|------|------|------|
| `protectionEnabled` | 主 App | CB 管道 / WE / 主 App | 全局开关 |
| `categories.*` | 主 App | 规则编译 / WE | 免费默认 true；Pro 能力默认 false |
| `pausedRegistrableDomains` | **Web Extension**（主） | CB 重载逻辑 / WE | eTLD+1 小写；Pause/Resume |
| `activeRuleVersion` | 主 App RuleUpdater | 诊断 / About | 可选展示 |
| `subscription.tier` | 主 App StoreKit | WE popup Tap 门闸 | `free` \| `trial` \| `pro` \| `expired` |

**Tap 规则**建议独立文件，避免配置膨胀：

```text
SharedConfig/v1/tap-rules.json
```

```json
{
  "schemaVersion": 1,
  "rules": [
    {
      "id": "uuid",
      "domain": "example.com",
      "selector": "...",
      "createdAt": "ISO-8601"
    }
  ]
}
```

- 仅 WE 与（可选）主 App 只读诊断写入。  
- 卸装/清数据可丢；无云同步。

### 2.3 域名规范化

- 输入：当前 tab URL。  
- 输出：registrable domain（eTLD+1），小写，无 scheme/path。  
- `www.example.com` → `example.com`。  
- 无法解析时：Pause 失败并提示（不静默写坏数据）。  
- **单元测试必覆盖** 常见公共后缀与 IDN 策略（实现选定库或系统 API 后固定）。

### 2.4 写入规则

1. 读 → 改 → **临时文件 + replace** 原子提交。  
2. `schemaVersion` 迁移表 + 单测。  
3. Pause 变更后必须 **请求 Content Blocker reload**（及 WE 侧内存状态刷新）。  
4. 主 App 改 `protectionEnabled` / categories 后同样 reload。

---

## 3. Content Blocker

### 3.1 职责

- 根据 **编译后的规则集** 向 Safari 提供 content-blocking JSON。  
- 规则来源：内置基线包 + 更新包 + 类别开关过滤 + **paused 域忽略/放行**。  
- **不**实现 popup；**不**读页面 DOM。

### 3.2 与 Pause 的关系

实现二选一（工程选型后写死，产品效果相同）：

| 策略 | 做法 |
|------|------|
| A. 忽略规则 | 对 `pausedRegistrableDomains` 不注入触发域规则 / 使用 `unless-domain` 类能力（若规则格式支持） |
| B. 放行规则 | 为暂停域生成高优先级 ignore 规则 |

要求：Pause 后该站广告拦截应停止；Resume 后恢复。  
**禁止**因 Pause 导致全局规则文件损坏或假保护。

### 3.3 Reload

主 App 与 WE 在状态变更后调用：

- `SFContentBlockerManager.reloadContentBlocker(withIdentifier:)`

失败：记录本地错误；UI 不得显示 Protected 若 CB 实际未加载（主 App 已有诚实状态原则；扩展顶栏同理尽量对齐）。

---

## 4. Web Extension

### 4.1 表面

| 表面 | 内容 |
|------|------|
| **popup** | 仅 3 项 + 只读顶栏；见产品文档 |
| **background / service worker**（若平台提供） | 消息中继、配置读 |
| **content scripts** | Tap 点选模式、YouTube/X 增强（受开关与订阅约束） |

### 4.2 Popup 状态机（实现枚举）

与产品对齐：

```text
site_protected | site_paused | global_off | not_enabled | permission_needed
```

| 检测 | 来源 |
|------|------|
| 当前 host | `tabs` / 扩展 API 当前页 URL → eTLD+1 |
| 是否 paused | `pausedRegistrableDomains` |
| 全局 | `protectionEnabled` |
| 扩展/CB 可用 | 主 App 写入的 `extensionHealth`（可选）或 WE 自检 + 用户打开 popup 时读配置；**not_enabled** 以「关键扩展未开」为准，与主 App Setup 一致 |
| Pro | `subscription.tier` ∈ {trial, pro} |

### 4.3 三项行为

| 项 | 实现要点 |
|----|----------|
| Pause / Resume | 更新 `pausedRegistrableDomains` → reload CB → 刷新 popup 文案 |
| Tap to Block | `tier` 不足 → 深链主 App（见 §5）；足够 → 向 active tab 发 `startTapMode` |
| Report issue | 扩展内轻量表单 **或** 深链 `stillwall://feedback?domain=&type=`（二选一，实现写死） |

### 4.4 Tap 点选（骨架）

1. content script 进入选择模式（高亮 hover、点击捕获）。  
2. 生成稳定 selector（实现可迭代；失败返回 `couldn't_block`）。  
3. 写入 `tap-rules.json` 并注入 hide 规则 / declarative 补充。  
4. **Undo last：** 栈内最近一条 rule id 可删。  
5. 退出模式：Done 或取消。

**V-005：** 在真机 Safari 验证点选 API 与权限提示后再锁 UI 细节。

### 4.5 YouTube & X

- **无 popup 菜单项。**  
- content script 仅在对应域 + `categories.youtubeAndX` + 订阅允许时启用。  
- 与 CB 规则互补；失败不导致假全局 Protected。

### 4.6 权限（审核向）

- 遵循 **最小 host 权限**；能 optional permissions 则按需请求。  
- 扩展内 **禁止** IAP、营销订阅墙（Guideline 4.4）。  
- 不实现 paywall bypass 脚本或规则。

---

## 5. 与主 App 深链

| URL（建议） | 用途 |
|-------------|------|
| `stillwall://home` | Open Stillwall 默认 |
| `stillwall://setup` | 扩展未启用 |
| `stillwall://upgrade?feature=tap` | 未订阅点 Tap |
| `stillwall://feedback?domain=&type=` | Report 跳转方案 |

URL scheme / Universal Link 以工程配置为准；需在 Info.plist 注册。

---

## 6. 模块边界（建议）

共享（App + Extensions 可见，Swift 包或 shared folder）：

| 模块 | 职责 |
|------|------|
| `SharedConfig` | schema、读写、迁移、域名归一化 |
| `DomainNormalizer` | eTLD+1 |
| `ContentBlockerReloader` | reload 封装 |
| `SubscriptionSnapshot` | 仅快照结构，无 StoreKit 在扩展内 |

主 App only：

| 模块 | 职责 |
|------|------|
| `ProtectionState` | 推导 Home protected/off/needsSetup |
| `RuleStore` / `RuleUpdater` | 规则包 |
| `SubscriptionStore` | StoreKit 2 → 写入 snapshot |

Web Extension：

| 模块 | 职责 |
|------|------|
| `PopupViewModel` | 3 项 + 状态 |
| `TapModeController` | 点选 |
| `ReportFlow` | 反馈 |

---

## 7. 构建与标识（占位）

创建 Xcode 工程时填写并回写本文：

| 项 | 值 |
|----|-----|
| App Bundle ID | _TBD_ |
| Content Blocker Bundle ID | _TBD_ |
| Web Extension Bundle ID | _TBD_ |
| App Group | _TBD_ |
| 主 App ↔ WE 关联 | Xcode Safari Extension 标准配置 |

---

## 8. 测试清单（工程）

| 优先级 | 用例 |
|--------|------|
| P0 | Pause 域后 CB 对该站不拦；Resume 恢复 |
| P0 | 全局 Off 时 popup 不为 Protected |
| P0 | 未订阅 Tap 不进入点选、可打开主 App |
| P0 | config 原子写与 schema 迁移单测 |
| P1 | Tap 成功 hide + Undo last |
| P1 | youtube.com 仅在开关+订阅时跑增强脚本 |
| P1 | Report 预填 domain、无自动上传历史 |

对照站点：[quality/safari-test-sites.md](../quality/safari-test-sites.md)。

---

## 9. 实现顺序建议

1. App Group + `SharedConfig` + 域名归一化 + 单测  
2. Content Blocker 基线规则 + reload  
3. Web Extension popup 三态（Protected / Paused / Not enabled）+ Pause/Resume  
4. 主 App 写 `protectionEnabled` / 订阅快照  
5. Report 深链或表单  
6. Tap mode（依赖 V-005）  
7. YouTube/X scripts  

---

## 10. 关联

| 文档 | 关系 |
|------|------|
| [design/safari-extension.md](../design/safari-extension.md) | 产品 3 项与文案 |
| [engineering/ios-client.md](ios-client.md) | 主 App targets 与状态 |
| [decision-log](../decisions/decision-log.md) | D-311～D-314、T-EXT-* |

## 11. 修订

| 日期 | 说明 |
|------|------|
| 2026-07-28 | 初版：targets、App Group schema、CB/WE、深链、实现顺序 |
