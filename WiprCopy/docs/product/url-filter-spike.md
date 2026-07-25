# URL Filter spike 清单

状态：**已规划**（决策：上架锁定前先 spike；默认目标自建 PIR）。  
文档语言：中文。

## 目标

在隐私红线内，证明系统级拦截（Apple URL Filters）在 iPhone 与 Mac 上可上架。

## Spike 范围外

- 打磨 UI、规则包、App Store 文案  
- 完整生产级名单体量  
- Web Extension（Extra）  

## 范围内

- [ ] Apple 示例 / 文档：`NEURLFilterManager`、`NEURLFilterControlProvider`、Bloom 预过滤、PIR 服务  
- [ ] iOS 与 macOS 上的 App + 扩展 target  
- [ ] 从 App 启用/关闭 Filter；配置持久化  
- [ ] 预过滤拉取间隔  
- [ ] 系统级拦截一小套固定测试 URL（不限于 Safari）  
- [ ] 确认与 VPN、iCloud Private Relay 主路径可并存  
- [ ] 记录 App 进程能/不能观察到什么  
- [ ] 粗运维笔记：托管 PIR、token、更新失败行为（fail open vs closed）  

## 成功 → 下一步

默认：生产化自建 PIR + 名单管线；v1 系统级含在基础购买内。

## 失败 / 过重 → 回退

v1 仍保留系统级，缩小名单和/或降低刷新频率；**不**砍主楔子，也**不**降为单独核心 IAP。

## 参考

- [URL filters](https://developer.apple.com/documentation/networkextension/url-filters)  
- [Filtering traffic by URL](https://developer.apple.com/documentation/networkextension/filtering-traffic-by-url)  
- WWDC25: Filter and tunnel network traffic with NetworkExtension  
- 产品决策：[prd.md](prd.md) · Agent 规则：[`AGENTS.md`](../../AGENTS.md)  
