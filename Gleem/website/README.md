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
| 联系邮箱（待域名落地） | `privacy@stillwall.app` · `support@stillwall.app` |

### 上线前仍须确认

1. **域名**与上述邮箱是否最终使用 `stillwall.app`（若否，全局替换邮箱与 README）  
2. ASC Privacy / Support URL → `https://<domain>/privacy` · `/support`（`_redirects`）  
3. App 上架后抽查 App Store 链接是否可打开产品页  

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
