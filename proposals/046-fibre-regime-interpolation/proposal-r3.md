# Proposal 046-fibre-regime-interpolation, round 3

This round applies `review-r2.md`: replacement (d) to the insert, finding 2 to the proposal record, and finding 3 by a
refining script. It contains no new research and no new claims. The derivations of `proposal-r1.md` ("Research and
reasoning") are unchanged and are not repeated. r2's text stands except where this round says it is superseded.

## Result

Unchanged in substance from r2. For CP^{1,2} (finite fibre) x K at the IKKT content and the frozen leading symbol, the
package computes the fibre spectrum, the exact Duhamel interpolation between the two readings of the 045 paragraph, and the
first-order background-torsion corrections on fibre-constant modes.

Bounded no-go, within the hypotheses listed below: within these computations, no open range of the K scale gives a single
Einstein coefficient on the five traceless level-one polarisations with c_A = c_T.

The result does not reach further than that, in three respects:
- The range M ~ coth^2 tau, where the first-order torsion parameter is of order one, is not computed.
- Isolated tuned values of the K data are not excluded. They would lie where the fibre trace dominates, and would need two
  independent forms to vanish and the cone to match.
- Nothing is derived for a critical-path step. Problems B and F stay OPEN and PROGRAMME-CONDITIONAL.

Regime statements, with the root values of `s6_root_refine.py`. These supersede the grid values in r2's "Result", its check
notes for replacements (b) and (c), and its "Special instructions":
- The condition for a small second-harmonic weight is M * Sum_{J>=1}(2J+1)/mu_J << 1 and M << mu_2. It can hold for a given
  n at small enough M (beta_X = 0.065 at M = 0.01, n = 30). At fixed M it fails as n -> infinity, since the sum grows as
  2 ln n.
- Where the torsion expansion holds (M >> coth^2 tau), beta_X is of order one and tends to one as n grows. This is the
  fibre-trace reading as the leading reading, not beta_X close to one at every n. The row-by-row evidence is in the table
  below. r2's list "0.895-0.974 at n = 30 and 300" is withdrawn, because it included the zeros at L/c = 1, which have
  coth^2 tau/M* of 1.79 and 2.46 and do not satisfy M >> coth^2 tau.
- The L/c = 1 zeros have coth^2 tau/M* between 0.546 and 2.46. The L/c = 1 and 10 zeros together span 0.090 to 2.46, and the
  L/c = 0 zeros span 4.13 to 12.66. r2's figures (0.554 to 2.48, 0.093 to 2.48, 4.16 to 13.1) were left grid endpoints from
  s4. The zeros with parameter near or above one are not in a controlled torsion regime.

Zeros of the non-Einstein coefficient at the nine s4 rows, base point (5,3), roots from `s6_root_refine.out.txt`:

| n | L/c | M* | beta_X | coth^2 tau/M* | Reading against M >> coth^2 tau |
|---|---|---|---|---|---|
| 2 | 0 | 0.67236 | 0.39253 | 4.13137 | not satisfied |
| 2 | 1 | 5.08753 | 0.51999 | 0.54600 | parameter below one, not small |
| 2 | 10 | 30.76179 | 0.52001 | 0.09030 | satisfied |
| 30 | 0 | 0.29196 | 0.65703 | 9.51416 | not satisfied |
| 30 | 1 | 1.54965 | 0.89810 | 1.79252 | not satisfied |
| 30 | 10 | 5.17699 | 0.95436 | 0.53656 | parameter below one, not small |
| 300 | 0 | 0.21940 | 0.71846 | 12.66092 | not satisfied |
| 300 | 1 | 1.13007 | 0.92880 | 2.45806 | not satisfied |
| 300 | 10 | 3.62756 | 0.97425 | 0.76574 | parameter below one, not small |

The last column is a reading of the size of the parameter, not a separate computed result. Of these nine zeros, only
n = 2, L/c = 10 has a parameter well below one. So the rows alone do not establish "tends to one as n grows" inside the
controlled range. That statement rests on claim 9 (beta_X -> 1 as n -> infinity at fixed M, H10 and H11), together with the
review's reading of the insert wording. The insert does not use the row list.

Comparison with Steinacker 2303.08012, unchanged from r2: mu_J = J(J+2) is the frozen-coefficient value of Box on the
polynomials C.t^J. It agrees with m_s^2 = 3s of eq. (7.5) at J = 1 and differs for J >= 2. The two are not reconciled here.
The modes of the cited work are sections of an equivariant bundle, so the difference may be one of operator or convention.
This package makes no claim that any statement of the cited work is wrong, and its conclusions hold for both spectra.

## Target and status

Re-read this round from the current `chapters/appH-microscopic-proofs.tex`:

- **Problem F**, `sec:status-F` (label L1363, ledger-label paragraph L1365, status text L1366-1369): "Status: OPEN. Priority:
  CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does
  not satisfy the matrix-derived criterion." This reading covers the full sentence, which the review verified only in part.
- **Problem B**, `sec:status-B` (label L42, status text L44-46): "Status: OPEN. Priority: CRITICAL PATH. Completion:
  PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not
  derived."

Chapter 17 (`sec:ch17-done`, L691), unchanged from r2:
- Item 2, original target for B: Assumption EE is a lemma, with fixed-volume variations including the non-conformal tensor
  block, and no use of Assumption `ass:dictionary`.
- Item 6, original target for F: A, B, C and the sign/scheme dependence of G_eff computed from the specified operators;
  G_eff is not an input.
- Sub-target used here: G_T = G_A (normalisation paragraph, appH L174-179).

Critical-path set from `sec:ch17-done`, as read at r2 and confirmed by the review: A, B, C, D1, E, F, G-derived, N. This
round re-read only its first items (L700-716), which agree, and found no discrepancy.

Dependencies: F depends on D1, E and the class; B depends on A (replica/state) and F.

Classification: PROGRAMME-CONDITIONAL; nothing DERIVED.

## Source reading

**Digest + targeted reads.** This is not a full scan.

Digest status: `python scripts/make_digest.py --check` prints `DIGEST CURRENT`; tree-hash 339cd7f99f895f0d, chapters-hash
1a7f276e1d394df7, `dirty-chapters: no`. r2's stale-digest report no longer applies. No full scan is due for this round: no
definition, assumption, scope or status passage changes, and the review places the next gatekeeper scan at ordinal 45.

Read in full this round: `review-r2.md`, `proposal-r2.md`, `appH_insert.tex`, `s4_window_scan.py`, the saved
`s4_window_scan.out.txt`, `s5_insert_mechanics.py`, `compile_check.py`, `apply_r2_replacements.py`.

Targeted reads: appH L43-46 and L1365-1369 (status labels); the appH anchor line by search; ch17 L700-716; `reports/ledger.md`
L343-344 (the 046 entry).

Not re-read: the 045 paragraph body (its occurrence count is checked by s5), Steinacker 2303.08012, the SME scout.

Unreadable files: none.

## Research and reasoning

No new research. How each finding of `review-r2.md` is addressed:

| # | Severity | Finding | Action |
|---|---|---|---|
| 1 | Minor | Grid values make `\ge4.2`, `\le30`, `\le0.67` and "between 0.52 and 0.97" false as printed | Replacement (d) applied verbatim; bytes and hash match the review (see below) |
| 2 | Minor, record only | r2 quotes grid values and an over-wide row list | Root values and the corrected row list in "Result" above; r2's statements listed there are superseded; insert unaffected |
| 3 | Note | s4 does not produce the corrected numbers | `s6_root_refine.py` added; it reproduces the review's table (see below) |

Earlier findings: the review reports findings 1-7 of `review-r1.md` as closed or as no-change items. This round leaves their
text untouched.

### Corrections to r2's record, one by one

| r2 location | r2 text | Correct value |
|---|---|---|
| "Result", second regime bullet | 0.520 at n = 2 and 0.895-0.974 at n = 30 and 300 | withdrawn; see the table in "Result" |
| "Result", third regime bullet | L/c = 1: 0.554 to 2.48 | 0.546 to 2.46 |
| Check note (b) | beta_X 0.520 (n = 2), 0.895 and 0.953 (n = 30), 0.928 and 0.974 (n = 300) | 0.520, 0.898 and 0.954, 0.929 and 0.974 |
| Check note (c) | same rows 0.093 to 2.48; L/c = 0 rows 4.16 to 13.1 | 0.090 to 2.46; 4.13 to 12.66 |
| "Special instructions", residual | minimum 4.16 at n = 2, M* = 0.668 | root minimum 4.131 at M* = 0.6724; this was also a grid value, and the question is settled by (d) |
| "Decisions Taken" 6 | 4.2 left unedited | closed by (d) |

The ledger's current 046 entry (L343-344) quotes none of these figures, so it has nothing to correct. A later ledger line for
046 should use the root values; `reports/` is outside this proposal's write scope.

### Root refinement (finding 3)

Equation from review-r2: f(M) = W_B(M) lambda_L + (1 + 24 L/c)/M^2 = 0, with W_B = W1 beta_X. This is s4's coefficient N(M), in
which -4 (L/c) lambda_P with lambda_P = -6 gives the 24 L/c. Inputs are taken from s4 and not retyped: `cJJ_closed` and `W_index`
are compiled from the source of `s4_window_scan.py` with `ast`, since importing s4 would rerun it and rewrite its output, and
lambda_L = -1.956233 is read from the saved s4 output. As a check, the extracted `W_index` returns s4's check lines (M = 0.1:
W1 15.787537, beta_X 0.400031; M = 3: 5.290595, 0.935904).

