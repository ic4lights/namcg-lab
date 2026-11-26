SME-SCOUT: 11 routes | TOP: F:Lorentzian iε Schwinger / perturbative-in-flux organisation of the CP^{1,2} one-loop coefficient (Casimir identities of 1910.00839 eqs 2.6, 2.18; Steinacker–Tran 2405.09804 eqs 4.1–4.3 + fn 16); B:classify the replica via Herzog–Nishioka (contact term vs modular boundary term) plus Lewkowycz–Maldacena smooth-replica logic; B:holonomy-Rényi template for c_A at intermediate flux (Jing–Niu–Xian 2511.01366, eqs 61, 67, 127–128) | EMERGENCE-RISK: low

(Saved verbatim by the orchestrator; the SME agent is read-only. Advice only. No derivations and no manuscript text.)

# SME scout: replica/flux datum for B, regulator and stability for F, Lorentzian tie to E

## 0. Reading mode and trust level

- **Repository reading: digest + targeted reads.** I read the ledger tail (017–022), `proposals/021-spin-contact-term/review-r2.md`, `proposals/022-Qinv-contraction/review-r2.md`, and the previous scout `reports/sme-scout-gluing-fermions-20261015.md`. I read no chapter files. I did not repeat the previous scout's content (graded-trace twist, SO(1,9) character supertrace, Troost locus, Larsen–Wilczek, Fursaev–Miele).
- **Literature reading.** Every arXiv ID below was fetched live from the abs page or an HTML/ar5iv full text. The fetch tool summarises pages, so equation numbers are as reported by that tool. Re-open the paper before putting an equation number in the manuscript. Where I saw only an abstract I say so.
- **Search coverage.** Several WebSearch and arXiv-API queries per topic. Papers dated 2026 (e.g. 2609.08955, 2609.40183) were opened on their abs pages and exist as listed.
- **Not opened or not used.** 2609.13163 was listed by the API with inconsistent date metadata and was not opened. Dowker 1510.08378 and Belin et al. full text were not read in this scout.

## 1. Bottom line in eight points

1. **No published result gives an entanglement area coefficient as a function of an intermediate flux of ∇lnρ through a conical tip.** I found none after searching squashed cones, regularised cones, cosmic-brane/backreaction and dilaton-gravity Rényi. The 021 datum "c_A at intermediate flux" is not available off the shelf. The closest published analogue is an Abelian holonomy (charged Rényi) at the tip, where the area coefficient is an explicit quadratic function of the holonomy (§2, R-B2). The analogy has a real caveat: a holonomy is compact and periodic, while ∇lnρ is a real gradient.
2. **The 2-versus-0 split in 021 has exactly the shape of the published non-minimal-coupling dispute.** Solodukhin's review, §3.16, eqs (141)–(144), says the δ-potential on the cone gives the (1/6−ξ) entropy that matches the renormalisation of 1/G, and the review does not accept it as an entanglement entropy. Herzog–Nishioka (1610.02261, eqs (5), (24), (98)) take the opposite resolution. The modular Hamiltonian has a boundary term. In the path integral it is a codimension-2 counterterm, equivalent to the Friedrichs extension, that removes the δ-potential. The entropy is then ξ-independent, and the Adler–Zee contact term δΘ/δR is what makes the induced-G side ξ-dependent. For NAMCG, "fixed-state replica" corresponds to H–N's contact-free answer, and the "smooth replica carrying the R_G^(1) = −2□δlnρ contact" corresponds to the Solodukhin/Adler–Zee δ-potential answer. The literature has not settled which is "the" entanglement entropy. A 2025 paper (2511.21504) still uses the δ-term route without discussing H–N.
3. **A genuinely dynamical emergent metric changes the question.** In Lewkowycz–Maldacena (1304.4926) and Dong (1601.06788) the replica is the backreacted smooth geometry. This is forced when the metric is dynamical. If NAMCG's G is dynamical at the order considered, the smooth replica is the one that defines the generalised entropy. Then G_A = G_T holds by construction, so the 0 = 0 at IKKT is a consistency identity, not evidence. This reading is my inference from the verified sources, not a statement in them.
4. **The matrix-model literature does say how the state selects the entanglement frame.** Frenkel (2311.10131) finds that for a general noncommutative background the area law holds with respect to a metric G̃ = κ(σ)G, with κ set by the state through K_ij = ⟨Π^iΠ^j⟩ (eqs (67), (74), (76), (11)). The author draws the string-frame/Einstein-frame analogy. This is the only published statement I found about which conformal frame a matrix state's entanglement sees. It is the natural home for a "ρ-gradient" datum, but it is for Gauss-law (edge-mode) entropy in matrix QM, not the Poisson-limit field-theory replica.
5. **Matrix-model area laws found so far have coefficient 1/e², not 1/G.** Frenkel–Hartnoll (2301.01325 abstract): proportionality constant = inverse emergent Maxwell coupling. Craps et al. (2602.02683 abstract): in c = 1 matrix QM the dilaton-dependent gravitational area term is absent from the singlet sector and is conjectured to sit in non-singlet sectors. Both are relevant to 021's open avenue "symplectic-gauge edge term, bounded at c_A = 1".
6. **The published IKKT one-loop programme does not use a heat-kernel or Casimir proper-time cutoff.** The regulator is a Lorentzian Schwinger integral with α → α − iε (Steinacker–Tran 2405.09804 eqs (4.1)–(4.3) and fn 16: needed because □_{1,3} is not positive; Manta–Steinacker–Tran 2411.02598 eqs (3.4)–(3.5), fn 9; Karczmarek–Steinacker 2207.00399 abstract). Finiteness is attributed to maximal SUSY plus finitely many degrees of freedom per volume. I found no paper using the so(4,2) Casimir as the proper-time operator. The Casimir identities themselves are standard in that literature: □ = C²[so(4,1)] − C²[so(3,1)] (1910.00839 eq (2.18)), □_H = −C²[so(4,2)] + C²[so(4,1)] (eq (2.6)).
7. **Tachyonic formal modes are treated as artefacts or removed by changing the background in the published work.** 2411.02598 gives m_s² = −s/R² for the undeformed background and calls it presumably an artefact. It replaces it by a positive Δ_J² (eq (2.37)) via a modified background T^μ̇ = f(τ)t^μ̇ (Appendix C). 2609.08955 §8 says extra modes "seem unstable at face value" but expects stabilisation by vacuum energy. 2509.24753 stabilises a fuzzy K only through a classical RR charge/rotation (eqs (3.27), (3.35), (4.27)–(4.28)); for ℓ = 0 it is unstable. This agrees with 022's finding that the compact five-matrix background (49/154/385/814 negative modes) is unstable, and says the published cure is a change of background, not a regulator.
8. **For E, the literature says do not Wick-rotate.** Chou–Nishimura–Tripathi (2501.17798, accepted PRL) find the Euclidean and Lorentzian IIB matrix models inequivalent in an N = 2 Lefschetz-thimble study without fermions. Steinacker (2609.08955, §4, as reported by the tool) says a full Wick rotation is not useful for his approach. A Euclidean G_N sign or heat-trace coefficient therefore has no independent claim to be the Lorentzian one.

