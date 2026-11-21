# Proposal 059-d1-lorentz-local-frame, local round 2

Responds to `proposals/local-gpu/_local-review/group2-B-C-D1.md`, section 059 (VERDICT ACCEPT WITH REQUIRED REVISIONS, FLAGS: RESEARCHER-DECISION, findings M1-M3, m1-m4). Supersedes the gpu `proposal-r3.md` / `insertion-block.tex` for this branch. The gpu numbering is not this branch's numbering; the r3 text is not in the current tree.

## Result

The S^2 toy has been recomputed with **equivariant lifts**, which is option (b). On the frame bundle Z = SO(3) of the unit sphere:
- D_a = u_a^b(e_b - omega_b xi), with u_1^1 = u_2^2 = cos psi and u_1^2 = -u_2^1 = -sin psi, together with S_12 = +xi, satisfy **both** class relations exactly.
- The data are T = 0, F = 0, R_12^12 = -1 and t_a = 0, so [D_1, D_2] = -S_12.
- The local rotation identity of the class holds for every base function lambda.
- The opposite orientation of u gives T != 0. With this horizontal lift, S_12 = -xi violates relation (I).

**Ghost spectrum in the equivariant setting.** The lifted Killing fields rho~_i commute with D_a and S_12, and Sum rho~_i^2 = D_1^2 + D_2^2 + S_12^2 holds exactly. It follows that the class ghost [X^a, [X_a, .]] on the A_a gauge parameters, which are base functions, is minus the Laplace-Beltrami operator: spectrum l(l+1), multiplicity 2l+1.

**Redundancy in the equivariant setting.** The redundancy lifts to Sum x_i rho~_i = -S_12. That is vertical, so it vanishes on base functions.

**Two finite-N truncations.** These are new derivation-grade content for the D1 finite-N question.
1. **Frame-equivariant truncation.** This is the Peter-Weyl projection P_L of L^2(Z), or any finite-dimensional unitary representation of the compact algebra (su(2), so(5)).
   - Exact: both class relations, the compressed redundancy, and the ghost eigenvalue l(l+1) with multiplicity 2l+1 for l <= 2L.
   - Lost: the commutative algebra A. A lemma shows that on a finite-dimensional Hilbert space every ad X_a preserving a commutative *-algebra vanishes on it. In the Peter-Weyl case the product defect sits only on the cutoff blocks.
2. **Fuzzy sphere (isometry-equivariant).** This keeps the earlier exact results: Leibniz rule, closure, and the ghost multiset l <= N-1.
   - It carries **no frame index**: D_1 does not preserve its Hilbert space.
   - The frame redundancy is ordering-dependent and now **exact**: Sum X_i L_i F = (hbar_eff/2) l(l+1) F one-sided, and 0 symmetrised. This replaces the fitted slope.

**Bounded obstruction for the Lorentzian fibre.** A finite-dimensional representation of so(3,1) by anti-Hermitian matrices is zero, and relation (I) then forces D_a = 0. Finite realisations with eta therefore need an indefinite (Krein) form. The so(4,1) fundamental is checked.

**Composite paragraph.** It is made conditional verbatim (M3).

**Not done.** None of this derives the selection of the class, A, the frame or its non-degeneracy. Problem D / D1 stays OPEN. Rule 3 applies: a toy and conditional sub-lemmas do not close anything.

## Target and status

- **Problem D, Appendix H L716-720 (verbatim).** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- **Chapter 17, L329-361.** D1 closure requires three things:
  - the omega, A_mu, B and ghost operators and the field content to be specified;
  - the locked frame to exist and be non-degenerate, derived rather than taken from ass:frame-lock / ass:nondeg;
  - in the dependency order (L650, L712), D1 comes first and gates C and F.
- **Discrepancy check.** I found none between ch17 and appH for D.
- **Dependencies.** The package relies on the "First-order equivariant class" paragraphs (appH L1511-1597) and on Section E L1735, the statement that non-compact members need N -> infinity.
- **Classification.** PROGRAMME-CONDITIONAL; the package is not DERIVED.

## Source reading

Digest plus targeted reads. This is not a full scan: no definition, assumption or status passage is changed, and the gatekeeper's full-scan trigger (c) does not apply.
- **Digest.** `make_digest.py --check` printed DIGEST CURRENT, with dirty-chapters: yes (the uncommitted 070). The appH sha256 4ea0ee0f... matches the orchestrator's value.
- **Read in full:**
  - appH Problem D, L713-760 and L1494-1599: the three first-order-class paragraphs and the one-loop/reflected-form paragraph;
  - ch17 L325-365, L645-655 and L708-716;
  - ch03 L245-295 (eq:VEV, ass:frame-lock, eq:Phi-transform);
  - ch04 L30-185 (constant-vacuum obstruction, Repair I/II, def:composite-metric, ass:nondeg);
  - ch10 L1-60 and L130-200 (two groups, ass:local-lorentz, dressed connection, unitary gauge, thm:locking);
  - appH L1735 (Section E, non-compact members);
  - the local review section 059;
  - gpu r3 proposal, block and scripts;
  - the 068 `core.py` conventions header.
- **Unreadable files.** None.

## Research and reasoning

### M1: RESEARCHER-DECISION, option (b) taken

