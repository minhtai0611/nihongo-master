"""Build 日本語 MASTER — Second Edition."""
import json, re, sys, os
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    NextPageTemplate, PageBreak, KeepTogether, CondPageBreak, Flowable, Table, TableStyle)
from reportlab.lib.colors import HexColor
import theme as T
from theme import guard
import blocks as B
T.register_fonts(); T.build_styles()
import frontmatter as FM

DOC = json.load(open('/home/user/build/doc.json'))
import renumber, indexfix
COR = json.load(open('/home/user/build/corrections.json')) if os.path.exists('/home/user/build/corrections.json') else {}

GLYPH_FIX = [('\u9488','\u91dd'), ('\u2717','\u00d7'), ('\u27e8','\u3008'), ('\u27e9','\u3009')]
def norm(t):
    if not t: return ''
    for a,b in GLYPH_FIX: t=t.replace(a,b)
    return re.sub(r'\s+',' ',t).strip()
def clean(t):
    t=norm(t)
    for old,new in COR.get('replace',[]): t=t.replace(old,new)
    return t

STATE=dict(part='', chap='', keyn=0, headings=[])
def newkey(p='x'):
    STATE['keyn']+=1; return f'{p}{STATE["keyn"]}'

class KW(Flowable):
    """zero-height flowable that records a bookmark"""
    def __init__(self,key,text,level):
        Flowable.__init__(self); self._bookmark=dict(key=key,text=text,level=level)
    def wrap(self,aw,ah): return (0,0)
    def draw(self): pass

