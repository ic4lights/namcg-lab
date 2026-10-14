VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3, M2 | FLAGS: PRIOR-CLAIM-ERROR, AUTHOR-DECISION | PROGRESS: first | OPEN: 0/3

## Verdict
The core results hold up when re-derived. Lemma 1 (no cutoff-dependent derivative term from the scaffold operator at fixed A_μ), the conformal-mode counterexample, and Lemma 2 (scaffold-rotation invariance rules out linearized diffeomorphism invariance, Einstein–Hilbert and Fierz–Pauli structures for any fixed linear image of the Φ components) are all correct. The final inference of `prop:scaffold` is a genuine error in merged text. Three replacement texts still overstate what was shown, so revisions are required before integration.

## Source reading
**Full scan.** `python scripts/make_digest.py --check` printed `DIGEST CURRENT`. Digest header: hash d3558e44b583da45, dirty-chapters: no, `files: 30`. I read every one of the 30 manifest files under `chapters/` in full: ch01–ch18 and appA–appL, including all 1869 lines of appH and all 787 lines of ch17. No file was unreadable.

**Discrepancy:** the orchestrator said there are 60 chapter files. The manifest and `find chapters -name '*.tex'` both give 30. The researcher's count of 30 is correct.

I also read `MILESTONE.md` and `reports/ledger.md`. There are no earlier reviews in `proposals/003-auto-target/`.

## Claim under review
**Claims:**
- **(i)** Lemma 1: for the displayed action eq:Smicro + eq:V on the scaffold g^(0), with A_μ held at a background value, the cutoff dependence of W_E^(1) contains no derivative of Φ̄. Its Λ² curvature term belongs to g^(0). The composite-metric (∂σ)²Λ² coefficient is zero, and building the operator on g supplies all of it.
- **(ii)** The (∂σ)² term at one loop is finite and positive: ΔZ = 3λ/(4π²).
- **(iii)** Lemma 2: on a flat scaffold, with a regulator, gauge fixing and vacuum that are all rotation-invariant, no order in loops produces an invariant under h → h + p⊗ξ + ξ⊗p. In particular no linearized EH or massless FP form is generated for the composite metric.
- **(iv)** PRIOR-CLAIM corrections in ch08 `prop:scaffold`, appB L110–112 and ch05 L249–251.

**Original target (F):** "evaluate the weighted a_1 and the curvature-linear part of a_2 on the locked block, including diffeomorphism and local-Lorentz ghosts and the radial-mode threshold, with a scheme stated". The ch17 criterion is "Problem F has A,B,C and the sign/scheme dependence of G_eff computed from the specified operators; G_eff is not an input."

Current statuses, quoted verbatim from Appendix H:
- **F:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." ch17 says "CRITICAL PATH; OPEN."
- **C:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope outcome only when its operator, coupling and phenomenological test are supplied; it does not by itself meet the matrix-derived criterion."
- **B:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- **D:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."

The critical-path set in ch17 §sec:ch17-done is A, B, C, D1, E, F, G-derived and N; H, I and J are optional. This matches Appendix H, and the proposal's status table matches both.

## Checks performed
**Anchors and labels (direct verification).**
- `\section{Problem G: HBEV}` occurs exactly once, at appH L1472.
- These replacement sentences exist exactly as quoted:
  - ch08 L285: "The justification is the derivative expansion:"
  - ch08 L294–296: "Self-consistently substituting…"
  - appB L110–112
  - ch05 L249–251
- All 24 cited labels are defined exactly once.
- `\LUV` is defined.
- `Lemma~\ref{lem:msigma}` follows existing usage (ch17 L211, L240, L319).
- All four target files use CRLF line endings.

**Scripts (re-run with C:\Python312\python, outputs in the scratchpad).** All three reproduce the saved outputs exactly: `check_scaffold_hessian`, `check_bubble_lambda`, `check_invariance_nogo`.

