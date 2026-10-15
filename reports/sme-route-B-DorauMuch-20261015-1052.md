SME-ROUTE: CONDITIONAL | PRIMARY: For the NAMCG Poisson-limit fluctuation operator on the emergent metric G, compute the replica-cone (entanglement) area coefficient and compare it with the induced Einstein-Hilbert coefficient of the same operator, i.e. a Susskind-Uglum / Sakharov entropy-action identity with the contact term Q made explicit | EMERGENCE-RISK: low

Requested by the author on 2026-10-15 ("research and derive breakthrough to problem B from" Dorau & Much, PRL 136, 091602). Saved verbatim from the independent SME agent (advisory, read-only).

# SME route map for Problem B (Dorau-Much and the Jacobson line)

Read-only advisory. No derivations or manuscript text are written here.

## 0. Bottom line

- **The paper gives no breakthrough for B.** It is a rigorous Araki-Uhlmann treatment of the matter side of Jacobson 1995. It takes as inputs the metric, the area-entropy proportionality (S = A/4, or just δA ∝ S_rel with α > 0 chosen), Raychaudhuri focusing and local conservation. B asks for exactly those inputs to be derived.
- **The literature it builds on does give a sharp reduction.** Jacobson's stationarity postulate (the MVEH, maximal vacuum entanglement hypothesis) is not a consequence of relative-entropy kinematics. It is equivalent, at linear order, to the field equation for the emergent metric. For NAMCG that equation is the induced-action operator identity of Problems F, C and D1.
- **B therefore cannot be closed entropically.** The derivable pieces are:
  - (i) the area coefficient, via the entropy-action identity;
  - (ii) the equivalence "EE for the tensor block ⇔ tensor quadratic operator = linearized Einstein operator with the same G_eff as the area coefficient";
  - (iii) consistency and positivity checks.
- **Best available target.** The entropy-action identity, including the contact term. It is a conditional sharpening. It could also produce a reproducible obstruction, which would be a consequential correction.

## 1. What I read and verified

Reading mode: digest and targeted reads, not a full scan. The manuscript reads were:
- appH sec:status-B in full, and appH lines 130-310 (replica insertion identity, Problem C);
- ch06 in full;
- appB lines 86-195;
- ch08 ass:emergent-op and its remark;
- appG (file `appG-sector-entropy.tex`);
- ch17 lines 118-160 and 640-735;
- the ledger tail;
- the opening of proposals/014-level1-dynamics/proposal-r2.md;
- the "Remaining open step" of proposal 012;
- my earlier report.

Sources actually read:
- **Dorau-Much, arXiv:2510.24491v3.** All 6 pages as images, including eqs. 1-28, footnotes 39, 47 and 40, and the reference list. Not checked against the PRL text.
- **Jacobson, arXiv:1505.04753 (PRL 116, 201101).** Pages 1-5 as images, covering eqs. 1-27 and the discussion. Not read: the appendices.
- **Casini-Galante-Myers, arXiv:1601.00528 (JHEP).** Pages 1-6 as images, covering the introduction and summary, eqs. 1.1-1.8.
- **Solodukhin, Living Rev. Rel. 14, 8 (arXiv:1104.3712).** pp. 69-71 as images (sec. 8.1-8.3, eqs. 318-325).

Abstract-level only (title and abstract fetched, full text not read):
- Speranza 1602.01380.
- Jafferis-Lewkowycz-Maldacena-Suh 1512.06431.
- Jacobson gr-qc/9404039 (an essay).
- Susskind-Uglum hep-th/9401070.
- Frolov-Fursaev-Zelnikov hep-th/9607104.
- Jacobson-Visser 2212.10607.
- Bousso et al. 1506.02669.
- Hollands-Longo 2503.04651.
- Faulkner et al. 1605.08072.
- Lashkari-Van Raamsdonk 1508.00897.
- Casini 0804.2182.
- Engelhardt-Wall 1408.3203.
- Karczmarek-Sabella-Garnier 1310.8345.
- Matrix QM entanglement review 2512.03163.

