VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: SME-CONSULT | PROGRESS: first | OPEN: 0/2

## Verdict
The mathematics holds: the exact Poisson identities and the leading-symbol algebra reproduce independently, including at base points with y^i != 0. But "derived conserved extra stress" overstates (ii), because conservation of X = wE - T is the Bianchi identity plus the conservation of the input T. The text also has one wrong definition (ell_5), an undefined H, and gaps in its physical wording. No breakthrough, no milestone.

## Source reading
Digest + targeted reads; not a full scan (none required: no definition, assumption or status passage changes). I did not run `make_digest.py --check`; I relied on the orchestrator's CURRENT report. Read in full: proposal-r1.md; all four scripts and outputs (lib_ls.py included); MILESTONE.md; scout entry R14 and the ledger lines on "derived extra stress"; appH lines 1842-1907 (013/014 paragraphs and the anchor); appH 1103-1112 (sec:status-F head); Kumar-Steinacker arXiv:2312.01317 pp. 1-13 (fetched; Sec. 4 and Eqs. 4.18-4.29 read). 015 files ignored per instruction.

## Claim under review
Problem F, also bearing on B and A. Appendix H (sec:status-F), verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." Original target: A, B, C and the sign/scheme of G_eff computed from specified operators, with G_eff not an input. Not met; no label change proposed.
Claims: (i) Poisson-limit Noether identity {X^a,E_a}=0 and a stress divergence identity; (ii) a "derived conserved extra stress" at the leading symbol of the 013/014 level-one sector; (iii) the modified Einstein equation (w+Lambda L)E = T and its crossover; (iv) the extra roots.

## Checks performed
(i), by hand. Let S = sum {X^a,{X^b,Z_ba}} with Z_ba={X_b,X_a} antisymmetric. Relabelling a<->b gives S = -S', S' = sum {X^b,{X^a,Z_ba}}. Jacobi gives S - S' = {F^{ab},Z_ba} = -{F^{ab},F_ab}, which vanishes because eta is diagonal and {f,f}=0. So S = 0, and the mu^2 term vanishes by antisymmetry. Hence {X^a,E_a}=0 exactly and off-shell for arbitrary X. It is the standard Noether identity of the gauge invariance dX={Lambda,X}.
- The mu^2 piece of the stress identity checks by hand: {X_a, mu^2 X^a X^b} = mu^2 X_a F^{ab}, which equals the mu^2 part of -F^b_c E^c.
- {X_a, eta^{ab} f/4} = {X^b,f}/4, so the trace-subtracted form is exact on E=0. The "trace term" is the Lagrangian term (1/4) eta F^2, not the trace of T^{ab}: a wording point.
- T^{ab} is the eta-variation of the action. The volume form is eta-independent, so there is no -1/2 eta L term.
- E_c is the correct field equation (Liouville integration by parts, checked).
- The linear identity is the O(A) part of {X^a,E_a}=0 with E^(0)_a=(3+mu^2)T_a.
- I re-ran check_noether_poisson.py for both signs of the bracket: all True.

