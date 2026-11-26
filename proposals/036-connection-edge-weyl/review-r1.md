VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: first | OPEN: 0/2

## Verdict
The bounded no-go and the correction of 035 are mathematically sound, and the DW reading is correctly hedged. Two wording revisions are required before integration. The insert must record the undecided comparator, and the 035 replacement clause must be reworded so that it states the convention and reads correctly.

## Source reading
Digest plus targeted reads. `make_digest.py --check` printed DIGEST STALE, and chapters are dirty (032, 033, 035 uncommitted, expected). I did not read every chapter file.

Read directly:
- the whole proposal and `appH_insert.tex`;
- `chapters/appH-microscopic-proofs.tex` lines 38-48 (Problem B label), 248-282 (031/033/035 blocks) and the anchor at 282;
- the 035 proposal and reviews (grep), and the 035 scripts `metric_delta_pairing.py` and `diag_family_holonomy.py`;
- `reports/ledger.md` tail;
- DW arXiv:1506.05792, PDF pages 1-3 and 29-36 (title, abstract, contents, Sec. VII, Eqs. 83-98, Sec. VIII).

For the PRIOR-CLAIM-ERROR scan I grepped all `chapters/*.tex` for `c_b`, `anti-self-dual one`, `\mathcal J_{34}`, `kappa_X` and `sec:status-B`.
- The affected formula occurs only at appH line 278.
- `appG-sector-entropy.tex` only references `sec:status-B`.
- This is a symbol-level scan, not a full read of every chapter. The correction changes one formula, not a definition, scope or status passage, so I judge 3(c) not strictly triggered. I applied 3(d) by reading the affected passages.

## Claim under review
036 is a bounded no-go: edge and contact terms of the vector/connection sector do not supply the missing -2κ_X W of the completed Weyl gap 2κ_X (033), beyond the Lorentz-Noether contact of 035. It also corrects the ASD sentence of 035.

Appendix H, quoted verbatim for B (line 45 and the label block): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- A (line 16): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label."
- Chapter 17 requires A, B, C, D1, E, F, G-derived and N; H, I and J are optional.
- No label changes in the proposal.

## Checks performed
- **Anchor.** `\section{Problem C: conformal mode and Cassini}` occurs exactly once (line 282), immediately after the 035 block. The insert has 0 TAB characters, no `\label`, no `\ref`, and one `\cite{DonnellyWall2016}`. The key exists at `bib/namcg.bib:522`. The replaced 035 clause occurs once (line 278). The insert has one closing status sentence.
- **Re-run:** `diag_family_chirality.py`, `gap_profile.py`, `e_first_order.py`, `hodge_maxwell_check.py`, `hodge_vs_poisson.py`, `edge_weyl_fit.py`, `metric_delta_pairing.py` (035). All outputs match the proposal's quoted values.
- **Independent analytic check of the chirality sign.** The vector connection is built from M^{μν}_σ = 2Θ^{rσ}∂_rΘ^{μν} + A_s δ, with G, Γ and A_s independent of the sign s of Θ^{34}.
  - The (34) entries of ω are linear in s, and the (12) entries do not involve s.
  - So the J_34 component of Ω_12 carries s, giving H = c_a J_12 + χ c_b J_34 with c_b the exponent of |Θ^34|. This agrees with the script.
  - The metric deltas (c_a, c_b) are independent of s.
- **Scope.** The checks are exact-arithmetic at sampled jets and symbolic. They are not proofs for general classes.

## Decision on the possible PRIOR-CLAIM-ERROR (re-derived)
This is a genuine error in the merged 035 sentence, not only a convention difference. It is minor in effect: the qualitative conclusion is unchanged.

1. 035 defines the family by Θ^{12}=r^{-εc_a}, Θ^{34}=r^{-εc_b}, and finds H = c_a J_12 + c_b J_34. That is correct only for the positive Θ^{34} (self-dual) family.
2. The ASD gap in 035 comes from `metric_delta_pairing.py`. For ASD it uses c_b in two incompatible roles:
   - in the metric deltas and the N_tot coefficient, c_b is the exponent of |Θ^34|;
   - in the κ_X coefficient (4 − 2c_a − 2c_b), c_b is the J_34 coefficient of H.
