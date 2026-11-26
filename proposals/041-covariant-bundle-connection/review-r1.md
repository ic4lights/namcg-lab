VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The central structural results are sound and correctly bounded: B is not a rotation connection, the Moser-variable covariant operator holds numerically at J = dJ = 0, and the covariant a_1 and the −1/−4 split of r follow. Three statements in the insert are wrong or over-labelled (a factor 2 in the stated axion form E, "exact" labels on sampled numerical identities, and an unqualified "diffeomorphism covariance" claim) and must be corrected before integration. The F block largely restates a relation already merged, and optional edit (b) should be dropped.

## Source reading
- Digest plus targeted reads in full, under CLAUDE.md 3(d). The dirty working tree was read directly, not HEAD. This is not a full scan.
- Appendix H, Problem B: ledger label (L44-47), normalisation paragraph (L174-179), the order Λ² paragraph (038, L306-330) and the order Λ_UV² paragraph (039, L332-341), up to `\section{Problem C...}` (L343).
- Appendix H, Problem D: head (L511-514) and the fermionic-content paragraph (L188-191).
- Appendix H, Problem F: ledger (L1309), the Θ-built heat-kernel paragraph (L2123-2131), the Casimir paragraph (L2156-2181), the 032/034/040 blocks (L2261-2306), up to `\section{Problem G}` (L2308).
- I did not re-read Chapter 10 or Chapter 17 in this round. I rely on the proposal's quoted Chapter 17 and Appendix H labels and checked them only against the Appendix H ledger lines above. Treat the Chapter 10 and Chapter 17 consistency check as not independently done by me.
- The previous reviews of proposals 039 and 040 were not re-read. They were not needed for the points below.

## Claim under review
Question: does the matrix model supply a covariant bundle connection for the connection-sector fluctuation operator, and what does that do to the κ_X ρ²X term and to the B residue c_A − c_T^ext?

Quoted statuses from Appendix H, verbatim:
- Problem B: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- Problem D: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B …"
- Problem F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."

No label change is proposed and none is made.

## Checks performed (direct)
- **Anchors.** Python on the working-tree file, CRLF normalised: `\section{Problem C: conformal mode and Cassini}` occurs once and `\section{Problem G: HBEV}` occurs once. Both OLD strings, (a) and (b), occur once.
- **Insert mechanics.**
  - `appH_insert.tex` contains 0 TAB, 0 CR, 0 non-ASCII and 0 other control characters.
  - Braces balance (net 0), `\(`/`\)` balance (net 0), and `\[` and `\]` are 4 and 4.
  - No `\ref`, `\label` or `\cite`.
  - The non-comment lines equal the two blocks in proposal-r1.md exactly. The four leading `%%` lines must be stripped on integration.
  - Each block ends with one scoped status sentence.
  - No process language found. The references "preceding paragraph" and "paragraph on the order Λ²" resolve to 039 and 038 respectively.
  - I did not re-run the scratch pdflatex build. I read `compile_check.out.txt` (two passes exit 0, no undefined refs or duplicate labels), which the integrator must repeat via `scripts/build_check.py`.
- **Scripts re-run.**
  - s1: B = crossed w, residual about 1e-15 for both signatures, on class and non-class coframes. The shift law is exchanged (best scale −1.0000, residual about 1e-12), and the "if B were a connection" residual is 0.6-1.0.
  - s2c: H − 2M_G − bE = 0 exactly at 6 rational points.
  - s10: similarity invariance to about 1e-14.
  - s5: Gilkey routine reproduces √G a_1 = (4/6)ρR[g_ρ] + ρ²X at six jets.
  - s11 and s11b: Maxwell–dilaton a_1 matches −R/3 + □lnρ − V² to 8 digits, and the axion part ratio is +1.0000 (Euclid) and −1.0000 (Lorentz).
  - s6c: null vector (1/2, −1, 3/2, 1, −2, 1), residual 5.8e-12 (Euclid) and 2.3e-13 (Lorentz), with a_1 formulas to 3e-11.
  - s8: dim ker C2 = 0 at all 12 draws.
  - s3b: first-order coefficients agree to about 1e-15 and principal parts to 1e-13, at J = dJ = 0 jets.
  - s3c: the mismatch scales linearly along ONE line only.
  - s7: Box = C41 − C31 exactly. Only R sign −1 commutes. Only the Zeeman sign −1 solves the fit, with (α, β, γ) = (1, 1, 3).
