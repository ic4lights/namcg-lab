SME-SCOUT: 9 routes | TOP: F:compare the 027 mass-supertrace remainder with Steinacker's K-free fibre term (2303.08012 Sec 7.1.2, eqs 7.5, 7.8, 7.11-7.13) and the Pauli-Sakharov supertrace formula (Visser gr-qc/0204062 eqs 21, 36); B:a_3 mixed quartic with KK sum, reuse of the V_4,mix chain (2303.08012 eqs 6.19-6.31, 2411.02598 eqs 3.11-3.35); B:A-side log coefficient assembled from Laplace-type conical a_2^Sigma plus bundle-curvature and torsion pieces (Solodukhin 1104.3712 eq 70, Hanisch-Pfaeffle-Stephan 0911.5074) | EMERGENCE-RISK: low

(Saved verbatim by the orchestrator; the SME agent is read-only. Advice only. No derivations and no manuscript text.)

# SME scout: second variation / A-dependence (F) and a_3 KK term plus A-side log (B)

## 0. Reading mode and trust level

- **Repository reading: digest + targeted reads.** I read `reports/ledger.md` (entries 017-027), `proposals/026-next-order-curved/review-r2.md` (in full), and the previous scouts `sme-scout-gluing-fermions-20261015.md` and `sme-scout-flux-regulator-20261017.md`. I did not re-read `proposals/027-*/review-r2.md` and I read no chapter files. I rely on the ledger summary of 027. I do not repeat the content of the previous scouts.
- **Literature reading.** Every ID below was opened live on its arXiv abs page or on an ar5iv/arXiv-HTML full text. The fetch tool summarises pages, so equation numbers are as reported by that tool. Re-open the paper before putting an equation number into the manuscript. Where I saw only an abstract I say so.
- **Not verified.** I could not open the Springer page for JHEP04(2026)044 (redirect to a login), so I do not know its arXiv ID. I did not open Bern-Morgan (my guessed arXiv ID returned 404, so I do not cite it). The claim that Dirac and scalar nonzero spectra coincide on self-dual backgrounds came only from search snippets: not independently verified.

## 1. Bottom line in nine points

1. **The published EH mechanism does not come from a Hessian.** In Steinacker 2303.08012 and Manta-Steinacker-Tran 2411.02598 the effective action is evaluated on an arbitrary background T-bar, with no fluctuation expansion. The quartic V_4[δF] = -4 tr δF^4 + (tr δF^2)^2 (2303.08012 eq 4.21; 2609.08955 eq 88) is built from the bilocal quantity δF(x,y) = F(x) - F(y) on open-string modes. The metric enters only afterwards, through a torsion-to-Ricci identity (2411.02598 eq 3.31, "H_grav is related to R"). So in the literature the "A-dependence" is the dependence of Gamma[T-bar] on the background flux, organised as a flux expansion of the SO(1,9) character (2411.02598 eqs 3.11, 3.15-3.16). It is not a computation of δ²Gamma/δA². The Hessian does appear in 2609.08955 Sec 7.2 (eqs 93-100, footnote 27), but only after the EH term has been identified. That is a statement about the quadratic action, and it mixes the classical Yang-Mills part with the one-loop part.
2. **Your two findings reproduce the published structure.** 026's weighted a_2 = (1/2) S_4, a quartic in the connection b that vanishes iff b is chiral, has the same shape as the published pure-M term V_4(T)^{μνρσ} k_μ k_ν k_ρ k_σ (2303.08012 eqs 5.7-5.9). Steinacker calls that term "a sub-leading higher-derivative contribution ... which will be dropped": no EH term. Your "mass-insertion lemma" and "a_3 mixed quartic with a KK 1/μ² sum" match his mixed term V_4,mix = 2(δF^{αβ}δF_{αβ})(δF^{ij}δF_{ij}) (eq 6.19), which is the only published EH entry point. Your 026 conclusion is therefore consistent with the field.
3. **What plays the role of m_K.**
   - In 2303.08012, m_Λ² = m_K² μ_Λ² (eq 6.6), where m_K is the scale parameter of the fuzzy K (stated after eq 6.12). The transverse flux enters as (δF^{ij}δF_{ij})Υ_Λ = m_K⁴ C_Λ² Υ_Λ (eq 6.20).
   - The EH coefficient is 1/G_N = (2c_K²/π³) ρ^{-2} m_K² with c_K² = (π²/8) Σ_Λ C_Λ²/μ_Λ² > 0 (eqs 6.30-6.31).
   - m_K is one scale doing two jobs. The flux squared contributes m_K⁴, the propagator moment contributes 1/m_Λ² (eq 6.27: 4ρ²κ̃_(4) = iπ²/(3m²) ρ^{-4}), and the ratio is m_K².
   - In 2411.02598, m_K is the maximal eigenvalue of the transverse □_6 (eqs 2.32, 2.41), tied to the flux by Bohr-Sommerfeld (eqs 2.33-2.34). The ratio ϑ_K[2]/ϑ_K[4] ~ 1/d_K justifies truncating (eq 3.43). Explicit value (|K| = 4): 1/G_N ≈ (J² d_K^{3/2}/π) Δ_K²/ρ² (eq 3.49), as reported by the tool.
