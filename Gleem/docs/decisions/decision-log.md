# 决策记录

## 1. 使用说明

本文件记录产品负责人已确认的关键决策。修改已确认决策时，须新增记录并注明替代关系，不直接抹掉历史。

| 状态 | 含义 |
|------|------|
| **已确认** | 当前实施必须遵守 |
| **待验证** | 外部依赖或事实未确认，不能写成既定能力 |
| **暂缓** | 当前版本不做，是否进入范围需重新决策 |
| **已替代** | 被更新决策取代，仅供追溯 |

**权威顺序：** [产品总纲领](../product/product-charter.md) 与本文一致；若冲突，以更新时间更晚且状态为「已确认」的条目 + 总纲领修订为准。

---

## 2. 已确认决策

### 2.1 产品与范围

| ID | 决策 | 状态 | 说明 |
| --- | --- | --- | --- |
| D-101 | 按真实可上架产品建设 | 已确认 | 非学习型复刻 |
| D-102 | 定位为 iOS Safari 中心的 Ad Block | 已确认 | 简单、少步骤；见总纲领 §2 |
| D-103 | 产品理念：尽量不做 Custom Rules | 已确认 | 降低使用负担 |
| D-104 | 首要用户为希望少步骤启用的普通用户 | 已确认 | 非规则玩家 |
| D-105 | UI 与商店文案以英文为主 | 已确认 | 文档协作可用中文 |
| D-106 | 对外名暂用 Stillwall；Gleem 为内部代号 | 已确认 | 商标/重名核查前可调整 |
| D-107 | v1 明确不做清单以总纲领 §9 为准 | 已确认 | 含 Custom Rules、全 App 拦截、TV、Mac 交付等 |

### 2.2 商业与权益

| ID | 决策 | 状态 | 说明 |
| --- | --- | --- | --- |
| D-201 | Safari 核心拦截永久免费 | 已确认 | Ads/Privacy/Annoyances/Regional + 全局开关；站点控制在扩展（见 D-309） |
| D-202 | Pro：$14.99/年 | 已确认 | 仅年订 |
| D-203 | 试用 1 个月 | 已确认 | 从升级页/Pro 入口开始，非进 Home 门禁 |
| D-204 | 支持 Family Sharing | 已确认 | — |
| D-205 | 无月订、无终身买断 | 已确认 | — |
| D-206 | 多设备无席位费；同 Apple ID | 已确认 | 免费与 Pro 均随 ID/订阅 |
| D-207 | Mac 权益不另收费，但非 v1 交付 | 已确认 | Coming soon |
| D-208 | 首次启动不强制付费墙 | 已确认 | 主路径为开 Safari 拦截 |

### 2.3 功能分层

| ID | 决策 | 状态 | 说明 |
| --- | --- | --- | --- |
| D-301 | 免费：Ads、Privacy、Annoyances、Regional（默认开） | 已确认 | Regional 按语言全自动 |
| D-302 | 主 App 免费：全局保护 On/Off | 已确认 | **已替代**原「Pause 时长 + App 内 Allowlist」方案；见 D-309 |
| D-303 | Pro：YouTube & X 合并为一个开关 | 已确认 | 仅 Safari 网页 |
| D-304 | Pro：Battery Boost、Strict Mode（默认关） | 已确认 | Strict 叠加更严 |
| D-305 | Pro：Tap to Block；Home 为入口行 | 已确认 | 非纯开关；规则仅本机 |
| D-306 | 不做 Custom Rules 编辑器 | 已确认 | 与 D-103 一致 |
| D-307 | 不承诺原生 YouTube/X App 去广告 | 已确认 | 文案须限定 Safari |
| D-308 | 规则日更自动；不做用户开关 | 已确认 | About 可展示版本 |
| D-309 | 站点放行 / 当前站控制仅在 Safari 扩展中配置 | 已确认 | 主 App **不做** Allowed Sites 页；对齐 Safari 扩展能力，避免重复 UI |
| D-310 | 主 App 不做定时 Pause（15m/1h/Until resume） | 已确认 | 仅全局开关；需要临时停拦：关全局或用扩展放行站点 |
| D-311 | 扩展 popup **固定 3 项** | 已确认 | ① Pause/Resume on this site · ② Tap to Block · ③ Report issue；只读顶栏不算项；硬上限 5，v1 不凑满；见 [safari-extension.md](../design/safari-extension.md) |
| D-312 | 本站 Pause：eTLD+1、持久至 Resume | 已确认 | 无 session-only、无 15m/1h；`www` 与裸域同一站 |
| D-313 | 扩展内无 IAP；未订阅 Tap 回主 App | 已确认 | 符合 App Store 4.4；Open Stillwall 非常态第 4 项 |
| D-314 | v1 不做 Paywall Bypass | 已确认 | 不集成 bypass-paywalls 类能力；非增值点 |

### 2.4 平台与技术

| ID | 决策 | 状态 | 说明 |
| --- | --- | --- | --- |
| D-401 | 最低 iOS/iPadOS 26 | 已确认 | — |
| D-402 | v1 仅 Safari：Content Blocker + Web Extension | 已确认 | — |
| D-403 | 不使用 VPN | 已确认 | — |
| D-404 | v1 不做系统级跨 App 过滤 | 已确认 | 未来若做：系统 Filter，非 VPN |
| D-405 | 不做 Apple TV；Mac 非 v1 | 已确认 | — |
| D-406 | 授权引导文案合成一次 | 已确认 | 系统 UI 仍可能分步 |

### 2.5 体验与流程

