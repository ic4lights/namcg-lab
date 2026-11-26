# Proposal 051-finite-rank-pairing-torsion-modes, round 1

## Result

Target taken: 050 avenue 1, the torsion sector as the gate for N, computed from the pairing the matrix action already has rather than from an expectation.

Established, at quadratic order about the flat point of the first-order equivariant class (and, for the labels, the de Sitter group case):

1. **The spectrum sits on commuting matrices.** At flat space X_a is unitarily -p~_a tensor 1 on L^2(R^4) tensor L^2(SO(3,1)). In Hilbert-Schmidt kernels the linearised operator is (E A)_b = Q.Q A_b - Q_b Q.A with real Q. On shell at Q != 0 the form eta^{ab} conj(A_a) A_b is positive definite on Q-perp/Q. In background gauge the operator is a multiplication operator, with no eigenvector and no Jordan block on Hilbert-Schmidt kernels. This also holds exactly for commuting N x N matrices.
2. **Exact field redefinition.** With h_b^c = f_b^c + y_g f_b^{gc}, w_b^{cd} = f_b^{cd}, the 40 linear equations of 050 are ten Maxwell equations: E2 = Mx[f^{de}], E1 + y_g E2^{ge} = -Mx[f^e]. Also 2 E3_b = d_c E1_b^c - eta_bg E2_c^{gc}, identically, which explains why E3 never changed a rank in 050. The labels are P_g and J_lambda, the right-invariant fields on ISO(3,1), which commute with X_a. With the order-zero field that is 11 Maxwell fields and 22 = 20 + 2 polarisations.
3. **What the double zeros are.** They are the nilpotent action of translations on the labels. The 050 statement stands at fixed eigenvalue of translations. The y-linear solutions are d/dt of the bounded family e^{ik.y} exp(t J_lambda), which solves the equation for all t.
4. **Sign on truncations.** On any finite-rank truncation the odd-time-index components h_i^0 and w_i^{0j}, with i transverse, have positive pairing, and h_i^mu proportional to q^mu has positive rather than zero pairing. This is a tension with Furuta et al. (expected negative, without an action) and with Ho-Kawai-Steinacker (time components of tensor fields negative; "no clear correspondence"). It is not a contradiction and does not settle which form governs effective fields. The caution is reported as standing for the covariant reading.
5. **The double zero under cutoff.** A 2 x 2 block on cut-off probes is Hermitian on a positive Gram matrix. Its eigenvalues are +-kappa + O(sigma^2) with kappa -> 0 as the fibre width sigma -> 0, so there are two simple poles with residues of one sign. A Jordan block appears only in the basis in which one probe has diverging norm.

What this does **not** do: it does not remove the torsion modes. They stay massless at this order, each protected by its gauge parameter, so the gate moves from "negative norm and double zeros" to "excess massless positive modes". It says nothing about curved backgrounds, where a generic Lorentzian operator has complex pairs (numerical, not solutions). It is not a statement on the graviton two-point function of Problem N. D, F, N stay OPEN and PROGRAMME-CONDITIONAL.

## Target and status

**Why this target.**
- 050 avenue 1 was asked for as "a norm from a regulated action or finite-rank pairing". The sign of the torsion modes was an expectation (Furuta footnote at hep-th/0611093 L677-682 of the source: "although we have not started from any field theory action"). It can be computed from Equation eq:Smatrix itself with no new input. That turns a supplied or expected input into a computed one, in a bounded class, and a computation that could have gone against the route was possible: had the pairing been indefinite on Q-perp/Q, the SO(3,1) fibre would have paid for local rotations.
- 050 avenue 3 (selection) has no comparably sharp computation available now; this package supplies one small fact for it, that the flat point has the spectrum of a commuting background with multiplicity.
- 049's rotating K and non-derivative branch are independent and remain queued. D1 and N had the sharpest open question from the last accepted review.
- SME scout `reports/sme-scout-20261101-after45.md` lists D1 as R3 (done by 050); no later scout exists. Its other routes are on F/N/C in the 044-049 class, already followed in 047-049.

**Exact labels, read this round.**
- Problem D (appH L569-570): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- Problem F (appH L1405-1406): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN ..."
- Problem N (appH L2954-2955): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

**Original targets (ch17 L712-717, L727-731).** D1: SO(3,1) gauge symmetry derived from the matrix algebra and condensate, with omega, A_mu, B and ghost operators and field content; locked frame and non-degeneracy derived. N: Assumption ass:EFT-a2 discharged, no propagating Ostrogradsky ghost for p < L_UV in the derived graviton two-point function, for alpha and G_eff computed in F.

