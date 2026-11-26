VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
The insert is exactly r2 plus replacement (d), every printed number holds, and "(it tends to one as \(n\) grows)" is correct as written. No byte needs to change.

**Accepted text:** `proposals/046-fibre-regime-interpolation/appH_insert.tex`, 10874 bytes, ASCII, LF, sha256 `81bb7f1674b176f3c675377154f60fbc79641dde13b39ece9c219786234c9c71`. Insert it as one block immediately before `\section{Problem G: HBEV}`, converted to CRLF, with one blank line before the anchor and no edit to the 045 paragraph.

## Source reading
- **Method:** digest + targeted reads, not a full scan.
- **Digest:** `make_digest --check` prints DIGEST CURRENT; head 0ca0efe, tree-hash 339cd7f99f895f0d, chapters-hash 1a7f276e1d394df7, dirty-chapters: no. `git status` shows `chapters/` and `bib/` clean.
- **Scan requirement:** ordinal 44, and no definition, assumption, scope or status passage changes, so no full scan is due. It falls due at 45.
- **Read in full:** proposal-r3.md, review-r1.md, review-r2.md, appH_insert.tex, the insert diff, s6_root_refine.py, s4 L1-110 (including `W_index` and `cJJ_closed`), compile_check.py L1-40.
- **Targeted reads:**
  - appH L42-47 and L1363-1369 (labels);
  - appH L2402-2404 (line-cut excerpt) and the line before the anchor;
  - ch17 `sec:ch17-done` L689-738;
  - ledger L338-350.
