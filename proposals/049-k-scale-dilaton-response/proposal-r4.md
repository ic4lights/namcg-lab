# Proposal 049-k-scale-dilaton-response, round 4

## Result

**R1 is verified and applied verbatim, and nothing else in the insert changed. The insert has the bytes the review expected: 22821 bytes, sha256 eba2c8ed7f120413377176df1da08adf4cd5e4d57458b07561ee5fedbd6fa256 (LF, ASCII, no BOM).** This round adds no new claim. It updates the record only: G4 and the claim table now use the R1 reason, and the review's rulings on G2 and G5 are adopted.

The result of the package, as ruled in review-r2 and review-r3. In the frozen class at V = T, late time, static channel:

    beta_K = 2(4 U_4 + 2 U_2 + Y)/U_chichi = -2 U_t'/U_chichi

1. At a local minimum, beta_K has the sign opposite to the slope of the tree term.
2. "S1 and V = T are incompatible for Uhat >= 0" holds only where Y <= 4|U_4| + 2|U_2|. On S^2_N at large N that is chi^2 >= (sqrt 39 - 3) vartheta/4.
3. Y = (15F/64 pi^2) vartheta^2 sqrt|g| N_K at the frozen symbol with the fibre flux dropped.
4. **Exact on the background, with every fibre flux included:** tr_V - 2 tr_D + 4 = (P_+ - 2)(P_- - 2), and the integrand is |P_+ - 2|^2 >= 0 on each principal-series component.
5. **Scope of the level form (G6).** Its J-dependent terms hold only with the cross term dropped, because the cross term changes the weights at the same relative order s J^2. What carries over is the non-negativity on each component, the value at M_A^2 >> mu_n, and the order of the correction. So at equal weights the fibre flux does not change the **leading** value of Y or its sign on the background.
6. **S1 is neither excluded nor derived.** With Uhat > 0 it is reachable only as tuned supplied tree data at chi^2 < (sqrt 39 - 3) vartheta/4, where the one-loop term is not small against the tree term.
7. **Undeformed quartic alone on S^2_N.** There is no local minimum at weak coupling.

Nothing is DERIVED. C, F and N remain OPEN and PROGRAMME-CONDITIONAL.

## Target and status

| Problem | appH label (verbatim, as re-read in review-r3) | Original target | Class here |
|---|---|---|---|
| C (L404-407) | "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope outcome only when its operator, coupling and phenomenological test are supplied; it does not by itself meet the matrix-derived criterion." | Scalar operator, coupling, Cassini comparison; Assumption gap-psi discharged | PROGRAMME-CONDITIONAL |
| F (L1366-1369) | "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." | A, B, C and sign/scheme of G_eff from specified operators | PROGRAMME-CONDITIONAL |
| N (L2858-2859) | "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL." | No propagating Ostrogradsky ghost for p < L_UV | PROGRAMME-CONDITIONAL |

I did not re-open these label lines this round; they are carried from review-r3, which re-read them. The critical-path set (A, B, C, D1, E, F, G-derived, N) is carried from the reviews and CLAUDE.md, with no discrepancy.

**Dependencies:** the 044-048 paragraphs (factorisation L2375; frozen closed forms L2442; Levi-Civita form and J_ab L2440; levels mu_J L2407; S1/S2 record L2482-2486); supplied IKKT content.

## Source reading

**Digest + targeted reads. Not a full scan.**

- **Digest state.** `make_digest.py --check` prints **DIGEST CURRENT**. Digest head f1e7332, `dirty-chapters: no`. The author committed 046-048 in ecfdade, so the manuscript baseline is now committed text.
- **Scan rule.** Review-r3 ruled that this package changes no definition, assumption, scope or status passage, and this round changes one clause of the insert. None of the triggers in item 3 of the CLAUDE.md protocol applies to this round.
- **Read in full:** review-r3.md, proposal-r3.md, s10, s6, compile_check.py, prior s6 and compile outputs.
- **Read in part:** the insert around R1 (the level form of Y and the sentences before it); appH L2490 and the bytes before it; s11 L351-355 (section D, not re-run).
- **Not re-read:** ch17, the bibliography, the source papers, the label lines above. No ch17 claim changes.
- Unreadable files: none.