**Dependencies.** N needs F. Both need a derived class. This package supplies neither.

**Classification.** PROGRAMME-CONDITIONAL. Nothing is DERIVED for a critical-path target. No discrepancy found between ch17 and appH on the passages read.

## Source reading

**Digest + targeted reads. No full scan.** `make_digest.py --check` printed DIGEST CURRENT at start and end; `dirty-chapters: yes` from the uncommitted 049 and 050 integrations, so I read working-tree files. No full scan is due: this would be ordinal 49 (the ledger gives "Next integration is 49; the 5th-item full scan is due at 50"), and the proposal changes no definition, assumption, scope or status passage.

**Manuscript read in full:** appH L1346-1385 (the 050 block, in full), appH L2950-3084 (Problem N), ch17 L50-109 (labels), L325-354 (D), L495-516 (N), L690-749 (criterion), ch03 L95-184 (Definition, Equation eq:Smatrix). Labels verified by script.

**Project records read:** 050 review-r2 and sme-consult-r1 (in full), 049 review-r4 (in full), the end of reports/ledger.md (entries 047-050), 050 s3 and s7 (conventions, in part), MILESTONE.md (triggers), SME scout after45 (headings only). Unreadable files: none.

**Literature read directly from arXiv TeX sources (line numbers of those files):**
| Source | Read | Used for |
|---|---|---|
| Ho-Kawai-Steinacker, 2509.06646v2 | L130-160, L240-262, L312-345, L630-1049, L1320-1350 | bilocal positivity (L667-689), quenched equivalence (L312-345), a_i^0 negative (L723-724), zero-norm c_i^+ (L943), trace divergences (L945-982), "no clear correspondence" (L1329-1335) |
| Furuta et al., hep-th/0611093 | L670-690, L1525-1535, L1735-1760, L1815-1856, L2028-2060, L2135-2150 | negative-norm reading with its footnote, physical components, group-manifold passages |
| Hanada, hep-th/0606163 | L875-890, L1625-1690 | commuting right action on a bundle that is a Lie group; E_prin(R^n) = ISO(n); uniform p_(a), quenched reduced model |
| Sakai, 1709.02588 | L720-735, L1095-1108 | linear system; metricity remarks |
| Steinacker, 2609.08955 | L549, L566, L1081, L1244-1252, L1270-1292 | Hilbert-Schmidt inner product and no-ghost statement on covariant quantum spacetime |
| Steinacker, 1910.00839 | L293-297, L1250-1262 (with grep) | no-ghost theorem; "excessive dof and the associated ghost issues" about the HKK route |
| Hehl, 1204.3672 | L615-625, L758-765, L1240-1246, grep for Kibble | translational and Lorentz field strengths |
| Kibble 1961 | Crossref record only, not read | cited through Hehl's statement "the first to gauge the Poincare group" |

**Citation-list and search work.**
- INSPIRE `refersto:recid` lists read by title: 2509.06646 (17 citers), hep-th/0611093 (27 citers). HKK and 0602210 lists from the SME's saved JSON, filtered by title.
- WebSearch (extended) on the negative-norm and double-pole question: nothing on double poles in this class, consistent with the SME's 050 result.
- The arXiv abstract API returned empty for my batched queries, so I did **not** read abstracts of 2604.25052, 2605.13294, 2605.10720, 2605.13972. They are citers of HKS, unread and not independently checked. Also unread: Sakai's thesis, Kawai PTPS 171, Sakai 1905.10067 beyond a grep.
- A failed search is not evidence of absence. **No novelty is claimed anywhere in this proposal.**

**Prior statements found, attributed in the insert or here:**
- Bilocal positivity for commuting backgrounds: HKS, planar sector with quenched diagonal elements. Item 1 above is the tree-level fibre version, and its fibre-less content is theirs.
- Spectrum of the flat bundle: Hanada 2006 (Euclidean Spin(n)).
- Right action and ISO(n): Hanada 2006. Furuta also has commuting left and right pairs (L2141).
- Hilbert-Schmidt pairing and no ghosts: Steinacker (different background; his statement depends on the covariant structure). Steinacker also attributes ghost issues to the HKK route; that caution is kept.
- Yang-Mills form with extra indices: Furuta L1815-1820 ("Yang-Mills theory with extra indices mu, c and d"). The triangularity is theirs and Sakai's. The combination E1 + y E2 and the identity for E3 I did not find in what I read.
- Torsion and curvature as translational and Lorentz field strengths: Poincare gauge theory, Kibble and Hehl. The linear form T = F + y F is the familiar structure of that theory; I did not locate a specific equation in the passages read and cite only the general statement.

