# Audit matrix — 日本語 MASTER, Second Edition

This is the working record of the audit that produced the Second Edition. It is
kept separate from the book itself: the book states *what* it claims, this file
records *what was checked, how, and what could not be resolved*.

- **Baseline:** `Nihongo_Master_N5-N1.pdf`, 402 pages, 346 bookmarks, 23,391,372 bytes, PDF 1.7.
- **Second Edition:** 386 pages, 361 bookmarks, ~2.1 MB, A4, single file.
- **Source of truth for content:** the baseline PDF itself. No other copy of the
  manuscript exists; everything in the new book is either baseline content that
  survived the audit, or new writing.
- **Rebuild:** `cd tools && python3 extract.py && python3 group.py && python3 -c "import render; render.build('../Nihongo_Master_N5-N1_2nd_Edition.pdf')"` — repo-local, no external working directory.

---

## 1. How the baseline was read

| Step | Script | Output | Note |
|---|---|---|---|
| Text + geometry extraction | `build/extract.py` | `ir.json` | PyMuPDF `get_text("dict")` spans; plain `get_text()` produced U+FFFD on three pages |
| Semantic blocking | `build/group.py` | `doc.json` | 402 pages → typed blocks (paragraph, table, callout, example, heading) |
| Text search | `build/findtext.py` | — | regex over blocks, used before writing every correction |
| Correction set | `build/mkcorrections.py` | `corrections.json` | each `old` string verified to occur verbatim in `doc.json` |
| Numbering repair | `build/renumber.py` | — | heading/caption renumbering + cross-reference repair |
| Index rebuild | `build/indexfix.py` | — | R16 rebuilt as a real column grid |
| New sections | `build/newsections.py` | — | R46–R69 |

The full extracted text (402 pages, ~501,710 characters) lives at
`audit/full.txt`; the bookmark dump at `audit/toc.txt`.

---

## 2. Phase order actually executed

1. **Content audit** — read all 402 pages; catalogued architecture, section
   inventory, and numbering.
2. **Structural audit** — matched the 346 baseline bookmarks against extracted
   headings; found the heading set and the printed TOC disagree in places.
3. **Accuracy audit** — targeted search for absolute claims
   (`không bao giờ` 12 hits, `tuyệt đối` 12 hits), for absolute-looking rules in
   the reference sections, and for examples used to prove rules they contradict.
4. **Defect triage** — separated (a) factual errors, (b) over-generalisation,
   (c) numbering defects, (d) layout defects, (e) genuine gaps.
5. **Source verification** — web verification of every externally checkable
   claim that the Second Edition adds or re-states (list in §5).
6. **Correction writing** — 11 verified replacements (`corrections.json`).
7. **Numbering repair** — 48 sub-headings, 3 table captions, 27 cross-references.
8. **Gap filling** — new sections R46–R69 written as flowable generators.
9. **Reference-index rebuild** — R16 rebuilt from raw geometry.
10. **Layout pass** — running heads, heading/rule collision, blank pages, TOC scope.
11. **Bookmark pass** — full hierarchy restored (depth 4, 361 entries).
12. **QA pass** — glyph coverage, placeholder leakage, sparse-page scan, index completeness.
13. **Completeness check** — index page references compared baseline vs new.
14. **Documentation** — this file.

(Front-matter, colophon, back matter and the Can-do maps were edited in step 8
and revisited in step 10.)

---

## 3. Confirmed errors in the baseline, and their disposition

