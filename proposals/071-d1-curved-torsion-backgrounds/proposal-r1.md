# Proposal 071-d1-curved-torsion-backgrounds, round 1

## Result

**What is established.**
1. **Exact backgrounds with curvature and torsion both nonzero.** In the first-order equivariant class, on left-invariant data with a *nonzero constant* connection `w_a^{cd}`, two explicit families solve the first two brackets of the matrix equation exactly, for symbolic parameters, with `R != 0` and `T != 0`. (i) A flat frame (`c = 0`, frame metric Minkowski) with `w = s k (x) B + m (x) N`, on the hyperbola `(m_1 - s)^2 - m_3^2 = s^2`. (ii) Time x Heisenberg (`[E_3,E_1] = kappa E_2`) with `w = k (x) (zeta N + x N')`. Here `k_a = (1,0,1,0)` is null, `B` is the boost in the 0-2 plane, and `N, N'` are null rotations fixing `n = -k`. Both families have rank-one, null-type curvature (`R_abcd R^abcd = 0`) with nonzero Ricci tensor `R_ab^{ae}`, which the torsion terms cancel in the first bracket. The third bracket holds: (ii) and the trace-free point of (i) need `t = 0`, and the general point of (i) has `F = -c t = 0`. This supplies the missing input that the frontier edge names: "a background with both R != 0 and T != 0 that solves the matrix equation (no source read supplies one)". The section values were also checked at the operator level, on the bundle, against the vector fields themselves.
2. **Linearised equations at `R != 0` on family (i).** These generalise (R1)/(R2) of the integrated 068 paragraph:
   - The translation labels still reduce exactly to the gauge-invariant order-zero operator `Q`, which now contains the connection. The labels carry a connection part `omega = -f w_I`.
   - (R1) fails: the connection equations depend on `h`.
   - The forty equations remain block-triangular in the variables `(f, omega')`. The 24-equation connection block `Y` has generic rank 18 and is not six copies of `Q`.
   - The kernel is the ten gauge directions. The diffeomorphism directions now need the term `omega = xi^c R_ca`.
3. **No gauge-invariant mass or gap on family (i)** (hazard F3 respected).
   - Every characteristic root found lies on a null cone shifted along `k`: `(q - alpha k)^2 = 0`, with `alpha` in a finite set (numerical).
   - The background has an exact boost-dilation symmetry, under which `w -> e^{-theta} w`. Because of it, the set of values of `q^2` on the characteristic variety is invariant under every positive rescaling. So no mass shell `q^2 = -m^2` is isolated, and the background has no invariant scale (rigorous, given the symmetry).
   - The non-derivative terms are nonzero, but they produce cone shifts, not masses.
   - Imaginary shifts give section values that grow along the null coordinate `k.y`. No norm is used, so no stability claim is made.

**What is not established.** None of this closes D1. The class, its algebra `A`, these backgrounds, the frame and its non-degeneracy are not selected by the matrix integral. There is no norm and no regulated trace, and everything is tree level and linear order. Family (ii) and the non-null survey solutions are not linearised. Problems D, F and N remain OPEN and PROGRAMME-CONDITIONAL.

## Target and status

- **Problem:** D (D1 route), `sec:status-D`. Ledger (appH L718-721): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2 ... D remains OPEN and the matrix-derived criterion is unmet."
- **Original target** (ch17 L330-343, L650-653, L712-716): derive local SO(3,1) from the matrix algebra and condensate, specify the `omega, A_mu, B` and ghost operators and the field content, and derive the existence and non-degeneracy of the locked frame.
- **Missing step** (appH L745-756): "derive the effective dynamics of the independent diagonal connection or retain it as unresolved field content. Generator counting alone does not settle its torsion or propagating modes." This package attacks the "torsion or propagating modes" item. It does so on the first backgrounds where the 068 reduction (R1) can fail, which is the gap named in the 068 review (avenue (c)).
- **Dependencies:** ch17 L650-653: D1 supplies the operators consumed by F. F gates N, and C is tied to F through `G_eff` (appH L712). D1 is the upstream gating problem, so it was attacked first, per the derivation-first directive.
- **Completion classification:** PROGRAMME-CONDITIONAL (unchanged).
- **Discrepancies between ch17 and appH:** none found for D. The CRITICAL PATH OPEN set at full-GR scope is A, B, C, D, E, F, G, N (8). H, I and J are OPEN and OPTIONAL (3). The total is 11 OPEN, and all are unchanged by this package.

## Source reading