4. **There is a published K-free EH-like term on the covariant FLRW space, and it is Lorentz-violating.** 2303.08012 Sec 7.1.2 (eqs 7.8, 7.11-7.13) gets a mixed fibre-S²-with-M term from the Leibniz split of δF acting on φ_sm(y)Y_sm(t). It uses [F^{αβ}, t^i] = -(i/R²)(η^{αi}t^β - η^{βi}t^α). The one-loop term is (7.12), with prefactor -(1/(2π)⁴)(π²/(8R²)) and weight ρ^{-6} Σ_{s>0} k̃^s/(3s), using κ̃_(4)(m_s²) = iπ²/(12 m_s²) ρ^{-6} with m_s² = 3s/R² (7.5, 7.13). Steinacker states that k̃_{αβγδ} "is not Lorentz invariant a priori, reflecting a time-like vector field", and must be suppressed by c_K² m_K² ≫ 1/R² (7.14, 7.25). He therefore does not obtain Newton's constant on the minimal space without K. This is the closest published analogue of the F frontier.
5. **The Pauli-Sakharov supertrace formula is the published form of the mass-insertion lemma.** Visser gr-qc/0204062 gives 1/G = 1/G_0 - (1/2π) Str[k_1 κ² - k_1 m² ln(κ²/m²)] (eq 21). With the Pauli conditions Str(k_1) = Str(k_1 m²)-type finiteness (eq 35) one gets 1/G = -(1/2π) Str[k_1 m² ln(m²/μ²)] (eq 36; Frolov-Fursaev eq 42-44). Here k_1 is the field's R-coefficient in a_1 (his Table 1: minimal scalar 1/6, conformal scalar 0, Weyl -1/6, Dirac -1/3, massless vector -2/3). Two consequences. (i) Your "weighted a_1 = 0" is Str k_1 = 0 with the matrix-model non-minimal couplings fixed. (ii) The surviving coefficient is a mass supertrace weighted by k_1, and its sign "depends on the spectrum and is not fixed" (Visser). That agrees with 027. Note the dependence on the scalar coupling ξ: by my own arithmetic from his table, an N=4 multiplet gives Str k_1 = 1 with minimal scalars and 0 with conformal ones. The matrix action must therefore fix ξ. This arithmetic is mine and not stated in the paper.
6. **Sign of G_N from IKKT.** I found no 2025-2026 paper that fixes the sign independently of c_K² > 0. In 2303.08012 the sign of 1/G_N follows from C_Λ² > 0 because the target metric on K is Euclidean (eq 6.20); the paper does not discuss the sign explicitly (inference by the fetch tool, and by me). 2609.08955 eq 92 defines 1/G_N ≡ (1/(4πρ²)) Tr_K(δF_ij δF^ij/□_6) and states no sign discussion. 2411.02598 shows an explicit minus in eq 3.30 and a plus in the definition 3.33; the tool could not reconcile them. Combined with the i in κ̃_(4) (eq 6.27) and the Lorentzian iε, signs are convention-fragile (Battista-Steinacker 2310.11126 v2 corrected a sign). Do not transfer a Euclidean positive moment to a Lorentzian sign without tracking these factors.
7. **A-side log coefficient: no published a_2^Σ for a connection with torsion or bundle curvature.** Solodukhin's review (1104.3712) gives a_2^Σ for -(∇²+X) in eq (70), explicitly without bundle curvature Ω_ab and without extrinsic curvature (Sec 3.7.2). Fursaev hep-th/9405143 treats only Riemann components (abstract). Fursaev-Miele (read in the previous scout) is a_1-level for spin 1/2 and 1. Bulk a_2 for a Dirac operator with totally antisymmetric torsion is published (Hanisch-Pfäffle-Stephan 0911.5074; Pfäffle-Stephan 1101.1424). The conical Dirac heat kernel with a flavour monodromy is in Bianchi et al. 2104.01220 (abstract read only). The assembled twisted-Dirac cone a_2^Σ is therefore a new combination of known ingredients.
8. **Chirality and SUSY: the pattern is known in amplitudes.** All-plus (self-dual) one-loop amplitudes "vanish in supersymmetric theories" (Bern-Dixon-Perelstein-Rozowsky hep-th/9811140 abstract). Self-dual YM and gravity amplitudes are tied to N=4 and N=8 (Bern-Dixon-Dunbar-Kosower hep-th/9611127). This is the amplitude-level counterpart of your 0 = 0 on (A)SD backgrounds and S_4 > 0 only when both chiralities are present. It is analogy only: those are scattering amplitudes, not heat-kernel coefficients on a curved Poisson background.
9. **Whether the nonzero S_4 or the mixed term is a "genuine lift" is a hypothesis-class question.** Steinacker's trace is bilocal and exact in |x-y|, with the finite string-mode spread Δ² in the propagator (2303.08012 eq 4.19: δF/(|x-y|² + 2Δ² - iε)). NAMCG's Seeley-DeWitt coefficients are a local derivative expansion in the Poisson limit. My inference: the two agree only where the bilocal integral is dominated by |x-y| below the curvature scale. The EH coefficient in (6.31) comes from an integral saturated at |x-y| ~ Δ, so it may not be reproduced by a finite number of local a_n. This is why Moyal/bilocal corrections are a real route and not a footnote.