- **Independent analytic checks.**
  - The Maxwell–dilaton operator reduces to −∇² + V·∇ + (Ric + ∇V), with ω = −V/2 and tr E = −R + □lnρ − V². This gives a_1 = −R/3 + □lnρ − V², as claimed.
  - ρ^{-1}∂(ρGA) = ∇·A − V·A, as claimed.
  - 𝔍^ν = ρ^{-1}∂_μ(ρG^{μν}), as claimed.
  - The conformal rescaling ρR[g_ρ] = ρ²(R_G + 3□lnρ − (3/2)V²) holds, and X = −R − □lnρ + 6s|U|² follows.
  - Eliminating |U|² with the stationary-set identity gives −4R + 6V² − 10□lnρ.
  - Internal consistency: on the merged on-modes (V = 0, ⟨R⟩ = −X/4), X = −R + 6s|U|² and s|U|² = −R/2 both give X. So the −4 route is consistent with the merged on-mode value.
  - The J-part is genuinely needed on those off-shell modes, because s12 gives s|U|²/X = 0.116 and 0.227, not 1/8. This is correctly disclosed.
- **Finding 1: factor 2 in E (checked by script).** The matrix `E[I,J] = 8ε` used in s2c and s3, as a quadratic form in the six F components, equals 2 ε^{μνρσ}F_{μν}F_{ρσ}. The numerical ratio is 1.99999999. M_G as a form equals ρ G^{μρ}G^{νσ}F_{μν}F_{ρσ}; this is correct.

## Findings

1. **Major. Location: Block 1, Moser variables, "\(\partial^2L/\partial\omega\partial\omega=2\mathsf M_G+b\,\mathsf E\) … \(\mathsf E\) the form \(\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\)".**
   - Finding: as a quadratic form the verified E is 2εFF, not εFF.
   - Reason: with the stated definitions the axion coupling would be b/2 in the quadratic action. The verified coefficient 6s|∂ϑ − ϑV|² holds for ϑ = ρb with b from s2/s2c. The quadratic action is ρGGFF + b εFF, which is the Hessian halved. With E = εFF, ϑ would be ρb/2 and the coefficient 6 would be wrong by a factor of 4.
   - Required action: define E as the form 2ε^{μνρσ}F_{μν}F_{ρσ} and state the quadratic action (snippet A).

2. **Major. Location: Block 1, labels on numerical identities.** The following are stated in a way that reads as theorems.
   - "is, exactly (rational arithmetic at six points)". It is verified at six sampled rational points, not proved for general ω.
   - "has the same principal, first-order and zeroth-order coefficients" is numerical at sampled J = dJ = 0 jets. The statement "mismatch is linear in J and ∂J" rests on s3c, a single one-parameter line along which |J| and |dJ| scale together. It cannot separate the two.
   - "satisfy exactly one linear relation (rank five of six)" is numerical, 14 jets per signature, residual 6e-12, not proved. The sentence "so that on the stationary set also X = −4R_G + …" extends it to the whole stationary set.
   - "the Goldstone-extremised frame is not the coframe of any matrix background (twelve draws)" overreaches. It was tested only for the antisymmetry condition, for sampled generic constant ω̄. The proposal itself notes that (anti-)self-dual ω̄ may admit a two-dimensional family and was not tested. Closedness of the rotated form was not examined.
   - Required action: label each as numerical or sampled and scope each as in snippets B, C and D.

3. **Major. Location: Block 1, "This is a covariance under diffeomorphisms of the chart acting on \((G,\rho,\vartheta)\)".** The proposal itself records (item 7b) that G is not a tensor under chart diffeomorphisms, because it is built with the constant η contracted with the matrix index, which is the coordinate index. The insert omits this. A reader would take it to be diffeomorphism symmetry of the matrix model, which Problem D keeps separately (L944-995). Add the clause in snippet E.

4. **Minor. Location: Block 1, heat-kernel paragraph.** The text writes "\(a_1=\operatorname{tr}(E+R_G/6)\)". The manuscript uses \(\operatorname{tr}(R/6-E)\) (L309). Because E is undefined in the insert, this introduces a sign-convention clash. State a_1 in the manuscript normalisation instead (snippet D).