3. In the ASD family these differ by χ = −1. The consistent result, as a function of the exponent c_b, is N_tot(3c_a − 2c_b − 3)/30 + 2κ_X(2 − c_a + c_b), the same as SD. This is reproduced by the 036 script.
4. If c_b is instead read as the J_34 coefficient, the N_tot term would have to become +N_tot c_b/15. So "−N_tot c_b/15 + 2κ_X(1−c_b)" is wrong under either single-parameter reading.
5. Conclusions that survive:
   - "equals 2κ_X at c_b = 0";
   - "the κ_X part vanishes only for a holonomy of chirality opposite to Θ̄" (this is c_b = −χ in J_34 coefficient);
   - "no content-independent profile removes the gap in this family".
6. The ledger entry for 035 already writes (1 + χ c_b), i.e. the corrected form. The manuscript text is the only place with the error.

## Findings
1. **Major. Replacement clause (b).**
   - Location: the 036 replacement of the 035 ASD clause.
   - Finding: the proposed clause "...for which the holonomy is … if |Θ^{34}|=r^{-εc_b}" leaves the sentence's trailing ", and equals 2κ_X at c_b=0" with an unclear subject. It also does not say that the ASD family has Θ^{34}<0.
   - Required action: use the snippet below. The mathematics is confirmed.
2. **Major. Comparator not recorded.**
   - Location: insert, closing paragraph before the scope sentence.
   - Finding: the insert says that only a holonomy generator beyond J_12 attached to Σ has the required index property. That omits the alternative the proposal itself ranks first: the gap is relative to the metric-universal comparator 12κ_C^T (−4κ_X), whereas the Noether/Wald entropy in the variables (G, ω) assigns −2κ_X and equals the replica (035).
   - Assessment: the comparator question is genuinely open, not settled by this package. 033 already says the cross-term rule "does not fix the entropy of a part of the quadratic form carried by non-metric invariants … that part is the gap" and 035 states −2κ_X against −4κ_X. No merged statement is falsified. The insert should not read as if the gap could only be closed by a new contact.
   - Required action: add one sentence after "...singular metric on Σ", for example: "The gap is also relative to the comparator \(12\kappa_C^T\) assigned to \(\operatorname{tr}\Omega^2\) by the metric-universal rule; whether the entropy of this non-metric term is that value or the Noether value \(-2\kappa_X\) of the preceding paragraph, which equals the replica, is not decided here." No new physics is needed.
3. **Minor. Endomorphism sentence.**
   - Finding: "the antisymmetric part is a divergence of Θ^{ρσ}∂_ρΘ^{μν}" omits the reason it vanishes. The divergence is −Θ̄^{rn}∂_n∂_rδΘ − (∂_nΘ^{rn})∂_rΘ, whose first term vanishes by antisymmetry and whose second is second order.
   - Fix: "...a divergence of Θ^{ρσ}∂_ρΘ^{μν}, which vanishes at first order about constant Θ̄".
4. **Minor. DW wording.**
   - DW Sec. VIII explicitly leaves extrinsic geometry open. It does not mention Weyl dependence; its classes are B×F and S^1×H^3 (conformally flat).
   - Suggested: "that paper does not treat the dependence on the Weyl tensor, and leaves that on the extrinsic geometry open".
   - DW Eqs. 97-98 are verified: wrong-sign scalar, ⟨T^a_a⟩ = −R/24π, S_edge ~ (1/3) ln ε. The generalisation to a Σ-operator with Weyl-dependent data remains the proposal's hypothesis, and it is stated as one.
5. **Minor. "stated above".**
   - "the extended cross-term rule stated above" is not stated in this block. Replace with "of the preceding paragraph".

