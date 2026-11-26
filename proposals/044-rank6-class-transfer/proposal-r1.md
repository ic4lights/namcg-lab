# Proposal 044-rank6-class-transfer, round 1

## Result

The class transfer is done in the only class in which a matrix-model Einstein–Hilbert coefficient has been reported: product backgrounds M x K at the maximally supersymmetric (IKKT) content, with K a fuzzy space in the transverse directions. This is the route of SME scout R2 and of Steinacker 2303.08012.

What is established:

1. **Exact factorisation lemma (class-independent).** On any product background, with no mixed flux and with commuting M- and K-operators, the weighted one-loop heat trace of the IKKT content factorises exactly into M-only, K-only and mixed pieces:
   - str e^{-sH} = s0^K (v^M - 2σ^M) + s0^M (v^K - τ^K) - (1/2)(σ+^M τ+^K + σ-^M τ-^K) for the split d_M = 4;
   - str e^{-sH} = s0^K (v^M - σ8^M) + s0^M (v^K - 4τ2^K) - (1/2) σ8^M τ2^K for the split d_M = 7.

   This is checked with random non-commuting finite-dimensional operators and explicit so(10) Clifford algebras; the relative residual is below 1e-12.
2. **Order counting.**
   - The M-only and K-only terms start at fourth order in the flux of their own block.
   - The mixed term starts at order (2,2), where it equals -(1/8) v2^M v2^K exactly (relative difference 4e-12 and 2e-13 in the two splits).
   - **The vector index part never enters the mixed term**, because Σ^{ab}Σ^{ij} = 0 on the vector representation. The mixed term is a pure spinor index part.
   - The scalar heat trace of M enters only multiplied by the K-supertrace (v^K - τ^K).
3. **Two-derivative part, four-coordinate M.** This is NAMCG's four-coordinate Poisson class, which is Steinacker's basic brane of his Sec. 6. The K-dependent two-derivative induced action is
   -(1/32π²) ∫ [ (1/6) W_R ρR[g_ρ] + W_X ρ²X ],
   with:
   - W_R = ∫ ds s^-2 (v^K - τ^K)(s), of indefinite sign;
   - W_X = -(1/8) ∫ ds s^-2 τ^K(s) < 0, by the Peierls–Bogoliubov inequality.

   Both are finite without a cutoff and set by the K scale. The ρ²X part is exactly Steinacker's T·T mixed term (his Sec. 6.2).
4. **Axial torsion is sourced by the tensor modes.** On the two δρ = 0 (tensor) modes about constant θ̄, the following hold identically in the polarisation (exact rational arithmetic, four backgrounds):
   - V = 0;
   - 𝒯 = X/4;
   - (3/2)S² = X/2.

   So ρ²X acts as -4ρR[g_ρ]. Half of this is the teleparallel R term (r = -2). The other half is the axial torsion, which is not zero even on the on-shell null mode.

   Consequences:
   - c_T = W_R/6 - 4W_X. The mixed part has the sign of a scalar component, i.e. a positive induced EH in this class.
   - Steinacker's G_N corresponds to the R-coefficient -2W_X of the teleparallel presentation. On the tensor modes the effective coefficient is therefore 1/G_T = 2/G_N for the mixed part.
5. **Replica comparison.** On the same class, with the three replica prescriptions of the ledger:

   | replica | c_A | c_A - c_T |
   |---|---|---|
   | fixed-state (antiperiodic Dirac) | W_R/6 - 2W_X + 2·N_K·Λ² | 2W_X + 2N_K Λ² |
   | periodic | W_R/6 | 4W_X |
   | smooth | -W_R/12 | -W_R/4 + 4W_X |

   Here N_K = dim Mat(H_K). So G_A ≠ G_T in this class:
   - the periodic gap does not vanish for W_X ≠ 0;
   - the smooth gap vanishes only for W_R = 16 W_X, a condition on K;
   - the fixed-state gap is a cutoff-dependent Λ² term (the ledger value c_A = 2 at (6,2), carried by every K mode) plus the finite 2W_X.

   **What happens to the ϑ/X obstruction of 041–043.** The vector X obstruction (weight κ_X) disappears: the vector index part cancels against the Dirac fields at the a_1 level and is absent from the mixed term. In its place there is a Dirac-index (axial-torsion) mismatch. The finite gap would vanish, with the same index density and cone value, exactly for tensor modes that source neither the axial nor the vector torsion.
6. **Rank-6 classes.**
   - **Product M x K.** Its rank is that of M, from merged 011.
   - **D-coordinate brane (009 class).** Two exact results:
     - The scalar operator is -λΔ_ĝ with ĝ = (√|g|/ρ)G, |det ĝ| = |det g|, and its a_1 density is (1/6)ρR[ĝ] pointwise. Since ρ is constant, the scalar part is exactly ρ × EH(ĝ): Einstein on every polarisation.
     - The linearised Einstein operator of ĝ has rank min(6, D-1) on the first-order image; this is exact rational, D = 4..11.
   - **Brane M ⊂ R^7 with K ⊂ R^3 (bending no-go).** The mixed-term index density X_7 contains the transverse bending term (p·p)(p·K·p)|φ|². This is fourth order in p, checked exactly. The EH form of ĝ on those modes is second order in p. So no single G_T exists on the transverse polarisations at the leading symbol whenever the K flux is nonzero.
   - **CP^{1,2} x K.** This is the structure S²_n ×̄ M^{3,1} × K of Steinacker's Sec. 7, with generators matching 013 (verified in 1901.03522 eq. (2.21)). It is the only rank-6 class not excluded. Its decisive datum is not computed: the Dirac index density on the six level-one modes, and whether those modes source the axial torsion.