## 2. Route map (a): B, the replica/flux sub-lemma (Problem A sub-lemma)

### R-B1 (TOP): classify the 021 replicas against the published contact-term resolutions
- **Sub-lemma.** Map the 021 pair {fixed-state replica, first-order smooth replica} onto {Herzog–Nishioka boundary term / Friedrichs extension, Solodukhin–Adler–Zee δ-potential contact}. State which of c_A = 2, 1, 0 each corresponds to, and whether the vector contact −1 (Kabat/Donnelly–Wall) is the gauge analogue of the H–N term. Then state what the dynamical-metric argument (LM/Dong) implies if G = G[Θ] is dynamical at the order considered.
- **Key references and equations.**
  - Solodukhin 1104.3712, §3.16: eqs (141)–(144); §3.7.1 eqs (56)–(59) on δ² terms of order (1−α)². Read via ar5iv.
  - Herzog–Nishioka 1610.02261: §2.1 eqs (5), (10)–(12) and boundary condition (15); §2.2 eqs (16)–(25), counterterm (24) δI_E = −2π(1−α)ξ∫φ². §5 eqs (80)–(82) Adler–Zee, (83)–(90) trace/EOM freedom, (93)–(98) Rosenhaus–Smolkin and the statement that adding the boundary term amounts to removing the contact term. They identify the counterterm with the Friedrichs extension. The sign of the path-integral term flips in Lorentzian signature (their remark after (24)).
  - Lewkowycz–Maldacena 1304.4926 and Dong 1601.06788 (abstracts only): the replica is the backreacted smooth geometry; cosmic-brane tension T_n = (n−1)/(4nG_N).
  - Kabat hep-th/9503016 (abstract) and Donnelly–Wall 1506.05792 (already in the bib) for the vector contact.
- **NAMCG objects.** The 021 block: R_G^(1) = −2□δlnρ, Q_f = Q_s = 1/4, c_A^sm = −N_tot/12, and the 2/1/0 table.
- **Expected form.**
  - A table of which published prescription each 021 number matches.
  - If the dynamical-metric argument applies, a statement that G_A = G_T follows from the generalised-entropy structure, and hence that 0 = 0 is the expected consistency identity.
  - The remaining physical content is then whether the Λ² coefficient of the induced action, not of the replica, is nonzero.