class Book(BaseDocTemplate):
    def __init__(self,fn):
        BaseDocTemplate.__init__(self,fn,pagesize=(T.PAGE_W,T.PAGE_H),
            title='日本語 MASTER — N5 → N1 · Ấn bản thứ hai',
            author='Biên soạn tổng hợp cho người học Việt Nam',
            subject='Giáo trình và sách tra cứu tiếng Nhật N5–N1',
            creator='ReportLab · phông nhúng toàn bộ')
        self.h_part=''; self.h_chap=''
        self.page_heads={}
        f=Frame(T.ML,T.MB,T.CW,T.PAGE_H-T.MT-T.MB,id='b',
                leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        self._lastlevel=-1
        self.addPageTemplates([
            PageTemplate('plain',[f],onPage=self.nofolio),
            PageTemplate('body',[f],onPage=self.body_page),
            PageTemplate('chap',[f],onPage=self.chap_page),
            PageTemplate('part',[f],onPage=self.nofolio),
        ])
    def handle_documentBegin(self):
        # reset per-pass running heads (multiBuild reuses the same instance)
        self.h_part=''; self.h_chap=''
        self.page_heads={}; self._lastlevel=-1
        BaseDocTemplate.handle_documentBegin(self)
    def nofolio(self,c,d): pass
    def chap_page(self,c,d): self._foot(c)
    def body_page(self,c,d):
        pn=c.getPageNumber()
        hp,hc=self.page_heads.get(pn,(self.h_part,self.h_chap))
        c.saveState()
        c.setFont('Sans',7.3); c.setFillColor(T.GREY)
        c.drawString(T.ML, T.PAGE_H-T.MT+15, hp[:70])
        c.drawRightString(T.PAGE_W-T.MR, T.PAGE_H-T.MT+15, hc[:70])
        c.setStrokeColor(T.RULE_SOFT); c.setLineWidth(0.5)
        c.line(T.ML, T.PAGE_H-T.MT+10, T.PAGE_W-T.MR, T.PAGE_H-T.MT+10)
        c.restoreState(); self._foot(c)
    def _foot(self,c):
        c.saveState(); c.setFont('Sans',8.6); c.setFillColor(T.GREY)
        c.drawRightString(T.PAGE_W-T.MR, T.MB-17, str(c.getPageNumber()))
        c.setStrokeColor(T.RULE_SOFT); c.setLineWidth(0.5)
        c.line(T.PAGE_W-T.MR-30, T.MB-12, T.PAGE_W-T.MR, T.MB-12)
        c.restoreState()
    def afterFlowable(self,fl):
        k=getattr(fl,'_bookmark',None)
        if k:
            lv=k['level']
            if self._lastlevel < 0: lv=0
            elif lv > self._lastlevel+1: lv=self._lastlevel+1
            k['level']=lv; self._lastlevel=lv
            if lv==0:
                self.h_part=k['text']; self.h_chap=''
            elif lv==1:
                self.h_chap=k['text']
            if lv<=1 and self.page_heads.get(self.page) is None:
                self.page_heads[self.page]=(self.h_part,self.h_chap)
            STATE['headings'].append(dict(k, page=self.page))
            self.canv.bookmarkPage(k['key'], fit='XYZ', top=T.PAGE_H)
            self.canv.addOutlineEntry(k['text'][:130], k['key'], level=k['level'],
                                      closed=(k['level']>1))
            # printed TOC lists parts, chapters and R-sections; the PDF outline
            # keeps every level-3 sub-heading as well
            if k['level'] <= 1:
                self.notify('TOCEntry', (k['level'], k['text'], self.page, k['key']))

# ---------------------------------------------------------------- flowables
class Cover(Flowable):
    def wrap(self,aw,ah): self._w,self._h=aw,ah; return (aw,ah)
    def draw(self):
        c=self.canv; w,h=self._w,self._h
        c.saveState()
        c.setFillColor(T.WASHI); c.rect(-T.ML,-T.MB,T.PAGE_W,T.PAGE_H,stroke=0,fill=1)
        c.setFillColor(T.SUMI); c.rect(-T.ML,h-6,T.PAGE_W,6,stroke=0,fill=1)
        c.setFillColor(T.VERMILION); c.rect(-T.ML,h-12,120,6,stroke=0,fill=1)
        c.setFont('DispB',54); c.setFillColor(T.SUMI)
        c.drawString(0,h-150,'日本語')
        c.setFont('ZenB',40); c.setFillColor(T.INDIGO)
        c.drawString(0,h-206,'MASTER')
        c.setStrokeColor(T.RULE); c.setLineWidth(0.8); c.line(0,h-232,w*0.62,h-232)
        c.setFont('SansB',13); c.setFillColor(T.SUMI)
        c.drawString(0,h-262,'N5  →  N4  →  N3  →  N2  →  N1')
        c.setFont('Body',11.4); c.setFillColor(T.INK_SOFT)
        c.drawString(0,h-296,'Giáo trình và sách tra cứu tiếng Nhật cho người học Việt Nam')
        for j,txt in enumerate(['Hệ thống chữ viết · Ngữ pháp · Từ vựng · Phát âm',
                                'Nghe · Nói · Đọc · Viết · Kính ngữ · Văn hóa',
                                'Dụng học · Cấu trúc thông tin · Ngôn ngữ viết · Biến thể xã hội']):
            c.drawString(0,h-320-j*17,txt)
        c.setFillColor(T.GOLD); c.rect(0,h-410,54,2.2,stroke=0,fill=1)
        c.setFont('SansB',10.5); c.setFillColor(T.VERMILION)
        c.drawString(0,h-436,'ẤN BẢN THỨ HAI ／ 第二版')
        c.setFont('Body',9.6); c.setFillColor(T.INK_SOFT)
        c.drawString(0,h-458,'Hiệu đính · Mở rộng · Kiểm chứng lại toàn bộ')
        c.setFont('Sans',8.2); c.setFillColor(T.GREY)
        c.drawString(0,10,'Một tập duy nhất · A4 · Tài liệu học và tra cứu dài hạn')
        c.restoreState()

class PartDivider(Flowable):
    def __init__(self,d): self.d=d
    def wrap(self,aw,ah): self._w,self._h=aw,ah; return (aw,ah)
    def draw(self):
        c=self.canv; w,h=self._w,self._h; d=self.d
        c.saveState()
        c.setFillColor(T.VERMILION); c.setFont('SansB',9.6)
        c.drawString(0,h-24,d['num'])
        c.setFont('ZenB',92); c.setFillColor(T.SUMI)
        c.drawString(-4,h-136,d.get('code',''))
        if d.get('ja'):
            c.setFont('DispB',29); c.setFillColor(T.SUMI)
            c.drawString(0,h-196,d['ja'])
        c.setStrokeColor(T.GOLD); c.setLineWidth(1.4); c.line(0,h-216,58,h-216)
        if d.get('vi'):
            c.setFont('Body',12.6); c.setFillColor(T.INK_SOFT)
            c.drawString(0,h-244,d['vi'])
        if d.get('desc'):
            c.setFont('Body',9.9); c.setFillColor(T.INK)
            txt=d['desc']; y=h-282; ln=''
            for word in txt.split():
                if T.CW*0.82 < 0: break
                test=(ln+' '+word).strip()
                if c.stringWidth(test,'Body',9.9) > T.CW*0.84:
                    c.drawString(0,y,ln); y-=16.2; ln=word
                else: ln=test
            if ln: c.drawString(0,y,ln)
        c.restoreState()

# ============================================================ second edition
_CORR = None
def _corrections():
    global _CORR
    if _CORR is None:
        p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'corrections.json')
        try:
            with open(p,encoding='utf-8') as f: _CORR=json.load(f)
        except FileNotFoundError:
            _CORR=dict(replace=[],nuke=[])
    return _CORR

