# Gleem 项目文档

> `Gleem` 当前仅为内部项目代号，不是最终公开品牌名。候选公开名称需要在招募公开测试用户前完成 App Store 重名、域名和目标市场商标核查。

## 1. 文档目的

本目录是 Gleem 产品、设计、研发、规则、隐私、测试、发布和运营工作的统一事实来源。除 Apple API、代码标识符、产品文案等专用名词外，文档统一使用中文，方便中国开发团队协作。

如文档之间出现冲突，按以下优先级处理：

1. [决策记录](decisions/decision-log.md)中状态为“已确认”的决策。
2. [产品定义](product/product-definition.md)与[范围和商业模式](product/scope-and-business.md)。
3. 对应专业分类下的详细设计。
4. 尚未验证的建议、候选方案和开放问题。

## 2. 当前里程碑

当前目标是在两周内发布私有 TestFlight。该版本验证 Safari 免费拦截体验，不包含正式收费和跨 App URL Filter。

两周版本的核心能力：

- iPhone/iPad，最低 iOS/iPadOS 26。
- Safari 广告与追踪器拦截。
- YouTube Safari 专项拦截。
- X Safari Promoted Posts 拦截。
- Cookie consent、Open in App、Newsletter 和反广告拦截提示。
- `All Quiet / One Quick Step / Paused` 可信且低负担的保护状态。
- 网站放行、临时暂停、自动规则更新和用户主动反馈。

商业正式版在 Apple 相关能力准备完成后增加：

- 基于 `NEURLFilterManager` 的 Pro 跨 App URL 过滤。
- 美国区 `$19.99/年`，7 天免费试用，支持 Family Sharing。

## 3. 文档导航

### 产品

- [产品定义](product/product-definition.md)：目标用户、问题、价值主张、定位和成功标准。
- [范围和商业模式](product/scope-and-business.md)：免费/Pro 边界、里程碑范围、定价与获客。

### 设计

- [设计原则与视觉规范](design/design-system.md)：品牌人格、视觉语言、组件、动效和无障碍要求。
- [App 完整流程](design/app-flow.md)：统一覆盖 TestFlight、正式付费、扩展设置、规则更新、放行、反馈和故障恢复。
- [App 流程视觉稿](design/Gleem-App-Flows.free)：Lunacy 可编辑源文件；[PDF 预览](design/Gleem-App-Flows.pdf)。
- [信息架构与用户流程](design/user-flows.md)：页面结构与关键流程摘要；详细逻辑以 App 完整流程为准。

### 工程

- [系统架构](engineering/system-architecture.md)：客户端、扩展、规则服务与未来 PIR 的边界。
- [iOS 客户端设计](engineering/ios-client.md)：Targets、状态模型、数据共享、权限和失败处理。
- [后端与规则交付](engineering/backend-and-delivery.md)：清单、签名、缓存、回滚和零数据约束。

### 数据与拦截规则

- [拦截规则系统](rules/filtering-rules.md)：规则分类、来源、编译、专项脚本、质量门槛和更新流程。

### 隐私、安全与合规

- [隐私、安全与合规](privacy/privacy-security-compliance.md)：零数据承诺、权限、数据流、供应链和审核要求。

### 质量

- [测试与验收](quality/test-and-acceptance.md)：测试分层、站点矩阵、失败场景和发布门槛。

### 发布

- [两周 TestFlight 计划](release/two-week-testflight-plan.md)：每日里程碑、依赖、风险和降级顺序。

### 运营

- [支持与事故响应](operations/support-and-incidents.md)：漏拦/误杀反馈、规则修复、严重等级和响应流程。

### 决策

- [决策记录](decisions/decision-log.md)：已确认决策、待验证事实和明确不做事项。

## 4. 统一术语

| 术语 | 含义 |
| --- | --- |
| 主 App | 用户从 App Store/TestFlight 安装并直接打开的 SwiftUI App |
| Content Blocker | 不读取网页内容，由 Safari 执行声明式规则的内容拦截扩展 |
| Gleem Extra | 仅访问 `youtube.com` 和 `x.com` 的可选 Safari Web Extension |
| Safari 保护 | Content Blocker 与 Gleem Extra 在 Safari 内提供的拦截能力 |
| Pro 保护 | 正式商业版中基于 URL Filter 的跨 App 过滤能力 |
| 干扰项 | Cookie consent、Open in App、Newsletter、自动播放和 anti-adblock 提示 |
| 放行 | 对指定网站暂时或长期停止相关拦截 |
| 规则包 | 经过编译、校验、签名后交付给客户端的一组规则 |
| PIR | Private Information Retrieval，URL Filter 使用的隐私查询机制 |

## 5. 文档维护规则

- 产品范围变化必须先更新决策记录，再更新受影响文档。
- “已完成”“已验证”只能用于真实运行或测试通过的内容。
- 未完成的 Apple entitlement、商标、许可证和审核事项必须保持“待验证”状态。
- 不在文档中写入密钥、Token、证书、真实用户数据或私有服务凭据。
- 公开文案不得承诺原生 YouTube/X App 广告完全消失。