The script ran brentq in s4's grid bracket for every integer 2 <= n <= 300, a superset of the review's sample (n = 2..60 and every
5th n up to 300). On the review's sample it agrees with every entry of the review's table at the printed digits:

| L/c | M* range | beta_X range | coth^2 tau/M* range |
|---|---|---|---|
| 0 | 0.2194 (n=300) to 0.6724 (n=2) | 0.3925 to 0.7185 | 4.131 to 12.66 |
| 1 | 1.1301 to 5.0875 | 0.51999 to 0.9288 | 0.546 to 2.458 |
| 10 | 3.6276 to 30.762 | 0.52001 to 0.97425 | 0.0903 to 0.7657 |

Over every integer 2 <= n <= 300 the ranges are the same:
- The insert's printed inequalities (0.21 <= M* <= 0.68, coth^2/M* >= 4.1, 1.1 <= M* <= 31, 0.51 <= beta_X <= 0.98) all hold.
- The four pre-(d) inequalities all fail.
- M* decreases in n at each L/c.
- Each n and L/c has exactly one sign change on s4's grid.

Limit of that check: the "one value M*" claim is tested only by sign changes on a 241-point grid, so it is a grid statement and
not a proof. All these numbers remain single-scale model values at one base point and one wave vector.

### Hypotheses of the bounded no-go (unchanged from r1)

