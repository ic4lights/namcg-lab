VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The computations check out: residue 4, delta contact −N_tot/4 (so 7/2 − N_s/4), vector holonomy contact −α_vσ, and Dirac holonomy zero. The paragraph's closing sentence contradicts its own r-analysis, and one scoping clause is missing. Both need fixing before integration.

## Source reading
Digest plus targeted reads. The digest is stale (`--check` prints "DIGEST STALE (head changed)"), and the working tree is dirty with the 037 integration (expected).

Decision on the full-scan rule:
- CLAUDE.md 3(d) applies in the form "read the affected passages directly". I did that.
- 3(c) does not apply. The block adds one paragraph and changes no definition, assumption, scope sentence or status line.
- Ordinal 36 is not a multiple of 5.
- I did NOT do a full scan, so no manifest is claimed.

Passages read in full:
- the proposal, `appH_insert.tex`, and the s1–s8 scripts and outputs;
- Appendix H L168–L204 and L276–L306, covering the normalisation paragraph (L174–L179), the fermionic-content, gluing and smooth-cone paragraphs, and the 037 block;
- the torsion-invariant paragraph (L2013–L2020).

I also grepped all chapters for "no entropy", "bounded on the replica" and "Noether". The only hits for "no entropy" and "bounded on the replica" are in appH L177.

I did not re-open the Chapter 17 and Appendix H status lines myself. I rely on the proposal's quotation of them and found no contradiction in the passages I read.

## Claim under review
Bounded obstruction at order Λ² under the 031 hypotheses. The target is the 1/G_A − 1/G_T = 2Λ²_{UV,v}/π gap.
- B (as quoted in the proposal, and consistent with my reads): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL."
- A (as quoted in the proposal, and consistent with my reads): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

## Checks performed
Re-run by me: s1, s2, s3, s4, s6, s7, s8. I read the saved s5 output rather than re-running it (it takes minutes).

- **Residue and contacts.**
  - c_A − c_T = 4κ_X = 4 at n_D = 0, since κ_X = 1 − n_D/2 matches the ledger weights (L234).
  - The E_δ contact is −N_tot/4 with N_tot = N_s + 2, which gives 7/2 − N_s/4. Verified in s7.
  - The zeros at N_s = 14, 10, 18 are correct.
  - The Kabat sign/branch convention agrees with ledger L191 (−1 on n<1, +1 on n>1).
- **Twisted-cone constant.** s2 matches C(n,a) = B_2(a)/(2n) − n/12 to about 1e-12 at 12 pairs.
  - I hand-checked the first-order step: (1 − n∂_n) of the linear term −α(1−n)/2 gives −α/2 per component, so two components give −α.
  - The normalisation is consistent: the base value is 1/6 per real scalar.
- **Dirac holonomy.** It is zero at first order. This is conditional on the less singular extension, and the block states that.
- **Torsion algebra (s1).** TT, TT′ and 𝒯 decompose exactly in V², S², q², and the R-coefficients −2, 4, 1 hold. The identities R = −𝒯 − 2∇·V and the ledger ρ²X identity are exact on random two-jets (finite-amplitude generic two-jets of a closed ω).
- **Mode ratios (s4).** S² : q² : X = 1/3 : 2/3 : 1 and ⟨R⟩ = −⟨X⟩/4. The mode-null remainder has a nonzero cross term between modes.
- **Joint versus pure Lie derivative (s3).** The family and the span of e12, e34 are invariant under the joint flow only. The pure Lie derivative is nonzero. X·u² = 2(n−1)²/n² is unbounded at Σ for n ≠ 1 in the singular-ρ family.
- **Noether charge (s5 output).** J = dQ − E e ξ holds to 1e-30, and Q ∝ ξ. This agrees with the standard structure of a first-order teleparallel-type functional. The pure-diffeo charge vanishes on Σ for such L(e, de).
- **Local-rotation null direction (s8).** It is (1/4, 1/2, −1) with residual 1.7e-29. This is the TEGR combination. Numerical, d = 3.
- **Citations.** Crossref confirms author, title, volume and pages for all three keys.
  - IyerWald1994: PRD 50, 846–864.
  - JacobsonKangMyers1994: PRD 49, 6587–6598.
  - Foster2006: PRD 73, 024005.
  - Abstracts via arXiv fetch: Foster says the first-law derivation fails because the unit vector is necessarily singular at the bifurcation surface, with no definitive entropy. JKM says ambiguities in the Noether construction do not affect the entropy.
  - The block's attributions are supported at abstract level. The Iyer–Wald step about Y was not independently re-read in the paper.
  - `grep -c` finds 0 existing entries for each of the three keys in `bib/namcg.bib`.
  - LewkowyczMaldacena2013 exists (L548).
  - Declining the Mohd attribution is correct: it is unverified and unused.
