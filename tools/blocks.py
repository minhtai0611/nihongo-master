"""Custom flowables for the editorial system."""
from reportlab.platypus import Flowable, KeepTogether, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
import theme as T
from theme import guard, style as S

def P(txt, st, base='Body'):
    return Paragraph(guard(txt, base), S(st))

class HRule(Flowable):
    def __init__(self, w=None, thick=0.6, color=T.RULE, space=6, dash=None):
        Flowable.__init__(self); self.w=w; self.thick=thick; self.color=color
        self.space=space; self.dash=dash
    def wrap(self, aw, ah):
        self._w = self.w or aw; return (self._w, self.thick+self.space*2)
    def draw(self):
        c=self.canv; c.saveState()
        c.setStrokeColor(self.color); c.setLineWidth(self.thick)
        if self.dash: c.setDash(self.dash)
        y=self.space+self.thick/2
        c.line(0,y,self._w,y); c.restoreState()

class SectionHead(Flowable):
    """h2: rule above, Japanese + Vietnamese title."""
    RULE_GAP = 5.0
    def __init__(self, text, width=None):
        Flowable.__init__(self); self.text=text; self.width=width
    def wrap(self, aw, ah):
        self._w = self.width or aw
        st = ParagraphStyle('h2x', parent=S('h2'))
        st.spaceBefore = 0; st.spaceAfter = 0
        self._p = Paragraph(guard(self.text,'BodyB'), st)
        w,h = self._p.wrap(self._w, 10000)
        self._th = h
        return (self._w, h + self.RULE_GAP + 7.0)
    def draw(self):
        c=self.canv; c.saveState()
        y = self._th + self.RULE_GAP
        c.setStrokeColor(T.VERMILION); c.setLineWidth(1.4)
        c.line(0, y, 26, y)
        c.setStrokeColor(T.RULE); c.setLineWidth(0.5)
        c.line(28, y, self._w, y)
        c.restoreState()
        self._p.drawOn(c, 0, 0)

class Callout(Flowable):
    """Tinted box: label (sans bold) + body paragraph(s)."""
    def __init__(self, label, body, width=None, tone='indigo', pad=8.5):
        Flowable.__init__(self)
        self.label=label; self.body=body; self.width=width; self.tone=tone; self.pad=pad
    def wrap(self, aw, ah):
        self._w = self.width or aw
        tw = self._w - self.pad*2 - 3
        self._lp = P(self.label, 'callabel', 'SansB') if self.label else None
        self._bp = P(self.body, 'callbody', 'Body') if self.body else None
        h = 0
        if self._lp: h += self._lp.wrap(tw, 1000)[1] + 3.5
        if self._bp: h += self._bp.wrap(tw, 1000)[1]
        self._th = h + self.pad*2
        return (self._w, self._th + 8)
    def draw(self):
        c=self.canv; c.saveState()
        tones = {'indigo':(T.INDIGO_L, T.INDIGO), 'gold':(T.GOLD_L, T.GOLD),
                 'teal':(T.TEAL_L, T.TEAL), 'washi':(T.WASHI_2, T.GREY_L)}
        bg, bar = tones.get(self.tone, tones['indigo'])
        y0 = 4; y1 = self._th + 4
        c.setFillColor(bg); c.rect(0, y0, self._w, self._th, stroke=0, fill=1)
        c.setFillColor(bar); c.rect(0, y0, 2.2, self._th, stroke=0, fill=1)
        c.restoreState()
        y = self._th + 4 - self.pad
        if self._lp:
            h=self._lp.wrap(self._w-self.pad*2-3,1000)[1]
            self._lp.drawOn(c, self.pad+3, y-h); y -= h+3.5
        if self._bp:
            h=self._bp.wrap(self._w-self.pad*2-3,1000)[1]
            self._bp.drawOn(c, self.pad+3, y-h)

class Verify(Flowable):
    """要検証 / CẦN KIỂM CHỨNG box."""
    def __init__(self, label, body, width=None):
        Flowable.__init__(self); self.label=label; self.body=body; self.width=width
    def wrap(self, aw, ah):
        self._w = width = self.width or aw
        self._lp = P(self.label, 'veriflab', 'SansB')
        self._bp = P(self.body, 'verif', 'Body')
        tw = width - 20
        h = self._lp.wrap(tw,1000)[1] + 3 + self._bp.wrap(tw,1000)[1]
        self._th = h + 16
        return (width, self._th + 8)
    def draw(self):
        c=self.canv; c.saveState()
        c.setFillColor(T.GOLD_L); c.rect(0,4,self._w,self._th,stroke=0,fill=1)
        c.setStrokeColor(T.GOLD); c.setLineWidth(0.7); c.setDash(2,2)
        c.rect(0,4,self._w,self._th,stroke=1,fill=0)
        c.restoreState()
        y=self._th+4-8
        h=self._lp.wrap(self._w-20,1000)[1]; self._lp.drawOn(c,10,y-h); y-=h+3
        h=self._bp.wrap(self._w-20,1000)[1]; self._bp.drawOn(c,10,y-h)

