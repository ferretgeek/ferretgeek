"""Render the "Activity / 足迹" cards from live GitHub data.

Runs in GitHub Actions with the standard library only. Text is drawn from
pre-outlined glyphs in glyphs.json (built locally by the design tools), so the
workflow needs no font files: fixed labels are stored as whole strings, and
numbers / repository / language names are composed from per-character glyphs.

Usage: GITHUB_TOKEN=... python scripts/stats.py [--from-json assets/stats/stats.json]
"""
from __future__ import annotations

import datetime as dt
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLYPHS = json.loads((Path(__file__).with_name('glyphs.json')).read_text(encoding='utf-8'))
OUT = ROOT / 'assets' / 'stats'
USER = 'ferretgeek'

# Fixed labels. tools/bake_stats.py outlines exactly these strings.
STRINGS = {
    'zh': {
        'projects': '开源项目', 'projects_note': '公开仓库，不含主页',
        'stars': '获得星标', 'stars_note': '最多：',
        'contrib': '近一年贡献', 'streak_pre': '最长连续 ', 'streak_post': ' 天',
        'since': '始于', 'years_pre': '在 GitHub 上的第 ', 'years_post': ' 年',
        'ink': '墨迹', 'ink_note': '近一年的每日贡献', 'legend': ['清', '淡', '重', '浓', '焦'],
        'langs': '语言', 'langs_note': '按代码量统计', 'other': '其他', 'updated': '更新于 ',
        'weekdays': ['一', '三', '五'], 'months': [f'{m}月' for m in range(1, 13)],
    },
    'en': {
        'projects': 'Open-source projects', 'projects_note': 'Public repositories',
        'stars': 'Stars earned', 'stars_note': 'Most: ',
        'contrib': 'Contributions', 'streak_pre': 'Longest streak: ', 'streak_post': ' days',
        'since': 'On GitHub since', 'years_pre': 'Year ', 'years_post': ' on GitHub',
        'ink': 'Ink trail', 'ink_note': 'Daily contributions, past year', 'legend': ['Less', '', '', '', 'More'],
        'langs': 'Languages', 'langs_note': 'By code size', 'other': 'Other', 'updated': 'Updated ',
        'weekdays': ['Mon', 'Wed', 'Fri'], 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                                                      'Sep', 'Oct', 'Nov', 'Dec'],
    },
}
# style -> used for both baked strings and per-character composition
STYLES = {
    'num': ('light', 50), 'label': ('medium', 15), 'note': ('regular', 12.5), 'title': ('semibold', 16),
    'small': ('regular', 12), 'tiny': ('medium', 11),
}
LANG_COLORS = {
    'light': ['#2B2622', '#B2352A', '#4A6670', '#A0703C', '#6F8B6E', '#C09A4A', '#A79C8C'],
    'dark': ['#E6DCC8', '#D65A43', '#7FA0A8', '#C99562', '#90AE8E', '#D8B866', '#6E665A'],
}
INK_LEVELS = {'NONE': 0, 'FIRST_QUARTILE': 1, 'SECOND_QUARTILE': 2, 'THIRD_QUARTILE': 3, 'FOURTH_QUARTILE': 4}

QUERY = """query($login: String!) { user(login: $login) {
  createdAt
  repositories(ownerAffiliations: OWNER, privacy: PUBLIC, isFork: false, first: 100) { nodes {
    name stargazerCount forkCount isArchived
    languages(first: 20, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name } } } } }
  contributionsCollection { contributionCalendar { totalContributions
    weeks { contributionDays { date contributionCount contributionLevel weekday } } } } } }"""


# ------------------------------------------------------------------ data
def fetch() -> dict:
    token = os.environ['GITHUB_TOKEN']
    req = urllib.request.Request('https://api.github.com/graphql',
                                 data=json.dumps({'query': QUERY, 'variables': {'login': USER}}).encode(),
                                 headers={'Authorization': f'bearer {token}', 'User-Agent': 'profile-stats'})
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = json.load(resp)
    if 'errors' in body:
        raise RuntimeError(body['errors'])
    return body['data']['user']


