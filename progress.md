# 进度记录

## 2026-08-24 · 通用三方表新增「非电商平台的三方订单」列
- 先核实表语义：行=`thirdpart_general_order` 字段，列=各电商渠道取值；3~5 行为渠道元信息行，52~57 行列对齐左移一列。已写入 findings。
- `+dim-insert --position Q` 被服务端拒（column index 16 越界，原表仅 A~P）；改为直接 `+csv-put` 写 Q2 触发网格自动扩列，成功。
- `+cells-set` 一次性写入 Q2:Q57（56 格，值+样式），`+cols-resize` 设 Q 宽 290。
- 回读校验通过：A1:P186 与改动前逐字节一致；合并区/隐藏列/冻结/行高未变；56 格全部非空且与 A 列字段名逐行对齐。
- 8 个待确认单元格用琥珀底色 + 【待确认】前缀标注（good_price / confirmed / yc_good_id / yc_refund_time / payment_channel / sellfrom / product_id / platform）。
- 未新建 sheet、未新建文档，未 git commit。

## 2026-08-24 · 查找李文雅三方订单字段口径表
- 通讯录按姓名解析失败（空结果）。
- Drive 多组关键词检索；无 `.xlsx`；主匹配为 Base「三方订单数据注解」（末次编辑李文雅）。
- 更完整的 Sheet「三方订单表 / 通用三方表」末次编辑为李永成，作相似候选。
- `member-list` / `search:message` 权限不足已记录。

## 2026-08-24 · 评审包原址更新机制实测（本轮）
- 确认无 `minio-upload-gateway/` 源码。
- 一次性键二次 PUT：HTTP 200，线上内容从 A 变为 B（sha256 对齐）。
- `expires_in` 上限 604800（7 天）；30 天被 422 拒绝。
- 续期路径穷举失败：无 DELETE、无 overwrite、直传 UUID。
- 已把机制写入 review-package skill：`publish_minio.py`、硬规则 14、gateway-overwrite-request.md。
- 正式评审包对象当时未修改。探测对象无法删除，已列出键名。

## 2026-08-24 · 管理员删键后原址 first 回发
- 删前探测（cache-bust）：固定链接 HEAD/GET 均为 **404 NoSuchKey**；`prototypes/` 前缀那份 HEAD/GET 亦 **404 NoSuchKey**。删除成功，可当新键首发。
- 第一次 first 因本地 `exp:"__SAVE_EXP__"` 与脚本注入格式不符而停在注入（presign 已成功且未改名，未 PUT）。已把占位改成模板的 `exp:0/*__SAVE_EXP__*/` 后重发。
- 第二次 first：`key == requested_key`，`key_conflict_resolved: false`，`expires_in: 604800`，PUT HTTP 200。
- 回读 sha256 `2b0c8d8c1343d493754cf38f3630bf23a4611e63eb4d9066182158137cb4dda9` 与注入后本地一致；无 `__SAVE_URL__` 残留。
- 线上抽检含「渠道必填」「十进制 10MB / 10,000,000」「【Sheet 名】错误正文」前缀。`prototypes/` 键未回发（本就不存在）。未 git commit 评审包 HTML。

