import concurrent.futures,datetime,hashlib,json,re,threading,time,urllib.parse,urllib.request,xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo
from html import unescape

ALLOWED={'geocoding-api.open-meteo.com','api.open-meteo.com','air-quality-api.open-meteo.com','overpass-api.de','www.bing.com','query1.finance.yahoo.com'}
class Redirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  u=urllib.parse.urlsplit(newurl)
  if u.scheme!='https' or u.hostname not in ALLOWED:raise ValueError('Unexpected source redirect')
  return super().redirect_request(req,fp,code,msg,headers,newurl)
OPENER=urllib.request.build_opener(Redirect)
def fetch(url):
 u=urllib.parse.urlsplit(url)
 if u.scheme!='https' or u.hostname not in ALLOWED:raise ValueError('Unapproved source')
 req=urllib.request.Request(url,headers={'User-Agent':'OctosCompositionStudy/1.0'})
 with OPENER.open(req,timeout=18) as r:
  raw=r.read(2*1024*1024+1)
  if len(raw)>2*1024*1024:raise ValueError('Response exceeds 2 MiB')
 return raw

def url(base,**params):return base+'?'+urllib.parse.urlencode(params)
class Adapters:
 def __init__(self):self.geo={};self.lock=threading.Lock()
 def geocode(self,city):
  with self.lock:
   future=self.geo.get(city);owner=future is None
   if owner:future=concurrent.futures.Future();self.geo[city]=future
  if owner:
   try:
    u=url('https://geocoding-api.open-meteo.com/v1/search',name=city,count=5,language='en',format='json')
    rows=json.loads(fetch(u)).get('results',[])
    if not rows:raise ValueError('Location not found')
    p=rows[0];future.set_result({'name':p['name'],'country':p.get('country',''),'lat':p['latitude'],'lon':p['longitude'],'timezone':p.get('timezone','UTC'),'geocode_url':u})
   except Exception as e:future.set_exception(e)
  return future.result()
 def run(self,job):
  start=time.perf_counter();kind=job['kind'];params=job['params'];stamp=datetime.datetime.now(datetime.timezone.utc).isoformat();u=''
  try:
   if kind in ['weather','air','places']:
    p=self.geocode(params['city'])
   if kind=='weather':
    u=url('https://api.open-meteo.com/v1/forecast',latitude=p['lat'],longitude=p['lon'],timezone=p['timezone'],forecast_days=8,daily='temperature_2m_max,temperature_2m_min,precipitation_probability_max,wind_speed_10m_max,sunrise,sunset')
    j=json.loads(fetch(u));d=j['daily'];today=datetime.datetime.now(ZoneInfo(p['timezone'])).date();h=params['horizon']
    if h=='this_week':end=today+datetime.timedelta(days=6-today.weekday());begin=today
    elif h=='weekend':begin=today+datetime.timedelta(days=max(0,5-today.weekday()));end=begin+datetime.timedelta(days=6-begin.weekday())
    else:begin=today;end=today+datetime.timedelta(days={'today':0,'next3days':2,'next7days':6}.get(h,6))
    rows=[{'date':day,'high_c':d['temperature_2m_max'][i],'low_c':d['temperature_2m_min'][i],'rain_probability_pct':d['precipitation_probability_max'][i],'wind_kmh':d['wind_speed_10m_max'][i],'sunrise':d['sunrise'][i],'sunset':d['sunset'][i]} for i,day in enumerate(d['time']) if begin.isoformat()<=day<=end.isoformat()]
    data={'place':p,'timezone':j['timezone'],'horizon':h,'days':rows}
   elif kind=='air':
    u=url('https://air-quality-api.open-meteo.com/v1/air-quality',latitude=p['lat'],longitude=p['lon'],timezone=p['timezone'],current='us_aqi,pm2_5',hourly='us_aqi',forecast_days=5)
    j=json.loads(fetch(u));days={}
    for day,n in zip(j['hourly']['time'],j['hourly']['us_aqi']):
     if n is not None:days.setdefault(day[:10],[]).append(n)
    data={'place':p['name'],'current':j['current'],'forecast_daily_max_us_aqi':{day:max(ns) for day,ns in days.items()},'measurement':'Open-Meteo modeled US AQI; hourly forecast daily maximum, not a personal exposure measurement'}
   elif kind=='places':
    q=f'[out:json][timeout:10];(nwr(around:7000,{p["lat"]},{p["lon"]})[tourism=museum];nwr(around:7000,{p["lat"]},{p["lon"]})[leisure=park];);out center tags 20;'
    u=url('https://overpass-api.de/api/interpreter',data=q);j=json.loads(fetch(u));items=[]
    for e in j.get('elements',[]):
     tags=e.get('tags',{});name=tags.get('name:en',tags.get('name',''))
     if not name:continue
     items.append({'name':name,'kind':'museum' if tags.get('tourism')=='museum' else 'park','url':f'https://www.openstreetmap.org/{e["type"]}/{e["id"]}','notable':bool(tags.get('wikidata') or tags.get('wikipedia'))})
    items.sort(key=lambda e:not e['notable']);items=[p for kind in ['park','museum'] for p in [x for x in items if x['kind']==kind][:4]];data={'place':p['name'],'items':items[:8],'coverage':'OSM mapped museums and parks within 7 km of the geocoded center; hours and tickets not checked'}
    if not items:raise ValueError('No named places returned')
    missing=sorted({'park','museum'}-{x['kind'] for x in items})
    if missing:data['coverage']+='; no '+', '.join(missing)+' returned by this limited query; this does not establish their absence in the city'
   elif kind=='quote':
    sym=params['ticker']
    if not re.fullmatch(r'[A-Z][A-Z0-9.-]{0,9}',sym):raise ValueError('Invalid ticker')
    u=url('https://query1.finance.yahoo.com/v8/finance/chart/'+urllib.parse.quote(sym),interval='1d',range='5d');j=json.loads(fetch(u));r=j['chart']['result'][0];m=r['meta'];bars=r['indicators']['quote'][0]['close'];ts=r.get('timestamp',[])
    obs=[(t,c) for t,c in zip(ts,bars) if c is not None];latest=m['regularMarketPrice'];prev=m.get('previousClose')
    if m.get('symbol') != sym:raise ValueError('Quote symbol mismatch')
    # range=5d chartPreviousClose is the range baseline, not yesterday's close.
    if len(obs)>1:prev=obs[-2][1]
    if prev is None or prev<=0:raise ValueError('Previous-session close unavailable')
    data={'ticker':sym,'company':m.get('longName',m.get('shortName',sym)),'currency':m['currency'],'price':latest,'quote_at':datetime.datetime.fromtimestamp(m['regularMarketTime'],datetime.timezone.utc).isoformat(),'previous_close':round(prev,4),'previous_close_bar_start_at':datetime.datetime.fromtimestamp(obs[-2][0],datetime.timezone.utc).isoformat() if len(obs)>1 else None,'change_pct':round((latest/prev-1)*100,3),'daily_closes':[{'at':datetime.datetime.fromtimestamp(t,datetime.timezone.utc).isoformat(),'close':round(c,4)} for t,c in obs],'baseline':'previous completed daily bar close; not return since a headline'}
   elif kind=='news':
    q=params['topic'];u=url('https://www.bing.com/news/search',q=q,format='rss',mkt='en-US');root=ET.fromstring(fetch(u));items=[]
    from email.utils import parsedate_to_datetime
    now=datetime.datetime.now(datetime.timezone.utc)
    for item in root.findall('./channel/item'):
     title=item.findtext('title','');link=item.findtext('link','');desc=unescape(re.sub('<[^>]+>',' ',item.findtext('description','')));pub=item.findtext('pubDate','')
     try:dt=parsedate_to_datetime(pub)
     except Exception:continue
     if not now-datetime.timedelta(hours=72)<=dt<=now+datetime.timedelta(minutes=5):continue
     parsed=urllib.parse.urlsplit(link)
     if parsed.hostname=='www.bing.com':link=urllib.parse.parse_qs(parsed.query).get('url',[link])[0]
     parsed=urllib.parse.urlsplit(link)
     if parsed.scheme not in ['https','http'] or not parsed.hostname or parsed.hostname=='www.bing.com':continue
     if any(i['url']==link for i in items):continue
     items.append({'title':title,'excerpt':desc[:650],'url':link,'publisher':parsed.hostname,'published_at':dt.isoformat()})
    data={'topic':q,'items':items[:5],'coverage':'Bing News indexed titles and excerpts from the past 72 hours; full articles not read'}
    if not items:raise ValueError('No fresh indexed news')
   else:raise ValueError('Unknown adapter')
   return {'id':job['id'],'kind':kind,'status':'ready','retrieved_at':stamp,'url':u,'data':data,'elapsed_s':time.perf_counter()-start}
  except Exception as e:
   return {'id':job['id'],'kind':kind,'status':'failed','retrieved_at':stamp,'url':u,'error':str(e),'data':{},'elapsed_s':time.perf_counter()-start}
