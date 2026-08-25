# 进度记录

## 2026-08-25
- 已读取 `review-package`、`proto-note`、`deploy-prototype` 与上下文规划规范。
- 已读取评审包模板、界面/中后台类型参考、changeset schema。
- 已核对线上通用三方截图与仓库 `admin-dropped-orders.html`、`admin-orders.html`。
- 已建立独立交付目录，确保不修改现有 v14 MinIO 大评审包。
- 已完成独立高保真原型：双 Tab、数据隔离、非电商渠道文案、created_at 东八区展示、UTC ISO 请求示例与 6 条 proto-note 标注。
- 已完成独立评审包：简介、行为/数据变更、存量处理、字段与时间规则、校验反馈、外网 iframe 与决策事项。
- 浏览器验证通过：电商/非电商切换、非电商平台锁定、三条非电商演示数据与 created_at 时间列正常；无业务 JavaScript 错误。
- `deploy-prototype` 实际脚本对 `Leo-ai05/prototypes` 推送被 403 拒绝，已按用户允许的备选路径发布到本仓库 GitHub Pages 独立目录。
- 已在生产力方舟创建同名子文件夹及两篇 docx，文档 owner 为当前用户朱楚茗；已互链外网评审包、外网原型和对应文档。
- 两篇文档已验证 `link_share_entity=tenant_editable`、`comment_entity=anyone_can_edit`、`security_entity=anyone_can_edit`、`share_entity=anyone`。
- 当前 OpenAPI schema 不支持修改 `manage_collaborator_entity`，直接请求返回 `1063001 Invalid parameter`；该字段保持 `collaborator_can_view`。
- 已取得 SDD FR-1/FR-2/FR-3 block ID 并回填原型变更卡深链。
- GitHub Pages 最终流水线成功；评审包与原型两个 HTTPS 链接均已外网回读，且评审包 iframe 指向同仓独立原型 URL。