- **Mode:** digest + targeted reads. `make_digest.py --check` printed `DIGEST CURRENT`. The digest flags `dirty-chapters: yes`, because appH and bib are uncommitted from the 068/069 integrations. The live appH sha256 is `d8d8b678...9180`, which matches the dispatch.
- **Read in full:**
  - appH L715-760 (the Problem D ledger, the missing step and the opening);
  - appH L1496-1630: the conjugate-coordinate frame-index paragraph, the class paragraph, the pairing/commutant paragraph, the one-loop/reflected-form paragraph, the 059 compact toy, the locked-frame composite, and the 068 paragraph;
  - ch17 L328-371 (Problem D) and L645-716 (order and criteria);
  - ch10 L1-310 (groups, locking, eq:dressed-omega, prop:B-torsion-free).
- **Labels used and verified** (each defined once in `chapters/*.tex`): `eq:Smatrix`, `ass:frame-lock`, `ass:nondeg`, `ass:lorentzian`, `ass:local-lorentz`, `ass:EFT-a2`, `ch:vierbein-emergence`.
- **Other sources read:** the 068 proposal folder (core.py and tools.py, copied here as `core068.py`/`tools068.py`), its review-r2-final, `reports/pathfinder/plan-2026-11-21b.md`, and the frontier edge `D1.R-T-nonzero-backgrounds` (used as a pointer only).
- **No full scan.** This package changes no definition, assumption, scope statement or status passage.

## Research and reasoning

### 1. Class reduction for left-invariant data with constant connection
- **Setup.** Take a 4-dim Lie group with `[E_a,E_b] = c_ab^d E_d` and constant connection components `w_a^{cd}`. Then `Om_ab^c = w_a^{cd} eta_db`, `T = -c - Om + Om^T` and `R_ab^f_c = Om Om - Om Om - c Om`. These are constants. The brackets reduce to polynomial equations (bg.py):
  - `B1 = -nabla^a T_ab^e + T T + R_ab^{ae}`;
  - `B2 = nabla^a R - T R`, where `nabla` acts algebraically through `Om`.
- **Operator-level check (s0).** The formulas were checked independently on the bundle, which is embedded in `G x GL(4)`. There `S_cd` acts on the first index of `u` and `D_a = u_a^b(E_b + (u Om_b) d/du)`. The check covers four things:
  - the first relation;
  - `T(u)` and `R(u)` read off from `[D_a,D_b]`, compared with the Lorentz-rotated section values;
  - the vector field `eta^{ac}[D_c,[D_a,D_b]]` at random Lorentz `u`;
  - a control (random `W`, not a solution), which gives a residual of 78-140.
- **Hermiticity.** For trace-free torsion `t = 0`. Otherwise `t_a = 1/2 T_ac^c` (constant section values). Since `[V_a+t_a, V_b+t_b] = [V_a,V_b] + V_a t_b - V_b t_a`, we get `F_ab = nabla_a t_b - nabla_b t_a + T_ab^c t_c`. With constant components, `nabla_a t_b = Om_ab^c t_c`, so `F_ab = (Om_ab^c - Om_ba^c + T_ab^c) t_c = -c_ab^c t_c`, which is zero on a flat frame. The `t` part enters only the third bracket.

### 2. Search and exact families
- **Least-squares survey (s3, numerical).**
  - Flat frame, `eta`: 59 of 60 starts converge and 56 of them have `R != 0`, all with `R_abcd R^abcd = 0` (to `3e-15`).
  - Flat frame, Euclidean: no start converges. This is numerical, not a proof. A trace identity was tested and `tr B1` is not sign-definite.
  - With `c` free and Jacobi imposed: 4 stored solutions on algebras with a 2-dim abelian derived algebra. Three of them have `R_abcd R^abcd != 0` (`-7e-4`, `9e-4`, `-4e-3` at `|R| ~ 0.1`).
