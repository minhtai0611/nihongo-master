# -*- coding: utf-8 -*-
"""Rebuild the reference index (R16) as a faithful multi-column grid.

The First Edition prints R16 as newspaper columns: R16.1 (日本語索引) in three
columns of *term + Vietnamese gloss + page number*, R16.2 (ベトナム語索引) in two
columns of *Vietnamese gloss + Japanese form + page number*, with level markers
(N5/N4/N3/N2/N1/REF) standing alone in the first column.

A block extractor built for ruled tables linearises that only by accident, so
those seven pages are re-read here from the raw text lines (ir.json) and rebuilt
as one row per visual line, one cell per column.  Nothing is added, invented,
re-sorted or translated: every string placed in the grid comes from the page it
belongs to, in the order the page prints it.
"""
import json, re, os, collections

PAGES = (317, 318, 319, 320, 321, 322, 323)
ENTRY_MAX = 8.6            # pt; index entries are set at 7.4-8.5 pt
HEAD_MIN, HEAD_MAX = 9.0, 11.0   # pt; the R16.1 / R16.2 headings (h4)
WIDTH_MAX = 215.0          # pt; wider lines are prose, not index entries
ROW_TOL = 3.0              # pt; a page number sits 1.2 pt below its term
ANCHOR_MIN = 4             # rows needed before an x counts as a column edge
ANCHOR_TOL = 3.0           # pt; clustering tolerance for column edges
MIN_COL_GAP = 100.0        # pt; two columns are at least this far apart
NUM = re.compile(r'^[\d,\s]+$')
HEAD = re.compile(r'^R1[56]')


WITH_NEW_TERMS = True


def index_lines(page):
    return [L for L in page['lines']
            if L['size'] <= ENTRY_MAX and L['text'].strip()
            and (L['x2'] - L['x']) <= WIDTH_MAX]


def heading_lines(page):
    return [L for L in page['lines']
            if HEAD_MIN <= L['size'] <= HEAD_MAX and L['text'].strip()
            and HEAD.match(L['text'].strip())]


def _rows(lines, tol=ROW_TOL):
    out, cur = [], []
    for L in sorted(lines, key=lambda L: (round(L['y'], 1), L['x'])):
        if cur and abs(L['y'] - cur[0]['y']) <= tol:
            cur.append(L)
        else:
            if cur: out.append(cur)
            cur = [L]
    if cur: out.append(cur)
    return [sorted(r, key=lambda L: L['x']) for r in out]


def split_regions(lines, heads):
    """Vertical regions delimited by the section headings; prose dropped."""
    ys = sorted(L['y'] for L in heads)
    if not ys:
        bounds = [(0.0, 1e9)]
    else:
        bounds = [(0.0, ys[0])] + [(ys[i], ys[i + 1])
                                   for i in range(len(ys) - 1)] \
                 + [(ys[-1], 1e9)]
    out = []
    for a, b in bounds:
        sub = [L for L in lines if a <= L['y'] < b]
        if sub: out.append((a, b, sub))
    return out


def _cluster(vals, tol):
    out = []
    for v in sorted(vals):
        if out and v - out[-1][-1] <= tol:
            out[-1].append(v)
        else:
            out.append([v])
    return out


def anchors(sub):
    """Left edges of the entry columns, left to right.

    Columns here are aligned row by row, so the left edge of a column is the x
    that most lines in it start at.  Page-number columns are dropped (they are
    always numeric), and gloss sub-columns fall out of the spacing rule.
    """
    cnt = collections.Counter(round(L['x'], 1) for L in sub)
    groups = _cluster(list(cnt), ANCHOR_TOL)
    ranked = sorted(((sum(cnt[x] for x in g), g) for g in groups), reverse=True)
    if not ranked: return []
    floor = max(ANCHOR_MIN, 0.25 * ranked[0][0])
    keep = []
    for n, g in ranked:
        if n < floor: continue
        xs = [x for x in g]
        lines = [L for L in sub if round(L['x'], 1) in set(xs)]
        if not lines: continue
        if sum(1 for L in lines if NUM.match(L['text'].strip())) >= 0.5 * len(lines):
            continue                      # a page-number column
        x = sum(g) / len(g)
        if any(abs(x - k) < MIN_COL_GAP for k in keep):
            continue                      # a gloss sub-column of a kept column
        keep.append(x)
    return sorted(keep)