**Non-equivariant lifts (r3 toy).** Coordinates are (theta, phi, psi) with xi = d_psi. Take e_hat_a = e_a - omega^12(e_a) xi, with omega^12(e_1) = 0 and omega^12(e_2) = -cot theta. Then:
- e_hat_1 = d_theta and e_hat_2 = csc theta d_phi + cot theta d_psi;
- [e_hat_1, e_hat_2] = -cot theta e_hat_2 - xi;
- [xi, e_hat_a] = 0, so relation (I) [S_12, D_a] = delta_a2 D_1 - delta_a1 D_2 fails for every S_12 proportional to xi.

This confirms M1. The r3 "T_12^2 = cot theta" was the base anholonomy, not torsion. That contradicted "torsion-free" and also local 068, whose `core.py` uses T_ab^c = -C_ab^c - Om_ab^c + Om_ba^c, so T = 0 for Levi-Civita even with anholonomy C != 0.

**Equivariant lifts.** Take D_a = u_a^b e_hat_b with u in SO(2).
- **Orientation.** With u_1^2 = s sin psi, only s = -1 gives a [D_1, D_2] with no D-component, i.e. T = 0. (Script E1(B) prints [D_1,D_2] = -2 sin psi cot theta D_1 - 2 cos psi cot theta D_2 - xi for s = +1, and -xi for s = -1.)
- **Relation (I).** By hand, [d_psi, D_1] = -D_2 and [d_psi, D_2] = D_1 for s = -1. Relation (I) requires [S_12, D_1] = -D_2, hence S_12 = +xi.
- **Relation (II).** [D_1, D_2] = -xi = -S_12 = R_12^12 S_12, with R_12^12 = -1, T = 0 and F = 0, all constant.
- **Hermiticity.** div D_a = 0 in sin theta dtheta dphi dpsi, so t_a = T_ac^c / 2 = 0, consistent with T = 0.
- **Ricci.** In the manuscript convention R_ab^ae = -Ric_b^e (appH L1528), so Ric = +delta, the unit sphere.
- **Local rotation.** For an Abelian fibre, lambda^{cd} = u u lambda_hat = det(u) lambda_hat = lambda (base function). By hand: [lambda S, D_1] = lambda[S, D_1] - (D_1 lambda) S = -lambda D_2 - (D_1 lambda) S, and lambda^c_1 D_c = lambda^{21} D_2 = -lambda D_2. Both D_a are checked for a generic function lambda(theta, phi).

**Sign remark on the gatekeeper's S_12 = -xi.** The sign of S_12 relative to xi is fixed by the choice of horizontal lift. With e_hat_a = e_a - omega_a xi it is +xi. The gatekeeper's -xi is the same structure after psi -> -psi, which takes xi to -xi and turns the lift into e_a + omega_a xi'. The convention-independent data are T = 0, F = 0 and R_12^12 = -1, and these agree with the gatekeeper's verification. The block states the lift explicitly, so the sign is unambiguous.

**Killing lifts and the ghost spectrum.**
- **The fields.** With rho_i = eps_ijk x_j d_k, the base fields are:
  - rho_1 = -sin phi d_theta - cot theta cos phi d_phi;
  - rho_2 = cos phi d_theta - cot theta sin phi d_phi;
  - rho_3 = d_phi.
- **The lifts.** Requiring [rho_i + c_i xi, D_a] = 0 makes the D-components of the bracket proportional to (c_i + cos phi / sin theta), (c_i + sin phi / sin theta) and c_3. This forces c = (-cos phi / sin theta, -sin phi / sin theta, 0), and the xi-component then vanishes identically (E1(D)).
- **Group theory.** The rho~_i generate the left SO(3) action on Z = SO(3). The pair (D_1, D_2, -S_12) closes as so(3) and generates the right action. The two Casimirs coincide on L^2(SO(3)), so Sum rho~_i^2 = D_1^2 + D_2^2 + S_12^2, checked on a generic f(theta, phi, psi).
- **Ghost.** Gauge parameters of A_a are multiplication operators by base functions Lambda, with S_12 Lambda = 0. With X_a = i D_a: [X_a, Lambda] = i(D_a Lambda) and [X_a, i D_a Lambda] = -D_a^2 Lambda, so the ghost is -(D_1^2 + D_2^2) = -Laplace-Beltrami. Its spectrum is l(l+1) with multiplicity 2l+1, checked on all Y_lm with l <= 4.
- **Redundancy.** Sum x_i rho~_i = -xi = -S_12, a vertical field that vanishes on base functions, while Sum x_i rho_i = 0 on the base.

### M2

The r3 sentence "the commutator of two first-order operators is not itself first-order" is false, since commutators of vector fields are vector fields. The block now says: "the commutator of two lifts is not in the span of the lifts over the base functions". It also states the basis dependence: the xi-coefficient is -1 in (e_hat_a, xi), -csc^2 theta in (e_a, xi), and the constant R_12^12 = -1 in (D_a, S_12). Script E1(A) checks the first two and E1(B) the third.

### Finite N (re-derived in the equivariant setting)

**Lemma (exact).** Let H be finite-dimensional and A subset End(H) a commutative *-algebra. Then A is isomorphic to C^n and is spanned by its minimal projections P. Let delta be a derivation of End(H) with delta(A) subset A. Then:
- delta(P) = delta(P^2) = 2 P delta(P), by commutativity in A;
- multiplying by P gives P delta(P) = 2 P delta(P), so P delta(P) = 0 and delta(P) = 0.

