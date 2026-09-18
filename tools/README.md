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
| `blocks.py` | ReportLab flowables: section head, callout, verification box, example, data table, bullets, **dialogue panel** and **why-this-sounds-natural block** (both split across pages) |
| `frontmatter.py` | colophon, printed table of contents, back matter |
| `newsections.py` | the new reference sections R46–R69, the Can-do maps, the bibliography, the numbering note |
| `realjapanese.py` | the five 実際の日本語 ／ REAL JAPANESE interludes, one per level boundary, each a dialogue panel + a line-by-line "why this sounds natural" block |
| `getfonts.py` | fetches the twelve text faces into `fonts/` (they are not committed) |
| `render.py` | assembles the story, applies the pre-passes, builds the PDF and the bookmark tree |

## Fonts

The twelve faces the book is set in (Shippori Mincho, Zen Old Mincho, Zen Kaku
Gothic New, Noto Serif JP, Noto Sans JP, Noto Sans Latin) are third-party
binaries under the SIL Open Font Licence and are **not committed** — together
they are ~60 MB and can be reconstructed in a minute:

```bash
python3 getfonts.py                # -> tools/fonts/   (61.8 MB, 12 faces)
```

It takes them from the Google Fonts repository. Eight of the twelve are shipped
there only as variable fonts; `getfonts.py` instances them to static Regular and
Bold with fontTools and rejects anything without a `glyf` table, because
ReportLab cannot embed PostScript/CFF outlines (the `.otf` builds of these faces
are unusable here). `theme.py` looks in `$NIHONGO_FONTS`, then `tools/fonts/`,
then the legacy `/home/user/fonts/`.

## The 実際の日本語 ／ REAL JAPANESE interludes

`realjapanese.py` holds five interludes — one at each level boundary, printed
immediately after that level's Can-do map. Each is a scene (convenience store,
restaurant, a request that gets refused, a project meeting, a media montage)
with three layers: the exchange itself as a dialogue panel, a line-by-line
"why this sounds natural" block, and two comparison tables (what a textbook
teaches → what people say → where the difference comes from), plus a limit box.

Two rules govern the file:

* **The honesty rule.** The exchanges are editorial reconstructions, not
  transcripts, and this edition queried no corpus. Every claim carries one of
  the book's six confidence levels printed at the point of use; each interlude
  ends with a box stating what has a source (e.g. 敬語の指針, 国語に関する世論
  調査), what is the editors' arrangement, and what is left 要検証.
* **The romaji rule.** Romaji is full in ① and ②, present only on new vocabulary
  in ③, and absent in ④ and ⑤ — the N5 → N1 progression of R17/R20, applied.

The device is not new: the First Edition already had なぜ ／ VÌ SAO NGHE TỰ
NHIÊN boxes inside the reference sections (R28, R36, R44, R51). The interludes
reuse that exact house label and open the same device up along a whole
conversation instead of one question at a time.

## Order of operations

Everything resolves its inputs and outputs next to the scripts, so the repo can
be rebuilt without any external working directory (set `NIHONGO_BUILD` to point
the pipeline somewhere else):

```bash
cd tools
python3 getfonts.py                # once: fetch the twelve text faces
python3 extract.py                 # baseline PDF  -> ir.json      (~3 s)
python3 group.py                   # ir.json      -> doc.json      (~0.5 s)
python3 -c "import render; render.build('../Nihongo_Master_N5-N1_2nd_Edition.pdf')"
```

After a rebuild, the build prints a glyph-coverage line. It must read
`glyph coverage: every character set has a face`: a character no registered face
carries renders as a blank, which is invisible in proof-reading by eye. (This
check caught a Chinese variant character that had slipped into the 実際の日本語
interludes.) The build was verified under ReportLab 4.2.5 and 5.0.1 — both give
407 pages, byte-identical page text and an identical outline.

### Two-pass build (the index map)

The index (R16) inherits the First Edition's entries, so its page numbers have
to be translated into this edition's pagination. That correspondence is built
from the *built* PDF, so a full rebuild is two render passes:

```bash
python3 -c "import render; render.build('/tmp/pass1.pdf')"
python3 idxmap.py /tmp/pass1.pdf                # -> idxmap.json
python3 -c "import render; render.build('/tmp/pass2.pdf')"   # settle the numbers
python3 idxmap.py /tmp/pass2.pdf                # confirm the map is stable
```

`idxmap.json` is committed. Regenerate it whenever the layout moves, or the
index will cite the previous layout's pages.

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
