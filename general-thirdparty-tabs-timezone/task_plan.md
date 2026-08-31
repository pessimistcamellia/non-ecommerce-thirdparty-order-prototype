# 任务计划：通用三方双 Tab 与时区统一

## 目标
独立交付只包含「通用三方双 Tab、非电商数据分区、字段口径、created_at 查询/展示、UTC 请求转换、导出时区」的评审包、高保真标注原型、飞书需求说明与 SDD；固定评审入口发布到内网 MinIO。

## 阶段
- [completed] 1. 读取 skills、线上截图与现有后台 Tab 样式
- [completed] 2. 制作独立高保真标注原型与评审包
- [completed] 3. 本地交互与内容门禁验证
- [completed] 4. 部署 GitHub Pages 外网独立路径
- [completed] 5. 创建飞书需求说明与 SDD、互链并开放权限
- [completed] 6. 更新规划文件并自动打开全部本地产物
- [completed] 7. 恢复 template 编辑引擎与 GitHub 本地持久化
- [completed] 8. 原链接重部署并完成线上全量交互验证
- [completed] 10. 按截图定稿行为变更并删除数据变更节
- [completed] 11. 读取「导入&直充-非电商平台的三方订单」群中任政与朱楚茗的沟通，提炼确认项与待定项
- [completed] 12. 核对飞书「三方订单表」及线上评审包人工编辑，确定四件套更新范围
- [completed] 13. 原地更新高保真原型、评审包生成器与内网版本
- [completed] 14. 原地更新飞书需求说明与 SDD，并回读校验
- [completed] 15. 固定评审包链接原址发布；新版原型发布为新对象并完成线上交互及内容门禁
- [completed] 16. 按复核结论修正 Excel 非电商操作口径与原型 `yc_good_id` 示例，并保持评审包入口不变

## 硬约束
- 不修改或混入现有 v14 MinIO 大评审包。
- 评审包固定使用 `general-thirdparty-tabs-timezone-review-20260825.html`，不得换链接。
- 原型对象如因网关拒绝覆盖，可发布新对象并由固定评审包入口改指向新版原型。
- 范围只包含本任务正文，不扩展 Excel 导入、掉单 Base、10MB、上传渠道必填弹窗。
- 原型使用最新 proto-note 标注引擎；若有弹窗，仅用 `.modal-mask` + `.is-open`。
- 本轮评审包、原型、需求说明、SDD 均沿用原链接；发布前先拉取并保留线上人工编辑。

## 错误记录
| 错误 | 尝试次数 | 解决方案 |
|---|---:|---|
| deploy-prototype 文档中的旧脚本路径不存在 | 1 | 改用实际技能目录下脚本 |
| `Leo-ai05/prototypes` 推送被 GitHub 403 拒绝 | 1 | 改用已授权的 `pessimistcamellia/non-ecommerce-thirdparty-order-prototype` GitHub Pages 独立目录 |
| OpenAPI 不接受 `manage_collaborator_entity=collaborator_can_edit` | 1 | 已完成 `tenant_editable`、评论/复制可编辑、分享范围 anyone；保留现有协作者管理设置并在交付说明中披露 |
| 生成脚本用 `re.sub` 直接替换含 `\d` 的模板脚本时报 bad escape | 1 | replacement 改用 lambda，按原字节注入 template 编辑引擎 |
| 原型旧 key 即使传 `overwrite=true` 仍被网关改名 | 2 | 不上传冲突派生 key；改发 `prototype-20260828-v2.html`，固定评审包原址改指新原型 |