def _fix_str(s, pairs, hits):
    for i,(o,n) in enumerate(pairs):
        if o and o!=n and o in s:
            s=s.replace(o,n); hits[i]=hits.get(i,0)+s.count(n)
    return s

def apply_corrections(doc=None):
    """Pre-pass: rewrite flagged passages in every text field before rendering."""
    doc = DOC if doc is None else doc
    pairs=_corrections().get('replace',[])
    nuke=[k for k in _corrections().get('nuke',[]) if k]
    hits={}
    def w(x):
        if isinstance(x,str): return _fix_str(x,pairs,hits)
        if isinstance(x,list): return [w(i) for i in x]
        if isinstance(x,dict): return {k:(w(v)) for k,v in x.items()}
        return x
    pages=w(doc.get('pages',[])); doc['pages']=pages
    # second pass: drop any block whose text is now empty or in the nuke list
    if nuke:
        for pg in pages:
            bl=pg.get('blocks')
            if bl:
                pg['blocks']=[b for b in bl
                              if not any(n in str(b.get(k,'')) for n in nuke for k in ('text',))]
    return hits

class SectionDivider(Flowable):
    """Editorial opener for the extended reference block inside Part VI."""
    def wrap(self,aw,ah): self._w,self._h=aw,ah; return (aw,ah)
    def draw(self):
        c=self.canv; w,h=self._w,self._h
        c.saveState()
        c.setFillColor(T.VERMILION); c.setFont('SansB',9.4)
        c.drawString(0,h-30,'PHẦN VI ／ TRA CỨU TỔNG HỢP · TIẾP THEO')
        c.setStrokeColor(T.GOLD); c.setLineWidth(1.2); c.line(0,h-46,64,h-46)
        c.setFont('DispB',25); c.setFillColor(T.SUMI)
        c.drawString(0,h-92,'引き出し — 続き')
        c.setFont('Body',12.4); c.setFillColor(T.INK_SOFT)
        c.drawString(0,h-120,'Phần tra cứu mở rộng: R46 → R69')
        c.setFont('Body',9.9); c.setFillColor(T.INK)
        for i,line in enumerate([
            'Phần R1–R45 ở trên giữ nguyên. Phần này bổ sung những mảng mà ấn bản thứ',
            'nhất còn thiếu — dụng học, cấu trúc thông tin, tiếng Nhật công việc và',
            'học thuật, ngôn ngữ đang thay đổi, đối chiếu Việt–Nhật — và nâng sổ đăng',
            'ký kiểm chứng cùng thư mục lên mức dùng được lâu dài.',
        ]):
            c.drawString(0,h-158-i*16.4,line)
        c.restoreState()

_NEW = [
    ('reference_map', 'Bảng đối chiếu mục tra cứu', None),
    ('r46_romanization', 'R46 — La-tinh hoá', None),
    ('r47_pronunciation', 'R47 — Phát âm', None),
    ('r49_spoken', 'R49 — Tiếng Nhật nói', None),
    ('r50_information', 'R50 — Cấu trúc thông tin', None),
    ('r51_pragmatics', 'R51 — Dụng học', '_r51_cont'),
    ('r53_final_particles', 'R53 — Trợ từ cuối câu', None),
    ('r54_literal_actual', 'R54 — Nghĩa đen và nghĩa thực', None),
    ('r59_business', 'R59 — Tiếng Nhật công việc', None),
    ('r60_academic', 'R60 — Học thuật và văn bản công', None),
    ('r61_modern', 'R61 — Tiếng Nhật hiện đại', None),
    ('r62_classical_modern', 'R62 — Cổ văn và hiện đại', None),
    ('r65_vn_contrast', 'R65 — Đối chiếu Việt–Nhật', None),
    ('r66_error_atlas', 'R66 — Bản đồ lỗi', None),
    ('r67_source_hierarchy', 'R67 — Phân cấp nguồn', None),
    ('r68_register_upgrade', 'R68 — Sổ đăng ký kiểm chứng', None),
    ('bibliography', 'Thư mục theo nhóm nguồn', None),
    ('candos', 'Bản đồ năng lực N5 → N1', None),
]

