SME-SCOUT: 9 routes | TOP: A/B-gluing:graded-trace (Tr rho^n) derivation of the fermion replica twist, Casini-Huerta + Fursaev-Miele; B-next-order:Manta-Steinacker-Tran SO(1,9) character supertrace as organiser (alpha^0, alpha^2 cancellation, then alpha^4); F:Troost self-dual / flux-inequality locus for the Nielsen-Olesen sector | EMERGENCE-RISK: low

(Saved verbatim by the orchestrator; the SME agent is read-only. Advice only: no derivations and no manuscript text.)

# SME scout: replica gluing for fermions, and next-order (log / a_2) comparison in the D=10 content

**Reading mode.**
- Digest + targeted reads of the repository: `reports/ledger.md` (015–017 entries), `proposals/017-GT-GA-gap/review-r2.md`, `proposals/018-induced-coefficient-cp12/review-r2.md`, and the earlier `reports/sme-scout-gap-GT-GA-20261015.md`.
- I did not read the chapters or the proposals' derivations.
- Every paper below was opened by live fetch. For each I record what I read: abstract only, or full text via ar5iv/arXiv HTML with section or equation numbers.
- "Not independently verified" marks everything else.

---

## 0. Bottom line in six points

1. **The fermion gluing is not a free choice.** The literature fixes it as follows.
   - Casini–Huerta (arXiv:0905.2562, full text read to ~100k characters):
     - On the n-sheeted surface the field on the upper side of the n-th cut equals (−1)^{n+1} times the field on the lower side. One minus sign comes from each copy of the density matrix, plus one for the trace.
     - These are Cartesian-component Grassmann fields.
     - Diagonalising the replica matrix gives twist phases e^{i2πk/n}, with k running over −(n−1)/2…(n−1)/2 (eqs. 16–19).
     - The entropy is then S = 2∫₁^∞ dλ log Z[λ]/(λ−1)² (eq. 28).
     - Footnote 2: for the Rindler wedge ρ ∝ e^{−2πK}, and ρⁿ corresponds to a rotation by 2πn, "which the paper uses to explain the origin of the fermionic signs".
   - Fursaev–Miele (arXiv:hep-th/9605153, ar5iv full text):
     - In polar tetrads the spin-1/2 field is antiperiodic (eq. 4.4).
     - Removing the spin connection by ψ = e^{−(i/2)σ₃τ}ψ′ gives twist phases e^{iδ±} = −e^{±iβ/2} (eqs. 4.6, 4.11).
     - The conical term is Tr K = (β/2π) Tr K_{R²} − (β/24π)((2π/β)² − 1) (eq. 4.12).
     - The coefficient is A₁^{(1/2)}|_{C_β} = −(β/6)((2π/β)² − 1), minus the scalar conical term (eq. 4.13).
   - This is the 017 "antiperiodic, spinor-transported" prescription.
2. **Reading of 017's "periodic" branch (my inference, not stated by any source).** The standard thermal reading is that periodic fermions compute a graded trace Tr[(−1)^F ρⁿ], not Tr ρⁿ. Casini–Huerta tie the sign to the thermal antiperiodicity. For a graded trace the boson/fermion cancellation "0 = 0 at n_D = 2" is a Witten-index-type supertrace cancellation. It would not be a statement about entanglement entropy. This should be tested, not assumed.
3. **SUSY does not select the gluing for entanglement entropy.**
   - Nishioka–Yaakov (arXiv:1306.2958) add an R-symmetry gauge field A = ((q−1)/2)dτ (eq. 2.15). They say the ordinary replica construction "is not a supersymmetric observable".
   - They show S_q^susy → S = −F as q → 1 (eq. 4.1), with first correction (π²/16) τ_rr (q−1) (eq. 4.7).
   - The R-holonomy μ = q−1 therefore drops out of entanglement entropy at first order. It matters for Rényi entropies, not for G_A.
