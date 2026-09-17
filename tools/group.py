# -*- coding: utf-8 -*-
"""Group extracted lines into semantic blocks (v4).

Two structural passes:
  1. y-band analysis -> table regions (works for caption-less tables too)
  2. original PDF bookmarks -> authoritative heading identification
"""
import json, re
from collections import Counter

import os as _os
BASE = _os.environ.get('NIHONGO_BUILD') or _os.path.dirname(_os.path.abspath(__file__))
def _p(name): return _os.path.join(BASE, name)

IR = json.load(open(_p('ir.json')))
JA_RE = re.compile(r'^[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\u4e00-\u9fff\uff00-\uffef\u2460-\u24ff]+$')
CAP_RE = re.compile(r'^(BẢNG|Bảng)\b', re.I)
BUL = re.compile(r'^[•\u00b7]$')
NUMBUL = re.compile(r'^\d{1,2}[.)]$')
NUMSEC = re.compile(r'^(\d+(\.\d+)+|R\d+(\.\d+)*)\s')

def is_marker(t):
    """A line that is nothing but a list marker: • · 1. 2) …"""
    return bool(BUL.match(t) or NUMBUL.match(t))

def is_bullet(t):
    """Narrow test used by the table builder: the source uses the same bullet
    glyph as a table filler, so numbered markers must NOT be stripped from
    table cells."""
    return bool(BUL.match(t))

def is_clabel(L):
    """Bold 7.4/7.6 pt label at an indented x — a callout or run-in heading."""
    return ('Bold' in L['font'] and round(L['maxsize'],1) in (7.4,7.6)
            and L['x'] > 45)

def upper_ratio(t):
    ls=[c for c in t if c.isalpha()]
    return sum(1 for c in ls if c.isupper())/len(ls) if ls else 0.0

def solo_label(lines, i):
    """is_clabel + nothing else on the same baseline: excludes the small bold
    *table header* cells, which share their line with other cells."""
    if not is_clabel(lines[i]): return False
    L = lines[i]
    return not any(j != i and abs(M['y']-L['y']) < 2.5
                   for j, M in enumerate(lines))

def order_markers(lines):
    """Put a lone list marker immediately before the line it labels.

    In the source PDF a marker's baseline sits up to ~0.5 pt below the first
    line of its item, so a plain y-then-x sort emits the marker *after* its own
    text; the marker then either starts a spurious item or is swallowed by the
    preceding paragraph (this is what flattened numbered lists in the 1st ed.).
    Only lines that are currently mis-ordered are moved, so table order and
    markers that are already correct are untouched."""
    out = list(lines)
    for L in lines:
        if not is_marker(L['text']): continue
        cands = [M for M in lines if M is not L and M['x'] > L['x'] + 1.5
                 and -2.0 <= (M['y'] - L['y']) <= 2.0]
        if not cands: continue
        tgt = min(cands, key=lambda M: abs(M['y'] - L['y']))
        if out.index(L) > out.index(tgt):
            out.remove(L); out.insert(out.index(tgt), L)
    return out

# ---------------------------------------------------------------- bookmarks
def norm_txt(s):
    s = re.sub(r'\s+', '', s or '')
    return s.lower()

def load_bookmark_index():
    idx = {}
    for lvl, title, pg in IR['toc']:
        idx.setdefault(pg, []).append((lvl, title, norm_txt(title)))
    return idx
BM = load_bookmark_index()

def match_bookmark(page_no, text, x=None):
    """Return (level, title) if this line is a bookmark target on this page."""
    cands = BM.get(page_no, [])
    nt = norm_txt(text)
    if not nt: return None
    best = None
    for lvl, title, t in cands:
        if not t: continue
        if nt == t or t.endswith(nt) or nt.endswith(t) or t in nt:
            if best is None or abs(len(t)-len(nt)) < abs(len(best[1])-len(nt)):
                best = (lvl, title)
    return best

# ------------------------------------------------------------------- roles
def role(L):
    sz, x, t, f = L['size'], L['x'], L['text'], L['font']
    m = L['maxsize']
    if m >= 80:            return 'partnum'
    if m == 27.0:          return 'part-ja'
    if m == 11.5:          return 'part-vi'
    if m == 20.0:          return 'chap-ja'
    if m == 13.0:          return 'chap-vi'
    if m == 10.0:          return 'chap-dek'
    if m == 10.4:          return 'chap-body'
    if m == 15.0:          return 'disp15'
    if m == 9.0 and 'Bold' in f: return 'chap-label'
    if m == 9.4:           return 'dek'
    if m == 9.8:           return 'h3'
    if m == 9.6 and f.startswith('NotoSans') and 'Bold' in f: return 'h4'
    if m == 7.4 and CAP_RE.match(t): return 'tblcap'
    if m == 11.0:          return 'ex-ja'
    if m == 7.6 and f.startswith('NotoSans') and 'Bold' not in f: return 'ex-romaji'
    if m == 9.0:           return 'ex-vi'
    if m == 8.4:           return 'ex-note'
    if m == 9.5:           return 'partdesc'
    if m == 9.1:           return 'callbody'
    if m <= 8.85:          return 'cell'
    if m in (9.6, 9.2, 10.0, 8.6): return 'para'
    return 'other'

