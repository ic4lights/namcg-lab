# Proposal 059-d1-lorentz-local-frame, local round 3

This round answers `review-local-r2.md` (ACCEPT WITH REQUIRED REVISIONS, findings m1 to m4, no flags). It is a minimal revision: four sentence-level replacements in the insertion block. Nothing else changes. Everything in `proposal-local-r2.md` stands unless this file says otherwise: the Result, Target and status, Research and reasoning, Claim classification, bibliography additions (`bib-additions-local-r2.bib`, reused unchanged) and the ranked avenues.

## Result

The result is unchanged from local r2. The S^2 toy uses equivariant lifts (option (b)), with the two finite-N truncations and the bounded Lorentzian finite-N obstruction. The obstruction is that an anti-Hermitian finite-dimensional so(3,1) representation is zero, so a finite realisation with eta needs a Krein form. The composite paragraph is unchanged. Nothing closes: D / D1 stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Target and status

Unchanged from local r2. Problem D, sub-problem D1 (Lorentz local frame / connection content): OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. The block is placed at the end of the Problem D section, immediately before `\section{Problem E: signature}`.

## Source reading

Digest + targeted reads. `scratch/digest.md` reports `dirty-chapters: yes` because the tree carries uncommitted edits that are not part of this proposal. This round makes no new manuscript reliance. It edits only the block and checks it against the same appH pre-image, sha256 4ea0ee0f.... No full scan was made; the gatekeeper's disposition schedules one.

## Research and reasoning (changes only)

**m1 (required, applied verbatim).** The lemma "delta(P) = 2P delta(P), hence P delta(P) = 0 and delta(P) = 0" uses minimal projections. These exist when the commutative algebra is a *-algebra, so the replacement makes that hypothesis explicit. It also adds the hypothesis-free fallback. A finite-dimensional commutative algebra has finitely many characters, so its spectrum is finite and no base of positive dimension can be realised.

**m2 (required, applied verbatim).** The fundamental representation in the preceding clause is of so(4,1). The replacement says that the `sec:status-E` statement rests on the same fact for so(4,1) ⊃ so(3,1). The fact is that a non-compact simple algebra has no non-trivial finite-dimensional anti-Hermitian representation.

**m3 (optional, adopted). Factor verified.** The block defines `\mathcal L_i = \hbar_eff^{-1} ad_{X_i}`, so `[X_i,F] = hbar_eff L_i F`. For any X, `{X,[X,F]} = X^2 F - F X^2 = [X^2,F]`. Hence

    (1/2) sum_i {X_i, L_i F} = (2 hbar_eff)^{-1} sum_i {X_i,[X_i,F]} = (2 hbar_eff)^{-1} [sum_i X_i^2, F],

and the factor (2 hbar_eff)^{-1} is correct. The commutator is zero because sum_i X_i^2 = J^2/(j(j+1)) = 1. This form also matches the one-sided line. Write sum_i X_i L_i F = (2 hbar_eff)^{-1}(sum_i {X_i,[X_i,F]} + sum_i [X_i,[X_i,F]]), use sum_i [X_i,[X_i,F]] = hbar_eff^2 l(l+1) F on spin l, and the result is (1/2) hbar_eff l(l+1) F, as the block states. `d1_equivariant_finiteN.py` check A tests both statements numerically: "one-sided redundancy = (hbar^2/2) l(l+1) F" and "symmetric = 0".

**m4 (optional, adopted). Sign verified.** The so(5) sentence now states T = 0, F = 0 and R_ab^cd = -(delta_a^c delta_b^d - delta_a^d delta_b^c) explicitly. It adds "so that R_12^12 = -1", which is the a=1, b=2, c=1, d=2 component: -(1*1 - 0*0) = -1. This matches the S^2 toy and the su(2) truncation, where the block uses R_12^12 = -1. The same convention gives the unit-sphere Ricci -R_ab^ae = +(n-1) delta_b^e, which for n = 2 is the block's -R_ab^ae = delta_b^e. This is also the sign that `d1_equivariant_finiteN.py` check B2 tests ("T=0, R=-(dd-dd) (unit S^4), F=0", reps 5, 4 and 20, errors 0.0e+00). "Checked in dimensions 4, 5 and 20" is dropped. The claim covers any finite-dimensional unitary representation, which is justified because the relations are Lie-algebra identities in so(5). The three dimensions remain recorded in the script output.

## Claim classification

Unchanged from local r2. m1 adds one established fact: a finite-dimensional commutative algebra has finite spectrum. The m3 rewrite is an established identity. The m4 rewrite makes an existing established claim explicit.

## Proposed changes

File `chapters/appH-microscopic-proofs.tex`. The anchor, placement and procedure are the same as in local r2. Insert `insertion-block-local-r3.tex`, converted to CRLF, plus one blank CRLF line, immediately before the unique line `\section{Problem E: signature}`. The source block file keeps the r2 convention: UTF-8 without BOM and LF line endings, which the apply script asserts and converts to CRLF on insertion. The inserted manuscript bytes are therefore CRLF, with 0 bare LF after insertion. The r3 block replaces the r2 block in full. Apart from these four replacements it is byte-identical to `insertion-block-local-r2.tex`, which is kept.

Exact diffs from r2. Each old string occurs exactly once in r2, and the generating script asserted this.