def columns(sub, anch):
    """Assign every line to the column edge at or nearest to its left."""
    cols = [[] for _ in anch]
    for L in sub:
        idx = 0
        for i, e in enumerate(anch):
            if L['x'] >= e - 3.0:
                idx = i
        cols[idx].append(L)
    return cols


def load_map():
    """First-Edition -> Second-Edition page correspondence (see idxmap.py).

    The index printed in the First Edition cites First-Edition pages, which no
    longer hold in a re-typeset book, so every number is translated through this
    map.  If the map is missing the numbers are printed unchanged (the index is
    then consistent with the First Edition, not with this one)."""
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'idxmap.json')
    try:
        with open(p, encoding='utf-8') as f:
            return {k: int(v) for k, v in json.load(f)['map'].items()}
    except FileNotFoundError:
        print('   idxmap.json not found: index page numbers left as printed')
        return {}


NUMPAT = re.compile(r'(?<![\d.])(\d{1,3})(?![\d.])')


def remap_numbers(cell, m):
    """Translate the page references inside one index cell."""
    if not m:
        return cell
    def rep(mo):
        n = int(mo.group(1))
        if 20 <= n <= 402 and str(n) in m:
            return str(m[str(n)])
        return mo.group(1)
    return NUMPAT.sub(rep, cell)


def cell_lines(lines):
    """One string per visual row, with short numeric rows folded into the
    line above (the First Edition prints each page number beside its entry)."""
    out = []
    for r in _rows(lines, tol=ROW_TOL):
        txt = ' '.join(L['text'].strip() for L in r if L['text'].strip())
        txt = re.sub(r'\s+', ' ', txt).strip()
        if not txt: continue
        if re.match(r'^(N[1-5]|REF)$', txt):
            out.append(txt)            # a level marker keeps its own row
        elif NUM.match(txt) and out:
            out[-1] = (out[-1] + '  ' + txt).strip()
        else:
            out.append(txt)
    return out


PAGE_MAP = load_map()


def page_items(page):
    """-> list of grids; each grid is a list of columns of strings."""
    lines = index_lines(page)
    if not lines: return []
    grids = []
    for a, b, sub in split_regions(lines, heading_lines(page)):
        if not any(NUM.match(L['text'].strip()) for L in sub):
            continue                      # the 'how to use' note above the index
        anch = anchors(sub)
        if not anch: continue
        cols = [[remap_numbers(x, PAGE_MAP) for x in cell_lines(c)]
                for c in columns(sub, anch)]
        if any(cols): grids.append(cols)
    return grids



