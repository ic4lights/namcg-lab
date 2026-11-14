# Proposal 067-product-sphere-edge, round 1

## Result

Follow-up of 065 (bounded no-go for the relational block entropy of Fliss-Frenkel-Hartnoll-Soni, arXiv:2408.05274, on a compact fuzzy factor), along its open avenues 1 (a block with a three-dimensional edge) and 3 (tests of the functional). The setting is the smallest within-core relaxation of 065's "one-dimensional edge of a cap": a compact **four-dimensional** fuzzy factor, the product of two deformed fuzzy spheres, X^I = (A_1 J (x) 1, 1 (x) A_2 J), with blocks whose Poisson-limit edge is three-dimensional (the dimension type of dM in def:HBEV).

**Mixed outcome: one cause of the 065 no-go is removed, two persist, and the measure is identified.**

Established, exact at finite N:
1. **Edge operator.** For a toric block (projector on a set Omega of joint J^3 (x) 1, 1 (x) J^3 eigenvectors) without the pattern inside/outside/inside on three consecutive sites, E = sum_I Theta X^I Thetabar X^I Theta is diagonal, with entry = sum over nearest-neighbour links to outside sites of k_f i(N-i), k_f = (sigma_{f,1}^2 + sigma_{f,2}^2)/4. The edge map has rank = number of edge sites (not one, as for the cap of 065). s^2 = Tr E (065's datum); T = Tr E^{1/2} is the trace norm of the edge map.
2. **Cap x whole second sphere** (edge = circle x S^2): rank N, T = N s_1, s^2 = N s_1^2, independent of A_2. Product block: rank M_1 + M_2 - 1, s^2 = M_2 s_1^2 + M_1 s_2^2, T = (M_2 - 1) s_1 + (M_1 - 1) s_2 + sqrt(s_1^2 + s_2^2).
3. **Pointwise identity.** rho sqrt(K^{mu nu} d_mu f d_nu f) is the 3-volume density of {f = 0} in gt = (sqrt g / rho)^{2/3} K^{-1}; K(df, df) = sum_I {f, x^I}^2.
4. **Charge reduction.** Q = -2i(Y - Y^dagger), Y = sum_a X^a_{S Sbar} Pi^a_{Sbar S}; its nonzero spectrum is that of an explicit 2r x 2r matrix; for alpha = 0 it is +-2 sv(C_perp). For torus-invariant Gaussian momenta <Y Y^dagger> is diagonal on the edge sites (state-weighted E); for cap x whole sphere it is s_1^2 W times the identity on the N edge sites. Q contains no contraction of the directions; delta_IJ enters only through the isotropy of the supplied variance.

Established in the Poisson limit (kinematic) and numerically:
5. **Measure.** sqrt2 T >= P_K (the weighted K-perimeter of item 3), with equality iff the edge is along a lattice direction or the diagonal and the speed along the generating flow is constant. Scaling exponents under (A_1 -> lam A_1, A_2 -> lam A_2): T and P_K (1, 0); induced 3-volume (1, 2); K^{-1} 3-volume (-1, -2). So T is neither the induced nor the K^{-1} 3-volume: transverse edge directions are weighted by the number of sites (symplectic volume).
6. **Crystalline anisotropy at fixed toric frame.** For oblique half-plane blocks the T-density per unit lattice length is (n_1 - n_2) sqrt(e_1) + n_2 sqrt(e_1 + e_2) >= sqrt(n_1^2 e_1 + n_2^2 e_2); the excess reaches 11% in the sampled cases.
7. **Rows.** Monte Carlo (N = 16): the number of boxes per side is 0.85-0.95 of 2 sqrt(W) T, i.e. it follows T (extensive over the 3D edge), not s.
8. **Dimension.** For r equal rows of length ell per side, log d = 2 r ell [log(M/(r + ell)) + c], 0.80 < c < 0.97; d log d / d log M = 2 r ell; sub-additive in r.

**Consequences for G-derived (conditional on the imported leading-order FFHS entropy, at fixed frame).**
- (a) *Removed:* 065's cause "single row / one-dimensional edge". On a 4D factor the coefficient of the logarithm is (within the numerical accuracy of item 7) a sum over the sites of a 3D edge of a locally determined quantity.
- (b) *Identified:* the measure of that sum. It is not the induced area. It is a 3-volume (of gt, conformal to K^{-1}) only for axis-aligned or diagonal edges with constant speed.
- (c) *Persisting:* rank dependence, now through log(M/(r + ell)) (for ell << N the depth M_1 behind the edge), and non-additivity in r; fixed-frame anisotropy; supplied state, cut-offs and frame; compact factor with positive contraction; no map to eq:g-from-e.

No entropy density on dM, no stationarity and no Lambda_eff are derived. G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Target and status

- **Problem.** G (HBEV), G-derived level.
- **Appendix H, sec:status-G (L2850-2894 at HEAD 54a2dcb).** Ledger label, verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and G-external support at most a scope-limited model; G remains OPEN and neither satisfies the matrix-derived criterion." Status paragraph: "The mechanism is CLOSED CONDITIONALLY under the stated boundary entropy; derivation of the infrared entropy density and stationarity from the matrix theory is OPEN." The 065 paragraph (L2871-2894) follows.
- **Chapter 17 (L474-495).** "CRITICAL PATH; mechanism CLOSED CONDITIONALLY, derivation OPEN." "G is DERIVED only when the entropy density and stationarity relation are derived from the matrix theory and Lambda_eff follows from them ... The required entropy density is the one in Assumption ass:Sent-density, derived by the replica construction from the matrix theory, and boundary stationarity Assumption ass:bdy-EE must likewise be derived rather than retained."
- **Original target.** Matrix-derived S_ent(h_ij, phi) on dM (mass dimension three, expansion eq:Sent-exp), matrix-derived stationarity eq:bdy-EE, and Lambda_eff from eq:Leff.
- **Dependencies.** G_eff (F); the replica construction of ch06, hence ass:dictionary (A); the emergent metric eq:g-from-e (D1); the dimensional conversion noted in ch12.
- **This package.** PROGRAMME-CONDITIONAL; conditional lemmas plus a bounded no-go continuation. No status change.
- **Discrepancies.** None new. The 065 author item (sec:status-G has no "Missing step" paragraph; ch12 dimensional gap not recorded in appH G) is unchanged and, as instructed, not edited here.

## Source reading

Digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT` (HEAD 54a2dcb, dirty-chapters: no, all files unchanged). Read in full: appH sec:status-G L2850-2894 (whole section including the 065 paragraph); ch17 L465-500; ch12 L1-60 and L100-230 (def:HBEV, ass:Sent-density, eq:BY, ass:bdy-EE, thm:Leff); ch03 L160-205 (def:matrix-coords-ext) and L340-360 (ass:dictionary); reports/ledger.md L600-667 (064-066); reports/sme-scout-20261108-after60.md (whole); reports/sme-scout-20261114-1206.md (sections 0 and R1-R4, G lines by grep); proposals/065 proposal-r2.md L1-140, review-r2.md, s4_state_scaling.py, apply_check.py. No full scan: none is required (no definition, assumption, scope or status passage is changed). No file was unreadable.

Scout weighting. The 20261114 scout's R3 (G-derived, avenue 1: spacetime-block subsystem via the symbol map, with an "extensive-vs-area regime test") is the route this package takes on a compact 4D factor. Its literature leads (Karczmarek-Sabella-Garnier 1310.8345; Fliss-Frenkel 2512.03163) were not opened by me and are not cited: not independently verified. Its R4 (Jacobson-Visser fixed-volume partition function) and R5 (centre-based entropy) are listed below as open avenues, not used.

## Research and reasoning

### 1. Setting and why it is the right relaxation

065's bearing (i): "the block is a region of the factor ... its edge is not the boundary dM", with a one-dimensional edge and a rank-one edge map (single row). The cheapest hypothesis to relax without leaving the positive-contraction, compact class (where FFHS's construction exists and 065's lemmas hold) is the dimension: a four-dimensional factor whose blocks have three-dimensional edges. S^2_N x S^2_N with independent deformations A_1, A_2 keeps everything exactly computable and lets the two candidate geometries (induced tensor g, operator tensor K) be told apart, which the round sphere of FFHS could not do (065). Spacetime stays emergent: no metric is introduced; g, K and gt are tensors defined from the configuration and delta_IJ as in def:matrix-coords-ext.

### 2. Edge-operator lemma (exact; e1, e3 Part 0)

Write A_f^a_1 J^1 + A_f^a_2 J^2 = (1/2)(A^a_1 - i A^a_2) J^+ + (1/2)(A^a_1 + i A^a_2) J^-. Theta is diagonal in |i_1, i_2), and J^3 is diagonal, so Theta (J^3-part) Thetabar = 0. Each X^I acts in one factor only, and E sums X^I ... X^I over the same I, so no term mixes the factors. In factor f, Theta X Thetabar X Theta contains
- J^+ Thetabar J^- and J^- Thetabar J^+: diagonal; at site i they give |<i-1|J^+|i>|^2 = i(N-i) if the neighbour i-1 is outside, and (i+1)(N-i-1) if i+1 is outside, with coefficient sum_a |(A^a_1 - iA^a_2)/2|^2 = (1/4) sum_a ((A^a_1)^2 + (A^a_2)^2) = k_f. Since ||col_1||^2 + ||col_2||^2 is the trace of A^T A on the (1,2) plane, k_f = (sigma_1^2 + sigma_2^2)/4, as in 065 for n = e_3.
- J^+ Thetabar J^+ and J^- Thetabar J^-: connect i to i -+ 2 through an outside site i -+ 1 with both ends inside: exactly the excluded pattern. Coefficient sum_a (A^a_1 -+ i A^a_2)^2 / 4 = (||col_1||^2 - ||col_2||^2 -+ 2i col_1.col_2)/4, zero iff A^T A is a multiple of the identity on the plane, i.e. sigma_1 = sigma_2.

Hence the statement. rank(edge map) = rank(E) = number of sites with a nonzero diagonal entry = number of edge sites. Tr E = sum_I ||Theta X^I Thetabar||^2 = (1/2) Tr(Theta Box Theta) (065). Closed forms: for {i_1 < M_1} only the sites i_1 = M_1 - 1 (all i_2) have an outside neighbour, each with E = k_1 M_1 (N - M_1) = s_1^2. For the product block, the M_2 - 1 sites (M_1 - 1, i_2 < M_2 - 1) have E = s_1^2, the M_1 - 1 sites (i_1 < M_1 - 1, M_2 - 1) have E = s_2^2 and the corner has s_1^2 + s_2^2.

### 3. What T measures (e2)

*Pointwise identity (exact).* With K^{mu nu} = theta^{alpha mu} g_{alpha beta} theta^{beta nu} and g = delta_IJ dx^I dx^J: K(df, df) = delta_IJ {f, x^I}{f, x^J}. In coordinates with f = y^0, the cofactor identity gives det_3(K^{-1}|_{ij}) = det(K^{-1}) K^{00}, and det(K^{-1}) = 1/(det theta)^2 det g = rho^4 / det g. So (sqrt g / rho) sqrt(det_3 K^{-1}) = rho sqrt(K^{00}), and (sqrt g/rho) sqrt(det_3 K^{-1}) = sqrt(det_3 gt) for gt = (sqrt g/rho)^{2/3} K^{-1}.

*Cap x whole sphere.* Action-angle coordinates (I_f, phi_f), omega = dI ^ dphi, rho = 1, one site per (2 pi) of dI dphi. f = I_1 - M_1: {f, x} = d_{phi_1} x, |d_{phi_1} x|^2 = R^2 sin^2(theta) |A_1 e_phi|^2. The matrix element X_{i,i+1} is the first Fourier coefficient in phi_1, so E per site is the L^2(phi_1) average, E = (1/2)<|d_phi x|^2>_phi (this is 065's s^2 = (4 pi)^{-1} oint |d_phi x|^2), whereas P_K has the L^1 average. Hence sqrt2 T / P_K = rms/mean >= 1 (Jensen), equality iff the speed is constant, iff sigma_1 = sigma_2. T is the sum over the N fibre sites: the fibre is counted by sites, and A_2 drops out.

*Scalings (exact).* g and K^{-1} are block diagonal; the edge has one direction in factor 1 and two in factor 2. Under A_f -> lam A_f the f-block of g scales by lam^2 and the f-block of K^{-1} by lam^{-2}. This gives the exponents in the Result; gt and P_K reproduce (1, 0).

*Oblique edges.* For a i_1 + b i_2 < c, a >= b >= 0: in each line of fixed i_2 only the last site is an edge site (a site below it has its i_2-neighbour inside because the boundary drops by at most one site per column). It has an outside i_2-neighbour exactly where the boundary steps. Per unit Euclidean length there are n_1 columns and n_2 steps. Hence the densities n_1 (rank), n_1 e_1 + n_2 e_2 (s^2) and (n_1 - n_2) sqrt(e_1) + n_2 sqrt(e_1 + e_2) (T). The inequality is Minkowski's for the vectors (n_1 - n_2)(sqrt e_1, 0) and n_2 (sqrt e_1, sqrt e_2), whose sum is (n_1 sqrt e_1, n_2 sqrt e_2); equality iff one coefficient vanishes. On the round product |d_phi x_f|^2 = 2 e_f and the cross term vanishes, so the right-hand side is the density of P_K / sqrt2. e2 confirms the lattice sums against the integrals at N = 200, 800, 3200.

Interpretation. s^2 (quadratic) has an L^1-type density n_1 e_1 + n_2 e_2 for a sharp projector, and T a crystalline one. Neither is a Riemannian edge volume except in aligned cases. This is a fixed-frame statement about sharp toric projectors.

### 4. Rows of the edge representation (e3)

Q = -2i sum_a (X^a_{S Sbar} Pi^a_{Sbar S} - h.c.) (FFHS Eq. (4.4), as verified in 065) = -2i (Y - Y^dagger). Y maps into range(X_{S Sbar}) = span of edge sites. With U the M x r matrix of edge-site basis vectors, Y = U C; C = alpha U^dagger + C_perp, C_perp U = 0; QR: C_perp^dagger = V R with V^dagger V = 1, V^dagger U = 0. Then Q U = U(-2i)(alpha - alpha^dagger) + 2i V R, Q V = -2i U R^dagger, and Q vanishes on the complement: the stated block matrix. For alpha = 0 its square is diag(4 R^dagger R, 4 R R^dagger). Tr Q = 4 Im Tr alpha is the U(1) charge; it vanishes on the constraint surface, and is not imposed in the Monte Carlo (stated in the text).

Gaussian momenta with <pi_{lm} conj pi_{l'm'}> = f delta delta in the basis Y_{l_1 m_1} (x) Y_{l_2 m_2}: <Pi_{vj} conj Pi_{v'j}> requires equal weights v - j = v' - j, so D is diagonal. Two links into the same outside site belong to different factors (the same-factor case is the excluded pattern), and their coefficient vectors c^a are supported on different a, so <Y Y^dagger> = sum over links of kappa D_v on the diagonal. For the cap x whole sphere the sum over j of the second factor runs over a full row, so the Schur row-sum identity of 065 gives the factor (2 l_2 + 1)/N, uniformly in i_2.

Monte Carlo: sum of positive eigenvalues of Q against 2 Tr <Y Y^dagger>^{1/2} = 2 sqrt(W) T: ratios 0.85 (l_c1 = 3), 0.94, 0.93, 0.95. The deficit is the Jensen gap plus the edge-site part of the row (W_perp/W = 0.65 at l_c1 = 3, 0.88-0.89 otherwise). The rows are not equal (relative spread 0.3): the diagram is not an exact rectangle; the equal-row dimension in item 8 is therefore an idealisation, stated as such in the closing sentence ("equal rows for the dimension").

### 5. Dimension (e4)

Weyl formula for (ell^r, 0^{M-2r}, (-ell)^r), cross-checked against the hook-content formula for one-sided rectangles and against dim(adjoint) = M^2 - 1. For a one-sided rectangle the hook sum gives log d ~ r ell [log M - ((r+ell)^2 log(r+ell) - r^2 log r - ell^2 log ell)/(2 r ell) + 3/2], i.e. r ell [log(M/(r+ell)) + c] with c -> 1 for r << ell (FFHS's log(eM/ell)) and c = 3/2 - log 2 = 0.807 at r = ell; the two-sided numerics give 0.80 < c < 0.97. This asymptotic form is my estimate; the text states only the numerical range.

### 6. Fork: hypotheses of the remaining obstruction, and what each avenue gave

| # | Hypothesis the obstruction depends on | Relaxation | Explored here | Outcome |
|---|---|---|---|---|
| H1 | one-dimensional edge, rank-one edge map (065) | 4D factor, 3D edge | yes | removed: rank = number of edge sites; boxes follow T |
| H2 | "area" = induced area | compare g, K^{-1}, conformal classes | yes | measure is P_K-type: 3-volume of gt only in aligned, constant-speed cases |
| H3 | fixed toric frame, sharp projector | oblique toric blocks | partly | crystalline anisotropy up to 11%; non-toric projectors and the frame average not done |
| H4 | rank dependence |mu| log M | multi-row diagrams | yes | weakened to log(M/(r+ell)) (depth), not removed; sub-additive in r |
| H5 | supplied state | e^{-S/2} on the Euclidean weight; OS reconstruction | no (065 did the first) | open |
| H6 | positive contraction, compact factor | Lorentzian / non-compact block | only the remark that Q has no contraction and delta enters via the variance | open |
| H7 | no map to eq:g-from-e | A, D1 | no | open (depends on other critical-path problems) |
| H8 | leading-order saddle of FFHS | subleading terms; other entropies | no | open |

Ranked open avenues (for follow-up packages):
1. **Mutual-information / relative combinations that cancel the depth dependence** (H4). log d ~ |mu| log(M/(r+ell)) suggests testing S(Sigma_1) + S(Sigma_2) - S(union) for nested or adjacent toric blocks sharing an edge; this needs the two-sided multi-row diagrams and the entropy of the off-diagonal sector (the complement of a block is not a block). Highest value: it is the only route found that could turn the functional into a boundary-local one.
2. **Frame average and non-toric projectors** (H3): whether the minimisation over frames of FFHS removes the crystalline anisotropy (a Wulff-type problem for the density of item 6) and selects gt.
3. **Fixed-volume Euclidean partition function** (scout 20261114 R4, Jacobson-Visser): independent of the factorisation route; uses rho = 1/|Pf theta| as the volume constraint. Not examined here.
4. **Within-core state** (H5): e^{-S/2} for the product factor, where the kinetic operator Box_1 + Box_2 makes W depend on A_2 and could change the fibre weighting from site-counting; OS reconstruction on fibre modes (065 avenue 2).
5. **Non-compact / Lorentzian block** (H6), e.g. a block of M x K product backgrounds: the lemma of section 2 extends to any configuration that is tridiagonal in a joint eigenbasis, but with an indefinite variance the Gaussian state does not exist (065).
6. **Centre-based / algebraic entropy** (scout R5) and the 2303.08012 vacuum term (065 avenue 6).

### 7. Literature

Only arXiv:2408.05274 (SciPost Phys. 18, 171 (2025)) is used, for Eq. (4.4) and the leading-order entropy log d_mu, both as verified from the source in 065; it is already in bib/namcg.bib (key FlissFrenkelHartnollSoni2025). No new reference. Scout leads 1310.8345, 2512.03163, 2212.10607: not independently verified, not cited.

### 8. Comparison with the original target

The target is a local density on dM of emergent spacetime, from the replica construction, plus stationarity. This package shows that on a 4D positive-contraction factor the FFHS edge functional has an edge-extensive coefficient with an identified measure, but remains non-local through the depth, frame-dependent, state-dependent and unrelated to eq:g-from-e. It does not derive any part of the target.

## Claim classification

| Claim | Class |
|---|---|
| Edge-operator lemma; rank; closed forms for cap x sphere and product blocks | established (exact, finite N) |
| Off-diagonal entry in the excluded pattern iff sigma_1 != sigma_2 | established (exact) |
| Pointwise identity rho sqrt(K(df,df)) = 3-volume density of gt | established (exact) |
| sqrt2 T / P_K = rms/mean >= 1 for cap x sphere | established (Poisson-limit kinematics with M(N-M) -> (N sin theta / 2)^2) |
| Scaling exponents of T, P_K, Vol_g, Vol_{K^{-1}} | established (exact) |
| Half-plane densities and the Minkowski inequality | established (counting argument); lattice sums checked numerically |
| Charge reduction to a 2r x 2r matrix | established (exact) |
| <Y Y^dagger> diagonal; uniform W for cap x sphere | established (exact, for the stated Gaussian class) |
| boxes per side ~ 2 sqrt(W) T | numerical (N = 16, 60 samples, 5-15%) |
| log d = 2 r ell [log(M/(r+ell)) + c], 0.80 < c < 0.97; sub-additivity in r | numerical (exact formula evaluated) |
| "log d_mu is not an integral of a local edge density" | conditional (leading-order FFHS entropy, fixed frame, equal rows) |
| state, cut-offs, frame | supplied inputs |
| relation of gt to eq:g-from-e; frame minimisation; Lorentzian block | unresolved |

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`. One insertion, nothing replaced or removed.

**Anchor (occurs once; checked by `apply_check.py`):** the closing sentence of the 065 paragraph followed by the Problem H header,

    ...Assumptions~\ref{ass:Sent-density} and~\ref{ass:bdy-EE} are not discharged, and Problem~G remains open and PROGRAMME-CONDITIONAL.
    <blank line>
    \section{Problem H: modular origin of the interpolating function}

Insert after that sentence (line 2894) a blank line and the block below; the existing blank line and the Problem H header follow. All existing text of sec:status-G is kept.

The exact text is `proposals/067-product-sphere-edge/appH_insert.tex` (LF, ASCII, 10606 bytes, sha256 4ee4d8920f7bd8c5e4cbb9516036cf175cf8fdee9c6bb2d96e82cbe8a5b6bb52); the integrator converts to CRLF. Resulting appH: 634866 bytes, sha256 e098f9812e0058f6133f17f83866e2bd039769d9ca74849c3ba1c9c7f5e14d1a, 3405 CRLF, 0 bare LF. The block is reproduced here; the file is authoritative.

```latex
\paragraph{Edge of a toric block on a product of two fuzzy spheres (conditional; bounded).}
Take the six Hermitian \(N^2\times N^2\) matrices \(X^I=(A_1{}^a{}_bJ^b\otimes1,\;1\otimes A_2{}^a{}_bJ^b)\), with \(A_1,A_2\) real and invertible, \(J^b\) the \(N\)-dimensional irreducible representation of \(\mathfrak{su}(2)\) and the positive contraction \(\delta_{IJ}\); this is a compact four-dimensional fuzzy factor. Let \(|i_1,i_2)\), \(0\le i_f\le N-1\), be the joint eigenvectors of \(J^3\otimes1\) and \(1\otimes J^3\), with eigenvalues \(\tfrac12(N-1)-i_f\), and let \(\Theta\) be the projector on a set \(\Omega\) of sites \((i_1,i_2)\), called here a toric block; the spectral projectors of \(a\,J^3\otimes1+b\,1\otimes J^3\) are of this form. In the Poisson limit the edge of such a block is three-dimensional, the dimension of \(\partial M\) in Definition~\ref{def:HBEV}, whereas the cap of the preceding paragraph has a one-dimensional edge.

\emph{Edge operator.} Suppose that no line of sites in either lattice direction meets \(\Omega\) in the pattern inside, outside, inside on three consecutive sites. Then \(E\equiv\sum_I\Theta X^I\bar\Theta X^I\Theta\) is diagonal in \(|i_1,i_2)\), and its entry at a site of \(\Omega\) is the sum, over the nearest-neighbour links from that site to sites outside \(\Omega\), of \(\kappa=k_f\,i(N-i)\) for a link between \(i-1\) and \(i\) in factor \(f\), with \(k_f=\tfrac14(\sigma_{f,1}^2+\sigma_{f,2}^2)\) and \(\sigma_{f,1,2}\) the singular values of \(A_f\) on the plane orthogonal to the third axis (exact). So the rank of the map \(\mathcal E=(\Theta X^I\bar\Theta)_I\) is the number of edge sites, the sites of \(\Omega\) with a neighbour outside; \(s^2=\operatorname{Tr}E\) is the squared norm of the preceding paragraph, and \(T\equiv\operatorname{Tr}E^{1/2}\) is the trace norm of \(\mathcal E\). If the pattern occurs in factor \(f\), \(E\) has an entry between the two inside sites proportional to \(\sum_a(A_f{}^a{}_1-\mathrm iA_f{}^a{}_2)^2\), which vanishes only for \(\sigma_{f,1}=\sigma_{f,2}\) (exact). For the cap times the whole second sphere, \(\Omega=\{i_1<M_1\}\), the rank is \(N\) and \(E=s_1^2\) on each of the \(N\) edge sites, with \(s_1^2=k_1M_1(N-M_1)\), so
\[
T=N\,s_1,\qquad s^2=N\,s_1^2,
\]
both independent of \(A_2\) (exact). For the product block \(\Omega=\{i_1<M_1,\ i_2<M_2\}\) with \(M_f<N\) and \(s_f^2=k_fM_f(N-M_f)\), the rank is \(M_1+M_2-1\), \(s^2=M_2s_1^2+M_1s_2^2\) and \(T=(M_2-1)s_1+(M_1-1)s_2+(s_1^2+s_2^2)^{1/2}\) (exact).

\emph{Measure.} Let \(x^I\) be the symbols, \(\theta^{\alpha\beta}\) the Poisson bivector, \(\rho=1/|\operatorname{Pf}\theta|\), and let \(g_{\alpha\beta}\) and \(K^{\mu\nu}\) be the induced tensor and the operator tensor defined as in Definition~\ref{def:matrix-coords-ext} with \(\delta_{IJ}\) in place of \(\eta_{IJ}\). For a function \(f\), \(K^{\mu\nu}\partial_\mu f\partial_\nu f=\sum_I\{f,x^I\}^2\), and
\[
P_K\equiv(2\pi)^{-2}\int\mathrm d^4y\,\rho\,\delta(f)\,\bigl(K^{\mu\nu}\partial_\mu f\,\partial_\nu f\bigr)^{1/2}
\]
is \((2\pi)^{-2}\) times the three-volume of \(\{f=0\}\) in the tensor \(\tilde\gamma_{\mu\nu}=(\sqrt g/\rho)^{2/3}(K^{-1})_{\mu\nu}\), with \(\sqrt g=(\det g_{\alpha\beta})^{1/2}\) (exact, a pointwise identity; the normalisation is one site per volume \((2\pi)^2\) of \(\rho\,\mathrm d^4y\)). For the cap times the whole second sphere, with \(M_1(N-M_1)\to(\tfrac12N\sin\theta)^2\) as in the preceding paragraph, \(\sqrt2\,T/P_K\) is the ratio of the root mean square to the mean of the speed \(|\partial_{\phi_1}x|\) over the angle \(\phi_1\) of the flow that generates the cut; it is at least \(1\), with equality only for \(\sigma_{1,1}=\sigma_{1,2}\). Under \(A_1\to\lambda A_1\) and under \(A_2\to\lambda A_2\), \(T\) and \(P_K\) scale as \(\lambda\) and \(\lambda^0\), the three-volume of the edge in \(g\) as \(\lambda\) and \(\lambda^2\), and that in \(K^{-1}\) as \(\lambda^{-1}\) and \(\lambda^{-2}\) (exact). So \(T\) weighs the directions of the edge that are transverse to that flow by the number of sites, that is by the symplectic volume, and only the direction of the flow by a length in the induced tensor; it is the three-volume of the edge neither in \(g\) nor in \(K^{-1}\). For a half-plane block \(a\,i_1+b\,i_2<c\) with \(a\ge b\ge0\) on the round product, \(A_f=\nu_f1\), the edge sites are the last sites of the lines of fixed \(i_2\), and such a site has a second outside neighbour where the boundary steps. Per unit Euclidean length of the boundary line in the plane of \((i_1,i_2)\), with unit normal \((n_1,n_2)\) and \(e_f=k_fi_f(N-i_f)\), the number of edge sites is therefore \(n_1\), the density of \(s^2\) is \(n_1e_1+n_2e_2\), and the density of \(T\) is
\[
(n_1-n_2)\,e_1^{1/2}+n_2\,(e_1+e_2)^{1/2}\;\ge\;\bigl(n_1^2e_1+n_2^2e_2\bigr)^{1/2},
\]
the right-hand side being the density of \(P_K/\sqrt2\); equality holds only for \(n_2=0\) and for \(n_1=n_2\). At \(N=3200\) the lattice sums agree with the integrals of these densities to \(10^{-4}\), and \(\sqrt2\,T/P_K\) is \(1.113\) and \(1.096\) for \(b/a=\sqrt2-1\) and \(3^{-1/2}\), with \(\nu_2/\nu_1=1.6\) and the line through the centre of the square (numerical). At a fixed toric frame \(T\) is therefore a functional of the edge that depends on its direction relative to the lattice of sites, and it is not the volume of the edge in a quadratic form.

\emph{Rows.} The classicalised charge of~\cite{FlissFrenkelHartnollSoni2025} is \(Q=-2\mathrm i(Y-Y^\dagger)\) with \(Y=\sum_aX^a_{\Sigma\bar\Sigma}\Pi^a_{\bar\Sigma\Sigma}\); it contains no contraction of the directions. The range of \(Y\) lies in the span of the \(r\) edge sites; let \(U\) be the matrix of their basis vectors, \(C=U^\dagger Y\), \(\alpha=CU\) and \(C_\perp=C(1-UU^\dagger)\). For \(2r\le M\) the nonzero spectrum of \(Q\) is that of the Hermitian matrix with blocks \(-2\mathrm i(\alpha-\alpha^\dagger)\), \(-2\mathrm iR^\dagger\), \(2\mathrm iR\), \(0\), where \(R^\dagger R=C_\perp C_\perp^\dagger\); for \(\alpha=0\) it is \(\pm2\) times the singular values of \(C_\perp\) (exact). Take Gaussian momenta, independent in \(a\), with variance \(f(l_1,l_2)\) on the matrices of spins \((l_1,l_2)\) under the two adjoint actions. Then \(\langle YY^\dagger\rangle\) is diagonal on the edge sites, with entry the sum over the links to outside sites \(v\) of \(\kappa\,D_v\), \(D_v=\sum_{j\in\Omega}\langle|\Pi_{vj}|^2\rangle\) (exact); the contraction \(\delta_{IJ}\) in \(E\) is that of this variance. For the cap times the whole second sphere \(D_v=W\equiv\sum_{l_1,l_2}f(l_1,l_2)\,(2l_2+1)N^{-1}w_{l_1}\) on every such link, with \(w_{l_1}\) the sum over the boundary row inside the cap of the squared entries of the spin-\(l_1\) matrices of the first factor, so \(\langle YY^\dagger\rangle=s_1^2W\) on the \(N\) edge sites (exact). At \(N=16\), \(M_1=8\), \(A_f\) multiples of the identity and \(f=\tfrac12l_1\) for \(l_1\le l_{c1}\), \(l_2\le l_{c2}\) and zero otherwise, the sum of the positive eigenvalues of \(Q\), in units of \(2Ns_1W^{1/2}=2W^{1/2}T\), is \(0.85\), \(0.94\), \(0.93\), \(0.95\) for \((l_{c1},l_{c2})=(3,3),(8,3),(15,3),(15,8)\), with sixteen positive eigenvalues whose standard deviation is \(0.3\) of their mean in the last three cases (numerical, \(60\) samples, momenta not constrained to \(\operatorname{Tr}Q=0\)). In this regime the number of boxes of the diagram on each side is therefore close to \(2W^{1/2}T\): it follows \(T\), which here is \(N^{1/2}s\), and not \(s\).

\emph{Dimension.} For the highest weight of \(U(M)\) with \(r\) rows of length \(\ell\) and \(r\) rows of length \(-\ell\), the Weyl dimension formula gives \(\mathrm d\log d/\mathrm d\log M=2r\ell\) to within \(2\%\) for \(M\ge4000\), \(r\le160\), \(\ell\le40\), and \(\log d=2r\ell\,[\log(M/(r+\ell))+c]\) with \(0.80<c<0.97\) for \(1\le r\le160\), \(4\le\ell\le400\), \(M=4000\) and \(16000\); for \(r>1\) this is below \(r\) times the value for one row on each side, by a factor between \(0.69\) and \(0.98\) in that range (numerical). For the cap times the whole second sphere, \(M=M_1N\) and \(r=N\): at \(M_1=50\), \(\ell=30\), \(\log d/(2N\ell)\) rises from \(3.38\) at \(N=10\) to \(4.60\) at \(N=160\), against \(\log M_1=3.91\) (numerical). The rank of the block thus enters through \(M/(r+\ell)\), which for \(\ell\ll N\) is the depth \(M_1\) of the block behind its edge.

\emph{Bearing on Assumption~\ref{ass:Sent-density}.} (i) On this four-dimensional factor the number of boxes, the coefficient of the logarithm in \(\log d_\mu\), is, within the accuracy of the numerical comparison above, a sum over the sites of a three-dimensional edge of a quantity fixed by the links at that site and by the row sums \(D_v\) of the state; the single row of the preceding paragraph was special to a one-dimensional edge. (ii) The measure of that sum is \(T\) weighted by the state. It coincides with a volume, that of \(\tilde\gamma\) up to the factor \(\sqrt2\,(2\pi)^2\), only for an edge along a lattice direction or along the diagonal, with constant speed along the flow; \(\tilde\gamma\) is not the induced tensor, is not \(K^{-1}\), and is not identified with the metric of Equation~\eqref{eq:g-from-e}, whose relation to the matrix configuration rests on Assumption~\ref{ass:dictionary} and Problem~D. (iii) The dependence on the rank remains, through \(\log(M/(r+\ell))\), and the value for \(r\) rows is not \(r\) times the value for one row, so at this order \(\log d_\mu\) is not the integral over the edge of a density fixed by local data of the edge (conditional on the leading-order entropy of~\cite{FlissFrenkelHartnollSoni2025}, at fixed frame). (iv) The row sums \(D_v\), the cut-offs and the frame are supplied, as in the preceding paragraph, and the factor is compact with a positive contraction.

These statements are for the product of two deformed fuzzy spheres with positive contraction, toric blocks at one fixed frame without the excluded pattern, Gaussian momenta with the stated variances, equal rows for the dimension, and the leading semiclassical order of~\cite{FlissFrenkelHartnollSoni2025}; the frame average and its minimisation, projectors that are not toric, a block of a non-compact or Lorentzian factor and the state are not treated. They derive no entropy density on \(\partial M\), no value or scaling of \(S_{\mathrm{ent}}^{\mathrm{(IR)}}\), no boundary stationarity and no \(\Lambda_{\mathrm{eff}}\); Assumptions~\ref{ass:Sent-density} and~\ref{ass:bdy-EE} are not discharged, and Problem~G remains open and PROGRAMME-CONDITIONAL.
```

**Labels referenced (each exists exactly once):** ass:Sent-density, ass:bdy-EE (ch12); def:HBEV (ch12); def:matrix-coords-ext, ass:dictionary (ch03); eq:g-from-e (ch04). No new label. Cite key FlissFrenkelHartnollSoni2025 exists once in bib/namcg.bib. No bib change.

**Stale passages elsewhere:** none. The 065 paragraph's bearing (i) ("its edge is not the boundary dM") and (ii) remain true for the single cap it treats; the new paragraph says explicitly that the single row was special to a one-dimensional edge. The closing status sentence appears once in the new block; the 065 paragraph keeps its own.

**Build.** Scratch build outside the repository with the would-be appH: pdflatex, bibtex, pdflatex, pdflatex all exit 0; 384 pages; 0 undefined, 0 multiply defined; 24 overfull hboxes (same as the 065 record). See `build_r1.txt`.

## Verification scripts

All in `proposals/067-product-sphere-edge/`; all print to stdout only and end with PASS; saved outputs alongside. Run from the repository root with the system `python` (numpy 2.4.6).

| Command | Checks | Expected invariant output |
|---|---|---|
| `python proposals/067-product-sphere-edge/e1_edge_operator.py` | E diagonal and equal to the link formula for product, half-plane and two-disc blocks (N = 6, 9, 12, generic A); Tr E = (1/2)Tr(Theta Box Theta); T; rank = edge sites; product closed forms; off-diagonal entries in the excluded pattern iff non-conformal A | `max deviation over gap-free cases: 2.84e-14`; single-gap rows `offdiag=1.2e+01` (non-conformal) and `0.0e+00` (conformal); `PASS e1` (output identical to `e1_edge_operator_output.txt`) |
| `python proposals/067-product-sphere-edge/e2_perimeter.py` | (A) pointwise identities; (B) T = N s_1, sqrt2 T/P_K = rms/mean, P_K = (2 pi)^{-2} Vol_3[gt] by quadrature, scaling exponents; (C) half-plane densities at N = 200, 800, 3200 | `(A) ... max relative deviation 1.60e-11`; exponents `(+1,+0)`, `(+1,+2)`, `(-1,-2)`, `(+1,+0)`, `(+1,+0)`; `T/T_cryst=1.00000` at N = 3200; `T/(P_K/sqrt2)=1.11267`, `1.09592`, `1.02160`; `PASS e2` |
| `python proposals/067-product-sphere-edge/e3_charge_rows.py` | Part 0: cap x sphere at operator level (rank N, A_2-independence); Part 1: exact second moments, D diagonal, <YY^+> = diag(Et), uniform W; Part 2: spectrum of Q = spectrum of the reduced matrix; Part 3: Monte Carlo ratios | Part 0 `max dev 7.1e-15`; Part 1 deviations <= 1.1e-13; Part 2 <= 6.4e-14; Part 3 column `<sum pos Q>/(2 N s1 sqrt W)` = 0.8537, 0.9438, 0.9346, 0.9512, `cv(rows)` = 0.584, 0.298, 0.301, 0.310; `PASS e3` (seeded) |
| `python proposals/067-product-sphere-edge/e4_dimension.py` | Weyl vs hook-content; slope, c, sub-additivity; cap x sphere at fixed depth | `max |difference of logs| = 2.8e-14`; c between 0.8065 and 0.9604; ratio column between 0.6917 and 0.9820; (iv) 3.3811 ... 4.6006; `PASS e4` |
| `python proposals/067-product-sphere-edge/apply_check.py` | baseline hash, unique anchor, insertion, CRLF, refs, cite, balance, no process language | `anchor occurrences: 1`; `result appH: 634866 e098f981...`; `APPLY CHECK PASS` |

Note on Part 1 of e3: the "two corner blocks" case has Re<Tr Y^2>/<Tr YY^+> = +0.05, the other cases 0.0000; this ratio is reported, not used.

## Decisions Taken

1. **Which relaxation to compute first:** the compact 4D product factor with toric blocks, rather than a non-compact Lorentzian block. Reason: it isolates the dimension of the edge (065's first cause) while keeping FFHS's construction and all 065 lemmas valid, and it is exactly solvable. Rejected for this package: a block of the doubleton / M x K background (no positive Gaussian state; 065), and the Jacobson-Visser route (independent method; queued as avenue 3).
2. **T, not s, as the reported functional.** The multi-row analysis shows the number of boxes follows the trace norm. s is kept for continuity with 065.
3. **gt is stated as an identity, with no name from the literature.** The manuscript does not define a conformally rescaled effective metric; importing one would add an unverified citation. Rejected: citing a literature "effective metric".
4. **The 065 paragraph is not edited.** Its statements are correct for the single cap; the new paragraph records what changes in 4D.
5. **No status-passage edit** (the Missing-step item of ledger 065 is left for a later package with a full scan, as instructed).
6. **Equal-row idealisation for the dimension** is stated in the scope sentence rather than replaced by sampled diagrams; the rows' 30% spread does not change the leading |mu| log M term (065, exact for any fixed diagram).

## Milestone assessment

Routine. It is a conditional sharpening and a bounded no-go continuation on a compact positive-contraction factor: no critical-path step is derived (not M1), no class of routes kept open by the manuscript is ruled out beyond 065 (not M2), no merged claim is found wrong (not M3), no label or scope change is proposed (not M4, M5). Not a breakthrough candidate.

## Status-label recommendation

Critical-path set from ch17 and appH at HEAD: A, B, C, D (D1), E, F, G (derived level), N, all OPEN. Affected label: G only; **unchanged** (OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL). No label edit is proposed.

## Author decision needed

None.

## Remaining open step

To close G-derived one still needs, from the matrix theory: (1) a subsystem or partition-function construction whose entropy is a local density on the boundary of a region of the emergent spacetime, with no dependence on the depth/rank (here log(M/(r+ell)) remains) and no dependence on a supplied frame; (2) a state or weight fixed by the integral (here supplied); (3) the identification of the measure with sqrt|h| of eq:g-from-e (here gt at best, in special cases; this needs A and D1); (4) the expansion eq:Sent-exp with its coefficients; (5) boundary stationarity ass:bdy-EE; (6) Lambda_eff from eq:Leff including the ch12 dimensional conversion. The ranked avenues are in section 6 above; the first is the mutual-information-type combination for adjacent toric blocks.

## Special instructions for the gatekeeper

- Do not read item (a)/(i) as a derivation of a boundary density: the edge-extensive statement concerns the coefficient |mu| only, rests on a Monte Carlo comparison at N = 16 (5-15% accuracy, unconstrained Tr Q) and on a supplied Gaussian state.
- The equality "T = Vol_3[gt]/(sqrt2 (2 pi)^2)" holds only for aligned or diagonal edges with constant speed; the diagonal case was checked on the round product only. Please re-derive the cofactor step of the pointwise identity and the Minkowski step.
- The asymptotic form of c in section 5 (0.807 at r = ell) is my estimate and is not in the manuscript text; the text gives the numerical range only.
- Check the counting argument for half-plane blocks (a >= b >= 0): one edge site per column, a second outside neighbour exactly at steps.
- delta_IJ replaces eta_IJ of def:matrix-coords-ext explicitly; nothing is claimed for a Lorentzian contraction.
- e3 Part 3 uses a separable variance; Part 1 uses a non-separable one. The uniform-W formula is exact for both.
- No full scan was done and none is claimed. Integration ordinal: check the ledger for whether the 5th-item scan is due.
- `apply_check.py` writes nothing into the repository; with an argument it writes the would-be appH to a directory outside it.
