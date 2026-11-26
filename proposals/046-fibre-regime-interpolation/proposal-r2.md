# Proposal 046-fibre-regime-interpolation, round 2

This round applies the corrections of `review-r1.md`. It contains no new research and no new claims. The derivations of
`proposal-r1.md` (section "Research and reasoning") are unchanged and are not repeated; where r1's summary wording
carried an error the gatekeeper found in the insert, the corrected wording below supersedes it.

## Result

For CP^{1,2} (finite fibre) x K at the IKKT content and the frozen leading symbol, the package computes the fibre
spectrum, the exact Duhamel interpolation between the two readings of the 045 paragraph, and the first-order
background-torsion corrections on fibre-constant modes.

Bounded no-go, within the hypotheses listed below: within these computations, no open range of the K scale gives a
single Einstein coefficient on the five traceless level-one polarisations with c_A = c_T.

The result does not reach further than that, in three respects:
- The range M ~ coth^2 tau, where the first-order torsion parameter is of order one, is not computed.
- Isolated tuned values of the K data are not excluded. They would lie where the fibre trace dominates, and would need
  two independent forms to vanish and the cone to match.
- Nothing is derived for a critical-path step. Problems B and F stay OPEN and PROGRAMME-CONDITIONAL.

Corrected regime statements (these supersede the matching wording in r1):
- The condition for a small second-harmonic weight is M * Sum_{J>=1}(2J+1)/mu_J << 1 and M << mu_2. It can hold for a
  given n at small enough M (beta_X = 0.065 at M = 0.01, n = 30). At fixed M it fails as n -> infinity, since the sum
  grows as 2 ln n.
- Where the torsion expansion holds (M >> coth^2 tau), beta_X is of order one and tends to one as n grows. The saved s4
  rows give 0.520 at n = 2 and 0.895-0.974 at n = 30 and 300. This is the fibre-trace reading as the leading reading,
  not beta_X close to one at every n.
- The L/c = 1 zeros have coth^2 tau/M* between 0.554 and 2.48. "Trace regime" in r1 described their beta_X only. These
  entries are not in a controlled torsion regime.

Comparison with Steinacker 2303.08012: mu_J = J(J+2) is the frozen-coefficient value of Box on the polynomials C.t^J.
It agrees with m_s^2 = 3s of eq. (7.5) at J = 1 and differs for J >= 2. The two are not reconciled here. The modes of
the cited work are sections of an equivariant bundle, so the difference may be one of operator or convention. This
package makes no claim that any statement of the cited work is wrong, and its conclusions hold for both spectra.

## Target and status

Quoted from the current `chapters/appH-microscopic-proofs.tex` (re-read this round):

- **Problem F**, `sec:status-F` (label L1363, ledger-label paragraph L1365, status text from L1366): "Status: OPEN.
  Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F
  OPEN and does not satisfy the matrix-derived criterion."
- **Problem B**, `sec:status-B` (label L42, status text L45-47): "Status: OPEN. Priority: CRITICAL PATH. Completion:
  PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is
  not derived."

Chapter 17 (`sec:ch17-done`, L691):
- Item 2, original target for B: Assumption EE is a lemma, with fixed-volume variations including the non-conformal
  tensor block, and no use of Assumption `ass:dictionary`.
- Item 6, original target for F: A, B, C and the sign/scheme dependence of G_eff computed from the specified operators;
  G_eff is not an input.
- Sub-target used here: G_T = G_A (normalisation paragraph, appH L174-179).

Critical-path set from `sec:ch17-done`: A, B, C, D1, E, F, G-derived, N. No discrepancy found in the passages read this
round.

Dependencies: F depends on D1, E and the class; B depends on A (replica/state) and F.

Classification: PROGRAMME-CONDITIONAL; nothing DERIVED.

## Source reading

**Digest + targeted reads.** This is not a full scan.

Digest status, which differs from the premise of the round's brief:
- `python scripts/make_digest.py --check` printed `DIGEST STALE (head changed)`. Digest head is 0059f49; HEAD is
  fe5723f.
- I did not regenerate it, because the script writes to `scratch/`, outside this proposal's write scope. I also did not
  run `--changed`, since that path rewrites the digest as well.
