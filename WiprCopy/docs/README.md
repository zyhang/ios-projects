# docs

产品侧文档与设计资产。实现代码、工程配置不放在此目录。

面向**欧美等海外用户**（见根目录 [`AGENTS.md`](../AGENTS.md)）。**中国人开发、欧美人使用**：对内文档默认中文，用户可见界面与商店文案默认英文。

## 语言约定

| 内容 | 默认语言 |
|------|----------|
| PRD、产品/开发说明、README、设计说明与标注 | **中文** |
| 线框/高保真中的**界面字符串**、App Store 面向用户的文案 | **英文** |
| 系统 API / 框架名 | 英文原名 |

详见 [`AGENTS.md`](../AGENTS.md) 规则 0。

## 目录

| 路径 | 用途 |
|------|------|
| [`product/prd.md`](product/prd.md) | **PRD 权威源**（定位、MVP、决策、范围外） |
| [`product/`](product/) | 产品专题文档索引与深挖 |
| [`wireframes/`](wireframes/) | 线框图、信息架构、流程草图（低保真） |
| [`design/`](design/) | 高保真视觉、UI 标注、导出切图、品牌素材（**重设计中**） |
| [`archive/`](archive/) | 已封存设计稿；v1 见 [`archive/design-v1-2026-07-25/`](archive/design-v1-2026-07-25/) |

## 约定

1. **硬性规则**以 [`AGENTS.md`](../AGENTS.md) 为准；**产品决策**以 [`product/prd.md`](product/prd.md) 及专题文档为准。线框与高保真不得与已对齐决策冲突。
2. **写文档用中文；写界面用英文。**
3. 文件命名：`YYYY-MM-DD-简短英文名` 或稳定主题名（如 `home-status`）；版本迭代用后缀 `-v2`。
4. 图片优先 PNG/PDF/SVG；Figma 链接写在对应 `product` 或本目录下的 markdown 索引里。
5. 新增成体系文档时，在本 README 或 `product/README.md` 补一条索引；变更产品决策时改 PRD，不把决策表堆进 `AGENTS.md`。
