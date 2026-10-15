SME-CONSULT: answered (Q1 and Q2 fully; Q3 partly)

Saved verbatim from the independent SME agent (mode 2, gatekeeper consultant), answering the SME consultation request in review-r1-provisional.md.

**What I read.** I pulled the PDFs of arXiv:2601.08031 (v1), arXiv:2609.08955 (v1), arXiv:2312.01317 (v1) and arXiv:0812.3761 (v2) and converted them to text locally. For 2601.08031 I also read the arXiv HTML to recover the LaTeX symbols that the PDF text drops. For 2601.08031 I read Sec. 3 to 3.2 and Sec. 4 around eq. (4.44)-(4.46) and Sec. 5. For 2609.08955 I read Sec. 8 (eqs. 110-115 and the discussion after them). For 2312.01317 I read App. C only. For 0812.3761 I read Sec. 4 and the abstract. I did not read the other chapters of these papers in full.

**Q1. Crossover form and m².** Yes, it is stated as the scout report says.
- In 2601.08031 eq. (3.25), harmonic gauge and linearised about a flat background, the equation is (1 − m² □̃⁻¹) δ𝒢^{μν} ≈ 8πG_N T^{μν}. Eq. (3.27) gives the equivalent form δ𝒢 ≈ 8πG_N □̃/(□̃ − m²) T.
- Eq. (3.28) defines δT = m²/(□̃ − m²) T = T[C]. Eq. (3.24) shows the origin: T^{μν}[C] ≈ −2α² r⁻⁴ □̃⁻¹ δḠ^{μν}, with Ḡ the trace-reversed metric perturbation.
- The m² is eq. (3.26) = (4.45): m² := 32π G_N α² r⁻⁴. I took this from the HTML LaTeX. α and r are background quantities (α² is a dilaton-type background parameter, r a background radius). I did not independently check what they are.
- The review 2609.08955 repeats this as eqs. (112)-(115). Eq. (114) is m² := 32π G_N α² r⁻⁴, and footnote 31 says the scale holds in Cartesian local normal coordinates. It adds "An equivalent form is" δ𝒢 ≈ 8πG(T+δT), δT = m²/(□̃−m²) T.
- The sign convention matters. For the static quasi-static reduction, eq. (3.30)-(3.31) gives a negative mass term, m²_cross = 1/L²_cross = (3/…)·m², with a numerical factor I could not read from the PDF text. The extra vacuum modes obey (−□̃ + m²) δḠ_{μν} = 0.

