# OpenDesign 参考笔记（Stillwall 营销站）

来源：[opendesign.cc](https://opendesign.cc/) · 协议：`https://opendesign.cc/skill.md`

## 需求定调

| 项 | Stillwall |
|----|-----------|
| 领域 | Consumer utility · Safari · privacy-adjacent |
| 气质 | calm · restrained · honest · unobtrusive |
| 密度 | 宽松营销页（非 dashboard） |
| 明暗 | 以浅暖色为主；深色可作为对比版本 |

**观点：** 广告拦截站最容易做成「威胁雷达 / 霓虹盾牌」——与产品理念相反。正确方向是 **安静的高级感**，像隐私浏览器或精品 Mac 工具，而不是安全厂商 landing。

## 推荐系统（catalog 检索）

| 优先级 | slug | 为何合适 | 借什么 | 不借什么 |
|--------|------|----------|--------|----------|
| **主参考** | [`zen-browser`](https://opendesign.cc/en/sites/zen-browser) | 隐私浏览器、calm/premium、暖纸底、serif 标题 | 布局骨架、字阶节奏、间距、动效时长、语气 | coral accent（改用 Stillwall `#2F6A58`） |
| 辅 · 温度 | [`claude`](https://opendesign.cc/en/sites/claude) | 暖 monochrome、克制、专业冷静 | 暖灰边线、serif display 权威感 | 无品牌 accent 时的过冷灰 |
| 辅 · 产品 | [`replay-software`](https://opendesign.cc/en/sites/replay-software) | Mac 工具站、大字号 + 产品图 | 居中单栏、大 hero 产品图 | 纯白刺眼底（略暖化） |
| 备选 | `campsite` · `getdooapp` · `apple` | SaaS/产品克制或 Apple 产品页留白 | 结构模块 | 高饱和 CTA 橙红 / 全黑英雄 |

明确 **不** 作为主参考：`linear` / `raycast`（偏 dev-tool 暗色高能）、高饱和 playful 站。

## Zen Browser 关键 tokens（已落地 v4）

来自 `https://opendesign.cc/packs/zen-browser/spec.json` 与 `DESIGN_SPEC.en.md`：

```
bg:      #F2F0E3  → Stillwall 映射为略偏品牌的暖纸 #F3F1E8 / #F7F6F2
ink:     #2E2E2E
muted:   #9E9E9E
accent:  #F76F53  → 替换为 brand #2F6A58
radius:  8 / 12 / 24 / 999
motion:  150 / 200 / 600 · cubic-bezier(0.4, 0, 0.2, 1)
layout:  centered single-column hero · container 1280 · paragraph 680
type:    display serif ~60/1.0 · body sans 16/1.5
```

### Don'ts（遵守）

- 不用纯冷白底 / 冷科技蓝主色  
- 不用拥挤网格堆卖点  
- 不用弹跳夸张动效  
- 不用攻击性营销文案  

## 版本对应

| 版本 | 与 OpenDesign 关系 |
|------|-------------------|
| v1 Calm Editorial | 灵感近 Wipr；未接 OD tokens |
| v2 Product Hero | 结构近 Magic Lasso |
| v3 Quiet Manifesto | 深色理念叙事 |
| **v4 Zen Calm** | **主接地：zen-browser 系统 + Stillwall 品牌色** |
| **v5 Product Theater** ⭐ | **已选结构**：apple 全宽色带 + campsite 浅色模块；accent → `#2F6A58`（D-110） |
| **v6 Quiet Gazette** | **主接地：thebrowser-company 系统**（2026-07-29 新研究；tokens 见下） |

## v6 Quiet Gazette — The Browser Company tokens（已落地）

来源 `https://opendesign.cc/packs/thebrowser-company/DESIGN.md` 与 `DESIGN_SPEC.en.md`：

```
bg:      #EDEEE7（暖纸，strict two-tone；不替换为纯白）
ink:     #000000 → Stillwall 软化为 #101210
ink-soft: rgba(0,0,0,0.85) → rgba(16,18,16,0.78)
muted:   #A0A0A0 → #8B8C85
line:    rgba(0,0,0,0.15)
accent:  原站无 hue accent → 品牌 #2F6A58 仅用于 pill CTA / 编号 / kicker
radius:  0 / 0 / 0 / 999（除 pill 外一律直角，无阴影）
motion:  200 / 250 / 400 · cubic-bezier(0.4, 0, 0.2, 1)；hover 仅颜色/填充变化
layout:  单居中栏 · container 1280 · paragraph 680 · 大段垂直留白
type:    transitional-serif（display 斜体）+ geometric-mono（uppercase 大 tracking 标签）
         → 落地为 Newsreader（Google Fonts）+ ui-monospace
```

**版式转译：** 头版 hero（italic serif 两行标题 + FIG. 编号截图框）→「社论」前提段 →
免费功能做成报纸**目录**（No. 01–07 编号 + hairline）→ Pro 为**「晚报」深色版**
（#121914 反色）→「更正与澄清」三栏边界声明（§ 1–3）→ mono 版记页脚。

**文案来源：** 直白句式借 Wipr 2（“the things that make the web slow and ugly”），
分类/卖点结构借 Magic Lasso；**功能事实以 product-charter.md 为准**
（YouTube & X 标注 in Safari only；不写省电百分比；不承诺系统级拦截）。

**遵守的 Don'ts：** 不用饱和背景色、不用阴影/3D、不用 sans 大标题、不用圆角容器、
不用侵略性 CTA（mono 小写链接 + 单一 brand pill）。

拉取完整 pack：

```
https://opendesign.cc/packs/zen-browser/DESIGN_SPEC.en.md
https://opendesign.cc/packs/zen-browser/spec.json
```
