# Proposal 049-k-scale-dilaton-response, round 2

## Result

**F1 is correct, and the headline of r1 is withdrawn.** The potential of chi must include the first term s_0^K(v^M - 2 sigma^M) of the merged factorisation. With it, in the frozen class at V = T, late time and static channel:

    beta_K = 2(4 U_4 + 2 U_2 + Y)/U_chichi = -2 U_t'/U_chichi

So at a local minimum beta_K has the sign opposite to the slope of the tree term. "S1 and V = T are incompatible for Uhat >= 0" holds only where Y <= 4|U_4| + 2|U_2|. On S^2_N at large N this is chi^2 >= 0.811 vartheta.

1. **Y and the sharper form verified independently,** in exact or 60-digit arithmetic (s7): Y = (15F/64 pi^2) vartheta^2 sqrt|g| N_K; x_0 = (sqrt 39 - 3)/4; the bound 10/13; beta_K = 1 at x = 3/10 with Uhat > 0.
2. **Fibre flux computed (new mathematics; s8; rank-1 avenue of review-r1).**
   - Exactly on the background, per state of an irreducible so(3,1) component: tr_V - 2 tr_D + 4 = (P_+ - 2)(P_- - 2).
   - On unitary principal-series components the two factors are complex conjugates, so the first-term integrand is >= 0 with every fibre flux included.
   - At level J the leading form is s^2[(15/4) vartheta^2 - s vartheta c_J + s^2 c_J^2], c_J = J(J+1), positive.
   - It sums to a level form of Y that reduces to the value above at relative order (n/chi N)^2 with a logarithm. That is the equal-weight condition.
   - **Consequence:** at equal weights the fibre flux changes neither Y nor its sign on the background, so the chi^2 < 0.81 vartheta branch with beta_K > 0 and Uhat > 0 survives this check.
3. **What stays out of reach.** Y's fibre-flux part is at the background only. Not computed: the response of the fibre levels to hbar, the base-fibre cross term, the second-order non-derivative terms at chi^2 <~ vartheta, higher loops.
4. **S1 is neither excluded nor derived here.** It is a condition: a tree term of negative slope with a value fixed by supplied tree data. At the example point the tree quartic is of the order of Y, so the one-loop term is not small against the tree term.
5. **Weak coupling on the undeformed quartic.** There is no local minimum at weak coupling on S^2_N for V_t = abar chi^4 alone: a minimum needs 10/13 < |eps| < 1, with x > 5/2 and beta_K < -1. The m_chi formula and the window of r1 are corrected or deleted accordingly.

Parts of r1 that stand are in the claim table. Nothing is DERIVED. C, F and N remain OPEN and PROGRAMME-CONDITIONAL.

## Target and status

| Problem | appH label (verbatim, re-read) | Original target | Class here |
|---|---|---|---|
| C (L404-407) | "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope outcome only when its operator, coupling and phenomenological test are supplied; it does not by itself meet the matrix-derived criterion." | Scalar operator, coupling, Cassini comparison; Assumption gap-psi discharged | PROGRAMME-CONDITIONAL |
| F (L1366-1369) | "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." | A, B, C and sign/scheme of G_eff from specified operators | PROGRAMME-CONDITIONAL |
| N (L2858-2859) | "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL." | No propagating Ostrogradsky ghost for p < L_UV | PROGRAMME-CONDITIONAL |

Labels are carried from r1 and review-r1, which re-read them; this round did not edit or re-open those lines. The critical-path set (A, B, C, D1, E, F, G-derived, N) is unchanged.

**Dependencies:** the 044-048 paragraphs (factorisation L2375; frozen closed forms L2442; Levi-Civita form and J_ab L2440; levels mu_J L2407; S1/S2 record L2482-2486); supplied IKKT content.

## Source reading

**Digest + targeted reads. Not a full scan.**

