# 信息架构与用户流程

> 页面级摘要。完整状态以 [app-flow.md](app-flow.md) 为准；范围以 [产品总纲领](../product/product-charter.md) 为准。

---

## 1. 导航结构

**无底部 Tab。**

```text
App
├── Welcome
├── Setup (Safari Protection)     门禁 / 模态
├── Home
│   ├── Upgrade
│   └── More
│         ├── Help
│         ├── Feedback
│         ├── About
│         ├── Privacy Policy
│         ├── Website
│         ├── Restore / Manage Subscription
```

**主 App 无：** Allowed Sites、Pause sheet、定时暂停、Strict Mode、Tap to Block（D-317）。

**Safari 扩展 popup（非主 App 导航树；固定 2 项 · D-317）：**

1. Pause / Resume on this site  
2. Report issue  

规格：[safari-extension.md](safari-extension.md)。

---

## 2. 关键用户流程

### 2.1 新用户：安装 → Home

Welcome → Setup → Home（默认免费类别 On）。

### 2.2 回访：管理类别

打开 App → 查看或调整类别开关 → 离开。Home 顶部文案固定，无 On/Off 页面切换。

### 2.3 扩展被关

检测失败 → 模态 Setup → 系统设置 → 回 App。  
若用户打开扩展 popup：Not enabled → Open Stillwall。

### 2.4 暂时关掉所有拦截

Home → **逐个关闭** Ads / Privacy / Annoyances / Regional（及已开的 Pro 类别）。**无**全局一键总开关、无 15m/1h 选项。

### 2.5 只放行某个网站

**不在 App 内操作名单。**

```text
Safari → Stillwall 扩展 popup → Pause on this site
（恢复）→ Resume on this site
```

### 2.6 Tap to Block

**v1 不做**（D-317）。

### 2.7 Report / Feedback

扩展槽 2 **Report issue**（预填域名）**或** More → Feedback。

### 2.8 升级 Pro

Pro 行 → Upgrade（扩展内不买）。

### 2.9 关闭某一类拦截

Home 关 Ads（或 Privacy 等）→ 其他已开启类别仍可生效。

---

## 3. 能力与入口映射

| 用户意图 | 入口 |
|----------|------|
| 看当前站是否生效 | 扩展顶栏（当前站）；Home 只表达类别选择 |
| 关掉/打开某类拦截 | 主 App **对应类别开关**（无全局总开关） |
| 放行 / 恢复某站 | 扩展 **Pause / Resume on this site** |
| 报告坏站/漏拦 | 扩展 **Report issue** 或 App Feedback |
| 少广告/追踪/弹窗 | Ads / Privacy / Annoyances |
| 地区规则 | Regional（自动） |
| YouTube/X 网页 | YouTube & X（Pro，Home 开关） |
| 耗电脚本 | Battery Boost（Pro，Home） |
| 订阅 | Upgrade（主 App） |
| 隐私/帮助 | More |
| Strict / Tap to Block | **v1 不做**（D-317） |

---

## 4. 文案语气

| 场景 | 语气 |
|------|------|
| Home | 中性、固定，不宣称当前保护状态 |
| 全部类别 Off | Home 不切页；扩展顶栏说明当前无拦截 |
| 需设置 | 清晰步骤 |
| 站点例外 | Help：Go to Safari → extension… |
