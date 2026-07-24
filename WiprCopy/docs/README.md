# docs

产品侧文档与设计资产。实现代码、工程配置不放在此目录。

面向**欧美等海外用户**（见根目录 `AGENTS.md`）。设计稿、线框图、产品文案默认按海外习惯与英文语境组织。

## 目录

| 路径 | 用途 |
|------|------|
| [`product/`](product/) | 产品文档：定位、范围、决策、PRD、changelog |
| [`wireframes/`](wireframes/) | 线框图、信息架构、流程草图（低保真） |
| [`design/`](design/) | 高保真视觉、UI 标注、导出切图、品牌素材 |

## 约定

1. **产品决策以 `AGENTS.md` + `product/` 为准**；线框与高保真不得与已对齐决策冲突。
2. 文件命名：`YYYY-MM-DD-简短英文名` 或稳定主题名（如 `home-status`）；版本迭代用后缀 `-v2`。
3. 图片优先 PNG/PDF/SVG；Figma 链接写在对应 `product` 或本目录下的 markdown 索引里。
4. 新增成体系文档时，在本 README 或 `product/README.md` 补一条索引。