- **Constraints.**
  - Solodukhin explicitly does not accept the δ-potential result as an entanglement entropy, and says the appropriate treatment of non-minimally coupled fields is "not yet available" (§3.16). Do not present either replica as settled.
  - H–N is a scalar free-field analysis (half-space and spherical surfaces, flat background). The Dirac and gauge cases are not in it.
  - I did not read whether H–N relate their boundary term 2πξ∫φ² to Wald's −2πξφ²-type term. Check this before claiming that the Wald/Dong comparison closes the gap.
  - 2511.21504 (Manea) is a recent example of the δ-term heat-kernel route without H–N (eqs (3.16)–(3.17), (5.39)–(5.43)). It shows the split persists in current practice. I read it only to that extent and do not recommend it as an authority.
- **Emergence.** Preserved. The replica choice is a statement about the Θ-built G and ρ.
- **Feasibility.** High, as a classification. **Value:** a conditional sharpening that moves 021's "which replica" from open to "two published prescriptions, one of which is dictated if G is dynamical". It is not a derivation of G_T = G_A.

### R-B2: holonomy-Rényi template for c_A at intermediate flux
- **Sub-lemma.** Use the area coefficient on a cone with an Abelian holonomy μ_E as the nearest published function that interpolates between a "no flux" value and another value. Test whether the Dirac c_A(flux) in the 021 class has the same low-degree polynomial structure in an effective holonomy built from ∇lnρ.
- **Key reference.** Jing–Niu–Xian 2511.01366 (JHEP; v3 2026-05-07), via arXiv HTML:
  - twist Φ(ϕ+2πα) = e^{iμ_E}Φ(ϕ), eq (32);
  - surface coefficient C₂(α,μ_E) = (1/6)(1/α²−1) + μ_E²/(4π²α²) − μ_E/(2πα²), eqs (61), (63), (126);
  - von Neumann weight (1/6 − μ_E/2π + μ_E²/4π²), eqs (67), (127)–(128). It equals 1/6 at μ_E = 0 and 2π, and −1/12 at μ_E = π.
  - The tool flagged a sign-convention inconsistency between eq (67) and the d = 2 form eq (68) and the use of |μ_E| in (127). Re-read before using.
  - Scalars only. No Dirac result in the paper.
- **Related.**
  - Belin et al. 1310.4180 (abstract only): charged Rényi entropies with a Wilson line around the entangling surface; free-field computations.
  - Dowker 1510.08378 (abstract, from the previous scout): Dirac twist weights vary with chemical potential.
- **NAMCG objects.** The 021 weights (+1 Dirac, −1 vector, 0 scalars/ghosts), the endpoints c_A = 2 (zero flux) and 0 (full deficit), and the interpretation of ∇lnρ flux as a tip datum.
- **Expected form.** A closed-form function of one flux parameter, probably polynomial of low degree, with the 021 endpoints as boundary values. A midpoint value would be a falsifiable prediction of the template.
- **Constraints.**
  - Holonomy is compact: the formula is 2π-periodic. ∇lnρ flux is a real non-compact quantity. A periodic formula applied to it would be an unjustified identification.
  - For a real (non-imaginary) background potential the analytic continuation of μ_E must be done, and the resulting coefficient need not be a polynomial.
  - The flux in NAMCG enters through the weighted Lichnerowicz term (a curvature-type coupling, 021), not through a minimal U(1) coupling of a charged field. The template is an analogy for the form, not a derivation.
- **Emergence.** Preserved.
- **Feasibility.** Medium-low. **Value:** conditional sharpening. If the structure matches, it supplies an interpolation law. If not, it shows that gradient flux is a different class from holonomy.

### R-B3: state-dependent entanglement frame (Problem A)
- **Sub-lemma.** Ask whether the 021 "flux of ∇lnρ" is the gradient of a state-dependent conformal factor κ between the emergent G and the metric G̃ in which the matrix entanglement obeys an area law. If so, the replica "selected by the state" is the one where the entangling data are measured in G̃, and the flux becomes a statement about ∇lnκ.
- **Key references and equations.** Frenkel 2311.10131 (via HTML):
  - Subregion by projector Θ_Σ = χ_Σ(X), eqs (27)–(30).
  - Edge-mode operator Q_Σ, eqs (38), (75). Entropy split, eq (41).
  - Effective metric: Tr[Q²] = Tr[Θ O_Q(Θ)] + O(1/N), eq (74), with O_Q = K_ij[X^i,[X^j,·]], eq (76), K_ij = ⟨Π^iΠ^j⟩, eq (67). Area law with respect to G̃ from eq (11), not G. G̃ = κ(σ)G when K ∝ δ.
  - Frenkel–Hartnoll 2301.01325 (abstract only): Gauss-law entanglement, coefficient equal to the inverse emergent Maxwell coupling.
