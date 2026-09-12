"""Build a standalone gallery from sanitized octos-ohos-capture results."""
import argparse
import html
import json
from pathlib import Path


def build(root):
    records = []
    for path in root.glob('*/result.json'):
        r = json.loads(path.read_text())
        if r.get('superseded_by'):
            continue
        records.append(r)
    records.sort(key=lambda r: (['weather', 'news', 'stock'].index(r['name'].split('-')[0]), r['name']))
    cards, rows = [], []
    for r in records:
        name = r['name']
        first = next((m['elapsed_ms'] / 1000 for m in r['metrics'] if m['event'] == 'first_text'), None)
        total = r.get('generation_total_ms', sum(m.get('elapsed_ms', 0) for m in r['metrics'] if m['event'] == 'completed')) / 1000
        cached = sum(u.get('cache_read_tokens', 0) for u in r['provider_iterations'])
        prompt = sum(u.get('input_tokens', 0) + u.get('cache_read_tokens', 0) + u.get('cache_write_tokens', 0) for u in r['provider_iterations'])
        hit = f'{100 * cached / prompt:.1f}%' if prompt else 'unreported'
        status = 'Native structure checked' if r['structural_pass'] else 'Needs repair'
        esc = html.escape
        cards.append(f'''<article data-app="{name.split('-')[0]}">
<div class="caption"><h2>{esc(name.replace('-', ' '))}</h2><p>{esc(r['theme'])} · {r['native_descendants']} native descendants</p></div>
<div class="phone"><a href="{name}/screen.png"><img src="{name}/screen.png" alt="Native phone screenshot: {esc(name)}" loading="lazy"></a></div>
<div class="caption"><p><b>{total:.1f}s</b> generation including repairs · {hit} input cached</p>
<p>{status}. {esc(r.get('visual_review', 'pending'))}</p>
<details><summary>Prompt and evidence</summary><p>{esc(r['prompt'])}</p>
<a href="{name}/result.json">Measurements and differences</a> · <a href="{name}/WidgetTreeDump.json">Native hierarchy</a> · <a href="{name}/WidgetSnapshot.json">Bounds, text and state</a> · <a href="{name}/native.splash">Realized widgets</a></details></div></article>''')
        rows.append(f'<tr><td>{esc(name)}</td><td>{first:.1f}</td><td>{total:.1f}</td><td>{r.get("repair_rounds", 0)}</td><td>{hit}</td></tr>')
    page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Octos on Mate 70 Air — native theme variations</title><style>
*{box-sizing:border-box}body{margin:0;background:#f3f5f8;color:#172033;font:15px/1.5 system-ui,sans-serif}main{max-width:1440px;margin:auto;padding:32px}h1{font-size:32px;line-height:1.2}h2{font-size:17px;text-transform:capitalize;margin:0}p{margin:8px 0}a{color:#244fb2}header{max-width:900px;margin-bottom:28px}.filters{display:flex;gap:8px;margin:20px 0}.filters button{font:inherit;border:1px solid #bdc9d9;border-radius:24px;padding:7px 18px;background:white;cursor:pointer}.filters button[aria-pressed=true]{background:#172033;color:white}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px}article{background:white;border:1px solid #dce2ea;border-radius:16px;overflow:hidden}article[hidden]{display:none}.caption{padding:16px}.phone{height:620px;overflow:auto;background:#101114;margin:0 16px;border-radius:10px}.phone img{width:100%;display:block}details{font-size:13px}table{width:100%;border-collapse:collapse;background:white;margin:24px 0}td,th{text-align:left;border-bottom:1px solid #dae1e9;padding:10px}small{color:#546273}@media(max-width:600px){main{padding:16px}.phone{height:600px}.metrics{overflow:auto}}
</style><main><header><h1>Octos on Mate 70 Air</h1><p>Real native Makepad screenshots from context-driven generation. The model selects a theme and composes app widgets; these are not design mockups.</p><p>Weather, news and stock with Taskplan, Atro and Camo. Scroll inside a phone frame or open its screenshot at full size.</p><small>Times include automatic repair turns. Provider KV cache counters demonstrate reuse; latency also depends on inference mode, output length and network conditions. See <a href="README.md">the validation report</a>.</small></header>
<nav class="filters" aria-label="Filter app"><button aria-pressed="true" data-filter="all">All</button><button aria-pressed="false" data-filter="weather">Weather</button><button aria-pressed="false" data-filter="news">News</button><button aria-pressed="false" data-filter="stock">Stock</button></nav>
<section class="grid">''' + ''.join(cards) + '''</section><div class="metrics"><table><thead><tr><th>Context</th><th>First text (s)</th><th>Total (s)</th><th>Repairs</th><th>Input cached</th></tr></thead><tbody>''' + ''.join(rows) + '''</tbody></table></div></main><script>
document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('[data-filter]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));document.querySelectorAll('article').forEach(c=>c.hidden=b.dataset.filter!=='all'&&c.dataset.app!==b.dataset.filter)}));
</script></html>'''
    (root / 'index.html').write_text(page)
    print(f'{len(records)} captures: {root / "index.html"}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    build(parser.parse_args().directory)
