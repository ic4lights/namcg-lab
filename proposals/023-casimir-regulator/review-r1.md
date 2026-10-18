VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1

## Verdict
The algebra, pencil, window and compact results are reproduced, and the claim is correctly bounded. But the displayed symbol of Δ_κ has a sign error against the block's own convention for σ(·), and the eight-matrix sentence overreaches its sampling. Both are small fixes.

## Source reading
Digest + targeted reads. `make_digest.py --check` printed DIGEST STALE, which is expected given the dirty chapters.

Read in full:
- proposal-r1.md and block-r1.tex. The block is byte-identical to the proposal's block.
- The appH 022 paragraphs (lines 1995–2017) and the anchor region.
- The scripts and their outputs.

Not read: the SME scout report, which I did not open. No full scan was done. It is not due, because the block changes no scope, definition or status statement and I found no PRIOR-CLAIM-ERROR.

## Claim under review
- **Claim.** In the Poisson-limit, one-loop, leading-symbol, four-matrix class, a Casimir-type regulator can be built from C_42 and C_41. A function of C_42 alone cannot regulate. Δ_κ with 1/2<κ<1 is a conditional, added regulator. The negative direction is bounded, not removed. The package also records an exact compact spectrum and an eight-matrix (T, λη·y) fork.
- **Target.** Problem F, matrix-derived G_eff: sign and size from the one-loop trace. AppH wording, verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL." I did not re-read the Problem F ledger entry word for word, so the "Reduced-scope result" qualifier quoted in the proposal is not independently verified. E is the dependency.
- **Labels.** No label change is proposed.

## Checks performed (direct)
- **exact_algebra_P4.py**, both signs of the bracket:
  - μ² = −3.
  - Box = C_41 − C_31.
  - The linear fit has a unique solution with w = 0, giving H_V = C_G − C_41 − C_Σ + μ² for the correlated index-sign.
  - [C_42, H_V] = [C_41, H_V] = 0.
  - C_42 − C_41 = −Σ_{A≤4} η_AA (J^{A5})².
  - Centrality of C_42 and C_41's commutation with so(4,1) give the commutations by structure. C_G, C_Σ and C_41 mutually commute, so H_V commutes with C_41 and C_42.
  - The ghost operator −Box = C_31 − C_41 commutes as well.
- **sym_pencil.py:** the pencil eigenvalues are 1/2 (×4) and 1 (×2), deviation 2.7e-13 over 30 points. The signature of C_42 and C_41 is (2,4) (sym_signatures.out). The K_41 − κK_42 scan is positive definite for κ = 0.55, 0.75, 0.95 and 0.999, degenerate at 0.5 and 1, and indefinite outside. So the positive interval is 1/2 < κ < 1. The positive combination is A_κ = K_41 − κK_42 = α(κ−1/2)q_b + β(1−κ)q_f, where K_i denotes the quadratic form σ(C_i) as the block defines it.
- **window_local.py, re-run:**
  - Generalised eigenvalues of (K_H, A_{3/4}): −2 at all 8 points, two zeros, and three positive values that grow with (y⁴)².
  - Window volume det^{-1/2} equals the closed form [(κ−1/2)²(1−κ)]^{-1} at 5 values of κ.
  - d_* ranges over 1.72–5.55 at six points. This is numerical only, and it uses the non-commuting Euclid-contracted model. The block hedges it correctly.
  - The finite local window density follows because A_κ is positive definite, so the window is compact.
- **compact_exact.py, re-run:** formula versus dense diagonalisation, max difference 1.2e-13 for N = 1, 2, 3. The lowest eigenvalue is −(A+3) and the negative-mode counts are 38, 124, 344, 750. The mode-count identity 4·C(A+3,3)² matches. The 2.5e-3 fraction at A = 48 was not re-run, but extrapolates consistently from A = 24 and 32. The exponents are marked "not proved".
- **eight_stationarity.py:** bilinear coefficients λ−3 and 3λ−1, equal only at λ = −1 (common value −4).
- **sym_eight_scan.py:** (3,3) for λ ≤ −0.01, (5,1) at λ = 0.01, 0.1, 10, and degenerate (4,0,2) at λ = 1.
- **Anchor:** `\section{Problem G: HBEV}` occurs once, at appH line 2019, immediately after the 022 closing paragraph (line 2017). Both labels exist: `ch:vierbein-emergence` (ch04 line 2) and `ass:lorentzian` (ch04 line 322).
- **Build:** compile_check_r1 reports 0 errors, 0 undefined and 0 multiply-defined references. I did not re-run it.
- **Literature:** none cited in the block. The SME-scout claims were not independently verified.