- **Sparse/ansatz search.** It found two clean families. Both are verified exactly by `s1_backgrounds.py` (sympy, symbolic in `s, m1, m3 / tau, kappa, zeta, x`).
  - **(i)** Ansatz `w = s k B + m N`, `m = (0,m1,0,m3)`. Here `B2 == 0` identically and `B1 ∝ m1^2 - 2 m1 s - m3^2`. The rational parametrisation is `m1 = s(1+(tau+1/tau)/2)`, `m3 = s(tau-1/tau)/2`. Then:
    - `R_ab^{cd}` takes values on the line of N, has rank 1, with entries `s m1`, `s m3`; so `R != 0` iff `s != 0` and `m != 0`;
    - `R_abcd R^abcd = 0`, `T_abc T^abc = 0`, `R_ab^ab = -2 s m1`;
    - the trace is `(s+m1) k`, which is trace-free at `tau = -2+sqrt3`, i.e. `m = (0,-s,0,sqrt3 s)`;
    - the Ricci tensor is nonzero.
  - **(ii)** Heisenberg family. The general `k (x) X` ansatz leaves the second bracket equal to `k_2 kappa X (x)` (four linear forms). Solving those forms for `k = (1,0,1,0)` gives `X in span(N, N', B)`. Every `B1` entry then also vanishes for `X = zeta N + x N'`, which is exact for symbolic `kappa, zeta, x`. Then:
    - the only nonzero curvature pair is `R_13^{cd} = kappa(zeta N + x N')`;
    - `T_abc T^abc = 2 kappa^2`, the torsion is trace-free, and `RR = R_ab^ab = 0`.
- **Explored avenue: isotropic backgrounds** (x1, x1b; exact).
  - Flat frame with the general SO(3)-invariant constant connection `w_i = alpha J_i + beta K_i`: `B1_00 = 3 s beta^2`, so `beta = 0`, and then `B1_ii = -6 alpha^2`, so there is no solution.
  - R x S^3 with static isotropic torsion: `B1_00` forces `beta = 0`, and then `-2 kappa^2/a^2 + 6 kappa alpha/a - 6 alpha^2 = 0` has negative discriminant, so there is no real solution. In particular the totally antisymmetric "lambda-connections" of a bi-invariant metric fail.
  - The time-dependent flat FLRW ansatz with `alpha = 0` reduces to `beta' = -s beta^2` and `a''/a = 3 beta^2 + 3 beta H + 2 H^2` (Lorentzian). The second and first brackets are consistent (a Noether identity), so local real solutions exist, but they are singular at finite `t` and are not pursued. This is recorded only in the proposal, not in the insert.

### 3. Linearisation on family (i) (s2; `core068.M_op`)
`core068.M_op` is the 068 linearisation of the closed bracket formulas. It accepts any constant `cbar, wbar`.

**(a) Gauge kernel.** The gauge directions must include `omega_a^{de} = xi^c R_ca^{de}` for diffeomorphisms. The derivation is `[xi^c D_c, D_a] = -(D_a xi^c) D_c + xi^c(-T_ca^e D_e + 1/2 R_ca^{de} S_de)`. Without this term `|M G| ~ 4-12`; with it `|M G| ~ 3e-15`. At generic real `q` the rank is 30 and the kernel is spanned by `G`.

**(b) (R1) fails.** `|dB2/dh| ~ 9-10` at the samples, against exactly 0 on the 068 Heisenberg background.

**(c) Generalised (R2).**
- The translations `∂_I` commute with `D_a` and `S` (constant coefficients).
- At `u = 1`, `∂_I = D_I - vert(w_I)`, and the vertical field of right multiplication by `Om_I` equals `1/2 w_I^{cd} S_cd`.
- So the fluctuation `1/2{f_a, ∂_I}` has section values `h_a^c = -f_a δ^c_I` and `omega = -f_a w_I`.
- The adjoint compatibility `E_b[1/2{f,C}] = 1/2{E_b[f],C}` (appH pairing paragraph) maps it to the operator `(Qf)_b ∂_I`, whose bracket components are `B1 = (Qf) δ_I` and `B2 = -(Qf) w_I`.
- `Q` is the linearised third bracket, with `nabla` containing `w`.
- Numerically the residual is 2e-15 for both points of (i), at 3 random `q` each.

**(d) Block-triangular form.** This follows from (c) exactly. In `x' = (f, omega')`, with `f^I = -h^I` and `omega' = omega - h^I w_I`, and outputs `g^I = B1^I`, `B2' = B2 + B1^I w_I`, the label image `u_I(g)` has `B2' = -g w_I + g w_I = 0`. Hence `dB2'/df = 0` (numerically 5e-15). The 24x24 block `Y` has rank 18: 6 rotation directions project into it.

**(e) Roots.** `char_roots` (068 tools) was run along `q = (t, kvec)` for 4 `kvec`, with two random compressions. Every root satisfies `q^2/(2 k.q) = alpha`, constant across lines.
- At the trace-free point (`s = 1`): `alpha in {±√3, ±√3 ± i, ±√3 + 2i}`; `Q` gives `±√3` only; `Y` carries all of them.
- At `tau = 1` (`m = (0,2,0,0)`): `alpha in {-i/2, -3i/2, -5i/2}`; `Q` gives `-3i/2`.
- Converse (rank drop at random complex points of each cone, sigma_30/sigma_1): about 1e-16 at `tau = 1`, against 1e-3 at control points, so it is clean there. At the trace-free point the ratio is 3e-10 to 5e-5, against 1e-4 to 3e-3 at control points. The separation is weak there, consistent with defective (Jordan) roots, and the insert says so.

