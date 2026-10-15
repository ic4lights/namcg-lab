VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: AUTHOR-DECISION | PROGRESS: first | OPEN: 0/2

## Verdict
The core algebra is sound and reproduced independently: the rank-6 immersion, the quadratic image relation, the 3-mode linear response, and the Einstein-operator rank 3 against 6 conserved sources. Two major wording and scope defects must be fixed before integration: the "metric seen by the operators" scope inconsistency, and the overreach in "whatever the coefficients of an induced action". There are also several minor fixes. This is a bounded conditional obstruction, not a breakthrough.

## Source reading
Digest plus targeted reads. `make_digest.py --check` printed DIGEST CURRENT. I read in full:
- appH Problem F ledger label and the 005 paragraph (L1650-1813), and the Problem A label.
- ch08 `ass:emergent-op` and `rem:ch8-scaffold-vs-emergent` (L280-315).
- ch03 `def:matrix-coords`, `eq:V` and `eq:vacuum-manifold`, `rem:ch3-moyal-check`, `rem:ch3-trace-quadratic` (L96-562).
- ch04 `eq:vev-is-frame` and `def:composite-metric`.
- MILESTONE.md and the tail of `reports/ledger.md`.

Not a full scan. The proposal changes no definition, assumption, label or scope text. No unreadable files. I did not compile LaTeX, because that would write into the repository.

## Claim under review
The target is the missing link that ⟨Φ⟩/v is the coframe, i.e. discharging `ass:emergent-op` (Problem F; also A, B, C, D1). The proposal does not derive it. It records a bounded obstruction in the class H_A: four Hermitian matrices, Poisson limit, constant η, real nondegenerate Θ, K = ΘᵀηΘ, G = K⁻¹, ρ = 1/|Pf|.

Appendix H, quoted verbatim:
- F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- A: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

Chapter 17 still lists A, B, C, D1, E, F, G-derived and N. No label change is proposed.

## Checks performed
**Re-run of the researcher's scripts.** All four ran cleanly and gave the saved outputs, including `check_embedding_and_vacuum.py`, which was run after the final edits:
- `check_theta_image.py`: char poly, relation `(Kη)² − ½tr(Kη)Kη − Pf² = 0`, rank 6 at 40 and 39 random points, rank 5 at the Pf = 0 point, Lorentzian minimum of ‖N² + c‖² equal to 2c².
- `check_linear_response.py`: dG formula, d ln ρ = p·u, u = q gives dG = 0, rank 3, Einstein rank 3 against 6 for both G and g_ρ.
- `check_embedding_and_vacuum.py`: K = θᵀgθ for D = 4, 6, 10; G = 1 − 2nnᵀ; tangent count 2.
- `verify_anchors_labels.py`: anchor occurs once; every cited label occurs once. It prints a harmless "LUV macro: check preamble".

**My own numerical check.** I wrote it in stdin, with nothing written to the repository. It uses a random Θ̄ and p, and a central finite difference of G = (ΘᵀηΘ)⁻¹ along T = q⊗u − u⊗q.
- The (δG, δρ) map has singular values 3.59, 1.47, 0.81 and about 1e-10, so rank 3.
- I applied the linearised Einstein operator for the background Ḡ to each δG. The rank is 3, with singular values 4.66, 2.28, 1.12 and about 1e-10.
- The outputs satisfy pᵘE_μν = 0. The generic-h Einstein operator has rank 6.
- This confirms the 3-against-6 count independently of the researcher's script. It covers one random sample, not a proof.

**Analytic re-derivation.**
- K = −Θη Θη, so Kη = −N² with N = Θη ∈ so(η). I checked that det N = −Pf², so the constant term of the char poly is −(E·B)², as in `rem:ch3-moyal-check`.
- In sl2 ⊕ sl2 over C, N² = (ν₊+ν₋)𝟙 + 2n₊⊗n₋ with n±² = ν±𝟙. The scalar and (3,3) parts are independent. A kernel element of dΘ ↦ d(N²) therefore needs dn₊⊗n₋ + n₊⊗dn₋ = 0, hence dn₊ = −λn₊ and dn₋ = +λn₋ (n± ≠ 0 when Pf ≠ 0). The scalar part gives λ(ν₊−ν₋) = 0, and ν₊−ν₋ = 2i Im ν₊ ≠ 0 iff E·B ≠ 0. So the kernel is trivial and the rank is 6.
- At E·B = 0, Θ ≠ 0 the duality rotation is a kernel direction, so the rank is 5. This is a differential of Θ ↦ K only, since G is undefined at Pf = 0 (finding 6).
- The image relation follows from the eigenvalues c ± 2√(ν₊ν₋) of N², each doubly degenerate. Their product is (ν₊−ν₋)² = −4(Im ν)² = −Pf², matching the script.
- `K = c g⁻¹` impossibility: K = θᵀgθ = −θgθ gives (θg)² = −c. N = θg ∈ so(g), and for real Lorentzian g it is conjugate to the η case. The constant term of the char poly is −(E·B)² ≤ 0 < c². Valid, and it extends `rem:ch3-moyal-check` pointwise to general real Lorentzian g.
- Gauge counting. The matrix gauge is the single function λ, with δa^μ = Θ^{μρ}∂_ρλ, so 4 − 1 = 3 gauge-invariant functions. This is consistent with `rem:ch3-trace-quadratic` and the 005 "three-dimensional quotient". Nonlinearly, closed 2-forms near ω̄ are ω̄ + dα (locally), which gives 3 functions. The gauge is 1-dimensional.
- Item 7: T ≡ 𝓕_Θ in `rem:ch3-trace-quadratic`. u ↦ T and u ↦ (δG, δρ) share the kernel span(q), so the tree-level quadratic action is algebraic in (δG, δρ) at quadratic order about constant Θ̄. This is correct and not dependent on extra assumptions.
- Item 6 (vacuum): e = η⁻¹ω̂ gives eᵀe = −ω̂², so eᵀe = 1 iff ω̂² = −1. This reproduces the researcher's result for the displayed potential `eq:V` with a Euclidean δ contraction on the internal index. The 2-of-6 tangent count is a check of the script, not an independent derivation.

