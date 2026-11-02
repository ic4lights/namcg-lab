# Proposal 050-frame-bundle-local-lorentz, round 1

## Result

Target: Problem D1, the local Lorentz gauge symmetry from the matrix algebra. D1 stays OPEN. Nothing here is DERIVED in the Chapter 17 sense.

1. **Bounded obstruction (exact, Poisson limit).** In the conjugate-coordinate class on the single orbit CP^{1,2}, the matrix gauge group gives no six-parameter local rotation of the frame index.
   - Fibre orders do not mix: a parameter of fibre order J acts on T^a at order J. So only J = 1 acts on the frame at linear order, which gives three functions xi.
   - The algebraic action of xi is a rotation by a bivector in the 3-dimensional W_y. W_y is not a subalgebra of so(3,1) for m != 0.
   - Its boost part equals the displacement of y: y_nu lambda^{nu sigma} = -s m xi^sigma.
   - No nonconstant parameter fixes y. No SO(4,1)-equivariant base carries a vertical so(3,1).
   - This also fills in the "algebraic part" that merged text left uncomputed at the first-order response paragraph. It is smaller than the Maxwell shift by the factor 1/(sinh tau cosh tau |q| l).

2. **The hypothesis that fails is the representation, and relaxing it works at tree level (conditional).** Same action, C = 0, no new field and no fundamental metric: take the operators to be the first-order equivariant class, a commutative algebra A, derivations D_a, and a free unitary SO(3,1) action S_cd closing with D_a. This is the Hanada-Kawai-Kimura construction, read here with the Lorentzian matrix contraction. In that class:
   - six arbitrary local rotations are unitary conjugations, with e rotating and omega shifting inhomogeneously;
   - longitudinal diffeomorphisms are present;
   - the Dirac operator has the connection term that the merged text records as absent in the four-coordinate class;
   - the matrix equation decomposes exactly into three parts; at T = 0 it is Ric = 0 plus free Maxwell.
   Checked exactly on pp-waves, Schwarzschild, Kasner, de Sitter and S^2 x R^2.

3. **New relative to the cited source (as far as I could check):**
   - the full formula with torsion, checked on unrelated e and omega;
   - the linear spectrum with torsion: 14 null solutions beyond gauge, of which 2 are torsion-free with simple zeros, and 6 of the 12 torsion modes head double zeros at q^2 = 0;
   - the link to the merged class: T_a, M_ab in the regular representation of SO(4,1) obey the same identity with the same mu^2 = -3, with base dS_4;
   - generators from commutators on rank-six curvature (Schwarzschild, Kasner);
   - the order-zero no-source statement as an exact lemma, and its relaxation by a compact factor, with an exact null Kaluza-Klein solution.

**Not established:** that the matrix integral selects this class; the frame or non-degeneracy; a regulated action or norm; loops; sources beyond Kaluza-Klein fields; G_eff; any statement on Ostrogradsky ghosts; the identification with Presentation B or with the emergent metric.

## Target and status

Verbatim from `chapters/appH-microscopic-proofs.tex`, Problem D ledger label: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."

**Original target (ch17, Section done, item D1):** "an SO(3,1) gauge symmetry is derived from the matrix algebra and condensate, with the omega, A_mu, B and ghost operators specified and the field content stated. The locked frame and its non-degeneracy on the claimed domain are derived, not assumed (Assumptions frame-lock and nondeg)."

**Classification of this package:** PROGRAMME-CONDITIONAL. It also touches F and N only as stated scope limits. No label change.

**Dependencies used:** merged conjugate-coordinate paragraphs in sec:status-F (notation, field equation with the bilinear term, W_y); opening of sec:status-D (Leibniz defect); Definition matrix-coords (operator-valued Theta allowed).

**Discrepancies:** none between ch17 and Appendix H on D. Ch17 and Appendix H both name D1 as critical path.

### Why this target, honestly

Candidates weighed, on the Chapter 17 criterion:

| Candidate | What it could decide | Expected value |
|---|---|---|
| 049 avenue 1 (non-derivative sector on x < x_0) | Whether a branch with tuned tree data gives a long-range force | Low to moderate. 049 shows the branch needs supplied tree data with the loop term not small, so even a good answer is a statement about a tuned point in the same class |
| 049 avenue 2 (rotating K, 2509.24753) | Whether a K the theory selects gives beta_K near 1 | Moderate, and the natural next package on C. Same frozen-symbol hypotheses on CP^{1,2}, and merged text already shows exponent -1/6 for the homogeneous mode |
| D1 | A critical-path problem with no direct package since 043 | Higher. A bounded result either way changes the direction. The 2026-11-01 SME scout ranks D1 next after its R1 and R2, which 048 and 049 have now taken |