- H1-H9 of 045: product M x K with no mixed flux; IKKT content supplied; Poisson limit on M; one loop; frozen leading symbol at
  y^i = 0; hybrid fibre treatment; 044 cone values; orientation-even mixed term; formal eta.
- Inert amplitudes set to zero, not eliminated.
- H10: fibre levels from -Box at zero base momentum, with the J-diagonal cross term dropped.
- H11: commutative Clebsch-Gordan coefficients with truncation at J <= n.
- H12: torsion correction for J = 0 loop modes only, first order in Tbar^2.
- H13: single-scale K model tau^K = F^2 s^2 e^{-sM} for the quoted numbers.
- Level-one graviton; leading symbol.

### Fork: relaxations (unchanged from r1)

| Hypothesis | Relaxation | Explored here? / outcome |
|---|---|---|
| H12 first-order torsion | resum Tbar exactly (Gaussian k-integral of tr e^{-sZ}, Euclidean section) | not done; would decide the sign of the non-Einstein coefficient at small M |
| H10 cross term dropped | include the J-diagonal (q.L, J) cross term in the level weights | closed form obtained (s1); weights not recomputed; expected O(1) change and still power-law |
| inert = 0 | Schur-eliminate the inert amplitudes with the tree Maxwell forms | not done |
| fibre-flux first term | compute S^2-M on J >= 1 levels | power counting only |
| product background / no mixed flux | K flux varying along the fibre (equivariant K) so that fibre and K fluxes mix | not explored |
| level-one graviton | graviton from J = 2 or mixed hs modes | not explored |
| cone values | cone corrections at order s Tbar^2 | not computed |
| presentation | five-matrix presentation M^{A5} | not explored |

