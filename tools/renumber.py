# -*- coding: utf-8 -*-
"""Repair the reference-section numbering of the First Edition.

The First Edition numbered the sub-headings inside the reference sections
R21-R34 with a leading number that is one less than the section it belongs to
(20.x inside R21, 21.x inside R22, ... 33.x inside R34), while the table
captions in the same sections already used the correct section number.  R26
additionally had a gap (no R26.3) and a duplicate (R26.6 twice).  This module
rewrites both, and then repairs the forty-odd cross-references in the running
text that pointed at the old numbers.

Everything here is a *numbering* repair: no claim, example or explanation of
the First Edition is changed.
"""
import copy, re

# ---------------------------------------------------------------- references
# exact substrings, taken from the First Edition and verified against doc.json
REF_FIX = [
    # R21 — examples of rendaku / Lyman (tables R21.2 and R21.3)
    ('bảng 20.2–20.3',            'bảng R21.2–R21.3'),
    # R24 — the five stages of the language (table R24.1)
    ('bảng 23.1',                 'bảng R24.1'),
    # R25 — policy milestones (table R25.2)
    ('bảng 24.2',                 'bảng R25.2'),
    # R26 — agent suppression is the sub-section 26.6
    ('mục 25.6',                  'mục 26.6'),
    # R27 — examples of nanori (table R27.2)
    ('Bảng 26.2',                 'Bảng R27.2'),
    # R28 — the five keigo forms (R28.1) and baito-keigo (R28.2)
    ('bảng 27.1',                 'bảng R28.1'),
    ('Bảng 27.2',                 'Bảng R28.2'),
    # R29 — the voicing contrast in mimetic words (table R29.2)
    ('bảng 28.2',                 'bảng R29.2'),
    # R31 — compound accent (R31.2) and accent systems by region (R31.4)
    ('Bảng 30.2',                 'Bảng R31.2'),
    ('bảng 30.4',                 'bảng R31.4'),
    # R32 — openings and closings are tables R32.1-R32.2; the cushion
    #       phrases are the sub-section 32.3 (prose, no table)
    ('Các cụm ở bảng 31.1–31.3',  'Các cụm ở mục 32.1–32.3'),
    # R33 — the three tables of epistemic modality
    ('Bảng 32.1–32.3',            'Bảng R33.1–R33.3'),
    # style normalisation: a reference to an R-table keeps the R prefix
    ('bảng 19.3',                 'bảng R19.3'),
    ('Bảng 18.5',                 'Bảng R18.5'),
    ('Bảng 36.1',                 'Bảng R36.1'),
]

# ---------------------------------------------------------------- headings
_HEAD = re.compile(r'^(\d{1,2})\.(\d+)([a-z]?)(\s|$)')
_CAP = re.compile(r'^(.*?BẢNG\s+R)(\d+)\.(\d+)([a-z]?)(.*)$')
_SECT = re.compile(r'^R(\d+)\b')
_LAB = re.compile(r'^R(\d+)\s*／')

# sections whose sub-headings carry a wrong leading number (First Edition)
HEAD_FIX_FROM, HEAD_FIX_TO = 21, 34
# section whose table captions need re-sequencing (gap + duplicate)
RESEQ = {26}

TEXT_FIELDS = ('text', 'cap', 'body', 'label', 'note', 'vi', 'ja', 'headers', 'rows')


def _walk_strings(obj, fn):
    """Apply fn to every string in the nested structure (in place)."""
    if isinstance(obj, str):
        return fn(obj)
    if isinstance(obj, list):
        return [_walk_strings(x, fn) for x in obj]
    if isinstance(obj, dict):
        return {k: _walk_strings(v, fn) for k, v in obj.items()}
    return obj


def repair(doc):
    """Return a corrected copy of doc, plus a log of what changed."""
    doc = copy.deepcopy(doc)
    log = {'headings': [], 'captions': [], 'refs': []}
    cur = None
    seqs = {}
    for pg in doc['pages']:
        blocks = pg.get('blocks') or []
        lab = next((b.get('text') for b in blocks if b.get('t') == 'chap-label'), '')
        m = _LAB.match(lab or '')
        if m:
            cur = int(m.group(1))
        for b in blocks:
            t = b.get('t')
            if t == 'h2':
                m2 = _SECT.match(b.get('text') or '')
                if m2:
                    cur = int(m2.group(1))
                continue
            if t in ('h3', 'h4') and cur is not None:
                txt = b.get('text') or ''
                m3 = _HEAD.match(txt)
                if (m3 and HEAD_FIX_FROM <= cur <= HEAD_FIX_TO
                        and int(m3.group(1)) != cur):
                    new = f'{cur}.{m3.group(2)}{m3.group(3)}{txt[m3.end(3):]}'
                    log['headings'].append((pg['no'], txt[:52], new[:52]))
                    b['text'] = new
            if t == 'table' and cur is not None:
                cap = b.get('cap') or ''
                m4 = _CAP.match(cap)
                if m4:
                    seqs[cur] = seqs.get(cur, 0) + 1
                    want = seqs[cur] if cur in RESEQ else int(m4.group(3))
                    if int(m4.group(2)) != cur or int(m4.group(3)) != want:
                        newcap = f'{m4.group(1)}{cur}.{want}{m4.group(4)}{m4.group(5)}'
                        log['captions'].append((pg['no'], cap[:52], newcap[:52]))
                        b['cap'] = newcap
    # ---- cross-references in the running text
    def fixref(s):
        for old, new in REF_FIX:
            if old in s:
                log['refs'].append((old, new))
                s = s.replace(old, new)
        return s
    for pg in doc['pages']:
        for b in pg.get('blocks') or []:
            b.update(_walk_strings(b, fixref))
    return doc, log


if __name__ == '__main__':
    import json, sys
    p = sys.argv[1] if len(sys.argv) > 1 else 'doc.json'
    d = json.load(open(p, encoding='utf-8'))
    d2, log = repair(d)
    print('headings rewritten :', len(log['headings']))
    print('captions rewritten :', len(log['captions']))
    print('references fixed   :', len(log['refs']), 'of', len(REF_FIX))
    for k in ('headings', 'captions'):
        for a in log[k][:6]:
            print('   ', a)
