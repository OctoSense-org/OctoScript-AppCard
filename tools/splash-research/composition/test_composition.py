"""Regression checks for actual scheduling and the mistakes found in live review."""
import json
from pathlib import Path
import select
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import adapters
import cards
import decisions
import model
import run

BIN = Path(__file__).resolve().parents[1] / 'target/release/composition-vm'

class VmTests(unittest.TestCase):
    def start(self, count=3):
        p = subprocess.Popen([str(BIN)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0)
        self.addCleanup(self.close, p)
        jobs = [{'id': str(i), 'kind': 'weather', 'params': {}} for i in range(count)]
        self.send(p, {'jobs': jobs, 'intent': 'test', 'plan': {}, 'output_schema': {'type': 'object', 'required': ['ok'], 'properties': {'ok': {'type': 'boolean'}}, 'additionalProperties': False}})
        return p

    @staticmethod
    def close(p):
        if p.poll() is None:
            p.kill()
        p.communicate(timeout=3)

    @staticmethod
    def send(p, value):
        p.stdin.write((json.dumps(value) + '\n').encode())
        p.stdin.flush()

    def receive(self, p):
        self.assertTrue(select.select([p.stdout], [], [], 3)[0], 'VM response timed out')
        line = p.stdout.readline()
        self.assertTrue(line, 'VM exited without a response')
        return json.loads(line)

    def test_parallel_fetch_and_out_of_order_completion(self):
        p = self.start()
        calls = [self.receive(p) for _ in range(3)]
        self.assertEqual([c['tool'] for c in calls], ['composition.fetch'] * 3)
        # No result was sent before all three fetches were issued.
        for i in [2, 1, 0]:
            self.send(p, {'reply': calls[i]['invoke'], 'output': {'id': str(i), 'status': 'failed' if i == 1 else 'ready'}})
        synth = self.receive(p)
        self.assertEqual(synth['tool'], 'composition.synthesize')
        self.assertEqual([e['id'] for e in synth['input']['evidence']], ['0', '1', '2'])
        self.assertEqual(synth['input']['evidence'][1]['status'], 'failed')
        self.send(p, {'reply': synth['invoke'], 'output': {'ok': True}})
        self.assertEqual(self.receive(p)['done']['answer'], {'ok': True})
        self.assertEqual(p.wait(timeout=3), 0)

    def test_unknown_reply_rejected(self):
        p = self.start(1)
        self.receive(p)
        self.send(p, {'reply': 'unadmitted', 'output': {}})
        self.assertNotEqual(p.wait(timeout=3), 0)
        self.assertIn(b'unknown/duplicate', p.stderr.read())

    def test_output_schema_rejected(self):
        p = self.start(1)
        call = self.receive(p)
        self.send(p, {'reply': call['invoke'], 'output': {'id': '0'}})
        synth = self.receive(p)
        self.send(p, {'reply': synth['invoke'], 'output': {'wrong': 'shape'}})
        self.assertNotEqual(p.wait(timeout=3), 0)

    def test_source_budget(self):
        p = self.start(9)
        self.assertNotEqual(p.wait(timeout=3), 0)


def weather(city, rain=(80, 61)):
    return {'id': 'weather_' + city, 'kind': 'weather', 'status': 'ready', 'data': {
        'place': {'name': city}, 'days': [{'date': f'2026-09-{12+i}', 'high_c': 31, 'low_c': 25,
        'rain_probability_pct': n, 'wind_kmh': 10, 'sunrise': f'2026-09-{12+i}T06:00',
        'sunset': f'2026-09-{12+i}T18:30'} for i, n in enumerate(rain)]}}

class DecisionTests(unittest.TestCase):
    def test_rain_order_and_aqi_ties(self):
        facts = decisions.comparisons([weather('Singapore')])
        self.assertEqual(facts['cities'][0]['preferred_outdoor_date'], '2026-09-13')
        self.assertEqual(facts['cities'][0]['lowest_rain_probability_pct'], 61)

    def test_unhealthy_air_blocks_weather_only_running_advice(self):
        air = {'id': 'air', 'kind': 'air', 'status': 'ready', 'data': {'place': 'Beijing',
            'forecast_daily_max_us_aqi': {'2026-09-12': 161, '2026-09-13': 159}}}
        facts = decisions.comparisons([weather('Beijing', (0, 2)), air])
        self.assertIsNone(facts['cities'][0]['preferred_outdoor_date'])
        answer = decisions.indoor_plan({'family': 'outdoor', 'language': 'zh-CN'}, facts)
        self.assertIn('室内运动', answer['summary'])
        self.assertIn('air', answer['picks'][0]['source_ids'])

    def test_daylight_duration_not_sunset_clock(self):
        a, b = weather('Tokyo', (31, 15)), weather('Kyoto', (30, 86))
        for row in b['data']['days']:
            row['sunrise'] = row['date'] + 'T07:00'
            row['sunset'] = row['date'] + 'T19:00'
        facts = decisions.comparisons([a, b])
        self.assertEqual(facts['same_date_comparisons'][0]['lowest_rain_cities'], ['Kyoto'])
        self.assertEqual(facts['same_date_comparisons'][1]['lowest_rain_cities'], ['Tokyo'])
        self.assertEqual(facts['same_date_comparisons'][0]['longest_daylight_cities'], ['Tokyo'])

    def test_explicit_this_week_overrides_model_weekend(self):
        plan = {'title': 'Beijing', 'family': 'travel', 'cities': ['Beijing'], 'tickers': [], 'horizon': 'weekend'}
        with patch.object(model, 'call', return_value=(json.dumps(plan), {})):
            p, timing = model.plan('Beijing tour this week')
        self.assertEqual(p['horizon'], 'this_week')
        self.assertEqual(timing['corrections']['horizon']['model'], 'weekend')

    def test_unknown_evidence_citation_rejected(self):
        bad = {'summary': 'x', 'limitations': '', 'picks': [{'title': 'x', 'body': 'x', 'source_ids': ['invented']}] * 3}
        with patch.object(model, 'call', return_value=(json.dumps(bad), {})):
            with self.assertRaisesRegex(ValueError, 'Unknown source'):
                model.synthesize({'plan': {'family': 'market'}, 'evidence': [{'id':'actual','status':'failed'}]})

    def test_quote_uses_previous_bar_not_five_day_baseline(self):
        raw = {'chart': {'result': [{'meta': {'symbol': 'TEST', 'regularMarketPrice': 110,
            'regularMarketTime': 300, 'currency': 'USD', 'chartPreviousClose': 80},
            'timestamp': [100, 200, 300], 'indicators': {'quote': [{'close': [90, 100, 110]}]}}]}}
        with patch.object(adapters, 'fetch', return_value=json.dumps(raw).encode()):
            result = adapters.Adapters().run({'id': 'q', 'kind': 'quote', 'params': {'ticker': 'TEST'}})
        self.assertEqual(result['data']['previous_close'], 100)
        self.assertAlmostEqual(result['data']['change_pct'], 10)

    def test_templates_compile_and_empty_link_is_guarded(self):
        with tempfile.TemporaryDirectory() as tmp:
            for family in ['travel', 'outdoor', 'compare', 'briefing', 'market']:
                path = Path(tmp) / (family + '.card')
                path.write_text(cards.template('test', {'family': family}))
                valid, why = cards.check(path)
                self.assertTrue(valid, why)
                self.assertIn('when facts.url1 != ""', path.read_text())

    def test_adapters_refuse_unapproved_host(self):
        with self.assertRaisesRegex(ValueError, 'Unapproved source'):
            adapters.fetch('https://localhost/internal')

if __name__ == '__main__':
    unittest.main()