## 2. Route map (a): Problem F, the A-dependence and the Newton coefficient

### R-F1 (TOP): compare the 027 remainder with the K-free fibre term (2303.08012 Sec 7.1.2) and with the Pauli-Sakharov supertrace
- **Sub-lemma.** In the CP^{1,2} four-matrix class with the IKKT content, write the species-dependent remainder (027: -(4 μ² + n_ex μ_i²) j(a), Re j > 0) in the Pauli-Sakharov form Str[k_1 m² (moment)]. Then compare its structure with the published fibre-mixed term, whose "mass" is the fibre Casimir mass m_s² and whose moment is κ̃_(4)(m_s²) ∝ 1/m_s². Decide whether the mass supertrace of 027 can be identified with Σ_s k̃^s/(3s) over the hs tower, in which case the Newton coefficient is the Lorentz-violating term (7.12) and not a covariant EH term.
- **Equations to reuse.**
  - 2303.08012: Leibniz split (7.8), the commutator [F^{αβ}, t^i] below it, the reduction (7.11), the one-loop term (7.12), the mass formula m_s² = 3s/R² (7.5), the moment (7.13), the pure-S² term (7.15), and the dominance conditions (7.14), (7.25).
  - Visser gr-qc/0204062: eqs (21), (35), (36) and Table 1 (k_1 per species). Frolov-Fursaev eqs (42)-(44) as quoted by Visser.
  - 2411.02598: Δ_J² replacing a possibly negative m_s² (eq 2.37, Appendix C), and 1/G_N in terms of Tr_{hs⊗g}(δF δF/(□_6 + Δ_J²)) (eq 3.33).
