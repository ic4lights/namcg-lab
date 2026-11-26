# Review r1 - item 130 (gatekeeper)

Source: gatekeeper agent, 2026-11-26. Saved verbatim by the orchestrator (HTML entities restored to plain
characters; content unaltered). Pins are sha256[:12] (orchestrator style).

---

VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/0

## Verdict
Both payload edits are byte-minimal, wrapper-only, and independently reproduce the claimed 14 -> 1 overfull-hbox reduction with zero content, label, citation or status change; accepted as-is.

## Source reading
digest + targeted reads (correct level: the payload changes no definition, assumption, scope statement or status passage; no manuscript prose changes at all, so full-scan triggers 3(a)-(d) do not apply). Read in full: `proposals/130-margin-tightening/proposal-r1.md`, `payloadA-preamble.tex`, `payloadB-ch03.diff`, `cert_130.py`, `journal-130.md` (listed; scripts read in full), `namcg-book7.tex` L1-40 + full `\include`/`\bibliography` list, `chapters/ch03-matrix-action.tex` L780-830 (whole table block), `chapters/appH-microscopic-proofs.tex` L3425-3450 (residual paragraph). No unreadable files. `git status` after all verification: `namcg-book7.tex`, `chapters/`, `bib/` clean.

## Claim under review
Two typographic edits (preamble `\setlength{\emergencystretch}{2em}`; local `\tabcolsep` wrapper on the ch03 scales table) reduce right-margin Overfull \hbox count 14 -> 1 (max 17.02pt -> 1.215pt). Not an Appendix H problem; carries no status/priority/completion label. Critical-path set (A, B, C, D1, E, F, G-derived, N) untouched - confirmed no manuscript text changes anywhere.

