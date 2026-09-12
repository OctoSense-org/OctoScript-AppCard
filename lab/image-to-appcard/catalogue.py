#!/usr/bin/env python3
"""Author reproducible image briefs and runtime widget composition contracts.

These are design fixtures, not live weather, news or financial feeds. Geometry
here is the requested contract; observe.py records what the image model drew.
"""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
PALETTES = [
    ('Sage', 'F5F6F0', 'FFFFFF', '19372D', '718078', 'E3EDE3', '285F49'),
    ('Midnight', '111827', '1C293C', 'F2F5FC', '9AACC5', '253C58', '92C9ED'),
    ('Cobalt', 'F3F5FA', 'FFFFFF', '172D56', '75829B', 'DFE9FF', '2F61D5'),
    ('Apricot', 'FBF4EC', 'FFFFFF', '482F28', '987D70', 'F6D8BE', 'A34E2F'),
    ('Editorial', 'F4F2EB', 'FCFBF7', '252922', '797E70', 'E4E7D4', '536241'),
    ('Denim', 'EAF0F4', 'F8FBFD', '213B50', '72899A', 'CFDFE8', '355F7A'),
    ('Lavender', 'F4F0FA', 'FFFFFF', '3A2A56', '8C7C9C', 'E5DDF4', '7551A9'),
    ('Clay', 'F4EEE8', 'FFFCF8', '42352D', '988679', 'E9D6C7', '996343'),
    ('Mint', 'EDF6F1', 'FFFFFF', '173E34', '77968C', 'D5EDE1', '22785D'),
    ('Electric', '171C1C', '252D2C', 'F3F7E9', 'A0AFA9', '384F43', 'D2EF82'),
]

def rgba(s): return int('ff' + s.lstrip('#'), 16)
def hexcolor(n): return '#' + f'{n:08x}'[2:]
def walk(n):
    yield n
    for c in n.get('c', []): yield from walk(c)