## Research and reasoning

No new mathematics. Sections A, B, E, F and G of proposal-r2.md stand as written, apart from the corrections recorded in r3 and below. Sections C and D are restated where the reviews changed them.

### Verification of R1

Replacement, from review-r3:

- old: `every summand positive since the bracket has negative discriminant in \(\mathcal D\), which reduces`
- new: `every summand positive (the bracket times \(\mathcal D^3\) is a positive definite quadratic form in \(\vartheta\mathcal D\) and \(c_J\)), which reduces`

Proof that the new reason is valid for every J in the sum.

1. **Bracket.** With D = M_A^2 + mu_J, the bracket 15 vartheta^2/(4D) - vartheta c_J/D^2 + 2 c_J^2/D^3 times D^3 equals (15/4) a^2 - a c + 2 c^2 at a = vartheta D, c = c_J. It is also the proper-time integral of the printed average: the integral over s from 0 to infinity of [(15/4) vartheta^2 - s vartheta c_J + s^2 c_J^2] e^{-sD} (s12, residual 0).
2. **Definiteness.** The matrix is [[15/4, -1/2], [-1/2, 2]], with leading minor 15/4 > 0 and determinant 15/2 - 1/4 = 29/4 > 0. Equivalently, (15/4) a^2 - a c + 2 c^2 = (15/4)(a - (2/15) c)^2 + (29/15) c^2. The form vanishes only at a = c = 0.
3. **Range.** The sum runs over M_A != 0 and D >> vartheta. So D > 0 and a = vartheta D > 0, with vartheta > 0 on the leaf. Hence the form is strictly positive for every c_J, and so is the bracket.
4. **J = 0.** Here c_J = 0, a > 0, and the form is (15/4) a^2 > 0. The bracket is 15 vartheta^2/(4D). The new reason covers this case with no separate clause. The old reason did not, because the discriminant vanishes at c = 0.

R1 therefore closes F-H1. The cross-term scope of the level form (G6) is unchanged: the positivity is of the printed bracket, which holds with the cross term dropped.

### Record of G1-G9 (updated)

| Item | Check | Outcome |
|---|---|---|
| G1 | Fibre-constant modes number one, not F. Dropping the fibre flux gives F equal copies, each w(xi) = 15 xi^2 at xi = s vartheta/2, so (15/4) vartheta^2 s^2 per mode (r2 section A) | correct |
| G2 | From L2216 and L2440: H_0 = -Box = C_31 - C_41, so Z = H_i - H_0 = C_tot - C_31 - C_Sigma. On T_a = M^{a4}, real generators give C_31 = -3 and C_41 = -6 (so(4,1) adjoint; s11 C), reproducing H_0 T_a = 3 T_a (L2407). The singlet has Z = 0 + 3 + 3 = 6. The Hessian check gives H X_b = 3 Box X_b exactly, and its quadratic form agrees with second differences of the action | correct; review ruling below |
| G3 | Derivation below, plus exact computation in the enveloping algebra (s11 A) and at complex labels (s11 B) | correct |
| G4 | Bracket = q(D)/D^3 with q = (15/4) vartheta^2 D^2 - vartheta c D + 2c^2, a positive definite form in vartheta D and c (s11 D, s12) | correct with R1 |
| G5 | Normalisation and both limits below | correct; review ruling below |
| G6 | Second-order hand estimate below | correct as an order statement |
| G7 | x = a/b at L2422 confirmed. The only other x in the insert is x_n in the vacuum part, a different symbol and not touched | correct |
| G8 | Antecedent of "This" was lost; the new sentence stands alone, with its own finite-list caveat | correct |
| G9 | -4x^2 - 6x + 15/2 = 0 gives x = (sqrt 39 - 3)/4 = 0.81125, so "0.81" as a strict bound was false on [0.81, 0.8112) | correct |

**Observation 1 (G4), resolved by R1.** The r3 reason used the discriminant, which is -29 vartheta^2 c_J^2 and vanishes at J = 0. Review-r3 ruled that reason literally false for those summands, as F-H1. It also noted that a discriminant belongs to the numerator polynomial, not to the rational bracket. The insert now gives the positive-definiteness reason, valid for every J.