I judge that one more package on B, C, F, N in this class has lower expected value than breaking out, and I chose D1. The computation then gave more than the bounded no-go that the scout predicted. It did not give closure.

## Source reading

**Method: digest + targeted reads. No full scan.** The package changes no definition, assumption, scope or status passage, and only adds paragraphs.

- `make_digest.py --check` printed DIGEST CURRENT. `dirty-chapters: yes`, as the task states, because of the 049 integration, so I read the working-tree files.
- **Read in full:** digest; 049 review-r4; sme-scout-20261101-after45; ledger section list and 048-049 avenues.
- **Appendix H:** L332-398; L565-904 (start of Problem D through the real-block paragraph); L2096-2170 (conjugate-coordinate paragraphs); L2490-2547 (049 insert).
- **ch17:** L50-160, L325-385, L695-754.
- **ch03:** L90-280, L340-385. **ch10:** L30-160.
- **Not read:** Appendix H L905-1345 (rest of D, on Presentation-B completed actions); I grepped them for D1 and Hanada, Kawai and frame-bundle terms, with no hits. Other chapters only through the digest and label index.
- **Unreadable files:** none. The arXiv PDF of 2509.06646 came back as binary through the fetch tool, so I used its HTML version.
- **Process slip:** my first tool rounds batched read-only calls, against the serial rule. Nothing changed, and later calls were serial.

## Research and reasoning

### A. Conjugate-coordinate class

Notation: T^a = M^{a4}, y^mu = M^{mu5}, m = M^{45} = y^4, R = 1, {T^a,y^mu} = s eta^{a mu} m, {T^a,T^b} = s M^{ab}, {y^a,y^b} = -s M^{ab}, y.y = y_mu y^mu = -l^2 - m^2.

**Formula for M.** At y^i = 0 the merged fibre structure (self-duality on y-perp) gives T^i = (y^0/l) n^i, M^{i0} = (m/l) n^i, M^{ij} = sigma eps^{ijk} n^k, with |n| = l (found numerically: |n|^2 / l^2 = 1 to 1e-12). Covariantly,

M^{mu nu} = [ m (y^mu T^nu - y^nu T^mu) + sigma l eps^{mu nu rho lam} y_rho T_lam ] / y.y.

The realisation fits this with sigma = +1, residual 5e-13 (s4).

**Action of xi.** For Lambda = xi_mu(y) T^mu, with xi.y = 0 (allowed because T.y = 0):
- {Lambda,T^nu} = xi_mu s M^{mu nu} + T^sigma d_rho xi_sigma {y^rho,T^nu} = lambda^nu_sigma T^sigma - s m T^sigma d^nu xi_sigma,
- lambda^{nu sigma} = (s/y.y)[ m (xi^nu y^sigma - y^nu xi^sigma) + sigma l eps^{mu nu rho sigma} xi_mu y_rho ].

The term m xi^nu y^sigma contributes zero on T_sigma and makes lambda antisymmetric. Then:
- {Lambda,y^mu} = s m xi^mu - s T^sigma d_rho xi_sigma M^{rho mu};
- y_nu lambda^{nu sigma} = -s m xi^sigma, cancelling the displacement so that y.T = 0 is preserved. That is the content of "boost = displacement".

**W_y is not a subalgebra.** With K, J the boosts and rotations about y, the commutator of aK(xi)+bJ(xi) with aK(xi')+bJ(xi') is (b^2 - a^2) J(xi x xi') + 2ab K(xi x xi'), up to a sign convention. For it to stay in the span with a, b both nonzero needs a^2 + b^2 = 0, and for b = 0 it fails. So it closes only for a = 0, i.e. m = 0. Exact dimension of W + [W,W] is 6 at the four base points and 3 at y^4 = 0 (s4c).

