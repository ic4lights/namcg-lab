VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: first | OPEN: 0/1

## Verdict
The core theorem, the N = 2 proof, the Definition C reduction and the correction of the 052 sentence all survive independent re-derivation. Six byte-level changes are still required, one of them major: Definition C omits its convergence factor and does not say which "Euclidean model" it means.

## Scan ruling
**Ruling: the scan requirement is met by relying on the recorded ordinal-50 full scan. No new scan is claimed.** The ruling covers CLAUDE.md 3(c), triggered by E1, and 3(b), triggered by the M3 verdict. Ordinal 51 is not a 5th item.

**Hash verification, recomputed by me:**

| Item | Value | Meaning |
|---|---|---|
| Working tree with the 27-line 052 block removed (appH L1424-1450), appH | sha256 `407a1a0e...3f86` | Equals review-r2's value |
| Same tree, `make_digest.content_hash` | `717cadc85cf88f78` | Equals review-r2's value |
| Raw HEAD blobs | `b30bd17cfe401d22` | Differs only by line endings: `core.autocrlf=true`, LF blobs |
| Other 29 files, working tree against HEAD | Identical modulo EOL | Confirmed file by file |
| appH numstat | 27 added, 0 removed | The 052 block only |
| Current chapters-hash | `37430d59c9c4ecaf` | For the next round |
| Current appH sha256 | `f3d20921ddb323b0e704c993f6d3ed7a8c7a8875848be92ad6f07df6fe1b1285` | For the next round |

`make_digest --check` prints DIGEST CURRENT. `dirty-chapters: yes` comes from 052 only.

**Read in full by me:**
- appH L1424-1465 (the whole 052 block, every passage E1 touches, all of Problem E)
- ch17 L394-399 and the L718 item
- ch04 L285-354, including ass:lorentzian
- ch03 L139-157, including eq:Smatrix

**Grep across all chapters:** Wick, contour, Euclidean model/integral/matrix/positivity, Lorentzian matrix/integral, Austing, "no longer related", i-epsilon, convergence regulator, flat direction, reflection statement, Pfaffian, the Steinacker2026Invitation citation. The only statements on this topic are ch04 L325, ch17 L397-399, and appH L1447 and L1460. L1460, L325 and ch17 stand; L1447 is what E1 corrects. I found nothing else that goes stale.

**Limits of this ruling:**
- It rests on review-r2's composite record, which is r1's reading of 29 files plus r2's reading of appH.
- It is not a precedent beyond this situation of near-identical bytes, a recent scan and one small scope edit.
- It lapses if r2 changes any chapter byte other than the 052 block's pending commit. Line-ending-only differences do not count. Recheck the hashes above.

## Source reading
Digest header + targeted reads, relying on the scan record above. Not a full scan. No unreadable files.

Literature read from TeX (scratchpad only):
- hep-th/0103159: Sec. 2 setup and Sec. 4 in full
- 2501.17798: whole, plus the three figures rendered
- 2404.14045: through the IKKT definition
- 2604.19836: Sec. 2
- 2609.08955: Sec. "The Lorentzian IKKT model"
- 2205.04726 and 2408.04000: contour passages

## Claim under review
- **Target:** Problem E, derive Lorentzian signature. Appendix H verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature." and "Remains Assumption~\ref{ass:lorentzian}." Ch17: "OPEN; CRITICAL PATH for the matrix-derived label."
- **Package:** at finite N, for polynomial O of degree k < 14, lim I_eps[O] = e^{7 pi i (N^2-1)/4} x Euclidean integral of O at phases. This is proved at N = 2 and conditional for N >= 3. The package also covers fixed eps, regulator and mass statements, Definition C at N = 2, and correction E1 of the 052 sentence.
- **Effect on the target:** it does not derive the target.

