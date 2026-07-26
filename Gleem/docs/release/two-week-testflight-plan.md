# 两周 TestFlight 发布计划

## 1. 交付目标

在 14 个自然日内完成一个可安装、可真实测试的 iPhone/iPad 私有 TestFlight MVP，用于验证：

- 用户是否愿意启用并长期保留 Safari 广告拦截。
- YouTube Safari、X Safari 和常见 annoyances 是否构成明显差异化价值。
- 用户是否理解免费能力与未来 Pro 的边界。
- 是否有足够用户愿意开始 7 天试用，并最终为每年 `$19.99` 付费。

首个 TestFlight 不接入真实订阅购买，不包含 `NEURLFilterManager`、Private Information Retrieval 或原生 App 广告拦截。Pro 只展示经明确标注的 Preview。

## 2. 第 14 天“发布”的定义

两周目标受 Apple 构建处理和 Beta App Review 影响，因此分为两个可验证状态：

1. 必须达成：候选构建已上传 App Store Connect，可供内部测试，外部测试资料已准备并提交。
2. 期望达成：Apple 审核通过，指定的私有外部测试者可安装。

不能控制的 Apple 审核等待不视为研发失败，但必须提前提交，避免把审核工作留到最后一天。

## 3. MVP 范围

### 3.1 必须交付

- iOS/iPadOS 26 App。
- Safari Content Blocker。
- 基础广告和追踪器拦截。
- YouTube Safari 增强拦截。
- X Safari Promoted Posts 隐藏。
- Cookie consent、Open in App、newsletter、anti-adblock 等 annoyances 的首批规则。
- Gleem Extra Safari Web Extension，仅请求 youtube.com 与 x.com 权限。
- 首页真实状态：`Protected`、`Action Needed`、`Paused`。
- 单站点 Allowlist。
- 临时暂停和自动恢复。
- 签名规则更新、校验失败保留旧版本、回滚能力。
- `Missed Ad` 与 `Site Broken` 用户主动反馈。
- Pro Preview 和清晰的能力边界。
- 隐私、权限、TestFlight 测试说明。

### 3.2 明确不做

- 真实 StoreKit 订阅与收据校验。
- 月订阅、终身买断或账号系统。
- `NEURLFilterManager`、PIR、VPN、DNS 服务。
- 原生 YouTube、X App 广告拦截承诺。
- Android、macOS、其他浏览器。
- 云端同步、跨设备账号。
- 用户行为分析 SDK 和广告归因 SDK。
- 本地化；首发产品界面为英文。

## 4. 工作角色

即使由一人或少量成员兼任，也应按职责检查：

| 职责 | 主要产出 |
| --- | --- |
| 产品 | 范围、优先级、文案边界、测试者招募 |
| iOS | App、Content Blocker、Web Extension、状态与配置 |
| 规则 | 上游清单评估、编译、自有规则、回归与回滚 |
| 设计 | 关键流程、视觉系统、图标与商店素材 |
| QA | 设备矩阵、真实站点、隐私抓包和发布验收 |
| 运营 | TestFlight 说明、反馈处理、已知问题和测试者沟通 |

AI 编程工具可以缩短实现与排查时间，但不能替代 Apple 审核、真实设备行为、规则许可证核查和品牌法律核查。

## 5. 14 天日程

### Day 1：冻结产品边界与工程骨架

- 确认本文的必须交付和不做清单。
- 创建 App、Content Blocker、Gleem Extra targets。
- 定义 App Group、Bundle ID、Signing 和构建配置。
- 确认内部代号与对外名称分离。
- 立即开始 App Store 名称、商标和规则许可证核查。

退出条件：工程可在模拟器和至少一台真机安装；各 target 能被系统识别。

### Day 2：完成状态模型与开启引导

- 实现 `Protected`、`Action Needed`、`Paused` 状态机。
- 实现 Safari 扩展开启说明和状态刷新。
- 建立 App Group 配置结构。
- 完成首页低保真流程与英文核心文案。

退出条件：用户可以按引导完成基础扩展开启，App 展示真实状态而非模拟结果。