Hence ad X_a vanishes on A. The class requires the adjoint actions of D_a and S_cd to be a basis of vector fields on Z = spec A, which therefore fails for dim Z > 0 at every finite N. The *-closure is needed: C[x]/(x^2) has the nonzero derivation x -> x. The class's A contains complex conjugates, as functions do, so the hypothesis is met.

**Frame-equivariant truncations (exact).**
- **Lie-algebraic relations.**
  - In any unitary su(2) representation, X_a = J_a (a = 1, 2) and S_12 = i J_3 give [iJ_3, J_1] = -J_2, [iJ_3, J_2] = J_1 and [J_1, J_2] = iJ_3 = S_12 = -[D_1, D_2]. These are the class relations with T = 0, R = -1 and F = 0.
  - For so(5), [E_cd, E_a5] = delta_da E_c5 - delta_ca E_d5 and [E_a5, E_b5] = -E_ab. That gives R_ab^cd = -(delta delta - delta delta) and Ric = 3, the unit S^4, in every unitary representation. Representations 4, 5 and 20 are checked.
- **Peter-Weyl.** P_L commutes with both the right and the left actions. Hence P M_f P transforms covariantly: [X_a, P M_f P] = P [X_a, M_f] P = P M_{i D_a f} P. On a compressed base function Y = P M_{D^l_{mu 0}} P:
  - the ghost Sum_{a=1,2} [X_a, [X_a, Y]] equals P M_{(C - X_3^2) f} P = l(l+1) Y;
  - Y is nonzero exactly for l <= 2L (Clebsch-Gordan), and the Y_{l mu} are linearly independent (left-isotypic and Schur; rank checked);
  - Sum_i (P M_{x_i} P) rho~_i = P (Sum_i x_i rho~_i) P = -S_12 P;
  - the product defect is -P M_f (1-P) M_g P. On a block j, M_g reaches j + l_g, so the defect vanishes for j <= L - l_g. It is nonzero on j = L for degree-one f and g (E2 C5).
- **Script conventions.** The script realises functions on SO(3) by Wigner coefficients phi^j_mn = sqrt(2j+1) D^j_mn, with exact CG products. It also checks convention consistency (C2: [X_a, M_f] = M_{X_a f}).

**Fuzzy sphere (exact plus one numerical item).** The gatekeeper accepted these previously; this round re-derives them.
- **Ordering-dependent redundancy, a new closed form.** For F in the spin-l part of End(V_j), with Sum_i X_i^2 = 1:
  - Sum_i [X_i, [X_i, F]] = 2F - 2 Sum_i X_i F X_i, so Sum_i X_i [X_i, F] = F - Sum_i X_i F X_i = (1/2) hbar^2 l(l+1) F;
  - therefore Sum_i X_i L_i F = (hbar/2) l(l+1) F, while (1/2) Sum_i {X_i, [X_i, F]} = (1/2)[Sum_i X_i^2, F] = 0.
  - The r3 statement "violated at O(hbar)" is thus true for the one-sided ordering, false for the symmetrised one, and now exact. For the r3 test vectors (l = 1), the closed form gives defect = hbar, which matches the r3 fitted slope of -1.
- **No frame index.** For odd N, V_j is identified with the right-weight-j functions in block j, i.e. the holomorphic sections of the degree-2j bundle. This subspace is preserved by the left action rho~ and not by X_1 (E2 C6). Berezin-Toeplitz is isometry-equivariant, not frame-equivariant, and this is why the redundant 3-field frame rho_i appears instead of D_a.

**Lorentzian bounded obstruction (exact proof).**
- **Statement.** so(3,1) is a simple real Lie algebra. A representation by anti-Hermitian n x n matrices maps it into u(n), and its kernel is an ideal, so the map is either zero or injective. If injective, so(3,1) would carry the positive invariant form -tr(XY), which would make it compact. It is not compact. So S_cd = 0, and relation (I) at a = d != c gives eta_dd D_c = 0, i.e. D_c = 0.
- **Hypotheses:**
  - (h1) finite-dimensional H;
  - (h2) S_cd anti-Hermitian, i.e. a unitary SO(3,1) action, as in the class definition at appH L1512;
  - (h3) the relations hold exactly;
  - (h4) Lorentzian eta on the fibre.
- **Consistency.** This agrees with Section E L1735.

**Fork: relaxations and ranked open avenues (derivation-first).**
1. *Relax (h2) to a Krein form.* This is positive-aimed. Finite matrices satisfying both relations with eta exist; the so(4,1) fundamental is eta-anti-self-adjoint (E2 B3). The appH reflected-form paragraph already uses a Krein majorant. **Next package (ranked first):**
   - build a finite-N Krein-space realisation of the de Sitter point;
   - compute the ghost operator and the quadratic form on it;
   - test whether the indefinite part is confined to the gauge and odd-label sectors.
   A positive result would be a finite-N D1 ingredient: frame relations plus a specified ghost operator.