5. **Minor. Location: Block 1, Dirac statement.** The insert uses "\(\gamma^AD_A\)" and "\(\gamma^Ae_A{}^\nu\partial_\nu\)". D_A is undefined, and the manuscript writes \(\gamma^\mu D_\mu\) (the Poisson limit of \(\Gamma^\mu[\hat X_\mu,\Psi]\), L190). In the Poisson limit this is a derivative with no spin-connection term (the action is ρ-weighted), and the covariant-looking part of \(\mathcal O_f\) arises only on squaring, via β_σ. The "not shown covariant" scope is acceptable; the notation should match (snippet F).

6. **Minor. Location: Block 1, notation.** The insert introduces b as the axion coefficient. The 038 paragraph (L326) uses "\((G,\rho,b)\) give \(r=0\)" with a different b. Add one clause saying (G,ρ,ϑ) is not that set, since the axial torsion is not dual to dϑ (s4 negative check). Alternatively rename the insert's b.

7. **Minor. Location: Block 2 (Problem F).**
   - The relation "\(H_V=-C_{41}+C_{31}^{\rm tot}-C_V\), \(C_V=-3\)" is not new. The merged Casimir paragraph (L2159-2161) already has the exact relation \(H_V=C_G-C_{41}-C_\Sigma+\mu^2\) with μ²=−3. The insert's mass-free operator equals that H_V − μ², and C_V = C_Σ. The block also reuses the symbol H_V for the mass-free operator.
   - Reading both consistently, the content is the same. Presenting it as a fresh exact finding duplicates a merged result.
   - What is new is the interpretation: the vector operator commutes with J^{ab}+R^{ab}, so the y^μ dependence of F1, F2 reflects the base point and not a missing connection. Also new is the observation that no point of the Lorentzian leaf is Lorentz-fixed ((y⁰)² ≥ ℓ²).
   - This is modest but accurate. F1 depends on y only through the scalar y^μy_μ = −ℓ² − (y⁴)². F2 = κ²(α·y)² is the term containing y^μ as a vector. I verified both against the displayed formulas.
   - Required action: cite the existing relation (snippet G). Also state that the f1 = f2 points y^μ = 0, |y⁴| = ℓ refer to so(6) with δ; for so(4,2) with δ the merged text places them at y⁰ = −√2ℓ (L2135).

8. **Minor. Location: PRIOR-CLAIM qualifications.**
   - Edit (a): not required to correct any false statement, but it is a defensible qualification. The 038 sentence "stays undetermined until D is settled" is not false. It is no longer the only route, because Moser variables give covariance without D and still leave r undetermined. Accept (a) with the wording in snippet H, which avoids the vague "takes two values".
   - Edit (b): do not integrate. The old sentence is true (rotating the Θ-built frame leaves the class). The new clause "on the stationary set the density is a function of G, ρ and one pseudoscalar" rests on the numerical operator identity and adds an unlabelled numerical claim to an exact-style paragraph.
   - No merged sentence is false. No PRIOR-CLAIM-ERROR.

## Direct answers to the specific questions

**(a) Consistency with 038 and 039.**
- "The merged value is the −4 case" is correct as a statement of the on-mode value in the normalisation and 038 paragraphs. They say "c_T = N_tot/6 − 4κ_X" on-mode and "r=−4 would match … selected only by the match".
- 039's r = −2 comes from the dressed density (S = 0, ρ²X → 2𝒯 + 2V²). That is not a presentation of the Moser-variable X, so "corresponds to neither" is accurate, though the phrase invites confusion with 038's coframe elimination values (−2, 1, 4, 0). The ledger sentence "r=−2 leaves 2κ_X" is untouched.
- Two independent routes now give −4: the on-mode route and the stationary-set elimination route. The proposal correctly declines to treat this as selection.
- No merged sentence becomes false. The two OLD strings match once each in the working-tree file.

**(b) The exact claims.**
- (1) is re-verified. B = crossed w is analytic, from de^A = −w^A_B∧e^B, and checked. The shift law is exchanged. Similarity invariance of the heat-kernel diagonal is the standard fact and was checked. The no-go is scoped correctly to similarities and to the dressing e → Λe, with the hypothesis class stated in the insert, apart from the Goldstone overreach in finding 2.
- (2) holds, subject to the E correction in finding 1.
  - The Moser argument is valid for four coordinates in the Poisson limit. ω_X − ω is exact, and the linear term is proportional to 𝔍.
  - The 6-point exact identity is labelled "exactly", which needs the label in finding 2.
  - The operator identity is numerical.
  - The mismatch scaling is evidence along one line only.
