VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/4

## Verdict
The invariance classification and the Goldstone-extremised density are sound and reproducible, and no merged sentence becomes false. Four sentences in the block overstate or misstate (a false "half" factor, a V-notation clash, an unqualified "whole non-invariance" and "on the stationary set", and an under-stated status of the Stueckelberg dressing), so the text must be corrected before integration.

## Source reading
Digest plus targeted reads; this is not a full scan. The working tree is dirty with the accepted 038 block and bib entries, as expected. Per CLAUDE.md 3(d) I read the affected passages directly:
- appH L150-202 and L300-333: the normalisation paragraph, the fermionic-content and replica paragraphs, the 037 and 038 blocks, and the anchor.
- appH L497-526: the Problem D head.
- appH L708-716, L842-850 and L1040-1070: the passages on D2 and the compensating-field no-go.
- appH L2039-2047: the torsion-invariant paragraph.
- ch10 L60-270: Lorentz locking and Eq. dressed-omega.
- Ledger labels for A, B and D, and the Chapter 17 B and D openings (grep plus short context).

I did not read appH L202-300 or the rest of Chapter 17 in full. Prior reviews 037-r2 and 038-r1/r2 were not re-read; I relied on the merged text. No unreadable files.

## Claim under review
The claim concerns B's tensor-versus-area normalisation, with a bearing on D. Current ledger statuses, quoted verbatim:
- Problem B: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived." Chapter 17 reads "CRITICAL PATH; OPEN. The fixed-algebra first-law identity is established, but not the required stationarity."
- Problem D: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- Problem A: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

The Chapter 17 matrix-derived set is unchanged: A, B, C, D1, E, F, G-derived and N.

The claims are:
1. The rotation-invariant first-order densities are exactly span{𝒯, |∂lnρ|²}.
2. If one assumes a Stueckelberg dressing with tree-level stationarity of Λ, the Noether coefficient is r = −2, not −4.
3. The residue c_A − c_T^ext equals 2 for all content.

No label change is proposed.

## Checks performed
- **Scripts.** I re-ran s1, s2, s3, s4, s5 and s6; all outputs match the proposal.
  - s1: the finite-variation check of P agrees to 1e-8. The null space of the divergence map is exactly 2-dimensional (3 nonzero singular values of 5) in d = 3, 4 and both signatures, with residual below 1e-14 against span{𝒯, W²}.
  - s5: the exact rational solution is a1 = −a3/4, a2 = −a3/2.
  - s2: S² and 𝒯 equal 1/3 and 1/4 of X on the δρ = 0 modes. The identity X = 2𝒯 + (3/2)S² + 2V² holds to 1e-12. At the stationary point S² is about 1e-28 and X_ext/X = 0.5 to 6e-13. The Hessian signs are (12,0) Euclidean and (6,6) Lorentzian.
  - s4: the cone family has zero rotation equation. Generic Poisson-class jets give nonzero A[X] and A[𝒯] ≈ 1e-14.
  - s6: the composite connection equals the torsion 1-form, with residual 4e-16.
