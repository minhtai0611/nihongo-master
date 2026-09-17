import json, sys, re
d=json.load(open('/home/user/build/doc.json'))
pat=sys.argv[1]
ctx=int(sys.argv[2]) if len(sys.argv)>2 else 260
rx=re.compile(pat, re.I)
for p in d['pages']:
    for b in p.get('blocks',[]):
        vals=[]
        for k in ('text','label','body','ja','romaji','vi','note','cap'):
            if isinstance(b.get(k),str): vals.append((k,b[k]))
        if b['t']=='table':
            for h in (b.get('headers') or []): vals.append(('th',h))
            for r in b.get('rows',[]):
                for c in r: vals.append(('td',c))
        for k,v in vals:
            for m in rx.finditer(v):
                s=max(0,m.start()-ctx//2); e=min(len(v),m.end()+ctx//2)
                print(f"p{p['no']:3d} {b['t']:8s} {k:7s} …{v[s:e]}…")
                print()
