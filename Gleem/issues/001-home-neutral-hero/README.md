# Issue 001：Home 顶部改为中性价值文案（去掉 On / Safari Protection 状态区）

| 字段 | 内容 |
|------|------|
| 状态 | open（**文案/目标已锁定**；待主 App 源码合入） |
| 优先级 | P0（与已确认产品决策 D-315 / D-316 冲突） |
| 类型 | ui / copy / behavior |
| 影响范围 | 主 App · Home |
| 相关文档 | `docs/product/product-charter.md` §7.3；`docs/design/screens.md` S03；`docs/decisions/decision-log.md` D-315、D-316 |
| 创建日期 | 2026-07-31 |

## 问题现象

实机 Home 顶部仍为「保护状态」叙事：

- 绿色 **On** pill  
- 大标题 **Safari Protection**  
- 副文案 **Active modules are blocking in Safari.**

这与 v1 已确认决策冲突：Home **不做** On/Off 状态区、**不做**保护状态 pill、**不**用状态驱动标题。

![当前 · 状态 pill + Safari Protection](before/home-status-pill.jpg)

![当前 · Ads 开启时同一状态区](before/home-ads-on.jpg)

## 期望结果

与设计稿 / 产品总纲领一致：

1. **移除**顶部状态 pill（On / Off 等）。  
2. 标题与副文案改为固定中性价值文案（**不**随类别开关变化）：

```text
A quieter Safari, on your terms.
Choose what stays out of your way.
```

3. 类别开关列表、PRO 行、More（`…`）保持现有能力与顺序，无需因本 issue 改业务逻辑。  
4. 全部类别 Off 时，**仍显示同一套**顶部文案与列表布局（仅拦截不生效；诚实状态由 Safari 扩展顶栏表达，不在此页做 On/Off 变体）。

设计参考：

![期望 · Hi-fi Home](after/home-design-target.png)

## 修改说明（给开发）

### UI

- 删除 Home header 中的 status pill / 保护状态组件及其绑定的 `isProtected` / `globalOn` 一类展示逻辑。  
- Value Hero 使用上述两行固定英文文案；排版对齐 `docs/design/design-system.md` §7.1（Value Hero）。  
- **不要**把「全局总开关」加回来（D-315）。  
- **不要**再维护 Home On / Home Off 两套页面或标题变体（D-316）。

### 文案

| 位置 | 使用 |
|------|------|
| 主标题 | `A quieter Safari, on your terms.` |
| 副文案 | `Choose what stays out of your way.` |
| 删除 | `Safari Protection`、`Active modules are blocking in Safari.`、状态 pill `On`/`Off` |

### 勿误改

- 类别行文案、PRO badge（**无** Tap 行 · D-317）  
- 右上角 More  
- 规则编译进度条（见 issue **002**）  
- Setup 门禁与扩展状态检测（丢失授权仍应模态拉回 Setup，但 **Home 成功页本身不展示保护 pill**）

### 深色模式 / 动态字体

- 中性文案需同时检查 Dark 与 Large Type（设计导出：`07-Home-Dark`、`11-Home-LargeType`）。
- Large Type：标题可折行，**行高随文字增高、列表可滚**，勿裁切；副文案可略缩短（见 issue **005** 文案锁定表），但**主标题句式不得改回状态叙事**。

### Hallmark 增补（2026-07-31 全局设计审计）

**设计理念对齐：** Hi-fi 已统一为「安静的 Settings 列表 + 中性价值文案」；实机 On pill 把产品重新拉回「监控台 / 安全中控」，与人格 *calm because it is working* 冲突。本 issue 是人格级修复，不只是换标题。

| 做 | 不做 |
|----|------|
| 对齐 `after/home-design-target.png` 的 Value Hero 留白与字阶 | 用仪表盘、盾牌大图、威胁计数填空白 |
| More 保持弱圆形 `…` 控件 | 把全局开关或 Pause 塞回顶栏 |
| 类别列表 r18 白卡、系统绿 Switch、暖金 PRO | Free 行再堆一排领先图标（密度留给 Welcome） |
| 列表下方留白可保留（克制） | 为填满屏幕加统计卡 / 环形图 |

**视觉细节（对齐 design-system §3 / §7.1）：**

- 水平 inset **16**；Large Title **34 Bold**；副文案 **17** + `textSecondary`（约 0.65 opacity）
- Hero 与列表卡之间保持呼吸感（稿面约一段舒适 gap，勿贴死）
- 右上 More ≥ **44×44**；Dark 下 hero 字为近白，卡为 elevated 深灰

跨页 Free/Pro 节奏与文案统一见 **005**。

## 验收标准

- [ ] Home 顶部无 On/Off（或其它保护状态）pill  
- [ ] 主副文案为固定中性句，切换任意类别开关后文案不变  
- [ ] 无「Safari Protection」作为 Home 主标题  
- [ ] 全部类别 Off 时页面结构与顶部文案不变  
- [ ] 与 `screens.md` S03 / charter §7.3 一致  
- [ ] Light / Dark / Large Type 顶栏均无状态 pill，且不裁切标题  
- [ ] 观感接近 Hi-fi：Settings 列表气质，非安全 dashboard  

## 附件

| 文件 | 说明 |
|------|------|
| `before/home-status-pill.jpg` | 实机：状态 pill + Safari Protection（Ads 关） |
| `before/home-ads-on.jpg` | 实机：Ads 开，状态区仍在 |
| `before/home-status-pill-hires.png` | 同源高分辨率截图 |
| `after/home-design-target.png` | Hi-fi 设计目标（phone-preview `03-Home`） |
