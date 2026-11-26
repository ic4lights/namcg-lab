VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The all-X supertrace lemma, the vanishing of the species constants for n ≤ 3, and the s² growth of the order-Z⁴ integrand all re-derive. The block has a sign error in the mass-linear term. It misstates the A-dependence of the flux (omits the first-order sin φ term). It uses an undefined K^{μν} and slightly overstates the "no EH form" scope. These need correction before integration.

## Source reading
Digest + targeted reads. `--check` printed DIGEST STALE, which is expected with the uncommitted appH. Only appH is dirty, so under CLAUDE.md 3(d) I read the affected passages directly. No file was unreadable.
- Read in full: proposal-r1.md, block-r1.tex, all scripts and outputs in the folder.
- appH lines 2085-2129 (the 025/027 blocks and the 026 passage, lines 215-240), the Problem F entry context, K^{μν} at line 1913, and ledger entries 024-027.
- Not a full scan: ordinal 26 is not a cadence item and no definition or status changes.

## Claim under review
Within the CP^{1,2} four-matrix class, every species operator has the form H_i = (−Box_X)⊗1 + Σ_i^{ab}⊗{F_ab,·} + m_i for arbitrary X. The weighted supertrace then cancels through n = 3 insertions of Z. The weight-two coefficient reduces to M_str times a first-jet moment. The order-Z⁴ term is non-expandable because its Schwinger integrand grows as s². The integrand is not Lorentz invariant.

Target statuses at the current criterion (Chapter 17: A, B, C, D1, E, F, G-derived, N). The verbatim quote is taken from the 027 review, which the proposal relies on; I did not independently re-read Appendix H for it.
- Problem F: "OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; 'treating G_eff as an input leaves F OPEN'".
- Problem E: OPEN, CRITICAL PATH for the matrix-derived label, PROGRAMME-CONDITIONAL.

No label is touched.

## Checks performed (direct unless stated)
- **Tensor lemma (point 1).** I wrote an independent script (scratchpad `chk.py`) using a different complex Dirac representation of Cl(3,1) and four copies of it.
  - Σ w d = 0.
  - Σ w tr(Z…Z) = 0 for n = 1, 2, 3, over all 12³ ordered tuples.
  - n = 4 gives 1.5, nonzero.
  - Flipping the relative sign of Z_D gives 2.0 at n = 3, so the n = 3 cancellation does depend on Z_D = −Σ_D with Z_V = −Σ_V. This agrees with the proposal.
  - The Dirac to vector trace ratio is ½.
  - The structural reason: Σ_V and Σ_D carry the same Lie algebra (both +rhs), the symmetric cubic invariant is absent for so(3,1), and the antisymmetric part scales with the index ratio ½.
- **Operator identities (i)-(iii).** I re-ran `arbitrary_X_identities.py`: all True for random polynomial X.
- **Factorisation.** Σ_i acts on the species index and commutes with all operators, so each Duhamel term is a species constant times an operator trace with the same ordering. I verified this by reading the argument and by `duhamel_toy.py`.
  - The toy confirms c_0 = c_1 = c_3 ≈ 0.
  - It confirms c_2 = −M_str Tr[χe^{−H}] with M_str = −7.8 at the toy masses (4μ² + 6μ_i² with μ² = −3, μ_i² = 0.7).
  - M_str = −12 + 6μ_i² vanishes at μ_i² = 2.
  - Convergence is not claimed in the block. Good.
- **s² growth (point 3).**
  - I confirmed |C| = f_e² + f_m² and the kernel-plane flux is nonzero.
  - The integrand has log-slopes of 2.00 at the four tested points, in the `z4_large_s.py` output.
  - The heuristic matches: four non-kernel directions give det^{−1/2} ~ s^{−2}, and the s⁴ factor gives s².
  - The closed-form logarithm and its series −6(f_e² + f_m²)²/σ⁴ were checked numerically (ratio → −6).
  - The block states that the second variation of the logarithm is not computed. Good.
- **Hessian (point 2).** `mass_moment_stats.py` gives 5 positive, 14 negative and 40 indefinite out of 59 draws, which sums to 59. This is numerical and sampled at frozen coefficients, at φ = π/2.
- **Covariance (point 4).**
  - The ⟨λ²⟩ scan agrees with the block: the real part changes by a factor of 2.0 and the modulus by 2.4 over rapidity 1.2.
  - I did not re-derive the 2-180 ratio; it is integrand level, at one proper time, at κ = ¾.
  - Steinacker, arXiv 2303.08012 (key `Steinacker2023`, present in bib): I fetched the ar5iv text. Section 7.1.2 says "is not Lorentz invariant a priori, reflecting the presence of a time-like vector field on the FLRW space-time". Section 7.2.1 says "the latter is not Lorentz invariant, and should be suppressed to obtain a reasonable gravity theory". These match the proposal at section level. Equation numbers were not re-checked.
  - Visser gr-qc/0204062 (Mod. Phys. Lett. A17, 977): eq. 21 is 1/G = 1/G₀ − (1/2π) str[k₁κ² − k₁m² ln(κ²/m²)]; eq. 33 is str(I) = str(m²) = str(m⁴) = 0; eq. 35 is str(k₁) = str(k₁m²) = 0; eq. 36 is 1/G = 1/G₀ − (1/2π) str[k₁m² ln(m²/μ²)].
  - The block cites neither paper, so nothing in the LaTeX is overstated on this point.
