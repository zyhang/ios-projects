# Issue 010：App Store 截图框外 Title/Subtitle 按 D-512 重生成

| 字段 | 内容 |
|------|------|
| 状态 | **open** |
| 优先级 | **P1**（上架上传前；不阻塞主 App 代码） |
| 类型 | store / design / docs-sync |
| 影响范围 | App Store 截图成片顶栏文案 · ASC 上传素材 |
| 相关文档 | D-512；`docs/release/app-store-assets/screenshot-plan.md` |
| 创建日期 | 2026-07-31 |
| 来源 | 优化覆盖审计：D-512 仅写在 plan，**008 未包含框外顶栏重渲** |

## 问题现象

**008** 已处理：框内 Welcome CTA、Setup 诚实文案、域名 URL。  

**未处理：** 成片**绿色顶栏** Title / Subtitle 仍可能是旧叙事（例如槽 2 *annoyances blocked* 绝对感）。  
产品已锁定 **D-512** 柔化表，但开发/发布同学若只看「008 done」会以为商店素材全部 OK。

## 期望结果

按 [`screenshot-plan.md`](../../docs/release/app-store-assets/screenshot-plan.md) **Sequence 表**重生成（或手工改顶栏）全套：

| Order | Title | Subtitle |
|------:|-------|----------|
| 1 | A quieter Safari, on your terms | Choose what stays out of your way |
| 2 | A quieter Safari | Ads, trackers, and annoyances **stay out of your way** |
| 3 | Enable in a few steps | Content blockers + extension in Safari |
| 4 | Free core protection | Ads, privacy, annoyances—yours to control |
| 5 | Pro tools when you need them | YouTube & X in Safari · Tap to Block |
| 6 | Categories you control | Turn features on or off as you need |

目录：`iphone-6.5-1242x2688/`、`iphone-6.5-1284x2778/`、`ipad-13/`（若上传 iPad）。

框内 UI 保持 008 已刷新的 CTA / Setup 诚实文案。

## 修改说明

| 角色 | 动作 |
|------|------|
| 设计 / 发布 | 用现有 phone UI 源 + 新顶栏文案出成片 |
| 产品 | 上传前对照 D-512 表逐张过目 |
| 开发 | 通常无 App 代码改动 |

## 验收标准

- [ ] 三套尺寸（或实际上传套）顶栏与上表一致  
- [ ] 无 *annoyances blocked* 等已否决绝对句  
- [ ] 框内 Welcome CTA 仍为 `Set Up in Safari`  
- [ ] screenshot-plan Connect 清单「按新 Title/Subtitle 重生成顶栏」已勾  

## 附件

- 权威表：`docs/release/app-store-assets/screenshot-plan.md`  
- 相关 done：`issues/008-store-packaging-cta-domain/`（框内 + URL，不含本 issue）  