4. **IKKT does produce an Einstein–Hilbert term with definite positive sign, but not from a Λ² coefficient.**
   - Steinacker (arXiv:2303.08012): maximal SUSY cancels the leading terms, and the first non-vanishing term is n = 4 in the flux expansion. The EH term comes from a mixed 4D–K term. 1/G_N = (2c_K²/π³) ρ⁻² m_K² with c_K² = (π²/8) Σ C_Λ²/μ_Λ² > 0 (eqs. 6.30–6.32, 7.23–7.24).
   - He argues that a heat-kernel UV cutoff is not appropriate there, because non-local string modes dominate.
   - Manta–Steinacker–Tran (arXiv:2411.02598) confirm 1/G_N > 0 in (3.49).
   - Consequence: at the D=10 content c_T = 0 is consistent with the literature (the Λ² analogue cancels). Any G_eff in the matrix-derived sense then lives at the next order. That order is finite and cutoff-insensitive in Steinacker's treatment, whereas a replica area coefficient is cutoff-sensitive.
5. **The Nielsen–Olesen sector is a bosonic spectral fact.**
   - Troost (arXiv:hep-th/9909187, ar5iv, §§7–10):
     - Gauge-field levels are λ = 2π(Σ(2m_i+1)f_i ± 2f_k) (eq. 35).
     - There are no tachyons iff f₁ ≤ f₂+…+f_n (§9).
     - On T⁴ this forces f₁ = f₂ (self-dual), which coincides with preserved SUSY.
     - Fermion levels are ±2πf₁ ± … ± 2πf_n (eq. 43).
   - These match 018's lowest vector eigenvalue −|f₁−f₂|.
   - My inference: the squared Dirac spectrum is non-negative, so the fermion heat trace is bounded. It cannot cancel an e^{+s|f₁−f₂|} blow-up of the vector trace. Adding fermions alone therefore does not cure the Euclidean divergence. The cures that the literature supports are self-duality (f₁ = f₂), additional flux components (Troost's inequality), or a different organisation of the one-loop integral (Steinacker's Lorentzian character expansion).
6. **A real constraint for the "tensor block" avenue.** Fursaev–Miele show spin-2 (Sec. 3.2, eqs. 3.38–3.39) and spin-3/2 (Sec. 4.2, eq. 4.33) conical traces differ from the smooth values as β → 2π. The cause is broken local translational isometries. Spin 0, 1/2 and 1 do not show this. Treating the metric-fluctuation block as a scalar-like internal-index vector (as 015/017 do) is therefore an assumption to be justified, not a given.

---

## 1. Verification record

