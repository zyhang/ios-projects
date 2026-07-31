# Screenshot plan (v1)

## Sequence (locked)

| Order | Source UI | Title | Subtitle | Store-ready files |
|------:|-----------|-------|----------|-------------------|
| 1 | `03-Home.png` | A quieter Safari, on your terms | Choose what stays out of your way | `01-Home.png` |
| 2 | `01-Welcome.png` | A quieter Safari | Ads, trackers, and annoyances blocked | `02-Welcome.png` |
| 3 | `02-Setup.png` | Enable in a few steps | Turn on Stillwall in Safari settings | `03-Setup.png` |
| 4 | `03-Home.png` | Block ads, trackers, annoyances | Free core protection. Pro when you need it | `04-Home-Features.png` |
| 5 | `05-Upgrade.png` | Pro tools when you need them | YouTube & X in Safari · Tap to Block | `05-Upgrade.png` |
| 6 | `03-Home.png`（能力列表近景） | Categories you control | Turn features on or off as you need | `06-Home-Categories.png`（可选） |

UI 源：`docs/design/exports/phone-preview/`  
成片目录：`docs/release/app-store-assets/screenshots/`

**文案（D-510 / issue 008）：** Welcome 主 CTA 权威为 **Set Up in Safari**。导出与成片须替换弃用串 `Set Up Safari Protection`；Setup 须诚实 **6 Content Blockers + Web Extension**（勿 *both extensions*）；商店框外 Title/Subtitle 不受影响。URL 尾部用 `yilinglabs.com`（见 description）。

## 尺寸（以 ASC 报错/当前槽为准）

Connect 要求的 **iPhone 竖屏** 合法尺寸包括：

| 像素 | 路径（本仓库已生成） | 建议用途 |
|------|----------------------|----------|
| **1242 × 2688** | `screenshots/iphone-6.5-1242x2688/` | 优先上传此套 |
| **1284 × 2778** | `screenshots/iphone-6.5-1284x2778/` | 备选同等内容 |

亦接受横屏：`2688 × 1242`、`2778 × 1284`（本包未生成横屏）。

| 其它目录 | 说明 |
|----------|------|
| `iphone-6.7/`（1290×2796） | **旧错误尺寸，已删除** |
| `ipad-13/`（2064×2752） | iPad 槽；若 ASC 对 iPad 另有尺寸要求再改 |

## Style

- 顶栏品牌绿 `#2F6A58` + 白/浅绿标题  
- 浅灰画布 `#F2F2F7` + 居中设备图  
- 第 6 张使用能力列表近景，其余保持完整设备画面
- 浅色主套；Dark / Large Type 不作主槽  

## App Store Connect

- [x] 带标题成片（**1242×2688** 与 **1284×2778**）  
- [x] Welcome CTA / Setup 诚实文案像素已于 2026-07-31 刷新（issue **008**）  
- [ ] 上传 `iphone-6.5-1242x2688/` 全套（或 1284×2778）  
- [ ] iPad 槽按 ASC 要求核对尺寸后上传  
- [x] 无 App Preview