## Checks performed
- **Bytes/hashes (direct, my own script `scratch/gk130/bytes_check2.py`, chr(92) construction after my first heredoc mangled backslashes):** payloadA = 36 B `f4aa60aa4099`, ASCII, CRLF-terminated; insertion bytes extracted from the diff itself: ins1 = 30 B `717a15da8b92`, ins2 = 3 B `e22faa535bd2`; diff 1026 B `8b2f0ffa435a`; cert_130.py 9107 B `2054773e2663`. All match claims. Live-tree anchors: `\setstretch{1.12}` count 1; `\begin{tabular}{@{}ll@{}}` count 1 (L802); `\end{tabular}` count 1 (L812). Tracked hashes: book tex `bf3e291ffb15`, ch03 `1e3e37b31a1e` - match.
- **CRITICAL semantic check (payloadB):** applied both insertions via anchor replace, then stripped them: result byte-IDENTICAL to live ch03 (`strip-restore identical: True`, patched delta exactly +33 B). Diff plus-lines are exactly the two wrapper lines; all cell/math bytes untouched; table-block brace balance 0; group opens before `\begin{tabular}` and closes after `\end{tabular}` inside the `center` environment, so `\tabcolsep` is locally scoped and the table renders identical content. Width arithmetic independently checked: 2 inter-column separations x 3pt saving = 6pt shrink vs 5.04942pt overflow -> 0.95pt clearance; candidate compile confirms 0 boxes in the ch03 region.
- **CRITICAL semantic check (payloadA):** line is exactly the standard TeX `\dimen` assignment, a legal preamble placement (global effect for the document body; standard Mittelbach remedy); no other `\emergencystretch` set anywhere in the preamble or `chapters/` (grep: no matches), so no conflict or supersession. Probe rerun in my scratch dir: `DEFAULT_EMERGECYSTRETCH EC=0.0pt` - the line is a genuine default-changing edit.
- **Reproduction pack (direct re-run):** `python -I proposals/130-margin-tightening/cert_130.py` from repo root -> `CERT130 PASS BASE14 CAND1 CH03SITE0 MAX1.215`; positive controls fired (parser 1 box @ 9.99; region 1-in/1-out); BASE rc 0 with ch03-region [5.04942]; CAND rc 0, 1 box, owner appH, mirror trace true; TRACKED hashes unchanged. Writes confined to `scratch/margin-typo/cert/` as designed. Parser uses string-split on `'Overfull '+chr(92)+'hbox ('` - correct construction, no backslash-h regex.
- **Own independent compile (`scratch/gk130/gk_build.py`, own parser, 2 passes each, -output-directory into scratch/gk130 only):** BASELINE from live root tree: rc 0, exactly 14 boxes, sizes 17.02370/16.28656/12.27011/11.18150/8.50606/7.81596/7.72087/6.00660/5.04942/2.99620/1.68848/1.33446/1.21500/0.32002 with per-file+line attribution exactly matching the dispatch list (ch13 L52-55, ch02 L71-75, appH L2803/L138/L2950/L4033/L1600/L3514/L4038/L2900/L3437, ch03 L802-813, ch17 L475-481, ch06 L42-49); 0 error lines, 0 undefined refs/citations, 448 pages, PDF 3297556 B - byte-size identical to tracked root PDF. CANDIDATE mirror (both patches): rc 0, exactly 1 box (1.215pt, appH L3437-3438), ch03 site gone, 0 error lines, 0 undefined refs, 448 pages, 0 Overfull boxes >2pt (introduces zero new overfulls of any size).
- **Honest-cost check:** baseline Underfull \hbox = 4, candidate = 6; the two new notices are exactly appH L3514-3525 (badness 2005) and L4033-4034 (badness 4132) - the paragraphs that previously overflowed by 6.01/7.82pt. Verified. (The proposal's secondary remark that Underfull \vbox counts shift by +-1 I did not verify; non-load-bearing.)
- **Residual acceptance:** 1.215pt is size-identical in baseline and candidate (stretch-invariant -> consistent with an unbreakable inline-math atom; the L3437 paragraph read and is dense `\operatorname`/`\det`/integral inlines), below the 2pt guard threshold; leaving it is the correct scope for a typographic-only package.
- **Provenance note resolved:** commit 0e39eb6 (2026-11-26 10:24) diff confirms `bindingoffset=0.05in -> 0.0in` in `namcg-book7.tex`. The 450-page figure recorded 11-25 predates that geometry change, so neither integrator nor researcher erred; both my clean runs and both cert runs give 448. The researcher's correction is right for the current tree. Not a proposal defect.

## Findings
None blocking, none major, none minor. Two notes for the integrator (not findings): (1) the `\end{tabular}` anchor is file-locally unique only - re-verify count 1 against the live tree at splice time per the standard serialization rule; (2) the proposal's prose is accurate as written; no integrated manuscript text exists to police beyond the two byte insertions.

## Scope of what is established
Verified byte state: payloadA 36 B `f4aa60aa4099`; payloadB insertions 30 B `717a15da8b92` + 3 B `e22faa535bd2`; diff 1026 B `8b2f0ffa435a`; strip-restore byte-identity of patched ch03; anchors unique (1/1/1) on the live tree; no competing `\emergencystretch` default (measured 0.0pt). Verified counts: baseline 14 overfull boxes max 17.0237pt; candidate 1 box 1.215pt; ch03 region 0; 448 pages both, rc 0, 0 undefined refs; Underfull \hbox 4 -> 6 with the two new sites localized. Cost accepted: 2 loose-line notices; residual 1.215pt accepted under the 2pt guard. Nothing about the physics content is established, changed, or implied by this package; no problem OPENED or CLOSED (no problem was open-able here).

## Recommended disposition
Integrate as-is. Integrate-ready statement:
- **namcg-book7.tex** - PRE 4257 B `bf3e291ffb15`. Byte anchor `\setstretch{1.12}`+CRLF (count 1, L22): insert payloadA bytes (36 B, `f4aa60aa4099`) immediately after the anchor line. Pure insertion (anchor keeps its CRLF; payload ends CRLF; no join consumed): **POST 4293 B**.
- **chapters/ch03-matrix-action.tex** - PRE 37978 B `1e3e37b31a1e`. Insert `{\setlength{\tabcolsep}{3pt}`+CRLF (30 B, `717a15da8b92`) immediately before byte anchor `\begin{tabular}{@{}ll@{}}` (count 1, L802), and `}`+CRLF (3 B, `e22faa535bd2`) immediately after byte anchor `\end{tabular}` (count 1, L812). Both pure insertions: **POST 38011 B = PRE + 33** (independently reproduced: patched-mirror delta +33, strip-restore identical).
- **chapters/appH-microscopic-proofs.tex** - NO CHANGE (residual 1.215pt accepted).
- Cert line: `CERT130 PASS BASE14 CAND1 CH03SITE0 MAX1.215`; gatekeeper's independent compile: BASE14/CAND1, max residual 1.215pt appH L3437-3438, 0 new overfulls, 448 pages, 0 undefined refs, tracked PDF/log unchanged by verification.

## Corrected snippet
None needed.
