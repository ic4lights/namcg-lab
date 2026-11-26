VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The four exact lemmas, the Poisson-limit inequality, the state-scaling numerics and the literature attributions check out. Three passages of the insertion state more than was shown, and each needs exact replacement text before integration:
- the flow angle is defined through the wrong generator;
- the two-cap union is labelled "exact" for caps more general than the coaxial pair actually treated;
- the non-additivity and counterterm sentences go beyond the fixed-frame, leading-order statement that was established.

## Source reading
- **Mode.** Digest plus targeted reads.
- **Digest status.** `python scripts/make_digest.py --check` printed `DIGEST CURRENT`; `dirty-chapters: yes`. The only dirty file is appH, from 064's uncommitted integration (+29 lines). That is expected under the 2026-10-15 directive. I applied 3(d) by reading the affected passages of the working tree directly.
- **Read in full:**
  - appH L2800–2894: the end of sec:status-F (the 064 working-tree text around the anchor), all of sec:status-G (L2850–2869), and the start of sec:status-H.
  - ch17: L470–495 (Problem G and the G completion levels), L655–670 (dependency order), L715–730 (completion criterion, item G-derived).
  - ch12 L1–270: eq:rho-debt, def:HBEV, ass:Sent-density / eq:Sent-exp, ass:bdy-EE / eq:bdy-EE, thm:Leff / eq:Leff, and the Remark "Dimensional status".
  - ch03 L125–206 (eq:Smatrix, def:matrix-coords-ext) and L336–372 (ass:dictionary).
  - ch04 L150–170 (def:composite-metric, eq:g-from-e).
  - ch06 L170–220 (sec:ch6-replica).
  - bib: the Steinacker2023 entry and the bib tail (CRLF).
  - MILESTONE.md and the ledger tail (L516–614).
  - The full proposal-r1.md and appH_insert.tex.
- **Grep check.** `edge mode|relational|Hartnoll|minimal area|Ryu` over chapters/ turned up no existing passage that this insertion contradicts or makes stale.
- **Scan ruling.** This is ordinal 63, so 3(a) does not apply; the next scan is at 65. 3(b) does not apply because I find no milestone (see below).
  - 3(c) does not apply. The insertion is a conditional paragraph placed next to the problem's ledger section, as `CLAUDE.md` prescribes. It changes no definition, assumption, scope statement or status text. Its closing sentence restates the existing label ("open and PROGRAMME-CONDITIONAL"), consistent with the Ledger label at L2853–2857.
  - Being the first paragraph in a section that until now held only Ledger/Status text does not change that section's scope. The scope is fixed by the Ledger label and the Status paragraph, and both are untouched.
- **No full scan was performed.** No file was unreadable.

## Claim under review
- **Claim.**
  - Exact finite-N lemmas on a compact fuzzy factor for the relational block entropy of Fliss–Frenkel–Hartnoll–Soni (2408.05274): the edge identity; the rank-one cap block on X=AJ with s²=¼M(N−M)(σ₁²+σ₂²); the rank-one charge spectrum and the two-cap union; the hook-content rank derivative.
  - A Poisson-limit inequality P ≤ 2√2πs.
  - Scalar-proxy numerics: ℓ∝s; reproduction of the paper's Eq. (3.14) coefficient; a different l_c power for e^{−S/2}.
  - Consequences: the state, l_c and the frame group are supplied inputs; the entropy is not the HBEV density of ass:Sent-density (sector, locality and metric mismatches).
  - Presented as a bounded no-go.
- **Original target.** G-derived: a matrix-derived local density S_ent(h_ij,φ) on ∂M of the form eq:Sent-exp, matrix-derived eq:bdy-EE, and Λ_eff from eq:Leff (ch17 "G completion levels"; completion item "Problem~G-derived").
- **Appendix H, verbatim.** Ledger label: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and G-external support at most a scope-limited model; G remains OPEN and neither satisfies the matrix-derived criterion." Status: "The mechanism is CLOSED CONDITIONALLY under the stated boundary entropy; derivation of the infrared entropy density and stationarity from the matrix theory is OPEN. A boundary-model or externally justified result is programme-conditional and supports only a scope-limited model."
- **ch17, verbatim.** "CRITICAL PATH; mechanism CLOSED CONDITIONALLY, derivation OPEN."

## Checks performed
**Direct re-derivations (by hand):**
- **Lemma 1.** Write Y=[X,Θ], so Y†=−Y.
  - Tr(Y†Y) = 2Tr(ΘX²) − 2Tr(XΘXΘ), and Tr(ΘXΘ̄X) = Tr(ΘX²) − Tr(ΘXΘX). That gives the factor ½.
  - Tr(Θ[X,Y]) = Tr(Y(ΘX−XΘ)) = −Tr(Y²) = Tr(Y†Y).
  - Verified.
