VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The computations are correct (I re-derived the key identities and re-ran the scripts). The inserted text overstates the Weyl-coefficient test as "not depending on the choice of independent variables" and leaves the inherited hypotheses and the status of the Dirac "periodic" row too implicit, so it needs the wording changes below before integration.

## Source reading
- **Full scan.** Every `chapters/**/*.tex` was read in full. The manifest is 30 files: `appA`–`appL` (12) and `ch01`–`ch18` (18). The scan was required by CLAUDE.md 3(a) (ordinal 30) and 3(d) (digest STALE).
- **Chapter state.** `git status` showed no uncommitted `chapters/` or `bib/` changes at review time. The 025–031 text is therefore in the files I read.
- **Not read.** No unreadable files. I did not read the tail of `proposals/031`; I read the ledger entry for 031 and the merged 029–031 text in appH.
- **Also read:** the full proposal, `appH_insert.tex`, and all scripts and outputs I relied on.

## Claim under review
- **Claim.** Content dependence of the log-order comparison off (N_s,n_D)=(6,2): closed forms for σ_per, σ_cmp, σ_fs, the Dirac lemma, the rotation-invariant SD family, the T-side a_2, and the Weyl-coefficient plane-wave test. The gaps are 4−2n_D (periodic), 4−n_D (fixed-state) and 2−n_D (completed).
- **Original target.** Problem B (area term / G relation; tensor-block stationarity). Nothing here closes it.
- **Appendix H, Problem B, verbatim.** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- **Appendix H, Problem A, verbatim.** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. … claims no derivation from the matrix model."
- **Appendix H, Problem F (the induced-action side), verbatim.** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL."
- **Chapter 17 critical set (`sec:ch17-done`).** A, B, C, D1, E, F, G-derived, N. No label change is proposed and none is warranted.

## Checks performed
**Anchor and characters (verified).**
- The anchor "Problem~B stays open and PROGRAMME-CONDITIONAL." occurs once in the working tree, on line 254. `\section{Problem C: conformal mode and Cassini}` is on line 256, so the block goes in between.
- `appH_insert.tex` has 0 TAB, 0 CR and no control or non-ASCII characters. It has balanced braces and 93/93 `\(`…`\)`.
- It is LF; the integrator must convert it to CRLF, as appH has 2677 CRLF and 0 TAB.
- No new `\label` or `\ref`. `\LUV` is defined in `namcg-book7.tex`. `Solodukhin2011` exists in `bib/namcg.bib` and arXiv 1104.3712 matches (Living Rev. Relativity 14 (2011) 8, "Entanglement entropy of black holes"; fetched).
- The closing status sentence appears once inside the block.

**Closed forms for general (N_s,n_D) — re-derived independently by hand and confirmed by script.**
- **Sector sums.** Σ w tr 1 = N_tot, and ā_1 = N_tot(R/6−e) + κ_X X′. The vector gives 4(R/6−e)+X′; a Dirac field gives 4(R/6−e)+X′/2.
- **Wald rule against eq. (70).** I decomposed the scalar a_2 = (1/180)(Riem²−Ric²+5/2R²) into (kC, kE, kR) = (1/120, −1/360, 1/72). The rule "entropy density = 12(kC W + kE R_Σ + kR R)" then gives R/6 − (R_Σ−3W)/30, which is exactly the scalar eq. (70) value. The −5 : 1 ratio of the R and (R_ii−2R_ijij) coefficients also checks. The cross-term normalisation is therefore not fitted.
- **Contacts = −(3/2)ā_1 + κ_X τ_Ω.** A uniform E_δ gives a cross term ∝ tr(E_G+R/6)·E_δ = −π a_1 per unit (1−n). With 24π/(16π²) this is exactly −(3/2) a_1. The vector Ω_δ contact is τ, and the Dirac one is −τ/2 per field, so the sum is κ_X τ.
- **Dirac lemma.** D−D_per = (3/2)(4R/6−trE_f) − τ/2, which equals the FS cross term R − (3/2)trE_f − τ/2. This is an exact identity, given the Z_n weights (−1/2, 1, 1/2) inherited from 029/031. The nontrivial content is that those independently obtained weights agree with the universal cross term.
- **Rotation-invariant SD family.** With e=R/6, W=0, X′=3g/2 and τ=R_Σ+3g/4: σ_cmp = κ_X R_Σ − (N_tot/30)R_Σ = (28−N_s−11n_D)/30 · R_Σ, with the g-dependence cancelling. This rests on the 18-point exact identities of 029/031, which are not proved. The proposal classifies this correctly as "numerical-exact, 11 points".
- **T side.** On chiral points, tr_D of any polynomial in su(2)_L generators equals ½ tr_V, so d′ = v′/2 holds exactly. The 15 points and the stated line "vanishes on these backgrounds only for N_tot=κ_X=0" check out. The ratio s/v′ varies across backgrounds, so the line statement is right.

