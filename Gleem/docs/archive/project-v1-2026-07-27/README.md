# 归档：项目文档 v1（2026-07-27）

本目录保存 **Gleem / Stillwall 第一套完整产品研发文档体系** 的快照，已从 `docs/` 工作区整体迁出，便于**全应用重构**（产品、流程、设计、工程与运营文档一并重做）。

> **本目录不是现行权威。** 对照旧方案时请显式引用 `archive/project-v1-2026-07-27`。

## 为何整包归档

- 上一轮仅封存了流程与设计稿；现决定对整个应用与文档体系重构。
- 产品定义（PRD）、决策、范围、工程、规则、隐私、质量、发布、运营一并封存，避免重构时误把旧决策当作现行约束。
- 重构期间以 [`docs/`](../../) 为空白工作区，按需重建。

## 目录清单

| 路径 | 说明 |
|------|------|
| [docs-README.md](docs-README.md) | 归档前 `docs/README.md` 导航与术语表快照 |
| [product/](product/) | 产品定义、范围与商业模式（PRD） |
| [decisions/](decisions/) | 决策记录（D-001 起） |
| [design/](design/) | 设计原则、App 流程、用户流程、Lunacy 流程图与视觉探索 |
| [engineering/](engineering/) | 系统架构、iOS 客户端、后端与规则交付 |
| [rules/](rules/) | 拦截规则系统 |
| [privacy/](privacy/) | 隐私、安全与合规 |
| [quality/](quality/) | 测试与验收 |
| [release/](release/) | 两周 TestFlight 计划 |
| [operations/](operations/) | 支持与事故响应 |

### 设计子目录要点

| 文件 | 说明 |
|------|------|
| [design/design-system.md](design/design-system.md) | 设计原则与视觉规范 |
| [design/app-flow.md](design/app-flow.md) | App 完整流程逻辑事实源 |
| [design/user-flows.md](design/user-flows.md) | 信息架构与用户流程摘要 |
| [design/Gleem-App-Flows.free](design/Gleem-App-Flows.free) / [.pdf](design/Gleem-App-Flows.pdf) | Lunacy 流程图 |
| [design/Stillwall-Visual-Exploration.free](design/Stillwall-Visual-Exploration.free) | Stillwall 视觉探索 |
| [design/README-flows-and-visuals-interim.md](design/README-flows-and-visuals-interim.md) | 曾单独封存流程/视觉时的说明（历史） |

### 产品子目录要点

| 文件 | 说明 |
|------|------|
| [product/product-definition.md](product/product-definition.md) | 产品定义（目标用户、主张、成功标准） |
| [product/scope-and-business.md](product/scope-and-business.md) | 范围与商业模式 |

## 本轮方案摘要（仅供对照，非现行规范）

| 项 | v1 选择 |
|----|---------|
| 内部代号 / 对外名 | Gleem / Stillwall（对外名曾待商标核查） |
| 平台 | iPhone/iPad，最低 iOS/iPadOS 26 |
| 免费 | Safari Content Blocker + YouTube/X 专项 + 干扰项 |
| Pro | `NEURLFilterManager` 跨 App URL 过滤；`$19.99/年`，7 天试用 |
| 隐私 | 零数据收集、无账号、无第三方分析 |
| 状态语言 | `All Quiet` / `One Quick Step` / `Paused` |
| 近期里程碑 | 两周私有 TestFlight（不含真实收费与 URL Filter） |

## 预览归档流程图

```bash
open docs/archive/project-v1-2026-07-27/design/Gleem-App-Flows.pdf
```

## 引用规则

- **不要**在新 PRD / 决策 / 设计 / 工程文档中默认继承本目录结论。
- 若某条旧决策仍成立，应在新决策记录中**重新确认**并写明来源「见 archive/project-v1-2026-07-27」。
- 新文档体系写在 `docs/` 下，并更新 `docs/README.md` 导航。

## 相关历史

- 更早一轮仅视觉归档见 git `8d487b2`（原 `WiprCopy/docs/archive/design-v1-2026-07-25`）。
- 本快照包含归档当日工作区中对 `app-flow.md` / `user-flows.md` 的未提交修订。
