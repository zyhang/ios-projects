# Issue 009：Help / 恢复路径文案（禁止 Home On；指向扩展 Pause）

| 字段 | 内容 |
|------|------|
| 状态 | **open**（规格已锁 · **App Help 页仍待开发实现**） |
| 优先级 | **P1**（首次用户误杀时的可发现性；主路径 001–004 之后尽快） |
| 类型 | copy / ui / docs-sync |
| 影响范围 | 主 App · Help（S07）· 可选首次 Home 提示 · 与扩展入口说明 |
| 相关文档 | charter §5.9–5.10；screens S07；T-EXT-07；V-002；`docs/engineering/ui-copy-en.md` §7；`docs/design/secondary-screens.md` |
| 创建日期 | 2026-07-31 |
| 来源 | Journey polish review 2026-07-31 |
| 说明 | 2026-07-31 曾误标 done（仅规格完成）。**仅 issue open 才会触发开发**——已改回 open。 |

## 问题现象

产品正确地把「本站临时放行」放在 **Safari 扩展 · Pause on this site**（D-309），主 App **无** Allowed Sites。

但对**首次安装的普通人**：

1. Home 中性文案**不会**教他去扩展（符合 D-316，但发现性弱）。  
2. Help 在 screens 仅有条目建议，**无**锁定英文正文，实现易抄错 Support 旧句。  
3. 对外 Support 文案曾写「Home shows On」——App 内 Help **禁止**同源复制该错误。  
4. T-EXT-07 / V-002：打开扩展的系统路径未最终验证，**禁止**写死未验证图标位置。

结果：站点坏了 → 用户只会拨类别开关或卸载，而找不到 3 秒 Pause。

## 期望结果

### 1. Help 条目与正文（en 权威方向）

实现 Help 时至少包含（标题可微调）：

| 条目标题（建议） | 正文必须包含的语义 |
|------------------|-------------------|
| How to enable protection | 指向 Setup / `Set Up in Safari`；**6 CB + Web Extension** + Allow All Websites；**不要**写 Home 显示 On |
| Site broken? | **优先：** Safari → Stillwall extension → **Pause on this site**；备选：关闭相关类别开关；需要时 Resume（**不**提 Strict） |
| How to open the extension | 「In Safari, open the Stillwall extension」+ **以 App 内 Setup/系统说明为准**；路径细节依赖 V-002，未验证前用中性描述 |
| YouTube & X | **Safari websites only**，非原生 App |
| Send feedback | App Feedback 或扩展 **Report issue**（popup 第 2 项） |

**无** Tap to Block 帮助条（D-317）。

### 2. 禁止句（App 内任何 Help/空状态）

- Home protection **On** / **Off** badge 作为成功标准  
- `Set Up Safari Protection`（用 `Set Up in Safari`）  
- 含糊 *both extensions* 替代 6+1  
- 未验证的「点地址栏某个具体图标」死路径（除非 V-002 已确认）

### 3. 可选增强（intent-optional · 产品确认后再做）

首次 Setup 成功进入 Home 后，**一次性**非阻塞 tip（非状态 pill），例如：

```text
Tip: If a site looks wrong, open the Stillwall extension in Safari and choose Pause on this site.
```

- 不改变 D-316 Value Hero  
- 可关闭 / 仅显示一次  
- 文案需产品确认后写入 005 或本 issue

### 4. 与 006 的关系

| Issue | 分工 |
|-------|------|
| **006** | 次级页 / 扩展视觉与实现 |
| **009** | **App 内 Help** 文案与恢复路径（本 issue） |

## 修改说明（给开发）

1. 实现 S07 时使用上表语义；字符串进 Localizable，与 005 单一源策略一致。  
2. 自查：工程内搜索 `Safari Protection`、`protection On`、`both extensions`。  
3. **无** S05 Tap 说明页（D-317）。  
4. V-002 完成后：只更新「如何打开扩展」的路径句，不改 Pause 产品语义。

## 验收标准

### 规格（产品/设计 · 已完成）

- [x] 正文锁定于 `ui-copy-en.md` §7  
- [x] screens S07 / secondary-screens 已对齐  
- [x] secondary-preview 有 Help 列表 + Site broken 详情  

### 开发实现（**未完成 · 本 issue 关闭条件**）

- [ ] App 内存在 Help 列表页（S07），含上表全部条目  
- [ ] Site broken 详情（或等价展开）优先写扩展 **Pause on this site**  
- [ ] 全文搜索无 Home protection On、无 `Set Up Safari Protection`、无含糊 *both extensions*  
- [ ] 打开扩展说明不依赖未验证死路径  
- [ ] （可选 tip）产品确认后再做 — 非本 issue 关闭条件  

## 规格交付说明（2026-07-31）

- 权威正文：`docs/engineering/ui-copy-en.md` §7  
- 视觉临时稿：`docs/design/exports/secondary-preview/`  
- **关闭本 issue = App 内 Help 已实现并通过验收**，不是「文档写完」  

## 附件

- `docs/design/screens.md` S07  
- `docs/design/safari-extension.md` §5.1  
- `docs/design/journey-polish-review-2026-07-31.md` §2.4 / §2.6 / §2.7  