- **NAMCG objects.** The Problem A state, ρ, and the Poisson-limit metric G built from Θ.
- **Constraints.**
  - Frenkel's setting is matrix QM with a Gauss-law edge-mode entropy and a Gaussian wavefunction near a classical minimum. It is not the Poisson-limit replica.
  - It uses a fixed-time subregion projector, and K_ij is a momentum-space (Π) correlator, which has no obvious Euclidean heat-kernel analogue.
  - The paper does not use a Liouville density ρ (checked in the part I read). The identification of κ with ρ would be a hypothesis.
  - The coefficient is 1/e², not 1/G, so this supplies the A-side frame question, not the area coefficient.
- **Emergence.** Preserved, and positively relevant. The frame is emergent from the state.
- **Feasibility.** Medium-low. **Value:** potentially a genuine Problem A structural statement (state selects the replica frame), but a conditional one.

### R-B4: edge-sector origin of a missing gravitational area term
- **Sub-lemma.** Check whether the Maxwell-like edge term for the symplectic gauge sector (021 avenue 3, bounded at c_A = 1) has the 1/e² structure of Frenkel–Hartnoll, and whether any dilaton-dependent area term lives in a non-singlet or edge sector as proposed by Craps et al.
- **Key references.** Craps et al. 2602.02683 (abstract only): the leg-pole transformation cannot produce the gravitational area term; non-singlet sectors suggested. Frenkel–Hartnoll 2301.01325; Fliss–Frenkel–Hartnoll–Soni 2408.05274 (from the previous scout); review 2512.03163 (not re-read here).
- **Feasibility.** Low-medium. **Value:** hypothesis check; it keeps the bound c_A ≤ 1 honest.
- **Constraint.** Čubrović 2203.10697 uses "replicas" for quenched disorder in the IIB matrix model, not entanglement replicas. Do not cite it for B. Target-space entanglement papers I opened (Tsuchiya–Yamashiro 2201.06871) treat a different matrix model (bubbling geometry). None addresses a modular Hamiltonian or replica gluing in IKKT on a covariant quantum space.

## 3. Route map (b): F, regulator and stability

Context for the 022 top avenue (so(4,2) Casimir as proper-time operator in the four-matrix class). The relevant published facts are these: the Casimir identities exist, the regulator used is not a Casimir cutoff, and the stabilisation mechanisms are not regulator choices.

### R-F1 (TOP): formulate the CP^{1,2} one-loop coefficient with the Lorentzian iε Schwinger integral, organised perturbatively in the flux
- **Sub-lemma.** Replace the Euclidean heat trace e^{-sBox_E} by the Lorentzian form used in the IKKT literature, with α → α − iε, applied to the formal Lorentzian density already recorded in 018, (5m²−3l²)/(4m⁶). Expand in the flux through the SO(1,9) character as in the previous scout's R-b1. The Nielsen–Olesen blow-up e^{s|f1−f2|} belongs to the resummed Euclidean heat trace and need not be present order by order in the flux expansion.
- **Key references and equations.**
  - Steinacker–Tran 2405.09804: eqs (4.1)–(4.3), fn 16 (the oscillatory integral is needed in Minkowski signature because □_{1,3} is not positive), eq (5.11) (the 6d operator [ℱ,[ℱ,·]] is non-negative, so the internal inner product is positive), eqs (5.6) onward (O(α⁰) and O(α²) cancel by maximal SUSY). The mass formula is in §6, which I did not read.
  - Manta–Steinacker–Tran 2411.02598: eqs (3.4)–(3.5) with fn 9, character Q₁₀ eq (3.7), momentum integral (3.23), result (3.30), definition of 1/G_N (3.33), explicit |K| = 4 value (3.49).
  - Steinacker 2609.08955: eqs (86)–(88) (one-loop trace log with (□ − iε), V₄[δℱ] = −4tr δℱ⁴ + (trδℱ²)²), vacuum energy (90), EH term (91), definition of G_N (92). The tool reported that the G_N sign is not stated in the part it returned (§7.2 truncated), and that V₄ ≤ 0 holds for Euclidean ℱ of rank ≤ 4.
  - Casimir identities: Steinacker 1910.00839 eqs (2.6), (2.7)/(2.9), (2.18), (4.6): □ = C²[so(4,1)] − C²[so(3,1)] on the sectors 𝒞^s, spin Casimir 𝒮² = 2C²[so(4,1)] − C²[so(4,2)] = 2s(s+1), fluctuation operator 𝒟² = □ − 2ℐ. These match the 018 statements Box = C_so(4,1) − C_so(3,1) and H_V.
