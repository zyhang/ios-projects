# Safari 测试站点清单

> 用于 Stillwall（内部代号 Gleem）在 **iOS / iPadOS Safari** 上的广告、追踪、烦人项与地区规则验收。  
> 范围以 [产品总纲领](../product/product-charter.md) 为准：仅 Safari 网页；不测原生 YouTube/X App；v1 不做系统级跨 App 拦截。

**文档状态：** 初版（2026-07-28）  
**更新原则：** 榜单位次会波动；本清单以**类别覆盖与能力映射**为准，不追求实时 Top 排名。

---

## 1. 使用方式

| 项 | 说明 |
|----|------|
| 浏览器 | **Safari（iOS / iPadOS）**；优先移动站；可选再抽查桌面布局 |
| 语言 | 默认 `en-US` 跑最小套件；`ja` / `ko` / `en-AU` / `de` / `fr` / `en-GB` 做地区回归 |
| 登录 | 登录墙站点测**公开首页 + 文章/商品详情**即可，不强制登录 |
| 不做 | 成人站、明确绕过地区限制、原生 App 内广告 |
| 准则 | 购物 / 银行 / 政务：**兼容 > 拦截率** |

### 1.1 优先级

| 级 | 含义 |
|----|------|
| **P0** | 每次发版 / TestFlight 必测 |
| **P1** | 地区包更新或完整回归 |
| **P2** | 抽样 / 专项 |

### 1.2 能力与验收映射（总纲领）

| ID | 能力 | 总纲领 | 层级 |
|----|------|--------|------|
| CAP-ADS | Ads | §5.1 | 免费 |
| CAP-PRIV | Privacy | §5.2 | 免费 |
| CAP-ANN | Annoyances | §5.3 | 免费 |
| CAP-REG | Regional Ad Blocking | §5.4 | 免费 |
| CAP-YTX | YouTube & X（Safari） | §5.5 | Pro |
| CAP-BAT | Battery Boost | §5.6 | Pro |
| CAP-STRICT | Strict Mode | §5.7 | Pro |
| CAP-TAP | Tap to Block | §5.8 | Pro |
| CAP-CAT | 类别开关（无全局总开关） | §5.9 / §5.12 | 免费 |
| CAP-SITE | 站点放行（Safari 扩展） | §5.10 | 免费 |
| CAP-UPDATE | 规则更新 | §5.11 | 免费 |
| CAP-HONEST | 诚实状态 / 无假保护中 | §5.12、§10.3 | — |
| CAP-COMPAT | 误杀可恢复 / 关键站完整 | §2.3、§10.1 | — |

### 1.3 推荐记录字段

| 字段 | 示例 |
|------|------|
| URL | https://m.youtube.com |
| 系统语言 | en-US / ja / ko / en-AU |
| 模式 | Free 默认 · +YTX · +Strict · +Tap |
| 广告 | 明显减少 / 部分 / 否 |
| 弹层/CMP | 改善 / 无变化 / 误伤 |
| 功能损坏 | 无 / 图片 / 播放 / 结账 / 登录… |
| 恢复 | 无需 · 关相关类别 · 扩展放行 |
| 构建 / 规则版本 | — |
| 备注 | — |

### 1.4 通过标准（与总纲领 §10 对齐）

1. 默认开启 Ads / Privacy / Annoyances / Regional 后，P0 新闻与门户站**广告或追踪干扰明显减少**（不要求 100%）。  
2. Wikipedia、政务、公营媒体等**不应被明显破坏**。  
3. Amazon / 购物站图片与核心路径可用；损坏时可通过**关相关类别或扩展放行**恢复（CAP-SITE / CAP-CAT）。  
4. YouTube / X **仅在 Safari 网页 + Pro** 验收；文案不承诺原生 App。  
5. 扩展或 Content Blocker 被关时，不得显示「保护中」（CAP-HONEST）。

---

## 2. 最小回归套件（约 25 站，发版默认）

系统语言先 `en-US` 全跑；再各用 `ja` / `ko` / `en-AU` 抽 5 站。

