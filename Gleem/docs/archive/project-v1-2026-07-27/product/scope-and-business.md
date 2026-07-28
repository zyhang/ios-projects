# 范围与商业模式

> **已归档（2026-07-27，project-v1）**：本文属于全量文档快照的一部分，不再作为现行权威。见 [归档说明](../README.md)。重构请写到 `docs/`。

## 1. 版本分层

项目分为三个阶段，不允许跨阶段偷带范围。

### 1.1 阶段 A：两周私有 TestFlight

目标是验证免费 Safari 产品体验与规则质量。

包含：

- 英文 SwiftUI 主 App。
- iPhone/iPad，最低 iOS/iPadOS 26。
- 首次启用引导。
- `All Quiet / One Quick Step / Paused` 状态。
- Safari 基础广告与追踪器拦截。
- YouTube Safari 专项拦截。
- X Safari Promoted Posts 拦截。
- 干扰项拦截。
- 网站放行与临时暂停。
- 自动规则更新。
- 本地诊断导出。
- `Missed Ad / Site Broken` 主动反馈。
- Pro 页面和年订阅方案预览。

不包含：

- `NEURLFilterManager`、PIR 和跨 App 实际过滤。
- 真实订阅收费。
- 正式 App Store 发布。
- 原生 YouTube/X App 专项能力。
- 自定义规则、Tap to Block。
- 拦截统计和节省流量估算。
- 账号、iCloud 同步。

### 1.2 阶段 B：Pro 技术验证

进入条件：

- Apple URL Filter/OHTTP relay 相关能力可用于分发签名构建。
- PIR 数据集、服务器和隐私边界完成技术验证。
- 在真实设备上完成 URL Filter 失败、离线和回滚测试。

包含：

- 基于 `NEURLFilterManager` 的跨 App URL 过滤。
- Pro 状态与权限引导。
- App/网站放行策略。
- StoreKit 测试环境订阅。
- Pro 试用与恢复购买。

### 1.3 阶段 C：正式商业发布

进入条件：

- Pro 技术验证通过。
- 隐私政策、支持页面和服务条款准备完成。
- 最终品牌完成基础商标、App Store 和域名核查。
- Beta App Review 与正式 App Review 资料准备完成。
- 规则源许可证确认并保留证据。

## 2. 免费版与 Pro 边界

### 2.1 免费版

免费版永久提供完整 Safari 体验：

- 广告与追踪器拦截。
- YouTube Safari 专项拦截。
- X Safari Promoted Posts 拦截。
- Cookie consent、Open in App、Newsletter、anti-adblock 等干扰项。
- 自动规则更新。
- 网站放行与临时暂停。
- 状态自检和主动反馈。

### 2.2 Pro

Pro 只解决一个清晰问题：

> 在不替换 VPN 或 DNS 的前提下，将广告与追踪请求过滤扩展到更多 App。

不通过隐藏基础 Safari 能力制造付费墙。

## 3. 定价

### 3.1 已确认方案

- 仅年订阅，不提供月订阅。
- 美国区首发价：`$19.99/年`。
- 7 天免费试用，绑定年订阅。
- 支持 Family Sharing。
- 不提供终身买断。
- 其他市场使用 App Store 对应价格档位。

### 3.2 定价页面原则

- 只展示一个付费选项。
- 清楚说明免费 Safari 功能不会因未订阅而失效。
- 试用开始前显示试用结束日期、续费价格和取消方式。
- 不使用倒计时、虚假折扣、预选同意或其他 dark patterns。
- TestFlight 阶段只能预览，不得让测试者误以为已经产生真实收费。

## 4. 获客策略

### 4.1 首批用户来源

- 英文落地页与 TestFlight waitlist。
- Reddit：`r/iOS`、`r/Safari`、`r/privacy` 等允许相关内容的社区。
- X 上关注 Apple、Safari 和隐私工具的用户。
- Product Hunt 和独立开发者社区。
- 已公开表达对 Wipr、AdGuard、Magic Lasso 不满意的用户讨论。

任何社区发布前必须检查版规，不进行伪装用户、批量私信或垃圾推广。

### 4.2 暂不采用

- Apple Search Ads。
- 广泛付费社交广告。
- 购买评论、榜单或虚假下载。
- 依赖“拦截所有原生 App 广告”的误导宣传。

## 5. 商业验证

### 5.1 首轮样本

- 目标用户：100 人。
- Pro 试用：至少 30 人。
- 年订阅：至少 10 人。

### 5.2 数据来源

由于坚持零数据收集：

- 下载、试用和订阅数据使用 App Store Connect 聚合信息。
- TestFlight 激活和故障体验依赖用户主动反馈与访谈。
- 不接入第三方漏斗、归因或 session replay。

### 5.3 继续投入条件

满足以下条件才扩大投入：

- 达到或接近付费验证线。
- 用户反馈确认跨 App 保护是明确付费理由。
- 规则维护与 PIR 基础设施成本可控。
- 没有不可接受的审核、隐私或网络稳定性问题。

## 6. 明确不做

- Android、Windows、Mac、Apple TV、Vision Pro 首发支持。
- VPN、代理和地域解锁服务。
- 家长控制与成人内容过滤。
- 恶意软件或反钓鱼产品承诺。
- 用户画像、广告归因和精细行为分析。
- 原生 YouTube/X App 广告完全拦截。
- 为了功能数量复刻 Magic Lasso 的统计、自定义规则和全平台能力。