- **Consistency with merged text (point 5).**
  - 026: weighted a₁ = 0, a₂ = ½𝒮₄, and the mass insertion −m_i a₁^{(i)} are consistent with the block's n ≤ 3 statement and its M_str and c₁₂ constants.
  - 027: the remainder −(4μ² + n_ex μ_i²) j(a) is consistent.
  - No merged sentence becomes false. No PRIOR-CLAIM-ERROR, so no 3(c) scan.
- **Anchor and bib (point 7).**
  - `\section{Problem G: HBEV}` occurs once, at line 2130, directly after the 027 block, whose last sentence is "Problem~F remains open".
  - The label `ch:vierbein-emergence` exists.
  - There is no bib change. The compile check reports 0 errors, 0 undefined and 0 multiply-defined, 289 pages. I did not rebuild.

## Findings

1. **Major. Sign error in the mass-linear term.**
   - Location: block, Species sums ("the term linear in the masses is −M_str Tr[χΦ′(H_X)]") and Consequences (ii) ("−M_str∫χ(σ_X−i0)^{−1}").
   - Finding: m is a scalar, so the first-order term is exactly +M_str Tr[χΦ′(H_X)]. The toy script uses Φ = exp(−·), for which Φ′ = −exp(−·) and c_2 = −M_str Tr[χe^{−H}]. This contradicts the block's literal formula.
   - Finding: with the 027 convention Σln = −∫ds/s Tr e^{−is(H−iε)}, Φ′(H) = 1/(H−i0). The leading-symbol term is therefore +M_str∫χ(σ_X−i0)^{−1}. The minus sign in 027's "−(4μ²+n_ex μ_i²) j(a)" belongs to its Q-convention, where Σln = −(4π)^{−2}Λ²Q, so the contribution to Σln is +M_str·j. The block's (ii) mixes the two conventions.
   - Also: "the term linear in the masses" must read "without Z insertions". Terms linear in m with two Z insertions are the nonzero c₁₂, which the block lists separately.
   - Required action: state +M_str Tr[χΦ′(H_X)], or state the result for Φ = e^{−(·)} (−M_str Tr[χe^{−H_X}]). In (ii), either state the sign consistently with the 027 convention or write "proportional to M_str with the moment ∫χ(σ_X−i0)^{−1}". The block should claim no sign of G_eff in any case.

2. **Major. Flux shift: "enters only through" is false as stated.**
   - Location: Consequences (iii).
   - Finding: the proposal's own formula gives Ham(F^{ab}) = s c_ab + ε s(α^a q^b − α^b q^a)[sin φ Ham(M^{45}) + m cos φ Y_q]. The sin φ Ham(M^{45}) term is first order in q and is the larger term at general phase. The cos term is second order in q.
   - Finding: the analysis in `lorentz_diag.py` is consistent only at the phase φ = 0 (sin φ = 0). There W is unshifted, the Gaussian prefactor is unshifted and F is exactly linear in ε, because {cos φ, cos φ} = 0. That is a legitimate way to isolate the second-jet (∂h)²-type term, but it is not stated.
   - Required action: state that the shift F → F⁰ + εc(ξ·Y_q)(q_aα_b − q_bα_a), c = −s y⁴ cos φ, holds at the phase φ = 0 where the first-jet terms vanish. Drop "only through ... at the leading order in q", or add the sin φ term.

3. **Major. Undefined K^{μν} and scope of "no EH form".**
   - Location: Consequences (ii).
   - Finding: K^{μν} is defined only in the earlier Θ-class paragraph (line 1913), not in this CP^{1,2} setting, and the map from A to δK is not established here. The phrase "no term with more than one derivative of A" is also wrong as worded: a second variation of a function of the first jet has ∂A∂A.
   - Finding: the "no EH form" statement holds only for the leading-symbol term. The M_str term at the next-to-leading symbol involves the second jet of X and can contain EH-form pieces. The block's closing paragraph says the EH-form dependence is "not computed", which sits in tension with (ii)'s "none of Einstein–Hilbert form".
   - Required action: say "this leading-symbol term depends on A only through its first derivatives, so its second variation has no second-derivative term; the next-to-leading symbol, which involves the second jet, is not computed". State the reading of the metric fluctuation as a hypothesis ("if the metric fluctuation is taken to be built from the first jet of A; not established here"), or drop the K^{μν} language. The proposal summary item 2 ("exactly zero for every A") must carry the same restriction: it is exact only for the count, spin and cubic terms.

