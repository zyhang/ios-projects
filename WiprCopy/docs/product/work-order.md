# 推荐开工顺序

状态：**已对齐**团队习惯。  
文档语言：中文。

## 顺序

1. **名称 / 品牌** — 产品名、one-liner、语气 ✅（Gleem / Block Ads & Trackers）  
2. **线框** — IA、关键流程（`docs/wireframes/`）✅ 首轮  
3. **视觉设计** — 高保真、图标方向（`docs/design/`）✅ hi-fi HTML + tokens（图标待定）  
4. **工程** — App 壳、IAP、拦截器、名单、URL Filter  
5. **URL Filter spike** — 可与 (2)–(3) 并行；营销宣称「system-wide」前**必须**通过  

## 为何如此

- 符合本团队习惯（先身份与体验）。  
- 设计仍受 [`prd.md`](prd.md) 已锁定决策与 [`AGENTS.md`](../../AGENTS.md) 约束（隐私、包、自救、商业）。  
- URL Filters 技术风险真实：不能用打磨替代 spike；与设计并行，避免临近上架被卡。  

## 设计约束（不得漂移）

- 海外用户、**界面英文**（`AGENTS.md` 规则 0–1；[prd.md](prd.md) §2）  
- 隐私本地、不采集浏览（`AGENTS.md` 规则 2；[prd.md](prd.md) §3）  
- 主状态：保护开关、名单新鲜度、错误配置 — [prd.md](prd.md) §7  
- 规则包：Core / Annoyances / Strict — [rule-packs.md](rule-packs.md)  
- 自救：暂停、按站放行、报错 — [breakage-recovery.md](breakage-recovery.md)  
- 解锁：免费 App + 一个含系统级在内的 IAP — [commerce.md](commerce.md)  
- **文档中文 / 界面文案英文** — `AGENTS.md` 规则 0  