- **NAMCG objects.** The 027 supertrace remainder; the invariant-sector scalar D_1; the fibre cutoff S² of the 025 window; the so(4,2) Casimir identities (022-023).
- **Expected form.** A table matching the 027 remainder with the published (7.12) up to Lorentzian/Euclidean factors. A genuine finding would be either (a) the same Lorentz-violating tensor k̃_{αβγδ}, which establishes that the minimal space has no covariant Newton coefficient at this order, or (b) a covariant combination in the window.
- **No-gos and cautions.**
  - Steinacker explicitly says the S²-M term "is not Lorentz invariant, and should be suppressed", and he gets covariant EH only with K. Matching it is a no-go-type statement for F in the four-matrix class, not a failure.
  - The mass formula m_s² = 3s/R² (2303.08012, M^{3,1}_n) differs from the minimal-space statement m_s² = -s/R² in 2411.02598 (previous scout). Do not mix them without checking the presentation of the space.
  - The Euclidean positive moment cannot be carried to a Lorentzian sign: track the i in κ̃_(4) and the Lorentzian iε.
- **Emergence.** Preserved. **Feasibility.** Medium-high as a comparison. **Value.** Conditional sharpening; it could convert "no G found" into "the published term is the same Lorentz-violating one".

### R-F2: use the published definition of A-dependence (background functional, not Hessian)
- **Sub-lemma.** Organise the A-dependence as the coefficient of δF_{μ̇ν̇}δF^{μ̇ν̇} in the character expansion, Q_grav = α² δF_{μ̇ν̇}δF^{μ̇ν̇} G_6[α] (2411.02598 eqs 3.11, 3.15-3.16), instead of the Hessian δ²/δA². In the four-matrix class the transverse factor G_6 has no six-dimensional flux (the transverse matrices vanish), so the claim to test is that the O(α⁴) term has no δF·δF product with a transverse flux. That would show formally why the A-dependence cannot produce a covariant EH term without K.
- **Equations.** 2411.02598 eqs 3.4, 3.7, 3.9, 3.13, 3.28; 2303.08012 eqs 4.16-4.21; 2609.08955 eqs 86-88.
- **Cautions.**
  - A Hessian of the full effective action around a non-flat background contains the classical Yang-Mills term and the one-loop term together (2609.08955 Sec 7.2, footnote 27: extra modes with modified dispersion, Sec 8). Isolating the one-loop part needs the supertrace expansion, not the on-shell Hessian.
  - Kumar-Steinacker 2312.01317 (abstract read) derive generalised Einstein equations by varying the one-loop action, including dilaton, axion and an "anharmonicity tensor". That is a first variation and shows what the published equation of motion looks like.
- **Emergence.** Preserved. **Feasibility.** Medium. **Value.** A structural statement (an obstruction) for the class, conditional on the 027 hypotheses.

### R-F3: Moyal/bilocal check of the local expansion
- **Sub-lemma.** Test whether the finite-Δ² bilocal integral (2303.08012 eqs 4.19-4.20) and the NAMCG local a_n expansion agree to the order that matters, and where Δ² enters the 025-027 window as the matrix-intrinsic regulator. Δ² is the natural matrix-derived replacement for the Delta_kappa Gaussian window.
- **Equations.** 2303.08012 eqs 4.19-4.21 and 5.8-5.10. Blaschke-Steinacker-Wohlgenannt 1012.4344 (JHEP 1103:002; abstract and Secs 3-6 partly read): noncommutative Seeley-DeWitt-type expansion Tr e^{-αD̸²} = Σ α^{(n-4)/2} Γ^{(n)} (eq 3.1) for the matrix-model Dirac operator D̸² = [X,[X,·]] + Σ_ab[Θ^ab,·] (eq 4.2). The tool did not return an explicit Λ² coefficient in terms of R; "double-commutator terms lead to curvature terms ... which usually diverge as Λ²" (Sec 6.4). Klammer-Steinacker 0805.1157 (abstract read): fermion integration yields EH plus a dilaton-like term, at least on-shell, with N=4 as an exception to UV/IR mixing.
- **Constraint.** These papers use a gauge-invariant cutoff Λ on the noncommutative Dirac operator, which Steinacker later rejects for IKKT (2303.08012; see the previous scout).
- **Feasibility.** Low-medium (laborious). **Value.** Potentially closes the question of whether Poisson-limit coefficients are the right object. Conditional.