- **My own checks.**
  - Algebra: X = 2𝒯 + (3/2)S² + 2V². I derived it from 𝒯 = X/4 + TT′/2 − V² and the merged relation S² = (X − 2TT′)/3 (L2040). It holds exactly.
  - Koszul step: S = e_A∧de^A, the first-order amplitude satisfies p∧Ŝ = 0, and rotations shift it by p∧Φ with Φ an arbitrary 2-form. The image of p∧ is the kernel of p∧ for p ≠ 0, so S can be rotated away. A rotation shifts V orthogonally to p.
  - Euclidean Hessian: I derived analytically that it is 3/2|p∧Φ|² + 2|p·λ|². The kernel requires λ = p∧a with a ∝ p, hence λ = 0, so it is positive definite for p² ≠ 0. The Lorentzian (6,6) count is numerical only; the block says "in the cases tested".
  - Extension ambiguity (scratchpad `cls.py`): on random closed-ω 2-jets, in d = 4 and both signatures, the five invariants (TT, TT′, V², V·W, W²) have an exactly 2-dimensional null space. It equals span{V·(V−W), W·(V−W)}. So "multiples of V − ∂lnρ" is the complete class-vanishing ambiguity in this basis, and no such addition reaches the invariant span.
  - Residue arithmetic: c_A − c_T = 4κ_X + n_D = 4 − n_D. Then c_A − c_T^ext = 2κ_X + n_D = 2 for all n_D. With the holonomy contact it is 2 − α_vσ = 1 / 3, consistent with the merged table convention (3 / 5 before the dressing). At n_D = 0, 1/G_A − 1/G_T^ext = Λ²/π follows from the merged relation 1/G = cΛ²/2π.
  - Mechanics: 5588 bytes, 0 TAB, 0 CR, 0 non-ASCII and 0 control characters other than LF (checked with Python). Braces balance. \( and \) balance at 83 each. The only reference is \eqref{eq:dressed-omega}, unique at ch10 L133. \LUV is defined in the preamble. The anchor `\section{Problem C: conformal mode and Cassini}` occurs exactly once, after the 038 block. There are no labels, citations or process language. The block closes with one status sentence.
- **Not verified.** The Hayashi–Shirafuji uniqueness of TEGR among new-general-relativity Lagrangians (consistent with the result, but not re-read). Hessian signatures beyond the cases tested. Everything off the quadratic plane-wave class and the cone family.

## Findings

**F1 (major). Location: block, Noether paragraph, "half of the value 4−n_D before the dressing".**
- Finding: the reduction is by 2κ_X = 2 − n_D, not a factor 1/2. It is half only at n_D = 0 (4 → 2) and unchanged at n_D = 2 (2 → 2). The proposal's summary "halves the gap" has the same defect.
- Required action: replace as in the corrected snippet.

**F2 (major). Location: block, "Classification" sentence: "the whole non-invariance of κ_Xρ²X is the axial term".**
- Finding: this is exact only for the representative with V² replaced by |∂lnρ|². For X = T·T with V the torsion trace, the term 2(V² − |∂lnρ|²) vanishes on the class but is not rotation-invariant. Its variation −4V·δV is nonzero on class frames, and s1 and s4 measure A[X], not A[S²]. s4 shows A[X] ≠ A[S²] on generic class jets (for example 10.2 versus 6.0, 8.75 versus 3.66).
- Required action: qualify the sentence as in the snippet.

**F3 (major). Location: block, "Noether coefficient", first sentence: "On the stationary set the density depends on e only through G and ρ".**
- Finding: this is shown only at the plane-wave stationary points and on the cone family, where S = 0 and V = ∂lnρ. The rotation equation A[Λe] = 0 does not by itself imply S = 0 in general, and the block lists "the stationary set beyond the cone family" as not derived.
- Required action: restrict the sentence to those points, as in the snippet.

**F4 (major). Location: block, "Dressed density" first sentence.**
- Finding, status of the dressing:
  - Eq. dressed-omega dresses the spin connection ω_μ, not the coframe. The action e → Λe on the matrix-built coframe, and the form ρ²X[Λe] of the density, are stipulations, not consequences of Chapter 10.
  - In Chapter 10, Λ = 𝕀 is a gauge choice. The merged paragraph "A compensating field alone does not change the spectrum" (L1049-1062) records that the Stueckelberg gauge makes the action equal to the original. So, with e the Θ-built frame, the unitary gauge gives the undressed density. The result needs Λ treated as a field, with stationarity as an additional choice. The proposal's own H2 says frozen Λ = 1 returns the 038 indeterminacy, but the block does not say so.
- Required action: state the stipulation and the gauge point explicitly. This also keeps the block consistent with L1049-1062.

**F5 (minor). Location: block setting sentence.**
- Finding: it sets V_μ = ∂_μ lnρ, but the classification uses V_μV^μ and V^μ∂_μ lnρ as independent terms for a general coframe. The merged definition (L2040) is V_μ = G^{λν}T_{λμν}, equal to ∂_μ lnρ on the class.
- Required action: fix as in the snippet.