(ii)/(iii), my own script, independent of lib_ls.py (numpy floating point, so a numerical check, not a proof): C:/Users/redgi/AppData/Local/Temp/claude/C--Users-redgi-Projects-namcg-lab/4d0177a0-6b3d-45ad-bb6d-645d2be99f00/scratchpad/gk.py.
- I built W_y from the 013 description (self-dual two-forms of y^perp in R^{1,4}, random orthonormal frame, projected to indices 0..3) and used a separate linearised-Einstein implementation.
- Base points: (5,0,0,0,3), (13,0,0,0,5), and generic (6,1.5,-2,1,2.5), (9,3,-4,2,-3) with y^i != 0; two random q each.
- I solved Lambda*M c + H^T(wE[h]-T) = 0 for random conserved T and checked: s_i.q=0; Gram G = q_perp^2*1 - s4 s4^T; X symmetric with q.X=0; X = -(Lambda/2) sum s~^i (x) (M c_i); and (w+Lambda L)E = T. All residuals are 1e-13 or below.
- The spectrum of L is 1/(2g) (x2), 1/(g+xi) (x2), (g +- sqrt(g(g+8xi)))/(8 g xi), with xi the third eigenvalue of G, xi = g - |s4|^2 for y^i != 0. This matches the stated formulas.
- So the y^i=0 restriction is NOT essential to (ii)/(iii). It is used only to write xi=-sigma q^2 and q_perp^2 in closed form.
- I re-ran check_sector_poles.py: determinant, L spectrum and the 014 cross-check reproduce. The printed determinant also carries g^6 xi^3, absorbed in the LaTeX "proportional to".
- TT-like channel: (w+Lambda/(2g))E=T gives (1+rho/(2g))E=T/w. With y^i=0, g = k^2+sigma*omega^2 and sigma=y4^2/ell^2, so omega^2=-(k^2+rho/2)/sigma. Correct.
- I did not re-run check_mirage_stress.py (slow sympy); my script covers the same relations numerically.

Anchor and labels:
- `\section{Problem G: HBEV}` occurs once, at appH line 1907. The preceding 014 paragraph closes at line 1905 with the status sentence.
- eq:Smatrix, ch:vierbein-emergence, ass:EE and sec:status-F each occur once. Bib keys KumarSteinacker2023 and Steinacker2026 exist.
- No new labels or bib entries; no label change; spacetime stays emergent.
- 015's text goes in sec:status-B, far from this anchor. If 015 also inserted before sec:status-G, the order would need coordination.

Literature: I read Kumar-Steinacker directly. C_{mu nu} is defined by dS_YM = -4 int rho C dE. It is ambiguous under C -> C + dC, "fixed in Appendix C through the conservation of the Einstein tensor" (Eqs. 4.21, 4.29). I did NOT read 2601.08031 or 2609.08955. The linearised (1-m^2 Box^-1) form, the "c/3" modes and the "apparent tachyon" are not independently verified.

## Findings

**F1. Major. Location: header and text of the second paragraph ("Derived stress"); milestone paragraph of the proposal.**
- Finding: "derived conserved extra stress" overstates (ii). X := wE[h] - T is symmetric by definition and is conserved because the linearised Einstein tensor obeys the Bianchi identity and the input T is conserved by assumption.
- The qq ambiguity is not "chosen so that the divergence vanishes". X is fixed, and q^mu X_{mu nu}=0 is a consequence of the inputs.
- The solved amplitude equations give X = -(Lambda/2) sum s~^i (x) (M c_i) = -Lambda L[E]. That closed form is the content: the tree-level force conjugate to h, expressed through the amplitudes.
- This is the same logic as Kumar-Steinacker, where the C -> C + dC ambiguity is fixed by conservation. The statement "in the literature as extracted conservation is argued; here derived" is unsupported.
- Comparison with 008/009 and the ledger's "additional derived conserved stress":
  - 008/009 found a rank deficiency of E[h] (3 against 6 conserved sources) in the H_A class.
  - 013 showed that in CP^{1,2} the rank is 6, so no component is missing.
  - 016's X is the 014 tree-level term recast as a stress, with the induced term w supplied. It is not the object 008/009 said was missing.
  - The 014 obstruction (no local E[h]=T from the tree level alone) is bypassed only by supplying w. Nothing is resolved.
- Required action: retitle ("Extra stress and crossover response at the leading symbol"; delete "Derived stress"). Replace the conservation sentence (see Corrected snippet). State that T_C = -Lambda L[E] expresses the tree-level equations and is not an independent derivation of conservation. Make no claim to supply the stress of 008/009.

