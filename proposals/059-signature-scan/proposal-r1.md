# Proposal 059-signature-scan, round 1

## Result

This is a bounded result for Problem E. It is a conditional sharpening, not a derivation. I replace the supplied η in S_b by a real nondegenerate target contraction h₀ of signature (10−t, t) and keep Definition (A). Five things follow.

1. **Rigidity lemma (exact, new, elementary).** Let h be complex symmetric with Im det(h|_E) ≥ 0 for every real 2-plane E. If Re h is invertible with at least two positive and at least two negative eigenvalues, then h is real.
   - The proof is about ten lines, using Im det(r+is) = tr(adj(r)s) for 2×2 blocks.
   - It does not need 056's inertia lemma or a generalisation of 057's plane class.
   - At N=2 the hypothesis is exactly the closed damping condition Re iS_b ≤ 0. At N ≥ 3 it is implied by that condition, by restriction to an su(2) block.

2. **Claim A (algebraic).** The real invertible forms in the closure of 𝔆 are exactly those with t ∈ {0, 1, 9, 10}, i.e. ±δ and ±(9,1) up to real congruence.
   - This follows from 055 (ii), and independently from the lemma.
   - It is the matrix analogue of the Kontsevich–Segal allowability domain, whose real boundary points are Lorentzian. I verified this in Witten 2111.06514, Eq. (3.5), the passage on (3.6), and the KS abstract.
   - The analogy has two differences. Both are stated in the insert.

3. **Claim B (contours), 2 ≤ t ≤ 8.** This is stronger than the scout's pointer.
   - **(a) Paths.** Every continuous path of invertible linear contours from a real contour along which Re iS_b ≤ 0 keeps h real. This holds at every N, for every regulator, and with any mass term.
   - **(b) Single contours.** For regulators with P⁻¹h₀ having only the eigenvalues ±c, which includes Definition (A) with h₀ = diag(±1), every linear contour with Re M positive definite and Re iS_b ≤ 0 has real h. This is the generalisation of 056 (i) to t negative entries.
   - **(c) Consequence.** On all these contours S_b is real, so none is damped, and the ε=0 integrand is not absolutely integrable. The dominated convergence that gives the t=1 limit in the 053 paragraph is therefore unavailable on every such contour and on every invertible limit of them.
   - For t ∈ {0,1} (and 9, 10 by evenness of S_b in h₀), such paths to damped contours exist.

4. **Claim C (verified from a source I opened).** A Majorana–Weyl spinor in signature (s,t) exists exactly when s − t ≡ 0 mod 8.
   - Source: Van Proeyen, hep-th/9910030, Eqs. (3.25) and (3.28) and Table 2, read from the PDF pages.
   - In d=10 this gives t ∈ {1,5,9}.
   - IKKT's fermion is a single ten-dimensional MW spinor: hep-th/9612115, p. 2, where θ¹ = θ² = ψ after κ-fixing. I read this on the PDF pages.

5. **Conditional statement.** Assume (P1): the ε→0 limit of Definition (A) is obtained by dominated convergence on a damped linear contour reached from the Hermitian contour by a path with Re iS_b ≤ 0. Assume (P2): the supplied fermion is a single MW spinor for h₀.
   - Then t ∈ {1,9}, i.e. h₀ = ±Tᵀη T.
   - (P1) alone leaves {0,1,9,10}, and (P2) alone admits (5,5).

**Fork explored, colour mixing (§6, H2; proposal only).** At N=2, first order, linear maps that also mix the colour components have no damping direction other than the complexified symmetries O(h₀,ℂ)×O(3,ℂ). This is proved analytically and agrees with an LP probe. The non-perturbative statement is open.

**Witten comparison.** This is a correction to the scout's pointer, not to the manuscript.
- Witten's two boundary approaches to one Lorentzian metric, −(1∓iε), correspond in the matrix weight to h versus h̄. These are the damped sets of e^{iS_b} and of e^{−iS_b}, i.e. Definition (A) and its complex conjugate.
- The 055/057 split 𝔆₀ / −𝔆₀ is something else: it is h ↦ −h, the overall sign of the contraction, which S_b does not see. η lies in cl(𝔆₀) only, and −η in cl(−𝔆₀) only.
- So "almost word for word" (scout §0.2) is not right, and no Feynman / anti-Feynman reading of −𝔆₀ is supported.

**Scope.**
- h₀ is the contraction of the target (matrix) indices, not the emergent metric. The induced tensor of def:matrix-coords-ext is the pull-back of h₀ by a configuration. For a (9,1) h₀, its restriction to a 4-plane is positive definite, Lorentzian or degenerate depending on the configuration.
- Nothing here derives Lorentzian signature of the composite metric. Assumption ass:lorentzian is **not** discharged.
- Problem E stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Target and status

- **Problem:** E, signature.
- **Appendix H, L1486–1489, verbatim:** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- **ch17 L394–399:** "OPEN; CRITICAL PATH for the matrix-derived label. … rotating because the infrared world is Lorentzian is not a derivation."
- **ch17 L718–719 (completion criterion):** "Problem~E: Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})."
- **ch17 L739–742:** an item met only by an imposed premise, input or reduced scope yields at most a scope-limited model.
- Appendix H and ch17 are consistent. No discrepancy found.
- **Original target:** derive Lorentzian signature rather than retaining ass:lorentzian.
- **Dependencies:**
  - the 053–057 paragraphs of sec:status-E (Definition (A), 𝓡_u, 𝔆, 𝔆₀, the inertia lemma, the plane class);
  - def:matrix-coords-ext (ch03 L173), in which the matrix-index form is retained "as Assumption ass:lorentzian";
  - ass:lorentzian (ch04 L322), stated for the Presentation-B η_AB.
- **Classification of this package:** PROGRAMME-CONDITIONAL. The selection holds only under the imposed premises P1 and P2, and only for the target contraction.

**Current critical-path set**, from ch17 L700–733 and Appendix H: A, B, C, D1, E, F, G-derived, N. This agrees with the CLAUDE.md snapshot.

## Source reading

