SME-SCOUT: 7 routes | TOP: F/N:closed helicity-two level-one two-point function (tree form + induced form), poles and residues, against Steinacker 2601.08031 Eqs. 4.41-4.46; F/C:Newtonian channel (helicity 0 + trace/dilaton at q.y=0), where the 047 forms appear to give the opposite sign to c_T^TT at late times; D1:level-one gauge parameters and the Lorentz generators of 2601.08031 App. A.2-A.3, read against Hanada-Kawai-Kimura | EMERGENCE-RISK: low

Date: 2026-11-01. Branch working. Scout after integration 45 (ledger through 047).

## 0. Bottom line

1. **New finding.** The non-Lorentz-covariant fibre-trace structure of 045-047 appears in the published literature. Steinacker 2601.08031 Eq. 4.41/4.44 has the factor (d_0^2 - (1/5) d_i^2) on transversal modes and (1/5 -> 3/5) on longitudinal modes. By hand, the printed 047 forms reproduce the first factor, up to a term suppressed by 1/sinh^2 tau, and reproduce the ratio of the two on the null cone (section 2). No 044-047 proposal or review compared this paper. appH L2092 still says these results "have not been checked against the present operators".
2. **Gap 1, the 1/x term.** It looks like a change-of-variables denominator, not the signature of an integrated-out tower. Written in the frame amplitude it is polynomial. I would demote Schur elimination as the top avenue.
3. **Gap 2, on-shell TT versus Newton.** These are different channels. TT sits at |x| -> infinity. The published Newtonian/Schwarzschild mode sits at x = 1 - coth^2 tau and is a helicity-0 mode mixed with the trace/dilaton. The 047 forms suggest a sign flip there at late times. If this survives checking, it is the most consequential open question in the class.
4. **Gap 3, the negative replica gap.** Published contact and edge mechanisms have the wrong sign and the wrong species to supply it. Treat it as a missing fibre-resolved cone or entropy functional, not as a contact-term problem.
5. **Switch target?** Yes, in part. Stop narrowing "one coefficient on five polarisations for all q" on CP^{1,2} x K. 045, 046 and 047 have established that about as far as it is useful, and the field does not claim it. Move to the on-shell two-point function (F/N), the Newtonian channel (F/C), then D1. No route to A, E or G-derived beats these.

## 1. What I read, and limits

- **Mode:** digest not used, no `make_digest --check`; targeted reads only, no full scan.
- **Read in full:** ledger 045-047; sme-scout-20261101.md; 047 review-r3.md; 047 appH_insert.tex; appH L2376-2417.
- **Read as status passages:** appH Problem A, D (opening), E, F (label and missing step), G, N (opening); ch17 L690-749.
- **Process slip:** my first two tool rounds batched read-only calls, against the sequential rule in CLAUDE.md. Nothing changed, and later calls were serial.
- **How the literature was read:** through WebFetch, which returns a small model's reading of the page, not the raw text. Equation forms and quotes below are therefore second-hand. **The researcher must confirm Eqs. 4.33, 4.41-4.46 of 2601.08031 from the source before relying on them.**
- **Depth per source:**
  - HTML body, nearly whole: 2601.08031; 1910.00839 (Secs. 6.4 and 7-8 in the second part); 2609.08955 (Secs. 7-9 in the second part); 2405.09804 (intro, Secs. 4-6); ar5iv hep-th/9806078.
  - HTML, up to the truncation point: 2312.01317; 2502.02498 (first 100000 characters); 2601.13131.
  - Abstract record only: 2101.07297, 1306.4338, 1502.03758, hep-th/9607104, hep-th/9705207, hep-th/0508211, 2609.40183.
- **My own algebra:** done by hand from the printed 047 forms, no script run, not reviewed. It is marked MY CHECK. It is a pointer for the researcher and gatekeeper, not a result.

## 2. The dictionary with 2601.08031 (MY CHECK, the basis for everything below)