4. **Minor. Covariance wording.**
   - Location: Consequences (iii).
   - The dependence of ⟨(ξ·Y_q)²⟩ on q·y does not involve the flux at all. It involves only the window, the background point and Y_q. "Through the vector y^μ and the background flux" is therefore not shown for that quantity.
   - The block should say that the integrand of the order-F⁴ term at fixed proper time (θ = π/2 − 0.35) and κ = ¾ depends on q·y at fixed q·q, through y^μ and the window. Both the window and the FLRW-type leaf single out y^μ, so the diagnostic does not separate them.
   - The "2 to 180" ratio compares norms of different tensors and belongs in the proposal only.
   - "This term is not Lorentz invariant" should be "its integrand". The term has no finite coefficient, as (iv) says.
   - The "same type as Steinacker" remark is in the proposal only; keep it out of the LaTeX.

5. **Minor. Hessian wording.**
   - Specify that the Hessian is of the real (principal-value) part of the mass moment, and that it is numerical and sampled at frozen coefficients at φ = π/2.
   - Replace "because the window is not gauge invariant" by "numerically nonzero in all draws". The reason is unverified: constant α ∝ q is only gauge-like at frozen m(y).

6. **Minor, proposal only.** Visser's k₁ differs by species (his Table 1: ⅙ for a minimal scalar, −⅓ for a Dirac spinor). M_str ∝ str(m²) is Visser's eq. 33, not eq. 35 "with k₁ equal for all components". Do not carry that sentence into any text.

## Scope of what is established
- **Established (exact algebra, formal expansion):** the all-X species form H_i, the tensor identities T_0 = … = T_3 = 0 (T_4 ≠ 0), the factorisation lemma, and the identification of the first nonvanishing species constants. These are M_str; Σ w d m²; c₁₂ (the vector mass times tr ΣΣ); and T_4. Convergence is not claimed.
- **Established (leading symbol, within the class):** the weight-two term depends on A only through the first jet.
- **Numerical only:** the Hessian indefiniteness, the s² growth at four points, and the integrand-level q·y dependence.
- **Not established:**
  - any EH-form coefficient or sign;
  - the next-to-leading symbol;
  - the second variation of the logarithm;
  - the map from A to the metric fluctuation;
  - the finite Lorentzian meaning of the F⁴ term.
- **Hypothesis class of the no-go:**
  - Poisson limit, one loop, leading symbol;
  - the leaf CP^{1,2} four-matrix class with μ² = −3;
  - transverse matrices vanishing;
  - the supplied 16-component fermion content with no bilinear mass;
  - a species-independent window χ(Δ_κ) built from the fixed T;
  - the formal Duhamel expansion.
- **Problems E and F remain OPEN, PROGRAMME-CONDITIONAL.** Nothing is DERIVED, no label change, no sign of G_eff. Spacetime stays emergent and there is no Wick-rotation claim.
- **Open avenues, ranked:**
  1. Nilpotent (Landau) resummation of the non-expanded logarithm: finite, hypoelliptic, and the direct route to an F⁴ constant. This relaxes the Schwinger expansion.
  2. Next-to-leading symbol of the M_str term on the six-dimensional leaf (R/6 + E structure). This is the only place an EH-form piece can enter in this class, and it relaxes "leading symbol".
  3. Fermion mass patterns (scalar m_F or matrix bilinears). These break T_2 = 0 and relax "no bilinear mass".
  4. Transverse flux or fuzzy K, with the mixed invariant. This relaxes "transverse matrices vanishing".
  5. Species- or A-dependent windows. This relaxes the common window and breaks the lemma.
  6. Eight-matrix sets and Moyal terms.

## Recommended disposition
Revise findings 1-3 (required) and 4-5 (wording), then re-review. Significance is adequate for a bounded no-go: an exact lemma that sharpens 026 and 027 and removes three candidate sources of an EH term. The package is coherent and not separable.

## Corrected snippet (no new physics)
- In Species sums, replace "the term linear in the masses is −M_str Tr[χ Φ′(H_X)]" with "the term linear in the masses and without insertions of 𝒵 is \(+M_{\mathrm{str}}\operatorname{Tr}[\chi\,\Phi'(H_X)]\) (for \(\Phi=e^{-(\cdot)}\) this is \(-M_{\mathrm{str}}\operatorname{Tr}[\chi e^{-H_X}]\))".
- In (ii), replace "At the leading symbol that term is −M_str∫χ(σ_X−i0)^{−1} …" with "At the leading symbol that term is proportional to \(M_{\mathrm{str}}\int\chi\,(\sigma_X-\mathrm i0)^{-1}\) …". Then replace "Its second variation therefore contains no term with more than one derivative of A, that is, in the reading … none of Einstein–Hilbert form" with "This leading-symbol term depends on \(A\) only through its first derivatives, so its second variation contains no second derivative of the fluctuation and no term of Einstein–Hilbert form; the next-to-leading symbol, which involves the second jet of \(X\), is not computed."
- In (iii), qualify the flux shift with "at the phase \(\phi=0\), where the first-jet terms vanish". Replace "through the vector y^μ and the background flux" with "at the integrand level, at fixed proper time, through the vector \(y^\mu\) and the window".

Extra assumption in the corrected snippet: φ = 0 is the evaluation phase, which is the proposal's own implicit choice.
