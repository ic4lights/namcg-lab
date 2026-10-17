VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The core calculations hold up. I re-derived the invariant-sector first correction independently, reproduced Q(a), and checked the paper citations. The block as written misstates three things against the merged text and the paper: the density normalisation, the scheme-dependence of the sign change of Re Q, and the relation of the cone/fibre window to 023. These are wording corrections that need no new physics.

## Source reading
- Digest + targeted reads. `make_digest.py --check` printed DIGEST STALE, and `dirty-chapters: yes` is expected (the 024 integration in sec:status-B).
- I read directly in full:
  - proposal-r1.md and block-r1.tex;
  - the appH 022 and 023 blocks (lines 2017-2059), the anchor at line 2061, and the sec:status-E and sec:status-F ledger paragraphs;
  - the merged 018 passage at line 2002;
  - the script outputs;
  - the R-F2 entry of the SME scout.
- I opened the PDFs of 1910.00839 (eqs 2.7, 2.9, 3.42-3.46, footnote 8) and 2502.02498 (eqs 65-70, footnote 4).
- This is not a full scan. No definition, assumption, status or label is changed, and the 5th-integration cadence does not apply (ordinal 23). No PRIOR-CLAIM-ERROR was found, so 3(c) is not triggered.

## Claim under review
- Claim: a bounded, conditional package on the conjugate-coordinate class. It covers fibre admissibility (R-F2), a Lorentzian iε Gaussian-window trace (R-F1/E1), and an exact invariant-sector check on ℝ×H³. It claims no sign of G_eff.
- Target: Problem F, coefficients A, B, C, and the sign and size of w. Appendix H says for F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL."
- Problem E is touched only as a comparison. Appendix H says for E: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- No label change is proposed, and I agree none is warranted.

## Checks performed
**Direct verification**
1. **Footnote 8 and the cone.**
   - The cone content of eq 3.44 is real. From (2.7), S² = 2C41 − C42, and (3.43), −C41 > 9/4 − S²/2, one gets −C42 > 9/2 in the paper's convention.
   - The footnote literally prints "C2[so(4,2)] > 9/2", without the minus. The block's "−C42 > 9/2" is therefore a derived form and not a quotation.
   - The footnote says only "it is plausible that those are precisely the principal series irreps of SO(4,2) in End(H_n). However, this will not be investigated." The block's "stated there as plausible, not proved" is accurate.
   - Sign relation C^here = −C^there: I checked the chain operator positivity → principal symbol −σ ≥ 0. It is consistent with 023's convention that the principal symbol of Δ_κ is −σ(Δ_κ).
2. **Hypothesis class versus 023.** See Findings F1. The claim is not materially false.
3. **Compactness.**
   - With q_f ≤ Q, any upper cutoff αq_b − βq_f ≤ Λ² gives q_b ≤ (Λ² + βQ)/α, which is compact.
   - The cone is therefore not needed for compactness. The fibre bound does the work.
   - The fibre bound is a cutoff of S² = 2C41 − C42, so it is not "C42 alone".
4. **Citations.**
   - Keys Steinacker2019NoGhost and MantaSteinacker2025 exist in `bib/namcg.bib`.
   - 2502.02498 eq 70 reads "s ≲ m = r⁻¹x⁰".
   - Footnote 4 reads "This corrects some statements on the hs cutoff in previous works". The block's attribution is hedged and acceptable.
   - Eq 2.9 and the n+1-dimensional SU(2)_L representation of the lowest-weight state (line 257) support (a).
5. **Fibre radius.** `fibre_cutoff.out.txt` shows 10 points, with one of |L±| = 0 and the other equal to ℓ. This is consistent with the block, which hedges the (b)/(c) tension as "not reconciled here".
6. **Gaussian symbol.**
   - I checked (2π)⁻⁶π³Λ⁶ det(σ_W)^{-1/2} ∏(1+isΛ²λ_k)^{-1/2} = (4π)⁻³ ….
   - I checked (σ−i0)⁻¹ = i∫₀^∞ ds e^{−isσ}.
   - The isotropic closed form 2/(a+c) matches the numerics in `window_moments.out.txt`.
   - The 4000-sample positivity scan has minimum Re·√∏|λ| ≈ 1e−4 > 0. It is numerical only, and the block says so.
