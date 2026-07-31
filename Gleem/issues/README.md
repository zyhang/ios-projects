# Issues

Stillwall（Gleem）**开发任务入口**。产品/设计优化必须落到本目录 issue，开发才按此改。

- **规则：** [AGENTS.md](./AGENTS.md)  
- **英文 UI 源：** [`docs/engineering/ui-copy-en.md`](../docs/engineering/ui-copy-en.md)  
- **产品范围真相：** [`docs/product/product-charter.md`](../docs/product/product-charter.md)  
- **原则：** 只写在 design/decision、**未** open issue 的项 = **不触发开发**

## 索引

| 序号 | 目录 | 标题 | 状态 | 优先级 | 谁做 |
|------|------|------|------|--------|------|
| 001 | [001-home-neutral-hero](./001-home-neutral-hero/) | Home 中性 Value Hero（去 On pill） | **open** | P0 | 开发 |
| 002 | [002-filter-progress-copy](./002-filter-progress-copy/) | 规则进度条英文 + 品牌软提示 | **open** | P1 | 开发 |
| 003 | [003-setup-open-settings](./003-setup-open-settings/) | Setup 深链 hint + 诚实三步 + D-511 清单 | **open** | P1 | 开发 |
| 004 | [004-pro-pricing-and-cancel-ux](./004-pro-pricing-and-cancel-ux/) | Pro $14.99 + 取消静默；**利益仅 YT&X+Battery** | **open** | P0/P1 | 开发 |
| 005 | [005-cross-screen-consistency](./005-cross-screen-consistency/) | 跨页文案 / ui-copy；**无 Strict/Tap** | **open** | P2 | 开发 |
| 006 | [006-secondary-and-extension-hifi](./006-secondary-and-extension-hifi/) | 次级页 + 扩展 **2 项** popup | **open** | P1 | 开发 |
| 007 | [007-support-trust-copy-d316](./007-support-trust-copy-d316/) | Support 信任文案 | **done** | P0 | 文档 |
| 008 | [008-store-packaging-cta-domain](./008-store-packaging-cta-domain/) | 商店框内 CTA + 域名 | **done** | P1 | 文档/素材 |
| 009 | [009-help-recovery-path-copy](./009-help-recovery-path-copy/) | App Help（**无 Tap**） | **open** | P1 | 开发 |
| 010 | [010-store-screenshot-titles-d512](./010-store-screenshot-titles-d512/) | 商店框外 Title/Subtitle | **open** | P1 | 设计/发布 |
| 011 | [011-remove-strict-and-tap-d317](./011-remove-strict-and-tap-d317/) | **v1 移除 Strict + Tap（D-317）** | **open** | **P0** | 开发 |

## 建议开发顺序

1. **011**（范围：从 UI/模型去掉 Strict/Tap）+ **001**、**004**  
2. **003**、**002**  
3. **005** 文案 catalog  
4. **009** Help、**006** 次级页 + 扩展 2 项  
5. **010** 上架截图顶栏  

**无需开发：** 007、008  

## v1 能力（D-317 后 · 给开发速查）

| 层 | 内容 |
|----|------|
| Home 免费 | Ads · Privacy · Annoyances · Regional |
| Home Pro | YouTube & X · Battery Boost |
| **不做** | Strict Mode · Tap to Block · 全局总开关 · Allowed Sites |
| 扩展 popup | **Pause/Resume** · **Report issue**（仅 2 项） |

## 已锁定文案（摘录）

| 项 | 权威 |
|----|------|
| Welcome CTA | `Set Up in Safari`（D-510） |
| Setup | 6 CB + Web Extension + D-511 清单 |
| Pro 利益 | 仅 YT&X + Battery（D-317） |
| 完整表 | [ui-copy-en.md](../docs/engineering/ui-copy-en.md) |

## 设计审计日志

| 日期 | 说明 |
|------|------|
| 2026-07-31 | Journey polish；001–010 |
| 2026-07-31 | **D-317** 砍 Strict/Tap；总纲领 + 设计 + **011** |

新建 issue 后请更新本表。
