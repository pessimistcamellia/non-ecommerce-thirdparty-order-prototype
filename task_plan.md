# 任务计划：评审包原址更新机制（实测 + 写进 skill）

## 目标
彻底解决「评审包内容更新必须换链接」：用一次性测试键验证同键二次 PUT、预签名有效期、续期路径，再把可长期执行的机制写进 review-package skill。不碰正式评审包对象。

## 阶段
- [completed] 0. 查找李文雅参与的运营后台三方订单字段存储口径表（Drive 搜索 + 打开候选核验）
- [completed] 1. 确认无 minio-upload-gateway 源码；探测网关路由
- [completed] 2. 第一步：全新测试键 presign → PUT A → 同 URL PUT B → sha256 判定覆盖
- [completed] 3. 第二步：expires_in 上限（3600 / 86400 / 604800 / 30 天）
- [completed] 4. 第三步：穷举续期路径（其他接口 / DELETE / 直传指定键）
- [completed] 5. 第四步：更新 skill / references / template / scripts
- [completed] 6. 规划文件收尾 + open -a Cursor
- [completed] 7. 在电子表格「三方订单表 / 通用三方表」末尾新增列「非电商平台的三方订单」（Q 列，Q2:Q57 共 56 行）
- [completed] 8. 管理员删正式键后探测 404，`--mode first` 原址回发最新评审包
- [completed] 9. 订单列表与掉单管理落地双 Tab、非电商平台锁定、隐藏恒空列与渠道文案
- [completed] 10. 通用三方表 Q37 回填共用 sellfrom / CL from，并回读验证
- [completed] 11. 原地更新 6 份需求说明 / SDD，评审包简介挂通用三方表
- [completed] 12. 原型已提交并通过 Pages；内网恢复后 `--mode update` 按固定 key 原址发布成功（PUT 200，线上/本地 sha256 逐字节一致），线上抽检全过
- [completed] 13. 评审包正文确认不含 CF/CL/sellfrom 取值（发布前 grep 0 命中，无需删改）；Q37 已填 sellfrom + CL from
- [blocked] 14. `CF from` 取值缺口：本表 / 服务期 PRD / 飞书全局检索均无该口径，已在 Q37 以【待确认】标注，待业务给值后回填

## 硬约束
- 正式键仅在管理员 DELETE 且公开 URL 已 404 后，才允许 `--mode first` 发回同一 key（2026-08-24 已完成）
- 不改本仓库业务代码（原型/PRD/SDD）；评审包 HTML 不 git commit
- 探测对象能删则删，删不掉列出键名
- 结论必须贴真实 HTTP 状态码与响应体

## 错误记录
- 默认非交互 zsh 的 PATH 不含 `/usr/bin`，curl 报 command not found；补全 PATH 后正常。
- 正式包首发第一次：本地 `exp:"__SAVE_EXP__"` 导致 inject 失败；presign 未改名且未 PUT，改占位后重发成功。
