# Issue 011：v1 移除 Strict Mode 与 Tap to Block（D-317）

| 字段 | 内容 |
|------|------|
| 状态 | **open** |
| 优先级 | **P0**（范围变更；与旧实现/旧稿冲突时必须改） |
| 类型 | product-scope / ui / copy |
| 影响范围 | 主 App Home / Upgrade / Welcome · Help · 扩展 popup · 商店卖点 · **营销站 / Support / Privacy** |
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
4. 商店/营销素材中的 Strict/Tap 字样不在本 issue 范围（见 docs/release/，非开发 issue）。  
5. **网站（对外）：** 营销首页 Pro 目录、`website/support`、`website/privacy` 与 ASC 镜像文案不得再卖 Strict / Tap；Home 成片截图仅 6 行。

## 验收标准

### 产品 / 文档（已完成）

- [x] 总纲领 + decision D-317  
- [x] design / ui-copy / issues 对齐  

### 设计稿 · Lunacy

- [x] Hi-fi Home 去掉 Strict / Tap 并 **重导出**（含 Dark / LT）  
- [x] Hi-fi Upgrade 仅 YT&X + Battery 并 **重导出**  
- [x] Welcome 卖点去掉 Strict/Tap 并重导  
- [ ] **用户须在 Lunacy 中保存** `Stillwall-HiFi-v1.free`（Ctrl+S）  
- [ ] Wireframes 扩展改为 2 项并导出 SE01*（006）  
- [x] 同步 issue after/ 与商店合成图（本轮已做）  

### 开发实现

- [ ] Home 仅 6 能力行，无 Strict / Tap  
- [ ] Upgrade 仅 YT&X + Battery  
- [ ] 扩展 popup 仅 Pause + Report  
- [ ] 工程字符串搜索无用户可见 `Strict Mode` / `Tap to Block`  
- [ ] Help 无 Tap 路径；恢复路径 = 关类别或 Pause  

**导出日志：** `docs/design/exports/lunacy-export-log-2026-07-31.md`（主路径已导，**仍含旧 Strict/Tap 像素**）  
- [x] **网站（2026-07-31）：** `website/index.html` Pro 仅 YT&X + Battery；Support/Privacy/support-en-US 去掉 Strict·Tap；站内 `03-Home` / `05-Upgrade` 截图已裁掉两行（`01-Welcome` 列表仍可能在 CTA 下透出旧行，lab 用，正式首页未引用）  

## 附件

- 总纲领：`docs/product/product-charter.md`（D-317 修订）  
- 决策：`docs/decisions/decision-log.md` D-317  
- 设计：`screens.md` S05 移除；`safari-extension.md` 2 项  
