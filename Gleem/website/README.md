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

## 上线前必改

1. **App Store URL** — `index.html` 中 `#app-store-link` 与所有 Download 按钮 `href`
2. **法律主体** — `\<LEGAL_ENTITY_NAME\>`
3. **联系邮箱** — `privacy@…` / `support@…`（legal 页）
4. **域名** — 部署后把 ASC Privacy / Support URL 设为  
   `https://<domain>/privacy` · `https://<domain>/support`  
   （依赖 `_redirects` 或等价 rewrite）

部署：将 `website/` 作为站点根（Netlify / GitHub Pages / Cloudflare Pages）。

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
