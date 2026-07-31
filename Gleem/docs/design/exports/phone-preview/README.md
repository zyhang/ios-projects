# 手机预览导出（Hi-fi P0）

从 Lunacy `Stillwall-HiFi-v1.free` · **Depth Pass · Hi-fi P0** 导出。  
**最近同步：** 2026-07-31 — D-510 文案、Setup 诚实说明/深链 hint、去完成金勾、Home 进度条与 Pro 区间距；逻辑 390×844 导出并放大 **2× → 780×1688**。

| 项 | 说明 |
|----|------|
| 尺寸 | 逻辑 **390×844**，导出 **2× → 780×1688** PNG |
| 格式 | PNG，可直接 AirDrop / 相册 / Safari 打开 |
| 主路径 | `01`–`05` |
| Dark | `06`–`08` |
| Large Type | `09`–`11` |

## 在手机上看

1. **单张图：** 把 `docs/design/exports/phone-preview/*.png` 用隔空投送 / 微信发到 iPhone，在「照片」里全屏查看。  
2. **整页滑动：** 用 Mac 本地起服务后同一 Wi‑Fi 用手机 Safari 打开 `index.html`：

```bash
cd docs/design/exports/phone-preview
python3 -m http.server 8765
# 手机访问 http://<你的Mac局域网IP>:8765/
```

## 文件列表

| 文件 | 画板 |
|------|------|
| 01-Welcome.png | Welcome |
| 02-Setup.png | Setup |
| 03-Home.png | Home |
| 05-Upgrade.png | Upgrade |
| 06-Welcome-Dark.png | Welcome · Dark |
| 07-Home-Dark.png | Home · Dark |
| 08-Upgrade-Dark.png | Upgrade · Dark |
| 09-Welcome-LargeType.png | Welcome · Large Type |
| 10-Setup-LargeType.png | Setup · Large Type |
| 11-Home-LargeType.png | Home · Large Type |

扩展 popup（SE）目前仅在线框稿；未包含在本批 Hi-fi 导出中。次级预览见 [`../secondary-preview/`](../secondary-preview/)。

## Lunacy 导出（2026-07-31）

从 **`Stillwall-HiFi-v1.free` · Depth Pass · Hi-fi P0** 经 Automation `export` **scale=2** 写入本目录（780×1688）。  
日志：[`../lunacy-export-log-2026-07-31.md`](../lunacy-export-log-2026-07-31.md)。

| 注意 | 说明 |
|------|------|
| **D-317** | 当前 Hi-fi 画板 **仍含** Strict / Tap；改稿前导出**不能**当 D-317 终稿 |
| Welcome CTA | 以稿面为准；若仍为旧串须改稿后重导 |
| 次级/扩展 | 在 Wireframes；须在 MCP 当前文档中打开后再导 |

Issue after 目标图已从本目录同步：001 / 003 / 004 / 005。