- **Not re-read:** the full body of the 045 paragraph (only the corrected sentence's occurrence count and its closing line) and Steinacker 2303.08012. Nothing relying on them changed.
- **Unreadable files:** none.
- **Process note:** my first batch of reads ran in parallel, against the sequential rule in `CLAUDE.md`. They were read-only and later calls were serial.

## Claim under review
- **Claim:** unchanged in substance. For CP^{1,2} x K at IKKT content and frozen leading symbol, the package gives the fibre spectrum, the Duhamel interpolation, first-order background-torsion corrections, and a bounded no-go. Within these computations, no open range of the K scale gives a single Einstein coefficient with c_A = c_T on the five traceless polarisations.
- **Round 3 changes:** five numbers in one clause, plus record corrections and a new refining script.
- **Original targets:** ch17 `sec:ch17-done` item 2 (B is a lemma) and item 6 (F computed, G_eff not an input); sub-target G_T = G_A.
- **Critical-path set as read:** A, B, C, D1, E, F, G-derived, N. No discrepancy.
- **Problem B (verbatim, L45-47):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- **Problem F (verbatim, L1366-1369):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion." I read the whole label this round, which closes the partial read noted in r2.

## Checks performed
All runs used copies in my scratchpad. `git status` is unchanged afterwards, and I wrote nothing to the repo.

**1. Insert bytes (my own script)**
- HEAD blob is r2: 10874 bytes, sha `6294d416...`.
- I extracted (d) programmatically from review-r2.md. The old string occurs once in HEAD and 0 times in the working file; the new string occurs 0 and 1 times.
- r2 + (d) is byte-identical to the working file, with the expected sha `81bb7f16...`. Only line 12 of 15 differs. CR 0, TAB 0, non-ASCII 0.

**2. Mechanics (my own check)**
- Anchor occurs once in appH and once across all chapters, at L2404, preceded by the 045 closing line and a blank line. appH is fully CRLF.
- Braces and `\( \)` balance; no `\label`; one `\paragraph`.
- `ass:lorentzian`, `ch:vierbein-emergence` and `sec:status-B` each have one label; `Steinacker2023` has one bib entry.
- The title fragment occurs 0 times in appH; the corrected 045 sentence occurs once.
- No process language. The word hits ("background", "above", "here") are ordinary uses.

**3. Build**
`compile_check.py` on a scratch copy of the script and insert, built from the current tree: baseline 323 pages, with insert 325 pages. Exit codes all 0, no undefined references or citations, no duplicate labels, CRLF preserved.

**4. s6 re-run on a copy outside the repo**
- Exit 0, empty stderr, about 28 s. The output is byte-identical to the saved `s6_root_refine.out.txt`.
- The nine rows of the proposal's table match the output at every printed digit.
- All four printed inequalities hold for every integer 2 <= n <= 300; all four pre-(d) inequalities fail.
- s6 matches s4's coefficient: N(M) = W1 beta_X lambda_L + 1/M^2 + 24 (L/c)/M^2 (s4 docstring L15). So f(M) is the right equation.
- Scan size is 299 values for every integer and 107 for the review's sample, as stated.

**5. Independent recoding of beta_X (my own numpy code)**
- It reproduces the insert's values: J(J+2) 0.065, 0.40, 0.859, 0.964; 3J 0.185, 0.693, 0.944, 0.968.
- It reproduces the s4 check lines to six digits.
- c(J,J') closed forms match sympy Clebsch-Gordan coefficients for J <= 8, and each row sums to 1.

**6. Consequence bound and sum, re-derived**
- M Sum << 1 gives coth^2/M >> coth^2 Sum >= 1, because the J = 1 term is 1.
- The sum is 5.835, 10.325, 14.918 at n = 30, 300, 3000, with increments of 2 ln 10.

**Not re-verified this round**
- s1-s4 and s5 were not re-run. No computation changed; r2 reports s1-s4 identical. My own mechanics check replaces s5.
- lambda_L = -1.956233 is taken from the saved s4 output.
- The torsion code is still not independently rewritten (as at r1 and r2).

## Ruling on the researcher's flag: the wording is correct as it stands
The flag treats the nine rows as the evidence for the parenthetical, but they are the wrong test. Those rows are the zeros of N(M), which are special values of M. The insert's sentence concerns beta_X as a function of (M, n) across the whole range M >> coth^2 tau. So I tested that range directly, at the base-point value coth^2 tau = 25/9.

| n | M/coth^2 = 3 | 10 | 100 | 1e4 | M -> infinity |
|---|---|---|---|---|---|
| 2 | 0.5234 | 0.5204 | 0.5151 | 0.5143 | 0.5143 |
| 10 | 0.9067 | 0.9101 | 0.8797 | 0.8641 | 0.8639 |
| 30 | 0.9646 | 0.9762 | 0.9722 | 0.9524 | 0.9516 |
| 300 | 0.9872 | 0.9951 | 0.9985 | 0.9973 | 0.9950 |
| 1e4 | 0.9931 | 0.9977 | 0.9997 | 0.99998 | 0.9998 or above |
| 1e6 | 0.9957 | 0.9986 | 0.9998 | 1.0000 | 1.0000 |

- **"Of order one":** over M/coth^2 in [3, 1e6] and 2 <= n <= 500, the minimum of beta_X is 0.51429. That is the n = 2 large-M limit, and 18/35 by hand from the truncated c(J,J') weights.
- **"Tends to one as n grows":** this holds in the whole range. The minimum over M >= 3 coth^2 for each n rises to 0.9957 at n = 1e6. beta_X increased with n at every step from 2 to 2000 at the four values of M tested.
- **Analytic reason:**
  - At fixed M, W1 ~ 2 ln n.
  - W1 (1 - beta_X) stays bounded, since the O(1/J) terms of the J -> J+2 and J -> J-2 weights cancel at large J and the truncation loss at J ~ n is O(1/n).
  - So 1 - beta_X = O(1/ln n). Numerically, (1 - beta_X) 2 ln n settles near 0.04 at M = 10 coth^2.
  - At M -> infinity for fixed n, beta_X -> Sum(2J+1)c / Sum(2J+1), and 1 - beta_X is about 1.5/n (0.0149 at n = 100).
- **Consequence for the record:** the proposal's statement that the sentence rests on claim 9 is right but understated. It also has direct numerical support on the controlled range, under H10, H11 and H13, all of which the insert's closing sentence lists.
- **Convergence caveat:** at fixed M, convergence is slow. At n = 2 the two readings have comparable weight (beta_X = 0.51), so "leading" there means only "not smaller". The insert already carries this: "of order one" comes first, the setting is the Poisson limit, and the 0.51-0.98 range is printed in the next sentence. This does not make the wording false, and I require no edit.

## Findings
**New findings:** no blocking, major or minor finding requires a change.

**Earlier findings re-verified**
- **review-r2 finding 1:** closed. (d) was applied exactly, and the numbers hold literally.
- **review-r2 finding 2:** closed, record only.
  - proposal-r3's corrections match the roots: 0.546-2.46, 0.090-2.46, 4.13-12.66, and 0.520, 0.898, 0.954, 0.929, 0.974.
  - The 0.895-0.974 list is withdrawn, and the reason given (parameters 1.79 and 2.46 at L/c = 1) is correct.
  - The ledger's 046 entry quotes none of these figures.
- **review-r2 finding 3:** closed. s6 reproduces the review's table on the 107-value sample and extends it to all integers.
- **review-r1 findings 1-3:** the replacements remain in the file unchanged, because only (d) differs from r2.
- **review-r1 findings 4-7:** remain no-change or adequate; claims 1-14 and 15b are unchanged, by diff of the claim tables. Only claim 15 is reworded, and 15a is added, as stated.

**Notes for the record, not conditions of acceptance**
1. **B status lines.** proposal-r3 gives B's status text as L44-46 and its targeted read as L43-46. The text is at L45-47. The quotation is correct, and no manuscript text is affected.
2. **Claim 15a is conservative.** The proposal calls uniqueness of M* grid-level. The proof below gives uniqueness for all M > 0.
   - The zero solves M^2 W_B(M) = (1 + 24 L/c)/|lambda_L|. M^2 W_B is a positive sum of terms M^2/(M+a) and M^2 ln(1+d/A)/d, with A = M + lo.
   - Each term increases in M. Using ln(1+x) >= 2x/(2+x), the derivative condition reduces to 4/(2A+d) >= M/(A(A+d)), which holds because M <= A and 4(A+d) >= 2A+d.
   - M^2 W_B runs from 0 to infinity. So for L/c >= 0 and lambda_L < 0 there is exactly one zero for every n, which supports the insert's "changes sign at one value".
   - This covers uniqueness only, at first-order torsion and with lambda_L from one base point and one wave vector. A later ledger line may record it, but the insert needs no change.
3. **Ledger.** The next ledger line for 046 should use the root values, as the proposal says.

## Scope of what is established
- **Exact:** the spectrum mu_J = J(J+2) for the frozen-coefficient loop operator; the Duhamel weights; the calibration 1/4; L1 + L2 = SC2 - SC1 at seven points; the power-law tail; beta_X -> 1 as n -> infinity (H10, H11).
- **Numerical or model-conditional:**
  - the beta_X table and half-spread 2.42 beta_X (H13);
  - the span structure and lambda range;
  - the M* ranges (free L/c, first-order torsion, J = 0 only, base point (5,3)).
- **Open:**
  - the range M ~ coth^2 tau and the tuned points;
  - the S^2-M part;
  - the cone at torsion order;
  - the inert amplitudes;
  - the trace polarisation;
  - K itself;
  - G_eff.
- **Status:** PROGRAMME-CONDITIONAL; nothing is DERIVED. Problems B and F stay OPEN. No label change is proposed.
- **No-go class:** rank-6 CP^{1,2} x K, level-one graviton, IKKT content supplied, frozen leading symbol, inert amplitudes zero, product background without mixed flux, cross term dropped, first-order torsion on J = 0 modes. It closes no direction outside this class.
- **Open avenues, ranked (unchanged):**
  1. Exact Gaussian resummation of the background torsion, with the cone at the same order; this decides M ~ coth^2 tau and the tuned points.
  2. Schur elimination of the inert and J = 2 amplitudes.
  3. The S^2-M fibre-flux part with the cross term kept.
  4. Equivariant K with mixed M-K flux, which could suppress the tail.
  5. A J = 2 or hs-mode graviton.
  6. Other presentations (M^{A5}, non-product).
  7. Reconciling J(J+2) with 3s; the findings do not depend on it.

**Milestone:** M2 and M3 are not met, and M1, M4 and M5 do not apply. Not a breakthrough.

## Recommended disposition
Integrate as-is, with the bytes above converted to CRLF, immediately before `\section{Problem G: HBEV}` in `chapters/appH-microscopic-proofs.tex`. Do not edit the 045 paragraph. Only the author merges. This `ACCEPT` is a review verdict, not merge approval.

## Corrected snippet
None. No byte changes.

## Files
- Accepted insert: `C:\Users\redgi\Projects\namcg-lab\proposals\046-fibre-regime-interpolation\appH_insert.tex`
- Proposal: `C:\Users\redgi\Projects\namcg-lab\proposals\046-fibre-regime-interpolation\proposal-r3.md`
- My beta_X check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\r3\gk_beta.py`
- My byte check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\r3\gk_bytes.py`
- My mechanics check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\r3\gk_mech.py`