**Selection rule.**
- For zeta with zeta.y = zeta.zeta = 0, (zeta.T)^J is a harmonic polynomial of degree J on the fibre.
- Terms from {f (zeta.T)^J, T^a}: (zeta.T)^J {f,T^a}; (zeta.T)^{J-1} T^mu {zeta_mu,T^a}; (zeta.T)^{J-1} zeta_mu M^{mu a}.
- Using M: zeta_mu M^{mu a} = [ -m y^a (zeta.T) + sigma l (eta.T) ]/y.y with eta^lam = eps^{mu a rho lam} zeta_mu y_rho, and eta.y = eta.zeta = 0.
- (zeta.T)^{J-1}(eta.T) has fibre Laplacian proportional to zeta.eta = 0.
- The derivative term has Laplacian proportional to zeta^mu d zeta_mu = (1/2) d(zeta.zeta) = 0.
- So the output is order J exactly. s4d: projections on levels 0..6 for J <= 4 show only level J.

Scope: linear order about T^a. The field-dependent part {Lambda, A^a} is not covered.

**No vertical parameter.**
- {Lambda,y^mu} = 0 gives {Lambda,{y^mu,y^nu}} = 0 by Jacobi, so {Lambda,M^{mu nu}} = 0.
- T^mu = -M^{mu sigma} y_sigma / y^4 and y^4 is a function of y on the sheet, so {Lambda,T^mu} = 0.
- All 15 generators commute with Lambda, and they separate points, so Lambda is constant on the connected sheet.

**Equivariance.** The stabiliser in SO(4,1) of a point of the sheet is U(2) (10 - 6 = 4 dimensions, over H^4 with SO(4) acting on S^2 through SU(2)). An equivariant map to G/SO(3,1) would need U(2) conjugate into SO(3,1), whose compact subgroups have rank one.

**Exact hypothesis class of the obstruction (O-orbit):** Poisson limit; one orbit CP^{1,2}; base functions y^mu; gauge parameters that are functions on the leaf; linear order about T^a; four matrix coordinates with extra matrices not acting on y at this order.

### B. Fork: every hypothesis and its relaxation

| Hypothesis | Relaxation | What it gave | Status |
|---|---|---|---|
| Single minimal orbit (irreducible) | Regular representation of the same so(4,1) | Same T_a, M_ab and same identity, with M_ab vertical and base dS_4 | Done (s5a) |
| Base functions noncommuting and generating the leaf | Commutative A with [X,A] in A | Leibniz defect absent, six functions | Done (section C) |
| Compact fibre | Non-compact SO(3,1), unitary regular representation | Boost generators anti-Hermitian | Done, domains not treated |
| Bilinear term required (CP^{1,2}) | Drop it | Ricci-flat solutions of the quartic term alone | Done (s1) |
| Matter order zero | Extra first-order matrices along a compact factor | Kaluza-Klein stress in Ric(4) | Done, one exact example (s5d) |
| Tree level | Loops | Not attempted | Open |
| Frozen wave on flat space for the torsion spectrum | Curved background; norm | Not attempted; a frozen estimate on de Sitter is unreliable since the commutators of D are of the same order as the mass scale | Open |
| Finite-rank variations only | Regulated action | Not attempted; the naive trace is not cyclic on these operators by my own hand estimate, see below | Open |

Fermion content, the Lorentzian contraction and the choice of A are kept as stated.

### C. First-order equivariant class

**Algebraic definition (no manifold assumed).** H separable, X_a = i D_a Hermitian, A commutative *-algebra, [D_a, A] in A, S_cd anti-Hermitian derivations forming a free proper unitary action of SO(3,1), relations

- [S_cd, D_a] = eta_ad D_c - eta_ac D_d,
- [D_a, D_b] = -T_ab^c D_c + (1/2) R_ab^cd S_cd + Phi_ab,

coefficients in A, D_a and S_cd pointwise independent on the spectrum Z of A. Absolute parallelism with these relations reconstructs the principal bundle Z -> Z/SO(3,1) with frame and connection (the Cartan-connection reconstruction; standard, no citation is added and it can be dropped if the gatekeeper prefers). Coordinates give:

D_a = u_a^b e_b^mu ( d_mu - u_f^g w_mu^c_g d/du_f^c ) + t_a - i A_a, t_a = (1/2) T_ac^c.

**Hermiticity.** div D_a = T_ac^c in the measure |det e|^{-1} d^4y dHaar(u) (exact in s2). Reason: the vertical part is a coefficient times Haar-divergence-free right-multiplication fields.

**Equation.** From the two relations only (treating Phi as central, which is the extra-coordinate device of s2b):

