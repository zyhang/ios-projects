# 信息架构与用户流程

> 本文保留页面级摘要。完整状态分支、阶段标签和跨系统流程以 [App 完整流程](app-flow.md) 为准。

## 1. 导航结构

首版建议使用简单层级，不使用多 Tab dashboard。

```text
App
├── Overview
│   ├── Protection Status
│   ├── Safari Protection
│   ├── YouTube & X
│   ├── Block Annoyances
│   └── Pro Preview
├── Allowlist
├── Support
│   ├── Report Missed Ad
│   ├── Report Broken Site
│   ├── Export Diagnostics
│   └── Privacy
└── About
    ├── Rule Version
    ├── App Version
    └── Acknowledgements
```

首版可以通过 NavigationStack 从 Overview 进入二级页面，不需要底部 Tab Bar。

## 2. 首次启用流程

### 2.1 目标

- 先让 Safari 免费保护生效。
- 在用户看到价值后再介绍 Pro。
- 权限请求与用户理解保持同步。
- 不一次性要求所有权限。

### 2.2 推荐流程

```text
A1 Welcome
  ↓ Set Up Safari Protection
A2 One Toggle in Settings
  ↓ Open Settings（深链到 Safari Extensions）
用户开启 Stillwall + All Websites
  ↓ 返回 App，自动检测
  ├── 未启用 → A3 仍未开启（同页状态提示，仅可再次 Open Settings）
  └── 已启用 → A4 All Quiet → 进入 Overview / Home
        ↓
可选：一键启用 Enhanced Protection
  ↓
合并检测 YouTube 与 X 必要权限
        ↓
Overview
```

**门禁：** 未完成免费 Safari Protection 授权前不得进入 Home / Overview。不提供 `I'll do this later`；否则后续功能没有意义。

### 2.3 权限说明

Content Blocker：

- 强调 Safari 负责执行规则。
- 说明基础扩展不能查看或上报浏览内容。
- 对用户说结果（打开 Safari Extensions、打开 Stillwall），不暴露 Shortcuts 实现细节。

Enhanced Protection（技术实现为 Gleem Extra）：

- 在请求权限前说明为什么需要页面访问。
- 明确权限只覆盖 YouTube 和 X。
- 允许用户跳过；跳过不影响基础 Safari 保护。
- 与 Safari Protection 不同：基础授权不可跳过，Enhanced 可跳过。

### 2.4 失败处理

- 用户从 Settings 返回时自动重新检查。
- 不循环弹出权限请求。
- **不提供** `I'll do this later` / `Finish Later` 跳过首次 Safari 授权。
- 未开启时留在 One Toggle（A3 状态可见：`Still off · We'll keep checking`）。
- 若系统状态无法准确判断，显示 `Check Settings` / 仍未开启态，不伪装为 `All Quiet`。

## 3. Overview 状态

### 3.1 All Quiet

条件：

- Content Blocker 已启用。
- 本地规则包存在且通过完整性校验。
- 规则未超过失效阈值。
- 当前不在全局暂停中。

显示：

- `All Quiet`
- `Safari is protected with the latest available rules.`
- 次级显示 YouTube & X 是否完整启用。

### 3.2 One Quick Step

可能原因：

- Content Blocker 未启用。
- 规则包签名或哈希失败。
- 规则长时间未更新。
- 扩展 reload 失败。
- 未来 Pro 过滤器异常或未授权。

规则：

- 只展示当前最优先的一个修复动作。
- 详情页可列出其他次要问题。
- 不把可选 Enhanced Protection 未启用视为基础保护故障。

### 3.3 Paused

暂停类型：

- 全局暂停。
- 当前网站放行。
- 定时暂停。

显示：

- 暂停范围。
- 自动恢复时间。
- `Resume Now`。

暂停到期必须本地自动恢复，不能依赖服务器。

## 4. 网站放行

### 4.1 入口

- 主 App Allowlist 页面。
- Gleem Extra 的 Safari toolbar action。
- 页面异常反馈流程中的快速放行建议。

### 4.2 行为

- 默认按 registrable domain 放行，如 `news.example.com` 归一化为 `example.com`。
- 用户可看到并删除所有放行项。
- 放行影响基础 Safari 与 Gleem Extra 时，需要明确说明。
- 首版不提供复杂 URL path 级规则。

## 5. 临时暂停

建议选项：

- 15 minutes
- 1 hour
- Until tomorrow
- Until I resume

原则：

- 默认突出短期选项。
- 暂停后立即更新状态。
- 到期时间存储在本地，并能跨进程读取。
- 系统时间变化后重新计算，不无限延长。

## 6. YouTube/X 专项流程

### 6.1 未授权

Overview 中显示：

- `Enhanced Protection: Off`
- 说明开启后可增强 YouTube 与 X 的动态广告处理。
- 用户只看到一个开启动作，不分别理解两个域名权限。

### 6.2 已授权

- 只有两项必要权限都有效时才显示 `Enhanced Protection: On`。
- 任一权限缺失时统一显示 `Setup Needed`，不显示部分开启。
- 不显示具体浏览记录或拦截次数。
- 提供一次关闭整个 Enhanced Protection 的入口。

### 6.3 专项规则失效

- 远程 feature flag 可停用单个 site module。
- 停用后降级到基础 Content Blocker。
- 不因专项脚本异常阻塞页面主要内容。

## 7. Pro 预览与未来订阅

### 7.1 TestFlight

- 可打开 Pro 介绍页。
- 标注 `Preview — not available in this beta`。
- 不触发真实购买。
- 可以展示未来权限流程，但不能伪造已保护状态。

### 7.2 正式版

```text
用户理解免费 Safari 价值
  ↓
打开 Pro
  ↓
查看跨 App 能力和限制
  ↓
确认 $19.99/year + 7-day trial
  ↓
StoreKit 购买
  ↓
请求 URL Filter 授权
  ↓
本地验证过滤状态
  ↓
All Quiet
```

副文案说明 `Safari and supported apps are covered.`。购买成功但系统过滤未启用时，状态应为 `One Quick Step`，不能显示完整保护。

## 8. 反馈流程

### 8.1 Missed Ad

```text
选择 Missed Ad
  ↓
确认域名
  ↓
可选说明/截图
  ↓
查看将发送的诊断字段
  ↓
用户确认后通过 App 内反馈 API 提交
```

### 8.2 Site Broken

在发送反馈前先临时允许当前网站并自动刷新，询问网站是否恢复。恢复后再提供可选兼容性报告；未恢复时撤销测试并提交更详细结果。

### 8.3 默认诊断字段

- 当前域名。
- App 版本/build。
- iOS/iPadOS 版本。
- 设备型号类别。
- Content Blocker 状态。
- Gleem Extra 版本和授权状态。
- 规则版本与生成时间。
- 暂停/放行状态。

不得包含完整浏览历史、其他域名、请求内容或设备广告标识符。

## 9. 空状态与异常文案

| 场景 | 文案目标 |
| --- | --- |
| Allowlist 为空 | 解释通常无需放行，出现页面异常时再添加 |
| 离线无法更新 | 继续使用上一个有效规则包，说明稍后重试 |
| 规则损坏 | 回退内置规则并提示修复，不让用户失去全部保护 |
| 反馈服务不可用 | 保存本地草稿；恢复网络后仍需用户再次确认，不自动发送 |
| Pro 未开放 | 清楚标记 preview，不诱导购买 |