**Scripts re-run in the proposal folder.** Output went to scratch and was compared with the saved outputs:
- `content_scan.py`: identical, 0 nonzero checks over 20 points.
- `dirac_lemma_symbolic.py`: D−D_per−contact = 0.
- `tt_gap.py`: identical; gaps 4−2n_D, 4−n_D, 2−n_D, independent of N_s, for SD and ASD.
- `quad_check.py`: identical; (v−4s)/ε² = (1/12)trΩ²/ε² and (d−4s)/(v−4s) = 0.5 at two seeds.
- The pickle rank (`omega_riemann_full.pkl`) is 20 / 33 / 33 (dR / dΩ / joint).
- Not re-run: `lin_test.py`, `tt_test.py`, the heavy jet scripts (I used the saved outputs).

**Independent check of the central Weyl-test inputs (my own code, scratchpad, no imports from the proposal).**
- Setup: ω = ω̄ + ε dα with ω̄ = η³ (and the ASD analogue), δρ=0 imposed by tr(Θ̄Δ)=0, G = ωωᵀ, b_σ = G_{στ}Θ^{ρτ}∂_ρΘ, linearised Riemann, phase-averaged.
- tr Ω² / C² = −4.000000 on random modes for both chiralities, against the Levi-Civita value −Riem²/C² = −2.000000. Euler averages to 0 and R = 0.
- tr(JΩ_12) = −R_ijij with ratio 1.000000 on 12 random modes.
- This confirms κ_J = −1/3 and τ^(1) = −R_ijij, so the gap arithmetic α_W − 12κ_C^T follows.

**Consistency of the gaps with the merged Λ² gaps.**
- Periodic: 4−2n_D = c_A−c_T (appH line 189). Fixed state: 4−n_D (line 189 and 196). Both match.
- Completed: the proposal's table lists −N_tot/4 + 4κ_X, which is the smooth-replica Λ² gap, as the comparison column. That is not equal to 2−n_D, and the insert correctly does not claim equality.
- Structurally, gap_fs = n_D + 4b is exactly the "weight of ρ²X plus the Lichnerowicz +1 per Dirac" decomposition of line 196.

**Prior-text consistency.**
- At (6,2): σ_per = 0 (as in 031), σ_cmp = 0 on the SD family (as in 031), and σ_fs = (3/2)g − R_Σ (as in 029 and line 250). The completed Weyl gap is 0 at n_D=2, in line with the 031 "equality of vanishing coefficients". The fixed-state gap is 2 there, as at Λ².
- **PRIOR-CLAIM-ERROR: none.** The block adds context to 029–031 and contradicts no merged sentence.

**Not verified.** I did not re-derive the 029/031 inputs themselves (the Z_n weights, Dirac a=11/360, the delta content on the Θ¹²=1/f family). I used them as stated.

## Findings