## Checks performed
**Re-derived by hand (direct verification):**
- Re i S_b = -sin(pi u/2) S_E, and the regulator real part, window u < 2/3.
- Stokes boundary term: polynomial x e^{-eps cos(3 pi u/4) R^2}. Nothing arrives from infinity.
- Pfaffian phase e^{i pi u g} and measure phase e^{3 pi i g/4}, total e^{7 pi i g/4}. At u = 1, A_0 = e^{i pi/8}(-i At_0).
- Domination and the rate: |e^{-eps w}-1| <= eps|w| for Re w >= 0, which gives k <= 11.
- The delta factor: phases stay in [-3 pi/8, 3 pi/8] and [-pi/8, pi/8].
- Pf identity proof, including corank 2 giving second-order vanishing, and sigma.L eigenvalues 1 (x4), -2 (x2), so c' = 4.
- Cauchy-Binet.
- Wishart reduction and flat corner: rho^{k/2-8} d rho, so k < 14 exactly. The same power appears for the C integrand in both corners (g_+ large, g_3 large).
- Mass brackets and window. The joint limit needs gamma -> 0 as stated.
- M-regulator argument. The SO(9,1) Ward identity holds on all of SO(9,1). For the non-identity component with det = 1, S = gamma^1 gives Pf invariance, using evenness of degree 8g. Explicit check: boosted Tr A_0^2 reproduces e^{-3 pi i/4}x.
- Definition C: measure power r^{d-2}, FP eigenvalues, Stokes faces, sign count +,-,+.
- Second derivation of C by another route: C's integrand is the Lorentzian Wishart pushforward onto the signature (2,1) sector of G. Its Jacobian is |det G|^{(D-4)/2} |V(g_+,g_-,-g_3)|, and the spacelike (3,0) sector is the one the slice loses.

**My own numerics (checks, not proofs; scratchpad `gk53/gk_a.py`, `gk_b.py`):**
- Pf/(det G)^4 = 256 at random complex A, with my own real symmetric gammas found by clique search.
- Pfaffian phase ratio at u = 0.3, 0.6, 1 matches e^{i pi u g}.
- Own quadrature: E = C(u=1) = C(u=0.7) to the digits printed (5 decimals):
  - gamma = -7.9: 0.10954+0.91787i
  - gamma = -5.6: 0.25018+1.21017i
  - gamma = -2: 0.95962+1.9211i
  - gamma = -0.5: 1.69093+2.76611i
- D = 10 with Pfaffian, gamma = 0: E = C(u=1) = 3.61081(1+i), which equals e^{i pi/4}(1/2)(10.2129). The saved `n2_defC_vs_E.out` value 3.6126 is about 5e-4 high from its grid. That number is not in the insert.
- **Smeared-delta Monte Carlo of the C reduction**, Gaussian test weight, full determinant, s = 0.3, 0.1, 0.03, 0.01. Ratio to the closed-form reduced value:
  - d = 4: 0.908, 1.013, 1.011, 1.006 (+-0.001)
  - d = 5: 0.892, 0.999, 1.002, 1.001
  - This confirms that the A_0 = 0 sector drops out as s -> 0, compatible with the predicted O(s^{d-3}).
- Own real-contour grid for C at gamma = -2 reproduces the saved table:
  - eps = 0.4: 0.6593+2.1412i (saved 0.6597+2.1417i)
  - eps = 0.2: 0.7402+1.9635i (saved 0.7400+1.9631i)
- Researcher's `pf_su2_identity.py` and `n2_defC_vs_E.py` re-run: byte-identical to saved outputs.

**Not re-run:** `n2_reduced.py` (over an hour), `n2_mc_check.py`, `n2_defC_realcontour.py`. The saved outputs were read and compared with my values. The N = 3 probe was not re-run.

**Numerics labelling:** the Monte Carlo at D = 10, eps = 1.5 does not appear in the insert, and the proposal labels it failed. Pfaffian identity numerics, the Cauchy-Binet bound and the N = 3 probe are labelled correctly as checks.