def _tag_generated(F, force_l1=False):
    """Give generated flowables their outline bookmarks."""
    for f in F:
        if getattr(f,'_bookmark',None): continue
        if isinstance(f, B.SectionHead):
            txt=f.text
            f._bookmark=dict(key=newkey('s'), text=txt,
                             level=1 if force_l1 else _lvl(txt,'h2'))
        else:
            txt=getattr(f,'text',None)
            sty=getattr(f,'style',None)
            if txt and sty in (T.ST['h3'], T.ST['h4']):
                lv=_lvl(txt,'h3' if sty is T.ST['h3'] else 'h4')
                if lv: f._bookmark=dict(key=newkey('s'), text=txt, level=lv)

def new_sections():
    import importlib, newsections as NS
    importlib.reload(NS)
    out=[]
    for fn, label, cont in _NEW:
        g=getattr(NS, fn, None)
        if g is None:
            print('  ! missing generator', fn); continue
        F=list(g())
        if cont:
            F += list(getattr(NS, cont)())
        _tag_generated(F)
        out += F
        print(f'  + {label}: {len(F)} flowables')
    return out

def cando_for(level):
    import importlib, newsections as NS
    importlib.reload(NS)
    F=list(NS.cando_one(level))
    _tag_generated(F, force_l1=True)
    return F

def build_story():
    st=[]; STATE['headings']=[]; STATE['keyn']=0
    global DOC
    hits=apply_corrections()
    print('corrections applied to %d/%d entries' % (len(hits), len(_corrections().get('replace',[]))))
    DOC, rlog = renumber.repair(DOC)
    ilog = indexfix.apply(DOC)
    print('reference index rebuilt: %s' % (', '.join('p%d %s' % (p, n) for p, n, _ in ilog)))
    print('reference numbering repaired: %d sub-headings, %d captions, %d cross-references'
          % (len(rlog['headings']), len(rlog['captions']), len(rlog['refs'])))
    st.append(NextPageTemplate('plain')); st.append(Cover()); st.append(PageBreak())
    st += FM.colophon()
    st.append(NextPageTemplate('body'))
    # ---- main body ----
    toc_done=False
    for pg in DOC['pages']:
        no=pg['no']
        if no < 5: continue
        k=pg['kind']
        if k in ('toc','cover'): continue
        if k=='part-divider':
            if not toc_done:
                st.append(NextPageTemplate('body')); st.append(PageBreak())
                st.append(TOCMarker())
                st += FM.toc_head()
                st.append(FM.toc_flow())
                toc_done=True
            # Can-do map for the level that has just ended (brief §46)
            prev = {'N4':'N5','N3':'N4','N2':'N3','N1':'N2','REF':'N1'}.get(pg.get('num'))
            if prev:
                st.append(NextPageTemplate('body'))
                st += cando_for(prev)
            STATE['part']=pg.get('vi') or pg.get('num','')
            STATE['chap']=''''''
            st.append(NextPageTemplate('part')); st.append(PageBreak())
            code=re.sub(r'^PHẦN\s*','',pg.get('num','')).strip()
            st.append(KW(newkey('p'), pg.get('vi') or pg['num'], 0))
            st.append(mark_part(PartDivider(dict(pg, code=code))))
            continue
        if k=='chapter-opener':
            bl=pg['blocks']
            lab=next((b['text'] for b in bl if b['t']=='chap-label'), '')
            ja =next((b['text'] for b in bl if b['t']=='chap-ja'), '')
            vi =next((b['text'] for b in bl if b['t']=='chap-vi'), '')
            dek=next((b['text'] for b in bl if b['t']=='chap-dek'), '')
            STATE['chap']=clean(vi)[:64]
            st.append(NextPageTemplate('chap')); st.append(PageBreak())
            _lt=clean(lab); _vt=clean(vi); _jt=clean(ja)
            if _lt and _lt.startswith('R'):
                _bmtext=(_lt+(' · '+_jt if _jt else '')) or _vt
            else:
                _bmtext=(_lt+(' · '+_vt if _vt else '')) if _lt else _vt
            st.append(KW(newkey('c'), _bmtext, 1))
            st.append(ChapterHead(clean(lab), clean(ja), clean(vi), clean(dek)))
            used=0
            for b in bl:
                if b['t'] in ('chap-label','chap-ja','chap-vi','chap-dek'): continue
                for f in render_block(b, head=True): st.append(f)
            st.append(NextPageTemplate('body'))
            continue
        for b in pg.get('blocks',[]):
            for f in render_block(b): st.append(f)
    # ---- Part VI continuation: the R46-R69 reference block (2nd edition) ----
    print('building second-edition reference sections...')
    st.append(NextPageTemplate('part')); st.append(PageBreak())
    st.append(KW(newkey('p'), 'Phần tra cứu mở rộng R46 → R69', 0))
    st.append(PartDivider(dict(num='PHẦN VI — TIẾP', code='続', ja='引き出し',
        vi='Phần tra cứu mở rộng R46 → R69',
        desc='Những mảng mà ấn bản thứ nhất còn thiếu: dụng học, cấu trúc thông tin, '
             'tiếng Nhật công việc và học thuật, ngôn ngữ đang thay đổi, đối chiếu '
             'Việt–Nhật — cùng sổ đăng ký kiểm chứng và thư mục được nâng lên mức '
             'dùng được lâu dài.')))
    st.append(NextPageTemplate('body'))
    st += new_sections()
    st += FM.backmatter()
    return st