**F1 — major — insert, first sentence of "Weyl coefficient on plane waves"; proposal Result item 5 and "Decisions Taken".**
- **Finding.** "A comparison that does not depend on the choice of independent variables" overstates the result. The T-side quadratic form on these modes is unambiguous. The comparison with the area side is not variable-independent.
- **Reason.** On the δρ=0 modes the endomorphism data (R^(1), e^(1), X′^(1), ā_1^(1)) vanish at first order. So the Q=0 versus Q=1/4 (G,ρ,∂Θ) versus (G,torsion) contact ambiguity of 024/031 drops out. That is a property of the chosen modes. It is not general variable independence.
- The coefficient κ_C^T multiplies C² only because every quadratic invariant collapses to ∝C² on these modes. The assignment of entropy 12κ_C^T·W to the whole form uses the cross-term (Wald) rule for a metric Weyl-squared term. Any part of the form carried by non-metric invariants of Θ (torsion-squared, the excess of tr Ω² over the Levi-Civita value) gets no such assignment from the rule. Here that excess is exactly the 2κ_X gap, so the (G, torsion) issue is present in the result, not absent from it.
- The rows also depend on the replica prescription, the Dirac gluing and delta universality.
- The researcher's own "Remaining open step" (variable-independent Iyer–Wald/Dong entropy) concedes this.
- **Required action.** Replace the phrase as in the corrected snippet (a). Say the test is insensitive to the endomorphism-contact ambiguity because the a_1-type data vanish on these modes, and state that the entropy assignment to non-metric parts of the form is not fixed by the rule. Strike "variable-independent" from the proposal's framing. This is not a retraction of any merged sentence.

**F2 — major — insert, closing paragraph (hypothesis list and hedging); proposal Result item 5, rows 1 and 3.**
- **Finding.** Inherited hypotheses are referenced ("the delta content of the preceding paragraph, with the hypotheses stated there") but not enumerated.
  - **Dirac hybrid not named.** The fixed-state replica is not the trace of the n-th power of one state. In the periodic row the Dirac gluing is the unrotated periodic gluing, which 029 states "is not Tr ρⁿ" (it is the graded trace for even n). The periodic gap 4−2n_D is therefore a formal replica result for n_D≠0.
  - **Uniform E_δ not named.** Uniform E_δ on every component, including Dirac, is not named as an assumption.
  - **Proper-time limit omitted.** "One common proper-time limit" is missing from the closing list. It matters for the ln Λ coefficient.
  - **No formal-parameter hedge.** Nothing says that (N_s,n_D) ≠ (6,2) are formal parameters of the computation and not proposed matrix-model contents. The sentence about the "line n_D=2 for every N_s" could be read as suggesting candidate contents.
- **Required action.** Add the hypotheses and the hedge as in snippet (c). Keep "Problem~B stays open and PROGRAMME-CONDITIONAL."

**F3 — minor — insert, "The completed gap is 2κ_X: … 33 independent components …".**
- **Finding.** The rank count (dΩ 33, dR 20, joint 33) is exact and correct. It shows Ω^v is not determined by Riemann: the joint rank equals rank dΩ, so R is a linear image of Ω but not conversely. It does not by itself explain or fix the value 2κ_X.
- **The sharper statement, fully verified.** tr Ω² = −4C², twice the Levi-Civita value −2C², while tr(JΩ_12) = −R_ijij has its Levi-Civita value. The Ω_δ cross term therefore captures half of the Ω² term's contribution to the coefficient of W. Algebraically, α_W(comp) = N_tot/10 − 2κ_X against 12κ_C^T = N_tot/10 − 4κ_X.
- **Required action.** Give the verified statement and keep the rank count as scoped supplementary evidence (snippet (b)). This also matches "Check that … 33-vs-20 statement stay scoped to the first jet fixed".

