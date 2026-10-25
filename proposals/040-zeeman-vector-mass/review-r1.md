VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: first | OPEN: 0/2

## Verdict
The Zeeman log coefficients, the supertrace cancellation and the bounded one-orbit-point no-go are sound and correctly scoped. The 034 sign error is real, but the proposal under-reports it. The same sign error is in the merged 032 Landau-model Fin/c values, and the 034 numbers should be corrected in place rather than only by an appended subparagraph.

## Source reading
Digest + targeted reads. `make_digest.py --check` printed `DIGEST STALE (head changed)`, and the chapters are dirty from the accepted 038/039 integrations. I therefore applied CLAUDE.md 3(d) by direct reads, not a full scan. I read in full:
- the Problem F ledger label (`sec:status-F`) and the Problem E ledger label (`sec:status-E`);
- the Problem F paragraphs from the supertrace block (line 2235) through the 034 block, ending before `\section{Problem G: HBEV}` (line 2295);
- the Chapter 17 Problem F passage (line 403).

I also read `proposal-r1.md`, `appH_insert.tex`, `l3_fin.py`, the 032 scripts `s6` and `s7` and the 032 proposals, and the 040 `.out.txt` files.

## Claim under review
Problem F (Appendix H `sec:status-F`), verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."

Chapter 17: "CRITICAL PATH; OPEN."

Problem E: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL." The proposal does not touch E.

The claim is a bounded no-go for the Zeeman-dressed vector-mass term. Its class is: Poisson limit, CP^{1,2}, one loop, nilpotent symbol with a central seam field, Lorentzian i-eps, tetrad part, one orbit point for the finite part. It also corrects a 034 sign error. No label changes.

## Checks performed

**(a) The 034 sign error is confirmed, and it is broader than the proposal says.**
- Fin = lim[∫_{s0}^∞ T2 − c ln(1/s0)]. With T2 ≈ c/s on [s0, s1], this gives Fin = ∫_0^{s1}(T2 − c/s) + c ln s1 + ∫_{s1}^∞ T2. The `+c ln s1` follows from the definition.
- `l3_fin.integrate` (line 21) uses `tot += -c*mp.log(rho1*PH)`.
- I ran `t6_fin_sign_check.py`. It gives 5.414+1.200i for c e^{-s}/s, against the expected −γ = −0.5772. Flipping the sign gives −0.5772.
- I re-ran `t7`. The corrected normalised residuals and scheme-invariant defects match the insert: 0.63/0.82, 0.49/0.99, 0.011/0.94, and defects 0.19/0.075, 4.5e-3/4.4e-3, 2.8e-4/8e-8.
- Corrected tetrad (yy) quotient spectra of both Re and Im have both signs in all six cases, so "both signs" survives for the tetrad part. The 'full' Re spectrum at the first sample becomes [−1, −0.097, −0.001], which is negative definite to rounding. No merged claim is made about 'full' (the 034 block says the full remainder "was not tested"), so nothing merged becomes false. The insert's wording "the quotient spectra of the real parts" must say "tetrad part".
- Proportionality to A is invariant under adding a multiple of A, so non-proportionality is unaffected. Normalised residuals and sign-definiteness of quotient spectra are not invariant. The insert says this correctly.

**New finding: the same error is in the merged 032 block.**
- `032-landau-resummation/s7_resummed_sector_mp.py` line 35 has the same `tot += -c*mp.log(rho1*PH)`. `s6` also has `reg - c*np.log(s1)`.
- Its Fin/c values are merged at `appH` line 2278 ("Einstein--Hilbert sector in a four-dimensional Landau model"): real parts 7.6, 8.1, 6.8 at (0.7,1.3) and 7.6, 5.9, 7.3 at (1.92,1.0).
- At fixed (a,b), Fin/c is shifted by the constant 2 ln s1, with s1 = (0.05/max(a,b)) e^{-0.6i}. Using the stored `s7` outputs, I computed:
  - (0.7,1.3): shift −6.516−1.2i. Corrected Fin/c is 1.05−1.43i, 1.58−1.00i, 0.27−1.52i.
  - (1.919,1.0): shift −7.295−1.2i. Corrected Fin/c is 0.31+0.08i, −1.40−0.15i, 0.03+0.06i.