7. **Flux.**
   - The outputs show one real and one imaginary pair at all 32 samples, and tr F² = −F_abF^ab holds.
   - I(F) = b² − a² is negative at y4² = 0.005, 0.063, 0.367 and positive from 0.619 up. The "≲ 0.4" threshold is an interpolation.
   - A real 2-form in 3+1 dimensions generically has this structure.
   - Imaginary Zeeman eigenvalues give e^{±2sa} growth. Real ones give phases. The block states this correctly.
8. **Independent check of D1.**
   - I built the Laplace-type operator zΔ_H4 + wΔ_H3 with G^{ττ} = z and G^{ij} = (z sech²τ + w) ĥ^{ij}, and computed R/6 − ½∇·ω − ¼ω² symbolically.
   - It equals the researcher's D1(z,w,τ) at three random points to 15 digits.
   - D0 follows exactly from the √g ratio.
   - I also reproduced the pure-Box coefficient from a separate sympy computation with the opposite metric sign, and the sign flip works out. The coefficient is c_s = (5a² − 3)/(4a²).
9. **Q(a).** I recomputed Q at a = 0.5, 1, 2 with mpmath on two different rotated contours (−π/4 and −π/6). Both give identical values, e.g. 1.11371 + 3.0i at a = 1. This confirms the contour-independence of the computation given the subtraction at x = 1.
10. **Anchor.**
    - `\section{Problem G: HBEV}` occurs once, at line 2061, immediately after the 023 block, which ends "…Problem~F remains open."
    - `\LUV` is defined at `namcg-book7.tex:54`. `ch:vierbein-emergence` and `ass:lorentzian` exist.
    - No new labels or bib entries are needed.
    - I did not re-run `build_check.py`. I only read `compile_check_r1.out.txt`, which reports 0 errors and 0 undefined references on a scratch copy.

**Not verified**
- The positivity of the mass moment beyond the 4000 samples.
- The kernel-of-σ(Box) statement beyond 8 points.
- 2405.09804 and 2411.02598, which the proposal itself marks unverified.
- That a smoothing multiplier of the quantisation map is a function of the Casimirs, which the proposal itself calls an expectation.

## Findings

**F1 (major). Location: "Admissible cone" paragraph; scope relative to the merged 023 block.**
- Finding: the block's content is a conditional relaxation of 023's hypothesis class. It does not make any merged sentence false.
  - 023 consequence (i) says "No function of C42 alone is an elliptic regulator…". That remains true as stated: no fibre bound, no cone.
  - 025 adds a fibre bound βq_f ≤ Q. That bound is a cutoff of S² = 2C41 − C42, so the regulator is a function of (C41, C42). This is the 023 class of "functions of C42 and C41", not a counterexample to (i).
- Three problems in the block:
  - It never says that 023's no-go remains valid in its own hypothesis class.
  - It says "Δκ is not needed" and "the divergence of the window volume at the ends of the interval is absent", but all Lorentzian computations that follow use the Gaussian window of Δκ (κ = 3/4), whose fibre extent is ~Λ, not a fixed Q.
    - Those moments are therefore not computed for the cone/fibre-bounded window.
    - Only the κ→1 end is cured by the fibre bound. At κ→½ the "rescaling by 2κ−1" diverges instead.
  - The cone is not what regularises, as shown above.
- Required action:
  - State that 023 (i) stands for functions of C42 alone, and that the present statement adds the S² bound.
  - Say that the cone only restricts to the admissible sector and is not needed for compactness.
  - Say that the Lorentzian moments, flux and exact-sector results below are for the Δκ Gaussian and not for the fibre-bounded window.
  - Replace "the divergence … at the ends of the interval is absent" by a statement for the κ→1 end only. Alternatively drop "κ is not needed" in favour of "κ only rescales Λ² at fixed Q".