What is **not** established:
- No G_eff value or sign, since W_R is indefinite and K is not constructed.
- No closure of B or F.
- Nothing for D1 or E.
- The CP^{1,2} computation.

## Target and status

Current labels, quoted verbatim from Appendix H; they agree with the Chapter 17 passages `sec:ch17-bearing` and `sec:ch17-coeff`:
- **Problem F** (`sec:status-F`, L1366): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
  - Ch17 original target: "Problem F has A,B,C and the sign/scheme dependence of G_eff computed from the specified operators; G_eff is not an input."
- **Problem B** (`sec:status-B`, L45): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
  - Ch17 target: Assumption EE as a lemma, including fixed-volume variations of the non-conformal tensor block, with no use of Assumption dictionary.
  - The sub-target used here is the G_T = G_A consistency (normalisation paragraph, L174).

Critical-path set: Ch17 `sec:ch17-done` lists A, B, C, D1, E, F, G-derived and N. Appendix H agrees; no discrepancy was found.

Dependencies:
- F depends on D1 (ghost content), E (continuation) and the class choice.
- B depends on A (state and replica) and on F (which class carries the Einstein form).

Completion classification of this package's results: **PROGRAMME-CONDITIONAL**. Nothing is DERIVED.

## Source reading

**Full scan.** I read every file of the current manifest (30 files) in full:
- `chapters/ch01`–`ch18`;
- `appA`–`appG`;
- `appI`–`appL`;
- `appH`, in chunks covering L1–399, 400–1361, 1362–2369 and 2370–2873.

Digest: `scratch/digest.md` reported DIGEST CURRENT with `dirty-chapters: yes`, so CLAUDE.md 3(d) applies. The dirty diff (`git diff`) was read in full. It is exactly the accepted 043 appH block before `\section{Problem C}`, the ch07 L227 sign fix, and the Chen2022 bib entry.

Also read:
- `proposals/strategy-20261025/assessment.md`;
- `reports/sme-scout-20261025.md`;
- `proposals/043-…/review-r1.md` and `review-r2.md`;
- the ledger entries 005–043;
- `MILESTONE.md`;
- the 009 rank script.

No unreadable files.

## Research and reasoning

### 1. Class choice

The task offered three candidate classes:
- (i) CP^{1,2} (013);
- (ii) an embedded brane with D ≥ 7 coordinates (009);
- (iii) the fuzzy-KK route M × K (SME R2).

Why the fuzzy-KK route at the IKKT content:
- At (6,2) the Λ² and log EH terms vanish identically (026, 031).
- In every merged class the only reported EH entry point is a mass or KK scale. Merged 026 says "Steinacker's route needs fuzzy extra dimensions", and merged L2103 is consistent with this.
- Without K, the D-coordinate brane at IKKT content also has no Λ² term.
- The F-chain in CP^{1,2} without K (023–040) is a diminishing-returns line.

So the decisive structure is that of the mixed M–K term, and the first package must establish that structure class-independently. It can then be applied to the three M-classes: four-coordinate (rank 3), D_M = 7 brane (rank 6), and CP^{1,2} (rank 6).

**Structural match with Steinacker, from fetched full texts.**

From 2303.08012:
- Sec. 4.1 eq. (4.5)–(4.9): frame E^{aμ} = {T^a, x^μ}; effective metric G = ρ^{-2}γ; torsion T^{ab μ} = {F^{ab}, x^μ}. This T^{abμ} is the NAMCG T^{αβμ} = Θ^{μρ}∂_ρΘ^{αβ} of the merged torsion paragraph (L2108).
- (4.11)–(4.13): the axion is the totally antisymmetric torsion, which the equations of motion make exact (T̃ = -2∂ϑ̃). There is also the teleparallel identity for R.
- (4.16)–(4.18): one-loop formula, with vector weight 1, spinor weight -1/2, ghosts -2, and Σ^{(ψ)} = (i/4)[Γ,Γ]. These are the weights used here.
- Sec. 5: basic brane M with T^μ = X^μ, i.e. the NAMCG four-coordinate class. Without K the local action is higher-derivative.
- Sec. 6, (6.9): V4 decomposes into M, K and mixed 2F^{μν}F_{μν}F^{ij}F_{ij}.
- (6.17): the K contribution is evaluated as an effective potential.
- (6.22)–(6.32): the mixed term becomes T·T·G, and then R + (1/2)T̃T̃ + dilaton. "For T̃ = 0 = ∂ρ we recover the Einstein–Hilbert action".
- Sec. 7, (7.1)–(7.6): CP^{1,2} = S²_n ×̄ M^{3,1}, F^{μν} = -{t^μ, t^ν}; mixed M–K term as in (6.24).

From 1901.03522 (2.21): X^a := r M^{a5}, T^a := R^{-1} M^{a4}. This matches NAMCG 013 (T^a = M^{a4}/R, y^μ = M^{μ5}/R).

So the S²-bundle structure the SME asked to check does match the NAMCG CP^{1,2} leaf, with T^a as the background and y^μ as the base, up to normalisation.

**Imported from Steinacker: nothing as a result.** The structure is used as a comparison, and every statement in the insert is derived here.

### 2. Factorisation lemma (derivation)

All IKKT fluctuation operators in background gauge have the form H_i = H_0 ⊗ 1 + Σ_i^{AB} ⊗ 𝔽_AB:
- Σ_i is the vector (10), spinor (16, Weyl) or trivial (ghost) representation of so(10);
- 𝔽_AB is the action of F_AB = {X_A, X_B}.

The merged L2295 paragraph has this structure for CP^{1,2} with inert transverse matrices.