**Ruling on G2, adopted (review-r3 (b)): no byte change.** The sentence is literally true as printed in its context. It sets H_i = H_0 + Z with Z = C_31^tot - C_31 - C_Sigma, which has no mu^2. "The form of the preceding paragraphs" is L2440, "without mass terms", with H_i = C_31^tot - C_41 - C_Sigma, and the class at L2371 is H_0 + Sigma.F. On T_a, C_G = 0, C_41 = -6 and C_Sigma = -3 give 9 = 3 H_0 T_a with H_0 T_a = 3 T_a. The reading in which mu^2 is added to both operators is not the manuscript's H_0 here. My r3 observation raising it is withdrawn. Z = 6 holds in every reading.

**Ruling on G5, adopted (review-r3, limit 4): no qualifier needed.** "S -> 4" needs N^2 chi^2 >> mu_J as well as mu_J >> chi^2. But mu_J <= n(n+2), so chi N >> n supplies it for every J <= n. The same sentence of the insert names that condition, and the block holds equal weights. The cutoff correction is in effect of the order (n/chi N)^2 already stated there. The review's figures for this (S = 1.00 at mu = N^2 chi^2 and 0.033 at 10 N^2 chi^2 for N = 2048; S = 3.9935, 3.9099, 3.8880 at J = n with chi N/n = 102, 10.2, 8.6; the maximum 3.99887 near mu = 1170 at N = 4096) are the review's and were not re-run here. "Less for smaller mu_J" and "at most (n/N)^2" stand as the review ruled them.

### C. Fibre flux: exact identity (unchanged from r3)

**Correction of r2.** Section C of r2 wrote Z = 2A.sigma on (1/2,0). For Hermitian A it is **Z = -2A.sigma**, and on (0,1/2) **Z = -2B.sigma**. The eigenvalues 1 -+ Xi stated in r2 are right. Total spin j - 1/2 has Z = 1 + Xi, and total spin j + 1/2 has Z = 1 - Xi.

**Definitions.** H_i = H_0 + Z, Z = C^{tot,i}_31 - C_31 - C_{Sigma_i}, C_31 = (1/2) J_ab J^ab in real generators. Over C, A = (L + iN)/2 and B = (L - iN)/2 are commuting su(2), and C_31 = N^2 - L^2 = -2(A^2 + B^2).

**Derivation using only the relations (G3).** Let W = A.sigma. Then:

1. sigma_i sigma_j = delta_ij + i eps_ijk sigma_k together with A x A = iA gives W^2 = A^2 - W.
2. For Z = -2W: Z^2 = 2Z + 4A^2.
3. Hence **(Z - 1)^2 = 4A^2 + 1 = Xi^2** on a component where A^2 = j(j+1) is scalar.
4. The trace of Z over the spinor block is -2A_i tr sigma_i = 0, as an operator on the orbital space.
5. So e^{-sZ} = e^{-s}[cosh(s Xi) - (Z - 1) sinh(s Xi)/Xi], and its block trace is P(Xi) = e^{-s}[2 cosh(s Xi) + 2 sinh(s Xi)/Xi].

No dimension count enters, and no multiplicity (Xi +- 1)/Xi is used. Unitarity and Hermiticity of A, B are not used; only the relations and the scalar Casimir are. This is the point on principal series, where A and B are not Hermitian.

**Vector.** Z_V = Z_A + Z_B with [Z_A, Z_B] = 0, so tr_V e^{-sZ} = P_+ P_- and tr_V - 2 tr_D + 4 = (P_+ - 2)(P_- - 2).

**Expansion.** P - 2 = s^2 (Xi^2 - 1)(1 - (2/3) s + ...), so the first term starts at s^4, as the merged text says.

**Principal series.** Xi_+- = +-m_L + i varsigma, so Xi_-^2 = conj(Xi_+^2). P is entire in Xi^2 with real coefficients, so the integrand is |P_+ - 2|^2 >= 0 on each component, exactly.