- `make_digest.py --check` printed **DIGEST STALE (head changed)**. The digest head is 6727f2b and HEAD is 67e748a, which is the commit of review-r1 only. `git status` shows `chapters/appH-microscopic-proofs.tex` modified as stated in the task (`dirty-chapters: yes`). I did not regenerate the digest, since that would write outside my folder. I read working-tree files, and the orchestrator may want to refresh it.
- Read in full: review-r1.md, proposal-r1.md, appH_insert.r1.tex, repl_old.txt, firstterm.py and firstterm2.py as data; appH L2368-2417, L2419-2457, L2459-2490; s4, klib, s6, compile_check.
- Not re-read this round: ch17, the bibliography, the three source papers. r1 and review-r1 read them, and no ch17 claim changes.
- Literature read this round: David, Gaberdiel, Gopakumar, arXiv:0911.5085, Eqs. (5.12)-(5.13), from pdftotext of the fetched PDF (see section G).
- This round changes no definition, assumption, scope statement or status passage: it adds one conditional paragraph and one bib entry, so no full scan is required on that ground. Unreadable files: none.

## Research and reasoning

### A. Verification of Y (F1)

**Gaussian form.** In the rest frame of y, N_i = y^0 k_i, and <k_i k_j> = delta_ij/(2 s m^2), so b = s N has variance xi = s vartheta/2 per component. The Dirac eigenvalues are exp(+-i|b|), and the vector eigenvalues are exp(+-2i|b|), 1, 1.

Using <cos(c|b|)> = (1 - c^2 xi) exp(-c^2 xi/2) (s7 A, symbolic), this reproduces the merged closed forms. So

    w(xi) = tr_V - 2 tr_D + 4 = <(2 cos|b| - 2)^2> = 15 xi^2 - (35/2) xi^3 + ... >= 0

**Per K-mode.** dU/dln chi in units a = F sqrt|g|/32 pi^2 is 2 a_A I(a_A), with the exact closed form

    I(a) = 6 a ln a + 2(a+th) ln(a+th) - 8(a+th/4) ln(a+th/4) + 4 th ln(a+th) - 4 th ln(a+th/4)

Here 2aI -> (15/2) vartheta^2 - (35/8) vartheta^3/a. It was checked against quadrature to 15 digits (s7 B). Hence Y = (15/2) vartheta^2 N_K a. The review's value is confirmed.

**Completeness at this order.** Merged L2440 states that the first term's order s^2 coefficient has no term linear or quadratic in the curvature. I rely on that passage and did not re-derive it.

**On S^2_N (s7 C, 60 digits, N up to 4096):**
- Y/(7.5 vartheta^2(N^2-1)) -> 1 (0.9999982 at N = 4096, x = 0.3);
- the full frozen mixed term against 2U_2 -> 1 (above 0.9999 at N >= 256, x >= 0.1);
- L'/(N^2 vartheta^2) -> -4x^2 - 6x + 15/2 (5.3399867 against 5.34).

Spectra were checked against brute force at N = 4. dY/dln chi over Y at x = 0.3 is 6e-3, 5.5e-4, 4.5e-5 at N = 64, 256, 1024, which justifies neglecting it in the forms.

### B. Sharper form

T̄^{ab mu} y_mu = 0 identically (s7 G). So delta g_{mu nu} proportional to y_mu y_nu leaves every Gaussian moment of Z(k) unchanged, and at late time (hbar lapse-only) the fibre-constant loop density at fixed T̄ is sqrt|g| times a function of chi.

Then U = U_t(chi) + e^{-2 phi} L(chi), and stationarity gives beta_K = 2L'/U_chichi = -2U_t'/U_chichi. An independent root solve of the stationarity condition in phi gives dln chi/dphi = 1.0 (s7 F).

**Forms with Y (s7 D, symbolic):**
- quartic alone: -1/(1 + eps - Y/4 Utilde);
- quartic + cubic: 2 L'/(4 Utilde + 4 U_4 - 2 U_2 - 3Y);
- quartic + mass: L'/(4 Utilde + 4 U_4 - Y).