**Consistency with 005.** I found no contradiction. The 005 sentence "At the sample points tested the map has rank six" is strengthened rather than contradicted. The new Einstein-rank-3 result agrees with 005's "no pure-gauge perturbation lies in the tangent space".

**Anchor.** The text "do not apply; no linearized-diffeomorphism invariance is claimed. Problems~B, C, D and~F remain open." occurs exactly once (appH L1812-1813), immediately before `\section{Problem G: HBEV}` at L1815. The anchor is valid.

**Not verified.** No literature is cited, so there is none to check. I did not compile LaTeX.

## Findings

1. **Major. "Metric seen by the operators" paragraph: scope inconsistency.**
   - Location: the third paragraph of the proposed text, and its closing paragraph.
   - Finding: the paragraph introduces D ≥ 4 coordinate matrices with the embedding dictionary Φ^I_μ := ∂_μ x^I and states a result for them. The closing paragraph then says the result does not apply to "additional matrix coordinates". It also says the operators "sit on G, not on a metric of the form (eq:g-from-e)". But the preceding 005 paragraph shows that G itself has the form `eq:g-from-e` for the Θ-coframe e. What fails is the identification of G with the Φ-induced g = ΦᵀηΦ and with ⟨Φ⟩/v. The embedding dictionary is an imported reading, not part of the four-matrix class. The conclusion "ass:emergent-op read with that metric is not discharged by this class" is true only for that reading.
   - Required action: label the embedding reading as an assumed dictionary, state that the K = c g⁻¹ result holds pointwise for any real Lorentzian g, and drop the wording that suggests no `eq:g-from-e` metric exists. State that the conclusion is about the embedding reading (see the corrected snippet).

2. **Major. The "whatever the coefficients of an induced action" headline overreaches.**
   - Location: the linear-response paragraph, sentence beginning "Hence E[h]=T … solvable only …".
   - Finding: what is shown is that any linear local relation from the 3-dimensional space of (δG, δρ) modes at fixed generic p to the 6-dimensional space of conserved sources has rank ≤ 3. That is a dimension count and is correct. It is not a statement about the field equations of an induced action. Varying the four functions a^μ yields only the projection of (E − T) onto the 3-dimensional image (3 equations, one gauge identity), not the tensor equation E = T. The manuscript's framework also carries an extra stress (T_ent, the backreaction tensor 𝒢 of Chapters 11-14), which the text mentions only as a caveat. "Conserved" means p^μT_μν = 0 with respect to the constant background.
   - Required action: restate the conclusion as "the tensor equation E[h]=T (any linear relation between (δG, δρ) and T) cannot hold for generic conserved T without an additional conserved stress", and define "conserved". State explicitly that varying a^μ gives only the projected equations.

3. **Minor. "Four conditions on the ten components".**
   - Finding: the matrix relation is necessary. It is not shown that the relation is sufficient, or that it yields exactly four independent conditions.
   - Required action: say instead "so the six-dimensional image has codimension four in the ten-dimensional space of metrics, and lies in the set cut out by the relation".

4. **Minor. The N-coordinate parenthetical "a necessary functional count N−1+4≥11".**
   - Finding: it is unexplained in the manuscript and is a conjecture or sketch by the researcher's own classification. My check of the count is consistent: N−4 embedding functions plus 3 for ω, minus nothing further, plus 4 diffeos. It is a heuristic, not a theorem.
   - Required action: delete the parenthetical from the manuscript text. Keep the N ≥ 8 reading as an author question only.

