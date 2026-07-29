# release

发布、TestFlight 与 **App Store 提审** 资料。

## App Store（v1 基础包）

| 文件 | 说明 |
|------|------|
| [app-store-submission.md](app-store-submission.md) | **提审总览**（名称、分类、订阅、隐私、清单） |
| [grilling-decisions-2026-07-28.md](grilling-decisions-2026-07-28.md) | grilling 锁定决策 |
| [app-store-assets/](app-store-assets/) | 图标、文案、截图计划、ASC 速填表 |

### 资产

- **Icon：** `app-store-assets/icon/AppIcon-1024.png`（+ 多尺寸）  
- **Copy：** `app-store-assets/copy/*.txt` / privacy & support markdown  
- **Screenshots（成片）：**  
  - **iPhone（ASC 合规竖屏）：**  
    - `app-store-assets/screenshots/iphone-6.5-1242x2688/`（**1242×2688**，优先）  
    - `app-store-assets/screenshots/iphone-6.5-1284x2778/`（**1284×2778**）  
  - iPad：`app-store-assets/screenshots/ipad-13/`  
  - 计划：`app-store-assets/screenshot-plan.md`  
  - 注意：`iphone-6.7/`（1290×2796）为旧尺寸，当前 ASC 槽勿用
- **可部署站点：** `app-store-assets/site/`（`privacy.html` · `support.html` · `index.html`）  
  - 本地预览：`cd app-store-assets/site && python3 -m http.server 8765`  

### 上架前门禁

见 [app-store-submission.md](app-store-submission.md) 顶部 checklist（V-001 / V-003 / V-004、真 URL、法务名、Bundle `<org>`）。