2. *Relax "A commutative" to a noncommutative coefficient algebra* (fuzzy-S^4 / Berezin-Toeplitz type, appropriate to the compact so(5) case). Positive-aimed, for the class relations with coefficients in a noncommutative algebra. The question is whether a non-degeneracy criterion for the frame (ass:nondeg) can be stated there. This attacks the D1 "frame and its non-degeneracy" requirement.
3. *Relax (h4) by Euclidean so(5) with reflection.* This one is exact at finite N (E2 B2). It is gated on Problem E (Lorentzian reconstruction; appH Section E), and the findings that transfer there are B2 and B3.
4. *Relax (h1) by N -> infinity with a regulated trace.* This is the status quo; the regulated trace is open (appH L1528).
5. *Relax (h3) to approximate relations at O(hbar).* The likely outcome is the same bounded obstruction with error terms, so it is not proposed while 1-2 are open.

### M3 (verbatim)

The three replacements are applied exactly as the review gives them:
- "on a gauge-invariant reading, which Chapters~\ref{ch:vierbein-emergence} and~\ref{ch:lorentz-locking} do not adopt, the locking of Assumption~\ref{ass:frame-lock} would be represented";
- "On that reading Assumption~\ref{ass:nondeg} would become";
- "and the locking would be read as".

The gauge-invariant reading is **not** adopted: it conflicts with ch04 Repair II (eq:vev-is-frame, a literal VEV) and with ch10 (broken generators, unitary gauge, thm:locking), and adopting it would be STRUCTURAL.

### m1-m4

- m1: rho_i = eps_ijk x_j d_k is defined in the block.
- m2: replaced verbatim. "Compare the Berezin--Toeplitz finite-size regularization of covariant-derivative configurations, including \(S^2\), of \cite{HattoriSekoTsuchiya2026}".
- m3: "for Higgs fields in the fundamental representation" is inserted after "showed that".
- m4: both paragraph titles carry "(conditional; not closure)".

### Literature

- HattoriSekoTsuchiya2026: arXiv 2606.24577, fetched this round. Title, authors, PTEP (2026) 083B01, DOI 10.1093/ptep/ptag120. The abstract mentions finite-size matrices, covariant derivatives, S^2 and Berezin-Toeplitz quantization. Only "compare" is claimed.
- Elitzur 1975 (PRD 12, 3978) and Fradkin-Shenker 1979 (PRD 19, 3682): the records are as in r1, which the gpu gatekeeper verified. I did not re-fetch them this round; they are standard. The claims attributed are restricted to compact groups on the lattice and, for Fradkin-Shenker, fundamental-representation Higgs fields.
- HoKawaiSteinacker2025: already in bib and cited in appH for bilocal fields.
- No other literature is imported. The so(5)/su(2) statements are elementary representation theory, derived and checked here.

## Claim classification

| Claim | Class |
|---|---|
| Non-equivariant lifts violate (I); their anholonomy is not torsion | established (exact sympy + hand) |
| Equivariant lifts: (I), (II) with T = 0, F = 0, R_12^12 = -1, t_a = 0, S_12 = +xi for the stated lift; the opposite orientation has T != 0 | established |
| Local rotation identity of the class on the toy | established |
| Lifts rho~_i commute with D_a, S_12; Casimir identity; ghost on base functions = -Laplace-Beltrami, l(l+1), multiplicity 2l+1 | established |
| Sum x_i rho~_i = -S_12 | established |
| Basis dependence of the curvature coefficient (-1, -csc^2, constant -1) | established |
| Finite-dim lemma: ad X_a vanishes on any preserved commutative *-algebra | established (proof) |
| Exact finite-N class relations in su(2), so(5) unitary representations | established (algebra + numerics) |
| Peter-Weyl compression: relations, ghost l(l+1) multiplicity 2l+1 for l <= 2L, compressed redundancy exact; defect only for j > L - l_g | established (proof + exact-CG numerics, L <= 3) |
| Fuzzy sphere: Leibniz, closure, ghost multiset (l <= N-1) | established (Casimir + numerics) |
| Fuzzy redundancy: one-sided (hbar/2) l(l+1) F, symmetric 0 | established (proof + numerics) |
| Moyal-vs-Poisson O(hbar_eff) | numerical (slope -1.065) |
| Fuzzy Hilbert space not preserved by D_1 (no frame index), odd N | established |
| Lorentzian finite-dim unitary obstruction (h1-h4) | established, bounded no-go |
| Krein-form realisation exists (so(4,1) fundamental) | established (example) |
| Elitzur, Fradkin-Shenker statements | literature (compact, lattice); extension to the noncompact frame group unresolved |
| Composite reading of the locking | conjecture/mechanism, explicitly not adopted |
| Selection of the class, A, frame, non-degeneracy by matrix dynamics | unresolved |

## Proposed changes

**File.** `chapters/appH-microscopic-proofs.tex` only. Bib additions go to the integrator, for `bib/namcg.bib`.

**Anchor.** The unique line `\section{Problem E: signature}`, with exactly 1 occurrence, at byte offset 257407 of the current file. It is preceded by `\r\n\r\n`, after the last sentence of the Problem D paragraph "First-order equivariant class: one loop about commuting matrices, ...": "Problems~D, E, F and~N remain open and PROGRAMME-CONDITIONAL." That sentence is not unique in the file, so it is not used as the anchor.

**Insertion.** Insert immediately before the anchor the CRLF form of `insertion-block-local-r2.tex`, followed by one blank CRLF line. Nothing is replaced, and all existing text is kept.

