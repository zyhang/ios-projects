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

### Hallmark 增补 · 视觉规格（Hi-fi 无独立画板，按系统组件语言补齐）

进度反馈必须**像 Stillwall 的一部分**，不能像系统调试条或第三方 VPN 的「正在连接…」恐吓条。

| 项 | 规范 |
|----|------|
| 形态 | 底部 **胶囊 / 圆角条**（参考 Setup 的 `Private by design` 安心条气质，非全宽告警 banner） |
| 底色 | `brandSoft` / 浅分组面（Light `#EAF3EF` 系或 `surfaceElevated` + 细边）；**禁止**刺眼橙/红作进行中态 |
| 图标 | 小型 `progress` / 旋转 activity，线宽克制；品牌绿或 secondary，**非**警报 |
| 字 | 标题 15 SemiBold / 副文案 13 Regular · `textPrimary` + `textSecondary`；**仅英文默认** |
| 动效 | ≤300ms 淡入；Reduce Motion 时仅 opacity；成功后淡出，**不**庆祝弹窗 |
| 位置 | Home 底安全区上方；列表仍可滚动；不盖住 More |

文案优先用产品词 *filters / blockers*，避免「筛选器引擎 / 规则包编译」等工程话术（与 design-system §9 一致）。

### 勿误改

- 编译/下发规则的工程逻辑本身（除非已有明显 bug）  
- Home 顶部文案（见 **001**）

## 验收标准

- [ ] 进度条文案为英文（默认 en），不再出现「应用筛选器 / 正在为 Safari 准备筛选器」  
- [ ] 视觉属品牌软提示（绿灰安心条气质），非系统灰中文调试条、非告警色  
- [ ] 开关变更后仍有可理解的进度或完成后的稳定状态  
- [ ] 快速连点多开关不产生错误堆叠 UI  
- [ ] 失败路径有可读英文提示（若实现失败态）  
- [ ] Reduce Motion 下无刺眼循环大动画  

## 附件

| 文件 | 说明 |
|------|------|
| `before/filter-progress-chinese.jpg` | 实机中文进度条 |