**Austing-Wheater audit (Sec. 2 setup and Sec. 4 read from TeX):**
- The quoted sentence exists at L1009-1011.
- Every step in Sec. 4 is a bound on a modulus. No positivity or cancellation is used.
- The bosonic exponent depends only on real x.
- Gauge rotation uses invariance, and P_theta is invariant.
- "say x_1" (L341) is the only symmetric step. A union bound over mu, including mu = 0, replaces it, since each case bounds identically.
- k_c arithmetic reproduced; at g = 3 it agrees with my exact count.
- "Same proof" is acceptable when labelled conditional, provided the insert names this one change.
- AW themselves prove no lower bound for N >= 3.

**052 sentence attribution:** 2609.08955 L757 reads "The Lorentzian model is then no longer related to the Euclidean model by Wick rotation." Accurate. The opposite quartic sign (L724) and the conjugation remark are also correct.

**2604.19836:** eq: TrAsq and the gamma < 0 / gamma > 0 statements (L599-608) support the attributions.

**Citations:**
- Crossref and INSPIRE confirm PRL 134, 211601 and PRL 134, 041603 (titles, authors), plus JHEP 04 (2001) 019.
- INSPIRE confirms the 2604.19836 record.
- All four bib entries are correct and there is no key collision.
- `bib/namcg.bib` has no CR bytes, so append with LF.

**Mechanics on a scratch copy, with all six changes below applied:**
- Each old string occurs exactly once.
- E1 old string: 1. Anchor: 1.
- No bare LF after CRLF conversion. Insert is ASCII.
- pdflatex + bibtex + 2 pdflatex: 357 pages, 0 undefined or multiply defined references.
- The repository is unchanged except the expected appH and bib.

## Findings
**F1. Severity: major. Location: insert, Definition (C), "So for gamma <= 0, wherever the integrals converge...".**
- Finding: two hypotheses are missing.
  - (a) (C) on the real contour is not absolutely convergent, as 2404.14045 L1079-1081 says. The Stokes step from u = 0 needs a convergence factor removed last.
  - (b) "Euclidean model" here is not the e^{-S_E} object of the preceding display without phases. The equality holds with O and S_gamma on R_1, equivalently for the model A_0 = -i A_D of 2501.17798, Eq. Euclidean-ikkt.
  - The ratio also needs a non-vanishing denominator.
- Required action: replacement S4.

**F2. Severity: minor. Location: insert, Pf identity.** "vanishes when a singular value does" is insufficient. It needs second order, and c_P != 0 needs the value at s = (1,1,1). Replacement S2.

**F3. Severity: minor. Location: insert, AW sentence.** It does not record that the one symmetric step becomes a finite sum, or that the phase keeps the entry bound. AW's sentence reads "from now on". Replacement S1.

**F4. Severity: minor. Location: insert, moments.** The table is of moduli. Replacement S3.

**F5. Severity: minor. Location: insert, closing sentence.** "no datum beyond the Euclidean model" omits the N >= 3 condition and the retained mass at gamma < 0. Replacement S5.

**F6. Severity: minor. Location: E1.** The new text folds the conditional status into "hypotheses recorded". State it, since this text corrects a prior claim. Replacement S6.

**F7. Severity: record only, no text.** Prior work: 2408.04000 (Eq. Wick-rotation_MM, "Cauchy's theorem equates... as long as the inserted operators have no singularity") and 2205.04726 (L261-272) also state the deformation. In the passages I read, neither gives a Pfaffian bound or a regulator limit. "May be folklore, no novelty" stands. Citers listed through INSPIRE for 2501.17798 (20), 2604.19836 (9), 2404.14045 (28), hep-th/0103159 (95; post-2019 subset scanned). I found no proof with a regulator limit; I read only contour greps of the eight I downloaded. Not evidence of absence.

**F8. Severity: record only. Asano et al. (2404.14045) artifact claim.** Its artifact claim is made for the real-weight toy model and for gamma > 0 with convergence factors. Its N = 2 demonstration is in a paper "in preparation", not verified. Its Gaussian example gives finite cutoff results and identical invariant observables for cutoff and gauge-fixed models, which agrees with this package. Its one-vector gauge-fixed example also keeps only x_i = 0, as the researcher's a = 0 ruling does. No contradiction within gamma <= 0.

