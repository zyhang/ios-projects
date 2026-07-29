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

拉取完整 pack：

```
https://opendesign.cc/packs/zen-browser/DESIGN_SPEC.en.md
https://opendesign.cc/packs/zen-browser/spec.json
```
