VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

FINAL review of proposal 016 r1 (supersedes the provisional report; SME answer read at C:/Users/redgi/Projects/namcg-lab/proposals/016-mirage-stress/sme-consult-r1.md; SME-CONSULT flag removed as resolved).

## Verdict
The mathematics holds: the exact Poisson identities and the leading-symbol algebra reproduce independently, including at y^i != 0. But "derived conserved extra stress" overstates (ii), because conservation of X = wE - T is Bianchi plus the conservation of the input T. The matrix-level conservation identity is prior art, and the LaTeX contains a wrong definition (ell_5). The package therefore needs the revisions below. No breakthrough, no milestone.

## Source reading
Digest + targeted reads; not a full scan (none required: no definition, assumption or status passage changes). I relied on the orchestrator's CURRENT digest report and did not run `make_digest.py --check`. Read in full: proposal-r1.md; all four scripts and outputs; MILESTONE.md; scout entry R14 and the ledger lines on the "derived extra stress"; appH 1842-1907; appH 1103-1112 (sec:status-F); Kumar-Steinacker 2312.01317 pp. 1-13; and the SME reply sme-consult-r1.md. 015 files ignored.

## Claim under review
Problem F, also bearing on B and A. Appendix H (sec:status-F), verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." Target: A, B, C and the sign/scheme of G_eff computed from specified operators, with G_eff not an input. Not met; no label change.
Claims:
- (i) the Poisson-limit Noether identity {X^a,E_a}=0 and the stress divergence identity;
- (ii) a "derived conserved extra stress" at the leading symbol of the 013/014 level-one sector;
- (iii) the modified Einstein equation (w+Lambda L)E=T and its crossover;
- (iv) the extra roots.

## Checks performed
(i), by hand.
- Let S = sum {X^a,{X^b,Z_ba}} with Z_ba={X_b,X_a} antisymmetric. Relabelling a<->b gives S=-S'.
- Jacobi gives S-S' = {F^{ab},Z_ba} = -{F^{ab},F_ab}, which is zero because eta is diagonal and {f,f}=0. So S=0.
- The mu^2 term vanishes by antisymmetry. Hence {X^a,E_a}=0 is exact and off-shell for arbitrary X. It is the Noether identity of the gauge invariance dX={Lambda,X}.
- The mu^2 piece of the stress identity: {X_a, mu^2 X^aX^b} = mu^2 X_a F^{ab}, which matches the mu^2 part of -F^b_c E^c.
- {X_a, eta^{ab}f/4} = {X^b,f}/4, so the trace-subtracted form is exact on E=0. The subtracted term is (1/4)eta F^2, the Lagrangian term, not the trace of T^{ab}.
- T^{ab} is the eta-variation of the action; E_c is the correct field equation.
- The linear identity is the O(A) part of {X^a,E_a}=0, with E^(0)_a=(3+mu^2)T_a.
- I re-ran check_noether_poisson.py for both bracket signs: all True.

(ii)/(iii), my own script (numpy floating point, a numerical check, not a proof, independent of lib_ls.py): C:/Users/redgi/AppData/Local/Temp/claude/C--Users-redgi-Projects-namcg-lab/4d0177a0-6b3d-45ad-bb6d-645d2be99f00/scratchpad/gk.py.
- W_y was built from the 013 description (self-dual forms of y^perp in R^{1,4}). Base points were (5,0,0,0,3), (13,0,0,0,5), and generic (6,1.5,-2,1,2.5), (9,3,-4,2,-3) with y^i != 0.
- I checked: s_i.q=0; Gram G = q_perp^2*1 - s4 s4^T; X symmetric with q.X=0; X = -(Lambda/2) sum s~^i (x) (M c_i); (w+Lambda L)E=T. All residuals are 1e-13 or below.
- The spectrum of L matches the stated formulas, with xi = g - |s4|^2 for y^i != 0. So the y^i=0 restriction is NOT essential; it only enables the closed forms xi=-sigma q^2 and q_perp^2.
- I re-ran check_sector_poles.py: determinant, spectrum and 014 cross-check reproduce. I did not re-run check_mirage_stress.py (slow sympy); my script covers the same relations.
- TT-like channel: omega^2 = -(k^2+rho/2)/sigma, correct.