1. m1. Old:
```latex
So every \(\mathrm{ad}\,\hat X_a\) that preserves \(\mathcal A\) vanishes on it, and no base of positive dimension is realised.
```
New:
```latex
So, for \(\mathcal A\) closed under the adjoint, as the functions on \(Z\) are, every \(\mathrm{ad}\,\hat X_a\) that preserves \(\mathcal A\) vanishes on it; in any case a finite-dimensional commutative algebra has finite spectrum, so no base of positive dimension is realised.
```
2. m2. Old:
```latex
this is the fact behind the statement in
```
New:
```latex
the same fact for \(\mathfrak{so}(4,1)\supset\mathfrak{so}(3,1)\) underlies the statement in
```
3. m3. Old:
```latex
\tfrac12\sum_i\{X_i,[X_i,F]\}=\tfrac12[\sum_iX_i^2,F]=0
```
New:
```latex
\tfrac12\sum_i\{X_i,\mathcal L_iF\}=(2\hbar_{\mathrm{eff}})^{-1}[\sum_iX_i^2,F]=0
```
4. m4. Old:
```latex
do the same for any finite-dimensional unitary representation \(\rho\) of \(\mathfrak{so}(5)\), checked in dimensions \(4\), \(5\) and \(20\).
```
New:
```latex
satisfy both relations with \(\mathsf T=0\), \(\mathsf F=0\) and \(\mathsf R_{ab}{}^{cd}=-(\delta_a{}^c\delta_b{}^d-\delta_a{}^d\delta_b{}^c)\), so that \(\mathsf R_{12}{}^{12}=-1\), for any finite-dimensional unitary representation \(\rho\) of \(\mathfrak{so}(5)\).
```

`diff insertion-block-local-r2.tex insertion-block-local-r3.tex` shows a single changed line, because the truncation paragraph is one source line. No labels, refs or citations were added or removed. The full r3 block is `insertion-block-local-r3.tex`.

Bibliography: unchanged. The block still uses `HattoriSekoTsuchiya2026`, `Elitzur1975` and `FradkinShenker1979` from `bib-additions-local-r2.bib`, and `HoKawaiSteinacker2025`, which is already in `bib/namcg.bib`.

## Verification scripts

- `apply_and_build_local_r3.py` is `apply_and_build_local_r2.py` with three changes. It reads the r3 block. Its docstring reads r3. It pins and asserts the post hash `POST`. The bib file, anchor and PRE hash are unchanged. The output is saved as `apply_and_build_local_r3.out`.
- `d1_equivariant_toy_symbolic.py` and `d1_equivariant_finiteN.py` were re-run unchanged with `python -I`. Their outputs are byte-identical to the saved `d1_equivariant_toy_symbolic.out` and `d1_equivariant_finiteN.out`: 20 and 30 PASS lines plus ALL PASS, 0 FAIL.

Reproduction pack. Run these from `proposals/local-gpu/059-d1-lorentz-local-frame/`:

    python -I apply_and_build_local_r3.py --build
      appH pre  sha256 4ea0ee0f50b0676ee161ff8ebd6620e3bd775ae74ffb1796b07d8a78f9e24b18 bytes 702490 CRLF 3557 bare LF 0
      pre-hash matches expected: True
      block LF bytes 9753 sha256 cfdca9e8bdb77b042f234993ffca0a927d794264b687b0fafd37dedb2be85a88
      block CRLF bytes 9760 sha256 b997222714415a0e824241106a91bd345ef2aa5ed5c4d48d845ce74e8a0e8f27
      anchor offset 257407
      appH post sha256 8d1eb5dccd6c808feb0bfbc935b5d5d0444dbfd8a46ac9c56c56519d07cfd41e bytes 712252 CRLF 3565 bare LF 0
      post-hash matches expected: True
      10 labels each defined once; 3 cites in additions, HoKawaiSteinacker2025 in bib
      pdflatex/bibtex rc 0, 404 pages, undefined/multiply-defined warnings: 0, BUILD CLEAN, temp copy removed: True
    python -I d1_equivariant_toy_symbolic.py   -> ALL PASS, identical to d1_equivariant_toy_symbolic.out
    python -I d1_equivariant_finiteN.py        -> ALL PASS, identical to d1_equivariant_finiteN.out

The build ran in a temporary copy outside the repository, which was then deleted.

## Decisions Taken

- I adopted m3. It is the gatekeeper's parallel form, and I verified its factor against the block's definition of `\mathcal L_i`, as shown above.
- I adopted m4. I wrote the curvature as -(dd - dd) with the explicit consequence R_12^12 = -1. This is consistent with the toy and su(2) lines and with check B2. I dropped the list of tested dimensions because the statement holds for all representations.
- I kept the r2 convention of an LF source block. The apply script requires it, and the manuscript bytes are CRLF either way.
- No other change.

## Milestone assessment

Routine.

## Status-label recommendation

None. D / D1 stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. The current critical-path set (A, B, C, D1, E, F, G-derived, N) is unchanged.

## Author decision needed

None.

## Remaining open step

Unchanged from local r2. The class, A, the frame and its non-degeneracy are still to be derived from the matrix dynamics. The ranked avenues are those in review-local-r2:
1. Krein-form finite-N realisation (relax the positive-definite form).
2. A noncommutative coefficient algebra.
3. Euclidean so(5) (gated on E).
4. N -> infinity with a regulated trace.
5. Approximate relations.

## Special instructions for the gatekeeper

- Confirm that the r2 -> r3 diff is exactly the four replacements above.
- Confirm the post hash 8d1eb5dc....
- The full scan scheduled in review-local-r2 is still due.
- Do not assert any closure of D / D1.
