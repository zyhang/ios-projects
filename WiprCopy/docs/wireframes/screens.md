# 屏幕线框 — Gleem（v1）

ASCII 仅表示结构。**极简 chrome。界面英文。**  
无 Tab bar。无手动更新名单按钮。  
说明语言：中文。

---

## 视觉密度（全屏通用）

- 大留白；首屏元素少  
- 需要操作时优先 **一个** 主按钮；健康态为零  
- 次要操作：文字按钮或 More  
- 字体主导；图标仅在有用时出现  

---

## Welcome（3 页）— 视觉优先

权威设计文档：**[`docs/design/welcome.md`](../design/welcome.md)**。

仅首次启动。**3 页。** 插画/动效承载含义；**每页一句标题（英文）**。

| 页 | 视觉 | 标题（EN） | CTA（EN） |
|----|------|------------|-----------|
| W1 | 页面上广告/噪音消散 | Without the noise. | Continue |
| W2 | Safari + App 格子 | Safari & Apps. | Continue |
| | | 可选 micro: One purchase. No subscription. | |
| W3 | 数据留在设备 | Stays on your device. | Get Started |

```
┌─────────────────────────────────┐
│                                 │
│     [ hero art / motion ]       │
│                                 │
│        {one headline}           │
│                                 │
│           ○ ● ○                 │
│   ┌─────────────────────────┐   │
│   │   Continue / Get Started│   │
│   └─────────────────────────┘   │
└─────────────────────────────────┘
```

备注：Welcome ≠ 设置 ≠ About。Skip 可选。Reduce Motion → 静态平静帧。完整规则见 `welcome.md`。

---

## Home（根 — 无 Tab）

### 共用 chrome

```
┌─────────────────────────────────┐
│  Gleem                    More  │  ← text or ••• ; NOT tab bar
│                                 │
│         (main content)          │
│                                 │
└─────────────────────────────────┘
```

### H1 — Protected（理想默认）

```
┌─────────────────────────────────┐
│  Gleem                    More  │
│                                 │
│                                 │
│                                 │
│       You’re protected.         │  ← one line, large
│                                 │
│         Safari · Apps           │  ← quiet meta, optional
│                                 │
│                                 │
│                                 │
│                                 │
│                                 │
│      Something broken?          │  ← text only, low contrast
│                                 │
└─────────────────────────────────┘
```

**无** “Update now”。**无**名单年龄，除非日后需要单行软诊断（优先沉默）。  
健康态**无**主按钮。暂停在 More → Pause & Allowances（或日后 long-press/menu — H1 不强制）。

更安静可选：两端都开时去掉 “Safari · Apps”；仅部分开启时显示。

### H2 — Needs setup

```
┌─────────────────────────────────┐
│  Gleem                    More  │
│                                 │
│                                 │
│     Safari blocking is off.     │
│                                 │
│   ┌─────────────────────────┐   │
│   │    Enable in Safari     │   │  sole primary
│   └─────────────────────────┘   │
│                                 │
│                                 │
└─────────────────────────────────┘
```

若 Safari 与 Apps 都关：一句覆盖两者，或优先 Safari、下次再 Apps — **一次一个 CTA**。

### H3 — Locked

```
┌─────────────────────────────────┐
│  Gleem                    More  │
│                                 │
│                                 │
│     Unlock to protect           │
│     this device.                │
│                                 │
│   ┌─────────────────────────┐   │
│   │     Unlock Gleem        │   │
│   └─────────────────────────┘   │
│                                 │
│        Restore Purchase         │
│                                 │
└─────────────────────────────────┘
```

### H4 — Paused

```
┌─────────────────────────────────┐
│  Gleem                    More  │
│                                 │
│                                 │
│     Protection paused.          │
│                                 │
│   ┌─────────────────────────┐   │
│   │   Resume protection     │   │
│   └─────────────────────────┘   │
│                                 │
└─────────────────────────────────┘
```

### Home 状态文案（单句，英文）

| 状态 | 文案 |
|------|------|
| 一切正常 | You’re protected. |
| Safari 关 | Safari blocking is off. |
| Apps 关 | App blocking is off. |
| 都关 | Gleem isn’t enabled yet. |
| 已暂停 | Protection paused. |
| 未解锁 | Unlock to protect this device. |
| 少见：名单卡住 | Protection on. Lists will refresh soon. *（无按钮）* |

---

## O4 — Unlock（sheet 或全屏）

```
┌─────────────────────────────────┐
│                                 │
│     Unlock Gleem                │
│                                 │
│     Safari + apps.              │
│     Rule packs. List updates.   │
│     One purchase — no           │
│     subscription.               │
│                                 │
│   ┌─────────────────────────┐   │
│   │   Unlock — $X.XX        │   │
│   └─────────────────────────┘   │
│                                 │
│     Restore · Not now           │
│                                 │
│     Family Sharing ready.       │
└─────────────────────────────────┘
```