**F2 (major). Location: "Invariant sector, exactly".**
- Finding: the block says the pure-Box coefficient (5m²−3ℓ²)/(4m²) is "the formal density of the preceding paragraphs". The merged 018 text (appH line 2002) gives the density √|G|(R_G/6 − E) = (5m²−3ℓ²)/(4m⁶).
- Reason: these are consistent but not identical. For G^{μν} = m²η^{μν}, √|G_{μν}| = m⁻⁴. The scalar coefficient (5m²−3ℓ²)/(4m²) is the Seeley–DeWitt a₁, and the merged density is m⁻⁴ times it. My symbolic check confirms a₁ in the merged sign convention.
- Required action: write "the Seeley–DeWitt coefficient (5m²−3ℓ²)/(4m²), whose product with √|G| = m⁻⁴ is the density (5m²−3ℓ²)/(4m⁶) of the preceding paragraphs". The proposal's phrase "appendix density (5m²−3ℓ²)/(4m²)" must not be carried into the manuscript. The zero at a² = 3/5 is unaffected.

**F3 (major). Location: "Invariant sector, exactly", Re Q sign change at a ≃ 0.62.**
- Finding: the zero of Re Q depends on the subtraction convention. Q is defined with the mode-count term subtracted on the real axis over x < 1, and the remainder is −2 ln(μ²t) plus a constant. Changing the subtraction point to c shifts Q by 2 ln c, which moves the root.
- Required action: say that the location of the sign change is convention dependent and has no invariant meaning. Alternatively drop the numerical root and keep only that Re Q is indefinite in the chosen subtraction. The existing "plus … a scale-dependent logarithm" clause hedges the value but not the quoted root.
- Also state that the d₁(0) = R_{H⁴}/6 term is the curvature of the auxiliary window geometry (the mode-count term). That is one more reason this density is not a G_eff coefficient.

**F4 (minor). Location: "Fibre cutoffs".**
- The sentence "this is the sense of 'unbounded fibre' in the preceding paragraphs" quotes a phrase that does not occur in the merged appH text. The "unbounded fibre" wording comes from the SME scout. What the merged text says is "In the Poisson limit |ζ| is unbounded" and "the fibre … is compact, so ζ is expected to be bounded by the fibre harmonic number".
- "Equivalently the centre variable ζ" is also stronger than the merged text.
- Required action: remove the quoted phrase and attribution, and say "|ζ| is unbounded in the Poisson limit and expected to be bounded by the fibre harmonic number".

**F5 (minor). Location: "Admissible cone".**
- Write "equivalent, by (2.7) and (3.43), to −C42 > 9/2 in that convention (footnote 8 prints C2[so(4,2)] > 9/2)". The block should not read as quoting the paper.

**F6 (minor). Location: "Flux".**
- "ln det(σ+Z) … is finite" should read "has integrable logarithmic singularities at σ = ±2b". The factor σ² − 4b² vanishes on the real axis; the iε prescription makes it finite after integration.
- "Absent order by order in the flux … and for the magnetic pair" is fine. The block should add "at the leading symbol and at the sampled points".
- Complex Zeeman eigenvalues of an η-self-adjoint H_V are an instability-type feature. The block does not claim stability, which is correct.

## Scope of what is established
- **Proved or checked exactly.**
  - The invariant-sector first correction D₁(z,w,τ) is independently confirmed. The pure-Box coefficient equals the merged a₁.
  - The Gaussian symbol formula for Tr[χ e^{−is…}] at the leading symbol.
  - S² = 2C41 − C42 is vertical in 023's splitting. The algebra for compactness under a fibre bound holds.
- **Numerical at sampled points.**
  - The fibre radius |L| = ℓ at 10 points.
  - The flux eigenvalue structure and the sign change of F_abF^ab.
  - The positivity of the mass moment, and its ratio to the Euclid contraction (1.1–2.3×).
- **Conditional.** The admissible cone, which rests on footnote 8 of 1910.00839 (plausible, not proved), and the window as a regulator.
- **Unresolved.**
  - The vector, ghost and fibre second variation under A.
  - The F² term, which is indefinite on the leaf.
  - The mode-count constant, which cancels only if N_b = N_f.
  - The reconciliation of (b) s ≤ x⁰/r with (a) s ≤ n.
  - The covariance of the window (built from background M^{AB}).