**Rulings on the listed questions:**

1. **N = 2 limit:** verified, including phase, rotation, no contribution from infinity, k < 14 and O(eps) for k <= 11.
2. **N >= 3:** acceptable as conditional, with S1. Z_E != 0 is correctly a named hypothesis.
3. **Fixed eps and mass/regulator statements:** verified.
4. **Definition C:**
   - The reduction is verified, including the a = 0 sector, by proof, an independent route and smeared Monte Carlo.
   - The conflict with 2501.17798 is unresolved and the insert records it neutrally. I found no error in the reduction.
   - Evidence, read by eye from the rendered figures: at 1/|gamma| about 0.127 the published Euclidean point is about 1.00, against 0.918 from direct quadrature of the printed E model, a model with no slice in it. That is about the size of the E-L gap there. At gamma = -5.6, E about 1.21 agrees with quadrature while L about 1.30, roughly 2 of its error bars above. Near gamma -> 0-, plotted L stays well below the exact value (4.8 at gamma = -0.1).
   - This suggests a numerical systematic but does not prove one, and the insert must not say so.
   - SME consultation is not needed because the verdict does not depend on settling it. The loop may ask later whether the "full paper" of 2501.17798 or the "largeD" paper exists.
5. **052 sentence: PRIOR-CLAIM-ERROR, narrow.**
   - Attribution is accurate.
   - As an unqualified manuscript statement, the first clause ("no longer related") is true at fixed eps and false in the limit eps -> 0 at finite N for these observables (proved at N = 2, conditional for N >= 3).
   - The second clause ("does not bear") is, strictly, unsupported rather than proved false. The reflection statement concerns a tree-level form on a commuting background, not these moments, so the correct content is "not excluded", which is what E1 says. I do not adopt the researcher's "both clauses false" for the second clause.
   - The error is overbreadth. It is not load-bearing for 052's mathematics.
   - E1 is the minimal correct edit, with S6. "Its" must go, since its antecedent would shift. The citation moves to Problem E, where the sentence is attributed.
6. **Limits:** all stated. The narrowing of the scout's "cannot come from that limit" is correct, since the theorem concerns these moments only. Eta question: evidence only, no decision needed.
7. **Numerics and literature:** covered above.
8. **Milestone:** M3, since an accepted claim is overbroad to the point of being false in a limit. No label changes. Not a breakthrough; M1 does not apply. One scoped closing status sentence. Emergence kept: eta on the matrix indices stays a retained input and Assumption ass:lorentzian stands. No process language. Per the directive, this does not stop the loop: integrate on ACCEPT and record.

## Scope of what is established
- **Proved at N = 2:**
  - the limit, with rate
  - Pf = c_P (det G)^4 and the Cauchy-Binet bound
  - k < 14 sharp for the modulus
  - regulator independence and SO(9,1) invariance of the limit
  - the gamma statements
  - Definition C equality for gamma <= 0, with a convergence factor, for invariant O