**Hashes** (from `apply_and_build_local_r2.py`):
- pre: appH sha256 `4ea0ee0f50b0676ee161ff8ebd6620e3bd775ae74ffb1796b07d8a78f9e24b18`, 702490 B, 3557 CRLF, 0 bare LF;
- block: LF 9401 B, sha256 `215637bf290a25e4a94f1c712227bd932ca7d3c51c4a97b4e66620cf3d72fc96`; CRLF 9408 B, sha256 `00152256d61b56da5aa97ac1c1d5d0bf79d5fbfd51d7b2a99391f784a79c7cc3`;
- post: appH sha256 `b6ce7529ec3aae5b79a02ab711f644808e12b0f7b64131a6effbc1c6d7abbf9d`, 711900 B (= 702490 + 9408 + 2), 3565 CRLF, 0 bare LF; the anchor is still unique.

The fenced block below is byte-identical to `insertion-block-local-r2.tex`, which adds a final newline.

```latex
\paragraph{First-order equivariant class on a compact toy: equivariant lifts and finite-\(N\) truncations (conditional; not closure).}
Replace \(\mathrm{SO}(3,1)\) in the first-order equivariant class above by \(\mathrm{SO}(2)\) and \(\eta\) by the Euclidean contraction, and take the base to be the unit two-sphere, with coframe \(\theta^1=\mathrm d\theta\), \(\theta^2=\sin\theta\,\mathrm d\varphi\), orthonormal frame \(e_1=\partial_\theta\), \(e_2=(\sin\theta)^{-1}\partial_\varphi\) and Levi-Civita connection \(\omega^{12}=-\cos\theta\,\mathrm d\varphi\). On the frame bundle \(Z=\mathrm{SO}(3)\), with fibre angle \(\psi\) and \(\xi=\partial_\psi\), the horizontal lifts \(\hat e_a=e_a-\omega^{12}(e_a)\,\xi\) satisfy exactly \([\hat e_1,\hat e_2]=-\cot\theta\,\hat e_2-\xi\) and \([\xi,\hat e_a]=0\). They do not rotate the frame index, so they violate the first relation of the class for \(\mathcal S_{12}\) any multiple of \(\xi\); read through the second relation alone they would place the anholonomy \([e_1,e_2]=-\cot\theta\,e_2\) of the base frame in the slot of \(\mathsf T\), although the connection is torsion-free. The equivariant lifts \(\mathbb D_a=u_a{}^b\hat e_b\), with \(u_1{}^1=u_2{}^2=\cos\psi\) and \(u_1{}^2=-u_2{}^1=-\sin\psi\), and \(\mathcal S_{12}=\xi\) satisfy both relations exactly, with \(\mathsf T=0\), \(\mathsf F=0\) and \(\mathsf R_{12}{}^{12}=-1\), that is \([\mathbb D_1,\mathbb D_2]=-\mathcal S_{12}\); the opposite orientation of \(u\) gives \(\mathsf T\neq0\), and \(\mathcal S_{12}=-\xi\) violates the first relation. The \(\mathbb D_a\) are divergence-free in \(\sin\theta\,\mathrm d\theta\,\mathrm d\varphi\,\mathrm d\psi\), so \(\mathsf t_a=0\); \(-\mathsf R_{ab}{}^{ae}=\delta_b{}^e\) is the Ricci tensor of the unit sphere; and for every real \(\lambda=\lambda^{12}\) on the base, \([\lambda\mathcal S_{12},\mathbb D_a]=\lambda^c{}_a\mathbb D_c-(\mathbb D_a\lambda)\mathcal S_{12}\), the local rotation of the class. When the curvature is nonzero the commutator of two lifts is not in the span of the lifts over the base functions, so the slot \(\tfrac12\mathsf R_{ab}{}^{cd}\mathcal S_{cd}\) of the class relation is not optional. Its coefficient depends on the basis: for \([\hat e_1,\hat e_2]\) the \(\xi\)-component is \(-1\) in the basis \((\hat e_a,\xi)\) and \(-\csc^2\theta\) in the basis \((e_a,\xi)\), while in the equivariant basis \((\mathbb D_a,\mathcal S_{12})\) it is the constant \(\mathsf R_{12}{}^{12}=-1\). With \(x\) the unit vector of the base point and \(\rho_i=\varepsilon_{ijk}x_j\partial_k\), the lifts \(\tilde\rho_i=\rho_i+c_i\xi\), with \(c_1=-\cos\varphi/\sin\theta\), \(c_2=-\sin\varphi/\sin\theta\) and \(c_3=0\), commute with \(\mathbb D_a\) and \(\mathcal S_{12}\), and \(\sum_i\tilde\rho_i^2=\mathbb D_1^2+\mathbb D_2^2+\mathcal S_{12}^2\). The gauge parameters of \(A_a\) are base functions \(\Lambda\), with \(\mathcal S_{12}\Lambda=0\). On them the ghost operator \([\hat X^a,[\hat X_a,\Lambda]]=-(\mathbb D_1^2+\mathbb D_2^2)\Lambda\) is minus the Laplace--Beltrami operator, with spectrum \(l(l+1)\) and multiplicity \(2l+1\). The redundancy \(\sum_ix_i\rho_i=0\) of the base lifts to \(\sum_ix_i\tilde\rho_i=-\mathcal S_{12}\), which vanishes on base functions.

Two truncations to finite matrices keep different parts of this structure. In the first, the relations are Lie-algebraic here. In the spin-\(j\) representation, \(N=2j+1\), the matrices \(\hat X_a=J_a\) (\(a=1,2\)) and \(\mathcal S_{12}=\mathrm iJ_3\) satisfy both relations with \(\mathsf T=0\), \(\mathsf F=0\) and \(\mathsf R_{12}{}^{12}=-1\) for every \(N\). For the unit four-sphere, \(\hat X_a=\mathrm i\rho(E_{a5})\) and \(\mathcal S_{ab}=\rho(E_{ab})\) do the same for any finite-dimensional unitary representation \(\rho\) of \(\mathfrak{so}(5)\), checked in dimensions \(4\), \(5\) and \(20\). The commutative algebra \(\mathcal A\) does not survive at finite \(N\). On a finite-dimensional Hilbert space a commutative \(*\)-algebra is spanned by its minimal projections \(P\). A derivation \(\delta\) that preserves the algebra obeys \(\delta(P)=2P\delta(P)\), hence \(P\delta(P)=0\) and \(\delta(P)=0\). So every \(\mathrm{ad}\,\hat X_a\) that preserves \(\mathcal A\) vanishes on it, and no base of positive dimension is realised. Within this, the projection \(P_L\) of \(L^2(Z)=\bigoplus_jV_j\otimes V_j^*\) onto \(j\le L\) commutes with \(\mathbb D_a\), \(\mathcal S_{12}\) and \(\tilde\rho_i\), so the compressions \(P_LM_fP_L\) of the multiplication operators \(M_f\) satisfy \([\hat X_a,P_LM_fP_L]=P_LM_{\mathrm i\mathbb D_af}P_L\). It follows exactly that the relations hold on the range of \(P_L\), that \(\sum_i(P_LM_{x_i}P_L)\,\tilde\rho_i=-\mathcal S_{12}P_L\), and that the ghost operator has the eigenvalue \(l(l+1)\) on the compressed base functions with multiplicity \(2l+1\) for \(l\le2L\). Commutativity fails only at the cutoff: \(P_LM_fP_LM_gP_L-P_LM_{fg}P_L=-P_LM_f(1-P_L)M_gP_L\) vanishes on the blocks \(j\le L-l\) for \(g\) of degree \(l\), and is nonzero on \(j=L\) for \(f,g\) of degree one. The second truncation, the fuzzy sphere, keeps the isometries instead. With \(X_i=J_i/\sqrt{j(j+1)}\) one has \([X_i,X_j]=\mathrm i\hbar_{\mathrm{eff}}\varepsilon_{ijk}X_k\), with \(\hbar_{\mathrm{eff}}=1/\sqrt{j(j+1)}\). The inner derivations \(\mathcal L_i=\hbar_{\mathrm{eff}}^{-1}\operatorname{ad}_{X_i}\) obey the Leibniz rule and \([\mathcal L_i,\mathcal L_j]=\mathrm i\varepsilon_{ijk}\mathcal L_k\) exactly, and \(\sum_i\operatorname{ad}_{X_i}^2/\hbar_{\mathrm{eff}}^2\) on \(\operatorname{End}(\mathbb C^N)\) has the spectrum \(\{l(l+1):0\le l\le N-1\}\) with multiplicity \(2l+1\). By the Casimir identity above, this is the ghost spectrum on base functions, truncated. For odd \(N\) its Hilbert space \(V_j\) is the span of the functions of right weight \(j\) in the block \(j\), which the \(\tilde\rho_i\) preserve and \(\mathbb D_1\) does not, so this truncation carries no frame index. Moving coefficient functions across its product errs from the Poisson bracket at order \(\hbar_{\mathrm{eff}}\) (numerical). The redundancy of the base frame depends on the ordering: on the spin-\(l\) part \(F\) of \(\operatorname{End}(\mathbb C^N)\), \(\sum_iX_i\mathcal L_iF=\tfrac12\hbar_{\mathrm{eff}}\,l(l+1)F\), while \(\tfrac12\sum_i\{X_i,[X_i,F]\}=\tfrac12[\sum_iX_i^2,F]=0\). Compare the Berezin--Toeplitz finite-size regularization of covariant-derivative configurations, including \(S^2\), of \cite{HattoriSekoTsuchiya2026}. For the Lorentzian fibre the first truncation is not available. \(\mathfrak{so}(3,1)\) is simple and not compact, so every representation of it by anti-Hermitian matrices of finite size is zero, and with \(\mathcal S_{cd}=0\) the first relation at \(a=d\neq c\) gives \(\mathbb D_c=0\). Finite matrices that satisfy both relations with \(\eta\), such as the fundamental representation of \(\mathfrak{so}(4,1)\), have generators that are anti-self-adjoint only for an indefinite form; this is the fact behind the statement in Section~\ref{sec:status-E} that the members with a non-compact five-index algebra exist only for \(N\to\infty\). The toy is compact in base and fibre, Abelian in fibre and two-dimensional. It retains neither \(\mathrm{SO}(3,1)\) nor the \((7,3)\) kinetic signature nor the selection of the class by the matrix equation. It does not derive \(\mathcal A\), the frame or its non-degeneracy, so Assumptions~\ref{ass:frame-lock}, \ref{ass:nondeg} and~\ref{ass:local-lorentz} are not discharged.

\paragraph{The locked frame as a gauge-invariant composite (conditional; not closure).}
Elitzur's theorem \cite{Elitzur1975} rules out a nonzero expectation value of a gauge-variant local field for a compact structure group. Fradkin and Shenker \cite{FradkinShenker1979} showed that, for Higgs fields in the fundamental representation, the Higgs and confinement regimes of such theories are analytically connected without any local order parameter. Both statements are established for compact gauge groups on the lattice; their extension to the noncompact frame group is not established. The expectation value of Equation~\eqref{eq:VEV} is gauge-covariant under Equation~\eqref{eq:Phi-transform}. On a gauge-invariant reading, which Chapters~\ref{ch:vierbein-emergence} and~\ref{ch:lorentz-locking} do not adopt, the locking of Assumption~\ref{ass:frame-lock} would be represented not by the nonzero expectation value itself but by composites that are bilocal in the base, in the spirit of the bilocal fields of \cite{HoKawaiSteinacker2025}, with parallel transporters built from the connection of the class above relating the two points; the composite metric of Equation~\eqref{eq:g-from-e} is invariant under tangent-space rotations. On that reading Assumption~\ref{ass:nondeg} would become a non-degeneracy statement about the two-point composite rather than a consequence of a broken symmetry, and the locking would be read as a complementarity of regimes rather than a local spontaneous breaking. The construction presupposes the connection content that the closure of Problem~D1 in Chapter~\ref{ch:agenda} requires to be specified. It is recorded as a mechanism whose selection by the matrix dynamics is open, and it discharges neither Assumption~\ref{ass:frame-lock} nor Assumption~\ref{ass:nondeg}. Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
```