[D^a,[D_a,D_b]] = (-D^a T_ab^e + T_ab^c T^a_c^e + R_ab^{ae}) D_e + (1/2)(D^a R_ab^de - T_ab^c R^a_c^de) S_de + (D^a Phi_ab - T_ab^c Phi^a_c).

Derivation of the middle term: -T_ab^c [D^a,D_c] gives T T D - (1/2) T R S - T Phi. (1/2) R_ab^cd [D^a,S_cd] = -(1/2) R_ab^cd (delta^a_d D_c - delta^a_c D_d) = R_ab^{ae} D_e.

Independence of D_e, S_de and the order-zero part makes each bracket vanish. At T = 0: R_ab^{ae} = -Ric_b^e (s1, sign tested on backgrounds with Ric != 0). The second bracket is D^a R_ab^de, which vanishes given Ric = 0 by the Bianchi identity. In the form of~HKK Eq. 103 the third is nabla^a Phi_ab = 0.

**Bilinear term.** The merged equation {X^b,{X_b,X_a}} = mu^2 X_a with [ , ] -> i{ , } is [X^b,[X_b,X_a]] = -mu^2 X_a. With X = iD, [X^b,[X_b,X_a]] = Ric_a^e X_e, so Ric_ab = -mu^2 eta_ab. At mu^2 = -3 this gives Ric = 3 eta, which s1 finds on the conformal chart of de Sitter and s5a finds on the regular representation.

**Local rotation.** For lambda^cd = u^c_f u^d_g lambda-hat^fg(y): [ (1/2) lambda^cd S_cd, D_a ] = lambda^c_a D_c - (1/2)(D_a lambda^cd) S_cd, by the first relation. The same vertical vector field equals the left action on the second index of u with parameter lambda-hat(y). So it is the pull-back by a vertical automorphism of Z, a unitary operator on L^2(Z). HKK Eqs. 139-140 state the corresponding e and omega transformations.

**Field content and ghosts.** e (16), omega (24), A (4); gauge parameters 6 + 4 + 1. The class of first-order operators is closed under commutators, hence consistent as a truncation of the equation of motion, and equivariance is preserved because the background is invariant under the diagonal of the global index rotation and the right action. Ghost operator in background gauge: [X^a,[X_a, . ]] on End(H), the same formula as the matrix action. Merged operators in the conjugate-coordinate class are unaffected.

**Dirac.** gamma^a u_a^b = rho(u) gamma^b rho(u)^{-1} with rho(uv) = rho(u) rho(v). On Psi = rho(u) psi(y), along u -> u(1 - w_mu), rho changes by rho X with X = (1/4) w_{mu ab} gamma^a gamma^b, since [X, gamma^c] = -gamma^d w^c_d (s5b, including a finite check). Hence gamma^a D_a Psi = rho(u) gamma^b e_b^mu (d_mu + (1/4) w_{mu cd} gamma^c gamma^d) psi at t = A = 0.

**Central Theta.** On the flat bundle a_a = -(1/2) Theta_ab (u^{-1} y)^b gives D_a a_b - D_b a_a = Theta_ab (s5e), so X_a = i D_a + a_a satisfies Equation eq:NC with c-number Theta. Since [a_a, f] = 0 for f in A, K is unchanged, and the equation of motion holds because the commutator is central. This breaks the diagonal Lorentz group to the stabiliser of Theta. **Note:** the insert writes A_a proportional to this, without the numerical factor.

**Sources.** X^i = phi^i tensor L^i with phi^i in A and fixed Hermitian L^i: [X^i,[X_i,i D_b]] = -i phi_i (D_b phi_j) [L^i,L^j], order zero. So the first bracket stays. At T = 0 this means Ric = 0 for every order-zero bosonic field and for order-zero fermion bilinears.
Exact hypothesis class (O-source): tree level, matter in A tensor a fixed factor.
Relaxation tested: first-order extra matrices along a compact factor give Ric^{(D)} = 0. The null wave of s5d has Ric(5) proportional to (c0 + f0^2/2) and Ric(4)_00 = -c0, with F = f0 e^2 ^ (e^0 + e^1), so Ric(4)_00 = (1/2) F_02^2 exactly at c0 = -f0^2/2.

### D. Linear spectrum

D_a -> D_a - h_a^c D_c + (1/2) w_a^cd S_cd gives T_ab^c = d_a h_b^c - d_b h_a^c + w_b^c_a - w_a^c_b and R_ab^cd = d_a w_b^cd - d_b w_a^cd, derived from the relations. Equations:
- E1 = -d^a T_ab^e + R_ab^{ae};
- E2 = d^a R_ab^de;
- E3 = d^a (d_a t_b - d_b t_a).

