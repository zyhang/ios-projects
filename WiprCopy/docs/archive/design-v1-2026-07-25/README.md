# 归档：设计 v1（2026-07-25）

本目录保存 **Gleem 第一轮视觉 / 高保真 UI**，已从 `docs/design/` 迁出，便于全新视觉与 UI 重设计。

## 为何归档

- 产品决策（PRD、名单、商业、IA）保留为活文档。
- 第一轮视觉语言（暖纸画布、沉静绿 accent、hi-fi HTML、Welcome 视觉方案）整体封存，**不再作为当前设计权威源**。
- 重设计期间以空的 [`docs/design/`](../../design/) 为工作区。

## 内容清单

| 文件 | 说明 |
|------|------|
| [hi-fi.html](hi-fi.html) | 高保真界面集（Welcome、Home、Unlock、Enable、More 等） |
| [tokens.md](tokens.md) | v1 design tokens（暖纸 `#F4F2EE`、沉静绿 `#2C6E5A` 等） |
| [welcome.md](welcome.md) | Welcome 3 页视觉优先方案与文案 |
| [README.design.md](README.design.md) | 当时 `docs/design/README.md` 快照 |

## 视觉方向摘要（仅供对照，非现行规范）

| 项 | v1 选择 |
|----|---------|
| 画布 | 暖纸色 `#F4F2EE` |
| 主色 | 沉静绿 `#2C6E5A` |
| 导航 | 无 Tab；Home + More |
| 密度 | 大留白；健康 Home 几乎无按钮 |
| Welcome | 3 页：噪音 → Safari & Apps → on-device |

## 预览归档 hi-fi

```bash
open docs/archive/design-v1-2026-07-25/hi-fi.html
```

## 未迁入本目录（仍为活文档）

| 路径 | 原因 |
|------|------|
| `docs/product/*`、`docs/product/prd.md` | 产品决策与范围 |
| `docs/wireframes/*` | 信息架构与流程骨架（可随 UI 重设计迭代，但非本轮视觉封存） |
| `AGENTS.md` | 硬性规则 |

## 引用规则

- **不要**在新设计文档里把本目录当作默认 tokens / Welcome 权威。
- 需要对照旧方案时，显式写「见 archive/design-v1-2026-07-25」。
- 新视觉落地后写在 `docs/design/`，并在该目录 README 中更新索引。