Anchor and labels:
- `\section{Problem G: HBEV}` occurs once, at appH line 1907. The preceding 014 paragraph closes at line 1905.
- eq:Smatrix, ch:vierbein-emergence, ass:EE and sec:status-F each occur once. Bib keys KumarSteinacker2023 and Steinacker2026 exist.
- No new labels or bib entries; no label change; spacetime stays emergent.
- 015's text goes in sec:status-B, far from this anchor. If 015 also inserted before sec:status-G, the order would need coordination.

Literature:
- I read Kumar-Steinacker directly: C is ambiguous under C -> C + dC and "fixed in Appendix C through conservation of the Einstein tensor".
- Via the SME, I take as evidence (not independently verified by me) the following. 2601.08031 eq. (3.25) and review eqs. (112)-(115) give (1 - m^2 Box~^-1) dG ~ 8 pi G T with m^2 = 32 pi G_N alpha^2 r^-4. The extra modes are not covariant poles: they are a non-boost-invariant dispersion with velocity c/sqrt3 or c/sqrt5 from the cosmic frame, isotropic in rotations, and expected to be an artefact. Conservation of T[C] is imposed by fixing the ambiguity (harmonic gauge at linear order), not derived. The massless matrix identity [X_a,T^{ab}] ~ e.o.m. is known (Steinacker 0812.3761 eqs. 88-90, credited to Abou-Zeid-Dorn hep-th/0104244; semiclassical versions in eqs. 93-99). The exact form {X^a,E_a}=0 and the massive (mu^2) stress identity were not found in the literature.
- The SME could not map q_perp, xi, sigma onto the papers' notation, so a match is unconfirmed.

## Findings

**F1. Major. Location: header and text of the second paragraph ("Derived stress"); milestone paragraph of the proposal.**
- Finding: "derived conserved extra stress" overstates (ii). X := wE[h] - T is symmetric by definition and conserved because E obeys the Bianchi identity and the input T is conserved.
- The qq ambiguity is not "chosen" so that the divergence vanishes: X is fixed, and q^mu X_{mu nu}=0 is a consequence of the inputs.
- The closed form X = -(Lambda/2) sum s~^i (x) (M c_i) = -Lambda L[E] is the content. It is the tree-level force conjugate to h, expressed through the amplitudes.
- The SME confirms that this is exactly how the literature obtains conservation of T[C]: it fixes the ambiguity by Einstein-tensor and matter conservation (2312.01317 App. C), with harmonic gauge at linear order in 2601.08031. So the "literature argues, here derived" contrast is unsupported. What the package adds is the explicit, exactly solvable linear map X = -Lambda L[E] in one class, not a derivation of conservation.
- 008/009 comparison:
  - 008/009's missing stress concerned a rank deficiency (3 against 6) in the H_A class.
  - 013 showed the rank is 6 in CP^{1,2}, so no component is missing.
  - 016's X is the 014 tree-level term recast as a stress, with the induced term supplied. It is not the 008/009 object, and the 014 obstruction is bypassed only by supplying w. Nothing is resolved.
- Required action: retitle to "Extra stress and crossover response at the leading symbol" and delete "Derived stress". Replace the conservation sentence (see Corrected snippet). State that the structure parallels the ambiguity-fixing of Kumar-Steinacker and is not a new derivation of conservation. Make no claim to supply the stress of 008/009.

**F2. Major. Location: second paragraph, "ell_5^2 = ell^2 - (y^4)^2".**
- ell^2 = -y_a y^a (a=0..4) is already the 5D quantity, so the formula is wrong as written. The scripts, my check and the 014 paragraph all use ell_5^2 = y0^2 - y4^2 - |y|^2 = ell^2.
- Required action: delete the symbol ell_5 and use ell throughout.

