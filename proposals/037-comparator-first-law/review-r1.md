VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The decomposition, dictionary arithmetic and equivariance results reproduce exactly, and the "comparator is not forced" point is sound. Two sentences of the insert overstate the result and must be reworded before integration. The "Noether value with the replica's own holonomy" comparison is vacuous. The Noether density is stated for the composite connection without its auxiliary-variable hypothesis.

## Source reading
Full scan. `scripts/make_digest.py --check` printed `DIGEST STALE`, and `appH` is dirty with the expected 032/033/035/036 text. I read every current `chapters/*.tex` in full, which is the manifest of 30 files:
- ch01 through ch18, including ch17-agenda.
- appA through appL, including all 2737 lines of `appH-microscopic-proofs.tex` (Problems A, B, C, D, E, F, G, H, I, J, N).

The full scan was required by `CLAUDE.md` 3(d), by 3(c) (the insert revisits a scope statement in the 033/036 blocks), and by the ordinal (34, with 35 pending). `*.aux` and `figs/` are not in the manifest. I also read in full:
- `proposal-r1.md`, `appH_insert.tex`, all six 037 scripts and their libraries.
- `reports/sme-scout-torsion-entropy-20261018.md`.
- `proposals/036-connection-edge-weyl/review-r2.md`.
- `reports/ledger.md` (tail).
- `MILESTONE.md`.

Proposals 034 and beyond were ignored as instructed.

## Claim under review
Conditional claim, Problem B (with A). Original target of B, per Chapter 17: derive `\delta S_D=0` at fixed volume, with the tensor block, from the microscopic action.

Appendix H, verbatim:
- B: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- A: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- Chapter 17 requires A, B, C, D1, E, F, G-derived and N; H, I and J are optional. No discrepancy between Chapter 17 and Appendix H.

The claim is that the 033 Weyl gap `2\kappa_X` is relative to a metric-universal comparator `12\kappa_C^T`. That comparator is the entropy of a metric functional with the same mode values as `\mathrm{tr}\,\Omega^2`. It is not shown to be the entropy of `\mathrm{tr}\,\Omega^2`. The only first law constructible for the composite connection pairs with `\mathcal J_{12}` and gives `-2\kappa_X`. Against that value the completed replica has no gap, and the residuals of the periodic, fixed-state and completed replicas are `2-n_D`, `2` and `0`.

## Checks performed

**Direct re-runs.** All outputs are identical to the submitted `*.out.txt`.
- `a_decomposition.py` and `a2_frame_variants.py`:
  - `<Ω,Ω>=-4C²`, `<R,R>=-2C²`, and `ℓ_J12(Ω)=ℓ_J12(R)=-R_ijij`.
  - `<Ω,R>=0` for the identity identification and `-2C²` for the coframe identification.
  - It follows that `Ω=R+N` with `<N,R>=0`, `<N,N>=<R,R>`, `ℓ(N)=0` under the coframe identification.
  - Both chiralities.
- `b_dictionary.py`:
  - W-coefficients are `N_tot/10`, `N_tot/10+n_D` and `N_tot/10-2+n_D`, i.e. `(α_v,α_f)=(0,0),(0,1),(1,1)`.
  - The comparator is `N_tot/10-4κ_X`, i.e. `(2,2)`.
  - Gaps are `4-2n_D`, `4-n_D`, `2-n_D`; residuals against `(1,1)` are `2-n_D`, `2`, `0`.
  - I also checked by hand that this arithmetic matches 033's gaps, including the `N_tot` part.
- `c_equivariance.py`: zero mismatch only for the diagonal rotation.
- `e_extension.py`: `Q_1=Q_2` on single modes, `B_1≠B_2` on pairs and on generic closed jets.
- `f_multiplier_toy.py`: reproduces.

**My own check.** `gk_check.py` is in the session scratchpad and was not run in the proposal folder. It reuses the 037 libraries on six modes per chirality and confirms:
- `Riem²=2C²`, `Ric²=C²/2`, `R=0`, `E_4=0` at quadratic order on the modes, and `trΩ²=-4C²`.
- The 033 metric cross-term rule (`12κ_C W+12κ_E R_Σ+12κ_R R` in the basis `C²,E_4,R²`), applied to the Levi-Civita functional `a·Riem²` with `a=-1/12`, equals `τ_Ω=tr(J_12Ω_12)` exactly. This used `Riem²=2C²-E_4+R²/3`.
- Therefore the Noether value `-2κ_X W+κ_X R_Σ` is the metric rule applied to the Levi-Civita part of `Ω`. The comparator `-4κ_X` differs only because `tr Ω²` carries twice the `C²` weight of `tr R²` on these modes.
- This independently supports the submitted claim: the factor 2 is norm doubling, not a first-law output.