## 2026-08-24 · 产品建议落地与文档同步
- 订单管理页新增电商/非电商双 Tab；非电商平台值锁定不可改，隐藏主播、预售、买家留言、商品数量四列；电商 Tab 保持现有筛选与列集。
- 掉单管理页非电商 Tab 锁定第三方平台；店铺 ID/名称的 label、placeholder、表头同步改为渠道 ID/名称，底层继续复用 shop 字段。
- 通用三方表 Q37 写入 `xinmeiti_feidianshangpingtai=新媒体私域直充（小宝爸爸/大V店/万物心选/圣智蓝图共用；CL from 同值）`，revision 5661 回读一致。
- 原地追加更新 6 份需求说明 / SDD，均新增「本轮产品建议落地/实现约束（订单列表与掉单管理）」章节并挂通用三方表链接。
- 评审包简介已增加「通用三方表字段取值（含非电商平台列）」；变更清单、规则与验收同步补齐。
- 固定评审包链接只允许 `--mode update`，不再 first、不换链。
- 原型 commit `2013b86` 已 push；GitHub Pages run `32729186785` 成功，线上 `admin-orders.html` 与本地 sha256 均为 `d2edb43b8960c6370406a73defdf3dcd541e252d021a32312938bb909dc93575`。
- 评审包本地 sha256=`2c04f862e0832f7c39dbff91e48b8d728e32f92fb8328567d319fd035b915e87`，真实 `__SAVE__.exp=1788179760297` 保持未占位。
- `publish_minio.py --mode update` 在读取固定公开 URL 时失败：域名解析到 `10.8.8.139`，curl / urllib / requests / Chrome 均在 TLS 握手或连接阶段返回 `SSL_ERROR_SYSCALL` / `SSLEOFError` / `ERR_CONNECTION_CLOSED`；脚本在 GET 阶段退出，未执行 PUT，未新建 URL。

## 2026-08-24 21:10 · 发布收口重试（未发布成功，根因=内网不可达）
- 本地 `review-package.html` 校验通过：`__SAVE__.url` 为真实 presigned（`X-Amz-Date=20260824T123600Z`、`X-Amz-Expires=604800`、`SignedHeaders=content-type;host`），`exp:1788179760297` 为整数毫秒，无 `__SAVE_*__` 占位；sha256 `2c04f862e0832f7c39dbff91e48b8d728e32f92fb8328567d319fd035b915e87`，全程未被修改。
- `--mode update` 重试仍在 `fetch(public_url)` 阶段抛 `ssl.SSLEOFError: EOF occurred in violation of protocol` → `URLError`，未进入 PUT。
- 按备选路径直接用页面内 `__SAVE__.url` + `Content-Type: text/html` 做 PUT：`curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL`，`http=000`，5s 内失败。**PUT 同样未成功，线上对象未变更。**
- 根因定位（非脚本 / 非 TLS 配置问题，而是内网无路由）：
  - `minio.yc345.tv → 10.8.8.139`，`onion-fp-demo.yc345.tv → 10.8.8.69`（presign 网关）；两者 443 均 0 字节即断，80 端口 `Empty reply from server`，ICMP 100% 丢包。
  - 出口只有 `en0 = 172.20.10.5`（iPhone 热点网段，接口标记 `constrained`）；`scutil --nc list` 为空、无 EasyConnect/aTrust/AnyConnect 等客户端、Wi-Fi 未关联任何网络 → 无企业 VPN 通道。
  - Clash Verge (mihomo) TUN `utun0/198.18.0.1` 接管 `10.8.8.0/16`；规则本身已是 `DomainSuffix yc345.tv → DIRECT`、`IPCIDR 10.8.0.0/16 → DIRECT`，故不是代理误转发；`nc` 能连通只是 gVisor 栈本地接受 TCP。
  - `curl --interface en0` 绕过隧道直连 → `Connection timed out (28)`，证明热点侧确实没有到 `10.8.8.0/24` 的路径。
  - 时间线：presign 于 20:36 CST 成功（当时内网可达），20:53 起全部不可达；21:01–21:08 每 12s 探测共 22 次，全部 `http=000`。