**Checks (s11, r3 outputs).**
- Enveloping algebra, exact PBW normal ordering with no matrix for the orbital generators:
  - C_tot - C_orb - C_S = -2A.sigma; (Z-1)^2 = 4A^2 + 1; block trace of Z is 0;
  - block trace of Z^k equals (-1)^k k! [s^k] P for k <= 8;
  - tr_V Z_V^k equals the same for P_+ P_- for k <= 6;
  - C_31 = -2(A^2 + B^2) and the closure of A, B from the so(3,1) relations alone.
- Verma modules at complex j, including Xi = +-m_L + i varsigma, truncated with interior entries only: (Z-1)^2 - Xi^2 below 5e-13; partial trace of e^{-sZ} against P below 3e-16.
- A script is a check here, and the proof is the five steps above. The exact k-by-k results reach finite order only.

### D. Fibre flux: level form (positivity updated by R1)

The moment formula, the by-parts identity f(z) = z^2 - z + 15/4, the commuting check and the exact Plancherel average stand as in r2 (s8, unchanged). Corrections:

- **Cross term (G6).** Second-order hand estimate from merged L2407: the singular values (2m/|y^0|)((y^4 q_0 J)^2 + (ell |q| m_L)^2)^{1/2} with a Gaussian q of variance of order 1/(s m^2) give a relative effect of order s J^2 at fixed vartheta. The first order vanishes by parity in q. This is the order of the retained -(4/15) s c_J/vartheta and of the s^2 c_J^2 term. So the coefficient of the middle term and the D in the denominators do not survive quantitatively. This is an order estimate, not a computation of the level form with the cross term.
- **Commutation.** The non-negativity is untouched, since the cross term is -Box minus parts that are functions of so(3,1) invariants at a fixed level, and Box commutes with J_ab (L2440). The integrand depends only on the labels.
- **Positivity of the bracket (G4, R1).** Summands, not terms; the middle term of the bracket is negative. On the range M_A != 0, D >> vartheta, the bracket times D^3 is a positive definite quadratic form in vartheta D and c_J, with determinant 29/4, including at J = 0.

**Mixed term (G5).**
- *Normalisation (s11 E).* The Dirac index part is tr_D - 4 = s^2 (Xi_+^2 + Xi_-^2 - 2) = -2 s^2 C_31 = -2 s^2 (N^2 - c_J), so sigma^M gains +2 s^2 c_J. With the mixed term -(1/4) sigma^M tau^K of merged L2375, -(1/2) int ds/s s^-2 under d/dln chi gives -c_J c_i b_i/(b_i + mu_J) in units 1/32 pi^2. A level carries (2J+1) in the units of the display.
- *Limit chi^2 >> mu.* The c_i sum to zero at each l. Then S(mu) = -Sum c_i b_i/(b_i + mu) -> mu Sum c_i/b_i, and the summand is 8(1/l^2 - 1/(l+1)^2) exactly, so **S -> 8(1 - 1/N^2) mu/chi^2**.
- *Limit mu >> chi^2, with N^2 chi^2 >> mu.* With u = l + 1/2 and G(u) = u^2 chi^2/(u^2 chi^2 + mu), the Taylor expansion of the three towers gives summand 2uG'' - 2G', and the integral over u gives -4[G]_0^inf. So **S -> 4**.
- *Numerics, chi^2 = 1 (s11 E).*

| mu/chi^2 | N | S | comparison |
|---|---|---|---|
| 1e-4 | 2048 | 0.00079989 | S/(8 mu/chi^2) = 0.99986 |
| 0.1 | 2048 | 0.6997 | S/(8 mu/chi^2) = 0.8746 |
| 1 | 2048 | 3.0468 | S/4 = 0.7617 |
| 10 | 2048 | 3.9304 | S/4 = 0.9826 |
| 1000 | 8192 | 3.99921 | S/4 = 0.99980 |

  The largest S on these grids is 3.99921, below 4. For mu >~ N^2 chi^2, S falls again (0.35 at mu = 1e7, N = 2048). That lies outside the range mu_J <= n(n+2) with chi N >> n, as the ruling above records.