Each has dY/dln chi set to zero. The homogeneous exponent is (8U_4 + 2U_2 + Y'/2)/U_chichi, and it is 1/2 for V_t = 0 at any Y.

**Large-N law:** x_0 = (sqrt 39 - 3)/4 = 0.8112495 (s7 E).

**Quartic alone.** A x^2 - 6x + 15/2 = 0, with A = 4(1/|eps| - 1). The discriminant 36 - 30A gives |eps| >= 10/13.
- U_chichi = 2x(2Ax - 6) > 0 only on the larger root, and U_chichi = 0 at the double root.
- For |eps| >= 1 there is one positive root, a maximum.

**A minimum therefore requires 10/13 < |eps| < 1, with x > 5/2** (strict, a slight sharpening of R8). There beta_K < -1: at A = 1, x = 4.22, beta_K = -8.62.

**Counterexample (s7 F, exact rationals), units a N^2 vartheta^2, x = 3/10:**
- L' = 267/50, L'' = -126/25, U_chichi = 10.68, beta_K = 1 exactly.
- Cubic route: quartic 1587/200 = 7.935, cubic -309/25 = -12.36, |eps| = 0.01134.
- Mass route: quartic 33/10, mass -927/100, |eps| = 0.02727.

All agree with the review. With exact finite-N sums the tree data shift by under 0.6% at N = 64.

**Sign of the approach to zero.** Where the tree stabiliser dominates, beta_K -> 0 from above when the tree slope is negative. This is the natural regime of a Myers-type cubic at x < 0.81, and it was not in the review's R7. I added it.

### C. Fibre flux: exact identity (new)

Merged L2440: on the background, F_ab acts as J_ab, which commutes with Box, and H_i = C^{tot,i}_{31} - C_{41} - C_{Sigma_i}. So Z_Sigma = C_tot - C_orb - C_Sigma with C = (1/2) J_ab J^ab in real generators (C = -3 on the vector, s8 A).

**Sign.** This is a real point. On orbital = vector the singlet has Z = +6, which matches H_V T_a = 3 H_0 T_a = 9 T_a, an identity of the double commutator with H_0 T_a = 3 T_a. The same convention reproduces the closed vector spectra of S^2_N at l = 1, 2, 3 (s8 A). With the opposite sign there would be a growing factor e^{+s}; there is none.

**Identity.** With so(3,1) = su(2)_+ + su(2)_- over C and Xi_+- = 2 j_+- + 1, Z on the Dirac spinor is 2A.sigma on (1/2, 0) and 2B.sigma on (0, 1/2), with signs fixed as above. On the vector it is the sum of the two, and the two commute. Eigenvalues on j +- 1/2 give per state

    P(Xi) = e^{-s}[2 cosh(s Xi) + 2 sinh(s Xi)/Xi]
    tr_D = P_+ + P_-,   tr_V = P_+ P_-,   tr_V - 2 tr_D + 4 = (P_+ - 2)(P_- - 2)

This is confirmed with explicit vector matrices and explicit gamma matrices at six finite-dimensional labels, to 1e-11 or better (s8 A). P - 2 = s^2(Xi^2 - 1)(1 - (2/3)s + ...), so the first term starts at s^4, as the merged text says.

**Positivity.** On unitary principal series Xi_+- = +-m_L + i varsigma, so Xi_-^2 = conj(Xi_+^2). P depends on Xi^2 only, so P_- = conj(P_+) and the integrand is |P_+ - 2|^2 >= 0. This is exact, for every s and J.

Passing from this to Y >= 0 needs a non-negative weight of the multiplicity spaces in e^{s Box}. That holds for the spatial Gaussian; the direction along y is a spectator with the formal Gaussian of the class.

### D. Fibre flux: level form (new)

Fibre order J at y is a spin-J section over the slice: rotations about y act as spin J, and boosts act as N_i = y^0 k_i at the leading symbol. Harmonic analysis gives helicities |m_L| <= J, density varsigma^2 + m_L^2, and squared boost N^2 = varsigma^2 + 1 - m_L^2 + c_J. The last is the Casimir relation L^2 - N^2 = m_L^2 - varsigma^2 - 1 with L^2 = c_J. Literature check in section G.

With H_0 = N^2/vartheta + mu_J (merged L2407, cross term dropped) and t = s/vartheta, the leading form of the integrand for small s is s^4 (varsigma^2 + m_L^2)^2, so the average is

    s^4 e^{-t c} < e^{t m^2} [15/(4t^2) + (9/2) m^2/t + 3 m^4 + 2 t m^6] >

In the limit of large J at fixed z = t J^2, the average over m becomes an integral, and by parts with M_k = int_0^1 u^{2k} e^{z u^2} du, (2k+1) M_k + 2z M_{k+1} = e^z, one gets exactly

    e^{-z} int_0^1 e^{z u^2}[15/4 + (9/2) z u^2 + 3 z^2 u^4 + 2 z^3 u^6] du = z^2 - z + 15/4

(s8 B, quadrature to 20 digits). Hence W_J(s) = s^2[(15/4) vartheta^2 - s vartheta c_J + s^2 c_J^2], positive since its discriminant is negative.

**Independent check without the Casimir identity (s8 C).** With commuting N = (0,0,n) and explicit spin-J matrices, (1/24)(tr_V Z^4 - 2 tr_D Z^4)/(2J+1) = n^4 - (2/3)c n^2 + c^2 - c/3, at J = 1, 2, 3. The Gaussian average of the top terms is 15/(4t^2) - c/t + c^2.

**Exact Plancherel average (s8 D):**
- the ratio to W_J is nearly J-independent at small s: at s = 1e-3, vartheta = 1 it runs from 0.99789 (J = 0) to 0.99784 (J = 10), and at vartheta = 2 it is 0.99740 for all J <= 10;
- the deficit matches -(7/12 vartheta + 4/3 + 1/(5 vartheta)) s;
- the frozen limit reproduces w(xi);
- Y_{A,J} exact against closed form: ratios 0.969 to 0.999 at a from 20 to 2000.

Those J-independent corrections to the slice average are *not* claimed as complete, because the slice average is frozen in tau: its a_1 is the slice value, not R/6 + E_0. Only the J-dependent leading part and the positivity are claimed.

**Level form:**

    Y = (sqrt|g|/32 pi^2) Sum_A Sum_{J<=n} (2J+1) 2 M_A^2 [15 vartheta^2/(4D) - vartheta c_J/D^2 + 2 c_J^2/D^3],   D = M_A^2 + mu_J

**Expansion (s8 E).** Relative correction -(mu_J + (4/15) c_J/vartheta)/M_A^2, for M_A^2 >> mu_J. On S^2_N the sum over A carries 2 ln N/chi^2.

| N | n | x | vartheta | Y / value above | L'/(N^2 vartheta^2) | law | n/(chi N) |
|---|---|---|---|---|---|---|---|
| 1024 | 10 | 0.3 | 1 | 0.99792 | 5.3257 | 5.34 | 0.018 |
| 256 | 10 | 0.3 | 1 | 0.97835 | 5.1947 | 5.34 | 0.071 |
| 256 | 10 | 0.81 | 1 | 0.99045 | -0.0230 | 0.0156 | 0.043 |
| 256 | 40 | 0.1 | 1 | 0.72143 | 4.8883 | 6.86 | 0.49 |

The third row shows that the root x_0 moves slightly at finite n, as expected. The last row shows positivity persisting outside the equal-weight regime, where the expansion estimate fails and the closed form is the statement.

**Mixed term with the fibre flux.** sigma^M gains +2 s^2 c_J, which gives L' a contribution -c_J Sum c_i b_i/(b_i + mu_J) -> 4 c_J per level. Its ratio to Y matches 4<c>/(7.5 vartheta^2 N^2): 3.05e-5 at N = 1024, n = 10 (s8 E).

**Cross term.** It commutes with J_ab, so the positivity above is unaffected. Its effect on the weights is of relative order s J^2, the same order as the level weight, so it is small at equal weights and uncontrolled outside. It is dropped, under the merged hypothesis.

### E. Other corrected text

**F2.** At Y = 0 the necessary condition for beta_K > 0 is only 4U_4 + 2U_2 > 0, hence Uhat < 0. beta_K = 1 is attained in the cubic case at U_4 = Utilde - (3/2) U_2 (example Utilde = 1, U_2 = -1, U_4 = 5/2, C_3 = -4, U_chichi = 16, s7 D), and in the mass case only as a limit from below. The false route statement of r1 is gone.

**F3.** Checked by hand: on non-compact stacks s_0 ~ s^-3, so v - tau ~ s, tau ~ s^-1, giving Uhat ~ 1/s_c, V - T ~ ln s_c, T ~ 1/s_c^2. R9 is correct.

**F4.** R1 applied.

**F5.** Phase average rechecked: (A/4 pi^2) m^-4 m^2 q^2 (t/4m^2)^2 (1/2) = q^2 t^2/(4L). R12 is correct.

**F6.** g, V_0, U and the Yukawa condition are fixed; see the table.

**Vacuum term (consequence of F1, added by me).** q_b^2 is "given U_4 alone". At chi^2 <~ vartheta, U_2 and the first term are of the same size and carry second-order non-derivative terms, not computed. E4 states this.

### F. "(S1) not the computed coupling" and stale passages (F7)

**New reading.** The r1 sentence is deleted.
- Above m_chi: S2.
- Where the tree stabiliser dominates: S2 approximately.
- Below m_chi: beta_K = -2 U_t'/U_chichi, so S1 is a condition on supplied tree data and on chi^2/vartheta.
- Uhat >= 0 and Y <= 4|U_4| + 2|U_2| (on S^2_N: chi^2 >= 0.81 vartheta): beta_K <= 0, S1 excluded in this class.
- Uhat >= 0 and Y above: beta_K > 0, S1 reachable, not selected.
- Uhat < 0: S1 reachable at negligible Y, q_b^2 < 0.

**Stale passages (redone by grep and reading).**
- L2486 "(S1) is, on the mass shell, the source of the same action with M^2 ∝ rho/sqrt|g|, ..., which is not derived": still true. The insert does not derive it either. No change.
- L2413, L2415, L2417, L2457 "fibre-flux part ... not computed": these concern the part with two base derivatives of the wave (per-level J^2/mu_J by power counting). That remains not computed; the insert says so. The non-derivative background value computed here does not make them false. No change.
- L2413 "logarithmic at both ends and not suppressed by the flux of K": consistent; Y is its derivative in ln chi.
- L2402 "logarithmic and fibre-flux contributions" not computed: concerns the two-derivative forms, still true. L2440 "complete at that order": relied on, not changed.
- 044-048 S1/S2 statements: unchanged. PRIOR-CLAIM-ERROR: none.

No replacement outside the insert is proposed.

### G. Literature

**Verified this round:** J. R. David, M. R. Gaberdiel, R. Gopakumar, "The Heat Kernel on AdS_3 and its Applications", arXiv:0911.5085, JHEP 1004:125. The fetched PDF's Eqs. (5.12)-(5.13) give, for spin s on H_3^+, eigenvalue -(lambda^2 + s + 1) and measure proportional to (lambda^2 + s^2). This agrees with my N^2 at m_L = s and with the density here. It attributes the measure to Camporesi and Higuchi; I did not read their papers. It is used only as a check, and is not cited in the insert, so no new bib entry is needed.

**Carried from r1 and review-r1, not re-fetched:** 2303.08012, 2509.24753, 2601.08031 as cited in the insert. `MantaSteinacker2025b` is verified and stays unchanged.

### Hypotheses and forks

**Common hypotheses:** Poisson limit; one loop; IKKT content supplied; product background without mixed flux; K single-scale with fixed Lambda^i; matter mass from chi alone; frozen symbol; formal continuation; first-order response; q.y = 0; V = T; late time; q below m_chi; local minimum of chi with tree kinetic term; equal weights.

**Obstruction classes.** None closes a direction outside its hypotheses.
- **O4a, beta_K <= 0.** Common hypotheses plus U_4 <= 0, U_2 < 0, Y <= 4|U_4| + 2|U_2|, with Y including the fibre flux at the background. On S^2_N at large N with chi N >> n: chi^2 >= 0.81 vartheta. Not a no-go for S1 outside this range.
- **O4b, no minimum at weak coupling.** Undeformed quartic alone on S^2_N at large N; a minimum needs 10/13 < |eps| < 1. Requires the same class; dropped entirely once a cubic or mass term is present.
- **O5, ratio 1 at large tau.** Needs light t and beta_K = 1, at V = T, equal weights, late static, first order. Unchanged by Y, since it uses beta_K as a number.

| Hypothesis | Relaxation | Explored | What it gave |
|---|---|---|---|
| First term dropped | keep it, fibre-constant | yes | Y; sign rule; branch x < 0.81 |
| Fibre flux in Y | all levels, background | yes | positive integrand, level form, unchanged at equal weights |
| Tree stabiliser | none, cubic, mass | yes | exact forms; S1 attained with Uhat > 0, tuned |
| Sign of Uhat | Uhat < 0 | partly | S1 reachable, q_b^2 < 0; flat stacks only with s-limit |
| Compact K, Uhat < 0 | scan | weak | scan uninformative (r1 s5 E); no non-existence claim |
| Light t, q below m_chi, V = T, equal weights | as r1 | partly | as r1, statements unchanged |
| Response of the fibre levels | first variation at J >= 1 | no | open |
| Non-derivative terms at chi^2 <~ vartheta | second order in alpha of U_2 and first term | no | open; decisive for long-range statement |
| Rotating K | fluctuation operator | no | open; hand estimate of r1 remains unverified |

**Ranked open avenues (each keeps spacetime emergent).**
1. Non-derivative sector of t on the branch x < 0.81: second-order terms of U_2 and the first term, tadpole, q_*^2 (with -U_chi,phi^2/2U_chichi), V_00, V_01. This now decides whether the branch gives a long-range force. It may use the factorised form (P_+ - 2)(P_- - 2).
2. Fluctuation operator about the rotating K, static channel, uniform omega.
3. Actual cubic tree coefficient for a K selected by the theory: does anything fix beta_K = 1? Control of one-loop against tree where the tree quartic is of the order of Y, and higher loops.
4. Fibre-flux part with two base derivatives of the wave (L2415), using the same harmonic decomposition; response of fibre levels.
5. Compact K with Uhat < 0, or a proof of absence.
6. Level-dependent and external-harmonic weights; fibre Laplacian; cross term.
7. Loop kinetic and W_R mixing of chi; non-singlet moduli; composition dependence.
8. D1, overdue and independent; a reasonable next package if avenue 1 stalls.

## Claim classification

| Claim | Class |
|---|---|
| Tree form on psi Lambda_A; rigid in gamma at fixed K | established (Poisson limit, product) |
| l-loop exponent -l at fixed K; "order one only from chi" | power counting, not derived |
| Gamma_1 depends only on chi^2/lambda; homogeneous exponent | established where the proper-time form converges (Y' neglected in the general form) |
| U_4, U_2 forms | established from the merged factorisation; conditional on it |
| Y at frozen symbol, fibre-constant | established here; completeness at that order relies on merged L2440 |
| beta_K = -2U_t'/U_chichi, sign rule | established for these forms (first order, V = T, late static, fibre-constant response) |
| Forms with Y; x_0; 10/13; x > 5/2; beta_K = 1 at x = 3/10 | established algebra; large-N law on S^2_N is numerical at 60 digits, not proved in closed form |
| Identity tr_V - 2 tr_D + 4 = (P_+ - 2)(P_- - 2) | established identity, new (background; relies on merged J_ab form) |
| Integrand >= 0 on principal series | established, new |
| Y >= 0 with fibre flux | conditional: multiplicity weight in the formal continuation, cross term dropped |
| Level form of Y | conditional: leading in s, frozen, cross term dropped; checked against exact slice average |
| Equal-weight stability of Y on S^2_N | numerical |
| Uhat values, 4 ln N + 1.016, flat-stack signs with an s-limit | numerical or established as in r1 |
| I[X_beta], g2, potentials, poles (given U_4 alone) | conditional on equal weights; exact within them |
| O4a, O4b, O5 | conditional on the stated classes |
| S1 point at x = 3/10 | tuned tree data supplied; not derived; one-loop not small against tree |
| Inputs retained | IKKT content, formal continuation, K, stabiliser, q_*^2 |

**Open:** C, F, N remain OPEN and PROGRAMME-CONDITIONAL.

## Proposed changes

**File `chapters/appH-microscopic-proofs.tex`.** One insertion, no replacement.

- **Anchor:** immediately before the unique line `\section{Problem G: HBEV}` (count 1 by s6), after the 048 closing sentence.
- **Kept:** everything.
- **Text:** `proposals/049-k-scale-dilaton-response/appH_insert.tex`, **21698 bytes, sha256 92f8033b70adb8140f1c70b69e81f101ae30597d10d662c4c70f72045a10e4e2**, ASCII, LF, no BOM; built by s9 from appH_insert.r1.tex (sha 13879e6c...). This file is the `latex` block; it is not duplicated here. The integrator restores CRLF.
- **Labels verified:** eq:Smatrix, ass:gap-psi, ass:lorentzian, ch:vierbein-emergence, once each. No new labels.
- **Cites verified:** Steinacker2023, Steinacker2026, Bertotti2003 in bib; MantaSteinacker2025b from the entry below.

**File `bib/namcg.bib` (integrator).** Unchanged from r1, verified by review-r1:

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

**Stale passages elsewhere:** none require a change; see section F.

### Map of review-r1 to this round

Script s9 requires each old string once in turn and refuses to write on a mismatch. All of R1-R20 and E1-E5 applied.

| Item | Done | Verified / change and why |
|---|---|---|
| R1 | as given | Power counting wording correct |
| R2 | as given | Correct scope |
| R3 | changed | Value verified. Added "on fibre-constant modes" and the merged completeness clause. Replaced "not computed" with a pointer, since item 2 computed it. "the derivative of the density" since U is defined later |
| R4 | changed | Added the reason T̄.y = 0 and "fibre-constant part of Y"; "U ... with the first term" |
| R5 | as given | s7 D, F |
| R6 | changed | "chi^2 >> vartheta" replaced by "chi^2 That >> vartheta N_K", since Lambda^i normalisation makes the former K-dependent |
| R7 | changed | Forms verified (s7 D). Added "Y' neglected" and "from above where it is negative" |
| R8 | changed | Verified. Strict inequalities: U_chichi = 0 at |eps| = 10/13, and a maximum for |eps| >= 1. Added the x = 3/10 example with its caveat |
| R9 | as given | Hand check in section E |
| R10 | as given | Algebra checked |
| R11 | as given | Plus E1 for the coupling |
| R12 | as given | Rechecked |
| R13, R14 | as given | Verified: pole at q_b^2 - q_*^2 |
| R15 | changed | Sharper: Y <= 4|U_4| + 2|U_2| rather than chi^2 >> vartheta; records the case above it |
| R16 | as given | Window vacuous |
| R17 | changed | Same condition as R15 |
| R18 | changed | Fibre-flux caveat removed by item 2; Uhat < 0 case stated as available at negligible Y; "relation not derived" added |
| R19 | changed | Scope of the fibre flux added |
| R20 | changed | New exact and leading statements added |
| E1 | new | Coupling note (F6) |
| E2 | new | Homogeneous form with Y' neglected |
| E3 | new | "Fibre flux in the first term" block (item 2) |
| E4 | new | Vacuum term at chi^2 <~ vartheta |
| E5 | new | Mixed term with all frozen orders against U_2 |
| F1 | closed | Option (a) with Y verified; headline, table and classes restated |
| F2 | closed | R7, R18, section E |
| F3 | closed | R9 |
| F4 | closed | R1 |
| F5 | closed | R12 |
| F6 | closed | g: E1, R11. V_0: R13. U: R4. Yukawa: R14 |
| F7 | closed | Section F |

## Verification scripts

In `proposals/049-k-scale-dilaton-response/`. New outputs are `*.r2.out.txt`; r1 outputs are untouched. s1-s5 were not changed or re-run (their statements stand at Y = 0, and s4 D is a test of the algebra at Y = 0 only).

| Script | Checked | Result |
|---|---|---|
| s7_first_term.py | Y closed form; large-N law; forms with Y; x_0; 10/13; counterexample; T̄.y | as quoted; exact rationals for F; 60 digits elsewhere |
| s8_fibre_flux.py | sign of Z; identity; scaling form; commuting check; exact Plancherel; level table | residuals <= 1e-11; f(z) to 20 digits; ratios as quoted |
| s9_apply_r2.py | builds the insert; refuses on mismatch | R1-R20, E1-E5 applied; size and sha above |
| s6_insert_mechanics.py | ASCII, labels, cites, status count | ASCII, CR 0, one status sentence, anchor count 1, labels 1 each; MantaSteinacker2025b 0 in bib, as expected until integration; "round " only from "background" (false positive) |
| compile_check.py | build with and without insert plus bib, outside repo | exit [0,0,0,0] both; 333 and 339 pages; 0 undefined refs and citations; 0 multiply defined; scratch removed. Rendered pages not inspected |

`appH_insert.r1.tex` and `repl_old.r1.txt` are unchanged copies of the r1 insert and the review's file. My first s7 quadrature showed a constant offset from small-s cancellation at 25 digits; the integrand now uses the series below 1e-4 and agrees to 15 digits.

## Decisions Taken

1. **RESEARCHER-DECISION: option (a), carry Y through and keep the Uhat > 0 route open.** Evidence: Y verified independently, and the fibre-flux part computed and found not to change it at equal weights. So (a) is supported, not only preferred, and (b) would discard a correct and favourable branch. Rejected: (b), which would leave chi^2 <~ vartheta untreated although the computation exists. Cost of (a): the insert is longer, and the branch is conditional as stated.
2. **Compute the fibre-flux part now:** it fit. Its central identity is short and checkable, and it replaces a caveat with a result. Not computed: the part with two base derivatives, and the response of levels.
3. **Use the exact Casimir route, not only a commuting-symbol expansion:** it gives positivity for all J and s. The commuting check is kept as independent evidence.
4. **Claim only the J-dependent leading part of W_J.** The J-independent slice corrections are frozen in tau and would mislead.
5. **Include the x = 3/10 example with its caveat:** it is the concrete counterexample to r1's headline. A label-free statement alone would be less checkable.
6. **Do not cite 0911.5085 in the insert:** it is a check only, and this avoids a bib entry.
7. **O4b is kept narrow,** and the window is deleted rather than re-derived, since no weak-coupling minimum exists for its case.

## Milestone assessment

**Routine.** Not a breakthrough: nothing is derived for the emergent metric, the S1-compatible point is tuned with supplied tree data, and the non-derivative sector is not computed.

M2 is not met: the corrected class is a bounded restriction on a coupling that 048 kept as a non-derived input, and the no-go is narrower than in r1. M3 is not met: nothing merged is false. M4, M5: none.

## Status-label recommendation

Critical-path list from Ch.17 and appH: A, B, C, D1, E, F, G-derived, N. Affected labels: none.

## Author decision needed

None.

## Remaining open step

To close C in this class: the non-derivative sector of t on a stated K (q_*^2, V_00, V_01, what cancels the vacuum term, and the second-order terms at chi^2 <~ vartheta); beta_K for the K selected by the theory, with its actual tree data; composition dependence; the Cassini comparison on the emergent metric, with Assumption gap-psi discharged. F needs the operators without the equal-weight input and with K selected. N needs control of the extra root.

## Special instructions for the gatekeeper

**New mathematics to review in full (sections C, D; s8; insert block "Fibre flux in the first term"):**
- the sign of Z (s8 A), since the opposite sign changes e^{-s} to e^{+s} and the large-s behaviour;
- the identity and the principal-series labels;
- the use of the merged J_ab form;
- whether the slice harmonic analysis is a fair reading of the leading symbol at a frozen point;
- H_0 = N^2/vartheta + mu_J with the cross term dropped;
- the by-parts identity f(z) = z^2 - z + 15/4;
- the 4 c_J mixed-term estimate.

**Also re-derive:** Y via the closed form I(a); the T̄.y argument; 10/13 and the strict inequalities.

**Check especially:** "the fibre flux does not change Y or its sign" is scoped to the background, equal weights and the frozen symbol. Is "positive" in the level form clear enough that it does not suggest Y >= 0 in the Lorentzian path integral beyond the formal continuation? My R6 and R15 go further than your text; check them.

**Must not be asserted:**
- that S1 is derived, or selected, by this class;
- a Cassini bound on the emergent metric;
- that compact K with Uhat < 0 do not exist;
- that the branch x < 0.81 gives a long-range force (non-derivative terms are not computed);
- anything about the rotating K beyond the homogeneous relation;
- that published works are contradicted.

**Scan:** no definition, assumption, scope or status passage changes; ordinal and scan rule as you determine. The digest is stale by one review-only commit.