def summarize(user: dict, today: dt.date) -> dict:
    repos = [r for r in user['repositories']['nodes'] if r['name'] != USER]
    langs: dict[str, int] = {}
    for r in repos:
        for e in r['languages']['edges']:
            langs[e['node']['name']] = langs.get(e['node']['name'], 0) + e['size']
    total = sum(langs.values()) or 1
    ranked = sorted(langs.items(), key=lambda kv: -kv[1])
    top = [{'name': n, 'share': s / total} for n, s in ranked[:6]]
    rest = sum(s for _, s in ranked[6:]) / total
    if rest > 0:
        top.append({'name': None, 'share': rest})
    cal = user['contributionsCollection']['contributionCalendar']
    days = [d for w in cal['weeks'] for d in w['contributionDays']]
    streak = best = 0
    for d in days:
        streak = streak + 1 if d['contributionCount'] > 0 else 0
        best = max(best, streak)
    starred = max(repos, key=lambda r: r['stargazerCount'])
    created = dt.date.fromisoformat(user['createdAt'][:10])
    since = created.year
    full_years = today.year - created.year - ((today.month, today.day) < (created.month, created.day))
    return {
        'updated': today.isoformat(),
        'projects': len(repos),
        'stars': sum(r['stargazerCount'] for r in repos),
        'forks': sum(r['forkCount'] for r in repos),
        'top_repo': {'name': starred['name'], 'stars': starred['stargazerCount']},
        'contributions': cal['totalContributions'],
        'longest_streak': best,
        'since': since,
        'year_on_github': full_years + 1,
        'languages': top,
        'weeks': [[[d['date'], d['contributionCount'], INK_LEVELS[d['contributionLevel']]]
                   for d in w['contributionDays']] for w in cal['weeks']],
        'first_weekday': cal['weeks'][0]['contributionDays'][0]['weekday'],
    }


# ------------------------------------------------------------------ drawing
class Doc:
    def __init__(self, w: float, h: float, title: str):
        self.w, self.h, self.title = w, h, title
        self.defs: list[str] = []
        self.body: list[str] = []
        self.used: set[str] = set()

    def _glyph(self, key: str) -> None:
        if key not in self.used:
            self.used.add(key)
            self.defs.append(f'<path id="{key}" d="{GLYPHS["glyphs"][key]}"/>')

    def _placements(self, lang: str, style: str, text: str):
        """[(key, x_em, scale_em)], width_em — whole baked string, else per character."""
        baked = GLYPHS['strings'].get(f'{lang}|{style}|{text}')
        if baked:
            return baked['g'], baked['w']
        chars = GLYPHS['chars'][style]
        out, pen = [], 0.0
        for ch in text:
            if ch not in chars:  # never fail the workflow over an unexpected name
                print(f'warning: no glyph for {ch!r} in style {style}', file=sys.stderr)
                ch = '?'
            key, adv, scale = chars[ch]
            if key:
                out.append([key, pen, scale])
            pen += adv
        return out, pen

    def width(self, lang: str, style: str, text: str, size: float | None = None) -> float:
        return self._placements(lang, style, text)[1] * (size or STYLES[style][1])

    def text(self, x: float, y: float, text: str, lang: str, style: str, fill: str,
             anchor: str = 'start', size: float | None = None) -> float:
        size = size or STYLES[style][1]
        glyphs, w_em = self._placements(lang, style, text)
        width = w_em * size
        if anchor == 'middle':
            x -= width / 2
        elif anchor == 'end':
            x -= width
        uses = []
        for key, gx, scale in glyphs:
            self._glyph(key)
            uses.append(f'<use href="#{key}" transform="translate({x + gx * size:.2f} {y:.2f}) scale({scale * size:.5f})"/>')
        self.body.append(f'<g fill="{fill}">' + ''.join(uses) + '</g>')
        return width

    def add(self, s: str) -> None:
        self.body.append(s)

    def render(self) -> str:
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                f'viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{self.title}">\n'
                f'<title>{self.title}</title>\n<defs>{"".join(self.defs)}</defs>\n'
                + '\n'.join(self.body) + '\n</svg>\n')