def merge(ls, sep=' '):
    out = ''
    for l in ls:
        t = l['text']
        if not out: out = t
        elif out.endswith(('-', '–')) or t[:1] in '，）。，、': out += t
        else: out += sep + t
    return re.sub(r'\s+', ' ', out).strip()

# ------------------------------------------------------------ table regions
STRUCT = {'partnum','part-ja','part-vi','partdesc','chap-label','chap-ja','chap-vi',
          'chap-dek','h3','h4','tblcap'}

def anchors_of(lines, gap=22.0):
    xs = sorted({round(l['x'],1) for l in lines
                 if not is_bullet(l['text']) and l.get('role') not in STRUCT})
    anchors=[]
    for x in xs:
        if not anchors or x-anchors[-1] > gap: anchors.append(x)
    return anchors

def _bands(lines, tol=5.0):
    bs=[]
    for l in lines:
        if bs and abs(l['y']-bs[-1]['y'])<tol: bs[-1]['lines'].append(l)
        else: bs.append(dict(y=l['y'], lines=[l]))
    return bs

def _is_tabular(band):
    cells=[l for l in band['lines'] if not is_bullet(l['text']) and l['role'] not in STRUCT]
    if len(cells)<2: return False
    xs=sorted(l['x'] for l in cells)
    return any(xs[k+1]-xs[k] > 25.0 for k in range(len(xs)-1))

def _anchors(lines, gap=22.0):
    xs=sorted({round(l['x'],1) for l in lines
               if not is_bullet(l['text']) and l['role'] not in STRUCT})
    out=[]
    for x in xs:
        if not out or x-out[-1] > gap: out.append(x)
    return out

def table_regions(lines):
    """Seed from same-y multi-column bands, then extend along column anchors."""
    if not lines: return [], []
    bands=_bands(lines)
    idx={}
    for k,l in enumerate(lines): idx[id(l)]=k
    tab=[_is_tabular(b) for b in bands]
    regions=[]; allanchors=[]
    i=0
    while i < len(bands):
        if not tab[i]: i+=1; continue
        j=i
        while j+1 < len(bands) and tab[j+1]: j+=1
        if j-i+1 >= 1:
            seed_lines=[l for b in bands[i:j+1] for l in b['lines']]
            an=_anchors(seed_lines)
            if len(an) >= 2:
                # size the table's own cells are set in
                dom=Counter(round(l['size'],1) for l in seed_lines
                            if l['role'] not in STRUCT).most_common(1)[0][0]
                start=idx[id(bands[i]['lines'][0])]
                end=idx[id(bands[j]['lines'][-1])]
                # extend upward
                while start-1 >= 0:
                    l=lines[start-1]
                    if l['role'] in STRUCT: break
                    if is_marker(l['text']) and abs(round(l['size'],1)-dom) > 0.5: break
                    ci=_col(l['x'],an)
                    if not _fits(l,an,ci): break
                    if lines[start]['y']-l['y'] > 30.0: break
                    start-=1
                # extend downward
                while end+1 < len(lines):
                    l=lines[end+1]
                    if l['role'] in STRUCT: break
                    # a list marker set in body size is not a cell; nor is a
                    # body-size line that introduces such a list
                    if is_marker(l['text']) and abs(round(l['size'],1)-dom) > 0.5: break
                    if (abs(round(l['size'],1)-dom) > 0.5 and end+2 < len(lines)
                        and is_marker(lines[end+2]['text'])):
                        break
                    ci=_col(l['x'],an)
                    if not _fits(l,an,ci): break
                    if l['y']-lines[end]['y'] > 30.0: break
                    end+=1
                regions.append((start,end,an))
                allanchors=an
        i=j+1
    # merge overlapping regions
    regions.sort()
    merged=[]
    for r in regions:
        if merged and r[0] <= merged[-1][1]+1:
            if r[1] > merged[-1][1]:
                merged[-1]=(merged[-1][0], r[1], merged[-1][2])
        else:
            merged.append(list(r) if False else (r[0],r[1],r[2]))
    return [(a_,b_) for a_,b_,_ in merged], (merged[0][2] if merged else [])

