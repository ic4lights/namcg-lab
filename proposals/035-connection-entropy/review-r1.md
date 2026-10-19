VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The bounded, conditional computations are sound and correctly hedged. Two wording fixes are needed in the insert (a hypothesis made explicit, and the "Euler" label scoped to the fit basis). A third item is a request to flag the extension of the cone rule. No label changes and no emergence issue.

## Source reading
Digest plus targeted reads. The digest is stale (`dirty-chapters`), as expected from the 032/033 integrations. I did not do a full scan. Ordinal 32 is not a 5th item, the block changes no scope statement, and I found no PRIOR-CLAIM-ERROR.

I read in full:
- the proposal;
- `appH_insert.tex`;
- all five scripts and their outputs;
- appH lines 255–275, the end of the 033 block and the anchor.

I did not re-read Chapter 17 and the rest of Problem B in full. The status quoted below is from the proposal and the 033 context, with no discrepancy seen.

## Claim under review
Problem B (sec:status-B). Quoted status: "Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL". Original target: tensor-block stationarity and the area/G relation. The proposal claims a bounded obstruction and classification only.

## Checks performed

**Anchor and encoding (point 4).**
- `\section{Problem C: conformal mode and Cassini}` occurs once, at line 275.
- It is preceded by a blank line and the end of the 033 paragraph (the second "Problem~B stays open…" occurrence). The proposed point (after the 033 block, before `\section{Problem C…}`) is therefore correct.
- I found 0 TAB characters in the insert and in appH.
- There are no corrupted escapes. The insert is ASCII, with LF endings that the integrator must convert to CRLF.
- The insert adds no labels, refs or cites.
- The status sentence appears once, at the end of the block.

**Scripts re-run (points 1–3).**
- `metric_delta_pairing.py` gives gap(1,0) = 2−n_D for both chiralities.
  - It gives an N_tot coefficient of c_a/10 − c_b/15 − 1/10, which is −c_b/15 at c_a=1.
  - It gives a κ_X coefficient of 4−2c_a+2c_b (SD) and 4−2c_a−2c_b (ASD).
  - These match the insert: 2κ_X(1±c_b) with −N_tot c_b/15.
- `pairing_modes.py`:
  - SD: tr(J_12Ω_12) = −2W+R_Σ and tr(J_34Ω_12) = +2W−R_Σ.
  - ASD: tr(J_34Ω_12) = −2W+R_Σ.
  - So H = J_12 − χJ_34 gives −4W+2R_Σ for both chiralities.
  - J_13 and the other generators have no (W,R_Σ) fit, so they are excluded by equivariance as stated.
  - J_12 alone gives −2W, confirming that the Lorentz-tied charge assigns −2κ_X to W.
- `diag_family_holonomy.py` runs and gives:
  - R_1212 delta = −2 L_a e^{2l1};
  - R_{a3a3} and R_{a4a4} deltas = −L_b e^{2l2};
  - R_3434 delta = 0;
  - the Ω_12 matrix.
  - These match the claimed H and Riemann deltas.
- `tau_decomposition.py`: on the 17 totally geodesic points the fit is rank 5 with coefficients (−2,1,2/3,1/2,−4). On the three non-totally-geodesic points the system is inconsistent, as expected. This agrees with τ_Ω = R_Σ − 2W + (a_1^v − X′/2) once a_1^v = 2R/3 − 4e + X′.
  - The independent evidence is thinner than "17 points" suggests: 11 of the points are one rotation-invariant SD family, and the non-SD J=0 points come in identical pairs.
  - The insert's "not proved" wording is adequate.

**Literature (point 1).**
- arXiv:1507.01054 exists. Authors and title: Jacobson–Mohd, "Black hole entropy and Lorentz-diffeomorphism Noether charge". Its abstract confirms the combined diffeo+Lorentz charge and the regular-frame argument.
- arXiv:2012.14892 exists: Elgood–Ortín–Pereñíguez. The abstract confirms momentum maps and a Lorentz/gauge-invariant Wald formula.
- Neither paper was opened at the equation level. The equation numbers (46–49, 6.1, 6.2, 7.3) remain not independently verified.
- The insert cites neither paper and states its charge construction as "if … tied … through a regular frame". It does not depend on the equation numbers, so this is acceptable.

