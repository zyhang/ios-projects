# 归档：设计与流程 v2（2026-07-27）

本目录保存 **Gleem / Stillwall 第二轮流程文档与设计稿**，已从 `docs/design/` 迁出，便于流程与视觉重构。

## 为何归档

- 产品定义、范围、工程、规则、隐私等活文档保持不变。
- 当前 App 完整流程、用户流程摘要、Lunacy 流程图与视觉探索稿整体封存，**不再作为当前流程 / 设计权威源**。
- 重构期间以 [`docs/design/`](../../design/) 为工作区；品牌原则见仍存活的 [`design-system.md`](../../design/design-system.md)。

## 内容清单

| 文件 | 说明 |
|------|------|
| [app-flow.md](app-flow.md) | App 完整流程逻辑事实源（含阶段 A/B/C、泳道、门禁与恢复） |
| [user-flows.md](user-flows.md) | 信息架构与用户流程页面级摘要 |
| [Gleem-App-Flows.free](Gleem-App-Flows.free) | Lunacy 可编辑流程图源文件 |
| [Gleem-App-Flows.pdf](Gleem-App-Flows.pdf) | 流程图 PDF 快速预览 |
| [Stillwall-Visual-Exploration.free](Stillwall-Visual-Exploration.free) | Stillwall 视觉探索 Lunacy 源文件 |

## 本轮要点摘要（仅供对照，非现行规范）

| 项 | v2 选择 |
|----|---------|
| 流程权威 | `app-flow.md`；Lunacy/PDF 须与其对齐 |
| 导航 | 无底部 Tab；Overview → 二级页（NavigationStack） |
| 门禁 | Safari Protection 授权完成前不得进 Home |
| 状态语言 | `All Quiet` / `One Quick Step` / `Paused` |
| 阶段 | A TestFlight · B Pro 技术验证 · C 正式商业版 |
| 视觉探索 | Stillwall 品牌视觉探索稿（与流程稿分文件） |

## 预览归档 PDF

```bash
open docs/archive/design-v2-2026-07-27/Gleem-App-Flows.pdf
```

Lunacy 源文件在本机用 Lunacy 打开对应 `.free` 即可。

## 未迁入本目录（仍为活文档）

| 路径 | 原因 |
|------|------|
| `docs/design/design-system.md` | 设计原则与视觉规范，重构时仍可作约束基线 |
| `docs/product/*` | 产品定义与范围 |
| `docs/decisions/*` | 已确认决策 |
| 工程 / 规则 / 隐私 / 质量 / 发布 / 运营 | 非本轮流程与设计稿范围 |

## 引用规则

- **不要**在新流程或设计文档里把本目录当作默认权威。
- 需要对照旧方案时，显式写「见 `archive/design-v2-2026-07-27`」。
- 重构产出写在 `docs/design/`，并在该目录 README 与 `docs/README.md` 中更新索引。