- 未换链、未 `--mode first`、未改产品文案、未 git commit `review-package.html`。
- 本地内容抽检（离线 grep，等内网恢复后需在线复核）：双 Tab ✅、非电商平台锁死+「当前 Tab 已锁定，不可修改」✅、隐藏四列 ✅、渠道 ID/名称文案 ✅（`shop_id/shop_name` 复用）、简介「通用三方表字段取值（含非电商平台列）」链接 ✅、渠道必填「请选择渠道」✅、`10 × 1000 × 1000 = 10,000,000` ✅、`【Sheet 名】` 前缀 ✅。
- 抽检偏差：`sellfrom` 与 `xinmeiti_feidianshangpingtai` 在评审包 HTML 中**不存在**（0 次命中）；这两个取值本轮只写在飞书通用三方表 Q37，评审包仅以「字段口径」链接引用。未按抽检项补写文案（本轮禁止改产品文案）。
- 待用户恢复内网（回办公网或连企业 VPN）后，直接重跑 `--mode update` 即可；presigned URL 有效期至 2026-08-31，无需重新 presign。

## 2026-08-24 23:5x · 内网恢复后原址 update 发布成功
- 内网已恢复：`en0=192.168.3.49`（不再是热点），`utun7` 承载 `10.8/16` 路由；`minio.yc345.tv → 10.8.8.139` HEAD 200、耗时 0.06s。
- 发布前 grep 评审包 HTML：`sellfrom` / `xinmeiti_feidianshangpingtai` / `CL from` / `CF from` **0 命中**，正文本就干净，无需删改；简介保留「通用三方表字段取值（含非电商平台列）」链接（`shtcnEioTaphv14DdQVtmKlv6Eh`）。未改任何产品文案。
- `publish_minio.py --mode update`（固定 key，未换链、未 first）：复用线上 `__SAVE__` presigned URL，`exp_ms=1788179760297`、剩余 592966s；`PUT HTTP 200`，etag `2b95310d3877ed8fd70514db02a75ce8`。
- 回读（cache-bust 两次 + final 一次）：`http=200`、`size=89800`、`Content-Type: text/html`；线上 sha256 `2c04f862e0832f7c39dbff91e48b8d728e32f92fb8328567d319fd035b915e87` 与本地**逐字节一致**（`cmp` MATCH），无 `__SAVE_*__` 残留。
- 线上抽检全过：双 Tab ✅、非电商平台锁定 +「当前 Tab 已锁定，不可修改」✅、隐藏主播/预售/买家留言/商品数量四列 ✅、渠道 ID/名称文案（10 处）✅、渠道必填「请选择渠道」×3 ✅、`10,000,000` ×3 与 `10 × 1000 × 1000` ×3 ✅、`【Sheet 名】` ✅、简介通用三方表链接 ✅；正文无 CF/CL/sellfrom 取值字符串 ✅。
- 通用三方表 Q 列核查：Q37（A37=`sellfrom`）原值 `xinmeiti_feidianshangpingtai=新媒体私域直充（小宝爸爸/大V店/万物心选/圣智蓝图共用；CL from 同值）`，已填且非【待确认】。
- `CF from` **在任何来源都不存在**：本表 `+cells-search "CF from"` 0 命中（字段行仅到第 57 行，A58:A186 全空）；服务期/业绩归属 PRD `ZsgHdqisto2wDFxMTkrcZ4Pfnud` 全文 30020 字符内无 `CF from`/`cf_from`/`cfFrom`/`channel from` 等任何变体（keyword 命中仅为我自己的查询串被回显）；`docs +search "CF from"` 0 结果；仓库内仅有我自己写的 progress/task_plan 提及。
- 因无口径来源、拒绝编造，Q37 追加标注：`；【待确认】CF from 取值未在服务期/业绩归属 PRD 中定义，也未在本表任何行出现，待业务确认`。增量写入保留原琥珀样式 `#FFF3CD/#856404`，Q36/Q38 未动，revision 5661 → 5663，回读一致。
- 未 git commit `review-package.html`（保持 ` M` 未暂存）。

## 2026-08-31 · 双 Tab 落位纠错并重新发布

### 根因
大评审包里原本没有「通用三方」原型页（最初需求是「原型就不加了」，第 7 节只有枚举新增一条）。后来批准「非电商 Tab 锁死平台 / 隐藏恒空列 / 店铺改渠道」三条建议时没有承载页面，被落到了 `admin-orders.html`（运营后台 · 订单管理）。佐证：主播/预售/买家留言/商品数量四列只有订单管理页才有，通用三方页根本没有这些列。

