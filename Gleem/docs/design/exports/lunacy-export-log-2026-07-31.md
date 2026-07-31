# Lunacy 高清导出记录（2026-07-31）

## Issue 对照：哪些需要从 Lunacy 导出

| Issue | 是否需要 Lunacy 高清 PNG | 说明 | 本次结果 |
|-------|--------------------------|------|----------|
| **001** Home 中性 Hero | **是**（after 目标图） | 主路径 Home | ✅ 已从 Hi-fi 导出并写入 `after/` |
| **002** 进度条 | 否（无独立画板） | 按 design-system 组件规格 | — |
| **003** Setup | **是**（after 目标图） | Setup 诚实文案/无金勾 | ✅ 已导出；**稿面仍可能含旧文案**（见下） |
| **004** Upgrade | **是**（after 目标图） | Paywall 布局 | ✅ 已导出；**稿面仍含 Strict/Tap 四利益**（D-317 未改稿） |
| **005** 跨页一致 | **是** | Welcome/Setup/Home/Upgrade + Dark/LT | ✅ 主路径 10 帧 @2× 已导出 |
| **006** 次级+扩展 | **是**（正式关闭条件） | More/Help/SE 等 | ⚠️ **未导出**：当前 MCP 连接的是 Hi-fi 文档，Wireframes 未切换到自动化会话 |
| **007** Support | 否 | 文案 | — |
| **008** 商店框内 CTA | **是**（phone-preview 源） | Welcome/Setup 像素 | ✅ 已用最新 Hi-fi 导出覆盖 phone-preview |
| **009** Help | 部分 | 视觉归 006；规格已有 | ⚠️ 随 006，Wireframes 未导出 |
| **010** 商店框外标题 | **是**（成片） | D-512 顶栏 | ✅ 已用新 phone-preview **合成**全套截图 |
| **011** 去 Strict/Tap | **是**（改稿后重导） | 须先改 Lunacy 再导出 | ⛔ **Hi-fi 稿仍含 Strict/Tap**，导出仅反映旧稿 |

## 本次执行明细

### A. 主路径 Hi-fi（`Stillwall-HiFi-v1.free` · Depth Pass · Hi-fi P0）

| 画板 | Layer ID | 输出文件（2× · 780×1688） |
|------|----------|---------------------------|
| Welcome | `3JE0c6s4QUWjuu0DMafY8Q` | `phone-preview/01-Welcome.png` |
| Setup | `BaL0CBGFB0OZ1uvkWEJCDA` | `02-Setup.png` |
| Home | `Fkm0oE4qzESlFYdqEhTDHg` | `03-Home.png` |
| Upgrade | `H9P0kdz0G0CVC64IjzUHxA` | `05-Upgrade.png` |
| Welcome Dark | `xuotA4VTfkSMo0lzXBM-qw` | `06-Welcome-Dark.png` |
| Home Dark | `3ly1SMS6dEmhP9zC1Lbpyw` | `07-Home-Dark.png` |
| Upgrade Dark | `Yltg0Mf6ZEysXvAFzNjv7g` | `08-Upgrade-Dark.png` |
| Welcome LT | `Sv80-JOkikeiAsrAVNlWZg` | `09-Welcome-LargeType.png` |
| Setup LT | `lQFqVn57-kS-w7Z7fdBOew` | `10-Setup-LargeType.png` |
| Home LT | `Vraj7y-dsUe4L6KCHXGBFg` | `11-Home-LargeType.png` |

同步到：

- `issues/001|003|004|005/.../after/*`
- `website/shared/assets/screenshots/*`

### B. 商店成片（issue **010**）

自 `phone-preview` 按 D-512 顶栏文案合成：

- `screenshots/iphone-6.5-1242x2688/`
- `screenshots/iphone-6.5-1284x2778/`
- `screenshots/ipad-13/`

各 6 张（01–06）。

### C. 次级 / 扩展（issue **006**）— 未完成

Wireframes 中已有画板（文件内 ID）：

| 画板 | ID |
|------|-----|
| S06 More | `jmk8dgF9VE2M4oF5lI1P7Q` |
| S07 Help | `8JhMceJgTUKhDrKaqiUt5g` |
| S09 Feedback | `vJHM5TsHZk-b1lRL-YfEPg` |
| S10 About | `nqkiVOCNkkevzWFDJ4Jo9Q` |
| SE01 Protected | `SE01PopupCard0000000AA` |
| SE01a Paused | `SE01aPopupCard000000AA` |
| SE01b Not enabled | `SE01bPopupCard000000AA` |
| SE01c Off in app | `SE01cPopupCard000000AA` |
| S05 Tap | `geuBCIzFHUqdVhe2sxvvCA`（**D-317 obsolete，勿导出作权威**） |

**阻塞：** Lunacy Automation 当前会话绑定 **Hi-fi** 文档（viewport 未切换）。在系统中双击打开 Wireframes 后 MCP 仍连旧文档，导出 SE/More 返回 InternalServerError。

**请你：** 在 **已连接 Automation 的那一个** Lunacy 窗口中打开 `Stillwall-Wireframes-v1.free`（或合并画板到 Hi-fi），告知后可再跑一轮导出到 `exports/secondary-preview/png/`。

## D-317 改稿 + 重导（同日续）

**已在 Lunacy live 文档删除** Strict / Tap 相关行（Home ×3、Upgrade ×2、Welcome ×3 共 26 层）。

| 画板 | 结果（live 数据） |
|------|-------------------|
| Home / Dark | `list.complete` 高约 311.65，**6 行**至 Battery |
| Home · Large Type | 列表收短，无 Strict/Tap 子层 |
| Upgrade / Dark | `Pro benefits` 高约 128.33，**仅 YT&X + Battery**；Offer/CTA 上移 |
| Welcome 系列 | Strict/Tap 卖点行已删；Daily updates 上移 |

**请用户在 Lunacy 中 Ctrl+S 保存** `Stillwall-HiFi-v1.free`，否则磁盘 `.free` 与 live 不一致。

已重导 2× PNG → `phone-preview/` + issue `after/` + 商店成片合成。

## 复现命令（Hi-fi 已打开时）

通过 MCP `lunacy__export`，`scale: 2`，layerIds 见上表。