On a product background:
- H = H_M ⊗ 1 + 1 ⊗ H_K;
- 𝔽_ab acts on M only and 𝔽_ij acts on K only;
- F^{ai} = 0.

Then:
- **Vector.** R^10 = R^d ⊕ R^{10-d}, and Σ_V^{ab}, Σ_V^{ij} act on the two summands separately. The vector heat trace is V^M s0^K + s0^M V^K, exactly.
- **Spinor.** Build Γ^a = γ^a ⊗ 1 and Γ^i = γ_5^M ⊗ γ^i_K. Then Σ^{ab} = σ^{ab} ⊗ 1 and Σ^{ij} = 1 ⊗ σ^{ij} commute, and 16 = (2+,4+) ⊕ (2-,4-) for d = 4 or (8,2) for d = 7. The spinor heat trace factorises blockwise.
- **Ghosts.** -2 s0^M s0^K.

Writing V = d·s0 + v etc. gives the stated formulas. The s0^M s0^K coefficient is 4 + 6 - 2 - 8 = 0, and for d = 7 it is 7 + 3 - 2 - 8 = 0.

Order counting:
- **Vector index part.** The first-order vector index part vanishes because tr Σ = 0.
- **Second order.** Dynkin indices give v2^M = 2(σ2+ + σ2-) for so(4), v2^K = τ2+ + τ2- for so(6), v2^M = σ8 for so(7) and v2^K = 4τ2 for so(3). So the first two terms have no second-order part.
- **Third order.** The structure-constant parts cancel with the same index weights. The so(6) d-symbol parts cancel between 4 and 4̄, because odd traces flip sign under conjugation. Hence c03 = c30 = 0, checked.
- **Mixed term.** It is -(1/2)(σ+τ+ + σ-τ-) = -(1/4)στ - (1/4)(σ+-σ-)(τ+-τ-). The second part is odd in each orientation and starts at order (2,3). With τ2+ = τ2- (conjugate representations, even order), c22 = -(1/8) v2^M v2^K.

**Positivity of τ^K.** By the Peierls–Bogoliubov inequality, Tr e^{A+B} ≥ Tr e^{A} exp(Tr(B e^A)/Tr e^A) with A = -s h ⊗ 1 and B = -s Σk. Since Tr(B e^A) ∝ tr Σ = 0, we get τ^K ≥ 0. Checked: the minimum of τ^K/s0^K is > 0 over 20 random draws × 4 values of s.

### 3. Two-derivative densities and coefficients (4-coordinate M)

Inputs from merged text:
- s0^M has a_1 density (1/6)ρR[g_ρ] (L1943).
- The vector index density is ρ²X (L1982; √G a_1(O_v) = (4/6)ρR + ρ²X).
- The Dirac index density is (1/2)ρ²X (L189).

Γ_E = -(1/2)∫ds/s str. The heat trace is (4πs)^{-2}[… + s·density]. Hence Γ ⊃ -(1/32π²) ∫ds s^{-2} (…). This gives W_R and W_X as stated, with W_X = -(1/4)·(1/2)·∫ds s^{-2} τ^K.

Units: c, from Γ ⊃ -(1/32π²) c ∫ρR, so a scalar component with Λ² gives c = Λ²/6. This matches merged S = (Λ²A_G/8π)c and 1/G = cΛ²/2π (L307).

On-mode values. A new exact check (s2) on the δρ = 0 modes gives:
- V = 0;
- 𝒯/X = 1/4;
- (3/2)S²/X = 1/2;
- the merged identity X = 2𝒯 + (3/2)S_{λμν}S^{λμν} + 2V² is verified.

With R ≅ -𝒯 (the merged identity √G(R + 𝒯 + 2∇V) = 0, up to a total derivative) this gives ρ²X ≅ -4ρR. Hence c_T = W_R/6 - 4W_X.

Teleparallel presentation: X = -2R + (3/2)S² + 2V², i.e. r = -2.

**Area.** The cone is on the M chart (pulled back), so the factorisation holds on the cover. The cone index parts per 4-component Dirac field, unweighted, from merged L189/L194/L200:
- antiperiodic -1/3 - 4/6 = -1;
- periodic 0;
- smooth: -(1/2) × the ρR coefficient, i.e. 0 for the X density in the torsion reading (L215).

The vector cone index part is 0 for the pulled-back gluing.

The mixed cone term is -(1/4)σ_cone τ^K. It has the same s-weighting as the bulk: the cone term ∝ s^{-1}A against the bulk (4πs)^{-2}s, giving the same ∫ds s^{-2} τ^K. So c_A^{mix} = (-2)W_X for fixed-state and 0 for periodic and smooth.

The scalar part gives c_A = W_R/6 for fixed-state and periodic, and -W_R/12 for smooth.

The first term's cone gives the Dirac excess 2 per K mode at order Λ², while its bulk two-derivative part is 0.

s4 tabulates all of this.

### 4. D-coordinate brane: scalar density and rank

O_s = -ρ^{-1}∂(ρK∂) with K = θ^T g θ, and ρ = 1/|Pf θ| constant in Darboux coordinates. With λ := √|g|/ρ and ĝ := λG:
- √ĝ ĝ^{-1} = ρK;
- λ/√ĝ = 1/ρ.

Hence O_s = -λΔ_ĝ. In Laplace form on G this is -Δ_G - ∂lnλ·∂, so E = ½□lnλ + ¼|∂lnλ|² (NAMCG sign). The 4D conformal formula then gives √G(R_G/6 - E) = (1/6)(√ĝ/λ)R[ĝ] = (1/6)ρR[ĝ]. For D = 4 (λ = 1/ρ) this reduces to merged L1943.

