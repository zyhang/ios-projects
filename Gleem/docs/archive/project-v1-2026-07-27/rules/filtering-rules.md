# 拦截规则系统

> **已归档（2026-07-27，project-v1）**：本文属于全量文档快照的一部分，不再作为现行权威。见 [归档说明](../README.md)。重构请写到 `docs/`。

## 1. 目标

规则系统决定产品实际效果。首版不从零编写广告库，而是基于成熟上游规则，经过许可证审核、编译、去重、冲突检查和真实站点回归后交付。

规则质量目标：

- 拦截效果稳定。
- 误杀可快速恢复。
- 来源和许可证可追溯。
- 每次更新有差异、测试和回滚。
- 不通过上传浏览行为学习规则。

## 2. 规则分类

| 类别 | 目的 | 免费/Pro |
| --- | --- | --- |
| Ads | 常见网页广告请求与元素 | 免费 |
| Trackers | 第三方追踪脚本与请求 | 免费 |
| Annoyances | Cookie、Open in App、Newsletter 等 | 免费 |
| Anti-adblock | 常见“关闭广告拦截器”提示 | 免费 |
| YouTube | YouTube Safari 专项规则和内置脚本 | 免费 |
| X | X Safari Promoted Posts 内置脚本 | 免费 |
| App Ads | 已知第三方 App 广告/追踪 URL | Pro |
| Exceptions | 修复误杀与兼容性 | 免费/Pro |

## 3. 候选上游

候选包括但不限于：

- EasyList。
- EasyPrivacy。
- Fanboy Annoyances。
- AdGuard filters。
- 合适的 DNS/host 级广告与追踪列表。

注意：

- 上述仅为候选，不代表已经获得商业再分发许可。
- 每个规则源必须记录仓库 URL、commit/tag、许可证文本和使用范围。
- 不允许因为规则公开可下载就默认可以商业打包。
- 许可证不兼容时必须替换、独立获取授权或不使用。

## 4. 自有规则层

Gleem 自有层包括：

- 上游格式无法直接表达的 Safari 兼容规则。
- YouTube/X 专项静态参数和选择器。
- 已验证的漏拦补充。
- 误杀 exception。
- 临时紧急禁用规则。

每条自有规则需要：

- 唯一 ID。
- 来源/反馈编号。
- 添加原因。
- 适用域名。
- 创建日期。
- 回归用例。
- 计划复查日期。

## 5. 编译流水线

```text
固定上游版本
  ↓
许可证与来源检查
  ↓
解析与标准化
  ↓
分类和去重
  ↓
冲突/高风险规则检查
  ↓
转换 Safari Content Blocker 格式
  ↓
合并 Gleem exceptions
  ↓
schema/数量/大小校验
  ↓
站点回归与 golden tests
  ↓
生成差异摘要
  ↓
签名发布
```

## 6. 标准化与去重

- 域名转小写和 Punycode。
- 规范化 wildcard 与正则表达式。
- 合并完全重复规则。
- 保留 allow/exception 高于 block 的优先关系。
- 禁止无边界的全局脚本或媒体屏蔽。
- 对广泛匹配规则标记高风险并要求人工审核。
- 保留从产物回溯上游规则的映射。

## 7. Safari Content Blocker

支持的主要动作：

- 阻止请求。
- 隐藏元素。
- 处理 Cookie/资源加载。
- 按 domain、resource type、load type 限定。

规则要求：

- 正则必须能被 Safari 接受。
- 大规则集按稳定分类拆分，避免任意切片。
- allowlist 需要在最终规则中正确覆盖 block。
- CSS hiding 不得造成全页空白或禁止滚动。
- anti-adblock 规则优先采用小范围 site-specific 方案。

## 8. YouTube 专项

目标：

- Safari 网页版视频广告与页面广告。
- 不承诺原生 YouTube App。

实现层次：

1. Content Blocker 网络/元素规则。
2. Gleem Extra 的内置页面脚本。
3. 远程静态参数和模块启停。

要求：

- 不读取账号、观看历史或评论内容。
- DOM observer 有范围和节流。
- 页面结构未知时 fail open。
- 不把背景播放、下载、SponsorBlock、隐藏 Shorts 等功能偷带进广告拦截 MVP。
- YouTube 变化后可以远程关闭异常模块。

## 9. X 专项

目标：

- 在 `x.com` Safari 网页版隐藏标记为 Promoted 的内容。
- 不承诺原生 X App。

要求：

- 只处理明确的推广标记，不基于作者、观点或内容关键词屏蔽。
- 不读取私信、草稿、输入框或账号数据。
- DOM 变更后未知条目默认显示，避免误删普通 Posts。
- 操作幂等，滚动加载不重复破坏布局。

## 10. Annoyances

首版一个统一开关，内部可以包含：

- Cookie consent。
- Open in App。
- Newsletter/sign-up overlays。
- 自动播放干扰。
- Anti-adblock warning。

安全要求：

- 隐藏 overlay 时同时检查 scroll lock。
- 不自动点击“接受全部 Cookie”。
- 不绕过付费墙。
- 不屏蔽网站核心登录、支付或安全确认。
- 对欧盟 consent 页面保持审慎，必要时只隐藏非阻塞提示。

## 11. App Ads / URL Filter

阶段 B 使用：

- 只处理已知广告/追踪 URL 数据集。
- URL Filter 不解析 App 返回数据或 UI。
- 第一方同域广告通常不可安全阻断。
- 广告与内容共用请求时默认放行。
- 规则误判必须优先保护 App 可用性。

## 12. 规则版本

建议版本格式：

```text
YYYY.MM.DD.N
```

例如：

```text
2026.07.26.1
```

每次发布记录：

- 上游版本。
- 自有规则 diff。
- 新增、删除、exception 数量。
- 测试结果。
- 已知问题。
- 可回滚目标。

## 13. 更新频率

- 常规规则：每天最多一次发布，不为了“每日更新”制造无意义版本。
- YouTube/X 紧急适配：通过加急流程。
- 严重误杀：立即回滚或禁用模块。
- 用户设备：前台启动检查，后台尽力刷新。

## 14. 质量门槛

发布必须满足：

- 无语法错误。
- 无未知许可证来源。
- 无重复 ID。
- 无未经审核的全局宽匹配。
- golden site regression 通过。
- YouTube/X smoke test 通过。
- allowlist 与 pause 测试通过。
- 旧规则回滚测试通过。
- 产物签名和哈希通过。

## 15. 规则效果评价

不上传用户命中数据。效果评价依赖：

- 固定站点回归矩阵。
- 人工浏览检查。
- 用户主动提交的漏拦/误杀。
- 上游规则变更。
- TestFlight 定向访谈。

禁止：

- 在页面注入隐蔽 beacon。
- 上报访问域名。
- 用唯一规则 URL 追踪设备。