- **Block bytes and anchor.**
  - `appH_insert.tex` is 10032 bytes with 0 CR and no tab (the CR check uses grep). I could not run the non-ASCII check, because `grep -P` errored in this locale.
  - The anchor `\section{Problem C: conformal mode and Cassini}` occurs exactly once (L306), directly after the 037 block that ends "Problem~B stays open and PROGRAMME-CONDITIONAL."
  - `\LUV` is defined in `namcg-book7.tex`. booktabs is already in use in Appendix H (L168).
  - No `\label` or `\ref` is introduced, and there is no process language.
  - CRLF must be applied by the integrator, as the block is LF.
- **Emergence.** Preserved. The coframe e = η⁻¹ω is built from the Poisson bivector. The block states the contraction is with the fixed matrix η, not a spacetime metric. No label changes.

## Findings

1. **Major. Location:** the final paragraph of the block, "no value of the Noether coefficient obtained from the density supplies the required −4κ_X…".
   - **Finding:** this contradicts the block's own earlier statement that c_W − c_T = κ_X(r+4), zero for every content at r = −4. It also contradicts "any real r is obtained by adding r(R + 𝒯 + 2∇·V) = 0".
   - **Reason:** the Noether route is not a mismatch. It is an indeterminacy (your item 2): "no match" is ill-posed for the Noether coefficient, because r = −4 is attainable. The genuinely rigid obstruction statements are the replica-contact rows and the pure-diffeo vanishing of the charge on Σ.
   - **Required action:** reword so that the replica/contact rows are a mismatch and the Noether coefficient is undetermined. For example: "no canonical value of the Noether coefficient follows from the density; r = −4 would match but is selected only by the match, and the ledger value r = −2 leaves 2κ_X". Also change the closing "obstruction" wording to "mismatch for the replica contacts; indeterminacy of the Noether coefficient". Check the proposal and report wording to the same effect. The proposal's own text already says "free real r"; only the merged sentence is inconsistent.

2. **Major. Location:** replica scoping, lines 2–4 and 19 of the block, against appH L177.
   - **Finding:** the block mixes two replicas without saying which is used where.
     - Row 1 ("fixed-state") uses the regular-ρ replica, for which X is bounded and "contributes no entropy" in L177.
     - The dragging and regularity text uses the singular-ρ family f = |z|^{n−1}, where X is unbounded (X u² = 2(n−1)²/n²).
     - c_W(r) = N_tot/6 + κ_X r assigns entropy to X in a presentation with r ≠ 0.
   - **Reason:** this is not a contradiction of L177, which is explicitly scoped "for the replica of the first paragraph". The proposal is correct that the sentence stays true as written. Without a clause, a reader could take the new block to falsify it. I do not flag PRIOR-CLAIM-ERROR.
   - **Required action:** add one sentence to the block. Suggested wording: "'Contributes no entropy' in the normalisation paragraph refers to the fixed-state replica, or equivalently to the presentation r = 0; a Wald-type coefficient of ρ²X is presentation dependent (below)." Also state in the dragging paragraph that the singular-ρ family is the second reading of the "Which geometry carries the cone" paragraph (L172).

3. **Minor. Location:** the Noether paragraph.
   - **Finding:** "R" is ambiguous. The torsion identity R = −𝒯 − 2∇·V is for R[G], while the density uses ρR[g_ρ] and the ledger identity uses ρR[g_ρ]. The values r = −2, 1, 4 are checked in s1 for the stated presentations.
   - **Required action:** add a clause saying that R denotes R[G] with √G = ρ², and that the presentations differ from ρR[g_ρ] by V² and total-derivative terms, which are kept in the remainder. Make the "R-free remainder" language precise accordingly.

4. **Minor. Location:** the first paragraph of the block ("Write the entropy of a sector as … and σ…").
   - **Finding:** the sign convention σ and the holonomy α_v = 1 are asserted. α_v = 1 is fixed by c_a = 1 from the cone angle, not derived from the matrix state, and the block says so only in passing.
   - **Required action:** none beyond keeping the existing closing sentence listing the holonomy and replica as not derived. The block already does this.

