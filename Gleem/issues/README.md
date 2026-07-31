# Issues

Stillwall（Gleem）**App / 扩展开发任务入口**。产品/设计优化必须落到本目录 issue，开发才按此改。

- **规则：** [AGENTS.md](./AGENTS.md)  
- **英文 UI 源：** [`docs/engineering/ui-copy-en.md`](../docs/engineering/ui-copy-en.md)  
- **产品范围真相：** [`docs/product/product-charter.md`](../docs/product/product-charter.md)  
- **范围：** 仅 **主 App + Safari 扩展** 实现债。网站 / App Store 资料 **不** 放本目录（见 `docs/release/`、`website/`）。

## 索引

| 序号 | 目录 | 标题 | 状态 | 优先级 |
|------|------|------|------|--------|
| 001 | [001-home-neutral-hero](./001-home-neutral-hero/) | Home 中性 Value Hero（去 On pill） | **open** | P0 |
| 002 | [002-filter-progress-copy](./002-filter-progress-copy/) | 规则进度条英文 + 品牌软提示 | **open** | P1 |
| 003 | [003-setup-open-settings](./003-setup-open-settings/) | Setup 深链 hint + 诚实三步 + D-511 清单 | **open** | P1 |
| 004 | [004-pro-pricing-and-cancel-ux](./004-pro-pricing-and-cancel-ux/) | Pro $14.99 + 取消静默；利益仅 YT&X+Battery | **open** | P0/P1 |
| 005 | [005-cross-screen-consistency](./005-cross-screen-consistency/) | 跨页文案 / ui-copy；无 Strict/Tap | **open** | P2 |
| 006 | [006-secondary-and-extension-hifi](./006-secondary-and-extension-hifi/) | 次级页 + 扩展 **2 项** popup | **open** | P1 |
| 009 | [009-help-recovery-path-copy](./009-help-recovery-path-copy/) | App Help（无 Tap） | **open** | P1 |
| 011 | [011-remove-strict-and-tap-d317](./011-remove-strict-and-tap-d317/) | v1 移除 Strict + Tap（D-317） | **open** | **P0** |

## 建议开发顺序

1. **011** + **001**、**004**  
2. **003**、**002**  
3. **005** 文案 catalog  
4. **009** Help、**006** 次级页 + 扩展  

## v1 能力（D-317 后 · 速查）

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

## 修订

| 日期 | 说明 |
|------|------|
| 2026-07-31 | 建立 001–011（含 journey polish / D-317） |
| 2026-07-31 | **删除** 007 / 008 / 010（网站 Support、App Store 包装与截图 — 非 App/扩展开发 issue） |

新建 issue 后请更新本表。