---

## O2 — Enable Safari（最少步骤）

```
┌─────────────────────────────────┐
│  ←                              │
│                                 │
│     Enable in Safari            │
│                                 │
│     Settings → Apps → Safari    │
│     → Extensions → Gleem        │
│                                 │
│   ┌─────────────────────────┐   │
│   │    Open Settings        │   │
│   └─────────────────────────┘   │
│                                 │
│     Done?  [ Continue ]         │
│                                 │
└─────────────────────────────────┘
```

多步收成一段短说明 + Open Settings。

---

## O3 — Enable app-wide

```
┌─────────────────────────────────┐
│  ←                              │
│                                 │
│     Enable for apps             │
│                                 │
│     Not a VPN. We don’t see     │
│     your traffic. Works with    │
│     VPNs & Private Relay.       │
│                                 │
│   ┌─────────────────────────┐   │
│   │    Enable               │   │
│   └─────────────────────────┘   │
│                                 │
│     Skip for now                │
│                                 │
└─────────────────────────────────┘
```

---

## M0 — More（仅列表）

```
┌─────────────────────────────────┐
│  ←  More                        │
│                                 │
│  Rule Packs                  ›  │
│  Pause & Allowances          ›  │
│  Report a Problem            ›  │
│  Help                        ›  │
│                                 │
│  Privacy                     ›  │
│  Acknowledgements            ›  │
│  Restore Purchase            ›  │
│  About Gleem                 ›  │
│                                 │
└─────────────────────────────────┘
```

安静分隔分组。v1 线框不要求图标。

---

## P1 — Rule Packs

```
┌─────────────────────────────────┐
│  ←  Rule Packs                  │
│                                 │
│  Core                      On   │  not a user toggle
│  Essentials. Always on.         │
│                                 │
│  Annoyances              [ ON ] │
│  Nags, banners, sign-up walls   │
│                                 │
│  Strict                 [ OFF ] │
│  Stronger. May break sites.     │
│                                 │
│  Applies to Safari and apps.    │
└─────────────────────────────────┘
```

---

## R1 — Pause & Allowances

```
┌─────────────────────────────────┐
│  ←  Pause & Allowances          │
│                                 │
│  Pause protection        [  ]   │
│                                 │
│  Allowed websites               │
│  example.com                 ✕  │
│  [ Allow a website ]            │
│                                 │
│  App blocking                   │
│  How to turn off app filter  ›  │
│                                 │
└─────────────────────────────────┘
```

---

## R2 — Allow website

```
┌─────────────────────────────────┐
│  Allow website                  │
│  [ domain                     ] │
│  Until I remove it              │
│  [ Allow ]                      │
└─────────────────────────────────┘
```

时长选项保持最少（v1 一个默认即可）。

---

## R3 — Report

```
┌─────────────────────────────────┐
│  ←  Report                      │
│                                 │
│  Only what you send below.      │
│                                 │
│  What happened?                 │
│  ┌───────────────────────────┐  │
│  │                           │  │
│  └───────────────────────────┘  │
│  Site or app (optional)         │
│  [                           ]  │
│  Email (optional)               │
│  [                           ]  │
│                                 │
│  [ Send ]                       │
└─────────────────────────────────┘
```

---

## S1 — Help

```
┌─────────────────────────────────┐
│  ←  Help                        │
│                                 │
│  Enable Safari               ›  │
│  Enable app blocking         ›  │
│  Pause or allow a site       ›  │
│  Family Sharing              ›  │
│                                 │
└─────────────────────────────────┘
```

短列表；每行打开稀疏步骤页（风格同 O2/O3）。

---

## S2 — Privacy

```
┌─────────────────────────────────┐
│  ←  Privacy                     │
│                                 │
│  We don’t collect your          │
│  browsing.                      │
│                                 │
│  Lists update in the            │
│  background without uploading   │
│  where you go.                  │
│                                 │
│  [ Privacy Policy ]             │
└─────────────────────────────────┘
```

---

## S3 — About

```
┌─────────────────────────────────┐
│  ←  About                       │
│                                 │
│  Gleem                          │
│  Block Ads & Trackers           │
│  1.0                            │
│                                 │
│  Independent. On-device.         │
│  No one pays to be unblocked.   │
│                                 │
│  Acknowledgements            ›  │
│  Contact                     ›  │
└─────────────────────────────────┘
```

---

## Mac

- 同样 Home + More（菜单栏或工具栏 trailing）。  
- 无多 Tab 工具窗口。  
- Welcome 可为一次多步面板。  