def mark_part(f): return f

class TOCMarker(Flowable):
    def __init__(self): Flowable.__init__(self); self._tocmark=True
    def wrap(self,aw,ah): return (0,0)
    def draw(self): pass

class ChapterHead(Flowable):
    def __init__(self,lab,ja,vi,dek):
        self.lab=lab; self.ja=ja; self.vi=vi; self.dek=dek; self._bm=None
    def wrap(self,aw,ah):
        self._w=aw
        self._ps=[]
        y=0
        if self.lab: p=Paragraph(guard(self.lab,'SansB'),T.ST['chaplabel']); self._ps.append((p,'lab'))
        if self.ja:  p=Paragraph(guard(self.ja,'DispB'),T.ST['chapja']);   self._ps.append((p,'ja'))
        if self.vi:  p=Paragraph(guard(self.vi,'Body'),T.ST['chapvi']);   self._ps.append((p,'vi'))
        if self.dek: p=Paragraph(guard(self.dek,'Body'),T.ST['chapdek']); self._ps.append((p,'dek'))
        h=0
        for p,k in self._ps:
            hh=p.wrap(aw,1000)[1]; p._h=hh
            h += hh + {'lab':6,'ja':7,'vi':8,'dek':0}[k]
        self._h=h+26
        return (aw,self._h)
    def draw(self):
        c=self.canv; y=self._h-4
        for p,k in self._ps:
            if k=='lab':
                c.saveState(); c.setStrokeColor(T.VERMILION); c.setLineWidth(1.5)
                c.line(0,y+2,34,y+2); c.restoreState()
            y-=p._h; p.drawOn(c,0,y)
            y -= {'lab':6,'ja':7,'vi':8,'dek':0}[k]
            if k=='vi':
                c.saveState(); c.setStrokeColor(T.RULE); c.setLineWidth(0.6)
                c.line(0,y-4,self._w,y-4); c.restoreState()

_NUM3=re.compile(r'^R?\d+\.\d+\.\d+')      # 2.1.1 -> sub-sub
_NUM2=re.compile(r'^R?\d+\.\d+')              # 2.1 / R13.1 -> sub
_NUM2B=re.compile(r'^\d+\.\d+[a-z]?\s')       # 2.6b  -> sub
_ABC=re.compile(r'^[A-Z]\.\s')                 # A. / B. -> sub
_RSEC=re.compile(r'^R\d+\s|^R\d+\s?／')        # R13 / R46 heads -> chapter level

def _lvl(txt, t):
    """Bookmark level for a heading. 0=part 1=chapter/R-section 2=sub 3=sub-sub."""
    txt=(txt or '').strip()
    if t=='h2':
        return 1 if _RSEC.match(txt) else 2
    if _NUM3.match(txt): return 3
    if _NUM2.match(txt) or _NUM2B.match(txt) or _ABC.match(txt): return 2
    return None