| # | URL | 能力 | 优先级 | 说明 |
|---|-----|------|--------|------|
| 1 | https://www.google.com | CAP-ADS, CAP-COMPAT | P0 | 搜索结果完整性 |
| 2 | https://m.youtube.com | CAP-YTX | P0 | Pro：预/中插；播放器完整 |
| 3 | https://x.com | CAP-YTX | P0 | Pro：推广内容 |
| 4 | https://en.wikipedia.org | CAP-COMPAT | P0 | 干净站零误伤 |
| 5 | https://www.reddit.com | CAP-ADS | P0 | 信息流广告 |
| 6 | https://www.cnn.com | CAP-ADS, CAP-PRIV | P0 | 美区新闻重广告 |
| 7 | https://www.dailymail.co.uk | CAP-ADS, CAP-ANN | P0 | 英区小报极重广告 |
| 8 | https://www.bbc.co.uk | CAP-COMPAT, CAP-REG | P0 | 英区头部；少广告也要完整 |
| 9 | https://www.theguardian.com | CAP-ANN, CAP-ADS | P0 | CMP + 赞助 |
| 10 | https://www.amazon.com | CAP-COMPAT, CAP-ADS | P0 | 购物误杀矩阵 |
| 11 | https://www.yahoo.com | CAP-ADS, CAP-PRIV | P0 | 门户展示广告 |
| 12 | https://www.gov.uk | CAP-COMPAT | P0 | 政务零误伤 |
| 13 | https://www.spiegel.de | CAP-ANN, CAP-REG | P0 | 德文 CMP（语言 `de`） |
| 14 | https://www.lemonde.fr | CAP-ANN, CAP-REG | P0 | 法文 CMP（语言 `fr`） |
| 15 | https://www.yahoo.co.jp | CAP-REG, CAP-ADS | P0 | 日区门户（语言 `ja`） |
| 16 | https://www.amazon.co.jp | CAP-COMPAT, CAP-REG | P0 | 日区购物误杀 |
| 17 | https://www.rakuten.co.jp | CAP-REG, CAP-ADS | P0 | 日区电商 |
| 18 | https://www.naver.com | CAP-REG, CAP-ADS | P0 | 韩区头部（语言 `ko`） |
| 19 | https://www.coupang.com | CAP-COMPAT, CAP-REG | P0 | 韩区购物 |
| 20 | https://namu.wiki | CAP-REG, CAP-ADS | P0 | 韩区高流量 Wiki |
| 21 | https://www.news.com.au | CAP-ADS, CAP-REG | P0 | 澳区重广告（语言 `en-AU`） |
| 22 | https://www.abc.net.au | CAP-COMPAT | P0 | 澳公营媒体 |
| 23 | https://www.amazon.com.au | CAP-COMPAT | P0 | 澳区购物 |
| 24 | https://maps.google.com | CAP-COMPAT | P0 | 地图冒烟 |
| 25 | https://mail.google.com | CAP-COMPAT | P0 | 邮件登录/列表冒烟 |

**模式叠加（在 2–3、6–11 上追加）：**

- +Strict（CAP-STRICT）：记录 breakage，确认可关 Strict 或扩展放行恢复。  
- +Tap（CAP-TAP）：任选 2 个仍有残留元素的新闻站。  
- 规则更新后（CAP-UPDATE）：抽跑本表 P0 子集。

---

## 3. 跨区共用全球站

| 站点 | URL | 能力 | 优先级 | 测试重点 |
|------|-----|------|--------|----------|
| Google | https://www.google.com | CAP-ADS, CAP-COMPAT | P0 | 搜索广告 vs 自然结果；勿误伤结果页 |
| YouTube 网页 | https://m.youtube.com | CAP-YTX | P0 | 预/中插；评论与推荐 |
| X | https://x.com | CAP-YTX | P0 | 推广帖；媒体加载 |
| Wikipedia | https://en.wikipedia.org | CAP-COMPAT | P0 | 几乎无广告；完整性 |
| Reddit | https://www.reddit.com | CAP-ADS | P0 | 信息流广告、线程展开 |
| Instagram Web | https://www.instagram.com | CAP-ADS, CAP-COMPAT | P1 | 登录墙、feed 广告占位 |
| Facebook Web | https://www.facebook.com | CAP-ADS, CAP-PRIV | P1 | 信息流广告、重脚本 |
| ChatGPT | https://chatgpt.com | CAP-COMPAT | P1 | SPA 勿误杀核心 UI |
| Bing | https://www.bing.com | CAP-ADS | P2 | 搜索广告 |
| LinkedIn | https://www.linkedin.com | CAP-ADS | P2 | 推广职位 |
| TikTok Web | https://www.tiktok.com | CAP-COMPAT | P2 | 重脚本视频站 |
| Twitch | https://www.twitch.tv | CAP-ADS | P2 | 视频贴片广告 |

---

## 4. 欧美（US / UK / EU）

### 4.1 美国