| ID | 决策 | 状态 | 说明 |
| --- | --- | --- | --- |
| D-501 | 无 Tab；单 Home + 次级页 | 已确认 | — |
| D-502 | Welcome 为 1 长页滚动卖点 | 已确认 | 顶标题/理念，中卖点，底主按钮 |
| D-503 | 未完成 Safari 授权不得进 Home | 已确认 | 模态引导直至完成 |
| D-504 | Home：上状态+全局开关、下能力列表 | 已确认 | 顺序见总纲领 |
| D-505 | 主 App 不展示 Allowed Sites / Pause 入口 | 已确认 | **替代**原「状态区下 Pause+Allow 固定入口」；站点设置见 D-309 |
| D-506 | 扩展被关不得显示假保护中 | 已确认 | 模态拉回授权 |
| D-507 | 主 App 视觉以 Lunacy Hi-fi P0 + design-system 为准 | 已确认 | 品牌主色 `#2F6A58`；暖金仅 Pro；系统字体实现；见 [design-system.md](../design/design-system.md) |
| D-508 | 扩展 popup 无全局开关、无类别列表 | 已确认 | 全局/类别仅主 App；扩展为当前站情境 |
| D-509 | App Store 基础元数据以 release 包为准 | 已确认 | Name Stillwall；Subtitle Ad Block for Safari；Utilities；见 [app-store-submission.md](../release/app-store-submission.md)（V-001 可整包更名） |

### 2.6 隐私

| ID | 决策 | 状态 | 说明 |
| --- | --- | --- | --- |
| D-601 | 无产品账号 | 已确认 | — |
| D-602 | 不收集浏览历史上传 | 已确认 | — |
| D-603 | 无第三方分析/广告 SDK | 已确认 | — |
| D-604 | 全局/类别开关与 Tap 规则仅本机；站点例外在扩展侧本地 | 已确认 | 主 App 无名单库 |
| D-605 | Feedback 可选手动附域名 + 发送前预览 | 已确认 | 用户主动提交 |
| D-606 | v1 不接第三方崩溃 SDK | 已确认 | 变更须重决策 |

---

## 3. 待验证

| ID | 事项 | 状态 | 说明 |
| --- | --- | --- | --- |
| V-001 | Stillwall 商标、App Store 重名、域名 | 待验证 | 不通过则更名 |
| V-002 | Content Blocker + Web Extension 在 iOS 26 上的最终权限文案与系统路径 | 待验证 | 影响引导截图与文案 |
| V-003 | StoreKit 试用 1 个月 + $14.99 年 + Family Sharing 配置细节 | 待验证 | 以 App Store Connect 为准 |
| V-004 | 规则源许可证与归因文案 | 待验证 | About / 开源声明 |
| V-005 | Tap to Block 在 Safari Web Extension 的可行交互与限制 | 待验证 | 影响入口页说明；属扩展 TODO |

---

## 3.1 Safari 扩展侧工作包

> 产品规格见 [design/safari-extension.md](../design/safari-extension.md)。决策：D-309～D-314、D-508。

| ID | 事项 | 状态 |
| --- | --- | --- |
| T-EXT-01 | 扩展 popup / 菜单 IA（固定 3 项） | **产品已确认** |
| T-EXT-02 | 当前站 Pause / Resume（eTLD+1、持久） | **产品已确认**；工程规格已写，代码待做 |
| T-EXT-03 | Tap to Block 扩展内流程 | 产品+工程骨架已定；**V-005** + 实现 |
| T-EXT-04 | YouTube & X 扩展侧行为与权限 | 工程纲要已写；实现 TODO |
| T-EXT-05 | 扩展线框 / 高保真 SE01–SE03 | **Lunacy 线框已画**（Wireframes v1 · ROW 4）；Hi-fi 可选 |
| T-EXT-06 | 扩展 ↔ 主 App 状态同步 | **schema 已定**（engineering/safari-extension）；代码待做 |
| T-EXT-07 | Help「去 Safari 扩展」完整引导 | TODO（**V-002**） |

---

## 4. 暂缓（非 v1）

| ID | 事项 | 状态 | 说明 |
| --- | --- | --- | --- |
| S-001 | 系统级 URL Filter（非 VPN） | 暂缓 | 平台已预留 iOS 26；范围另决 |
| S-002 | Mac 客户端 | 暂缓 | Coming soon 文案级 |
| S-003 | 云同步 Allow/Tap | 暂缓 | 依赖账号模型，当前无账号 |
| S-004 | Performance Insights 看板 | 暂缓 | 总纲领明确不做 v1 |
| S-005 | Custom Rules | 暂缓 | 产品理念反对；非「以后默认做」 |
| S-006 | 主 App 内 Allowed Sites / 定时 Pause UI | 暂缓 | 已明确 v1 不做；站点控制在扩展（D-309/D-310） |
| S-007 | Paywall Bypass | 暂缓/否决 | 与 D-314 一致；不做增值 |

---

## 5. 修订记录

| 日期 | 说明 |
|------|------|
| 2026-07-27 | 根据产品 grilling 与 [product-charter](../product/product-charter.md) 建立 D-1xx～D-6xx |
| 2026-07-27 | D-309/D-310：站点控制下沉 Safari 扩展；主 App 仅全局开关，移除 Pause 时长与 Allowed Sites |
| 2026-07-27 | 登记 T-EXT-01～07：Safari 扩展侧工作 TODO，后续完善 |
| 2026-07-28 | D-311～D-314、D-508：扩展 popup 3 项、Pause 语义、无扩展 IAP、不做 paywall bypass；T-EXT-01/02 产品确认 |
| 2026-07-28 | engineering 扩展/主 App 规格；SE 线框蓝图与 popup mock；T-EXT-05/06 推进 |
| 2026-07-28 | Lunacy Wireframes v1 增加 ROW 4（SE01–SE03）；T-EXT-05 线框已画 |
