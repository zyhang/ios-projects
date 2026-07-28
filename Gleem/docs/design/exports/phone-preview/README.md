# 手机预览导出（Hi-fi P0）

从 Lunacy `Stillwall-HiFi-v1.free` · **Depth Pass · Hi-fi P0** 导出。

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
| 03-Home-On.png | Home · On |
| 04-Home-Off.png | Home · Off |
| 05-Upgrade.png | Upgrade |
| 06-Welcome-Dark.png | Welcome · Dark |
| 07-Home-Dark.png | Home · Dark |
| 08-Upgrade-Dark.png | Upgrade · Dark |
| 09-Welcome-LargeType.png | Welcome · Large Type |
| 10-Setup-LargeType.png | Setup · Large Type |
| 11-Home-LargeType.png | Home · Large Type |

扩展 popup（SE）目前仅在线框稿；未包含在本批 Hi-fi 导出中。