- So the merged absolute values are wrong. The merged remark that the real part "varies between frames by roughly 20%" is also false: the spread is now of order the size of the values.
- The qualitative conclusion, orientation dependence of the finite remainder, is unchanged and in fact stronger. The Maxwell-part integrals have c = 0 and are unaffected.
- The shift is exact and additive, but the researcher must confirm the numbers by a rerun or the additive identity. I have not re-run `s7`, which takes about 80 s per frame.
- A grep of the other proposals for the `log(rho1`/`ln(s1)` pattern found no other use. Only 032 (s6, s7) and 034/040 (`l3_fin`) carry it.

**(b) Zeeman log coefficients and cancellation.** I re-ran the checks in the `l1b` and `t1`–`t4` outputs.
- Fits: vector g1 = −0.83366, g2 = −0.33334, against −5/6 and −1/3, which are 4A − F1 (1/6 − 1 = −5/6; −4/12 = −1/3). Dirac g1 = −0.33347, g2 = −0.33333, against −1/3, −1/3, which are 4A − F1/2. Scalar fits to A.
- Independent structural check: the weighted supertrace is (4A−F1) + n_ex A − 2A − 2(4A − F1/2) = (n_ex − 6)A. This vanishes for the manuscript's identity Σ w d = 0 (n_ex = 6), and F1 cancels exactly because trΣ_DΣ_D = ½ trΣ_VΣ_V with the four weight −1/2 Dirac blocks. This independently supports the relative normalisation of the V V and N N terms.
- The mass-linear log is Σ w m c = M_str A − μ²F1, as stated.
- The operator coefficient −2Z is consistent with the already-merged `L_a` (−2{F_ab, ε^b}). Gauge invariance for both signs of N is in `t2`, and the sign is fixed by the longitudinal identity.
- The Nikishov-type spin decomposition E±: e^{±2s f_e}, B±: e^{±2i s f_m}, and the growth table in `t3`, are consistent. The ray exponents match the 032 statement. Blocks containing E+ grow for θ < θ*, those containing B+ grow for θ > θ*, and at θ* growth is slow (polynomial).
- `t4` reproduces the leading-symbol check: branch groups −4.007−9.981i and −4.015−9.973i, regulator extrapolation −4.007 to −4.013 and −9.984 to −9.992i. The agreement is about 0.01. It is a leading-symbol check only, and the insert says so.

**(c) Scoping of the finite-part statements.**
- l10 matches the insert numbers: defects 0.91–0.98 vs 4A−F1, 0.79–0.82 vs A, supertrace 0.87–1.0, gauge ≤ 5.5e-6, Re vector form positive definite for all six m², Im definite for m² ≤ 0.6, and Re(xQ_S − 3Q_V) definite for x ranges containing [0,21].
- The scoping is adequate. It states one orbit point, a regulated family, no m² = 0 claim, and a fork rather than a closure.
- Two small gaps are listed under Findings.

**(d) Insert mechanics.**
- Python byte check of `appH_insert.tex`: 0 TAB, 0 CR, 0 non-ASCII, 0 control characters other than LF, ends with LF.
- Braces balance (0). `\(` and `\)` both count 151.
- `\section{Problem G: HBEV}` occurs exactly once. The text before it is the 034 closing sentence "This changes no ledger label; Problem~F remains open.", so the anchor is correct.
- `\ref{ch:vierbein-emergence}` appears once in the insert, and the label exists once in `ch04-vierbein-emergence.tex:2`. No bib entry is needed.
- No process language. "above" appears once, in "the longitudinal-mode identity above", which refers to the same paragraph and is acceptable.
- The proposal's scratch compile reports 309 pages, 0 errors, 0 undefined, 0 multiply defined. I did not recompile; the log is in `compile_check.out.txt`.
- There is exactly one closing scoped status sentence.

**(e) Breakthrough.** No. It is a bounded no-go plus a correction. Agreed with the researcher.

## Findings

1. **Major.** Location: insert, last subparagraph, and merged `appH` lines 2278 and 2289.
   - Finding: the correction is incomplete and in the wrong place. The Landau-model Fin/c values of the 032 block (line 2278, absolute values and the "roughly 20%" frame spread) carry the same sign error and are not mentioned.
   - Finding: the 034 numbers (line 2289) remain wrong in the manuscript, with only a later subparagraph saying they are superseded. That leaves two inconsistent statements in the text.
   - Required action: edit the merged sentences in place (old→new below) and reduce the new subparagraph to the statement of the error and the invariant defects. Flag PRIOR-CLAIM-ERROR for 032 and 034. The researcher must verify the corrected 032 values by rerun or the additive identity.