- *Relative size.* Sum_J (2J+1) 4 c_J /(F (15/2) vartheta^2 N^2) = (4/15) n(n+2)/(vartheta^2 N^2) at the limit value 4. That gives 3.05e-5 at N = 1024, n = 10, vartheta = 1, against (n/N)^2 = 9.5e-5. "Relative order at most (n/N)^2" is correct as an order statement.

### Rulings of the reviews adopted

- **Review-r2.** R3, R4, R6, R7, R15, R17, R19, R20, E1-E5: accepted, as ruled. R3 is amended by G1. E3 is amended by G2-G6. R8: accepted, with G7. R18: accepted, with G9. F1-F7: closed.
- **Review-r3.** F-G1 to F-G9 closed, with F-G4's text corrected by R1. F-H1 closed by R1. The rulings on G2 and G5 are adopted above. The r3 digest and source-reading point is ruled acceptable.
- **Y and m_L notation; "positive" in the level form:** acceptable as ruled, no change.
- **PRIOR-CLAIM-ERROR:** none. 044-048 stand; the merged "not computed" statements remain true.

### Hypotheses and obstruction classes (adopted from the reviews)

**Common hypotheses:** Poisson limit; one loop; IKKT content supplied; product background without mixed flux; K single-scale with fixed Lambda; matter mass from chi alone; frozen symbol; formal continuation; first-order response; q.y = 0; V = T; late time; q below m_chi; local minimum with tree kinetic term; equal weights.

None of these classes closes a direction outside its hypotheses.

- **O4a, beta_K <= 0.** Common hypotheses plus U_4 <= 0, U_2 < 0, Y <= 4|U_4| + 2|U_2|, with Y's fibre flux at the background and cross term dropped. On S^2_N at large N with chi N >> n: chi^2 >= (sqrt 39 - 3) vartheta/4. Relaxing Y, the sign of Uhat, or the tree slope escapes it.
- **O4b, no minimum at weak coupling.** V_t = abar chi^4 alone on S^2_N at large N; a minimum needs 10/13 < |eps| < 1, x > 5/2, beta_K < -1. Any cubic or mass term removes it.
- **O5, ratio 1 at large tau.** Needs light t and beta_K = 1, at V = T, equal weights, late static, first order.

**What each explored relaxation gave.**

| Hypothesis | Relaxation | Explored | What it gave |
|---|---|---|---|
| First term dropped | keep it, fibre-constant | yes | Y; sign rule; branch chi^2 < (sqrt 39 - 3) vartheta/4 |
| Fibre flux in Y | all levels, background | yes | non-negative integrand exactly; leading Y unchanged at equal weights; J-dependent terms only with the cross term dropped |
| Tree stabiliser | none, cubic, mass | yes | exact forms; S1 attained with Uhat > 0, tuned |
| Sign of Uhat | Uhat < 0 | partly | S1 reachable, q_b^2 < 0; flat stacks only with an s-limit |
| Compact K, Uhat < 0 | scan | weak | scan uninformative; no non-existence claim |
| Light t, q below m_chi, V = T, equal weights | as r1 | partly | statements unchanged |
| Cross term | keep it | order estimate only | relative order s J^2; open (avenue 4) |
| Response of the fibre levels | first variation at J >= 1 | no | open (avenue 4) |
| Non-derivative terms at chi^2 <~ vartheta | second order | no | open (avenue 1) |
| Rotating K | fluctuation operator | no | open (avenue 2) |

**Open avenues, ranked (adopted from review-r3; each keeps spacetime emergent).**

1. Non-derivative sector of t on the branch x < x_0: second-order terms of U_2 and the first term, using the factorised (P_+ - 2)(P_- - 2); tadpole; q_*^2 with -U_chi,phi^2/2U_chichi; V_00, V_01. This decides whether the branch gives a long-range force.
2. Fluctuation operator about the rotating K, static channel, uniform omega (hand estimate of r1 still unverified).
3. Actual cubic coefficient for a K selected by the theory: whether anything fixes beta_K = 1; control of one-loop against tree where the tree quartic is of the order of Y; higher loops.
4. Two-derivative fibre-flux part (L2415) and the response of fibre levels, using the same so(3,1) decomposition, with the cross term kept. It is an invariant function on each component, which may make this tractable.
5. Compact K with Uhat < 0 and no negative mode, or a proof of absence (no non-existence claimed).
6. Level-dependent and external-harmonic weights; fibre Laplacian.
7. Loop kinetic and W_R mixing of chi; non-singlet moduli; composition dependence.
8. D1, overdue and independent; a reasonable next package if avenue 1 stalls.