### R-F4: fermion content / mass pattern (Visser Table 1 as bookkeeping)
- **Sub-lemma.** Use Visser's per-species k_1 and the Pauli conditions to list which mass patterns (SUSY-breaking splittings within a multiplet, or a KK tower with equal boson/fermion levels) give nonzero Str[k_1 m² ln m²] and with what sign. This is a check on 027's "mass pattern" avenue, independent of any NAMCG geometry.
- **Cautions.** Visser notes the k_1 constraints "are not derivable from unbroken SUSY alone" and that a Frolov-Fursaev sign differs from his eq (38); I did not resolve it. IKKT masses come from flux, not a Lagrangian mass term.
- **Feasibility.** High. **Value.** Bookkeeping that bounds what a mass-pattern route can give; not a derivation of G.

## 3. Route map (b): Problem B, the a_3 KK term and the A-side log

### R-B1 (TOP): the a_3 mixed quartic with a KK sum, reusing the published V_4,mix chain
- **Sub-lemma.** Add a transverse fuzzy K (matrices Y^i with [T^α, Y^i] = 0) to the NAMCG class. Show that the weight-two (EH) coefficient of the quartic is the product of the 026 weight-two quantity on the 4D side with the transverse factor m_K⁴ C_Λ² and the propagator moment 1/m_Λ² = 1/(m_K² μ_Λ²), summed over Λ. This produces c_K² = (π²/8) Σ C_Λ²/μ_Λ² and 1/G ∝ ρ^{-2} m_K² in the class, which is the candidate form of the cone-side (T-side) EH coefficient.
- **Equations to reuse.**
  - 2303.08012: V_4,mix (6.19); (δF^{ij}δF_{ij})Υ_Λ = m_K⁴ C_Λ² Υ_Λ (6.20); 4D factor 2 m_K⁴ C_Λ² T^{αβμ}T_{αβ}^ν k_μ k_ν (6.23); trace and KK sum (6.24); κ̃_(4) (6.25-6.27); induced coefficient (6.29); c_K² (6.30); 1/G_N (6.31); the action (6.32), which contains R + (1/2) T̃T̃ - 2ρ^{-2}∂ρ∂ρ. The KK masses: eq 6.6. The shifted denominator μ_Λ² + m_s²/m_K² when the S² fibre is also present (7.22).
  - 2411.02598: the same result as a flux expansion, 1/G_N ≈ (1/(4πρ²)) (ϑ_K[2] - (1/6)ϑ_K[4]) (3.35); the hs-trace and Δ_J² (2.37).
  - 2609.08955 eqs 91-92.
- **What m_K must be in NAMCG.** A transverse matrix datum: either the eigenvalue scale of □_6 on a fuzzy K, or, in a SUSY-breaking presentation, a mass. NAMCG's 026 "mass-insertion lemma" says the same thing: EH enters only via a scale that breaks the supertrace cancellation. The published K realises it by flux, not by a Lagrangian mass.
- **No-gos and cautions.**
  - The published derivation assumes a product background [T^α, K^i] = 0 and drops the derivative-of-torsion term (6.22) when curvature ≪ k². That is a hypothesis to state.
  - c_K² > 0 requires the Euclidean target metric on K (6.20).
  - 4D EH is not obtained without K (Sec 7.1); the K-free S²-M term is Lorentz-violating.
  - K is classically unstable unless stabilised: static K collapses and the cure is a large RR charge or rotation (Manta-Steinacker 2509.24753, per previous scout). 2609.08955 Sec 6 assumes stabilisation by RR charge, and Steinacker-Tran 2405.09804 (abstract) links K stabilisation at one loop to a U(1) flux bundle that also breaks superconformal symmetry by a KK scale.
  - Steinacker rejects a heat-kernel cutoff for this trace (the iε Schwinger form instead), so a NAMCG Seeley-DeWitt a_3 is a different organisation of the same quantity. Treat agreement as something to test.