- **NAMCG objects.** 018 formal Lorentzian density; 022 identity H_V = C_so(4,2) − C_G + C_Σ + μ²; the 011 torsion identity.
- **Constraints.**
  - Steinacker argues (2303.08012 §3, from the previous scout) that a heat-kernel UV cutoff is inappropriate. A Casimir-based proper-time regulator is a different object, and I found no paper that uses it. Treat "so(4,2) Casimir regulator" as new, with no published template.
  - The published sign of 1/G_N rests on c_K² > 0 or Δ² > 0 for a compact fuzzy K (2303.08012 eqs (6.30)–(6.32); 2411.02598 eq (3.49)). It does not come from the Λ² coefficient. NAMCG's w must be compared with this structure, not with a cutoff coefficient.
  - Battista–Steinacker 2310.11126 v2 corrected a sign error in eq (79) that changed the conclusions. Signs in this family are fragile.
  - The published constant η_{ab} in □ = η_{ab}[T^a,[T^b,·]] is a Lorentzian bilinear in the action. That is an input to the matrix model. NAMCG's four-matrix class has the same kind of input (022), so this route does not by itself address E.
- **Emergence.** Preserved if η is kept as the action's bilinear form and the metric is read from the symbol. At risk only if the iε contour is chosen using a background metric. State the contour in terms of the operator □ only.
- **Feasibility.** Medium. **Value:** a genuine step for F if it gives a finite, sign-definite w without the NO divergence. Otherwise a sharpening that locates the divergence in the resummation.

### R-F2: matrix-intrinsic fibre truncation (admissible modes)
- **Sub-lemma.** Check whether the matrix-intrinsic admissibility condition on 𝒞^s (a bound relating the SO(4,1) quadratic Casimir to the spin s) and the spin cutoff s ≤ m = r⁻¹x⁰ provide the "fibre-harmonic cutoff" that 018, 020 and 022 list as avenues (4), (5), without a non-matrix input.
- **Key references and equations.**
  - 1910.00839 eq (3.34): r⁻²□_H > s² + s + 9/4 on admissible modes; Lemma 5.1 (𝒦 > 0); eqs (5.37)–(5.40) (complex eigenvalues replaced by real vectors).
  - Manta–Steinacker 2502.02498 eq (70): cutoff s ≤ m = r⁻¹x⁰ from the S² fibre uncertainty ΔT ~ r⁻¹√m; eq (29): End(ℋ₀) ≅ 𝒞(ℂP^{1,2}) for almost-local functions; eqs (5), (8c), (9)–(12).
  - 2411.02598: only modes in the image of the quantisation map are integrated (§2).
- **Constraints.**
  - The cutoff is position dependent (via x⁰), so it is not SO(4,1)-invariant in an obvious way. A hypothesis check is needed against 022's hypothesis class.
  - In these papers the fibre S² is compact with a fuzzy cutoff, whereas the 018–022 text speaks of an "unbounded fibre". I could not reconcile the two from the review texts alone. This should be confirmed against the chapters before this route is attempted.
- **Emergence.** Preserved. **Feasibility.** Medium. **Value:** conditional sharpening; it may turn an arbitrary regulator into a matrix-derived one.

### R-F3: stabilisation by charge/rotation, and why it needs Lorentzian time
- **Sub-lemma (bounded).** State what published stabilisation mechanisms would imply for the 022 compact negative-mode counts, without trying to use them.
- **Key references and equations.**
  - Manta–Steinacker 2509.24753 (via HTML): static K collapses classically (§3.2.2); rotating ansatz f = χe^{iω}, eq (3.27); constraint [𝒦⁺,𝒦⁻] = 0, eqs (3.18), (3.29); RR-charge conservation ω̇ = ℓ/(αχ)² e^{−3τ}, eq (3.35); V_eff eq (4.27) with minimum (4.28); for ℓ = 0 the minimum is at χ = 0 (unstable). Quantum effects are invoked only for ε and the dilaton (§3.3). The paper's one-loop treatment is a sketch (eq (3.53)).
  - Steinacker–Tran 2405.09804 introduction: coupling K to a U(1) flux bundle stabilises K (detailed analysis in their §7, not read).
  - Berenstein–Trancanelli 1011.2749 and Sugiyama–Yoshida hep-th/0207190 (abstracts, from the previous scout).
- **Value.** A rotation/charge stabiliser is a time-dependent Lorentzian mechanism. It cannot appear in a Euclidean heat trace. This is a published reason why a Euclidean-only F can show negative modes that the Lorentzian programme does not count.
- **Feasibility.** Low as an attempt. **Use:** a constraint on what a "stable compact section" must look like.

