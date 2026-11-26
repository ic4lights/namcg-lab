# Proposal 049-k-scale-dilaton-response, round 3

## Result

**G1-G9 are verified and applied verbatim. The insert has the bytes the review expected: 22769 bytes, sha256 b19b4c9890f65a15f33ec0fb21bc5af957ad2e56617335ec3e7f3ff7d47e43e3 (LF).** This round adds no new claim. Two wording observations on texts I applied unchanged are in "Verification of G1-G9", for the gatekeeper to rule on. Neither changes a conclusion.

The result of the package, as ruled in review-r2. In the frozen class at V = T, late time, static channel:

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

| Problem | appH label (verbatim, as re-read in review-r2) | Original target | Class here |
|---|---|---|---|
| C (L404-407) | "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope outcome only when its operator, coupling and phenomenological test are supplied; it does not by itself meet the matrix-derived criterion." | Scalar operator, coupling, Cassini comparison; Assumption gap-psi discharged | PROGRAMME-CONDITIONAL |
| F (L1366-1369) | "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." | A, B, C and sign/scheme of G_eff from specified operators | PROGRAMME-CONDITIONAL |
| N (L2858-2859) | "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL." | No propagating Ostrogradsky ghost for p < L_UV | PROGRAMME-CONDITIONAL |

I did not re-open these label lines this round; they are carried from review-r2, which re-read them. The critical-path set (A, B, C, D1, E, F, G-derived, N) is as the review recorded it, with no discrepancy against CLAUDE.md.

**Dependencies:** the 044-048 paragraphs (factorisation L2375; frozen closed forms L2442; Levi-Civita form and J_ab L2440; levels mu_J L2407; S1/S2 record L2482-2486); supplied IKKT content.

## Source reading

**Digest + targeted reads. Not a full scan.**

- **Digest state.** `make_digest.py --check` prints **DIGEST STALE (head changed)**. The digest head is be9268e and HEAD is 9cd61bf. `git diff --stat be9268e HEAD` shows one file, review-r2.md, so no chapter differs between the two commits. I did not regenerate the digest, since that writes outside my folder.
- **dirty-chapters: yes.** The only modified chapter is appH, +86 lines against HEAD. The task states this is solely the accepted 046-048 integrations awaiting the author's commit; I did not check that diff line by line. I read the working tree.
- **Scan rule, flagged.** CLAUDE.md item 3(d) literally asks for a full scan when the digest is stale or dirty. I did not do one. The task sets this round to verification and application of accepted replacements, with no new claim, and review-r2 ruled digest + targeted reads for the same package. The orchestrator or gatekeeper should confirm that this is acceptable.
- **Read in full:** review-r2.md, proposal-r2.md, appH_insert.tex (r2 bytes), s6, compile_check.py, s8 from L300 to its end, prior s6 and compile outputs.
- **Read in the working tree:** appH L2216-2220 (Casimirs, H_V with mu^2), L2370-2382 (factorisation; long lines cut at 1500 characters), L2407, L2413, L2422, L2440.
- **Not re-read:** ch17, the bibliography, the source papers. No ch17 claim changes.
- Unreadable files: none.

## Research and reasoning

No new mathematics. Sections A, B, E, F and G of proposal-r2.md stand as written, apart from the corrections below. Sections C and D are restated where the review changed them.

### Verification of G1-G9

Each text was checked before it was applied; s11 holds the scripted part. The review's own algebra was not assumed.