**F4 — minor — insert, assorted.**
- (i) τ_Ω is used in the first display and defined only by "as above" after it. Say "τ_Ω of the preceding paragraphs".
- (ii) "it vanishes on these backgrounds only for N_tot=κ_X=0": write "vanishes on all these backgrounds simultaneously only for". At a single point N_tot s + κ_X v′ = 0 has a one-parameter solution line.
- (iii) The sentence "The first two equal the differences c_A−c_T at order Λ²" is correct. Add that the completed gap has no Λ² counterpart of the same form.
- (iv) The 20 points "J≠0 radial profiles and generic closed ω, for the last only as algebraic identities". State that the closed-form checks at the J≠0 and generic points are algebraic identities (pointwise, Σ not necessarily totally geodesic) and that the rotation-invariant closed form rests on 11 points.

## Scope of what is established

**Proved or exact, given inherited inputs.**
- The closed forms for σ_per, σ_cmp, σ_fs and the contact identity −(3/2)ā_1 + κ_X τ_Ω. These follow from the per-component formulas, the Z_n Dirac weights and the cross-term rule.
- The symbolic Dirac lemma.
- The T-side decomposition a_2^tot = N_tot s + κ_X v′ on chiral points.
- The second-order identities v−4s = (1/12)trΩ² and d−4s = ½(v−4s) (exact at the sampled cubic potentials, and consistent with the analytic argument that X_mat is second order).
- κ_J = −1/3 and τ^(1) = −R_ijij on δρ=0 modes about constant (A)SD Θ̄.
- The gap arithmetic 4−2n_D, 4−n_D, 2−n_D, independent of N_s.

**Numerical-exact, not proved.**
- The rotation-invariant SD closed form (28−N_s−11n_D)/30 · R_Σ (11 points, resting on the unproved 029/031 identities).
- d′ = v′/2 on the J=0 non-SD points (it holds exactly whenever b is chirally valued).
- The rank 33 versus 20.

**Conditional on inherited hypotheses.**
- The imported prescription S_BH = S_ent − Q, delta universality (E_δ uniform on every component, Ω_δ = 2π(1−n)J δ_Σ, from the family Θ¹²=1/f), the Dirac hybrid replica (antiperiodic Dirac with pulled-back bosons; the periodic row is the graded-trace Dirac gluing), the n<1 branch, first order in 1−n, a totally geodesic Σ, one common proper-time limit, α=1, Yukawas dropped, Poisson limit, one loop, and constant (A)SD Θ̄ with δρ=0 modes and the W coefficient only.

**Interpretation.**
- It is a mismatch of c-type (Weyl) coefficients between the replica entropy and the induced-action quadratic form, for stated replicas, driven by the non-Riemannian part of the bundle curvature of the vector connection.
- It is not a statement about G_eff or the Einstein–Hilbert coefficient. The proposal states this, and the insert's closing sentence says "give no value or sign of G_eff".
- It is not G_T≠G_A: that is an Λ²-order notion, and the log-order test concerns a different coefficient.
- The pure-scalar sector reproduces the standard matching (gap 0 at b=0), so the machinery behaves correctly there.
- The vanishing of the periodic and completed gaps on n_D=2 is the N_tot × conformal-scalar counting and tests neither G nor the index-weighted sector.

**Labels.** Problem B stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. A, F and the other critical-path items are unchanged. No emergence issue arises: spacetime is not made fundamental.

**Significance.** This is a coherent bounded package. It gives the first nonvanishing log-order comparison, a clean general-content formula, and a second-order c-type test whose periodic and fixed-state gaps reproduce the Λ² gaps. The bundled claims share context, assumptions and scripts, and splitting is not needed. It is not a derivation of a critical-path step, not a decisive no-go, and not a breakthrough, so there is no BREAKTHROUGH flag.