**Independent re-derivations, done by hand:**
- **Hessian blocks at φ₀𝕀.** V₂ = (λ/2)(3φ₀²−v²)Tr h² + (λ/2)(φ₀²−v²)Tr k². The commutator cross term vanishes by trace cyclicity. This gives E_H, E_K and tr E = 16λ(v²+4vσ+2σ²). ✓
- **Cutoff dependence.** ∂_Λ I = 2Λ⁻¹f(Λ⁻²) ✓. a₂ in eq:appA-a2 contains derivatives of E only through D²E, a total derivative; (∇E)² first appears in a₃. ✓
- **Conformal mode.** For g = Ω²δ, √gR = 6(∂Ω)² − 6∂(Ω∂Ω). The chain −N₀Λ²/(32π²v²) ↔ +3(∂σ)²/(8πG v²) ↔ ΔZ = −3/(4πGv²), with 1/(16πG) = N₀Λ²/(192π²), is consistent with eq:Z-sigma and eq:universal-R. ✓
- **Bubble.** The second-order Duhamel term with s_min = Λ⁻² reproduces B(p) = (1/16π²)∫dx E₁(·). ∂_{p²}B|₀ = −e^{−m²/Λ²}/(96π²m²). This gives W ⊃ (3λ/8π²)e^{−λv²/Λ²}∫(∂σ)², so ΔZ = 3λ/(4π²) for s_max = ∞. ✓
- **Lemma 2.** Under pure scaffold rotation Φ_a(x) → Φ_a(R⁻¹x) (the tangent and internal labels do not rotate), eq:Smicro and eq:D-both are invariant. So F(Rp) = F(p) and F depends only on p². Invariance under the shift ⇔ the shift lies in the radical of Q_p. Using p′ = |p|e_i and ξ = e_j shows the radical is all of Sym², so Q_p = 0. ✓
  - The extra global diagonal symmetry (scaffold × tangent × internal rotation) also exists in Euclidean signature. It does not rescue EH, because the pure scaffold rotation is a separate symmetry. This is the right hypothesis to isolate.
- **My own script, `gk_ircut.py` in the scratchpad.** It checks the bubble with the manuscript's IR limit s_max = μ⁻² (eq:s-limits). Massive block: unchanged for μ ≪ m. Massless block: ∂_{p²}B₀ → (1/Λ² − 1/μ²)/(96π²), confirmed numerically. Under eq:s-limits the anti-Hermitian block therefore adds a positive, IR-regulator-dependent local term ΔZ_K = (λ²v²/12π²)(1/μ² − 1/Λ²) for p² ≪ μ². (Finding 3.)
- **ch05 A-mixing.** At Φ̄ = v𝕀, Tr(DΦ†DΦ) ⊃ Tr((∂Y − vA)²) with no H–A cross term (cf. appH L1365–1380). Under the manuscript's own identification M = ηh (appH L1033–1037), however, the T_{0i} components lie in the anti-Hermitian block. For complex δΦ, the imaginary parts of ψ and T lie there as well. (Finding 1.)
- **ψ–T orthogonality.** In mixed form, ψ maps to (ψ/4)𝕀 and T to ηT, with Tr(ηT) = 0. There is therefore no ψ–T cross term in either the kinetic or the potential quadratic form. ✓

**Literature.** Weinberg–Witten appears only in the author note, not in the LaTeX. I did not independently verify it. No other citations are added.

