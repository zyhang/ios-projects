# Issue 011：v1 移除 Strict Mode 与 Tap to Block（D-317）

| 字段 | 内容 |
|------|------|
| 状态 | **open** |
| 优先级 | **P0**（范围变更；与旧实现/旧稿冲突时必须改） |
| 类型 | product-scope / ui / copy |
| 影响范围 | 主 App Home / Upgrade / Welcome · Help · 扩展 popup · 商店卖点 |
| 相关文档 | 总纲领 D-317；`product-charter` §2.2 / §4.2 / §5.7 / §7.3 / §9 / §14 |
| 创建日期 | 2026-07-31 |
| 来源 | 产品确认 v1 砍掉 Strict + Tap（路径 B） |

## 问题现象

历史规格与部分 issue/设计资产仍描述：

- Home 第 7 行 Strict Mode、第 8 行 Tap to Block  
- Upgrade 四利益（含 Strict / Tap）  
- 扩展 popup 第 2 项 Tap to Block（共 3 项）  
- S05 Tap 说明页  

**产品决策 D-317：** 上述 **v1 全部不做**。

## 期望结果

### 主 App

| 面 | 要求 |
|----|------|
| Home 能力列表 | **仅 6 行**：Ads → Privacy → Annoyances → Regional → YouTube & X → Battery Boost |
| | **无** Strict 行、**无** Tap 入口行 |
| Upgrade | 利益 **仅** YouTube & X in Safari、Battery Boost |
| Welcome 卖点 | **无** Strict / Tap 条目 |
| Help | **无** Tap 专题；Site broken **不**提 Strict |
| S05 | **不实现** |

### Safari 扩展

| 面 | 要求 |
|----|------|
| popup 常态 | **仅 2 项**：① Pause/Resume on this site · ② Report issue |
| | **无** Tap to Block 槽 |
| SE02 页内点选 | **不实现** |

### 文案源

以 `docs/engineering/ui-copy-en.md`（D-317 后）与总纲领为准。

## 修改说明（给开发）

1. 删除/隐藏任何 Strict、Tap 的 model 字段、开关 UI、导航。  
2. 扩展菜单改 2 项；同步 App Group 若曾为 Tap 预留可保留字段但不暴露 UI。  
3. 与 **005** 文案表、**006** 次级/扩展、**009** Help 一并验收。  
4. 商店/截图若仍写 Tap 或 Strict → 见 **010** / 描述文案（文档侧已改 description）。

## 验收标准

- [ ] Home 仅 6 能力行，无 Strict / Tap  
- [ ] Upgrade 仅 YT&X + Battery  
- [ ] 扩展 popup 仅 Pause + Report  
- [ ] 工程字符串搜索无用户可见 `Strict Mode` / `Tap to Block`（About/历史注释除外）  
- [ ] Help 无 Tap 路径；恢复路径 = 关类别或 Pause  

## 附件

- 总纲领：`docs/product/product-charter.md`（D-317 修订）  
- 决策：`docs/decisions/decision-log.md` D-317  
- 设计：`screens.md` S05 移除；`safari-extension.md` 2 项  
