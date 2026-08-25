from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
ENGINE = Path("/Users/zhuchuming/.cursor/skills/proto-note/assets/diff-annotator.js").read_text()
REVIEW_TEMPLATE = Path("/Users/zhuchuming/.cursor/skills/review-package/template.html").read_text()

PROTOTYPE_URL = "https://pessimistcamellia.github.io/non-ecommerce-thirdparty-order-prototype/general-thirdparty-tabs-timezone/prototype.html"
PACKAGE_URL = "https://pessimistcamellia.github.io/non-ecommerce-thirdparty-order-prototype/general-thirdparty-tabs-timezone/review-package.html"
REQ_URL = "https://guanghe.feishu.cn/docx/Lpn2d8rjCo48VzxcT8lcWgUJn3e"
SDD_URL = "https://guanghe.feishu.cn/docx/KHQfdClRjo5vnaxWTGjcdVJ3nS4"


prototype = r"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>运营后台 · 通用三方</title>
<style>
*{box-sizing:border-box}html,body{margin:0;min-width:1540px;background:#f5f6f7;color:#606266;font:13px/1.5 -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif}
button,input,select{font:inherit}.shell{display:flex;width:1520px;min-height:100vh;background:#fff}.sidebar{width:168px;flex:none;background:#071a2c;color:#c8d2e1}.brand{height:54px;display:flex;align-items:center;padding:0 12px;color:#fff;font-size:15px;font-weight:650;border-bottom:1px solid rgba(255,255,255,.08)}.side-group{padding:13px 14px 7px;color:#718197;font-size:12px}.side-item{height:40px;display:flex;align-items:center;padding:0 18px;color:#c8d2e1;text-decoration:none}.side-item.active{color:#fff;background:#1687e9}.main{width:1352px;padding:0 18px 40px;overflow:hidden}.breadcrumb{height:50px;display:flex;align-items:center;color:#8f959e;border-bottom:1px solid #edf0f3;font-size:12px}
.tabs{display:flex;gap:28px;height:52px;align-items:flex-end;border-bottom:1px solid #e8ebef}.tab{position:relative;height:52px;padding:0 2px 13px;border:0;background:transparent;color:#606266;cursor:pointer;font-weight:500}.tab:hover,.tab.active{color:#1687e9}.tab.active{font-weight:600}.tab.active:after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:2px;background:#1687e9}
.filters{padding:18px 10px 4px}.filter-row{display:flex;align-items:flex-end;gap:16px;margin-bottom:14px}.field{display:flex;flex-direction:column;gap:6px}.field label{color:#606266}.field.required label:before{content:"*";color:#f56c6c;margin-right:3px}.input,.select{height:32px;width:126px;padding:0 10px;border:1px solid #dcdfe6;border-radius:3px;background:#fff;color:#606266}.input.wide{width:238px}.input.time{width:310px}.select:disabled{color:#606266;background:#f5f7fa;cursor:not-allowed}.actions{display:flex;align-items:center;gap:10px}.btn{height:32px;padding:0 18px;border:1px solid #dcdfe6;border-radius:3px;background:#fff;color:#606266;cursor:pointer}.btn.primary{border-color:#409eff;background:#409eff;color:#fff}.btn:hover{opacity:.88}.export-note{color:#909399;font-size:12px}.request-preview{margin:0 10px 14px;padding:9px 12px;border:1px solid #d9ecff;border-radius:4px;background:#f4faff;color:#606266}.request-preview b{color:#3370ff}.request-preview code{color:#4e5969;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.table-wrap{width:100%;overflow-x:auto;border-top:1px solid #f0f1f3}.table{width:1840px;border-collapse:collapse;table-layout:fixed}.table th,.table td{padding:11px 9px;border-bottom:1px solid #ebeef5;text-align:left;vertical-align:middle;font-size:13px}.table th{height:48px;color:#7a8495;background:#fff;font-weight:600}.table tbody tr:hover td{background:#f7faff}.mono{font-variant-numeric:tabular-nums;word-break:break-all}.money{font-variant-numeric:tabular-nums}.link{border:0;background:transparent;color:#1687e9;cursor:pointer}.pagination{display:flex;justify-content:flex-end;gap:8px;align-items:center;padding-top:16px;color:#909399}.page{min-width:30px;height:28px;border:1px solid #1687e9;border-radius:3px;background:#1687e9;color:#fff}.toast{position:fixed;left:50%;top:22px;z-index:10000;transform:translateX(-50%);padding:10px 18px;border-radius:4px;background:#303133;color:#fff;opacity:0;pointer-events:none;transition:.2s}.toast.show{opacity:.94}.empty{display:none;padding:70px;text-align:center;color:#a2a9b3}
</style>
</head>
<body>
<main id="generalThirdpartyPage" class="shell" data-diff-page="运营后台 · 通用三方">
  <aside class="sidebar">
    <div class="brand">洋葱学园APP运营平台</div>
    <div class="side-group">微信生态</div><a class="side-item">微信公众号</a>
    <div class="side-group">App配置</div><a class="side-item">版本管理</a>
    <div class="side-group">学生运营</div><a class="side-item">用户管理</a>
    <div class="side-group">渠道投放</div><a class="side-item">检测链接</a>
    <div class="side-group">三方订单管理</div>
    <a class="side-item">微店</a><a class="side-item">抖店</a><a class="side-item active">通用三方</a><a class="side-item">掉单管理</a><a class="side-item">三方数据管理</a>
  </aside>
  <section class="main">
    <div class="breadcrumb">渠道投放&nbsp; / &nbsp;通用三方</div>
    <div id="platformTabs" class="tabs" role="tablist">
      <button class="tab active" data-tab="ecommerce" role="tab" aria-selected="true">电商平台</button>
      <button class="tab" data-tab="non-ecommerce" role="tab" aria-selected="false">非电商平台</button>
    </div>
    <section id="filterArea" class="filters">
      <div class="filter-row">
        <div class="field"><label>第三方平台</label><select id="platform" class="select"></select></div>
        <div class="field"><label id="channelIdLabel">店铺ID</label><input id="channelId" class="input" placeholder="请输入店铺id"></div>
        <div class="field"><label id="channelNameLabel">店铺名称</label><input id="channelName" class="input" placeholder="请输入店铺名称"></div>
        <div id="createdAtFilter" class="field required"><label>订单创建时间</label><input id="createdRange" class="input time" value="2026-08-01 00:00:00 至 2026-08-25 23:59:59" readonly></div>
      </div>
      <div class="filter-row">
        <div class="field"><label>父订单ID</label><input id="parentId" class="input" placeholder="请输入父订单id"></div>
        <div class="field"><label>洋葱商品名称</label><input id="goodsName" class="input" placeholder="请输入洋葱商品名称"></div>
        <div class="field"><label>洋葱商品ID</label><input id="goodsId" class="input" placeholder="请输入商品ID"></div>
        <div class="field"><label>洋葱用户ID</label><input id="userId" class="input" placeholder="请输入userid"></div>
        <div class="field"><label>退款状态</label><select id="refundStatus" class="select"><option value="">请选择退款状态</option><option>未退款</option><option>退款成功</option></select></div>
      </div>
      <div class="filter-row">
        <div class="actions"><button id="query" class="btn primary">查询</button><button id="clear" class="btn">清空</button><button id="export" class="btn primary">导出</button></div>
        <span class="export-note">导出需指定单个第三方平台，且时间范围不得超过 90 天</span>
      </div>
    </section>
    <div id="utcPreview" class="request-preview"><b>时间口径演示：</b>页面按 Asia/Shanghai 选择与展示；请求转换为 UTC ISO：
      <code>2026-07-31T16:00:00.000Z ~ 2026-08-25T15:59:59.000Z</code>；后端过滤 <code>thirdpart_general_order.created_at</code>。
    </div>
    <div id="orderTable" class="table-wrap">
      <table class="table">
        <colgroup><col style="width:160px"><col style="width:170px"><col style="width:150px"><col style="width:90px"><col style="width:90px"><col style="width:140px"><col style="width:110px"><col style="width:160px"><col style="width:155px"><col style="width:90px"><col style="width:100px"><col style="width:90px"><col style="width:90px"><col style="width:80px"></colgroup>
        <thead><tr><th>yc商品名称</th><th>yc订单ID</th><th>yc商品ID</th><th>yc订单实付金额</th><th>yc退款金额</th><th>yc用户ID</th><th>yc订单状态</th><th>父订单ID</th><th id="createdAtColumn">订单创建时间</th><th>支付金额</th><th>订单状态</th><th>退款金额</th><th id="channelColumn">店铺名称</th><th>操作</th></tr></thead>
        <tbody id="rows"></tbody>
      </table>
      <div id="empty" class="empty">暂无符合条件的订单</div>
    </div>
    <div class="pagination"><span id="total">共 0 条</span><button class="page">1</button><span>20 条/页</span></div>
  </section>
</main>
<div id="toast" class="toast"></div>
<script>
(() => {
const ecommerce=[
 {platform:'天猫',channelId:'499187844',channel:'洋葱学园旗舰店',goods:'小学数学同步课（12个月）',ycOrder:'6a8d127aab9c6ed83993a568',goodsId:'96cb56d2-8188-4cdf-863f-cb87939d246f',ycPaid:498,ycRefund:0,user:'668f51e82f81630001ce1c04',ycStatus:'支付成功',parent:'33163662390442438751',createdAt:'2026-08-25 11:56:40',paid:498,status:'支付成功',refund:0},
 {platform:'小红书',channelId:'redbook-onion',channel:'洋葱学园课程店',goods:'7天全科同步课',ycOrder:'6a8d0fd68f333997f07474e3',goodsId:'4bfc6d78-f959-46b6-a6c5-7fddb9ca3b7d',ycPaid:19.9,ycRefund:0,user:'6690f21c3826f10001f32db9',ycStatus:'支付成功',parent:'P803181507530099321',createdAt:'2026-08-25 11:45:20',paid:19.9,status:'支付成功',refund:0},
 {platform:'抖店',channelId:'douyin-yc',channel:'洋葱学园官方店',goods:'初中物理实验成长包',ycOrder:'6a8cfa206583dcd971268af2',goodsId:'2d331ea1-940c-4ebf-a390-721db0148850',ycPaid:299,ycRefund:299,user:'668d12f8da2b970001ce3cc9',ycStatus:'退款成功',parent:'DOU2026082400928',createdAt:'2026-08-24 20:08:11',paid:299,status:'退款成功',refund:299}
];
const nonEcommerce=[
 {platform:'非电商平台的三方订单',channelId:'xiaobaobaba',channel:'小宝爸爸',goods:'洋葱数学思维年度组合课',ycOrder:'6a910712f4ea593f142cc001',goodsId:'COMBO-2026-MATH',ycPaid:899,ycRefund:0,user:'6691aa7017a25e0001c055a8',ycStatus:'支付成功',parent:'xiaobaobaba20260818001',createdAt:'2026-08-18 15:26:42',paid:899,status:'支付成功',refund:0},
 {platform:'非电商平台的三方订单',channelId:'davdian',channel:'大V店',goods:'洋葱英语全年成长课',ycOrder:'6a910742178ab591cdf10122',goodsId:'COMBO-2026-ENGLISH',ycPaid:699,ycRefund:0,user:'6691aba336ad770001b93a12',ycStatus:'支付成功',parent:'davdian20260818002',createdAt:'2026-08-18 15:42:08',paid:699,status:'支付成功',refund:0},
 {platform:'非电商平台的三方订单',channelId:'wanwuxinxuan',channel:'万物心选',goods:'洋葱物理实验成长包',ycOrder:'6a91078dcf01b993dd520163',goodsId:'COMBO-2026-PHYSICS',ycPaid:498,ycRefund:198,user:'6691ac1dd4f6830001c18b0a',ycStatus:'支付成功',parent:'wanwuxinxuan20260818003',createdAt:'2026-08-18 16:06:31',paid:498,status:'支付成功',refund:198}
];
let tab='ecommerce';
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
function toast(text){$('#toast').textContent=text;$('#toast').classList.add('show');setTimeout(()=>$('#toast').classList.remove('show'),2200)}
function setup(){
 const non=tab==='non-ecommerce';
 $('#platform').innerHTML=(non?['非电商平台的三方订单']:['','天猫','小红书','抖店']).map(v=>`<option value="${v}">${v||'请选择'}</option>`).join('');
 $('#platform').value=non?'非电商平台的三方订单':'';$('#platform').disabled=non;
 $('#channelIdLabel').textContent=non?'渠道ID':'店铺ID';$('#channelNameLabel').textContent=non?'渠道名称':'店铺名称';$('#channelColumn').textContent=non?'渠道名称':'店铺名称';
 $('#channelId').placeholder=non?'请输入渠道ID':'请输入店铺id';$('#channelName').placeholder=non?'请输入渠道名称':'请输入店铺名称';
}
function data(){
 let rows=tab==='ecommerce'?ecommerce:nonEcommerce;
 const f={p:$('#platform').value,id:$('#channelId').value.trim(),name:$('#channelName').value.trim(),parent:$('#parentId').value.trim(),goods:$('#goodsName').value.trim(),goodsId:$('#goodsId').value.trim(),user:$('#userId').value.trim(),refund:$('#refundStatus').value};
 return rows.filter(r=>(!f.p||r.platform===f.p)&&(!f.id||r.channelId.includes(f.id))&&(!f.name||r.channel.includes(f.name))&&(!f.parent||r.parent.includes(f.parent))&&(!f.goods||r.goods.includes(f.goods))&&(!f.goodsId||r.goodsId.includes(f.goodsId))&&(!f.user||r.user.includes(f.user))&&(!f.refund||(f.refund==='退款成功'?r.refund>0:r.refund===0)));
}
function render(){
 const rows=data();$('#rows').innerHTML=rows.map(r=>`<tr><td>${r.goods}</td><td class="mono">${r.ycOrder}</td><td class="mono">${r.goodsId}</td><td class="money">${r.ycPaid}</td><td class="money">${r.ycRefund}</td><td class="mono">${r.user}</td><td>${r.ycStatus}</td><td class="mono">${r.parent}</td><td class="mono">${r.createdAt}</td><td class="money">${r.paid}</td><td>${r.status}</td><td class="money">${r.refund}</td><td>${r.channel}</td><td><button class="link">激活课程</button></td></tr>`).join('');
 $('#empty').style.display=rows.length?'none':'block';$('#orderTable table').style.display=rows.length?'table':'none';$('#total').textContent=`共 ${rows.length} 条`;
}
function switchTab(next){tab=next;$$('.tab').forEach(b=>{const on=b.dataset.tab===next;b.classList.toggle('active',on);b.setAttribute('aria-selected',on)});clear(false);setup();render()}
function clear(doRender=true){['channelId','channelName','parentId','goodsName','goodsId','userId'].forEach(id=>$('#'+id).value='');$('#refundStatus').value='';if(doRender)render()}
$$('.tab').forEach(b=>b.addEventListener('click',()=>switchTab(b.dataset.tab)));$('#query').addEventListener('click',()=>{render();toast('已按订单创建时间（东八区）查询')});$('#clear').addEventListener('click',()=>{clear();setup()});$('#export').addEventListener('click',()=>{if(!$('#platform').value)return toast('请选择单个第三方平台');toast('导出任务已创建：created_at 与全部时间按东八区输出')});
setup();render();
window.DIFF_HOOKS={locate(pageId){if(pageId==='generalThirdpartyPage'){}},setDemoState(controlId,value){if(controlId==='platformView')switchTab(value)}};
})();
</script>
<script>
window.DIFF_CHANGESET={meta:{sddTitle:'SDD · 通用三方双 Tab 与时区统一',sddUrl:'__SDD_URL__',sddType:'feishu',demoControls:[{id:'platformView',label:'平台数据分区',default:'ecommerce',options:[{value:'ecommerce',label:'电商平台'},{value:'non-ecommerce',label:'非电商平台'}]}]},changes:[
{id:'chg-general-tabs',level:'module',page:'generalThirdpartyPage',module:'平台分类',target:'#platformTabs',type:'new',title:'新增电商与非电商双 Tab',desc:'通用三方按平台类型隔离，默认进入电商平台，交互与掉单管理一致。',before:'线上通用三方无平台类型 Tab',after:'默认电商平台 Tab + 非电商平台 Tab',examples:[{case:'默认进入',input:'打开通用三方',result:'展示电商平台订单'},{case:'切换',input:'点击非电商平台',result:'只展示非电商平台订单'}],sdd:{section:'FR-1 平台双 Tab 与查询隔离'}},
{id:'chg-general-scope',level:'module',page:'generalThirdpartyPage',module:'非电商数据分区',target:'#filterArea',type:'logic',title:'非电商数据独立查询与展示',desc:'非电商 Tab 锁定第三方平台并将店铺文案改为渠道 ID/名称；两类数据不可串查。',before:'线上只有电商三方数据列表',after:'非电商数据进入独立 Tab，平台值不可修改',examples:[{case:'渠道筛选',input:'非电商平台；渠道ID=xiaobaobaba',result:'只展示小宝爸爸订单'},{case:'切回电商',input:'点击电商平台',result:'恢复电商平台筛选和数据'}],sdd:{section:'FR-1 平台双 Tab 与查询隔离'}},
{id:'chg-created-at-display',level:'field',page:'generalThirdpartyPage',module:'时间展示',target:'#createdAtColumn',type:'enum',title:'列表展示 created_at 东八区时间',desc:'列表主时间列为订单创建时间，与筛选字段一致，按 Asia/Shanghai 格式化。',before:'列表把 pay_time 按 UTC 墙钟原样展示，时间少 8 小时',after:'列名为订单创建时间，展示 created_at 的东八区时间',examples:[{case:'创建时间',input:'created_at=2026-08-18T07:26:42.000Z',result:'展示 2026-08-18 15:26:42'}],sdd:{section:'FR-2 时间筛选与展示统一'}},
{id:'chg-created-at-filter',level:'field',page:'generalThirdpartyPage',module:'时间展示',target:'#createdAtFilter',type:'logic',title:'筛选按东八区选择 created_at',desc:'运营选择的时间范围按 Asia/Shanghai 解释，后端按该范围过滤 created_at。',before:'筛选时区与列表展示口径不一致',after:'筛选、过滤、列表展示使用同一 created_at 字段和东八区口径',sdd:{section:'FR-2 时间筛选与展示统一'}},
{id:'chg-request-utc',level:'module',page:'generalThirdpartyPage',module:'请求转换',target:'#utcPreview',type:'flow',title:'请求边界转换为 UTC ISO',desc:'前端把东八区起止时间转换为 UTC ISO 后发给后端，不改变运营输入与展示时区。',before:'时间转换链路未统一，UTC 墙钟值被直接展示',after:'页面东八区 ↔ 请求 UTC ISO ↔ created_at 过滤',examples:[{case:'开始时间',input:'2026-08-01 00:00:00 Asia/Shanghai',result:'2026-07-31T16:00:00.000Z'},{case:'结束时间',input:'2026-08-25 23:59:59 Asia/Shanghai',result:'2026-08-25T15:59:59.000Z'}],sdd:{section:'FR-2 时间筛选与展示统一'}},
{id:'chg-export-timezone',level:'module',page:'generalThirdpartyPage',module:'导出',target:'#export',type:'logic',title:'导出时间统一为东八区',desc:'导出按 created_at 过滤，订单创建时间按 Asia/Shanghai 输出；保留现有单平台与 90 天限制。',before:'导出 pay_time 按 UTC 墙钟原样展示',after:'导出筛选与时间列均使用 created_at 东八区口径',sdd:{section:'FR-3 导出口径'}}
]};
</script>
<script>
__ENGINE__
</script>
</body></html>""".replace("__ENGINE__", ENGINE).replace("__SDD_URL__", SDD_URL).replace(
    "sdd:{section:'FR-1 平台双 Tab 与查询隔离'}",
    "sdd:{section:'FR-1 平台双 Tab 与查询隔离',blockId:'doxcn2Uj6WHQONJPYKyDv0Bahje'}",
).replace(
    "sdd:{section:'FR-2 时间筛选与展示统一'}",
    "sdd:{section:'FR-2 时间筛选与展示统一',blockId:'doxcnE78JECH5jhfUex8syoEm7Z'}",
).replace(
    "sdd:{section:'FR-3 导出口径'}",
    "sdd:{section:'FR-3 导出口径',blockId:'doxcnEMxRdr51C56ZZuXkAyMEDe'}",
)


package = r"""<!doctype html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>通用三方双 Tab 与时区统一 · 评审包</title>
<style>
:root{--bg:#f5f6f8;--card:#fff;--ink:#1f2329;--ink2:#51565d;--ink3:#8f959e;--line:#e3e5e8;--accent:#3370ff;--green:#2ea44f;--amber:#b8860b}
*{box-sizing:border-box;margin:0;padding:0}body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--ink);font-size:15px;line-height:1.65}.wrap{max-width:1180px;margin:auto;padding:24px 20px 80px}header{padding:26px 0 16px}h1{font-size:23px}.sub{color:var(--ink2);margin-top:6px}.meta{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}.chip{padding:2px 10px;border:1px solid var(--line);border-radius:999px;background:#fff;color:var(--ink2);font-size:13px}nav{display:flex;gap:4px;border-bottom:2px solid var(--line);margin:14px 0 22px;position:sticky;top:0;background:var(--bg);z-index:9;padding-top:8px}nav button{border:0;background:none;padding:10px 14px;font-size:15px;color:var(--ink2);cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-2px;font-weight:500}nav button.on{color:var(--accent);border-bottom-color:var(--accent);font-weight:600}.tab{display:none}.tab.on{display:block}.card{background:#fff;border:1px solid var(--line);border-radius:10px;padding:18px 20px;margin-bottom:16px}.card h3{font-size:16px;margin-bottom:10px}.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}ul,ol{padding-left:20px}table{width:100%;border-collapse:collapse;font-size:14px;margin-bottom:18px}th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}th{background:#fafbfc;color:var(--ink2)}a{color:var(--accent)}.note{color:var(--ink3);font-size:13px}.iframe-card{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px}.iframe-card iframe{display:block;width:100%;height:720px;border:1px solid var(--line);border-radius:6px}.pill{display:inline-block;padding:1px 7px;border-radius:4px;background:#eef3ff;color:#1a56db;font-size:12px}.dm-h{font-size:16px;font-weight:700;margin:24px 0 8px}.dm-row{display:flex;gap:8px;padding:9px 0;border-bottom:1px solid var(--line)}.dm-add{display:flex;gap:8px;margin-top:10px}.dm-add input{flex:1;padding:8px;border:1px solid var(--line);border-radius:6px}.dm-add button,.export-btn{border:0;background:var(--accent);color:#fff;border-radius:6px;padding:8px 16px;cursor:pointer}.export-btn{position:fixed;right:20px;top:14px;z-index:20;background:#fff;color:var(--ink2);border:1px solid var(--line)}
@media(max-width:880px){.grid2{grid-template-columns:1fr}}
</style></head><body><button class="export-btn" id="exportHtml">导出 HTML</button><div class="wrap">
<header><h1>通用三方双 Tab 与时区统一 · 评审包</h1><div class="sub">高保真原型呈现通用三方页的平台数据分区、查询筛选、created_at 时间展示与 UTC 请求转换。</div><div class="meta"><span class="chip">需求类型：界面 · 中后台</span><span class="chip">通用三方</span><span class="chip">双 Tab</span><span class="chip">非电商平台</span><span class="chip">created_at</span><span class="chip">Asia/Shanghai</span><span class="chip">UTC ISO</span><span class="chip">导出</span></div></header>
<nav id="nav"><button class="on" data-tab="intro">① 简介</button><button data-tab="changes">② 变更清单</button><button data-tab="rules">③ 字段与时间规则</button><button data-tab="prototype">④ 高保真交互原型</button><button data-tab="decisions">⑤ 决策事项</button></nav>
<section id="intro" class="tab on">
<div class="grid2"><div class="card"><h3>背景与问题</h3><ul><li><b>页面无平台类型分区：</b>通用三方现有电商数据与已 ready 的非电商数据缺少前端隔离入口。</li><li><b>查询与展示字段错位：</b>筛选按订单创建时间，列表和导出却以 pay_time 充当主时间列。</li><li><b>时区少 8 小时：</b>列表和导出把 UTC 墙钟值原样展示，未转换回东八区。</li></ul></div><div class="card"><h3>目标</h3><ol><li>默认电商平台 Tab，非电商订单只在非电商平台 Tab 展示，两类数据查询结果互不串行。</li><li>筛选、后端过滤、列表与导出统一使用 created_at；运营输入和输出均为东八区。</li><li>请求边界统一转换为 UTC ISO，示例可在原型中复现。</li></ol></div></div>
<div class="grid2"><div class="card"><h3>范围 · 要做什么</h3><ul><li>新增「电商平台 / 非电商平台」双 Tab，视觉与掉单管理一致。</li><li>非电商 Tab 锁定第三方平台，店铺文案改为渠道 ID/名称。</li><li>列表主时间列改为订单创建时间，展示 created_at 东八区时间。</li><li>查询请求转 UTC ISO；导出按 created_at 过滤并按东八区展示。</li></ul></div><div class="card"><h3>范围 · 不做什么</h3><ul><li>不展开 Excel 导入、掉单 Base、10MB 文件限制、上传渠道必填弹窗。</li><li>不改变现有导出的单平台与 90 天限制，只明确反馈文案。</li><li>本页截图无主播、预售、买家留言、数量列，因此不新增也不专门隐藏这些列。</li></ul></div></div>
<div class="card"><h3>相关文档</h3><table><tr><th>文档</th><th>链接</th></tr><tr><td>需求说明</td><td><a href="__REQUIREMENT_URL__" target="_blank">需求说明 · 通用三方双 Tab 与时区统一</a></td></tr><tr><td>SDD</td><td><a href="__SDD_URL__" target="_blank">SDD · 通用三方双 Tab 与时区统一</a></td></tr><tr><td>高保真原型</td><td><a href="__PROTOTYPE_URL__" target="_blank">外网原型</a></td></tr></table></div>
</section>
<section id="changes" class="tab"><h3>行为变更</h3><table><tr><th>序号</th><th>位置（端 · 平台 · 页面）</th><th>优先级</th><th>变更内容</th><th>开发团队</th></tr>
<tr><td>1</td><td>运营后台 · 通用三方列表</td><td>P0 / P1</td><td><b>1-1 P0 【新增】</b>双 Tab：电商平台默认、非电商平台独立展示。<br><b>1-2 P1 【变更】</b>非电商 Tab 锁定平台，店铺 ID/名称改为渠道 ID/名称。<br><b>1-3 P1 【变更】</b>查询按 Tab 隔离数据源，清空和切换不得串数据。</td><td></td></tr>
<tr><td>2</td><td>运营后台 · 通用三方列表</td><td>P0 / P1</td><td><b>2-2 P1 【变更】</b>查询条件里的订单创建时间，与查询结果的列表保持数据一致</td><td></td></tr></table></section>
<section id="rules" class="tab"><div class="card"><h3>字段口径</h3><table><tr><th>页面位置</th><th>字段</th><th>读取 / 传输</th><th>展示</th></tr><tr><td>查询条件</td><td>订单创建时间</td><td>按 Asia/Shanghai 选择；请求转 UTC ISO</td><td>东八区年月日时分秒</td></tr><tr><td>后端过滤</td><td>thirdpart_general_order.created_at</td><td>按请求 UTC 起止过滤</td><td>不直接展示 UTC 墙钟值</td></tr><tr><td>列表 / 导出</td><td>created_at</td><td>服务端或前端统一转换</td><td>列名「订单创建时间」，Asia/Shanghai</td></tr><tr><td>可选列</td><td>pay_time</td><td>仅在业务仍需展示时保留</td><td>列名「支付时间」，Asia/Shanghai</td></tr></table></div>
<div class="card"><h3>校验与反馈</h3><table><tr><th>校验项</th><th>规则</th><th>是否必填</th><th>报错反馈文案</th></tr><tr><td>订单创建时间</td><td>查询必须提供起止时间，按 Asia/Shanghai 解释。</td><td>必填</td><td>请选择订单创建时间</td></tr><tr><td>导出平台</td><td>导出必须指定单个第三方平台；非电商 Tab 已锁定为单个平台值。</td><td>条件必填</td><td>请选择单个第三方平台</td></tr><tr><td>导出时间范围</td><td>起止时间跨度不得超过 90 天。</td><td>必填</td><td>导出时间范围不得超过 90 天</td></tr></table></div>
<div class="card"><h3>验收示例</h3><table><tr><th>输入</th><th>请求</th><th>预期展示</th></tr><tr><td>2026-08-01 00:00:00（东八区）</td><td>2026-07-31T16:00:00.000Z</td><td>列表/导出仍显示 2026-08-01 00:00:00</td></tr><tr><td>created_at=2026-08-18T07:26:42.000Z</td><td>后端按 created_at 命中</td><td>订单创建时间=2026-08-18 15:26:42</td></tr></table></div></section>
<section id="prototype" class="tab"><div class="iframe-card"><iframe src="__PROTOTYPE_URL__" title="通用三方高保真原型"></iframe></div></section>
<section id="decisions" class="tab"><div class="card"><div class="dm-h">待办事项</div><div id="todoList"></div><div class="dm-add"><input id="todoInput" placeholder="新增待办事项"><button data-add="todo">添加</button></div><div class="dm-h">决策共识</div><div id="consensusList"></div><div class="dm-add"><input id="consensusInput" placeholder="新增决策共识"><button data-add="consensus">添加</button></div><div class="dm-h">评审意见</div><div id="reviewList"></div><div class="dm-add"><input id="reviewInput" placeholder="新增评审意见"><button data-add="review">添加</button></div></div></section>
</div><script>
const nav=document.querySelector('#nav');nav.addEventListener('click',e=>{if(e.target.tagName!=='BUTTON')return;document.querySelectorAll('#nav button').forEach(b=>b.classList.remove('on'));document.querySelectorAll('.tab').forEach(s=>s.classList.remove('on'));e.target.classList.add('on');document.getElementById(e.target.dataset.tab).classList.add('on')});
const KEY='general-thirdparty-tabs-timezone-decisions-v1';let store;try{store=JSON.parse(localStorage.getItem(KEY))}catch(e){}store=store||{todo:[],consensus:[],review:[]};
function draw(){['todo','consensus','review'].forEach(k=>{document.getElementById(k+'List').innerHTML=store[k].map((x,i)=>`<div class="dm-row"><span class="pill">${new Date(x.at).toLocaleString('zh-CN')}</span><span style="flex:1">${x.text}</span><button data-del="${k}:${i}">删除</button></div>`).join('')})}function save(){localStorage.setItem(KEY,JSON.stringify(store));draw()}document.addEventListener('click',e=>{if(e.target.dataset.add){const k=e.target.dataset.add,inp=document.getElementById(k+'Input');if(inp.value.trim()){store[k].push({text:inp.value.trim(),at:Date.now()});inp.value='';save()}}if(e.target.dataset.del){const [k,i]=e.target.dataset.del.split(':');store[k].splice(+i,1);save()}});draw();
document.getElementById('exportHtml').addEventListener('click',()=>{const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['<!doctype html>\n'+document.documentElement.outerHTML],{type:'text/html'}));a.download='general-thirdparty-tabs-timezone-review.html';a.click()});
</script></body></html>""".replace("__PROTOTYPE_URL__", PROTOTYPE_URL).replace("__REQUIREMENT_URL__", REQ_URL).replace("__SDD_URL__", SDD_URL)

# GitHub Pages 版直接复用 review-package/template.html 的完整编辑与决策引擎。
# 只删除 MinIO 的 window.__SAVE__ 注入位；编辑、localStorage/IndexedDB 与导出均保留。
template_style = re.search(r"<style>(.*?)</style>", REVIEW_TEMPLATE, re.S).group(1)
editor_script = re.search(
    r'(<script>\s*/\* ===== 在线编辑：.*?</script>)',
    REVIEW_TEMPLATE,
    re.S,
).group(1)
editor_script = re.sub(
    r'^window\.__SAVE__=\{url:"__SAVE_URL__",exp:0/\*__SAVE_EXP__\*/\};\s*$',
    '',
    editor_script,
    flags=re.M,
)
decision_script = re.search(
    r'(<script>\s*/\* ===== 决策事项 \+ 分页评审意见.*?</script>)',
    REVIEW_TEMPLATE,
    re.S,
).group(1)
package = package.replace("</style></head>", template_style + "\n</style></head>")
package = package.replace(
    '<body><button class="export-btn" id="exportHtml">导出 HTML</button>',
    '<body>',
)
package = re.sub(
    r'<section id="decisions" class="tab">.*?</section>',
    '<section id="decisions" class="tab"><div id="dmRoot"></div></section>',
    package,
    flags=re.S,
)
runtime = r"""
</div>
<div id="rvPanel">
  <div class="rv-t">本页评审意见 · <span id="rvTab"></span></div>
  <div id="rvList"></div>
  <div class="dm-add"><input id="rvT" placeholder="记录评审意见"><input id="rvB" class="dm-by" placeholder="撰写人"><select id="rvC" class="dm-catmini"><option value="">分类（可不选）</option><option value="pend">待办事项</option><option value="dec">决策共识</option></select><button id="rvAdd">添加</button></div>
</div>
<div id="rvFab">评审意见<span id="rvN"></span></div>
<script>
const nav=document.querySelector('#nav');nav.addEventListener('click',e=>{if(e.target.tagName!=='BUTTON')return;document.querySelectorAll('#nav button').forEach(b=>b.classList.remove('on'));document.querySelectorAll('.tab').forEach(s=>s.classList.remove('on'));e.target.classList.add('on');document.getElementById(e.target.dataset.tab).classList.add('on')});
</script>
""" + editor_script + decision_script + "\n</body></html>"
package = re.sub(
    r'</div><script>\s*const nav=document\.querySelector.*?</script></body></html>',
    lambda _: runtime,
    package,
    flags=re.S,
)
assert "✎ 编辑" in package and "dmRoot" in package
assert "window.__SAVE__={" not in package
assert "__SAVE_URL__" not in package and "__SAVE_EXP__" not in package


requirement = """# 需求说明 · 通用三方双 Tab 与时区统一

## 待定问题

无（本次产出均已基于明确输入，无待确认项）。

| 相关文档 | 链接 |
|---|---|
| 需求评审包 | [外网评审包](""" + PACKAGE_URL + """) |
| 对应 SDD | [SDD · 通用三方双 Tab 与时区统一](__SDD_URL__) |
| 高保真原型 | [外网高保真原型](""" + PROTOTYPE_URL + """) |
| 需求标签 | 通用三方 · 双 Tab · 非电商平台 · created_at · Asia/Shanghai · UTC ISO · 导出 |

## 背景与问题
- **页面无平台类型分区：**通用三方现有电商数据与已 ready 的非电商数据缺少前端隔离入口。
- **查询与展示字段错位：**筛选按订单创建时间，列表和导出却以 `pay_time` 充当主时间列。
- **时区少 8 小时：**列表和导出把 UTC 墙钟值原样展示，未转换回东八区。

## 目标
1. 默认电商平台 Tab，非电商订单只在非电商平台 Tab 展示，两类数据查询结果互不串行。
2. 筛选、后端过滤、列表与导出统一使用 `created_at`；运营输入和输出均为东八区。
3. 请求边界统一转换为 UTC ISO。

## 范围
### 要做
- 新增「电商平台 / 非电商平台」双 Tab，视觉与掉单管理一致。
- 非电商 Tab 锁定第三方平台，店铺文案改为渠道 ID/名称。
- 列表主时间列改为订单创建时间，展示 `created_at` 东八区时间。
- 查询请求转 UTC ISO；导出按 `created_at` 过滤并按东八区展示。

### 不做
- 不展开 Excel 导入、掉单 Base、10MB 文件限制、上传渠道必填弹窗。
- 不改变现有导出的单平台与 90 天限制。
- 不新增截图中不存在的主播、预售、买家留言、数量列。

## 行为变更
1. 通用三方新增双 Tab：电商平台默认、非电商平台独立展示。
2. 非电商 Tab 锁定平台，店铺 ID/名称改为渠道 ID/名称。
3. 查询按 Tab 隔离数据源，清空和切换不得串数据。
4. 主时间列改为「订单创建时间」，展示 `created_at`。
5. `created_at` 按 `Asia/Shanghai` 格式化；若保留 `pay_time`，列名必须为支付时间并同样转东八区。
6. 前端将东八区起止时间转换为 UTC ISO；后端过滤 `thirdpart_general_order.created_at`。
7. 导出按 `created_at` 过滤并按东八区输出时间，保留单平台与 90 天限制。

## 数据口径
| 对象 | 口径 |
|---|---|
| `thirdpart_general_order.created_at` | 查询过滤、列表主时间列与导出时间列的统一字段；展示格式为 `Asia/Shanghai` |
| `pay_time` | 不再冒充订单创建时间；如保留，明确列名「支付时间」并转为 `Asia/Shanghai` |
| 平台类型 / 渠道信息 | 按电商/非电商分区；非电商平台值固定，展示渠道 ID/名称 |

## 校验与反馈
| 校验项 | 规则 | 是否必填 | 报错反馈文案 |
|---|---|---|---|
| 订单创建时间 | 必须提供起止时间，按 `Asia/Shanghai` 解释 | 必填 | 请选择订单创建时间 |
| 导出平台 | 必须指定单个第三方平台 | 条件必填 | 请选择单个第三方平台 |
| 导出时间范围 | 起止时间跨度不得超过 90 天 | 必填 | 导出时间范围不得超过 90 天 |
""".replace("__SDD_URL__", SDD_URL)


sdd = """# SDD · 通用三方双 Tab 与时区统一

## 待定问题

无（本次产出均已基于明确输入，无待确认项）。

| 相关文档 | 链接 |
|---|---|
| 需求评审包 | [外网评审包](""" + PACKAGE_URL + """) |
| 需求说明 | [需求说明 · 通用三方双 Tab 与时区统一](__REQUIREMENT_URL__) |
| 高保真原型 | [外网高保真原型](""" + PROTOTYPE_URL + """) |
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
""".replace("__REQUIREMENT_URL__", REQ_URL)

requirement = requirement.replace("__SDD_URL__", SDD_URL)
sdd = sdd.replace("__REQUIREMENT_URL__", REQ_URL)

for name, content in {
    "prototype.html": prototype,
    "review-package.html": package,
    "需求说明.md": requirement,
    "SDD.md": sdd,
}.items():
    (ROOT / name).write_text(content)
    print(ROOT / name)