**Merged text.**
- 033 (gaps, and "that part is the gap"): unchanged and still true, because those gaps are stated relative to the comparator.
- 035 (Noether `-2κ_X` under the tied-frame, auxiliary-variable hypothesis): consistent.
- 036 ("whether the entropy of this non-metric term is that value or the Noether value ... is not decided here"): remains true as a statement about 036. The insert supplies an argument and no merged sentence becomes false. This is the decision of an open question, not a `PRIOR-CLAIM-ERROR`.
- No stale statement elsewhere in the 30 files.

**Bibliography and equivariance.**
- Jacobson–Mohd (arXiv 1507.01054; Crossref): PRD 92, 124010 (2015), Ted Jacobson and Arif Mohd. The BibTeX entry matches. The abstract supports the statement that the diffeomorphism-only charge is unsuitable because a regular frame cannot be Killing-invariant at the bifurcation surface.
- Frolov–Fursaev (arXiv hep-th/9703178; Crossref): PRD 56, 2212–2225 (1997). The BibTeX entry matches.
- Neither new key exists in `bib/namcg.bib`, and no key or DOI is duplicated.
- arXiv 2012.14892 is Elgood, Ortín, Pereñíguez, "The first law and Wald entropy formula of heterotic stringy black holes at first order in alpha prime", JHEP 05 (2021) 110. The researcher's correction of the scout (which had "Elgood–Meessen–Ortín") is right. It is not cited in the insert.
- `c_equivariance.py`: the failures for non-orthogonal maps and non-linear chart changes follow from the fixed δ/η contraction in `K=Θ^TηΘ`. The chart-only and index-only failures follow from `Θ` supplying both the chart and the matrix indices of `b`. This supports "tensorial only under the diagonal rotation". It does not discriminate further.

**Anchor and characters.**
- The insert is identical to the proposal block.
- It is 5033 bytes, pure ASCII, with 0 TAB, 0 CR and no control characters.
- Braces and `\(`/`\)` are balanced. Only `\cite{JacobsonMohd2015}` and `\cite{FrolovFursaev1997}` are added, with no `\label` and no `\ref`.
- `\section{Problem C: conformal mode and Cassini}` occurs exactly once (line 295). It is preceded by the blank line after the 036 block ending "Problem~B stays open and PROGRAMME-CONDITIONAL." (line 293).
- The repeated closing status line follows the file's established pattern.
- The researcher's 301-page scratch compile is not independently verified.

## Findings

**F1. Major. Dictionary paragraph.**
- Finding: "the Noether entropy of the induced action with holonomies `(α_v,α_f)`" and "Relative to the Noether value with the holonomy of the replica the gaps `4-2n_D`, `4-n_D`, `2-n_D` therefore vanish" overstate the result.
- Reason:
  - The Noether (Jacobson–Mohd) charge has a fixed pairing `H=𝒥_{12}`, i.e. `(1,1)`. There is no Noether value at `(0,0)` or `(0,1)`.
  - `E(α_v,α_f)=N_tot/10-2α_v+n_Dα_f` is the cross term `Σκ_i tr(H_iΩ_12)` for a chosen holonomy.
  - The replicas' `(α_v,α_f)` are read off from their gluing. So vanishing "gaps" at `(0,0)` and `(0,1)` are identities, and the completed one is the same cross term with the same deltas.
  - The researcher's own "Decisions Taken" rejects "fixing it by matching the replica". The sentence does exactly that.
  - "`12κ_C^T` is its value at `α_v=α_f=2`, twice the replica rotation" can be read as a physical holonomy. 036 shows `-4κ_X` needs `J_12-χJ_34` with a singular `Σ` metric.
- Required action: reword as in the corrected snippet. Delete the vanishing-gap sentence. Keep the residuals against `(1,1)`. State that the `(2,2)` entry is a statement about the coefficient of `W` only.