**F6 (minor). Location: block, "Hessian over the six rotation amplitudes".**
- Finding: this conflicts with "twelve real parameters" later in the sentence.
- Required action: change to "twelve real rotation amplitudes".

## Answers to the specific questions

1. **X identity and S → 0.**
   - The identity is re-derived. The dressing is an input from Chapter 10 / Assumption local-lorentz (see F4), not a derived output.
   - Given the stipulation, r = −2 follows without fiat. The stationary point has S = 0, X_ext = 2𝒯 + 2W², and 𝒯 ≃ −R, so the R coefficient is −2.
   - The two "routes" (the eigenvalue ratio 1/2 and the 𝒯 ≃ −R decomposition) are not independent: both use ⟨R⟩ = −X/4 = −𝒯 on the modes. They are a consistency check, which the block does not overclaim.
   - The selection of Λ by stationarity, rather than Λ = 𝕀, is a choice (F4 and H2).

2. **Consistency with 038.**
   - No merged sentence becomes false, so no PRIOR-CLAIM-ERROR.
     - "c_T = N_tot/6 − 4κ_X" and "c_W − c_T = κ_X(r+4)" are defined for the undressed density.
     - "r = −4 would match and is selected only by the match" and "undetermined until Problem D is settled" remain literally true, since Problem D is not settled. The new block conditionally narrows them.
     - "1/G_A − 1/G_T = 2Λ²/π" and "4 − n_D" stay valid for the undressed class.
   - c_T^ext = c_T + 2κ_X is consistent with the normalisation paragraph (L177). It is the eigenvalue −N_tot/24 + κ_X/2, which gives N_tot/6 − 2κ_X.
   - The new symbol c_T^ext is first defined in the block by its value. That is acceptable, since the value is tied to the half-eigenvalue statement in the preceding paragraph.
   - The merged text does not need an edit.

3. **Problem D.** The block makes no label change. It leaves D1 unaddressed and says so. After F4 is fixed it is consistent with the merged L1049-1062 no-go and with the D2 text at L842-850.

4. **2-D null direction and Hessian.**
   - Null direction: confirmed numerically (s1) and exactly at quadratic order (s5) for d = 3 and 4, both signatures. It is a known result (TEGR is the unique locally-Lorentz-invariant member of the family); the block does not claim novelty.
   - Hessian: the Euclidean positive definiteness is also proved analytically (above). The Lorentzian (6,6) count is numerical for the cases tested. The block's wording, "in the Lorentzian cases tested", is acceptable.

5. **Mechanics.** All pass (see Checks). The only issues are the wording items F1-F6.

6. **Breakthrough assessment.**
   - Not a breakthrough, in agreement with the researcher.
   - It is a conditional reduction on an assumed dressing. It narrows the gap from 4 − n_D to 2 and gives a target: a contact of modulus 2.
   - It derives no critical-path step and warrants no label change.

## Scope of what is established
- **Established, algebraic or numerical identity.**
  - The invariant span is {𝒯, W²}: exact at quadratic order, numerical at nonlinear order for d = 3, 4.
  - X = 2𝒯 + (3/2)S² + 2V².
  - The V − W ambiguity cannot reach the invariant span.
  - The Euclidean Hessian is positive definite.
- **Established numerically under hypotheses.**
  - At the plane-wave stationary point, S = 0 and X_ext/X = 1/2.
  - On the cone family, A = 0 and S = 0.
  - The Lorentzian Hessian is (6,6) in the cases tested.
- **Conditional, PROGRAMME-CONDITIONAL.**
  - r = −2, c_W = c_T^ext, and the residue 2 (1 / 3 with the vector holonomy contact). These hold given the dressing e → Λe, the form ρ²X[Λe], tree-level stationarity of Λ, constant Θ̄, the plane-wave Poisson class, the fixed-state replica and antiperiodic Dirac gluing.