| # | Baseline location | Problem | Disposition |
|---|---|---|---|
| 1 | p.52 | 「だ không bao giờ xuất hiện trong văn viết trang trọng」 — absolute and false | Rewritten: register-based explanation, だ in headlines/slogans/dialogue |
| 2 | p.43–44 | 「Không dùng hai は trong cùng một mệnh đề」 — stated as a prohibition | Rewritten: not ungrammatical; each は adds a contrast axis |
| 3 | p.44 | 「が bắt buộc trong ba trường hợp」 | Rewritten: near-always, with the topic-promotion exceptions named |
| 4 | p.45 | 「を chỉ đi với động từ」 — misleading definition | Rewritten: adds 家を出る / 道を歩く / 大学を卒業する |
| 5 | p.39 | 「mỗi từ chỉ có một điểm rơi duy nhất」 | Rewritten: at most one; heiban words exist; sentence-level accent added |
| 6 | p.39 | mora table romanised 東京 as `to-u-kyo-u` | Corrected to `to-o-kyo-o` |
| 7 | p.43 | devoicing stated as a rule; contradicted by its own examples | Rewritten: necessary vs sufficient condition; four modulating factors |
| 8 | p.44 | 「Người Nhật sẽ không bao giờ chê bạn lịch sự quá mức」 | Rewritten: both directions acknowledged, over-politeness named |
| 9 | p.335 | pitch-accent dictionary advice (one dictionary only) | Extended with the audio-dictionary check |
| 10 | p.339 | 恋仇 こいがたき listed under 「連濁 bị chặn」 | Located; recorded in R66 as a mislabelling class |
| 11 | pp.340–341 | 電話をする / 注意をする / 写真を写す marked ✗ | Located; contradicted by R22 (collocation) and by common usage |
| 12 | p.338 | R21.1 さ→ざ row held a た-row example and a garbled 雨+服→あまば | Located; recorded as a defective row |
| 13 | p.224 | Ryukyuan described as 「khác hệ」 | Located; R25 states the Ryukyuan languages are Japonic |
| 14 | p.226 | unsourced katakana statistic; incomplete スマート gloss | Flagged 要検証 |
| 15 | R11 (p.291) | Kubozono 2002 cited for loanword clipping | Citation repaired to Kubozono 2010, DOI 10.15084/00000559 |

---

## 3b. Structural defects found while proof-reading the re-typeset pages

The re-typesetting itself introduced a class of defect that text-level review
cannot see: three printed devices were destroyed by the line-sorting step, so
their content survived but stopped being readable as a device. Found by
comparing rendered pages against the First Edition and then measuring the source
geometry (marker x, body x, baseline offset).

| Device | Number affected | Evidence in the source PDF | Repair |
|---|---|---|---|
| Numbered list with hanging indent | 6 lists (p.49 `Ba hệ quả quan trọng`, p.99, p.101 five-step method, …) | marker at x≈68.8, item text at x≈79.1, marker baseline 0.2–0.4 pt *below* its own first line | markers recognised (`1.` `2)`), each paired to the indented line it labels; numbering kept |
| Run-in label | 604 labels | 7.4–7.6 pt bold line alone on its baseline (e.g. `Ý nghĩa cốt lõi / 中心的な意味`), body at 9.2 pt below | emitted as `label`, set as a small vermilion line — the First Edition's own device |
| Boxed callout swallowed by the preceding paragraph | 36 labels (of 275) | label carries `／`, 9.1 pt body follows | paragraph loop now stops at a label; box restored |
| Table row that is only a list marker | 3 rows (p.49 BẢNG 3.1, p.346 BẢNG R25.2) | body-size marker inside the table region | extension of the table region stops at body-size markers |

Verification after the repair, against the previous Second-Edition build:

- whole-book character multiset **identical** (zero characters lost or gained
  except the six restored list bullets);
- 287 tables, 84 `h2`, 361 bookmarks — unchanged;
- the two borderline tables checked by hand: `BẢNG 3.1` (now ends before the
  list) and `BẢNG R25.2` (wrapped date cells `4)` / `7)` kept inside the table).

Because 604 labels now occupy their own lines, the book grew from 368 to 386
pages. This is a deliberate legibility cost, not padding: each label line
belongs to an explanation that was previously buried mid-paragraph.

---

## 4. Structural repairs

### 4.1 Reference numbering (R21–R34)

The baseline numbers the sub-headings inside R21–R34 with the number of the
*previous* section: 20.x inside R21, 21.x inside R22, … 33.x inside R34, while
the table captions in the same sections use the correct number. R26 also had a
missing number and a duplicate.