- **Mode:** digest + targeted reads. No full scan was done.
- **Digest:** `python scripts/make_digest.py --check` printed `DIGEST CURRENT`.
- **Working tree:** the dirty chapters are appH (055–057) and ch13, ch16, appE, appI (058).
- **Baseline appH:** 569524 bytes, sha256 9443341b…7bcd, CRLF 3266 and bare LF 0. This matches the brief.
- **Read in full:**
  - appH L1482–1577: all of Problem E, including the dirty 055, 056 and 057 blocks.
  - ch17 L690–752 (completion criterion) and L394–399 (Problem E).
  - ch04 L313–333 (sec:ch4-signature, ass:lorentzian).
  - ch03 L95–200 (def:matrix-coords, eq:Smatrix, def:matrix-coords-ext).
  - appH L1478 and L1480 (the reflection paragraph's bearing on E).
  - reports/ledger.md L280–400 (053–058).
  - the whole scout report reports/sme-scout-20261108-after55.md.
  - 057 apply_check and review-r2.
- **Not read:** the other dirty chapters (ch13, ch16, appE, appI). They are not touched or relied on.
- **Unreadable files:** none.
- **Literature opened this session:**
  - Witten 2111.06514: PDF pp. 8–11 read as images. Eqs. (3.1)–(3.6), the "two different ways" passage, and footnote 8.
  - Kontsevich–Segal 2105.10161: abstract.
  - Van Proeyen hep-th/9910030: PDF pp. 19–22 read as images. Table 1, Eqs. (3.17)–(3.28), Table 2.
  - IKKT hep-th/9612115: abstract, and PDF pp. 1–3 read as images, Eqs. (2.1)–(2.6).

## Research and reasoning

### 0. Setting

- **Action.** Define S_b^{h₀} = −(1/4g²) Σ (h₀)_{μρ}(h₀)_{νσ} Tr[A_μ,A_ν][A_ρ,A_σ]. This is the existing S_b for h₀ = η.
- **Contour form.** On A = ΛX the action is the same expression in X with h = Λᵀh₀Λ.
- **N = 2.** S_b = (1/4g²) Σ_{a<b} [h(x^a,x^a)h(x^b,x^b) − h(x^a,x^b)²]. This is checked numerically for random complex Λ and every t: the constant is 1/4 to 6.5e-16 (`rigidity_checks.txt`, B).
  - So 𝔆, 𝔆₀ and the normal form of 055 depend only on h, not on h₀.
  - What h₀ fixes is the starting point: Λ(0) real gives h(0) real with the inertia of h₀.
- **Every h is reachable.** Over ℂ every nondegenerate symmetric form is congruent to every other, so for every h₀ there are linear contours with h ∈ 𝔆, e.g. Λ with Λᵀh₀Λ = e^{iπ/4}𝟙.
  - The whole question is therefore whether such contours are joined to the real contour, or are admissible for the regulator.
- **Evenness.** S_b is even in h₀: it is quadratic in h₀. The (det 𝒢)⁴ Pfaffian form at N=2 is also even. So t and 10−t give the same integrand, with 𝔆₀ and −𝔆₀ exchanged. Checked in B.
- **The closed condition.** At N=2, Re iS_b ≤ 0 for all X is equivalent to Im det(h|_E) ≥ 0 for every real 2-plane E.
  - Proof: set x³ = 0 for one direction; summing over pairs gives the other.
  - The sign is basis-independent, because a real change of basis of E multiplies det by (det P)² > 0.
  - For N ≥ 3 the condition is implied by restriction to an su(2) block, as in 055 and 057 (i). Check B confirms that the su(2) block in N=3 reproduces the N=2 value exactly.

### 1. Rigidity lemma (established, exact)

**Statement.** Let h = R + iS be complex symmetric. Assume Im det(h|_E) ≥ 0 for all real 2-planes E, and R invertible with p ≥ 2 positive and q ≥ 2 negative eigenvalues. Then S = 0.

**Proof.**
- For 2×2 real symmetric r and s, det(r+is) = det r − det s + i tr(adj(r)s). This is exact; sympy check A.
- Split ℝ¹⁰ = V₊ ⊕ V₋ R-orthogonally. Let λ be the eigenvalues of S|V₊ relative to R, and ν those of S|V₋ relative to −R.
- *Planes in V₊.* With an R-orthonormal basis, R_E = 𝟙 and adj 𝟙 = 𝟙, so the condition reads tr S_E ≥ 0. The minimum over such planes is λ₁+λ₂ (Ky Fan). So λ₁+λ₂ ≥ 0, which needs p ≥ 2.
- *Planes in V₋.* R_E = −𝟙 and adj(−𝟙) = −𝟙, so tr S_E ≤ 0. Hence ν_{q−1}+ν_q ≤ 0, which needs q ≥ 2.
- *Mixed planes.* Take e ∈ V₊ and f ∈ V₋ with R_E = diag(1,−1). Then adj = diag(−1,1), and the condition is S(f,f) − S(e,e) ≥ 0. So λ_p ≤ ν₁.
- *The chain.* 0 ≤ λ₂ ≤ λ_p ≤ ν₁ ≤ ν_{q−1} ≤ 0. Here λ₂ ≥ 0 because λ₁ ≤ λ₂ and λ₁+λ₂ ≥ 0; ν_{q−1} ≤ 0 likewise. Then λ₁ ≥ −λ₂ = 0 = λ_p, so every λ vanishes; ν_q ≤ −ν_{q−1} = 0 = ν₁, so every ν vanishes. Hence S|V₊ = 0 and S|V₋ = 0.
- *Off-diagonal block.* Take e₁ ∈ V₊ with R = 1, and f₁, f₂ ∈ V₋ R-orthonormal; this needs q ≥ 2. Let e = cosh a·e₁ + sinh a·f₁. Then R(e,e) = 1, R(e,f₂) = 0 and R(f₂,f₂) = −1. The condition gives −S(e,e) + S(f₂,f₂) = −sinh(2a)·S(e₁,f₁) ≥ 0 for all real a, so S(e₁,f₁) = 0. ∎

**Topological corollary.**
- For 2 ≤ t ≤ 8, the real forms with t negative eigenvalues form a subset that is open in 𝔇_inv := {h invertible : Im det(h|_E) ≥ 0 ∀E}. Openness follows from the lemma plus continuity of eigenvalues. The subset is also closed in 𝔇_inv.
- Since 𝔆 ⊂ 𝔇_inv contains no real h, these forms are not in cl(𝔆).

**Sharpness for q ≤ 1.**
- 𝓡_u (t=1, u=0.3) and e^{0.2i}𝟙 (t=0) satisfy the closed condition with S ≠ 0. Check D gives sampled minima +7.3e-2 and +5.4e-2.
- So both hypotheses p ≥ 2 and q ≥ 2 are needed.

**Numerical certificate.**
- The constructive proof is implemented in check C. It picks whichever of the four plane types is violated.
- I ran 2800 random (R, S) over t = 2..8, with ‖S‖ from 1e-8 to 10. Half of the S were adversarial: S vanishing on the definite blocks, or S = +𝟙 on V₊ and −𝟙 on V₋.
- Every trial produced a plane with Im det < 0. The maximum of Im det/‖S‖ was −4.3e-4. All four cases occurred.

### 2. Claim A (established)

- **Restriction.** By 055 (ii), Re h has at least nine non-negative eigenvalues on cl(𝔆₀) (check E: the minimum count of positive eigenvalues on random 𝔆₀ elements is 9). A real invertible h in cl(𝔆₀) therefore has at least nine positive eigenvalues, so t ≤ 1. Symmetrically, t ≥ 9 on cl(−𝔆₀).
- **Occurrence.** 𝔆₀ is invariant under real congruence, by its definition as Tᵀ diag(d) T. e^{iθ}TᵀT ∈ 𝔆₀ for θ ∈ (0, π/2). η = lim 𝓡_u. The negatives give t = 9, 10.
- **Independent proof** via the lemma's corollary (§1).

### 3. Claim B (established at every N for the stated class)

- **(a) Paths.** h(τ) = Λ(τ)ᵀh₀Λ(τ) is continuous and invertible, and h(0) is real with the inertia of h₀.
  - Let τ* = sup{τ : h real on [0,τ]}. On [0,τ*], h is real (by closedness) and invertible, so its signature is constant.
  - If τ* < 1, then Re h(τ) has the same signature near τ*, so h(τ) is real there by the lemma. This is a contradiction.
  - Only the quartic condition enters, so this holds for every regulator and every mass term.
- **(b) Single contours.** In a real basis with P = 𝟙 and h₀ = c(𝟙 − 2Σ_{j≤t} e_j e_jᵀ):
  - h = c(M − 2Σ ℓ_jℓ_jᵀ), with M = ΛᵀΛ and ℓ_j = Λᵀe_j.
  - For v = Λ⁻¹e_j: hv = cΛᵀ(e_j − 2e_j) = −cΛᵀe_j = −cMv.
  - With R and S real symmetric, v̄ᵀRv = Re(v̄ᵀhv) = −c·v̄ᵀ(Re M)v < 0 on the t-dimensional complex span. So Re h has at least t negative eigenvalues.
  - On {Re ℓ_jᵀx = 0 for all j}, of dimension at least 10−t, Re h ≥ c Re M > 0. So Re h has at least 10−t positive eigenvalues.
  - Hence the inertia is exactly (10−t, t). Check F found exact agreement on 167 random admissible contours over t = 0..10.
  - Then the lemma applies to each contour.
- **(c) Consequences.**
  - For real h, S_b(ΛX) is real for Hermitian X at every N, since commutators are anti-Hermitian. Check B, N=3 general X: |Im|/|S| < 6e-17.
  - The ε=0 integrand has modulus |w(ΛX)|, times the constant Jacobian. In polar coordinates ∫|w∘Λ| = ∫r^{deg+n−1}dr·∫_S|w∘Λ| = ∞.
  - Domination on limits follows as in 057 (iii): a dominating function for the family would dominate the pointwise limit.
- **t ∈ {0,1}.**
  - For t = 0, the path A = e^{iπτ/8}X has h = e^{iπτ/4}𝟙, Re M = cos(πτ/4) and Re iS_b = −sin(πτ/2)·S_E, using S_b^{𝟙} = S_E because Tr(CC) = −‖C‖² for anti-Hermitian C.
  - For t = 1 the path is 𝓡_u: 053, with u ∈ (0, 2/3) admissible and damped.
- **Per-index phases** (the scout's MY CHECK) are the special case h = diag(h₀_μ e^{iβ_μ}). Check I: every small nonzero perturbation violates the closed condition for t = 2..8, consistent with the lemma.

### 4. Claim C (cited; verified from the source)

- **Majorana condition.** Van Proeyen (3.25): a Majorana spinor exists for s−t ≡ 0, 1, 7 mod 8, for 2 mod 8 with η(−)^{d/2} = +1, and for 6 mod 8 with η(−)^{d/2} = −1.
- **Chirality.** (3.28): "MW spinor: s − t = 0 mod 4", from compatibility with the chiral projection.
- **Combined.** s−t ≡ 0 mod 8. Table 2 at d = 10 confirms MW for t ≡ 1 mod 4.
- **d = 10.** t ∈ {1, 5, 9} (check H).
- **IKKT content.** IKKT (2.1): "θ¹ and θ² are Majorana-Weyl spinors in ten dimensions having the same chiralities". The κ-gauge θ¹ = θ² = ψ (2.6) then gives a single MW spinor ψ.
- **Not used.**
  - The scout's Hull (7,3) remark.
  - The claim "Euclidean IKKT has a complex Pfaffian". Table 2 shows that d=10, t=0 admits Majorana (M⁻) but not MW, and that is all I use.

### 5. The Kontsevich–Segal / Witten comparison (established for the matrix side; literature side verified)

- **KS abstract (verbatim fragments from the fetch).** "postulating that the partition function and the correlators extend analytically to a certain domain of complex-valued metrics"; "Ordinary Riemannian metrics are contained in the allowable domain, while Lorentzian metrics lie on its boundary."
- **Witten (3.5):** Σ|Arg λ_i| < π, which is "Theorem 2.2 in [6]" (= KS).
- **Witten (3.6):** −(1∓iε)dx₁² + Σdx_j². He says "a Lorentz signature metric is on the boundary of the space of allowable metrics in two different ways". One sign gives the standard Feynman integral and the other "a complex conjugate Feynman integral". He adds that the two "cannot be considered 'close'".
- **Real metrics with t ≥ 2.** Σ|Arg| = tπ ≥ 2π. This is my own one-line consequence of (3.5).
- **Matrix side.**
  - Check G: h = diag(−(1−0.2i), (1+0.05i)·𝟙₉) is damped for e^{iS_b}. Its conjugate has a plane with Im det = −0.14 < 0, so it damps e^{−iS_b} instead.
  - −h has nine negative Re-eigenvalues, so it is in the −𝔆₀ class at −η.
  - Hence the Feynman / anti-Feynman pair corresponds to (𝔆 for e^{iS_b}, 𝔆̄ for e^{−iS_b}). The manuscript already notes that the opposite-sign convention gives the complex conjugate integral.
  - The 𝔆₀/−𝔆₀ pair is the sign of h₀.
- **Differences.**
  - The KS domain is conjugation-invariant, because its condition is on Re of an expression that includes √det g, and the sign of √det g carries the e^{±iS} choice. It is connected; Witten notes it is contractible onto the Euclidean metrics.
  - The matrix 𝔆 is not conjugation-invariant, because the i in e^{iS_b} is explicit. It is invariant under h ↦ −h, because S_b has no √det.
- **Status.** I cite KS only as a proposed axiom and use it as an analogy.

### 6. The fork: hypotheses of the 2 ≤ t ≤ 8 exclusion, relaxations explored, avenues open

| # | Hypothesis | Relaxation | Explored here? | Outcome |
|---|---|---|---|---|
| H1 | linear contours | non-linear contours / Lefschetz thimbles | no | open |
| H2 | colour-blind Λ | colour-mixing Λ ∈ GL(30,ℂ) at N=2 | yes, at first order (analytic proof + LP probe) | no first-order damping direction except complexified symmetries; non-perturbative statement open |
| H3 | Re iS_b ≤ 0 along the path | other representations of the limit (conditionally convergent, oscillatory) | no | open |
| H4 | regulator | any regulator, P arbitrary | yes | path statement (a) is regulator-independent; (b) needs P⁻¹h₀ = ±c |
| H5 | γ = 0 | mass term | yes | (a) is γ-independent |
| H6 | ε→0 at fixed N | N→∞ first | no | open |
| H7 | real h₀ | complex h₀ | reasoning | complex h₀ is complex-congruent to every real one, so it changes only the starting contour; it does not define a different real integral |
| H8 | fermion content MW (P2) | other content (bosonic, complex Weyl) | yes | the P1 statement alone already leaves t ∈ {0,1,9,10}, for any nonzero homogeneous w |
| H9 | P1 itself (damped representation) | does the limit exist at all for 2 ≤ t ≤ 8? | no | open |

**H2, colour-mixing linear maps at N = 2, first order (established; proposal only, not in the insert).**

*Setting.* x = (x¹,x²,x³) ∈ (ℝ¹⁰)³ and S = (1/4)Σ_{a<b} m_ab, with m_ab = h(x^a,x^a)h(x^b,x^b) − h(x^a,x^b)² and h = h₀ real of signature (10−t,t), 2 ≤ t ≤ 8. Take Λ(τ) = 1 + τ(K_R + iK_I), with K_I = (K_ab) a 3×3 array of real 10×10 blocks (K_ab feeds x^b into x^a). Re iS_b ≤ 0 along the path requires, to first order, g(x) := ∂_τ Im S = Σ_a ∇_aS·Σ_b K_ab x^b ≥ 0 for all real x.

*Claim.* g ≥ 0 forces K_I ∈ so(h₀)⊗𝟙₃ ⊕ 𝟙₁₀⊗so(3), the tangent space of the complexified symmetry group O(h₀,ℂ)×O(3,ℂ) of S, and then g ≡ 0.

*Proof.*
1. **Pair restriction.** Put x^c = 0. Then g = P_ab(x^a,x^b), because m_ac and m_bc are O(τ²) there.
2. **Off-diagonal blocks are scalar.** Under x^a → s x^a, x^b → x^b/s (which fixes the bivector), P_ab = c₀ + s⁻²c₋ + s²c₊ with c₊ = ∇_bS·K_ba x^a. c₊ is linear in x^b, so c₊ ≥ 0 for all x^b forces c₊ ≡ 0. That means h(x^a,x^a)K_ba x^a = (x^aᵀhK_ba x^a) x^a for all x^a, so K_ba = κ_ba𝟙. Likewise K_ab = κ_ab𝟙. Scalar shears drop out of P_ab, since ∇_bS·x^a = 0.
3. **Diagonal blocks.** Write K_aa = K + D and K_bb = K − D. P_ab = tr(adj(h|_E)(Kᵀh+hK)|_E) + (a part odd under x^a ↔ x^b). Both orderings must be ≥ 0, so the even part is ≥ 0 for every plane E. By the linearised form of the rigidity lemma (its proof uses only tr(adj R_E S_E) ≥ 0), Kᵀh + hK = 0. This holds for all three pairs, so every K_aa ∈ so(h), hence D ∈ so(h). The odd part is then 4h(x^a,x^b)·x^aᵀhDx^b, up to the factor 1/4 in S. It must vanish, which forces hD = 0, so D = 0. So all K_aa equal one K ∈ so(h₀).
4. **Cross terms.** What remains is κ_s (symmetric, zero diagonal). By Cayley–Hamilton, g = (1/2)tr(κ_s(trG·G − G²)) = −(1/2)tr(κ_s adj G), with G = xᵀhx. At G = diag(g₁,g₂,g₃) + εE_{ab}, which is realisable for p, q ≥ 2 with g's of either sign, this is ε κ_ab g_c + O(ε²). It takes both signs unless κ_ab = 0. ∎

*Checks.*
- `colour_first_order_checks.py` → `colour_first_order_checks.txt`, ALL PASS at t = 2, 5, 8:
  - the s² scaling;
  - ∇_bS·x^a = 0 to 7e-16;
  - P_ab = h₁₂·x^aᵀhDx^b to 4e-11, and its oddness;
  - symmetric κ gives g of both signs;
  - symmetry directions give g ≡ 0 to finite-difference accuracy.
- `colour_mixing_probe.py` → `colour_mixing_probe.txt`, a cutting-plane LP over K_I with structured sampling. Results:
  - Colour-blind (100 variables): t = 2 and t = 5 give LP optimum ≤ 1e-16; t = 1 converges to a positive direction (optimum 0.095, residual fresh-pool violation 2e-4 against a |g| scale of 0.66), as 𝓡_u predicts.
  - Colour-mixing (900 variables): t = 2 and t = 5 give optimum −7e-13 and −3e-14, with fresh-pool |g| ≤ 6e-11 against a scale of about 2. t = 1 gives a positive optimum of 0.083, with the cutting plane not fully converged after 8 iterations (residual violation 0.025 against a scale of 2.95).
  - This agrees with the analytic claim. It is numerical, not a proof.

*What this does not give.* First order is necessary, not sufficient. A path tangent to the symmetry orbit can still leave it at second order, and the colour-blind lemma is exact only because the contour enters through h alone. The non-perturbative colour-mixing statement stays open (avenue 2), so the insert keeps "no statement about linear maps that also mix the colour components".

**Ranked open avenues for E** (for the orchestrator):
1. **R2 of the scout (D1/E):** the time direction of the composite metric on a selected background. This is the step that would actually bear on ass:lorentzian. This package shows the target-contraction step can at best be conditional, and that the composite signature is a configuration property even for a (9,1) target.
2. **H2:** colour-mixing linear maps at N=2, non-perturbatively. Show that near a real 30×30 Λ the set {Re iS_b ≤ 0} consists of the complexified symmetry orbit of real contours, e.g. by a second-order version of the first-order proof above or by a normal form modulo O(h₀,ℂ)×O(3,ℂ).
3. **H9/H3:** existence of lim_{ε→0} I_ε for h₀ of signature (8,2) or (5,5) at N=2, bosonic first. This decides whether P1 is a genuine restriction or only a restriction of representation.
4. **H1:** thimbles for 2 ≤ t ≤ 8 at N=2.
5. **H6:** N→∞ first. Low feasibility.

## Claim classification

| Claim | Class |
|---|---|
| Im det(r+is) = tr(adj r · s) for 2×2 | established identity |
| Rigidity lemma (p, q ≥ 2 ⇒ h real) | established derivation (proved; numerically certified) |
| Claim A: real points of cl(𝔆) are t ∈ {0,1,9,10} | established (corollary of the merged 055 (ii); independent proof via the lemma) |
| (iii)(a) path statement, every N, any regulator, any γ | established, for linear colour-blind contours |
| (iii)(b) inertia for P⁻¹h₀ = ±c, and single-contour reality | established |
| (iii)(c) non-integrability at ε=0 and unavailability of domination | established |
| Paths to damped contours for t ∈ {0,1,9,10} | established (053 𝓡_u; explicit e^{iπτ/8}) |
| MW iff s−t ≡ 0 mod 8; t ∈ {1,5,9} in d=10 | cited, verified in Van Proeyen (3.25), (3.28), Table 2 |
| IKKT fermion is one MW spinor | cited, verified in IKKT hep-th/9612115 p. 2 |
| t ∈ {1,9} under P1 ∧ P2 | conditional result (P1 imposed; P2 supplied input) |
| KS allowability analogy | conjecture-level analogy (KS is a proposed axiom); the matrix-side facts are established |
| Feynman/anti-Feynman ↔ h, h̄ rather than 𝔆₀, −𝔆₀ | established on the matrix side; literature side verified (Witten p. 10) |
| Composite-metric signature depends on the configuration | established (pull-back of a (9,1) form to a 4-plane) |
| Colour mixing at N=2, first order: only symmetry directions | established (first order only; proposal, not insert) |
| Colour-mixing LP probe | numerical probe only |
| Lorentzian signature of the emergent metric | unresolved, not addressed |

## Proposed changes

### chapters/appH-microscopic-proofs.tex: one insertion, no deletions

- **Location.** A new paragraph immediately before the Problem E Status paragraph, after the 057 block. It ends "…the positive mass does not discharge Assumption~\ref{ass:lorentzian}."
- **Anchor (unique; count 1, line 1575 of the baseline):**
  ```
  \paragraph{Status.}
  Remains Assumption~\ref{ass:lorentzian}.
  ```
  The anchor is 61 bytes CRLF, sha256 a7c77412…26cc.
- **Placement.** The insert goes before the anchor, followed by one blank line. The anchor and everything else are kept verbatim.
- **Full text:** `proposals/059-signature-scan/appH_insert.tex`. It is ASCII and LF, with no trailing whitespace; the integrator converts it to CRLF. It is reproduced here:

```latex
\paragraph{Real target contractions of other signatures (algebraic at every \(N\)).}
Keep Definition~(A) and the notation of the three preceding paragraphs, but replace \(\eta\) in \(S_{\mathrm b}\) by a real symmetric invertible \(h_0\) with \(10-t\) positive and \(t\) negative eigenvalues, \(S_{\mathrm b}=-\tfrac1{4g_{\mathrm{YM}}^2}\sum_{\mu,\nu,\rho,\sigma}(h_0)_{\mu\rho}(h_0)_{\nu\sigma}\operatorname{Tr}[A_\mu,A_\nu][A_\rho,A_\sigma]\), and let the factor \(w(A)\) multiplying \(\mathrm e^{\mathrm iS_{\mathrm b}}\) be a homogeneous polynomial that does not vanish identically, such as \(1\) or a Pfaffian. On the contour \(A_\mu=\sum_\nu\Lambda_{\mu\nu}X_\nu\) put \(h=\Lambda^{\mathrm T}h_0\Lambda\). The formula for \(S_{\mathrm b}\) at \(N=2\) and the set \(\mathfrak C=\mathfrak C_0\cup(-\mathfrak C_0)\) are then those of the paragraph on linear contours that mix the indices, which is the case \(h_0=\eta\). Since \(S_{\mathrm b}\) is even in \(h_0\), the values \(t\) and \(10-t\) give the same integrand, with \(\mathfrak C_0\) and \(-\mathfrak C_0\) exchanged. At \(N=2\) the condition \(\operatorname{Re}\mathrm iS_{\mathrm b}\le0\) on the contour is \(\operatorname{Im}\det(h|_E)\ge0\) for every real 2-plane \(E\), the determinant being taken in a real basis of \(E\), and for \(N\ge3\) it implies this, by restriction to an \(\mathfrak{su}(2)\) block.

(i) \emph{Real boundary points.} By (ii) of the paragraph on linear contours that mix the indices, \(\operatorname{Re}h\) has at least nine non-negative eigenvalues on the closure of \(\mathfrak C_0\) and at least nine non-positive ones on that of \(-\mathfrak C_0\). So the real invertible forms in the closure of \(\mathfrak C\) are those with \(t\in\{0,1,9,10\}\), and all of these occur: \(\mathfrak C_0\) is invariant under real congruences, \(T^{\mathrm T}T\) is the limit of \(\mathrm e^{\mathrm i\theta}T^{\mathrm T}T\in\mathfrak C_0\) as \(\theta\to0^+\), and \(\eta\) is the limit of the \(\mathcal R_u\). This is an analogue, for the quartic weight of the matrix integral, of the allowable complex metrics proposed in~\cite{KontsevichSegal2021} as the domain to which quantum field theories continue analytically, which contains the Riemannian metrics and has the Lorentzian ones on its boundary. In a real basis diagonalising such a metric the condition is \(\sum_i|\operatorname{Arg}\lambda_i|<\pi\), Eq.~(3.5) of~\cite{Witten2021ComplexMetrics}, which a real metric with \(t\ge2\) violates also in its closed form. Two differences matter. \(\mathfrak C\) is invariant under \(h\mapsto-h\), whence the two classes and the values \(t=9,10\), whereas the allowable domain contains no negative definite metric. And~\cite{Witten2021ComplexMetrics} reaches a Lorentzian metric from the allowable domain in two ways, with time component \(-(1\mp\mathrm i\epsilon)\), which give the Feynman integral and its complex conjugate. For the matrix weight the corresponding pair is \(h\) and \(\bar h\). Since \(\operatorname{Im}\det(\bar h|_E)=-\operatorname{Im}\det(h|_E)\), for \(h\in\mathfrak C\) the form \(\bar h\) damps \(\mathrm e^{-\mathrm iS_{\mathrm b}}\), the opposite sign of the quartic term noted under Definition~(A), whose integral is the complex conjugate. The classes \(\mathfrak C_0\) and \(-\mathfrak C_0\) are not this pair. They are exchanged by the overall sign of the contraction, and \(\eta\) lies in the closure of \(\mathfrak C_0\) only, \(-\eta\) in that of \(-\mathfrak C_0\) only.

(ii) \emph{Rigidity.} Let \(h\) be complex symmetric with \(\operatorname{Im}\det(h|_E)\ge0\) for every real 2-plane \(E\), and let \(R=\operatorname{Re}h\) be invertible with at least two positive and at least two negative eigenvalues. Then \(h\) is real. For real symmetric \(2\times2\) matrices \(r,s\) one has \(\operatorname{Im}\det(r+\mathrm is)=\operatorname{tr}(\operatorname{adj}(r)\,s)\). Write \(S=\operatorname{Im}h\) and split \(\mathbb R^{10}=V_+\oplus V_-\), orthogonally for \(R\), with \(R\) positive definite on \(V_+\) and negative definite on \(V_-\). Let \(\lambda_1\le\dots\le\lambda_p\) be the eigenvalues of \(S\) on \(V_+\) relative to \(R\), and \(\nu_1\le\dots\le\nu_q\) those on \(V_-\) relative to \(-R\). A plane in \(V_+\), in an \(R\)-orthonormal basis, gives \(\lambda_1+\lambda_2\ge0\). A plane in \(V_-\) gives \(\nu_{q-1}+\nu_q\le0\). A plane spanned by \(e\in V_+\) and \(f\in V_-\) with \(R(e,e)=1=-R(f,f)\) gives \(S(f,f)\ge S(e,e)\), so \(\lambda_p\le\nu_1\). Hence \(0\le\lambda_2\le\lambda_p\le\nu_1\le\nu_{q-1}\le0\), and with the two sums all \(\lambda_i\) and \(\nu_j\) vanish. Finally, for \(e_1\in V_+\) with \(R(e_1,e_1)=1\) and \(R\)-orthogonal \(f_1,f_2\in V_-\) with \(R(f_k,f_k)=-1\), the plane spanned by \(\cosh a\,e_1+\sinh a\,f_1\) and \(f_2\) gives \(-\sinh(2a)\,S(e_1,f_1)\ge0\) for all real \(a\), so \(S(e_1,f_1)=0\) and \(S=0\). By continuity of eigenvalues, for \(2\le t\le8\) the real forms with \(t\) negative eigenvalues are therefore open and closed in the set of invertible complex symmetric \(h\) with \(\operatorname{Im}\det(h|_E)\ge0\) for all \(E\). In particular they are not in the closure of \(\mathfrak C\), which gives (i) again for these \(t\).

(iii) \emph{Contours.} Let \(2\le t\le8\). (a) Let \(\Lambda(\tau)\), \(0\le\tau\le1\), be continuous and invertible, with \(\Lambda(0)\) real and \(\operatorname{Re}\mathrm iS_{\mathrm b}\le0\) on every contour of the path. Then \(h(\tau)\) is real for all \(\tau\): it is real and of constant signature up to the supremum of the \(\tau\) at which it is real, and by (ii) beyond it. This holds at every \(N\), for every regulator and with any mass term, which do not enter the condition. (b) Suppose that in a real basis in which the regulator form \(P\) is the identity, \(h_0\) is diagonal with entries \(\pm c\), \(c>0\), as for Definition~(A) with \(h_0=\mathrm{diag}(\pm1)\). With \(M=\Lambda^{\mathrm T}P\Lambda\) and \(\ell_j\) the rows of \(\Lambda\) for the \(t\) negative entries, \(h=c(M-2\sum_j\ell_j\ell_j^{\mathrm T})\), and \(hv=-cMv\) on the span of the \(\Lambda^{-1}e_j\). If \(\operatorname{Re}M\) is positive definite, then \(\operatorname{Re}h\) is positive definite on the real \(x\) with \(\operatorname{Re}\ell_j^{\mathrm T}x=0\) for all \(j\), a subspace of dimension at least \(10-t\), and \(\bar v^{\mathrm T}(\operatorname{Re}h)v=-c\,\bar v^{\mathrm T}(\operatorname{Re}M)v<0\) on that span, so \(\operatorname{Re}h\) has the inertia of \(h_0\), as in (i) of the paragraph on the regulator for \(t=1\). By (ii), every linear contour with \(\operatorname{Re}M\) positive definite and \(\operatorname{Re}\mathrm iS_{\mathrm b}\le0\) then has real \(h\), whether or not a path leads to it. (c) On the contours of (a) and (b), \(S_{\mathrm b}\) is real at every \(N\), so none of them is damped, and at \(\epsilon=0\) the integrand has modulus \(|w(\Lambda X)|\), which is not integrable, since \(w\circ\Lambda\) is a homogeneous polynomial that does not vanish identically. The dominated convergence used for \(t=1\) in the paragraph on the regulated Lorentzian integral is therefore unavailable on every such contour, and on every invertible limit of such contours as \(\epsilon\to0\), whose \(h\) is again real, since a dominating function would also dominate the integrand at \(\epsilon=0\) on the limit. For \(t\in\{0,1\}\) paths ending on damped contours exist: the \(\mathcal R_u\) for \(h_0=\eta\), and \(A=\mathrm e^{\pi\mathrm i\tau/8}X\) for \(h_0=\mathbb 1\), with \(\operatorname{Re}M=\cos(\pi\tau/4)\mathbb 1\) and \(\operatorname{Re}\mathrm iS_{\mathrm b}=-\sin(\pi\tau/2)S_{\mathrm E}(X)\). For \(t\in\{9,10\}\) the same contours serve, by evenness.

(iv) \emph{Fermion content.} A Majorana--Weyl spinor exists in signature \((s,t)\) exactly when \(s-t\equiv0\bmod8\): the Majorana condition and the compatibility of the reality condition with the chiral projection, Eqs.~(3.25) and~(3.28) of~\cite{VanProeyen1999}, together leave these cases, as in Table~2 there. For \(s+t=10\) this means \(t\in\{1,5,9\}\). The content of~\cite{IKKT1997} is one Majorana--Weyl spinor.

So, for linear contours that do not mix the colour components, Definition~(A) and \(\epsilon\to0\) taken at fixed \(N\), two premises fix the signature of the contraction. (P1) The limit is obtained, as for \(t=1\) in the paragraph on the regulated Lorentzian integral, by dominated convergence on a damped linear contour reached from the Hermitian contour by a path as in (iii)(a). (P2) The supplied fermion is a single Majorana--Weyl spinor for \(h_0\). Then \(t\in\{0,1,9,10\}\cap\{1,5,9\}=\{1,9\}\), so \(h_0=\pm T^{\mathrm T}\eta T\) with \(T\) real and invertible. \(S_{\mathrm b}\) does not see the sign, and \(T\) turns the regulator into a positive definite form, for which that paragraph gives the same limit. (P1) alone leaves \(t\in\{0,1,9,10\}\), and (P2) alone admits \(t=5\). The form \(h_0\) contracts the matrix indices and is not the emergent metric. The induced tensor of Definition~\ref{def:matrix-coords-ext} is its pull-back by a configuration, and for \(h_0\) of signature \((9,1)\) the restriction to a four-dimensional tangent space is positive definite, Lorentzian or degenerate according to the configuration, so the signature of the composite metric is a property of the background and is not derived here. (P1) is a condition on the representation of the integral within linear contours, and (P2) is supplied content, since Equation~\eqref{eq:Smatrix} is bosonic. This is no statement about non-linear contours, about linear maps that also mix the colour components, about whether the limit exists for \(2\le t\le8\), about fixed \(\gamma>0\), about \(N\to\infty\) taken first, or about Definitions~(B) and~(C). The signature selected under (P1) and (P2) is that of a contraction of matrix indices, both premises are imposed, and Assumption~\ref{ass:lorentzian} is not discharged.
```

**Labels, references and citations used.**
- `\ref{def:matrix-coords-ext}`: ch03 L173, unique.
- `\eqref{eq:Smatrix}`: ch03 L143, unique.
- `\ref{ass:lorentzian}`: ch04 L322, unique.
- `\cite{IKKT1997}`: existing key.
- New citation keys, all absent from the bib before: `KontsevichSegal2021`, `Witten2021ComplexMetrics`, `VanProeyen1999`.
- No new labels.

**Cross-references to unlabeled paragraphs.** These follow the 055–057 convention of describing the paragraph by name:
- "the paragraph on linear contours that mix the indices" (055);
- "the paragraph on the regulator" (056);
- "the paragraph on the regulated Lorentzian integral" (053).

**Hashes** (from `apply_check.txt`):
- appH baseline: 569524 bytes, sha256 9443341b74f991d49fee3b08830dd44da7f9a12245922f52aaa193b0bd607bcd, CRLF.
- Insert LF: 9934 bytes, sha256 ac95c6691538edc112fbe03006481b729a4c79ae6a75dbcd1e2666b2e43e9680.
- Insert CRLF: 9946 bytes, sha256 a7afb1a510927c1b4f9e2dd54a2331e1e22a06ca433aed6dc959f3a4d151a33a.
- Resulting appH: 579472 bytes, sha256 daad5415810797c1f3abca428ab232ba6fbfca98e6973604b4ae8fcca6982e29, CRLF 3279, bare LF 0.

### bib/namcg.bib: append three entries (integrator only)

- **Placement.** Append after the last entry (ChouNishimuraTripathi2025), separated by one blank line, with CRLF line endings.
- **Entries.** Exact text, LF form in `bib_entries.bib`:

```bibtex
@misc{KontsevichSegal2021,
  author  = {Kontsevich, Maxim and Segal, Graeme},
  title   = {Wick rotation and the positivity of energy in quantum field theory},
  year    = {2021},
  eprint  = {2105.10161},
  archivePrefix = {arXiv},
  primaryClass = {hep-th}
}

@misc{Witten2021ComplexMetrics,
  author  = {Witten, Edward},
  title   = {A Note On Complex Spacetime Metrics},
  year    = {2021},
  eprint  = {2111.06514},
  archivePrefix = {arXiv}
}

@misc{VanProeyen1999,
  author  = {Van Proeyen, Antoine},
  title   = {Tools for supersymmetry},
  year    = {1999},
  eprint  = {hep-th/9910030},
  archivePrefix = {arXiv}
}
```

**Verification of each entry.**
- KS: arXiv listing fetched. Title and authors as above. Submitted 21 May 2021, hep-th. No journal reference is listed, so none is given.
- Witten: arXiv listing fetched. Title and author as above. v1 12 Nov 2021, v2 11 Feb 2022. No journal reference is listed. PDF read.
- Van Proeyen: arXiv listing fetched. Title and author as above, report number KUL-TF-99/37. No journal reference is listed. PDF pages 19–22 read.

**bib hashes.**
- Entries LF: 625 bytes, sha256 cf79b6c0…91d7.
- Entries CRLF: 649 bytes, sha256 c025a964…3c5a.
- namcg.bib now: 25976 bytes, a651fe60…c42b, CRLF.
- namcg.bib after the append (CRLF blank line plus entries): 26627 bytes, sha256 acbee1ce97a86bf8c68d1e4aca168f8d20ad7fb0df26b002af3c6338c93e738f.

### Stale passages elsewhere

None. The new paragraph contradicts no existing sentence.

def:matrix-coords-ext (ch03 L196–197) says "its Lorentzian signature is retained as Assumption~\ref{ass:lorentzian}". That is still true, so I propose no edit. See "Author decision needed" for an optional pointer.

## Verification scripts

All are in `proposals/059-signature-scan/`. Outputs are saved as `.txt`.

- **`rigidity_checks.py` → `rigidity_checks.txt`** (ALL PASS):
  - A: sympy identity.
  - B: S_b = (1/4)Σ minors with h = Λᵀh₀Λ for all t; evenness in h₀; N=3 su(2) block; real h ⇒ real S_b at N=3 for general X.
  - C: constructive certificate of the lemma, 2800 trials including adversarial ones.
  - D: sharpness at t = 0, 1.
  - E: Claim A eigenvalue count.
  - F: generalised inertia.
  - G: Witten comparison.
  - H: MW bookkeeping.
  - I: per-index phases.
- **`colour_first_order_checks.py` → `colour_first_order_checks.txt`** (ALL PASS): numerical checks of each step of the first-order colour-mixing proof (§6, H2) at t = 2, 5, 8.
- **`colour_mixing_probe.py` → `colour_mixing_probe.txt`:** cutting-plane LP probe of first-order directions, colour-blind and colour-mixing, at t = 1, 2, 5. Numerical, not a proof.
- **`apply_check.py` → `apply_check.txt`:**
  - Checks the baseline hash, anchor uniqueness and insert form.
  - Writes the would-be appH only outside the repository, refusing paths inside it.
  - Backslashes are built from byte 92.
- **Scratch build** in the session scratchpad, outside the repository:
  - Contents: namcg-book7.tex, chapters, frontmatter, figs and bib, with the resulting appH and the appended bib.
  - Sequence: pdflatex, bibtex, pdflatex, pdflatex, all with exit code 0.
  - Output: **367 pages** (baseline 365).
  - 0 undefined or multiply-defined references or citations, by log grep. No bibtex warnings.
  - The three new keys appear in the .bbl.
  - The scratch copy remains in the scratchpad; it is not in the repository.

## Decisions Taken

1. **Route.** The scout's "generalise 057's plane class" was not needed. The direct rigidity lemma is simpler and stronger: it is regulator- and mass-independent and holds at every N. Rejected: a per-index-phase-only N=2 statement, which is weaker and is subsumed.
2. **Scope of (iii)(b).** I stated the single-contour version only for P⁻¹h₀ = ±c. This is the exact generalisation of 056 (i). 056 (iii) shows the inertia is not fixed for general P, and the path statement (a) covers general P anyway.
3. **P1 wording.** P1 is phrased as the representation actually used by 053 (dominated convergence on a damped linear contour joined by a Stokes path). Rejected: a phrasing like "the integral is well defined", which (iii) does not exclude for 2 ≤ t ≤ 8.
4. **Weight w.** I kept a general nonzero homogeneous polynomial, so that the P1 conclusion does not depend on the fermion content. P2 enters only in (iv).
5. **Composite-metric scope.** I derived it from def:matrix-coords-ext itself (pull-back), rather than citing 1709.10480 or 2512.03161, which are not in the bib and which I did not open this session.
6. **Witten comparison.** I recorded it in the insert because the brief asked for it before any physical interpretation of −𝔆₀, and it blocks a misreading of 055–057. Rejected: leaving the scout's "word for word" claim unaddressed.
7. **Colour mixing.** I proved the first-order statement (§6, H2) but kept it out of the insert. It is first order only, and the insert's scope sentence remains accurate without it. Rejected: inserting a first-order claim that could be read as covering colour-mixing contours. Recommended instead: a follow-up package for the non-perturbative version.

## Milestone assessment

- **M2 (non-stopping):** a new bounded no-go. For 2 ≤ t ≤ 8, no linear colour-blind contour joined to the real contour by a path with Re iS_b ≤ 0 is damped. This holds at every N, for any regulator and any mass, and also contour by contour for Re M > 0 with Definition (A)'s regulator. It rules out the damped-representation route for those signatures.
- **Not M1.** Lorentzian signature is not derived. The selection of the target contraction holds only under the imposed P1 and the supplied P2, and the target contraction is not the emergent metric.
- **Not M3.** No merged claim is found wrong. The Witten-comparison correction concerns the scout report, not manuscript text.
- **Not a breakthrough.**

## Status-label recommendation

- **Critical-path set** (ch17 L700–733; Appendix H): A, B, C, D1, E, F, G-derived, N.
- **Affected label:** E only. It remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.
- **No change recommended.**

## Author decision needed

1. **Carried from the scout §8.5.** Can premises of the type P1 (a condition on how the regulated integral is represented) and P2 (supplied MW content) count toward "derived" for E?
   - My reading: they do not, under ch17 L692–698 and L739–742. P2 is an input, because eq:Smatrix is bosonic. And even full success here leaves the composite-metric signature to the background.
   - No text change is proposed on this basis.
2. **Optional wording, not proposed for integration here.** def:matrix-coords-ext (ch03 L196–197) and ass:lorentzian (ch04 L322–328) could carry a forward pointer: "the signature of the matrix-index form is fixed, up to sign, by the conditions recorded in Section~\ref{sec:status-E}, which are imposed".
   - This touches a definition and an assumption, so under CLAUDE.md 3(c) it would need a full scan and a separate package.
   - I do not recommend it now. The pointer could be misread as discharging the assumption.

No structural or emergence-changing option is proposed.

## Remaining open step

To close E, Lorentzian signature of the **emergent** metric must be derived without ass:lorentzian. After this package, the following would still be needed:

- (a) a selection of the target contraction from the matrix integral that does not impose P1 and P2, or a derivation of them. P2 cannot be derived from the bosonic eq:Smatrix.
- (b) a derivation that the selected background's composite metric has exactly one time direction on the claimed domain. This is scout R2, a D1/selection problem.
- (c) independence from deformations, taken in a stated order of limits.

Open items within this route:
- colour-mixing and non-linear contours;
- existence of the ε→0 limit for 2 ≤ t ≤ 8;
- N→∞ first.

## Special instructions for the gatekeeper

- **Re-derive the lemma, in particular the off-diagonal step.** It needs q ≥ 2 for f₂. Its mirror would need p ≥ 2; note that the proof uses p ≥ 2 only in the V₊-plane step.
- **Check the open-and-closed argument for (iii)(a).** It uses invertibility of Λ(τ), and not any regulator condition.
- **Check (iii)(b)'s inertia computation,** including the v̄ᵀ(Re h)v = Re(v̄ᵀhv) step for complex v.
- **Must not be asserted:**
  - that Lorentzian signature, or the signature of the emergent/composite metric, is derived;
  - that ass:lorentzian is discharged or weakened in the manuscript;
  - that KS allowability is a theorem about matrix integrals;
  - that the limit fails to exist for 2 ≤ t ≤ 8 (only the damped linear representation is excluded).
- **Literature.**
  - Witten pp. 8–11, Van Proeyen pp. 19–22 and IKKT pp. 2–3 were read as page images.
  - KS: only the abstract.
  - Statements I did not independently verify are not used in the insert: Segal's Oxford abstract wording ("but not metrics of other signatures"), Hull hep-th/9807127, 1709.10480, 2512.03161 and 2609.40183.
- **Integration ordinal** would be 57. No label change.