Not independently verified:
- Any specific claim I make about the content of these works beyond their abstracts.
- Kabat's contact-term paper, which I cite only as a pointer, not as read or checked. I did not fetch it.
- Longo 2019 and Casini-Grillo-Pontello 2019. I know them only as D-M references.

## 2. Problem B's exact missing step in NAMCG terms

Write S_D[Φ] for the replica entropy of the diamond D(G[Φ], ℓ) built from the emergent metric. Then ass:EE, eq:first-law-zero and Proposition ward (prop:ward) say that, for every allowed fixed-volume δΦ in the tensor block, the sum of two terms vanishes: the modular-energy term 2π/κ ∫ξ δ⟨T^op⟩ and the area term δA/4G_eff.

The decomposition follows Jacobson, with the same split as CGM eq. 1.1-1.2: δS_tot = δS_UV + δS_IR, with δS_UV = η δA (geometry) and δS_IR = δ⟨K⟩ (first law, a state variation). Three separate things are missing.

- **B1 (stationarity).** A derivation that the sum vanishes for off-shell compactly supported tensor variations. Since T^op[h] is the metric variation of the block's quadratic action, this is an operator identity: K_T[h] = −(1/8πG)·E[h] with m_T = 0 (K_T the tensor-block quadratic operator, E the linearized Einstein operator). It must hold for h in the tensor block and not only on shell.
- **B2 (area coefficient).** That the coefficient η multiplying δA|_V is the same number as 1/(16πG_eff) in the induced Einstein-Hilbert term of the same operator. At present eq:first-law only "names" 1/(4G_eff), and ch06 defers the identification to ch08 and Problem F.
- **B3 (map).** The scaffold-to-emergent map (ass:emergent-op), so that the replica cone and the volume constraint are formulated on G and not on g⁽⁰⁾.

The geometric part δA|_V = −(Ω ℓ^d/(d²−1))(G_00 + λ g_00) (Jacobson eq. 22) is plain differential geometry on the emergent metric once G is defined. It is not a missing step.

## 3. Mechanisms, what each would derive, and whether NAMCG has the objects

### 3.1 Jacobson-2016 equilibrium with a UV area term

- **Structure.** Jacobson assumes "the area density of vacuum entanglement entropy η is finite and universal." The MVEH is a postulate: total entropy at fixed volume is stationary for first-order variations from a maximally symmetric vacuum. For conformal matter it is equivalent to the Einstein equation, which is a theorem in the metric-given setting. For non-conformal matter it needs the conjecture δ⟨K⟩ = c(δ⟨T_00⟩ + δX) of eq. 21.
- **That conjecture is itself in trouble.** CGM and Speranza (abstract-level) find an extra R^{2Δ}δ⟨O⟩² term for relevant operators with Δ < d/2. For NAMCG's non-conformal tensor block this is a standing risk. Per CGM's abstract, ways around it exist.
- **Needs from NAMCG.**
  - A finite, universal η. A matrix regularization naturally supplies a finite cutoff, but see the caution in 3.5.
  - An off-shell form of δ⟨K⟩. This needs the BW-type formula H_D = (2π/κ)∫ξT + H_area, which is Problem A territory (appB says no BW theorem is claimed for the matrix potential).
- **What it derives.** With these inputs it gives Einstein ⇔ stationarity. It cannot give stationarity from nothing.
- **Emergence.** Preserved provided the volume and area are those of G.
- **Feasibility.** Reduction: high. Closure of B: not available.

### 3.2 Entropy-action (Sakharov / Susskind-Uglum) identity