- 48 sub-headings renumbered to match their section.
- 3 captions in R26 renumbered (gap closed, duplicate removed): R26.1–R26.7.
- 27 cross-references in the running text repaired (15 distinct strings).
- Recorded in the book itself, in the reference map and in the numbering note.

### 4.2 Reference index (R16)

The baseline prints R16 in newspaper columns; the baseline's own layout spills
entries across column and page boundaries, so the text is fragmented mid-word.
The Second Edition re-reads those seven pages from raw geometry and prints them
as a genuine three-column index grid (two columns for the Vietnamese index),
with the level markers N5/N4/N3/N2/N1/REF kept as their own lines.

Completeness check: every page reference present in the baseline index is
present in the new index. The only references not carried over are the baseline
index's *own* folios (317–323), which are not references to content.

**Page-number translation.** The baseline index cites *First-Edition* pages, so
in a re-typeset book every number is stale. Measured on a 150-reference sample:
20 % resolved on the cited page in the first pass of this edition, against 82 %
in the First Edition — i.e. the defect was real and large. `tools/idxmap.py`
rebuilds the correspondence (baseline bookmarks matched against this edition's
bookmarks, ~370 validated anchor points, linear interpolation between them) and
`indexfix.py` translates every index number through it. After the remap the same
sample resolves **113/150** and a sample re-read out of the *printed* index
resolves 112/133. The map is committed as `tools/idxmap.json`; it must be
regenerated whenever the layout changes (two-pass build, see `tools/README.md`).

### 4.3 Layout

| Defect | Cause | Fix |
|---|---|---|
| Heading rule drawn across the first line of the title | `wrap()` returned only the text height | rule offset by `RULE_GAP` |
| Running head stale / wrong chapter name | module-level state set only at chapter boundaries | per-page heading state, resolved on the *first* heading of each page |
| Blank page between a Can-do map and the Part divider | two page breaks in sequence | one |
| Nearly-empty last TOC page | TOC that also listed 238 sub-headings | printed TOC limited to parts / chapters / R-sections; the PDF outline keeps everything |
| Pages whose content stopped halfway | chapter-boundary page breaks with nothing following | content reflows; 0 pages now end above 42 % of the text block |

Final fill statistics: median 0.95, mean 0.94; the only light pages are the six
part dividers (intentional, type B).

---

## 5. External claims verified for this edition

All verified by fetching the issuing body's own publication; access date
17 September 2026.

| Claim | Source | Used in |
|---|---|---|
| 「敬語の指針」, 文化審議会答申, 平成19年2月2日; five types, 尊敬語 / 謙譲語Ⅰ / 謙譲語Ⅱ（丁重語）/ 丁寧語 / 美化語 | 文化庁 | R3, R28, R59 |
| 「日本語教育の参照枠」報告, 文化審議会国語分科会, 令和3年10月12日; six CEFR levels A1–C2, 493 Can-do, five 言語活動 | 文化庁 | Can-do maps, R68 |
| JF 日本語教育スタンダード; levels driven by 課題遂行能力 (Can-do) | 国際交流基金 | Can-do maps |
| 「公用文作成の考え方」建議 2022-01-07; 内閣官房長官通知 2022-01-11; classification of 公用文; 、 for horizontal writing | 文化庁 | R60 |
| 「ローマ字のつづり方」内閣告示第四号, 令和七年十二月二十二日, 内閣総理大臣 高市早苗; 昭和二十九年内閣告示第一号 abolished; Hepburn-based (`shi` `chi` `tsu` `fu` `ju`); 撥音 `n`, 促音 doubled, 長音 macron or doubled vowel; established spellings unchanged; IME input unaffected | 文化庁 国語施策情報, 内閣告示・内閣訓令 page (fetched 2026-09-17) | R20, R46, R61 |
| JLPT CEFR reference display from December 2025; thresholds N5 80+ A1, N4 90+ A2, N3 95–103 A2 / 104+ B1, N2 90–111 B1 / 112+ B2, N1 100–141 B2 / 142+ C1; shown only to those who pass, and only for 言語能力・受容活動能力 (no speaking/writing/interaction); level structure unchanged | 日本語能力試験 公式 `Indication of the CEFR Level for Reference` (fetched 2026-09-17) | R11, R61, Can-do maps |