### Literature

Nothing new this round and nothing re-fetched.
- David, Gaberdiel, Gopakumar, arXiv:0911.5085 is a check only and is not cited in the insert. Review-r2 confirmed its (5.10), (5.12), (5.13) for transverse helicity s; the extension to |m_L| < J is the standard induced-representation statement.
- Camporesi-Higuchi were read by neither of us, and no claim rests on them directly.
- 2303.08012, 2509.24753, 2601.08031 and Bertotti2003 are carried from earlier rounds, not re-fetched this round.

## Claim classification

Restated as in r3. The G4 line is updated by R1; the G5 line records the ruling. No claim is new.

| Claim | Class |
|---|---|
| Tree form on psi Lambda_A; rigid in gamma at fixed K | established (Poisson limit, product) |
| l-loop exponent -l at fixed K; "order one only from chi" | power counting, not derived |
| Gamma_1 depends only on chi^2/lambda; homogeneous exponent 1/2 at V_t = 0 | established where the proper-time form converges (dY/dln chi neglected in the general form) |
| U_4, U_2 forms | established from the merged factorisation; conditional on it |
| Y at frozen symbol, with the fibre flux dropped (G1) | established; completeness at that order relies on merged L2440 |
| beta_K = 2L'/U_chichi = -2U_t'/U_chichi, sign rule | established for these forms (first order, V = T, late static, fibre-constant response) |
| Forms with Y; 10/13; x > 5/2; beta_K = 1 at x = 3/10 | established algebra given the law below |
| Large-N law -4x^2 - 6x + 15/2 and x_0 = (sqrt 39 - 3)/4 as its root (exact root, G9) | numerical at 60 digits, not proved in closed form; x_0 is exact as the root of that law |
| Z = C_tot - C_31 - C_Sigma, sign by H_V T_a = 3 H_0 T_a (G2, as ruled: mass-free form of L2440) | established (relies on merged L2407, L2440) |
| (Z - 1)^2 = Xi^2 and vanishing block trace, on each chiral block, in any representation with scalar Casimir (G3) | established from the su(2) relations alone |
| Identity tr_V - 2 tr_D + 4 = (P_+ - 2)(P_- - 2) | established identity, new (background; relies on merged J_ab form; proved by the G3 route, not by the finite-dimensional checks) |
| Integrand >= 0 on each principal-series component, every fibre flux | established, new (exact) |
| Y >= 0 with fibre flux | conditional: positive multiplicity weight in the formal continuation; level form with cross term dropped |
| **Level form of Y (G4, G6, R1):** leading in s, frozen, every summand positive on M_A != 0, D >> vartheta. Bracket times D^3 is a positive definite quadratic form in vartheta D and c_J (determinant 29/4), including J = 0 | conditional: holds only with the cross term dropped. The positivity of the printed bracket is established algebra |
| Cross term changes the weights at relative order s J^2; J-dependent terms do not survive quantitatively (G6) | order estimate, not computed |
| Leading Y and its sign unchanged by the fibre flux at equal weights, background (G6) | conditional (hypotheses of the level form and the estimate above); numerics on S^2_N (0.998) with the cross term dropped |
| Mixed term: 4(2J+1) c_J at level J for mu_J >> chi^2, with chi N >> n supplying N^2 chi^2 >> mu_J; less for smaller mu_J (G5) | limits 4 and 8 mu/chi^2 by hand and numerical check; "less" numerical; cross term dropped |
| Uhat values, 4 ln N + 1.016, flat-stack signs with an s-limit | numerical, or established as in r1 |
| I[X_beta], g2, potentials, poles (given U_4 alone) | conditional on equal weights; exact within them |
| O4a, O4b, O5 | conditional on the stated classes |
| S1 point at x = 3/10 | tuned tree data supplied; not derived; one-loop not small against tree |
| Inputs retained | IKKT content, formal continuation, K, stabiliser, q_*^2 |

