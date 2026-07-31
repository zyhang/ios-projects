# Screenshot plan (v1)

## Sequence（叙事锁定 · 2026-07-31 修订）

**原则：** 框外 Title/Subtitle 服务**首次普通人** 3 秒扫读；语气与产品一致——安静、诚实、不承诺 100% 清空；**不**用威胁计数。

| Order | Source UI | Title（框外） | Subtitle（框外） | Store file |
|------:|-----------|---------------|------------------|------------|
| 1 | `03-Home.png` | A quieter Safari, on your terms | Choose what stays out of your way | `01-Home.png` |
| 2 | `01-Welcome.png` | A quieter Safari | Ads, trackers, and annoyances stay out of your way | `02-Welcome.png` |
| 3 | `02-Setup.png` | Enable in a few steps | Content blockers + extension in Safari | `03-Setup.png` |
| 4 | `03-Home.png` | Free core protection | Ads, privacy, annoyances—yours to control | `04-Home-Features.png` |
| 5 | `05-Upgrade.png` | Pro tools when you need them | YouTube & X in Safari · Battery Boost | `05-Upgrade.png` |
| 6 | `03-Home.png`（列表近景） | Categories you control | Turn features on or off as you need | `06-Home-Categories.png` |

### 相对旧稿的变更

| 槽 | 旧 Subtitle / 语气 | 新 | 原因 |
|----|--------------------|----|------|
| 2 | *Ads, trackers, and annoyances **blocked*** | *…**stay out of your way*** | 避免「已 100% 拦截」绝对感；与 Welcome 副文案同源 |
| 3 | Turn on Stillwall in Safari settings | **Content blockers + extension in Safari** | 诚实预告 6+1 形态，不装成「一键」 |
| 4 | Free core protection. Pro when you need it | **Ads, privacy, annoyances—yours to control** | 强化「类别可控」而非堆 Pro |

UI 源：`docs/design/exports/phone-preview/`  
成片目录：`docs/release/app-store-assets/screenshots/`

**框内 UI（D-510 / 008）：**

- Welcome CTA = **`Set Up in Safari`**  
- Setup = 6 Content Blockers + Web Extension；无完成金勾  
- Home = 中性 Value Hero（实现见 001）  
- 价格像素 = **$14.99**（实现见 004）

成片顶栏文案下次生成脚本时按上表刷新；**当前仓库成片顶栏可能仍为旧 subtitle**——上传前优先改 Title/Subtitle 字符串或重跑套图。

## 尺寸

| 像素 | 路径 | 用途 |
|------|------|------|
| **1242 × 2688** | `screenshots/iphone-6.5-1242x2688/` | 优先上传 |
| **1284 × 2778** | `screenshots/iphone-6.5-1284x2778/` | 备选 |
| **2064 × 2752** | `screenshots/ipad-13/` | iPad 槽 |

## Style

- 顶栏品牌绿 `#2F6A58` + 白/浅绿标题  
- 浅灰画布 `#F2F2F7` + 居中设备图  
- 第 6 张列表近景；其余完整设备  
- 浅色主套；Dark / Large Type 不作主槽  
- **禁止：** 假拦截大数字、红警威胁风、与 App 不一致的旧 CTA  

## 叙事弧（给营销/设计）

```text
1 结果感（安静 Home）
2 品牌承诺（Welcome · 非绝对 blocked）
3 启用真实（Setup · blockers + extension）
4 免费核心可控
5 Pro 增强（Safari only）
6 类别开关细节
```

## App Store Connect

- [x] 带标题成片尺寸就绪  
- [x] Welcome CTA / Setup 诚实文案像素（008）  
- [x] 框外叙事表修订（本文件）  
- [x] 按新 Title/Subtitle **重生成顶栏**（2026-07-31 合成；框内仍待 D-317 改稿）  
- [ ] 上传 iPhone 套  
- [ ] iPad 槽核对后上传  
- [x] 无 App Preview  