### Day 3：接入首批基础规则

- 选定候选上游规则并记录版本、来源、许可证。
- 建立规则编译、去重、分片和格式校验。
- 生成首个可加载的 Safari Content Blocker 规则包。
- 在新闻、内容和工具类站点完成冒烟测试。

退出条件：基础广告和追踪器在真机 Safari 中有可观察效果，主要内容仍可用。

### Day 4：完成规则更新安全链路

- 定义 Manifest、规则包哈希和 Ed25519 签名。
- 实现下载、验证、原子替换和重载。
- 实现损坏包拒绝与上一版本保留。
- 建立 staging 与 production 规则通道。

退出条件：成功更新、断网、损坏文件、签名错误和版本回退场景均有验证结果。

### Day 5：Allowlist 与暂停

- 实现站点域名标准化和 Allowlist。
- 实现临时暂停、明确到期时间和自动恢复。
- 处理配置变更后的扩展重载。
- 完成设置页基础结构。

退出条件：一个站点可以独立恢复原始行为，暂停到期后保护自动恢复。

### Day 6：YouTube Safari

- 实现 YouTube 专用规则和必要的 Gleem Extra 页面逻辑。
- 覆盖首页、搜索、播放页和站内导航。
- 验证未登录与测试账号登录状态。
- 为不支持场景准备准确限制文案。

退出条件：定义内场景有效；脚本异常不会导致页面无法播放或无限刷新。

### Day 7：X Safari 与 annoyances

- 实现 X Promoted Posts 识别与隐藏。
- 覆盖时间线、搜索和帖子详情。
- 接入首批 cookie consent、Open in App、newsletter、anti-adblock 规则。
- 验证动态内容加载和无限滚动。

退出条件：推广内容处理有效，正常帖子、滚动和详情交互不被破坏。

### Day 8：设计精修与可访问性

- 将界面收敛为冷静、优雅、Apple-native 的视觉语言。
- 补齐空状态、错误状态、加载状态和权限状态。
- 检查 Dynamic Type、VoiceOver、深浅色和 Reduce Motion。
- 准备 App 图标和 TestFlight 基础素材。

退出条件：核心流程无占位设计，关键操作在 iPhone 和 iPad 均清晰可用。

### Day 9：反馈与诊断

- 实现 `Missed Ad` 与 `Site Broken`。
- 只生成用户确认过的最小诊断信息。
- 完成暂停、Allowlist、关闭 Gleem Extra 的定位引导。
- 定义 Issue 标签和处理流程。

退出条件：反馈可达团队，且抓包确认不会静默上传浏览数据。

### Day 10：Pro Preview 与产品文案

- 展示未来 App-wide protection 的价值和边界。
- 明确标注 Preview、尚不可购买。
- 写明未来计划：`$19.99/year`、7 天试用、Family Sharing；最终商店价格仍需发布前确认。
- 删除所有月订阅和原生 YouTube/X 保证文案。

退出条件：测试者能分清当前免费能力、未来 Pro 能力和暂未交付内容。

### Day 11：完整回归与性能基线

- 执行设备、站点、状态和网络异常矩阵。
- 测量启动、更新、内存和规则包体积。
- 执行隐私抓包验证。
- 分类 P0 至 P3 问题。

退出条件：无未定位的 P0；P1 有负责人和当天处理计划。

### Day 12：修复与发布候选

- 只处理阻断发布和明显影响核心价值的问题。
- 冻结新功能和大范围规则扩张。
- 生成 Release Candidate。
- 完成回滚演练和已知问题清单。

退出条件：所有 P0、P1 已关闭；P2 均有是否接受的明确决定。

### Day 13：上传与审核准备

- 上传 App Store Connect。
- 完成 Export Compliance、隐私问卷和 Beta App Review 信息。
- 提供审核所需的扩展开启步骤、功能说明和测试备注。
- 建立内部测试组，向小批测试者验证安装流程。

退出条件：内部测试可安装；外部测试提交审核；未发现签名或 entitlement 问题。

### Day 14：私有测试启动

