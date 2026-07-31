# Issue 002：规则编译进度条改为英文产品文案（非中文系统串）

| 字段 | 内容 |
|------|------|
| 状态 | open |
| 优先级 | P1 |
| 类型 | copy / ui |
| 影响范围 | 主 App · Home（类别开关变更后的进度反馈） |
| 相关文档 | `docs/product/product-charter.md` §3（UI 英文优先）；`docs/design/screens.md`（界面文案：英文） |
| 创建日期 | 2026-07-31 |

## 问题现象

切换类别开关后，Home 底部出现进度条，文案为中文：

- **应用筛选器**  
- **正在为 Safari 准备筛选器…**

产品 v1 主界面约定为 **英文**；中文串像系统/调试默认文案，与页面其余英文不一致。

![当前 · 中文进度条](before/filter-progress-chinese.jpg)

## 期望结果

1. 保留「开关变更后需要重新编译 / 下发 Content Blocker 规则」时的**非阻塞进度反馈**（好实践，勿静默卡死）。  
2. 文案全部改为英文，语气简洁、非技术：  
   - 标题：`Updating filters`  
   - 副文案：`Preparing blockers for Safari…`  
3. 成功后自动消失；失败时用简短英文错误（可重试），**不要**露出内部 API 名。  
4. 若 App 已做或将做本地化：此串走 **Localizable**，`en` 为源语言；当前截图中的硬编码中文应去掉。v1 商店/主 UI 仍以英文为准。

## 修改说明（给开发）

### 文案（en 默认）

| Key 建议 | 文案 |
|----------|------|
| `filter_progress.title` | `Updating filters` |
| `filter_progress.subtitle` | `Preparing blockers for Safari…` |
| `filter_progress.failed`（若有） | `Couldn’t update filters. Try again.` |

### UX

- 底部条 / toast 不遮挡主列表关键开关（可点穿透或置于安全区上方）。  
- 连续快速拨动多个开关：合并为一次编译，进度条不闪烁重启（debounce / coalesce）。  
- 时长极短（<300ms）可考虑不展示，避免闪一下；超过则显示。

### 勿误改

- 编译/下发规则的工程逻辑本身（除非已有明显 bug）  
- Home 顶部文案（见 **001**）

## 验收标准

- [ ] 进度条文案为英文（默认 en），不再出现「应用筛选器 / 正在为 Safari 准备筛选器」  
- [ ] 开关变更后仍有可理解的进度或完成后的稳定状态  
- [ ] 快速连点多开关不产生错误堆叠 UI  
- [ ] 失败路径有可读英文提示（若实现失败态）  

## 附件

| 文件 | 说明 |
|------|------|
| `before/filter-progress-chinese.jpg` | 实机中文进度条 |