## Findings

1. **Minor, major in effect for hedging. B-R1 hypothesis.**
   - Location: the insert, first paragraph, "If the internal group is not tied to the frame, the charge vanishes at the bifurcation surface".
   - Finding: the vanishing needs the momentum map to vanish. That in turn needs a regular connection with no Chern–Simons term and L_ξ A = 0 with Ψ = 0 at ξ = 0. This is exactly the point the Elgood et al. formalism makes non-trivial. The proposal asserts it as "standard" but did not check the equations.
   - Required action: add "for a regular connection with vanishing momentum map" (or equivalent). The insert already attributes nothing to the literature.

2. **Minor. B-R3 basis dependence.**
   - Location: the insert, third paragraph, "The coefficient of the Euler density R_Σ … is therefore κ_X − N_tot/30" and "not Euler densities".
   - Finding: the split into R_Σ and (a_1, X′) is relative to the fit basis (W, R_Σ, R, e, X′). The claim that this coefficient is a-type, and the Chern–Weil statement, are conjectural. The insert wisely omits the Chern–Weil claim.
   - Required action: say "in the basis (W, R_Σ, R, e, X′) of the fit" and do not call the leftover densities "genuinely non-topological" beyond that basis.

3. **Minor. Extension to warp deltas.**
   - The insert says "with all deltas inserted in the cross term". It does not flag that this applies the cone rule beyond the cone, as the proposal's classification table does.
   - Required action: add "(an extension of the cross-term rule, not derived)".
   - Also state that the claim "metric induced on Σ singular at order ε" for c_b ≠ 0 is read off the delta structure and is not separately checked.

No fitting to the target: c_b is mapped, not tuned. No label is changed. Emergence is preserved: the independent connection is an auxiliary bookkeeping variable, and Θ-bar is the fundamental input, not a metric. The insert says "auxiliary independent field" but should make "bookkeeping" explicit (optional).

Point 3: merged 029/031/033 text is consistent with these results. In particular, 033's τ_Ω^(1) = −2W+R_Σ agrees with the decomposition at first order. The family-specific 029 proportionality is a scope clarification and not a PRIOR-CLAIM-ERROR. Note that the insert itself does not state it.

## Scope of what is established
- **Established algebra and symbolic results:**
  - The cross-term/Lorentz-Noether equivalence, assuming a tied frame.
  - The exact diagonal-family holonomy and Riemann deltas.
  - The pairing table on SD/ASD modes.
- **Conditional:**
  - The gap formula, which depends on applying the cross-term rule to the warp deltas.
  - The statement that no content-independent profile closes the gap. This holds in the diagonal family only (Θ^{12} = r^{−εc_a}, Θ^{34} = r^{−εc_b}), with the 033 hypotheses.
- **Numerical, not proved:** the τ_Ω decomposition at 17 totally geodesic points.
- **Unresolved:** which holonomy the matrix state selects; the T-side Euler coefficient.
- Problem B stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No label change.

Relaxations that could still favour the derivation, ranked:
1. Edge or contact terms of the connection sector contributing −2κ_X W (Donnelly–Wall type). This is the most promising: it directly supplies the missing piece.
2. Non-chiral Θ-bar and δρ ≠ 0 modes.
3. Off-diagonal equivariant Θ with Burgers/vortex-type deltas.
4. A smooth-cone replica instead of the cross-term rule (AB heat trace, n>1).
5. O(h²) Dong K² terms with contortion.
6. Finite-n/fixed-state versions.

## Recommended disposition
Revise the insert with the three wording fixes above, then integrate. Place it before `\section{Problem C…}`. No other change.

## Corrected snippet
Apply by substitution only; no new physics.
- In sentence 4 of paragraph 1: "…the charge vanishes at the bifurcation surface for a regular connection with vanishing momentum map, and the term is absent."
- In paragraph 2: "With all deltas inserted in the cross term of the weighted \(a_2\) (an extension of the cross-term rule beyond the cone, not derived), the gap …"
- In paragraph 3: "The coefficient of \(R_\Sigma\) in the basis \((W,R_\Sigma,R,e,X')\) of the fit is therefore …, and the remainder is a combination of the \(\Lambda^2\)-order densities \(a_1\) and \(X'\)."