**(f) Boost-dilation symmetry** (exact, by hand; numerical 1e-16).
- Under `exp(theta B)`, `n` has eigenvalue `-1`, so `k_a -> e^{-theta} k_a` and `[B,N] = -N`, i.e. `N -> e^{-theta} N`. `B` and `m` (which lives in the 1-3 plane) are fixed. Hence `w -> e^{-theta} w`.
- `D -> lambda D` is a symmetry of the cubic homogeneous equation. On the flat frame it is `w -> lambda w` together with `y -> y/lambda`, so `V(lambda w) = lambda V(w)` for the characteristic set `V`.
- Combined with Lorentz covariance `V(L w) = L V(w)`, this gives `V = e^{±theta} L_theta V`, so `{q^2 : q in V}` is invariant under every positive rescaling.
- Consequence: if `q^2 = -m^2` occurs, so does `-lambda^2 m^2` for all `lambda > 0`. There is no isolated mass shell and no invariant gap scale. This is the precise sense of "no gauge-invariant mass" claimed, and it does not rest on the numerical roots.

**F3 hazard.** `M(0) != 0`: the non-derivative terms are present. By (e) and (f) they do not create a mass. The imaginary `alpha` are of the form `e^{beta k.y}`, which looks like a local boost weight. That reading is not claimed as a removal, because after the pure-gauge local boost `exp(s (k.y) B)` the `N` term becomes `y`-dependent.

**Comparison with the original target.** The result gives the operator content (`Q` with connection, the `Y` block, the gauge kernel) on the first `R != 0`, `T != 0` backgrounds. It also shows that this null family neither gaps nor reorganises the torsion/Lorentz modes into massive ones. It does not derive SO(3,1), the frame, the selection of the class, or a norm, so the D1 target remains open.

**Literature.** No new citations. The bracket formulas and the class come from the integrated paragraphs, whose citations (HKK 2006, FHKK 2007) were not re-verified here. No literature result is imported.

## Claim classification