def _fits(l, anchors, ci, slop=14.0):
    """Reject full-width paragraphs masquerading as cells (they cross column edges)."""
    if ci is None: return False
    if ci >= len(anchors)-1: return True
    return l['x2'] <= anchors[ci+1] + slop

def _col(x, anchors, tol=6.0):
    for k,a in enumerate(anchors):
        if abs(x-a) <= tol: return k
    return None

def build_table(region_lines, anchors):
    """Rows broken at bands containing a first-column cell; within a band, left to right."""
    bands = _bands(region_lines, tol=5.0)

    grid=[]; cur=None
    for bd in bands:
        cells=[l for l in bd['lines'] if l['role'] not in STRUCT and not is_bullet(l['text'])]
        if not cells: continue
        cells.sort(key=lambda l: l['x'])
        cis=[(_col(l['x'],anchors), l) for l in cells]
        cis=[(k,l) for k,l in cis if _fits(l,anchors,k)]

        if not cis: continue
        has0 = any(k==0 for k,_ in cis)
        if has0 or cur is None:
            cur={}; grid.append(cur)
        for k,l in cis:
            cur[k] = (cur[k] + ' ' + l['text']).strip() if cur.get(k) else l['text']
    if not grid: return None, [], None
    ncol = max(max(g.keys()) for g in grid) + 1
    rows = [[g.get(k,'') for k in range(ncol)] for g in grid]
    right = max(l['x2'] for l in region_lines)
    edges = anchors[1:] + [max(right, anchors[-1]+30)]
    widths = [max(edges[k]-anchors[k], 24) for k in range(len(anchors))]
    if len(widths) != ncol: widths = None
    hdr=None
    if len(rows) > 2 and sum(bool(c) for c in rows[0]) >= 2 and all(len(c) <= 52 for c in rows[0]):
        hdr = rows[0]; rows = rows[1:]
    return hdr, rows, widths

# -------------------------------------------------------------- group page
def group_page(lines, page_no):
    lines = order_markers(lines)
    for L in lines: L['role'] = role(L)
    regions, anchors = table_regions(lines)
    in_table = {}
    for st, en in regions:
        for k in range(st, en+1): in_table[k] = (st, en)
    blocks = []; i = 0; n = len(lines)
    while i < n:
        L = lines[i]; R = L['role']
        if i in in_table:
            st, en = in_table[i]
            hdr, rows, widths = build_table(lines[st:en+1], anchors)
            cap = None
            if blocks and blocks[-1].get('t')=='_tblcap':
                cap = blocks.pop()['text']
            if hdr is None and not rows:
                i = en + 1; continue
            blocks.append(dict(t='table', cap=cap, headers=hdr, rows=rows, colw=widths))
            i = en + 1
            continue
        if R == 'tblcap':
            # caption with no following table -> plain paragraph
            blocks.append(dict(t='_tblcap', text=L['text'])); i += 1; continue
        bm = match_bookmark(page_no, L['text']) if R in ('disp15', 'h3', 'para', 'chap-ja', 'chap-vi') else None
        if R == 'disp15':
            if bm and (bm[0] >= 3 or NUMSEC.match(L['text'])):
                blocks.append(dict(t='h2', text=L['text'], bm=bm)); i += 1; continue
            if NUMSEC.match(L['text']):
                blocks.append(dict(t='h2', text=L['text'])); i += 1; continue
            # display line (proverb / kanji card / haiku)
            blocks.append(dict(t='disp', text=L['text'])); i += 1; continue
        if R in ('partnum','part-ja','part-vi','partdesc','chap-label','chap-ja','chap-vi','chap-dek'):
            blocks.append(dict(t=R, text=L['text'])); i += 1; continue
        if R in ('h3','h4'):
            blocks.append(dict(t=R, text=L['text'])); i += 1; continue
        if R == 'dek':
            ls = []
            while i < n and lines[i]['role'] == 'dek': ls.append(lines[i]); i += 1
            blocks.append(dict(t='dek', text=merge(ls))); continue
        if is_marker(L['text']) and i not in in_table:
            items = []
            while i < n and is_marker(lines[i]['text']) and i not in in_table:
                mrk = lines[i]['text']; mx = lines[i]['x']; txt = ''; i += 1
                # an item's text is indented past its marker (measured: +6 to
                # +11 pt); a line back at the marker's own x starts a new
                # paragraph, so the list ends there.
                while (i < n and i not in in_table
                       and lines[i]['role'] in ('para','callbody','other','cell','ex-vi','ex-note')
                       and not is_marker(lines[i]['text'])
                       and not is_clabel(lines[i])
                       and lines[i]['x'] >= mx + 4.0):
                    txt = (txt + ' ' + lines[i]['text']) if txt else lines[i]['text']
                    i += 1
                if txt: items.append(dict(m=mrk, t=txt))
            if items: blocks.append(dict(t='bullets', items=items))
            continue
        if R == 'ex-ja':
            # 11pt lines are examples only when a romaji / Vietnamese / note
            # line follows in the same visual group; otherwise they are subheads.
            j = i
            while j < n and lines[j]['role'] == 'ex-ja': j += 1
            k = j
            while k < n and lines[k]['role'] in ('ex-romaji','ex-vi','ex-note'): k += 1
            is_ex = (j > i) and (k > j)
            if is_ex:
                ja = [lines[x] for x in range(i, j)]
                rom = [lines[x] for x in range(j, k) if lines[x]['role']=='ex-romaji']
                vi  = [lines[x] for x in range(j, k) if lines[x]['role']=='ex-vi']
                nt  = [lines[x] for x in range(j, k) if lines[x]['role']=='ex-note']
                blocks.append(dict(t='example', ja=merge(ja), romaji=merge(rom),
                                   vi=merge(vi), note=merge(nt)))
                i = k
            else:
                blocks.append(dict(t='h4', text=merge([lines[i]]))); i += 1
            continue
        if solo_label(lines, i):
            nxt = lines[i+1] if i+1 < n else None
            # A boxed callout in this book is an uppercase label carrying the
            # full-width slash, set above 9.1 pt body text; anything else is a
            # run-in heading above its own explanation (1st-edition device).
            boxed = (nxt is not None and nxt['role'] == 'callbody'
                     and ('\uff0f' in L['text'] or upper_ratio(L['text']) > 0.6))
            if boxed:
                lbl = L['text']; i += 1; body = []
                while i < n and lines[i]['role'] == 'callbody' and not is_marker(lines[i]['text']):
                    body.append(lines[i]); i += 1
                blocks.append(dict(t='callout', label=lbl, body=merge(body))); continue
            blocks.append(dict(t='label', text=L['text'])); i += 1; continue
        if R in ('para','callbody','other','chap-body','ex-vi','ex-note','cell'):
            ls = []
            while i < n and i not in in_table \
                  and lines[i]['role'] in ('para','callbody','other','chap-body','ex-vi','ex-note','cell') \
                  and not is_marker(lines[i]['text']) and not solo_label(lines, i):
                ls.append(lines[i]); i += 1
            if not ls: i += 1; continue
            txt = merge(ls)
            bmx = match_bookmark(page_no, ls[0]['text']) if len(ls) >= 1 else None
            if bmx and bmx[0] >= 2 and len(txt) < 80 and bmx[0] <= 3:
                blocks.append(dict(t='h3', text=txt, bm=bmx))
            else:
                blocks.append(dict(t='p', text=txt))
            continue
        i += 1
    return blocks

