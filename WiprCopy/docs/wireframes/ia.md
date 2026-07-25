# 信息架构 — Gleem

低保真。**界面英文。** 极简。iPhone 优先；Mac/iPad 共用同一层级。  
说明语言：中文。

## 设计原则（导航与框架）

1. **无 Tab bar。** 唯一主表面是 Home。其余一律从单一次级入口 **More**（Wipr 式 overflow）push 进入。  
2. **健康态 Home 几乎为空** — 一句状态、可选安静次要信息、仅在需要时一个主操作。  
3. **名单自动更新** — Home（及 v1 UI）永不出现手动 “Update rules”。名单过期仅以软状态/诊断文案呈现（若真有问题）。  
4. **Welcome 视觉优先** — 品类（安静拦截）→ **Safari** → 信任；不是设置倾倒。**不以 system-wide 为主叙事**（PRD 2026-07-25）。结构见 [screens.md](screens.md)。  
5. **文案与密度** — 短英文句、大留白、少按钮。Indie 冷静，非仪表盘。  

## 导航模型（v1）

```
┌──────────────────────────────────────┐
│  Home  (root, always)                │
│    status · fix/unlock if needed     │
│    [More]  →  list of secondary      │
└──────────────────────────────────────┘
         │
         ▼ push
┌──────────────────────────────────────┐
│  More (plain list)                   │
│    Rule Packs                        │
│    Pause & Allowances                │
│    Report a Problem                  │
│    Help                              │
│    Privacy                           │
│    Acknowledgements                  │
│    Restore Purchase                  │
│    About Gleem                       │
└──────────────────────────────────────┘
```

| 入口 | 方式 |
|------|------|
| **Home** | 根。无 Tab。 |
| **More** | 工具栏 trailing，或右上安静文字按钮（Wipr 风）。不是底部 Tab。 |
| 深层页 | 从 More（或 Home CTA 进设置）标准返回栈。 |

**Mac：** 单窗口；Home 为主；More 打开列表或 sheet。侧边栏仅当仍像「一个 App、一个状态」时可选，勿做成多模块 IDE。

```
Gleem
├── Welcome (3 pages, first launch only)
├── Home
│   ├── One-sentence status
│   ├── Safari / Apps (minimal presence indicators — only if useful)
│   ├── Diagnostics line (only if misconfigured / paused / locked)
│   └── Single primary CTA when action required
│         (no “Update lists” button)
│
└── More → …
    ├── Rule Packs
    ├── Pause & Allowances
    ├── Report a Problem
    ├── Help
    ├── Privacy
    ├── Acknowledgements
    ├── Restore Purchase
    └── About Gleem
```

## 屏幕清单（v1）

| ID | 屏幕 | 如何打开 |
|----|------|----------|
| W1–W3 | Welcome 页 | 首次启动 |
| H1 | Home — Protected | 根 |
| H2 | Home — Needs setup | 根 |
| H3 | Home — Locked | 根 |
| H4 | Home — Paused | 根 |
| O2 | Enable Safari | Home CTA / Help |
| O3 | Enable app-wide | Home CTA / Help |
| O4 | Unlock | Home CTA / Welcome 结束 |
| M0 | More 列表 | Home → More |
| P1 | Rule Packs | More |
| R1 | Pause & Allowances | More / Home “Something broken?” |
| R2 | Allow website | R1 sheet |
| R3 | Report a Problem | More |
| S1 | Help hub | More |
| S2 | Privacy | More |
| S3 | About | More |
| S4 | Acknowledgements | More |

## Home 故意不放的内容

- 手动刷新名单  
- 拦截次数 / 图表  
- 健康态多按钮操作行  
- 底部导航  