**F2. Major. Location: second paragraph, "ell_5^2 = ell^2 - (y^4)^2".**
- Finding: ell^2 = -y_a y^a (a=0..4) is already the 5D quantity (appH 1860/1862), so the formula is wrong as written.
- All scripts and my check use ell_5^2 = y0^2 - y4^2 - |y|^2, which equals ell^2. The formulas q_perp^2 = q^2+(q.y)^2/ell^2, sigma = y4^2/ell^2 and (y0/ell)^2 are correct and agree with the 014 paragraph (yhat=y/ell).
- Required action: delete the symbol ell_5 and use ell throughout.

**F3. Minor. Location: second paragraph, definitions.**
- H (the map c -> h) and D^S are undefined.
- The factor varkappa of the 014 paragraph is dropped silently; say it is absorbed in w and Lambda.
- State that the operator bold-L is taken on the 6-dimensional span of the symmetrised s_i s_j, and that it is invertible for q^2 != 0 and xi != 0.
- "(spacelike q)" after "g+8xi<0" is not an equivalence: for small sigma, g+8xi > 0 even for spacelike q. Drop it.

**F4. Minor. Location: Crossover and Roots sentences (physical reading).**
- The text correctly says q_perp^2 is Euclidean-definite. It should also say:
  - (a) The Einstein part wE is the supplied input. The result is that input plus a non-local, frame-dependent tree-level correction, not a derivation of an Einstein equation.
  - (b) The dispersion is elliptic in omega, not wave-like. For rho>0 the TT-like channel has no real-frequency root at any k. For rho<0 (the sign the proposal reports for a healthy-sign induced term, left open in the LaTeX) the roots are real only for k^2<|rho|/2. Above that, omega^2<0 with a growth rate proportional to k at large k. Whether these are retarded poles is untreated.
  - (c) The tree form c^T M c = q^2 tr(D G D^T) has an indefinite G (negative xi for spacelike q), which is the source of the complex generalised eigenvalues.
- The anisotropy is SO(3,1)-covariant if y^mu is a vector (q_perp^2 = q^2+(q.y)^2/ell^2). It is a preferred direction of the background, not an explicit breaking of covariance. Say so, to prevent a misreading as "Lorentz violation".

**F5. Minor. Location: first paragraph.**
- (i) is the standard gauge Noether identity and is not used in (ii)-(iii). Its disclaimers (no identification with an Einstein source; frame-derivative terms) are right. Optionally add that T^{ab} is a matrix-index tensor and {X_a,.} is a frame derivative, so this is not nabla_mu T^{mu nu}.
- Replace "trace term" with "the term (1/4) eta^{ab} F_{cd}F^{cd}".

**F6. Minor. Location: citations.**
- The comparison with KumarSteinacker2023 and Steinacker2026 must stay "structural". Do not attribute the (1-m^2 Box^-1) form or the extra modes to them, since this is unverified.

Package coherence: (i) and (ii)-(iii) share the matrix setting but (i) is not used by the others. Acceptable as one package given the explicit disclaimer.

## Scope of what is established
**Established (exact computation within the class).**
- The matrix Noether identity, the stress divergence identity and the linear identity.
- At the leading symbol, tree level plus an input induced EH form and a conserved source: the decomposition of h, the closed form X = -Lambda L[E], the exact equation (w+Lambda L)E=T, the L spectrum and the dispersion determinant.
- These hold at the checked points, including generic y^i != 0 (my check), with the 013/014 model S_i.

**Conditional or input.** The induced coefficient w (hence G_eff and rho), the conserved T and its coupling through h, mu^2=-3, and the identification of h with the emergent metric.

**Open.** Subleading order, the sign and size of w, a matrix-derived matter coupling, whether the extra roots are retarded poles (constraints and gauge fixing untreated), and the nonlinear order.

DERIVED nothing toward F's target; PROGRAMME-CONDITIONAL. Problems A, B, C, D1, E, F, G-derived and N stay OPEN / CRITICAL PATH as recorded in Appendix H.

**BREAKTHROUGH: not flagged.** The package derives no critical-path step. The "derived stress" is a definitional rewrite whose conservation comes from the inputs. The 008/009 obstruction is not resolved. It is a bounded structural finding, and milestone trigger 1 is not met even weakly.