s3 checks:
- (i) the algebra, both signatures;
- (ii) the density at a random jet, exactly;
- (iii) the rank of linearised Einstein of ĝ on the 009 first-order image: min(6, D-1). The Hamiltonian gauge is a ĝ-diffeo because δ ln λ = ½ tr(g^{-1}δg) = p·ξ_H = 0.

**Bending.** X_D = -tr(B_σB^σ) = g^{ρλ}∂_ρΘ^{IJ}∂_λΘ_{IJ}, using θGθ^T = g^{-1}. On a transverse wave, δΘ^{ai} = θ^{aν}∂_νφ, so X_D ⊃ 2 g^{ρλ}K^{νκ}∂_ρ∂_νφ ∂_λ∂_κφ. This gives an L⁴ coefficient of (p·p)(p·K·p)|φ|² after phase averaging, which s3 (iv) confirms exactly.

EH(ĝ) on these modes:
- δĝ at first order is algebraic in φ (∝ IIφ at the point);
- the quadratic EH form is ∝ p²(δĝ)²;
- the linear term in δĝ^{(2)} ~ ∂φ∂φ multiplies the background Einstein tensor ~ II², and the ∂∂δĝ^{(2)} pieces are total derivatives.

So EH(ĝ) is O(p²II²): different homogeneity, not proportional.

For d_M = 7 the mixed term multiplies the so(7) spinor index part, which at a_1 equals the vector index part (T(8) = T(7), s1).

### 5. Literature checked

- **Steinacker 2303.08012** (JHEP 05 (2023) 129, bib key `Steinacker2023`, already in bib): full text fetched via arXiv PDF; sections 4–7 read.
- **Sperling–Steinacker 1901.03522** (`SperlingSteinacker2019`, already in bib): full text fetched; Sec. 2 generator definitions (2.21) read.
- **IKKT1997**: already in bib; used only for the content.
- **Peierls–Bogoliubov inequality**: standard; no citation added.
- **Not independently verified**: Steinacker 2110.03936 (not fetched; not cited). Also the claim that Steinacker's evaluation omits the curvature term of the K-only contribution: this is stated only as "not given there" for Sec. 6.1, based on reading eqs. (6.10)–(6.18).

### 6. Comparison with the original targets

- **F.** The original target is computed A, B, C and the G_eff sign. This package computes the structure of the K-induced two-derivative coefficient (W_R/6 - 4W_X) and the sign of its mixed part (positive). The sign of W_R and the construction of K remain open, so F stays OPEN.
- **B.** The original target is EE as a lemma. The G_T = G_A sub-target fails in this class for all three ledger replicas, so B stays OPEN.

### 7. Hypothesis class of the no-gos, relaxations and open avenues

Hypotheses:
- H1: product background with no mixed flux and commuting factors;
- H2: IKKT content;
- H3: Poisson limit on M with the local heat-kernel expansion;
- H4: one loop;
- H5: the ledger replicas (fixed-state, periodic, smooth);
- H6: off-shell quadratic form on the δρ = 0 modes about constant θ̄ (4-coordinate M);
- H7: frozen coefficients / leading symbol for the brane bending;
- H8: orientation-even part of the mixed term.

Avenues explored in this package:
- **On-shell (H6).** The axial torsion is nonzero on the on-shell null mode (s2), so the equations of motion do not remove it at first order. Quadratic invariants vanish on single null waves, so the comparison remains off-shell.
- **Other rank-6 class (H1 kept, M varied).** The brane gives the bending no-go. The scalar part is Einstein on all six polarisations (a positive sub-result).
- **Other replicas (H5).** All three ledger replicas were checked; none closes.

Ranked open avenues:
1. **CP^{1,2} (finite fibre n) × K.** Compute the M-Dirac index density (D_M² = -□ + Σ_S·𝔽, a Casimir-type operator; cf. merged 041 for the vector) on the six level-one amplitudes, and test whether they source the axial torsion of the frame {T^a, y^μ}. If not, the finite fixed-state gap closes; the Λ² excess would remain.
   - This relaxes H3 on the fibre, using Steinacker's finite fibre.
   - It is the only route left in which the finite G_A = G_T can hold.
2. **The Λ² Dirac excess of the fixed-state replica.** This is the generic SUSY "entanglement counts B + F, Sakharov counts str" tension, and it is independent of the class. The relaxation is the replica selected by the matrix state (Problem A): edge modes or a holonomy contact of modulus 2 per Dirac.
3. **Non-product backgrounds (H1).** With mixed flux F^{ai} ≠ 0 the vector index part enters the mixed term again. One test is a K fibred over M, e.g. a brane in R^7 with K in normal directions that carry II.
4. **The orientation-odd mixed term for chiral K (H8).** A Nieh–Yan/Pontryagin-type parity-odd density times the su(4) d-symbol of the K flux.
5. **The sign of W_R for explicit K** (fuzzy S², S²×S²) and its ratio to W_X: the G_eff sign in this class (F).
6. **The brane in the regime p ≪ |II|** (H7), and the Gauss–Codazzi-consistent background.

## Claim classification