**Ranked open avenues** (the gatekeeper's ranking, unchanged in `review-r2.md`):
1. Exact Gaussian resummation of the background torsion, with the cone at the same order; this decides M ~ coth^2 tau and the
   tuned points.
2. Schur elimination of the inert and J = 2 amplitudes.
3. The S^2-M fibre-flux part with the cross term kept.
4. Equivariant K with mixed M-K flux, which could suppress the tail.
5. A J = 2 or hs-mode graviton.
6. Other presentations (M^{A5}, non-product).
7. Reconciling J(J+2) with 3s; the findings do not depend on it.

## Claim classification

Only claim 15 changes wording, and 15a is added to record the refinement. The others are as in r2.

| # | Claim | Class |
|---|---|---|
| 1 | Box t = -3t and Box(tt) = -6tt + 2 eta MM | established (exact polynomial identity) |
| 2 | eta MM = c_theta eta + yy - tt on the orbit | established numerically (40 points, 1e-15) |
| 3 | mu_J = J(J+2) on fibre harmonics, frozen coefficients | established (from 1 and 2; numerical check at 2 base points) |
| 4 | mu_J equals 3J at J = 1 and differs from it for J >= 2; possibly an operator or convention difference; no statement of the cited work is claimed wrong | established as a comparison; reason unresolved |
| 5 | Cross term J-diagonal, closed-form singular values | derivation plus Monte Carlo check (4%) |
| 6 | Duhamel weights; scalar kernel F1, F2; calibration 1/4 | established (symbolic, exact) |
| 7 | Interpolation formula; L1 + L2 = SC2 - SC1; L2 = 0 on the five | established at the frozen symbol under H10-H11 (exact at 7 cases) |
| 8 | Mixed gap on the five = -W_X^(2)(lambda_i + 2) | conditional (044 cone values; cone diagonal) |
| 9 | Power-law level weights; beta_X -> 1 as n -> infinity at fixed M | established given tau^K ~ tau_2 s^2 at small s (H10, H11) |
| 10 | beta_X numbers; half-spread 2.42 beta_X | numerical, single-scale model (H13) |
| 11 | The 045 regime sentence is an incomplete labelled argument, corrected in the new paragraph: the condition is M Sum (2J+1)/mu_J << 1, which at fixed M fails as n -> infinity | established within H10-H11 |
| 12 | Q1^D = m^4 IX1 | established at the frozen symbol (10 points, machine precision) |
| 13 | Span structure; P2hat = -6 Q2hat mod EH; lambda range; (3/2) coth^2 tau | numerical (residual < 1e-11 at 7 points); not proved |
| 14 | No open range of the K scale gives a single coefficient with c_A = c_T, within these computations | conditional (first-order torsion, J = 0, H1-H13) |
| 14b | The range M ~ coth^2 tau | unresolved (not computed) |
| 15 | M* ranges and beta_X values, now brentq roots | numerical, model, base (5,3); L/c is a free parameter |
| 15a | One sign change of the coefficient for each integer 2 <= n <= 300 and L/c = 0, 1, 10 | numerical, grid-level only (241 points); not proved |
| 15b | Tuned isolated K data could give a single coefficient on the five | conjecture, not excluded; needs the L1 coefficient to vanish and a cone match (uncomputed) |
| 16 | S^2-M per-level weight ~ J^2/mu_J | conjecture (power counting) |
| 17 | No G_eff value, no closure | unresolved |

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`

**Candidate text.** `proposals/046-fibre-regime-interpolation/appH_insert.tex` is the authoritative copy: 10874 bytes, ASCII, LF,
0 CR, 0 TAB, sha256 `81bb7f1674b176f3c675377154f60fbc79641dde13b39ece9c219786234c9c71`, as `review-r2.md` requires. Git warns
that it may convert this file to CRLF when it touches it, so the hash and the CR count apply to the LF form. The r2 file was
10874 bytes, sha256 `6294d41602769e13180ce74d961899082dfd6a55d2c1506e58ba9301ba9784b2`. The two differ only on line 12 of 15, in
five numbers of one clause.

**Target location and anchor.** Unchanged from r2. In Appendix H, between the 045 paragraph and Problem G:
- Anchor: the line `\section{Problem G: HBEV}`, at L2404 of the committed file, exactly 1 occurrence in appH and in no other
  chapter file.
- Preceding text: the 045 closing paragraph, ending "...or bear on Assumption~\ref{ass:lorentzian}. Problems~B and~F remain open
  and PROGRAMME-CONDITIONAL."
- Insertion: immediately before the anchor, as one block, with one blank line between its last line and the anchor. Nothing is
  replaced or removed. The integrator converts the block to CRLF.

**Replacement applied**, extracted by script from `review-r2.md` (the old string occurred exactly once):

(d) In "Consequence":
```latex
it lies at \(0.21\le M^*\le0.68\) with \(\coth^2\tau/M^*\ge4.1\) for \(L/c=0\), and at \(1.1\le M^*\le31\) with \(\beta_X\) between \(0.51\) and \(0.98\) for \(L/c=1\) and \(10\)
```
replaces `it lies at \(0.21\le M^*\le0.67\) with \(\coth^2\tau/M^*\ge4.2\) for \(L/c=0\), and at \(1.1\le M^*\le30\) with \(\beta_X\) between \(0.52\) and \(0.97\) for \(L/c=1\) and \(10\)`

Replacements (a), (b) and (c) of r2 stay in place. Labels verified by s5: `ass:lorentzian`, `ch:vierbein-emergence` and `sec:status-B`
each occur once; `Steinacker2023` has one bib entry; the insert adds no `\label`.

**045 paragraph: no edit.** The merged sentence stays in place, and the insert's correction depends on it (one occurrence, checked
by s5). It is an incomplete labelled argument, corrected in the new paragraph, not a false claim, and no PRIOR-CLAIM-ERROR flag is
raised.

**Stale passages.** None. **BibTeX.** None new.

## Verification scripts

All are in `proposals/046-fibre-regime-interpolation/`.

**New this round:**

`apply_r3_replacement.py` (output `apply_r3_replacement.out.txt`). It extracts (d) from `review-r2.md`, requires the old string
exactly once, and refuses to write unless the result has the review's size and hash:
```
before: 10874 bytes, sha256 6294d41602769e13180ce74d961899082dfd6a55d2c1506e58ba9301ba9784b2
(d) old occurrences 1 -> replaced; length change +0
after: 10874 bytes, sha256 81bb7f1674b176f3c675377154f60fbc79641dde13b39ece9c219786234c9c71
non-ASCII 0; CR 0; TAB 0
matches review-r2 expected bytes and hash: True
lines changed: [12] of 15
```
It is single-use: on a re-run its first assertion stops it without writing. A word-level `git diff` shows exactly the five number
changes: 0.67 to 0.68, 4.2 to 4.1, 30 to 31, 0.52 to 0.51, 0.97 to 0.98.

`s6_root_refine.py` (output `s6_root_refine.out.txt`; runs in about 30 s and writes only its own output). Results are quoted in
"Research and reasoning" and the table in "Result". Summary lines of the output:
```
review table reproduced at the printed digits: True
0.21 <= M* <= 0.68 (L/c = 0)                            True
coth^2/M* >= 4.1 (L/c = 0)                              True
1.1 <= M* <= 31 (L/c = 1, 10)                           True
0.51 <= beta_X <= 0.98 (L/c = 1, 10)                    True
exactly one sign change on the grid, all n and L/c      True
```
The same output's section (5) shows that all four pre-(d) inequalities are false for the roots.

**Re-run this round:**

`s5_insert_mechanics.py`, against the committed Appendix H (shown without its macro-list line; `s5_insert_mechanics.out.txt` is
unchanged by the re-run):
```
bytes 10874; non-ASCII 0; CR 0; TAB 0
brace balance 0; \( - \) 0; \[ - \] 0
\label in insert: 0; \paragraph count: 1
ref ass:lorentzian: label occurrences in chapters = 1
ref ch:vierbein-emergence: label occurrences in chapters = 1
ref sec:status-B: label occurrences in chapters = 1
cite Steinacker2023: bib entries = 1
anchor '\section{Problem G: HBEV}' occurrences in appH: 1
title fragment 'fibre spectrum, proper-time interpolation between the two readings' occurrences in appH: 0
process-language scan: []
line before anchor ends with: an}. Problems~B and~F remain open and PROGRAMME-CONDITIONAL.
045 sentence corrected by the insert, occurrences in appH: 1
```
A separate search of `chapters/` confirms the anchor at appH L2404 only.

`compile_check.py`, a scratch build outside the repository, without and with the corrected insert. The scratch copy was removed,
and `compile_check.out.txt` is unchanged by the re-run:
```
baseline (current working tree): CRLF preserved True; exit codes (pdflatex, bibtex, pdflatex, pdflatex) [0, 0, 0, 0]; 323 pages
   undefined refs: []
   undefined citations: []
   multiply defined labels: []
