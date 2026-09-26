from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
PAIRS='''消息|Messages
搜索|Search
2016届同学群|Class of 2016
2016届同学聚会|Class of 2016 reunion
2016届同学聚会餐费|Class of 2016 dinner
王宁：好久不见，一起聚聚吧|Wang Ning: Let's catch up
林老师|Teacher Lin
明天见|See you tomorrow
昨天|Yesterday
家人|Family
周末一起吃饭|Dinner this weekend
查看邀请|View invitation
王宁|Wang Ning
好久不见，找个周末一起吃饭吧|It's been a while. Dinner together?
十年同窗 再聚一堂|Ten years, together again
周五 10月23日18:30|Fri 23 Oct · 18:30
周六 10月24日18:30|Sat 24 Oct · 18:30
周日 10月25日12:00|Sun 25 Oct · 12:00
去投票|Open poll
群资料|Group info
10月21日 星期三|Wed 21 October
聚会 · 时间投票|Reunion · time poll
王宁邀请你选择时间|Wang Ning invites your vote
3个时段 · 18位同学|3 times · 18 classmates
选择时间|Choose time
日历|Calendar
聚会|Reunion
支付|Payment
聚会 · 选择时间|Reunion · choose a time
与工作例会冲突|Work meeting conflict
日历空闲|Calendar is free
确认参加|Confirm RSVP
返回|Back
已选择 周六晚餐|Selected: Saturday dinner
重新选择|Reset choice
聚会 · 已报名|Reunion · RSVP sent
你的时间偏好已提交|Your preferred time is saved
王宁正在确认场地|Wang Ning is confirming the venue
场地确认后再加入日历|Calendar follows venue confirmation
查看报名|View RSVP
聚会 · 已确认|Reunion · confirmed
木光餐厅 · 桂花路8号|Muguang · 8 Guihua Road
来自王宁的最新确认|Confirmed by Wang Ning
查看聚会|View reunion
日历 · 已更新|Calendar · updated
同学聚会|Class reunion
10月24日18:30–21:00|24 Oct · 18:30–21:00
已加入个人日历|Added to your calendar
确认|Confirm
撤销日程|Undo calendar
日历记录已撤销|Calendar entry removed
报名仍然有效|Your RSVP is still active
重新加入|Restore event
支付 · 待付款|Payment · due
收款人|Recipient
用途|Purpose
活动|Event
聚会餐费|Reunion dinner
已报名 · 木光餐厅|RSVP active · Muguang
支付 ¥180|Pay ¥180
取消支付|Cancel payment
聚会报名仍有效|Your RSVP remains active
你已确认参加本次聚会|Your attendance is confirmed
支付 · 已取消|Payment · cancelled
收款人 王宁|To Wang Ning
本次支付已取消|This payment was cancelled
聚会报名不受影响|Your RSVP is unchanged
重新打开支付|Reopen payment
支付 · 已完成|Payment · completed
¥180已支付|¥180 paid
凭证|Receipt
支付记录已保存|Your receipt is saved
查看聚会详情|View reunion details
聚会详情|Reunion details
组织者|Organizer
报名|RSVP
已确认|Confirmed
凑份子|Your share
返回桌面|Back to desktop'''
translations={cn.replace(' ',''):en for cn,en in (line.split('|',1) for line in PAIRS.splitlines())}
def en(text):
 if not re.search('[\u3400-\u9fff]',text):return text
 key=text.replace(' ','')
 if key not in translations:raise ValueError('Missing English: '+text)
 return translations[key]
frames={}
for row in json.loads((ROOT/'source/native-catalogue.json').read_text()):
 frame=int(row['id'][-2:]);texts={id:{**text,'en':en(text['cn'])} for id,text in row['texts'].items()}
 mapping=json.loads((ROOT/'cards'/row['id']/'mapping.json').read_text())
 nodes={node['source_id']:node for node in mapping['elements']}
 dock={}
 for id,text in texts.items():
  icon={'消息':'dock_message','日历':'dock_calendar','聚会':'dock_group','支付':'dock_wallet'}.get(text['cn'])
  if text['bounds'][1]>700 and icon in nodes:
   x,y,w,h=nodes[icon]['bounds'];dock[id]={'center':x+w/2}
 frames[frame]={'texts':texts,'controls':row['controls'],'dock':dock}
prefix='// Generated bilingual frame catalogue; native source IDs bind all labels and controls.\nconst FRAMES='+json.dumps(frames,ensure_ascii=False,separators=(',',':'))+';\n'
(ROOT/'wizard/service.mjs').write_text(prefix+(ROOT/'scripts/service.template.mjs').read_text())
print('Bilingual native labels',sum(len(v['texts']) for v in frames.values()))