| Item | Check | Outcome |
|---|---|---|
| G1 | Fibre-constant modes number one, not F. Dropping the fibre flux gives F equal copies, each w(xi) = 15 xi^2 at xi = s vartheta/2, so (15/4) vartheta^2 s^2 per mode (r2 section A) | correct |
| G2 | From L2216 and L2440: H_0 = -Box = C_31 - C_41, so Z = H_i - H_0 = C_tot - C_31 - C_Sigma. On T_a = M^{a4}, real generators give C_31 = -3 and C_41 = -6 (so(4,1) adjoint; s11 C), reproducing H_0 T_a = 3 T_a (L2407). The singlet has Z = 0 + 3 + 3 = 6. The Hessian check gives H X_b = 3 Box X_b exactly, and its quadratic form agrees with second differences of the action | correct; see observation 2 |
| G3 | Derivation below, plus exact computation in the enveloping algebra (s11 A) and at complex labels (s11 B) | correct |
| G4 | Bracket = q(D)/D^3 with q = (15/4) vartheta^2 D^2 - vartheta c D + 2c^2, discriminant -29 vartheta^2 c^2 (s11 D) | conclusion correct; see observation 1 |
| G5 | Normalisation and both limits below | correct |
| G6 | Second-order hand estimate below | correct as an order statement |
| G7 | x = a/b at L2422 confirmed. The only other x in the insert is x_n in the vacuum part, a different symbol and not touched | correct |
| G8 | Antecedent of "This" was lost; the new sentence stands alone, with its own finite-list caveat | correct |
| G9 | -4x^2 - 6x + 15/2 = 0 gives x = (sqrt 39 - 3)/4 = 0.81125, so "0.81" as a strict bound was false on [0.81, 0.8112) | correct |

**Observation 1 (G4, applied verbatim).** At J = 0, c_J = 0, so the discriminant is 0, not negative. There q has a double root at D = 0, and the bracket is 15 vartheta^2/(4D) > 0 on the stated range. So "every summand positive" is true, and the stated reason is complete only for J >= 1. I do not regard this as an error in the claim, so I did not stop. If the gatekeeper wants the literal reason complete, the text would need something like "for J >= 1 (at J = 0 the bracket is 15 vartheta^2/4D)". **That change is not applied.**

**Observation 2 (G2, applied verbatim).** H_V T_a = 3 H_0 T_a holds for the mass-free operators, matching "without mass terms" at L2440. The form at L2218 carries mu^2 = -3, which would give H_V T_a = 6 T_a and H_0 T_a = 0 if the same mu^2 were added to both. Z is the difference, so Z = 6 is not affected, and "in the form of the preceding paragraphs" can be read as L2440. Whether the sentence needs "without mass terms" is left to the gatekeeper. **No change applied.**

### C. Fibre flux: exact identity (restated, with the review's correction)

**Correction of r2.** Section C of r2 wrote Z = 2A.sigma on (1/2,0). For Hermitian A it is **Z = -2A.sigma**, and on (0,1/2) **Z = -2B.sigma**. The eigenvalues 1 -+ Xi stated in r2 are right. Total spin j - 1/2 has Z = 1 + Xi, and total spin j + 1/2 has Z = 1 - Xi.

**Definitions.** H_i = H_0 + Z, Z = C^{tot,i}_31 - C_31 - C_{Sigma_i}, C_31 = (1/2) J_ab J^ab in real generators. Over C, A = (L + iN)/2 and B = (L - iN)/2 are commuting su(2), and C_31 = N^2 - L^2 = -2(A^2 + B^2).

**Derivation using only the relations (G3).** Let W = A.sigma. Then:

1. sigma_i sigma_j = delta_ij + i eps_ijk sigma_k together with A x A = iA gives W^2 = A^2 - W.
2. For Z = -2W: Z^2 = 2Z + 4A^2.
3. Hence **(Z - 1)^2 = 4A^2 + 1 = Xi^2** on a component where A^2 = j(j+1) is scalar.
4. The trace of Z over the spinor block is -2A_i tr sigma_i = 0, as an operator on the orbital space.
5. So e^{-sZ} = e^{-s}[cosh(s Xi) - (Z - 1) sinh(s Xi)/Xi], and its block trace is P(Xi) = e^{-s}[2 cosh(s Xi) + 2 sinh(s Xi)/Xi].