| Claim | Class |
|---|---|
| (i), (ii) solve brackets 1-2 for symbolic parameters; invariants as listed | established (exact, sympy, s1) |
| Section values match the operator relations on the bundle; matrix-equation vector field vanishes | numerical (s0, residual < 1e-13; control 1e2) |
| `F = -c t` for constant section values, hence third bracket holds on (i) | established (by hand) |
| Survey counts; no Euclidean flat solution; RR != 0 solutions on solvable algebras | numerical, not a classification (s3) |
| Isotropic static and flat isotropic no-go (in the stated ansatz) | established (exact, x1/x1b), recorded in proposal only |
| Gauge kernel = 10 directions with `xi R` term | numerical (s2 (a)); the formula for the gauge directions is established (by hand) |
| (R1) fails at R != 0 | numerical (s2 (b)) |
| Translation-label reduction to Q with connection part | established by adjoint compatibility + commutation; numerical check 2e-15 |
| Block-triangular form, rank-18 connection block | the triangularity is established (follows from the label identity); the rank is numerical |
| Roots on shifted cones with the stated alpha | numerical (s2 (d), (f)); converse clean at tau = 1, weak at the trace-free point |
| Boost-dilation symmetry; no isolated mass shell / no invariant scale on (i) | established (by hand, given the symmetry; numerical check of the symmetry) |
| No stability statement for imaginary shifts | scope statement |
| Selection of the class/backgrounds, frame, non-degeneracy, norm | unresolved |

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`, section `sec:status-D`. Only this file changes; there is no bibliography change.

**Anchor:**
- Insert the block below, followed by one blank line, immediately before the unique line `\section{Problem E: signature}` (pre-image line 1631).
- That puts it directly after the integrated 068 paragraph. The 068 paragraph's last sentence ends "..., \ref{ass:local-lorentz} and~\ref{ass:EFT-a2} are not discharged; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL."
- Nothing is replaced, and all existing text is kept. The exact CRLF block is `appH_insert_r1.tex`, applied by `apply_and_build_r1.py`.

```latex
\paragraph{First-order equivariant class on left-invariant backgrounds with curvature and torsion: exact solutions and the linearised equations (conditional; not closure).}
Keep the class of the preceding paragraph on a four-dimensional Lie group, with left-invariant frame \(E_a\), \([E_a,E_b]=\mathsf c_{ab}{}^dE_d\) and \(\mathbb D_a=u_a{}^bE_b\) plus the connection term of the class, but give the connection constant components \(\omega_a{}^{cd}=w_a{}^{cd}\) in this frame. The section values \(\mathsf T\) and \(\mathsf R\) are then constants, polynomial of degree at most two in \(\mathsf c\) and \(w\); they agree with the relations computed for the vector fields on the bundle at random Lorentz \(u\) (numerical, residual below \(10^{-13}\)), and the first two brackets of the matrix equation become polynomial equations in \(\mathsf c\) and \(w\). With \(\eta=\mathrm{diag}(-1,1,1,1)\), let \(B^{cd}\) be the boost bivector with \(B^{02}=1\), let \(N^{cd}\) and \(N'^{cd}\) be the null rotations with \(N^{01}=N^{12}=1\) and \(N'^{03}=-N'^{23}=1\), which fix the null direction \(n^a=(1,0,-1,0)\), and let \(k_a=(1,0,1,0)\), so that \(k^a=-n^a\); components not listed vanish apart from antisymmetry. Two families solve both brackets exactly, for symbolic parameters, with \(\mathsf R\neq0\) and \(\mathsf T\neq0\):
\begin{itemize}
\item[(i)] the flat frame, \(\mathsf c=0\), with \(w_a{}^{cd}=s\,k_aB^{cd}+m_aN^{cd}\), \(m_a=(0,m_1,0,m_3)\) and \((m_1-s)^2-m_3^2=s^2\). In this ansatz the second bracket vanishes identically and the first is proportional to \(m_1^2-2m_1s-m_3^2\). Here \(\mathsf R_{ab}{}^{cd}\) has rank one with values on the line of \(N\), \(\mathsf R\neq0\) for \(s\neq0\) unless \(m=0\), \(\mathsf R_{abcd}\mathsf R^{abcd}=0\), \(\mathsf T_{abc}\mathsf T^{abc}=0\), \(\mathsf R_{ab}{}^{ab}=-2sm_1\), and \(\mathsf T_{ac}{}^c=(s+m_1)k_a\), which vanishes at \(m=(0,-s,0,\pm\sqrt3\,s)\). The frame metric is that of Minkowski space. For constant section values the order-zero field \(\mathsf t_a=\tfrac12\mathsf T_{ac}{}^c\) of the class gives \(\mathsf F_{ab}=-\mathsf c_{ab}{}^c\mathsf t_c\) (by hand), which is zero here, so the third bracket also holds;
\item[(ii)] time times the Heisenberg group of the preceding paragraph, \([E_3,E_1]=\kappa E_2\), with \(w_a{}^{cd}=k_a(\zeta N^{cd}+xN'^{cd})\). The torsion is trace-free, \(\mathsf R_{13}{}^{cd}=\kappa(\zeta N^{cd}+xN'^{cd})\) is the only nonzero pair, \(\mathsf R_{abcd}\mathsf R^{abcd}=\mathsf R_{ab}{}^{ab}=0\) and \(\mathsf T_{abc}\mathsf T^{abc}=2\kappa^2\).
\end{itemize}
In both families the Ricci tensor \(\mathsf R_{ab}{}^{ae}\) of the connection is nonzero and is cancelled in the first bracket by the torsion terms. In a numerical survey with \(\mathsf c=0\), 56 of 60 least-squares starts converged to solutions with \(\mathsf R\neq0\) for \(\eta\), all with \(\mathsf R_{abcd}\mathsf R^{abcd}=0\) to \(10^{-14}\), and none converged for the Euclidean contraction; with \(\mathsf c\) free, solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) were found on algebras with a two-dimensional abelian derived algebra (numerical, not a classification).