- **Emergence.** Preserved if K is part of the matrix data and the metric is read from the symbol of the 4D quartic. At risk if a target metric on K is imposed from outside; state that the Euclidean K metric is the matrix Casimir form.
- **Feasibility.** Medium. **Value.** If the weight-two coefficient reproduces (6.31) within the NAMCG class, a genuine step for B/F. Otherwise a conditional sharpening locating the entry point.

### R-B2 (TOP): the A-side cone log coefficient as an assembly of published ingredients
- **Sub-lemma.** Write the squared Dirac operator with the matrix-model connection as a Laplace-type operator -(∇^T)² + E on a bundle with curvature Ω (including torsion in the connection), apply the Fursaev conical expansion to obtain the surface a_2^Σ including the Ω-dependent pieces, and compare with the T-side zero of 026.
- **Equations and sources.**
  - Solodukhin 1104.3712: a_2^Σ for -(∇²+X), eq (70) [(π/3)((1-α)(1+α)/α)∫_Σ(R̄/6 + X) - (π/180)((1-α)(1+α)(1+α²)/α³)∫_Σ(R̄_ii - 2R̄_ijij)]; 4d log term eq (82); Dirac area-law weight 1/2 (Sec 3.14, eq 126); a_1 for spin 1/2 (eq 136). Sec 3.7.2 states that extrinsic curvature does not appear in (70) because the fixed surface of the Abelian isometry has K = 0; Sec 3.10.2 cites Dowker that extrinsic-curvature invariants could modify it.
  - Fursaev hep-th/9405143 (abstract only).
  - Bulk a_2 for Dirac with totally antisymmetric torsion: Hanisch-Pfäffle-Stephan 0911.5074 (CMP 300:877); Pfäffle-Stephan 1101.1424 (a_2 contains the scalar curvature and tr E only; torsion enters a_4). Search snippets say the two papers' conventions differ: check before comparing numbers.
  - Dirac conical kernel with flavour monodromy: Bianchi et al. 2104.01220 (abstract read only). Charged heat kernel and Sommerfeld formula: Jing-Niu-Xian 2511.01366 (previous scout, scalars only).
- **Expected form.** A closed expression ∫_Σ(c_1 R̄ + c_2 (R̄_ii - 2R̄_ijij) + c_3 tr E + c_4 tr Ω_ab Ω^ab + ...), whose Ω-terms are the new part. In the 4-dimensional Solodukhin formula for conformal operators the log is a χ(Σ)-term plus a c-weighted extrinsic-curvature term (lectures 2201.13310, snippet); the NAMCG operator is not conformal, so a = c does not apply.
- **Cautions.**
  - Regularity: the previous scouts and 024 show that analyticity in n of the s-wave index fails for a singular ρ (|n-1|/(2n)). Any a_2^Σ built from a smooth family must be checked for the same non-analytic structure.
  - Dong 1602.08493 (via search; abstract not opened by me) finds f_b ≠ f_c holographically; at n → 1 only the c-type term matters, so the Rényi conjecture f_b = f_c is not an input.
  - No published replica entropy with torsion: the only torsion-and-entanglement hits were cosmological Dirac entanglement in Einstein-Cartan (Luongo-Mancini 2101.11567) and holographic relative entropy (1607.00263), neither a conical computation. Not independently verified beyond titles.
- **Emergence.** Preserved. **Feasibility.** Medium (assembly plus checks). **Value.** If the A-side log reproduces zero at the SUSY content, it would be the first independent consistency check of the 026 T-side zero; if not, it exposes a G_A ≠ G_T at log order.

### R-B3: chirality as a vanishing mechanism and the lift
- **Sub-lemma.** State the 026 chirality theorem in the language of helicity sectors and test the prediction "nonzero only if both chiralities are present" against the J ≠ 0 or non-chiral perturbations. The 026 identity S_4 = 8 tr A tr B + 16 tr(C C^T) has the SD × ASD structure of an MHV-type contribution.
- **Sources.** hep-th/9811140 and hep-th/9809160 (abstracts): all-plus (self-dual) amplitudes correspond to self-dual configurations and vanish in SUSY theories. Bern et al. hep-th/9611127: self-dual YM and gravity one-loop amplitudes related to N=4 and N=8. Miller 2608.26242 (abstract only): self-dual Einstein gravity is one-loop exact, finite, with only all-plus amplitudes nonzero.
- **Cautions.** Amplitude-level statement, not a heat-kernel theorem. The classical chirality of a Poisson bivector is not the helicity of external states. Use as organising analogy only.
- **Feasibility.** High as a remark. **Value.** Context for 026; no new coefficient.

