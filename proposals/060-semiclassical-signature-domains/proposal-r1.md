# Proposal 060-semiclassical-signature-domains, round 1

## Result

This package tests the two supplied background classes against the semi-classical criterion of Steinacker, arXiv:2605.13294 (v2), and maps where the kinetic tensor of each is Lorentzian, Euclidean or degenerate. It makes no label change. Problems D and E stay OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL.

1. **The criterion, from the source.** I read it from the v2 TeX source and the arXiv v2 PDF. Δ_T is the maximal uncertainty of the quasi-coherent states, the ground states of Σ_a(T̄^a − t^a)² (Eq. 13). The proposed condition is max_{a,t'} |⟨⟨t|𝒜_a|t'⟩⟨t'|𝒜_a|t⟩⟩|^{1/2} ≪ Δ_T, with the absolute value and |t'−t| < Δ_T for Minkowski signature (Eqs. 16, 17).
   - The paper *proposes* it ("we propose"). It evaluates it with tree-level propagators in a Lorentz/Feynman gauge, and states that it fails for commutative backgrounds.
   - The equation numbers the scouts used (104, 115) are wrong for v2. The coupling is Eq. (89) and the late-time estimate is Eq. (100).
2. **First-order equivariant class (packages 050–052), flat point: bounded no-go.** This result is established at tree level in background Feynman gauge.
   - Δ_T = 0: the displacement operator has no eigenvector, and at finite N the eigenvectors are exact. So the criterion fails, as the paper says for commutative backgrounds.
   - For a normalised Gaussian state of width σ in p̃ = up, the fibre drops out by the unit Jacobian. The exact Gaussian integrals give a ratio of the two sides of g_YM/2σ² (Euclidean contraction) or 2^{-3/4} g_YM/σ² (η, Definition A).
   - A semi-classical window therefore needs a width σ ≫ g_YM^{1/2} that the background does not fix. The weight w of packages 051/052 is such a width, and it is supplied, not derived.
3. **Signature of the kinetic tensor.** These lemmas are exact.
   - (i) Gram positivity: with a positive semidefinite contraction on the frame span, γ is positive semidefinite, and so is any positive average. So no Lorentzian kinetic tensor arises in the Euclidean model. This is consistent with 2512.03161.
   - (ii) Sylvester: for a rank-4 frame that does not depend on the fibre, sig γ = sig(h₀|_W).
   - (iii) A fibre average of (3,1) tensors can have another signature.
4. **CP^{1,2} class (packages 045–049), conjugate coordinates T^a = M^{a4}, y^μ = M^{μ5}.** These results are exact in the Poisson limit.
   - E^{aμ} = ±mη^{aμ} does not depend on the fibre, so γ = m²η⁻¹Hη⁻¹ with H = Lᵀh₀L.
   - A new exact Lie-algebra identity gives H_{cc'}[T^c,[T^{c'},T^a]] = η^{c₀c₀}[tr(η⁻¹H)T^a − (η⁻¹H)^a_b T^b]. So the equation of motion with the h₀-contracted mass holds **iff H = cη, with γ = 3cη^{c₀c₀}**.
   - With h₀ of signature (9,1), which is what 059 gives under P1∧P2, this forces c > 0. Then W is timelike, γ > 0, and the kinetic tensor is **Lorentzian on all of m ≠ 0**. It vanishes identically at the bounce m = 0, and the frame is non-degenerate exactly on m ≠ 0.
   - **No selection.** The compact twin 𝔰𝔬(6), with the same identity and the same sign γ > 0, gives a positive definite kinetic tensor for spacelike W.
   - **Order of limits.** 𝔰𝔬(4,2) has no nontrivial finite-dimensional Hermitian representation. So within this family the non-zero finite-N solutions are compact and Euclidean, and **the Lorentzian member exists only for N → ∞ first**.
5. **Base coordinates as matrices (y^μ = M^{μ5}, the presentation behind 1709.10480).** These results are exact, and also checked on the explicit realisation.
   - γ = −3c.
   - At a fibre point the kinetic tensor has signature (3,1), with its negative direction along the spacelike fibre vector t.
   - The fibre average is diag(m², (2ℓ²−m²)/3, …). It is positive definite for 0 < m² < 2ℓ², degenerate at m = 0 and at m² = 2ℓ², and Lorentzian with reversed overall sign for m² > 2ℓ².
   - This is the "Euclidean pre-bounce" mechanism of 1709.10480, which I verified from its source. There the five-matrix version is Euclidean everywhere for κ² = 1 and Lorentzian only for κ² > 1, which needs two mass parameters.
