# Proposal 072-d1-heisenberg-wider-linearised, round 2

This is a minimal revision of r1 in response to `review-r1.md` (AWRR; F1 and F2 major, F3-F7 minor, F8 optional).
The mathematics, the scripts s1-s6 and their outputs, the target, the ranked avenues and the scope are unchanged
from `proposal-r1.md`. Sections not repeated here are as in r1, except for the items listed under "Changes from r1".

## Result

The result is unchanged from r1 (see `proposal-r1.md`, "Result", items 1-5). The changes are wording only:
- The root display now states its exactness scope: exact in the J-blocks; numerical, at sampled points, for
  l <= 9 otherwise.
- The no-gap sentence now says why there is no gap (no momentum-independent term).
- The no-gap sentence now also records that chi enters as a rate, with the p -> 0 imaginary root q0 = -i c chi.
- "rate" becomes |Im q0|.

The package remains a bounded tree-level, linear-order no-gap result on the null-leg constant-connection
Heisenberg family. Problems D, F and N stay OPEN.

## Target and status

Unchanged from r1:
- Problem D: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.
- ch17 D1.
- Missing step: appH, Problem D ledger.
- Dependencies: 068 and 071.

The live appH sha256 is b98a3a34d2ac71800ceae7369db90d373d8bcdc139fe7fb81e7bad3e552df1c0. It was re-verified
before writing.

## Source reading

Digest + targeted reads:
- `make_digest.py --check` printed `DIGEST CURRENT` (dirty-chapters: yes).
- I re-read appH L1644-1648, the 071 closing paragraph and the anchor, to check that the assumptions named in the
  F8 closer are listed there ("the assumptions listed in the preceding paragraph"). They are: ass:frame-lock,
  ass:nondeg, ass:lorentzian, ass:local-lorentz and ass:EFT-a2. The non-identification with the emergent metric of
  ch:vierbein-emergence is also there.