- **Content.** For minimally coupled constituents, the cone entanglement entropy equals the Bekenstein-Hawking entropy written with the induced G. Solodukhin 1104.3712 eqs. 318-320 give, for N_0 scalars and N_1/2 Dirac fields (N = N_0 + 2N_1/2), 1/G_ind = N/(12πε²) and S_ent = N A/(48πε²) = A/(4G_ind).
- **Non-minimal fields break it.** The same review (eqs. 322-323) gives S_BH = S_ent − Q with Q = 2π Σ ξ_s ∫_Σ ⟨φ_s²⟩. Q is UV divergent. Solodukhin's abstract also lists the problem for gauge fields. Kabat's contact-term paper is a pointer only, not verified.
- **Why this is the real area-term mechanism for NAMCG.** The area coefficient comes from the heat kernel of the operator, with no S = A/4 input. This is where NAMCG is ahead of D-M: D-M's α is free until S = A/4 is imposed, whereas NAMCG, if the identity holds, determines α from the operator (G_ind) instead of assuming it.
- **Needs from NAMCG.**
  - The scalar, connection and ghost operators already specified in the 005 paragraph. It records the identity √|G|(R_G/6 − E) = ρR[g_ρ]/6, the connection-sector trace (4/6)ρR + ρ²X and ghosts −2/6 ρR.
  - A definition of the replica geometry on G that is consistent with ass:emergent-op.
  - A common regulator for the entropy and the effective action, since the equality holds for a common proper-time cutoff.
- **Subtlety specific to NAMCG (my observation, not verified).** The scalar-sector endomorphism E carries a curvature of a second metric g_ρ ≠ G. Whether the replica makes only G conical or also g_ρ (equivalently, also ρ) decides whether a Q-type contact term arises. This links to Problem A, because it asks which object is replicated.
- **Emergence.** Preserved if the cone is on G. It would be at risk if the cone were silently built on g⁽⁰⁾ or on η.
- **Feasibility.** Medium-high for the scalar sector, medium for connection and ghosts. A conditional sharpening, not a breakthrough.

### 3.3 Converse direction (Einstein ⇒ stationarity), as noted by D-M

- **What it would derive.** If the effective action of G contains (1/16πG)∫√G R with G equal to the area coefficient, then EE follows at linear order. It is a theorem in Jacobson's metric-given setting (conformal matter, first order).
- **Needs.** The Einstein-type field equation for the emergent metric, which NAMCG lacks. 008 and 009 show that E[h] = T fails for generic conserved T without an extra derived conserved stress. 013 shows the rank obstruction is lifted in the CP^{1,2} class. 014 shows that the tree-level equations there give an algebraic degree-0 response in h, not an Einstein-type one. The Einstein structure appears only from an induced term which is an input in that package.
- **Consequence.** Used as a derivation of B it is circular, since Theorem mT uses EE to get m_T = 0. Used after F, it is a consistency check.
- **Feasibility.** Not now. Useful as a test once F is derived.

### 3.4 First law plus second-order positivity (Fisher information / canonical energy)

- **Facts.** The first variation of S_rel at the reference state vanishes identically. The content is at second order: the Fisher information is positive. Lashkari-Van Raamsdonk (abstract-level) show this equals canonical energy for holographic CFT balls. Hollands-Longo (abstract-level) give a shape-derivative formula for relative entropy that yields the QNEC.
- **What it could give NAMCG.** A positivity or sign test on the quadratic form of the tensor and level-1 amplitudes. 014 leaves the overall sign of the level-1 Maxwell-type kernel unfixed ("opposite to −1/4 F² in η", weight convention not fixed by eq:Smatrix). A relative-entropy positivity condition on the vacuum restricted to a diamond could constrain that sign.
- **Needs.** A state on the diamond algebra as a function of Θ. In a finite-dimensional compression algebra the abstract algebra is the same for all Θ. This is an observation for the researcher to check, not a result: the same rank means the same algebra. The identification of the subspace P_D across Θ is the Problem A map.
- **What it derives.** Inequalities, not stationarity. Closest to Problem N. It is a conditional sharpening only.
- **Feasibility.** Medium-low, speculative.

### 3.5 Target-space entanglement of the matrix diamond (risk check on η)