| # | Claim | Class |
|---|---|---|
| 1 | Exact factorisation of the IKKT weighted heat trace on product backgrounds (d=4, d=7 splits) | established identity (algebraic; numerical check 1e-12) |
| 2 | M-only/K-only terms start at 4th order; mixed starts at (2,2) with -(1/8)v2^M v2^K; vector absent from mixed term | established (Dynkin/conjugation identities; numerical) |
| 3 | τ^K ≥ 0, hence W_X < 0 | established (Peierls–Bogoliubov; numerical check) |
| 4 | Two-derivative K-dependent density (1/6)W_R ρR + W_X ρ²X in the 4-coordinate class | conditional (Poisson limit, local heat-kernel expansion on M, product background, one loop) |
| 5 | On δρ=0 modes: V=0, 𝒯=X/4, (3/2)S²=X/2 identically in polarisation | established for constant θ̄, Euclidean (exact rational, 4 backgrounds) |
| 6 | Axial torsion nonzero on on-shell null δρ=0 mode | established at 3 sampled Lorentzian backgrounds (exact algebraic) |
| 7 | c_T = W_R/6 - 4W_X; mixed part positive | conditional (claims 4–5, Euclidean sign convention of the class) |
| 8 | c_A for fixed-state/periodic/smooth replicas; G_A ≠ G_T unless W_X = 0 (smooth: unless W_R = 16W_X) | conditional (ledger replica prescriptions and cone values as inputs) |
| 9 | Fixed-state Dirac cone value -1 equals r=-2 teleparallel R-coefficient of the Dirac index density | observation (equality of two numbers, not derived) |
| 10 | D-coordinate class: O_s = -λΔ_ĝ, density (1/6)ρR[ĝ], |det ĝ| = |det g| | established (exact algebra + standard conformal formula; jet check) |
| 11 | Linearised Einstein rank of ĝ = min(6, D-1) on first-order image | established at one exact-rational draw per D (frozen data), generic by semicontinuity |
| 12 | Bending term (p·p)(p·Kp)|φ|² in X_7; EH(ĝ) O(p²) on transverse modes; no single G_T | established at frozen coefficients (exact check at one background + derivative counting) |
| 13 | NAMCG CP^{1,2} class = Steinacker's S²_n ×̄ M^{3,1} (T^a = R^{-1}M^{a4}, X^a = rM^{a5}) | literature, verified by fetched full text |
| 14 | Steinacker's mixed term = ρ²X part; his G_N ↔ -2W_X | conditional identification (matching of definitions verified textually; normalisations not reproduced) |
| 15 | CP^{1,2} × K would close the finite fixed-state gap if axial torsion not sourced | conjecture/criterion (unresolved computation) |
| 16 | No G_eff value or sign; no closure | unresolved |

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`

- **Placement.** The new paragraph goes at the end of the Problem F ledger, after the last F block (the merged 041 paragraph "Conjugate-coordinate class: the Casimir form of the Zeeman-dressed vector operator and the base-point dependence"). It goes immediately before the unique line `\section{Problem G: HBEV}`.
  - That anchor occurs once; checked by s5.
  - Insert one blank line before the anchor.
- **Text.** The block is `proposals/044-rank6-class-transfer/appH_insert.tex`:
  - 10397 bytes, LF, ASCII, 0 TAB, 0 CR;
  - braces and `\(` `\)` balanced;
  - one `\paragraph`, no `\label`.
- **Line endings.** The integrator converts the block to CRLF.
- **Existing text.** Nothing is replaced or removed.
- **References.**
  - `\ref`s used: `sec:status-B` and `ch:vierbein-emergence`, each defined once.
  - Cites used: `IKKT1997`, `Steinacker2023` and `SperlingSteinacker2019`, all already in `bib/namcg.bib`.
  - No BibTeX is added.

```latex
\paragraph{Product backgrounds \(M\times K\) at the maximally supersymmetric content: factorisation of the one-loop trace and the index part of the induced Einstein coefficient (conditional; bounded no-go).}
Work in the Poisson limit with the content of~\cite{IKKT1997}, supplied as an input since the displayed action is bosonic: the ten-component vector with weight \(1\), the ghosts with weight \(-2\) and one sixteen-component Weyl spinor with weight \(-\tfrac12\), with operators \(H_0+\Sigma^{AB}\mathbb F_{AB}\), where \(H_0\) is the common scalar operator, \(\Sigma^{AB}\) are the generators of the vector or spinor representation and \(\mathbb F_{AB}\) is the action of the flux \(\{X_A,X_B\}\). Take a product background: the indices split into a block \(M\) of dimension \(d\) and a block \(K\) of dimension \(10-d\), \(\{X^a,X^i\}=0\) for \(a\) in \(M\) and \(i\) in \(K\), the fluctuations are functions on \(M\) times matrices of a fuzzy space \(K\), and the operators of the two factors commute.

\emph{Factorisation.} On one factor write \(s_0\) for the trace of \(e^{-sH_0}\), \(v\) for the trace over the vector representation of the block minus its dimension times \(s_0\) (the index part), and, for \(d=4\), \(\sigma_\pm\) and \(\tau_\pm\) for the index parts of the chiral spinors of \(\mathfrak{so}(4)\) and \(\mathfrak{so}(6)\), \(\sigma=\sigma_++\sigma_-\), \(\tau=\tau_++\tau_-\). Then, exactly,
\[
  \operatorname{str}e^{-sH}=s_0^K\bigl(v^M-2\sigma^M\bigr)+s_0^M\bigl(v^K-\tau^K\bigr)-\tfrac12\bigl(\sigma_+^M\tau_+^K+\sigma_-^M\tau_-^K\bigr),
\]
and for \(d=7\), with the spinor blocks \(8\) of \(\mathfrak{so}(7)\) and \(2\) of \(\mathfrak{so}(3)\), \(s_0^K(v^M-\sigma_8^M)+s_0^M(v^K-4\tau_2^K)-\tfrac12\sigma_8^M\tau_2^K\) (checked with random non-commuting finite-dimensional operators, relative residual below \(10^{-12}\)). The index parts of the vector and of the spinors agree at second order in the flux, so the first two terms start at fourth order in the flux of their block, and the mixed term starts at second order in each, where it equals \(-\tfrac18v_2^Mv_2^K\) with \(v_2\) the second-order index part of the vector (Fourier extraction of the coefficients in both splits). The vector representation does not enter the mixed term, since \(\Sigma^{ab}\Sigma^{ij}=0\) on it. For \(d=4\) the mixed term is \(-\tfrac14\sigma^M\tau^K-\tfrac14(\sigma_+^M-\sigma_-^M)(\tau_+^K-\tau_-^K)\); the second part is odd under the orientation of each block, starts at third order in the flux of \(K\) and is not treated, and \(\tau^K=v_2^K\) at second order. The mixed term corresponds to the term \(2F^{\mu\nu}F_{\mu\nu}F^{ij}F_{ij}\) of Section~6.2 of~\cite{Steinacker2023}. This covers, for product backgrounds, transverse matrices with flux, which the paragraph on the supertrace at an arbitrary matrix fluctuation does not treat.