**Labels referenced.** Each has exactly one `\label`, and none is added: `ass:frame-lock`, `ass:local-lorentz`, `ass:nondeg`, `ch:agenda`, `ch:lorentz-locking`, `ch:vierbein-emergence`, `eq:Phi-transform`, `eq:VEV`, `eq:g-from-e`, `sec:status-E`.

**Citations.** `HoKawaiSteinacker2025` is already in the bib. Three keys are new: `HattoriSekoTsuchiya2026`, `Elitzur1975` and `FradkinShenker1979`, in the file `bib-additions-local-r2.bib`, verbatim:

```bibtex
@article{HattoriSekoTsuchiya2026,
  author  = {Hattori, Keiichiro and Seko, Tatsuya and Tsuchiya, Asato},
  title   = {Description of curved spacetimes by finite-size matrices in the type {IIB} matrix model},
  journal = {Prog. Theor. Exp. Phys.},
  year    = {2026},
  pages   = {083B01},
  doi     = {10.1093/ptep/ptag120},
  eprint  = {2606.24577},
  archivePrefix = {arXiv}
}

@article{Elitzur1975,
  author  = {Elitzur, Shmuel},
  title   = {Impossibility of spontaneously breaking local symmetries},
  journal = {Phys. Rev. D},
  volume  = {12},
  pages   = {3978--3982},
  year    = {1975},
  doi     = {10.1103/PhysRevD.12.3978}
}

@article{FradkinShenker1979,
  author  = {Fradkin, Eduardo and Shenker, Stephen H.},
  title   = {Phase diagrams of lattice gauge theories with {H}iggs fields},
  journal = {Phys. Rev. D},
  volume  = {19},
  pages   = {3682--3697},
  year    = {1979},
  doi     = {10.1103/PhysRevD.19.3682}
}
```