**Open avenues after this mismatch, ranked by promise.**
1. Variable-independent entropy of the log induced action: Dong or Iyer–Wald with the vector connection b (or the coframe torsion) as an independent field, instead of the metric cross-term rule. This relaxes the "metric Wald assignment" hypothesis and decides whether the 2κ_X W term is the entropy of the non-metric part. This is the most promising avenue.
2. Common replica or state selection for both orders: test whether a single gluing (antiperiodic Dirac plus an Ω contact, selected by modular flow) closes the 4−n_D gaps at both Λ² and log order. They coincide, but only as a computed coincidence.
3. Direct smooth-cone log replica (exact Aharonov–Bohm heat trace, |1−n| non-analytic terms, n>1 branch). This relaxes first order in 1−n and delta universality.
4. Non-chiral Θ̄ and δρ≠0 modes. The generic-mode ratio trΩ²/(−Riem²) is not 2 (appH-independent data in `omega_vs_riem_ratio.out.txt`), so the structure of the gap must be rechecked off the (A)SD, δρ=0 slice. This also bears on the Euler coefficient via the global-coframe statement (E_4 = d(CS)), which is invisible to the quadratic form.
5. Content variation (extra vectors or KK towers shifting κ_X and N_tot independently). This is a formal exploration, not a prediction.
6. Non-geodesic Σ and edge content.

## Recommended disposition
Revise, then integrate: apply F1–F4 and the snippets below. The mathematics stands. After revision, a short r2 check of the new wording is enough.

## Corrected snippet
These are rewordings of existing statements only. They add no new physics and no new assumption.

(a) Replace the opening of the Weyl paragraph:
```
\emph{Weyl coefficient on plane waves.} A comparison that is not affected by the choice between the variables \((G,\rho,\partial\Theta)\) and \((G,\text{torsion})\) for the endomorphism contacts is the coefficient of \(C^2\), because \(R\), \(e\), \(X'\) and \(\bar a_1\) vanish to first order on the modes with \(\delta\rho=0\) about a constant self-dual or anti-self-dual \(\bar\Theta\). It is read from the quadratic form of the weighted \(a_2\) on those modes, against the coefficient of the Weyl projection \(W\) in the first-order area-side density, where a metric functional \(\kappa_CC^2+\kappa_E\mathcal E_4+\kappa_RR^2\) is assigned the entropy density \(12\kappa_CW+12\kappa_ER_\Sigma+12\kappa_RR\) by the cross-term rule. The rule does not fix the entropy of a part of the quadratic form carried by non-metric invariants of \(\Theta\); that part is the gap below.
```
(b) Replace the sentence beginning "The completed gap is \(2\kappa_X\)":
```
The completed gap is \(2\kappa_X\). On these modes \(\operatorname{tr}\Omega^2=-4C^2\) is twice its Levi-Civita value \(-2C^2\), whereas \(\operatorname{tr}(\mathcal J\Omega_{12})=-R_{ijij}\) has its Levi-Civita value, so that the cross term with \(\Omega_\delta\) accounts for half of the contribution of the \(\Omega^2\) term to the coefficient of \(W\). The bundle curvature \(\Omega^v\) is not determined by the Riemann tensor: at fixed first jet its second jet has 33 independent components against the 20 of the Riemann tensor (45 random second jets, exact rank), and the Riemann second jet is a linear image of that of \(\Omega^v\).
```
(c) Add to the closing paragraph (before "They use the Dirac weights …"):
```
The contents \((N_s,n_D)\neq(6,2)\) are parameters of the computation and are not proposed field contents of the matrix model. The replicas are the hybrid fixed-state replica, whose Dirac fields have the antiperiodic gluing and are not the trace of the \(n\)-th power of one state, the periodic replica, whose Dirac fields have the unrotated periodic gluing (the graded trace), and the replica completed by the uniform \(E_\delta\) and by \(\Omega_\delta\) on every component, with one common proper-time limit for all sectors.
```
(d) In the first display paragraph, replace "and \(\tau_\Omega\) as above" with "and \(\tau_\Omega\) as in the preceding paragraphs". Replace "it vanishes on these backgrounds only for" with "it vanishes on all these backgrounds only for".

Relevant paths:
- C:\Users\redgi\Projects\namcg-lab\proposals\033-log-content-scan\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\proposals\033-log-content-scan\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (anchor line 254; next section line 256)
- My independent check: C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\4d0177a0-6b3d-45ad-bb6d-645d2be99f00\scratchpad\indep_check.py