- 对候选构建执行最终冒烟测试。
- 发布给已批准的私有测试组；若仍在审核，先运行内部测试。
- 发送测试任务、隐私说明、已知限制和反馈入口。
- 建立每日问题复盘节奏。

退出条件：测试者能完成安装、启用、浏览、暂停、Allowlist 和反馈完整闭环。

## 6. 延期时的裁剪顺序

不能通过降低隐私、安全或基本稳定性换取准时。若工期不足，按以下顺序收窄：

1. 减少 annoyances 覆盖站点数量，保留能力和最常见样本。
2. 缩减 Pro Preview 的视觉复杂度，保留准确说明。
3. 减少非关键设置项与装饰动画。
4. 减少规则来源数量，保留许可证清晰且质量稳定的集合。
5. 将非核心站点兼容性问题列为已知限制。

不可裁剪：

- 真实状态展示。
- Allowlist 和暂停恢复。
- 规则签名、校验失败保护和回滚。
- 隐私边界和权限说明。
- YouTube、X 的定义内核心验证。
- 至少一台 iPhone 和一台 iPad 的真机测试。

## 7. 风险清单

| 风险 | 影响 | 应对 |
| --- | --- | --- |
| Safari 规则限制或系统行为与预期不同 | 核心能力不足 | Day 1 至 Day 3 真机验证，不等到界面完成 |
| YouTube/X 页面快速变化 | 差异化能力失效 | 独立规则层、真实回归、快速规则发布 |
| 上游规则许可证不适合商业使用 | 无法合法发布 | 发布前逐项核查并保存证据，未确认不进入 production |
| Apple 签名、entitlement 或审核延迟 | TestFlight 延期 | Day 1 配置，Day 13 前上传，先内部测试 |
| 规则误伤关键站点 | 用户失去信任 | 保守默认、Allowlist、快速回滚和 Site Broken 优先级 |
| 对外名称存在商标冲突 | 无法上架或需返工 | `Gleem` 仅内部代号，尽早完成候选名称检索 |
| “App 广告拦截”被误解为 VPN/DNS 或全能拦截 | 审核和预期风险 | 文案明确未来 URL Filter 技术与能力限制 |
| 两周内功能过载 | 稳定性下降 | Day 1 冻结范围，Day 12 停止新增功能 |

## 8. TestFlight 运营目标

初始目标：

- 招募 100 名符合市场画像的目标测试者。
- 观察至少 30 名用户表达或执行未来 Pro 试用意愿。
- 在真实付费版本上线后验证至少 10 名年订阅用户。

TestFlight 阶段不应把“点击 Preview”直接等同于真实付费。应同时观察：

- 扩展开启完成率。
- 首日和七日仍保持保护开启的比例。
- Allowlist 与暂停的使用原因。
- YouTube/X 的有效反馈与失效频率。
- `Missed Ad` 与 `Site Broken` 的数量、类型和解决时间。
- 付费意愿访谈或明确登记。

在没有分析 SDK 的前提下，数据通过 TestFlight 邀请记录、用户主动反馈和小规模访谈收集；不得暗中建立浏览行为追踪。

## 9. 发布资料清单

- 英文产品名称候选和副标题。
- App 图标与基础截图。
- 简短、明确的 Beta 描述。
- 扩展开启步骤。
- YouTube/X 及 Pro Preview 的限制说明。
- 隐私政策链接。
- 支持与反馈入口。
- Beta App Review 测试说明。
- 上游规则来源和许可证记录。
- 构建号、Git commit、规则版本、已知问题。
- 回滚操作和负责人。

## 10. TestFlight 结束后的决策

两周发布只是验证开始。首轮测试结束后，根据证据决定：

- 继续修复 Safari 核心体验，还是扩大站点覆盖。
- YouTube/X 是否足以形成付费差异化。
- 是否进入 `NEURLFilterManager` 与 PIR 的资格和技术验证。
- 是否开始真实 StoreKit 年订阅实现。
- 对外品牌名称是否具备注册和上架条件。

任何决定都应基于测试数据、反馈原文和可复现问题，不因已投入开发成本而自动继续。