class Page:
    def __init__(self, app, number, title, structure):
        self.app, self.number, self.title, self.structure = app, number, title, structure
        self.palette = PALETTES[number-1]
        _, self.bg, self.panel, self.ink, self.muted, self.tint, self.accent = self.palette
        self.root = dict(t='stack', id='page', x=0, y=0, w=406, h=776,
                         variant='surface', bg=rgba(self.bg), c=[])
        self.font = 'camo/DMSans'
        self.graphics = {}
    def add(self, n, parent=None):
        (self.root if parent is None else parent).setdefault('c', []).append(n)
        return n
    def box(self, id, x, y, w, h, color=None, radius=20, parent=None):
        return self.add(dict(t='stack', id=id, x=x, y=y, w=w, h=h,
                             variant='surface', bg=rgba(color or self.panel), radius=radius, c=[]), parent)
    def group(self, id, x, y, w, h, parent=None):
        return self.add(dict(t='stack', id=id, x=x, y=y, w=w, h=h, c=[]), parent)
    def text(self, id, text, x, y, w, size=16, weight=500, color=None, parent=None, h=None, align=0):
        family = 'Bold' if weight>=600 else 'Regular' if weight<=400 else 'Medium'
        return self.add(dict(t='text', id=id, text=text, x=x, y=y, w=w, h=h or round(size*1.3,2),
                             size=size, weight=weight, line_height=round(size*1.3,2), alignx=align,
                             variant='single_line', font_src=f'self:resources/{self.font}-{family}.ttf',
                             color=rgba(color or self.ink)), parent)
    def button(self, id, text, x=24, y=708, w=358, h=44, filled=True, parent=None):
        g=self.group(id,x,y,w,h,parent)
        g['kit']=json.dumps({'widget':'KitButton','bindings':{'control':[2],'label':[1]}},separators=(',',':'))
        self.box(id+'_surface',x,y,w,h,self.accent if filled else self.panel,14,g)
        self.text(id+'_label',text,x+8,y+(h-20)/2,w-16,14,500,
                  self.bg if filled and self.number in (2,10) else 'FFFFFF' if filled else self.ink,g,h=20,align=.5)
        self.add(dict(t='button', id=id+'_control',x=x,y=y,w=w,h=h,enabled=1),g)
        return g
    def icon(self,id,x,y,w=42,h=36,kind='sun',parent=None):
        self.graphics[id]={'kind':kind,'ink':'#'+self.accent,'sun':'#E8BD63','cloud':'#B6CCC1'}
        return self.add(dict(t='svg',id=id,x=x,y=y,w=w,h=h,src=f'http://127.0.0.1:8170/ux-images/{self.app}-{self.number:02d}/assets/{id}.svg'),parent)
    def header(self,title=None,eyebrow=None):
        self.text('heading',title or self.title,24,32,290,30,700)
        self.text('subtitle',eyebrow or 'Monday, September 7',24,76,350,13,400,self.muted)
    def metric(self,id,label,value,x,y,w=171,h=92):
        g=self.box(id,x,y,w,h)
        self.text(id+'_label',label,x+16,y+14,w-32,12,500,self.muted,g)
        self.text(id+'_value',value,x+16,y+39,w-32,25,700,parent=g)
        return g
    def section(self,id,label,y,detail=None):
        self.text(id,label,24,y,250,20,700)
        if detail:self.text(id+'_detail',detail,270,y+5,112,11,400,self.muted,align=1)
    def forecast(self,y,vertical=False,days=None):
        days=days or [('Now','24°','cloud'),('Tue','25°','sun'),('Wed','23°','cloud'),('Thu','22°','sun')]
        g=self.box('forecast',24,y,358,len(days)*64 if vertical else 112)
        for i,(day,temp,icon) in enumerate(days):
            if vertical:
                cy=y+i*64; row=self.group('day_'+str(i),24,cy,358,64,g)
                self.text('day_label_'+str(i),day,42,cy+20,120,14,parent=row)
                self.icon('day_icon_'+str(i),208,cy+16,34,28,icon,row)
                self.text('day_temp_'+str(i),temp,290,cy+17,70,21,700,parent=row,align=1)
            else:
                x=24+i*89.5;row=self.group('day_'+str(i),x,y,89.5,112,g)
                self.text('day_label_'+str(i),day,x+8,y+13,73.5,12,500,self.muted,row,align=.5)
                self.icon('day_icon_'+str(i),x+28,y+39,34,28,icon,row)
                self.text('day_temp_'+str(i),temp,x+8,y+78,73.5,17,700,parent=row,align=.5)
    def chart(self,id,x,y,w,h,kind='line',parent=None):
        return self.icon(id,x,y,w,h,kind,parent)
    def story(self,id,tag,line1,line2,y,number=None,card=True):
        g=self.box(id,24,y,358,112) if card else self.group(id,24,y,358,112)
        left=44
        if number is not None:
            self.text(id+'_number',str(number).zfill(2),40,y+18,45,25,700,self.accent,g);left=98
        self.text(id+'_tag',tag.upper(),left,y+14,260,10,700,self.muted,g)
        self.text(id+'_title',line1,left,y+36,370-left,19,700,parent=g)
        self.text(id+'_title2',line2,left,y+61,370-left,19,700,parent=g)
        self.text(id+'_meta','4 min read',left,y+88,150,10,400,self.muted,g)
    def quote(self,id,symbol,name,price,change,y,x=24,w=358):
        g=self.box(id,x,y,w,72)
        self.text(id+'_symbol',symbol,x+16,y+12,w-32,16,700,parent=g)
        self.text(id+'_name',name,x+16,y+40,w-32,11,400,self.muted,g)
        self.text(id+'_price',price,x+w-135,y+10,119,18,700,parent=g,align=1)
        self.text(id+'_change',change,x+w-135,y+40,119,11,500,self.accent,g,align=1)
    def save(self):
        dest=HERE/f'{self.app}-{self.number:02d}';dest.mkdir(exist_ok=True)
        doc={'schema_version':1,'id':dest.name,'app':self.app,'number':self.number,'title':self.title,
             'structure':self.structure,'artboard':[406,776], 'font_family':'DM Sans',
             'palette':dict(zip(('name','page','panel','ink','muted','tint','accent'),self.palette)),
             'content_source':'deterministic design fixture','tree':self.root,'graphics':self.graphics}
        (dest/'contract.json').write_text(json.dumps(doc,indent=2)+'\n')
        rows=[]
        for n in walk(self.root):
            info={k:n[k] for k in ('id','t','x','y','w','h','text','size','weight','alignx','radius') if k in n}
            for k in ('bg','color'):
                if k in n:info[k]=hexcolor(n[k])
            if n['t']=='svg':info['graphic']=self.graphics[n['id']]['kind']
            if n['t']=='button':continue
            rows.append(json.dumps(info,ensure_ascii=False,separators=(',',':')))
        prompt=f'''Generate exactly ONE polished mobile {self.app} app UX mockup titled "{self.title}". Flat front-on full-bleed canvas, aspect 406:776. No device frame, no status bar, no browser chrome, no shadows outside the canvas, no perspective, no annotations or extra panels. This is a real visual design reference for a native Makepad implementation.

Design direction: {self.structure}. Palette: {json.dumps(doc['palette'])}. Refined, intentional negative space, crisp typography. Use DM Sans Regular (400), Medium (500), Bold (700) exactly. All font sizes below are logical CSS pixels. Render all quoted text exactly; content is a fictional static design fixture. Keep figures as provided. Avoid photographic imagery, textures, blur and glass; the graphics are clean native vector icons/charts. Use restrained flat fills and the specified corner radii. No invented text, tabs, icons or dividers. Never print IDs, coordinates or font names.

The following is the exact layout specification in a 406 by 776 coordinate system (origin top left). Scale the whole canvas uniformly. x/y/w/h are logical pixels, size is CSS font size, alignx 0 means left and 0.5 means centered. Text bounds are line boxes, not glyph outlines. Preserve the hierarchy and positions; larger stack rectangles group subsequent items. Do not auto-center left-aligned labels or rearrange this structure. Native buttons should look operable.
'''+'\n'.join(rows)+'\n\nRender only this single finished app screen. Fit every element within the artboard.\n'
        (dest/'image-prompt.md').write_text(prompt)
        return doc