def render_block(b, head=False):
    out=[]; t=b.get('t')
    if t=='h2':
        txt=clean(b['text'])
        out.append(CondPageBreak(96))
        f=B.SectionHead(txt); f._bookmark=dict(key=newkey('s'),text=txt,level=_lvl(txt,'h2'))
        out.append(f)
    elif t=='h3':
        txt=clean(b['text'])
        out.append(CondPageBreak(64))
        p3=Paragraph(guard(txt,'BodyB'),T.ST['h3'])
        lv=_lvl(txt,'h3')
        if lv: p3._bookmark=dict(key=newkey('s'),text=txt,level=lv)
        out.append(p3)
    elif t=='h4':
        txt=clean(b['text'])
        out.append(CondPageBreak(58))
        p4=Paragraph(guard(txt,'SansB'),T.ST['h4'])
        lv=_lvl(txt,'h4')
        if lv: p4._bookmark=dict(key=newkey('s'),text=txt,level=lv)
        out.append(p4)
    elif t=='disp':
        out.append(CondPageBreak(56))
        out.append(Paragraph(guard(clean(b['text']),'DispB'),T.ST['chapja']))
    elif t=='dek':  out.append(Paragraph(guard(clean(b['text']),'Body'),T.ST['lead']))
    elif t=='p':
        txt=clean(b['text'])
        if not txt: return out
        out.append(Paragraph(guard(txt),T.ST['body']))
    elif t=='bullets':
        out.append(B.Bullets([clean(i) for i in b['items']])); out.append(Spacer(1,5))
    elif t=='callout':
        lab=clean(b['label']); body=clean(b['body'])
        if not lab and not body: return out
        out.append(KeepTogether([B.Callout(lab.upper(),body)])); out.append(Spacer(1,7))
    elif t=='example':
        ja=clean(b['ja']); ro=clean(b['romaji']); vi=clean(b['vi']); nt=clean(b['note'])
        if not (ja or vi): return out
        out.append(KeepTogether([B.Example(ja,ro,vi,nt)])); out.append(Spacer(1,4))
    elif t=='idx':
        # reference index rebuilt as a real multi-column grid (see indexfix.py)
        for gi,grid in enumerate(b.get('grids') or []):
            ncol=max(1,len(grid)); nrow=max((len(c) for c in grid), default=0)
            if not nrow: continue
            cw=T.CW/float(ncol)
            data=[]
            for i in range(nrow):
                row=[]
                for c in grid:
                    txt=c[i] if i < len(c) else ''
                    txt=txt.replace('&','&amp;').replace('<','&lt;')
                    stl=T.ST['idx']
                    if txt in ('N1','N2','N3','N4','N5','REF'):
                        txt='<b>%s</b>' % txt
                        stl=T.ST['idx']
                    row.append(Paragraph(guard(txt,'Body'), stl) if txt else '')
                data.append(row)
            tb=Table(data, colWidths=[cw]*ncol, repeatRows=0)
            tb.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                ('LEFTPADDING',(0,0),(-1,-1),0),
                ('RIGHTPADDING',(0,0),(-1,-1),7.5),
                ('TOPPADDING',(0,0),(-1,-1),0),
                ('BOTTOMPADDING',(0,0),(-1,-1),1.1)]))
            out.append(tb)
            if gi+1 < len(b.get('grids') or []):
                out.append(Spacer(1, 9))
        out.append(Spacer(1, 6))
    elif t=='table':
        rows=[[clean(c) for c in r] for r in (b.get('rows') or []) if any((x or '').strip() for x in r)]
        hdr=[clean(h) for h in (b.get('headers') or [])] or None
        cap=clean(b.get('cap'))
        if not rows and not hdr: return out
        colw=b.get('colw')
        out.append(CondPageBreak(60))
        if cap:
            cp=T.ST['tblcap']; cp.keepWithNext=1
            out.append(Paragraph(guard(cap,'SansB'), cp))
        out.append(B.make_table(hdr, rows, colw))
        out.append(Spacer(1,10))
    return out

def build(path, headings=None):
    doc=Book(path)
    story=build_story()
    doc.multiBuild(story)
    seen={}; order=[]
    for h in STATE['headings']:
        if h['key'] in seen:
            seen[h['key']]=h
        else:
            seen[h['key']]=h; order.append(h['key'])
    return [seen[k] for k in order]

if __name__=='__main__':
    hs=build('/home/user/build/book.pdf')
    print("headings:",len(hs))