## Research and reasoning

### 1. Setup and hypotheses

Flat point: e = delta, omega = 0, A = 0, so X_a = i u_a^b d_b on H = L^2(R^4 x SO(3,1), d^4y dHaar). Action: Equation eq:Smatrix with C = 0, no matter. Quadratic order. No gauge-fixing is assumed in the on-shell statements.

### 2. Commuting form (exact)

With p_b the eigenvalue of -i d_b, X_a = -u_a^b p_b. Since det u = 1, (p,u) -> (p~ = up, u) has unit Jacobian at fixed u, and (W f)(p~,u) = f(u^{-1}p~,u) is unitary. So X_a is unitarily -p~_a tensor 1.

Second variation, by hand. With F = 0 at the background, the first order of [X_a+A_a, X_b+A_b] is D_ab = [X_a,A_b] - [X_b,A_a]. Then Tr D^{ab} D_ab = 2 Tr [X_a,A_b][X^a,A^b] - 2 Tr [X_a,A_b][X^b,A^a] = -2 eta^{ab} Tr(A_a (E A)_b), using Tr([X,B]C) = -Tr(B[X,C]) and [X_a,X_b] = 0, where (E A)_b = [X^a,[X_a,A_b]] - [X_b,[X^a,A_a]]. So S_2 = +(1/(2 g^2)) eta^{ab} Tr(A_a (E A)_b). On a kernel, ad X_a is multiplication by Q_a(m,m') = X_a(m) - X_a(m'). Checked numerically at finite N (s4 part f).

On shell:
- Q.Q != 0: E A = 0 gives A_b = Q_b (Q.A)/Q.Q, which is the gauge direction delta A_b = Q_b Lambda.
- Q.Q = 0, Q != 0: E A = 0 gives Q_b (Q.A) = 0, so Q.A = 0. Real and imaginary parts lie in Q-perp, on which eta is positive semi-definite with kernel Q. So eta^{ab} conj(A_a) A_b is positive definite on Q-perp/Q.
- Q = 0: E = 0; these are the moduli of the commuting set, with an indefinite form.

The sign statement is about signature. The overall sign of S_2 relative to matter is not addressed: with eq:Smatrix and (-,+,+,+) a mode with spatial index has S_2 = +(1/2g^2) Int d_a A d^a A, the opposite of the usual sign for weight e^{iS}. That is a common sign. It does not bear on a relative ghost. I record it for the gatekeeper; it is not used.

In background gauge E is multiplication by Q.Q, a self-adjoint operator on Hilbert-Schmidt kernels, so a probe O has spectral measure rho(s) = Int |O|^2 delta(Q.Q - s), positive.

### 3. Labels (exact)

Commutant. X_a = i u_a^b d_b. Let V = -u_a^c lam_c^b d/du_a^b - y_g lam^{gc} d_c. Then [V, D_a] = V(u_a^b) d_b - D_a(-y_g lam^{gc}) d_c = -u_a^c lam_c^b d_b + u_a^b lam_b^c d_c = 0. Fibre part: (1/2) lam^{cd} u^r_c u^s_d S_rs acts on u as -u_a^c lam_c^b (s1 part G). Flow: F(y,u) -> F(Lambda y, u Lambda^{-1}) up to convention; unit Jacobian on y and right invariance of Haar make exp(t J) unitary. P_g = -i d_g commutes with X_a since X_a has no y dependence.

Ad-compatibility: E_b is a composition of ad X_a and ad [X_a,X_b]. If C commutes with X_a it commutes with [X_a,X_b], so ad of either acts on (1/2){f,C} as (1/2){ad f, C}. So E_b[(1/2){f,C}] = (1/2){E_b[f],C}, with any bilinear term linear and unaffected.

Redefinition. With T_ab^c = d_a h_b^c - d_b h_a^c + w_b^c_a - w_a^c_b:
d_a(y_g f_b^{gc}) = eta_ag f_b^{gc} + y_g d_a f_b^{gc}, and w_b^c_a = f_b^{cf} eta_fa = -f_b^{fc} eta_fa, so the explicit terms cancel: T_ab^c = F_ab^c + y_g F_ab^{gc}, R_ab^{cd} = F_ab^{cd}.