6. **Coupling.** By SO(4,1) equivariance, ρ_M ∝ 1/|m|.
   - In the conjugate presentation this gives g_YM² ∝ |m|⁻³ at every m, extending Eq. (89). The coupling diverges exactly at the only non-Lorentzian locus, m = 0.
   - The paper's late-time estimate (Eq. 100) puts the semi-classical domain inside the Lorentzian one.
   - In the base presentation g² ∝ |2ℓ²−m²|^{-3/2}, which is finite on its Euclidean domain.

**Bottom line for E and D1.** Together with 059, the composite signature in the manuscript's CP^{1,2} presentation reduces to three things:
- the target contraction, (9,1) under P1∧P2;
- the real form of the background algebra, which is a supplied input;
- the classical equation, which forces compatibility but does not select the real form.

The Lorentzian member requires N → ∞ first and fixed γ > 0. That is exactly the corner that 053–059 leave open. Nothing here derives a signature, a background or a frame.

## Target and status

- **Targets:** scout route R2 (reports/sme-scout-20261108-after55.md, and R2 of after-50). Problems E and D1.
- **Problem E** (appH L1486–1489, verbatim): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
  - Original target (ch17 L395–399 and item 5 of L718): "Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})". Euclidean positivity and formal Wick rotation do not select it.
- **Problem D** (appH L600–603): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2 …".
  - D1 target (ch17 L331–343 and item 4): SO(3,1) gauge symmetry derived from the matrix algebra and condensate, with operators and field content; "the locked frame and its non-degeneracy on the claimed domain are derived, not assumed (Assumptions frame-lock and nondeg)".
- **Dependencies:** ass:lorentzian (ch04 L322–328), ass:frame-lock, ass:nondeg, def:matrix-coords-ext (ch03 L172–196), eq:Smatrix. Also the 050–052 blocks (appH L1377–1480) and the 045–049 conjugate-coordinate blocks (appH L2330, L2599–2774). Package 059's (P1, P2) is in appH L1575–1586.
- **Discrepancies:** none found between ch17 and appH for D and E. The critical-path set from ch17 L700–733 is A, B, C, D1, E, F, G-derived, N, consistent with the ledger.
- **Classification of the package:** PROGRAMME-CONDITIONAL throughout. The results are a bounded no-go and conditional sharpening. Nothing is DERIVED for the original targets.

## Source reading

- **Mode:** digest + targeted reads. `python scripts/make_digest.py --check` printed DIGEST CURRENT. The digest reports dirty-chapters: yes; the dirty Problem E part is 055–057 and 059, and I read it in full.
- **Read in full:**
  - appH Problem D, L596–700 (header, missing step, opening paragraphs) and L1377–1481 (blocks 050–052);
  - appH Problem E, L1482–1590 (all paragraphs, 053–059, Status);
  - appH L2599–2650 (blocks 045–047) and L2688–2720 (048, beginning of 049);
  - targeted passages at L2330, L2430, L2625 and L2636;
  - ch17 L320–400 and L685–755;
  - ch04 L290–340 (ass:lorentzian);
  - ch03 L95–205 (def:matrix-coords, def:matrix-coords-ext, eq:Smatrix).
- **Also read:** both scout reports, proposals/059 review-r2, and the ledger L286–443 (053–059). The ledger has no entries for 038–052; I used the appH text for those.
- **Not read in full:** the remainder of block 049 (L2721–2774) and Problem F outside the passages cited. No full scan is claimed, and none is due: this is a new conditional paragraph with no change to a definition, assumption, scope or status passage. Integration ordinal would be 58; the next scan is due at 60.
- **No unreadable files.**

## Research and reasoning

### 2.1 The criterion (verified from source)

