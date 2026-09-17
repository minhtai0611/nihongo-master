# Rebuild pipeline — 日本語 MASTER, Second Edition

The Second Edition was produced by re-typesetting the First Edition, not by
re-writing it from a manuscript: the only source of the book's content is
`../Nihongo_Master_N5-N1.pdf`. This directory holds the pipeline that turns that
PDF into `../Nihongo_Master_N5-N1_2nd_Edition.pdf`.

## Files

| File | Role |
|---|---|
| `extract.py` | PyMuPDF pass over the baseline PDF → `ir.json` (page geometry + text spans + the 346 bookmarks) |
| `group.py` | `ir.json` → `doc.json`: 402 pages of spans → typed blocks (paragraph, table, callout, example, heading, part divider) |
| `doc.json` | committed because it is the actual input of the renderer; ~850 KB |
| `findtext.py` | `python3 findtext.py "<regex>"` — search `doc.json`, print block type + surrounding context. Used before writing every correction. |
| `mkcorrections.py` | regenerates `corrections.json` and verifies that every `old` string occurs verbatim in `doc.json` |
| `corrections.json` | the 11 verified text replacements (Second Edition accuracy fixes) |
| `renumber.py` | repairs the reference numbering (sub-headings R21–R34, captions in R26, 27 cross-references) |
| `indexfix.py` | rebuilds the reference index (R16) from raw geometry as a real column grid |
| `theme.py` | design system: palette, frame metrics, font registry, glyph fallback, paragraph styles |
| `blocks.py` | ReportLab flowables: section head, callout, verification box, example, data table, bullets |
| `frontmatter.py` | colophon, printed table of contents, back matter |
| `newsections.py` | the new reference sections R46–R69, the Can-do maps, the bibliography, the numbering note |
| `render.py` | assembles the story, applies the pre-passes, builds the PDF and the bookmark tree |

## Order of operations

```bash
cd tools
python3 extract.py                 # baseline PDF  -> ir.json      (~7 s)
python3 group.py                   # ir.json      -> doc.json      (~0.4 s)
python3 -c "import render; render.build('../Nihongo_Master_N5-N1_2nd_Edition.pdf')"
```

`render.build()` applies, in order: `corrections.json` (text fixes) →
`renumber.py` (numbering repair) → `indexfix.py` (index rebuild) → the baseline
body → five Can-do maps at the part boundaries → the R46–R69 block → back
matter. Build time is about 8 seconds.

`ir.json` (4.1 MB) is not committed: it is a pure function of the baseline PDF
and `extract.py`.

## Typography requirements

`theme.py` expects the Noto CJK **static instances** in `/home/user/fonts/`:

```
NotoSerifJP-Regular.ttf   NotoSerifJP-Bold.ttf
NotoSansJP-Regular.ttf    NotoSansJP-Bold.ttf
NotoSansLatin-Regular.ttf NotoSansLatin-Bold.ttf
```

The `.otf`/CFF members of the Noto CJK family **cannot** be used: ReportLab
rejects PostScript outlines (`postscript outlines are not supported`). The Latin
instances are required for IPA and for Vietnamese diacritics that the JP faces
lack; `theme.guard()` routes those code points automatically.

## Output

- 368 pages, A4, 361 bookmarks (outline depth 4), ~2.1 MB, fonts embedded.
- Printed table of contents lists parts, chapters and R-sections; the PDF
  outline additionally carries every sub-heading and every R-section.