**Class of the finding.** It holds within the Poisson limit, the level-one sector, the leading symbol, frozen coefficients, and tree level plus the input EH form. It is not a no-go beyond those hypotheses.

**Open avenues, ranked (relaxations that could still favour the infrared or full-GR derivation).**
1. Subleading order 1/(|q|ell): masses, frame connection and harmonic mixing could change the indefinite-G structure and the extra roots. It also decides whether rho >~ 1/ell^2 lies in the regime of validity.
2. Compute the induced coefficient in this class (heat kernel with the Theta-built regulator). This fixes the sign and size of w and rho, i.e. F's own target, and selects the rho>0 or rho<0 branch.
3. Relax the frozen frame: average over the base cell and fibre classes to test whether the yhat-dependent q_perp^2 structure averages to an eta-covariant form. My check indicates y^i != 0 is not essential.
4. Replace the supplied T by a matrix-derived matter coupling, using the matrix stress of (i) after relating the frame divergence to the coordinate divergence.
5. Doubleton phase-space constraints on the inert modes, which could remove the indefinite-G ghosts.
6. Nonlinear order, transverse matrices, N >= 8 matrix coordinates.

## SME consultation request
Provisional verdict given above.
1. In arXiv:2601.08031 and the review arXiv:2609.08955, is the linearised crossover form (1 - m^2 Box~^-1) dG ~ 8 pi G T stated as in the scout report, with what m^2? Is the "apparent tachyon" of the extra modes Lorentz-covariant or anisotropic?
2. Is the conservation of T[C] there derived, or imposed by fixing the C -> C + dC ambiguity (as in 2312.01317 App. C)?
3. Is the Poisson-limit identity {X^a,E_a}=0 and the divergence identity for the eta-variation stress already in the literature?
The verdict depends only mildly on the answers. They affect only how strongly F1 and F6 can be phrased.

## Recommended disposition
Revise, then integrate. Apply F1-F6, with F1 and F2 mandatory. The insertion before `\section{Problem G: HBEV}` is acceptable. Keep a single status sentence, at the end of the second paragraph only.

## Corrected snippet
No new physics is needed. Extra assumption: none. H is defined as the linear map c -> h, with varkappa absorbed in w and Lambda.

Definitions (replaces the ell_5 text):
```latex
\ldots with \(q_\perp^2=q^2+(q_\mu y^\mu)^2/\ell^2\) and \(\sigma=(y^4)^2/\ell^2\); the eigenvalues of \(G\) are \(g=q_\perp^2\) (twice) and \(\xi=-\sigma q^2\), along the spatial \(\mathbf q\); \((y^0/\ell)^2\) replaces \((y^0/\ell_5)^2\) in \(G\), and \(\ell_5\) is deleted.
```
Heading and conservation sentence (replaces "Derived stress"):
```latex
\emph{Extra stress.} ... \(q^\mu X_{\mu\nu}=0\) follows from the Bianchi identity of \(\mathcal E\) and the conservation of \(T\); the amplitude equations determine \(X\) up to \(q_\mu q_\nu\), which this condition fixes. The closed form \(X=-\tfrac12\Lambda\sum_i\tilde s^i\otimes Mc_i=-\Lambda\mathcal L\mathcal E\) expresses the extra stress through the tree-level equations; it is not an independent derivation of its conservation, and the Einstein part \(w\mathcal E\) is the supplied input.
```
Addition before the status sentence:
```latex
The relation is elliptic in \(\omega\) rather than wave-like: for \(\varrho>0\) the first channel has no real-frequency root, and for \(\varrho<0\) real roots exist only for \(k^2<|\varrho|/2\). The anisotropy is that of the background direction \(\hat y\), through \(q_\perp^2=q^2+(q\!\cdot\!\hat y)^2\), and \(G\) is indefinite for spacelike \(q\).
```