I downloaded the arXiv source of 2605.13294 v2 (revised 19 Oct 2026) into an isolated scratchpad directory, read it, compiled a copy and read the arXiv v2 PDF with pdftotext. Equation numbers are those of the v2 PDF:
- (13): Δ_T := max_a Δ T^a|_t = max_a ⟨t|(T^a − **t**^a)(T^a − **t**^a)|t⟩^{1/2}, with |t⟩ the ground states of H_t = Σ_a(T^a − t^a 𝟙)²;
- (15): Δ_T ≈ (max |⟨t|ℱ^{ab}|t⟩|)^{1/2};
- (16), Euclidean: Δ^{(Q)}𝒜|_t := max_{a,t'} ⟨⟨t|𝒜_a|t'⟩⟨t'|𝒜_a|t⟩⟩^{1/2} ≪ Δ_T;
- (17), Minkowski: the same with |⟨…⟩| inside the root and max over |t'−t| < Δ_T (printed "|t'−t'|"). The restriction is there "because light-like long string modes might violate the bound".

The paper says "we propose" for both. Its estimates are tree level (Lorentz gauge with Feynman parameter) and one loop only through the O(𝒜⁴) argument. It says: "this criterion fails for commutative backgrounds (except for the diagonal elements)". The other numbers:
- Moyal coupling g²_YM = 1/Δ⁴ (34), with footnote g²_YM = g²ħ/Δ⁴;
- covariant dilaton ρ² = ρ_M √|γ^{μν}| (88) and g²_YM = r⁴/(2 sinh³τ) (89);
- late-time estimate Δ^Q𝒜 ≈ (Δ/(√2 r)) g_YM ≪ Δ_T = Δ/r (100).

**Observation (external paper, not for the manuscript):** its integral formula (64), ∫d⁴k e^{-k·k/2}/(k_η² − iε) = π²(1+i), is low by a factor 2. The correct value is 2π²(1+i), checked in s1 by a Schwinger closed form and by the δ-function imaginary part. This changes (63) and (99) by a factor 2, and Δ^Q by √2, so no "≪" conclusion changes.

### 2.2 First-order equivariant class, flat point

From appH L1416ff (051): X̂_a is multiplication by −u_a{}^b p_b, unitarily equivalent to −p̃_a ⊗ 1. Then S₂ = (1/2g²)η^{ab}Tr(A_a(ℰA)_b), and in background gauge the operator is multiplication by Q·Q, with Q = −p̃ + p̃'.

- **Δ_T.** H_t = Σ_a(p̃_a + t_a)² is a multiplication operator whose level sets have measure zero, so it has no eigenvector. Wavepackets concentrating at p̃ = −t have ⟨X⟩ = t and Δ_T → 0, so inf Δ_T = 0 and no quasi-coherent state exists. At finite N, for commuting matrices, the eigenvectors have Δ_T = 0 exactly. Off-diagonal entries have ⟨|A_ij|²⟩ = g²/|x_i − x_j|² > 0. So (16) fails: this is the paper's own remark, made explicit for this class.
- **Window.** For a Hermitian kernel, Tr(A_a A_b Q²) = ∫∫ Q² A_a(m,m') \bar A_b(m,m'). Each unordered pair appears twice, so a complex entry has weight (1/g²)Q²|A|². This gives ⟨|A_a(m,m')|²⟩ = g²/|Q|² (Euclidean) and ±i g²/(Q·Q + iε) (η, Definition A, sign set by η^{aa}). Then ⟨|⟨ψ|A_a|ψ⟩|²⟩ = g² ∫∫|ψ(m)|²|ψ(m')|² G(Q). Only the p̃-marginal of |ψ|² enters, because det u = 1. For the marginal N(t, σ²𝟙₄), δ = p̃ − p̃' ~ N(0, 2σ²𝟙₄).
  - Euclidean: E[1/|δ|²] = ∫₀^∞(1+2λs²)^{-2}dλ = 1/(2s²) = 1/(4σ²).
  - Lorentzian: E[i/(δ_η² + i0)] = ∫₀^∞ dλ (1+2iλs²)^{-1/2}(1−2iλs²)^{-3/2} = (1+i)/(2s²). The antiderivative is d/du[((1+iu)/(1−iu))^{1/2}] = i(1+iu)^{-1/2}(1−iu)^{-3/2}, with limit i at u → ∞. The modulus is 1/(2√2 σ²).
  - With Δ_T = σ the ratios are g/(2σ²) and 2^{-3/4} g/σ².
  - Maximum over t': in the Euclidean case it is at t' = t. The Gaussian average of the 4D Newtonian kernel 1/|x|² is radial and superharmonic, hence radially decreasing; s1(c) shows this numerically too. For η no larger modulus occurs at the sampled |d| ≤ σ along time, space and diagonal axes (numerical).
  - This is the same structure as the paper's Moyal case (ratio g_YM/√2 with g_YM = g/Δ²), with σ in place of Δ. So a commuting background has no intrinsic coupling: it is set by the supplied state width.
- **Loops.** Package 052 showed that at one loop, with the IKKT content and a common regulator, the second variation about commuting matrices vanishes (O(A⁴)). The tree form is therefore also the one-loop quadratic form at fixed ς, so the tree-level evaluation is not an artefact of truncating at tree level, within 052's hypotheses.

### 2.3 Signature lemmas

- (i) γ = Σ h₀(E^μ, E^ν) is a Gram matrix when h₀ ≥ 0 on the span, so it is positive semidefinite; positive combinations preserve this.
- (ii) If the 10×4 frame matrix has rank 4 and does not depend on the fibre, then γ = EᵀH̃E with an invertible 4×4 block, and Sylvester's law gives the inertia of h₀|_W. For a (9,1) form the restriction to a 4-plane has n₋ ≤ 1 by interlacing. The possible cases are (3,1), (4,0), or degenerate positive semidefinite (null plane); s2 samples only (3,1) and (4,0) generically.
- (iii) The base presentation (2.5) is an example.

### 2.4 Conjugate-coordinate class

- E^{aμ} = {T^a, y^μ} = ±mη^{aμ} is fibre-independent. This is appH L2625 ("exact in the Lie–Poisson algebra") and L2330. s3 re-checks it with residual 0 at 40 points.
- γ^{μν} = H_ab E^{aμ}E^{bν} = m²(η⁻¹Hη⁻¹)^{μν}.
- **Identity.** From [M^{a4}, M^{b4}] = −iη^{44}M^{ab} and [M^{ab}, M^{c4}] = i(η^{bc}M^{a4} − η^{ac}M^{b4}) we get [T^c,[T^{c'},T^a]] = −η^{44}(η^{ac}T^{c'} − η^{cc'}T^a), and contracting with H gives the displayed identity. s2 checks it symbolically for a general symmetric H in 𝔰𝔬(4,2) (c₀ = 4 and c₀ = 5), 𝔰𝔬(6) and 𝔰𝔬(4,1). The identity is odd under M → −M on both sides, so the i-convention does not matter.
- **EOM.** S_b + S_γ with the manuscript's signs gives [A^μ,[A_μ,A_ν]] = γA_ν (s4(i), finite differences). With A = LT the EOM is L[(tr P)𝟙 − P]η^{c₀c₀}T = γLT, with P = η⁻¹H. Since L has rank 4 and the T^a are independent, (tr P)𝟙 − P = (γ/η^{c₀c₀})𝟙, which holds iff P = c𝟙 (s2 solves it), with γ = 3cη^{c₀c₀}.
- **(9,1).** H = cη_S with η_S = (3,1) and c < 0 would have inertia (1,3), which is impossible since n₋ ≤ 1. And c = 0 would make W totally null of dimension 4, which is also impossible. So c > 0, W is timelike, and γ = 3c > 0 (η^{44} = +1).
- **Compact twin.** In 𝔰𝔬(6) the same E formula (Lie-algebraic, so on every orbit) and the same identity with η = δ give H = cδ, γ = 3c > 0 and a positive definite kinetic tensor. The classical equation therefore does not select between the real forms.
- **Finite N.** A Lie-algebra homomorphism ρ: 𝔰𝔬(4,2) → 𝔲(N) is zero or injective, since the algebra is simple. Subalgebras of 𝔲(N) carry the positive invariant form −tr(XY), so a simple subalgebra has a negative definite Killing form. 𝔰𝔬(4,2) has Killing inertia (8,7) (s2). Hence there is no nontrivial Hermitian N×N representation; 𝔰𝔬(6) ≅ 𝔰𝔲(4) has one. "Within this family" means four matrices T^I = L^I_a M^{ac₀} with exact Lie relations.
  - This is consistent with Liao–Maeta ("only exists in N→∞ limit", their abstract) and with 2605's remark that for finite N only approximate vacua are expected.

### 2.5 Base presentation and 1709.10480

Take y^μ = M^{μ5} as the four matrices, with c₀ = 5, η^{55} = −1, so γ = −3c. The point formula γ_pt = η_αβ M^{αμ}M^{βν} = ℓ²η + yy − tt follows from the orbit relation η_CD M^{AC}M^{BD} = ℓ²η^{AB}; it is in appH L2636 with c_θ, and s3(a, d) checks it with residual 4.5e-13.
- In the rest frame of y, t⁰ = 0 and |t|² = ℓ² + m². The pointwise eigenvalues are m² and ℓ², ℓ², −m², and the negative direction is along t (s3, |cos| = 1).
- The SO(3) stabiliser acts transitively on the fibre S² and the conditional measure is invariant. So [t_i t_j] = |t|²/3 δ_ij and [γ] = diag(m², (2ℓ²−m²)/3 ×3). s3 checks this by Monte Carlo at 14 points (residual ≤ 0.07, MC noise) and exactly at one point; the signature table is (4,0) for m²/ℓ² < 2 and (1,3) above.
- **1709.10480 (v3 TeX source read; JHEP 02 (2018) 033 via Crossref):**
  - Section "Lorentzian fuzzy hyperboloids": five matrices with g = diag(−κ², 1,1,1,1). The EOM 4r² + m̃₀² = 0 = (3+κ²)r² + m² has equal masses only for κ² = 1.
  - The averaged γ̃ = 3P_H is Euclidean for κ² = 1. The signature changes at cosh 2η₀ = (κ²+5)/(κ²−1), "provided κ²>1".
  - Abstract: "the brane is Euclidean 'before' the BB".
  - My four-matrix result is the same mechanism (fibre averaging, case iii). I do not claim it appears in that paper.
- **2512.03161 (v2 source read):** Euclidean IKKT; six 𝔰𝔬(1,3) generators solve the massless EOM with the Euclidean sum (re-checked in s2: all double commutators vanish); the effective metric is "Euclidean … with SU(2) isometry". This is consistent with lemma (i).

### 2.6 Coupling

- The map y^A = M^{A5} (A = 0..4) goes from the orbit to {y_A y^A = −ℓ²}. It is equivariant under SO(4,1) ⊂ SO(4,2) fixing index 5.
- The Liouville measure is SO(4,2)-invariant, and its pushforward is locally finite because the fibre is compact. So the pushforward is the unique invariant measure on SO(4,1)/SO(4), which is d⁴(y_i, m)/|y⁰| (s4(ii) checks boost invariance to 2e-10). In the coordinates y^μ, on each part m ≷ 0, this is d⁴y/|m|.
- So ρ² = ρ_M|det γ^{μν}|^{1/2} ∝ |m|³ (conjugate), which matches (89) because sinh τ = m/ℓ. In the base presentation ρ² ∝ |2ℓ² − m²|^{3/2} (s4(iii)).
- I make no claim that the criterion holds or fails near m = 0. The paper's estimate (100) is derived only at late τ.

### 2.7 Comparison with the original targets

- **E** needs the signature derived rather than retained. This package shows that, beyond the target contraction (059), the composite signature in the manuscript's class is set by the real form of the supplied background algebra, which is the open selection step. It also shows that the Lorentzian member requires N → ∞ first, and that the commuting point of the other class is not semi-classical. None of this derives the signature.
- **D1** needs the frame and its non-degeneracy derived on the claimed domain. In the conjugate presentation the frame is non-degenerate exactly on m ≠ 0, which is a property of the supplied class. The flat point of the first-order class needs a supplied width.

### 2.8 Fork: hypotheses and relaxations

**No-go 1 (flat point fails the criterion).** Hypotheses:
- H1: commuting background;
- H2: tree level, with the one-loop quadratic form equal to it under 052's hypotheses;
- H3: background Feynman gauge;
- H4: quasi-coherent states as in (13);
- H5: the proposed criterion (16)/(17).

Relaxations explored:
- H1 → width-σ states: a window σ ≫ g^{1/2} exists but needs a supplied scale.
- H2 → one loop: 052 gives no change at second order with IKKT content.
- H3: Δ^Q is gauge-dependent through Q_aQ_b terms. Not explored; it does not affect Δ_T = 0.

Open:
- curved members, where [𝔻_a, 𝔻_b] = ½ℛ𝒮 gives curvature-induced noncommutativity, including the de Sitter member in the regular representation;
- fermionic backgrounds (2605's discussion cites Aoki et al. as a possible rescue);
- coarse-graining scale derived from the integral.

**No-go 2 (no classical selection of the composite signature; the Lorentzian member exists only for N → ∞).** Hypotheses:
- G1: four generators T = L M^{ac₀} with exact Lie relations;
- G2: isotropic h₀-contracted mass;
- G3: tree-level EOM;
- G4: a simple real form.

Relaxations explored:
- G2 → anisotropic (1709.10480, κ): a Lorentzian domain exists, but needs two mass parameters, a supplied deformation;
- G1 → six generators (Liao–Maeta): Euclidean, by lemma (i);
- G1 → base coordinates: fibre averaging gives a signature change with an isotropic mass at γ < 0.

Open:
- one-loop effective action comparing the 𝔰𝔬(4,2) and 𝔰𝔬(6) members at N → ∞ (a dominance or selection test);
- approximate finite-N truncations of 𝔰𝔬(4,2), and whether they solve the EOM to controlled error;
- non-Lie backgrounds.

**Ranked open avenues:**
1. Selection between the 𝔰𝔬(4,2) and 𝔰𝔬(6) members at N → ∞, fixed γ > 0: compare one-loop effective potentials (IKKT content) on the two members. This is the step where a signature could be selected by the integral, not by hand. It bears directly on E and D1.
2. Curved members of the first-order class: Δ_T from ½ℛ𝒮, and whether any member passes (16)/(17). In particular the de Sitter member, where X_a = iE_{a4} in L²(SO(4,1)) decomposes into unitary irreps.
3. Conjugate presentation near the bounce: a fluctuation estimate valid at m → 0 (not only late τ), and the criterion for the factor K and the transverse modes of the product backgrounds.
4. N → ∞ first in Definition (A) at fixed γ > 0: whether the conjugate background is a saddle of the regulated integral (057 avenue 1, now with a concrete candidate).
5. Base presentation: a fluctuation estimate on its Euclidean domain 0 < m² < 2ℓ², i.e. whether a 1709.10480-type pre-bounce region is semi-classical.

### 2.9 Literature checked

**Read from source in this session:**
- 2605.13294 v2: TeX source and arXiv PDF; equation numbers from the PDF.
- 1709.10480 v3: TeX source; DOI 10.1007/JHEP02(2018)033 confirmed by the Crossref API (JHEP vol. 2018, issue 2, article 33).
- 2512.03161 v2: TeX source; arXiv abstract page (authors Henry Liao, Reishi Maeta; no journal ref).

**Not independently verified:**
- the scouts' WebFetch equation numbers, which are superseded;
- the existence of minimal SO(6) orbits with the analogous constraint (not used; the E formula is Lie-algebraic).

## Claim classification

| Claim | Class |
|---|---|
| Criterion (13), (16), (17) as stated in 2605.13294 v2; it is proposed there | input (cited, verified from source) |
| Flat point: Δ_T = 0, so the criterion fails | established (tree level, this class) |
| Gaussian-state values g²/4σ², modulus g²/(2√2σ²); ratios g/2σ², 2^{-3/4}g/σ² | established (exact Gaussian integrals; max over t' numerical for η) |
| Width σ ≫ g^{1/2} needed and not fixed by the background; w is a supplied width | established / input |
| Lemmas (i), (ii), (iii) | established |
| E^{aμ} = ±mη^{aμ} fibre-independent; γ = m²η⁻¹Hη⁻¹; rank 0 at m = 0 | established (Poisson limit; merged text plus re-check) |
| Lie identity; EOM iff H = cη, γ = 3cη^{c₀c₀} | established (exact) |
| With h₀ (9,1): c > 0, W timelike, Lorentzian on m ≠ 0 | conditional (on h₀, which 059 fixes only under P1∧P2, and on the supplied class) |
| 𝔰𝔬(6) twin, Euclidean at the same γ > 0 | established |
| No finite-dim Hermitian rep of 𝔰𝔬(4,2); Lorentzian member only for N → ∞ (within the family) | established |
| Base presentation: point signature (3,1) along t; average diag(m², (2ℓ²−m²)/3); signature table | established (exact plus numerical check) |
| 1709.10480 κ statements; 2512.03161 Euclidean metric | input (cited, verified from source) |
| ρ_M ∝ 1/|m|; g² ∝ |m|⁻³ and |2ℓ²−m²|^{-3/2} | established (Poisson limit; uses 2605's definition of g) |
| Semi-classical domain of (100) lies inside the Lorentzian domain | conditional (on 2605's late-time estimate) |
| Criterion near m → 0, for K and transverse modes, curved first-order members, one loop on CP^{1,2} | unresolved |
| Selection of the real form, W or the background; derivation of the signature | unresolved |

## Proposed changes

### chapters/appH-microscopic-proofs.tex (one insertion; nothing replaced)

- **Anchor** (unique, count 1, line 1588 of the working file): `\paragraph{Status.}` CRLF `Remains Assumption~\ref{ass:lorentzian}.` in Problem E.
- **Placement:** insert the block immediately before the anchor, followed by one CRLF blank line. The preceding bytes already end in a blank line, and the 059 paragraph ending "…and Assumption~\ref{ass:lorentzian} is not discharged." stays unchanged.
- **Kept:** all existing text.
- **Exact text:** `proposals/060-semiclassical-signature-domains/appH_insert.tex`. It is LF in the proposal and pure ASCII, with no tabs and no CR. The integrator converts it to CRLF; `apply_check.py` does this.
- **Hashes:**
  - insert: LF 10284 B, f2a08fbcd9e5ec46db6a79e43eff0324701e5fef973fd4a97a3c2525069994ee; CRLF 10304 B, feb6788dae063047f07c2178d4b4ebccf84fb3e6cb68637a848c05b2ed819dd2;
  - result appH: 590057 B, sha256 c0e28e0225281b80491cb1365952c0c38bbc362becd23e3fc2f7b6848840b45f, CRLF 3300, bare LF 0;
  - baseline matched: 579751 B, b6c505ad…5a8a.

The block is reproduced here:

```latex
\paragraph{The semi-classical criterion and the signature of the kinetic tensor on the supplied backgrounds (conditional; bounded no-go).}
[full text: see appH_insert.tex; 8 paragraphs: opening; Criterion; The flat point of the first-order equivariant class;
 Signature of the kinetic tensor (i)-(iii); Conjugate coordinates (with the displayed identity); Base coordinates as
 matrices; Coupling; closing scope paragraph ending "Problems~D and~E remain open and PROGRAMME-CONDITIONAL."]
```

The authoritative text is the file. It is not duplicated here, so the two cannot diverge.

- **Labels used, each verified unique:** sec:status-D, sec:status-F, eq:Smatrix, ass:lorentzian, ass:frame-lock, ass:nondeg, ch:vierbein-emergence. The block adds no new labels.
- **Citations:** Steinacker2026Weak, Steinacker2018BB and LiaoMaeta2025 are new. Definition (A) and S_γ refer to the first E paragraph by name.
- **Style:** one scoped closing sentence and no process language.

### bib/namcg.bib (append three entries)

- **File:** `bib_entries.bib` (906 B CRLF, 2227428977ea…83f8), appended after a CRLF blank line.
- **Result:** 27535 B, sha256 1a27efb32c924e20f57e12a54674d9f078f716ce5a59b89710719d0ac68cbe37, CRLF 922, bare LF 0. There are no duplicate keys.
- **Baseline matched:** 26627 B, acbee1ce…738f.

```bibtex
@misc{Steinacker2026Weak,
  author  = {Steinacker, Harold C.},
  title   = {Quantum spacetime and quantum fluctuations in the {IKKT} model at weak coupling},
  year    = {2026},
  eprint  = {2605.13294},
  archivePrefix = {arXiv}
}

@article{Steinacker2018BB,
  author  = {Steinacker, Harold C.},
  title   = {Cosmological space-times with resolved {Big Bang} in {Yang--Mills} matrix models},
  journal = {Journal of High Energy Physics},
  volume  = {2018},
  number  = {2},
  pages   = {033},
  year    = {2018},
  doi     = {10.1007/JHEP02(2018)033},
  eprint  = {1709.10480},
  archivePrefix = {arXiv}
}

@misc{LiaoMaeta2025,
  author  = {Liao, Henry and Maeta, Reishi},
  title   = {A New Type of Saddle in the {Euclidean} {IKKT} Matrix Model and Its Emergent Geometry},
  year    = {2025},
  eprint  = {2512.03161},
  archivePrefix = {arXiv},
  primaryClass = {hep-th}
}
```

### Stale passages elsewhere

None. The new paragraph does not contradict merged text:
- appH L2330 already distinguishes K from the induced tensor;
- L2430 (five-matrix presentation: no Lorentzian horizontal contraction) is consistent with lemma (i) and the H⁴ picture;
- the 059 closing sentence is narrowed further, not contradicted.

## Verification scripts

All are in `proposals/060-semiclassical-signature-domains/`, with outputs in `.txt`.

- **`s1_commuting_point_criterion.py` → `.out.txt`:**
  - Euclidean E[1/|δ|²] = 1/(4σ²), by closed form, quadrature and Monte Carlo (2e6 samples);
  - Lorentzian Schwinger closed form (1+i)/(2s²), numerically, with K = 1+i;
  - the 2605 integral formula: numeric 2π²(1+i) against the printed π²(1+i);
  - max over the shift d (Euclidean decreasing; Lorentzian on |d| ≤ σ);
  - det u = 1.
- **`s2_eom_real_forms.py` → `.out.txt`:**
  - the bracket convention reproduced;
  - the Lie identity for symbolic symmetric H in 𝔰𝔬(4,2) (c₀ = 4, 5), 𝔰𝔬(6) and 𝔰𝔬(4,1);
  - the solution condition P = c𝟙;
  - inertia of (9,1) restrictions;
  - the Liao–Maeta double commutators vanish;
  - Killing-form inertia: 𝔰𝔬(4,2) (8,7), 𝔰𝔬(4,1) (4,6), 𝔰𝔬(6) (0,15).
- **`s3_cp12_kinetic_signature.py` → `.out.txt`,** using the explicit realisation (`cp12_realisation.py`, copied from 045):
  - the orbit relation (8e-13);
  - E = ±mη⁻¹ (residual 0);
  - γ_pt = ℓ²η + yy − tt (4.5e-13);
  - the negative direction along t;
  - the fibre average and the signature table across m (Monte Carlo plus exact).
- **`s4_eom_sign_and_coupling.py` → `.out.txt`:**
  - EOM sign by finite differences;
  - hyperboloid measure and boost invariance;
  - exponents ρ² ∝ m³ and ∝ |2c − m²|^{3/2}.
- **`apply_check.py` → `apply_check.txt`:** baselines, unique anchor (built from chr(92)), insert and result hashes, CRLF counts, refs, labels and cites, duplicate bib keys. `--out DIR` writes patched copies outside the repository only.
- **Helper edit scripts:** `edit_eqnums.py`, `edit_wording.py`, `edit_wording2.py` (raw strings; already applied to appH_insert.tex).
- **Scratch build (outside the repository):**
  - steps: full copy of the sources, patched appH and bib, then pdflatex, bibtex, pdflatex, pdflatex;
  - result: PASS, **371 pages** (was 367), 0 undefined or multiply-defined references or citations, bibtex clean;
  - no overfull boxes in the inserted lines;
  - the three new bibitems resolve.
  - My removal of the scratch build directories (scratchpad build060, build2605) was denied. They are left in place and the denial was not worked around.

## Decisions Taken

1. **Sub-target.**
   - Chosen: both classes against (16)/(17), plus the signature domain. For the first-order class only the flat point was tested, because 051/052 rest on it and it is decisive. For the CP^{1,2} class the conjugate presentation is the manuscript's own (045–049).
   - The base presentation was added because it is the mechanism of 1709.10480, the comparison the task asked for, and it isolates lemma (iii).
   - Curved first-order members and the K factor were deferred (avenues 2–3). Folding them in would exceed what can be verified in one package.
2. **Placement.**
   - Chosen: one paragraph in Problem E, before Status, with the D1 non-degeneracy consequence in its closing sentence.
   - A second insert in Problem D was rejected: the result is one argument, and splitting it would duplicate the scope sentences.
3. **Equation numbers.**
   - Chosen: the arXiv v2 PDF numbering (13, 16, 17, 88, 89, 100).
   - The scouts' (104), (115), which come from a second-hand reading, were rejected.
4. **The factor-2 issue in 2605's Eq. (64).** Recorded in the proposal only. It is immaterial to every "≪" statement and is an external paper's matter.
5. **Bib entries.** Only the three sources read from source were added. Hislop–Longo, Kontsevich–Segal and the others are not touched.
6. **Wording "kinetic tensor"** rather than "composite metric" in the manuscript block. This follows 059's F1, since the composite or emergent metric is a manuscript term (ch04) that is not identified here.

## Milestone assessment

M2 (bounded no-go; non-stopping): this package rules out three things within stated hypothesis classes.
- (a) The semi-classical reading of the flat point of the first-order class under the 2605 criterion, without a supplied width.
- (b) Classical selection of the kinetic-tensor signature within the four-generator Lie family with an isotropic mass. The compact twin solves at the same sign.
- (c) Any finite-N exact Lorentzian member of that family.

The no-gos are bounded by hypotheses H1–H5 and G1–G4 (Section 2.8).
- **Not M1:** nothing is derived for D1 or E.
- **Not M3:** no merged claim is found wrong. The 2605 factor 2 is external.
- **Not M4 or M5.**
- **Not a breakthrough.**

## Status-label recommendation

The critical-path set from ch17 L700–733 and the ledger is A, B, C, D1, E, F, G-derived, N. Affected labels are D and E, which are unchanged: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. I recommend no label change.

## Author decision needed

None.

The carried question, whether premises like P1/P2 could ever count toward "derived" for E, is unchanged by this package. Both readings remain "no".

## Remaining open step

E still needs a derivation from the integral itself that (a) fixes the target contraction without P1/P2, and (b) selects a background whose kinetic tensor is Lorentzian on the claimed domain. In the manuscript's class, (b) means selecting the real form 𝔰𝔬(4,2) over its compact twin, which this package shows the classical equation does not do. It also means (c) controlling the limit N → ∞ first at fixed γ > 0, and then γ → 0.

D1 additionally needs the frame and its non-degeneracy derived, with the bounce m = 0 excluded from or treated on the claimed domain, and a semi-classical regime that does not rest on a supplied width.

The next computable step is avenue 1 (one-loop comparison of the two real forms at N → ∞).

## Special instructions for the gatekeeper

- **Do not let the text assert any of the following:**
  - that a signature is derived;
  - that the classical equation selects the Lorentzian member;
  - that the 2605 criterion holds near m = 0;
  - anything about K, curved first-order members or one loop on CP^{1,2}.
- **"Only for N → ∞"** is within the four-generator Lie family with exact relations. Check that the sentence says so.
- **Re-derive:**
  - the Lie identity by hand from the bracket;
  - c > 0 from the (9,1) interlacing;
  - the base-presentation average.
- **Re-run** s1–s4 and apply_check.
- **Check the equation numbers** against the arXiv v2 PDF; 2605.13294 has a v1 with different content.
- **Check the 1709.10480 statements** (κ² = 1 gives γ̃ = 3P_H; Lorentzian only for κ² > 1; the two masses) against its source section "Lorentzian fuzzy hyperboloids".
- **The Gaussian normalisation** uses 051's S₂ = (1/2g²)η^{ab}Tr(A(ℰA)). Each unordered kernel pair is counted twice, which gives ⟨|A|²⟩ = g²/|Q|².
- **The Moyal comparison** ("has the form of g/Δ²") is structural only; normalisations of g differ.
- **The scratch build** included bibtex; the integrator's `build_check.py` does not run bibtex, so bibtex must be run once at integration.
