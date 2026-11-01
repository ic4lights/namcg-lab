VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
Replacements (a), (b) and (c) were applied verbatim and the 045 edit is withdrawn. One clause of numbers still needs a verbatim fix, because s4 reports left grid endpoints rather than roots. That makes `\ge4.2` and `\le30` false as printed; this review accepts the insert only with fix (d) below.

**Accepted text:** r2 `appH_insert.tex` with exactly replacement (d) and nothing else: 10874 bytes, ASCII, LF, sha256 `81bb7f1674b176f3c675377154f60fbc79641dde13b39ece9c219786234c9c71`.

If those bytes match, I need no further review round and no new research. Apart from applying (d), the integrator should convert the block to CRLF and insert it as specified in the proposal.

## Source reading
- **Method:** digest + targeted reads, not a full scan.
- **Digest:** `make_digest --check` prints DIGEST CURRENT; head fe5723f, tree-hash 339cd7f99f895f0d, dirty-chapters: no. `git status` shows `chapters/` and `bib/` clean.
- **Scan requirement:** ordinal 44, and no definition, assumption, scope or status passage changes, so no full scan is due. The researcher's question about reading 3(d) strictly is moot, because the digest was regenerated and is current. The full scan falls due at 45.
- **Read in full:** proposal-r2.md, review-r1.md, the insert diff, s4_window_scan.py, the header of compile_check.py.
- **Read as truncated excerpts (line-length cut):** appH L42-47, L172-179, L1363-1367, L2398-2405 (the 045 paragraph and anchor).
- **Also read:** ch17 `sec:ch17-done` L689-738; ledger L335-350.
- **Not re-read:** Steinacker 2303.08012 (read at r1, nothing changed). The two stale-statement passages (045's uncomputed list, 044's scoped sentence) rest on r1 plus the excerpt above.
- **Unreadable files:** none.

## Claim under review
- **Claim:** unchanged from r1. For CP^{1,2} x K at IKKT content and frozen leading symbol, the package gives the fibre spectrum, the Duhamel interpolation and the first-order background-torsion corrections, and a bounded no-go. Within these computations, no open range of the K scale gives a single Einstein coefficient with c_A = c_T on the five traceless polarisations.
- **Original targets:** ch17 items 2 and 6; sub-target G_T = G_A.
- **Critical-path set (`sec:ch17-done`):** A, B, C, D1, E, F, G-derived, N. No discrepancy found.
- **Problem F ledger label (verbatim):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." The label text was verified only in part this round (excerpt cut after "Reduced-scope result: treating"); the rest comes from r1 and the unchanged chapter hash.
- **Problem B ledger label (verbatim):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."

## Checks performed
All runs used copies in my scratchpad, because the scripts overwrite their `.out.txt` next to themselves. `git status` is unchanged afterwards and I wrote nothing to the repo.

**Replacements, byte check (my own script)**
- I took the HEAD blob of the insert (10683 bytes, sha `3059afeb...`) and extracted the three pairs programmatically from review-r1.md.
- Each old string occurred once in HEAD and 0 times in the working file; each new string occurs once.
- r1 + (a,b,c) is byte-identical to the working insert (10874 bytes, sha `6294d416...`, 0 CR, 0 TAB, 0 non-ASCII). Nothing else changed.

**045 edit withdrawn**
- `chapters/` is unmodified.
- The merged sentence "The full trace approaches them when the fibre gaps exceed the scale of" occurs on one line of appH, so the insert's correction still has its target.

**Re-runs**
- s1, s2, s3 and s4 all exit 0 with empty stderr, and each `.out.txt` is identical to the saved one.
- compile_check.py, run on the insert with (d) applied, against a scratch copy of the tree: baseline 323 pages, with insert 325 pages; no undefined references or citations, no duplicate labels, CRLF preserved, exit codes 0.

**Mechanics (my own check)**
- Anchor `\section{Problem G: HBEV}` occurs once; braces and `\( \)` balance; no `\label`; one `\paragraph`.
- Refs ass:lorentzian, ch:vierbein-emergence and sec:status-B each have one label; `Steinacker2023` has one bib entry.
- The process-word hit "round" is only from "background".
- appH is fully CRLF (0 bare LF).

