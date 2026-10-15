VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 (narrow, bounded; not a breakthrough) | FLAGS: none | PROGRESS: first | OPEN: 0/0

## Verdict
The mathematics holds: the background and gauge-invariance identities, the leading-symbol Maxwell structure and the bounded order-mismatch no-go all reproduce. Two small wording corrections are required: a "constant multiple" qualifier, and the small-q crossover sentence against the |q|ℓ≫1 window.

## Source reading
Digest + targeted reads. The digest was reported CURRENT; I did not re-run the check. This is not a full scan, which is not due at ordinal 14 and is not triggered, since no definition, scope or status text is edited.

I read in full:
- the proposal and `appH_insert.tex`;
- `ch03` lines 120-210 (`eq:Smatrix`) and 470-490;
- appH lines 350-361, 1100-1112 and 1831-1871 (the 011, 013 and "Why y^μ" paragraphs, plus the anchor);
- `MILESTONE.md`;
- the `.out` files of the 014 scripts.

I did not re-read Chapter 17 or `reports/ledger.md` this round. I relied on the proposal's quotation of the Chapter 17 criterion, and the Appendix H Problem F label I read directly. I did not read other chapters' mentions of the background.

## Claim under review
Target: Problem F (primary), with A, D1, E and N by dependency. These are the dynamics of the 12 first-harmonic amplitudes in the CP^{1,2} class and whether an Einstein-type equation follows at tree level.

Appendix H, Problem F, verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."

The proposal derives nothing on the critical path and proposes no label change.

## Checks performed

**Item 1: background and gauge invariance (direct).**
- I re-derived the field equation by hand. For S=(1/4g²)∫{X^a,X^b}{X_a,X_b}, using ∫{f,g}h=∫f{g,h}, the variation is δS=(1/g²)∫δX^a[−{X^b,{X_b,X_a}}+μ²X_a]. At X=T this gives (3+μ²)T_a, so stationarity needs μ²=−3.
- The sign step from −(1/4g²)Tr[X,X]² with [,]→i{,} to +(1/4g²)∫{,}{,} is correct.
- I re-ran `check_poisson_algebra_s2.py` for s=±1. The checks (1) {T_a,{T^a,T^b}}=−3T^b, (4) [D^a,D^b]=sJ^{ab}, (2) the closed form of L, and (3) L({Λ,T})=0 iff μ²=−3 (fails for 0 and 1) all give True. The script uses η6=diag(−,+,+,+,+,−).
- Merged 013 already records "□T^μ=−3T^μ/R²" for the scalar operator. The new identity is the same fact applied to the field equation.
- `eq:Smatrix` (ch03:143) contains only the quartic term, the cubic C term and S_matter. There is no mass term and no eq:V. A constant C contributes C_{abc}{X^b,X^c}∝C_{abc}M^{bc}. This is linearly independent of M_{a4} on the orbit (the orbit spans the dual because the adjoint of the simple algebra is irreducible). The argument is sound and not separately scripted, which the proposal says.
- A mass term Tr X² preserves the unitary-conjugation gauge symmetry of appH:353. It breaks only translation shifts of X, and the proposal does not rely on those.

**Item 1: no prior-claim error.**
- I grepped ch03 and appH. Merged 011 text says "off-shell backgrounds" (appH:1846).
- Merged 013 text says "does not derive the background".
- ch03:477 says the Moyal-Weyl background is a solution because its commutators are central. That is a different background and is unaffected.
- No merged text asserts that CP^{1,2} solves `eq:Smatrix`. So this is a new conditional input and a sharpening, not a PRIOR-CLAIM-ERROR. The proposal's own milestone self-assessment (trigger 3 does not apply) is correct.

**Item 1: structural change.**
- The μ² term is recorded as a class input and is not adopted into `eq:Smatrix`. It is not a structural change to the core.
- It is emergence-neutral. It makes no metric or spacetime fundamental, and it only stabilises a background of the matrix variables.
- No AUTHOR-DECISION is needed. If it were ever adopted into the core, that would be a separate structural proposal.
- The insert states explicitly that "The bilinear term is not part of (eq:Smatrix); it is an input of this class". This is the correct hedge.

**Item 2: leading symbol.**
- I re-derived S2~(m²/4g²)∫F². At leading order D^a=s m∂^a and L→−m²(∂²c_a−∂_a∂·c). The cross terms between D acting on c and D acting on the fibre function are of relative order 1/(|q|ℓ). So the form is pointwise on the fibre, diagonal in fibre harmonics, and massless at this order.
- The numerical check (`check_leading_symbol_numeric`) shows the remainder falling as 1/λ (7.6e-3 at λ=10 to 7.6e-5 at λ=1000). I read the output only; I did not re-run it. This is a check, not a proof, and the derivative counting is the proof.
- For the level-1 sector, the Gram matrix of the S_i is diag(25/8,…), so they are orthogonal with equal norm. The kinetic matrix is δ_ij, so the 12 amplitudes are 3 Maxwell fields with no relative ghost.
- The sign is stated honestly: the overall sign is common and opposite to −¼F² in η, and this is convention-dependent. This is consistent with the displayed sign of `eq:Smatrix`.
- κ>0 and SU(2)_R invariance are inherited from 013 (numerical).

**Item 3: no-go.** I re-ran `check_maxwell_factorisation.py` (about 2 s). Its output is identical to the saved `.out` file.
- All 10 entries of E[h(c)] are non-divisible by q².
- The 480-unknown linear solve for a polynomial P with E H = P M is inconsistent.
- The identity Q=q_⊥²P_⊥−q_⊥q_⊥ᵀ holds.
- The closed form of the sourced response matches exact-rational evaluation in 3 random trials.
- For null q, the rank of c→E[h] is 1.
- `check_null_wave_content.out` gives the identity E[h]=½qq tr h, a 6-dimensional image in h, 3 modulo diffeos, a kernel of H on Lorenz solutions of dimension 3, and the TT polarisations in the image. This is consistent with the 013 split 12=3+3+6.

My own derivation agrees:
- With a source J_i∝s_i^μT_{μν}, which is conserved because of q·T=0, c=J/q².
- h=(N/q²)(QT+TQ) is homogeneous of degree 0, because s_i is linear in q.
- E[h] is therefore homogeneous of degree 2. It cannot equal a constant multiple of T, and the printed trials show it is also not q²T.

Hypothesis class: the proposal states the bounds explicitly and consistently as Poisson limit, leaf CP^{1,2}, leading symbol, frozen coefficients, tree level, level-1 sector, conserved source coupled through h, sheet y⁴>0, and four matrices only. The closing paragraph names the induced term, subleading orders, other sectors and `ass:EE` as not excluded. It does not over-read as "matrix models cannot give Einstein equations". The hypotheses a within-core route could relax are:
- tree level, via the induced term (R1);
- leading symbol, via subleading masses and connection terms (R2);
- the class, via the doubleton constraints and other sectors (R3, R4);
- the source coupling being an input, not derived.

**Citations.**
- I fetched arXiv:1901.03522. The abstract says "This provides a background solution of the IKKT matrix model with mass term". The text's "a mass term is reported for the covariant backgrounds of SperlingSteinacker2019" is therefore supported at abstract level.
- I fetched arXiv:2303.08012. Its abstract says "The 3+1-dimensional Einstein-Hilbert action then arises in the one loop effective action". "Reported to arise at one loop" is supported.
- Both bib keys exist. The attribution is abstract-level only, and the proposal states that §6.3 of 1901.03522 was not read. No other Steinacker result is imported into the manuscript text.
- The additional comparison items (2025, 2019 NoGhost, 2016) are not used in the text. I did not verify them.

**Anchor, labels, LaTeX.**
- `\section{Problem G: HBEV}` occurs once, at line 1871, immediately after the 013 "Why y^μ" paragraph. I verified this.
- The only labels used are `eq:Smatrix`, `ch:vierbein-emergence` and `ass:EE`, all pre-existing. There are no new labels.
- The fenced block is identical to `appH_insert.tex` (diff empty).
- There is no process language.
- The first paragraph carries no status sentence. The second closes once with "This changes no ledger label; Problem F remains open."
- I did not run the build. The proposal reports a scratch build with 258 pages and 0 undefined references.

## Findings

1. **Minor (required).** Location: the "Response to a source" paragraph, last sentences. The text says E[h] "cannot equal a multiple of T". Strictly, E[h] has degree 2 and could only be proportional to q²T, which would be −□T, a higher-derivative relation. The degree argument excludes a constant multiple.
   Required action: write "cannot equal a constant multiple of T" and, in a clause, note that it is also not q²T (the scripted check (d) shows this for the sampled T).

2. **Minor (required).** Location: the "Induced term" paragraph. The leading-symbol class requires |q|ℓ≫1. "The tree-level form dominates at small q" and "above the scale set by the ratio of the two coefficients" are meaningful only if that crossover lies inside the window.
   Required action: add a clause such as "provided the crossover lies within |q|ℓ≫1; otherwise the induced form is subdominant throughout the regime of the class".

3. **Minor (not required).** The no-ghost statement is limited to the common overall sign of the quartic form. The proposal already says so, and nothing more is needed.

## Scope of what is established

Within the Poisson limit, leaf CP^{1,2}, X=T+A, the leading symbol in 1/(|q|ℓ), frozen coefficients, tree level, and sheet y⁴>0:

**Established (Poisson-algebra identities and derivative counting, exact or checked):**
- T is not stationary for the quartic term alone.
- With a bilinear term of coefficient μ²=−3/R² the background is stationary, and the amplitude action is exactly gauge invariant at quadratic order.
- The leading symbol is pointwise Maxwell and harmonic-diagonal, so the 12 level-1 amplitudes are 3 Maxwell fields with colour metric δ_ij and no mass at this order.
- Bounded no-go: no local relation E[h]=P(∂)J follows from the Maxwell equations, because E[h(c)] is cubic in q and the Maxwell operator is quadratic. The response to a conserved source is algebraic and of degree 0, so E[h]≠κT. For null q one polarisation violates the vacuum equation, with E[h]=½qq tr h.

**Conditional or input:**
- The bilinear term, the conserved-source coupling through h, and the 013 fibre-geometry results (numerical).
- The induced Einstein-Hilbert term (item 4 of the proposal) is an input only.

**Not derived:** masses, subleading terms, G_eff, any Einstein-type equation, or the identification of G with the emergent metric.

Status is unchanged: F and the other critical-path problems stay OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. This is not DERIVED, and no label change is proposed.

**Milestone and breakthrough.**
- Trigger 2 (a bounded no-go) applies only narrowly. It rules out the tree-level, leading-symbol Einstein-type route in this specific class. 013 already left open "an induced term or another structure", so this sharpens the existing position and does not remove a broadly open route. I judge it M2 in the narrow sense. The orchestrator may treat it as routine if it prefers.
- Trigger 3 does not apply (see above).
- Triggers 1, 4 and 5 do not apply.
- This is NOT a BREAKTHROUGH: no critical-path step is derived, and the no-go is bounded by H_dyn.

**Reading of merged 011/013 text.** No correction is needed. The new text consistently refines their "off-shell" and "does not derive the background" caveats. The only stale-risk is the 013 parenthetical "(no such action is computed in this class)". The new first paragraph supersedes it, and the proposal's treatment of it is adequate.

## Recommended disposition
Revise the two sentences in findings 1 and 2, then integrate. Nothing else needs to change.

## Corrected snippet
These need no new physics.

In the "Response to a source" paragraph, replace "it therefore cannot equal a multiple of \(T\)" with "it therefore cannot equal a constant multiple of \(T\) (the sampled cases also exclude \(q^2T\))".

In the "Induced term" paragraph, append after "...set by the ratio of the two coefficients": ", provided that scale lies within \(|q|\ell\gg1\); otherwise the induced form is subdominant throughout the regime of the class".

The 014 proposal files are in `C:\Users\redgi\Projects\namcg-lab\proposals\014-level1-dynamics\`. The insertion anchor is `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex`, line 1871.
