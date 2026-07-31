# 次级页与 Safari 扩展 · 设计规格（v1）

> **产品 + 设计权威（S05–S10 + SE）。** 主路径 Hi-fi 已齐；本文件补齐次级与扩展的 **IA、文案、组件、状态**，供 Lunacy 画板与工程对稿。  
> 视觉 token：[design-system.md](design-system.md) · 英文串：[ui-copy-en.md](../engineering/ui-copy-en.md) · 扩展逻辑：[safari-extension.md](safari-extension.md)

**状态：** 2026-07-31 建立（对应 issue **006** / **009**）  
**临时可点预览：** [exports/secondary-preview/index.html](exports/secondary-preview/index.html)

---

## 1. 设计原则（次级面）

与主路径同一人格：

- `surfaceGrouped` 底 + `surfaceElevated` r18 卡  
- 单主 CTA（若有）；次要动作用系统蓝或 chevron 行  
- **无**仪表盘、威胁数、第二套主色  
- 扩展 popup：**现场 3 秒动作**，不是第二 Home  

---

## 2. S06 — More

**导航：** Home → More（`…`）→ 列表 → 各页 push / Safari / 系统订阅

| 顺序 | 行 | 行为 |
|------|-----|------|
| 1 | Help | → S07 |
| 2 | Feedback | → S09 |
| 3 | About | → S10 |
| 4 | Privacy Policy | 系统浏览器 / SFSafariView → yilinglabs.com/privacy |
| 5 | Website | → yilinglabs.com |
| 6 | Restore Purchases | StoreKit restore；结果 inline / toast 英文 |
| 7 | Manage Subscription | 系统订阅管理（或说明路径） |

**禁止：** 账号、Allowed Sites、Status · Free、调试行、Request Canceled 常驻。

**布局：** 单分组白卡；行高 ≥48；系统 chevron；无行图标（与 Home Free 克制一致）。可选将 Restore / Manage 分第二分组。

---

## 3. S07 — Help

**入口：** More → Help  

**列表行（锁定标题）：**

| 行标题 | 副文案（列表） | 详情 |
|--------|----------------|------|
| How to enable protection | Set Up in Safari · 6 blockers + extension | 见 ui-copy §7 |
| Site broken? | Pause on this site in Safari extension | 见 ui-copy §7 |
| How to open the extension | In Safari · path may vary by iOS | V-002 中性 |
| YouTube & X | Safari websites only | |
| Tap to Block | Pro · extension item 2 | |
| Send feedback | App or Report issue | |

**详情页：** large title 或 inline；正文英文；底部可链 Setup / Feedback。  
**禁止：** Home shows On；`Set Up Safari Protection`；*both extensions*。

---

## 4. S05 — Tap to Block 说明

| 用户 | 内容 |
|------|------|
| Free | 三步说明 + Pause 提示 + 主 CTA `Unlock with Stillwall Pro` → Upgrade |
| Pro | 三步说明 + Pause 提示；**无**付费 CTA（可 `Open Safari` 中性 hint，可选） |

三步（固定）：

1. Open the Stillwall extension in Safari  
2. Tap Tap to Block  
3. Select page elements  

Footer：`To pause blocking on a site, use Pause on this site in the extension.`

---

## 5. S09 — Feedback

| 区 | 规格 |
|----|------|
| 类型 | Segment 或列表：`Site broken` / `Still seeing ads` / `Other`（可与扩展 Report 对齐） |
| 描述 | 多行 TextEditor |
| 域名 | 可选；placeholder `example.com` |
| 预览 | 发送前 sheet：类型 + 域名 + 描述摘要 |
| CTA | `Send` · brandPrimary；成功后 dismiss + 简短确认 |

隐私：主动提交；不默认抓浏览历史。

---

## 6. S10 — About

| 行/块 | 内容 |
|-------|------|
| 应用名 | Stillwall |
| 版本 | CFBundleShortVersionString（+ build 可选） |
| 规则包 | 规则版本号（若有） |
| 定位句 | `Quiet ad & tracker blocking for Safari.` |
| Acknowledgements | → 规则源归因（V-004） |
| Mac | `Mac — Coming soon`（可选一行） |
| 公司 | Yiling Labs |

无营销大图；Settings 列表气质。

---

## 7. SE01 — Extension popup

### 常态（Protected）

```text
example.com
● Protected
────────────────
Pause on this site
PRO  Tap to Block
Report issue
```

### 变体

| ID | 顶栏 | 槽 1 |
|----|------|------|
| SE01 | Protected | Pause on this site |
| SE01a | Paused | Resume on this site |
| SE01b | Not enabled | 整页降级：说明 + **Open Stillwall** |
| SE01c | Off in app | Open Stillwall（槽 1）· Tap · Report 仍可 |

**尺寸：** 宽约 320；圆角 14；项 min-height 48。  
**禁止：** IAP、类别列表、第 4 常驻项、全局开关。

### SE02 Tap 点选 / SE03 Report

见 [safari-extension.md](safari-extension.md)；Hi-fi 优先级低于 SE01 四态。

---

## 8. Lunacy 画板清单（006 关闭条件）

| 画板 | 优先级 |
|------|--------|
| More | P0 |
| Help 列表 | P0 |
| Tap to Block 说明（Free） | P0 |
| SE01 Protected | P0 |
| SE01a Paused / SE01b Not enabled | P1 |
| Help 详情 · Site broken（一屏） | P2 |
| Feedback / About | P2 |

导出：`docs/design/exports/phone-preview-secondary/` 或并入 secondary-preview 截图。

---

## 9. 与主路径的关系

| 主路径 | 次级 |
|--------|------|
| Home 中性 | Help 承担「如何恢复」教育 |
| 扩展诚实状态 | 主 App 不复制 Protected pill |
| Upgrade | Tap 说明 Free CTA 进入 |