- A read-only comparison of the digest header with the tree gives `chapters-hash` 1a7f276e1d394df7 for both, 30 files,
  and no per-file hash difference, with `dirty-chapters: no`. The staleness comes from later commits that do not touch
  `chapters/`, so the digest content is byte-accurate for the current chapters.
- Read literally, CLAUDE.md protocol item 3(d) asks for a full scan when the digest is stale. I did not do one, because
  the condition is head-only, this round makes three wording replacements, and no definition, assumption, scope
  statement or status passage changes. The gatekeeper or orchestrator should overrule this if they read 3(d) strictly.
  r1 was a full scan of the 30-file manifest.

Read in full this round:
- `review-r1.md`, `proposal-r1.md`, `appH_insert.tex`, `s5_insert_mechanics.py`, `compile_check.py`, `scripts/make_digest.py`;
- appH L2394-2404 (the 045 paragraph body and the anchor), L172-179, and the B and F status lines;
- ch17 L689-738;
- `reports/ledger.md` L340-344;
- the saved `s4_window_scan.out.txt` window table.

Partly read: `reports/sme-scout-20261101.md`, by search for its 046 and normalisation lines only. It is left for later
packages and nothing from it is used here.

Not re-read: Steinacker 2303.08012. The statements about it are those of r1 and of review finding 4.

Unreadable files: none.

## Research and reasoning

No new research. How each finding of `review-r1.md` is addressed:

| # | Severity | Finding | Action |
|---|---|---|---|
| 1 | Major | "fails for every M in the Poisson limit" is too strong | Replacement (a) applied verbatim; r1's matching wording corrected in "Result" above |
| 2 | Major | "beta_X is close to one" overstates s4 (0.52 at n = 2) | Replacement (b) applied verbatim; values re-read from the saved s4 output, see "Result" |
| 3 | Minor-to-major | The uncomputed range M ~ coth^2 tau is not stated | Replacement (c) applied verbatim; also stated in "Result" and in the no-go class below |
| 4 | Minor, no change | J(J+2) against 3s | Insert unchanged. r1's word "disagreement" is replaced by the neutral description above, and the claim table is reworded |
| 5 | Minor, no change | beta_X table and the power-law tail | Insert unchanged. H11 and H13 stay as stated |
| 6 | Decision | 045 sentence: no flag, no edit | r1's optional in-place replacement is withdrawn. No edit to the 045 paragraph is proposed |
| 7 | Adequate after 3 | No-go scoping | The hypothesis fork is kept below, with the gatekeeper's ranking of open avenues |
| Note | - | Description of the 045 sentence | It now reads: incomplete labelled argument, corrected in the new paragraph (see "Proposed changes") |

Each replacement sentence was checked against saved output only; no calculation changed:
- (a): the sum Sum_{J<=n}(2J+1)/(J(J+2)) has terms approaching 2/J, which gives 2 ln n. This statement is already in the
  insert's "Which regime" paragraph.
- (b): `s4_window_scan.out.txt` gives beta_X = 0.520 (n = 2), 0.895 and 0.953 (n = 30), 0.928 and 0.974 (n = 300) for
  L/c = 1 and 10.
- (c): coth^2 tau/M* in the same rows spans 0.093 to 2.48, and the L/c = 0 rows span 4.16 to 13.1. The sub-unit
  entries alone do not cover M ~ coth^2 tau, and the first-order result is not claimed there.

### Hypotheses of the bounded no-go (unchanged from r1)

- H1-H9 of 045: product M x K with no mixed flux; IKKT content supplied; Poisson limit on M; one loop; frozen leading
  symbol at y^i = 0; hybrid fibre treatment; 044 cone values; orientation-even mixed term; formal eta.
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