class Example(Flowable):
    """Example card: Japanese / romaji / Vietnamese / note."""
    def __init__(self, ja, romaji, vi, note, width=None):
        Flowable.__init__(self)
        self.ja=ja; self.romaji=romaji; self.vi=vi; self.note=note; self.width=width
    def wrap(self, aw, ah):
        self._w = self.width or aw
        tw = self._w - 12
        self._parts=[]
        for txt, st, base in ((self.ja,'exja','Disp'),(self.romaji,'exromaji','Sans'),
                              (self.vi,'exvi','Body'),(self.note,'exnote','Body')):
            if txt and txt.strip():
                p=P(txt, st, base); h=p.wrap(tw,1000)[1]
                self._parts.append((p,h,st)); 
        self._th = sum(h for _,h,_ in self._parts) + (len(self._parts)-1)*1.6
        return (self._w, self._th + 11)
    def draw(self):
        c=self.canv; c.saveState()
        c.setFillColor(T.RULE); c.rect(0, 5.5, 1.6, self._th, stroke=0, fill=1)
        c.restoreState()
        y = self._th + 5.5
        for p,h,st in self._parts:
            y -= h
            p.drawOn(c, 10, y)
            y -= (1.6 if st!='exnote' else 0)
            if st=='exja': y += 1.0

def make_table(headers, rows, colw=None, width=None, caption=None):
    """Return (caption_para, Table) so the table can split across pages."""
    data=[]
    if headers: data.append([P(h,'th','SansB') for h in headers])
    for r in rows:
        data.append([P(c,'td') for c in r])
    ncol=max(len(r) for r in data) if data else 1
    data=[r+['']*(ncol-len(r)) for r in data]
    if colw and len(colw)==ncol:
        tot=sum(colw); cw=[T.CW*w/tot for w in colw]
    else:
        cw=None
    t=Table(data, colWidths=cw, repeatRows=1 if headers else 0)
    st=[('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),5.5),('RIGHTPADDING',(0,0),(-1,-1),5.5),
        ('TOPPADDING',(0,0),(-1,-1),3.4),('BOTTOMPADDING',(0,0),(-1,-1),3.4),
        ('LINEBELOW',(0,0),(-1,-2),0.35,T.RULE_SOFT),
        ('LINEBELOW',(0,-1),(-1,-1),0.6,T.RULE)]
    if headers:
        st += [('BACKGROUND',(0,0),(-1,0),T.WASHI_2),
               ('LINEBELOW',(0,0),(-1,0),0.75,T.INK_SOFT),
               ('TOPPADDING',(0,0),(-1,0),4.4),('BOTTOMPADDING',(0,0),(-1,0),4.0)]
    t.setStyle(TableStyle(st))
    return t

class DataTable(Flowable):
    """Zebra-striped table with header row."""
    def __init__(self, cap, headers, rows, width=None, colw=None):
        Flowable.__init__(self)
        self.cap=cap; self.headers=headers; self.rows=rows
        self.width=width; self.colw=colw
    def wrap(self, aw, ah):
        self._w = self.width or aw
        data=[]
        if self.headers:
            data.append([P(h,'th','SansB') for h in self.headers])
        for r in self.rows:
            data.append([P(c,'td') if i==0 else P(c,'td') for i,c in enumerate(r)])
        ncol = max(len(r) for r in data) if data else 1
        data = [r + ['']*(ncol-len(r)) for r in data]
        if self.colw:
            tot=sum(self.colw); cw=[self._w*w/tot for w in self.colw]
        else:
            cw=None
        self._t = Table(data, colWidths=cw, repeatRows=1 if self.headers else 0)
        st=[('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),5.5),('RIGHTPADDING',(0,0),(-1,-1),5.5),
            ('TOPPADDING',(0,0),(-1,-1),3.4),('BOTTOMPADDING',(0,0),(-1,-1),3.4),
            ('LINEBELOW',(0,0),(-1,-2),0.35,T.RULE_SOFT),
            ('LINEBELOW',(0,-1),(-1,-1),0.6,T.RULE)]
        if self.headers:
            st += [('BACKGROUND',(0,0),(-1,0),T.WASHI_2),
                   ('LINEBELOW',(0,0),(-1,0),0.7,T.INK_SOFT),
                   ('TOPPADDING',(0,0),(-1,0),4.4),('BOTTOMPADDING',(0,0),(-1,0),4.0)]
        self._t.setStyle(TableStyle(st))
        w,h = self._t.wrap(self._w, ah)
        self._cap = P(self.cap,'tblcap','SansB') if self.cap else None
        ch = self._cap.wrap(self._w,1000)[1]+3.6 if self._cap else 0
        self._th = h
        return (self._w, ch + h + 8)
    def draw(self):
        c=self.canv
        y = self._th + 8
        if self._cap:
            h=self._cap.wrap(self._w,1000)[1]
            y -= h; self._cap.drawOn(c,0,y); y -= 3.6
        y -= self._th
        self._t.drawOn(c, 0, y)

class Bullets(Flowable):
    def __init__(self, items, width=None):
        Flowable.__init__(self); self.items=items; self.width=width
    def wrap(self, aw, ah):
        self._w=aw
        self._ps=[]
        for it in self.items:
            p=Paragraph('<bullet>&#8226;</bullet>'+guard(it), S('bullet'))
            self._ps.append((p, p.wrap(self._w,1000)[1]))
        self._th=sum(h for _,h in self._ps)
        return (self._w, self._th+4)
    def draw(self):
        y=self._th
        for p,h in self._ps:
            y-=h; p.drawOn(self.canv,0,y)