No dimension count enters, and no multiplicity (Xi +- 1)/Xi is used. The r2 phrase "eigenvalues on j +- 1/2 give per state" is therefore withdrawn as the argument for infinite-dimensional components, per F-G2. Unitarity and Hermiticity of A, B are not used; only the relations and the scalar Casimir are. This is the point on principal series, where A and B are not Hermitian.

**Vector.** Z_V = Z_A + Z_B with [Z_A, Z_B] = 0, so tr_V e^{-sZ} = P_+ P_- and tr_V - 2 tr_D + 4 = (P_+ - 2)(P_- - 2).

**Expansion.** P - 2 = s^2 (Xi^2 - 1)(1 - (2/3) s + ...), so the first term starts at s^4, as the merged text says.

**Principal series.** Xi_+- = +-m_L + i varsigma, so Xi_-^2 = conj(Xi_+^2). P is entire in Xi^2 with real coefficients, so the integrand is |P_+ - 2|^2 >= 0 on each component, exactly.

**Checks (s11).**
- Enveloping algebra, exact PBW normal ordering with no matrix for the orbital generators:
  - C_tot - C_orb - C_S = -2A.sigma; (Z-1)^2 = 4A^2 + 1; block trace of Z is 0;
  - block trace of Z^k equals (-1)^k k! [s^k] P for k <= 8;
  - tr_V Z_V^k equals the same for P_+ P_- for k <= 6;
  - C_31 = -2(A^2 + B^2) and the closure of A, B from the so(3,1) relations alone.
- Verma modules at complex j, including Xi = +-m_L + i varsigma, truncated with interior entries only: (Z-1)^2 - Xi^2 below 5e-13; partial trace of e^{-sZ} against P below 3e-16.
- A script is a check here, and the proof is the five steps above. The exact k-by-k results reach finite order only.

### D. Fibre flux: level form (scope corrected)

The moment formula, the by-parts identity f(z) = z^2 - z + 15/4, the commuting check and the exact Plancherel average stand as in r2 (s8, unchanged). Corrections:

- **Cross term (G6).** Second-order hand estimate from merged L2407: the singular values (2m/|y^0|)((y^4 q_0 J)^2 + (ell |q| m_L)^2)^{1/2} with a Gaussian q of variance of order 1/(s m^2) give a relative effect of order s J^2 at fixed vartheta. The first order vanishes by parity in q. This is the order of the retained -(4/15) s c_J/vartheta and of the s^2 c_J^2 term. So the coefficient of the middle term and the D in the denominators do not survive quantitatively. This is an order estimate, not a computation of the level form with the cross term.
- **Commutation.** The non-negativity is untouched, since the cross term is -Box minus parts that are functions of so(3,1) invariants at a fixed level, and Box commutes with J_ab (L2440). The integrand depends only on the labels.
- **Positivity of the bracket (G4).** Summands, not terms; the middle term of the bracket is negative. The range is M_A != 0 and D >> vartheta. See observation 1.

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

  The largest S on the grids is 3.99921, below 4. For mu >~ N^2 chi^2, S falls again (0.35 at mu = 1e7, N = 2048), but that lies outside equal weights, chi N >> n. So "for mu_J >> chi^2" is read in that regime, which the sentence is about.
- *Relative size.* Sum_J (2J+1) 4 c_J /(F (15/2) vartheta^2 N^2) = (4/15) n(n+2)/(vartheta^2 N^2) at the limit value 4. That gives 3.05e-5 at N = 1024, n = 10, vartheta = 1, against (n/N)^2 = 9.5e-5. "Relative order at most (n/N)^2" is correct as an order statement.

### Rulings of review-r2 adopted

- **R3, R4, R6, R7, R15, R17, R19, R20, E1-E5:** accepted, as ruled. R3 is amended by G1. E3 is amended by G2-G6.
- **R8:** accepted, with G7. **R18:** accepted, with G9.
- **F1-F7:** closed, with F6 needing G7 for the new x, which is now applied.
- **Y and m_L notation; "positive" in the level form:** acceptable as ruled, no change.
- **PRIOR-CLAIM-ERROR:** none. 044-048 stand; the merged "not computed" statements remain true.