On family (i) the coefficients are constant, so the translations \(\partial_I\) commute with all \(\mathbb D_a\) and \(\mathcal S_{cd}\), and at \(u=1\) one has \(\partial_I=\mathbb D_I-\tfrac12w_I{}^{cd}\mathcal S_{cd}\). With \(\mathbb D_a\to\mathbb D_a-h_a{}^c\mathbb D_c+\tfrac12\omega_a{}^{cd}\mathcal S_{cd}\) as before, the adjoint compatibility of the paragraph on the pairing of the action then gives, for each \(I\) and arbitrary functions \(f_a\), that the fluctuation \(h_a{}^c=-f_a\delta^c{}_I\), \(\omega_a{}^{cd}=-f_aw_I{}^{cd}\) has linearised brackets
\[
\mathcal E^{(1)}{}_b{}^e=\mathcal Q_b[f]\,\delta^e{}_I,\qquad
\mathcal E^{(2)}{}_b{}^{de}=-\mathcal Q_b[f]\,w_I{}^{de},
\]
with \(\mathcal Q\) the linearised third bracket on this background, \(\mathsf F_{ab}[A]=\nabla_aA_b-\nabla_bA_a+\mathsf T_{ab}{}^cA_c\) and \(\mathcal Q_b[A]=\nabla^a\mathsf F_{ab}[A]-\mathsf T_{ab}{}^c\mathsf F^a{}_c[A]\), where \(\nabla\) now contains \(w\) (checked at sampled \(q\), residual \(10^{-15}\)). This is the frame reduction of the preceding paragraph at \(\mathsf R\neq0\), with labels that now carry a connection part. The reduction of the connection equations to \(\mathcal Q\) fails, since the linearised curvature contains \(h\): the connection equations depend on pure frame fluctuations (numerical). In the variables \(f_b{}^I=-h_b{}^I\) and \(\omega'_b{}^{cd}=\omega_b{}^{cd}-h_b{}^Iw_I{}^{cd}\), the twenty-four combinations \(\mathcal E^{(2)}{}_b{}^{de}+\mathcal E^{(1)}{}_b{}^Iw_I{}^{de}\) contain \(\omega'\) alone, so the system is again block-triangular, the connection sourcing the frame labels, with a connection block of generic rank 18 that is not six copies of \(\mathcal Q\). The kernel at generic \(q\) is the ten gauge directions, whose diffeomorphism part now has \(\omega_a{}^{de}=\xi^c\mathsf R_{ca}{}^{de}\) (numerical). Along lines \(q=(t,\vec q)\) every characteristic root satisfies \(q^2=2\alpha\,k^aq_a\), that is \((q-\alpha k)^2=0\), for \(\alpha\) in a finite set: at \(s=1\), \(\alpha\in\{\pm\sqrt3,\pm\sqrt3\pm\mathrm i,\pm\sqrt3+2\mathrm i\}\) for \(m=(0,-1,0,\sqrt3)\), with \(\pm\sqrt3\) for \(\mathcal Q\), and \(\alpha\in\{-\tfrac{\mathrm i}2,-\tfrac{3\mathrm i}2,-\tfrac{5\mathrm i}2\}\) for \(m=(0,2,0,0)\), with \(-\tfrac{3\mathrm i}2\) for \(\mathcal Q\). Conversely the forty equations drop rank at random complex points of these cones (numerical; the relative smallest singular value is \(10^{-16}\) for \(m=(0,2,0,0)\), and between \(3\cdot10^{-10}\) and \(5\cdot10^{-5}\) at the trace-free point, against \(10^{-4}\) to \(3\cdot10^{-3}\) at random points off the cones, so that the converse is clean only for \(m=(0,2,0,0)\)). The background has an exact boost-dilation symmetry: \(\exp(\theta B)\) multiplies \(k_a\) and \(N\) by \(\mathrm e^{-\theta}\) and fixes \(B\) and \(m\), so it maps \(w\) to \(\mathrm e^{-\theta}w\), while \(\mathbb D_a\to\lambda\mathbb D_a\) maps solutions of the matrix equation to solutions. The set of characteristic \(q\) is therefore invariant under \(q\mapsto\mathrm e^{\pm\theta}\Lambda_\theta q\), with \(\Lambda_\theta\) the boost and the sign fixed by the action on covectors, so the set of values of \(q^2\) on it is invariant under multiplication by every positive number, and no value \(q^2=-m^2\) with \(m\neq0\) is isolated. So on family (i) the non-derivative terms, which are nonzero, shift the cones along \(k\) and do not produce a mass: no gauge-invariant gap appears for the Lorentz or torsion modes at this order, and the background supplies no invariant scale for one. The imaginary parts of \(\alpha\) give solutions whose section values contain \(\mathrm e^{\beta k_ay^a}\) with \(\beta\) real, which grow along the null coordinate \(k_ay^a\); since section values are frame components and no norm is used, no statement on stability is made.