**F3. Minor. Location: second paragraph, definitions.**
- H (the map c -> h) and D^S are undefined.
- varkappa of the 014 paragraph is dropped silently; say it is absorbed in w and Lambda.
- State that the operator bold-L is taken on the 6-dimensional span of the symmetrised s_i s_j, invertible for q^2 != 0 and xi != 0.
- "(spacelike q)" after "g+8xi<0" is not an equivalence. Drop it.

**F4. Minor. Location: Crossover and Roots sentences (physical reading).**
- Add the following to the text:
  - (a) The Einstein part wE is the supplied input. The result is that input plus a non-local, frame-dependent tree-level correction.
  - (b) The dispersion is elliptic in omega, not wave-like: for rho>0 there is no real-frequency root in the TT-like channel; for rho<0 real roots exist only for k^2<|rho|/2, and above that omega^2<0 with growth rate proportional to k. Whether these are retarded poles is untreated.
  - (c) G is indefinite for spacelike q.
- The anisotropy is that of the background direction yhat. It is SO(3,1)-covariant if y^mu is a vector, not an explicit breaking of covariance.
- Per the SME, the literature's extra modes are rotation-isotropic with velocity c/sqrt3 or c/sqrt5 and are in the same family of cosmic-frame non-boost-invariant effects. Do not claim a match: the notation mapping is unconfirmed. The present ellipticity (q_perp^2 positive definite) is stronger than a reduced speed and is a distinguishing feature.

**F5. Minor. Location: first paragraph.**
- The massless matrix-level identity [X_a,T^{ab}] ~ e.o.m. is prior art (Steinacker 0812.3761 eqs. 88-90, crediting Abou-Zeid-Dorn hep-th/0104244; semiclassical versions in its eqs. 93-99). It cannot be presented as new.
- The Poisson-limit form {X^a,E_a}=0 and the mu^2 variant {X_a,T^{ab}} = -F^b_c E^c + (1/4){X^b,F^2} were not found in the literature (SME: "not found", not "absent"). Say so with attribution.
- Prior art may be cited only if it is added to `bib/namcg.bib`. The SME has confirmed those two references in 0812.3761's reference list but did not open hep-th/0104244, so mark them "not independently verified". The researcher must supply and verify the bib entries (I did not fetch them), or else cite no new works and state "the massless identity is standard".
- Add that T^{ab} is a matrix-index tensor and {X_a,.} is a frame derivative, not nabla_mu T^{mu nu}.
- Replace "trace term" by "the term (1/4)eta^{ab}F_{cd}F^{cd}".

**F6. Minor. Location: citations.**
- The comparison with KumarSteinacker2023 and Steinacker2026 stays structural. It may now state, as verified by the SME, that in Steinacker2026 conservation of T[C] is imposed by the ambiguity, with the (1 - m^2 Box~^-1) form at linear order.
- Make no quantitative match: the q_perp, xi, sigma versus alpha, r mapping is unverified.

Package coherence: (i) is not used by (ii)-(iii) but shares the matrix setting; acceptable as one package given the explicit disclaimers.

## Scope of what is established
**Established (exact computation within the class).**
- The Noether and stress identities (the massless form being prior art).
- At the leading symbol, tree level plus an input induced EH form and a conserved source: the closed form X = -Lambda L[E], the exact equation (w+Lambda L)E=T, the L spectrum and the dispersion determinant. These hold at the checked points, including y^i != 0 (my check).

**Conditional or input.** w (hence G_eff and rho), the conserved T and its coupling, mu^2=-3, and the identification of h with the emergent metric.

**Open.** Subleading order, the sign and size of w, a matrix-derived matter coupling, whether the extra roots are retarded poles, and the nonlinear order.

DERIVED nothing toward F's target; PROGRAMME-CONDITIONAL. Problems A, B, C, D1, E, F, G-derived and N stay OPEN / CRITICAL PATH as recorded in Appendix H.