**Not established:** S1 or S2 for the K selected by the theory; level response; cross term; two-derivative fibre-flux part; second-order non-derivative terms at chi^2 <~ vartheta; mass of t; G_eff; any ghost statement; any Cassini bound on the emergent metric.

**Open:** C, F, N remain OPEN and PROGRAMME-CONDITIONAL.

## Proposed changes

**File `chapters/appH-microscopic-proofs.tex`.** One insertion, no replacement.

- **Anchor:** immediately before the line `\section{Problem G: HBEV}`, at L2490 of the committed baseline. Substring count 1 (s6), and one match across `chapters/`. The bytes are `\section{Problem G: HBEV}` + CRLF, preceded by the 048 closing sentence "...Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL." and a blank line.
- **Kept:** everything.
- **Text:** `proposals/049-k-scale-dilaton-response/appH_insert.tex`, **22821 bytes, sha256 eba2c8ed7f120413377176df1da08adf4cd5e4d57458b07561ee5fedbd6fa256**, ASCII, LF, no BOM. It was built by s12 from `appH_insert.r3.tex` (sha b19b4c98...) with R1 only. This file is the `latex` block and is not duplicated here. The integrator restores CRLF.
- **Labels verified:** eq:Smatrix, ass:gap-psi, ass:lorentzian, ch:vierbein-emergence, once each. No new labels.
- **Cites verified:** Steinacker2023, Steinacker2026, Bertotti2003 in bib; MantaSteinacker2025b from the entry below.

**File `bib/namcg.bib` (integrator).** Unchanged, kept in `new_bib_entry.bib`:

```bibtex
@misc{MantaSteinacker2025b,
  author  = {Manta, Alessandro and Steinacker, Harold C.},
  title   = {Dynamical Covariant Quantum Spacetime with Fuzzy Extra Dimensions
             in the {IKKT} Model},
  year    = {2025},
  eprint  = {2509.24753},
  archivePrefix = {arXiv}
}
```

**Stale passages elsewhere:** none require a change. The review checked r2 section F against L2402, L2413, L2415, L2417, L2440, L2457, L2486 and found it accurate. R1 does not touch those statements.

### Map of review-r3 to this round

| Item | Addressed by | How |
|---|---|---|
| F-H1 (minor), reason false at J = 0 | R1 | Verified (s12 part 1 and the proof above); applied verbatim by s12; no other byte changed |
| Record: observation 1 and the G4 line | G1-G9 record, claim table | Updated |
| Record: "not applied" remarks | this record | Dropped |
| Ruling (b) on G2 | G2 ruling above | Adopted; my r3 observation withdrawn; no byte change |
| Ruling on G5, limit 4 | G5 ruling above, section D | Adopted; no qualifier; no byte change |

No disagreement with any finding.

## Verification scripts

In `proposals/049-k-scale-dilaton-response/`. New outputs are `*.r4*.out.txt`; no earlier output was overwritten. s1-s5, s7, s8, s9 and s11 were not changed or re-run, since this round changes none of their content.

| Script | Checked | Result |
|---|---|---|
| s12_apply_r4.py | Part 1: R1's content by sympy (matrix, minors, completed square, bracket times D^3, proper-time integral, J = 0). Part 2: parses R1 and the stated size and sha as raw text from review-r3.md; checks source bytes; old string exactly once; result against the expected size and sha; refuses to write on any mismatch; re-runnable from `appH_insert.r3.tex` | Determinant 29/4; residuals 0. Old string once. 22821 bytes, sha256 eba2c8ed..., **equal to the review's** |
| s6_insert_mechanics.py | ASCII, labels, cites, status count, process words, anchor | ASCII, CR 0, no BOM, 12 blocks, no new labels, one status sentence, anchor count 1, labels 1 each. Bib 1 each, except MantaSteinacker2025b 0 as expected until integration. "round " only from "background" (false positive) |
| compile_check.py | Build with and without insert plus bib, outside the repo, against the committed baseline | Exit [0,0,0,0] both; 333 and 339 pages; 0 undefined refs and citations; 0 multiply defined; scratch removed. Rendered pages not inspected |

