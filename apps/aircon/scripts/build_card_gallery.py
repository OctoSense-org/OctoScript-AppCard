#!/usr/bin/env python3
"""Publish a static gallery of the actual independently mounted native cards."""
from pathlib import Path
import html, json
ROOT = Path(__file__).resolve().parents[1]
esc = html.escape
TITLES = {
 'order_card-03': ('订单已付款', '从桌面查看订单，或收起提醒'),
 'logistics_card-04': ('空调正在送来', '查看配送时间，联系配送员或调整时间'),
 'installation_card-05': ('预约上门安装', '送达事件触发安装服务，用户决定何时预约'),
 'installation_card-06': ('日历参与选时', '冲突时段不可选，确认按钮等待有效选择'),
 'installation_card-07': ('确认可用时段', '选中下午时段，再确认预约'),
 'installation_booking-08': ('安装预约成功', '服务保留预约，支持改约或明确取消'),
 'calendar_updated-08': ('日历已经更新', '确认表示已阅，撤销只移除这条日程'),
 'installation_booking-09': ('预约仍然有效', '撤销日历后，安装服务保留原预约'),
 'calendar_undone-09': ('重新加入日历', '用原来的事件身份恢复安装日程'),
 'installation_arriving-10': ('师傅正在路上', '查看预计到达时间和预约，直接联系师傅'),
 'payment_due-11': ('材料费待确认', '付款由用户确认，撤销仅关闭待付款请求'),
 'installation_complete-11': ('安装已经完成', '服务卡片保留状态，提供问题反馈入口'),
 'payment_complete-12': ('付款完成', '保留金额与回执入口，重复点击不重复付款'),
 'installation_complete-12': ('查看服务记录', '付款之后，安装服务仍有独立入口'),
}
OWNERS = {'shopping':'订单', 'logistics':'物流', 'installation':'安装', 'calendar':'日历', 'payment':'支付'}

def main():
 catalogue=json.loads((ROOT/'service-cards/catalogue.json').read_text())
 verification=json.loads((ROOT/'evidence/standalone-latest.json').read_text())
 evidence={c['id']:c for c in verification['cards']}
 parts=['''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>OctoSense · 独立服务卡片</title><style>
*{box-sizing:border-box}body{margin:0;background:#edf3ef;color:#31413c;font:15px/1.65 system-ui,"Noto Sans SC",sans-serif}header,main,footer{max-width:1200px;margin:auto;padding:30px 26px}header{padding-top:50px}small,.meta{color:#627c6d}h1{font-size:clamp(28px,4vw,46px);line-height:1.3;font-weight:500;margin:24px 0 14px}h2{font-size:18px;margin:4px 0}p{margin:8px 0 16px}a{color:#416d57;text-underline-offset:4px}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;align-items:start}.card{padding:18px;background:#f8fbf8;border:1px solid #dae4dc;border-radius:22px;min-width:0}.card img{display:block;width:100%;height:auto;border-radius:16px;background:#4c4d4b}.description{font-size:13px;min-height:44px;color:#607469}.meta{font-size:11px;margin:12px 0;overflow-wrap:anywhere}.links{display:flex;gap:14px;flex-wrap:wrap;font-size:12px}nav{display:flex;flex-wrap:wrap;gap:22px;margin-top:22px}footer{font-size:13px}@media(max-width:900px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:560px){.grid{grid-template-columns:1fr}header,main,footer{padding:24px 18px}.description{min-height:0}}
</style><header><small>OCTOSENSE / NATIVE SERVICE APP CARDS</small><h1>各自负责，彼此默契</h1><p>14 张独立卡片，连接订单、物流、安装、日历与支付<br>这里展示逐张独立挂载的真实 Makepad 截图，可点击图片查看原始尺寸</p><nav><a href="index.html">12 个完整场景对照</a><a href="../README.md">运行原生演示</a><a href="../evidence/conversion-report.md">查看验证报告</a></nav></header><main class="grid">''']
 for card in catalogue['cards']:
  ident=card['id'];result=evidence[ident];title,description=TITLES[ident]
  image='../'+result['evidence']+'/native.png'
  assert (ROOT/result['evidence']/'native.png').is_file()
  folder='../'+card['folder'];w,h=card['artboard']
  status='原生挂载与输入通过' if result['passed'] else '原生验证待修'
  parts.append(f'<article class="card" id="{esc(ident)}"><small>{OWNERS[card["owner_app"]]}服务</small><h2>{esc(title)}</h2><p class="description">{esc(description)}</p><a href="{esc(image)}" target="_blank" rel="noopener"><img src="{esc(image)}" alt="{esc(title)}，独立 Makepad 原生卡片" loading="lazy"></a><p class="meta">{status} · {w:.1f} × {h:.1f} 逻辑像素<br>{result["native_nodes"]} 个原生组件 · {result["controls_tested"]} 个按钮</p><div class="links"><a href="{esc(folder)}/page.card">卡片源码</a><a href="{esc(folder)}/page.data.json">数据</a><a href="{esc(folder)}/service-actions.json">服务动作</a><a href="../{esc(result["evidence"])}/result.json">验证记录</a></div></article>')
 parts.append('</main><footer>本页为实际原生截图预览，交互操作请在 Makepad Studio 中运行<br>服务与付款使用本地演示数据，完整画面与图像差异记录保留在场景对照页</footer></html>')
 (ROOT/'review/service-cards.html').write_text('\n'.join(parts))
 print(json.dumps({'gallery':'review/service-cards.html','cards':len(catalogue['cards'])}))

if __name__=='__main__':main()
