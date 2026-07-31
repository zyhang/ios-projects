# Setup 首次启用 · 认知减负规格（v1）

> **产品 + 设计权威补充。** 范围服从 [product-charter](../product/product-charter.md)；页面总表见 [screens.md](screens.md) S02；文案 key 见 [ui-copy-en.md](../engineering/ui-copy-en.md)。  
> **人格：** 诚实、冷静、Settings 气质——用清单降低漏开，不靠恐吓或「已完成」假勾。

**状态：** 已确认（Journey polish 后续 · 2026-07-31）  
**相关：** issue **003**（深链 + 诚实文案）、**D-510**、V-002（系统路径文案待验）

---

## 1. 问题（首次普通人）

系统侧真实要求是：

1. 打开 Settings → Safari → Extensions  
2. 打开 **6 个** Stillwall Content Blockers + **1 个** Web Extension  
3. Web Extension → **Allow All Websites**

若只说 *both extensions* 或只说 *all* 而不点名，用户容易：

- 只开 Web Extension  
- 只开部分 Content Blocker  
- 回到 App 仍被门禁，或「以为开了却不拦」

目标：在 **一屏 Setup** 内让用户形成可核对的心智模型，而不是再加第四步 wizard。

---

## 2. 信息结构（锁定）

保持 **三步** 主结构（勿改成 6+1 个大步骤）：

```text
Title: Enable Stillwall in Safari
Subtitle: 诚实总述（6 CB + Web Extension + website access）

① Open Settings
② Turn on Stillwall     ← 本规格加强区
③ Allow website access

[ Open Settings ]  CTA
return hint
Private by design
```

### 2.1 Step 2 加强（推荐实现 · 设计目标）

**主行（不变）：**

| 元素 | 文案 |
|------|------|
| Title | `Turn on Stillwall` |
| Detail（一行） | `Enable all 6 Content Blockers and the Web Extension` |

**附属清单（新增 · 步骤 2 下方或卡片内展开）：**

用 **小号 secondary 列表**（非第二套开关、非可点）：

```text
Look for names starting with Stillwall:

  · Ads
  · Privacy
  · Annoyances
  · Social
  · Other
  · Security
  · Web Extension   ← 与 CB 区分，可略强调
```

**设计要点：**

| 项 | 规范 |
|----|------|
| 视觉 | 嵌在 step 2 白卡内；字 13 / `textSecondary`；行距紧凑 |
| 图标 | 可选极小 bullet 或 monochrome 圆点；**无**绿色完成勾（未完成前） |
| Large Type | 清单可折叠为 `All 6 Content Blockers + Web Extension` 一行 + 展开 |
| 不要 | 要求用户在 App 内勾选 7 项；不要复制系统 UI 截图作唯一路径（V-002 未稳） |

### 2.2 文案 key（写入 ui-copy）

| Key | 文案 |
|-----|------|
| `setup.step2.checklist_lead` | `Look for names starting with Stillwall:` |
| `setup.step2.item_ads` … `security` | `Ads` / `Privacy` / `Annoyances` / `Social` / `Other` / `Security` |
| `setup.step2.item_web_extension` | `Web Extension` |
| `setup.step2.detail` | `Enable all 6 Content Blockers and the Web Extension`（保持） |

工程侧：清单为**静态说明**，不绑定权限检测勾选态（检测仍由门禁整体完成）。

---

## 3. 深链失败（与 003 一致 · 设计态）

| 态 | 视觉 | 文案方向 |
|----|------|----------|
| 默认 | 无错误条 | — |
| 深链失败 / 用户取消 | **hint** 条：`brandSoft` 或 secondary 灰，非橙红 error | `If Settings didn’t open, go to: Settings → Apps → Safari → Extensions` |
| 多次失败（可选） | 仍 hint；可略提高对比 | 同路径，勿 `Couldn't open…` 恐吓句 |

---

## 4. Emblem 与诚实状态

| 规则 | 说明 |
|------|------|
| 未完成 Setup | 顶 emblem **无**金勾 / 完成 badge |
| 检测通过离场 | 直接进 Home；**不必**在 Setup 上庆祝完成 |
| Home | 仍无 On pill（D-316） |

---

## 5. 成功标准（体验）

首次用户应能回答：

1. 我要去 **Settings → Safari → Extensions**  
2. 我要打开 **多个名字带 Stillwall 的开关**（不是「两个」）  
3. Web Extension 还要 **Allow All Websites**  
4. 回来后 App 会自己继续（门禁），不是看 Home 有没有 On  

---

## 6. 设计交付物

| 物 | 位置 |
|----|------|
| 本规格 | `docs/design/setup-first-run.md` |
| 线框/Hi-fi | 下次 Lunacy Depth Pass：Setup 画板增加 step2 清单 |
| 临时预览 | `exports/secondary-preview/` 可附 Setup 参考态（可选） |
| 开发对照 | issue **003** + `ui-copy-en.md` §2 |

---

## 7. 明确不做

- 四步以上 onboarding 长流程  
- App 内伪勾选 7 项「完成游戏」  
- 用威胁文案逼开扩展  
- 把 Content Blocker 内部技术名全部展开成段落说明  