**F2. Major. Composite constraint paragraph.**
- Finding: "A first law of the form of the Lorentz–diffeomorphism Noether charge ... is available only with this tie, and then gives the density `κ tr(HΩ_12)`" omits that this is the auxiliary-independent-connection reading, the hypothesis of the merged 035 block.
- Reason:
  - For the composite `ω=F[Θ]` the multiplier term `⟨λ,ω-F[Θ]⟩` has its own Noether contribution. `F` contains `∂Θ`, and `δ_ξΘ` involves `∂ξ`, which is non-zero at `Σ`.
  - It vanishes only if the combined diffeomorphism-plus-diagonal-rotation action annihilates `δΘ` at `Σ`. That is plausible by equivariance but is not shown.
  - The 1-D multiplier toy establishes only equivalence of field equations. It says nothing about the charge.
  - The diffeomorphism-covariant Iyer–Wald derivation is not available (Problem D). The sentence reads as more than that.
- Required action: add the auxiliary-variable hypothesis. Add that the charge of the constraint term is not computed. Describe the toy as a field-equation check only. Add the same item to the closing "do not derive" list.

**F3. Minor. "Comparator is an extension" paragraph.**
- Finding: "have the same value on each mode" and "is the entropy of the metric functional ..., not of `tr Ω²`".
- Reason:
  - The equality is verified on sampled modes (six per chirality in 033, four in `e_extension.py`), not proved for the family.
  - "Not of `tr Ω²`" presupposes a different value. What is established is that the comparator is not shown to be that entropy.
- Required action: use "on every sampled mode" and "is not shown to be the entropy of `tr Ω²`".

**F4. Minor. Multiplier sign.**
- Finding: the insert and Result item 2 give `λ=-D(∂L/∂Ω)`. The script, with `L+λ(ω-F)`, gives `λ=+ω''=+D(∂L/∂ω')`.
- Reason: the sign depends on a multiplier convention the insert does not state.
- Required action: drop the explicit sign or state the convention.

**F5. Minor. Frolov–Fursaev citation.**
- Finding: the abstract gives the surface term `Q` as a Noether charge of non-minimally coupled scalar fields. Using it for the vector holonomy contact is an analogy.
- Reason: "of the type" is acceptable only if the analogy is stated.
- Required action: add "by analogy with the Noether-charge term for non-minimally coupled scalars of FF".

## Scope of what is established

**Established** (exact or sampled arithmetic, for the 033 modes, totally geodesic `Σ`, first order in `1-n`, Euclidean section, coefficient of `W` only):
- `<Ω,Ω>=2<R,R>` and `ℓ_J12(Ω)=ℓ_J12(R)` on all sampled modes.
- The Noether value `-2κ_X` equals the metric cross-term rule applied to the Levi-Civita part of `Ω`.
- The comparator is the metric extension with doubled norm. Its cross term is not fixed by the mode values (`B_1≠B_2`).
- The dictionary arithmetic.
- The residuals `2-n_D`, `2`, `0` against `(1,1)`.

**Conditional.**
- The "artefact" reading holds only for the auxiliary-connection reading, equivariant tying, and delta content `Ω_δ=2π(1-n)𝒥δ_Σ` with no `N`-part. These are the 033/035 hypotheses.
- Agreement of the completed replica with the Noether value is an identity of two cross terms of the same `a_2`. The Dirac entry is a partial independent check (exact Landau–Aharonov–Bohm spin term versus the `a_2` index weight).
- It is not a selection by fiat. The researcher did not tune holonomy to close the gap, apart from the F1 wording. It is also not a derivation: the first-law pairing is conditional on F2.

**Not established.**
- Which holonomy the matrix state selects. The vector spin-complete branch is non-analytic at `n=1`.
- The Λ²-order `G_T` versus `G_A` mismatch for the first-derivative `ρ²X` term. This is the load-bearing identification and is untouched.
- The Euler coefficient and off-mode structure.
- Any derivation of Assumption~\ref{ass:EE}.

DERIVED nothing. Problems B and A remain OPEN and PROGRAMME-CONDITIONAL. No label is touched.

**Breakthrough assessment (`gatekeeper.md` criteria).** Not a breakthrough, and no `LABEL-CHANGE-PROPOSED`. It derives no critical-path step from the matrix theory. It is conditional, covers one coefficient on sampled modes, and its central agreement is an identity. It does not touch the Λ² identification. No milestone trigger fires: M1 no, M2 no, M3 no (no `PRIOR-CLAIM-ERROR`), M4 no, M5 no. Spacetime stays emergent: the connection is a bookkeeping variable and the "flow" acts on the matrix chart.