def fmt(n: int) -> str:
    return f'{n:,}'


def card(stats: dict, lang: str, theme: str) -> str:
    t = GLYPHS['themes'][theme]
    S = STRINGS[lang]
    W, H = 1000, 546
    doc = Doc(W, H, 'GitHub 足迹' if lang == 'zh' else 'GitHub activity')
    doc.defs.append(f'<pattern id="tx" width="144" height="144" patternUnits="userSpaceOnUse">'
                    f'<image href="{t["texture"]}" width="144" height="144"/></pattern>')
    doc.add(f'<rect width="{W}" height="{H}" rx="20" fill="{t["paper"]}"/>'
            f'<rect width="{W}" height="{H}" rx="20" fill="url(#tx)"/>'
            f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="20" fill="none" stroke="{t["line"]}"/>')

    # metrics row -------------------------------------------------------
    col = (W - 96) / 4
    metrics = [
        (fmt(stats['projects']), S['projects'], [(S['projects_note'], 'fixed')]),
        (fmt(stats['stars']), S['stars'], [(S['stars_note'], 'fixed'),
                                           (f'{stats["top_repo"]["name"]} {stats["top_repo"]["stars"]}', 'ascii')]),
        (fmt(stats['contributions']), S['contrib'], [(S['streak_pre'], 'fixed'), (str(stats['longest_streak']), 'ascii'),
                                                     (S['streak_post'], 'fixed')]),
        (str(stats['since']), S['since'], [(S['years_pre'], 'fixed'), (str(stats['year_on_github']), 'ascii'),
                                           (S['years_post'], 'fixed')]),
    ]
    for i, (value, label, note) in enumerate(metrics):
        x = 48 + col * i + (24 if i else 0)
        if i:
            doc.add(f'<path d="M{48 + col * i:.1f} 44V150" stroke="{t["line2"]}"/>')
        doc.text(x - 2, 96, value, lang, 'num', t['ink'])
        doc.text(x, 126, label, lang, 'label', t['ink2'])
        nx = x
        for part, kind in note:
            nx += doc.text(nx, 150, part, lang, 'note', t['ink3'])

    # ink heatmap -------------------------------------------------------
    y0 = 196
    doc.add(f'<path d="M48 176H{W - 48}" stroke="{t["line"]}"/>')
    tw = doc.text(48, y0 + 22, S['ink'], lang, 'title', t['ink'])
    doc.text(48 + tw + 14, y0 + 22, S['ink_note'], lang, 'note', t['ink3'])
    cell, gap = 12.5, 3.5
    step = cell + gap
    weeks = stats['weeks']
    gx0 = W - 48 - len(weeks) * step + gap
    gy0 = y0 + 62
    ink = t['ink']
    alpha = [None, .2, .42, .68, .95]
    last_month = None
    for wi, week in enumerate(weeks):
        for date, count, level in week:
            wd = dt.date.fromisoformat(date).isoweekday() % 7  # Sunday = 0
            x, y = gx0 + wi * step, gy0 + wd * step
            if level == 0:
                doc.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell}" height="{cell}" rx="3" fill="{t["line2"]}"/>')
            else:
                doc.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell}" height="{cell}" rx="3" fill="{ink}" '
                        f'fill-opacity="{alpha[level]}"><title>{date}: {count}</title></rect>')
        month = int(week[0][0][5:7])
        if month != last_month and wi < len(weeks) - 2:
            if last_month is not None or dt.date.fromisoformat(week[0][0]).day <= 7:
                doc.text(gx0 + wi * step, gy0 - 10, S['months'][month - 1], lang, 'tiny', t['ink3'])
            last_month = month
    for label, wd in zip(S['weekdays'], (1, 3, 5)):
        doc.text(gx0 - 10, gy0 + wd * step + cell - 2, label, lang, 'tiny', t['ink3'], anchor='end')
    # legend: 清 淡 重 浓 焦 (five shades of ink)
    lx = W - 48
    ly = y0 + 22
    for level in range(4, -1, -1):
        name = S['legend'][level]
        if name:
            lx -= doc.width(lang, 'tiny', name) + 4
            doc.text(lx, ly, name, lang, 'tiny', t['ink3'])
            lx -= 8
        lx -= cell
        fill = t['line2'] if level == 0 else ink
        op = '' if level == 0 else f' fill-opacity="{alpha[level]}"'
        doc.add(f'<rect x="{lx:.1f}" y="{ly - cell + 2:.1f}" width="{cell}" height="{cell}" rx="3" fill="{fill}"{op}/>')
        lx -= 6 if name == '' else 12

    # languages ---------------------------------------------------------
    y1 = gy0 + 7 * step + 34
    doc.add(f'<path d="M48 {y1:.1f}H{W - 48}" stroke="{t["line"]}"/>')
    tw = doc.text(48, y1 + 42, S['langs'], lang, 'title', t['ink'])
    doc.text(48 + tw + 14, y1 + 42, S['langs_note'], lang, 'note', t['ink3'])
    uw = doc.text(W - 48, y1 + 42, stats['updated'], lang, 'small', t['ink3'], anchor='end')
    doc.text(W - 48 - uw - 2, y1 + 42, S['updated'], lang, 'note', t['ink3'], anchor='end', size=12)
    bx, bw, by = 48, W - 96, y1 + 62
    colors = LANG_COLORS[theme]
    doc.defs.append(f'<clipPath id="bar"><rect x="{bx}" y="{by}" width="{bw}" height="10" rx="5"/></clipPath>')
    segs, cx = [], bx
    for i, item in enumerate(stats['languages']):
        w = bw * item['share']
        segs.append(f'<rect x="{cx:.2f}" y="{by}" width="{w + .6:.2f}" height="10" fill="{colors[min(i, len(colors) - 1)] if item["name"] else colors[-1]}"/>')
        cx += w
    doc.add(f'<g clip-path="url(#bar)">' + ''.join(segs) + '</g>')
    lx, ly = bx, by + 42
    for i, item in enumerate(stats['languages']):
        color = colors[min(i, len(colors) - 1)] if item['name'] else colors[-1]
        name = item['name'] or S['other']
        pct = f'{item["share"] * 100:.1f}%'
        doc.add(f'<circle cx="{lx + 5:.1f}" cy="{ly - 4.5:.1f}" r="4.5" fill="{color}"/>')
        nw = doc.text(lx + 16, ly, name, lang, 'note' if item['name'] is None else 'small', t['ink2'], size=13)
        pw = doc.text(lx + 16 + nw + 7, ly, pct, lang, 'small', t['ink3'], size=13)
        lx += 16 + nw + 7 + pw + 30
    return doc.render()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if '--from-json' in sys.argv:
        stats = json.loads(Path(sys.argv[sys.argv.index('--from-json') + 1]).read_text(encoding='utf-8'))
    else:
        stats = summarize(fetch(), dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date())
        (OUT / 'stats.json').write_text(json.dumps(stats, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for lang in ('zh', 'en'):
        for theme in ('light', 'dark'):
            (OUT / f'{lang}-{theme}.svg').write_text(card(stats, lang, theme), encoding='utf-8')
    print(f'stats: {stats["projects"]} projects, {stats["stars"]} stars, {stats["contributions"]} contributions')


if __name__ == '__main__':
    main()