Rest frame of y at y^i = 0, q = (q_0, k), s^2 = sinh^2 tau. The insert's identity y_perp^2 = m^2(x-1) implies y^2 = -(l^2 + m^2), so l^2/m^2 = 1/s^2 and theta = coth^2 tau = 1 + 1/s^2. At the base point (5,3): l = 4, m = 3, s^2 = 9/16.

**Helicity +-2.** The 047 eigenvalue is IX_2 = -(6/5)(4 + 1/x) = -(6/5)(4a+b)/a, and the 1/x comes from dividing by a. With amplitude c_i = D_ij s_j:
- IX_2 * EH(h-bar) = (1/15 m^4) q^2 (4a+b) (c.c), which is polynomial in q and c.
- Exactly, 4a + b = 5 m^2 (q_0^2 - (1/5) k^2) + 4 l^2 k^2.

So the published transversal factor (d_0^2 - (1/5) d_i^2) is the 047 helicity-two form up to a correction of relative order 1/s^2.

**Helicity +-1.** On the cone it is purely longitudinal, and per unit c.c the form tends to 2a against 4a for helicity two. The ratio is 1/2, which equals (1 - 3/5)/(1 - 1/5). Off the cone the two do not agree, but the published longitudinal form is only read at the on-shell factor.

**With both sectors.** For helicity two, reading the coefficient from the printed forms and the merged L2409 expansion:
- Induced coefficient: c(x) = c_T^TT + kappa/x, with kappa = (V_1 - T_1)/20 + (3/20) T_2 > 0, using T_2 >= T_1.
- Second factor in the form: q_0^2 - v^2 k^2, with v^2 = (kappa - c_T^TT/s^2)/(c_T^TT + kappa). In the index-only limit c_T^TT : kappa = 4:1, this gives 1/5 at large s.

