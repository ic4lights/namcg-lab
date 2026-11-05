VERDICT: ACCEPT | MILESTONE: none | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/0

## Verdict
Every r1 finding is closed. The 032 rerun confirms the corrected values, the three merged-edit old strings each occur exactly once, and the insert is mechanically clean. One wording tweak to merged Edit 3 is part of the accepted text (see below).

## Source reading
Targeted reads. The Problem F/E ledger entries, the 032/034 blocks and the Chapter 17 F passage were read in full in r1, and the working tree is unchanged apart from the proposal files. This is not a full scan. The digest is stale on head only.

## Checks performed
- **Insert diff, r1 to r2.** I normalised CRLF and diffed. The differences are exactly:
  - the paragraph title now reads "two preceding paragraphs";
  - "No ray of the closed fourth quadrant ...";
  - "(iii) for the real and imaginary parts of the forms Fin of T_2, on the quotient by κ, ...";
  - the replaced correction subparagraph;
  - "the rays of the first quadrant," added to the scope sentence.
  - Nothing else changed.
- **Correction subparagraph.** It matches my r1 text plus two clauses: the residual definition ‖Q−λA‖/‖Q‖, and the Im part at the strongly electric sample "vanishes to the accuracy of the quadrature". Both clauses are accurate. The Im Q there is about 1e-7 of |A|, and the corrected Im λ is 3e-8.
- **032 rerun.** `s7_corrected_sign.py` differs from the 032 `s7` in exactly one line, `tot += c*mp.log(rho1*PH)`. I read the output for all 9 frames:
  - (0.7,1.3): 1.0507−1.4343i, 1.5762−0.9997i, 0.2726−1.5214i;
  - (1.919,1.0): 0.3135+0.0814i, −1.3956−0.1486i, 0.0314+0.0649i;
  - (0.4696,1.0), not quoted in the manuscript: 1.2375−1.4915i, 0.5978−1.6837i, 1.3091−1.5277i.
  - The first two match my additive-shift numbers. The quoted imaginary ranges are right: −1.52 to −1.00, and −0.15 to 0.08.
- **Deviation on the frame spread.** It is justified. At (1.92,1.0) the real-part spread is about 1.7 and the mean is −0.35. At (0.7,1.3) the spread is about 1.3 and the mean about 0.97. The spread is therefore of order or larger than the mean in magnitude.
- **Old strings.** I checked them with Python on the current file (CRLF normalised). Edit 1's old string occurs 1 time, Edit 2's occurs 1 time, and Edit 3's occurs 1 time. None spans a line break.
- **Byte check of `appH_insert.tex`.** 0 TAB, 0 CR, 0 non-ASCII, no control characters other than LF, ends with LF. Braces balance. `\(` and `\)` both count 157. `\ref{ch:vierbein-emergence}` appears once. "above" appears once, referring to the same paragraph. There is no process language, no bib entry, and one closing scoped status sentence.
- **Anchor.** `\section{Problem G: HBEV}` occurs once. The insert goes immediately before it, after the 034 closing sentence.
- **Scope.** No label change. F stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. Emergence is untouched. This is not a breakthrough.

## Findings
- None blocking or major.
- Minor, resolved by the accepted string below: Edit 3's "larger than its mean" is awkward because the mean at (1.92,1.0) is negative. Use "the magnitude of its mean".

## Scope of what is established
No change from r1. It is a bounded no-go (class: Poisson limit, CP^{1,2}, one loop, nilpotent symbol with central seam field, Lorentzian i-eps, tetrad part, one orbit point, regulated) plus a PRIOR-CLAIM-ERROR correction of the sign of the log term in the Fin routine. The correction covers 032's Landau-model Fin/c values and 034's normalised residuals, and the qualitative conclusions of both stand. The open avenues are the same as in r1, in this order:
1. The window average over the centre variable of the full corrected Fin, using the shift-invariant defect and the finite massless supertrace form.
2. Analytic u-integration, which would give a branch-wise continuation with no regulator.
3. More orbit points.
4. Weight-one terms and a spectral Landau-level definition.
5. A connection-sector term for covariance.

## Recommended disposition
Integrate the insert and the three edits below.

## Accepted text, exactly
1. **Insert.** `proposals/040-zeeman-vector-mass/appH_insert.tex` (r2) as submitted. Place it immediately before `\section{Problem G: HBEV}` and convert to CRLF.

2. **Edit 1** (034 block, item (iii) of "Result in the class"). Replace exactly:
   - Old:
   ```
   is \(0.54\) and \(0.85\) (centre direction \(0.8\)), \(0.08\) and \(0.48\) (direction \(2.0\)) at one orbit point, and \(0.004\) and \(0.000\) at a second point
   ```
   - New:
   ```
   is \(0.63\) and \(0.82\) (centre direction \(0.8\)), \(0.49\) and \(0.99\) (direction \(2.0\)) at one orbit point, and \(0.011\) and \(0.94\) at a second point
   ```

3. **Edit 2** (032 Landau-model paragraph, values). Replace exactly:
   - Old:
   ```
   its real part is about \(7.6\), \(8.1\), \(6.8\) in three Lorentz frames of \(F\) at \((a,b)=(0.7,1.3)\) (data \(\kappa,\alpha,y\) rotated, \(A\) fixed; imaginary parts between \(-0.32\) and \(0.20\)), and \(7.6\), \(5.9\), \(7.3\) in three frames at \((a,b)=(1.92,1.0)\) (imaginary parts \(1.05\)--\(1.28\))
   ```
   - New:
   ```
   its real part is about \(1.05\), \(1.58\), \(0.27\) in three Lorentz frames of \(F\) at \((a,b)=(0.7,1.3)\) (data \(\kappa,\alpha,y\) rotated, \(A\) fixed; imaginary parts between \(-1.52\) and \(-1.00\)), and \(0.31\), \(-1.40\), \(0.03\) in three frames at \((a,b)=(1.92,1.0)\) (imaginary parts between \(-0.15\) and \(0.08\))
   ```

4. **Edit 3** (same paragraph, frame spread). This is the only departure from `merged_edits.md`. Replace exactly:
   - Old:
   ```
   the real part varies between frames by roughly \(20\%\)
   ```
   - New:
   ```
   the real part varies between frames by an amount of the order of, or larger than, the magnitude of its mean
   ```

The tweak to Edit 3 is mine and needs no new physics. No integrator action is needed beyond applying the strings verbatim and a build check. The unchanged statements are: the Maxwell-part percentages in 032, the flux-independent A of the logarithm, and 034's "eigenvalues of both signs in every case (as has A)" for the tetrad part.
