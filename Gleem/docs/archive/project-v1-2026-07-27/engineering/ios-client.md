# iOS 客户端设计

> **已归档（2026-07-27，project-v1）**：本文属于全量文档快照的一部分，不再作为现行权威。见 [归档说明](../README.md)。重构请写到 `docs/`。

## 1. 技术基线

- Swift 与 SwiftUI。
- 最低 iOS/iPadOS 26。
- 支持 iPhone、iPad。
- 使用 Swift Concurrency。
- 使用 StoreKit 2（正式订阅阶段）。
- 使用 App Group 共享最小状态。
- 使用 CryptoKit 验证规则签名和哈希。

具体 Xcode/Swift 小版本在项目创建时按当前稳定工具链锁定，文档不提前伪造。

## 2. 建议 Targets

| Target | 阶段 | 职责 |
| --- | --- | --- |
| Main App | A | SwiftUI UI、状态、规则更新、反馈 |
| Content Blocker Extension | A | Safari 声明式拦截 |
| Safari Web Extension | A | YouTube/X 页面级增强 |
| Unit Tests | A | 状态、规则、签名、归一化 |
| UI Tests | A | 引导、暂停、反馈、Pro Preview |
| URL Filter Control Provider | B | 获取并配置 URL Filter 数据 |

是否拆分额外模块以实际代码复杂度为准，不为了架构形式提前拆包。

## 3. 模块边界

建议逻辑模块：

- `ProtectionState`
- `RuleStore`
- `RuleUpdater`
- `AllowlistStore`
- `PauseController`
- `ExtensionStatus`
- `DiagnosticsBuilder`
- `SubscriptionStore`（阶段 B/C）

原则：

- UI 不直接读写 UserDefaults key。
- 扩展和主 App 使用同一套 Codable 数据模型。
- 状态计算集中，避免各页面自行解释。
- 不引入不必要的第三方状态管理库。

## 4. ProtectionState

建议事实模型：

```swift
struct ProtectionFacts {
    var contentBlockerEnabled: Bool
    var extraYouTubeAccess: PermissionState
    var extraXAccess: PermissionState
    var rulePackageState: RulePackageState
    var pauseState: PauseState
    var urlFilterState: URLFilterState?
    var subscriptionState: SubscriptionState?
}
```

由 facts 推导 UI：

```swift
enum ProtectionPresentation {
    case protected
    case actionNeeded(RecoveryAction)
    case paused(until: Date?)
}
```

规则：

- 可选 Extra 未授权不应让基础 Safari 状态变成完全未保护。
- 多个错误同时存在时按用户可修复性排序。
- 不使用网络事件计数影响状态。

## 5. 设置存储

App Group 中建议使用单一版本化配置：

```json
{
  "schemaVersion": 1,
  "pauseUntil": null,
  "allowlistedDomains": [],
  "youtubeEnhancementEnabled": true,
  "xEnhancementEnabled": true,
  "activeRuleVersion": "2026.07.26.1"
}
```

要求：

- 写入采用原子替换。
- schema migration 有单元测试。
- 域名在进入存储前做规范化。
- 不允许存储完整 URL path 或 query，除非未来有明确决策。

## 6. 规则更新

客户端更新顺序：

1. 获取小型 manifest。
2. 验证 manifest 签名与 schema。
3. 比较版本、最低 App 版本和发布时间。
4. 下载目标规则包。
5. 验证 SHA-256、大小和签名。
6. 在临时位置解析与预检。
7. 原子切换 active package。
8. 请求 Content Blocker reload。
9. reload 成功后记录最后成功版本。
10. 失败时回退上一版本。

触发时机：

- App 启动进入前台。
- 用户手动检查更新。
- `BGAppRefreshTask` 尽力执行。
- 系统不保证后台执行，UI 不得把“已安排”当成“已更新”。

## 7. Allowlist

### 7.1 域名规范化

- 统一小写。
- 移除尾随点。
- 支持 IDN/Punycode。
- 使用可靠 Public Suffix List 逻辑确定 registrable domain。
- 拒绝无效 host、IP 特殊值和空字符串。

### 7.2 生效

- 基础 Content Blocker 需要生成包含 `unless-domain`/对应排除规则的有效规则包并 reload。
- Gleem Extra 在内容脚本执行前读取 allowlist。
- 更新必须原子生效。

## 8. 暂停

- 使用绝对到期时间存储。
- App 与扩展每次读取时判断是否到期。
- 到期后清理状态并恢复。
- 全局暂停不能删除规则包。
- `Until I resume` 使用显式无到期状态。

## 9. Gleem Extra

### 9.1 权限

- manifest 只声明 YouTube/X 必要 host。
- 不申请任意网站读取权限。
- 不把权限授予与订阅绑定。

### 9.2 脚本设计

- YouTube 与 X 分开模块和测试夹具。
- 使用 MutationObserver 时限制观察范围并做节流。
- DOM 操作幂等，重复执行不产生空容器或布局抖动。
- 对未知页面结构 fail open。
- 不读取登录信息、私信、表单内容或用户发布内容。
- 不发送页面数据。

## 10. 诊断

本地诊断只包含：

- App/build、系统版本、设备类别。
- 扩展版本和授权状态。
- 规则版本、哈希前缀、更新时间和校验结果。
- pause/allowlist 是否影响当前域名。
- 最近一次规则更新错误的枚举和时间。

不包含：

- 浏览历史。
- 其他访问域名。
- 页面 HTML。
- 网络 payload。
- 广告标识符。

## 11. StoreKit

阶段 A：

- 只展示 Pro Preview。
- 可准备 StoreKit Configuration 做本地 UI 测试。
- 不在 TestFlight 向用户声称已收费。

阶段 B/C：

- 产品只有一个年订阅。
- 使用 StoreKit 2 entitlement 作为客户端事实来源。
- 支持恢复购买与 Family Sharing。
- 购买成功不等于 URL Filter 已启用。
- 试用、续费、到期和退款状态都需要测试。

## 12. UI 与线程要求

- 系统状态读取和规则更新不阻塞主线程。
- UI 状态变更在 MainActor。
- 取消离开页面后的无意义任务。
- 不用无限 spinner；长任务必须有明确状态。
- 网络失败提供重试，不自动高频轮询。
