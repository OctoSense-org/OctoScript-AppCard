#!/usr/bin/env python3
"""Generate an L0 app card with a real GLM model, under one of our theme packs.

The phone's own kernel currently pins its provider, so this drives Z.ai
directly: app spec (a2app/apps/<app>/app.md) + the L0 rules + the pack name
in, one validated .card out, repaired against the real realize() gate.

    GLM_KEY_FILE=... python3 gen_glm.py --app weather --theme camo --out X.card
"""
import json
import pathlib
import subprocess
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
SPLASH = REPO / "splash"
ENDPOINT = "https://api.z.ai/api/coding/paas/v4/chat/completions"


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def glm(prompt, model, key, timeout=300):
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        # GLM 5.3 spends a large hidden reasoning budget before the first
        # visible token; 4000 returned empty content for a card-sized ask.
        "max_tokens": 16000,
    }).encode()
    req = urllib.request.Request(
        ENDPOINT, data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = json.load(r)
    msg = d["choices"][0]["message"]
    text = (msg.get("content") or "").strip()
    if not text:
        raise SystemExit(
            f"empty content (finish={d['choices'][0].get('finish_reason')}, "
            f"reasoning={len(msg.get('reasoning_content') or '')} chars) — raise max_tokens")
    return text


def validate(card_path):
    r = subprocess.run(
        ["cargo", "run", "-q", "-p", "splash-ui-l0", "--example", "l0validate",
         "--", str(card_path)],
        capture_output=True, text=True, cwd=SPLASH)
    try:
        d = json.loads(r.stdout)
        return d.get("ok", False), d.get("diagnostics", [])
    except Exception:
        return False, [(r.stdout or r.stderr)[:300]]


RULES = """你在写一张 Splash L0 卡片（生成式 UI 的声明式卡片语言）。硬规则：

- 头两行：`# level: L0` 和 `# model: {model_tag}`，然后一行 `theme {theme}`（深色）或 `theme {theme_light}`（浅色）。主题包已带调色板、字体、圆角、深度——绝不写颜色、字号、文件路径。
- 只能用这些构造器：Surface(pad) Panel Card(tint) Col(align,gap,width) Row(width,align,gap) Grid(cols) Rule() Space() Field(text,placeholder) Chip(text,active,tone,width) Icon(name,size) Avatar(text) Band(text) Bubble(text,side) Fab(name) TabBar Tab(icon,label,active) TextHero(text,value,unit) TextTitle(text,width) TextBody(text,width) TextRow(text,width) TextEyebrow(text) TextCaption(text,value,glyph,suffix,width) TextValue(value,unit,tint) TextStat(value,tint) Tile(label,value,unit,glyph,shape) Thumb(src,shape) WeatherIcon(cond,size) TempBar(lo,hi,min,max) SunArc(rise,set,now) MoonPhase(phase,illum)
- token 以点开头：width: .fill、align: .center、pad: .page、tone: .primary、size: .hero。
- 数据必须绑定，不能写字面量：先 `source <名字> <sys 调用>`，再用 `<名字>.<字段>` 填进 value/text。模型绝不写真实数值——温度、点赞数、时间都由运行时取。
- 文案（标题、按钮字、栏目名）可以写字面量字符串。
- `view root Surface(pad: .page) { ... }` 包住全部；可以拆出 `view <名字> Col(...) { ... }` 再在 root 里按名字引用。
- 图标用语义名：Icon(name: .bell)，名字用下划线不用连字符；size 只有 .hero / .row / .tile 三档。
- 循环写法固定：`for d, i in week.days key d.dayname { ... }`——必须有 index 变量和 key，身份不能来自位置。
- gap 是数字不是 token：`Col(gap: 8)`，不能写 `gap: .sm`。
- TextCaption 的 value 也必须是绑定路径；要显示静态文字用 text。
- tint 只接受绑定路径（表示涨跌符号），不接受 token；不需要就别写。
- Tile.shape 只有 .card / .square；Thumb.shape 只有 .wide / .square / .hero。
- 诊断里 “It offers: …” 列出的就是该源的全部字段，不要用列表外的字段。
- 只输出卡片源码，不要 markdown 围栏，不要解释。

可用的数据源与字段：
{sources}

应用规格：
{spec}

请为这个应用写一张完整的首屏卡片，结构对齐规格里描述的信息层级。"""

SOURCES = {
    "weather": (
        'source place sys.geocode(name: "上海")\n'
        '  → place.lat / place.lon\n'
        'source now sys.weather(lat: place.lat, lon: place.lon,\n'
        '                       fields: [temp, feels, hi, lo, cond, humidity, wind, uv])\n'
        '  → now.temp / now.feels / now.hi / now.lo / now.cond / now.humidity / now.wind\n'
        'source week sys.weather(lat: place.lat, lon: place.lon, days: 7,\n'
        '                        fields: [dayname, cond, hi, lo])\n'
        '  → 逐日列表：`for d, i in week.days key d.dayname { ... }`，用 d.dayname / d.cond / d.hi / d.lo\n'
        '注意 sys.weather 只接受 lat/lon/days/fields/aggregate/day，没有 city 参数；'
        '没有 sys.forecast 这个源。'),
    "news": (
        'source top sys.news(count: 10, fields: [id, title, author, points, comments, url])\n'
        '  → 逐条列表：`for n, i in top key n.id { ... }`，用 n.title / n.author / n.points / n.comments'),
}


def main():
    app = arg("--app", "weather")
    theme = arg("--theme", "camo")
    model = arg("--model", "glm-5.3-flash")
    out = pathlib.Path(arg("--out", f"glm_{app}_{theme}.card"))
    key = pathlib.Path(arg("--key-file",
                           str(pathlib.Path.home() / ".zai_key"))).read_text().strip()
    spec = (REPO / "a2app" / "apps" / app / "app.md").read_text()[:6000]
    # str.format would eat the card syntax's own braces; substitute literally.
    prompt = (RULES.replace("{model_tag}", f"{app}-app")
              .replace("{theme_light}", f"{theme}_light")
              .replace("{theme}", theme)
              .replace("{sources}", SOURCES.get(app, ""))
              .replace("{spec}", spec))

    src = glm(prompt, model, key).strip()
    if src.startswith("```"):
        src = src.split("```")[1].split("\n", 1)[-1]
    out.write_text(src.strip() + "\n")
    ok, diags = validate(out)
    for attempt in range(4):
        if ok:
            break
        print(f"repair {attempt + 1}: {diags[:2]}", flush=True)
        fix = glm(prompt + "\n\n上一版卡片：\n" + out.read_text()
                  + "\n\n校验失败，诊断：\n" + "\n".join(f"- {d}" for d in diags[:6])
                  + "\n\n只输出修好的完整卡片源码。", model, key).strip()
        if fix.startswith("```"):
            fix = fix.split("```")[1].split("\n", 1)[-1]
        out.write_text(fix.strip() + "\n")
        ok, diags = validate(out)
    print(f"{out}: {'valid' if ok else 'INVALID ' + str(diags[:2])}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