- (3) The derivation was re-derived analytically as listed above. The numerical agreement a_1(V) = a_1(M) = formula to 3e-11 (14 jets per signature) supports it. The coefficient 6 is verified against the matrix operator through θ = ρb with the code's b.
- (4) The numerical stationary-set identity is real to about 6e-12 and rank-5, but unproved, and it is labelled "exactly one linear relation" in the insert.
- (6) The C_V = −3 identity is valid as an algebraic identity (s7), but is not new (finding 7).

**(c) Problem D scope.** The insert stays in scope. It claims only "no local Lorentz symmetry derived", a diffeomorphism-type covariance (once finding 3 is fixed), and a Dirac statement that is bounded and "not shown covariant". It does not claim local Lorentz symmetry is unnecessary for Problem D overall. The proposal's own summary item 5 ("the bosonic sector needs no local Lorentz symmetry for covariance in Moser variables") is more explicit than the insert; keep the insert's weaker wording.

**(d) Mechanics.** Passed, as above. One remaining item: the four leading `%%` comment lines must be removed. All required changes are snippets, so the insert needs re-submission.

**(e) Breakthrough assessment.**
- It is not a breakthrough. No critical-path step is derived and no important missing link is closed.
- It relocates the missing ingredient from frame non-invariance of X to the choice of which of G, ρ, ϑ are held fixed in the first law, and shows that 039's dressed frame leaves the matrix-realisable class (for the sampled generic ω̄). Both are consequential bounded results. No flag.

## Scope of what is established
- **Established identity or derivation.**
  - B_{c|ab} = w_{a|cb} − w_{b|ca}, and its exchanged shift law.
  - Similarity invariance of the heat-kernel diagonal.
  - The Moser construction: ω_X − ω is exact, and the second-order action is half the Hessian of an algebraic L(ω) plus a term proportional to 𝔍.
  - The analytic a_1 of a Maxwell–dilaton–axion operator.
  - The conformal relation, and X = −R − □lnρ + 6s|U|² given the operator identity.
  - Box = C41 − C31 and the Casimir relation on polynomials, already merged.
- **Numerical or sampled.**
  - The Hessian equals 2M_G + bE at 6 rational points.
  - S O_v S⁻¹ equals the Maxwell–axion operator coefficientwise at J = dJ = 0 jets (6 draws), and a_1 agrees on 14 jets per signature.
  - The stationary-set linear relation (14 jets per signature).
  - No in-class rotation for sampled generic constant ω̄ (12 draws).
- **Conditional.** r = −1 or −4, and a residue of 1 or 4 at n_D = 0, are conditional on the previous two groups. The vector holonomy contact of modulus 1 is not a continuation of Tr ρⁿ.
- **Open.**
  - The J-proportional part, which is eta-contracted (non-G-covariant).
  - The Wald/Noether charge for the constrained class.
  - The Dirac sector, replica and tip domain.
  - The gauge parameter α ≠ 1, and leaf dimension above 4.
  - The relation of the Φ-block to a^μ.
- **Hypothesis class of the "no connection" no-go.** Hessian in a^μ variables with the matrix index contracted by η, rotations implemented as a local similarity or as e → Λe, Poisson limit, four coordinates, α = 1, one loop. It does not bear on the exact Moyal model, the Φ-block, or a Dirac-sector connection.
- **Labels.** Nothing is DERIVED at the level of the original targets. Problems B, D and F remain OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL. Emergence is untouched: nothing makes spacetime or the metric fundamental, and G is explicitly not identified with the emergent metric.
- **Open avenues, ranked (the loop should follow these up).**
  1. The Wald/Noether charge for the constrained class. This is the located missing ingredient and decides between r = −1, −4 and a third value. It needs treatment of the non-tensorial dependence through η, and probably a proof that the constrained class admits a covariant variation.
  2. The explicit J-proportional part S O_v S⁻¹ − O_M (coefficients 19 and 1.9 numerically). It determines whether it is removable by a background redefinition, and is needed before any statement about G_T on the modes.
  3. An analytic proof of the Hessian identity and the stationary-set identity. These are the two sampled results the whole B reading depends on.
  4. The Dirac sector: a Moser-type structure for the fermionic Hessian, or the supersymmetric point (N_s, n_D) = (6, 2).
  5. The replica and tip domain for the covariant operator, and gauge dependence for α ≠ 1.
  6. Leaf dimension above 4, and the Φ-block covariance.

