# URL Filter spike 清单

状态：**后置**（v1 不作为上架门槛；Safari 主路径优先）。  
文档语言：中文。  
上级：[prd.md](prd.md) §5.5。

## 何时启动

- 团队确认要论证 **系统级全 App 拦截** 时再开本清单。  
- **不**阻塞 v1 的 Safari 设计、工程与上架。  
- 在 spike 通过并写入 PRD 之前，商店与 UI **不得**默认宣称 system-wide 已交付。

## 目标（未来）

在隐私红线内，证明系统级拦截（Apple URL Filters）在目标平台上可产品化。

## Spike 范围外

- 打磨 UI、规则包、App Store 文案（属 Safari v1 主线）  
- 完整生产级名单体量  
- Web Extension（Extra）  

## 范围内（启动后）

- [ ] Apple 示例 / 文档：`NEURLFilterManager`、`NEURLFilterControlProvider`、Bloom 预过滤、PIR 服务  
- [ ] 相关 App + 扩展 target  
- [ ] 从 App 启用/关闭 Filter；配置持久化  
- [ ] 预过滤拉取间隔  
- [ ] 系统级拦截一小套固定测试 URL（不限于 Safari）  
- [ ] 确认与 VPN、iCloud Private Relay 主路径可并存  
- [ ] 记录 App 进程能/不能观察到什么  
- [ ] 粗运维笔记：托管 PIR、token、更新失败行为（fail open vs closed）  

## 成功 → 下一步

- 更新 PRD：主/副楔子、MVP、one-liner、商业解锁说明  
- 更新线框与商店文案  
- 默认倾向：系统级打进**同一**买断 IAP（再确认）

## 失败 / 过重 → 回退

- 可继续只做 Safari；或缩小系统级名单/刷新频率  
- **不**为半成品系统级单独硬推第二核心 IAP 当主商业故事  

## 参考

- [URL filters](https://developer.apple.com/documentation/networkextension/url-filters)  
- [Filtering traffic by URL](https://developer.apple.com/documentation/networkextension/filtering-traffic-by-url)  
- WWDC25: Filter and tunnel network traffic with NetworkExtension  
- 产品决策：[prd.md](prd.md) · Agent 规则：[`AGENTS.md`](../../AGENTS.md)  