## Point-by-point on the scrutiny list
- **(1) Kabat-type contacts.** Verified in exact arithmetic on SD/ASD, generic and δρ=0 jets, two amplitudes. E_V = E_f = e·1 with zero symmetric-traceless and antisymmetric parts, and e = 0 for δρ=0. Hence tr(E_δ E^{(1)}) = e tr E_δ = 0 and R^{(1)} = 0. This holds for any E_δ and content at first order about constant Θ̄. It is sampled-jet evidence plus the analytic argument above, not a proof for all jet classes. It is correctly scoped.
- **(2) Donnelly–Wall edge modes.** Verified as above. The W-coefficient 0 of −R_Σ and the weight-Hessian argument reproduce. The potential argument (α+2β = κ_X/3 is content-dependent) is a characterisation, labelled as such. The "vector one edge scalar, Dirac none" premise is hedged with "if it carries…". No over-reading of DW.
- **(3) Holonomy contact.**
  - Gap formulas reproduced: raw N_tot(3c_a−2c_b−3)/30 + 2κ_X(2−c_a+c_b); Weyl-consistent (s−1)N_tot/10 − 2(s−2)κ_X.
  - Euler-combination W coefficient −2c_b and C·C′ = 2(c_a−c_b)W reproduced.
  - δρ=0 ⇔ c_b = −c_a holds for both chiralities (Pf Θ).
  - Hodge–Maxwell validation reproduced: W = 6/5, R_Σ = −31/15, gap 0, contact carrying 3 (−9/5 without). Consistent with the 62/12 ratios.
  - The endomorphism W = 3 is a machinery check, not a result for the matrix operator. The insert says so.
  - The extended rule and the Euler-W hypothesis are flagged as not derived.
- **(4) Comparator.** A genuine open fork. It does not change merged 033 or 035 statements, but it must be recorded (finding 2).
- **(5) Anchor, characters, bib, scope.** Verified as above. Emergence is untouched (no metric-fundamental claim). No labels are changed, and the closing line stays PROGRAMME-CONDITIONAL.

## Scope of what is established
- **Established (conditional, sampled jets).** On the 033 test modes, with a totally geodesic Σ, first order in 1−n, n<1, the completed replica, Poisson-limit one-loop operators and α=1:
  - endomorphism contacts have no W coefficient in the (G,ρ,∂Θ) presentation;
  - the diagonal-profile holonomy gap is chirality-independent in the exponent parametrisation, and no profile of the diagonal family closes it for all contents.
- **Conditional on a hypothesis.** The edge density is W-free only if the edge operator is the intrinsic abelian one of DW's classes.
- **Not derived.** The extended cross-term rule, the Euler-W dropping, and the "holonomy-type missing ingredient" conjecture.
- **Still open.** B and A: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No label change.
- **Open avenues, ranked.**
  1. The comparator: a second-order first law for the leaf action, with variation of both G and ω. This could turn the gap into a comparator artefact.
  2. Off-diagonal or equivariant profiles with a J_34 circulation and a regular Σ metric.
  3. The exact heat trace of the cone with holonomy, replacing the cross-term rule.
  4. The non-delta 1/r singular parts of ω and ln ρ.
  5. Edge algebra of the symplectic gauge group (non-abelian).
  6. Non-totally-geodesic Σ.
- **Hypotheses a within-core route could relax.** The cross-term rule (rank 1/3), the diagonal family (rank 2) and the comparator choice (rank 1).
- **Not a breakthrough.**

## Recommended disposition
Revise (findings 1 and 2 required, 3-5 minor), then integrate under ACCEPT. The ASD correction is part of the package and should be applied as the snippet below.

## Corrected snippet
Replacement for the 035 clause. The anchor occurs once: `and \(-N_{\mathrm{tot}}c_b/15+2\kappa_X(1-c_b)\) about an anti-self-dual one`.
```latex
and the same expression about an anti-self-dual one with \(\Theta^{34}=-r^{-\epsilon c_b}\), for which \(H=c_a\mathcal J_{12}-c_b\mathcal J_{34}\)
```
The sentence then continues unchanged, ", and equals \(2\kappa_X\) at \(c_b=0\)." No extra assumption is needed.

Insert addition (finding 2), placed in the closing paragraph after "...without a singular metric on \(\Sigma\).":
```latex
The gap is also relative to the comparator \(12\kappa_C^T\) assigned to \(\operatorname{tr}\Omega^2\) by the metric-universal rule; whether the entropy of this non-metric term is that value or the Noether value \(-2\kappa_X\) of the preceding paragraph, which equals the replica, is not decided here.
```
Apply the minor edits from findings 3-5 as stated.
