> **D-317（2026-07-31）：** v1 popup **仅 2 项**（Pause · Report）。下列若仍画 Tap / SE02，视为 **obsolete**，实现勿跟。

# Safari 扩展线框蓝图 SE01–SE03（v1）

> 供 Lunacy 绘制与实现对照。产品逻辑见 [safari-extension.md](safari-extension.md)。  
> **Lunacy：** 建议新画板页 `Safari Extension v1`（可与 Wireframes 同文件另页，或独立 `.free`）。  
> 当前自动化环境若未打开 Lunacy 文档，以本文为线框权威直至稿件入库。

**状态：** 线框规格已确认 · **Lunacy 已入库**（`Stillwall-Wireframes-v1.free` · ROW 4）

---

## 0. 画板总览

| 画板 ID | 名称 | 尺寸建议 | 内容 |
|---------|------|----------|------|
| **SE01** | Popup · Protected | **320 × 280**（popup 卡片；可放在 390×844 手机框内演示） | 3 项 · Pause |
| **SE01a** | Popup · Paused | 同 SE01 | 3 项 · Resume |
| **SE01b** | Popup · Not enabled | **320 × 200** | 单 CTA |
| **SE01c** | Popup · Off in app | 同 SE01 | 槽 1 引导 Open Stillwall |
| **SE02** | Tap mode chrome | 390×844 网页示意 + 顶/底工具条 | 点选中 |
| **SE03** | Report issue | 320×360 或全屏 sheet 示意 | 类型 + 域名 + 预览发送 |

**视觉 token（对齐 design-system，可简化为线框灰阶）：**

| 用途 | Light |
|------|--------|
| 卡片底 | `#FFFFFF` |
| 分组/页底 | `#F2F2F7` |
| 主文 | `#000000` 主标签 |
| 次文 | `#3C3C43` @ 60% |
| 分隔线 | `#3C3C43` @ 18% · 0.33pt |
| 保护点 | `#34C759` |
| 暂停点 | `#FF9F0A` 或次要灰 |
| 品牌（可选） | `#2F6A58` |
| Pro 金 | 仅 Tap 行小 PRO 标 `#7A5316` on `#FFF4D6` |
| 行高 | **≥ 44** pt 可点 |

---

## 1. SE01 — Popup · Protected

### 结构（自上而下）

```text
┌──────────────────────────────────┐  ← 圆角 12–14 卡片
│  padding 16                      │
│  example.com          13 regular │  ← 次要色 · 单行截断
│  ● Protected          15 medium  │  ← 绿点 8×8 + 文案
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  │  ← 分隔 全宽 inset 0 或 16
│  Pause on this site        ›     │  ← 17 regular · 行高 48
│  ─ ─ ─                           │
│  Tap to Block        PRO    ›    │  ← PRO 小胶囊可选
│  ─ ─ ─                           │
│  Report issue              ›     │
│  padding bottom 12               │
└──────────────────────────────────┘
```

### 标注

| 元素 | 规格 |
|------|------|
| 卡片宽 | **320**（Safari popup 近似；实现随系统） |
| 水平 padding | **16** |
| 顶栏 host | 次要、1 行 ellipsis |
| 顶栏状态 | 与 host 间距 **4** |
| 三项 | **仅此 3 行**；无第 4 主操作 |
| Chevron | 系统 SF Symbol 风格 `chevron.right`，次要色 |
| 禁止 | 全局开关、统计数字、品牌大 logo 占垂直空间 |

### 组件名（Lunacy）

- `SE/Popup/Card`  
- `SE/Popup/Header`  
- `SE/Popup/Row`  
- `SE/Badge/PRO`  

---

## 2. SE01a — Popup · Paused

与 SE01 **同一布局**，仅文案与状态色变：

| 元素 | 文案 |
|------|------|
| 状态 | **Paused**（橙点或灰点） |
| 槽 1 | **Resume on this site** |

其余两项不变。Lunacy 可用 Component 属性 `state=paused`。

---

## 3. SE01b — Popup · Not enabled

```text
┌──────────────────────────────────┐
│  Stillwall                       │
│  Not enabled                     │
│                                  │
│  Turn on Stillwall in Settings   │  ← 次要说明 2 行内
│  to use protection on this page. │
│                                  │
│  [ Open Stillwall ]              │  ← 单主按钮 brandPrimary 满宽
└──────────────────────────────────┘
```

- **不展示** Pause / Tap / Report 三行。  
- 主按钮高度 **50**，圆角 **12**。

---

## 4. SE01c — Popup · Off in app

```text
顶栏: example.com / Off in app
槽 1: Open Stillwall          ›   ← 或禁用 Pause 并副文案
槽 2: Tap to Block
槽 3: Report issue
```

推荐槽 1 直接 **Open Stillwall**，避免用户以为 Pause 能在全部类别 Off 下单独生效。

---

## 5. SE02 — Tap to Block（页内）

### 示意层次

1. 底层：模糊/示意新闻网页（低保真灰块即可）。  
2. 可选半透明遮罩。  
3. **顶条或底条工具栏（二选一，建议底条）：**

```text
[ Cancel ]     Tap an element to block     [ Done ]
```

4. 某一元素高亮描边 `brandPrimary` 2pt。  
5. 成功后轻 toast：`Blocked`（可选线框注释，不必独立画板）。  
6. 失败：`Couldn't block this element`。

### 未订阅

**不画**完整点选 UI；注释：从 SE01 槽 2 → 系统打开主 App Upgrade（S08）。

### Pro

行内 PRO 标记与主 App 一致。

---

## 6. SE03 — Report issue

### 布局（扩展内表单方案）

```text
Report issue          [Close]

Type
  ( ) Site broken
  ( ) Still seeing ads
  ( ) Other

Domain
  [ example.com        ]

Details (optional)
  [                    ]

[ Preview & Send ]  或  两步：Preview → Send
```

- 域名预填、可编辑。  
- 发送前预览页可与主 App Feedback 同构（注释即可）。  
- 若工程选深链方案：本画板改为「过渡说明 + Open Stillwall」一屏，并在注释写 `stillwall://feedback?...`。

---

## 7. 与主 App 对照条（可选画板）

一页并排：

| Home 全部类别 Off | SE01 Pause 本站 |
|---------------|-----------------|
| 一切不拦 | 仅该 eTLD+1 不拦 |

避免设计/开发混淆。

---

## 8. Lunacy 交付检查表

- [x] 画在 `Stillwall-Wireframes-v1.free` · **ROW 4 · Safari Extension popup**  
- [x] SE01 Protected · SE01a Paused · SE01c Off in app · SE01b Not enabled  
- [x] SE02 Tap 点选示意  
- [x] SE03 Report issue  
- [x] 英文文案对齐 3 项规格  
- [ ] 用户在 Lunacy 中 **Save** 写入磁盘（若未自动保存）  
- [ ] Hi-fi 精修（可选，跟主 App Depth Pass）  

---

## 9. 修订

| 日期 | 说明 |
|------|------|
| 2026-07-28 | 初版 SE01–SE03 线框蓝图与尺寸标注 |
| 2026-07-28 | Lunacy 写入 Wireframes v1 ROW 4 全部 SE 画板 |
