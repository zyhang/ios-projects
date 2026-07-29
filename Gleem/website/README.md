# Stillwall Website Lab

营销网站多版本工作区。目标：**简洁、理念清晰、具备 App 落地页必备模块**，并在细节处保留克制动效。

> 现有 App Store 合规最小站仍在  
> `docs/release/app-store-assets/site/`（Privacy / Support 占位）。  
> 本目录用于正式营销站探索与对比，选定方向后再合并上线结构。

---

## 本地预览

```bash
cd website
python3 -m http.server 8765
# 打开 http://127.0.0.1:8765/
```

对比入口：`index.html`  
各版本：`versions/v1-calm-editorial/` · `v2-product-hero/` · `v3-quiet-manifesto/`

---

## 目录结构

```
website/
├── index.html                 # 版本对比入口（内部 lab，noindex）
├── README.md
├── legal/                     # 全版本共用法律 / 支持页
│   ├── privacy.html
│   └── support.html
├── shared/
│   ├── assets/
│   │   ├── icon-*.png
│   │   ├── app-store-badge.svg
│   │   └── screenshots/       # 来自 design exports
│   ├── css/
│   │   └── tokens.css         # 品牌色 / 间距 token
│   └── js/
│       └── motion.js          # 滚动显现；尊重 reduced-motion
└── versions/
    ├── v1-calm-editorial/     # Wipr 式窄栏编辑排版
    ├── v2-product-hero/       # Hero + 手机 mock + 特性网格
    └── v3-quiet-manifesto/    # 深色理念叙事
```

后续新增版本建议：`versions/v4-<slug>/index.html`，并在根 `index.html` 卡片中登记。

---

## 版本一览

| 版本 | 气质 | 主要参考 | 适合何时选 |
|------|------|----------|------------|
| **v1 Calm Editorial** | 窄栏、文案优先、系统字体 | [Wipr](https://kaylees.site/wipr2.html) | 想要独立开发者气质、极简可信 |
| **v2 Product Hero** | 完整产品站模块、浅色 | [Magic Lasso](https://www.magiclasso.co/)（简化） | 默认上线候选、信息结构最全 |
| **v3 Quiet Manifesto** | 深色、原则叙事、氛围动效 | [Purify](https://www.purify-app.com/) 语气 + [UIBook](https://uibook.art/) 克制美学 | 强调品牌理念与「安静」 |

### 各版本共同具备（App 落地页最佳实践）

- 价值主张 / 一句话定位  
- App Store 下载 CTA（占位链接，待上架后替换）  
- 免费能力与 Pro 边界（诚实：Safari only、非 VPN）  
- Privacy Policy · Support 链接  
- 页脚法律主体占位  
- 品牌色对齐 App（`#2F6A58`）  
- 细节动效 + `prefers-reduced-motion`  

---

## 上线前必改

1. 替换所有 `href="#download"` / `#app-store` 为真实 App Store URL  
2. 替换 `\<LEGAL_ENTITY_NAME\>`、`privacy@\<domain\>`、`support@\<domain\>`  
3. 选定单一版本作为站点根（或把其 `index.html` 提升到 `website/` 并调整相对路径）  
4. 配置 `/privacy` · `/support` 路由（参考 `docs/release/app-store-assets/site/_redirects`）  
5. 去掉 lab 入口的 `noindex`（若 lab 不对外则保持）  

---

## 设计约束（与产品一致）

- 文案以英文对外（商店与 UI 一致）；协作说明可用中文  
- 不夸大「全 App 去广告」；YouTube/X 写清 **in Safari**  
- 不做威胁计数、赛博安全视觉  
- 动效服务状态与层次，不延迟关键反馈  

---

## 与旧站点关系

| 路径 | 角色 |
|------|------|
| `docs/release/app-store-assets/site/` | ASC 最小合规页（可继续部署） |
| `website/` | 营销站设计 lab + 未来正式站候选 |
