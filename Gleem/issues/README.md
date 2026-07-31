# Issues

Stillwall（Gleem）App **开发完成后的页面 / 功能问题** 与修改说明。

- **规则（Agent 与协作者必读）：** [AGENTS.md](./AGENTS.md)
- **组织方式：** `NNN-short-slug/` 子文件夹，一 issue 一目录，序号递增
- **读者：** 主要给开发人员——现象、期望、怎么改、截图与验收
- **英文 UI 源：** [`docs/engineering/ui-copy-en.md`](../docs/engineering/ui-copy-en.md)

## 索引

| 序号 | 目录 | 标题 | 状态 | 优先级 |
|------|------|------|------|--------|
| 001 | [001-home-neutral-hero](./001-home-neutral-hero/) | Home 去掉 On/Safari Protection 状态区，改为中性价值文案 | open · 规格就绪 | P0 |
| 002 | [002-filter-progress-copy](./002-filter-progress-copy/) | 规则编译进度条：英文 + 品牌软提示视觉 | open · 规格就绪 | P1 |
| 003 | [003-setup-open-settings](./003-setup-open-settings/) | Setup 深链失败体验 + 三步诚实文案 + 去误导金勾 | open · 规格/设计目标就绪 | P1 |
| 004 | [004-pro-pricing-and-cancel-ux](./004-pro-pricing-and-cancel-ux/) | Pro 定价 $14.99 + 取消购买静默 + 付费墙调性 | open · 规格就绪 | P0/P1 |
| 005 | [005-cross-screen-consistency](./005-cross-screen-consistency/) | 跨页文案锁定与视觉一致性（**D-510 已确认**） | open · 资产已刷 | P2 |
| 006 | [006-secondary-and-extension-hifi](./006-secondary-and-extension-hifi/) | 次级页与 Safari 扩展 Hi-fi 债 | **partial** · HTML 预览 | P2 |
| 007 | [007-support-trust-copy-d316](./007-support-trust-copy-d316/) | Support 废除「Home = On」/ both extensions / 旧 CTA | **done** | P0 |
| 008 | [008-store-packaging-cta-domain](./008-store-packaging-cta-domain/) | 商店截图 CTA + 域名占位 → yilinglabs.com | **done** | P1 |
| 009 | [009-help-recovery-path-copy](./009-help-recovery-path-copy/) | App Help 恢复路径文案（扩展 Pause；禁 Home On） | **done** · 规格 | P1 |

## 建议开发顺序

1. **主工程合入后：** **001**、**004**（与已确认产品决策直接冲突）  
2. **002**、**003**（体验与文案一致性）  
3. **005**（跨页 string catalog）  
4. **009** 的 SwiftUI Help 页（文案已锁）  
5. **006** Lunacy 正式 Hi-fi（HTML 预览可先开发）  

**文档/上架侧已完成：** 007、008（Support + 商店 URL/截图）。

> **说明（2026-07-31）：** 本 monorepo `Gleem/` 当前**无** Swift/Xcode 源码。001–005 的实现动作需在主 App 工程中落地；仓库已提供 `ui-copy-en.md` + 更新后的 Hi-fi/商店像素目标。

## 已锁定文案（D-510 · 2026-07-31）

| 项 | 权威 |
|----|------|
| Welcome CTA | `Set Up in Safari` |
| Strict（含 Large Type） | `Stronger blocking · Use with care` |
| Setup 能力描述 | 6 Content Blockers + Web Extension（勿 both extensions） |
| 完整副文案表 | [005](./005-cross-screen-consistency/) · [ui-copy-en.md](../docs/engineering/ui-copy-en.md) |

## 设计审计

| 日期 | 说明 |
|------|------|
| 2026-07-31 | Hallmark 全局 review：Hi-fi 主路径人格统一；实现漂移见 001–004；跨页与债项见 005–006 |
| 2026-07-31 | **Journey polish**：[`docs/design/journey-polish-review-2026-07-31.md`](../docs/design/journey-polish-review-2026-07-31.md)；007–009 创建并执行文档/商店侧 |
| 2026-07-31 | **设计续作**：D-511 Setup 名称清单、D-512 商店截图叙事、secondary-screens + secondary-preview 完整包 |

新建 issue 后请更新本表。
