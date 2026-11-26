VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The algebra is correct and reproducible. The scalar identity, the Θ-built composite metric, the connection-sector trace and the quadratic eigenvalues all re-verify. Three statements overreach or are ambiguous: the sign sentence, the X non-covariance wording and the N_tot definition. They must be tightened before this goes into appH. As a result it is a conditional computation, not an M2 no-go.

## Source reading
Digest plus targeted reads. I did not do a full scan.
- appH L1600-1660: the anchor paragraph and the following section heading.
- ch04 L80-180: `eq:vev-is-frame`, `def:composite-metric`, `eq:g-from-e`, `ass:nondeg`.
- ch03 L125-155 (`eq:Smatrix`) and L565-600 (`rem:ch3-varying-theta`).
- Label and bib greps.
- The proposal in full, plus its scripts and saved outputs.

I did not re-read Chapter 17 or the F entry in appH end to end. I relied on the proposal's quotations of the F entry and the Chapter 17 completion criterion (A, B, C, D1, E, F, G-derived, N; H, I, J optional). I spot-checked appH L1600-1650, which is consistent with those quotes.

## Claim under review
Presentation A in the Poisson limit, toward `ass:emergent-op`, for Problem F.

Problem F, quoted from the proposal's account of the appH ledger (not re-read in full by me): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL." The scoped line reads "Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."

The original F target is the weighted a_1 and curvature-linear a_2 on the locked block, with diffeomorphism and local-Lorentz ghosts and the radial threshold. This proposal does not touch that target.

## Checks performed
**Direct verification, by hand**
- Scalar sector: L = ρ⁻¹∂(ρK∂) = Δ_G − K dlnρ·∂. This gives D=∇+ω with ω=−½dlnρ and E=divω+ω², matching the proposal.
- Conformal formulas for G=ρg in 4D: R_G=ρ⁻¹[R−3□lnρ−(3/2)|∇lnρ|²]. This follows from Ω²=ρ, □Ω/Ω=½□lnρ+¼|∇lnρ|².
- I got E=ρ⁻¹[−½□lnρ−¼|∇lnρ|²]. Hence √|G|(R_G/6−E)=ρR[g_ρ]/6 exactly, with no unimodular-family assumption. Claim 1 is established, and the ρ-measure versus √G-measure difference is immaterial because conjugation by a function preserves the trace.
- |det g_ρ|=1, √|G|=ρ².
- Θ G Θᵀ = η⁻¹ follows from K=ΘᵀηΘ. With B antisymmetric when lowered, tr(B_σB^σ)=−X and tr B=0, so the cross terms drop. The signs are consistent: connection sector 4·ρR/6+ρ²X, ghosts −2·ρR/6, net (2/6)ρR+ρ²X.
- Eigenvalue arithmetic: −c[(N_tot/6)(−¼)·(−1)…] reduces to 1−N_tot/24 on the two TT-type modes, and to 1−(N_tot/6)(3/4)=1−N_tot/8 on the third. Here N_tot=N_s+2 is exactly the count the eigenvalues use.

**Claim 2**
- G_{μν}=η^{AB}ω_{μA}ω_{νB}=K⁻¹ is the form of `eq:g-from-e` for e=η⁻¹ω. An antisymmetric coframe is admissible as an algebraic input. It is nondegenerate whenever Θ is, and has the signature of η.
- The claim is correct but close to tautological. It says only that Θ-built metrics are a 6-parameter subfamily. Identifying A with μ through η is a fixed, non-covariant identification. This is the same non-invariance Lemma 2 excluded, relocated into ⟨Φ⟩/v ≟ ω. The proposal states this honestly.

**Scripts re-run (symbolic and numeric checks, not proofs)**
- `check_vector_sector_block.py -1` and `check_vector_sector_generic.py`: EL operator = ηO_v, −D²+E=O_v, scalar and vector identities all zero. Generic magnitudes are nonzero, so the checks are non-trivial.
- `check_soldering_and_frames.py`: K⁻¹=eηeᵀ in both signatures, η·e antisymmetric, rank 6, conformal-frame formula.
- `analyze_quadratic_forms_symbolic.py 1 1 2`: roots λ=ρ̄²p²/… giving +1 (×3) for X and −¼ (×2), −¾ (×1) for ρR, in ρ̄²p_η² units.
- `check_fp_crosscheck.py 1 1 2 1 2 3 5`: reproduces the FP cross-check matrix.
- I did not write an independent brute-force Ricci computation. The −¼ and −¾ values rest on the researcher's brute-force and FP cross-check scripts.

**Premises and repository checks**
- η is the index contraction in `eq:Smatrix` (ch03 L143-148). The premise holds.
- Emergence: Θ is the matrix background and G is built from Θ and the target contraction η. Nothing makes the metric fundamental. There is no emergence violation.
- No label is changed.
- All cited labels exist once each, including `ch:vierbein-emergence`, which was not in the proposal's verified list but exists. `Steinacker2010` is in the bib.
- The anchor sentence occurs once, at appH L1647-1648, followed by `\section{Problem G: HBEV}` at L1650.
- Repository touch: commit 3c448f6 changes only files under proposals/005…. Working-tree modifications (`.claude/agents/*`, untracked `proposals/006-…`) are not from this proposal. I did not check their provenance.
- Literature: `Steinacker2010` and `Steinacker2023` were not independently verified by me. The block does not rely on them for any result.

## Findings

