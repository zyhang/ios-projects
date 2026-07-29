# Identifiers · App Groups · Entitlements（Stillwall v1）

> **已锁定（2026-07-28）：** Team 前缀、主 Bundle、App Group 与能力勾选。  
> 在 [Apple Developer → Identifiers](https://developer.apple.com/account/resources/identifiers/list) 与 Xcode Targets 中按本文配置。  
> 产品范围：主 App + Safari Content Blocker + Safari Web Extension + StoreKit 年订。

| 项 | 值 |
|----|-----|
| Team ID / App ID Prefix | `NV2PNGX854` |
| 主 Bundle ID | `com.lingyi.stillwall` |
| App Group | `group.com.lingyi.stillwall` |
| 最低系统 | iOS / iPadOS 26 |

---

## 1. 三个 Explicit App ID

全部使用 **Explicit**（不要 Wildcard）。Description 可用下表「门户 Description」列。

| # | 门户 Description | Bundle ID | 用途 |
|---|------------------|-----------|------|
| 1 | Stillwall | `com.lingyi.stillwall` | 主 App（SwiftUI） |
| 2 | Stillwall Content Blocker | `com.lingyi.stillwall.blocker` | Safari Content Blocker Extension |
| 3 | Stillwall Web Extension | `com.lingyi.stillwall.extension` | Safari Web Extension |

扩展 Bundle **必须**是主 Bundle 的前缀 + 后缀（上表已满足）。

### 1.1 主 App：`com.lingyi.stillwall`

**Capabilities 勾选：**

| Capability | 勾选 | 配置 |
|------------|------|------|
| **App Groups** | ✅ | 勾选 `group.com.lingyi.stillwall` |
| **In-App Purchase** | ✅ | 无需额外子配置 |
| 其它列表项 | ❌ | 见 §4 黑名单 |

### 1.2 Content Blocker：`com.lingyi.stillwall.blocker`

**Capabilities：**

| Capability | 勾选 | 配置 |
|------------|------|------|
| **App Groups** | ✅ | 同一 `group.com.lingyi.stillwall` |
| Content Blocker / Safari Content Blocker（若门户列出） | ✅ | 按列表名称勾选 |
| In-App Purchase | ❌ | 购买只在主 App |
| 其它 | ❌ | — |

> 若门户扩展 ID 上**没有**单独的 Content Blocker 勾选项：仍创建该 App ID + App Groups，在 **Xcode** 的 Content Blocker target 中启用能力并签名即可（见 §3）。

### 1.3 Web Extension：`com.lingyi.stillwall.extension`

**Capabilities：**

| Capability | 勾选 | 配置 |
|------------|------|------|
| **App Groups** | ✅ | 同一 `group.com.lingyi.stillwall` |
| Safari Web Extension（若门户列出） | ✅ | 按列表名称勾选 |
| In-App Purchase | ❌ | — |
| 其它 | ❌ | — |

---

## 2. App Group

| 字段 | 值 |
|------|-----|
| Identifier | `group.com.lingyi.stillwall` |
| Description | Stillwall Shared |
| 挂载到 | 上述 **3 个** App ID 全部勾选 |

共享数据约定见 [safari-extension.md §2](safari-extension.md)（`SharedConfig` schema）。

---

## 3. Xcode Targets 与 Entitlements

### 3.1 Target 对照

| Target 名（建议） | Bundle ID | 类型 |
|-------------------|-----------|------|
| `Stillwall` | `com.lingyi.stillwall` | iOS App |
| `StillwallBlocker` | `com.lingyi.stillwall.blocker` | Content Blocker Extension |
| `StillwallExtension` | `com.lingyi.stillwall.extension` | Safari Web Extension |

Signing：Automatic，Team `NV2PNGX854`，各 target 选对应 App ID。

### 3.2 `Stillwall.entitlements`（主 App）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.lingyi.stillwall</string>
	</array>
</dict>
</plist>
```

In-App Purchase **不**需要单独 entitlement 键；开启 Capability 后由系统/签名处理。

### 3.3 `StillwallBlocker.entitlements`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.lingyi.stillwall</string>
	</array>
</dict>
</plist>
```

Content Blocker 的扩展类型由 **Info.plist / NSExtension** 声明（`com.apple.Safari.content-blocker`），不一定再多一条门户专用 entitlement 键；以 Xcode 生成模板为准。

### 3.4 `StillwallExtension.entitlements`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.lingyi.stillwall</string>
	</array>
</dict>
</plist>
```

Safari Web Extension 的 `NSExtensionPointIdentifier` 等以 Xcode Safari Web Extension 模板为准。

### 3.5 主 App Info.plist（摘要）

| Key | 说明 |
|-----|------|
| `CFBundleDisplayName` | `Stillwall` |
| `CFBundleIdentifier` | `com.lingyi.stillwall` |
| 嵌入扩展 | Embed Content Blocker + Safari Web Extension |

加密合规（ASC 已定）：仅标准 HTTPS → 常见 `ITSAppUsesNonExemptEncryption` = **NO**（以法务最终确认）。

### 3.6 StoreKit Product ID（与 ASC 对齐）

| 用途 | Product ID |
|------|------------|
| 年订 Pro | `com.lingyi.stillwall.pro.yearly` |
| ASC Reference Name | `pro_yearly_1499` |
| Display Name | Stillwall Pro (Yearly) |

详见 [app-store-submission.md](../release/app-store-submission.md)。

---

## 4. 明确不要开的 Capabilities（三端共用黑名单）

与 v1 总纲领冲突或用不上：

- Personal VPN  
- Network Extensions  
- Sign In with Apple  
- iCloud（含 CloudKit / iCloud Documents）  
- Push Notifications（v1 未做远程推送；规则更新用拉式即可）  
- Associated Domains（暂无）  
- Game Center / HealthKit / HomeKit / Wallet / Apple Pay  
- Family Controls / MDM / DriverKit / Background GPU 等无关项  

以后若加 Push 或 Associated Domains，先改总纲领 / 决策记录再开能力。

---

## 5. Developer 门户操作顺序（检查清单）

### 5.1 Identifiers

- [ ] **Register App Group**  
  - ID: `group.com.lingyi.stillwall`  
  - Description: `Stillwall Shared`  

- [ ] **Register App ID — Main**  
  - Description: `Stillwall`  
  - Bundle: `com.lingyi.stillwall`  
  - ✅ App Groups → 勾选 `group.com.lingyi.stillwall`  
  - ✅ In-App Purchase  

- [ ] **Register App ID — Blocker**  
  - Description: `Stillwall Content Blocker`  
  - Bundle: `com.lingyi.stillwall.blocker`  
  - ✅ App Groups → 同一 group  
  - ✅ Content Blocker（若有）  

- [ ] **Register App ID — Web Extension**  
  - Description: `Stillwall Web Extension`  
  - Bundle: `com.lingyi.stillwall.extension`  
  - ✅ App Groups → 同一 group  
  - ✅ Safari Web Extension（若有）  

### 5.2 Profiles（若不用 Xcode Automatic）

- [ ] Development + Distribution：主 App、Blocker、Extension 各一套（或让 Xcode 自动管理）

### 5.3 App Store Connect

- [ ] 新建 App，Bundle ID 选 `com.lingyi.stillwall`  
- [ ] IAP：`com.lingyi.stillwall.pro.yearly`  
- [ ] 元数据见 release 包  

### 5.4 Xcode

- [ ] 三 target Bundle ID 与上表一致  
- [ ] 三 target 均启用 App Groups → `group.com.lingyi.stillwall`  
- [ ] 主 App 启用 In-App Purchase  
- [ ] 主 App Embed 两个扩展  
- [ ] 真机：Settings → Safari → Extensions 可见两项  

---

## 6. 深链（可选，后续）

若实现 `stillwall://` 打开 Setup / Upgrade / Feedback：

- 主 App URL Types：`stillwall`  
- **不必**为此单独开 Associated Domains  
- 扩展 Report → 主 App 深链见 [safari-extension.md](safari-extension.md)

---

## 7. 与文档交叉引用

| 文档 | 关系 |
|------|------|
| [ios-client.md](ios-client.md) | 主 App targets / 模块 |
| [safari-extension.md](safari-extension.md) | App Group schema、popup、CB/WE |
| [app-store-submission.md](../release/app-store-submission.md) | 商店名、IAP 文案 |
| 产品总纲领 | 能力边界；改能力前先改总纲领 |

---

## 8. 修订

| 日期 | 说明 |
|------|------|
| 2026-07-28 | 锁定 `com.lingyi.stillwall` 三 ID + `group.com.lingyi.stillwall`；主 App 仅 App Groups + IAP |
