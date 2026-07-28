# 后端与规则交付

> **已归档（2026-07-27，project-v1）**：本文属于全量文档快照的一部分，不再作为现行权威。见 [归档说明](../README.md)。重构请写到 `docs/`。

## 1. 范围

首个 TestFlight 不建设用户账号、分析系统或复杂 API。后端仅承担静态规则交付；未来 Pro 阶段再增加 PIR 服务。

阶段 A：

- 规则 manifest。
- Content Blocker 规则包。
- Gleem Extra 静态参数/模块开关。
- 紧急回滚信息。

阶段 B：

- URL Filter Bloom filter 数据。
- PIR 数据库与查询服务。
- Apple OHTTP relay 对接。

## 2. 设计原则

- 静态优先。
- 内容可签名、可缓存、可回滚。
- 不为每台设备生成专属 URL。
- 不使用用户账号或设备 ID。
- 不记录用户访问或拦截内容。
- 任何后端故障不能导致持续断网。

## 3. 规则 manifest

建议字段：

```json
{
  "schemaVersion": 1,
  "releaseId": "2026.07.26.1",
  "generatedAt": "2026-07-26T00:00:00Z",
  "minimumAppVersion": "1.0.0",
  "expiresAt": "2026-08-09T00:00:00Z",
  "packages": [
    {
      "id": "safari-general",
      "url": "https://rules.example.com/2026.07.26.1/safari-general.json",
      "sha256": "...",
      "size": 123456
    }
  ],
  "modules": {
    "youtube": true,
    "x": true
  },
  "rollbackTo": null,
  "signature": "..."
}
```

规则：

- `releaseId` 单调可排序。
- `expiresAt` 只表示需要用户注意，不表示到期后删除规则。
- `minimumAppVersion` 防止新格式下发给旧客户端。
- package URL 不包含用户标识。
- manifest 签名覆盖除 `signature` 外的规范化内容。

## 4. 签名与密钥

建议：

- 使用 Ed25519 签名。
- 客户端内置公钥。
- 私钥存放于受控发布环境，不进入 Git。
- 生产签名与测试签名分离。
- 密钥轮换需要 manifest 支持下一公钥和双签过渡。

发布过程：

1. CI 拉取固定版本规则源。
2. 编译与测试。
3. 生成 package 和 SHA-256。
4. 生成人类可读差异摘要。
5. 人工批准。
6. 使用生产私钥签名。
7. 上传不可变版本路径。
8. 最后原子更新 latest manifest。

## 5. 缓存与 CDN

- 版本化 package 使用长缓存和 immutable。
- latest manifest 使用短缓存和 ETag。
- 客户端支持 `If-None-Match`。
- CDN/对象存储不得启用用户级分析。
- 基础设施日志关闭或设置最短必要保留期。
- 隐私政策如实披露 CDN/托管方可能处理 IP 和请求元数据。

“零数据收集”指 Gleem 不建立用户行为和浏览数据集，不得误写成互联网请求不经过任何基础设施。

## 6. 回滚

### 6.1 自动回滚条件

客户端发现：

- 包哈希不匹配。
- manifest 签名失败。
- JSON 解析失败。
- Safari reload 失败。
- schema 不支持。

处理：

- 拒绝新包。
- 保留上一有效版本。
- 记录本地错误。
- 下次前台进入时低频重试。

### 6.2 服务端紧急回滚

- latest manifest 指回上一稳定 release。
- 可关闭 YouTube 或 X 单站模块。
- 不远程下载可执行 JavaScript。
- 紧急修复发布后补充事故记录和回归用例。

## 7. 可用性

阶段 A 不需要高复杂度高可用：

- 静态对象存储 + CDN。
- 不引入数据库。
- 不引入队列。
- 不引入按用户动态响应。

最低要求：

- HTTPS。
- IPv6 可访问。
- 支持合理缓存。
- 监控仅检查公共端点可用性，不关联用户。
- 包上传和 manifest 切换可重复执行。

## 8. PIR 服务（阶段 B）

### 8.1 前置验证

- Apple 当前 URL Filter 和 OHTTP relay 分发要求。
- CloudKit/Identity & Trust 注册流程。
- Bloom filter 参数和误判率。
- PIR 数据库大小、请求延迟和成本。
- 隐私模型是否符合“服务器无法还原用户 URL”的承诺。

### 8.2 服务目标

- 不建立用户账号。
- 不记录可关联用户的查询。
- 对 OHTTP/PIR 请求进行容量控制，但不使用跨请求设备标识。
- 服务不可用时 URL Filter fail open。
- 数据集版本化、签名和可回滚。

### 8.3 禁止

- 把 PIR 退化为普通明文 URL 查询 API。
- 为调试临时记录完整查询。
- 将规则查询与订阅账号绑定。
- 未经披露将请求转交第三方分析服务。

## 9. 环境

建议最小环境：

- `development`：本地/模拟规则和测试签名。
- `beta`：TestFlight 规则源，独立签名。
- `production`：正式发布，受控签名。

不同环境使用不同 base URL、公钥和 manifest，不通过运行时用户开关切换生产环境。

## 10. 发布验收

- package 与 manifest 哈希一致。
- 签名验证通过。
- 旧客户端不会下载不兼容格式。
- CDN 返回正确 MIME 和缓存头。
- IPv4/IPv6 均可用。
- 离线继续使用旧规则。
- latest manifest 可回滚。
- 日志与监控设置符合隐私文档。