## Recommended disposition
Revise, then integrate. Accepted text, once revised exactly as below:
- Block 1 and Block 2, as amended by the snippets below.
- Optional edit (a), in the snippet H wording.
- Edit (b) is not accepted.

No bib change. After integration, run `scripts/build_check.py`.

## Corrected snippets (no new physics; extra assumptions: none)

**A (Hessian sentence, replacing the sentence beginning "That Hessian is, exactly").**
```latex
That Hessian equals \(2\mathsf M_G+b\,\mathsf E\) at six sampled rational points, in exact arithmetic and for both signatures (not proved for general \(\omega\)): \(\mathsf M_G\) is the quadratic form \(\rho\,G^{\mu\rho}G^{\nu\sigma}F_{\mu\nu}F_{\rho\sigma}\), \(\mathsf E\) the quadratic form \(2\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\) with \(\epsilon^{0123}=1\), and \(b=-\operatorname{sgn}(\operatorname{Pf}\Theta)\,\eta_{ac}\eta_{bd}\Theta^{ab}\Theta^{cd}/8\), so that the quadratic action is \(\rho\,G^{\mu\rho}G^{\nu\sigma}F_{\mu\nu}F_{\rho\sigma}+b\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\) up to the term proportional to \(\mathfrak J\). Apart from that term, the connection sector is a Maxwell field of the metric \(G\) with weight \(\rho\), coupled to the pseudoscalar \(\vartheta=\rho b\) through \(b\,\epsilon FF\); the variables \((G,\rho,\vartheta)\) are not the variables \((G,\rho,b)\) of the paragraph on the order \(\Lambda^2\), and the axial torsion is not the dual of \(\partial\vartheta\) (tested, residual \(0.3\)-\(1.0\)).
```
Delete the following original sentence, "Apart from the term proportional to \(\mathfrak J\), the connection sector is …", to avoid duplication. Keep the rest of the paragraph, including the gauge function.

**B (replacing "At points with … (six draws, first-order coefficients to \(10^{-15}\), both vanishing at zeroth order); away from \(\mathfrak J=0\) the mismatch is linear in \(\mathfrak J\) and \(\partial\mathfrak J\)").**
```latex
At sampled jets with \(\mathfrak J=0\) and \(\partial\mathfrak J=0\) (numerical: six draws, both signatures, first-order coefficients to \(10^{-15}\), both vanishing at zeroth order) the operator \(S\mathcal O_vS^{-1}\), \((Sa)_\nu=a^\mu\omega_{\mu\nu}\), has the same principal, first-order and zeroth-order coefficients as the Maxwell--axion operator in the \(\rho\)-weighted Lorenz gauge; along a one-parameter family leaving \(\mathfrak J=0\) the first- and zeroth-order differences grow linearly with the parameter.
```

**C (Goldstone sentence in the first paragraph, replacing "About a generic constant … (twelve draws, both signatures).").**
```latex
About the sampled generic constant \(\bar\omega\) (twelve draws, both signatures) the only first-order rotation that keeps \(\eta_{AB}e^B{}_\mu\) antisymmetric, a necessary condition for \(e\) to come from a two-form, is \(\lambda=0\); the Goldstone-extremised rotation of the preceding paragraph therefore does not satisfy this condition at those backgrounds. This was not tested for (anti-)self-dual \(\bar\omega\).
```