### Hypotheses and obstruction classes (adopted from review-r2)

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

**Open avenues, ranked (adopted from review-r2; each keeps spacetime emergent).**

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

Restated with G3 and G6. Items changed from r2 are marked.

| Claim | Class |
|---|---|
| Tree form on psi Lambda_A; rigid in gamma at fixed K | established (Poisson limit, product) |
| l-loop exponent -l at fixed K; "order one only from chi" | power counting, not derived |
| Gamma_1 depends only on chi^2/lambda; homogeneous exponent 1/2 at V_t = 0 | established where the proper-time form converges (dY/dln chi neglected in the general form) |
| U_4, U_2 forms | established from the merged factorisation; conditional on it |
| Y at frozen symbol, **with the fibre flux dropped** (G1) | established; completeness at that order relies on merged L2440 |
| beta_K = 2L'/U_chichi = -2U_t'/U_chichi, sign rule | established for these forms (first order, V = T, late static, fibre-constant response) |
| Forms with Y; 10/13; x > 5/2; beta_K = 1 at x = 3/10 | established algebra given the law below |
| Large-N law -4x^2 - 6x + 15/2 and x_0 = (sqrt 39 - 3)/4 as its root (**exact root**, G9) | numerical at 60 digits, not proved in closed form; x_0 is exact as the root of that law |
| Z = C_tot - C_31 - C_Sigma, sign by H_V T_a = 3 H_0 T_a (**G2**) | established (mass-free form; relies on merged L2407, L2440) |
| **(Z - 1)^2 = Xi^2 and vanishing block trace, on each chiral block, in any representation with scalar Casimir (G3)** | established from the su(2) relations alone |
| Identity tr_V - 2 tr_D + 4 = (P_+ - 2)(P_- - 2) | established identity, new (background; relies on merged J_ab form; proved by the G3 route, not by the finite-dimensional checks) |
| Integrand >= 0 on each principal-series component, every fibre flux | established, new (exact) |
| Y >= 0 with fibre flux | conditional: positive multiplicity weight in the formal continuation; level form with cross term dropped |
| Level form of Y (**G4, G6**): leading in s, frozen, every summand positive on M_A != 0, D >> vartheta | conditional: holds only with the cross term dropped |
| **Cross term changes the weights at relative order s J^2; J-dependent terms do not survive quantitatively (G6)** | order estimate, not computed |
| **Leading Y and its sign unchanged by the fibre flux at equal weights, background (G6)** | conditional (hypotheses of the level form and the estimate above); numerics on S^2_N (0.998) with the cross term dropped |
| **Mixed term: 4(2J+1) c_J at level J for mu_J >> chi^2, less for smaller mu_J (G5)** | limits 4 and 8 mu/chi^2 by hand and numerical check; "less" numerical; cross term dropped |
| Uhat values, 4 ln N + 1.016, flat-stack signs with an s-limit | numerical, or established as in r1 |
| I[X_beta], g2, potentials, poles (given U_4 alone) | conditional on equal weights; exact within them |
| O4a, O4b, O5 | conditional on the stated classes |
| S1 point at x = 3/10 | tuned tree data supplied; not derived; one-loop not small against tree |
| Inputs retained | IKKT content, formal continuation, K, stabiliser, q_*^2 |

**Not established:** S1 or S2 for the K selected by the theory; level response; cross term; two-derivative fibre-flux part; second-order non-derivative terms at chi^2 <~ vartheta; mass of t; G_eff; any ghost statement; any Cassini bound on the emergent metric.

**Open:** C, F, N remain OPEN and PROGRAMME-CONDITIONAL.

## Proposed changes

**File `chapters/appH-microscopic-proofs.tex`.** One insertion, no replacement.