**Not independently verified in this pass:** the readings of individual
pitch-accent entries in R19/R31 (these are dictionary-dependent and are already
tagged 要検証 in the book), and the exact contents of the baseline's romaji
tables beyond the 2025 内閣告示.

---

## 6. Verification register

- 59 「CẦN KIỂM CHỨNG / 要検証」 boxes in the Second Edition (baseline: 45).
- Six confidence levels used consistently: 公式 · 研究知見 · 使用実態 ·
  一般的な教育上の説明 · 編集上の整理 · 要検証.
- R68 restates the register as a working system: six reasons a claim can be
  uncertain (A–F), an eight-column record template, and an explicit
  prediction of which content will age.

**No corpus was queried for this edition.** Every 使用実態 label rests on
published descriptions, not on the editor running a query against BCCWJ, CSJ,
CEJC or I-JAS. This is stated in the book (R67, bibliography group 2) and is the
single largest limitation of the edition.

**No expert review.** The book has not been read by a Japanese-language teacher,
a native speaker reviewer, or a linguist. The colophon and R68 say so.

---

## 7. Open items carried into a third edition

1. Corpus verification of every 使用実態 claim (see §6).
2. Pitch-accent values in R19/R31/R48 against a single reference dictionary.
3. The 12 absolutism hits that were located but not all rewritten — the
   remaining ones are contrastive rather than false (e.g. 「không bao giờ」 used
   inside a *definition* of a contrast), and each needs a manual read.
4. Ryukyuan and Ainu: terminology and classification follow the baseline's R25;
   no new research was consulted.
5. Vietnamese glosses were inherited from the baseline and checked for
   consistency, not re-edited for style.
6. The reserved numbers R48, R52, R55–R58, R63, R64, R69 are permanently filled
   by baseline sections R19+R31, R43, R23, R44, R34, R45, R24, R25 and R16; the
   mapping is printed in the reference map. If a third edition wants a strict
   R1–R69 sequence, those nine sections have to be renumbered physically.

---

## 8. 実際の日本語 ／ REAL JAPANESE — the five interludes

The brief for the Second Edition asked for two things the book did not have: a
recurring **実際の日本語 ／ REAL JAPANESE** section, and its companion block on
**why this sounds natural**. §8 records what was built, on what evidence, and
where the limits are.

### 8.1 What was built

Five interludes, one at each level boundary, printed immediately after that
level's Can-do map (so the last page of a level shows the level's language in
use, not a summary):

| # | Scene | Level closed | Page |
|---|---|---|---|
| ① | Convenience store, 20:40 | N5 | 88 |
| ② | Restaurant — ordering and paying | N4 | 123 |
| ③ | A request, a refusal, and ウチ/ソト on the phone | N3 | 169 |
| ④ | A project meeting with a delay in it | N2 | 201 |
| ⑤ | Media montage — news, interview, advertisement, fiction | N1 | 238 |

Each has the same skeleton: context → dialogue panel → a line-by-line "why this
sounds natural" block → a "what a textbook teaches / what people say / where the
difference comes from" table → a "usable now" table → a limit box → the
confidence levels of that interlude stated in one line.

The device is not an invention of this edition. The First Edition already
printed なぜ ／ VÌ SAO NGHE TỰ NHIÊN boxes inside the reference sections (five of
them: pp. 106, 126, 262, 357, 377 of the baseline, i.e. R28, R36, R44, R51). The
interludes reuse that exact house label and open the same device along a whole
conversation rather than one question at a time. Nothing was styled to look
like a new feature.

### 8.2 Sources actually consulted for §8

