# 调研发现 · 评审包原址更新机制

## 待定问题

| # | 待定项 | 当前处理方式 | 需用户确认 |
|---|-----|----|-----|
| 1 | 通讯录搜不到「李文雅」open_id；`drive +member-list` 缺 `docs:permission.member:retrieve`，无法列出协作者 | 以 Drive 搜索结果里的 `owner_name` / `edit_user_name` 判断参与方式 | 是否补授权后再核协作者名单 |
| 2 | 无独立 `.xlsx` 命中；最完整口径在电子表格「三方订单表」，但末次编辑人是李永成 | 把李文雅末次编辑的 Base 当主匹配，电子表格作高度相似候选 | 目标是否就是 Base，还是那张更全的 Sheet |

无（网关实测部分均已基于明确输入）。

## 李文雅 · 三方订单列表字段怎么存（2026-08-24）

**主匹配（李文雅末次编辑，且内容是字段口径/落库）：**

- 标题：三方订单数据注解
- 类型：bitable（多维表格）
- 表名：三方订单通用表数据结构（列：字段名称 / 字段注释 / 天猫取值 / 微信视频号取值 / 抖店取值；行含 `id`、`shop_id`、`shop_name`、`spu_id`、`order_status`、`pay_time`、`order_id`、`amount` 等）
- 所有者：白天航；末次编辑：李文雅
- 链接：https://guanghe.feishu.cn/base/C6Lpb1PazaP6cUs4MzOcJNctn5g

**高度相似、字段更全，但搜到的末次编辑人不是李文雅：**

- 标题：三方订单表（子表「通用三方表」写明业务表 `growth_order_thirdparty.thirdpart_general_order` / `thirdpart_general_order` / `thirdpart_general_order_extra`，逐字段写各渠道怎么取、怎么存）
- 类型：sheet
- 所有者：白云；末次编辑：李永成
- 链接：https://guanghe.feishu.cn/sheets/shtcnEioTaphv14DdQVtmKlv6Eh

**非目标（财务上传模板字段，不是运营后台列表落库）：**

- 非电商平台订单及结算单字段-财务（wiki/sheet，所有者李莹莹）https://guanghe.feishu.cn/wiki/BYGkwfBKMikSdGkWRKUc7RAAnGd

失败项：`contact +search-user` 对「李文雅/文雅」返回空；`im +messages-search` 缺 `search:message`；`wiki +search` 无此子命令；本地 `findings.md` / `review-package.html` 未引用上述 Base。

## 「通用三方表」这张表在表达什么（2026-08-24 已用表内实际内容验证）

链接：https://guanghe.feishu.cn/sheets/shtcnEioTaphv14DdQVtmKlv6Eh （sheet_id `cVwpOI`）

用户的初步判断**成立**，但需补两点精确化：

1. **行 = 落库字段**：A 列是业务表 `growth_order_thirdparty.thirdpart_general_order` / `thirdpart_general_order_extra` 的字段名（A1 单元格写明），C 列是字段类型（varchar / int4 / timestamptz），D 列是字段含义注释。B 列「是否迁移」为隐藏列。
2. **列 = 各电商渠道该字段怎么取值**：第 2 行是渠道表头，E→P 依次为 快手 / 微店 / 抖音小程序 / 小红书 / 拼多多 / 京东(空) / 视频号小店(空) / 天猫旗舰店 / 京东 / 天猫 / 视频号小店 / 有赞。J、K 为隐藏空列。
3. **不只是字段行**：第 3~5 行是渠道级元信息行，不是字段——`三方API获取地址`、`其他备注`、`订单结构`（购物车/拆单口径）。
4. **行区块有两段**：6~50 行是订单主体字段；51~57 行是第二段（`spu_id` 重复 + 收货地址块 `user_name`/`province_name`/`city_name`/`area_name`/`address_info`/`tel_number`）。⚠️ 52~57 行列对齐比上半部分左移一列（类型落在 B、注释落在 C、D 为空），E 起的渠道列不受影响。
5. **单元格文案惯例**：直接写来源路径（`open.order.detail/data/orderBaseInfo/oid`）、写死值（`写死：2889008982`）、计算规则（`amount / count`）、`常规`（=系统按通用逻辑处理）、`无` / `没用到`（=该渠道不适用）、`空，废弃`（=字段已废弃）。**表内没有「不适用」「—」的用法**，所以本次新列一律沿用 `无` / `空，废弃`。
6. 冻结 2 行 4 列；A1:O1 为合并标题（P 列「有赞」是后追加的，落在合并区之外——本次新增 Q 列与之同构）。

## 本次新增列（Q 列）