### R-F4: structural consistency with the Casimir/Lie-algebra obstruction
- **Sub-lemma.** Check that 022's two facts (a five-matrix X^A = M^{A5} needs a bilinear μ² = +4, and the six presentations M^{Ac0} give Euclidean or (2,2) horizontal metrics) are consistent with Liao's classification.
- **Key reference.** Liao 2609.40183 (abstract and comments only): for Lie-algebra saddles in finite-dimensional unitary representations, a Casimir obstruction forces the symmetric form h = 0 when the complexified algebra is simple, which is said to explain why fuzzy spheres and expanding-universe solutions need mass terms or IR regulators. Lorentzian saddles in ≤ 11 dimensions need a nonzero solvable radical ("space can be semisimple; time must be solvable").
- **Constraints.** The result is for finite-dimensional Lie algebras. The doubleton of so(4,2) is infinite-dimensional, and the covariant quantum spaces are not Lie-algebra saddles in this sense. Treat it as a heuristic cross-check only. I have not read beyond the abstract.
- **Feasibility.** High as a bounded check. **Value:** consistency and a possible organising explanation for 022's "never Lorentzian".

## 4. Route map (c): E, Lorentzian-continuation tie

### R-E1 (TOP for E): do the weight-two coefficient in the Lorentzian iε form first, and only then compare with the Euclidean one
- **Sub-lemma.** Whatever sign and size w has in the Euclidean sub-Laplacian calculation is not a Lorentzian result unless reproduced with the Lorentzian density and the iε contour (R-F1).
- **Key references.**
  - Chou–Nishimura–Tripathi 2501.17798 (abstract): Euclidean and Lorentzian IIB matrix models are inequivalent in the N = 2 bosonic Lefschetz-thimble comparison. Different saddles appear near γ = 0 and for γ > 0. The conclusion is explicitly contrary to naive QFT expectation. Limitations: N = 2, no fermions.
  - Steinacker 2609.08955 §4 (tool-reported): a full Wick rotation is "not useful" and the Lorentzian model is not simply related to the Euclidean one.
  - Karczmarek–Steinacker 2207.00399 (abstract): the iε prescription reproduces the standard Feynman propagator locally at late times on a 1+1 Minkowski solution.
  - Hatakeyama et al. 2112.15368 (abstract): a constrained model where spacetime is Euclidean at early times and becomes Lorentzian at late times.
- **Constraint.** A continuation from the Euclidean value is not licensed by the published numerics. NAMCG's claim that a sign obtained in a Euclidean section carries over should be flagged as an assumption wherever it appears.
- **Emergence.** Preserved. **Feasibility.** Medium (same computation as R-F1). **Value:** converts a 'Euclidean w' into a statement about E.

### R-E2: numerical Lorentzian evidence as a consistency target (not a derivation)
- **References (abstracts only).** Anagnostopoulos et al. 2604.19836 (complex Langevin, N up to 128, deformed Lorentzian model: a (3+1)-dimensional expanding spacetime emerges with space and time smooth and real); 2604.25564 (Lorentz symmetry gauge-fixed, SUSY impact); 2407.03491, 2307.01681 (titles only); Nishimura 2205.04726 (mass-term route to late-time Lorentzian).
- **Use.** These show that emergence of a real Lorentzian time is a dynamical outcome in the full Lorentzian model, which is consistent with NAMCG keeping signature open (Problem E). They do not constrain the one-loop coefficient on a fixed covariant background.
- **Feasibility.** Not a derivation route. **Value:** context for the E disclaimer.

### R-E3: the signature input in the published programme
- **Observation.** In the IKKT papers above the Lorentzian signature is an input through the SO(9,1)-invariant bilinear in the action. It is "emergent" only in the sense that the induced metric on the brane is read from the symbol. NAMCG's retention of ass:lorentzian is in line with the field. A claim of matrix-derived signature would be ahead of what the Lorentzian IKKT literature asserts. 2609.40183 gives a structural criterion (solvable radical for time) in a restricted class.
- **Feasibility.** N/A. **Value:** calibration of what Problem E can realistically claim.

## 5. Ranking across routes