- No sign of w or G_eff follows. The block makes no such claim, has no Wick-rotation claim, and keeps spacetime emergent. Problem F remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. Problem E is unchanged.
- This is not a no-go beyond its hypotheses: Poisson limit, one loop, leading symbol plus the invariant-sector weight-two term at A = 0, four-matrix class with μ² = −3, Gaussian Casimir window, bosonic.

**Open avenues, ranked**
1. Compute the Lorentzian moments in the fibre-bounded cone window (q_f ≤ Q), which this package does not do.
2. Exact SO(4,1) spin-1 (Plancherel or finite-N) trace extending the exact sector to vector and ghost.
3. Weyl second variation under A in the Gaussian window.
4. Supertrace/fermionic content to remove the mode-count term.
5. A window built from dynamical matrices only (exact finite-N trace).
6. Reconcile s ≤ n with s ≤ x⁰/r (T^i diagonal sphere versus SU(2)_L radius).
7. The eight-matrix (5,1) Hessian.
8. Moyal terms.

## Recommended disposition
Revise, then integrate. Once F1–F3 are corrected and F4–F6 tidied, no further evidence is needed. There is no `AUTHOR-DECISION` and no `LABEL-CHANGE-PROPOSED`. The package is coherent: one conditional window result, one flux structure and one exact check, all in the 023 class.

## Corrected snippet
Only these substitutions (no new physics, no extra assumptions):

- **Fibre cutoffs, first sentence.** Replace with: "In the Poisson limit the fibre of the leaf is a compact two-sphere and \(|\zeta|\) is unbounded; it is expected to be bounded by the fibre harmonic number of the quantum space."
- **Admissible cone, F1.** After "…so a function of the central operator \(C_{42}\) regularises once the fibre is bounded", insert: "The cone restricts to the admissible sector and is not what bounds the window; the bound \(\beta q_f\le Q\) is a cutoff of \(S^2=2C_{41}-C_{42}\), so this relaxes the hypothesis of the preceding paragraph and does not contradict it for functions of \(C_{42}\) alone. The Lorentzian results below are for the Gaussian window of \(\Delta_\kappa\), not for this window." Replace "the divergence of the window volume at the ends of the interval is absent" by "the divergence at \(\kappa\to1\) is absent".
- **Footnote clause.** "equivalent, by (2.7) and (3.43), to \(-C_{42}>9/2\) in that convention".
- **Invariant sector, F2.** "…the Seeley–DeWitt coefficient \((5m^2-3\ell^2)/(4m^2)\), whose product with \(\sqrt{|G|}=m^{-4}\) is the density \((5m^2-3\ell^2)/(4m^6)\) of the preceding paragraphs, obtained by an independent route."
- **Invariant sector, F3.** Replace "\(\operatorname{Re}Q\) changes sign at \(a\simeq0.62\) (not at …) and is positive above" by "\(\operatorname{Re}Q\) is indefinite; with the subtraction at \(x=1\) it changes sign at \(a\simeq0.62\) (not at \(a^2=\tfrac35\)), a location that moves with the subtraction point". Add that the mode-count term is the \(R/6\) curvature of the auxiliary \(H^4\) window geometry.
- **Flux.** "has integrable logarithmic singularities at \(\sigma=\pm2b\)".

Relevant files:
- C:\Users\redgi\Projects\namcg-lab\proposals\025-lorentzian-window\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\proposals\025-lorentzian-window\block-r1.tex
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex, lines 2002 and 2034-2061
- My checks (scratchpad):
  - C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\4d0177a0-6b3d-45ad-bb6d-645d2be99f00\scratchpad\d1chk.py
  - C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\4d0177a0-6b3d-45ad-bb6d-645d2be99f00\scratchpad\a1chk.py
  - C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\4d0177a0-6b3d-45ad-bb6d-645d2be99f00\scratchpad\qchk.py