**Open avenues, ranked.**
1. The Λ²-order analogue: the entropy of the first-derivative `ρ²X` term in an Iyer–Wald treatment with `Θ` fundamental (Problem D lift). It decides `G_T` versus `G_A`.
2. The charge of the multiplier or constraint term, to settle whether `-2κ_X` is the composite-theory Noether value (F2). It could change the answer.
3. Whether the replica deforms the non-Levi-Civita part `N`: off-diagonal profiles with `J_34` circulation and a regular `Σ` metric, and the exact cone heat trace with holonomy.
4. Selection of `α_v` from the modular flow, and the n>1 branch and non-analyticity.
5. Non-geodesic `Σ` (Dong/Camps `K²` terms) and the Euler coefficient.

Hypotheses a within-core route could relax: the auxiliary-independent-connection reading, the completeness of the delta content, the first-order cross-term rule, and the hybrid fixed-state replica.

## Recommended disposition
Revise, then integrate. The required changes are wording and scope only and need no new physics. The same text could not be accepted unchanged, because F1 and F2 change what the manuscript records.

## Corrected snippet
No new physics; no extra assumptions beyond the 035 ones already merged.

1. Replace the sentence beginning "A first law of the form of" with:
```
A first law of the form of the Lorentz--diffeomorphism Noether charge~\cite{JacobsonMohd2015} can be formed only with this tie. If the connection is treated as an auxiliary independent field on which the Lagrangian depends through its curvature, it gives the density \(\kappa\,\operatorname{tr}(H\Omega_{12})\) with \(H=\mathcal J\); the charge of the constraint term is not computed. A covariance under general diffeomorphisms of the chart is not available for \(b\).
```
Also replace "gives \(\lambda=-D(\partial L/\partial\Omega)\) and the Euler--Lagrange expression of the composite Lagrangian (symbolic check in a one-dimensional toy)" with "fixes \(\lambda\) in terms of \(D(\partial L/\partial\Omega)\) and reproduces the Euler--Lagrange expression of the composite Lagrangian (a check of the field equations in a one-dimensional toy, not of a charge)".

2. Replace from "\emph{Dictionary.}" through "...vanish; relative to the spin-complete value \((1,1)\) the residuals are \(2-n_D\), \(2\), \(0\)." with:
```
\emph{Dictionary.} Let \(E(\alpha_v,\alpha_f)\) be the coefficient of \(W\) in the cross term \(\sum_i\kappa_i\operatorname{tr}(H_i\Omega_{12})\) with the holonomy \(H=\alpha_v\mathcal J\) on the vector bundle and \(H=\alpha_f\mathcal J\) on each Dirac fibre. It is \(N_{\mathrm{tot}}/10-2\alpha_v+n_D\alpha_f\), because \(\operatorname{tr}(\mathcal J\Omega_{12})\) has coefficient \(-2\) of \(W\). The Noether value of the preceding paragraph is \(E(1,1)\). The periodic, fixed-state and completed replicas have the coefficients of \(W\) of \(E\) at \((\alpha_v,\alpha_f)=(0,0)\), \((0,1)\), \((1,1)\) for all \((N_s,n_D)\) (exact arithmetic on six modes of each chirality), so their agreement with \(E\) at their own holonomy is an identity. The comparator \(12\kappa_C^T\) equals \(E(2,2)\); this is a statement about the coefficient of \(W\) and not about a holonomy of the bundle. Relative to \(E(1,1)\) the residuals of the periodic, fixed-state and completed replicas are \(2-n_D\), \(2\), \(0\).
```
Keep the following sentences unchanged: "For the periodic and completed replicas ... same deltas.", the Dirac sentence, and the Frolov–Fursaev sentence. In the last, replace "a contact of the type \(S_{\mathrm{BH}}=S_{\mathrm{ent}}-Q\)~\cite{FrolovFursaev1997}" with "a contact of the type \(S_{\mathrm{BH}}=S_{\mathrm{ent}}-Q\), by analogy with the Noether-charge term for non-minimally coupled scalars of~\cite{FrolovFursaev1997}".

3. In "The comparator is an extension", write "have the same value on every sampled mode" and "is not shown to be the entropy of \(\operatorname{tr}\Omega^2\)".

4. In the closing paragraph, add to the "do not derive" list: "the charge of the constraint term of the composite connection".