| 站点 | URL | 能力 | 优先级 | 测试重点 |
|------|-----|------|--------|----------|
| Amazon | https://www.amazon.com | CAP-COMPAT, CAP-ADS | P0 | 图片、加购、推荐条 |
| Yahoo | https://www.yahoo.com | CAP-ADS, CAP-PRIV | P0 | 展示广告、跟踪 |
| CNN | https://www.cnn.com | CAP-ADS, CAP-PRIV | P0 | 多广告位、自动播放 |
| NYTimes | https://www.nytimes.com | CAP-ADS | P0 | 订阅墙 + 广告混排 |
| ESPN | https://www.espn.com | CAP-ADS | P0 | 视频广告、比分页 |
| Weather.com | https://weather.com | CAP-ADS | P1 | 重度广告 |
| Walmart | https://www.walmart.com | CAP-COMPAT | P1 | 商品图、筛选 |
| eBay | https://www.ebay.com | CAP-ADS, CAP-COMPAT | P1 | 列表广告 vs 商品 |
| Target | https://www.target.com | CAP-COMPAT | P1 | 结账路径 |
| Craigslist | https://www.craigslist.org | CAP-COMPAT | P1 | 极简页勿过度拦截 |
| BuzzFeed | https://www.buzzfeed.com | CAP-ADS | P1 | 原生广告 |
| Fox News | https://www.foxnews.com | CAP-ADS | P1 | 视频 + 展示 |
| Washington Post | https://www.washingtonpost.com | CAP-ADS | P1 | 订阅墙 |
| IMDb | https://www.imdb.com | CAP-ADS | P2 | 列表广告 |
| Pinterest | https://www.pinterest.com | CAP-ADS | P2 | 推广 pin |
| Zillow | https://www.zillow.com | CAP-COMPAT | P2 | 地图/图 |
| WebMD | https://www.webmd.com | CAP-ADS | P2 | 重度广告 |
| Quora | https://www.quora.com | CAP-ADS | P2 | 推广回答 |
| Gmail Web | https://mail.google.com | CAP-COMPAT | P0 | 勿断登录/同步 |
| Google Maps | https://maps.google.com | CAP-COMPAT | P0 | 图块与搜索框 |

### 4.2 英国

| 站点 | URL | 能力 | 优先级 | 测试重点 |
|------|-----|------|--------|----------|
| BBC | https://www.bbc.co.uk | CAP-COMPAT, CAP-REG | P0 | 英区头部 |
| BBC News | https://www.bbc.com/news | CAP-COMPAT | P0 | 国际版布局 |
| Amazon UK | https://www.amazon.co.uk | CAP-COMPAT | P0 | 购物误杀 |
| The Guardian | https://www.theguardian.com | CAP-ANN, CAP-ADS | P0 | 赞助、CMP |
| Daily Mail | https://www.dailymail.co.uk | CAP-ADS, CAP-ANN | P0 | 广告/弹层极重 |
| Sky News | https://news.sky.com | CAP-ADS | P1 | 视频 + 展示 |
| The Sun | https://www.thesun.co.uk | CAP-ADS | P1 | 重度广告 |
| Telegraph | https://www.telegraph.co.uk | CAP-ADS | P1 | 订阅墙 |
| Independent | https://www.independent.co.uk | CAP-ADS | P1 | 展示广告 |
| GOV.UK | https://www.gov.uk | CAP-COMPAT | P0 | 政务必须完整 |
| eBay UK | https://www.ebay.co.uk | CAP-COMPAT | P1 | 列表/出价 |
| Argos | https://www.argos.co.uk | CAP-COMPAT | P1 | 商品图、库存 |
| John Lewis | https://www.johnlewis.com | CAP-COMPAT | P1 | 零售路径 |
| Rightmove | https://www.rightmove.co.uk | CAP-COMPAT | P2 | 地图/相册 |
| BBC iPlayer | https://www.bbc.co.uk/iplayer | CAP-COMPAT | P2 | 播控完整性（注意地区限制） |
| NHS | https://www.nhs.uk | CAP-COMPAT | P1 | 医疗可信站 |

### 4.3 欧洲大陆（DE / FR / 通用）— 兼测 Annoyances