| Rank | Route | Problem | Feasibility | Genuine or conditional | Emergence |
|---|---|---|---|---|---|
| 1 | R-F1 Lorentzian iε Schwinger, flux-perturbative organisation | F (and E) | medium | genuine step if finite and sign-definite; else sharpening | preserved |
| 2 | R-B1 classify replicas vs H–N / Solodukhin / LM | B, A | high | conditional sharpening | preserved |
| 3 | R-B2 holonomy-Rényi template for c_A(flux) | B | medium-low | conditional sharpening | preserved |
| 4 | R-E1 Lorentzian-first rule for w | E, F | medium | calibration; shares work with R-F1 | preserved |
| 5 | R-F2 matrix-intrinsic fibre truncation | F | medium | conditional sharpening | preserved |
| 6 | R-B3 state-dependent entanglement frame κ | A, B | medium-low | possible Problem A structure | preserved, positive |
| 7 | R-F4 Casimir/Lie-algebra consistency | F, E | high | bounded check | preserved |
| 8 | R-B4 edge-sector origin of area term | B | low-medium | hypothesis check | preserved |
| 9 | R-F3 charge/rotation stabilisation | F | low | constraint | preserved |
| 10 | R-E2 numerical Lorentzian IKKT as context | E | n/a | context | preserved |
| 11 | R-E3 signature input calibration | E | n/a | context | preserved |

**Top three targets.**
1. F: R-F1.
2. B: R-B1.
3. B: R-B2.

R-B1 is cheap and should be done before R-B2, because it fixes which replica the flux interpolation is about.

## 6. Conflicts and no-gos to respect

- **Solodukhin §3.16 (eqs 141–144):** the δ-potential entropy is not accepted as an entanglement entropy. The mismatch between the renormalisation of G and of the entropy is stated as a puzzle.
- **Herzog–Nishioka:** the entanglement result is ξ-independent once the boundary term is included, and the ξ-dependence of the induced-G side comes from the Adler–Zee contact term. If the NAMCG fixed-state replica is H–N's, then the gap between G_T and G_A is expected in the published scalar setting, and what remains is which quantity gravity sees.
- **Kabat and Donnelly–Wall:** the vector contact is an edge-mode effect (already used). The Dirac field with Levi-Civita spin connection has no such mismatch (Kabat abstract). 021 is consistent with this.
- **LM/Dong:** with a dynamical metric the replica must be the smooth one. A fixed-state replica is then not the generalised entropy. This applies only if G = G[Θ] is treated as dynamical at the order computed.
- **Steinacker:** heat-kernel cutoffs are not appropriate for the IKKT one-loop action (2303.08012 §3, from the previous scout), and a Euclidean continuation is not the route he takes (2609.08955 §4, tool-reported). NAMCG's Λ² comparison and Euclidean contraction inherit both caveats.
- **Chou–Nishimura–Tripathi:** Euclidean ≠ Lorentzian in the IIB matrix model (N = 2, bosonic).
- **Weinberg–Witten family:** not touched by any route here, since the graviton is a composite of matrix modes.

## 7. Verification record

