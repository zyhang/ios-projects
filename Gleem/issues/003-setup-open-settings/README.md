# Issue 003：Setup「Open Settings」深链失败体验 + 三步说明对齐文档

| 字段 | 内容 |
|------|------|
| 状态 | open |
| 优先级 | P1 |
| 类型 | behavior / copy / docs-sync |
| 影响范围 | 主 App · Setup（Safari 授权引导） |
| 相关文档 | `docs/design/screens.md` S02（已改为三步）；`docs/product/product-charter.md` §7.2 |
| 创建日期 | 2026-07-31 |

## 问题现象

Setup 页点击主按钮 **Open Settings** 后，出现橙色错误：

> Couldn't open Extensions. Go to Settings → Apps → Safari → Extensions.

深链到系统「扩展」页在部分 iOS 版本/环境下会失败，属常见平台限制。当前实现已给出手动路径，但：

1. 失败反馈偏「报错」感，首次启用压力大。  
2. 主按钮仍是 Open Settings，用户可能反复点、反复看到同一错误。  
3. 产品文档曾写「两步」，实现已是更清晰的 **三步**（Open Settings → 开启 6 个 Content Blockers + Web Extension → Allow website access），文档需与实现一致（文档侧已同步，见本仓库 `screens.md`）。

![当前 · 深链失败橙字](before/setup-open-settings-failed.jpg)

设计参考（成功态布局，非错误态）：

![参考 · Hi-fi Setup](after/setup-design-target.png)

## 期望结果

### 深链策略（最佳实践）

1. 点击 **Open Settings** 时：  
   - **优先**尝试打开最深可用 URL（Extensions / Safari 相关）。  
   - 失败则 fallback：`UIApplication.openSettingsURLString`（App 自身设置）或仅提示手动路径——**以能减少挫败为准**，不要空操作。  
2. 用户取消或系统无法打开时：  
   - **不要**用刺眼「错误红/永久失败」语气。  
   - 使用**指导性**文案（info / secondary），例如：

```text
If Settings didn’t open, go to:
Settings → Apps → Safari → Extensions
```

   或保留现有路径说明，但样式从「error」改为「hint」（次要灰/品牌色，非告警橙红，除非多次失败）。

3. 主按钮在首次失败后可保持 **Open Settings**（继续尝试），同时路径说明常驻可见，避免用户不知道下一步。  
4. 文案继续强调：**6 个 Content Blockers + Stillwall Web Extension** 全开，且 Web Extension **Allow All Websites**（与现有步骤 2/3 一致）。

### 三步结构（以现实现为准）

| # | 标题 | 要点 |
|---|------|------|
| 1 | Open Settings | Apps → Safari → Extensions |
| 2 | Turn on Stillwall | 全部 6 个 Content Blockers + Web Extension |
| 3 | Allow website access | Web Extension → Allow All Websites |

完成检测逻辑不变：未完成不得进 Home。

## 修改说明（给开发）

1. 梳理当前 open URL 列表与 iOS 版本兼容；失败时 fallback + 非 error 样式 hint。  
2. 区分：  
   - `user cancelled` / 无法打开 → hint  
   - 真异常（极少）→ 可短 toast，仍附手动路径  
3. 可选增强（P2，非必须）：检测权限已满足时自动 dismiss Setup / 进入 Home（若已有则保持）。  
4. 勿弱化「必须全开」的说明；误开不全会导致「以为开了但不拦」。

### 产品文档

- `docs/design/screens.md` S02 已改为三步结构（本 issue 配套）。  
- 实现与文档冲突时以 **三步 + 门禁** 为准。

## 验收标准

- [ ] 深链失败时用户仍能靠页面文案完成手动设置  
- [ ] 失败提示不表现为刺眼硬错误（或仅短暂出现后变为常驻 hint）  
- [ ] 三步说明完整：Settings、6 CB + Web Extension、Allow All Websites  
- [ ] 未完成授权不能进入 Home  
- [ ] 英文 UI  

## 附件

| 文件 | 说明 |
|------|------|
| `before/setup-open-settings-failed.jpg` | 实机：Open Settings 失败橙字 |
| `after/setup-design-target.png` | Hi-fi Setup 布局参考 |
