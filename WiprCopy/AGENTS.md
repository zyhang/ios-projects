# AGENTS.md

面向在本仓库工作的 **Agent / 协作者** 的必读约束。  
**产品需求与已对齐决策以 PRD 为准**，本文件不重复维护完整 PRD 正文。

| 文档 | 职责 |
|------|------|
| **本文件** | 硬性规则、文档地图、工作边界 |
| [`docs/product/prd.md`](docs/product/prd.md) | **PRD 权威源**：定位、MVP、商业、技术约束、范围外 |
| [`docs/product/`](docs/product/) | 专题深挖（命名、商业、规则包、名单、破站、spike…） |
| [`docs/wireframes/`](docs/wireframes/) | 信息架构与线框 |
| [`docs/design/`](docs/design/) | 高保真、tokens、Welcome（**视觉重设计中**） |
| [`docs/archive/`](docs/archive/) | 已封存的旧设计稿（非权威） |

实现代码、工程配置不放在 `docs/`（见 [`docs/README.md`](docs/README.md)）。

---

## 产品身份（摘要）

**Gleem** — 面向海外的隐私广告拦截：**Safari 优先**（v1），策展规则包，一次 IAP 解锁；系统级全 App / Mac 客户端拦截后置论证。

| 字段 | 值 |
|------|-----|
| App 显示名 | **Gleem**（已锁定） |
| 副标题 | **Block Ads & Trackers**（已锁定） |

命名细则、理想/立场文案归属 → [`docs/product/naming.md`](docs/product/naming.md)  
完整产品定义 → [`docs/product/prd.md`](docs/product/prd.md)

---

## 规则（必须遵守）

### 0. 文档语言与界面语言（必须遵守）

本产品由**中文团队开发**，面向**欧美等海外用户**使用。语言分工如下：

| 内容类型 | 默认语言 | 说明 |
|----------|----------|------|
| **PRD、产品决策、开发/工程说明、专题文档、索引 README** | **中文** | 写给团队与 Agent 读；便于对齐与评审 |
| **线框/设计文档中的说明、标注、决策叙述** | **中文** | 同上 |
| **产品界面文案、Welcome 标题、按钮、状态句、App Store 面向用户的 listing 正文** | **英文** | 真实上架与上屏内容；美式/国际通用英文 |
| **代码标识符、API、系统框架名** | 英文原名 | 如 Content Blocker、URL Filters、Family Sharing |

具体约定：

1. 新建或改写 **PRD / 开发文档**时默认用**中文**；不要把开发文档整篇改成英文，除非用户明确要求。  
2. **界面 mock、线框 ASCII 中的控件文案、hi-fi 上的用户可见字符串**保持 **英文**，与 `docs/design/`、`docs/wireframes/` 中的 UI 示例一致。  
3. 中文文档中引用界面文案时，用英文原文 + 必要时中文释义，例如：`You're protected.`（你已受保护）。  
4. **不得**因为文档用中文，就默认把 App 做成中文 UI 或按中文市场交互习惯设计（见规则 1）。

### 1. 目标用户与产品定位

本 App 面向**欧美等海外用户**设计与迭代。

后续所有工作——包括但不限于：

- 产品设计与信息架构  
- 交互与视觉习惯  
- **界面**文案语言、语气与用词（默认英文）  
- 功能取舍与优先级  
- 默认行为与可选项设计  

都必须贴合该客户群体的使用场景与预期，**不得偏离**（例如不得按中文市场习惯、国内浏览器生态或本地运营逻辑做默认假设）。

面向用户的界面与商店文案基调为**英文**；对内 PRD/开发文档用**中文**（见规则 0）。

