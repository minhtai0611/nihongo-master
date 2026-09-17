# Rebuild pipeline — 日本語 MASTER, Second Edition

The Second Edition was produced by re-typesetting the First Edition, not by
re-writing it from a manuscript: the only source of the book's content is
`../Nihongo_Master_N5-N1.pdf`. This directory holds the pipeline that turns that
PDF into `../Nihongo_Master_N5-N1_2nd_Edition.pdf`.

## Files

| File | Role |
|---|---|
| `extract.py` | PyMuPDF pass over the baseline PDF → `ir.json` (page geometry + text spans + the 346 bookmarks) |
| `group.py` | `ir.json` → `doc.json`: 402 pages of spans → typed blocks (paragraph, table, callout, example, heading, part divider, run-in label, bullet/numbered list). Also the list/heading repair described below. |
| `doc.json` | committed because it is the actual input of the renderer; ~875 KB |
| `findtext.py` | `python3 findtext.py "<regex>"` — search `doc.json`, print block type + surrounding context. Used before writing every correction. |
| `mkcorrections.py` | regenerates `corrections.json` and verifies that every `old` string occurs verbatim in `doc.json` |
| `corrections.json` | the 11 verified text replacements (Second Edition accuracy fixes) |
| `renumber.py` | repairs the reference numbering (sub-headings R21–R34, captions in R26, 27 cross-references) |
| `indexfix.py` | rebuilds the reference index (R16) from raw geometry as a real column grid **and translates its page numbers** through `idxmap.json` |
| `idxmap.py` | builds `idxmap.json`: the First-Edition → Second-Edition page correspondence (bookmark anchors + validated text matches, interpolated) |
| `idxmap.json` | committed build data: 402 baseline pages → pages of this edition |
| `theme.py` | design system: palette, frame metrics, font registry, glyph fallback, paragraph styles |
| `blocks.py` | ReportLab flowables: section head, callout, verification box, example, data table, bullets |
| `frontmatter.py` | colophon, printed table of contents, back matter |
| `newsections.py` | the new reference sections R46–R69, the Can-do maps, the bibliography, the numbering note |
| `render.py` | assembles the story, applies the pre-passes, builds the PDF and the bookmark tree |

## Order of operations

Everything resolves its inputs and outputs next to the scripts, so the repo can
be rebuilt without any external working directory (set `NIHONGO_BUILD` to point
the pipeline somewhere else):

```bash
cd tools
python3 extract.py                 # baseline PDF  -> ir.json      (~3 s)
python3 group.py                   # ir.json      -> doc.json      (~0.5 s)
python3 -c "import render; render.build('../Nihongo_Master_N5-N1_2nd_Edition.pdf')"
```

### Structural repairs done by `group.py`

The First Edition prints three devices that a naive y-then-x line sort destroys.
`group.py` reconstructs them, and each rule is derived from measured geometry
(marker and body x positions, baseline offsets) rather than from guesswork:

| Device | Why it broke | Repair |
|---|---|---|
| Numbered lists (`1.` `2.` …) with hanging indent | markers are set ~0.4 pt *below* their item's first line and were never recognised (the bullet test only matched a lone `•`), so items merged into the following paragraph | `NUMBUL` + `order_markers()` place each marker before the line it labels; items are emitted as `{'m','t'}` and rendered with their own number |
| Run-in labels (`Ý nghĩa cốt lõi / 中心的な意味`) | a 7.4–7.6 pt bold line was classed as a table cell, so the preceding paragraph swallowed it and the entry read as one long blob | `solo_label()` stops the paragraph at the label and emits a `label` block (small vermilion line, the First Edition's device) |
| Boxed callouts (`LỖI THƯỜNG GẶP ／ よくある誤り`) | same swallowing, leaving the callout body inside the previous paragraph | boxed when the label carries `／` and 9.1 pt body follows; the run-in case above otherwise |
| Table rows that are only a marker (`1.`) or a heading (`Ba hệ quả quan trọng:`) | the table-region extension walked past the table into the list | extension stops on body-size markers, so the table ends where the First Edition's table ends |

Verified after the repair: identical character multiset for the whole book
(zero characters lost), 287 tables, 84 `h2`, 361 bookmarks.

### The index page numbers

The First Edition's index cites First-Edition pages; re-typesetting invalidates
every one of them (measured: 20 % of sampled references resolved on the cited
page of the first pass of this edition, 82 % in the First Edition itself).

`idxmap.py` rebuilds the correspondence from evidence: the 346 baseline
bookmarks matched against the 361 bookmarks of this edition give ~370 anchor
points, each validated against the text of the page, and `make_map()`
interpolates between them. `indexfix.py` then translates every index number
through that map. Measured after the remap: **84 %** of sampled references
resolve on the cited page (112/133), up from 20 %.

Regenerate when the layout moves:

```bash
python3 -c "import render; render.build('../Nihongo_Master_N5-N1_2nd_Edition.pdf')"
python3 idxmap.py                       # rebuild the correspondence
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

- 386 pages, A4, 361 bookmarks (outline depth 4), ~2.1 MB, fonts embedded.
  (18 pages more than the 368-page first pass, because 604 run-in labels and
  six lists are set on their own lines instead of being run into paragraphs.)
- Printed table of contents lists parts, chapters and R-sections; the PDF
  outline additionally carries every sub-heading and every R-section.