def weather(n):
    titles=['Cupertino','Evening forecast','Hour by hour','Weather at a glance','The daily weather','Your cities','Rain watch','Conditions','Plan your week','Outside today']
    directions=['Calm sage dashboard: big hero, four-column forecast, two metrics.',
        'Dark split hero with the temperature on the left and an icon on the right; stacked daily forecast.',
        'Cobalt hourly timeline: compact summary, wide temperature chart, bottom metric tiles.',
        'Warm apricot bento: asymmetrical large weather card and stacked mini metrics.',
        'Editorial weather bulletin: oversized type without a hero box, thin information rows.',
        'City collection: one featured city and three independent location cards.',
        'Precipitation focus: wide radar-like vector rings, rain timeline, one humidity metric.',
        'Compact utility layout: horizontal conditions, a two-column metric grid, short outlook.',
        'Weekly planner: compact current weather followed by a long five-day forecast list.',
        'Outdoor activity dashboard: large comfort score, condition chips, sunrise and sunset tiles.']
    p=Page('weather',n,titles[n-1],directions[n-1]);p.header()
    if n==1:
        p.button('units','°C',330,34,52,44,False)
        g=p.box('current',24,118,358,240,p.tint,26)
        p.text('current_kicker','CURRENT WEATHER',48,144,240,12,700,p.muted,g)
        p.text('temperature','24°',46,183,213,94,500,parent=g)
        p.icon('weather_symbol',250,186,102,96,'cloud',g)
        p.text('condition','Partly cloudy',48,294,250,19,parent=g)
        p.text('range','H 27° · L 17°',48,323,220,13,400,p.muted,g)
        p.section('forecast_title','This week',384,'4-day outlook');p.forecast(422)
        p.section('details_title','Details',570)
        p.metric('humidity','Humidity','64%',24,610,171,86);p.metric('wind','Wind','12 km/h',211,610,171,86)
    elif n==2:
        p.text('location','CUPERTINO',24,123,300,12,700,p.muted)
        p.text('temperature','24°',24,154,240,94,500);p.icon('weather_symbol',268,165,106,96,'moon')
        p.text('condition','A calm, clear evening',24,276,350,18)
        p.section('forecast_title','Next few days',321);p.forecast(365,True)
    elif n==3:
        g=p.box('current',24,116,358,112,p.tint)
        p.text('temperature','24°',44,131,150,58,500,parent=g);p.text('condition','Partly cloudy',199,145,170,16,parent=g)
        p.text('location','Cupertino',199,178,150,12,400,p.muted,g)
        p.section('hourly_title','Temperature trend',264,'Next 12 hours')
        g=p.box('timeline',24,308,358,216);p.chart('temperature_chart',44,326,318,146,'line',g)
        for i,s in enumerate(['12 PM','3 PM','6 PM','9 PM']):p.text('hour_'+str(i),s,44+i*80,488,70,11,400,p.muted,g)
        p.metric('humidity','Humidity','64%',24,555);p.metric('wind','Wind','12 km/h',211,555)
    elif n==4:
        g=p.box('current',24,122,216,288,p.tint,24)
        p.text('location','Cupertino',44,143,178,18,700,parent=g);p.text('temperature','24°',44,176,180,76,500,parent=g)
        p.icon('weather_symbol',94,280,86,70,'cloud',g);p.text('condition','Partly cloudy',44,364,174,16,parent=g)
        p.metric('humidity','Humidity','64%',256,122,126,132);p.metric('wind','Wind','12 km/h',256,270,126,140)
        p.section('forecast_title','The week ahead',444);p.forecast(488)
        p.text('note','A little sunshine, a slower day.',24,644,358,15,400,p.muted)
    elif n==5:
        p.text('location','CUPERTINO, CALIFORNIA',24,126,358,11,700,p.muted)
        p.text('temperature','24°',19,160,300,132,500);p.icon('weather_symbol',271,216,100,85,'cloud')
        p.text('condition','A softer kind of sunshine.',24,332,358,24,700)
        p.text('range','High 27° / Low 17°',24,377,358,14,400,p.muted)
        p.forecast(433)
        p.metric('humidity','Humidity','64%',24,579);p.metric('wind','Wind','12 km/h',211,579)
    elif n==6:
        g=p.box('featured',24,118,358,182,p.tint)
        p.text('location','Cupertino',44,140,220,24,700,parent=g);p.text('condition','Partly cloudy',44,182,220,14,400,p.muted,g)
        p.text('temperature','24°',255,144,108,60,500,parent=g);p.icon('weather_symbol',282,226,54,46,'cloud',g)
        for i,(city,temp,label) in enumerate([('San Francisco','19°','Coastal clouds'),('Tokyo','28°','Light rain'),('Copenhagen','16°','Clear skies')]):
            g=p.box('city_'+str(i),24,324+i*116,358,98)
            p.text('city_name_'+str(i),city,44,342+i*116,235,21,700,parent=g)
            p.text('city_note_'+str(i),label,44,378+i*116,235,12,400,p.muted,g)
            p.text('city_temp_'+str(i),temp,285,349+i*116,76,30,500,parent=g,align=1)
    elif n==7:
        p.text('location','Cupertino',24,120,358,17,700)
        g=p.box('radar',24,164,358,254,p.tint);p.chart('rain_radar',75,180,256,220,'radar',g)
        p.text('rain_headline','Rain in 35 minutes',24,449,358,28,700)
        p.text('rain_note','A short shower, then clearer skies.',24,496,358,14,400,p.muted)
        p.metric('chance','Rain chance','80%',24,550);p.metric('humidity','Humidity','64%',211,550)
    elif n==8:
        g=p.box('current',24,118,358,120,p.tint)
        p.icon('weather_symbol',42,151,70,56,'cloud',g);p.text('temperature','24°',131,131,126,56,500,parent=g)
        p.text('location','Cupertino',264,146,105,14,700,parent=g);p.text('condition','Cloudy',264,181,105,12,400,p.muted,g)
        for i,(label,value) in enumerate([('Humidity','64%'),('Wind','12 km/h'),('Feels like','25°'),('UV index','4')]):p.metric('metric_'+str(i),label,value,24+(i%2)*187,272+(i//2)*110)
        p.section('forecast_title','Today into tomorrow',520);p.forecast(564)
    elif n==9:
        p.text('location','Cupertino',24,120,250,16,700);p.text('temperature','24°',277,110,105,48,500,align=1)
        p.section('forecast_title','Five-day outlook',181)
        p.forecast(227,True,[('Monday','24°','cloud'),('Tuesday','25°','sun'),('Wednesday','23°','cloud'),('Thursday','22°','sun'),('Friday','24°','sun')])
        p.text('note','Best day outside: Tuesday',24,592,358,18,700)
        p.text('note_detail','Low wind and long sunny intervals.',24,627,358,13,400,p.muted)
    else:
        g=p.box('comfort',24,121,358,283,p.tint,28)
        p.text('comfort_kicker','OUTDOOR COMFORT',44,141,316,12,700,p.muted,g)
        p.text('comfort_score','86',44,187,214,112,500,parent=g);p.icon('weather_symbol',266,215,86,75,'sun',g)
        p.text('comfort_label','A great day to get outside.',44,345,318,20,700,parent=g)
        p.metric('sunrise','Sunrise','6:42 AM',24,438);p.metric('sunset','Sunset','7:28 PM',211,438)
        p.text('activity','Try a late afternoon walk.',24,574,358,24,700)
        p.text('activity_detail','24° and a gentle breeze in Cupertino.',24,620,358,13,400,p.muted)
    p.button('primary','My cities' if n!=6 else 'Add a city');return p

STORIES=[('Design','A quieter city','starts with small streets'),('Science','The next chapter','of clean energy'),('Culture','Why we keep','making things by hand'),('Technology','Better tools for','everyday creativity')]
def news(n):
    titles=['The Daily','Your morning brief','Field Notes','Explore topics','The Sunday edit','News timeline','Listen today','Around you','Reading room','The business brief']
    directions=['Editorial front page with one large lead story and compact secondary stories.',
      'Numbered digest, three strong typographic rows, no hero image.',
      'Magazine cover hierarchy with an abstract landscape illustration and small story tiles.',
      'Topic-first bento grid with large category cards and a compact latest-news row.',
      'Quiet typographic newspaper: oversized headline and spacious stacked stories.',
      'Chronological news timeline with time markers and inset article cards.',
      'Audio-first news dashboard with large episode card and two upcoming episodes.',
      'Local news landing page with neighborhood identity and two stacked reports.',
      'Personal reading library with saved-article cards and progress indicators.',
      'Business bulletin: lead market headline, two-column topic cards and daily summary.']
    p=Page('news',n,titles[n-1],directions[n-1]);p.header(eyebrow='Independent stories. Fresh perspectives.')
    if n in (1,3,5,8):
        g=p.box('lead',24,122,358,310 if n in (1,3,8) else 270,p.tint,24)
        if n in (1,3,8):
            p.chart('lead_art',44,142,318,132,'landscape',g);ty=295
        else:ty=166
        p.text('lead_tag','DESIGN & CULTURE' if n!=8 else 'YOUR NEIGHBORHOOD',44,ty-1,318,11,700,p.muted,g)
        p.text('lead_title','A quieter city',44,ty+27,318,30,700,parent=g)
        p.text('lead_title2','starts with small streets',44,ty+68,318,23,700,parent=g)
        p.text('lead_meta','The Daily · 6 min read',44,ty+106,318,11,400,p.muted,g)
        for i,s in enumerate(STORIES[1:3]):p.story('story_'+str(i),*s,458+i*118 if n!=5 else 418+i*124,card=n!=5)
    elif n==2:
        p.text('intro','Three stories to start your day.',24,123,358,18,700)
        for i,s in enumerate(STORIES[:3]):p.story('story_'+str(i),*s,181+i*153,number=i+1,card=False)
        p.text('edition','A considered read, in under 15 minutes.',24,647,358,13,400,p.muted)
    elif n==4:
        for i,(label,count,kind) in enumerate([('World','24 stories','landscape'),('Science','12 stories','radar'),('Culture','18 stories','sun'),('Design','9 stories','landscape')]):
            x=24+(i%2)*187;y=126+(i//2)*192;g=p.box('topic_'+str(i),x,y,171,174,p.tint if i==0 else p.panel)
            p.icon('topic_art_'+str(i),x+110,y+18,40,36,kind,g)
            p.text('topic_title_'+str(i),label,x+16,y+88,139,23,700,parent=g)
            p.text('topic_count_'+str(i),count,x+16,y+129,139,12,400,p.muted,g)
        p.section('latest_section','Latest',545);p.story('latest',*STORIES[1],582)
    elif n==6:
        p.text('timeline_label','TODAY / SEPTEMBER 7',24,128,358,11,700,p.muted)
        for i,s in enumerate(STORIES[:3]):
            y=172+i*174;p.text('time_'+str(i),['09:42','08:30','07:15'][i],24,y,358,12,700,p.accent)
            p.story('story_'+str(i),*s,y+29)
    elif n==7:
        g=p.box('episode',24,124,358,310,p.tint,26)
        p.text('episode_tag','THE DAILY AUDIO',44,145,318,11,700,p.muted,g)
        p.chart('waveform',44,197,318,74,'wave',g)
        p.text('episode_title','The world, in focus.',44,301,318,27,700,parent=g)
        p.text('episode_meta','A 12-minute morning briefing',44,346,318,14,400,p.muted,g)
        p.button('play','Play episode',44,383,180,34,True,g)
        p.section('up_next','Up next',462)
        p.story('next',*STORIES[1],505);p.text('queue_note','New episodes every weekday.',24,659,358,13,400,p.muted)
    elif n==9:
        p.text('collection','SAVED FOR A SLOWER MOMENT',24,128,358,11,700,p.muted)
        for i,s in enumerate(STORIES[:3]):
            p.story('story_'+str(i),*s,174+i*158)
            p.box('progress_track_'+str(i),44,303+i*158,318,3,p.tint,1)
            p.box('progress_'+str(i),44,303+i*158,[210,90,40][i],3,p.accent,1)
    else:
        g=p.box('briefing',24,120,358,240,p.tint)
        p.text('lead_tag','THE BIG PICTURE',44,144,318,11,700,p.muted,g)
        p.text('lead_title','A new season',44,191,318,34,700,parent=g)
        p.text('lead_title2','for small business',44,240,318,30,700,parent=g)
        p.text('lead_meta','Analysis · 7 min read',44,314,318,12,400,p.muted,g)
        p.metric('markets','Markets','In focus',24,387,171,108);p.metric('ideas','Ideas','What is next',211,387,171,108)
        p.story('latest',*STORIES[3],534)
    p.button('primary','Your reading list' if n!=9 else 'Continue reading');return p

QUOTES=[('AAPL','Apple','182.40','+1.24%'),('NVDA','NVIDIA','124.80','+2.16%'),('MSFT','Microsoft','416.20','+0.83%')]
def stock(n):
    titles=['Portfolio','Watchlist','Market tiles','Apple','Market overview','Your allocation','Today’s movers','Compare','Holdings','Opening bell']
    directions=['Portfolio overview with large balance, area chart and two stock rows.',
      'Dark watchlist-first dashboard: compact market index summary then tall stock list.',
      'Two-column market tile grid with mini line charts inside each company card.',
      'Single security detail: oversized share price, full-width chart, compact metrics.',
      'Market dashboard with three index summaries and a large market trend chart.',
      'Allocation dashboard: large donut graphic, asset-class legend and total value.',
      'Ranked movers list, positive change badges and one featured company.',
      'Two-security comparison: paired quote cards, dual line chart and metric grid.',
      'Ledger-inspired holdings layout: large total, column headings and separated rows.',
      'Editorial market briefing with a headline, index cards and a short watchlist.']
    p=Page('stock',n,titles[n-1],directions[n-1]);p.header(eyebrow='Design fixture · Prices are illustrative')
    if n==1:
        g=p.box('portfolio',24,119,358,290,p.tint)
        p.text('balance_label','TOTAL VALUE',44,140,318,11,700,p.muted,g)
        p.text('balance','$42,860.24',44,174,318,43,700,parent=g)
        p.text('gain','+$842.16  (2.01%) today',44,238,318,13,500,p.accent,g)
        p.chart('portfolio_chart',44,284,318,96,'line',g)
        p.section('watchlist_title','Watchlist',438)
        for i,q in enumerate(QUOTES[:2]):p.quote('quote_'+str(i),*q,480+i*91)
    elif n in (2,7):
        g=p.box('summary',24,122,358,138,p.tint)
        p.text('summary_label','S&P 500' if n==2 else 'LEADING TODAY',44,145,318,12,700,p.muted,g)
        p.text('summary_value','5,420.18' if n==2 else 'NVIDIA +2.16%',44,184,318,36,700,parent=g)
        p.section('list_title','Your stocks' if n==2 else 'Top gainers',294)
        rows=QUOTES+[('GOOGL','Alphabet','165.30','+0.62%')]
        for i,q in enumerate(rows):p.quote('quote_'+str(i),*q,338+i*84)
    elif n==3:
        for i,q in enumerate(QUOTES+[('GOOGL','Alphabet','165.30','+0.62%')]):
            x=24+(i%2)*187;y=126+(i//2)*230;g=p.box('tile_'+str(i),x,y,171,210,p.tint if i==0 else p.panel)
            p.text('symbol_'+str(i),q[0],x+16,y+15,139,20,700,parent=g)
            p.text('price_'+str(i),'$'+q[2],x+16,y+54,139,25,700,parent=g)
            p.chart('chart_'+str(i),x+16,y+105,139,52,'line',g)
            p.text('gain_'+str(i),q[3],x+16,y+176,139,13,500,p.accent,g)
        p.text('note','Four companies. One clear view.',24,636,358,16,500,p.muted)
    elif n==4:
        p.text('symbol','AAPL · NASDAQ',24,128,358,12,700,p.muted)
        p.text('price','$182.40',24,164,358,62,700);p.text('gain','+2.24  (1.24%) today',24,255,358,15,500,p.accent)
        g=p.box('chart_panel',24,305,358,204);p.chart('price_chart',42,323,322,148,'line',g)
        for i,label in enumerate(['1D','1W','1M','1Y']):p.text('period_'+str(i),label,44+i*83,480,60,11,700,p.accent if i==0 else p.muted,g,align=.5)
        p.metric('open','Open','$180.16',24,553);p.metric('volume','Volume','48.2M',211,553)
    elif n==5:
        for i,(label,value) in enumerate([('S&P 500','5,420'),('NASDAQ','17,132'),('DOW','39,420')]):
            g=p.box('index_'+str(i),24+i*122,126,114,124,p.tint if i==0 else p.panel)
            p.text('index_label_'+str(i),label,36+i*122,143,90,10,700,p.muted,g)
            p.text('index_value_'+str(i),value,36+i*122,180,90,22,700,parent=g)
            p.text('index_gain_'+str(i),'+0.82%',36+i*122,218,90,11,500,p.accent,g)
        p.section('trend_title','Market trend',285)
        g=p.box('trend',24,332,358,212);p.chart('market_chart',44,355,318,162,'line',g)
        p.quote('quote',*QUOTES[0],578)
    elif n==6:
        p.text('balance','$42,860.24',24,122,358,40,700)
        p.text('allocation_note','A balanced view of your investments',24,180,358,13,400,p.muted)
        g=p.box('allocation',24,225,358,248);p.chart('donut',109,246,188,188,'donut',g)
        for i,(label,value) in enumerate([('Stocks','64%'),('Funds','28%'),('Cash','8%')]):
            y=507+i*58;p.box('swatch_'+str(i),24,y+4,12,12,p.accent if i==0 else p.muted if i==1 else p.tint,3)
            p.text('class_'+str(i),label,50,y,200,18,500);p.text('share_'+str(i),value,278,y,104,20,700,align=1)
    elif n==8:
        for i,q in enumerate(QUOTES[:2]):
            g=p.box('compare_'+str(i),24+i*187,127,171,142,p.tint if i==0 else p.panel)
            p.text('symbol_'+str(i),q[0],40+i*187,145,139,19,700,parent=g)
            p.text('price_'+str(i),'$'+q[2],40+i*187,187,139,26,700,parent=g)
            p.text('change_'+str(i),q[3],40+i*187,235,139,12,500,p.accent,g)
        p.section('performance_title','Relative performance',302)
        g=p.box('comparison',24,348,358,204);p.chart('comparison_chart',44,370,318,158,'compare',g)
        p.metric('apple_return','Apple / 1 month','+4.2%',24,584);p.metric('nvidia_return','NVIDIA / 1 month','+8.6%',211,584)
    elif n==9:
        p.text('balance_label','TOTAL HOLDINGS',24,130,358,11,700,p.muted)
        p.text('balance','$42,860.24',24,166,358,44,700)
        p.text('asset_header','ASSET',24,265,180,11,700,p.muted);p.text('value_header','VALUE / CHANGE',210,265,172,11,700,p.muted,align=1)
        for i,q in enumerate(QUOTES+[('GOOGL','Alphabet','165.30','+0.62%')]):p.quote('holding_'+str(i),*q,309+i*87)
    else:
        g=p.box('briefing',24,123,358,248,p.tint,26)
        p.text('briefing_tag','MONDAY MARKET BRIEF',44,146,318,11,700,p.muted,g)
        p.text('headline','A steady start.',44,194,318,35,700,parent=g)
        p.text('headline2','A wider perspective.',44,246,318,27,700,parent=g)
        p.text('briefing_meta','Your watchlist, in context.',44,323,318,13,400,p.muted,g)
        p.metric('index','S&P 500','+0.82%',24,402);p.metric('tech','NASDAQ','+1.16%',211,402)
        p.section('watchlist_title','On your radar',531);p.quote('quote',*QUOTES[0],578)
    p.button('primary','View watchlist' if n!=2 else 'Add a symbol');return p

def main():
    docs=[fn(n).save() for fn in (weather,news,stock) for n in range(1,11)]
    index=[{k:d[k] for k in ('id','app','number','title','structure')} for d in docs]
    (HERE/'catalogue.json').write_text(json.dumps(index,indent=2)+'\n')
    print(f'Authored {len(docs)} distinct layout contracts and image prompts.')

if __name__=='__main__':main()
