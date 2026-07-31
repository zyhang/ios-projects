# Issue 007：Support 信任文案对齐 D-316 / D-510（废除「Home = On」）

| 字段 | 内容 |
|------|------|
| 状态 | **done**（2026-07-31 已改 support md / website / site 包） |
| 优先级 | **P0**（对外教错成功标准；与已确认产品决策冲突） |
| 类型 | copy / docs-sync |
| 影响范围 | Support 页 · App Store Support URL 正文 · 站内 support HTML |
| 相关文档 | `docs/product/product-charter.md` §5.9 / §7.3；D-316、D-510；`docs/design/journey-polish-review-2026-07-31.md` |
| 创建日期 | 2026-07-31 |
| 来源 | Journey polish review 2026-07-31 |

## 问题现象

对外 Support 文案（至少以下三处同源错误）把 **已废弃的 Home 保护状态** 写成成功判据，并沿用弃用 Setup CTA / 「两个扩展」表述：

| 错误现状 | 冲突 |
|----------|------|
| Follow **Set Up Safari Protection** | D-510：权威 CTA = **Set Up in Safari** |
| enable **both** Stillwall extensions | 真实形态：**6 Content Blockers + 1 Web Extension** |
| Return to Stillwall — Home should show protection **On** | **D-316**：Home **无** On/Off 状态区；中性价值文案 |
| If Home does not show On… | 强化错误心智，与 001 修复目标相反 |

**涉及文件（须一并改）：**

- `docs/release/app-store-assets/copy/support-en-US.md`
- `website/support/index.html`
- `docs/release/app-store-assets/site/support.html`（若仍作 ASC 镜像）

站点异常 / Report / YouTube Safari only / 定价等段落**方向正确**，本 issue 不推翻，只修正「启用成功」叙事。

## 期望结果

### Enable protection（替换整段逻辑）

英文权威方向（可微调措辞，**语义不得回退**）：

```text
1. Open Stillwall.
2. Tap Set Up in Safari (or complete Setup if the app asks you to).
3. In Settings, turn on all Stillwall Content Blockers and the Stillwall Web Extension,
   then allow website access (Allow All Websites) as shown in the app.
4. Return to Stillwall. When setup is complete, you should reach Home with category
   controls (Ads, Privacy, and more). Home does not show an On/Off protection badge—
   your choices are the category switches. If setup is incomplete, Stillwall will ask
   you to finish enabling Safari access.
```

要点：

- **禁止**任何「Home shows On / Off / protected badge」成功标准  
- **禁止** *both extensions* 作为唯一描述；须体现 **多个 Content Blockers + Web Extension**  
- CTA 字符串与 App 一致：`Set Up in Safari`  
- 诚实：未完成系统授权时 App 会门禁 / 引导，而不是「Home 显示 On」

### Site broken 段（保持并略钉死）

已有「关类别 **或** 扩展 Pause」正确；确保不出现「先看 Home 是否 On」。

### 与 001 的关系

001 修 App Home UI；**007 修对外文档**。若只修 001 不修 007，用户仍会被 Support 教去找不存在的 On 状态。

## 修改说明（给开发 / 文案）

1. 按上表改三份 Support 源，保持段落结构与站内样式。  
2. 全文搜索 Support 相关：`protection On`、`Set Up Safari Protection`、`both` extensions。  
3. 若 App 内 Help 已实现且复制了旧 Support 句，同步改（完整 Help 规格见 **009**）。  
4. **不要**为了「好懂」把 Home 状态 pill 加回产品。

## 验收标准

- [x] `support-en-US.md` / `website/support` / site 包均无 Home **On** 成功判据  
- [x] 无弃用 CTA `Set Up Safari Protection`（或明确标注为历史）  
- [x] 启用步骤体现 Content Blockers（多）+ Web Extension + 网站访问  
- [x] Site broken 仍指向类别开关或扩展 **Pause on this site**  
- [x] 与 D-316、D-510、journey-polish 报告 §2.8 一致  

## 完成说明（2026-07-31）

已更新：`docs/release/app-store-assets/copy/support-en-US.md`、`website/support/index.html`、`docs/release/app-store-assets/site/support.html`。

**补充（同日）：** 营销首页 `website/index.html` 仍残留 *two Safari extensions* / *on by default · nothing to configure*，已按同一口径改为 **6 Content Blockers + Web Extension + website access**，并去掉 Home 全局 On/Off badge 叙事；`website/privacy` 与 privacy-policy 源文同步 Content Blockers 复数。`versions/*` 历史稿未改。  

## 附件

逻辑对照：`docs/design/journey-polish-review-2026-07-31.md` §2.8  
产品：`docs/decisions/decision-log.md` D-316、D-510  