### R-B4: Sakharov/Pauli supertrace for the T side
- **Sub-lemma.** State the 026 weighted a_1 = 0 as Str k_1 = 0 with explicit k_1 per species, and the surviving induced term as Str[k_1 m² ln(m²/μ²)]. Also check the Frolov-Fursaev contact-term treatment in the induced-gravity entropy literature (hep-th/9607104, abstract only read; hep-th/9703178 returned 404 on my ID, so not verified) for how the contact terms are handled when Str k_1 = 0.
- **Value.** Bookkeeping that connects B to the standard Sakharov formula; relevant to the 024 classification (H-N versus Solodukhin). Feasibility high.

## 4. Ranking across both problems

| Rank | Route | Problem | Feasibility | Type |
|---|---|---|---|---|
| 1 | R-F1 (fibre term and supertrace comparison) | F | medium-high | conditional sharpening, possibly an obstruction statement |
| 2 | R-B1 (V_4,mix chain with a KK sum) | B/F | medium | genuine step if reproduced in class |
| 3 | R-B2 (A-side log by assembly) | B/A | medium | genuine consistency check |
| 4 | R-F2 (character-expansion form of the A-dependence) | F | medium | obstruction for the four-matrix class |
| 5 | R-F3 (bilocal vs local) | F/B | low-medium | conditional |
| 6 | R-B4, R-F4 (Pauli-Sakharov bookkeeping) | B/F | high | bookkeeping |
| 7 | R-B3 (chirality analogy) | B | high | remark |

## 5. Constraints to respect (consolidated)

- **Published no-gos/limits.**
  - 4D EH is not obtained without K; the K-free fibre term is Lorentz-violating (2303.08012 Sec 7.1).
  - Pure-M V_4 is a higher-derivative term (eq 5.9).
  - Classical instability of K without charge or rotation (2509.24753, previous scout).
  - The Casimir obstruction for Lie-algebra saddles (Liao 2609.40183, abstract only, previous scout) as a heuristic.
  - Spin-2 and spin-3/2 conical traces are non-smooth in n (Fursaev-Miele, previous scout), so treating the metric-fluctuation block as a vector-like block is an assumption.
- **Convention hazards.** Signs in Lorentzian Schwinger form (factors of i in eqs 6.27, 3.30/3.33); the Visser/Frolov-Fursaev sign of eq (38) vs (44); the torsion conventions of Hanisch-Pfäffle-Stephan vs Pfäffle-Stephan.
- **Emergence.** All routes keep the metric emergent provided that (i) the Euclidean metric on K is the Casimir form of the transverse matrices, (ii) the effective metric G is read from the frame/symbol as in 2411.02598 eq 3.31, and (iii) no background metric fixes the iε contour.

## 6. Verification record

