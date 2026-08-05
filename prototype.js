(function () {
  'use strict'

  const STATE_KEY = 'proto-note:non-ecommerce-thirdparty-order:state:v1'
  const PAGE_LINKS = [
    { id: 'upload', label: '运营后台 · 文件上传', href: 'admin-upload.html' },
    { id: 'orders', label: '运营后台 · 订单管理', href: 'admin-orders.html' },
    { id: 'preview', label: '数据链路 · 三表预览', href: 'data-preview.html' },
    { id: 'consumer', label: 'C 端 · 我的购买', href: 'consumer.html' },
    { id: 'feishu', label: '飞书协作 · 渠道与未注册跟踪', href: 'feishu.html' },
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
        shopid: 'xiaobaobaba',
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
        refunded: 99,
        refundCount: 1,
        refundReason: '账期优惠差额退款',
        status: '部分退款',
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
    channel: {
      label: '渠道关系错误',
      fileName: '小宝爸爸_davdian_关系错误.xlsx',
      frontendError: 'Excel 渠道“小宝爸爸 / davdian”与渠道注册表不符',
    },
    multiFrontend: {
      label: '多项实时错误',
      fileName: '多项实时校验错误.xlsx',
      frontendErrors: [
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
          field: '商品数量',
          reason: '商品数量必须为 1',
        },
        {
          sheet: '支付成功订单表',
          row: '第 5 行',
          field: '渠道名称 / shopid',
          reason: '小宝爸爸 / davdian 与渠道注册表不匹配',
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
        shopid: 'xiaobaobaba',
        prepaid: true,
        commissionRule: '',
        commissionRate: null,
        status: '已生效',
        noticeStatus: '已周知',
      },
      {
        channelName: '大V店',
        shopid: 'davdian',
        prepaid: false,
        commissionRule: '',
        commissionRate: null,
        status: '已生效',
        noticeStatus: '已周知',
      },
      {
        channelName: '万物心选',
        shopid: 'wanwuxinxuan',
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
        shopid: 'xiaobaobaba',
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
        refunded: 400,
        refundCount: 2,
        refundReason: '两次部分退款',
        status: '部分退款',
        shipment: '无需发货',
        rights: '权益已发放',
        createdAt: '2026-07-31 11:02:18',
        activatedAt: '2026-07-31 11:02:40',
      },
      {
        id: 'davdian20260731102',
        channelName: '大V店',
        shopid: 'davdian',
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
        refunded: 0,
        refundCount: 0,
        refundReason: '',
        status: '已支付',
        shipment: '待发货',
        rights: '权益已发放',
        createdAt: '2026-07-31 17:18:42',
        activatedAt: '2026-07-31 17:19:10',
      },
      {
        id: 'wanwuxinxuan20260731103',
        channelName: '万物心选',
        shopid: 'wanwuxinxuan',
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
        refunded: 0,
        refundCount: 0,
        refundReason: '',
        status: '已支付',
        shipment: '无需发货',
        rights: '待注册后发放',
        createdAt: '2026-07-30 18:42:05',
        activatedAt: '',
      },
      {
        id: 'xiaobaobaba20260730100',
        channelName: '小宝爸爸',
        shopid: 'xiaobaobaba',
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
        refunded: 498,
        refundCount: 1,
        refundReason: '用户申请全额退款',
        status: '退款成功',
        shipment: '无需发货',
        rights: '权益已收回',
        createdAt: '2026-07-30 17:12:26',
        activatedAt: '2026-07-30 17:12:48',
      },
      {
        id: 'wanwuxinxuan20260729099',
        channelName: '万物心选',
        shopid: 'wanwuxinxuan',
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
        refunded: 699,
        refundCount: 1,
        refundReason: '未注册用户申请退款',
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
        shopid: 'wanwuxinxuan',
        phone: '13800138003',
        product: '洋葱数学思维进阶课',
        orderTime: '2026-07-30 18:42:05',
        registered: false,
        accountId: '',
        orderStatus: '已支付',
        processResult: '待处理',
      },
      {
        id: 'track-002',
        orderId: 'wanwuxinxuan20260729099',
        channelName: '万物心选',
        shopid: 'wanwuxinxuan',
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
    return {
      quantity: 1,
      accountId: order.registered ? `YC${String(order.phone || '').slice(-6)}` : '',
      refundReason: order.refunded ? '历史退款' : '',
      activatedAt: order.registered ? order.createdAt : '',
      ...order,
      ...addressParts,
    }
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
      orders: value.orders.map(normalizeOrder),
      channels: value.channels.map((item) => ({
        prepaid: false,
        commissionRule: '',
        commissionRate: null,
        status: '已生效',
        noticeStatus: '已周知',
        ...(fixture.channels.find((channel) => channel.shopid === item.shopid) || {}),
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
        orderStatus: order ? order.status : '已支付',
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
        shopid: order.shopid,
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
    downloadCsv,
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