## Findings
1. **Severity: major.**
   - **Location:** Item 4 (ch05 replacement).
   - **Finding:** The sentence "contains neither [ψ∂∂T nor A∂T] … A_μ mixes only with the anti-Hermitian part" draws a conclusion that does not follow. The ψ∂∂T part is correct: there is no ψ–T mixing at all at tree level. But A_μ mixes with K through 2iv Tr(A∂K) (the proposal's own L325). Under M = ηh (appH L1033–1037), T_{0i} ∈ K, and for complex δΦ the imaginary parts of T are in K too. So whenever G_int contains those generators (for example the U(4) branch of appH), there is a tree-level derivative A–T mixing.
   - **Required action:** Drop the A∂T clause or scope it; corrected snippet below. Restrict the PRIOR-CLAIM-ERROR for ch05 to the ψ∂∂T statement.
2. **Severity: major.**
   - **Location:** Item 2 (ch08 replacement of the final sentence of `prop:scaffold`).
   - **Finding:** The new text states without qualification that "for the displayed action … the Λ² curvature term is that of g^(0) and multiplies no derivative of the condensate". Lemma 1 holds only with A_μ held at a background value, and the proposal itself lists the A_μ-integrated theory as not covered. The integrated theory has sigma-model-type derivative couplings. The phrase "curvature term … multiplies no derivative" is also mis-aimed: R[g^(0)] multiplies tr 𝕀. The correct statement is that no cutoff-dependent term contains a derivative of Φ̄.
   - **Required action:** Add the fixed-A_μ qualifier, or cite Lemma 2, which covers eliminated connections, for the general "no composite-metric EH term" claim. Snippet below.
3. **Severity: major.**
   - **Location:** Item 1, third paragraph (finite (∂σ)² term).
   - **Finding:** The setup paragraph regulates with eq:W-again and eq:s-limits (s_max = μ⁻²). The finite-term result Z = 2N + 3λ/(4π²) + O(λv²/Λ²), and the statement that the K block gives "no Λ-dependent (∂σ)² coefficient" with only a non-analytic term, were computed with s_max = ∞. Under the stated limits, for p² ≪ μ², the massless block adds a positive local ΔZ_K = (λ²v²/12π²)(1/μ² − 1/Λ²). Your statement "no Λ-dependent coefficient" and the sign conclusion both survive, but the displayed value of Z does not.
   - **Required action:** State s_max → ∞ (μ → 0) for this paragraph, or include the μ-dependent K-block term. Add a script check for whichever is chosen.
4. **Severity: minor.**
   - **Location:** Item 1, third paragraph.
   - **Finding:** "the opposite-sign term of eq:Z-sigma enters only through the operator built on the emergent metric" overstates the result. Only its absence from this calculation is shown.
   - **Required action:** Reword to "is not produced in this calculation; in the manuscript it arises from the induced Einstein–Hilbert term, i.e. from the operator built on the emergent metric".
5. **Severity: minor.**
   - **Location:** Item 1, second paragraph.
   - **Finding:** "restricted or reduced form". If the full theory's gauge transformation also moves components outside h, that invariance passes to the reduced (Schur-complement) form, not to the restricted one.
   - **Required action:** Say that the physical criterion is the reduced form. The lemma as stated (if Q_p is invariant then Q_p = 0) is unaffected.
6. **Severity: minor.**
   - **Location:** Item 3 (appB).
   - **Finding:** `prop:scaffold` concerns heat-kernel operators, not the replica cover. Citing it as "recording" the premise for identifying the cover is loose.
   - **Required action:** Align with appH L72–75: "Identifying it with the emergent spacetime requires a specified map g^(0) → g, which the displayed action does not supply (cf. Proposition~\ref{prop:scaffold})."
7. **Severity: minor.**
   - **Location:** Stale passages the proposal does not list.
   - **Finding:** These become inconsistent or unflagged after the correction:
     - ch04 Exercise 7 (L418–423) asks when the replacement is "legitimate" and what error it "drops", deferring to Chapter 8.
     - ch08 L56–58, "Integrate η … on a slowly varying emergent background", is now an unflagged premise.
     - appG L19–29 identifies the area prefactor through the heat kernel.
     - ch16's inventory does not list the emergent-background premise (Author decision 1).
   - **Required action:** Add these to the author list. The integrator must not edit them without accepted text.
8. **Severity: minor / AUTHOR-DECISION.**
   - **Location:** ch08 `prop:scaffold` after correction.
   - **Finding:** A "Proposition" whose conclusion is now "a premise, not a consequence" would rest on a vague first sentence (undefined h^(0), ‖·‖). The new lead-in, "bounds what this choice changes", leans on that sentence.
   - **Required action:** The author should decide whether to convert it to a remark or a named assumption and whether to add it to the ch16 inventory.

**Earlier findings:** none; this is round 1.

**PRIOR-CLAIM-ERROR, confirmed independently:**
- The final sentence of `prop:scaffold` is a false implication. By the proposition's own wording the change is of "the same operators already kept". The counterexample shows the replacement moves the Λ²(∂σ)² coefficient from 0 to its full value, so the substitution is not controlled at that order. This is load-bearing for reading thm:Geff as a statement about the emergent metric, although ch04 L217–222 and appH L1194–1199 already call the operator a Presentation-B assumption.
- The ch05 ψ∂∂T clause is false for eq:Smicro at tree level. It is non-load-bearing.

## Scope of what is established
- **Proved:**
  - The Hessian structure and Lemma 1, under the scaffold proper-time regulator with A_μ fixed.
  - The conformal-mode counterexample.
  - The ψ–T orthogonality.
  - Lemma 2, under a flat scaffold, rotation-preserving regulator and gauge fixing, an invariant vacuum, and h any fixed linear image of the Φ components.
- **Conditional:** ΔZ = 3λ/(4π²), which holds only with A_μ fixed and s_max → ∞.
- **Not covered:**
  - The A_μ-integrated theory.
  - Θ-dependent regulators, which break the scaffold rotation symmetry and are excluded correctly.
  - Curved scaffolds.
  - Presentation A.
  - The Weinberg–Witten applicability.
- **Classification:** This is a no-go and dependency resolution for F, which stays PROGRAMME-CONDITIONAL. F, C, B and D remain OPEN / CRITICAL PATH. No label change is proposed, and none is warranted.
- **Milestones:**
  - **M3:** a merged implication is wrong.
  - **M2:** a new no-go excludes loop-generated composite-metric EH/FP terms in the scaffold-symmetric class.
  - **M5:** not triggered, because no structural change is proposed. The structural alternatives in Author decision 2 need the author.

## Recommended disposition
Revise the package, then return it to the author. It is coherent: all items address which metric the heat kernel induces, and the corrections follow from Lemmas 1 and 2. Fix Findings 1–3 and preferably 4–6. Because PRIOR-CLAIM-ERROR applies, the loop stops for the author whatever the next verdict.

## Corrected snippet
No new physics. The only extra assumption is the scope already stated in the proposal.

ch05 (replaces Item 4's LaTeX):
```latex
Mixing terms of the form \(\psi\,\partial\partial T\) and
\(A\,\partial T\) would be the usual linearized scalar--tensor and
vector--tensor mixings. The quadratic expansion of
\(S_{\mathrm{micro}}\) on the flat scaffold contains no
\(\psi\)--\(T\) mixing: its kinetic term contracts derivatives only
through \(g^{(0)\mu\nu}\), and the trace and \(\eta\)-traceless parts
are orthogonal in its kinetic and potential forms. The internal
connection \(A_\mu\) mixes only with the anti-Hermitian part of
\(\delta\Phi\), with the derivative index contracted with that of
\(A_\mu\); which components of \(T_{\mu\nu}\) lie in that part depends
on the identification of \(T_{\mu\nu}\) in \(\delta\Phi\) and on the
internal gauge group. A \(\psi\,\partial\partial T\) structure requires
an additional ingredient (Appendix~\ref{app:status},
Section~\ref{sec:status-F}).
```

ch08 (replaces the middle of Item 2(b)):
```latex
  For the displayed action~\eqref{eq:Smicro} with the operator built
  from \(g^{(0)}\) and the internal connection held at a background
  value, no \(\LUV\)-dependent term contains a derivative of the
  condensate (Appendix~\ref{app:status}, Section~\ref{sec:status-F});
  the emergent-metric coefficient of the identity is produced by the
  replacement.
```

Item 1, third paragraph: insert "With \(s_{\max}\to\infty\) for this finite term," before "At \(\bar A_\mu=0\)". If finite μ is kept instead, the researcher must add and check the term ΔZ_K = λ²v²/(12π²)(μ⁻² − Λ⁻²) for p² ≪ μ². I computed that term and checked it numerically in the scratchpad, but it is not in the proposal's scripts.

Relevant files:
- C:\Users\redgi\Projects\namcg-lab\proposals\003-auto-target\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\chapters\ch08-heat-kernel.tex (L280–297, L363–367)
- C:\Users\redgi\Projects\namcg-lab\chapters\ch05-lorentz-decomposition.tex (L238–252)
- C:\Users\redgi\Projects\namcg-lab\chapters\appB-modular.tex (L110–113)
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (L1033–1037, L1194–1199, L1365–1380, L1472)
- C:\Users\redgi\Projects\namcg-lab\chapters\ch04-vierbein-emergence.tex (L217–222, L418–423)