**Q1, tachyon: covariant or anisotropic?** Not Lorentz-covariant.
- Sec. 3.2: the extra modes "typically propagate with velocity c/√3, but appear to become tachyonic (and unstable) in the extreme IR scale L_cross". Standard GR modes □̃δḠ = 0 are unchanged.
- Eq. (4.44)-(4.46): the kinetic factor is (−k₀² + k²)(k₀² − k²/5 + m²). The 1/3 of Sec. 3 becomes 1/5 once the higher-spin sector is included, and the paper notes the geometric Sec. 3 treatment "does not fully capture the hs sector". The extra modes "seem to be tachyonic in the IR for k² < m²" (the paper's convention for the sign of the mass term).
- Sec. 4 says these modes have "a non-relativistic dispersion relation with group velocity less than c", and 2609.08955 calls them modes "propagating at a reduced speed … with apparent tachyonic mass of order −m²".
- So the tachyon is not a covariant mass² < 0 pole. It is a non-boost-invariant dispersion relation (k₀² = k²/3 or k²/5, minus m²). This comes from the preferred cosmic-frame direction of the FLRW-type background. It is rotation-isotropic in the paper's treatment; I did not see any explicit dependence on a spatial direction ŷ.
- Both papers say the instability is expected to be an artifact, to be cured by vacuum energy and the non-derivative YM terms (V₀₀ < 0, V₀₁ > 0). The cure is illustrated by plots only (Figs. 3-4), not proved.
- This is consistent with your proposal's "indefinite G / anisotropy from ŷ" language only if "ŷ" is the background-frame direction. I could not map your q_⊥, ξ, σ notation onto the paper's, so I cannot confirm the match.

**Q2. Is conservation of T[C] derived or imposed?** Imposed through the ambiguity, not derived.
- 2601.08031 eq. (3.5)-(3.6): C is defined by {C^μ, x_μ} = −e[F] and is not unique. It has the "gauge invariance" C → C + ∂C.
- The text after (3.11) says "the ambiguity (3.6) is used to make T^{μν}[C] divergence-free". Footnote 9 says the frame divergence constraint ∂_μ e^μ = 0, treated with Lagrange multipliers, "leads precisely to the ambiguity (3.6)".
- The same wording appears in footnote 30 of 2609.08955.
- At linear order, T[C] ≈ −2α² r⁻⁴ □̃⁻¹ δḠ is said to be divergence-free only "assuming the harmonic gauge condition ∂_μ δḠ^{μν} = 0" (after eq. 3.22). Also C^μ is called "essentially divergence-free ∂_μ C^μ ≈ 0 (A.13)" in the linearised regime. This is a gauge-choice statement rather than a derivation.
- 2312.01317 App. C does exactly this. It takes the divergence of the modified Einstein equation, "using the conservation of the Einstein tensor and of the energy-momentum tensor of matter". It then says the constraint "can be used to fix the remaining ambiguity in C_a → C_a + ∂ζ_a" and that it "determines precisely the 4 degrees of freedom" of C.
- So the Bianchi-plus-T-conservation route you describe in F2 is how the literature does it: conservation fixes the ambiguity. The papers present this as a feature, not as an independent derivation of ∇T[C] = 0.

**Q3. Poisson-limit Noether identity and stress divergence: already in the literature?** The matrix-level statement is known. I could not locate your exact Poisson-limit forms.
- Steinacker, arXiv:0812.3761 (Sec. 4, eq. 88-90), states that the translation symmetry X^a → X^a + c^a 1 gives the conservation law [X_a, T^{ac}]η_{aa} = 0, "which can also be verified directly using the matrix e.o.m. (11)". Here T^{ab} is the matrix energy-momentum tensor, T^{ab} = [X^a,X^c][X^b,X^c] + (a↔b) − ½η^{ab}[X^d,X^c][X_d,X_c] with η contractions.
- That paper credits the identity to Abou-Zeid and Dorn, hep-th/0104244 (its ref. [2, 41]), and discusses it with Das and Frenkel, hep-th/0212122 (its ref. [42]). I confirmed these citations in the reference list. I did not open those two papers.
- The semi-classical (Poisson) version is also in 0812.3761, as the "tangential" and "scalar" conservation laws (eqs. 93-99). I saw the text but did not re-derive it. I did not find a statement written as {X^a, E_a} = 0.
- Sec. 4 of 0812.3761 says the tangential law follows from the matrix e.o.m., and the scalar law follows from the tangential one. This matches your Noether identity in spirit, but I cannot say whether it is term-for-term the same identity.
- The recent review 2609.08955 (Sec. 8, p. 29) restates it: "the matrix model admits a conserved matrix energy momentum tensor [T_a, T^{ab}] = 0, which should keep potential instabilities in bound."
- Caveat on the μ² X^a X^b term. In 0812.3761 the stress is the pure YM F F form (with the trace term). It has no μ² X^a X^b term, since the mass term breaks the translation Noether symmetry. For the η-variation stress T^{ab} = F^{ac}F^b_c + μ² X^a X^b, the divergence identity [X_a, T^{ab}] ∝ e.o.m. must hold up to the μ² contribution. I found no reference that states that massive version, but I did not search the 2405.09804 or Manta-Steinacker mass-deformed literature in detail. So "known" applies to the massless-model identity. For the massive variant I would say not found.

**Could not verify.**
- The numerical prefactor in m²_cross = (…)·m² (eq. 3.31) from the text, since the PDF symbol extraction dropped it. I did not recover it from the HTML.
- The meaning of the symbols α and r in m².
- The full contents of hep-th/0104244 and hep-th/0212122.
- Any source for the Poisson-limit identity in the exact {X^a, E_a} = 0 form.
- Any source for the massive-model stress divergence identity.
- Any mapping of your q_⊥ / ξ / σ notation onto the papers' notation.

No label or verdict is offered.

Sources:
- https://arxiv.org/abs/2601.08031
- https://arxiv.org/abs/2609.08955
- https://arxiv.org/abs/2312.01317
- https://arxiv.org/abs/0812.3761