### 回退
- `git restore --source=2013b86^ --worktree -- admin-orders.html`，该 commit 对此文件的改动全部为 Tab 相关，回退后核验：`el-tabs` 0 处、`paymentPlatformFilter` 勾选项恢复、四列恒常显示、表头 12 列、5 行数据正常。

### 新建通用三方页
- `admin-general-thirdparty.html`：侧边栏「通用三方」选中、面包屑「渠道投放 / 通用三方」、Tab 样式复用掉单管理页。
- 非电商 Tab：第三方平台锁定为「非电商平台的三方订单」并禁用；店铺 ID/名称 → 渠道 ID/名称（筛选项 + 表头同步）；隐藏「渠道（销售来源）」筛选项（`public_sellfrom` 202506 已废弃不写入）；操作项「激活课程」。
- 列表 21 列按「通用三方订单表前端」对齐；`yc_good_id` 用 UUID 示例，与通用三方表非电商列一致。
- 踩到并修掉旧坑：`.gt-field { display:flex }` 会盖掉 `[hidden]{display:none}`，导致 `hidden` 属性无效；补 `.gt-field[hidden]{display:none}` 后浏览器实测 `sellfromWidth/Height = 0`。
- `prototype.js` PAGE_LINKS 新增 `general` 入口，`index.html` 新增卡片并把后续编号 04→09 顺移。

### 文档同步
- 评审包 `review-package.html`：问题描述补「非电商与电商订单混在一张列表」；范围条目改为通用三方页双 Tab；行为变更 4 项去掉 Tab 相关（4-1/4-2/4-3 重编号），7 项扩为 7-1～7-4；「订单列表 Tab 展示规则」表改为「通用三方 Tab 展示规则」共 5 条；流程图 ⑤ 文案同步。
- 六份飞书文档全部原地更新（`str_replace` 改标题保住 block id，`block_replace` 换正文段）：
    - 需求说明 ×3（`UYHRdsljPovrstxS8WjcWXHfnue` / `Ai5ndA0xxotxXnxomB0chKtsn6e` / `YwxLdUtMwoNFYsxcNgcc8Jbonxf`）：标题「本轮产品建议落地（通用三方列表与掉单管理）」、正文段改写、行为变更第 7 行扩为 7-1～7-4、范围 `<li>` 扩写。
    - SDD ×3（`Cw69djCbsosrPGxKlURcM3ZAn6m` / `RqMmdBkwooZ881xMV45cZAeNnAg` / `MrEodK4Tvo3yUvxtqWAcX3SKnQc`）：标题「本轮实现约束（通用三方列表与掉单管理）」、正文段改写、SDD-IMP-010 后追加 SDD-IMP-011（页面分区）与 SDD-IMP-012（非电商展示口径）。
- 回读六份文档：`主播` / `买家留言` / `（订单列表与掉单管理）` / `订单列表以 Tab` 残留全部为 0，新内容全部命中。

### 发布
- commit `8382bf2` 已推 GitHub，Pages 三个页面均 200；线上抽检：订单管理页 `el-tabs` 0 次、`paymentPlatformFilter` 2 次；通用三方页 `platformCategoryTabs` 2 次、`激活课程` 4 次。
- MinIO 固定链接 `--mode update` 原址更新成功：复用线上 `__SAVE__`（`exp_ms=1788179760297`，剩余 6175s），`PUT HTTP 200`，etag `270355aaace1dfdd709e23adf0e8466b`；`validate_minio_release.py` 回读 `ok:true`，线上与本地 sha256 均为 `ad3a3047…86cbc9`。
- 注意：该 presigned URL 于 2026-08-31 20:36 CST 到期，之后若还要原址更新需管理员先删对象再 `--mode first`。
