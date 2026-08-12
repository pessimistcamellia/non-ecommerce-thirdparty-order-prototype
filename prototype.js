(function () {
  'use strict'

  const STATE_KEY = 'proto-note:non-ecommerce-thirdparty-order:state:v1'
  const PAGE_LINKS = [
    { id: 'upload', label: '运营后台 · 三方数据管理', href: 'admin-upload.html' },
    { id: 'orders', label: '运营后台 · 订单管理', href: 'admin-orders.html' },
    { id: 'consumer', label: 'C 端 · 我的购买', href: 'consumer.html' },
  ]

  // 实际交付物为数据表的内容不做原型页面，直接链接真实多维表格
  const BASE_LINKS = [
    { label: '财务三表 Base', href: 'https://guanghe.feishu.cn/base/HTx5bBzkna9kOsse2stc8Zdrnqe' },
    { label: '渠道注册 Base', href: 'https://guanghe.feishu.cn/base/F0I2bV6KnaVBRzsLpwWcDa2Qnxh' },
    { label: '未注册跟踪 Base', href: 'https://guanghe.feishu.cn/base/UbRfb8m5Ua962tsiILEcvQJgn8b?table=tblW8EMJ8S8mK16U&view=vewMrq51ZI' },
  ]

  const FILE_TYPES_BY_PLATFORM = {
    天猫: [
      '天猫UV数据',
      '天猫直播订单明细',
      '天猫推广场景数据',
      '天猫专款交易明细',
      '天猫现金收支明细',
      '天猫微信支付账单',
    ],
    京东: ['京东UV数据', '京东非全站营销', '京东全站营销'],
    微店: ['微店账单'],
    PDD: ['拼多多账单'],
    抖店: ['抖店新结算单'],
    有赞: [],
    非电商平台的三方订单: ['导入订单'],
  }

  const UPLOAD_SCENARIOS = {
    normal: {
      label: '正常文件',
      fileName: '小宝爸爸_202608新增订单.xlsx',
      asyncResult: 'success',
      order: {
        id: 'xiaobaobaba20260804001',
        channelName: '小宝爸爸',
        channelId: 'xiaobaobaba',
        phone: '13800138006',
        registered: false,
        accountId: '',
        recipient: '赵晨',
        province: '上海市',
        city: '上海市',
        district: '浦东新区',
        detailAddress: '张江路 88 号',
        address: '上海市上海市浦东新区张江路 88 号',
        product: '洋葱英语年度课程',
        comboId: 'COMBO-2026-ENG',
        quantity: 1,
        paid: 899,
        listPrice: 999,
        refunded: 99,
        refundCount: 1,
        refundReason: '账期优惠差额退款',
        refunds: [
          {
            seq: 1,
            amount: 99,
            time: '2026-08-04 21:58:00',
            reasonDesc: '账期优惠差额退款（202608 账期）',
            importFile: '小宝爸爸_202608新增订单.xlsx',
            importer: 'chenxiaolei@guanghe.tv',
            recalled: false,
          },
        ],
        status: '支付成功',
        shipment: '无需发货',
        rights: '待注册后发放',
        createdAt: '2026-08-04 21:58:00',
        activatedAt: '',
      },
    },
    required: {
      label: '必填缺失',
      fileName: '支付表商品名称为空.xlsx',
      frontendError: '支付成功订单表第 2 行：商品名称为必填项',
    },
    duplicate: {
      label: '订单ID重复',
      fileName: '同文件订单ID重复.xlsx',
      frontendError: '支付成功订单表第 2、3 行：订单ID xiaobaobaba20260804002 重复',
    },
    amount: {
      label: '金额/数量错误',
      fileName: '金额数量错误.xlsx',
      frontendError: '支付成功订单表第 2 行：订单实付金额须大于 0，商品数量必须为 1',
    },
    multiFrontend: {
      label: '聚合错误',
      fileName: '全量实时校验错误.xlsx',
      frontendErrors: [
        {
          sheet: '工作簿',
          row: '—',
          field: 'sheet / 表头',
          reason: '缺少“退款订单表”，且支付成功订单表缺少“组合商品 ID”列',
        },
        {
          sheet: '支付成功订单表',
          row: '第 2 行',
          field: '商品名称',
          reason: '商品名称为必填项',
        },
        {
          sheet: '支付成功订单表',
          row: '第 2、3 行',
          field: '订单 ID',
          reason: '订单 ID xiaobaobaba20260804002 重复',
        },
        {
          sheet: '支付成功订单表',
          row: '第 4 行',
          field: '订单实付金额',
          reason: '订单实付金额必须为大于 0 的数字',
        },
        {
          sheet: '支付成功订单表',
          row: '第 5 行',
          field: '商品数量',
          reason: '商品数量必须为 1，当前值为 2',
        },
        {
          sheet: '支付成功订单表',
          row: '第 6 行',
          field: '电话号码',
          reason: '电话号码格式错误，必须为 11 位手机号',
        },
      ],
    },
    asyncProduct: {
      label: '异步商品失败',
      fileName: '组合商品不存在.xlsx',
      asyncResult: 'failed',
      asyncError: '组合商品 ID COMBO-9981 不存在',
    },
    asyncRefund: {
      label: '异步退款失败',
      fileName: '累计退款超额.xlsx',
      asyncResult: 'failed',
      asyncError: '订单 xiaobaobaba20260731101 累计退款超过可退金额',
    },
  }

  const clone = (value) => JSON.parse(JSON.stringify(value))

  const createFixture = () => ({
    version: 2,
    channels: [
      {
        channelName: '小宝爸爸',
        channelId: 'xiaobaobaba',
        prepaid: true,
        commissionRule: '',
        commissionRate: null,
        status: '已生效',
        noticeStatus: '已周知',
      },
      {
        channelName: '大V店',
        channelId: 'davdian',
        prepaid: false,
        commissionRule: '',
        commissionRate: null,
        status: '已生效',
        noticeStatus: '已周知',
      },
      {
        channelName: '万物心选',
        channelId: 'wanwuxinxuan',
        prepaid: false,
        commissionRule: '',
        commissionRate: null,
        status: '已生效',
        noticeStatus: '已周知',
      },
      {
        channelName: '圣智蓝图',
        channelId: 'shengzhilantu',
        prepaid: false,
        commissionRule: '',
        commissionRate: null,
        status: '已生效',
        noticeStatus: '已周知',
      },
    ],
    uploads: [
      {
        id: 150,
        platform: '非电商平台的三方订单',
        fileType: '导入订单',
        file: '大V店_202607结算订单.xlsx',
        time: '2026-07-31 17:18:42',
        user: 'panxingyu@guanghe.tv',
        result: 'success',
        total: 1,
        success: 1,
        failed: 0,
      },
      {
        id: 149,
        platform: '非电商平台的三方订单',
        fileType: '导入订单',
        file: '万物心选_202607订单_校验失败.xlsx',
        time: '2026-07-31 16:40:09',
        user: 'panxingyu@guanghe.tv',
        result: 'failed',
        total: 2,
        success: 0,
        failed: 2,
        errors: [
          '组合商品 ID COMBO-9981 不存在',
          '订单 xiaobaobaba20260731101 已成功导入，不可重复导入',
        ],
      },
      {
        id: 148,
        platform: '非电商平台的三方订单',
        fileType: '导入订单',
        file: '小宝爸爸_202607补单.xlsx',
        time: '2026-07-31 15:33:28',
        user: 'zhaoyiming@guanghe.tv',
        result: 'processing',
        total: 1,
        success: 0,
        failed: 0,
      },
      {
        id: 147,
        platform: '非电商平台的三方订单',
        fileType: '导入订单',
        file: '小宝爸爸_202607订单.xlsx',
        time: '2026-07-31 11:02:18',
        user: 'zhaoyiming@guanghe.tv',
        result: 'success',
        total: 1,
        success: 1,
        failed: 0,
      },
      {
        id: 146,
        platform: '非电商平台的三方订单',
        fileType: '导入订单',
        file: '万物心选_202607订单.xlsx',
        time: '2026-07-30 18:42:05',
        user: 'chenxiaolei@guanghe.tv',
        result: 'success',
        total: 1,
        success: 1,
        failed: 0,
      },
    ],
    orders: [
      {
        id: 'xiaobaobaba20260731101',
        channelName: '小宝爸爸',
        channelId: 'xiaobaobaba',
        phone: '13800138001',
        registered: true,
        accountId: 'YC138001',
        recipient: '王小满',
        province: '广东省',
        city: '深圳市',
        district: '南山区',
        detailAddress: '科技园科苑路 15 号',
        address: '广东省深圳市南山区科技园科苑路 15 号',
        product: '洋葱阅读成长组合课程',
        comboId: 'COMBO-2026-READ',
        quantity: 1,
        paid: 600,
        listPrice: 698,
        refunded: 400,
        refundCount: 2,
        refundReason: '两笔退款记录',
        refunds: [
          {
            seq: 1,
            amount: 150,
            time: '2026-08-01 10:05:00',
            reasonDesc: '用户与渠道协商退差价（202607 账期）',
            importFile: '小宝爸爸_202608账期退款.xlsx',
            importer: 'chenxiaolei@guanghe.tv',
            recalled: false,
          },
          {
            seq: 2,
            amount: 250,
            time: '2026-08-08 09:40:00',
            reasonDesc: '课程调换差额补退（202608 账期）',
            importFile: '小宝爸爸_202608账期退款二批.xlsx',
            importer: 'chenxiaolei@guanghe.tv',
            recalled: false,
          },
        ],
        status: '支付成功',
        shipment: '无需发货',
        rights: '权益已发放',
        createdAt: '2026-07-31 11:02:18',
        activatedAt: '2026-07-31 11:02:40',
      },
      {
        id: 'davdian20260731102',
        channelName: '大V店',
        channelId: 'davdian',
        phone: '13800138002',
        registered: true,
        accountId: 'YC138002',
        recipient: '陈思远',
        province: '浙江省',
        city: '杭州市',
        district: '余杭区',
        detailAddress: '文一西路 969 号',
        address: '浙江省杭州市余杭区文一西路 969 号',
        product: '洋葱科学年卡 + 实验器材礼盒',
        comboId: 'COMBO-2026-SCI',
        quantity: 1,
        paid: 6398,
        listPrice: 6398,
        refunded: 0,
        refundCount: 0,
        refundReason: '',
        status: '支付成功',
        shipment: '待发货',
        rights: '权益已发放',
        createdAt: '2026-07-31 17:18:42',
        activatedAt: '2026-07-31 17:19:10',
      },
      {
        id: 'wanwuxinxuan20260731103',
        channelName: '万物心选',
        channelId: 'wanwuxinxuan',
        phone: '13800138003',
        registered: false,
        accountId: '',
        recipient: '林秋实',
        province: '北京市',
        city: '北京市',
        district: '朝阳区',
        detailAddress: '望京东路 6 号',
        address: '北京市朝阳区望京东路 6 号',
        product: '洋葱数学思维进阶课',
        comboId: 'COMBO-2026-MATH',
        quantity: 1,
        paid: 1299,
        listPrice: 1299,
        refunded: 0,
        refundCount: 0,
        refundReason: '',
        status: '支付成功',
        shipment: '无需发货',
        rights: '待注册后发放',
        createdAt: '2026-07-30 18:42:05',
        activatedAt: '',
      },
      {
        id: 'xiaobaobaba20260730100',
        channelName: '小宝爸爸',
        channelId: 'xiaobaobaba',
        phone: '13800138005',
        registered: true,
        accountId: 'YC138005',
        recipient: '唐语桐',
        province: '四川省',
        city: '成都市',
        district: '高新区',
        detailAddress: '天府三街 199 号',
        address: '四川省成都市高新区天府三街 199 号',
        product: '小学数学同步课（12个月）',
        comboId: 'COMBO-2026-PRIMARY-MATH',
        quantity: 1,
        paid: 498,
        listPrice: 498,
        refunded: 498,
        refundCount: 1,
        refundReason: '用户申请全额退款',
        refunds: [
          {
            seq: 1,
            amount: 498,
            time: '2026-08-02 11:30:00',
            reasonDesc: '用户申请全额退款',
            importFile: '小宝爸爸_202608账期退款.xlsx',
            importer: 'chenxiaolei@guanghe.tv',
            recalled: true,
          },
        ],
        status: '退款成功',
        shipment: '无需发货',
        rights: '权益已收回',
        createdAt: '2026-07-30 17:12:26',
        activatedAt: '2026-07-30 17:12:48',
      },
      {
        id: 'wanwuxinxuan20260729099',
        channelName: '万物心选',
        channelId: 'wanwuxinxuan',
        phone: '13800138007',
        registered: false,
        accountId: '',
        recipient: '孙嘉禾',
        province: '江苏省',
        city: '南京市',
        district: '鼓楼区',
        detailAddress: '中山北路 81 号',
        address: '江苏省南京市鼓楼区中山北路 81 号',
        product: '洋葱物理启蒙课',
        comboId: 'COMBO-2026-PHYSICS',
        quantity: 1,
        paid: 699,
        listPrice: 799,
        refunded: 699,
        refundCount: 1,
        refundReason: '未注册用户申请退款',
        refunds: [
          {
            seq: 1,
            amount: 699,
            time: '2026-08-01 09:12:00',
            reasonDesc: '未注册用户申请退款',
            importFile: '万物心选_202608账期退款.xlsx',
            importer: 'chenxiaolei@guanghe.tv',
            recalled: false,
          },
        ],
        status: '退款成功',
        shipment: '无需发货',
        rights: '未发放（订单已退款）',
        createdAt: '2026-07-29 14:20:00',
        activatedAt: '',
      },
    ],
    unregistered: [
      {
        id: 'track-001',
        orderId: 'wanwuxinxuan20260731103',
        channelName: '万物心选',
        channelId: 'wanwuxinxuan',
        phone: '13800138003',
        product: '洋葱数学思维进阶课',
        orderTime: '2026-07-30 18:42:05',
        registered: false,
        accountId: '',
        orderStatus: '支付成功',
        processResult: '待处理',
      },
      {
        id: 'track-002',
        orderId: 'wanwuxinxuan20260729099',
        channelName: '万物心选',
        channelId: 'wanwuxinxuan',
        phone: '13800138007',
        product: '洋葱物理启蒙课',
        orderTime: '2026-07-29 14:20:00',
        registered: false,
        accountId: '',
        orderStatus: '退款成功',
        processResult: '已完成',
      },
    ],
    dataWarehouse: {
      status: '待推送',
      pushedAt: '',
      generatedAt: '2026-08-04 21:56:00',
      fileName: '非电商三方订单财务数据_20260804.xlsx',
    },
    notifications: [],
  })

  function normalizeOrder(order) {
    const addressParts = {
      province: order.province || '',
      city: order.city || '',
      district: order.district || '',
      detailAddress: order.detailAddress || order.address || '',
    }
    const normalized = {
      quantity: 1,
      accountId: order.registered ? `YC${String(order.phone || '').slice(-6)}` : '',
      refundReason: order.refunded ? '历史退款' : '',
      activatedAt: order.registered ? order.createdAt : '',
      ...order,
      ...addressParts,
    }
    // 洋葱订单没有“部分退款”状态：历史演示数据统一迁移为支付成功
    if (normalized.status === '部分退款' || normalized.status === '已支付') {
      normalized.status = '支付成功'
    }
    // 旧版本地状态没有逐笔退款记录：按累计金额补一条，保证订单详情退款信息区可渲染
    if (!Array.isArray(normalized.refunds)) {
      normalized.refunds = normalized.refunded > 0
        ? [{
            seq: 1,
            amount: normalized.refunded,
            time: normalized.createdAt || '',
            reasonDesc: normalized.refundReason || '历史退款',
            importFile: '',
            importer: '',
            recalled: normalized.status === '退款成功',
          }]
        : []
    }
    return normalized
  }

  function migrateState(value) {
    if (!value || !Array.isArray(value.orders) || !Array.isArray(value.uploads)) {
      return createFixture()
    }
    const fixture = createFixture()
    const state = {
      ...fixture,
      ...value,
      version: 2,
      uploads: value.uploads.map((item) => ({
        total: Number(item.success || 0) + Number(item.failed || 0) || 1,
        ...item,
      })),
      orders: value.orders.map((item) => {
        // 旧本地状态无逐笔退款记录时，优先回填内置示例数据的同单记录
        const fixtureOrder = fixture.orders.find((candidate) => candidate.id === item.id)
        if (fixtureOrder && !Array.isArray(item.refunds)) {
          return normalizeOrder({ ...item, refunds: fixtureOrder.refunds })
        }
        return normalizeOrder(item)
      }),
      channels: value.channels.map((item) => ({
        prepaid: false,
        commissionRule: '',
        commissionRate: null,
        status: '已生效',
        noticeStatus: '已周知',
        ...(fixture.channels.find((channel) => channel.channelId === item.channelId) || {}),
        ...item,
      })),
    }
    state.unregistered = (value.unregistered || []).map((item) => {
      const order = state.orders.find((candidate) => candidate.id === item.orderId)
      return {
        product: order ? order.product : '',
        orderTime: order ? order.createdAt : '',
        registered: false,
        accountId: '',
        orderStatus: order ? order.status : '支付成功',
        processResult:
          order && order.status === '退款成功' ? '已完成' : '待处理',
        ...item,
      }
    })
    fixture.orders.forEach((item) => {
      if (!state.orders.some((order) => order.id === item.id)) state.orders.push(item)
    })
    fixture.unregistered.forEach((item) => {
      if (!state.unregistered.some((track) => track.id === item.id)) state.unregistered.push(item)
    })
    return state
  }

  function loadState() {
    let state
    try {
      state = migrateState(JSON.parse(localStorage.getItem(STATE_KEY) || 'null'))
    } catch (error) {
      state = createFixture()
    }
    localStorage.setItem(STATE_KEY, JSON.stringify(state))
    return state
  }

  function saveState(nextState) {
    const state = migrateState(nextState)
    localStorage.setItem(STATE_KEY, JSON.stringify(state))
    window.dispatchEvent(
      new CustomEvent('prototype-state-change', { detail: clone(state) }),
    )
    return state
  }

  function resetState() {
    const state = createFixture()
    localStorage.setItem(STATE_KEY, JSON.stringify(state))
    window.dispatchEvent(
      new CustomEvent('prototype-state-change', { detail: clone(state) }),
    )
    notify('演示数据已重置')
    return state
  }

  function renderNav(activePage) {
    const mount = document.getElementById('prototypeNav')
    if (!mount) return
    mount.innerHTML = `<nav class="prototype-nav" aria-label="原型导航">
      <span class="prototype-nav__brand">非电商三方订单原型</span>
      ${PAGE_LINKS.map(
        (page) =>
          `<a class="${activePage === page.id ? 'is-active' : ''}" href="${page.href}">${page.label}</a>`,
      ).join('')}
      ${BASE_LINKS.map(
        (item) =>
          `<a class="prototype-nav__external" href="${item.href}" target="_blank" rel="noopener">${item.label} ↗</a>`,
      ).join('')}
      <button class="prototype-nav__reset" type="button">重置演示数据</button>
    </nav>`
    mount.querySelector('button').addEventListener('click', resetState)
  }

  function notify(message, type) {
    const old = document.querySelector('.prototype-toast')
    if (old) old.remove()
    const element = document.createElement('div')
    element.className = `prototype-toast prototype-toast--${type || 'info'}`
    element.setAttribute('role', 'status')
    element.textContent = message
    document.body.appendChild(element)
    setTimeout(() => element.remove(), 2600)
  }

  function addOrderFromScenario(state, scenario) {
    if (!scenario.order || state.orders.some((item) => item.id === scenario.order.id)) {
      return
    }
    const order = clone(scenario.order)
    state.orders.unshift(order)
    if (!order.registered) {
      state.unregistered.unshift({
        id: `track-${order.id}`,
        orderId: order.id,
        channelName: order.channelName,
        channelId: order.channelId,
        phone: order.phone,
        product: order.product,
        orderTime: order.createdAt,
        registered: false,
        accountId: '',
        orderStatus: order.status,
        processResult: order.status === '退款成功' ? '已完成' : '待处理',
      })
    }
    state.dataWarehouse.generatedAt = order.createdAt
    state.dataWarehouse.fileName = `非电商三方订单财务数据_${order.createdAt.slice(0, 10).replaceAll('-', '')}.xlsx`
    state.dataWarehouse.status = '待推送'
    state.dataWarehouse.pushedAt = ''
  }

  const formatMoney = (value) =>
    Number(value || 0).toLocaleString('zh-CN', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    })

  const maskPhone = (phone) =>
    String(phone || '').replace(/^(\d{3})\d{4}(\d{4})$/, '$1****$2')

  // 非电商三方订单导入模板（真实 .xlsx，双 sheet：支付成功订单表 + 退款订单表，各含一行示例）
  const TEMPLATE_XLSX_B64 =
    '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'

  function downloadXlsxTemplate(fileName) {
    const bytes = Uint8Array.from(atob(TEMPLATE_XLSX_B64), (ch) => ch.charCodeAt(0))
    const blob = new Blob([bytes], {
      type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    })
    const link = document.createElement('a')
    link.href = URL.createObjectURL(blob)
    link.download = fileName
    document.body.appendChild(link)
    link.click()
    link.remove()
    setTimeout(() => URL.revokeObjectURL(link.href), 500)
  }

  function downloadCsv(fileName, content) {
    const blob = new Blob([`\uFEFF${content}`], {
      type: 'text/csv;charset=utf-8',
    })
    const link = document.createElement('a')
    link.href = URL.createObjectURL(blob)
    link.download = fileName
    document.body.appendChild(link)
    link.click()
    link.remove()
    setTimeout(() => URL.revokeObjectURL(link.href), 500)
  }

  window.PrototypeApp = {
    STATE_KEY,
    FILE_TYPES_BY_PLATFORM,
    PAGE_LINKS,
    UPLOAD_SCENARIOS,
    addOrderFromScenario,
    clone,
    createFixture,
    TEMPLATE_XLSX_B64,
    downloadCsv,
    downloadXlsxTemplate,
    formatMoney,
    getState: loadState,
    maskPhone,
    notify,
    renderNav,
    resetState,
    saveState,
  }

  window.addEventListener('storage', (event) => {
    if (event.key === STATE_KEY) {
      window.dispatchEvent(
        new CustomEvent('prototype-state-change', { detail: loadState() }),
      )
    }
  })
})()
