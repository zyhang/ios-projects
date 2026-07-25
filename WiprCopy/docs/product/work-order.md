# 推荐开工顺序

状态：**已对齐**团队习惯；范围随 **Safari 优先** 收束。  
文档语言：中文。

## 顺序

1. **名称 / 品牌** — 产品名、one-liner、语气 ✅（Gleem / Block Ads & Trackers；one-liner 已改为 Safari 向）  
2. **定位 / PRD** — ✅ 2026-07-25 修订：C 为主 + 克制 plus；不以低价为主轴；系统级后置  
3. **线框** — IA、关键流程（`docs/wireframes/`）🔄 按 Safari 优先修订（去掉默认 system-wide 主路径）  
4. **视觉设计** — `docs/design/`：**冷静工具** 与 **干净生活** 两套方向对比后锁定 🔄  
5. **工程** — App 壳、IAP、Safari Content Blocker、名单、规则包、自救  
6. **系统级 / Mac 客户端** — **后置论证**；需要时再开 [url-filter-spike.md](url-filter-spike.md)，**不**绑死 v1 上架  

## 为何如此

- 先身份与 Safari 主路径，避免系统级与 Mac 战线拖垮 v1。  
- 设计受 [`prd.md`](prd.md) 与 [`AGENTS.md`](../../AGENTS.md) 约束。  
- Plus 能力逐项过门槛后再进线框，避免做成半吊子重型拦截器。  

## 设计约束（不得漂移）

- 海外用户、**界面英文**（`AGENTS.md` 规则 0–1；[prd.md](prd.md) §2）  
- 隐私本地、不采集浏览（`AGENTS.md` 规则 2；[prd.md](prd.md) §3）  
- 主状态：保护开关、名单新鲜度、Safari 错误配置 — [prd.md](prd.md) §7  
- 规则包：Core / Annoyances / Strict — [rule-packs.md](rule-packs.md)  
- 自救：暂停、按站放行、报错 — [breakage-recovery.md](breakage-recovery.md)  
- 解锁：免费 App + 一个覆盖 v1 Safari 能力的 IAP — [commerce.md](commerce.md)  
- **文档中文 / 界面文案英文** — `AGENTS.md` 规则 0  
- **v1 不默认卖 system-wide** — [prd.md](prd.md) §4.4 / §5.5  