Gauge: delta h_a^c = q_a xi^c and, for the rotation, delta w_a^cd = q_a lam^cd with delta h_b^g = lam^g_b, in the rescaling w = i wt.

Results (s3, exact):
- generic q: rank 30 of 40, kernel exactly the 10 gauge directions, at three sampled q;
- E3 does not change the rank at the sampled q;
- null q = (1,1,0,0): kernel 24, so 14 beyond gauge;
- T = 0 subspace: 12 dimensions = 10 + 2, with R rank 2 (the graviton polarisations);
- T totally antisymmetric: 13 dimensions, so 1 beyond those;
- chains: along q = (1+eps,1,0,0) and (1+eps,1,eps,0), the numbers of chains of length >= k beyond gauge are 14, 6, 0, ...;
- the 6 heads have R = 0, T rank 6, trace rank 1, axial rank 1, non-axial rank 6; none is torsion-free, and the totally antisymmetric mode is not among them.

Lorentz covariance makes all null q equivalent up to scale, so one null q suffices given the global diagonal symmetry. The two lines are a test, not a proof of independence from the line.

**No norm.** Why I attach no norm: on first-order operators, Tr F^2 is a phase-space integral with moments <pp> and <pi pi> of a cutoff. A variation with S-valued delta X gives different moments on the two sides of cyclicity under a hard cutoff, so I do not trust any action-level statement here (hand estimate, not in the insert). Stationarity against finite-rank variations is well defined and is the reading used.

### E. Literature

**Verified:**
- hep-th/0508211, Hanada-Kawai-Kimura, record fetched: Prog. Theor. Phys. 114 (2006) 1295-1316, DOI 10.1143/PTP.114.1295.
- Body through ar5iv HTML by the fetch tool: V_reg, Eqs. 38, 43, 98, 103, 106, 108, 133, 136-140; torsion set to zero with a propagating rank-three antisymmetric field stated; no energy-momentum term classically; divergent naive trace; Spin(10) with Euclidean form. These equation numbers are as reported by the tool's reading, not by my reading of raw LaTeX. The gatekeeper should confirm any it relies on.
- arXiv:2509.06646, Ho-Kawai-Steinacker, "General Relativity in IIB Matrix Model", HTML v2 through the same tool. "So far, this does not appear to have been very successful" (second category, matrices as momenta); the classical matrix action "cannot be interpreted as the Einstein-Hilbert action"; E-H action at one loop on the noncommutative background; no fibre in the commutative vacuum.

**Tension, not contradiction.** Those authors' judgement bears directly on this route. Their statements concern the action and a vacuum without this fibre; the insert's statements concern the equation of motion. I did not determine what specifically they consider unsuccessful. The evident gaps (no source, divergent trace, selection, bilocal modes) are the ones listed as untreated.

**Not independently verified:** Cartan-connection reconstruction as a citation (used as standard mathematics, not cited). The SME's statements on 2601 App. A.2-A.3 were not re-read, and the insert does not rely on them.

**Rotating K (2509.24753):** not read in this package.

## Claim classification