Then E1_b^e = -d^a T_ab^e + R_ab^{ae} = -d^a F_ab^e - F_gb^{ge} - y_g d^a F_ab^{ge} + F_ab^{ae}, where the middle terms cancel. So E1_b^e + y_g E2_b^{ge} = -Mx[f^e]_b. And E2_b^{de} = d^a R_ab^{de} = Mx[f^{de}]_b.

E3. 2E3_b = box T_bc^c - d_b d^a T_ac^c. Take the F part: Bianchi gives box F_bc = d_b Mx_c - d_c Mx_b, so box F_bc^c - d_b d^a F_ac^c = -d_c Mx_b^c. For the y term, box(y_g F_bc^{gc}) = 2 d_g F_bc^{gc} + y_g box F_bc^{gc}, and d^a d_b(y_g F_ac^{gc}) = eta_bg d^a F_ac^{gc} + d_b F_gc^{gc} + y_g d_b d^a F_ac^{gc}. The Bianchi identity on F_bc^{gc} gives 2 d_g F_bc^{gc} = d_b F_gc^{gc}, so these cancel, leaving -y_g d_c MJ_b^{gc} - eta_bg MJ_c^{gc}. Comparing with d_c E1_b^c (the y derivative term contains the antisymmetric trace, which vanishes) gives 2 E3_b = d_c E1_b^c - eta_bg E2_c^{gc}. Symbolic check for arbitrary functions: s1 part C.

So every (h,w) has this form: the map (f_P, f_J) -> (h,w) is invertible by (y-dependent) triangularity, so the identity is one for all fields, and E3 is implied by E1, E2. That matches the 050 observation (rank unchanged with or without E3) and explains it.

Chains. On e^{iq.y} with the 050 form, the h and w coefficients are constant, so the y term has to be absent. That restricted ansatz sees [[q^2,C],[0,q^2]] with C = lam -> q.lam. Rank of C at null q is 3 per polarisation (s1 part F; matches the SME's and gatekeeper's rank 6). In the commutant basis the same solutions are e^{iq.y} J_lambda. The operator ad P_g acts on them as q_g + nilpotent, since [P_g, J_lambda] = -lam_g^c P_c. So the Jordan block is that of the adjoint of iso(3,1), and it belongs to translations, not to E at fixed label. box and ad P_g commute; in the plane-wave basis ad P is diagonal and box has the chain, in the label basis box is diagonal and ad P has the chain. On Hilbert-Schmidt kernels both are self-adjoint and commuting, and neither has a chain. The first-order span is not a Hilbert-Schmidt subspace; it is a finite-dimensional, indecomposable, hence non-unitary, representation of the translations and Lorentz.

I do not claim the block is removed. A y-dependent redefinition is not translation invariant, and if y-translations are the physical momentum the mode is not an eigenstate. The content is: the y-linear solution is the first Taylor coefficient of a bounded unitary family that solves the equation for all t (exact, from the commutant).

### 4. Group case

For Z = G with X_a left-invariant, the right-invariant fields commute with X_a (s2 part D). A first-order field expands in them with coefficients contracting the dressed index with Ad(g^{-1}), so each coefficient has only the index a: a dressed one-form f_a. Take SO(4,1), X_a = i E_a4. By hand, with f_a order zero and [f,W] = -W(f): E_b[f] = -D^a(D_a f_b - D_b f_a) + [D_a,D_b] f^a. Exact check: [D_a,D_b] f^a = 3 f_b at an exact SO(4,1) point, and [D^a,[D_a,D_b]] = -3 D_b, the merged Ric = 3 eta (s2 part E). With the bilinear term the equation is E_b - 3 A_b, and the non-derivative terms cancel, leaving Maxwell. This cancellation is required by gauge invariance and is the only role of the bilinear term here. Labels: so(4,1) plus identity, 11 again. I did not analyse the spectrum of Maxwell on dS with this pairing beyond the equation.

For a background with no automorphisms of the parallelism, no nontrivial label exists except the identity. This is a limit of the method, not a claim.

### 5. Pairing on truncations

Let A_a(m,m') = u_a^r eps_r O(m,m'), u the fibre point of m, eps.eps = 1. Then eta^{ab} Int conj(A_a) A_b = Int |O|^2 pointwise, since u is Lorentz. The Hermitian part A + A^dagger has cross terms that vanish at k != 0, because the supports differ. So the pairing is |O|^2 whatever O is. With O a truncation of f(y) P_g, and f slowly varying on the scale of w: Int f^2 G_gh with G_gh = Int w p_g p_h. Boost invariance of w is impossible for a positive normalisable weight; a boost acts by congruence on G, so positivity holds in every frame.