\emph{Two-derivative part for four coordinates on \(M\).} Let \(M\) be the four-coordinate class of the Presentation~A paragraphs above, \(d=4\), Euclidean section. There \(s_0^M\) has the density \(\tfrac16\rho R[g_\rho]\), and the second-order index parts of the vector and of a Dirac field have the densities \(\rho^2X\) and \(\tfrac12\rho^2X\) (paragraph on fermionic content in Section~\ref{sec:status-B}). The first term has no two-derivative part, and the part of the induced action with two derivatives on \(M\) that depends on \(K\) is, apart from the orientation-odd remainder,
\[
  -\frac1{32\pi^2}\int\Bigl(\tfrac16W_R\,\rho R[g_\rho]+W_X\,\rho^2X\Bigr),\qquad
  W_R=\int_0^\infty\frac{\mathrm ds}{s^2}\bigl(v^K-\tau^K\bigr)(s),\qquad
  W_X=-\frac18\int_0^\infty\frac{\mathrm ds}{s^2}\,\tau^K(s),
\]
both finite without a cutoff and set by the scale of \(K\) when the vector operator of \(K\) has no negative mode (the spinor operator is a square); at second order in the flux of \(K\), \(\tau^K=v_2^K\). The spinor generators are traceless, so \(\tau^K\ge0\) by the Peierls--Bogoliubov inequality (checked at random data), and \(W_X<0\) for a nonzero flux of \(K\); \(W_R\) has no fixed sign. On the two modes with \(\delta\rho=0\) about constant \(\bar\Theta\) one has \(V_\mu=0\), \(\mathcal T=X/4\) and \(\tfrac32S_{\lambda\mu\nu}S^{\lambda\mu\nu}=X/2\) identically in the polarisation (exact rational arithmetic, four backgrounds), so \(\rho^2X\) acts as \(-4\rho R[g_\rho]\), of which the term \(-2\rho R[g_\rho]\) of the presentation \(r=-2\) of the paragraph on local frame rotations is one half and the axial torsion the other; the axial part of the torsion is also nonzero on the on-shell null mode with \(\delta\rho=0\) of the Lorentzian section. In the units \(c\) of the paragraph on the order \(\Lambda^2\) in Section~\ref{sec:status-B}, with \(\Lambda_{\mathrm{UV}}^2\) replaced by these integrals (\(1/G=c/2\pi\)), the tensor coefficient is \(c_T=\tfrac16W_R-4W_X\); the mixed part \(-4W_X>0\) has the sign of a scalar component. In the presentation \(r=-2\) the coefficient of \(\rho R[g_\rho]\) is \(\tfrac16W_R-2W_X\). The coefficient that~\cite{Steinacker2023} identifies with the inverse Newton constant corresponds to its part \(-2W_X\); the contribution of \(K\) alone is evaluated in Section~6.1 there as an effective potential, and its curvature term \(\tfrac16W_R\), of the same order in the scale of \(K\), is not given there.

\emph{Area coefficient.} The cone on \(M\) leaves \(K\) a spectator, so the factorisation holds on the replica cover. With the cone values of Section~\ref{sec:status-B} (Dirac index part \(-1\) per Dirac field for the antiperiodic gluing, \(0\) for the periodic one, and \(-\tfrac12\) times the coefficient of \(\rho R[g_\rho]\), with \(X\) kept as the torsion invariant, for the smooth replica), the fixed-state replica gives \(c_A=\tfrac16W_R-2W_X\) plus \(2\) per matrix mode of \(K\) at order \(\LUV^2\) (the value \(c_A=2\) at \(N_s=6\), \(n_D=2\), carried by the first term), the periodic replica \(c_A=\tfrac16W_R\) and the smooth replica \(c_A=-\tfrac1{12}W_R\). Hence \(c_A-c_T\) is \(4W_X\) for the periodic and \(-\tfrac14W_R+4W_X\) for the smooth replica, and for the fixed-state replica a cutoff-dependent term of order \(\LUV^2\) plus the finite part \(2W_X\): for \(W_X\neq0\) the periodic gap does not vanish and the smooth one vanishes only for \(W_R=16W_X\), a condition on \(K\). The vector index part, which with the weight \(\kappa_X\) carries the gap \(4\kappa_X\) of the paragraph on the normalisation, cancels against the Dirac fields in the first term and is absent from the mixed term. The finite part \(2W_X\) of the fixed-state gap is the axial-torsion part of the Dirac index density on the tensor modes; the Dirac cone value \(-1\) equals the coefficient of \(R\) in \(\tfrac12\rho^2X\) in the presentation \(r=-2\) (an equality of the two values, not derived), so, with the same index density and cone value, the finite gap would vanish for tensor modes that source neither the axial nor the vector torsion at first order.