细节与 MVP 范围见 PRD：[受众](docs/product/prd.md#2-受众)、[定位](docs/product/prd.md#4-定位与已对齐决策)。

### 2. 隐私优先：本地处理，不采集浏览信息

与 Wipr 同级的信任标准：**注重用户隐私**。

- **浏览相关信息留在本地**：用户访问了哪些站点/App、哪些请求被拦截等，默认不上传、不用于画像或分析。  
- **App 不采集**个人数据与浏览行为（无广告 SDK、无第三方分析 SDK、无静默追踪）。  
- 架构选型优先 Content Blocker、URL Filters 等**系统代为拦截、扩展不必读取页面内容**的路径；避免「为了统计/调试而拿到浏览数据」的设计。  
- 若某能力**必然**需要更高权限或离开设备的查询（例如 URL Filters 的 PIR 查询），必须：  
  - 走系统提供的隐私保护路径（如 PIR，使运营方无法得知用户查了什么）；  
  - 在产品与隐私说明中写清「我们看不到什么」；  
  - **不得**借机收集可还原浏览历史的日志。  
- 可选反馈/报错：仅用户主动提交；可匿名；提交内容最小化；用完即删；不得与浏览历史绑定做后台采集。  
- 功能取舍冲突时：**隐私与本地优先 > 功能炫技**（例如不做需要读浏览数据才能实现的拦截统计，除非将来有纯本地、零上传方案）。

产品级隐私需求见 PRD：[隐私原则](docs/product/prd.md#3-隐私原则产品需求)。

### 3. 产品决策以 PRD 为准

- **已对齐的产品决策、MVP、商业结构、规则包、名单策略、破站自救、技术约束、明确不做项** 一律以 [`docs/product/prd.md`](docs/product/prd.md) 及其所链专题文档为准。  
- 线框与高保真**不得**与 PRD 已对齐决策冲突。  
- 变更产品决策时：先改 PRD（及受影响专题文档），再改线框/设计/实现；**不要**只在本文件堆决策表。  
- 冲突优先级：**本文件规则 0–2（语言约定、受众、隐私） > PRD > 专题文档 > 线框/设计**。

---

## 文档地图（按任务）

| 任务 | 先读 |
|------|------|
| 改范围 / MVP / 定位 | [`docs/product/prd.md`](docs/product/prd.md) |
| 定价 / IAP / Family Sharing | [`docs/product/commerce.md`](docs/product/commerce.md) |
| 规则包 | [`docs/product/rule-packs.md`](docs/product/rule-packs.md) |
| 名单策展 | [`docs/product/blocklists.md`](docs/product/blocklists.md) |
| 破站自救 | [`docs/product/breakage-recovery.md`](docs/product/breakage-recovery.md) |
| 系统级 URL Filter | [`docs/product/url-filter-spike.md`](docs/product/url-filter-spike.md) |
| 命名与商店副标题 | [`docs/product/naming.md`](docs/product/naming.md) |
| 开工顺序 | [`docs/product/work-order.md`](docs/product/work-order.md) |
| Welcome / UI 视觉 | [`docs/design/`](docs/design/)（重设计中；新稿落地后更新索引） |
| 旧视觉对照（非权威） | [`docs/archive/design-v1-2026-07-25/`](docs/archive/design-v1-2026-07-25/) |
| 信息架构 / 线框 | [`docs/wireframes/`](docs/wireframes/) |

索引：[`docs/product/README.md`](docs/product/README.md)、[`docs/README.md`](docs/README.md)。

---

## 工作提示（Agent）

1. **写文档用中文，写界面用英文**（规则 0）；勿混用成「中文 UI」或「英文 PRD」除非用户要求。  
2. **设计先行**：名称 → 线框（Safari 优先）→ **冷静工具 / 干净生活** 双视觉对比 → 工程 — 见 [work-order](docs/product/work-order.md) 与 PRD。  
3. **v1 主路径是 Safari**；系统级 URL Filter / Mac 客户端拦截**后置**，勿默认写进商店宣称或 MVP 必达 — 见 PRD §4–5。  
4. 健康态 Home：极简状态句、无 Tab、无手动「更新名单」按钮 — 见 PRD 与 wireframes。  
5. 不确定是否属于 v1 时：打开 PRD 的 MVP / 后置 / 范围外，而不是自行扩 scope。  
6. Plus 能力须过 PRD 克制门槛；勿整包复刻 AdGuard。  