Outputs: `s12_apply_r4.r4.out.txt`, `s12_apply_r4.r4.rerun.out.txt`, `s6_insert_mechanics.r4.out.txt`, `compile_check.r4.out.txt`. `appH_insert.r3.tex` is the unchanged r3 insert.

**Diff.** A character-level comparison of `appH_insert.r3.tex` and `appH_insert.tex` shows differences only inside the R1 clause. This was run on the first application; the restoration described below reproduced the same sha256.

**Incident to record.** After the first s12 run I ran s10_apply_r3.py by mistake on the finished folder. s10 writes r3 bytes, so it reset `appH_insert.tex` to 22769 bytes, sha b19b4c98... I detected this by hashing and re-ran s12, which applied R1 from the archive (`s12_apply_r4.r4.rerun.out.txt`). The final file is 22821 bytes, sha eba2c8ed... The r2 and r3 archives still hash to 92f8033b... and b19b4c98... I regenerated `s6_insert_mechanics.r4.out.txt` after the restoration, and compile_check ran after it too, with the same sha confirmed afterwards. The earlier statement in s10's docstring, that re-running reproduces the same bytes, now holds only for the r3 stage. **Run s10 only on a copy.** s12 restores the final bytes if it is run by accident.

**Anchor grep.** An anchored shell grep for the section line returned 0 in one command, while s6, a byte-level read and a repository search each found one occurrence at the start of L2490. I did not diagnose that grep, and I rely on the byte-level result.

## Decisions Taken

No RESEARCHER-DECISION flag in review-r3 (FLAGS: none). Routine choices:

1. **Apply R1 as printed.** I checked it first and found it true for every J, so there was no reason to stop.
2. **Keep the r3 insert as `appH_insert.r3.tex`,** matching the r1 and r2 archives, so that s12 can be re-run and the diff reviewed.
3. **Attribute the review's G5 numerics to the review** rather than re-running them, since this round makes no new claim.

Earlier decisions stand: option (a) carrying Y through; the exact Casimir route; no citation of 0911.5085 in the insert; O4b kept narrow. "Claim only the J-dependent leading part of W_J" (r2 decision 4) remains narrowed by G6: those terms hold only with the cross term dropped.

## Milestone assessment

**Routine**, as ruled in review-r3. M2 not met: a bounded restriction on a coupling 048 kept as non-derived, the same standard as 044-048. M3 not met: nothing merged is false. M1, M4, M5: none. BREAKTHROUGH: no; the result is conditional, S1 is tuned, and the non-derivative sector is not computed. No SME consultation is needed.

## Status-label recommendation

Critical-path list as recorded in the reviews and CLAUDE.md: A, B, C, D1, E, F, G-derived, N. Affected labels: none.

## Author decision needed

None.

## Remaining open step

To close C in this class: the non-derivative sector of t on a stated K (q_*^2, V_00, V_01, what cancels the vacuum term, and the second-order terms at chi^2 <~ vartheta); beta_K for the K selected by the theory, with its actual tree data; composition dependence; the Cassini comparison on the emergent metric, with Assumption gap-psi discharged. F needs the operators without the equal-weight input and with K selected. N needs control of the extra root.

## Special instructions for the gatekeeper

**Verify:**
- bytes: 22821, sha256 eba2c8ed... (the review's copy3);
- that only R1 differs from r3 (`appH_insert.r3.tex` is the r3 file);
- the anchor against the committed baseline (ecfdade or later), now that the digest is current and `dirty-chapters: no`;
- that the G4 and G5 lines of this record match your rulings.

**Script hazard:** s10 overwrites `appH_insert.tex` with r3 bytes. Run it only on a copy (see "Incident to record").

**Must not be asserted:**
- that S1 is derived or selected by this class;
- a Cassini bound on the emergent metric;
- that compact K with Uhat < 0 do not exist;
- that the branch x < x_0 gives a long-range force (non-derivative terms are not computed);
- anything about the rotating K beyond the homogeneous relation;
- that published works are contradicted;
- the coefficients of the J-dependent terms of the level form beyond "cross term dropped".

The bib entry is unchanged. Nothing was committed.
