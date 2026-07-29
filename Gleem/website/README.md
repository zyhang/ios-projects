# Stillwall Website

正式营销站 + 历史版本 Lab。

**结构决策（D-110）：** 主站采用 **Product Theater**（原 v5）全宽色带骨架。

---

## 本地预览

```bash
cd website
python3 -m http.server 8765
```

| 页面 | URL |
|------|-----|
| **正式首页** | http://127.0.0.1:8765/ |
| Privacy | http://127.0.0.1:8765/legal/privacy.html |
| Support | http://127.0.0.1:8765/legal/support.html |
| 版本 Lab | http://127.0.0.1:8765/lab/ |

---

## 目录

```
website/
├── index.html                 # 正式营销首页（Product Theater）
├── _redirects                 # Netlify：/privacy · /support
├── README.md
├── legal/
│   ├── privacy.html
│   └── support.html
├── shared/                    # 图标、截图、tokens、motion.js
├── lab/                       # 多版本对比（内部）
├── versions/                  # v1–v5 历史稿
└── docs/
    └── opendesign-refs.md
```

---

## 主体与链接（已填）

| 项 | 值 |
|----|-----|
| 法律全称 | Xiamen Yiling Information Technology Co., Ltd. |
| 对外简称 | **Yiling Labs**（页脚/营销；Privacy 内写全称 + 简称） |
| App Store | https://apps.apple.com/app/id6795497808 |
| 计划主域名 | **`yilinglabs.com`**（公司唯一域名；产品走子路径/子域） |
| 联系邮箱 | `privacy@yilinglabs.com` · `support@yilinglabs.com` |

## 域名架构（单域名 · 产品扩展）

**决策：** 只注册公司域，不单独为 Stillwall 买产品域。新产品在同一域名下扩展。

| 角色 | 推荐 URL | 说明 |
|------|----------|------|
| 公司主页（可选） | `https://yilinglabs.com/` | About / 品牌；初期可 **301 → Stillwall** |
| **Stillwall 营销站** | `https://yilinglabs.com/stillwall/` | **推荐默认**；仓库 `website/` 部署在此路径 |
| Privacy（ASC） | `https://yilinglabs.com/stillwall/privacy` | 或 `/privacy` 若站点独占根路径 |
| Support（ASC） | `https://yilinglabs.com/stillwall/support` | 同上 |
| 备选 · 子域 | `https://stillwall.yilinglabs.com/` | 产品多了、要独立部署/证书时再拆 |

**优先用子路径，而不是一上来子域：**

1. 一站点、一证书、一部署，运维简单  
2. App Store 只要稳定 HTTPS URL，路径完全合格  
3. 以后产品多了再拆：`/product-b/` 或 `product-b.yilinglabs.com`

**初期若只有 Stillwall：** 也可把 `website/` 直接挂在根  
`https://yilinglabs.com/` · `/privacy` · `/support`，等第二款产品再挪到 `/stillwall/`。

### 上线前仍须确认

1. 在注册商购买并解析 **`yilinglabs.com`**（DNS 粗查曾显示可能空闲，以实时查询为准）  
2. 配置邮箱 `privacy@` / `support@`（Cloudflare Email Routing / Google Workspace 等）  
3. ASC Privacy / Support 填最终 HTTPS URL  
4. App 上架后抽查 App Store 链接  

部署：将 `website/` 作为站点根，或挂到 `/stillwall/` 子路径（按上表二选一）。

---

## 版本对照（Lab）

| 版本 | 说明 |
|------|------|
| v1 Calm Editorial | Wipr 窄栏 |
| v2 Product Hero | 标准产品站网格 |
| v3 Quiet Manifesto | 深色理念叙事 |
| v4 Zen Calm | OpenDesign zen-browser |
| **v5 Product Theater** | 已选结构 → **已提升为正式 `index.html`** |

---

## 与 ASC 最小站关系

| 路径 | 角色 |
|------|------|
| `docs/release/app-store-assets/site/` | 早期 ASC 最小合规页（可逐步弃用） |
| `website/` | **现行营销站 + Privacy/Support** |