| Source | Opened | What I read |
|---|---|---|
| Fursaev–Miele, hep-th/9605153 (NPB 484, 1997) | ar5iv | Sec. 4.1 (eqs. 4.4–4.13), Sec. 3.2 and 4.2 non-analytic surface terms |
| Casini–Huerta, 0905.2562 (J. Phys. A 42, 504007) | ar5iv, first ~100k chars | Sec. 2.1 fermion BCs, eqs. 11–19, 27–28, 70–78, 86–88, footnote 2 |
| Nishioka–Yaakov, 1306.2958 | ar5iv, first ~100k chars | Sec. 2 background, eqs. 1.8, 2.15, 3.70, 4.1, 4.7 |
| Nishioka–Yaakov, 1612.02894 | abstract | defect-operator reading in d = 3, 4, 5 |
| Huang–Zhou, 1408.3393 (JHEP 02 (2015) 068) | ar5iv, first ~100k chars | eqs. 26, 62–64, 68, 74, 77, 80, 85, 114–117 |
| Crossley–Dyer–Sonner, 1409.0542 | search summary and abstract | localisation on the ellipsoid, N = 4 SYM |
| Nian–Zhou, 1511.00313 | abstract | free (2,0) multiplet; a Killing spinor equation on the branched sphere appears in the text (seen only via search summary) |
| Klebanov–Pufu–Sachdev–Safdi, 1111.6290 | abstract | free-field Rényi on S¹×H^d agrees with branched coverings in d = 2, zeta regularisation |
| Dowker, 1510.08378 | abstract | charged-Rényi twist weights for Dirac fields vary with chemical potential |
| Lokhande–Mukhi, 1504.01921 | abstract | 2D fermion spin-structure sums are modular covariant, not invariant |
| Kabat, hep-th/9503016 | abstract | spin 0 and 1/2: BH entropy = entanglement entropy; spin 1: contact term |
| Larsen–Wilczek, hep-th/9506066 | abstract | conical entropy depends on curvature couplings even in flat space; fermion and gauge determinants related to non-minimal scalars |
| Solodukhin, Living Rev. 1104.3712 | ar5iv, ~200k chars | eq. 136: a₁^{(1/2)} = −(𝒟_{1/2}/6)∫R; eqs. 137, 141, 148: coefficients 𝒟_{1/2}/6, (1/6−ξ), 𝒟₁/6−1. The a, c log formula was NOT in the text I read. |
| Solodukhin, 0802.3117 | abstract | log term: type A anomaly fixes the topological part, type B the extrinsic part |
| Fursaev–Patrushev–Solodukhin, 1306.4000 | abstract | squashed cones; extrinsic-curvature surface terms |
| Fursaev, 1201.1702 (JHEP 05 (2012) 080) | abstract | divergent Rényi part of weakly coupled N = 4 SYM |
| Hung–Myers–Smolkin, 1407.6429 | abstract | twist-operator dimension expanded around n = 1; first terms universal, fixed by ⟨TT⟩; checked on free fields |
| Bianchi–Meineri–Myers–Smolkin, 1511.06713 | abstract | Rényi entropy and conformal defects; displacement operator |
| Lee–McGough–Safdi, 1403.1580 | abstract | 4D Rényi structure; numerics for free scalar and fermion |
| La Piana–Morsella, 2405.07888 (CMP 406 (2025)) | abstract | modular Hamiltonian of Weyl, Dirac, Majorana fields on the unit double cone |
| Bisognano–Wichmann 1976 | Crossref only (DOI 10.1063/1.522898, "On the duality condition for quantum fields", J. Math. Phys. 17, 303) | title and DOI verified; spinor content NOT independently verified |
| Steinacker, 2303.08012 (JHEP 05 (2023) 129) | ar5iv, ~whole text in three chunks | eqs. 2.13–2.14, 3.5–3.7, 4.16–4.21, 6.17–6.32, 7.12–7.24 |
| Steinacker, 2110.03936 (PLB 827 (2022) 136946) | abstract | |
| Manta–Steinacker–Tran, 2411.02598 | arXiv HTML, first ~100k chars | eqs. 3.7, 3.11, 3.13, 3.16, 3.33, 3.35, 3.49 |
| Battista–Steinacker, 2310.11126 | abstract | v2 corrects a sign error in eq. (79), which changed their conclusions |
| Kumar–Steinacker, 2312.01317; Steinacker, 2601.08031 | abstracts | |
| Steinacker, 1910.00839 (no ghosts); Sperling–Steinacker, 1901.03522 | abstracts | |
| Steinacker–Tran, 2305.19351; Manta–Steinacker, 2509.24753 | abstracts | |
| Steinacker, 1510.05779 | abstract | |
| Troost, hep-th/9909187 | ar5iv | §§7–10 as quoted above |
| Berenstein–Trancanelli, 1011.2749 | abstract | tachyons on fuzzy spheres resemble Nielsen–Olesen instabilities |
| Sugiyama–Yoshida, hep-th/0207190 | abstract | BMN supersymmetric fuzzy sphere is quantum stable; non-SUSY one is unstable |
| Karczmarek–Sabella-Garnier, 1310.8345 | abstract | scalar on the fuzzy sphere |
| Okuno–Suzuki–Tsuchiya, 1512.06484 | abstract | replica method in a matrix model, scalar on the fuzzy sphere |
| Suzuki–Tsuchiya, 1611.06336 | abstract | free-field entropy ∝ (boundary area)², volume-law crossover when interacting |
| Nair, 2207.04776 | abstract | fuzzy space defined by a state in a fermionic theory; region defined by integrating fields |
| Fliss–Frenkel–Hartnoll–Soni, 2408.05274; Fliss–Frenkel review, 2512.03163 | abstracts | matrix-QM entanglement, edge modes, minimal-area formula |