- 列名：`非电商平台的三方订单`，位于末列 Q，宽度 290（对齐 O:P）。
- 填写范围 Q2:Q57，共 56 行（含 1 行表头 + 3 行元信息 + 52 行字段）。
- 待确认单元格用琥珀底色 `#FFF3CD` + 文案前缀 `【待确认】`：Q16 `good_price`、Q18 `confirmed`、Q24 `yc_good_id`、Q32 `yc_refund_time`、Q33 `payment_channel`、Q37 `sellfrom`、Q39 `product_id`、Q40 `platform`。
- 其余单元格 1:1 沿用邻列样式（`#ffffff` / `#1f2329` / 13px / 垂直居中，不设自动换行）。
- 回读校验：A1:P186 与改动前逐字节一致；合并区 A1:O1、隐藏列 B/J/K、冻结 2 行 4 列、行高全部未变。

### 取值依据（来自本次非电商需求）
- Excel 模板（`prototype.js` 内嵌真实 xlsx 解码得到）：
  - 支付成功订单表：订单ID / 收件人姓名 / 电话号码 / 收货省 / 收货市 / 收货区 / 详细地址 / 商品名称 / 商品数量 / 组合商品ID / 订单实付金额
  - 退款订单表：订单ID / 本账期退款金额 / 退款原因描述
- 渠道枚举（渠道注册 Base）：小宝爸爸 `xiaobaobaba`、大V店 `davdian`、万物心选 `wanwuxinxuan`、圣智蓝图 `shengzhilantu`。
- 关键口径：渠道必填、10MB=10,000,000 字节（十进制）、失败原因带【Sheet名】前缀、任一失败整批 0 行入库、退款累计口径（`>=` 实付置退款成功）、退款原因描述写入洋葱订单 `refundInfoList`（本表无对应字段）。

## 网关实测（原任务）

## 网关源码
- `/Users/zhuchuming` 下 `**/minio-upload-gateway/**` 匹配数：0。本机仍无源码目录。
- OpenAPI：`GET https://onion-fp-demo.yc345.tv/openapi.json` 标题 `MinIO Upload Gateway` 1.0.0。

## 第一步：同键二次 PUT（一次性键）
- 键：`review-pkg-demos/_probe-f8ca95790e4ca35d.html`
- presign：HTTP 200，`key == requested_key`，`key_conflict_resolved: false`
- PUT A：HTTP **200**，体空，ETag `f73ef6b9d4fff7a6e5be3ef652805cd6`；GET sha256=`806814bb9be896ad2ab22d660cb6ca30f844ab19be23fe6584c82f059257fec4`（A）
- **同一 upload_url PUT B：HTTP 200**，体空，ETag `8db3c53e5c8a964514c3364db01adf3b`
- GET 后再哈希：`d795d636bf77620d0c269b59a88a55ef6c3320de49844e0dc2c14e5f41ddf672` = B
- **结论：原址覆盖可行。** `retention_days: 300` + `x-amz-expiration` 是生命周期删除，不是 WORM。

## 第二步：expires_in
- 合法：60～604800。3600/86400/604800 均 HTTP 200，`X-Amz-Expires` 与请求一致。
- 604800 当场 PUT/GET 成功。
- 604801 及以上、以及 <60：HTTP 422。

## 第三步：续期
- 路由仅有 `/` `/api/info` `/recent` `/health` `POST /v1/presign` `POST /v1/upload`
- 已存在键再 presign：必改名。overwrite 类字段忽略。
- 无 DELETE。匿名 DELETE 公开对象 403 AccessDenied。
- `/v1/upload` 只有 `file` + `prefix`，始终 UUID 名。

## 存量正式键
- `__SAVE__` 占位符 + 键已存在 → 不能经网关续签，也不能用页面 PUT。
- 救回原链：管理员 DELETE `onionext/review-pkg-demos/non-ecommerce-thirdparty-order-v14-20260812.html` 后按 `--mode first` 重发同一 key。
- **2026-08-24 已执行**：管理员删键后探测均为 404；`--mode first` 原 key 回发成功。固定链接 https://minio.yc345.tv/onionext/review-pkg-demos/non-ecommerce-thirdparty-order-v14-20260812.html 现为注入后内容，sha256=`2b0c8d8c1343d493754cf38f3630bf23a4611e63eb4d9066182158137cb4dda9`，`__SAVE__.exp=1788179760297`（约 7 天）。次键 `prototypes/review-pkg-demos/non-ecommerce-thirdparty-order-v14-20260812.html` 仍 404，未另发。窗口内更新走 `--mode update` 同 URL PUT，禁止再裸 presign。