with insert: CRLF preserved True; exit codes (pdflatex, bibtex, pdflatex, pdflatex) [0, 0, 0, 0]; 325 pages
   undefined refs: []
   undefined citations: []
   multiply defined labels: []
scratch removed: True
```
This is `compile_check.py`'s own build. `scripts/build_check.py` was not run, since no chapter changes in this folder.

**Not re-run this round:** `s1_fibre_spectrum.py`, `s2_duhamel_interpolation.py`, `s3_background_torsion.py`, `s4_window_scan.py`. No
computation changed. The review reports re-running all four with identical output. `s6` reads the saved s4 output and s4's source
only.

## Decisions Taken

r2's decisions 1-4 stand. Changes this round:

1. **Rounding at "4.2" (r2 decision 6).** Closed by the gatekeeper's (d), which covers the other grid-derived bounds as well.
2. **Stale digest (r2 decision 5).** Closed: the digest is current.
3. **Using s4's `W_index`.** Compiled from s4's source with `ast`. Alternatives rejected: importing s4, which reruns it and rewrites
   its output, and recoding the function, which would no longer be s4's own.
4. **Scan range in s6.** Every integer 2 <= n <= 300, because that is the range the insert states; the review's 107-value sample is
   reported as its own section so that the comparison with its table is direct.
5. **Row list (finding 2).** Replaced by the full nine-row table with a reading column, rather than a shortened list, so the record
   does not imply a stronger evidential basis for "tends to one" than the rows give.

## Milestone assessment

Routine; no milestone. This agrees with the review: M2 and M3 are not met, and M1, M4 and M5 do not apply. Not a breakthrough.

## Status-label recommendation

None. Problems B and F remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. The critical-path set from `sec:ch17-done` is A, B, C, D1, E,
F, G-derived, N. No status, priority or completion label is changed by this package.

## Author decision needed

None.

## Remaining open step

Unchanged from r2. For a single matrix-derived Einstein coefficient with G_A = G_T in a rank-6 class:
1. Resum the background torsion, or find the leading-order structure at M ~ coth^2 tau, together with the cone at the same order.
2. Eliminate the inert and J = 2 amplitudes.
3. Compute the S^2-M fibre-flux part.
4. Alternatively, find a background (equivariant K, mixed flux) in which the fibre-level tail and the background torsion are both
   suppressed relative to the K scale.
5. Fix the trace polarisation, K, the sign of W_R and the replica (Problem A), with derived signature (Problem E).

Closing Problem F or B would need all of this and more; see items 2 and 6 of `sec:ch17-done`.

## Special instructions for the gatekeeper

**Compare:** the insert's sha256 against the value in `review-r2.md`. They match, so by the review's own disposition no further review
round is needed for the insert.

**Please note, not a change request:** the "Result" table shows that only one of the nine rows (n = 2, L/c = 10) has a parameter well
below one, while the insert's "(it tends to one as \(n\) grows)" concerns M >> coth^2 tau. The insert wording is as the gatekeeper
supplied it, and I have not altered it. Its support is claim 9, not these rows.

**Do not assert:**
- any window or K-tuned point as an Einstein result;
- anything about M ~ coth^2 tau beyond "not computed";
- that 3J or any statement of the cited work is wrong;
- that S^2-M is computed;
- that the (3/2) coth^2 tau double eigenvalue is helicity two (not identified);
- that the single sign change is proved rather than grid-tested;
- any closure.