**Integrator sequence.** Add the bib entries first, then apply the appH insert, then build once. Since `build_check.py` does not run bibtex, the integrator must run bibtex once for the three new keys or they will show as undefined.

**Stale passages.** None are introduced. The ch03 "broken generators", ch10 and ass:nondeg wording is deliberately not harmonised with the composite reading, because the reading is not adopted (M3).

## Verification scripts

All are in `proposals/local-gpu/059-d1-lorentz-local-frame/` and run with `python -I`.

- `d1_equivariant_toy_symbolic.py` -> `.out`: **21 PASS, ALL PASS**. Exact sympy checks, groups (A)-(E) as listed in the docstring. Invariants:
  - "T = 0 fixes the orientation ... sgn=-1";
  - "S_12 = (1) xi";
  - "R_12^12 = -1";
  - "bundle redundancy ... (-1) xi = (-1) S_12";
  - "Y_lm eigenvalue l(l+1), all 2l+1 m, l<=4".
- `d1_equivariant_finiteN.py` -> `.out`: **31 PASS, ALL PASS**. Invariants:
  - A: one-sided redundancy = (hbar^2/2) l(l+1) F, with error <= 2.6e-15, and symmetric = 0, for N = 5..31;
  - A4: slope -1.065;
  - B1: N = 2..31;
  - B2: so(5) representations 4, 5 and 20 exact;
  - B3: |S_01 + S_01^dag| = 2.83;
  - C3: rank 9 / 25 / 49 for L = 1 / 2 / 3;
  - C4: c = +1.000000;
  - C5: the defect on blocks j < L is 0.0e+00.
