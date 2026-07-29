# iOS 主客户端工程纲要（v1）

> 与现行总纲领对齐的**主 App**工程摘要。扩展细节见 [safari-extension.md](safari-extension.md)。  
> 归档旧版在 `docs/archive/.../engineering/ios-client.md`，含 Pause 时长/跨 App 等**已废弃**方案，勿混用。

**文档状态：** 初版（2026-07-28）

---

## 1. 技术基线

| 项 | 决策 |
|----|------|
| 语言 / UI | Swift · SwiftUI |
| 最低系统 | iOS / iPadOS **26** |
| 设备 | iPhone、iPad |
| 并发 | Swift Concurrency |
| 订阅 | StoreKit 2（正式收费阶段） |
| 共享 | App Group `group.com.lingyi.stillwall`（见 [identifiers-and-entitlements.md](identifiers-and-entitlements.md)） |
| Bundle | `com.lingyi.stillwall`（+ `.blocker` / `.extension`） |
| 分析 / 崩溃 SDK | v1 **不接**第三方 |

---

## 2. Targets（阶段 A）

| Target | 职责 |
|--------|------|
| Main App | Welcome / Setup / Home / More / Upgrade / Feedback |
| Content Blocker Extension | 声明式拦截 |
| Safari Web Extension | popup 3 项 + Tap + YT/X |
| Unit Tests | SharedConfig、域名、状态推导 |
| UI Tests | 门禁、类别开关、Upgrade 入口（可选阶段） |

阶段 B（非 v1）：URL Filter 等见决策 S-001。

---

## 3. 主 App 模块

| 模块 | 职责 |
|------|------|
| `Onboarding` | Welcome + Setup 门禁 |
| `ProtectionState` | 由 facts 推导 `protected` / `off` / `needsSetup` |
| `SharedConfigStore` | 读写 App Group（与扩展共用） |
| `ExtensionStatusChecker` | CB / WE 是否启用 |
| `RuleStore` / `RuleUpdater` | 规则包下载、校验、reload |
| `SubscriptionStore` | StoreKit → `subscription` 快照 |
| `Feedback` | 用户主动反馈 + 预览 |

**原则：**

- 视图不直接拼 UserDefaults key。  
- **无**主 App Allowlist UI、**无**定时 Pause controller。  
- 本站 Pause 集合由扩展维护；主 App 不展示名单。

---

## 4. Protection 呈现（Home）

| 呈现 | 条件 |
|------|------|
| `needsSetup` | CB 或 WE 未开 |
| `protected` | 授权完成 + 任一类别开关 On（派生 `anyCategoryEnabled`） |
| `off` | 授权完成 + 全部类别开关 Off |

不把「某站 paused」算作 Home off；Home 不显示 per-site 状态（避免双 UI）。**无** `protectionEnabled` 用户开关。

---

## 5. 与扩展协作

| 主 App 动作 | 扩展侧效果 |
|-------------|------------|
| 切换类别 | 写 categories → reload CB（按变更类别增量编译优先） |
| 订阅变化 | 写 `subscription` → popup Tap 门闸变化 |
| Setup 完成 | 用户可打开 popup 三态正常路径 |
| 打开 `stillwall://…` | 路由到 Setup / Upgrade / Feedback |

| 扩展动作 | 主 App |
|----------|--------|
| Pause/Resume 域 | 主 App 无 UI；下次打开无需同步名单页 |
| Report 深链 | 打开 Feedback 并预填 |

---

## 6. 实现顺序（主 App + 扩展并联）

见 [safari-extension.md §9](safari-extension.md)。主 App 可先：

1. SwiftUI 壳 + 门禁状态机  
2. App Group 写入类别开关  
3. Extension 状态检测  
4. StoreKit 快照  
5. 规则更新管道  

---

## 7. 修订

| 日期 | 说明 |
|------|------|
| 2026-07-28 | 按现行总纲领重建；去掉归档方案中的定时 Pause / App 名单 |
| 2026-07-29 | 移除全局保护开关（D-315）；状态由类别开关派生 |
