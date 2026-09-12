"""Host-owned comparisons. These are explicit planning heuristics, not medical scoring."""
from datetime import datetime

AQI_GUIDANCE = 'https://www.airnow.gov/aqi/aqi-basics/'

def indoor_plan(plan, facts):
    """A conservative exercise plan when no forecast day clears the AQI rule."""
    cities = facts['cities']
    if plan['family'] != 'outdoor' or len(cities) != 1 or not cities[0]['all_dates_have_unhealthy_air']:
        return None
    city = cities[0]; days = city['days']; ids = city['source_ids']
    span = f"{days[0]['date']}–{days[-1]['date']}"
    lo = min(d['max_us_aqi'] for d in days); hi = max(d['max_us_aqi'] for d in days)
    if plan['language'] == 'zh-CN':
        summary = '预报每日最高 US AQI 均超过150；本次安排优先选择室内运动，减少长时间或高强度户外活动。'
        picks = [('优先室内运动', '把计划中的跑步或长时间户外活动改为室内活动。天气晴好不能抵消空气污染风险。'),
            ('预报依据', f'{span}，预报每日最高 US AQI 为{lo}–{hi}。这是模型预报，不能当作全天或某时段的实测值。'),
            ('出发前重新确认', '查看当地最新空气质量与天气。现有每日最高值无法支持选择一个空气更好的具体时段。')]
        limitations = '采用保守的行程规则；每日最高 AQI 不能代表每一小时的空气质量。'
    else:
        summary = 'Forecast daily maximum US AQI exceeds 150 throughout this plan. Prefer indoor activities and reduce long or intense outdoor exertion.'
        picks = [('Choose an indoor alternative', 'Move planned exercise or prolonged outdoor activities indoors. Low rain probability does not remove the air-quality concern.'),
            ('What the forecast shows', f'{span}: modeled daily maximum US AQI is {lo}–{hi}. These forecasts do not describe every hour or establish current measured exposure.'),
            ('Recheck before leaving', 'Check current local air quality and weather. Daily maxima cannot identify a specific hour with better air quality.')]
        limitations = 'Conservative planning rule; modeled daily maximum AQI is not an hourly exposure measurement.'
    return {'summary': summary, 'picks': [{'title': t, 'body': b, 'source_ids': ids} for t, b in picks], 'limitations': limitations}

def comparisons(evidence):
    ready = [e for e in evidence if e['status'] == 'ready']
    air = {e['data']['place']: e for e in ready if e['kind'] == 'air'}
    cities, dates = [], {}
    for e in ready:
        if e['kind'] != 'weather':
            continue
        d = e['data']; name = d['place']['name']; rows = []
        a = air.get(name)
        for day in d['days']:
            row = dict(day)
            row['daylight_minutes'] = int((datetime.fromisoformat(day['sunset']) - datetime.fromisoformat(day['sunrise'])).total_seconds() / 60)
            row['max_us_aqi'] = a['data']['forecast_daily_max_us_aqi'].get(day['date']) if a else None
            aqi = row['max_us_aqi']
            row['activity_note'] = ('Prefer an indoor alternative; reduce long or intense outdoor activity' if aqi is not None and aqi > 150
                else 'Sensitive groups should reduce prolonged or intense outdoor activity' if aqi is not None and aqi > 100
                else 'Recheck local conditions before leaving')
            row['heat_note'] = 'Plan shade, breaks and cooler hours; do not describe this high as mild' if day['high_c'] >= 30 else ''
            row['rain_note'] = 'Keep an indoor backup' if day['rain_probability_pct'] >= 40 else 'Lower rain probability is not a guarantee of no rain'
            rows.append(row); dates.setdefault(day['date'], []).append({'city': name, **row})
        if not rows:
            continue
        eligible = [r for r in rows if r['max_us_aqi'] is None or r['max_us_aqi'] <= 150]
        lowest = min(r['rain_probability_pct'] for r in rows)
        choice = min(eligible, key=lambda r: (r['rain_probability_pct'], r['high_c'] >= 30, r['wind_kmh'])) if eligible else None
        cities.append({'city': name, 'source_ids': [e['id']] + ([a['id']] if a else []),
            'lowest_rain_dates': [r['date'] for r in rows if r['rain_probability_pct'] == lowest],
            'lowest_rain_probability_pct': lowest, 'preferred_outdoor_date': choice['date'] if choice else None,
            'all_dates_have_unhealthy_air': not eligible, 'days': rows})
    daily_comparisons = []
    for date, rows in dates.items():
        if len(rows) < 2:
            continue
        values = {'date': date}
        for field, label, use_max in [('rain_probability_pct', 'lowest_rain_cities', False), ('high_c', 'cooler_high_cities', False), ('daylight_minutes', 'longest_daylight_cities', True), ('max_us_aqi', 'lowest_aqi_cities', False)]:
            present = [r for r in rows if r[field] is not None]
            if len(present) == len(rows):
                best = (max if use_max else min)(r[field] for r in present)
                values[label] = [r['city'] for r in present if r[field] == best]
        daily_comparisons.append(values)
    quotes = [e['data'] for e in ready if e['kind'] == 'quote']
    return {'cities': cities, 'same_date_comparisons': daily_comparisons,
        'quote_change_order': [q['ticker'] for q in sorted(quotes, key=lambda q: -q['change_pct'])],
        'rules': ['Outdoor-date preference excludes days with forecast maximum US AQI above 150, then ranks rain probability, heat and wind. This is a conservative planning heuristic using daily maxima, not an hourly safety guarantee.',
            'Equal values are ties. Sunset clock time is not daylight duration. Never infer volatility, a trend, valuation or investment merit from one session or nominal share prices.',
            'A daily high of 30 C or more requires heat planning; humidity and heat index were not retrieved.'],
        'aqi_category_reference': AQI_GUIDANCE}