- `apply_and_build_local_r2.py` -> `.out`: simulation with the hashes above.
  - With `--build` it copies chapters, frontmatter, bib, figs and the root tex/graphics into `tempfile.mkdtemp()` outside the repository and applies the insert and bib additions there. It then runs pdflatex, bibtex, pdflatex and pdflatex, scans the log, and removes the temp copy with `shutil.rmtree` restricted to that temp directory (there is no `rm -rf`).
  - The result this round: all passes rc 0, 404 pages, **0 undefined/multiply-defined warnings**, no bibtex warnings for the new keys, BUILD CLEAN, temp copy removed.
  - The repository appH is unchanged: sha256 4ea0ee0f... before and after.
- Superseded and kept for the record: `d1_toy_class_symbolic.py` (the non-equivariant r3 toy) and `d1_finiteN_class.py` (the r3 fuzzy checks). Their content is subsumed by E1(A) and E2(A).

**Reproduction pack:**
```
python -I proposals/local-gpu/059-d1-lorentz-local-frame/d1_equivariant_toy_symbolic.py   # ends "ALL PASS" (21 PASS)
python -I proposals/local-gpu/059-d1-lorentz-local-frame/d1_equivariant_finiteN.py        # ends "ALL PASS" (31 PASS)
python -I proposals/local-gpu/059-d1-lorentz-local-frame/apply_and_build_local_r2.py      # pre 4ea0ee0f..., post b6ce7529..., 711900 B
python -I proposals/local-gpu/059-d1-lorentz-local-frame/apply_and_build_local_r2.py --build   # BUILD CLEAN, 0 warnings
```

## Decisions Taken

- **M1 (RESEARCHER-DECISION): option (b), recompute with equivariant lifts.**
  - *Reason:* (b) puts the toy inside the class, satisfying both relations with T = 0, consistent with local 068. It also makes the ghost and redundancy statements genuinely about the class's operators, and it yields the frame-equivariant finite-N truncation, which carries data for the D1 finite-N question.
  - *Rejected:* option (a), relabelling, which would have kept a toy outside the class and contributed nothing positive.
  - *Sign:* S_12 = +xi for the stated lift e_a - omega_a xi. This differs from the gatekeeper's -xi only by the orientation convention psi -> -psi; the invariant data T = 0, F = 0 and R = -1 agree.
- **Fuzzy redundancy:** replace the fitted O(hbar) statement with the exact ordering-dependent identity. The fit was correct but weaker, and the exact identity also shows that the symmetric ordering has no defect, which avoids an overstatement.
- **Lorentzian bounded obstruction:** record it with its four hypotheses and the ranked relaxations. The Krein-space finite-N realisation is ranked first as the next positive-aimed package.
- **M3:** apply verbatim and keep the reading conditional. Adopting it is STRUCTURAL and is not proposed.
- **Anchor:** insert before `\section{Problem E: signature}`, which is unique, rather than after the non-unique status sentence.
- **Status sentence:** one sentence for the contiguous two-paragraph block, at its end: "Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL." This matches the scope of the class paragraphs. The first paragraph closes with a scope sentence (not discharged) and no status sentence.

## Milestone assessment

Routine. These are conditional sub-lemmas on a compact toy and finite-N structure lemmas. No critical-path step is derived from the matrix theory, and no MILESTONE.md trigger applies.

## Status-label recommendation

- **Critical-path set, re-derived from ch17 and appH:** A, B, C, D1, E, F, G-derived, N.
- **Problem D labels:** unchanged (OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL).
- **Label changes proposed:** none.

## Author decision needed

None.

## Remaining open step

D1 still requires all of the following:
- derive from the matrix integral the selection of the first-order class, or an equivalent one, together with its algebra A;
- derive the locked frame and its non-degeneracy, which discharges ass:frame-lock and ass:nondeg;
- specify omega, A_mu, B and the ghost operators with the field content at the Lorentzian fibre;
- give a regulated trace, or a finite-N form, for the Lorentzian class.

The next packages follow the ranking above:
1. Krein-space finite-N realisation at the de Sitter point: ghost operator and quadratic form.
2. A noncommutative coefficient algebra replacing A, with a non-degeneracy criterion.
3. Euclidean so(5) with reflection, which is gated on E.

## Special instructions for the gatekeeper

- Re-run the three scripts with `python -I` and compare against the saved `.out` files and the hashes above.
- Re-derive by hand:
  - the orientation and sign of S_12 for the stated lift;
  - [D_1, D_2] = -S_12;
  - the finite-dimensional derivation lemma, including why *-closure is needed;
  - the so(3,1) argument (simple and non-compact implies no nonzero anti-Hermitian finite representation; then (I) gives D = 0);
  - the fuzzy redundancy identity.
- Must NOT be asserted:
  - closure or narrowing of D or D1;
  - discharge of ass:frame-lock, ass:nondeg, ass:local-lorentz or ass:lorentzian;
  - adoption of the gauge-invariant reading;
  - that the finite truncations realise A or a base;
  - any statement about SO(3,1) at finite N beyond the bounded obstruction with hypotheses (h1)-(h4);
  - transfer of the Elitzur or Fradkin-Shenker results to the noncompact group.
- Check that the "Section~\ref{sec:status-E}" sentence correctly paraphrases appH L1735.
- Report, without fixing: no ch17-vs-appH discrepancy was found for D. The verdict on local 068 is unchanged, and its T = 0 convention is now consistent with this toy.