- **Anchor:** immediately before the unique line `\section{Problem G: HBEV}` (count 1 by s6), after the 048 closing sentence.
- **Kept:** everything.
- **Text:** `proposals/049-k-scale-dilaton-response/appH_insert.tex`, **22769 bytes, sha256 b19b4c9890f65a15f33ec0fb21bc5af957ad2e56617335ec3e7f3ff7d47e43e3**, ASCII, LF, no BOM. It was built by s10 from `appH_insert.r2.tex` (sha 92f8033b...) with G1-G9 only. This file is the `latex` block and is not duplicated here. The integrator restores CRLF.
- **Labels verified:** eq:Smatrix, ass:gap-psi, ass:lorentzian, ch:vierbein-emergence, once each. No new labels.
- **Cites verified:** Steinacker2023, Steinacker2026, Bertotti2003 in bib; MantaSteinacker2025b from the entry below.

**File `bib/namcg.bib` (integrator).** Unchanged from r1 and r2:

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

**Stale passages elsewhere:** none require a change. The review checked r2 section F against L2402, L2413, L2415, L2417, L2440, L2457, L2486 and found it accurate. G1-G9 do not touch those statements.

### Map of review-r2 to this round

| Finding | Addressed by | How |
|---|---|---|
| F-G1 (major) Z undefined, sign unrecorded | G2 | Applied verbatim; verified; observation 2 |
| F-G2 (major) finite-dimensional evidence for an infinite-dimensional claim | G3 | Applied verbatim; relations-only derivation in section C; s11 A, B |
| F-G3 (major) J-dependent terms same order as the cross term | G6 | Applied verbatim; hand order estimate in section D; claim table restated |
| F-G4 (minor) "each term positive" | G4 | Applied verbatim; observation 1 |
| F-G5 (minor) "4c_J per level" | G5 | Applied verbatim; both limits by hand and numerically |
| F-G6 (minor) fibre-constant modes number one | G1 | Applied verbatim |
| F-G7 (minor) x collides with L2422 | G7 | Applied verbatim |
| F-G8 (minor) "This" without antecedent | G8 | Applied verbatim |
| F-G9 (minor) rounded root in an inequality | G9 | Applied verbatim; also replaced in this record |
| Record slip "2A.sigma" | section C | Corrected to -2A.sigma, -2B.sigma |
| Record: claim table with G3, G6; G3 check; 8 mu/chi^2 check | Claim classification; s11 | Done |

No disagreement with any finding.

## Verification scripts

In `proposals/049-k-scale-dilaton-response/`. New outputs are `*.r3.out.txt`; no earlier output was overwritten. s1-s5, s7, s8 and s9 were not changed or re-run, since this round changes none of them and s8's sums are only re-derived independently in s11.

| Script | Checked | Result |
|---|---|---|
| s10_apply_r3.py | Parses G1-G9 as raw text from review-r2.md; checks source bytes; each old string once at its turn; result against the review's size and sha; refuses to write on any mismatch; re-runnable from `appH_insert.r2.tex` | All nine once, also once each in r2. 22769 bytes, sha256 b19b4c98..., **equal to the review's**. A second run reproduces the same bytes |
| s11_g3_g5_checks.py | (A) enveloping-algebra checks of G3 and the vector block; (B) Verma modules at complex labels; (C) sign of Z: Hessian by second differences, H X_b = 3 Box X_b, Casimirs on T_a; (D) G4 discriminant; (E) G5 normalisation and limits | (A) all exact, k <= 8 and k <= 6; (B) below 5e-13 and 3e-16; (C) residual 0.0, forms 4708.2954 and 4708.2968 (relative 3e-7 at e = 1e-3, consistent with the O(e^2) truncation of the second difference); (D) -29 c^2 vartheta^2; (E) as in section D |
| s6_insert_mechanics.py | ASCII, labels, cites, status count, process words | ASCII, CR 0, no BOM, 12 blocks, no new labels, one status sentence, anchor count 1, labels 1 each. Bib 1 each, except MantaSteinacker2025b 0 as expected until integration. "round " only from "background" (false positive) |
| compile_check.py | Build with and without insert plus bib, outside the repo | Exit [0,0,0,0] both; 333 and 339 pages; 0 undefined refs and citations; 0 multiply defined; scratch removed. Rendered pages not inspected |