| 站点 | URL | 能力 | 优先级 | 测试重点 |
|------|-----|------|--------|----------|
| Spiegel | https://www.spiegel.de | CAP-ANN, CAP-REG, CAP-ADS | P0 | 德文 CMP（`de`） |
| Bild | https://www.bild.de | CAP-ADS, CAP-ANN | P0 | 极重广告 |
| t-online | https://www.t-online.de | CAP-ADS | P1 | 门户广告 |
| Amazon DE | https://www.amazon.de | CAP-COMPAT | P0 | 购物 |
| Kleinanzeigen | https://www.kleinanzeigen.de | CAP-ADS, CAP-COMPAT | P1 | 分类 |
| Le Monde | https://www.lemonde.fr | CAP-ANN, CAP-ADS | P0 | 订阅 + 广告（`fr`） |
| Le Figaro | https://www.lefigaro.fr | CAP-ADS | P1 | 展示广告 |
| Le Boncoin | https://www.leboncoin.fr | CAP-REG, CAP-ADS | P0 | 法区分类 |
| Amazon FR | https://www.amazon.fr | CAP-COMPAT | P1 | 购物 |
| Orange | https://www.orange.fr | CAP-ADS | P2 | 法区门户 |
| Booking | https://www.booking.com | CAP-PRIV, CAP-COMPAT | P1 | 多语言、重跟踪 |
| Wikipedia DE/FR | https://de.wikipedia.org · https://fr.wikipedia.org | CAP-COMPAT | P1 | 本地语言完整性 |

**EU Annoyances 脚本：** 系统语言 `de` / `fr` / `en-GB` 各开 3 个新闻首页，记录 Cookie/隐私弹层是否被抑制、是否误伤正文（CAP-ANN）。

---

## 5. 日本（JP）

系统语言建议 `ja` 以验收 CAP-REG。

| 站点 | URL | 能力 | 优先级 | 测试重点 |
|------|-----|------|--------|----------|
| Yahoo! JAPAN | https://www.yahoo.co.jp | CAP-REG, CAP-ADS | P0 | 日区头部门户 |
| YouTube | https://m.youtube.com | CAP-YTX | P0 | 同全球 + 日文 UI |
| X | https://x.com | CAP-YTX | P0 | 推广内容 |
| Amazon JP | https://www.amazon.co.jp | CAP-COMPAT, CAP-REG | P0 | 图片/按钮误杀 |
| Rakuten | https://www.rakuten.co.jp | CAP-REG, CAP-ADS | P0 | 日系电商 |
| Pixiv | https://www.pixiv.net | CAP-COMPAT, CAP-ADS | P0 | 图片墙、登录墙 |
| note | https://note.com | CAP-ADS | P1 | 文章页 |
| Livedoor | https://www.livedoor.com | CAP-ADS | P1 | 门户广告 |
| NHK | https://www3.nhk.or.jp | CAP-COMPAT | P0 | 公营；兼容优先 |
| Asahi | https://www.asahi.com | CAP-ADS, CAP-REG | P1 | 日文新闻 |
| Cookpad | https://cookpad.com | CAP-COMPAT | P2 | 图文列表 |
| Mercari Web | https://jp.mercari.com | CAP-COMPAT | P1 | 商品图 |
| Kakaku | https://kakaku.com | CAP-ADS | P1 | 比价列表广告 |
| NicoNico | https://www.nicovideo.jp | CAP-COMPAT | P2 | 播放器 |
| Google JP | https://www.google.co.jp | CAP-ADS, CAP-REG | P0 | 地区域名 |
| tenki.jp | https://tenki.jp | CAP-ADS | P2 | 本地天气广告 |

**日区必过三联：** yahoo.co.jp · rakuten.co.jp · amazon.co.jp。

---

## 6. 韩国（KR）

系统语言建议 `ko`。

| 站点 | URL | 能力 | 优先级 | 测试重点 |
|------|-----|------|--------|----------|
| Naver | https://www.naver.com | CAP-REG, CAP-ADS, CAP-PRIV | P0 | 韩区绝对头部 |
| YouTube | https://m.youtube.com | CAP-YTX | P0 | Pro 专项 |
| namu.wiki | https://namu.wiki | CAP-REG, CAP-ADS | P0 | 高流量、脚本多 |
| Daum | https://www.daum.net | CAP-REG, CAP-ADS | P0 | 门户广告 |
| Coupang | https://www.coupang.com | CAP-COMPAT, CAP-REG | P0 | 购物误杀敏感 |
| Gmarket | https://www.gmarket.co.kr | CAP-ADS, CAP-COMPAT | P1 | 列表广告 |
| 11st | https://www.11st.co.kr | CAP-ADS, CAP-COMPAT | P1 | 列表广告 |
| Nate | https://www.nate.com | CAP-ADS | P1 | 门户 |
| Chosun | https://www.chosun.com | CAP-ADS, CAP-REG | P1 | 韩文新闻 |
| DCInside | https://www.dcinside.com | CAP-ADS | P1 | 重广告社区 |
| Google KR | https://www.google.co.kr | CAP-ADS, CAP-REG | P0 | 地区域名 |