## Findings

1. **Major (sign inconsistency).** Location: block, "Symbols" paragraph (the displayed σ(Δ_κ)), Consequences (ii)–(iv), and the Result item 4 summary.
   - **Finding.** The block defines σ(·) as the quadratic form Σ w(ξ·v)², the negative of the principal symbol. It also states σ(C_42) = −αq_b + βq_f and σ(C_41) = −(α/2)q_b + βq_f. By linearity, σ(κC_42 − C_41) = α(1/2−κ)q_b − β(1−κ)q_f, which is negative definite. The block displays the opposite sign, α(κ−1/2)q_b + β(1−κ)q_f, and calls it "positive definite".
   - **Reason.** The displayed formula is A_κ = K_41 − κK_42, the principal symbol of Δ_κ = κC_42 − C_41. That is the right object and the right operator: it is a positive operator in the −∂² sense, matching H_V = −Box + …. The operator choice is fine. The error is that the formula is labelled σ(Δ_κ) under a convention in which σ(Δ_κ) = −A_κ.
   - The same mismatch affects the window {σ(Δ_κ) ≤ Λ²} in (iii) and the pair (σ(Box), σ(Δ_{3/4})) in (iv). There σ(Box) is used as the form, which is correct for the principal symbol of H_V = −Box, while σ(Δ) is used as the principal symbol. The two entries of the pair therefore use opposite conventions.
   - **Required action.** Use −σ(Δ_κ) throughout where positivity is meant:
     - Displayed formula: −σ(Δ_κ) = α(κ−1/2)q_b + β(1−κ)q_f, the principal symbol of Δ_κ, positive definite exactly for 1/2<κ<1.
     - κ = 3/4: −σ(Δ_{3/4}) = ¼(αq_b + βq_f).
     - (ii): replace χ(σ(Δ_κ)/Λ²) with χ(−σ(Δ_κ)/Λ²).
     - (iii): window {−σ(Δ_κ) ≤ Λ²}.
     - (iv): "the generalised eigenvalues of (σ(Box), −σ(Δ_{3/4}))".
     - Optionally, say once that "symbol of H_V" means its principal symbol σ(Box).
   - **Interim wording.** Until a corrected block arrives, the integrated text would assert something false about the sign of σ(Δ_κ). The fix needs no new physics.

2. **Minor (overreach from sampling).** Location: "Eight matrices" paragraph, last sentence of the block, and Result item 7.
   - **Finding.** "A Lorentzian (5,1) induced form with no centre thus occurs for λ>0, λ≠1" rests on three sampled values (0.01, 0.1, 10). The sampling does not support it for all λ > 0.
   - **Reason.** It is also a 6-dimensional form on the leaf, not a statement about the emergent 4D signature.
   - **Required action.** Write "occurs at the sampled values λ = 0.01, 0.1, 10" and "signature (5,1)". Drop the word "Lorentzian", or write "of signature (5,1)". Keep "the Hessian is not examined" (already present) and the two-bilinear-coefficients statement.
   - **Check on the "no centre" claim.** It rests on horizontal rank 6, which the proposal states and I took from it without re-running. The rank-6 statement at λ = 1 also coexists with a degenerate rank-4 form there, as the block says.

3. **Minor.** The block says "the number of negative modes … falls to 2.5·10⁻³ at A=48", which is numerical (compact_scaling.py, not re-run). Add "numerically", or confine the claim to the stated exponents "(not proved)". This is already largely hedged.

## 022 text (C_42 symbol)
- The integrated 022 text says only that the full C_so(4,2) "has base symbol −2ℓ²g⁻¹". That is a base-block statement and is true: the base block of σ(C_42) is negative definite.
- It claims neither definiteness nor a Euclidean signature for the full 6D symbol. The words "Euclidean symbol" occur in 022 only in a different paragraph heading, about flux eigenvalues.
- The new block therefore sharpens a scope point. It is not a PRIOR-CLAIM-ERROR, so no M3 flag and no full scan.
- The five-matrix Box = C_41 − C_42 with base symbol ℓ²g⁻¹ in 022 is consistent with the pencil.