The comparison to the literature is exactly about the label index g: the covariant reading contracts g with eta. No cut-off positive weight has G proportional to eta, since G_00 >= 0 and G_11 >= 0 while eta_00 and eta_11 have opposite signs. Finite-dimensional tensors of a non-compact group cannot carry a positive invariant form, and iso(3,1) has none; the Hermitian images of the generators live in an infinite-dimensional unitary representation, where the trace form is infinite. Removing the cutoff diverges, and the limit gives no finite form.

**What could reverse the sign:** a renormalisation that subtracts divergences, or an analytically continued regulator, is not a limit of positive truncations and can have a different sign. In a continuation p_0 -> i p_4 of a Euclidean regulator one gets G proportional to eta. Whether the effective low-energy field has that form is not decided here, and I expect it to be decided by loops, since HKS's graviton is a Nambu-Goldstone mode of the diagonal elements and those are not in the tree pairing at Q = 0. So I keep "tension", not "contradiction".

### 6. The double zero under a cutoff (exact on the sample)

Probes at null k, one-parameter subgroup. Operator is multiplication by Q2(p,t) = (k + (1-Lam_t)p)^2 on an orthogonal decomposition in (p,t): ad X_b acts on e^{ik.y} g(P) R(t) by -u_b^c(k_c + p_c - (Lam_t)_c^d p_d), with u Lorentz. Orthonormal probes: phi^2 = N(0,sigma^2/2), psi_1 = phi, psi_2 = sqrt2 sigma phi', O_1 = (v.P) sqrt(w) Psi[psi_1]/norm. Using int t phi phi' = -1/2, H_12 = -(sigma/sqrt2) sqrt(v G v)(1 + O(sigma^2)). s3 gives this exactly in sympy for a boost and a rotation (covering line; periodic images exponentially small at small sigma), with diagonal entries of order sigma^2 P^2, and a Monte Carlo agrees at sigma = 0.05 (H12 = -0.07072, exact leading -0.07071).