**Not independently verified:**
- Nielsen–Olesen (1978) and Leutwyler (1981) originals.
- The claim a = c for N = 4 SYM. Henningson–Skenderis hep-th/9806087 abstract says only that the anomaly "agrees with N = 4 SYM".
- The spinor content of Bisognano–Wichmann 1976.
- The statement that the imaginary part of the effective potential is untouched by fermions.
- Larsen–Wilczek's full proportionality theorem beyond the abstract.
- Statements about arXiv numbers I did not open (e.g. Dong's shape-dependence paper, excluded).

I found no paper treating modular flow or the replica gluing of fermions in IKKT/BFSS or on a noncommutative/fuzzy space. Fermionic entanglement on fuzzy geometries exists only in Nair 2207.04776 (a state-based definition). Everything on matrix-model entanglement I opened concerns scalars or bosonic matrix QM.

---

## 2. Route map (a): replica-gluing sub-lemma from the matrix modular flow

### R-a1 (TOP): derive the fermion twist from a graded trace, Tr ρⁿ
- **Sub-lemma.** For a quasi-free (Gaussian) state on the Z₂-graded algebra of the Poisson-limit fermions on the diamond, Tr ρⁿ has twisted sectors with e^{i2πk/n}, k = −(n−1)/2,…,(n−1)/2. The sign (−1)^{n+1} is a consequence of the graded trace, not an input. The polar-frame statement is then antiperiodic at every n.
- **Key references and equations.**
  - Casini–Huerta eqs. (11)–(12), (16)–(19), (27)–(28), (86)–(88), and footnote 2.
  - Fursaev–Miele eqs. (4.4), (4.6), (4.11)–(4.13).
- **NAMCG objects.**
  - The matrix modular operator (Problem A).
  - The Poisson-limit spinor operator with the coframe spin connection.
  - The 017 pulled-back replica (I).
- **Expected form of result.**
  - The gluing is fixed, and the "unrotated periodic" branch is identified as a different object: Tr[(−1)^F ρⁿ]. It is not the entanglement entropy.
  - The antiperiodic gap 4 − n_D then stands, with 2 at n_D = 2. My reading: this would confirm that the D=10 mismatch c_A = 2 against c_T = 0 persists at Λ² order.
  - That is a negative, sharpening result for B. The remaining escape is a contact term, see R-c1.
- **Constraint.**
  - The k-sum continuation in n (via λ = e^{i2πa}) is the only standard way to reach n → 1.
  - Caveat from 017: the "unrotated pulled-back" frame is a Cartesian-type frame. In Cartesian components the Casini–Huerta sign is (−1)^{n+1}, which is periodic only for odd n. Whether "periodic for all n" is a legitimate continuation, I have not established. The reconciliation of the Cartesian-frame sign with the polar-frame antiperiodic statement is my inference from the verified sources and should be checked.
- **Emergence.** Preserved. The twist is frame-intrinsic.
- **Feasibility.** High for quasi-free states. Medium once interactions or Moyal terms enter.
- **Status of success.** Conditional sharpening that removes a hypothesis (the 017 gluing ambiguity). A genuine result only together with the Problem A state.

### R-a2: boost/modular template for fermions
- **Sub-lemma.** Use the flat-space fermionic modular group as a test case. Check that the Poisson-limit modular operator reduces to a boost acting on spinors, and that the imaginary-time (2π) continuation produces the (−1)^F sign.
- **References.**
  - Bisognano–Wichmann 1976 (J. Math. Phys. 17, 303; spinor content not independently verified).
  - La Piana–Morsella 2405.07888 for the one-particle modular group of Dirac/Majorana/Weyl on the double cone. The abstract also gives a relative entropy to one-particle states.
  - Casini–Huerta footnote 2.
- **NAMCG objects.** The Problem A modular Hamiltonian, the effective metric G built from Θ, the diamond algebra.
- **Emergence caution.** The flat-space theorems assume Minkowski signature and a prescribed metric. The wedge must be defined with the emergent G, not a background η.
- **Feasibility.** Medium. Success is a consistency check, not a closure.

### R-a3: SUSY holonomy as a consistency constraint
- **Sub-lemma.** Show that any matrix-derived gluing reduces, at n → 1, to the Nishioka–Yaakov statement S^susy → S. The R-holonomy cannot change the first-derivative coefficient.
- **References and equations.**
  - Nishioka–Yaakov eqs. (1.8), (2.15), (4.1), (4.7).
  - Huang–Zhou: holonomy phases e^{i2nπμ} for scalars (eq. 63) and e^{i(2πμ−π)n} for Weyl fermions (eq. 64). The vector is R-neutral (eq. 71). The SUSY condition is μ₁+μ₂+μ₃ = q−1 (eqs. 74, 77, 80), and the free-field ratios to S₁ are (3q+1)/(4q) for two equal U(1)s.
- **Dictionary to NAMCG.** The IKKT SO(6) of the N_s = 6 transverse matrices plays the role of N = 4 SO(6)_R. The "rotated vector" branch of 017 (3 − n_D or 5 − n_D, continuation-dependent) is a holonomy-type rotation of the internal index.
- **Feasibility.** Medium-low as a derivation. High as a bounded check.
- **Value.** It would show that the gluing ambiguity in 017 is invisible to G_A and visible only to Rényi quantities. It cannot close B.

### R-a4: matrix and fuzzy entanglement templates (constraints, not supply)
- Scalar only. Karczmarek–Sabella-Garnier 1310.8345, Okuno–Suzuki–Tsuchiya 1512.06484 (replica method, free and interacting), Suzuki–Tsuchiya 1611.06336 (∝ (boundary area)² for free fields), Fliss–Frenkel–Hartnoll–Soni 2408.05274 and the review 2512.03163 (relational subsystems, edge modes, minimal areas).
- The only fermionic fuzzy definition I found is Nair 2207.04776.
- **Constraint.** Matrix-regularised entropies do not follow the continuum area law. Suzuki–Tsuchiya find a (boundary area)² dependence tied to the matrix regularisation. A Poisson-limit cone computation drops this. State it as a hypothesis.
- **Feasibility.** Low for supplying the missing step. Medium as a hypothesis check.

---

## 3. Route map (b): next-order (log / a_2) comparison in the D=10 content

### R-b1 (TOP): use the SO(1,9) character as the supertrace organiser
- **What to reuse.** Manta–Steinacker–Tran eq. (3.7), Q₁₀ = Tr_R( e^{iαΣ^{(V)}δℱ} − ½ e^{iαΣ^{(Ψ)}δℱ} − 2 ). The weights are 1 for the 10D vector, −1/2 for the Majorana–Weyl spinor, and −2 for the ghosts. Per the paper, the expansion starts at O(α⁴): the α⁰ and α² terms cancel between bosons and fermions (eqs. 3.11–3.16 give the gravitational part). Also Steinacker 2303.08012 eq. (4.16) with its V₄[δℱ] = −4 tr δℱ⁴ + (tr δℱ²)² (eq. 4.21).
- **Sub-lemma.**
  - Step 1. Check that 017's b_total = 1 − n_D/2 and c_T = 0 at (n_D, N_s) = (2, 6) are the same two cancellations. The α⁰ condition is a dimension count (10 − 16/2 − 2 = 0). The α² condition is a Dynkin-index count. This is my reading of the structure; it is not stated in the papers' text I read.
  - Step 2. Identify the first non-vanishing Poisson-limit coefficient at the next order, i.e. the a_2-type term of the same operator, with the Weitzenböck torsion terms of 011.
  - Step 3. Compare with Steinacker's EH coefficient 1/G_N = (2c_K²/π³) ρ⁻² m_K², c_K² > 0 (6.30–6.32).
- **NAMCG objects.** The 017 Dirac a₁ and the Dynkin ratio; the 011 torsion identity for ρ²X; the Poisson-limit leaf.
- **Constraint.** Steinacker argues explicitly against a heat-kernel cutoff, because non-local string modes dominate small proper time (2303.08012, Sec. 3). A cutoff-sensitive Λ² (area) coefficient and a finite KK-scale G_N are therefore different kinds of quantity. The comparison G_T vs G_A at the next order should be posed on a cutoff-independent coefficient.
- **Sign information.** G_N > 0 in the literature, with c_K² > 0 (6.30) and eq. (3.49) of 2411.02598. Caution: the Battista–Steinacker v2 correction of a sign error that changed their conclusions shows that signs in this family are fragile.
- **Emergence.** Preserved. The characters are representations of the matrix-model SO(1,9), not of a fundamental metric.
- **Feasibility.** Medium for Steps 1–2. Low for a clean G_T vs G_A statement at this order.
- **Status of success.** Step 1 would be a conditional sharpening that explains the 017 zero from the structure. A sign-definite G_eff in a stated content would be a genuine advance, but only if the entropy side is also supplied.

### R-b2: log coefficients from the conical side
- **References.**
  - Solodukhin 0802.3117 (log term from type A and type B anomalies).
  - Fursaev–Patrushev–Solodukhin 1306.4000 (squashed cones, needed once Σ has extrinsic curvature).
  - Fursaev 1201.1702 (weak-coupling N = 4 SYM Rényi, divergent part).
  - Hung–Myers–Smolkin 1407.6429 (expansion around n = 1, first terms fixed by ⟨TT⟩).
  - Lee–McGough–Safdi 1403.1580 and Bianchi–Meineri–Myers–Smolkin 1511.06713 (shape dependence and displacement operator).
- **Standing facts.**
  - N = 4 SYM has a = c (standard; not independently verified here).
  - The log coefficient is scheme-independent, unlike the Λ² coefficient, so it is the natural quantity for G_T vs G_A.
- **Sub-lemma.** Compute the log coefficient of the cone partition function for the Poisson-limit D=10 content on a curved leaf. Compare it with the a_2 of the induced action.
- **Constraint.** On the 017 J = 0 constant-Θ̄ domain, the leaf is flat. The log terms then vanish identically. A non-flat leaf is needed, which is 017's open avenues 4 and 7.
- **Feasibility.** Low now, medium after non-constant J = 0 backgrounds.

### R-b3: finite-K traces as a sign source
- Steinacker's c_K² = (π²/8) Σ_Λ C_Λ²/μ_Λ² (6.30) and its refinement with S² modes (7.22) is a mode sum over the fuzzy extra space. It is finite and positive.
- Possible use for F: determine whether the CP^{1,2} fibre can supply an analogous positive sum.
- **Caution.** The fibre of CP^{1,2} is part of the brane (twistor fibre), not a separate K. Mapping c_K² onto 018's w is a hypothesis.
- **Feasibility.** Low-medium.

---

## 4. Route map (c): F, the Nielsen–Olesen sector

### R-f1 (TOP for F): locate the self-dual / BPS locus and the flux inequality
- **Sub-lemma.** In the CP^{1,2} Poisson-limit class, compute the two flux eigenvalues (f₁, f₂) of the symbol at each point. Find where f₁ = f₂ occurs. 018 reports only a sampled range for f₁/f₂.
- **References and equations.** Troost eq. (35) (gauge levels with ±2f_k), eq. (43) (fermion levels), §9 (stability iff f₁ ≤ f₂ + … + f_n; on T⁴ this forces f₁ = f₂, which coincides with SUSY). Berenstein–Trancanelli 1011.2749 on tachyons as Nielsen–Olesen modes of fuzzy spheres.
- **NAMCG objects.** The 018 nilpotent model, the vector-sector spectrum −|f₁−f₂|, the Euclidean contraction η → δ.
- **Expected form of result.** Either a locus where the vector sector has no tachyon, so that the heat trace converges, or a proof that f₁ = f₂ is never reached in the class. Additional transverse fluxes (the 6 internal matrices, the fibre) relax the condition to Troost's inequality.
- **Why not content alone.** My inference from the verified spectra: fermion levels (2πΣ(2m_i+1)f_i with Zeeman shifts ±f₁ ± f₂) give a non-negative squared Dirac spectrum, so adding fermions leaves the bosonic e^{+s|f₁−f₂|} divergence. SUSY content helps through the BPS locus and through which terms cancel, not by cancelling the tachyon.
- **Feasibility.** Medium-high for a classification result.
- **Status.** Conditional sharpening. It determines where w can be defined at all.

### R-f2: alternative organisations of the one-loop integral
- Steinacker's character expansion (above) treats Σ^{μν}δℱ_{μν} perturbatively in the flux and uses a Lorentzian iε prescription. It does not need the Euclidean heat trace of a tachyonic sector. This is my reading of the structure and I have not verified how the paper treats tachyonic modes.
- Related stability results: Sugiyama–Yoshida hep-th/0207190 (BMN supersymmetric fuzzy sphere quantum stable, non-SUSY one unstable), Steinacker 1510.05779 (softly broken SUSY stabilises the fuzzy S⁴), Steinacker 1910.00839 (no-ghost theorem on a cosmological background).
- **Feasibility.** Medium. Relevant to the gatekeeper's ranking: a content change enters here through the different integral, not through a spectral cancellation.

### R-c1 (constraint on B): contact terms in the Larsen–Wilczek sense
- Larsen–Wilczek hep-th/9506066: the conical entropy depends on curvature couplings even in flat space, and fermion and gauge determinants relate to non-minimally coupled scalars. Solodukhin 1104.3712: coefficients (1/6 − ξ) for a scalar (eq. 141) and 𝒟₁/6 − 1 for a vector (eq. 148). Kabat: the spin-1 mismatch between BH and entanglement entropy is a horizon contact term.
- **Mapping to hypothesise.** 011's Weitzenböck identity expresses ρ²X through ρR[g_ρ]. In that case X acts like a ξR-type non-minimal term, and the replica (II) value −1/2 (015) is the analogue of the ξ-dependent conical term. The G_A − G_T gap then looks like the known "non-minimal coupling puzzle" (the Solodukhin review has a section by that name; seen in its table of contents, not read). Whether it closes is the Susskind–Uglum question already in 015.
- **Feasibility.** Low-medium. This is a constraint on what any content-based fix must reproduce.

---

## 5. Ranking across routes

| Rank | Route | Problem | Feasibility | Breakthrough or sharpening | Emergence |
|---|---|---|---|---|---|
| 1 | R-a1 graded-trace twist | A/B | high | conditional sharpening; likely confirms the c_A = 2 vs c_T = 0 mismatch | preserved |
| 2 | R-b1 SO(1,9) character supertrace | B/F | medium | sharpening; genuine if a sign-definite G_eff follows | preserved |
| 3 | R-f1 self-dual / flux-inequality locus | F | medium-high | sharpening | preserved |
| 4 | R-a3 SUSY holonomy as consistency check | A/B | medium | consistency only | preserved |
| 5 | R-c1 Larsen–Wilczek contact-term mapping | B | low-medium | constraint | preserved |
| 6 | R-a2 modular-group template | A | medium | check | preserved (needs emergent G) |
| 7 | R-f2 Lorentzian/character organisation | F | medium | method | preserved |
| 8 | R-b2 log terms (curved leaf) | B | low now | genuine if completed | preserved |
| 9 | R-b3, R-a4 finite-K sums, matrix entanglement | F, A | low | hypothesis checks | preserved |

**Do not expect R-a1 to rescue B.** The most likely outcome is that antiperiodic gluing stands and the Λ² mismatch is real at the D=10 content. That is useful: it shifts the burden to contact terms (R-c1) and to the next order (R-b1).

## 6. Conflicts to respect
- No published no-go (Weinberg–Witten family) is touched by these routes. The graviton here is a composite of matrix modes.
- Fursaev–Miele: do not treat the spin-2 tensor block as scalar-like without justification (non-analytic at β = 2π).
- Nishioka–Yaakov: the ordinary replica construction is not supersymmetric. Any claim about "the SUSY gluing" needs the R-holonomy, and it affects only Rényi order.
- Lokhande–Mukhi and Dowker warn that fermion Rényi results depend on spin-structure sums and chemical potentials in other settings (2D, charged Rényi). Not a direct obstruction in 4D flat cones.
- Steinacker: heat-kernel cutoffs are argued to be inappropriate for the IKKT one-loop action on covariant quantum spaces. NAMCG's Λ² comparison inherits that caveat.

## 7. Suggested next targets for the researcher
1. R-a1, then re-state the 017 gap with the fixed gluing.
2. R-b1 Step 1 (the two cancellations), as a bounded check before any new computation.
3. R-f1 classification of the (f₁, f₂) locus in the CP^{1,2} class.