| Claim | Class |
|---|---|
| Formula for M^{mu nu}, bracket formulas, y_nu lambda^{nu sigma} = -s m xi^sigma | Established (exact; M formula by hand at rest plus numerical fit) |
| W_y not a subalgebra for m != 0 | Established (hand; exact span at four points) |
| Selection rule, no vertical parameter, no equivariant base | Established within class (hand; numerical projection J <= 4) |
| No six-parameter local rotation in the class | Bounded obstruction, hypotheses O-orbit |
| Relations imply the three-part formula | Established (algebra; exact on jets) |
| T = 0 equals Ric = 0 plus Maxwell | Established for the class; prior result of HKK; exact on six backgrounds |
| Six local rotations in U(H) | Established for the class; prior result of HKK; Lorentzian non-compact fibre: domains not treated |
| Dirac identity, de Sitter link, central Theta, curvature rank | Established (exact or numerical as labelled) |
| Spectrum numbers | Exact, linearised, flat, no norm; independence of the transversal line tested on two lines |
| Order-zero no-source | Bounded lemma, hypotheses O-source |
| Null KK solution | Established, one example |
| Class selected by the matrix integral; frame and non-degeneracy derived | Unresolved |
| Physical reading of torsion double zeros (ghost or not) | Unresolved |
| Reconstruction by Cartan connection | Standard input, not re-proved |

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`. Insert the bytes of `appH_insert.tex` immediately before the unique line `\section{Problem E: signature}` (L1346 in the current working tree; count 1 by s6). The preceding text "...leaves Problems~B, C, D, F and~G open." stays. Nothing is replaced.

Insert properties (s6): LF ASCII, 8 blocks, one closing status sentence, no new labels. Verified labels: ass:frame-lock, ass:local-lorentz, ass:lorentzian, ass:nondeg, ch:vierbein-emergence, def:matrix-coords, eq:LUV-def, eq:NC, eq:Smatrix, eq:Smicro, eq:dressed-omega, sec:status-F, sec:status-N, each count 1.

The "round " hit in the process scan is "background".

**Bib:** add the two entries of `new_bib_entries.bib` to `bib/namcg.bib`. Keys absent now.

**The LaTeX** is the file `proposals/050-frame-bundle-local-lorentz/appH_insert.tex`, not repeated here so that one copy is authoritative: LF form 14623 bytes, sha256 408a9d28fff6308559036268e399c018c0eb98cf383b48171ef449012c024c7c.

**Stale passages elsewhere:** none are false.
- L2123 and L2148-2164 (order count for E[h]) are scoped to the orbit class, and the insert says so.
- L673-675 calls a compensating frame module "a conjectured route, not a result established here" and is about the central Moyal branch; true as written.
- L873-887 ("Presentation A as specified contains no coframe...") says these facts "do not rule out an enlarged matrix construction"; true as written.
No replacement is proposed. Whether L673-675 should later point to the new paragraph is a wording choice for a later package.

**Anchor at byte level:** in this Bash tool a double backslash collapses. Match with `[\]section` or at byte level, anchor + CRLF, and convert the insert from LF to CRLF.

## Verification scripts

All in `proposals/050-frame-bundle-local-lorentz/`. Outputs are `*.r1.out.txt`, which nothing overwrites automatically; `bundlelib.py` and `cp12_realisation.py` (copy from 045) are local.

- `s1_operator_eom.py` (about 2.5 min): [S,D] rule, no D part in [D,D], [D^a,[D_a,D_b]] = -Ric_b^e D_e, exact at one point of the bundle with a rational Lorentz matrix, six backgrounds.
- `s2_torsion_eom.py` (about 1 min): full formula for unrelated e and w, d = 3 (two seeds), d = 4; div D_a = T_ac^c; exact Taylor jets at order 2.
- `s2b_order_zero.py`: order-zero bracket, d = 3.
- `s3_linear_spectrum.py`: ranks, gauge annihilation, null kernel, chains on two lines, torsion content.
- `s4_cp12_level_one.py`: formula for M; brackets; exact W_y spans; fibre-level projection for J <= 4; ratios.
- `s5_examples.py`: regular representation; spinor; curvature rank; null KK; central Theta.
- `s6_insert_mechanics.py`, `compile_check.py` (usage: python compile_check.py <dir outside the repo>, or set NAMCG_REPO).
- `make_helpers.py`: one-shot record of the r1 edits. It refuses to run twice (asserts the old text). **Do not run it.**

**Compile (`compile_check.r1.out.txt`):** baseline 339 pages; with insert and bib entries 343 pages; both exit [0,0,0,0], 0 undefined references, 0 undefined citations, 0 multiply defined labels; CRLF preserved; scratch removed.

## Decisions Taken

1. **Target: D1 over 049 avenue 1 and the rotating K.** Reasons above. Rejected alternatives remain queued. The rotating K is the natural next package on C.
2. **Route inside D1: representation relaxation rather than stopping at the orbit no-go.** Directive: a no-go is a fork. The frame-bundle class changes no action term, and adds no field.
3. **Emergence decision.** I treat the class as a choice of operators in the matrix model, defined algebraically: A, D, S. Z, M, e, omega are read off from them, and the action contains only the constant eta. The SME warned about taking the manifold as given. I decided this reading keeps spacetime emergent at the same standard as CP^{1,2}, which is also a supplied background with supplied base functions (merged L2126). I state plainly that selection of the class and of A is not derived. If the gatekeeper judges the reading insufficient, the fix is to narrow the wording, not to add structure.
4. **Equation of motion, not action.** The trace diverges, so I use stationarity against finite-rank variations and make no action-level claim.
5. **Notation.** Sans-serif T and R for torsion and curvature, to avoid T^a of the class and the axial or scalar T of Problem B; blackboard D for the first-order parts, to avoid merged D^a = {T^a, . }; L^i for the internal Hermitian matrices, since Lambda is the gauge parameter.
6. **Placement:** Problem D section, since D1 is the target. No new labels.

## Milestone assessment

**Candidate M2:** a bounded no-go that rules out one route in a stated class, at the same standard as earlier items. **Partial M1 candidate:** a matrix-derived local Lorentz realisation inside a stated class of operators, but with the class and frame not derived, so I do not claim M1 is met; the gatekeeper decides. M3: none, nothing merged is false. M4, M5: none.

**Breakthrough: not claimed.** The central tree-level statement is a known result of HKK 2005, and I found no matrix-theory derivation that selects the class. What does carry weight strategically is that this route has a tree-level vacuum Einstein equation with full local Lorentz and diffeomorphisms, and that the merged class is one representation of the same algebra. The published authors' caution on this route, the absent sources and the torsion double zeros all count against reading it as more.

## Status-label recommendation

Current critical-path list from ch17 Section done and Appendix H: A, B, C, D1, E, F, G-derived, N, all OPEN and PROGRAMME-CONDITIONAL. Affected labels: none. No change recommended.

## Author decision needed

None. The route keeps spacetime emergent and changes no label.

## Remaining open step

To close D1, ranked by what I expect to matter most for the infrared and full-GR derivations:

1. **Sources at the equation of motion:** matter that sources Ric beyond Kaluza-Klein fields. Candidates: fermion Psi with non-diagonal kernels (the first moment of the Wigner function is a stress tensor, by my own estimate, unverified); one-loop induced stress (HKK suggest quantum corrections, not derived); KK reduction on the K of Problems C and F, including whether it fixes moduli.
2. **Torsion sector:** norm, masses and the double zeros, on a curved background and with a regulated action or finite-rank pairing; whether fermions or a mass term lift the double zeros. This is where N enters.
3. **Selection:** whether the matrix integral prefers this class, against CP^{1,2} and the diagonal distribution of 2509.06646; regular versus minimal representation of so(4,1); what fixes A. This is where the frame and non-degeneracy would have to come from.
4. **Regulated trace and bilocal modes** of End(H), against 2509.06646 (unitarity, |k=0> constraints).
5. **Non-equivariant and higher-order fluctuations; supersymmetry** (HKK state that the restriction destroys global supersymmetry).
6. **Map to Presentation B:** whether u, e, omega reproduce Phi, Xi and B of Chapter 10, and whether the F operators follow in this class.
7. **Rotating K**, independent, remains the best next package on C.

## Special instructions for the gatekeeper

- **Test the emergence reading first.** The action has no metric and the class is algebraic. Whether the reading of L^2(Z) as operators in the matrix model meets the directive is the most important judgement here.
- **Do not let this read as closure of D1.** "Derived" in Chapter 17 requires the frame and non-degeneracy, which the class assumes.
- **Re-check independently:**
  - the three-part formula, including the Phi term and its sign;
  - sign R_ab^{ae} = -Ric_b^e;
  - Ric_ab = -mu^2 eta_ab;
  - the chain counts, in particular whether the transversal lines suffice and whether E3 or the Hermiticity shift changes anything;
  - the claim that the two simple zeros are the TT modes;
  - the bracket formula and y_nu lambda^{nu sigma} = -s m xi^sigma;
  - the selection-rule proof at J >= 2, including smooth y dependence of zeta.
- **The literature was read through a fetch tool.** Confirm HKK Eqs. and the 2509.06646 sentences from source if a claim depends on the wording. The insert's reading of 2509.06646 is the sentence most exposed to this.
- **"Consistent truncation" statement:** only as closure of first-order operators under commutators and invariance of the background. No statement on stability.
- **Numerical labels:** the fibre projection and the M fit are numerical; everything labelled exact uses rational arithmetic at the sampled points, which is a check of an algebraic identity at those points, with the hand derivation carrying the proof.
- **What the insert must not assert:** any norm or ghost statement; a Cassini or Newtonian result; G_eff; identification with the emergent metric; that the class is selected.
- **Ordinal:** the ledger says next integration is 48, with the 5th-item full scan due at 50, so no full scan is forced by count. The package changes no definition, assumption, scope or status passage.