2. **Major.** Location: insert, "Spin blocks and the continuation".
   - Finding: "No ray gives a convergent proper-time integral" is shown only on rays of the closed fourth quadrant, θ ∈ [0, π/2]. The preceding paragraph explicitly leaves first-quadrant rays unconsidered.
   - Required action: add "of the closed fourth quadrant" there, and add "does not consider the first-quadrant rays" to the final scope sentence.

3. **Minor.** Location: insert, correction paragraph.
   - Finding: "the quotient spectra of the real parts remain of both signs" is true only for the tetrad (yy) form, and for both Re and Im of it.
   - Required action: say "of the tetrad part, real and imaginary".

4. **Minor.** Location: insert, correction paragraph.
   - Finding: at the strongly electric sample the imaginary part of Q is of order 1e-7|A|. The corrected Im residual 0.94 and the Im defect 8e-8 are at the edge of the quoted numerical accuracy.
   - Required action: the text should not rest a claim on that entry beyond reporting the defect. The defects are reported, and no further wording is needed. Optionally state the quadrature accuracy.

5. **Minor.** Location: insert, finite-part paragraph.
   - Finding: the Re/Im sign data are for the Fin form of T2. The scope sentence already excludes the sign convention of the factor i of the mass-linear term. State explicitly "the real and imaginary parts of the form Fin of T_2".

6. **Minor.** Location: insert, correction paragraph.
   - Finding: define the residual (norm of Q−λA over norm of Q, with λ the best fit) and s_1 = (0.05/max(a,b)) e^{-0.6i}, so the correction is self-contained.

## Exact edits to merged text (PRIOR-CLAIM-ERROR)

**034 block, `appH` line 2289, item (iii):**
- Old: `is \(0.54\) and \(0.85\) (centre direction \(0.8\)), \(0.08\) and \(0.48\) (direction \(2.0\)) at one orbit point, and \(0.004\) and \(0.000\) at a second point`
- New: `is \(0.63\) and \(0.82\) (centre direction \(0.8\)), \(0.49\) and \(0.99\) (direction \(2.0\)) at one orbit point, and \(0.011\) and \(0.94\) at a second point`
- The tail "the quotient by \(\kappa\) has eigenvalues of both signs in every case (as has \(A\))" stays true.
- I could not confirm that grep matches these strings character-for-character (my grep escaping failed). The integrator must match them exactly.

**032 block, `appH` line 2278.** These edits are conditional on the researcher confirming the arithmetic in r2.
- Replace `its real part is about \(7.6\), \(8.1\), \(6.8\) in three Lorentz frames of \(F\) at \((a,b)=(0.7,1.3)\) (data \(\kappa,\alpha,y\) rotated, \(A\) fixed; imaginary parts between \(-0.32\) and \(0.20\)), and \(7.6\), \(5.9\), \(7.3\) in three frames at \((a,b)=(1.92,1.0)\) (imaginary parts \(1.05\)--\(1.28\))` with `its real part is about \(1.05\), \(1.58\), \(0.27\) in three Lorentz frames of \(F\) at \((a,b)=(0.7,1.3)\) (data \(\kappa,\alpha,y\) rotated, \(A\) fixed; imaginary parts between \(-1.52\) and \(-1.00\)), and \(0.31\), \(-1.40\), \(0.03\) in three frames at \((a,b)=(1.92,1.0)\) (imaginary parts between \(-0.15\) and \(0.08\))`.
- Replace `the real part varies between frames by roughly \(20\%\)` with `the real part varies between frames by an amount of the order of its mean`.
- The "Maxwell part ... 30–45%" and "order one" statements are unaffected (c = 0, no log).
- The paragraph's last sentence, about the flux-independent coefficient A of the logarithm, is unaffected.

**Replacement for the insert's last subparagraph:**