**Earlier claims and changed wording**
- (a): my values of the sum are 5.84, 10.33, 14.92 at n = 30, 300, 3000, with successive increments near 2 ln 10 = 4.6. The sum grows as 2 ln n plus a constant, so "fails at fixed M as n -> infinity" is correct. The J = 1 term equals 1, so the bound in Consequence holds.
- (b): beta_X at n = 2 is 0.5236, 0.5165, 0.5145, tending to 0.51429 as M grows (exact 36/70 from the truncated c(J,J') weights). At n = 30 and 300 it is 0.90-0.97 at the zeros. "Of order one, tends to one as n grows" is correct.
- (c): the first-order parameter is coth^2 tau / M. The L/c = 1 zeros have this parameter between 0.55 and 2.46, so stating the range as uncomputed is necessary and accurate.
- lambda range: LX coefficients run from -3.30292 to -0.32387, so `-3.31\le\lambda\le-0.32` is true as printed. P2 coefficient is -6 at all seven points; residuals in the insert's span test are at most 1.3e-11 (the larger residuals in the s4 output are for L1, which the insert says is outside that span).

**Ruling check on "4.2" (my own check)**
- s4's reported M* is `grid[k]`, the left endpoint of a bracket with ratio 10^(1/40) = 1.059, not a root.
- I solved W_B(M) lambda_L + (1 + 24 L/c)/M^2 = 0 by brentq, with lambda_L = -1.956233 and W_B as in s4's `W_index`, independently recoded.
- I scanned n = 2..60 and every 5th n up to 300; this also supports the insert's claim for 2 <= n <= 300, since s4 itself only ran n = 2, 30, 300.
- Each sampled n and L/c has exactly one zero, and M* decreases monotonically in n.

| L/c | M* range | beta_X range | coth^2 tau / M* range |
|---|---|---|---|
| 0 | 0.2194 (n=300) to 0.6724 (n=2) | 0.3925 to 0.7185 | 4.131 to 12.66 |
| 1 | 1.1301 to 5.0875 | 0.51999 to 0.9288 | 0.546 to 2.458 |
| 10 | 3.6276 to 30.762 | 0.52001 to 0.97425 | 0.0903 to 0.7657 |

**Not verified**
- Clebsch-Gordan closed forms and Isserlis moments beyond their script checks, and the torsion code was not independently rewritten (as at r1).
- These numbers remain single-scale model values at one base point.

## Findings

1. **Minor (numbers only, conclusion unaffected).** Insert, "Consequence", the M* clause.
   - **Finding:** the researcher's flag is correct but understates the problem. `\coth^2\tau/M^*\ge4.2` is false: the true minimum is 4.13. Even the researcher's 4.16 is a grid artefact.
   - **Same origin:** `M^*\le30` is false (30.76), `M^*\le0.67` is false by 0.002 (0.6724), and "between 0.52 and 0.97" excludes 0.51999 and 0.97425.
   - **Correction of my r1:** I reproduced the s4 output and accepted these numbers without noticing that s4 prints grid endpoints. This does not reach any merged text.
   - **Required action:** apply (d) below. I chose the bounds so that each printed inequality holds literally. `0.21` and `1.1` stay because they are true.

2. **Minor, proposal record only, no insert change.** proposal-r2.md, "Result" and the check notes for replacement (c), quote the grid values (0.554 to 2.48, 0.093 to 2.48, 4.16 to 13.1). The roots are 0.546 to 2.46, 0.090 to 2.46 and 4.13 to 12.66. The ledger entry should use the roots, or say the proposal figures are grid values. Its row list "0.895-0.974 at n = 30 and 300" also includes zeros with coth^2/M* of 1.8-2.5, which do not satisfy M >> coth^2 tau. The insert does not use that list.

3. **Reproducibility note, no change to the insert.** s4 does not produce the corrected numbers. They follow from the root equation above with s4's own `W_index`, at the values in the table. The orchestrator may add a small refining script to the proposal folder, but this is not a condition of acceptance, because the equation and table recorded here reproduce them.

**Earlier findings re-verified**
- Findings 1-3 of r1 are closed by (a), (b), (c), as verified above.
- Findings 4 and 5 remain no-change items. The insert's text on them is untouched, and the proposal's neutral rewording of the 3s comparison is accurate.
- Finding 6 is closed: no 045 edit, no PRIOR-CLAIM-ERROR, and the proposal now says "incomplete labelled argument".
- Finding 7 is adequate, with the uncomputed range now stated.

## Scope of what is established
Unchanged from r1, apart from the corrected numbers.
- **Exact:** the spectrum mu_J = J(J+2) for the frozen-coefficient loop operator; the Duhamel weights; the calibration 1/4; L1 + L2 = SC2 - SC1 at seven points; the power-law tail.
- **Numerical or model-conditional:** the beta_X table and the half-spread 2.42 beta_X (H13, n = 30); the span structure and lambda range; the M* ranges (free L/c, first-order torsion, J = 0 only, base point (5,3)).
- **Open:**
  - the range M ~ coth^2 tau;
  - tuned points;
  - the S^2-M part;
  - the cone at torsion order;
  - the inert amplitudes;
  - the trace polarisation;
  - K itself;
  - G_eff.
- **Status:** nothing is DERIVED. Problems B and F stay OPEN and PROGRAMME-CONDITIONAL.
- **No-go class:** rank-6 CP^{1,2} x K, level-one graviton, IKKT content supplied, frozen leading symbol, inert amplitudes zero, product background without mixed flux, cross term dropped, first-order torsion on J = 0 modes. It does not close any direction outside this class.
- **Open avenues, ranked (unchanged):**
  1. Exact Gaussian resummation of the background torsion, with the cone at the same order; this decides M ~ coth^2 tau and the tuned points.
  2. Schur elimination of the inert and J = 2 amplitudes.
  3. The S^2-M fibre-flux part with the cross term kept.
  4. Equivariant K with mixed M-K flux, which could suppress the tail.
  5. A J = 2 or hs-mode graviton.
  6. Other presentations (M^{A5}, non-product).
  7. Reconciling J(J+2) with 3s; the findings do not depend on it.

**Milestone:** M2 and M3 are not met, and M1, M4 and M5 do not apply. Not a breakthrough. No label change is proposed.

## Recommended disposition
Apply (d), confirm the sha256 above, then integrate before `\section{Problem G: HBEV}` as specified, converted to CRLF, with no edit to the 045 paragraph. No further review round is needed if the bytes match.

## Corrected snippet (wording only, no new physics, no extra assumptions)

(d) In "Consequence", replace (exactly one occurrence)
`it lies at \(0.21\le M^*\le0.67\) with \(\coth^2\tau/M^*\ge4.2\) for \(L/c=0\), and at \(1.1\le M^*\le30\) with \(\beta_X\) between \(0.52\) and \(0.97\) for \(L/c=1\) and \(10\)`
with
`it lies at \(0.21\le M^*\le0.68\) with \(\coth^2\tau/M^*\ge4.1\) for \(L/c=0\), and at \(1.1\le M^*\le31\) with \(\beta_X\) between \(0.51\) and \(0.98\) for \(L/c=1\) and \(10\)`

File: C:\Users\redgi\Projects\namcg-lab\proposals\046-fibre-regime-interpolation\appH_insert.tex
