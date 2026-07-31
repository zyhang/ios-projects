# Issues

Stillwall（Gleem）**开发任务入口**。产品/设计优化必须落到本目录 issue，开发才按此改。

- **规则：** [AGENTS.md](./AGENTS.md)  
- **英文 UI 源：** [`docs/engineering/ui-copy-en.md`](../docs/engineering/ui-copy-en.md)  
- **原则：** 只写在 design/decision 文档、**未** open issue 的项 = **不触发开发**

## 索引

| 序号 | 目录 | 标题 | 状态 | 优先级 | 谁做 |
|------|------|------|------|--------|------|
| 001 | [001-home-neutral-hero](./001-home-neutral-hero/) | Home 中性 Value Hero（去 On pill） | **open** | P0 | 开发 |
| 002 | [002-filter-progress-copy](./002-filter-progress-copy/) | 规则进度条英文 + 品牌软提示 | **open** | P1 | 开发 |
| 003 | [003-setup-open-settings](./003-setup-open-settings/) | Setup 深链 hint + 诚实三步 + **D-511 名称清单** | **open** | P1 | 开发 |
| 004 | [004-pro-pricing-and-cancel-ux](./004-pro-pricing-and-cancel-ux/) | Pro $14.99 + 取消购买静默 | **open** | P0/P1 | 开发 |
| 005 | [005-cross-screen-consistency](./005-cross-screen-consistency/) | 跨页文案 / `ui-copy-en` 单一源 | **open** | P2 | 开发 |
| 006 | [006-secondary-and-extension-hifi](./006-secondary-and-extension-hifi/) | **次级页 + 扩展 UI 实现**（More/Tap/Feedback/About/SE） | **open** | P1 | 开发（Lunacy 可选） |
| 007 | [007-support-trust-copy-d316](./007-support-trust-copy-d316/) | Support 信任文案（禁 Home=On） | **done** | P0 | 文档已完成 |
| 008 | [008-store-packaging-cta-domain](./008-store-packaging-cta-domain/) | 商店框内 CTA + 域名 URL | **done** | P1 | 素材/文档已完成 |
| 009 | [009-help-recovery-path-copy](./009-help-recovery-path-copy/) | **App Help 实现**（Pause 路径；禁 Home On） | **open** | P1 | 开发（规格已锁） |
| 010 | [010-store-screenshot-titles-d512](./010-store-screenshot-titles-d512/) | 商店截图**框外** Title/Subtitle（D-512） | **open** | P1 | 设计/发布 |

## 建议开发顺序

1. **001**、**004**（与决策直接冲突）  
2. **003**（含 D-511 清单）、**002**  
3. **005**（string catalog）  
4. **009** Help、**006** 次级页 + 扩展  
5. **010** 上架前重出截图顶栏  

**无需开发：** 007、008（已 done）。

## 优化 → Issue 覆盖表（审计 2026-07-31）

| 优化 / 决策 | 应触发谁 | Issue | 此前缺口 | 现状态 |
|-------------|----------|-------|----------|--------|
| Home 中性 hero / 去状态 pill | 开发 | **001** | — | open ✓ |
| 进度条英文 | 开发 | **002** | — | open ✓ |
| Setup 深链 + 诚实 6+1 + **名称清单 D-511** | 开发 | **003** | 清单仅一句带过 | **已写入修改说明+验收** ✓ |
| $14.99 / 取消静默 | 开发 | **004** | — | open ✓ |
| 跨页文案 + ui-copy 单一源 | 开发 | **005** | ui-copy 未钉进验收 | **已钉入** ✓ |
| Welcome CTA D-510 | 开发 | **005**（+001 联验） | — | open ✓ |
| More / Tap / Feedback / About / 扩展 UI | 开发 | **006** | 像「仅 Hi-fi 设计债」 | **改为 open 开发任务** ✓ |
| Support 对外文案 | 文档 | **007** | — | done ✓ |
| 商店框内 CTA + yilinglabs URL | 发布 | **008** | — | done ✓ |
| Help 恢复路径 **App 页** | 开发 | **009** | 误标 done | **改回 open** ✓ |
| 商店框外叙事 D-512 | 设计/发布 | **010** | 只在 screenshot-plan | **新建 010** ✓ |
| 可选首次 Home tip | — | 009 可选 | 未产品确认 | 不强制 ✓ |
| Lunacy 正式次级画板 | 设计 | 006 可选验收 | — | 不阻塞开发 ✓ |

## 已锁定文案（摘录）

| 项 | 权威 |
|----|------|
| Welcome CTA | `Set Up in Safari`（D-510） |
| Strict | `Stronger blocking · Use with care` |
| Setup | 6 CB + Web Extension + **D-511 名称清单** |
| 完整表 | [005](./005-cross-screen-consistency/) · [ui-copy-en.md](../docs/engineering/ui-copy-en.md) |

## 设计审计日志

| 日期 | 说明 |
|------|------|
| 2026-07-31 | Hallmark + Journey polish；001–009 |
| 2026-07-31 | D-511 / D-512 / secondary 规格 |
| 2026-07-31 | **覆盖审计**：009 重开、003/005/006 补强、新建 **010** |

新建 issue 后请更新本表与覆盖表。
