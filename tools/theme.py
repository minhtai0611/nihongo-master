"""Design system for 日本語 MASTER — Second Edition."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def _font_dir():
    """Where the twelve text faces live.

    ``NIHONGO_FONTS`` wins; otherwise a ``fonts/`` directory beside this file,
    otherwise the legacy path outside the repository.  They are third-party
    binaries and are not committed — run ``getfonts.py`` to fetch them."""
    env = os.environ.get('NIHONGO_FONTS')
    if env:
        return env.rstrip('/') + '/'
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (os.path.join(here, 'fonts'), '/home/user/fonts'):
        if os.path.isdir(cand):
            return cand.rstrip('/') + '/'
    return os.path.join(here, 'fonts') + '/'

F = _font_dir()

# ---------- palette (washi / sumi / indigo / vermilion / subdued gold) -------
SUMI      = HexColor('#1C1C21')
INK       = HexColor('#26262C')
INK_SOFT  = HexColor('#4A4A52')
GREY      = HexColor('#6E6E77')
GREY_L    = HexColor('#9A9AA2')
RULE      = HexColor('#D8D3C6')
RULE_SOFT = HexColor('#E7E3D8')
WASHI     = HexColor('#FCFAF5')
WASHI_2   = HexColor('#F6F2E8')
INDIGO    = HexColor('#1F3A5F')
INDIGO_L  = HexColor('#E8EDF4')
VERMILION = HexColor('#A8291C')
VERM_L    = HexColor('#FAEDEA')
GOLD      = HexColor('#9C7C36')
GOLD_L    = HexColor('#F6F0DF')
TEAL      = HexColor('#25605A')
TEAL_L    = HexColor('#E7F1EF')

PAGE_W, PAGE_H = A4
ML, MR, MT, MB = 64, 64, 62, 64
CW = PAGE_W - ML - MR            # content width

# ---------- fonts -----------------------------------------------------------
REG = [
    ('Body',   'NotoSerifJP-Regular.ttf'),
    ('BodyB',  'NotoSerifJP-Bold.ttf'),
    ('Sans',   'NotoSansJP-Regular.ttf'),
    ('SansB',  'NotoSansJP-Bold.ttf'),
    ('Disp',   'ShipporiMincho-Regular.ttf'),
    ('DispB',  'ShipporiMincho-Bold.ttf'),
    ('Zen',    'ZenOldMincho-Regular.ttf'),
    ('ZenB',   'ZenOldMincho-Bold.ttf'),
    ('Goth',   'ZenKakuGothicNew-Regular.ttf'),
    ('GothB',  'ZenKakuGothicNew-Bold.ttf'),
    ('Fall',   'NotoSansLatin-Regular.ttf'),
    ('FallB',  'NotoSansLatin-Bold.ttf'),
]
_registered = False
def register_fonts():
    global _registered
    if _registered: return
    for n, f in REG:
        pdfmetrics.registerFont(TTFont(n, F + f))
    _registered = True

# ---------- glyph fallback ---------------------------------------------------
_cov = {}
def coverage(name):
    if name in _cov: return _cov[name]
    from fontTools.ttLib import TTFont as FT
    fn = dict(REG)[name]
    t = FT(F + fn, lazy=True)
    cm = set()
    for tb in t['cmap'].tables: cm |= set(tb.cmap.keys())
    _cov[name] = cm
    return cm

FALLBACKS = {'Body':'Fall','BodyB':'FallB','Sans':'Fall','SansB':'FallB',
             'Disp':'Fall','DispB':'FallB','Zen':'Fall','ZenB':'FallB',
             'Goth':'Fall','GothB':'FallB'}
UNRESOLVED = set()

def guard(text, base='Body'):
    """Wrap characters the base font lacks in <font name=Fallback>."""
    if not text: return text
    cov = coverage(base); fb = coverage(FALLBACKS[base])
    out=[]; buf=''; mode=None   # mode: 0 covered, 1 fallback
    for ch in text:
        o=ord(ch)
        if o in cov: m=0
        elif o in fb: m=1
        else:
            UNRESOLVED.add(ch); m=0
        if mode is None or m==mode: buf+=ch
        else:
            out.append(buf if mode==0 else f'<font name="{FALLBACKS[base]}">{buf}</font>')
            buf=ch
        mode=m
    if buf: out.append(buf if mode==0 else f'<font name="{FALLBACKS[base]}">{buf}</font>')
    return ''.join(out)

# ---------- paragraph styles ------------------------------------------------
def S(name, **kw):
    base = dict(fontName='Body', fontSize=9.9, leading=15.3, textColor=INK,
                alignment=TA_LEFT, spaceBefore=0, spaceAfter=0)
    base.update(kw)
    return ParagraphStyle(name, **base)

ST = {}
def build_styles():
    ST.update(dict(
    body      = S('body', spaceAfter=5.4, firstLineIndent=0),
    body_tight= S('body_tight', spaceAfter=3.0),
    lead      = S('lead', fontName='Body', fontSize=10.6, leading=16.6,
                  textColor=INK_SOFT, spaceAfter=9),
    h2        = S('h2', fontName='BodyB', fontSize=15.2, leading=20.5,
                  textColor=SUMI, spaceBefore=16, spaceAfter=7),
    h3        = S('h3', fontName='BodyB', fontSize=10.5, leading=15.2,
                  textColor=INDIGO, spaceBefore=12, spaceAfter=4.5),
    h4        = S('h4', fontName='SansB', fontSize=9.6, leading=14,
                  textColor=INK, spaceBefore=9, spaceAfter=3),
    callabel  = S('callabel', fontName='SansB', fontSize=7.7, leading=11.4,
                  textColor=SUMI),
    # run-in label inside a grammar entry (“Ý nghĩa cốt lõi / 中心的な意味”):
    # a small bold line above its explanation, as printed in the 1st edition
    runin     = S('runin', fontName='SansB', fontSize=8.2, leading=11.8,
                  textColor=VERMILION, spaceBefore=7.5, spaceAfter=1.6),
    callbody  = S('callbody', fontName='Body', fontSize=9.4, leading=14.4,
                  textColor=INK, spaceAfter=3.2),
    exja      = S('exja', fontName='Disp', fontSize=11.4, leading=17.2,
                  textColor=SUMI, spaceAfter=1.0),
    exromaji  = S('exromaji', fontName='Sans', fontSize=7.9, leading=11.6,
                  textColor=GREY, spaceAfter=1.2),
    exvi      = S('exvi', fontName='Body', fontSize=9.2, leading=13.8,
                  textColor=INK, spaceAfter=1.0),
    exnote    = S('exnote', fontName='Body', fontSize=8.3, leading=12.4,
                  textColor=GREY, spaceAfter=0),
    tblcap    = S('tblcap', fontName='SansB', fontSize=7.7, leading=11.4,
                  textColor=SUMI, spaceBefore=10, spaceAfter=3.6),
    th        = S('th', fontName='SansB', fontSize=7.7, leading=11.0,
                  textColor=SUMI, alignment=TA_LEFT),
    td        = S('td', fontName='Body', fontSize=8.7, leading=12.6,
                  textColor=INK, alignment=TA_LEFT),
    tdb       = S('tdb', fontName='BodyB', fontSize=8.7, leading=12.6,
                  textColor=SUMI, alignment=TA_LEFT),
    tds       = S('tds', fontName='Body', fontSize=8.2, leading=11.8,
                  textColor=INK_SOFT, alignment=TA_LEFT),
    # --- 実際の日本語 / REAL JAPANESE interludes -------------------------
    # a spoken exchange is set as a panel: speaker in small sans vermilion,
    # the line itself in the reading face, romaji under it while the level's
    # policy still prints it, Vietnamese gloss last.
    dlgsp     = S('dlgsp', fontName='SansB', fontSize=8.0, leading=11.4,
                  textColor=VERMILION, spaceAfter=1.0),
    dlgja     = S('dlgja', fontName='Body', fontSize=11.0, leading=18.0,
                  textColor=SUMI, spaceAfter=1.0, leftIndent=2),
    dlgro     = S('dlgro', fontName='Sans', fontSize=7.7, leading=11.8,
                  textColor=GREY, spaceAfter=1.2, leftIndent=2),
    dlgvi     = S('dlgvi', fontName='Body', fontSize=9.1, leading=14.2,
                  textColor=INK, spaceAfter=0.6, leftIndent=2),
    dlgnt     = S('dlgnt', fontName='Body', fontSize=8.2, leading=12.6,
                  textColor=GREY, spaceAfter=0, leftIndent=2),
    # the 'why this sounds natural' block, set as marginalia
    snotelab  = S('snotelab', fontName='SansB', fontSize=8.2, leading=12.0,
                  textColor=SUMI, spaceAfter=0),
    snoteq    = S('snoteq', fontName='SansB', fontSize=9.3, leading=13.6,
                  textColor=VERMILION, spaceAfter=0),
    snoteb    = S('snoteb', fontName='Body', fontSize=9.3, leading=14.6,
                  textColor=INK, spaceAfter=0),
    idx       = S('idx', fontName='Body', fontSize=8.0, leading=10.6,
                  textColor=INK, alignment=TA_LEFT),
    idxnum    = S('idxnum', fontName='Body', fontSize=7.6, leading=10.6,
                  textColor=INK_SOFT, alignment=TA_LEFT),
    bullet    = S('bullet', fontName='Body', fontSize=9.7, leading=14.6,
                  textColor=INK, spaceAfter=2.4, leftIndent=11, bulletIndent=1,
                  bulletFontName='Body', bulletFontSize=8.4),
    runhead   = S('runhead', fontName='Sans', fontSize=7.4, leading=10,
                  textColor=GREY),
    folio     = S('folio', fontName='Sans', fontSize=8.6, leading=11,
                  textColor=GREY),
    partnum   = S('partnum', fontName='ZenB', fontSize=96, leading=104,
                  textColor=SUMI),
    partja    = S('partja', fontName='DispB', fontSize=31, leading=40,
                  textColor=SUMI),
    partvi    = S('partvi', fontName='Body', fontSize=12.4, leading=18,
                  textColor=INK_SOFT),
    partdesc  = S('partdesc', fontName='Body', fontSize=9.6, leading=15.4,
                  textColor=INK_SOFT),
    chaplabel = S('chaplabel', fontName='SansB', fontSize=9.0, leading=13,
                  textColor=VERMILION),
    chapja    = S('chapja', fontName='DispB', fontSize=22, leading=29,
                  textColor=SUMI),
    chapvi    = S('chapvi', fontName='Body', fontSize=13.4, leading=19,
                  textColor=INK),
    chapdek   = S('chapdek', fontName='Body', fontSize=10.2, leading=16,
                  textColor=GREY),
    chapbody  = S('chapbody', fontName='Body', fontSize=10.2, leading=16.4,
                  textColor=INK, spaceAfter=6),
    verif     = S('verif', fontName='Body', fontSize=9.1, leading=13.8,
                  textColor=INK),
    veriflab  = S('veriflab', fontName='SansB', fontSize=7.6, leading=11.2,
                  textColor=GOLD),
    tocchip   = S('tocchip', fontName='SansB', fontSize=9.4, leading=14,
                  textColor=INDIGO),
    tocsub    = S('tocsub', fontName='Body', fontSize=9.0, leading=13.4,
                  textColor=INK),
    small     = S('small', fontName='Body', fontSize=8.6, leading=13,
                  textColor=INK_SOFT),
    caption   = S('caption', fontName='Body', fontSize=8.2, leading=12.4,
                  textColor=GREY),
    )
    )

def style(k): return ST[k]