- **Not derived.** The Stueckelberg field or local rotation symmetry from the matrix model; any contact of modulus 2; the entropy of the rigid compensating rotation; the replica or holonomy selected by the matrix state.
- **Status.** B, D and A remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.
- **No-go class.** "r = −4 is not selected by local-rotation symmetry" holds only within: Poisson limit, Λ² order, the dressing stipulation, tree-level stationarity, constant-Θ̄ plane waves and the cone family. It does not close the direction beyond these hypotheses.
- **Open avenues, ranked most promising first.**
  1. H1: a covariant bundle connection for the fluctuation operator. s6 shows the Poisson composite connection is the torsion 1-form, not a rotation connection, so a diagonal-covariant operator would remove X. This is the hypothesis a within-core route could relax.
  2. H5: a replica or holonomy contact of modulus 2, for example the dressed-bundle holonomy around Σ with the Goldstone rotation added.
  3. H2: the loop-level treatment of Λ, and the gauge versus field status of Λ (F4).
  4. H3: the nonlinear stationary set (whether S = 0 persists).
  5. H4: the fermion X-term under the same rotations.
  6. H6: the Lorentzian ghost-sign Goldstones (relevant to D).

## Recommended disposition
Revise, then integrate. The accepted text is `appH_insert.tex` with exactly the substitutions below and no others. After they are applied it needs only the integrator's mechanical re-check of braces and the build, no further review.

## Corrected snippet
Each item replaces the matching string verbatim. No new physics or assumptions beyond the explicitly stated input in item 5.

1. F5, setting sentence. Old: `\(V_\mu=\partial_\mu\ln\rho\), \(\mathcal T=` → New: `\(V_\mu=G^{\lambda\nu}T_{\lambda\mu\nu}\), equal to \(\partial_\mu\ln\rho\) on the Poisson class, \(\mathcal T=`.

2. F2. Old: `then shows that the whole non-invariance of \(\kappa_X\rho^2X\) is the axial term \(\tfrac32\kappa_X\rho^2S^2\); on generic` → New: `then shows that, with \(V_\mu V^\mu\) replaced by its class value \(\lvert\partial\ln\rho\rvert^2\), the non-invariance of \(\kappa_X\rho^2X\) is the axial term \(\tfrac32\kappa_X\rho^2S^2\) (the difference \(2(V_\mu V^\mu-\lvert\partial\ln\rho\rvert^2)\) vanishes on the class but is not invariant); on generic`.

3. F4. Old: `\emph{Dressed density.} Let \(e\to\Lambda e\) with the Stueckelberg field of Equation~\eqref{eq:dressed-omega}; rotations are then a symmetry of the dressed density, and \(\Lambda\) is fixed by its own stationarity.` → New: `\emph{Dressed density.} Let the Stueckelberg field \(\Lambda\) of Equation~\eqref{eq:dressed-omega} act on the coframe, \(e\to\Lambda e\), with the density \(\kappa_X\rho^2X[\Lambda e]\); this is an input of Assumption~\ref{ass:local-lorentz} and is not derived. The density is then invariant under \(e\to\Lambda'e\), \(\Lambda\to\Lambda\Lambda'^{-1}\) of the pair, and \(\Lambda\) is treated as a field fixed by its own stationarity at the \(\Theta\)-built frame \(e\). In the unitary gauge \(\Lambda=\mathbb I\) with \(e\) that frame the density is the undressed one and \(r\) stays undetermined, as in the preceding paragraph.`

4. F6. Old: `The Hessian over the six rotation amplitudes` → New: `The Hessian over the twelve real rotation amplitudes`.

5. F3. Old: `On the stationary set the density depends on \(e\) only through \(G\) and \(\rho\), and` → New: `At the stationary points above, where \(S=0\) and \(V_\mu=\partial_\mu\ln\rho\), the density depends on \(e\) only through \(G\) and \(\rho\), and`.

6. F1. Old: `half of the value \(4-n_D\) before the dressing;` → New: `smaller by \(2\kappa_X\) than the value \(4-n_D\) before the dressing, that is half of it at \(n_D=0\) and unchanged at \(n_D=2\);`.

Files reviewed:
- proposals/039-lorentz-locking-noether/proposal-r1.md
- proposals/039-lorentz-locking-noether/appH_insert.tex
- chapters/appH-microscopic-proofs.tex
- chapters/ch10-lorentz-locking.tex
- Gatekeeper verification script (session scratchpad): cls.py