Outputs: `s10_apply_r3.r3.out.txt`, `s11_g3_g5_checks.r3.out.txt`, `s6_insert_mechanics.r3.out.txt`, `compile_check.r3.out.txt`. `appH_insert.r2.tex` is the unchanged r2 insert.

`s10_apply_r3.r3.out.txt` is the first run, which includes the "archived" line. A later run omits that line and writes identical bytes.

## Decisions Taken

No RESEARCHER-DECISION flag in review-r2 (FLAGS: none). Routine choices:

1. **Apply G2 and G4 verbatim and report observations 1 and 2 rather than stop.** In both cases the statement is true and only the wording of a reason or a qualifier could be sharpened, so neither meets "G text wrong". The alternative of stopping the round would hold nine verified texts for a J = 0 remark. The alternative of editing silently is excluded by the task. The gatekeeper can rule on both.
2. **Check G3 in the enveloping algebra as well as on matrices.** That is what "any representation" needs from a script. Verma modules at complex labels were added as the closest finite-computation stand-in for non-unitary infinite-dimensional components.
3. **Keep the r2 insert as `appH_insert.r2.tex`,** matching `appH_insert.r1.tex`, so that s10 can be re-run and the diff reviewed.

Earlier decisions stand: option (a) carrying Y through; the exact Casimir route; no citation of 0911.5085 in the insert; O4b kept narrow. "Claim only the J-dependent leading part of W_J" (r2 decision 4) is narrowed by G6: those terms hold only with the cross term dropped.

## Milestone assessment

**Routine**, as ruled in review-r2. M2 not met: a bounded restriction on a coupling 048 kept as non-derived, narrower than r1, same standard as 044-048. M3 not met: nothing merged is false. M1, M4, M5: none. BREAKTHROUGH: no; the result is conditional, S1 is tuned, and the non-derivative sector is not computed. No SME consultation is needed.

## Status-label recommendation

Critical-path list as recorded in review-r2 from ch17 and appH: A, B, C, D1, E, F, G-derived, N. Affected labels: none.

## Author decision needed

None.

## Remaining open step

To close C in this class: the non-derivative sector of t on a stated K (q_*^2, V_00, V_01, what cancels the vacuum term, and the second-order terms at chi^2 <~ vartheta); beta_K for the K selected by the theory, with its actual tree data; composition dependence; the Cassini comparison on the emergent metric, with Assumption gap-psi discharged. F needs the operators without the equal-weight input and with K selected. N needs control of the extra root.

## Special instructions for the gatekeeper

**Verify:**
- bytes: 22769, sha256 b19b4c98... against your copy2;
- that only G1-G9 differ from r2 (`appH_insert.r2.tex` is the r2 file);
- section C's sign correction and the five-step derivation;
- s11 sections A, C and E.

**Rule on:**
- observation 1 (G4 at J = 0);
- observation 2 (G2, mass-free form against L2218);
- the source-reading point: rule 3(d) of CLAUDE.md, digest stale by one review-only commit and dirty by the integrations awaiting the commit, no full scan here.

Either wording change would alter the expected bytes, so it would be a new text from you or a further round.

**Must not be asserted:**
- that S1 is derived or selected by this class;
- a Cassini bound on the emergent metric;
- that compact K with Uhat < 0 do not exist;
- that the branch x < x_0 gives a long-range force (non-derivative terms are not computed);
- anything about the rotating K beyond the homogeneous relation;
- that published works are contradicted;
- the coefficients of the J-dependent terms of the level form beyond "cross term dropped".

The bib entry is unchanged. Nothing was committed.