# ---------------------------------------------------------------------------
# R16.3 — the terms this edition adds.
#
# The inherited index (R16.1/R16.2) lists First-Edition terms and cites pages,
# which this edition can recompute (see load_map/remap_numbers above).  The
# second edition's new block (R46-R69) and the 実際の日本語 interludes (RJ1-RJ5)
# introduce vocabulary the First Edition never indexed.  Those entries cite the
# *section* that explains the term, not a page: a section number stays correct
# when the layout moves, a page number does not, and this edition has no
# mechanism to rebuild an index of its own writing.  Stated in the head of the
# grid so the reader knows which kind of number they are reading.
NEW_TERMS = [
    ('美化語', 'R28 · RJ1'), ('マニュアル敬語', 'R59 · RJ1'),
    ('ウチ・ソト', 'R28 · RJ3'), ('方言の敬語', 'R25 · RJ3'),
    ('役割語', 'R36 · RJ5'), ('である体', 'R61 · RJ5'),
    ('〜とみられます', 'R33 · RJ5'), ('情報構造', 'R26 · R50'),
    ('ゼロ代名詞', 'R26 · R50'), ('語用論', 'R51'),
    ('ポライトネス', 'R51'), ('談話標識', 'R43'),
    ('終助詞', 'R38 · R53'), ('縮約形', 'R49'),
    ('ローマ字表記', 'R17 · R46'), ('高低アクセント', 'R19 · R31 · R47'),
    ('コロケーション', 'R22'), ('類義語', 'R23'),
    ('登録変換', 'R44'), ('国字・名乗り', 'R27'),
    ('全角・半角', 'R30'), ('絵文字・顔文字', 'R34'),
    ('駅アナウンス', 'R35'), ('漢越語', 'R37'),
    ('同音異義語', 'R41'), ('略語', 'R40'),
    ('擬声語・擬態語', 'R29'), ('ビジネス日本語', 'R59'),
    ('公用文', 'R60'), ('学術日本語', 'R60'),
    ('検証登録簿', 'R68'), ('情報源の階層', 'R67'),
    ('実際の日本語 ①–⑤', 'RJ1–RJ5'),
]

NEW_TERMS_HEAD = ('R16.3 — Thuật ngữ của ấn bản thứ hai ／ 第二版で加わった術語　'
                  '（số ở cột phải là <b>mục</b>, không phải số trang ／ 右は頁ではなく項目番号）')


def new_terms_grids(ncol=2):
    items = ['%s — %s' % (t, r) for t, r in NEW_TERMS]
    rows = (len(items) + ncol - 1) // ncol
    cols = []
    for c in range(ncol):
        cols.append(items[c * rows:(c + 1) * rows])
    return cols

def apply(doc, ir_path=None):
    here = os.path.dirname(os.path.abspath(__file__))
    ir = json.load(open(ir_path or os.path.join(here, 'ir.json'), encoding='utf-8'))
    src = {p['no']: p for p in ir['pages']}
    log = []
    for pg in doc['pages']:
        if pg['no'] not in PAGES: continue
        blocks = pg.get('blocks')
        if not isinstance(blocks, list): continue
        grids = page_items(src[pg['no']])
        if not grids: continue
        keep, placed, dropped = [], False, 0
        for b in blocks:
            if b.get('t') == 'table':
                if not placed:
                    keep.append({'t': 'idx', 'grids': grids}); placed = True
                continue
            # stray fragments left in the block IR by the newspaper columns
            frag = ' '.join(str(b.get(k, '') or '') for k in
                            ('text', 'label', 'body', 'cap')).strip()
            if frag and re.fullmatch(r'[\d,\s]+', frag):
                dropped += 1; continue
            keep.append(b)
        if not placed:
            keep.append({'t': 'idx', 'grids': grids})
        if pg['no'] == max(PAGES) and WITH_NEW_TERMS:
            keep.append({'t': 'h4', 'text': NEW_TERMS_HEAD})
            keep.append({'t': 'idx', 'grids': [new_terms_grids()]})
        pg['blocks'] = keep
        log.append((pg['no'], [len(g) for g in grids],
                    sum(len(c) for g in grids for c in g)))
        if dropped: print('   index page %d: dropped %d stray fragment(s)' % (pg['no'], dropped))
    return log


def debug():
    here = os.path.dirname(os.path.abspath(__file__))
    ir = json.load(open(os.path.join(here, 'ir.json'), encoding='utf-8'))
    for page in ir['pages']:
        if page['no'] not in PAGES: continue
        grids = page_items(page)
        print('=== page', page['no'], [(len(g), sum(len(c) for c in g)) for g in grids])
        for g in grids:
            for j, c in enumerate(g):
                print('  --- column', j + 1, '(%d lines)' % len(c))
                for ln in c[:7]:
                    print('      ', ln)


if __name__ == '__main__':
    debug()