These statements are for Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and no matter term, tree level, the Lorentzian contraction, left-invariant backgrounds with constant connection, the two families named, and, for the linearised equations, linear order on family (i) in its character sectors, with the roots numerical. Family (ii) and the survey solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\), for which no scaling symmetry is shown, are not linearised here, and the nonlinear evolution, the regulated trace, the domains of the unbounded operators, loops and a norm are not treated. Nothing here shows that the matrix integral selects this class, these backgrounds or the algebra \(\mathcal A\), or yields the frame and its non-degeneracy, so Assumptions~\ref{ass:frame-lock}, \ref{ass:nondeg}, \ref{ass:lorentzian}, \ref{ass:local-lorentz} and~\ref{ass:EFT-a2} are not discharged, and the frame of these backgrounds is not identified with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
```

**Stale passages elsewhere:** none. The 068 paragraph's (R1)/(R2) statements are scoped to vanishing connection and stay correct. ch17 and ch10 are unaffected. The frontier edge text ("no source read supplies one") is a report-side pointer, not manuscript text.

## Verification scripts

All scripts are in `proposals/071-d1-curved-torsion-backgrounds/` and are run with `python -I` from any cwd. Each script adds its own folder to `sys.path`.

**Modules**

| File | Role |
|---|---|
| `bg.py` | constant section-value geometry and brackets (independent re-implementation; agrees with `core068.brackets` to 1e-15) |
| `symgeom.py` | exact sympy version of the same |
| `opcheck.py` | operator-level bundle check |
| `invariants.py` | invariants of the Lie algebra, the torsion and the curvature |
| `lin.py` | backgrounds; gauge vectors with the `xi R` term; `Q` with connection |
| `core068.py`, `tools068.py` | verbatim copies of the 068 `core.py`/`tools.py`; the only change is the import line in `tools068` |

**Reproduction pack**

| Command | Expected invariant output |
|---|---|
| `python -I s1_backgrounds.py` (about 3 min) | `B1 == 0 identically: True ; B2 == 0 identically: True` for F_tau and for H; general-m ansatz `B1 ∝ m1**2 - 2*m1*s - m3**2`, `B2` empty; trace `s*(tau**2+4*tau+1)/(2*tau)`; `T_abc T^abc = 0` (F), `2*kappa**2` (H); `R_abcd R^abcd = 0` for both; scalar `-s**2*(tau+1)**2/tau` (F), 0 (H); R rank 1; trace-free point `m = [0, -s, 0, sqrt(3)*s]`, trace `[0,0,0,0]` |
| `python -I s0_operator_check.py` (about 4 min) | for F and H, all entries ≤ 5e-14 and `matrix_eq_max` ≤ 1.4e-14; control `matrix_eq_max` ~ 1e2 |
| `python -I s2_linearised.py` (about 6 min) | (a) rank 30, `|MG|` ~ 1e-15, kernel = span G True, `|MG0|` O(1-10); (b) `|dB2/dh|` O(1-10); (c) `≤ 3e-15`; (d) alpha sets `{±1.73, ±1.73±1j, ±1.73+2j}` (trace-free) and `{-0.5j, -1.5j, -2.5j}` (tau=1), Q `{±1.73}` and `{-1.5j}`; converse at tau=1 ~ 1e-16 vs control ~ 1e-3; (e) `≤ 1e-15`; (f) `|dB2'/df| ≤ 1e-14`, rank Y = 18 |
| `python -I s3_survey.py` (about 6 min) | flat `eta`: `59 converged, 56 with R != 0`, `max |RR| ~ 3e-15`; flat Euclidean: `0 converged`; stored solvable solutions: residuals ≤ 4e-11, RR `-7.1e-04, 8.9e-04, -3.7e-03, ~1e-12`, `dim[g,g] 2`, derived series `[2, 0]` |
| `python -I x1_isotropic.py`, `python -I x1b_flrw.py` | isotropic flat: `B1_00 = 3 beta**2 s`; FLRW brackets as recorded |
| `python -I apply_and_build_r1.py --build` | pre `d8d8b678fa0ceabe03f3f9c2f56cc60dbe140aa845658beddb0c206ba26c9180`; post `a73760f2181d68d04e99915aac756907a2ef753f746e4920d388c37bfc0e13c0`; block sha256 `9ccda7041a51984b22994e2cdecba1967786c485673d2be3316caaf82c7e02f3`; `BUILD CLEAN`, 0 undefined/multiply-defined, 414 pages, temp copy removed |

## Decisions Taken

- **Background class.** I took left-invariant data with a constant nonzero connection. This is the minimal relaxation of the 068 hypothesis "vanishing connection", and it keeps exact harmonic analysis available.
  - Rejected first: isotropic and FLRW torsion. The static and flat isotropic cases have no solution (x1). The time-dependent case is singular and not homogeneous in time.
  - Rejected second: non-constant connections, which lose the polynomial reduction.
