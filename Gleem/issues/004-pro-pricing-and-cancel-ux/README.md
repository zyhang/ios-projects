# Issue 004：Pro 定价对齐 $14.99 + 用户取消购买不展示 Request Canceled

| 字段 | 内容 |
|------|------|
| 状态 | open（**定价/取消 UX 规格已锁**；待 StoreKit 主 App + ASC） |
| 优先级 | P0（定价错误）/ P1（取消态文案） |
| 类型 | behavior / copy |
| 影响范围 | 主 App · Upgrade / Paywall（StoreKit） |
| 相关文档 | `docs/product/product-charter.md` §4.1；`docs/design/screens.md` S08；App Store 订阅配置 |
| 创建日期 | 2026-07-31 |

## 问题现象

### 1. 价格与产品决策不一致

实机付费墙展示：

> 1 month free  
> Then **$9.99/year** · Family Sharing included  

产品总纲领与页面说明已锁定：

| 项 | v1 决策 |
|----|---------|
| 价格 | **$14.99 / 年** |
| 试用 | 1 个月 |
| 家庭共享 | 支持 |

### 2. 用户取消购买时露出 StoreKit 原始结果

红色文案 **Request Canceled**（用户关掉系统购买表时常见）。  
取消是正常行为，不应当作错误恐吓用户。

![当前 · $9.99 + Request Canceled](before/paywall-request-canceled.jpg)

设计参考（价格与布局目标）：

![期望 · Hi-fi Upgrade](after/upgrade-design-target.png)

## 期望结果

### 定价

1. 付费墙展示与 **App Store Connect 年订阅** 一致为 **$14.99/year**（试用 1 个月）。  
2. 展示文案建议：

```text
1 month free
Then $14.99/year · Family Sharing included
Cancel anytime in Apple subscriptions.
```

3. 价格优先从 **StoreKit 2 Product** 本地化价格读取；若 ASC 产品仍是 $9.99，需在 **App Store Connect** 改为 $14.99（或替换为正确 product id），客户端不要长期硬编码错误价。  
4. 硬编码 fallback 仅用于 ASC 未返回时，且必须为 `$14.99`（或当前商店本地化等价），**不得**再用 `$9.99`。

### 取消 / 错误展示

| StoreKit 结果 | UI |
|---------------|-----|
| 用户取消（`userCancelled` / 等效） | **静默**：不显示错误行；可保持按钮可点 |
| 待处理 / 家长审批等 | 中性说明（英文），非红字「Request Canceled」 |
| 真失败（网络、不可用等） | 简短可读英文错误 + 可再试；避免原始 `Request Canceled` 字面量 |

主按钮文案保持：**Start 1 Month Free Trial**；次要：**Restore Purchases**。  

**利益列表（D-317）：** 仅 **YouTube & X in Safari**、**Battery Boost**——**不要** Strict Mode / Tap to Block。

## 修改说明（给开发）

1. **核对**订阅 product id 与 ASC 标价；与 charter §4.1 对齐。  
2. 购买流程 `catch` / result 分支：  
   - cancel → `return` / clear error state  
   - success → unlock Pro UI  
   - other → localized friendly message  
3. 删除或替换任何直接展示 `error.localizedDescription` 且未过滤 cancel 的路径（截图中的 Request Canceled 即典型未过滤）。  
4. Terms / Privacy 链接保持可用。

### 勿误改

- 免费能力与 Pro 权益边界  
- Family Sharing 说明（保留）  
- 非首次进 Home 门禁（paywall 不是进 App 条件）

### Hallmark 增补（付费墙调性）

Upgrade 在 Hi-fi 中已是全 App **最干净的一屏**：利益列表 + Offer 卡 + 单主 CTA + 系统蓝 Restore。实现不要破坏这份克制。

| 项 | 规范 |
|----|------|
| 错误展示 | **仅**真失败时，在 CTA **下方** inline 一行可读英文（design-system §7.8）；字色可用语义红，但句子是人话，不是 StoreKit 原文 |
| 取消 | 清空 error state；无横幅、无 toast |
| 处理中 | CTA → `Processing…` + disabled（§7.8） |
| Restore | 保持系统蓝链接，不与主 CTA 抢绿色 |
| 利益行图标 | 小圆角井 + 品牌软绿底（对齐 Hi-fi）；与 Home 的 PRO 金徽标职责分离——**墙内不必再贴 PRO badge** |
| 利益副文案 | 与 Home / Welcome 锁定表一致（见 **005**），避免 Battery/Tap 各页各写一版 |
| 法律行 | 小字 secondary；Terms · Privacy 可点 |

**品味红线：** 不要为提高转化加假倒计时、假「仅剩 N 席」、多计划比价表、全屏粒子。Stillwall 的 Pro 是「需要时更强」，不是「你不安全快付钱」。

## 验收标准

- [ ] 付费墙年价展示为 **$14.99**（或 StoreKit 返回的本地化 $14.99 等价），不再出现 $9.99（除非 ASC 未改且需先改商店——此时阻塞上架）  
- [ ] 用户取消系统购买表后，页面**无**红色 Request Canceled  
- [ ] 真实购买失败仍有友好英文提示（inline，非原始 error 字符串）  
- [ ] 试用 CTA 与 Restore 行为正常；Processing 态可用  
- [ ] 布局/层级接近 Hi-fi：利益卡 → Offer → 单主 CTA  
- [ ] 与 charter §4.1、screens S08 一致  

## 附件

| 文件 | 说明 |
|------|------|
| `before/paywall-request-canceled.jpg` | 实机：$9.99 + Request Canceled |
| `after/upgrade-design-target.png` | Hi-fi Upgrade 参考 |