- **Caution on the area-law premise.** Karczmarek-Sabella-Garnier (abstract-level, 1310.8345) find that on the fuzzy sphere the entropy is not proportional to the boundary length. For regions covering a small fixed fraction of the sphere it is extensive. This conflicts with a naive area-law premise for a matrix-regularized region. The 2025 review 2512.03163 states the area-law conditions at large N for noncommutative geometries. I read only its abstract, so which conditions hold for NAMCG is not verified.
- **Consequence.** The "η finite and universal" assumption is not automatic in the matrix setting. A matrix model can have a finite cutoff and still fail the area law. NAMCG should not assume this.
- **Feasibility.** High difficulty (needs Problem A). I include it as a risk flag to be recorded, not as the next package.

### 3.6 Entanglement-wedge, JLMS and modular-flow arguments

- **Content.** JLMS (abstract-level): relative entropy equals bulk relative entropy at leading order in the bulk coupling. The area-operator form K = Â/4G + K_bulk is, as I recall it, from the JLMS body and is not verified here. Faulkner et al. 1605.08072 give first-order shape terms in modular Hamiltonians. Engelhardt-Wall (abstract-level) give extremality of generalized entropy under surface variations.
- **What NAMCG would need.** A holographic or bulk dual and an area operator. Neither exists. The area operator is exactly what NAMCG lacks, so using JLMS would import it.
- **Verdict.** Unlikely as a route. Useful only as a structural template: the full modular Hamiltonian needs an area operator, which is what H_area in eq:HD-boost names.

### 3.7 Jacobson-Visser fixed-volume partition function (abstract-level)

- It derives A/4G from a gravitational saddle with a volume constraint, using the Einstein-Hilbert action. That is a dynamical-metric framework with the EH term given. Unlikely for NAMCG at this stage.

## 4. The researcher's objection

**Is it right?** Narrowly, yes. The relative entropy of a family of states on a fixed finite-dimensional algebra, S(ρ‖σ) = Δ⟨K⟩ − ΔS, has vanishing first variation at σ. That is the first law restated. It carries neither the area term nor stationarity. I agree with the recommendation not to rewrite ass:EE and with the remark proposed for the ledger section.

**Where I would sharpen it.** The objection gives the wrong diagnosis of the gap, because the same limitation applies in every Jacobson-type argument.

1. Stationarity is not a property of S_rel in Jacobson or in D-M. In Jacobson it is a postulate, the MVEH. In D-M it is replaced by the proportionality δA = (α/2π)S_rel (eq. 20), whose coefficient is then identified through S = A/4. Neither derives it. A relative-entropy form of ass:EE neither weakens nor strengthens B.
2. Physical variations do not leave S_D stationary by themselves. For a source-created excitation, δS_D = tr(δρ K) ≠ 0 in general. Stationarity of the total (UV + IR) holds only if the geometry responds as the Einstein equation says. So EE for physical variations is the field equation, not an identity. This is the reduction in section 0. It also explains why the researcher's replica-insertion identity (appH, paragraph "Replica insertion identity") reduces, for a pure integration-variable shift, to a trivially satisfied condition.
3. Where does the area term have to come from? In Jacobson 2016 it is the UV input η δA, with the coefficient fixed afterwards by the requirement that G = 1/(4ħη) (eq. 27). It cannot come from relative entropy on a fixed algebra, because it is a variation of the algebra (the diamond itself changes with the metric), as the existing paragraph "Which first law is established" already says.
4. Can the matrix diamond supply it? Possibly, through a finite cutoff and the heat-kernel/cone coefficient of the same operator (route 3.2). But 3.5 shows that finiteness and an area law are not guaranteed in a matrix regularization.

## 5. Ranking