5. **Minor (confirmed).**
   - The Foster/Einstein-aether analogy is structural only. The block says "this is the form of the obstruction for the unit vector… a compensating rotation exists but is rigid". It does not claim the entropy is unidentified for NAMCG.
   - The 037 block's phrase "the gap … is not addressed" remains true of 037's own scope, so it is not stale. If desired, the integrator may leave it unchanged.

## Scope of what is established
- **Established (exact or high-precision computation, given the ledger inputs c_A, c_T, the family, the less singular Dirac extension and the first-order additive rule):**
  - the residue table;
  - the twisted-cone constant and the holonomy contact;
  - the torsion algebra and presentation coefficients;
  - joint-versus-pure Lie derivative;
  - the pure-diffeo charge Q ∝ ξ, which vanishes on Σ;
  - the singularity of the replica family;
  - the TEGR null direction (numerical, d = 3).
- **Conditional:**
  - everything on entropy of ρ²X, which uses the Iyer–Wald structure for the coframe presentation;
  - the additive rule for the combined E_δ + holonomy row;
  - the Dirac holonomy zero.
- **Not established:**
  - the replica, state and holonomy from the matrix model;
  - the first law with the rigid compensating rotation;
  - the exact singular-cone spectrum with holonomy;
  - the constraint-term charge;
  - any statement beyond the abstracts of the four uncited papers.
- **Classification:** PROGRAMME-CONDITIONAL. Problems B and A stay OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No label change.
- **No-go class:** at the 031 hypotheses (Poisson limit, Euclidean section, one loop, α = 1, Λ² term, totally geodesic Σ, first order in 1−n, the f-family, the additive rule). It does not say G_T ≠ G_A in general.
- **Open avenues, ranked by what I judge most promising for the infrared / full-GR derivation:**
  1. The local-frame-rotation link with Problem D. This decides whether the Lorentz-violating class [X] is forced or suppressed by Lorentz locking. It would make the Noether coefficient unique and could turn the Noether route from indeterminacy into a prediction or a match.
  2. The first law with the rigid compensating rotation. This is a relaxation of the hypothesis L_ξφ = 0.
  3. The replica from the modular flow (Problem A), including α_v and the n > 1 branch.
  4. The exact singular-cone spectrum, to test the additive rule.
  5. The constraint-term charge (B-R3).
  6. Fermion and edge-mode contacts, and a second circulation with a regular Σ metric.

## Recommended disposition
Revise, then integrate. Apply findings 1–3 to `appH_insert.tex` and to the proposal's wording. The integrator then inserts the block before `\section{Problem C…}`, with CRLF. The revision needs no new mathematics.

## Breakthrough assessment
Not a breakthrough. The proposal is a bounded obstruction plus an indeterminacy statement. It derives no critical-path step from the matrix theory, warrants no label change, and does not materially change what the derivation can achieve. It does usefully relocate the missing ingredient to the local-frame-rotation question (D), which is conditional and derives nothing about the matrix state. No milestone trigger.

Significance is adequate for one consolidated package: all claims share the 031 setting and the same ledger inputs.

## Corrected snippet
Replace the final paragraph's sentence beginning "None of the contacts above…" with the following. This needs no new assumption.

```
None of the contacts above (E-type, \(-\alpha_v\sigma\) with \(\alpha_v=1\), zero for Dirac) supplies the required \(-4\kappa_X\) of \(c\): the available vector contact has modulus \(1\) and the \(E_\delta\) contact depends on \(N_s\). The Noether coefficient is not obstructed but undetermined: the density fixes no value of \(r\), the value \(r=-4\) would match and is selected only by the match, and the value \(r=-2\) of the paragraph on the torsion invariant leaves \(2\kappa_X\). It stays undetermined until the frame is dragged by a flow whose internal part is a local symmetry, that is until the question of local frame rotations (Problem~D) is settled.
```

Add after the table's discussion, as the scoping sentence for finding 2:

```
The statement of the normalisation paragraph that \(\rho^2X\) contributes no entropy refers to the fixed-state replica, with \(\rho\) regular, or equivalently to the presentation \(r=0\) below; a Wald-type coefficient of \(\rho^2X\) is presentation dependent.
```

For finding 3, in the Noether paragraph state that \(R\) denotes \(R[G]\), with \(\sqrt{G}=\rho^2\).
