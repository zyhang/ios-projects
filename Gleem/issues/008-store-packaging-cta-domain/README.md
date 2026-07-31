# Issue 008：App Store 包装刷新（截图 CTA + 域名占位）

| 字段 | 内容 |
|------|------|
| 状态 | open |
| 优先级 | **P1**（上架前；不阻塞 001/004 代码，但阻塞「商店像素与 URL 诚实」） |
| 类型 | store / copy / docs-sync |
| 影响范围 | App Store 截图 · description · review notes · ASC URL 字段 |
| 相关文档 | D-108/D-109/D-113/D-510；`docs/release/app-store-assets/`；`docs/design/journey-polish-review-2026-07-31.md` |
| 创建日期 | 2026-07-31 |
| 来源 | Journey polish review 2026-07-31 |

## 问题现象

### 1. 截图框内 UI 过期

成片（如 `screenshots/iphone-6.5-*/02-Welcome.png`）与源导出 `phone-preview/01-Welcome.png` 中，主 CTA 仍为：

```text
Set Up Safari Protection
```

**D-510 权威：** `Set Up in Safari`。  
screenshot-plan 已备注「下次重导出替换」，**成片尚未更新**。首次用户在商店即看到与 App（修复后）不一致的按钮文案。

Setup 成片若仍含 *both extensions* / 预完成金勾，同样过期（与 003/005 锁定冲突）。

### 2. 描述与 Review Notes 域名占位

| 文件 | 现状 |
|------|------|
| `copy/description-en-US.txt` | `https://<domain>/privacy` · `/support` |
| `copy/review-notes-en-US.txt` | `https://<domain>/support` |
| `app-store-submission.md` 等 | 多处 `<domain>` |

**D-113 已确认：** `yilinglabs.com`（Privacy/Support：`https://yilinglabs.com/privacy` · `https://yilinglabs.com/support`）。  
Privacy 政策正文已写死 yilinglabs.com，与 description 占位**不一致**。

## 期望结果

1. **重导出** Welcome（及必要的 Setup）phone-preview → 按 `screenshot-plan.md` 再生全套 iPhone（及 iPad）成片。  
2. Welcome 像素主 CTA **仅** `Set Up in Safari`。  
3. Setup 像素：诚实 6 CB + Web Extension；顶 emblem **无**未完成即常驻金勾（design-system §7.7）。  
4. description / review-notes / submission 清单中 ASC 用 URL 全部为 **yilinglabs.com** 真值（或确认未上线时的临时策略写进 submission，禁止长期 `<domain>` 占位上架）。  
5. 框外 Title/Subtitle 序列可保持 screenshot-plan 锁定表；**可选**软化 *annoyances blocked*（intent-optional，非本 issue 必做）。

## 修改说明

| 角色 | 动作 |
|------|------|
| 设计 | Lunacy / 导出：改 CTA 与 Setup 文案 → `docs/design/exports/phone-preview/` |
| 发布 | 跑截图生成流程 → `screenshots/iphone-*` / `ipad-13` |
| 文案 | 替换 description、review-notes、submission 中 `<domain>` |
| 工程 | 无强制；App 内字符串以 005 为准，须与成片一致 |

### 与 005 的关系

005 锁文案源与跨页一致性；**008 专责商店成片与 ASC URL**。工程可先按 005 上线 App，上架上传前必须完成本 issue 截图刷新。

## 验收标准

- [ ] 全套商店 Welcome 截图像素 CTA = `Set Up in Safari`  
- [ ] Setup 成片无 *both extensions* 含糊句；无误导完成金勾  
- [ ] description / review-notes 无 `<domain>` 占位  
- [ ] ASC Privacy/Support URL 与 `yilinglabs.com` 一致且可打开  
- [ ] screenshot-plan 备注与成片状态一致（可更新 checklist 勾选）  

## 附件

- 过期示例路径：`docs/release/app-store-assets/screenshots/iphone-6.5-1284x2778/02-Welcome.png`  
- 计划：`docs/release/app-store-assets/screenshot-plan.md`  
- 报告：`docs/design/journey-polish-review-2026-07-31.md` §2.1  