**D (heat-kernel paragraph).**
- Replace "For the Maxwell--axion operator, \(a_1=\operatorname{tr}(E+R_G/6)\) is" with:
```latex
For the Maxwell--axion operator the coefficient \(a_1\), in the normalisation in which \(\sqrt{\lvert G\rvert}\,a_1(\mathcal O_v)=\tfrac46\rho R[g_\rho]+\rho^2X\), is
```
- Replace "(the Hodge operator with the dilaton term \(V\) and the axion term; checked at generic jets, relative agreement \(10^{-6}\) or better, both signatures). At points with \(\mathfrak J=\partial\mathfrak J=0\) it equals \(a_1(\mathcal O_v)\), for which … (fourteen random stationary jets per signature, \(3\times10^{-11}\)). With … this gives, on the stationary set," with:
```latex
(the Hodge operator with the dilaton term \(V\) and the axion term; the dilaton part is derived analytically, and the axion term is checked at generic jets, ratio \(1\) to six digits, both signatures). On fourteen random jets per signature with \(\mathfrak J=\partial\mathfrak J=0\) it equals \(a_1(\mathcal O_v)\) to \(3\times10^{-11}\), and \(\sqrt{\lvert G\rvert}\,a_1(\mathcal O_v)=\tfrac46\rho R[g_\rho]+\rho^2X\). With \(\rho R[g_\rho]=\rho^2(R_G+3\Box_G\ln\rho-\tfrac32\lvert V\rvert_G^2)\) this gives, on those jets,
```
- Replace "On the same jets the invariants satisfy exactly one linear relation (rank five of six)," and the sentence ending "so that on the stationary set also \(X=-4R_G+6\lvert V\rvert_G^2-10\Box_G\ln\rho\)." with:
```latex
On the same jets the six invariants satisfy one linear relation to numerical accuracy (rank five of six),
\[
  s_\eta\,\lvert\partial\vartheta-\vartheta V\rvert_G^2=-\tfrac12R_G+\lvert V\rvert_G^2-\tfrac32\Box_G\ln\rho
\]
(residual \(6\times10^{-12}\); numerical, not proved), so that on those jets also \(X=-4R_G+6\lvert V\rvert_G^2-10\Box_G\ln\rho\).
```

**E (covariance sentence).** Replace "This is a covariance under diffeomorphisms of the chart acting on \((G,\rho,\vartheta)\); it is not a local Lorentz symmetry of the matrix index." with:
```latex
This is covariance of the operator under changes of the coordinates \(y\) when \(G\), \(\rho\) and \(\vartheta\) are treated as tensor fields. These fields are built from \(\omega\) with the constant \(\eta\) contracted with the matrix index, which is the coordinate index, so it is not a symmetry of the matrix action under independent chart diffeomorphisms, and it is not a local Lorentz symmetry of the matrix index.
```

**F (Dirac clause in the final scope paragraph).** Replace "whose operator \(\gamma^AD_A\) is the frame derivative \(\gamma^Ae_A{}^\nu\partial_\nu\) without spin connection and is not shown to have a covariant form" with:
```latex
whose Dirac operator \(\gamma^\mu D_\mu\), the Poisson limit of \(\Gamma^\mu[\hat X_\mu,\Psi]\), is a frame derivative without a spin-connection term and is not shown to have a covariant form
```
In the same scope paragraph, after "(numerical, at sampled jets)" nothing more is needed. Add the words "the Hessian, operator and stationary-set identities are numerical at the sampled points stated" before "They do not cover the Dirac sector".

**G (Block 2, replacing "In exact polynomial arithmetic (random polynomial fields), \(\Box=C_{41}-C_{31}\) and … giving no such identity.").**
```latex
Let \(C_{31}^{\mathrm{tot}}\) be as above and let \(H_V^{0}=H_V-\mu^2\) denote the operator without the mass term. The exact relation of the paragraph on the Casimir of \(\mathfrak{so}(4,2)\), \(H_V=C_G-C_{41}-C_\Sigma+\mu^2\), with \(C_G=C_{31}^{\mathrm{tot}}\) and \(C_\Sigma=C_V=-3\), reads \(H_V^{0}=-C_{41}+C_{31}^{\mathrm{tot}}+3\) (re-checked on random polynomial fields; the other sign of \(R^{ab}\) and the opposite sign of the Zeeman term give no such identity).
```
- Keep the remainder, but change "For the compact form \(\mathfrak{so}(6)\) with \(\delta\) the points … they are the points where the preceding paragraphs find \(f_1=f_2\)" to:
```latex
For the compact form \(\mathfrak{so}(6)\) with \(\delta\) the points \(y^\mu=0\), \(\lvert y^4\rvert=\ell\) exist, and they are the points where the preceding paragraphs find \(f_1=f_2\) in that case.
```
- Also change the sentence beginning "In this class the vector operator is therefore a Casimir operator of the total Lorentz spin: a bundle connection covariant under \(J^{ab}+R^{ab}\) is present, …" to end with "…is not the absence of a connection, but the dependence of the induced form on the base point".

**H (optional edit (a), replacing the NEW string).**
```latex
In the coframe variables it stays undetermined until the frame is dragged by a flow whose internal part is a local symmetry, that is until the question of local frame rotations (Problem~D) is settled; in the variables \((G,\rho,\vartheta)\) of the paragraph on Moser variables the Noether coefficient takes two values related by one numerical identity, and covariance does not select one.
```
