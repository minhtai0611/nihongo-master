# -*- coding: utf-8 -*-
"""Fetch the twelve text faces the book is set in.

The fonts are not committed: together they are ~60 MB, they are third-party
files under the SIL Open Font Licence, and a repository is a bad place for a
binary that can be downloaded in a minute.  This script is the reproducible
substitute.  It writes into the directory given by ``NIHONGO_FONTS`` (default
``<this directory>/fonts``), which is where ``theme.py`` looks for them.

    python3 getfonts.py            # to tools/fonts/
    NIHONGO_FONTS=/tmp/f python3 getfonts.py

Source: the Google Fonts repository (github.com/google/fonts), OFL-licensed.
Six faces are shipped there as static TTFs and eight are shipped as one
variable font each; the variable ones are instantiated to static weights with
fontTools, and every file is checked for the ``glyf`` table that ReportLab
requires (it cannot embed PostScript/CFF outlines, so .otf faces are useless
here).

Network: uses ``gh api`` when the GitHub CLI is available and authenticated,
otherwise plain HTTPS to api.github.com.  Nothing is written that was not
downloaded or derived on the spot; if a file is missing the script says so and
exits instead of leaving a half-set font directory behind.
"""
import json
import os
import subprocess
import sys
import urllib.request

REPO = 'google/fonts'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('NIHONGO_FONTS') or os.path.join(HERE, 'fonts')

# name written -> path inside google/fonts
STATIC = {
    'ShipporiMincho-Regular.ttf':   'ofl/shipporimincho/ShipporiMincho-Regular.ttf',
    'ShipporiMincho-Bold.ttf':      'ofl/shipporimincho/ShipporiMincho-Bold.ttf',
    'ZenOldMincho-Regular.ttf':     'ofl/zenoldmincho/ZenOldMincho-Regular.ttf',
    'ZenOldMincho-Bold.ttf':        'ofl/zenoldmincho/ZenOldMincho-Bold.ttf',
    'ZenKakuGothicNew-Regular.ttf': 'ofl/zenkakugothicnew/ZenKakuGothicNew-Regular.ttf',
    'ZenKakuGothicNew-Bold.ttf':    'ofl/zenkakugothicnew/ZenKakuGothicNew-Bold.ttf',
}

# variable font -> [(name written, {axis: value})]
VARIABLE = {
    'ofl/notoserifjp/NotoSerifJP[wght].ttf': [
        ('NotoSerifJP-Regular.ttf', {'wght': 400}),
        ('NotoSerifJP-Bold.ttf',    {'wght': 700}),
    ],
    'ofl/notosansjp/NotoSansJP[wght].ttf': [
        ('NotoSansJP-Regular.ttf', {'wght': 400}),
        ('NotoSansJP-Bold.ttf',    {'wght': 700}),
    ],
    # Latin fallback: carries IPA and the Vietnamese diacritics the Japanese
    # faces do not have (see theme.guard()).
    'ofl/notosans/NotoSans[wdth,wght].ttf': [
        ('NotoSansLatin-Regular.ttf', {'wght': 400, 'wdth': 100}),
        ('NotoSansLatin-Bold.ttf',    {'wght': 700, 'wdth': 100}),
    ],
}


def have_gh():
    try:
        subprocess.run(['gh', 'auth', 'status'], capture_output=True, check=True)
        return True
    except Exception:
        return False


USE_GH = have_gh()


def fetch(path):
    """Return the bytes of one file in the repository."""
    if USE_GH:
        p = subprocess.run(['gh', 'api', '-H', 'Accept: application/vnd.github.raw',
                            '/repos/%s/contents/%s' % (REPO, path)],
                           capture_output=True)
        if p.returncode == 0 and p.stdout[:4] in (b'\x00\x01\x00\x00', b'OTTO', b'true', b'wOF2'):
            return p.stdout
        if p.returncode != 0:
            sys.exit('gh api failed for %s: %s' % (path, p.stderr.decode()[:300]))
    url = 'https://api.github.com/repos/%s/contents/%s' % (REPO, path)
    req = urllib.request.Request(url, headers={
        'Accept': 'application/vnd.github.raw', 'User-Agent': 'nihongo-master/getfonts'})
    with urllib.request.urlopen(req, timeout=180) as r:
        return r.read()


def check_ttf(data, name):
    """A font ReportLab can embed: TrueType outlines, not CFF."""
    from fontTools.ttLib import TTFont
    import io
    f = TTFont(io.BytesIO(data), fontNumber=0, lazy=True)
    tables = set(f.reader.tables.keys())
    f.close()
    if 'glyf' not in tables:
        sys.exit('%s has no glyf table (CFF outlines) — ReportLab cannot use it' % name)
    if 'cmap' not in tables:
        sys.exit('%s has no cmap table' % name)
    return len(data)


def main():
    os.makedirs(OUT, exist_ok=True)
    print('font directory: %s' % OUT)
    print('source: github.com/%s (OFL)  |  transport: %s'
          % (REPO, 'gh api' if USE_GH else 'https'))
    total = 0

    for name, path in sorted(STATIC.items()):
        print('  %-30s ' % name, end='', flush=True)
        data = fetch(path)
        check_ttf(data, name)
        with open(os.path.join(OUT, name), 'wb') as fh:
            fh.write(data)
        total += len(data)
        print('%.1f MB' % (len(data) / 1e6))

    from fontTools.ttLib import TTFont
    from fontTools.varLib import instancer
    import io
    for path, targets in VARIABLE.items():
        print('  %s (variable)' % path)
        raw = fetch(path)
        vf = TTFont(io.BytesIO(raw), lazy=False)
        axes = {a.axisTag: (a.minValue, a.defaultValue, a.maxValue) for a in vf['fvar'].axes}
        for name, loc in targets:
            for tag, val in loc.items():
                if tag not in axes:
                    sys.exit('%s: %s has no %s axis' % (name, path, tag))
                lo, _d, hi = axes[tag]
                if not (lo <= val <= hi):
                    sys.exit('%s: %s=%s outside %s..%s' % (name, tag, val, lo, hi))
            inst = instancer.instantiateVariableFont(vf, loc, inplace=False, updateFontNames=False)
            buf = io.BytesIO()
            inst.save(buf)
            data = buf.getvalue()
            check_ttf(data, name)
            with open(os.path.join(OUT, name), 'wb') as fh:
                fh.write(data)
            total += len(data)
            print('    -> %-26s %s  %.1f MB' % (name, loc, len(data) / 1e6))
        vf.close()

    expected = set(STATIC) | {n for t in VARIABLE.values() for n, _ in t}
    missing = expected - set(os.listdir(OUT))
    print('\n%d faces, %.1f MB written' % (len(expected) - len(missing), total / 1e6))
    if missing:
        sys.exit('still missing: %s' % ', '.join(sorted(missing)))
    print('all twelve faces present and glyf-outlined')


if __name__ == '__main__':
    main()
