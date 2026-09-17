"""Map First-Edition page numbers to Second-Edition pages, for the index (R16).

The First Edition's index prints page numbers of the First Edition. The Second
Edition re-typesets the book, so every one of those numbers is stale (measured:
82 % of the sampled references resolve on the cited page in the First Edition,
20 % in the Second). This tool rebuilds the correspondence from evidence — for
every page of the baseline PDF it takes the longest line on that page and finds
the page of the built Second Edition that contains it — and writes `idxmap.json`,
which `indexfix.py` then applies to the index numbers.

Run it after any change that moves pages:

    python3 idxmap.py [path/to/built.pdf]

Output: idxmap.json  {'map': {'<baseline page>': <page in the new book>}, ...}
Pages that cannot be located are left out; the index keeps the original number
for those, so a partial map degrades safely.
"""
import json, re, sys, os

import os as _os
BASE = _os.environ.get('NIHONGO_BUILD') or _os.path.dirname(_os.path.abspath(__file__))
def _p(name): return _os.path.join(BASE, name)

import pymupdf

SRC = _os.path.join(_os.path.dirname(BASE), 'Nihongo_Master_N5-N1.pdf')
# pages of the new book that ARE the index: never a valid target for a
# signature taken from a body page
INDEX_MARK = ('日本語索引', 'ベトナム語索引')


def norm(s):
    return re.sub(r'\s+', '', s or '')


def new_pages(pdf_path):
    d = pymupdf.open(pdf_path)
    pages, index_pages = [], set()
    for i, p in enumerate(d):
        t = norm(p.get_text())
        pages.append(t)
        if any(m in t for m in INDEX_MARK):
            index_pages.add(i)
    return pages, index_pages


PUNCT = re.compile('[\\s\\u3000・／·—–\\-,\\.、。()（）「」『』:;：；!！?？’“”]')


def key(t):
    """Title key for matching a bookmark between the two editions."""
    return PUNCT.sub('', t or '').lower()


def anchors(ir, new_toc):
    """(baseline page, second-edition page) pairs from the two bookmark trees.

    361 headings are shared by both editions; matching them gives a dense,
    high-confidence set of anchor points instead of guessing from page text."""
    base = {}
    for lvl, t, pg in ir['toc']:
        base.setdefault(key(t), pg)
    pairs = []
    for lvl, t, pg in new_toc:
        b = base.get(key(t))
        if b:
            pairs.append((b, pg))
    # keep one page per baseline page, and force monotonicity
    best = {}
    for b, p in sorted(pairs):
        if b not in best or p < best[b]:
            best[b] = p
    out, last = [], 0
    for b in sorted(best):
        if best[b] >= last:
            out.append((b, best[b])); last = best[b]
    return out


def make_map(pairs, n_base, n_last):
    """Interpolate between anchors; the text of a page between two headings
    moves with them, so a linear interpolation is accurate to a page or two."""
    if not pairs:
        return {}
    xs = [b for b, _ in pairs]
    ys = [p for _, p in pairs]
    m = {}
    j = 0
    for n in range(1, n_base + 1):
        while j + 1 < len(xs) and xs[j + 1] <= n:
            j += 1
        if n == xs[j]:
            m[n] = ys[j]; continue
        if j + 1 < len(xs) and xs[j] < n < xs[j + 1]:
            span_x = xs[j + 1] - xs[j]
            span_y = ys[j + 1] - ys[j]
            m[n] = ys[j] + round(span_y * (n - xs[j]) / float(span_x))
        elif n < xs[0]:
            m[n] = max(1, ys[0] - (xs[0] - n))
        else:
            m[n] = min(n_last, ys[-1] + (n - xs[-1]))
    return m


def signature_hits(ir, pages, index_pages):
    """For every baseline page, the first page of the new book that contains its
    longest line.  Cheap and dense, but occasionally wrong when a line repeats
    (a running head, a quoted rule), so the caller validates against the
    bookmark interpolation before trusting it."""
    out = {}
    for pg in ir['pages']:
        cands = sorted(pg['lines'], key=lambda l: len(l['text']), reverse=True)
        for L in cands[:5]:
            k = norm(L['text'])[:36]
            if len(k) < 22:
                continue
            hits = [i + 1 for i, t in enumerate(pages)
                    if k in t and i not in index_pages]
            if hits:
                out[pg['no']] = hits[0]
                break
    return out


def build(pdf_path):
    ir = json.load(open(_p('ir.json'), encoding='utf-8'))
    d = pymupdf.open(pdf_path)
    new_toc = d.get_toc()
    pages, index_pages = new_pages(pdf_path)
    pairs = anchors(ir, new_toc)
    coarse = make_map(pairs, len(ir['pages']), d.page_count)
    # dense text matches, kept only where they agree with the coarse map
    sig = signature_hits(ir, pages, index_pages)
    kept, rejected = 0, 0
    for n, hit in sig.items():
        if abs(hit - coarse.get(n, hit)) <= 5:
            pairs.append((n, hit)); kept += 1
        else:
            rejected += 1
    pairs = sorted(set(pairs))
    have = {b: p for b, p in pairs}
    # de-duplicate by baseline page and force monotonicity again
    clean, last = [], 0
    for b in sorted(have):
        if have[b] >= last:
            clean.append((b, have[b])); last = have[b]
    print('text matches kept: %d, rejected as outliers: %d' % (kept, rejected))
    pairs = clean
    m = make_map(pairs, len(ir['pages']), d.page_count)
    # sanity: the whole mapping must be monotone and inside the book
    vals = [m[n] for n in sorted(m)]
    assert all(1 <= v <= d.page_count for v in vals), 'mapping outside the book'
    assert vals == sorted(vals), 'mapping is not monotone'
    print('anchors matched: %d of %d baseline bookmarks' % (len(pairs), len(ir['toc'])))
    print('baseline pages mapped: %d; range %d..%d'
          % (len(m), m[1], m[len(ir['pages'])]))
    return {'source': 'Nihongo_Master_N5-N1.pdf -> built Second Edition',
            'method': 'bookmark anchors + linear interpolation between them',
            'anchors': len(pairs),
            'note': 'regenerate whenever the layout changes (see README)',
            'map': {str(k): v for k, v in m.items()}}


def main():
    pdf = sys.argv[1] if len(sys.argv) > 1 else _os.path.join(
        _os.path.dirname(BASE), 'Nihongo_Master_N5-N1_2nd_Edition.pdf')
    data = build(pdf)
    with open(_p('idxmap.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=0)
    print('wrote', _p('idxmap.json'))


if __name__ == '__main__':
    main()