**What this does and does not show:**
- Both calculations use four-fibre-vector moments. 2601 Eq. 4.42 is the Wick-like pairing with 3/5, and only the EH term carries it (the YM term has two u's, Eq. 4.33, giving 2/3).
- Normalisations and the tree coefficient were not compared.
- This identifies the structure of the two forms, not the coefficients.
- 2601 labels its reduction "projection to C^0" of a fibre-resolved expression. That is the NAMCG fibre trace with equal weights (beta_X = 1), not the NAMCG "averaged-frame reading". The ledger's two terms should not be matched by name.

**Field position.** On this point NAMCG is **consistent with, and sharper than, the published programme**:
- 2601 attributes "1/3 vs 1/5" to "the geometric treatment in section 3 does not fully capture the hs sector".
- Its Newtonian derivation states "all hs contributions were ignored".
- Sec. 3.2 says hs components matter at quadratic order "even for transverse-traceless modes".
- The 045-047 eigenvalues are exact closed forms, helicity-resolved, with a proved sign.

Do not present 046/047 as a new obstruction to the published theory. It is a closed-form version of a stated feature.

## 3. Routes by gap

### R1. F/N (gaps 1 and 2): the helicity-two two-point function with the tree form. Rank 1.

- **Literature:**
  - 2601 Eq. 4.44: quadratic action = prefactor x (A_tran box (d_0^2 - (1/5) d_i^2 - m^2) A_tran + A_long box (d_0^2 - (3/5) d_i^2 - m^2) A_long), with m^2 = 32 pi G_N alpha^2 r^-4 (Eq. 4.45).
  - "The common factor box implies that the transversal and longitudinal gravitational waves remain massless."
  - Extra modes are tachyonic in the IR. They are stabilised only by estimated terms V_00 < 0 and V_01 > 0 (Eq. 4.46, A.4, A.5), and the paper calls the instability "expected to be an artifact", not shown.
  - 2609.08955 Sec. 7.3: graviton mass is forbidden because delta h = L_xi h under volume-preserving diffeomorphisms.
- **Sub-lemma:** on helicity +-2 at level one, write S_2 = q^2 (c.c)[t + (c_T^TT a + kappa b) x norm], with t the NAMCG tree coefficient. State the two poles (q^2 = 0 and the second factor), v^2, the effective mass, and both residue signs in terms of T_i, V_i and t.
- **Why now:** 047 records that eliminating inert amplitudes through the induced forms alone changed only helicity +-1 at three sampled cases. So this channel may close at this order, though the tree form must be rechecked.
- **Hypotheses:** the 047 class with M >> coth^2 tau; the helicity-two sector only; the tree form on the same amplitudes.
- **Concern for N (MY CHECK):**
  - Partial fractions of 1/[(k^2 - q_0^2)(q_0^2 - w^2)] give opposite residues on the two poles. That is the standard Ostrogradsky pattern in the variable A.
  - The extra pole sits at the crossover scale, far below L_UV, unlike the Stelle pole in appH Problem N. So it lies inside the range p < L_UV that Chapter 17 item N names.
  - Published "ghost-free" statements (1910.00839 Thm 6.6, 2502.02498) concern the classical YM spectrum. 2601 says the extra modes "arise only after quantization". In the parts I read it does not mention Ostrogradsky.
  - Whether the pole is physical or a perturbative artefact is exactly what N must decide.
- **Feasibility:** high. All inputs exist except a check of the tree form.
- **Value:** conditional sharpening that links F and N for the first time, and could become a bounded obstruction to N. Not a closure.
- **Emergence:** preserved. A and the frame are matrix objects; the metric stays composite.

### R2. F/C (gap 2): the Newtonian channel. Rank 2.

- **Literature:**
  - 1910.00839 Sec. 7: the 6 physical metric modes come from A^(-)[phi^(2)] (5) plus A^(ex,1) (1). This matches the NAMCG six symmetric-D polarisations in count.
  - A^(-)[phi^(2)] splits into a graviton phi^(2,0), a vector phi^(2,1) and a scalar phi^(2,2). The scalar mode A^(-)[D+D+ phi] "underlies the linearized Schwarzschild solution".
  - **Dictionary to test:** k = 0, 1, 2 in phi^(2,k) against helicity +-2, +-1, 0 about y_perp in 047.
  - 2601 Sec. 4.1: the trace mode "is captured by the dilaton". This bears on the 047 phi and on Problem C.
  - 2601 Eq. 3.25, 3.37: at r << 1/m the linearised static GR result holds, but from Eq. 3.1 with hs parts ignored.
- **MY CHECK:** a static source has q.y = 0, so x = 1 - theta = -1/s^2... more exactly x = -l^2/m^2 and 1/x = -s^2. Generally 1/x = -s^2 (1-u^2)/(1+s^2 u^2), with u = q_0/|k|.
  - So 1/x is not small here. It is the largest term at late times.
  - Helicity 0 (phi = 2/3): IX_2 = -4 + (2/5)s^2 + 8/(5 s^2) (checked at (5,3), value -0.9306) and SC_2 = (1/20)[22/3 - s^2/3 - 4/(3 s^2)].
  - At large s the helicity-0 coefficient is approximately -s^2 [(V_1 - T_1)/60 + T_2/20] < 0, opposite to c_T^TT > 0 and of size sinh^2 tau.
  - The helicity-two coefficient at u = 0 is negative too, and the zero sits at v^2 above. This is the same sign change as q_0^2 - (1/5) k^2 in the published form.
- **Sub-lemma:** compute the coefficient of the static source response. This needs (i) helicity 0 with the trace polarisation in transverse gauge, since the Newtonian h is not traceless on the 3-space orthogonal to q; (ii) the trace form in the fibre trace, not yet computed (045 has it only in the averaged-frame reading); (iii) the tree term; (iv) the first-term shift. Expected outcome: either a sign and size for the Newtonian coefficient as a function of tau, or a statement that a frozen plane wave cannot represent the static response.
- **Caveats:**
  - The sign flip may be an artefact of the frozen symbol, or of the equal-weight fibre trace. The scale condition is (mk)^2 between theta and M, so large m narrows the window.
  - Matter coupling is not derived in NAMCG. 2312.01317 Eq. 4.2 couples matter to G, and the mode that couples matters.
- **Why it matters:** the published Newton limit rests on the projected geometric reading that 2601 itself says omits hs parts. If the NAMCG sign survives, this is a tension with published text that must be stated, not a contradiction of a proved theorem.
- **Feasibility:** medium. **Value:** potentially the most consequential result in the class, in either direction. Also bears on Problem C through the dilaton.
- **Emergence:** preserved. Watch that "Newtonian limit" does not import a background metric beyond the composite G.

### R3. D1: switch-target candidate. Rank 3.

- **Literature:**
  - Hanada-Kawai-Kimura hep-th/0508211 (Prog. Theor. Phys. 114 (2006) 1295): matrices as covariant derivatives on functions on the principal Spin(d)-bundle; diffeomorphisms and local Lorentz, with hs analogues, sit inside the unitary symmetry; S = -tr[A,A]^2 yields the Einstein equation at the equation-of-motion level. Abstract only.
  - 2601 App. A.2-A.3: gauge transformations are volume-preserving hs-deformed diffeomorphisms; "local Lorentz invariance emerges in low-energy physics"; boost generators (A.22) with {M^(0i), M^(0j)} = -(3/2) M^(ij) (A.25).
  - 2312.01317: the frame "lacks local Lorentz invariance" because of the divergence constraint.
  - 2609.08955: local Lorentz holds for the classical tensorial sector, and a non-local sector "does actually break Lorentz invariance".
- **Reading:** the published IKKT line does not supply an SO(3,1) gauge symmetry. It supplies emergent Lorentz in a sector, with an explicit constraint against the gauge version. Chapter 17 D1 requires the gauge symmetry, with omega, A_mu, B and ghost operators.
- **Sub-lemma:** in the conjugate-coordinate class, do gauge parameters Lambda = lambda_i(y) n^i act on level-one frame amplitudes as local rotations of the fibre index? Find what fixes the failure, and whether a rescaling of the A.22 generators gives so(3,1) on the relevant modes (MY READING: -(3/2) alone is removable by rescaling, but the closure on a field-dependent domain is what counts).
- **Expected outcome:** a bounded result either way: a derived local action on a stated sector, or a no-go for a gauge SO(3,1) in the class, which the 2312.01317 constraint suggests. Note that a no-go would raise an author-level question about D1 versus a sectoral statement. I propose no label or scope change.
- **Risk:** **high for emergence if the HKK manifold is taken as a given**, since it presupposes a manifold and a bundle. Use it as an algebra of operators in the vacuum presentation only.
- **Feasibility:** medium. **Value:** either result would open a new critical-path problem. Nothing in the last several packages has touched D1.

### R4. B/F (gap 3): fibre-resolved cone or Noether entropy of the induced functional. Rank 4.

**Published contact and edge mechanisms do not supply the negative mixed gap (MY READING of verified sources):**
- **Sign:** Frolov-Fursaev hep-th/9806078: S^BH = S^SM - Q with Q > 0 from vector constituents only. Scalars and spinors contribute to S^SM, not Q. So contact terms give c_A(bulk) - c_T = +Q > 0. Solodukhin 1502.03758 (search snippet of full text, not in the abstract) says the same: contact terms contribute negatively to the Newton constant. Donnelly-Wall 1506.05792: one negative scalar on the surface. NAMCG's gap is negative.
- **Species:** merged L2387 says the vector index "is absent from the mixed term", so the mixed gap is Dirac. Published Dirac constituents have no such Q.
- **047's own Lichnerowicz result** already closes the Dirac fibre-constant cone: to that order "the cone of the mixed term is not an independent quantity". The gap on TT is -(7/30)(V_1 - T_1) - (7/20) T_2. It comes entirely from second-harmonic weights B_i, while "the cone carries only the weight D". So it is a fibre-resolution mismatch, not a contact term.
- **Dabholkar-Harris-Moitra 2601.13131** (JHEP not listed): edge contributions from Riemann-linear couplings for any spin >= 1, via Harish-Chandra characters; string tower UV finite; bosonic only, fermions and type II not analysed, and no relation to 1/G stated. Useful for the first term because it speaks the same character language as the SO(1,9) formula of 2411.02598. It does not address the mixed term.

**Mechanisms that do match the structure:**
- **Non-gauge-invariance of the geometric area:** Ammon-Castro-Iqbal 1306.4338 ("standard notions of geometry are no longer gauge invariant"; Wilson line replaces RT; AdS3 only). In hs-valued NAMCG forms the cone in the base at each fibre point may not be the covariant object.
- **Noether charge of the functional actually induced:** Frolov et al. show the coefficient comes out right when the entropy functional matches the induced action. The IX_2/SC_2 functional is not diffeomorphism-covariant at second harmonic, so Iyer-Wald does not apply as is. Its symmetry is the hs-deformed volume-preserving diffeomorphism (2601 A.11-A.15).

**Sub-lemma:** (a) compute the cone at second-harmonic order, with the replica lifted to the 6-dimensional leaf and fibre-dependent entangling data; (b) test whether the B_i weights appear. Expected: either T_2 and V_1 - T_1 appear (gap reduced or closed on TT), or a definite residue.

**Fixed-state alternative:** the first-term cone part has the right sign (c_A = +2 per K mode at order Lambda^2), but it is cutoff dependent, while c_T is finite at this content. Same-regulator equality there would need Lambda to be fixed by the model (2601: Lambda_NC or the highest KK scale). That is not a mechanism yet.

**Feasibility:** low-medium; (a) is hard. **Value:** the only listed route that bears directly on B's tensor block. **Emergence:** preserved if the replica is defined on the leaf with composite metric.

### R5. Gap 1 proper: the 1/x structure and the tower. Rank 5, cheap lemma only.

- **MY CHECK / reading:** 1/x comes from inverting the map from amplitude to h-bar (G_ij has eigenvalues a, a, b). The gatekeeper's "not polynomial at fixed h-bar" is compatible with this, but its attribution to level-one restriction needs testing. I suggest the variable change as the alternative explanation.
- **Cheap lemma:** express all five-polarisation forms polynomially in c at all helicities, then re-pose "one coefficient" in those variables.
- **No real pole from the denominator (MY CHECK):** a > 0 for all real q != 0 in the listed ranges of x, so it adds no real pole. It vanishes on the cone at fixed q.y != 0. So on-shell residues do not see it. Off-shell static response does (R2).
- **What the literature does:**
  - It keeps frame variables and does not integrate out a tower. 2609.08955 Sec. 8: the YM term "cannot be written as a local function of the frame".
  - Non-locality is carried by an anharmonicity tensor via a box-tilde inverse (2601 Eq. 3.15, 3.25).
  - 1910.00839: mode-space diagonalisation has rational K-denominators (k(2s-k), s^2+K), and K is H^3 kinetic energy. This may be related to a; the relation is not checked.
- **Limits on Schur:**
  - 2405.09804: colour su(k) hs modes get mass at the K scale, but the authors "could not create a large gap" (lowest-spin mass exceeds hs siblings), and hs fields "do not seem to decouple". Its Sec. 6 does not treat frame fluctuations.
  - 2609.08955 Sec. 7.3: hs modes "expected" to get large mass via Tr(AA), with sign and scale not stated there and no separate abelian-sector analysis in 2405.
  - So elimination is not a controlled small-parameter expansion on current evidence. A self-consistent hs mass could suppress beta_X, which would change the 046 regime, but no published calculation gives it for the NAMCG loop modes. I would not bet a package on it now.
- **Level data for the open normalisation:** 2303.08012 Eq. 7.5 3s; 2405.09804 Eq. 4.4 m_s^2 = 3(s+1)/R^2; 2502.02498 S^2 = 2s(s+1); NAMCG J(J+2). These label different operators in part. Not reconciled.
- **n and cutoff:** 2502.02498 Sec. 5.1 gives a local cutoff s <= m = x^0/r. This is relevant to the 046 "n -> infinity" statement, since n is effectively tied to m and thus to tau. Not previously used.

### R6. E: constraint only. Rank 6.

- Liao 2609.40183 (30 Sep 2026; single author, abstract only, no journal): for Lie-algebraic saddles of IKKT, signature is read from a bilinear form h; simple algebras force h = 0; every nondegenerate Lorentzian saddle in up to 11 dimensions has a nonzero solvable radical ("space can be semisimple; time must be solvable"). Its scope excludes non-Lie-algebraic backgrounds. Useful as a constraint on any E attempt in the Lie-algebraic class; it does not derive signature.
- 2609.08955: signature through an infinitesimal Wick rotation, so assumed. It also says whether a 3+1 saddle dominates "is not clear".
- Numerical line: 2604.19836 (complex Langevin, deformations, search snippet), 2205.04726 (mass term needed for a signature change, search snippet). No derivation found.
- **Feasibility:** low. Do not switch here.

### R7. A and G-derived: nothing better. Rank 7.

- **A:** a new targeted search for modular Hamiltonians of matrix states, target-space or gauge-invariant subregion algebras found general reviews only. 2609.08955 does not discuss entanglement in the part read. Unchanged from the previous scout.
- **G-derived:** a search found no infrared-entropy or boundary derivation from a matrix theory. Published direction is different: vacuum energy "does not act as cosmological constant" (2303.08012, 2110.03936 via search snippets) and 2312.01317 scales it as rho^-4. A future G-derived claim must address this. 2509.24753 gives a(t) ~ t at late times, not acceleration (snippet).
- **N independently:** depends on F, so reached through R1.

## 4. Should the programme switch target?

**Assessment: narrow no more, in this form.**
- The Chapter 17 F item requires A, B, C and the sign/scheme dependence of G_eff computed from specified operators. appH's F missing step asks for operators, ghosts, limits and scheme. "One coefficient on five traceless polarisations for all q" is, in 047's own words, "a criterion of this ledger". It came through B's tensor block, and it is not what the field claims.
- 045-047 closed the regime, isolated-data and scale escapes. Remaining escapes (avenues 2, 4-8 of review-r3) refine a class whose central statement now has a published structural counterpart. Further packages there have low expected value, except as needed by R1/R2.
- **For the author (advice, no label change):** decide whether B's tensor block should be judged on all five off-shell polarisations or on the on-shell sector plus Newtonian response. This needs a decision on what a matrix-derived Einstein equation means when the theory has extra non-Ricci-flat modes. Evidence that would be needed either way: R1 and R2 outcomes.
- **Suggested order:** R1 (one package), then R2. If R2 gives a robust sign flip, that is a major finding and should be read against 2601 before anything else. Then R3 to break out of the class.
- **Avoid:** torsion on J >= 1 loops, K with W_R = 0, equivariant K, unless R1 or R2 demands them.

## 5. Constraints and concerns for the researcher

- Do not cite 2601 as deriving a single G on polarisations. Its Eq. 3.1 single G_N is cited from 2411.02598, and I did not see polarisation-dependence computed for it. Its Sec. 4 form is velocity dependent.
- The velocity statements differ between my two readings: 2601 says extra modes travel at about c/3; 2609 gives c/sqrt 3 for box-tilde and c/3 for the extra modes; and the 1/5 factor gives c/sqrt 5. 2601 says this difference is unresolved. Check the source. 
- The 2601 analysis is self-described as not settled: "not yet predictive at the cosmic scale"; "more work is required to see whether this gravity theory is physically viable". Do not use it as an established result.
- Neither the dictionary in section 2 nor the sign in R2 is checked by anyone but me, by hand. Run them with exact rational arithmetic first.
- 047's statement about "that work" refers to 2411.02598. It stays true as scoped, but any new appH text should compare with 2601.08031. L2092 will be out of date once this is done.
- Weinberg-Witten was not re-checked this session.

## 6. Literature checked

Verified records (arXiv or ar5iv page fetched):
- [2601.08031](https://arxiv.org/abs/2601.08031) Steinacker, "Modified gravity at large scales on quantum spacetime in the IKKT model". JHEP 04 (2026) 044 per a [Springer link](https://link.springer.com/article/10.1007/JHEP04(2026)044) in search results; journal page not fetched. "Mirage matter" is in the abstract itself, which resolves the previous scout's caveat.
- [2609.08955](https://arxiv.org/abs/2609.08955) Steinacker, invitation review. Its reference list gives JHEP 02, 031 for 2411.02598, supporting that citation.
- [1910.00839](https://arxiv.org/abs/1910.00839) Steinacker, hs kinematics and no ghosts.
- [2405.09804](https://arxiv.org/abs/2405.09804) Steinacker-Tran (authors per 2609's reference list; the fetched page showed Tran only).
- [2502.02498](https://arxiv.org/abs/2502.02498) Manta-Steinacker.
- [2312.01317](https://arxiv.org/abs/2312.01317) Kumar-Steinacker.
- [2101.07297](https://arxiv.org/abs/2101.07297) Fredenhagen-Steinacker, JHEP 05 (2021) 183.
- [hep-th/0508211](https://arxiv.org/abs/hep-th/0508211) Hanada-Kawai-Kimura.
- [hep-th/9607104](https://arxiv.org/abs/hep-th/9607104) Frolov-Fursaev-Zelnikov, Nucl. Phys. B486 (1997) 339.
- [hep-th/9705207](https://arxiv.org/abs/hep-th/9705207) Frolov-Fursaev.
- [hep-th/9806078](https://ar5iv.arxiv.org/html/hep-th/9806078) Frolov-Fursaev.
- [1306.4338](https://arxiv.org/abs/1306.4338) Ammon-Castro-Iqbal (related DOI 10.1007/JHEP10(2013)110).
- [1502.03758](https://arxiv.org/abs/1502.03758) Solodukhin (related DOI 10.1103/PhysRevD.91.084028).
- [2601.13131](https://arxiv.org/abs/2601.13131) Dabholkar-Harris-Moitra.
- [2609.40183](https://arxiv.org/abs/2609.40183) Liao.

Search snippets only, **not independently verified**: [2303.08012](https://pdf.arxiv.org/pdf/2303.08012) and [2110.03936](https://web3.arxiv.org/pdf/2110.03936) vacuum-energy sentences; [2509.24753](https://arxiv.org/abs/2509.24753) a(t) ~ t; [2604.19836](https://arxiv.org/pdf/2604.19836); [2205.04726](https://arxiv.org/pdf/2205.04726); [hep-th/9703178](https://arxiv.org/abs/hep-th/9703178); the sign sentence of 1502.03758's body; [1506.05792](https://arxiv.org/abs/1506.05792) negative-scalar phrasing (also verified in the earlier scout).

Carried from the earlier scout, not re-fetched: 2411.02598 content, 2303.08012 Eq. 7.5 (as quoted in merged appH).

Searches that found nothing: mode-mixing or tower integration on covariant quantum spacetime as an explicit calculation; a same-regulator treatment across massive fields, KK tower and SUSY multiplets; matrix-state modular Hamiltonians; IR boundary entropy from a matrix theory; a derivation selecting Lorentzian signature dynamically.

## 7. Suggested next targets (one line each)

1. R1: closed helicity-two level-one two-point function with the tree form; compare v^2, m^2 and residue signs with 2601 Eq. 4.44-4.46.
2. R2: static response coefficient (helicity 0 + trace in the fibre trace) as a function of tau; settle the sign against c_T^TT.
3. R3: action of level-one gauge parameters on level-one frames; local rotation or bounded no-go for D1 in this class.
4. R4: second-harmonic cone on the leaf; do the weights B_i appear?
5. Author question: is the B tensor block to be tested on all five off-shell polarisations, or on the on-shell sector and Newtonian response? (Advice only.)

Files: `C:\Users\redgi\Projects\namcg-lab\proposals\047-lichnerowicz-torsion-closed-forms\appH_insert.tex`, `C:\Users\redgi\Projects\namcg-lab\proposals\047-lichnerowicz-torsion-closed-forms\review-r3.md`, `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex`, `C:\Users\redgi\Projects\namcg-lab\chapters\ch17-agenda.tex`