| Rank | Route | What it yields | Verdict |
|---|---|---|---|
| 1 | 3.2 entropy-action identity with contact term | B2 (area coefficient), conditional; or an obstruction | Conditional sharpening, feasible, primary |
| 2 | Reduction: EE for the tensor block ⇔ K_T = −E/(8πG) with the same G | Shows B is F's operator identity and not an independent entropic fact | Record as a lemma or remark inside rank 1 |
| 3 | 3.5 target-space area-law test | Risk check on η | High difficulty (Problem A); record as a risk |
| 4 | 3.4 positivity (Fisher information) | Sign constraints (links to N and to 014's sign) | Speculative |
| 5 | 3.3 converse direction | Consistency check after F | Not available now |
| 6 | 3.1 full Jacobson equilibrium as a derivation | Nothing beyond 1-2 until F | Reduces to F |
| 7 | 3.6, 3.7 | Need a holographic or EH input | Unlikely |

## 6. Primary target for proposal 015

**Statement.** Take the 005 operator content: scalar, connection and ghost sectors, Poisson limit, bosonic 4D content, background gauge, diagonal heat kernel with a local cutoff, ass:emergent-op. Compute the n → 1 cone entropy coefficient for these operators on the emergent metric G, with a common proper-time regulator for both quantities. Compare it with the coefficient of ∫√G R in the same operators' induced action. Make the Q-type contact term explicit sector by sector.

**Hypotheses.**
- The cone is built on G. State explicitly whether ρ and g_ρ are continued consistently with it. This is the scaffold-versus-emergent choice, and it should be reported as a choice with both outcomes if it matters.
- Only the fields of the 005 content are replicated.
- No S = A/4 and no external G.

**Expected form of the result.** For the scalar sector, a difference
Δ_sector = 1/(4G_S) − 1/(4G_ind)
that vanishes for minimally coupled content and is proportional to the E-weighted ⟨φ²⟩ horizon term (Q = 2πΣξ∫⟨φ²⟩ in the Solodukhin form) otherwise. Quote the contact-term structure for the connection sector too, flagged as not verified, since gauge fields need care.

**Outcomes and their value.**
- Match: the area coefficient in eq:first-law is G_eff of the same operator. This resolves B2 at conditional scope and means D-M's free α is fixed by the operator. It does not close B.
- Mismatch: ass:EE with a single G_eff, as written in eq:first-law-zero and prop:ward, is inconsistent with the heat-kernel G_eff of the same operator. That is a reproducible obstruction and a correction to ch06 and appG, which currently call the cone result "standard".

**Feasibility.** Medium-high for the scalar sector. This is not a breakthrough for B. It is the exact reduction, with a likely new caveat.

**Secondary, if the researcher has room.**
1. State the reduction lemma (B ⇔ operator identity K_T = −E/8πG with the same G) and add the cross-check against 014: in H_dyn the tree-level tensor-sector response is degree 0 in h and cannot equal a degree-2 Einstein operator. So EE fails at tree level in that class unless an induced term supplies it.
2. Check whether 014's "cancellation of the tree-level coefficient needs a loop term ΣF_i²" is related to 005's net TT Maxwell-kernel coefficient 1 − N_tot/24. This is a low-confidence pointer only.

## 7. What this does not do

- It does not close B or touch labels.
- Success on the primary target would not satisfy ch17's B criterion, which requires EE no longer assumed, non-conformal tensor-block variations, and no use of ass:dictionary.
- The finite-dimensional-algebra point (same abstract algebra for all Θ) and the "fixed volume as fixed rank / Liouville volume" idea are my observations for the researcher to check, not derived results.
- A possible re-scoping of how m_T = 0 is obtained, for example from the exact gauge invariance established in 014 item 1, is a question for the author and is outside this route map. I have not assessed it.

Files read: /c/Users/redgi/Projects/namcg-lab/chapters/appH-microscopic-proofs.tex, ch06-entanglement-equilibrium.tex, appB-modular.tex, ch08-heat-kernel.tex, appG-sector-entropy.tex, ch17-agenda.tex, reports/ledger.md, reports/sme-lit-DorauMuch2026-20261015.md, proposals/012-dorau-much-positioning/proposal-r2.md, proposals/014-level1-dynamics/proposal-r2.md (opening).