| Source | What I opened | What I read |
|---|---|---|
| Solodukhin 1104.3712 | ar5iv, offsets 60000–235000 | §3.7.1, §3.9, §3.15, §3.16 (eqs 141–144), §4.2.1 remark |
| Herzog–Nishioka 1610.02261 | ar5iv, ~180k chars | §2.1–2.2 (eqs 5, 10–12, 15, 16–25), §5 (eqs 79–102), §7 |
| Lewkowycz–Maldacena 1304.4926 | abs | abstract only |
| Dong 1601.06788 | abs, search snippets | abstract; tension T_n from search snippet |
| Dong 1310.5713; Camps 1310.6659 | abs | abstracts only |
| Fursaev–Patrushev–Solodukhin 1306.4000 | abs | abstract only (squashed cones, extrinsic curvature) |
| Manea 2511.21504 | abs + HTML | eqs (2.5), (3.15)–(3.22), (4.28), (5.37)–(5.43) via tool |
| Jing–Niu–Xian 2511.01366 | abs + HTML to 100k chars | eqs (32)–(37), (55), (60)–(63), (67)–(71), (122)–(128) via tool; sign convention flagged |
| Belin et al. 1310.4180 | abs | abstract only; PDF unreadable by the tool |
| Frenkel 2311.10131 | abs + HTML to 100k chars | eqs (11), (25)–(30), (38), (41), (45)–(47), (61)–(66), (67), (74)–(76) |
| Frenkel–Hartnoll 2301.01325 | abs | abstract only |
| Craps et al. 2602.02683 | abs | abstract only |
| Tsuchiya–Yamashiro 2201.06871; Čubrović 2203.10697 | abs | abstracts only (not used as sources for B) |
| Fliss–Frenkel 2609.36015 | abs | abstract only (replica circle and conical deficit in the 't Hooft expansion; not used) |
| Steinacker 1910.00839 | HTML to 100k chars | eqs (2.6), (2.7), (2.9), (2.18), (3.34), (3.46), (4.6), (5.24)–(5.26), (5.37)–(5.40), Lemma 5.1 |
| Manta–Steinacker 2502.02498 | abs + HTML to 100k chars | eqs (5), (8c), (9)–(12), (29), (70) |
| Manta–Steinacker 2509.24753 | abs + HTML to 100k chars | eqs (3.18), (3.27), (3.29), (3.35), (3.51)–(3.54), (4.13), (4.27)–(4.28) |
| Manta–Steinacker–Tran 2411.02598 | HTML to 100k chars | eqs (2.37), (3.4)–(3.7), (3.23), (3.30), (3.33), (3.49), fn 9, App. C remark |
| Steinacker–Tran 2405.09804 | HTML to 100k chars | eqs (4.1)–(4.4), (5.6), (5.10)–(5.15), (5.21)–(5.27), fn 16; §6–7 not read |
| Steinacker 2609.08955 | HTML to ~180k chars (two fetches) | eqs (47)–(62), (85)–(92), (114); §4, §8 remarks |
| Battista–Steinacker 2310.11126; Kumar–Steinacker 2312.01317; Karczmarek–Steinacker 2207.00399 | abs | abstracts only |
| Chou–Nishimura–Tripathi 2501.17798 | abs | abstract only |
| Anagnostopoulos et al. 2604.19836, 2604.25564; Hatakeyama et al. 2112.15368 | abs | abstracts only |
| Liao 2609.40183 | abs (twice) | abstract and comments only |
| Muramatsu 2608.29688 | abs | abstract only (not used) |

**Not independently verified.**
- All equation numbers beyond those in the table were not re-opened.
- Steinacker 2609.08955 §7.2 G_N sign, which the tool reported as truncated.
- Whether H–N relate their boundary term to Wald's non-minimal term.
- The claim that any matrix-model paper selects a Poisson-limit replica. I searched and found none.
- A Dirac-fermion result for an area coefficient on a cone with holonomy. Not found.
- Statements in the previous scout about Nishioka–Yaakov, Casini–Huerta and Fursaev–Miele were not re-verified here.

**Searches that returned nothing relevant.**
- Area coefficient versus a ∇lnρ-type (gradient) flux at a conical tip.
- Modular Hamiltonian or replica gluing in IKKT/BFSS on a covariant quantum space.
- A proper-time regulator built from the so(4,2) Casimir.
- A one-loop effective action on H⁴_n/CP^{1,2} that treats Nielsen–Olesen sectors explicitly. The Steinacker programme treats tachyonic formal modes as artefacts and works with the Lorentzian iε integral.
- Das–Frenkel–Hartnoll–Mazenc–Ran–Tsuchiya as a joint target-space paper: the combination as named was not found. Tsuchiya–Yamashiro 2201.06871 and the Fliss/Frenkel/Hartnoll papers are the nearest items.

## 8. Suggested next targets for the researcher

1. R-B1, as a short classification note (no new computation): which published prescription each 021 value matches, and what the dynamical-metric reading implies.
2. R-F1/R-E1 together: the weight-two coefficient on the CP^{1,2} fibre with the Lorentzian density and the iε Schwinger integral, organised in the flux through the existing 018/022 formal density, with the Casimir identities of 1910.00839 as the operator input.
3. R-B2 once R-B1 fixes the replica. Treat the holonomy-Rényi form as a template to confirm or refute, with the non-compactness caveat stated up front.

## Summary for the orchestrator (≤ 10 lines)

- 11 routes. Top: F iε-Lorentzian Schwinger/flux-perturbative coefficient (R-F1, with E tie R-E1); B replica classification against Herzog–Nishioka/Solodukhin/Lewkowycz–Maldacena (R-B1); B holonomy-Rényi template for c_A(flux) (R-B2). Emergence risk low.
- No published area coefficient interpolates with a gradient flux; the nearest is the Abelian-holonomy cone result (Jing–Niu–Xian 2511.01366), quadratic in the holonomy, scalars only.
- 021's 2 vs 0 is the published ξR dispute: Solodukhin §3.16 (δ-potential, not accepted as entropy) against Herzog–Nishioka 1610.02261 (boundary term / Friedrichs extension; entropy ξ-independent). If G is dynamical, the smooth replica is mandatory (LM/Dong), so 0 = 0 is an identity.
- The IKKT one-loop programme uses a Lorentzian iε Schwinger regulator, treats −s/R² modes as artefacts or removes them by changing the background, and says Wick rotation is not useful; no so(4,2) Casimir proper-time regulator exists in print.
- Chou–Nishimura–Tripathi 2501.17798: Euclidean and Lorentzian IIB matrix models are inequivalent (N = 2, bosonic), so a Euclidean w does not by itself say anything about E.
- Frenkel 2311.10131 supplies the only state-dependent entanglement-frame statement (G̃ = κ(σ)G); matrix area laws in print have coefficient 1/e², not 1/G.
- All sources opened live; abstract-only items are marked in the table.