\emph{Classes with six polarisations.} For a product the linearised Einstein rank is that of \(M\) (paragraph on leaf dimension above four), so \(M\) must carry the six polarisations. For \(D\) matrix coordinates on a four-dimensional leaf with constant \(\theta\) in the chart \(y\), the scalar operator is \(-\lambda\Delta_{\hat g}\) with \(\hat g=\lambda G\), \(\lambda=\sqrt{\lvert g\rvert}/\rho\) and \(\lvert\det\hat g\rvert=\lvert\det g\rvert\), and its density is \(\tfrac16\rho R[\hat g]\) pointwise (exact algebra in both signatures; the density checked symbolically at a random Euclidean jet); \(\rho\) is constant, so the scalar part of the two-derivative density in this class is \(\rho\) times the Einstein--Hilbert functional of \(\hat g\). At the frozen data of the paragraph on more than four matrix coordinates the linearised Einstein operator of \(\hat g\) has rank \(\min(6,D-1)\) on the first-order image (one exact-rational draw for each \(4\le D\le11\)), and the Hamiltonian gauge direction is a linearised diffeomorphism of \(\hat g\). With \(d=7\) (four tangent and three normal directions) and \(K\) in the remaining three, the index density of the mixed term is \(X_7=g^{\rho\lambda}\partial_\rho\Theta^{IJ}\partial_\lambda\Theta_{IJ}\), which on a transverse wave \(\delta X^i=\phi_i\cos(p\cdot y)\) about \(x^i=\tfrac12\mathrm{II}^i_{\mu\nu}y^\mu y^\nu\) contains the term \((p\cdot g^{-1}p)(p\cdot Kp)\lvert\phi\rvert^2\) of fourth order in \(p\) at \(y=0\) (exact check at one background), whereas the Einstein--Hilbert form of \(\hat g\) on those modes is of second order in \(p\) by derivative counting, since \(\delta\hat g\) is algebraic in \(\phi\) at first order. The two forms are not proportional, so for a nonzero flux of \(K\) no single \(G_T\) covers the transverse polarisations at the frozen-coefficient leading symbol. The conjugate-coordinate class with \(K\) in the transverse directions has the structure \(S^2_n\,\bar\times\,M^{3,1}\times K\) of Section~7 of~\cite{Steinacker2023}, with frame \(\{t^\alpha,x^\mu\}\), where \(t^\alpha\) and \(x^\mu\) are the semiclassical forms of the generators \(T^a=R^{-1}M^{a4}\) and \(X^a=rM^{a5}\) of~\cite{SperlingSteinacker2019}, that is \(T^a\) and \(y^\mu\) here up to normalisation; there the mixed term is the spinor index part of the Dirac operator of the background \(T^a\) on \(\mathbb{CP}^{1,2}\). Its two-derivative density, its values on the six level-one amplitudes and on the cone, and whether those amplitudes source the axial torsion, are not computed; in the Poisson limit its heat trace is the hypoelliptic one of the paragraph on the \(\Theta\)-built heat kernel, whereas the cited construction uses a finite fibre.