# ---------------------------------------------------------- structural pages
def parse_partdiv(lines):
    d = dict(num='', ja='', vi='', desc='', foot='')
    for L in lines:
        m = L['maxsize']
        if m >= 80: d['num'] = L['text']
        elif m == 27.0: d['ja'] = L['text']
        elif m == 11.5: d['vi'] = L['text']
        elif m in (9.4, 9.6, 9.5): d['desc'] = (d['desc'] + ' ' + L['text']).strip()
        elif m <= 9.0 and '／' in L['text']: d['foot'] = L['text']
    return d

def main():
    out = []
    for p in IR['pages']:
        k = p['kind']; no = p['no']
        if k == 'part-divider':
            out.append(dict(no=no, kind=k, **parse_partdiv(p['lines'])))
        elif k in ('body', 'chapter-opener'):
            out.append(dict(no=no, kind=k, blocks=group_page(p['lines'], no)))
        else:
            out.append(dict(no=no, kind=k,
                            blocks=[dict(t='raw', text=l['text']) for l in p['lines']]))
    json.dump(dict(pages=out), open(_p('doc.json'), 'w'), ensure_ascii=False)
    c = Counter(b['t'] for pg in out for b in pg.get('blocks', []))
    print(c)
    tabs = [b for pg in out for b in pg.get('blocks', []) if b.get('t') == 'table']
    print(f"tables={len(tabs)} with-rows={sum(1 for t in tabs if t['rows'])}")
    h2 = [b for pg in out for b in pg.get('blocks', []) if b.get('t') == 'h2']
    print(f"h2={len(h2)} coded={sum(1 for b in h2 if NUMSEC.match(b['text']))} "
          f"bm={sum(1 for b in h2 if b.get('bm'))}")
    disp = [b for pg in out for b in pg.get('blocks', []) if b.get('t') == 'disp']
    print(f"disp15 lines={len(disp)}")

if __name__ == '__main__':
    main()
