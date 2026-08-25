# SDD · 通用三方双 Tab 与时区统一

## 待定问题

无（本次产出均已基于明确输入，无待确认项）。

| 相关文档 | 链接 |
|---|---|
| 需求评审包 | [外网评审包](https://pessimistcamellia.github.io/non-ecommerce-thirdparty-order-prototype/general-thirdparty-tabs-timezone/review-package.html) |
| 需求说明 | [需求说明 · 通用三方双 Tab 与时区统一](__REQUIREMENT_URL__) |
| 高保真原型 | [外网高保真原型](https://pessimistcamellia.github.io/non-ecommerce-thirdparty-order-prototype/general-thirdparty-tabs-timezone/prototype.html) |
| 需求标签 | 通用三方 · 双 Tab · 非电商平台 · created_at · Asia/Shanghai · UTC ISO · 导出 |

## 设计原则
1. 页面展示与运营输入统一为 `Asia/Shanghai`。
2. 网络请求统一传 UTC ISO，后端按 `thirdpart_general_order.created_at` 过滤。
3. `pay_time` 不得冒充 `created_at`；保留时必须明确列名并转换时区。
4. 电商与非电商查询条件、结果集合按 Tab 隔离。

## FR-1 平台双 Tab 与查询隔离
| ID | EARS 需求 |
|---|---|
| FR-1.1 | 当运营打开通用三方页面时，系统应默认选中「电商平台」Tab 并只展示电商平台订单。 |
| FR-1.2 | 当运营切换至「非电商平台」Tab 时，系统应只展示非电商平台订单，并将第三方平台锁定为「非电商平台的三方订单」。 |
| FR-1.3 | 当处于非电商 Tab 时，系统应将店铺 ID/名称文案展示为渠道 ID/名称；底层可继续复用现有 shop 字段。 |

## FR-2 时间筛选与展示统一
| ID | EARS 需求 |
|---|---|
| FR-2.1 | 当运营选择订单创建时间时，前端应按 `Asia/Shanghai` 解释起止值，并在请求边界转换为 UTC ISO。 |
| FR-2.2 | 当后端收到时间范围时，应使用该范围过滤 `thirdpart_general_order.created_at`。 |
| FR-2.3 | 当列表展示订单主时间时，系统应显示列名「订单创建时间」，并将 `created_at` 格式化为 `Asia/Shanghai`。 |
| FR-2.4 | 若列表仍展示 `pay_time`，则系统应将列名明确为「支付时间」，并格式化为 `Asia/Shanghai`。 |

## FR-3 导出口径
| ID | EARS 需求 |
|---|---|
| FR-3.1 | 当运营发起导出时，系统应按 `created_at` 过滤，并将订单创建时间按 `Asia/Shanghai` 输出。 |
| FR-3.2 | 如果未选择单个第三方平台，系统应反馈「请选择单个第三方平台」。 |
| FR-3.3 | 如果导出时间范围超过 90 天，系统应反馈「导出时间范围不得超过 90 天」。 |

## 时间转换示例
| 页面输入 / 数据 | UTC ISO / 过滤 | 页面或导出展示 |
|---|---|---|
| `2026-08-01 00:00:00`（东八区） | `2026-07-31T16:00:00.000Z` | `2026-08-01 00:00:00` |
| `created_at=2026-08-18T07:26:42.000Z` | 按 `created_at` 命中 | `2026-08-18 15:26:42` |

## 存量与回滚
- 不迁移、不回填存量订单。
- 前端 Tab 与时间展示可独立回滚；回滚不得改变服务端以 `created_at` 过滤的口径。
- 新旧前端并存时，接口继续接受 UTC ISO。

## 测试重点
- 默认 Tab 与切换后的数据隔离。
- 非电商平台锁定、渠道文案和筛选生效。
- 东八区跨日边界转换为 UTC ISO。
- 列表、导出不再少 8 小时。
- `created_at` 与 `pay_time` 列名、字段值不混用。