```
\emph{Correction to the finite-part values of two preceding paragraphs.} The routine that evaluated \(\mathrm{Fin}\) in the Landau-model and the Jacobi-commutator paragraphs added the term \(-c\ln s_1\), \(s_1=0.05\,\mathrm e^{-0.6\mathrm i}/\max(a,b)\) the end of the small-\(s\) interval, whereas the definition of \(\mathrm{Fin}\) gives \(+c\ln s_1\) (a test function \(c\,\mathrm e^{-s}/s\) returns \(5.41+1.20\mathrm i\) instead of \(-\gamma\) for \(c=1\)). The values differ by \(2c\ln s_1\): in the Landau model \(\mathrm{Fin}/c\) is shifted by the constant \(2\ln s_1\) at fixed \((a,b)\), and in the leaf the tetrad form is shifted by a multiple of the form \(A\); the values quoted in those paragraphs are the corrected ones. Proportionality to \(A\) is unaffected by a multiple of \(A\), and the defect \(\|Q-\lambda A\|/\|A\|\), with \(\lambda\) the best fit, is shift invariant: \(0.19\) and \(0.075\) (real, imaginary parts of the tetrad form; first sample), \(4.5\cdot10^{-3}\) and \(4.4\cdot10^{-3}\) (second sample) and \(2.8\cdot10^{-4}\) and \(8\cdot10^{-8}\) (strongly electric sample, \(f_e/f_m\simeq42\)). A normalised residual, and the signs of a quotient spectrum, are not shift invariant for a form that carries a logarithm, because \(A\) is indefinite; the quotient spectra of the real and imaginary parts of the tetrad form remain of both signs.
```

**Wording edits in the other insert paragraphs:**
- "Spin blocks and the continuation": `No ray gives a convergent proper-time integral` → `No ray of the closed fourth quadrant gives a convergent proper-time integral`.
- Final scope sentence: after "the continuation \(m^2\to0\) of the four-dimensional integral," add "the rays of the first quadrant,".

## Scope of what is established

**Established numerically at the stated sample and class** (Poisson limit, CP^{1,2}, one loop, nilpotent symbol with centre flux and central seam field, Lorentzian i-eps, tetrad part, one orbit point and one centre direction for Fin, regulator e^{-ism²} not removed):
- The log coefficients 4A − F1 (vector) and 4A − F1/2 (Dirac block).
- The structural cancellation of the supertrace logarithm and F1.
- The M_str A − μ²F1 form of the mass-linear log.
- The block growth structure on fourth-quadrant rays.
- The leading-symbol equivalence of the two continuation prescriptions.
- The regulated, non-proportional, m²-dependent Fin sign data.

**Not established:**
- Any value at m² = 0.
- The continuation prescription as a derivation.
- The charge and cross parts.
- Window averages.
- Weight-one terms.
- First-quadrant rays.
- Covariance, and any sign or value of G_eff.

Proportionality to A is not restored by the Zeeman term. F, E and all critical-path labels are unchanged. F remains OPEN, PROGRAMME-CONDITIONAL.

**Open avenues, ranked by promise.** Each relaxes one hypothesis of the no-go.
1. Window average over the centre variable of the full corrected Fin (tetrad + charge + cross), using the shift-invariant defect and the now-finite massless supertrace form. Relaxes per-centre-variable and tetrad-only. This is the best-posed sign test.
2. Exact analytic u-integration so that the continuation is branch-wise with no regulator. Relaxes the regulator and the quadrature, and would give definite sign data.
3. More orbit points, starting with the strongly electric limit, where 034 saw near-proportionality to A.
4. Weight-one terms and gradients, and a spectral Landau-level definition with ghost subtraction. Relaxes the nilpotent order.
5. A connection-sector (X) or fibre term for covariance. The y^μ dependence of A, F1 and F2 is untouched by the Zeeman term. This is where the covariance gap lies.

## Recommended disposition
Revise. The researcher submits r2 with:
- the edits above to the merged 034 and 032 text, and the replaced correction subparagraph;
- a rerun or an explicit exact-shift verification of the corrected 032 Fin/c values (and the third (a,b) case);
- the fourth-quadrant and tetrad wording fixes, and a note that Findings 4–6 are addressed.

No new physics is needed. Nothing is accepted verbatim until r2. After those edits the first four insert subparagraphs, with the two wording changes above, would be acceptable. The fifth (the correction) is accepted only in the replacement form given.

## Corrected snippet
Given above. The only extra assumption is that the integrator verifies the 032 corrected numbers (an additive shift of 2 ln s_1 at fixed (a,b)) before use.