- **Linearised example.** I linearised family (i) rather than (ii), because (i) has constant coefficients and a full translation commutant, so the spectrum is exact in characters. I report two points: the trace-free point, which avoids the `t` subtlety, and `tau = 1`, which has rational data and the cleanest numerics.
- **Meaning of "mass".** "Mass/gap" means an isolated value of `q^2` on the characteristic variety, which is gauge-invariant because the translation labels are commutant eigenvalues. Cone shifts along `k` are not counted as masses (hazard F3).
- **What goes into the insert.** The isotropic no-go and the FLRW reduction stay out of the insert (smallest text). The survey stays in as one sentence, because it locates the next avenue (non-null solutions).
- **Converse root test at the trace-free point.** The converse test there is numerically weak. I recorded it with its numbers and qualified it ("clean only for m=(0,2,0,0)"), rather than dropping the point.

## Milestone assessment

**Routine.** This is a conditional sub-lemma. It supplies the named missing input (R != 0, T != 0 solutions), generalises the 068 reduction and gives a bounded no-gap statement for one null family. No critical-path step is derived from the matrix theory, so no milestone trigger applies.

## Status-label recommendation

- **Critical-path list:** A, B, C, D (D1), E, F, G-derived and N, all OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. This is derived from ch17 L330-343 and L645-716 and from the appH ledger lines L16, L158, L552, L719, L1635, L1827, L3070 and L3512.
- **Optional:** H, I and J are OPEN and OPTIONAL.
- **Recommendation:** no label change.

## Author decision needed

None.

## Remaining open step

To close D1, the following are still needed:
- derive local SO(3,1) and the locked frame with its non-degeneracy from the matrix integral (selection of the class, of `A`, and of the backgrounds);
- specify `omega, A, B` and the ghost operators with a norm and a regulated trace.

On the narrower torsion/propagating-modes item, the ranked open avenues are (derivation-first):
1. **Linearise the non-null survey solutions** (`R_abcd R^abcd != 0`, solvable groups with a 2-dim abelian derived algebra). No scaling symmetry is shown for them, so they are the first place where an invariant scale, and hence a genuine gap, could appear. This needs the harmonic analysis of non-unimodular solvable groups (characters only on `q ⊥ [g,g]`, plus the infinite-dimensional representations).
2. **Linearise family (ii)** in the oscillator sectors `p != 0`. The Heisenberg structure constant `kappa` is not boost-covariant along `k`, so (ii) can carry an invariant scale. Test whether `R != 0` modifies the 068 Landau-level/Nielsen–Olesen growth `Gamma <= kappa/2`.
3. **Interpret the imaginary cone shifts** (`e^{beta k.y}` growth of section values) with a form. This ties to `D1.krein-finiteN-dS` and must not become an E package.
4. **(Bottom)** Further null families with `R_abcd R^abcd = 0` and a boost-dilation symmetry. The scaling argument already excludes an isolated mass shell for them, so their expected output is the same no-gap result.

**What transfers to F (gated on D1, ch17 L650-653):** on these backgrounds the operator content (`Q` with connection, the block `Y`, and the gauge kernel with the `xi R` term) is the tree-level `omega`/frame quadratic operator that a one-loop F computation would consume.

## Special instructions for the gatekeeper

- **Re-derive by hand:**
  1. `F = -c t` for constant section values;
  2. `∂_I = D_I - 1/2 w_I S` at `u = 1`, and the resulting label section values `(h, omega) = (-f δ_I, -f w_I)`; check the sign against s2 (c);
  3. the diffeomorphism gauge direction with `xi^c R_ca^{de}`;
  4. the boost-dilation argument, i.e. `[B,N] = -N` and `k -> e^{-theta} k` with the stated conventions, and the inference from it.
- **Must not be asserted:**
  - that the torsion modes are massless "in general";
  - that the backgrounds are selected;
  - that the imaginary shifts are or are not instabilities;
  - that (ii) or the survey solutions have no gap;
  - any norm statement.
- **The roots are numerical.** The converse test is clean only at `tau = 1`, and the insert says this.
- **The survey statement** ("56 of 60", "none for Euclidean") is numerical and not a classification.
- **Anchor:** insert before the unique `\section{Problem E: signature}`, after the 068 paragraph's status sentence. The pre-hash is the live appH (dirty tree from the 068/069 integrations). The block has exactly one status sentence, which is in its last paragraph. No new labels or citations are added.