- "Preceding paragraph" refers to the preceding `\paragraph` unit, here 071. That is the sense in which the insert
  already uses the phrase twice ("the wider ansatz ... of the preceding paragraph", "the survey of the preceding
  paragraph").

Full scan: not performed by the researcher in this round. The gatekeeper's 3(c) full scan is still owed, as the
review states.

## Research and reasoning

There is no new mathematics. One consistency check on S2/S3 was done by hand from the root formula
q0 = -(i/2)c chi +- ((p + (i/2)c chi)^2 + kappa p l)^{1/2}:
- At p = 0 the square root is +-(i/2)c chi.
- So q0 is 0 or -i c chi, with |Im q0| = |c chi|. This holds for every l.
- So for l >= 1 the supremum |c chi| is approached at p -> 0 as well as at p -> infinity. It is not attained at
  p > 0, by the r1 strict bound.
- This agrees with S2 ("as p -> 0 they tend to q0 = 0 and to the imaginary q0 = -i c chi") and with S3.

## Claim classification

Unchanged from r1. The S1 sentence makes the existing classification explicit in the text:
- exact: the J-block factorisation at zeta = x = 0;
- numerical: sampled points for l <= 9 otherwise;
- unresolved: higher levels.

## Changes from r1 (exact diffs)

### Block `appH_insert_r2.tex`

The block is generated from `appH_insert_r1.tex` by `make_insert_r2.py`. Each old string is asserted to occur
exactly once. The new strings are the gatekeeper's text, verbatim.

| # | Finding | r1 text | r2 text |
|---|---|---|---|
| 1 | F1 / S1 | `\]` newline `For \(l\ge3\)` | `\]` newline `This is exact in the blocks described below and numerical, at sampled points, for \(l\le9\) otherwise; higher levels are not checked. For \(l\ge3\)` |
| 2 | F3 / S1 | `of the maximal minors` | `of the minors of the generic rank` |
| 3 | F4 / S1 | `which contain all factors with \(l\le5\),` | `which on the observed pattern of levels contain all factors with \(l\le5\),` |
| 4 | F5 / S1 | `(exact in rational arithmetic)` | `(exact in rational arithmetic after rational reconstruction of the double-precision entries)` |
| 5 | F6 / S1 | `At \(\chi=0\) this gives the levels \(q_0^2=p^2+\kappa p\,l\) of the paragraph on left-invariant backgrounds with torsion for every \(\zeta,x\) (numerical).` | `At \(\chi=0\) and a sampled \((\zeta,x)\neq(0,0)\) the levels \(q_0^2=p^2+\kappa p\,l\) of the paragraph on left-invariant backgrounds with torsion are recovered (numerical).` |
| 6 | F2 / S2 | `No gauge-invariant gap or mass therefore appears for the Lorentz or torsion modes at this order, although the background carries the scale \(\kappa\) and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4\chi^2\kappa^2\neq0\), and no sign of a mass arises.` | `No term independent of the momentum enters, so no gauge-invariant gap or mass appears for the Lorentz or torsion modes at this order, although the background carries the scale \(\kappa\) and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4\chi^2\kappa^2\neq0\); \(\chi\) enters the roots only as a rate, since as \(p\to0\) they tend to \(q_0=0\) and to the imaginary \(q_0=-\mathrm ic\chi\).` |
| 7 | F2 / S3 | `with supremum \(|c\chi|\) as \(p\to\infty\);` | `with supremum \(|c\chi|\), approached as \(p\to0\) and as \(p\to\infty\);` |
| 8 | F7 / S3 | `its largest rate rises from` | `its largest \(|\operatorname{Im}q_0|\) rises from` |
| 9 | F7 / S3 | `Over all modes the largest rate is` | `Over all modes the largest \(|\operatorname{Im}q_0|\) is` |
| 10 | F8 | `Nothing here shows that the matrix integral selects this class, these backgrounds or the algebra \(\mathcal A\), or yields the frame and its non-degeneracy, so Assumptions~\ref{ass:frame-lock}, \ref{ass:nondeg}, \ref{ass:lorentzian}, \ref{ass:local-lorentz} and~\ref{ass:EFT-a2} are not discharged, and the frame of these backgrounds is not identified with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.` | `Nothing here shows that the matrix integral selects this class or these backgrounds, so the assumptions listed in the preceding paragraph are not discharged; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.` |

Nothing else in the block changed.

### Edit 2 (the stale sentence in the 071 closing paragraph): optional wording adopted

- r1 new string: `Family (ii) and its extension with \(\chi\neq0\) are linearised in the following paragraph; the survey solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\), for which no scaling symmetry is shown, are not linearised here, and`
- r2 new string: `Family (ii) and its extension with \(\chi\neq0\) are linearised in their Landau sectors in the following paragraph; the survey solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\), for which no scaling symmetry is shown, are not linearised here, and`
- The old string, which is unique in the live appH, is unchanged:
  `Family (ii), its extension with \(\chi\neq0\) and the survey solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\), for which no scaling symmetry is shown, are not linearised here, and`

## Proposed changes

### File `chapters/appH-microscopic-proofs.tex`

**Edit 1 (insert).**
- The placement is as in r1: the new block goes immediately before the unique line `\section{Problem E: signature}`
  (L1648). It directly follows the 071 closing paragraph, which ends `Problems~D, F and~N remain open and
  PROGRAMME-CONDITIONAL.`
- One blank CRLF line follows the block. Nothing is removed.
- The block, byte for byte, is `appH_insert_r2.tex`: CRLF, UTF-8 without BOM, 6317 bytes, 14 lines, bare LF 0,
  sha256 01b5d27a25bb8c19904ed13f26f29aae6b33d813bd66e11d3d63bbad01a42513.

```latex
\paragraph{First-order equivariant class on the Heisenberg background with curvature: Landau sectors of the linearised equations (conditional; not closure).}
Take the wider ansatz \(w_a{}^{cd}=k_a(\chi B^{cd}+\zeta N^{cd}+xN'^{cd})\) of the preceding paragraph on time times the Heisenberg group, with its normalisation and the fluctuation \(\mathbb D_a\to\mathbb D_a-h_a{}^c\mathbb D_c+\tfrac12\omega_a{}^{cd}\mathcal S_{cd}\), in the sectors of the paragraph on left-invariant backgrounds with torsion: \(E_0=\mathrm iq_0\), \(E_2=\mathrm ip\) with \(p>0\), and \(E_1\), \(E_3\) acting on oscillator levels. The linearised equations have real coefficients, so the sectors with \(p<0\) follow by complex conjugation. For a constant connection \(\mathsf F_{ab}[A]=E_aA_b-E_bA_a-\mathsf c_{ab}{}^dA_d\) contains no \(w\), and on this family
\[
\mathcal Q_b[A]=\mathcal Q_b[A]\big|_{w=0}-\chi\,k^a\mathsf F_{ab}[A]
\]
for all \(\zeta,x\) and all \(A\) (exact), so the connection adds only a gauge-invariant term of first order along the null \(k\). On \(A=(0,\phi,0,\mathrm i\phi)\), with \(\phi\) as in that paragraph, this gives \(\mathcal Q_b[A]=\bigl(q_0^2-p^2+\kappa p+\mathrm i\chi(q_0-p)\bigr)A_b\) (exact). The operator \(\mathcal Q\) agrees with the linearised third bracket of the operators on the bundle, order-zero part included (exact at a sampled point for polynomial \(A\), at two parameter sets). With \(q_\parallel=(q_0,0,p,0)\), every characteristic root of the forty equations in these sectors, a value of \(q_0\) at which their rank drops below its generic value, satisfies
\[
\bigl(q_\parallel+\tfrac{\mathrm i}2c\chi k\bigr)^2+\kappa p\,l=0,\quad\text{that is}\quad q_0^2-p^2+\mathrm ic\chi(q_0-p)=\kappa p\,l,\qquad c\in\{-1,1,3\},\ l\in\{-1,1,3,\dots\}.
\]
This is exact in the blocks described below and numerical, at sampled points, for \(l\le9\) otherwise; higher levels are not checked. For \(l\ge3\) the numbers of these quadratic factors are \(10\), \(6\) and \(4\) for \(c=1,3,-1\), twenty in all as at \(\chi=0\), and half of these at \(l=\pm1\); \(\mathcal Q\) has \(c=1\), and the class \(c=1\) has five times its multiplicities (numerical, at sampled \(\kappa,\chi,p\)). At \(\zeta=x=0\) a rotation of the \(1\)-\(3\) plane combined with the oscillator level is conserved, and in each of its blocks \(J=-2,\dots,3\), which on the observed pattern of levels contain all factors with \(l\le5\), the greatest common divisor of two random compressions of the minors of the generic rank, which every characteristic root annuls, is exactly the product of these factors at \((\kappa,p,\chi)=(1,\tfrac12,\tfrac12)\) and \((2,\tfrac14,-\tfrac13)\) (exact in rational arithmetic after rational reconstruction of the double-precision entries). For \(\zeta,x\neq0\) the same values and counts appear for \(l\le5\), and in the sector \(p=0\), where \(E_1\) and \(E_3\) commute, the roots lie on the complex cones \((q+\tfrac{\mathrm i}2c\chi k)^2=0\) with the same \(c\) (numerical, at sampled points). The kernel at generic \(q_0\) is the ten gauge directions for each level of the parameter, and the frame labels along \(E_0\) and \(E_2\) reduce to \(\mathcal Q\) as on family~(i) (numerical). At \(\chi=0\) and a sampled \((\zeta,x)\neq(0,0)\) the levels \(q_0^2=p^2+\kappa p\,l\) of the paragraph on left-invariant backgrounds with torsion are recovered (numerical).

So \(\chi\), \(\zeta\) and \(x\) shift no level: the values \(\kappa p\,l\) are those at \(\chi=0\), and \(\chi\) enters only through the imaginary null vector \(\tfrac{\mathrm i}2c\chi k\) added to \(q_\parallel\), whose contribution \(\mathrm ic\chi\,k^aq_a\) is linear in the momentum. No term independent of the momentum enters, so no gauge-invariant gap or mass appears for the Lorentz or torsion modes at this order, although the background carries the scale \(\kappa\) and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4\chi^2\kappa^2\neq0\); \(\chi\) enters the roots only as a rate, since as \(p\to0\) they tend to \(q_0=0\) and to the imaginary \(q_0=-\mathrm ic\chi\). The roots are \(q_0=-\tfrac{\mathrm i}2c\chi\pm\bigl((p+\tfrac{\mathrm i}2c\chi)^2+\kappa p\,l\bigr)^{1/2}\). For \(\chi\neq0\) none is real at \(p>0\), and their imaginary parts have both signs; for \(l\ge1\), \(|\operatorname{Im}q_0|<|c\chi|\), with supremum \(|c\chi|\), approached as \(p\to0\) and as \(p\to\infty\); for \(l=-1\) the largest value of \(|\operatorname{Im}q_0|\) is \(\tfrac12|c\chi|+\sigma_c\) with \(\sigma_c=\tfrac\kappa4+(\tfrac{\kappa^2}{16}+\tfrac14c^2\chi^2)^{1/2}\), attained at \(p=\sigma_c\) (by hand, checked numerically). For \(c=1\) this is the mode \(A\) above: the growing mode of the paragraph on left-invariant backgrounds with torsion persists at \(\chi\neq0\), its largest \(|\operatorname{Im}q_0|\) rises from \(\kappa/2\) to \(\tfrac12|\chi|+\sigma_1>\kappa/2\), and the growth is no longer confined to \(0<p<\kappa\). Over all modes the largest \(|\operatorname{Im}q_0|\) is \(\tfrac32|\chi|+\sigma_3\). These are section values and no norm is used, so, as for family~(i), no statement on stability is made.

These statements are for Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and no matter term, tree level, linear order in the fluctuation, the Lorentzian contraction and the wider family on time times the Heisenberg group with constant connection, in the sectors named. A norm, the nonlinear evolution of the growing modes, loops, for which the cancellation at second order about commuting matrices does not apply since the commutators of this background are nonzero, the solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) of the survey of the preceding paragraph, the regulated trace and the domains of the unbounded operators are not treated. On the Heisenberg algebra, constant connections with \(\eta^{ab}w_a{}^{cd}w_b{}^{ef}\neq0\), a form that vanishes on the wider family since \(k\) is null, also solve all three brackets, most of them with \(\mathsf R_{abcd}\mathsf R^{abcd}>0\) (numerical survey, not a classification); they are not linearised here. Nothing here shows that the matrix integral selects this class or these backgrounds, so the assumptions listed in the preceding paragraph are not discharged; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
```

**Edit 2 (stale passage in the 071 closing paragraph, L1646).**
- Replace the unique string
  `Family (ii), its extension with \(\chi\neq0\) and the survey solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\), for which no scaling symmetry is shown, are not linearised here, and`
- with
  `Family (ii) and its extension with \(\chi\neq0\) are linearised in their Landau sectors in the following paragraph; the survey solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\), for which no scaling symmetry is shown, are not linearised here, and`
- The rest of that paragraph is unchanged.

**Hashes and labels.**
- Pre-hash (live, re-verified): b98a3a34d2ac71800ceae7369db90d373d8bcdc139fe7fb81e7bad3e552df1c0, 753095 bytes.
- Post-hash after both edits: **a0efe483aea01e15fb88b95d351d0069f20b4bab9b23e5e09b573b0fddf4824d** (759480 bytes,
  bare LF 0).
- The only label referenced in the block is `eq:Smatrix`, defined once. F8 removed the `\ref`s to the five
  assumptions and to `ch:vierbein-emergence`. Those refs remain in the 071 closer, which the new closer points to.
- No new labels and no citations, so no bibliography change.
- There is one status sentence, in the last paragraph of the block.

## Verification scripts

New in r2:
- `make_insert_r2.py`: applies the ten replacements to `appH_insert_r1.tex`, asserting that each old string occurs
  once.
- `apply_and_build_r2.py`: has the same anchors as r1 and the Edit 2 text with "in their Landau sectors". It checks
  the pre-hash, the post-hash, the labels and the status sentence, then builds on a temporary copy outside the
  repository.

The r1 files are kept unchanged.

Reproduction pack, run from the proposal folder:

| Command | Expected invariant output |
|---|---|
| `python -I -B make_insert_r2.py` | ten lines `replaced once: ...`; `appH_insert_r2.tex bytes 6317 sha256 01b5d27a25bb8c19904ed13f26f29aae6b33d813bd66e11d3d63bbad01a42513 bare LF 0 lines 14` |
| `python -I -B apply_and_build_r2.py --build` | `pre-hash matches expected: True`; anchor and stale-passage anchor unique (L1648, L1646); `appH post sha256 a0efe483aea01e15fb88b95d351d0069f20b4bab9b23e5e09b573b0fddf4824d bytes 759480 bare LF 0`; `label eq:Smatrix defined 1`; pdflatex rc 0, 416 pages; `undefined/multiply-defined warnings: 0`; `BUILD CLEAN`; `temp copy removed: True` |
| `python -I -B s1_Q_exact.py` | byte-identical to `s1_Q_exact_output.txt` (checked with `cmp`: identical) |
| `python -I -B s5_p0_sector.py` | byte-identical to `s5_p0_sector_output.txt` (checked with `cmp`: identical) |

The saved outputs are `make_insert_r2_output.txt` and `apply_and_build_r2_output.txt`. s2, s3, s4 and s6 were not
re-run: no computation changed, and the gatekeeper re-ran them all in r1.

## Decisions Taken

- **S1-S3 adopted verbatim.** That includes all in-paragraph replacements.
- **F8 adopted.** I checked that the 071 closer, which is the preceding `\paragraph` unit, lists exactly the
  assumptions and the emergent-metric caveat that the r1 closer repeated. The shortened closer therefore loses no
  scope statement.
- **The optional Edit 2 wording is adopted** ("are linearised in their Landau sectors in the following paragraph").
  Reason: it states the sector restriction at the point where 071 hands over. This keeps the reader from inferring
  that the whole family was linearised. The p = 0 sector statement in the block is marked numerical and stays
  inside the block's own scope sentence ("in the sectors named").

## Milestone assessment

Routine. The result is unchanged from r1.

## Status-label recommendation

No change. D, F and N stay OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL. The critical path from ch17 and the appH
ledger is A, B, C, D1, E, F, G-derived and N.

## Author decision needed

None.

## Remaining open step

Unchanged from r1, including the ranked avenues: (1) non-null-leg connections (s4), (2) a pairing or Krein form,
(3) one loop, (4) nonlinear evolution, (5) non-constant connections, (6) other null-leg families, last.

## Special instructions for the gatekeeper

- Check that the diffs in the table are the only changes: compare `appH_insert_r1.tex` with `appH_insert_r2.tex`.
  `make_insert_r2.py` asserts that each replacement is applied once.
- Check that F8's "the assumptions listed in the preceding paragraph" resolves to the 071 closer (appH L1646), in
  the `\paragraph`-unit sense used elsewhere in the block.
- The 3(c) full scan is still owed, because Edit 2 changes a scope passage.
- Hashes: pre b98a3a34..., post a0efe483aea01e15fb88b95d351d0069f20b4bab9b23e5e09b573b0fddf4824d.
