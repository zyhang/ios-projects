# Screenshot plan (v1)

## Sequence (locked)

| Order | Source UI | Title | Subtitle | Store-ready files |
|------:|-----------|-------|----------|-------------------|
| 1 | `03-Home-On.png` | All quiet in Safari | Protection that stays out of the way | `screenshots/iphone-6.7/01-…` · `ipad-13/01-…` |
| 2 | `01-Welcome.png` | A quieter Safari | Ads, trackers, and annoyances blocked | `02-…` |
| 3 | `02-Setup.png` | Enable in a few steps | Turn on Stillwall in Safari settings | `03-…` |
| 4 | `03-Home-On.png` | Block ads, trackers, annoyances | Free core protection. Pro when you need it | `04-…` |
| 5 | `05-Upgrade.png` | Pro tools when you need them | YouTube & X in Safari · Tap to Block | `05-…` |
| 6 | `04-Home-Off.png` | One switch. Full control | Pause everything anytime | `06-…`（可选） |

UI 源：`docs/design/exports/phone-preview/`  
成片目录：`docs/release/app-store-assets/screenshots/`

## 尺寸

| 套 | 像素 | 路径 |
|----|------|------|
| iPhone 6.7" | **1290 × 2796** | `screenshots/iphone-6.7/` |
| iPad 13" | **2064 × 2752** | `screenshots/ipad-13/` |

## Style

- 顶栏品牌绿 `#2F6A58` + 白/浅绿标题  
- 浅灰画布 `#F2F2F7` + 居中设备图  
- 底部 Stillwall chip  
- 浅色主套；Dark / Large Type 不作主槽  

## App Store Connect

- [x] 带标题成片已生成（脚本）  
- [ ] 上传 iPhone 6.7"/6.9" 槽（以 ASC 当前必填为准；可用 1290×2796）  
- [ ] 上传 iPad 13" 槽  
- [x] 无 App Preview  

## 重新生成

```bash
# 若更新了 phone-preview，重跑 compose 脚本（见会话或 release 维护脚本）
python3 -c "print('re-run screenshot compose from docs if needed')"
```

源 UI 更新后，用同一序列重跑 compose 逻辑（品牌色与标题表见上表）。