- **Lemma 2.**
  - With the J³ basis in decreasing order, ⟨m|J₊|m−1⟩² at m=j−M+1 equals j(j+1)−(j−M+1)(j−M) = M(2j+1−M) = M(N−M). So J¹ and J² each have the single ΣΣ̄ entry ½√(M(N−M)) and −(i/2)√(M(N−M)), and the J³ block vanishes.
  - In the rotated basis the block is ½√(M(N−M))((AR)^a₁ − i(AR)^a₂)|u)(v|, so s² = ¼M(N−M)tr(AP_nAᵀ) = ¼M(N−M)(σ₁²+σ₂²).
  - Poisson limit: M=N sin²(θ/2) gives M(N−M)=(N sinθ/2)². With ∂_φx = (N/2)sinθ A(−sinφ e₁ + cosφ e₂), (4π)⁻¹∮|∂_φx|² = (N sinθ/2)²(σ₁²+σ₂²)/4 = s².
  - Cauchy–Schwarz gives P ≤ (2π∮|∂_φx|²)^{1/2} = 2√2πs, with equality iff |∂_φx| is constant, iff σ₁=σ₂. Verified.
  - This holds for φ the rotation angle about n, i.e. the flow of the symbol of n·J; see F1.
  - 2D tensors: K = θ²εᵀgε = θ² det g · g⁻¹, so K⁻¹ is conformal to g. Verified.
- **Lemma 3.**
  - X_{Σ̄Σ} = (X_{ΣΣ̄})† and Π is Hermitian, so Q = −2i(|u)(w| − |w)(u|).
  - With |w) = α|u) + β|ŵ), Q on span{u,ŵ} is [[−4Imα, −2iβ],[2iβ, 0]]. Its trace is −4Imα and its determinant −4β², so its eigenvalues are −2Imα ± 2(Im²α+β²)^{1/2}. Verified.
  - The union for two caps needs (v₁|Π restricted to Σ₂ to vanish, and conversely. That holds for coaxial caps with banded Π; see F2.
- **Schur row sum.** Σ_k T_kT_k† over an orthonormal basis of V_l is SU(2)-invariant on an irreducible C^N with trace 2l+1, hence equal to (2l+1)/N·1. Verified.
- **Proxy row length.** ⟨ℓ²⟩ = 4s²W follows for independent, equal-variance Π^a: the cross terms a≠b vanish. Verified.
- **Coefficient check.** For X=νJ, s² = ν²M(N−M)/2. With f=νl/2 the one-sided row sum is W ≈ νl_c³/(6N), so ⟨ℓ²⟩ ≈ ν³l_c³M(N−M)/(3N). Converting the paper's ℓ = √(ν³Λ³N)|∂Σ|/(4√3π) with |∂Σ| = 4π√(M(N−M))/N gives the same expression. Verified.
- **States.** ψ = e^{−κx²/4} gives ⟨π²⟩ = κ/4; the oscillator ground state with ω=√κ gives ⟨π²⟩ = √κ/2. Verified.
- **Lemma 4.** d log Π(M+c−r)/d log M = Σ M/(M+c−r) → |μ|, exactly, for a polynomial diagram. Verified.
- **Non-additivity estimate.** 30 log(5/4) + 20 log 5 = 38.88, which matches s5(d).

**Scripts.**
- s1, s2, s3, s4 and s5 were re-run with `python -I`, writing output to the scratchpad folder C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\r065. All exited 0.
- Every output is byte-identical to the corresponding saved .out.txt.
- The quoted values all appear in the s4 output: 1.0206→1.021, 1.0414→1.041, local exponents 2.979 and 3.931, and 16NW/l_c⁴ = 1.0693.
- The scripts write only to stdout. Grep for open/write/save found file writes only in apply_check.py, to the given outdir. `git status` was unchanged after the runs: nothing was written into the proposal folder or the repository.
- What the scripts cover: s1–s3 and s5(b) check exact identities numerically; s4 is a scalar-proxy numeric; s5(d) is a one-sided-diagram numeric. Symbolic or numeric output is a check, not a proof.

**Integration.**
- apply_check.py was re-run into the scratchpad folder C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk065apply and printed APPLY CHECK PASS.
- Baselines: appH is 614579 bytes, sha256 7d15a3f2…; bib is 29360 bytes, sha256 1d280848…. Both match the working tree.
- Results: appH sha256 c44095d54d874fedc79947344401bfcdadc70789314555672a19b6c703fa1e8a, 3378 CRLF lines, no bare LF. bib 29781 bytes, sha256 28fdd7f8cb62b2ad23da3cc05d819a0b750f7fdec096511fca60ab02135ea64d, 994 CRLF lines, no bare LF. I confirmed both hashes independently on my own output.
- The anchor (L2868–2870) occurs exactly once. The paragraph lands after "scope-limited model." and before `\section{Problem H…}`.
- All eight referenced labels exist exactly once. There are no new labels. Both cite keys resolve. I found no process language.
- Build: I did not rebuild. I read build_r1.txt: PASS, 380 pages, 0 undefined or multiply defined references, overfull boxes equal to the baseline.

**Literature.**
- arXiv 2408.05274 abstract page: title, authors, v2 of 30 May 2025, journal reference SciPost Phys. 18, 171 (2025).
- Crossref 10.21468/SciPostPhys.18.6.171: title, the four authors, vol. 18, issue 6, art. 171, published 2025-06-02. The bib entry matches.
- arXiv HTML v2 (Sects. 2–5 opening, via WebFetch) confirms:
  - Eq. (2.47), S_E = min_V log d_{μ_V}.
  - Eq. (2.54), the minimisation "over all subregions of the target space with a fixed volume".
  - Fig. 2, the cap as "the one with minimal boundary area".
  - Eqs. (3.10)/(3.11), the Gaussian state and the cutoff Λ on angular momentum.
  - Footnote 13, "metastable".
  - Eq. (3.12), the entry ν√(M(N−M)); Eq. (3.13), √(M(N−M)) = (N/4π)|∂Σ|.
  - Eq. (3.14), 2ℓ log(eM/ℓ) and the expression for ℓ.
  - Eq. (4.4), the classicalised charge; Eq. (4.6), its spectrum gives the row lengths.
  - Eq. (5.2), G = U(N′)⊗1_p; and the abstract's statement that coarse-graining is essential.
- Not read by me: Sects. 5.1–5.4 and the appendices. The frame-average saddle stays imported, as the insertion says.
- arXiv 2303.08012 abstract: the sentence "The vacuum energy does not act as cosmological constant, but stabilizes the brane structure at one loop" is confirmed verbatim. The DOI is 10.1007/JHEP05(2023)129.
- Frenkel–Hartnoll 2301.01325 and Frenkel 2311.10131 were not independently verified. Neither is cited in the insertion.

## Findings
**F1. Major.**
- *Location.* appH_insert.tex L14: "with \(\phi\) the angle of the flow generated by \(n\cdot x\)".
- *Finding.* x is never defined, and the context reads it as the target image (∂_φx, "ellipse in target space"). The Hamiltonian flow of n·x = (N/2)n·Aω is rotation about Aᵀn. Its orbits are not the cap boundary unless n is an eigenvector of Aᵀ.
- *Reason.* The derivation and s2 both use rotation about n, the flow of the symbol of n·J. As written, the "exact" Poisson-limit identity is false for generic A.
- *Required action.* Replace "In the Poisson limit, with \(M(N-M)\to(\tfrac12N\sin\theta)^2\)," with "In the Poisson limit, with \(x^a\) the symbol of \(X^a\) and \(M(N-M)\to(\tfrac12N\sin\theta)^2\),". Replace "generated by \(n\cdot x\)" with "generated by the symbol of \(n\cdot J\)".

**F2. Major.**
- *Location.* L16: "For two caps whose edges are farther apart than twice the band width of \(\Pi^a\), the nonzero spectrum is the union of the two single-cap pairs (exact)."
- *Finding.* The claim was derived and checked (s3) only for the two coaxial caps: the M₁ largest and M₂ smallest eigenvalues of one n·J. Spectral projectors of n₁·J and n₂·J with n₁≠n₂ are not orthogonal at finite N, so Θ₁+Θ₂ is not a projector, and banding refers to one eigenbasis.
- *Reason.* This is an "exact" label on a statement more general than what was proved.
- *Required action.* Replace the sentence with: "For the two caps of one axis \(n\), the spectral projectors of \(n\cdot J\) on its \(M_1\) largest and its \(M_2\) smallest eigenvalues, with edges farther apart than twice the band width of \(\Pi^a\) in the eigenbasis of \(n\cdot J\), the nonzero spectrum is the union of the two single-cap pairs (exact)."

**F3. Major.**
- *Location.* L20, item (ii), from "For two separated caps…" to "…form of Assumption~\ref{ass:Sent-density}."
- *Finding (a): fixed frame.* In 2408.05274 the entropy of a rank-(M₁+M₂) block is min_V log d_{μ_V} (Eq. (2.47)). That minimum selects the region of minimal boundary at fixed volume, not two separated caps. The non-additivity shown is a property of log d_{μ_V} at the fixed two-cap frame, i.e. of the functional being minimised, not of the minimised entropy. The text says "the value … is not additive over components" and then "the entropy therefore does not have the form". That reads as a statement about S_E.
- *Finding (b): two-sided factor.* The factor 2 in "2ℓ₁ log…" for the paper's two-sided diagrams was not computed. s5(d) is one-sided.
- *Finding (c): counterterm.* "no counterterm built from h_ij alone removes the term" is not shown. At fixed diagram, the part of |μ| log M set by N (log M = log N + log(M/N)) multiplies the row data like a cutoff-dependent coefficient. A local counterterm built from h_ij could absorb such a part, much as α₀L_UV³ is cutoff-dependent. What is not removable by a density fixed by the boundary data is the dependence on M beyond that, and this is not established here.
- *Reason.* Point (c) overstates the obstruction. Point (a) mixes the fixed-frame functional with the entropy. The conclusion that the functional is not of the assumed form still follows, conditionally, from fixed-frame non-additivity.
- *Required action.* Replace the passage with the corrected snippet below.

**F4. Minor.** L18, last sentence. The frame subgroup (Eq. (5.2) of the paper) is also a supplied coarse-graining, but the text lists only the state and l_c. Replace with: "The state, \(l_c\) and the subgroup of the frame average are therefore supplied inputs; none is fixed by the integral here."

**F5. Minor.** L18: "Where the weight is positive" should read "Where the weight is positive and integrable". A state needs normalisability. Replace "For the Lorentzian weight with a convergence regulator neither is a positive state." with "For the Lorentzian weight with a convergence regulator the weight is not positive, and neither construction applies as stated."

**F6. Minor.** L16: "The proportionality \(\ell\propto s\) holds for every such \(f\); its coefficient depends on \(f\) and on \(l_c\)." In the proxy ⟨ℓ²⟩ = 4s²W holds exactly. W depends on M at finite l_c (s4 shows a ratio of 0.87–1.21 across M at l_c=4, narrowing at larger l_c). Replace with: "So \(\langle\ell^2\rangle=4s^2W\) for every such \(f\), with \(W\) depending on \(f\), on \(l_c\) and, weakly at large \(l_c\), on \(M\) (numerical)."

**F7. Minor.**
- L10: "so the classical datum of the edge charge is the quadratic form" should read "so the squared norm of the classical datum of the edge charge is the quadratic form". The datum is the block; the identity gives its norm.
- L20: "For a fixed diagram \(\mu\)" should read "For a fixed polynomial diagram \(\mu\)". The hook-content formula covers polynomial irreps; the paper's two-sided weights are mixed.

**Researcher's flagged discrepancy (not blocking; recorded for the author).** Confirmed. sec:status-G has no "Missing step" paragraph. The ch12 Remark "Dimensional status" (L243–265) records that eq:Leff is dimensionally incomplete: the left side has mass dimension 4, the right side 3, so a boundary-to-bulk conversion of dimension one is missing. Neither appH G nor ch17's G-derived item mentions this. Adding it would be a status-passage edit with a full scan, so it should be a later package.

**No prior-claim error found.** I found no closure claim and no label change. The emergence caveat is explicit: the Hamiltonian ground state is said to need an evolution parameter the integral lacks. No fundamental time or metric is introduced.

## Scope of what is established
**Exact at finite N (once F1, F2 and F7 are applied):**
- Lemma 1.
- Lemma 2's rank-one block and s².
- Lemma 3's spectrum, and the union for coaxial caps with banded momenta.
- The Schur row sums.
- The hook-content rank derivative.

**Poisson limit.** For linear deformations X=AJ with φ the rotation about n, s² is the Dirichlet integral and P ≤ 2√2πs, with equality iff σ₁=σ₂. This is kinematic: the ellipsoid is not a stationary point, and the state's response is not computed. So the paper's round-sphere identification of the boundary datum with target-space length does not survive off-round deformations at the level of the classical datum.

**Numerical (scalar proxy).** The Eq. (3.14) coefficient is reproduced at leading order in l_c. The square root of the weight changes the power of l_c from about 3 to about 4.

**Imported and conditional.** S ≈ log d_μ, a single dominant irrep, and the frame-average minimum. Fixed-frame non-additivity of log d_{μ_V} is conditional on these. Hence "not of the form of ass:Sent-density" is a PROGRAMME-CONDITIONAL, bounded statement.

**Inputs.** The state, l_c and the frame subgroup.

**Unresolved.** The map from s to eq:g-from-e (Problems A and D1); the sector mismatch (the region of K is not ∂M).

**Not derived.** No entropy density on ∂M, no S_ent^(IR), no eq:bdy-EE, no Λ_eff. G remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. No label change.

**Class of the no-go.** It covers: a compact internal fuzzy factor with positive contraction; a single projector at a fixed frame (one cap, or two coaxial caps); leading semiclassical order with one dominant irrep; Gaussian proxy states with supplied variances; the FFHS subsystem algebra (block ΘXΘ with edge irreps). It does not close the relational-entropy route in general, nor the replica route of ass:Sent-density.

**Relaxations that could still favour G-derived, ranked:**
1. A spacetime-block subsystem. Use a finite-trace projector on a 4D region × fibre of a compact Euclidean 4D fuzzy space or a product such as S²×S², whose edge is 3D × fibre. This relaxes the "internal factor" hypothesis, which is the decisive sector mismatch. Multi-row diagrams are needed.
2. A within-core state. Use Osterwalder–Schrader reconstruction along a matrix-built reflection on fibre modes, which the existing flat-point no-go does not cover. This relaxes "supplied state" without external time. Without it, no route is matrix-derived.
3. A different subsystem algebra or a first-law variation. The commutant or frame-off-diagonal algebra of the paper's Sec. 2.4, fixed-rank δS, or mutual-information combinations could cancel the M-dependence. This relaxes "FFHS block algebra / leading log d_μ". Reading log(M/ℓ) as a scale-dependent area coefficient is a conjecture only.
4. A stationary non-symmetric background (squashed su(3)) with the state response. This relaxes the "kinematic X=AJ" hypothesis of the metric test.
5. Tying l_c and p to integral scales: the fibre truncation, the regulator, the IR scale.
6. The Steinacker 2303.08012 vacuum term: a ρ_Λ√−g term versus an embedding potential (low cost, indirect).

**Significance and coherence.** This is the first G-derived package. It is a bounded, verifiable obstruction that locates the missing ingredients (state, spacetime-block subsystem, metric map). The bundled claims share one construction. The vacuum-term sentence is weakly coupled to the rest but correctly scoped, and it belongs to G's eq:rho-debt context.

**Milestone.** None.
- M1: not met, since nothing on the critical path is derived.
- M2: not met. The excluded class (FFHS block entropy on an internal compact factor) is not a route the manuscript currently keeps open. The manuscript's G route is the replica construction of ass:Sent-density on ∂M, which is untouched. The researcher's "routine" is correct.
- M3, M4 and M5: none apply.

## Recommended disposition
Revise: apply F1–F3 (major) and F4–F7 (minor) verbatim as given, then re-run apply_check and the build. No new physics or assumptions are needed. The bib entry and the placement are acceptable as they stand.

## Corrected snippet
For F3, replace the text of item (ii) from "For two separated caps" through "the form of Assumption~\ref{ass:Sent-density}." with the following. It adds no new physics; it narrows the claims to what is shown.

```latex
For the two caps of one axis above, at that fixed frame, with rows \(\ell_1,\ell_2\) of one diagram of \(U(M_1+M_2)\), the value of \(\log d_\mu\) for a one-row diagram per cap exceeds the sum of the single-cap values by about \(\ell_1\log\frac{M_1+M_2}{M_1}+\ell_2\log\frac{M_1+M_2}{M_2}\), up to a correction of the order of a logarithm (numerical); the two-sided diagrams of~\cite{FlissFrenkelHartnollSoni2025} are not computed. The cause is that the block of the union contains the blocks between the caps. So the quantity that is minimised over frames is not additive over components; this is a statement at fixed frame, not about the minimised entropy of a block of rank \(M_1+M_2\). The integral over \(\partial M\) of a local density in \(h_{ij}\) and \(\phi\) is additive over far-separated components and depends on \(\partial M\) only through those data; a counterterm built from \(h_{ij}\) alone can remove at most a part of \(|\mu|\log M\) that is fixed by them, such as one set by \(N\) at fixed diagram, and is not shown to remove its dependence on the rank. At this order, and with the leading-order entropy of~\cite{FlissFrenkelHartnollSoni2025}, the functional \(\log d_\mu\) therefore does not have the form of Assumption~\ref{ass:Sent-density} (conditional).
```

Replacement text for F1, F2 and F4–F7 is given under each finding.

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3