These statements are for the Poisson limit on \(M\), one loop, the content stated, product backgrounds without mixed flux, the orientation-even part of the mixed term, the replicas of Section~\ref{sec:status-B} with the hypotheses stated there, and, for the transverse modes, frozen coefficients. They do not construct \(K\) or fix the sign of \(W_R\), so no value or sign of \(G_{\mathrm{eff}}\) follows; they do not derive the replica selected by the matrix state, identify \(G\) or \(\hat g\) with the emergent metric of Chapter~\ref{ch:vierbein-emergence}, or treat Moyal corrections, non-product backgrounds or a finite fibre. Problems~B and~F remain open and PROGRAMME-CONDITIONAL.
```
(Identical to `appH_insert.tex`, which is the authoritative byte-exact copy.)

Internal references to merged paragraphs are made by name. Each name matches an existing paragraph title:
- "the Presentation~A paragraphs above";
- "paragraph on fermionic content in Section~\ref{sec:status-B}";
- "paragraph on local frame rotations";
- "paragraph on the order \(\Lambda^2\) in Section~\ref{sec:status-B}";
- "paragraph on the normalisation";
- "paragraph on leaf dimension above four";
- "paragraph on more than four matrix coordinates";
- "paragraph on the supertrace at an arbitrary matrix fluctuation";
- "paragraph on the \(\Theta\)-built heat kernel".

Stale passages elsewhere: none. I checked the following merged sentences, and each remains true:
- L234: "In the construction of~\cite{Steinacker2023} the Einstein--Hilbert term is generated by a mixed quartic term ... the class above has no analogue of it".
- L2092: "One-loop IKKT calculations on a brane with compact fuzzy extra dimensions report ...".
- L2103: "The supersymmetric one-loop mechanism ... rests on field content that is not part of the present sector list". The new paragraph supplies that content explicitly as an input.
- L2162: "Suppose a term ... reported to arise at one loop in~\cite{Steinacker2023} ...".
- L1052–1079: the covariant quantum-space paragraph. The new paragraph does not adopt induced gravity in place of B; it compares G_T and G_A.

No PRIOR-CLAIM-ERROR.

## Verification scripts

All are in `proposals/044-rank6-class-transfer/`, each with a saved `.out.txt`:
- **`s1_factorisation.py`** (numpy/scipy, ~6 s):
  - (A) the factorisation identity for d=4 (pairing (++,--) matches; (+-,-+) does not) and d=7, at 3 random draws each;
  - (B) Taylor coefficients c_mn via 2D FFT: the vanishing pattern, c22 = -(1/8)v2^M v2^K, the Dynkin relations, and τ3± (structure-constant versus d-symbol parts);
  - (C) τ^K ≥ 0.
- **`s2_axial_torsion_4coord.py`** (sympy exact, ~2 min): on the δρ = 0 modes about constant θ̄, V = 0, the identity X = 2𝒯 + (3/2)S² + 2V², (3/2)S²/X = 1/2 and 𝒯/X = 1/4 identically in the polarisation (4 Euclidean backgrounds); and, on Lorentzian on-shell null modes, the axial torsion is nonzero (3 backgrounds).
- **`s3_brane_class.py`** (sympy exact, ~3 min):
  - (i) the ĝ algebraic identities, both signatures;
  - (ii) the scalar a_1 density = (1/6)(√ĝ/λ)R[ĝ] at a random second-order jet (exact; difference 0);
  - (iii) the linearised Einstein rank of ĝ = min(6, D-1), D = 4..11, and the Hamiltonian gauge as a ĝ-diffeo;
  - (iv) the bending L⁴ coefficient = (p·p)(p·Kp)|φ|².
- **`s4_replica_bookkeeping.py`** (sympy): c_T and c_A for the three replicas, the gaps, and the criterion.
- **`s5_insert_mechanics.py`**: bytes, balance, refs/labels, bib keys, anchor uniqueness, title collision, process-language scan.
- **`compile_check.py`**: scratch build of the CURRENT working tree outside the repository (pdflatex, bibtex, pdflatex ×2), with and without the insert. Baseline 317 pages; with the insert 321 pages. 0 undefined references, 0 undefined citations, 0 multiply defined labels. CRLF preserved; scratch removed.

## Decisions Taken

1. **Class.** I chose the product class M × K at the IKKT content, applied to three M-classes, over a single-class computation of the full CP^{1,2} heat kernel.
   - Reason: the only reported EH mechanism lives there. The factorisation lemma makes the rank-6 question reduce to one well-defined M-datum (the Dirac index density), and this favours the full-GR derivation.
   - Rejected:
     - the D ≥ 7 brane without K, which at IKKT content has no Λ² term (both N_tot and κ_X vanish) and no scale;
     - Λ² off (6,2) as a computational parameter, where the vector κ_X X_D gives the same bending non-Einstein term;
     - the full hypoelliptic CP^{1,2} computation, which cannot be verified in one package.
2. **Presentation of the tensor coefficient.** I used the on-mode value (r = -4 via the exact identity on δρ = 0 modes), not the teleparallel R-coefficient. The first law needs the coefficient of the actual quadratic form (merged normalisation paragraph). The teleparallel value is reported alongside.
3. **No bib additions.** 2110.03936 is not needed and was not fetched.
4. **Orientation-odd mixed term.** Left untreated and stated as such, rather than computed for a model chiral K. It is irrelevant for non-chiral K and does not alter the parity-even tensor coefficient.

## Milestone assessment

**Candidate M2 (bounded no-go), not a breakthrough.** In the fuzzy-KK product route, which the manuscript keeps open (L234, L2092, L2103), two things are established:
- at the leading two-derivative order G_A ≠ G_T for each ledger replica, with a computed, K-independent structure of the gap;
- for the D_M = 7 brane × K, no single G_T on the transverse polarisations.

The route is not closed beyond these hypotheses: CP^{1,2} × K and non-product backgrounds remain open.

No M1: no critical-path step is derived. No M3: no merged claim is wrong. No M4 or M5.

## Status-label recommendation

The current critical-path set from Ch17 `sec:ch17-done` and Appendix H is A, B, C, D1, E, F, G-derived and N. B and F, the affected problems, stay **OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL**. No label change is recommended.

## Author decision needed

None.

## Remaining open step

To close the B normalisation sub-target in a class that can carry full linearised GR (and, for F, to fix the G_eff sign), the following are needed:
1. In CP^{1,2} at finite fibre n with fuzzy K transverse, compute the two-derivative M-Dirac index density on the six gauge-invariant level-one amplitudes, together with its cone value, and determine whether those amplitudes source the axial torsion.
2. Derive the replica selected by the matrix state (Problem A) in a form that removes the Λ² Dirac excess of the fixed-state replica, e.g. an edge or holonomy contact of modulus 2 per Dirac field. Without this, the finite agreement would not suffice.
3. For an explicit K, compute W_R and W_X, which give the sign of c_T.
4. All of this must still be done without Assumption dictionary (Problem A) and with a derived signature (Problem E).

## Special instructions for the gatekeeper

- **Must not be asserted:**
  - that Steinacker's EH coefficient is "wrong";
  - that the CP^{1,2} × K class is shown to work, or to fail;
  - any G_eff sign. Only the mixed part is sign-definite; W_R is indefinite.
  - any closure, or local Lorentz symmetry.
- **Re-check:**
  - the factorisation for the d=4 pairing convention (s1 (A));
  - the order-(2,2) coefficient -(1/8);
  - the c-unit normalisations linking the bulk ∫ds s^{-2} to the cone ∫ds s^{-2} (Research §3);
  - the smooth-replica index value 0 (merged L215: coefficient of √G R_G at fixed coframe torsion);
  - the derivative counting of EH(ĝ) on transverse modes.
- The claim "its curvature term (1/6)W_R … is not given there" about Steinacker Sec. 6.1 rests on reading eqs. (6.10)–(6.18) of the arXiv v1 text. Please verify against the paper or soften it.
- s2 and s3 take a few minutes each.
