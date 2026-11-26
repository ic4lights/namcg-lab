# remote/claude .tex import and duplication review — 2026-11-25

Author instruction: bring in the .tex changes from the remote/claude branch, review for duplication, and identify
genuine corrections/improvements. Branch: `origin/remote/claude`, fetched tip `1aafb3d` (2026-11-25); merge-base with
`local/gpu` is `2cd49d0` (2026-11-05). Applied as uncommitted working-tree edits (author merges; no git merge was
done). Import method: per-block content analysis, never file checkout (branch appH predates our ordinals and would
have destroyed integrated work).

## 1. What was imported (uncommitted, in working tree)

| file | change | bytes now | classification |
|---|---|---|---|
| chapters/ch01-geometrogenesis.tex | replaces "It is a Ward identity of the microscopic theory, and that identity forbids..." with the hedged form: load-bearing hypothesis `Assumption~\ref{ass:EE}`, conditional Ward identity `Proposition~\ref{prop:ward}`, derivation open (`Problem~\ref{sec:status-B}`) | d7c1ca4e4652 / 16,547 / CRLF | GENUINE CORRECTION (claim-tier repair, rule 6) |
| namcg-book7.tex | geometry block: inner 0.72→0.9in, outer 0.60→0.45in, bindingoffset 0.10→0.05in | 30746a3add74 / 4,258 / CRLF | COSMETIC branch layout choice, imported per instruction; see flag below |

Both verified content-equal to the branch version modulo EOL (branch files are LF; ours remain CRLF). All three
cross-references (ass:EE ch06 L71, prop:ward ch06 L383, sec:status-B appH L156) exist.

FLAG (author): the imported book7 comments are internally wrong — "% slightly reduced" describes an increase of the
inside margin (0.72+0.10 = 0.82in → 0.9+0.05 = 0.95in) and "% total inside = 0.78in" states the wrong total. Values
imported verbatim; correct or revert the comments at the author's discretion. Net effect: wider text block; page
count unchanged at 450.

## 2. Duplication findings

- appE-rar-bridge, appI-gaia-wide, ch13-cores-galaxies, ch14-dissipation, ch16-falsifiers: **byte-identical at file
  level** between HEAD and branch (identical patches applied on both sides; nothing to import). The branch does not
  fix any author-queue MAJOR in these files (e.g. ch13 eq:G-sss sign is identical on both sides — still open).
- ch03, ch09, ch10, ch17: OURS-ONLY (branch lacks our later integrations).
- appH-microscopic-proofs: branch file (782,439 B) diverges from ours (883,075 B) by 592 KB; closest of our 96
  historical versions still differs by 405 KB → independent evolution, not a snapshot of ours. Of the branch's 59
  added blocks ≥40 B since merge-base: 1 byte-exact duplicate, 26 duplicates modulo the branch's de-standardized
  spelling "PROGRAMME CONDITIONAL" (ours: "PROGRAMME-CONDITIONAL", 48 occurrences), 11 duplicates modulo
  whitespace reflow → **38/59 (64%) are duplication**, not new work.
- Two pipelines produced byte-identical patches on five files and converging text on most of appH: the parallel
  workspace consumed the same integrated items; its divergence is mostly cosmetic + a set of original drafts (§4).

## 3. Blocks that are OLD or SUPERVISED versions of our own paragraphs — not imported

Branch paragraphs whose titles exist in our current appH (Explicit Weyl data flat-Abelian; Dragging regularity
covariance; Schwinger--Dyson insertion; Commutant labels at nonzero torsion; regulated Lorentzian integral; explicit
K fuzzy sphere; static scalar pole tachyonic; Edge entropy of a matrix block; and reflow-duplicates incl.
"Definitional status of the prescription"): word-level diffs show OUR versions carry the later gatekeeper-edited
content — e.g. our regulated-Lorentzian paragraph retains the status sentence "Assumption ass:lorentzian is not
discharged. Problem E remains open and PROGRAMME-CONDITIONAL" that the branch version lost, and our
C "Missing step." paragraph is the later "gauge-fixed quadratic scalar operator" wording (branch keeps the older
"full quadratic" variant plus a Cassini clause we edited out). Importing any of these would roll back integrated
text. Recorded, not imported.

## 4. Genuine branch-original material never on local/gpu — NOT imported (gatekeeper-unreviewed), held for author

Raw text: `reports/rc-parallel-apph-blocks-2026-11-25.md` (93,555 B, ASCII). Blocks (branch-diff index):

- 22: Problem C "Missing step." rewording variant (2,691 B) — our version is the newer edit; listed for comparison only.
- 27: 30,380 B — "Bearing on sec:status-E and the relaxations" reflection-positivity variant incl. singlets/constraint/
  mass/no-selection analysis (Ho--Kawai--Steinacker, Chatzistavrakidis A_{4,12}, Isono--Tomino, Liao2026 citations)
  + diverged drafts of the compact-toy and locked-frame-composite paragraphs we already have in reviewed form.
- 28: 23,711 B — "First-order equivariant class on the Heisenberg background with curvature: Landau sectors of the
  linearised equations" (E-area; title absent from all 96 historical appH blobs).
- 42: 300 B — TT-sector dispersion multline S_L = c·c·Z(q_0^2−k^2)(q_0^2−w^2) with c_T^TT, v^2, mu^2 (absent in ours).
- 48: 31,829 B — contains a leading fragment of a paragraph we have (diverged) + new paragraph "Conjugate-coordinate
  class times a fuzzy factor: the Hessian of a tree stabiliser on K, the one-loop weights on the cubic branch and the
  exchange of the scale of K (bounded no-go; correction of the cubic and mass branches)" (F-area).
- 49/50/51: 3,767 B — "The singlet sector at q=0", its "Consequence" paragraph, and its scope statement (F-area q=0
  channel; touches our Cassini/Newton comparison claims).
- Also inside block 20's region: citations `FlissFrenkelHartnollSoni2025`, `Frenkel2023EdgeModes` (edge-mode block
  entanglement) appear in branch text only; per rule 7 not imported and not independently verified.

Recommendation: if any of §4 should enter the manuscript, route it through the normal pipeline (researcher
re-derivation under our source pins → gatekeeper → integrator). Some of it (Heisenberg Landau sectors; fuzzy-factor
Hessian no-go) overlaps live E/F-area target space and could be briefed to the researcher as prior art rather than
imported.

## 5. Not imported, other

- Branch de-standardized spelling PROGRAMME-CONDITIONAL → "PROGRAMME CONDITIONAL" (49 occurrences): style drift,
  not an improvement; our hyphenated spelling kept throughout.
- Branch deletions of paragraphs we retain: all are their replacements of scope sentences (old text → reworded
  text); superseding text is the §3/§4 material.

## 6. Build

`python scripts/build_check.py` after the two imports: 2x pdflatex exit 0, 450 pages, bibtex 0 warnings, 0 undefined
refs/citations, 0 multiply-defined, tracked PDF restored, `git diff --check` clean. BUILD_CHECK PASS pages=450.

## 7. Process changes made from this review

- CLAUDE.md: import/EOL/spelling normalization convention (this review; 38/59 appH "new" blocks were false
  divergences until EOL+spelling were normalized).
- gatekeeper.md: claim-tier audit bullet for unconditional manuscript prose (the ch01 fix is the worked example).
- memory: remote/claude workspace facts and no-wholesale-import policy.