In the raw basis O_2raw = O_2/(sqrt2 sigma), the coupling tends to -P |v|/2 and the squared norm is 1/(2 sigma^2). That is how the Jordan block is recovered from a Hermitian matrix: the basis becomes singular. Bender-Mannheim discuss the equal-frequency Pais-Uhlenbeck case as a Jordan block; here, unlike the usual unequal-frequency form with opposite residues, the two poles have residues of one sign, since the Gram matrix is positive. Abstract-level only for those papers (taken from the SME's 050 report, not read by me), so it is not cited in the insert.

Limits: only one direction of the fibre is smeared; full smearing on G is not computed. The order sigma -> 0 before the momentum cutoff is removed is essential: at fixed sigma, a large P spreads the measure over a width of order sigma|k|P + sigma^2 P^2. So this does not establish a simple pole for an un-cut-off first-order probe, whose two-point function is not defined.

### 7. Beyond flat space

(M A)_b = box A_b - 2 [F_ab, A^a] with F_ab = [X_a,X_b]. By the Jacobi identity E_b[A] = (M A)_b - [X_b,[X^a,A_a]] on every background, so M is E_b in background gauge. M is J-symmetric for eta^{ab} Tr(A_a^dagger B_b) for every Hermitian X: Tr(A^{a dagger}[F_ab,B^b]) = Tr([A^{a dagger},F_ab] B^b) and ([F_ba,A^a])^dagger = [A^{a dagger},F_ab]. For a block (a,c) of M relative to HS, M^dagger_{ca} = 2 eta^{cc} ad F_ca while M_ca = 2 eta^{aa} ad F_ca, so HS-symmetry fails only in the time-space block; M is HS-symmetric when ad F_0i = 0. At a Jordan block the eigenvector is J-neutral: <v,v>_J = <(M-z)w,v>_J = <w,(M-z)v>_J = 0, z real.

s4 shows what can happen: random Hermitian 3 x 3, four matrices, not solutions, X_0 -> tau X_0: first complex pair at tau about 0.0089 at the seed used, with colliding eigenvectors tending to J-neutral. I do not take this as a statement about solutions. It is a warning: in a curved class background F_0i contains R S, so the positivity and absence of blocks are not automatic there.

### 8. Fork: the bounded statement and every hypothesis

Bounded statement: *the torsion modes stay massless at this order.* Hypotheses and relaxations:

| Hypothesis | Relaxation | Result here |
|---|---|---|
| Flat background | de Sitter group case | Same structure (labels so(4,1) plus identity), Maxwell. No mass |
| No bilinear term | Bilinear term on dS | Cancels against curvature, by gauge invariance. No mass |
| Order-zero background | Constant Theta_ab, A_a = Theta(u^{-1}y) type | F enters only the third bracket. First two brackets unchanged at linear order. No mass for h, w (exact, from the merged formula) |
| No extra matrices | K factor with fixed L | Singlets massless; non-singlets get the K mass, as a label with [L,.] != 0. Torsion singlets not lifted |
| Background torsion zero | Lie-algebra backgrounds, T != 0 | **Open.** F = f X is first order, so the third bracket is no longer order zero and the first two brackets gain terms. Avenue 1 below |
| Tree level | One loop | **Open.** Sakai 2017's result (SME 050 report) says massless at IIB content for T = 0 fields; independent torsion modes untreated. Avenue 2 |
| Commuting vacuum | Diagonal-element dynamics (HKS mass-gap assumption) | **Open.** Avenue 3 |
| First-order class | Higher orders in P | Same mechanism: the labels are all of the commutant; infinitely many massless labels at this order, as in HKS before their assumption |
| No fermions | Fermion fluctuations | Dirac operator gamma^a[X_a,.] has the same ad-compatibility, so fermion labels are free massless Dirac kernels (one line; not in the insert, not computed further) |

The gate therefore shifts. For the flat first-order class the obstruction at tree level is no longer negative norm and double zeros, but an excess of massless positive modes.

### 9. Comparison with the original targets

N asks for the graviton two-point function from the matrix path integral, for computed alpha, G_eff, with p < L_UV. This package computes neither. It gives a bounded input: at tree level, flat, the matrix integral's own pairing has no negative direction on shell at Q != 0, so an argument that the fibre class has Ostrogradsky ghosts cannot rest on the double zeros or odd-time-index signs at this level alone. It does not establish the converse. D1 is untouched: the class remains supplied.

## Claim classification

| Claim | Class |
|---|---|
| X_a unitarily -p~_a tensor 1 at flat point | established (spectrum for Spin(n) attributed to Hanada) |
| S_2 and E on kernels; on-shell positivity on Q-perp/Q; finite-N version | established identity (fibre-less planar statement attributed to HKS) |
| No eigenvector or Jordan block on HS kernels in background gauge | established, formal on the unbounded multiplication operator; domains untreated |
| Matrix measure flat in the HS metric at finite N | established |
| Commutant, E_b[(1/2){f,C}] = (1/2){E_b[f],C} | established identity |
| T = F + yF, E1 + yE2 = -Mx, E2 = Mx, 2E3 = dE1 - eta E2 | established identity, by hand and symbolic |
| Double zeros are the nilpotent action of translations on labels | established |
| e^{ik.y} exp(t J) solutions, unitary | established at formal level |
| dS labels and Maxwell | established by hand with exact point checks; spectrum not analysed |
| No mass at this order for the listed relaxations | conditional on hypotheses in Section 8 |
| Positive pairing on truncations; G never proportional to eta | established |
| Tension with Furuta and HKS | comparison of readings; not a contradiction; not settled |
| Which form governs the effective field | unresolved |
| Pencil form with kappa | exact on Gaussian w and one-parameter subgroup; leading formula for general w is an expansion; full-fibre smearing not computed |
| Krein symmetry, neutrality | established algebra |
| Complex pairs for random matrices | numerical, not solutions, seed-specific value |
| y-linear growth is not energy growth | not claimed; only "bounded operator family" is claimed |
| Selection, frame, non-degeneracy, B operator, masses, G_eff, graviton two-point | not treated, unresolved |

## Proposed changes

**File `chapters/appH-microscopic-proofs.tex`.** Insert the bytes of `appH_insert.tex` immediately before the unique line `\section{Problem E: signature}` + CRLF, that is, after the closing sentence of the 050 block ("Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL."). All existing text is kept; nothing is replaced. Anchor checked at byte level (count 1 with CRLF, 0 with bare LF) by s5.

The block is in the file, 12560 bytes LF, 12599 after conversion to CRLF, sha256 `13c124fa6bc0465f17a014d6e3694f8d78af909233c699093adbce3ecd2e69b2`, ASCII, no BOM. Fenced text is not repeated here to keep one source of truth; read `appH_insert.tex` as the proposed LaTeX. It closes with one status sentence and adds no labels.

Labels verified: ass:EFT-a2, ass:frame-lock, ass:local-lorentz, ass:lorentzian, ass:nondeg, ch:vierbein-emergence, eq:Smatrix, sec:status-N. Cites verified: FurutaHanadaKawaiKimura2007, Hanada2006, HoKawaiSteinacker2025, Steinacker2019NoGhost present; Hehl2017 and Kibble1961 new.

**File `bib/namcg.bib`.** Append the two entries of `new_bib_entries.bib` (convert to CRLF). Kibble 1961 verified at Crossref (title, journal, volume 2, pages 212-221, DOI 10.1063/1.1703702). Hehl verified at INSPIRE (Einstein Stud. 13, 145-169, 2017; DOI 10.1007/978-1-4939-3210-8_5; arXiv:1204.3672).

**Stale passages elsewhere:** none. Merged L1379 "No action is used here, so no sign of a norm follows here for these modes" concerns that paragraph and stays true; the new paragraph uses the pairing, not an action on the class. L1379's "double zero" stays true at fixed q, and the insert says so.

## Verification scripts

All in `proposals/051-finite-rank-pairing-torsion-modes/`, each with saved output `*.r1.out.txt`. Scripts do not rewrite the insert. Run with `PYTHONDONTWRITEBYTECODE=1`.

| Script | Checks | Result |
|---|---|---|
| `s1_label_identity.py` | A T = F + yF; B E2, E1 + yE2; C E3 identity (arbitrary functions, d = 4); D [V,D_a] = 0; E y-linear J modes solve E1, E2, E3 at null q; F counts 14 + 6 = 20, 22; G fibre part of J | all pass, exact |
| `s2_commutant_operator.py` | A box on e^{iqy} J and e^{iqy} R on a test function (c = -2); B Q.Q; C ad-compatibility, finite matrices (1e-14); D left and right fields; E dS: [D_a,D_b] f^a = 3 f_b, [D^a,[D_a,D_b]] = -3 D_b | all pass |
| `s3_cutoff_pencil.py` | exact H for boost and rotation; kappa; raw basis; seeded Monte Carlo; G | leading kappa ratio 1; MC agrees |
| `s4_krein_finite.py` | J-symmetry; commuting; ad F_0i = 0; generic complex pairs; neutrality at first collision; second variation against direct expansion (9e-6 at h = 1e-3, consistent with O(h^2)) | all pass; numerical |
| `s5_insert_mechanics.py` | ASCII, LF, anchor, labels, cites, one status sentence, no process words, no new labels | pass |
| `compile_check.py` | on a copy outside the repository: baseline 344 pages, with insert and bib 348 pages; exit codes [0,0,0,0]; 0 undefined references, citations, multiply defined labels; CRLF preserved; scratch removed | pass |

Symbolic and numeric output are checks; the arguments are in Sections 2-7. Runtime: s1 and s2 a few minutes each on this machine.

## Decisions Taken

1. **Target.** 050 avenue 1 over avenue 3 and the rotating K. Reason above. Rejected: selection now, for lack of a computation at comparable sharpness; 049 avenue 1, because it stays in a class where D1 is not addressed.
2. **Which pairing.** eta^{ab} Tr(A_a A_b) on finite-rank fluctuations, because it is the one the action and the flat measure supply. Rejected: a covariant regulator or heat kernel, because it is not positive and would insert the answer; I report instead what it would change (Section 5).
3. **Recording the tension.** As a tension, keeping the published caution as standing for the covariant reading, in line with the standing instruction. Rejected: presenting the result as refuting the negative-norm reading.
4. **Double zeros.** Keep the merged statement and add what it is. Rejected: saying it is an artefact or is removed, because at fixed translation eigenvalue it is exact and the redefinition is not translation invariant.
5. **Placement.** Problem D, after the 050 block, not Problem N, because the class is defined there and the status sentence names D, F, N. No new label; no repetition of a critical list.
6. **Scope of the insert.** Drop the fermion line and the Bender-Mannheim comparison from the insert. The first was not computed further and the second was not read by me.
7. **Emergence.** The class stays in the 050 surviving form: operators on one fixed separable Hilbert space, with Z and A as data of the class; the commuting form makes clear that at the flat point the X_a do not themselves select A. No fundamental metric or manifold is introduced. Assumption ass:lorentzian is retained: the (-,+,+,+) contraction of the matrix index is what makes Q-perp/Q positive only at null Q.

## Milestone assessment

Routine. M1 is not met: the class is supplied and this is quadratic order; nothing about N is derived from the matrix path integral. M2 is not met: the "stay massless" statement is a bounded statement with listed open relaxations, not a no-go ruling out a class of routes the manuscript keeps open. M3 is not met: the merged 050 text stands as scoped. M4, M5: none. I do not claim a breakthrough. If the gatekeeper finds this changes the direction materially (the gate moves from norm to excess massless modes), that is still not an M-trigger on the 044-050 standard.

## Status-label recommendation

Critical-path list per ch17 L700-732: A, B, C, D1, E, F, G-derived, N, consistent with appH. Affected labels: none. D, F, N unchanged. No label change proposed.

## Author decision needed

None.

## Remaining open step

For D1 and N, all of what the insert lists as untreated. Next avenues, ranked, each keeping spacetime emergent:

1. **Fluctuation spectrum at T != 0, the first background on which labels can get masses.** Lie-algebra backgrounds in the class (left-invariant with torsion; compare Furuta's group-manifold section), where F is first order. Compute E at fixed right-invariant label and see whether torsion labels gain non-derivative terms. Relaxes "background torsion zero". This is the direct continuation of the gate.
2. **One-loop two-point function of first-order probes with the cutoff of Section 5.** Compute how the label form changes, with IKKT content. Does a covariant form emerge, and with which sign for h_i^0? This decides the tension in the insert. Compare Sakai 2017's masslessness with independent torsion modes.
3. **Diagonal-element dynamics.** Which labels are Nambu-Goldstone in HKS's sense (SL(d) and Lorentz actions on the distribution); does the fibre multiplicity change the answer? This is where selection of the class would first be visible, and it connects to 050 avenue 3.
4. **Curved class backgrounds.** Spectrum of M about Ricci-flat pp-wave, with few automorphisms, to test whether complex pairs occur on solutions and whether J-neutral chains survive.
5. **Fully smeared fibre pencil, and a Plancherel treatment on L^2(SO(3,1)).** Replaces the one-parameter sample; 050 avenue 5.
6. **Full Hilbert-space Gupta-Bleuler construction per label**, with domains, to state a real norm rather than a pairing on kernels.

## Special instructions for the gatekeeper

**Must not be asserted:** that torsion modes are removed; that negative norm is absent for the effective field; that Furuta or HKS are wrong; that the double zeros are an artefact; that the class is selected; any N statement beyond quadratic order at flat space.

**Re-check first:**
- The hand derivation in Section 3 and the E3 identity.
- Whether the pointwise pairing in Section 5 is right with the u-dressing (u is the left fibre point in both factors of the Hermitian pairing; I argue the cross terms vanish at k != 0).
- That S_2's sign is immaterial as stated, and whether "This statement concerns the signature" is enough in the insert.
- Whether "not a choice of regulator at finite N" overreaches, since the flat class is infinite-dimensional. The sentence is limited to finite N.
- The pairing sentence "h_i^mu proportional to q^mu has positive and not zero norm": it needs w not on a hyperplane, and it compares against a fibre-less statement in HKS, whose c_i^+ is in their minimal model. I wrote "statements on tensor fields" for that reason.
- Whether the attribution of the Hilbert-Schmidt no-ghost result to `Steinacker2019NoGhost` is exact as "same kind of inner product". I read lines L293-297 and a grep, not the full proof. Its inner product is an SO(4,2)-invariant one on Mat(H); the claim is only about the kind.
- Kibble was not read; the citation rests on Hehl's description. Drop Kibble1961 if you prefer to cite only what was read.

**Known limits I would flag in my own work:** the pencil is one-parameter; dS was checked at one exact point plus the hand argument; the unread HKS citers listed under Source reading could contain any of this. No novelty is claimed.

**Process notes.**
- A heredoc double-backslash collapse broke an early s5 draft, as warned; the saved s5 uses `chr(92)` and was written with the Write tool, and the insert edits were made from a script written with the Write tool.
- One tool round issued several reads together at the start (digest, reviews, ledger counts) and two later rounds did the same (appH and ch17 ranges; WebSearch and a Bash abstract query), against the serial rule. Later calls were serial.
- Downloads went to scratchpad directories `lit051_2609` and `lit051_pgt`; sources were only read as text.
