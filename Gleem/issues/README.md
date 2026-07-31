# Issues

Stillwall（Gleem）App **开发完成后的页面 / 功能问题** 与修改说明。

- **规则（Agent 与协作者必读）：** [AGENTS.md](./AGENTS.md)
- **组织方式：** `NNN-short-slug/` 子文件夹，一 issue 一目录，序号递增
- **读者：** 主要给开发人员——现象、期望、怎么改、截图与验收

## 索引

| 序号 | 目录 | 标题 | 状态 | 优先级 |
|------|------|------|------|--------|
| 001 | [001-home-neutral-hero](./001-home-neutral-hero/) | Home 去掉 On/Safari Protection 状态区，改为中性价值文案 | open | P0 |
| 002 | [002-filter-progress-copy](./002-filter-progress-copy/) | 规则编译进度条：英文 + 品牌软提示视觉 | open | P1 |
| 003 | [003-setup-open-settings](./003-setup-open-settings/) | Setup 深链失败体验 + 三步诚实文案 + 去误导金勾 | open | P1 |
| 004 | [004-pro-pricing-and-cancel-ux](./004-pro-pricing-and-cancel-ux/) | Pro 定价 $14.99 + 取消购买静默 + 付费墙调性 | open | P0/P1 |
| 005 | [005-cross-screen-consistency](./005-cross-screen-consistency/) | 跨页文案锁定与视觉一致性（**D-510 已确认**） | open | P2 |
| 006 | [006-secondary-and-extension-hifi](./006-secondary-and-extension-hifi/) | 次级页与 Safari 扩展 Hi-fi 债 | open | P2 |

## 建议开发顺序

1. **001**、**004**（与已确认产品决策直接冲突）  
2. **002**、**003**（体验与文案一致性）  
3. **005**（跨页文案源；可与上两项并行）  
4. **006**（设计补画板；开发先跟文字规格）

## 已锁定文案（D-510 · 2026-07-31）

| 项 | 权威 |
|----|------|
| Welcome CTA | `Set Up in Safari` |
| Strict（含 Large Type） | `Stronger blocking · Use with care` |
| Setup 能力描述 | 6 Content Blockers + Web Extension（勿 both extensions） |
| 完整副文案表 | [005](./005-cross-screen-consistency/) |

## 设计审计

2026-07-31 Hallmark 全局 review：Hi-fi 主路径人格统一；实现漂移见 001–004；跨页与债项见 005–006。

新建 issue 后请更新本表。