5. **Minor. LaTeX and notation.**
   - ℓ is undefined; it should be a fixed length with e = η⁻¹(Θ/ℓ²)⁻¹.
   - "n is orthogonal to p" needs the metric (K, i.e. n̄ᵀKp = 0). n and p are covectors.
   - "symmetrisation without a factor ½" is clumsy. Use a ∘ b = abᵀ + baᵀ, defined as in the proposal.
   - e₀ and J are used without definition.
   - The vacuum statement must say the internal index is contracted with δ and the locked block is real.
   - Mark the nonlinear "3 against 7" count as a counting argument (conditional), not a derived result.

6. **Minor. "Rank five at Pf = 0".**
   - Finding: G does not exist there (det K = −Pf⁴ = 0).
   - Required action: say "the differential of Θ ↦ K has rank five when Θ ≠ 0 and Pf Θ = 0", or delete.

## Scope of what is established
The following are established in H_A, subject to the revisions above:
- Rank-6 immersion of Θ ↦ G at Pf ≠ 0.
- The image relation.
- 3-dimensional linear response about constant Θ̄ at generic p.
- Einstein-operator rank 3 against 6 conserved sources. The rank-3 count holds for G, for g_ρ, and in fact for any linear local operator on the 3-dimensional mode space.
- `K ≠ c g⁻¹` for real Lorentzian g.
- The tree-level quadratic action is algebraic in (δG, δρ).

Exact hypotheses of the obstruction: four matrix coordinates; Poisson limit; constant η; real nondegenerate Θ; linear order about constant Θ̄; generic p; an Einstein-type equation demanded for generic conserved T with no additional conserved stress.

Conditional: the vacuum-manifold mismatch, which applies only if e is identified with ⟨Φ⟩/v; and the nonlinear 3-against-7 count, a heuristic.

Not established: ⟨Φ⟩/v as the coframe; any value or sign of G_eff; anything for Presentation B with an independent Φ; Moyal corrections; T_ent.

Terminology: record this as a conditional obstruction, not a bare "no-go". The paragraph does not use the word "no-go", which is correct.

Hypotheses a within-core route could relax (named only; no research originated):
- a derived extra stress such as T_ent;
- Moyal corrections beyond the Poisson limit;
- non-constant backgrounds;
- fermion and scalar content;
- Presentation B with an independent Φ.

F, A, B, C and D remain OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL.

**N ≥ 8 relaxation.** It changes the Presentation-A matrix content of `def:matrix-coords`, so it is a structural proposal. If adopted it would be M5, and it needs an author decision. It is not adopted here and must remain an author item. This is why `AUTHOR-DECISION` is flagged.

**Milestone.** M2, bounded: it rules out four-matrix Poisson-limit Presentation A as a carrier of Einstein equations with generic sources and no extra stress, and rules out the embedding reading of `ass:emergent-op` in that class. Not M3 (no merged claim is wrong), not M1.

**BREAKTHROUGH.** Not flagged. The result is a bounded obstruction. It derives no critical-path step.

## Recommended disposition
Revise per findings 1-6 and resubmit as r2. The anchor and labels are fine; no stale-text change is needed. Keep the N ≥ 8 reading as an author-level question outside the manuscript text.

## Corrected snippet
Needs no new physics. Replace the "Metric seen by the operators" opening and the final paragraph as follows.

Opening of the third paragraph:
\emph{Metric seen by the operators.} Suppose, as an assumed dictionary not contained in the four-matrix class, that there are \(D\ge4\) coordinate matrices \(X^I\) with a Lorentzian \(\eta_{IJ}\), and put \(\Phi^I{}_\mu:=\partial_\mu x^I\), \(g:=\Phi^T\eta\Phi\). Then \(K=\theta^{T}g\,\theta\) exactly; for \(D=4\), \(x^I=y^I\) and \(g=\eta\). The relation \(K=c\,g^{-1}\), \(c\neq0\), would give \(N^2=-c\) with \(N=\theta g\in\mathfrak{so}(g)\), whose characteristic polynomial has constant term \(-(\mathbf E\cdot\mathbf B)^2\le0<c^2\); \(c=0\) contradicts invertibility. So, pointwise for any real Lorentzian \(g\), the operator metric \(G=K^{-1}\) is not \(g\); this extends Remark~\ref{rem:ch3-moyal-check}, and Assumption~\ref{ass:emergent-op} read with the metric of that embedding reading is not discharged. The metric \(G\) itself has the form~\eqref{eq:g-from-e} for the coframe of the preceding paragraph.

Closing paragraph, after "…not apply to an independent field \(\Phi\) of Presentation~B": delete the parenthetical "(a necessary functional count … condition)"; keep "to the embedding statement above beyond four coordinates, or to Moyal corrections".

For the linear-response conclusion, use: "Hence the tensor equation \(\mathcal E[h]=T\), and any linear local relation between \((\delta G,\delta\rho)\) and \(T\), can hold only for \(T\) in a subspace of dimension at most three of the six-dimensional space of sources with \(p^\mu T_{\mu\nu}=0\); varying the four functions \(a^\mu\) gives only the projection of the equation onto that image. This does not exclude an additional conserved stress that absorbs the codimension; such a stress would have to be derived."

Extra assumptions: none beyond the researcher's.