**Ranked open avenues** (the gatekeeper's ranking from `review-r1.md`, adopted):
1. Exact Gaussian resummation of the background torsion together with the cone at the same order. This would decide the
   uncomputed range M ~ coth^2 tau and the tuned points.
2. Schur elimination of the inert and J = 2 amplitudes.
3. The S^2-M fibre-flux part with the cross term kept.
4. Equivariant K with mixed M-K flux, which relaxes the product background and could suppress the tail.
5. A J = 2 or hs-mode graviton.
6. Other presentations (M^{A5}, non-product).
7. Reconciling J(J+2) with 3s to fix the fibre-level normalisation. The findings do not depend on it.

## Claim classification

Claims 4, 11 and 14 are reworded, and 14b is split out to state the uncomputed range. The others are as in r1.

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
| 15 | M* ranges and beta_X values | numerical, model, base (5,3); L/c is a free parameter |
| 15b | Tuned isolated K data could give a single coefficient on the five | conjecture, not excluded; needs the L1 coefficient to vanish and a cone match (uncomputed) |
| 16 | S^2-M per-level weight ~ J^2/mu_J | conjecture (power counting) |
| 17 | No G_eff value, no closure | unresolved |

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`

**Candidate text.** `proposals/046-fibre-regime-interpolation/appH_insert.tex` is the authoritative copy: 10874 bytes,
ASCII, LF, 0 CR, 0 TAB, sha256 `6294d41602769e13180ce74d961899082dfd6a55d2c1506e58ba9301ba9784b2`. Git warns that it may
convert this file to CRLF on checkout, so the hash and the CR count apply to the LF form. The r1 file is 10683 bytes,
sha256 `3059afeb673b66e284bdc1c8a4bcbb19be67e96580fe920d2eec724f87d1926a`. The two differ only in replacements (a), (b)
and (c), on lines 8 and 12 of the insert.

**Target location and anchor.** In Appendix H, between the 045 paragraph and Problem G:
- Anchor: the line `\section{Problem G: HBEV}`, at L2404 of the committed file, exactly 1 occurrence.
- Preceding text: L2402 is the 045 closing paragraph, ending "...or bear on Assumption~\ref{ass:lorentzian}.
  Problems~B and~F remain open and PROGRAMME-CONDITIONAL."; L2403 is blank.
- Insertion: immediately before L2404, as one block, with one blank line between its last line and the anchor. Nothing
  is replaced or removed. L2402 and the 045 paragraph stay as they are. The integrator converts the block to CRLF.

**Replacements applied**, verbatim from `review-r1.md` (each old string occurred exactly once):

(a) In "Which regime":
```latex
which, at fixed \(M\), fails as \(n\to\infty\), since the sum grows as \(2\ln n\).
```
replaces `which fails for every \(M\) in the Poisson limit.`

(b) In "Consequence":
```latex
the weight \(\beta_X\) is of order one (it tends to one as \(n\) grows) and the fibre trace of the preceding paragraph is the leading reading.
```
replaces `the weight \(\beta_X\) is close to one and the fibre trace of the preceding paragraph applies.`

(c) In the last sentence of "Consequence":
```latex
Within these computations no open range of the scale of \(K\) gives a single Einstein coefficient on the five traceless polarisations with \(c_A=c_T\); the range \(M\sim\coth^2\tau\), where the first-order torsion parameter is of order one, is not computed, and isolated values
```
replaces `Within these computations no open range of the scale of \(K\) gives a single Einstein coefficient on the five traceless polarisations with \(c_A=c_T\); isolated values`

**045 paragraph: no edit.** r1's optional in-place replacement is withdrawn. The merged sentence "The full trace approaches
them when the fibre gaps exceed the scale of \(K\), ... this is an argument and is not computed." (appH L2400, one
occurrence) is an incomplete labelled argument, corrected in the new paragraph. It is not a false claim and no
PRIOR-CLAIM-ERROR flag is raised. The insert's sentence "The argument of the preceding paragraph ... is therefore
incomplete: ..." depends on that sentence staying in place.

**Stale passages.** None. The review's stale-statement check holds: 045 lists the interpolation and the fibre spectrum as
uncomputed and the insert supplements it, and 044's "first term has no two-derivative part" stays scoped to the
four-coordinate class.

**BibTeX.** None new.

## Verification scripts

All are in `proposals/046-fibre-regime-interpolation/`.

**Run this round:**

`apply_r2_replacements.py` (new; output `apply_r2_replacements.out.txt`, shown without its word-span count line). It
requires each old string exactly once and stops otherwise.
```
before: 10683 bytes, sha256 3059afeb673b66e284bdc1c8a4bcbb19be67e96580fe920d2eec724f87d1926a
(a) old occurrences 1 -> replaced; length change +33
(b) old occurrences 1 -> replaced; length change +48
(c) old occurrences 1 -> replaced; length change +110
after: 10874 bytes, sha256 6294d41602769e13180ce74d961899082dfd6a55d2c1506e58ba9301ba9784b2
lines changed: [8, 12] of 15
```
The script is single-use: on a re-run its first assertion stops it without writing, because the old strings are gone.

`s5_insert_mechanics.py`, against the committed Appendix H (shown without its macro-list line):
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

`compile_check.py`, a scratch build outside the repository of the current tree, without and with the corrected insert:
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

**Not re-run this round:** `s1_fibre_spectrum.py`, `s2_duhamel_interpolation.py`, `s3_background_torsion.py`,
`s4_window_scan.py`. No computation changed. The gatekeeper re-ran them at r1. Their saved outputs stand and were not
modified; only the s4 window table was re-read.

## Decisions Taken

r1's decisions 1, 2, 3 and 5 stand. Changes this round:

1. **045 sentence (r1 decision 4, narrowed).** The correction stays in the new paragraph, and the optional in-place
   replacement is withdrawn, following review finding 6. Alternative rejected: the in-place edit, which would leave the
   insert's correction pointing at text that no longer exists.
2. **Prior-claim wording.** "Soft PRIOR-CLAIM-ERROR" is replaced by "incomplete labelled argument, corrected in the new
   paragraph", as the review's note requires.
3. **Wording of the Steinacker comparison.** "Disagreement" is dropped from the proposal text in favour of a neutral
   comparison, which the review's finding 4 supports. The insert's own phrasing is accurate per that finding and is
   unchanged.
4. **Avenue ranking.** The gatekeeper's ranked list is adopted. r1's item on the trace polarisation stays in "Remaining
   open step".
5. **Stale digest.** Not regenerated, for the write-scope reason in "Source reading"; the condition is reported instead.
6. **Rounding at "4.2".** Left unedited and flagged (see "Special instructions"), because this round is limited to
   (a), (b) and (c).

## Milestone assessment

Routine; no milestone. This agrees with the review: M2 is not met, since this is a bounded no-go that leaves the tuned
points, the intermediate range and several avenues open. M3 is not met, since the 045 sentence is an incomplete labelled
argument rather than a false claim. M1, M4 and M5 do not apply. Not a breakthrough.

## Status-label recommendation

None. Problems B and F remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. The critical-path set from `sec:ch17-done` is A,
B, C, D1, E, F, G-derived, N. No status, priority or completion label is changed by this package.

## Author decision needed

None.

## Remaining open step

For a single matrix-derived Einstein coefficient with G_A = G_T in a rank-6 class:
1. Resum the background torsion, or find the leading-order structure at M ~ coth^2 tau, together with the cone at the
   same order.
2. Eliminate the inert and J = 2 amplitudes.
3. Compute the S^2-M fibre-flux part.
4. Alternatively, find a background (equivariant K, mixed flux) in which the fibre-level tail and the background torsion
   are both suppressed relative to the K scale.
5. Fix the trace polarisation, K, the sign of W_R and the replica (Problem A), with derived signature (Problem E).

Closing Problem F or B would need all of this and more; see items 2 and 6 of `sec:ch17-done`.

## Special instructions for the gatekeeper

**Compare:** `appH_insert.tex` against the r1 version in git (commit 22d8d45). Only the three accepted replacements should
differ.

**One residual I found and did not edit.** Replacement (c)'s sentence is not affected, but the "Consequence" paragraph says
`\coth^2\tau/M^*\ge4.2` for L/c = 0. The saved s4 output has a minimum of 4.16 (n = 2, M* = 0.668), so 4.2 is that value
rounded up and the inequality is not strictly true as printed. The conclusion does not change, since the parameter is
still well above one. The round's instructions limit the insert to (a), (b) and (c), so I left it. Please rule on whether
it needs a fourth verbatim fix (for example `\ge4.1`), or stands as accepted. Without your instruction it stays as is.

**Digest and scan.** The digest is formally stale (head-only; see "Source reading"), and I did not perform a full scan.
Please rule if you read protocol item 3(d) strictly.

**Do not assert:**
- any window or K-tuned point as an Einstein result;
- anything about M ~ coth^2 tau beyond "not computed";
- that 3J or any statement of the cited work is wrong;
- that S^2-M is computed;
- that the (3/2) coth^2 tau double eigenvalue is helicity two (not identified);
- any closure.
