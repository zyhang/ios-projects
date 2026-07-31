# Issue 009：Help / 恢复路径文案（禁止 Home On；指向扩展 Pause）

| 字段 | 内容 |
|------|------|
| 状态 | open |
| 优先级 | **P1**（首次用户误杀时的可发现性；主路径 001–004 之后尽快） |
| 类型 | copy / ui / docs-sync |
| 影响范围 | 主 App · Help（S07）· 可选首次 Home 提示 · 与扩展入口说明 |
| 相关文档 | charter §5.9–5.10；screens S07；T-EXT-07；V-002；`docs/design/journey-polish-review-2026-07-31.md` |
| 创建日期 | 2026-07-31 |
| 来源 | Journey polish review 2026-07-31 |

## 问题现象

产品正确地把「本站临时放行」放在 **Safari 扩展 · Pause on this site**（D-309），主 App **无** Allowed Sites。

但对**首次安装的普通人**：

1. Home 中性文案**不会**教他去扩展（符合 D-316，但发现性弱）。  
2. Help 在 screens 仅有条目建议，**无**锁定英文正文，实现易抄错 Support 旧句。  
3. Support 曾写「Home shows On」（见 **007**）——若 Help 同源复制会再次污染 App。  
4. T-EXT-07 / V-002：打开扩展的系统路径未最终验证，**禁止**写死未验证图标位置。

结果：站点坏了 → 用户只会拨类别开关或卸载，而找不到 3 秒 Pause。

## 期望结果

### 1. Help 条目与正文（en 权威方向）

实现 Help 时至少包含（标题可微调）：

| 条目标题（建议） | 正文必须包含的语义 |
|------------------|-------------------|
| How to enable protection | 指向 Setup / `Set Up in Safari`；**6 CB + Web Extension** + Allow All Websites；**不要**写 Home 显示 On |
| Site broken? | **优先：** Safari → Stillwall extension → **Pause on this site**；备选：关闭相关类别或 Strict；需要时 Resume |
| How to open the extension | 「In Safari, open the Stillwall extension」+ **以 App 内 Setup/系统说明为准**；路径细节依赖 V-002，未验证前用中性描述 |
| YouTube & X | **Safari websites only**，非原生 App |
| Tap to Block | Pro；扩展第 2 项；规则本机 |
| Send feedback | App Feedback 或扩展 **Report issue** |

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

### 4. 与 006 / 007 的关系

| Issue | 分工 |
|-------|------|
| **006** | Help / 扩展 **视觉** Hi-fi |
| **007** | **对外 Support** 信任口径 |
| **009** | **App 内 Help** 文案与恢复路径（本 issue） |

## 修改说明（给开发）

1. 实现 S07 时使用上表语义；字符串进 Localizable，与 005 单一源策略一致。  
2. 自查：工程内搜索 `Safari Protection`、`protection On`、`both extensions`。  
3. Tap 说明页（S05）已有「Pause in extension」一句要求（screens）——实现时勿删。  
4. V-002 完成后：只更新「如何打开扩展」的路径句，不改 Pause 产品语义。

## 验收标准

- [ ] Help 含 Site broken → 扩展 Pause（及类别备选）  
- [ ] 全文无「Home shows On」类成功标准  
- [ ] CTA / 扩展数量表述与 D-510 一致  
- [ ] 打开扩展说明不依赖未验证死路径  
- [ ] （若做可选 tip）不恢复状态 pill，且仅一次  

## 附件

- `docs/design/screens.md` S07  
- `docs/design/safari-extension.md` §5.1  
- `docs/design/journey-polish-review-2026-07-31.md` §2.4 / §2.6 / §2.7  