**韩区必过三联：** naver.com · coupang.com · namu.wiki。

---

## 7. 澳大利亚（AU）

系统语言建议 `en-AU`。

| 站点 | URL | 能力 | 优先级 | 测试重点 |
|------|-----|------|--------|----------|
| news.com.au | https://www.news.com.au | CAP-ADS, CAP-REG | P0 | 广告极重 |
| nine.com.au | https://www.nine.com.au | CAP-ADS | P0 | 视频 + 展示 |
| ABC Australia | https://www.abc.net.au | CAP-COMPAT | P0 | 公营媒体 |
| SMH | https://www.smh.com.au | CAP-ADS | P0 | 订阅墙 + 广告 |
| The Age | https://www.theage.com.au | CAP-ADS | P1 | 媒体广告 |
| AFR | https://www.afr.com | CAP-ADS | P1 | 媒体广告 |
| Amazon AU | https://www.amazon.com.au | CAP-COMPAT | P0 | 购物误杀 |
| eBay AU | https://www.ebay.com.au | CAP-COMPAT | P1 | 列表 |
| Seek | https://www.seek.com.au | CAP-ADS | P1 | 推广职位 |
| realestate.com.au | https://www.realestate.com.au | CAP-COMPAT | P1 | 图/地图 |
| Domain | https://www.domain.com.au | CAP-COMPAT | P1 | 房产 |
| Gumtree AU | https://www.gumtree.com.au | CAP-ADS | P1 | 分类列表 |
| Canva | https://www.canva.com | CAP-COMPAT | P1 | SPA 编辑器勿误杀 |
| CommBank | https://www.commbank.com.au | CAP-COMPAT | P0 | 银行登录页冒烟 |
| BOM | https://www.bom.gov.au | CAP-COMPAT | P1 | 政务/天气 |
| Google AU | https://www.google.com.au | CAP-ADS, CAP-REG | P0 | 地区域名 |

---

## 8. 按能力的快捷索引

| 能力 ID | 推荐站点（子集） |
|---------|------------------|
| CAP-ADS | news.com.au, dailymail.co.uk, cnn.com, yahoo.com, naver.com, yahoo.co.jp |
| CAP-PRIV | 新闻站 + amazon 商品页（关注跨站跟踪感受） |
| CAP-ANN | spiegel.de, lemonde.fr, theguardian.com, bbc.co.uk, dailymail.co.uk |
| CAP-REG | yahoo.co.jp（ja）, naver.com（ko）, bbc.co.uk（en-GB）, news.com.au（en-AU）, spiegel.de（de） |
| CAP-YTX | m.youtube.com, x.com |
| CAP-STRICT | 对已通过新闻/门户再开 Strict，记录 breakage |
| CAP-TAP | 任选 2 个仍有残留元素的新闻站 |
| CAP-COMPAT | amazon.* 各区域, coupang.com, rakuten.co.jp, maps.google.com, mail.google.com |
| CAP-SITE / CAP-CAT | 故意找一处误杀 → 扩展放行 / 关相关类别 → 恢复 |
| 零误伤白名单 | wikipedia.org, gov.uk, abc.net.au, nhk.or.jp, nhs.uk |

---

## 9. 数据边界与免责

- 站点热度参考 Similarweb / Semrush 等公开摘要（约 2025–2026）及地区日常高频入口；**非实时官方排名**。  
- Safari 常用 ≠ 移动网页体验完美；部分产品以 App 为主，Web 仍测兼容。  
- v1 **仅 Safari 网页**；原生 App 广告不在本清单范围（见总纲领 §5.5、§9）。  
- 不收录成人站；不指导绕过付费墙或地区版权限制。  
- 银行/政务仅做**兼容冒烟**，不做攻击性测试。

---

## 10. 关联文档

| 文档 | 用途 |
|------|------|
| [产品总纲领](../product/product-charter.md) | 能力边界、Free/Pro、成功标准 §10 |
| [决策记录](../decisions/decision-log.md) | D-301～D-310、D-402 等 |
| 后续 `docs/quality/test-and-acceptance.md` | 完整验收流程（待按总纲领重建） |

---

## 11. 修订记录

| 日期 | 说明 |
|------|------|
| 2026-07-28 | 初版：欧美 / 日韩 / 澳 Safari 测试站 + 能力 ID 映射 + 最小回归套件 |