| Source | Opened | What I read |
|---|---|---|
| Steinacker 2303.08012 (JHEP 05 (2023) 129) | ar5iv HTML | text ranges 0-100k, 100-200k, 150-250k, 250k+ via tool: eqs 4.14-4.21, 5.3-5.10, 6.1-6.32, 7.1-7.38 as reported |
| Manta-Steinacker-Tran 2411.02598 | arXiv HTML | first ~100k chars: eqs 3.4-3.49, 2.32-2.41 as reported |
| Steinacker 2609.08955 (submitted 8 Sep 2026) | arXiv HTML | Sec 7 (eqs 84-105) as reported; abstract page |
| Klammer-Steinacker 0805.1157 (JHEP 0808:074) | abs page | abstract |
| Blaschke-Steinacker-Wohlgenannt 1012.4344 (JHEP 1103:002) | abs + ar5iv | abstract; Secs 3-6 partly (200k chars of ~176k+); Lambda² coefficient not extracted |
| Kumar-Steinacker 2312.01317 | abs page | abstract |
| Steinacker-Tran 2405.09804 | abs page | abstract |
| Battista-Steinacker 2310.11126 (v2 Feb 2025) | abs page | abstract |
| Manta-Steinacker 2502.02498 | abs page | abstract |
| Visser gr-qc/0204062 | ar5iv | eqs 20-23, 29-38, Table 1 as reported |
| Frolov-Fursaev-Zelnikov hep-th/9607104 | abs page | abstract |
| Solodukhin 1104.3712 | ar5iv | eqs 26-27, 55-59, 67, 70, 82-83, 126, 136-137 as reported |
| Fursaev hep-th/9405143 | abs page | abstract |
| Hanisch-Pfäffle-Stephan 0911.5074; Pfäffle-Stephan 1101.1424 | abs pages | abstracts; a_2 content from search snippets only |
| Bianchi et al. 2104.01220 | abs page | abstract |
| Faraji Astaneh-Berthiere-Fursaev-Solodukhin 1703.04186 | abs page | abstract |
| Lee-McGough-Safdi 1403.1580 | abs page | abstract (no f_a, f_b, f_c content there) |
| Bern-Dixon-Perelstein-Rozowsky hep-th/9809160, hep-th/9811140 | abs pages | abstracts |
| Bern-Dixon-Dunbar-Kosower hep-th/9611127 | abs page | abstract |
| Miller 2608.26242 | abs page | abstract |
| Dunne hep-th/0406216 | abs page | abstract only (not used for specifics) |
| Dong 1602.08493 (shape dependence), 1511.06713, Kim 1706.07110, Luongo-Mancini 2101.11567, 1607.00263, Liao 2609.40183, 2509.24753, 2511.01366 | search snippets or earlier scout | not independently verified in this scout beyond what is stated |
| JHEP04(2026)044 (modified gravity at large scales) | Springer page not reachable | not verified; arXiv ID unknown |

Not found: any published a_2^Σ for a twisted or torsionful Dirac operator; any 2025-2026 independent result on the sign of G_N from IKKT beyond c_K² > 0; any published BPS-index argument that the SD vanishing is lifted by a particular non-chiral background.

## 7. Summary for the orchestrator (10 lines)

1. The published EH route (Steinacker 2303.08012, Manta-Steinacker-Tran 2411.02598) evaluates the one-loop quartic on an arbitrary background via the bilocal δF(x,y) and the SO(1,9) character. It never takes δ²Γ/δA².
2. NAMCG's 026 quartic S_4 and 027 remainder correspond to the published pure-M term (eq 5.8-5.9, "dropped") and to the K-free fibre term (Sec 7.1.2, Lorentz-violating, eqs 7.11-7.13).
3. The only covariant EH entry is the mixed term V_4,mix (eq 6.19) giving 1/G_N = (2c_K²/π³)ρ^{-2}m_K², with m_K the transverse flux/KK scale (m_Λ² = m_K² μ_Λ², eq 6.6).
4. Visser/Frolov-Fursaev give 1/G = -(1/2π)Str[k_1 m² ln(m²/μ²)] when Str k_1 = 0: the published form of the mass-insertion lemma; its sign depends on the spectrum.
5. Top routes: F, compare the 027 remainder with the fibre term and the Pauli-Sakharov formula; B, V_4,mix chain with a KK sum; B, A-side log by assembly (Solodukhin eq 70 plus Ω and torsion).
6. No published a_2^Σ with bundle curvature or torsion; bulk torsion a_2 exists (Hanisch-Pfäffle-Stephan).
7. No new 2025-2026 sign result for G_N; sign rests on c_K² > 0 with a Euclidean K metric and on Lorentzian i factors.
8. Chirality/SUSY vanishing has an amplitude-level analogue (all-plus vanishes in SUSY); analogy only.
9. Emergence risk low provided K and its Euclidean metric are matrix data.
10. Unverified: JHEP04(2026)044, SD spectrum statement, Bern-Morgan, several snippets (see table).
