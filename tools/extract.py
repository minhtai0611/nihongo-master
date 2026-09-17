"""Extract Nihongo Master PDF into a structured IR for the 2nd edition rebuild."""
import pymupdf, json, re, statistics
from collections import defaultdict

SRC = '/home/user/nihongo-master/Nihongo_Master_N5-N1.pdf'
OUT = '/home/user/build/ir.json'

# ---- geometry constants measured from the original -------------------------
PAGE_W, PAGE_H = 595.28, 841.89
PN = 8.5          # page number size

def fam(s): return s['font'].split('+')[-1]

def line_info(l):
    sp = l['spans']
    txt = ''.join(s['text'] for s in sp).strip()
    if not txt: return None
    sizes = [round(s['size'],1) for s in sp]
    return dict(
        x=round(l['bbox'][0],1), y=round(l['bbox'][1],1),
        x2=round(l['bbox'][2],1), y2=round(l['bbox'][3],1),
        size=statistics.mode(sizes) if sizes else 0,
        maxsize=max(sizes), font=fam(sp[0]),
        text=txt,
        span_marks=[(round(s['bbox'][0],1), fam(s)) for s in sp],
    )

def page_lines(p):
    out=[]
    for b in p.get_text('dict')['blocks']:
        if b['type']!=0: continue
        for l in b['lines']:
            li=line_info(l)
            if li: out.append(li)
    out.sort(key=lambda d:(round(d['y'],1), d['x']))
    return out

def page_kind(lines, pno, page_count):
    txt=' '.join(l['text'] for l in lines)
    sizes={l['maxsize'] for l in lines}
    if pno==1: return 'cover'
    if 'MỤC LỤC' in txt: return 'toc'
    if any(l['maxsize']>=80 for l in lines): return 'part-divider'
    if re.match(r'^(CHƯƠNG\s+\d+|R\d+\s*／)', txt.strip()): return 'chapter-opener'
    if not lines: return 'blank'
    return 'body'

def main():
    doc = pymupdf.open(SRC)
    toc = doc.get_toc()
    pages=[]
    for i,p in enumerate(doc):
        lines=page_lines(p)
        kind=page_kind(lines, i+1, doc.page_count)
        pages.append(dict(no=i+1, kind=kind, lines=[l for l in lines
                       if not (l['size']==PN and l['y']>780)]))
    # ---- flat element stream -------------------------------------------------
    json.dump(dict(pages=pages, toc=toc), open(OUT,'w'), ensure_ascii=False)
    print('pages', len(pages))
    from collections import Counter
    print(Counter(p['kind'] for p in pages))

if __name__=='__main__':
    main()