## Items checked as requested
- **Labelling.** The regulator is stated to be "an additional element of the regularisation and not derived from the action". It uses J^{A5}, outside U(so(4,1)'). No κ is singled out. κ = 3/4 is described only as a natural reference value, and the volume coefficient diverges at both ends.
- **Negative direction.**
  - The window symbol of H_V has a point-independent lower bound (−2 in these units) but is negative on part of the window, so e^{-sH_V} still grows at large s. This is correctly said to be bounded, not removed.
  - The Zeeman bound is hedged as a numerical estimate at six points.
  - The compact formula and counts are verified for N ≤ 3 and exact from the formula. The branching derivation is not written out, and the block says only "checked".
- **Emergence and signature.** No Wick rotation and no Euclidean-to-Lorentzian transfer is asserted. The block states that it does not derive a signature, does not identify an induced metric with the emergent metric, and leaves Assumption `ass:lorentzian` in place.
- **Anchor.** Unique and after the 022 block.

## Scope of what is established
- **Established (exact algebra):** the four-matrix relations H_V = C_G − C_41 − C_Σ + μ² with w = 0, Box = C_41 − C_31, the identity for C_42 − C_41, and the commutations by centrality. The coefficient claim is exact as a polynomial-algebra statement, and I verified it in the script.
- **Numerical, structured:** σ(C_42) has signature (2,4), the pencil is (1/2, 1), and the positive window for 1/2<κ<1 holds on sampled points. The volume dependence follows from the pencil.
- **Conditional:**
  - No function of C_42 alone regulates the leading-symbol trace. Hypotheses: Poisson limit, leading symbol, local density, compactly supported χ, with H_V and Box built from J^{ab}, J^{a4}.
  - Δ_κ gives a finite window density and confines ζ, at the leading symbol and as an added regulator.
- **Open:** sign and size of w; the weight-two coefficient and its A-dependence; the Lorentzian i-ε treatment; fermions; Moyal terms; subleading symbol; any physical fixing of κ.
- **Status:** PROGRAMME-CONDITIONAL. Problem F stays OPEN. E is not bridged.

**Open avenues, ranked by promise for the infrared and full-GR derivation (for the loop to follow):**
1. The Lorentzian i-ε Schwinger trace Tr[e^{-isH_V} χ(Δ_κ/Λ²)] in the finite window. The window is now compact and Δ_κ commutes with H_V, so the weight-two coefficient is computable at the leading symbol.
2. Fix κ by a matrix-intrinsic fibre admissibility condition (compact fuzzy fibre / spin cutoff), which would remove the κ-dependence of the leading coefficient.
3. The exact so(4,1) harmonic analysis of H_V on normalisable states.
4. The Hessian of the eight-matrix λ>0 set, which has two independent bilinear coefficients and a nondegenerate (5,1) form with no centre; the Hessian is the missing check.
5. Fermions.

The hypothesis a within-core route could relax is "regulator is a function of Box_X". It is relaxed here to a function of (C_42, C_41).

## Recommended disposition
Revise, then integrate: apply Finding 1 (required) and Findings 2 and 3 (minor), then re-verify the build. Not a breakthrough; routine bounded result.

## Corrected snippet
Changes to the block (no new physics; the only addition is the explicit "−" sign):

```latex
\Delta_\kappa=\kappa\,C_{42}-C_{41},\qquad -\sigma(\Delta_\kappa)=\alpha(\kappa-\tfrac12)q_b+\beta(1-\kappa)q_f ,
```
followed by: "which is, as the principal symbol of \(\Delta_\kappa\), positive definite exactly for \(\tfrac12<\kappa<1\) …; the value \(\kappa=\tfrac34\) gives \(-\sigma(\Delta_{3/4})=\tfrac14(\alpha q_b+\beta q_f)\), the absolute value of \(\sigma(C_{42})\) in the splitting."

In Consequences (ii)–(iv): replace \(\chi(\sigma(\Delta_\kappa)/\LUV^2)\) with \(\chi(-\sigma(\Delta_\kappa)/\LUV^2)\); replace the window by \(\{-\sigma(\Delta_\kappa)\le\LUV^2\}\); and replace \((\sigma(\Box),\sigma(\Delta_{3/4}))\) with \((\sigma(\Box),-\sigma(\Delta_{3/4}))\).

Eight matrices, last sentence: "A \((5,1)\) induced form with no centre variable thus occurs at the sampled values \(\lambda=0.01,0.1,10\), and requires two independent bilinear coefficients; the Hessian of that set is not examined."

Relevant files:
- C:\Users\redgi\Projects\namcg-lab\proposals\023-casimir-regulator\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\proposals\023-casimir-regulator\block-r1.tex
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (lines 1995–2019)