- **Proved at any N:** fixed-eps contour identity for u < 2/3, and non-integrability on R_1 at fixed eps.
- **Conditional for N >= 3:** the same limit and its corollaries, on Lemma D (AW's proof extended) and on Z_E != 0 for ratios.
- **Numerical:** the tables, including log and 1/eps growth at k = 14, 16.
- **Unresolved:** the difference from the plots of 2501.17798; the even-rank count for C at N >= 3 (formal, correctly kept out of the insert).
- **Classification:** PROGRAMME-CONDITIONAL. Problem E is still OPEN. No signature is derived. Assumption ass:lorentzian is not discharged. Not stated: N -> infinity first, fixed gamma > 0, degree >= 14 beyond the numerics, non-polynomial O, C_{mu nu lambda} != 0, fermion mass.

**Obstruction classes (bounded):**
- *Limit class:* traceless SU(N) at finite N; IKKT content supplied; eq:Smatrix with C = 0 and no matter term; polynomial O of degree < 14; positive definite quadratic regulator; eps -> 0 before any other limit; gamma <= 0 or gamma -> 0 with gamma/eps bounded above. In this class the low moments are Euclidean with phases.
- *Definition C class:* N = 2, d >= 4, invariant O, gamma <= 0, convergence factor.

**Open avenues, ranked:**
1. Non-polynomial observables at N = 2 (Tr e^{ik.A}, timelike k first). No deformation is needed, and it tests a real-time reading of the integral itself.
2. N -> infinity first, starting from a controllable model. Non-uniformity of C_{O,N} is the point at issue.
3. C_{mu nu lambda} != 0, the manuscript's own cubic term. The rotated term is not sign-definite along flat directions.
4. Fixed gamma > 0 at N = 2: exact reduction and continuity at gamma -> 0+. This is a deformation, so rule 3 scopes it.
5. Definition C at N >= 3 and the discrepancy with 2501.17798.

Fermion mass is also open, as a deformation. R2 stays the next class-level test. It should state its order of limits, as the proposal says.

## Recommended disposition
Revise and return for r2 with exactly the bytes below, updating `apply_check.py` and the proposal's E1 text. The E2 anchor, the labels and `bib_additions.bib` are unchanged. All old strings were verified to occur once in `appH_insert.tex` or, for S6, in the proposal's E1 New text and `apply_check.py` NEW.

## Corrected snippet
No new physics. The only extra assumption made explicit is the convergence factor in S4.

**S1.**
- Old: `on their entries, as that reference says. The same proof therefore gives`
- New: `on their entries, as that reference says. The phase keeps that bound, and the step singling out one large matrix, written there for one index, becomes a finite sum over \(\mu\). The same proof therefore gives`

**S2.**
- Old: `and the resulting \(6\times6\) determinant vanishes when a singular value does (also checked`
- New: `and the resulting \(6\times6\) determinant, of degree six, vanishes to second order in each singular value and is nonzero when all three equal \(1\) (also checked`

**S3.**
- Old: `converges to the Euclidean value for \(2n\le12\)`
- New: `converges in modulus to the Euclidean value for \(2n\le12\)`

**S4.**
- Old: `So for \(\gamma\le0\), wherever the integrals converge, the invariant observables of (C) at \(N=2\) equal those of the Euclidean model (exact).`
- New: `So for \(\gamma\le0\), with a convergence factor as in (A) removed last, which (C) also needs since it is not absolutely convergent, and wherever the integrals converge and the partition function does not vanish, the expectation values of invariant observables of (C) at \(N=2\) equal those of the Euclidean model at the same phases (exact), namely the same \(O\) and \(S_\gamma\) on \(\mathcal R_1\) with weight \(\mathrm e^{-S_{\mathrm E}}\), which by the rotation \(A_\mu=\mathrm e^{\pi\mathrm i/8}\tilde A_\mu\) is the model with \(A_0=-\mathrm iA_{d+1}\) of~\cite{ChouNishimuraTripathi2025}.`

**S5.**
- Old: `the regulated integral therefore carries at finite \(N\) no datum beyond the Euclidean model and its phases.`
- New: `the regulated integral therefore carries at finite \(N\), conditionally for \(N\ge3\), no datum beyond the Euclidean model, with any mass term on \(\mathcal R_1\), and its phases.`

**S6 (E1 New text).**
- Old: `At finite \(N\), with the limit and the hypotheses recorded in Section~\ref{sec:status-E}, its polynomial moments`
- New: `At finite \(N\), in the limit and under the hypotheses recorded in Section~\ref{sec:status-E} (proved at \(N=2\), conditional for \(N\ge3\)), its polynomial moments`

**Process note:** one compound command of mine, which included `rm -rf` of a scratch directory, was denied. I reran it without the removal, using a new scratch directory. Nothing was written in the repository and no background job was started. Scratch files are in `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk53`.

**Relevant files:**
- C:\Users\redgi\Projects\namcg-lab\proposals\053-lorentzian-integral-limit-order\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\proposals\053-lorentzian-integral-limit-order\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\053-lorentzian-integral-limit-order\apply_check.py
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex
