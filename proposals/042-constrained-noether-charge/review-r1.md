VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/4

## Verdict
The core of proposal 042 r1 is sound: the covariantisation, the Lie-dragging in (γ, ω), the zero-charge lemma for first-order densities, the R_W identity and the compensation identity all check out. The insert as written overstates two sentences, leaves the 037/038 "not computed" statements stale, and leaves "first law" ambiguous between the Iyer–Wald identity and Eq. (first-law). Four wording fixes are required; no new mathematics is needed.

## Source reading
**Full scan** (CLAUDE.md 3(a): would be integration ordinal 40; 3(d): tree dirty with the uncommitted accepted 041 integration). `make_digest.py --check` printed DIGEST STALE (head changed), so I did not rely on the digest.
- I read in full every file of the current manifest, 30 files in `chapters/`.
  - Chapters: ch01 through ch18 (18 files).
  - Appendices: appA, appB, appC, appD, appE, appF, appG, appH (lines 1–2841, working tree), appI, appJ, appK, appL (12 files).
- No file was unreadable.
- I also read `appH_insert.tex`, `proposal-r1.md`, the SME-independent parts of `MILESTONE.md`, and the ledger tail.
- I did not re-read the prior review files. I took their content from the ledger entries and from the merged text.

**Chapter 17 versus Appendix H.** I found no discrepancy in status, priority or completion for A, B, C, D, E, F, G, H, I, J or N. The critical-path set in `sec:ch17-done` is A, B, C, D1, E, F, G-derived, N, as stated.

Verbatim current labels for the problems the proposal touches:
- **Problem B** (Appendix H): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived." Chapter 17: "CRITICAL PATH; OPEN. The fixed-algebra first-law identity is established, but not the required stationarity."
- **Problem D** (Appendix H): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- **Problem A** (Appendix H): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. The matrix-to-modular map remains unproved. A scope-limited Presentation-B model may retain Assumption~dictionary and claims no derivation from the matrix model."

**Merged sentences that are false.** I found none, so there is no PRIOR-CLAIM-ERROR. Two kinds of problem remain:
- Stale-but-true statements (see F3): "the charge of the constraint term … is not computed" occurs three times in appH:
  - the comparator paragraph: "…the charge of the constraint term is not computed";
  - the scope list of that paragraph: "…the charge of the constraint term of the composite connection…";
  - the order-Λ² paragraph: "The charge of the constraint term of the composite connection is not needed for this dependence … but it is not computed."
- Pre-existing hard-coded numbers, unrelated to 042:
  - ch16: "Theorems~7.3--12.4", "Theorem~7.3", "Appendix~D";
  - appE: "Theorem~7.3", "Assumption~E.1".
  CLAUDE.md says never to hard-code chapter numbers. These need a separate cleanup and are not a 042 matter.

## Claim under review
- **Claim (conditional, bounded indeterminacy).** This is for the Poisson limit, four coordinates, n_D=0, the LUV² density, and backgrounds Lie-dragged by the joint flow.
  - With γ=X*η, the invariants are chart-covariant in (γ, ω).
  - For every real r, L_r = L_0 + rκ_X√G R_W equals L_0 on the class, yet has Σ-charge coefficient c_W(r).
  - The f·Riem(γ) shift of the Σ-charge is compensated by an identically conserved improvement of the η-stress.
  - So the Iyer–Wald identity for the induced density does not select r.
  - The residue c_A−c_T is therefore an edge term, a property of the modular Hamiltonian (A) or of a local compensating symmetry (D1), not of the density.
- **Original target.** Problem B, sub-target "tensor-versus-area normalisation, c_A vs c_T" (the 041 avenue: Wald/Noether charge of the constrained class). The target is not derived. B stays `Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL`.

## Checks performed
**Anchor and mechanics** (direct, Python byte-level):
- `\section{Problem C: conformal mode and Cassini}` occurs exactly once, immediately after "…Problems~B and~D remain open and PROGRAMME-CONDITIONAL.\n\n".
- The title "Covariant variables, the joint flow" occurs 0 times.
- Insert: 7854 bytes, 0 CR, 0 TAB, 0 non-ASCII, 0 control bytes other than LF.
- Braces net 0, `\(`/`\)` net 0, one `\[ … \]` pair, final LF present.
- `eq:Top-FP` is defined exactly once (ch07). IyerWald1994 and JacobsonKangMyers1994 each occur once in `bib/namcg.bib`. `\LUV` is defined at `namcg-book7.tex:54`.
- No process language found, and there is a single closing status sentence ("Problems~B and~D remain open and PROGRAMME-CONDITIONAL.").
- `compile_check.out.txt` reports 0 undefined references/citations/duplicate labels. I did not re-run pdflatex; I take that as the proposal's evidence.

**Scripts re-run by me:**
- **s1** (about 2 min): exact rational zero difference for all six invariants in both signatures, and R_G+𝒯+2∇V−R_W=0 exactly at 3 non-flat γ per signature, with R_W≠0. This supports the covariance and the Weitzenböck identity at the sampled jets only.
- **s2**: tensorial L_ξω=0 for the span and the cone family, [e,B]=0 at Σ, and failure for generic constant ω. L_ξX=BX≠0.
- **s3**: the Σ-charge densities agree to 1e-16 when [e,B]=0 and not otherwise.
  - This check is algebraically trivial: antisym(e⁻¹BeG⁻¹)=antisym(BG⁻¹) when [e,B]=0.
  - The condition [e,B]=0 is not an extra restriction. For a (1,1)-tensor at a zero of ξ one has (L_ξe)|_Σ=−[B,e], so it is equivalent to stationarity of e at Σ.
- **s4**: reproduces E=−2∂∂f and ∂_bQ^{ab}=2ξ_cE^{ac} in both signatures.

**My own analytic check of the compensation identity** (more general than the polynomial sampling):
- Take Killing ξ in flat space (∂∂ξ=0) and f with algebraic curvature symmetries.
- ∂_bQ^{ab} reduces to −2T₁−4T₂+2ξ_cE^{ac}, with T₁=∂_bf^{abcd}∂_cξ_d and T₂=∂_df^{abcd}∂_bξ_c.
- The first Bianchi identity plus antisymmetry of ∂_cξ_d gives T₂=−T₁/2, so the sum vanishes. The identity therefore holds for general smooth f, not only for the sampled polynomials.
- On Σ, Q^{ab}=−2f^{abcd}∂_cξ_d.

**Step 3a argument** (first-order densities have no Σ-charge mod exact forms): I re-derived it.
- For L(γ, ∂γ, ω, ∂ω), Θ contains no ∂δφ, so J has at most first derivatives of ξ.
- Therefore the coefficient of ∂_αξ^β in Q^{μν} has k^{μ(να)}=0.
- With antisymmetry in μν, k is totally antisymmetric in its upper indices, so k∂ξ=∂(kξ)−(∂k)ξ is exact plus terms ∝ξ.
- This is correct for closed Σ, or for Σ with fall-off.

**Curvature densities:** for √G ℓ(R), Q|_Σ=2P·B holds for any torsion-free connection, since ξ=0 on Σ. R_W depends on second derivatives only through Riem(γ), so its charge is P_W·B with P_W∝e⁻¹…e. This is correct.

**Not independently verified:**
- The Step 4(iii) example Y^{μν}=εZ… (argued in the proposal, not scripted).
- The Step 6 identification of the "H=𝒥" and "not tied" readings with Ω versus Ω−Riem(γ) (argued, not computed).
- The tensoriality of the composite b=F[Θ] under (γ, ω). s1a tests only the six scalar invariants.
- Literature: Iyer–Wald and Jacobson–Kang–Myers are in the bib and were verified by the 038 gatekeeper. I did not re-fetch them. Novelty of the f·Riem(γ) ambiguity statement against the literature is not checked, and no SME consultation is needed for the verdict.

## Findings

**F1 (major).** Location: insert, "Compensation" paragraph, the sentence beginning "The shift of the charge on Σ is therefore the boost charge…".
- Finding: the sentence is false as stated when f does not decay. The proposal itself notes the boundary term at infinity, but the insert omits it.
- Reason: for constant f one has E=0, so the boost charge of the improvement is zero. Yet Q^{ab}=−2f^{abcd}∂_cξ_d is a nonzero constant on Σ, and the whole Σ-charge is the flux at infinity. By Stokes on the Cauchy surface, ∫_C 2ξ_cE^{ac}dS_a=∮_ΣQ−∮_∞Q. Equality of "the shift" with the boost charge needs a compactly supported variation of f, or decay.
- Required action: restate for variations of f of compact support and keep the term at infinity (verbatim text below).

**F2 (major).** Location: insert, "Consequence", the sentence "For n_D=0 the equality c_A=c_T is the statement that the edge term…".
- Finding: c_A≠c_T as numbers. The merged value is c_A−c_T=4−n_D=4κ_X at n_D=0, and after the 039 dressing c_A−c_T^ext=2κ_X. What is true is that the requirement G_A=G_T holds iff the edge term accompanying the replica contributes −4κ_X in units of c. My numeric check of the proposal's values is consistent: c_W(−4)=c_T, c_W(−2)=c_T^ext, c_W(0)=c_A.
- Required action: reword (verbatim text below).

**F3 (major).** Location: the insert as a whole, against the three "not computed" statements listed above.
- Finding: the insert computes the multiplier-term charge, but only for the covariantised composite and only in this class. Left as is, the ledger reads "not computed" in three places and "no charge on Σ" in the new paragraph, with no supersession.
- Reason: this is stale text, not a false merged claim.
- Required action: make the sentence in the insert state the scope and the supersession (verbatim text below). I do not require edits to the old paragraphs.
- Scope note: tensoriality of b under (γ, ω) is asserted, not scripted. It follows from the same invariant-theory argument as the other invariants, with matrix indices converted by γ, so I accept it as a scoped statement but not as separately checked.

**F4 (major).** Location: insert, "Consequence", first sentence "Within these hypotheses the first law does not select r", and the final scope paragraph.
- Finding: the object treated is the Iyer–Wald identity for the induced density, with T_η the response to γ taken as a background field. It is not identified with T^op_{μν} of Eq. (first-law) in Chapters 6–7 (the metric response of the tensor block), and the insert does not say so. Without this, a reader will take the result as a statement about Eq. (first-law).
- Required action: clarify both places (verbatim text below).

**F5 (minor).** Location: insert, "Covariant variables".
- Finding: ρ=|Pf ω|/√|det γ| is a scalar, and √G=ρ²√|γ|. The text writes the density as ρR[g_ρ]+κρ²X without the factor √|γ|, which equals 1 only in the matrix chart.
- Required action: add one clause on the weight (verbatim text below).

**F6 (minor).** Location: insert, "Compensation", the last sentence.
- Finding: "the same freedom is the ambiguity Θ→Θ+dY" is argued, not computed.
- Required action: soften to "corresponds to".

## Scope of what is established
**Established, conditional on the stated hypotheses.** The hypotheses are:
- the Poisson limit, four matrix coordinates, bosonic n_D=0;
- the LUV² density;
- backgrounds Lie-dragged by the joint flow and regular on Σ;
- local charges, closed Σ or fall-off;
- γ=X*η flat and not an independent dynamical field (emergence preserved: γ is the matrix contraction η in another chart, never identified with spacetime or G);
- classical Iyer–Wald, not the replica.

Within these:
- Local invariants are functionals of (γ, ω), identical to the matrix-chart values at the sampled jets (exact rational arithmetic, one jet per signature).
- (γ, ω, e, G, ρ, ϑ) are Lie-dragged by the joint flow and [e,B]=0 on Σ (symbolic, both signatures). L_ξX=BX≠0.
- First-order densities have no Σ-charge mod exact forms.
- R_G+𝒯+2∇V=R_W (Weitzenböck decomposition, exact at the sampled jets). The charges of √G R_G and √G R_W coincide on Σ when [e,B]=0, which is the stationarity condition itself.
- L_r=L_0 on the class with c_W(r)=N_tot/6+κ_Xr for every real r.
- The f·Riem(γ) shift of the Σ-charge is compensated, up to the flux at infinity, by an identically conserved improvement. This is proved analytically in general (above) and confirmed by s4.
- Hence the Iyer–Wald identity does not select r, which is bounded indeterminacy.

**Reformulation, not derivation.** c_A−c_T=4κ_X is equivalent to a required edge term of −4κ_X. No value of the edge term is derived.

**Conjecture/mechanism.** That the selection belongs to the modular Hamiltonian (A) or to a local compensating symmetry (D1). The proposal's "more than four coordinates does not remove the freedom" is likewise argued, not computed.

**Classification and labels.** PROGRAMME-CONDITIONAL. Nothing is DERIVED. B, D and A stay `Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL`. There is no label change and no `LABEL-CHANGE-PROPOSED`.

**Milestone and breakthrough assessment.**
- No MILESTONE trigger. In particular, no M2: this is an indeterminacy within stated hypotheses, as in the accepted 038 treatment, and routes through A and D1 remain open.
- It does close ledger avenue (1) of the 041 entry (Wald charge decides r) within the (γ, ω) class. The orchestrator may weigh that.
- No `BREAKTHROUGH` flag, in agreement with the researcher's self-assessment: the result narrows B and relocates the missing ingredient but derives no critical-path step.

**No-go class.** The statement "the first law does not select r" is bounded to the hypotheses above. It does not cover:
- the replica or Lewkowycz–Maldacena route;
- a modular Hamiltonian with edge modes;
- a derived local compensating symmetry (D1);
- more than four coordinates (Riem(γ)=KK on embeddings);
- the Dirac sector.

**Open avenues that could still favour the infrared/full-GR derivation, ranked by my judgement of promise:**
1. Chapter 7 T^op: define T^op as the response to a specified background on the δρ=0 modes, compute its superpotential, and test whether the edge term is −4κ_X. This is concrete, finite, and fixes the edge term by construction.
2. Modular-Hamiltonian edge term of the one-loop fluctuations in a joint-flow-stationary background (A∩B). This decides which edge accompanies the replica.
3. D1: derive whether the compensating η-rotation can be a local symmetry. Then JKM uniqueness fixes r; the 039 dressing gave r=−2, leaving 2κ_X.
4. More than four coordinates: compute f(Riem−KK) and the Y freedom. Riem(γ) is then not identically zero on the class, which may or may not remove the freedom (open).
5. Edge modes and nonlocal edge terms (symplectic gauge sector).
6. Lewkowycz–Maldacena dynamical replica for the singular-ρ family.
7. Dirac sector and the 041 analytic proofs.

The proposal's relaxation "γ dynamical" is correctly excluded as incompatible with emergence. It appears only in the proposal table, not in the insert, and I agree it must not appear in manuscript text except as a scope hypothesis ("use no metric other than the pull-back of η", already present).

## Recommended disposition
Revise. The insert is acceptable for integration once the six replacements below are made. For the rest of `appH_insert.tex`, ACCEPT means the current insert text exactly, with only these replacements. A revised round r2 is needed only to confirm the replacements.

## Corrected snippet
No new physics or assumptions are added. Each "old" string occurs once in `appH_insert.tex`.

**(1) Compensation, last two sentences.**
Old: `The shift of the charge on \(\Sigma\) is therefore the boost charge of the shift of \(T_\eta\) on the Cauchy surface of the wedge, and the relation of~\cite{IyerWald1994} between the charge on \(\Sigma\) and the boost charge of \(T_\eta\) holds for every \(r\). In the variables \((X^a,\omega)\) the same freedom is the ambiguity`
New: `By Stokes' theorem on the Cauchy surface of the wedge, the boost charge of the shift of \(T_\eta\) equals the shift of the charge on \(\Sigma\) minus the flux of \(Q^{ab}\) at spatial infinity. For variations of \(f\) of compact support the first-order change of the charge on \(\Sigma\) is therefore the boost charge of the change of \(T_\eta\), and the relation of~\cite{IyerWald1994} between the charge on \(\Sigma\) and the boost charge of \(T_\eta\), with its term at infinity, holds for every \(r\); for constant \(f\) the improvement vanishes and the charge on \(\Sigma\) is carried by that term. In the variables \((X^a,\omega)\) this freedom corresponds to the ambiguity`

**(2) Consequence, first sentence.**
Old: `Within these hypotheses the first law does not select \(r\).`
New: `Within these hypotheses the Iyer--Wald identity for the induced density does not select \(r\); the response \(T_\eta\) to \(\gamma\) is not identified here with \(T^{\mathrm{op}}_{\mu\nu}\) of Equation~\eqref{eq:first-law}.`

**(3) Consequence, n_D=0 sentence.**
Old: `For \(n_D=0\) the equality \(c_A=c_T\) is the statement that the edge term that accompanies the fixed-state replica is that of \(r=-4\), that is \(-4\kappa_X\) in units of \(c\) relative to \(L_0\).`
New: `For \(n_D=0\) the fixed-state replica has \(c_A-c_T=4\kappa_X\), so the requirement \(G_A=G_T\) of the paragraph on the normalisation holds if and only if the edge term that accompanies the replica contributes the coefficient of \(r=-4\), that is \(-4\kappa_X\) in units of \(c\) relative to \(L_0\).`

**(4) Consequence, last sentence (constraint term).**
Old: `A multiplier term for the constraint \(b=\mathcal F[\Theta]\) depends on first derivatives of \((\gamma,\omega)\) only and has no charge on \(\Sigma\).`
New: `For the constraint \(b=F[\Theta]\), with \(F\) the covariantised composite built from the first jets of \((\gamma,\omega)\), a multiplier term depends on first derivatives of \((\gamma,\omega)\) only and has no charge on \(\Sigma\); this is the charge that the paragraphs on the comparator and on the order \(\Lambda^2\) list as not computed, and it is computed only in this setting.`
Note: in the insert the symbol is `\(b=F[\Theta]\)` exactly as written, not `\mathcal F`. Use the literal string present in the file, `A multiplier term for the constraint \(b=F[\Theta]\) depends on first derivatives of \((\gamma,\omega)\) only and has no charge on \(\Sigma\).`

**(5) Covariant variables, weight clause.**
After `…and the torsion of \(e\) taken with the Levi-Civita connection of \(\gamma\).` insert: `Densities carry the factor \(\sqrt{\lvert\gamma\rvert}\), which is \(1\) in the matrix chart, so that \(\sqrt G=\rho^2\sqrt{\lvert\gamma\rvert}\).`

**(6) Final scope paragraph.**
Old: `They do not determine the edge term, the modular Hamiltonian, the replica or the Dirac sector,`
New: `They do not determine the edge term, the modular Hamiltonian, the replica or the Dirac sector, do not identify \(T_\eta\) with \(T^{\mathrm{op}}_{\mu\nu}\) of Equation~\eqref{eq:first-law},`

`eq:first-law` is defined once in ch06 (checked while scanning). After these edits the insert still has a single closing scoped status sentence.