**BREAKTHROUGH: not flagged, decided explicitly.** The package derives no critical-path step. The "derived stress" is a definitional rewrite whose conservation comes from inputs, in the same way as the literature. The 008/009 obstruction is not resolved. It is a bounded structural finding, and milestone trigger 1 is not met even weakly.

**Class of the finding.** It holds within the Poisson limit, the level-one sector, the leading symbol, frozen coefficients, and tree level plus the input EH form. It is not a no-go beyond those hypotheses.

**Open avenues, ranked (relaxations that could still favour the infrared or full-GR derivation).**
1. Subleading order 1/(|q|ell): masses, frame connection and harmonic mixing could change the indefinite-G structure and the extra roots. It also decides whether rho >~ 1/ell^2 lies in the regime of validity.
2. Compute the induced coefficient in this class (heat kernel with the Theta-built regulator). This fixes the sign and size of w and rho, i.e. F's own target, and selects the branch.
3. Relax the frozen frame: average over base cells and fibre classes to test whether the yhat-dependent q_perp^2 structure averages to an eta-covariant form, or maps onto the literature's reduced-speed modes. y^i != 0 is not essential (my check).
4. Replace the supplied T by a matrix-derived matter coupling, using the matrix stress of (i) after relating the frame divergence to the coordinate divergence.
5. Doubleton phase-space constraints on the inert modes, which could remove the indefinite-G ghosts.
6. Nonlinear order, transverse matrices, N >= 8 matrix coordinates.

## Recommended disposition
Revise, then integrate. F1 and F2 are mandatory; F3-F6 are minor. The insertion before `\section{Problem G: HBEV}` is acceptable. Keep a single status sentence, at the end of the second paragraph only.

## Corrected snippet
No new physics is needed. Extra assumption: none. H is the linear map c -> h, with varkappa absorbed in w and Lambda. The citation addition in F5 requires the researcher to supply and verify the bib entries; I have not done so.

Definitions (replaces the ell_5 text):
```latex
\ldots with \(q_\perp^2=q^2+(q_\mu y^\mu)^2/\ell^2\) and \(\sigma=(y^4)^2/\ell^2\); the eigenvalues of \(G\) are \(g=q_\perp^2\) (twice) and \(\xi=-\sigma q^2\), along the spatial \(\mathbf q\); \((y^0/\ell)^2\) replaces \((y^0/\ell_5)^2\) in \(G\), and \(\ell_5\) is deleted.
```
Heading and conservation sentence (replaces "Derived stress"):
```latex
\emph{Extra stress.} ... \(q^\mu X_{\mu\nu}=0\) follows from the Bianchi identity of \(\mathcal E\) and the conservation of \(T\); the amplitude equations determine \(X\) up to \(q_\mu q_\nu\), which this condition fixes, as the ambiguity of the anharmonicity tensor is fixed in~\cite{KumarSteinacker2023,Steinacker2026}. The closed form \(X=-\tfrac12\Lambda\sum_i\tilde s^i\otimes Mc_i=-\Lambda\mathcal L\mathcal E\) expresses the extra stress through the tree-level equations; it is not an independent derivation of its conservation, and the Einstein part \(w\mathcal E\) is the supplied input.
```
First paragraph, prior art (add after the identities):
```latex
For the massless model the matrix-level identity \([X_a,T^{ab}]\propto\) equation of motion is standard; the Poisson-limit form \(\{X^a,E_a\}=0\) and the divergence identity with the \(\mu^2\) term are recorded here as exact identities in the polynomial Poisson algebra.
```
Addition before the status sentence:
```latex
The relation is elliptic in \(\omega\) rather than wave-like: for \(\varrho>0\) the first channel has no real-frequency root, and for \(\varrho<0\) real roots exist only for \(k^2<|\varrho|/2\). The anisotropy is that of the background direction \(\hat y\), through \(q_\perp^2=q^2+(q\!\cdot\!\hat y)^2\), and \(G\) is indefinite for spacelike \(q\).
```