* **文化審議会答申「敬語の指針」 (平成19年2月2日, 文化庁, 77 pp.) — read in
  full for this revision on 2026-09-18** (bunka.go.jp, PDF). Used for: the five
  keigo types and the 謙譲語Ⅰ/Ⅱ distinction (第2章第1–3); お(ご)……する as a
  謙譲語Ⅰ form and the error of using it for the other party's action
  (第2章第1【注】); お(ご)……いたす as both 謙譲語Ⅰ and Ⅱ (第2章第3【補足イ】);
  でございます as 丁寧語 at 丁重語 level (第2章第4); いただく carrying the
  "receiving a favour" meaning (第2章第2【補足】); 自分側は立てない and the
  third-party conditions (第2章第6 (1)–(3)); dialectal keigo 〜はる and the
  Tōhoku/Kantō 文末表現 reference (第1章第2-1); the warning against gender- and
  generation-based prescriptions (第1章第2-2); the observation that public and
  broadcast keigo is taken as a model (第1章第2-5).
* **文化庁「国語に関する世論調査」(平成18年2月調査)**, as cited in 敬語の指針
  第1章第2-2: お弁当 used by 10–30 % of men in every generation against 70–80 %
  of women, and the あげる/やる shift. Quoted in interlude ① as an illustration
  that 美化語 is a matter of person and generation, not correctness.

### 8.3 What is editorial, and what is not

The dialogues are **editorial reconstructions written for this edition**. They
are not transcripts, not recordings, and not corpus examples — this edition
queried no corpus (§6). Consequently:

* every item in a "why this sounds natural" block ends with its confidence
  level (公式 where a document was read, 一般的な教育上の説明 for the usual
  teaching account, 編集上の整理 where the editors are describing a pattern they
  wrote, 要検証 where nothing could be established);
* each interlude's limit box states, in the book, which parts have sources and
  which do not;
* two items were deliberately **left unresolved and tagged**, because no source
  read for this edition settles them: 「〜のほう」 (very common in speech; no
  official text consulted governs it) and 「〜になります」 in service Japanese
  (widely discussed in journalism and guidebooks, but not treated in 敬語の指針).
  Likewise 「了解です」 with a superior (varies by workplace) and the frequency
  of any of these forms (no corpus was counted).

### 8.4 The index gained a third grid (R16.3)

The new terms introduced by R46–R69 and by the interludes are listed in a new
R16.3 grid. Its right-hand numbers are **section numbers, not page numbers** —
stated in the grid's own heading. A section number stays correct when the layout
moves; a page number does not, and this edition has no mechanism that could
rebuild an index of its own writing (the inherited R16.1/R16.2 grids are rebuilt
from the First Edition's geometry, `tools/indexfix.py`).

The index's inherited "how to use" note claimed the index “cannot drift from the
content”. That was true of the First Edition's generator and is not true here,
so it was corrected in place (corrections.json), with the measured resolution
rate printed instead. The index now also documents the translation step.

### 8.5 Verification of §8

* whole-book character multiset against the committed build: **lost 29, gained
  30,063**. The 29 are all the digit `9`, and they come from the index page
  remap rewriting ~500 numbers; every line of 25+ characters that is absent from
  the new build comes from the printed table of contents or from the index
  (297 lines, all accounted for: 108 TOC + 189 index). No prose was lost.
* printed table of contents re-checked by geometry: all five interludes and all
  five Can-do maps carry the correct page (`実際の日本語 ①` → 88, and so on).
* glyph coverage: every character in the new content has a face (the build
  prints this; it caught one Chinese variant character, since fixed).
* 407 pages, 367 bookmarks (depth 4), 2.2 MB, 0 U+FFFD, 0 control characters,
  seven light pages (all deliberate section ends).
* the working-tree PDF present at the start of this revision carried a broken
  text layer (81,448 control characters; MuPDF could not parse its embedded
  font programs). The committed build (HEAD) was sound, and this rebuild is
  sound; the text layer is now verified as part of the QA pass. Rebuilds under
  ReportLab 4.2.5 and 5.0.1 were compared and give identical page text,
  identical outline and the same 407 pages, so the defect was not a toolchain
  version issue.

### 8.6 Added to the open list

7. The interludes assert *what people say* from teaching descriptions and from
   the two official documents above. A third edition should test them against
   recorded speech (CEJC, I-JAS, BTSJ) or against native-speaker judgement
   collected for the purpose — and should say which.
8. 〜のほう, 〜になります and 了解です (see §8.3) need a source, or they stay
   tagged for good.