1. **Major.** Location: LaTeX paragraph "Quadratic form…", sentence "The Einstein–Hilbert-type piece has the sign of a positive induced 1/G_eff in the first form only if N_tot>24".
   - Finding: As written it is wrong. The EH piece contributes +cN_tot/24 times the positive-G sign for every N_tot>0. It is the net form (1−N_tot/24) that has that sign only for N_tot>24.
   - Further point: "sign of positive 1/G" is meaningful here only as the sign of the Maxwell-kernel coefficient of a quadratic form on gauge-built modes. Those modes are a 3-dimensional subspace per p of the metric fluctuations, with δg_ρ linear in T.
   - Required action: reword to "the net coefficient on the TT-type modes has the sign of a positive EH term only if N_tot>24", and add that this is a statement about the Maxwell-kernel coefficient on these modes. The "ρ²X has the opposite sign and dominates" part for N_tot=2 is correct.

2. **Major.** Location: LaTeX connection-sector sentence "for a generic Poisson bivector this fails", the "Neither X nor EH" framing, and the proposal's M2 claim.
   - Finding: The only evidence is a comparison of X with one candidate, 2K∂lnρ∂lnρ, at one numeric point. The proposal itself concedes that X may have a covariant rewriting.
   - Independent observation, using the proposal's own numbers: at quadratic order about constant Θ̄, X has eigenvalues (1,1,1). The covariant family αρR+βρ|∇lnρ|²_g has eigenvalues (−α/4, −α/4, −3α/4+β′). So α=−4 with a suitable β′ reproduces X exactly at this order. The quadratic data cannot distinguish X from a covariant term of opposite EH sign. The "bounded obstruction" is therefore not an established no-go, and the "N_tot>24" statement becomes a statement about the net effective EH coefficient only if X is so reinterpreted. This is not proved either.
   - Required action: in the LaTeX, state that the comparison is with that single expression and that no non-covariance is claimed. Do not call the result an obstruction anywhere in the manuscript text (it currently does not). Record in the ledger that the result is a conditional computation, not a no-go.

3. **Major.** Location: LaTeX definition "Let N_tot be the weighted number of components of scalar type, plus the net 2…".
   - Finding: The definition is ambiguous. It does not say which Φ and fermion components are counted, with what weight, or that each must have operator O_s with the common cutoff and no Φ–a mixing.
   - Required action: define N_s as the number of real components whose fluctuation operator is O_s with the same cutoff, counted with sign for statistics. State that N_tot is an input count, not derived. Keep the proposal's "32 components is an input" remark in the ledger, not as a manuscript claim.

4. **Minor.**
   - (a) The sentence "at generic Θ and p no pure-gauge perturbation lies in its tangent space" is only sampled. Say "at the sample points tested" for both clauses.
   - (b) The closing text refers to "the preceding scaffold-rotation paragraph", but the paragraph immediately before it is "What the two preceding results imply". Cite the scaffold-rotation statement by what it says, for example "Lemma 2 above", or describe it. The Lemma 2 label is not given in the proposal, so I did not check it.
   - (c) The symbols a for Θ^{01}=a(x⁰,x¹) and a^μ for the gauge potential clash. Rename one.
   - (d) Add "Euclidean" where signs of eigenvalues are quoted. The text already says signs refer to the Euclidean section.

## Scope of what is established
**Established identities:**
- The scalar-sector identity √|G|(R_G/6−E)=ρR[g_ρ]/6, for the Poisson-limit operator.
- G = η_{AB}e^Ae^B for e=η⁻¹Θ⁻¹.
- The connection-sector trace formula, given the stated quadratic action. This is established algebra, verified exactly on the block family and at a generic point.
- The eigenvalues +1, −¼, −¾.

**Conditional on:**
- The Poisson limit with Moyal terms dropped, though they are not small at the cutoff.
- A bosonic 4D matrix gauge sector, off-shell, in a minimal background gauge.
- A diagonal heat kernel with constant or local cutoff, and Euclidean signs.

**Not established:**
- `ass:emergent-op` is not discharged. ⟨Φ⟩/v=ω is not derived, Φ–a mixing is not treated, and N_tot is an input.
- No sign or value of G_eff follows.
- The obstruction is only a statement within that hypothesis class and is not shown not to be covariantly absorbable (finding 2).
- The class relaxed from Lemma 2 (H1-H4) is a 6-parameter nonlinear subfamily with no diffeomorphism protection, so this is not a Presentation-A closure either.

**Labels and breakthrough:**
- F, A, B, C, D1, E, G-derived and N remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. No label change is proposed or implied.
- This is not a BREAKTHROUGH.
- Milestone: none. This is not M1 because no critical-path step is derived. It is not a no-go (M2) because the claimed obstruction is not established as one (finding 2).

## Recommended disposition
Revise per findings 1-4 and resubmit the corrected block as round 2. The core derivations need no change, and only the text must be tightened. Once those corrections are made, the paragraph is an acceptable conditional sub-lemma on the Presentation-A form of `ass:emergent-op` for appH. It should be filed with ledger wording of "conditional computation", not "obstruction".

## Corrected snippet
Replacements for findings 1-3. They introduce no new physics, only wording fixes.

Finding 1, replacing the sign sentence: "The net coefficient on the two transverse-traceless-type modes has the sign of a positive induced Einstein–Hilbert term only if \(N_{\mathrm{tot}}>24\); the Einstein–Hilbert-type piece itself always has that sign. For the connection sector alone, \(\rho^2X\) has the opposite sign and dominates. This is a statement about the Maxwell-kernel coefficient on these modes."

Finding 2, replacing the end of the connection-sector paragraph: "…\(X=2K^{\mu\nu}\partial_\mu\ln\rho\,\partial_\nu\ln\rho\); for a generic Poisson bivector \(X\) differs from this one expression. No claim is made about other covariant rewritings of \(X\)."

Finding 3, replacing the N_tot definition: "Let \(N_{\mathrm{tot}}=N_s+2\), where \(N_s\) counts, with statistical sign, the real components whose fluctuation operator is \(\mathcal O_s\) with the same cutoff. It is an input, not a derived count."
