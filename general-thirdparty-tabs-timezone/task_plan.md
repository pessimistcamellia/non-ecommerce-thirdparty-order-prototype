# 任务计划：通用三方双 Tab 与时区统一

## 目标
独立交付只包含「通用三方双 Tab、非电商数据分区、created_at 查询/展示、UTC 请求转换、导出时区」的评审包、高保真标注原型、飞书需求说明与 SDD，并发布到 GitHub 外网。

## 阶段
- [completed] 1. 读取 skills、线上截图与现有后台 Tab 样式
- [completed] 2. 制作独立高保真标注原型与评审包
- [completed] 3. 本地交互与内容门禁验证
- [completed] 4. 部署 GitHub Pages 外网独立路径
- [completed] 5. 创建飞书需求说明与 SDD、互链并开放权限
- [completed] 6. 更新规划文件并自动打开全部本地产物

## 硬约束
- 不修改或混入现有 v14 MinIO 大评审包。
- 不使用 MinIO / onion-fp-demo / minio.yc345.tv。
- 评审包与原型使用独立外网 URL，评审包 iframe 指向外网原型。
- 范围只包含本任务正文，不扩展 Excel 导入、掉单 Base、10MB、上传渠道必填弹窗。
- 原型使用最新 proto-note 标注引擎；若有弹窗，仅用 `.modal-mask` + `.is-open`。

## 错误记录
| 错误 | 尝试次数 | 解决方案 |
|---|---:|---|
| deploy-prototype 文档中的旧脚本路径不存在 | 1 | 改用实际技能目录下脚本 |
| `Leo-ai05/prototypes` 推送被 GitHub 403 拒绝 | 1 | 改用已授权的 `pessimistcamellia/non-ecommerce-thirdparty-order-prototype` GitHub Pages 独立目录 |
| OpenAPI 不接受 `manage_collaborator_entity=collaborator_can_edit` | 1 | 已完成 `tenant_editable`、评论/复制可编辑、分享范围 anyone；保留现有协作者管理设置并在交付说明中披露 |
