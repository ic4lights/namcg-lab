# Proposal 073-d1-heisenberg-nonnull-leg, round 1

## Result

On time x Heisenberg (first-order equivariant class, constant connection, tree level), this package finds an
**exact family of solutions with non-null legs**. It derives the **complete characteristic structure** of the
forty linearised equations on that family. It then settles the question the 072 review left open (rank-1 avenue):
can a connection whose leg form eta^{ab} w_a w_b is nonzero produce a gauge-invariant gap for the Lorentz/torsion
modes? On this family the answer is no.

1. **Exact solutions (established, symbolic).** The family is
   w_a = k_a(chi B_n + th J_n) + P_a N_e + Q_a N_f, with the null line n = (1, s, -c, 0) at any tilt (s, c) on the
   unit circle and with
   P = zeta k + al e + (be+th) f, Q = x k + be e + ga f.
   It solves the first two brackets when th^2 - 2 th be - 2 be^2 - al^2 - ga^2 + 2 chi(al+ga) = 0, and additionally
   tau := chi+al+ga = 0 when s != 0. The third bracket holds.
   - Invariants: R_abcd R^abcd = 4 kappa^2 c^2 (th^2 - chi^2), which is > 0 for |th| > |chi|, and T_ac^c = tau k_a.
   - Every w_a fixes the null line n.
   - The 072 leg form is nonzero, but the vector operator eta^{ab} W_a W_b = -(eta^{ab}(P_aP_b+Q_aQ_b)) n (x) n^flat
     squares to zero.
   - The family contains the 072 wider family. It is checked at operator level on the bundle, order-zero part
     included, at two exact points.
   - In the 072 survey, most solutions have this form (numerical, not a classification).
2. **Exact identity.** On the whole ansatz, Q_b = Q_b|_{w=0} - tau k^a F_ab. The gauge-invariant order-zero operator
   therefore sees the connection only through the torsion trace tau. At s != 0 it is exactly the connection-free
   068 operator.
3. **Characteristic structure (exact at rational points, numerical elsewhere).** Every characteristic root of the
   forty equations satisfies (q_par + Lambda k_par)^2 + kappa p l = 0, where k_par = (1, 0, c, 0) and l is odd
   >= -1.
   - Lambda lies in the finite set {i tau/2, i(tau/2+chi), i(tau/2+chi) +- th, i(tau-3chi/2) +- rho}, with
     rho^2 = 3/2 th^2 - chi^2 + (tau-3chi)^2/4.
   - The multiplicities are 10, 2, 2, 2, 2, 2 factors per level.
   - The Landau levels kappa p l are never shifted.
4. **Decision on the gap.**
   - At s = 0, k_par is null and no momentum-independent term appears. This extends the 072 no-gap result to
     non-null legs and R_abcd R^abcd > 0.
   - At s != 0 there is, for the first time in this programme's Lorentz/torsion analysis, a
     **momentum-independent term s^2 Lambda^2** in the gauge-invariant characteristic equation, for every class with
     Lambda != 0. Its sign is not that of a mass:
     - for real Lambda it enters q0^2 as -s^2 Lambda^2 (tachyonic sign), and every branch reaches q0 = 0 at a finite
       p* > 0;
     - for imaginary Lambda the zero-momentum roots are imaginary (rates).
   - The Q class has Lambda = 0 and has no such term.
   - Hence no gauge-invariant gap or mass of definite sign arises on this family at tree level and linear order.
     This is a bounded result with its hypotheses listed below. It is not a no-go for D1, and no closure is claimed.

The structural lesson, which transfers to the next packages, is this. On constant-connection Heisenberg solutions,
the connection acts through complex constant shifts along a null leg. A momentum-independent term arises only from
the part of that null leg that the Landau quantisation does not resolve. The term is the square-completion of a
first-order term, not an independent mass term. A definite-sign gap therefore needs an ingredient that is absent
here: a norm, the bilinear term mu^2 (an intrinsic invariant scale), loops, or non-constant connections.

## Target and status

- **Problem D (local Lorentz)**, `chapters/appH-microscopic-proofs.tex` Sec. `sec:status-D` (L715-722):
  "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL." D2 is reduced scope only.
- **Chapter 17, D1** (`ch17-agenda.tex` L329-345, L650-653, L712-716): D1 closure requires "the omega, A_mu, B, and
  ghost operators and the resulting field content to be specified", and requires that the locked frame exist and be
  non-degenerate, derived from microscopic data.
- **Missing step targeted** (appH L745-748): "derive the effective dynamics of the independent diagonal connection
  or retain it as unresolved field content. Generator counting alone does not settle its torsion or propagating
  modes." This package addresses the propagating-mode / gap content of the torsion and Lorentz sector in the
  first-order equivariant class (appH L1513-1533), on left-invariant Heisenberg backgrounds. These continue 068
  (L1609-1629), 071 (L1631-1646) and 072 (L1648-1661).
- **Dependencies retained (not discharged).** The class itself and its selection by the matrix integral are
  retained, as are Assumptions `ass:frame-lock`, `ass:nondeg`, `ass:lorentzian`, `ass:local-lorentz` and
  `ass:EFT-a2` (as listed in the 071 paragraph).
- **Critical-path set** at the current full-GR / matrix-derived scope (ch17 + appH ledger labels): A, B, C, D1, E,
  F, G-derived, N. No discrepancy found between ch17 and appH for D.
- **Classification of this package: PROGRAMME-CONDITIONAL** (conditional on the class; tree level; linear order).

## Source reading

Digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT`, and the digest reports
`dirty-chapters: yes`. The appH file hash in the digest (`c8c07938df99`) equals the live
`chapters/appH-microscopic-proofs.tex` sha256 `c8c07938df995ac1…`, so the digest reflects the working tree, which
contains the uncommitted 072 integration.

Read in full:
- appH Problem D ledger and missing step (L715-760);
- the first-order equivariant class paragraph (L1513-1533);
- the 068/071/072 paragraphs and the locked-frame composite paragraph (L1606-1661);
- ch17 D-passages (L329-345, L645-655, L708-716).

Also read: the 072 review r1 (avenues), and the 068/071/072 code used read-only (`core068.py`, `bg.py`, `lin.py`,
`tools068.py`, `gk071r2_exact.py`, 072 `common.py`, `jblocks.py`, `s2`, `s3`, `s4`).

Not done: a full scan of all chapters. Because Edit 2 touches a scope sentence of the 072 paragraph, protocol 3(c)
requires the gatekeeper full scan.

## Research and reasoning

### R1. Exact solution family (S1, S2)

**Notation.** Write X(u,v)^{cd} = u^c v^d - u^d v^c. For (s, c) with s^2 + c^2 = 1, set:
- n = (1, s, -c, 0), n̂ = (0, s, -c, 0), e = (0, c, s, 0), f = (0, 0, 0, 1), k_a = -eta_ab n^b = (1, -s, c, 0);
- B_n = X(δ_0, -n̂), J_n = X(e, f), N_e = X(n, e), N_f = X(n, f).

At (s, c) = (0, 1) these are k, B, N, N' of 071/072 and J_13.

**How the ansatz was found (not a classification).** A numerical survey on the Heisenberg algebra (the 072 s4
seeds) showed that the clean solutions have three properties:
- every w_a has a common real null eigenvector n;
- in the basis adapted to n, the B_n and J_n legs are proportional to k;
- the null-rotation legs (P, Q) are general.

Substituting this ansatz with a rational tilt and adapted leg coordinates gave a Gröbner basis. It required:
- no l-legs;
- P_f = Q_e + th, which is the antisymmetric part of the 2x2 null-rotation leg matrix, fixed by th;
- the quadratic constraint;
- tau = 0 when s != 0.

**Symbolic verification (S1).** S1 then checks for symbolic (kappa, s, c, chi, th, zeta, x, al, be, ga), reducing
modulo c^2 + s^2 - 1:
- (a) s arbitrary with tau = 0, plus the constraint ⇒ B1 = B2 = 0 identically;
- (b) s = 0 with tau free, plus the constraint ⇒ B1 = B2 = 0;
- (c) with the constraint only, every remaining component vanishes at tau = 0 and at s = 0, and 13 distinct
  nonzero remainders exist. So at s != 0, tau != 0 the constraint alone does not suffice.

**Invariants.**
- R_abcd R^abcd = 4 kappa^2 c^2 (th^2 - chi^2).
- T_ac^c = tau k_a.
- R_ab^{ab} = 2 kappa (th + s^2(be - th) + c s x).
- T_abc T^abc = -2 kappa(2(th + s^2(be - th) + c s x) - kappa).

**Third bracket.** For s = 0 and tau != 0, t = tau k / 2 gives F_13 = kappa tau / 2, and the third bracket
nabla^a F_ab - T_ab^c F^a_c vanishes symbolically, as in 072 with chi → tau. For tau = 0, F = 0.

**Null line and leg operator.** W_a n = lambda_a n with lambda = (-chi, chi s, -c chi, 0). The vector operator is
L = eta^{ab} W_a W_b = -(eta^{ab}(P_aP_b + Q_aQ_b)) n n^flat, with
eta^{ab}(P_aP_b + Q_aQ_b) = al^2 + ga^2 + be^2 + (be+th)^2 (S1(f) prints al^2 + 2be^2 + 2 be th + ga^2 + th^2).
Since n is null, L^2 = 0. By hand: null rotations about one null vector compose to multiples of n n^flat, and the
k-leg part cancels because k is null. The tensor leg form eta^{ab} w_a^{cd} w_b^{ef}, the 072 s4 diagnostic, is
nonzero; S1(f) prints a sample. So the 072 survey's "non-null leg" solutions are of this kind: their real w^2 term
is nilpotent on vectors.

**Operator level (S2).** Following the construction of `gk071r2_exact.py`, with general constant w, om = -w,
t_a = ½·divergence, symbolic y and kappa, and a rational Cayley u, S2 checks at U2 (s = 0, tau = 7/5) and at
T1 (s = 3/5, entries in sqrt 2):
- the first relation;
- all components of [D^a, [D_a, D_b]], multiplication part included, are identically 0;
- the read-off T_ac^c = tau k_a, with F_13 = 7 kappa / 10 at U2.

**Survey comparison (S3).** The 072 s4 survey is re-run (same seeds) and classified: 107 clean solutions, 80 in the
family at strict tolerance, 25 more at loose tolerance, and 2 outside, where the leg-test defects are 1e-6 and 2e-5.
The degenerate solutions, with nilpotent w and RR close to 0, make the null-line test ill-conditioned (defect up to
5e-9). This is why loose tolerances are reported.

**Rational points.** The tilted constraint with tau = 0 is equivalent to X^2 + Y^2 + 5 chi^2 = 3 th^2
(X = 2be + th, Y = 2ga + chi). It has no nonzero integer solution up to 12 (search). Tilted points therefore use
sqrt 2; no rationality claim is made.

### R2. Exact identity for the order-zero operator (S1(g))

For constant w, F_ab[A] contains no w, as 072 noted. By hand:

Q_b - Q_b|_{w=0} = eta^{xa} Om_xa^z F_zb + 2 eta^{xa} Om_xb^z F_az - Om_ba^c F^a_c.

Here the second and third terms of nabla^a F - T^w F combine. The first term equals -(T_c^{cz}) F_zb. S1(g)
verifies symbolically, for every F, without the constraint, that on the ansatz the w-dependent remainder is exactly
-tau k^a F_ab. Hence:
- at s = 0, Q is the 072 operator with chi → tau, so its roots follow the 072 display with c = 1, chi → tau
  (exact, as in 072);
- at s != 0, tau = 0 and Q = Q|_{w=0}, the 068 operator, with levels q0^2 = p^2 + kappa p(2n+1∓2).

The gauge-invariant order-zero field is thus never gapped on this family.

### R3. Characteristic structure of the forty equations (S4–S7)

**p = 0 sectors (characters, no truncation; S4).** Every root satisfies (q + Lambda k)^2 = 0, with the fitted
Lambda independent of (q1, q3). This holds at 4 points (two untilted, two tilted, including chi != 0); the largest
deviation from the predicted set is 5e-3, attributable to multiple roots splitting. At U1 the result is exact:
U1 = (s = 0, chi = 1/4, th = 1/2, al = ga = 3/4, be = -1/4; tau = 7/4, rho = 3/4), and the check is repeated with
zeta, x != 0 at (q1, q3) = (1/2, 1/3). There the determinantal divisor D_r (degree 40, generic rank 30 of 40)
equals ∏ (q0^2 + 2 Lambda q0 - (q1^2 + q3^2)) with multiplicities 10, 2, 2, 2, 2, 2, remainder 0, over Q(i).

**Landau sectors, s = 0 (S5 exact; S6 numerical).**
- At U1 the background is SO(2)-symmetric, and J = n + helicity is conserved (leak 0). In every J-block,
  J = -2..3, at (kappa, p) = (1, 1/2) and (2, 1/4), D_r factors completely into
  q0^2 - p^2 + 2 Lambda (q0 - p) - kappa p l, remainder degree 0. The totals for l <= 5 are 5, 5, 10, 10 for class
  i tau/2 and 1, 1, 2, 2 for each other class, at l = -1, 1, 3, 5.
- At three non-symmetric points (U2; G1 with chi = 0.4; G2 with kappa = 1.7, tau = 0), the column cut gives the
  same counts. The kernel is the gauge span. Q's roots are all in class i tau/2.
- The class-i tau/2 roots carry chains and split by about 1e-3; the other classes agree to <1e-7. At most 2 of
  about 229 roots per sector are unassigned at tolerance 5e-3.

**Landau sectors, s != 0 (S7).** The solutions are not polynomial × Gaussian. The column cut finds only part of the
class Lambda = 0, S7(e): 108 roots, all in class 0 at T1, and 108 + 1 at T2; exploratory constant shifts of E_1 also failed, in scratch only and not used for any
claim. S7 therefore uses square truncations, N = 18 and N = 24:
- every converged eigenvalue (agreement 1e-8, |q0| < 2.5), 147 at T1 and 191 at T2, is assigned to
  (q_par + Lambda k_par)^2 + kappa p l = 0, with k_par = (1, 0, c, 0) and the same Lambda set (tau = 0), with zero
  unassigned;
- every predicted root for l = -1, 1, 3 is found within 8e-9 (T1) and 1.5e-7 (T2);
- the kernel of the column cut at generic q0 is the gauge span.

**Algebra of the root formula (by hand).**
(q_par + Lambda k_par)^2 = -(q0 + Lambda)^2 + (p + c Lambda)^2 = -(q0^2 - p^2 + 2 Lambda (q0 - c p) + s^2 Lambda^2).
The characteristic equation is therefore

  q0^2 - p^2 + 2 Lambda (q0 - c p) + s^2 Lambda^2 = kappa p l.

**Why k_par and not k.** In the Landau sector E_1 is an oscillator, not a character. The k_1 component of the
shift is not resolved, and only the central part (k_0, k_2) of the shift survives as c-numbers. This is the
mechanism behind the constant: k_par^2 = -(k_1)^2 = -s^2. It is a structural reading of the numerics, not a
derivation; the operator-level reason why the class roots are those of (Ê_par)^2 + E_perp^2 remains to be derived
(open step O1).

### R4. Gap decision and sign (by hand from the root formula)

- **s = 0.** The constant term is 0: q0 = 0 is a root at p → 0 for every class (the other root is -2 Lambda). Real
  parts ±th and ±Re rho are real null shifts. This is the same structure as the appH null-rotation background
  "(q + j th k)^2 = 0", which has no gap. Imaginary parts are rates.
- **s != 0.** The term s^2 Lambda^2 is momentum-independent. Three facts show it is not a mass.
  1. It equals the square-completion of 2 Lambda (q0 - c p) and vanishes as s → 0.
  2. As p → 0+, the roots are q0 = -Lambda(1 ∓ c). For imaginary Lambda these are imaginary (rates). Examples:
     at T2, class i chi gives -0.06i and -0.54i; at T1 there is no such class.
  3. For real Lambda (all classes at chi = 0, e.g. T1: Lambda = ±th, ±sqrt(3/2) th), the constant enters q0^2 as
     -s^2 Lambda^2 < 0, opposite to a mass. At q0 = 0 the equation reads p^2 + (2c Lambda + kappa l) p - s^2 Lambda^2 = 0.
     The product of its roots is -s^2 Lambda^2 < 0, so there is exactly one p* > 0 at which the branch has zero
     frequency, for every l.

  For general complex Lambda, the zero-momentum roots -Lambda(1 ∓ c) are complex, so the modes grow or decay.
- **Class Lambda = 0** (contains Q; 10 factors) has no constant.
- **Conclusion.** No root set of the form q0^2 = p^2 + kappa p l + m^2 with m^2 > 0 real and no first-order term
  appears.

**Gauge-invariance of the labels.** (q0, p) are eigenvalues of the central right-invariant fields partial_0 and
partial_2, which commute with all D_a and S_cd (appH L1611). Relabelling by other central symmetries,
q0 → q0 + b p, leaves the p → 0 limits and the zero-frequency crossing unchanged. At SO(2)-symmetric untilted points
an extra symmetry J_total exists, which is why real shifts by helicity × th carry no invariant meaning there.

### Hypotheses of the bounded result (fork list) and what each relaxation gave

| # | Hypothesis | Relaxation explored here | Outcome |
|---|---|---|---|
| H1 | connection along null leg only (072) | non-null legs P, Q with e/f components | exact family; leg operator nilpotent; no gap |
| H2 | null line in the E_0, E_2 plane | tilt s != 0 | first momentum-independent term s^2 Lambda^2; not a mass (sign/rates) |
| H3 | tau-type trace only via chi | general tau (s = 0) | Q = Q0 - tau k F exactly; rates only |
| H4 | SO(2) symmetry | S != 0, zeta, x != 0 | same Lambda set; zeta, x, S enter only via constraint |
| H5 | constant connection, left-invariant | not explored | open (avenue 4) |
| H6 | tree level | not explored | open (avenue 2) |
| H7 | no norm/pairing | not explored | open (avenue 1) |
| H8 | C_{μνλ}=0, no bilinear mu^2 term | not explored | open (avenue 3, ranked high) |
| H9 | linear order | not explored | open (avenue 5) |

### Literature

No new citation. The results are internal to the class as defined in appH (`HanadaKawaiKimura2006`,
`FurutaHanadaKawaiKimura2007` already cited there). The Landau analogy (`NielsenOlesen1978`) is already cited in the
068 paragraph and is not used further. Nothing was imported from the literature.

## Claim classification

- C1 (established, exact symbolic). The family solves B1 = B2 = 0 under the constraint, with tau = 0 for s != 0.
  Proven: the third bracket; RR = 4 kappa^2 c^2 (th^2 - chi^2); T_ac^c = tau k_a; the common null eigenvector;
  L = -(..) n n^flat and L^2 = 0. [S1]
- C2 (established, exact at two points). The operator-level relations and the matrix equation hold on the bundle,
  order-zero part included. [S2]
- C3 (established, exact symbolic). Q_b = Q_b|_{w=0} - tau k^a F_ab on the whole ansatz. Consequences for Q's roots
  follow from 068/072 established results. [S1(g)]
- C4 (numerical survey, not a classification). Of the 107 survey solutions (072 s4 seeds) that converge to residual
  1e-13, 80 pass the family tests at tolerances 1e-10 to 1e-9 and 25 more at 1e-8 to 1e-6. These are a null line,
  B_n/J_n legs along k, and tau = 0 off the E_0, E_2 plane. Two do not pass. For all 107, |(eta^{ab}W_aW_b)^2| <= 1.5e-11.
  The two outliers have defects of 1e-6 and 2e-5 in the leg test; one has n = (1,0,1,0), i.e. c = -1. [S3]
- C5 (exact at rational points). At p = 0 at U1 and U1z, D_r = ∏ over the Lambda set. In the Landau J-blocks at U1
  (two (kappa, p)), the full factorisation holds for blocks J = -2..3, with remainder 0. [S4(b), S5]
- C6 (numerical). The root formula (q_par + Lambda k_par)^2 + kappa p l = 0 with the Lambda set and multiplicities
  holds at sampled non-symmetric untilted points (column cut, l <= 5) and at tilted points (converged square-truncation
  eigenvalues). The general Lambda formula for arbitrary parameters is a numerical fit verified at six parameter
  points; it is not derived. [S4(a), S6, S7]
- C7 (established by hand, given C6). There is no momentum-independent term at s = 0. At s != 0 the term s^2 Lambda^2
  is present, and its sign/limit properties are as stated. Hence there is no gap or mass of definite sign on this
  family. [R4]
- C8 (unresolved).
  - Norm.
  - Loops.
  - Nonlinear evolution.
  - Survey solutions outside the family.
  - The selection of class or background by the matrix integral.
  - Identification with the emergent metric.
  - An analytic derivation of the Lambda set (O1).

## Proposed changes

### File `chapters/appH-microscopic-proofs.tex`

**Edit 1 (insert).** Insert the block `appH_insert_r1.tex` (CRLF, UTF-8 without BOM), followed by one blank CRLF
line, immediately before the unique line

```
\section{Problem E: signature}
```

It goes after the closing paragraph of "First-order equivariant class on the Heisenberg background with curvature:
Landau sectors of the linearised equations (conditional; not closure)". That closing paragraph begins "These
statements are for Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and no matter term, tree level, linear
order in the fluctuation, the Lorentzian contraction and the wider family" (unique). Nothing is removed. Labels
used: `eq:Smatrix`, `ch:vierbein-emergence`, each defined once; the script verifies this. No new labels and no
citations. The block has exactly one status sentence, at its end.

The block text is generated verbatim by `make_insert_r1.py` and reproduced here:

```latex
\paragraph{First-order equivariant class on the Heisenberg background: connections with legs off the null direction (conditional; not closure).}
Keep time times the Heisenberg group with the normalisation and the fluctuation of the preceding paragraph. For \(s^2+c^2=1\) let \(n^a=(1,s,-c,0)\), \(\hat n^a=(0,s,-c,0)\), \(e^a=(0,c,s,0)\), \(f^a=(0,0,0,1)\) and \(k_a=-\eta_{ab}n^b\), write \(X(u,v)^{cd}=u^cv^d-u^dv^c\), and let \(B_n=X(\delta_0,-\hat n)\), \(J_n=X(e,f)\), \(N_e=X(n,e)\) and \(N_f=X(n,f)\); at \((s,c)=(0,1)\) these are \(k\), \(B\), \(N\) and \(N'\) of the preceding paragraphs and the rotation of the \(1\)-\(3\) plane. Take
\[
w_a{}^{cd}=k_a(\chi B_n+\vartheta J_n)^{cd}+P_aN_e^{cd}+Q_aN_f^{cd},\qquad P_a=\zeta k_a+\alpha e_a+(\beta+\vartheta)f_a,\quad Q_a=xk_a+\beta e_a+\gamma f_a,
\]
which is the wider family at \(s=\vartheta=\alpha=\beta=\gamma=0\). For all real \(\kappa,\chi,\vartheta,\zeta,x\) the first two brackets hold when
\[
\vartheta^2-2\vartheta\beta-2\beta^2-\alpha^2-\gamma^2+2\chi(\alpha+\gamma)=0
\]
and, if \(s\neq0\), \(\tau:=\chi+\alpha+\gamma=0\); at \(s\neq0\) and generic \(\tau\neq0\) the constraint alone does not suffice. Then \(\mathsf T_{ac}{}^c=\tau k_a\), the third bracket holds, \(\mathsf R_{abcd}\mathsf R^{abcd}=4\kappa^2c^2(\vartheta^2-\chi^2)\), which is positive for \(|\vartheta|>|\chi|\), and every \(w_a\) fixes the null line of \(n\) (exact for symbolic parameters; for the operators on the bundle at a rational Lorentz \(u\), order-zero part included, exact at one point with \(s=0\), \(\tau\neq0\) and one with \(s=\tfrac35\)). The form \(\eta^{ab}w_a{}^{cd}w_b{}^{ef}\) is nonzero when one of \(\alpha\), \(\beta\), \(\beta+\vartheta\), \(\gamma\) is, but on vectors \(\eta^{ab}w_aw_b=-\eta^{ab}(P_aP_b+Q_aQ_b)\,n\otimes n^\flat\), whose square is zero (exact). Of the 107 solutions of the survey of the preceding paragraph that converge to residual \(10^{-13}\), 80 pass the tests for this form at tolerances \(10^{-10}\) to \(10^{-9}\), 25 more at \(10^{-8}\) to \(10^{-6}\), and two do not; for all of them \((\eta^{ab}w_aw_b)^2\) vanishes on vectors to \(2\cdot10^{-11}\) (numerical, not a classification).

On this family \(\mathcal Q_b[A]=\mathcal Q_b[A]|_{w=0}-\tau\,k^a\mathsf F_{ab}[A]\) for all \(A\) (exact), so at \(s=0\) the order-zero operator is that of the preceding paragraph with \(\chi\) replaced by \(\tau\), and at \(s\neq0\) it is the operator of the paragraph on left-invariant backgrounds with torsion. For the forty equations, in the sectors \(p=0\), where \(E_1\) and \(E_3\) commute, every characteristic root lies on a cone \((q+\Lambda k)^2=0\), and in the Landau sectors every root satisfies
\[
(q_\parallel+\Lambda k_\parallel)^2+\kappa p\,l=0,\quad\text{that is}\quad q_0^2-p^2+2\Lambda(q_0-cp)+s^2\Lambda^2=\kappa p\,l,\qquad k_\parallel=(1,0,c,0),\ l\in\{-1,1,3,\dots\},
\]
with \(\Lambda\) in the set
\[
\bigl\{\tfrac{\mathrm i}2\tau,\ \mathrm i(\tfrac\tau2+\chi),\ \mathrm i(\tfrac\tau2+\chi)\pm\vartheta,\ \mathrm i(\tau-\tfrac32\chi)\pm\rho\bigr\},\qquad\rho^2=\tfrac32\vartheta^2-\chi^2+\tfrac14(\tau-3\chi)^2,
\]
whose members carry \(10\), \(2\), \(2\), \(2\), \(2\) and \(2\) of the twenty quadratic factors at \(l\ge3\), and half of these at \(l=\pm1\). So \(\zeta\), \(x\), \(\alpha\), \(\beta\) and \(\gamma\) enter only through \(\tau\) and the constraint, and the levels \(\kappa p\,l\) are not shifted. At \(s=0\), \(\chi=\tfrac14\), \(\vartheta=\tfrac12\), \(\alpha=\gamma=\tfrac34\), \(\beta=-\tfrac14\), where the rotation of the \(1\)-\(3\) plane combined with the oscillator level is conserved, this is exact in rational arithmetic after rational reconstruction, in the sector \(p=0\) at a sampled \(q\), also with \(\zeta,x\neq0\), and in the blocks that on the observed pattern contain all factors with \(l\le5\), at \((\kappa,p)=(1,\tfrac12)\) and \((2,\tfrac14)\). Otherwise it is numerical at sampled points: at \(s=0\) for \(l\le5\) as in the preceding paragraph, and at \(s=\tfrac35\), where the solutions are not polynomials times the Landau Gaussian, for the eigenvalues of truncations to \(18\) and \(24\) oscillator levels that agree, all of which are assigned. The kernel at generic \(q_0\) is the ten gauge directions for each level (numerical).

At \(s=0\) the vector \(k_\parallel=k\) is null and no term independent of the momentum enters, as for the wider family, now on backgrounds with \(\mathsf R_{abcd}\mathsf R^{abcd}>0\) and a nonzero leg form; the real parts \(\pm\vartheta\) and \(\pm\operatorname{Re}\rho\) of \(\Lambda\) shift the cones along \(k\), as on the null-rotation background of the paragraph on left-invariant backgrounds with torsion, and the imaginary parts are rates. At \(s\neq0\) the null leg has a component along \(E_1\), on which the Landau sectors act by oscillators, and \(k_\parallel^2=-s^2\), so the characteristic equation contains the momentum-independent term \(s^2\Lambda^2\) for every class with \(\Lambda\neq0\); the class \(\Lambda=\tfrac{\mathrm i}2\tau=0\), which contains \(\mathcal Q\), has none. This term is not a mass: it completes the square of the first-order term \(2\Lambda(q_0-cp)\) and vanishes with \(s\); as \(p\to0\) the roots of a class tend to \(q_0=-\Lambda(1\mp c)\), which are imaginary for imaginary \(\Lambda\); and for real \(\Lambda\), as at \(\chi=0\), it enters \(q_0^2\) as \(-s^2\Lambda^2\), with the sign opposite to that of a mass term, and for each \(l\) one of the two roots vanishes at the \(p>0\) with \(p^2+(2c\Lambda+\kappa l)p=s^2\Lambda^2\). So no gauge-invariant gap or mass of definite sign appears for the Lorentz or torsion modes on this family at this order. No norm is used, so no statement on stability is made.

These statements are for Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and no matter term, tree level, linear order in the fluctuation, the Lorentzian contraction and this family on time times the Heisenberg group with constant connection, in the sectors named. The survey solutions outside the family, a norm, loops, the nonlinear evolution, the regulated trace and the domains of the unbounded operators are not treated. Nothing here shows that the matrix integral selects this class, these backgrounds or the algebra \(\mathcal A\), so the assumptions listed in the paragraph on left-invariant backgrounds with curvature and torsion are not discharged, and the frame of these backgrounds is not identified with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
```

**Edit 2 (stale passage in the 072 paragraph).** Replace the unique string

```
(numerical survey, not a classification); they are not linearised here.
```

with

```
(numerical survey, not a classification); those of the form of the following paragraph are linearised there.
```

All other text is kept. The 072 sentence on "the solutions with R_abcd R^abcd != 0 of the survey of the preceding
paragraph" refers to the 071 survey on other algebras and stays correct.

Hashes: appH pre sha256 `c8c07938df995ac1e6ebedc4e80bcc4ce43eaec9ec99c45696aad6474554ab52`, post sha256
`69ab958ad2af131bc0aa6c7074b1e2da9ab5572b2de708d89915777b7fe1740b`.

No other file changes. No bibliography change.

## Verification scripts

All are in `proposals/073-d1-heisenberg-nonnull-leg/`. They import 068/071/072 code read-only and write no
bytecode.

| script | checks | runtime |
|---|---|---|
| `common073.py` | family constructor, Lambda set | – |
| `s1_family_exact.py` | C1, C3 (symbolic) | ~25 s |
| `s2_operator_exact.py` | C2 (operator level, exact) | ~4 min |
| `s3_survey_structure.py` | C4 | ~10 min |
| `s4_p0_cones.py` | p = 0: numerical Lambda sets; exact D_r at U1, U1z | ~3 min |
| `s5_landau_jblocks.py` | C5 Landau exact J-blocks at U1 | ~6 min |
| `s6_landau_untilted.py` | C6 untilted, column cut; gauge kernel; Q | ~2 min |
| `s7_landau_tilted.py` | C6 tilted, square truncations; gauge kernel; s^2 Lambda^2; p→0 limits; column cut | ~8 min |
| `make_insert_r1.py` | writes `appH_insert_r1.tex` (CRLF) from text, filling survey counts from S3 output | – |
| `apply_and_build_r1.py` | applies to a copy outside repo; hashes; labels; `--build` builds there | ~3 min |

**Reproduction pack** (run from the proposal folder):
- `python -I -B s1_family_exact.py` → residual sets `{0}` for (a) and (b), and (c) `True`. Also:
  `R_abcd R^abcd - 4 kappa^2 c^2 (th^2 - chi^2) = 0`; `T_ac^c - tau k_a = [0,0,0,0]`; third bracket `[0,0,0,0]`;
  `W_a n = lambda_a n: True`; `L + ... == 0: True`; `L^2 == 0: True`; (g) `[0, 0, 0, 0]`.
- `python -I -B s2_operator_exact.py` → for U2 and T1: residual sets `{0}`, `{0}`, and `T_ac^c - tau k_a = [0,0,0,0]`.
  At U2, F pair `{(1, 3): 7*kappa/10}`.
- `python -I -B s4_p0_cones.py` → (b) for U1 and U1z: `degree of D_r 40`, multiplicities `10, 2, 2, 2, 2, 2`,
  `remainder degree 0`.
- `python -I -B s5_landau_jblocks.py` → every block `remainder degree 0`, `leak 0e+00`. Totals for l <= 5:
  `{0: {-1: 5, 1: 5, 3: 10, 5: 10}, 1..5: {-1: 1, 1: 1, 3: 2, 5: 2}}` at both (kappa, p).
- `python -I -B s6_landau_untilted.py` → kernel = gauge (50 = 50). Counts per (class, l), l <= 5: class 0 has
  10/10/20/20 (12/12/24/24 at U2, where classes 0 and 1 coincide) and the other classes 2/2/4/4; Q is in class 0 only.
- `python -I -B s7_landau_tilted.py` → `unassigned 0` at T1 and T2; predicted-root distance ≤ 1.5e-7;
  T1 s^2 Lambda^2 = 0.36, 0.54 (real); p → 0 roots ±0.2, ±1.8, ±0.2449, ±2.2045.
- `python -I -B s3_survey_structure.py` → counts as quoted in the block.
- `python -I -B apply_and_build_r1.py --build` → pre hash matches, post hash `69ab958ad2af131bc0aa6c7074b1e2da9ab5572b2de708d89915777b7fe1740b`, labels defined 1,
  `BUILD CLEAN`, temp copy removed.

## Decisions Taken

- **D-1 (route).** Took the 072 review's rank-1 avenue (non-null-leg connections), aimed at a positive gap
  determination. I did not start from survey points as "solutions". I first extracted the structure (null line,
  legs) and derived an exact family, so that the linearisation sits on exact backgrounds, as the task asked.
- **D-2 (gap criterion).** The criterion used is a momentum-independent term in the characteristic equation in the
  conserved central momenta (q0, p), plus its sign and the zero-momentum and zero-frequency behaviour. This is the
  072 criterion ("no term independent of the momentum"), refined because a tilt produces such a term. I rejected
  "q0 ≠ 0 at p = 0" as a criterion: on shifted cones it already holds at s = 0 and has no mass meaning. The 071
  family (i) and the appH null-rotation background treat it as no gap.
- **D-3 (tilted numerics).** Square truncations with a convergence test were used, because the eigenfunctions are
  not polynomial × Gaussian. This is stated in the block, and no exactness is claimed for s != 0 Landau sectors.
- **D-4 (survey wording).** Counts are reported with tolerances. They are not a classification.
- **D-5 (Edit 2).** A one-clause update to the 072 sentence that would otherwise become stale.
- **D-6 (sign convention).** The 071/072 normalisation is used (first-order part E_a + ½ w S at u = 1;
  om = -w at operator level). Roots are given in the 072 form (q0 for e^{i q0 y^0}).

## Milestone assessment

Routine. No critical-path step is derived. The package is a bounded determination (no definite-sign gap on an
exact, wider class), with a new structural identity and a first momentum-independent term that is shown not to be
a mass.

## Status-label recommendation

The current critical-path list (ch17 + appH ledger) is A, B, C, D1, E, F, G-derived, N. All labels are unchanged.
D, F and N remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

**To close D1 at full scope (unchanged).** Derive local SO(3,1) and the locked frame from the matrix data, select
the class, and specify omega, A, B and the ghost operators together with their field content and propagating modes
(including norms).

**Ranked avenues for the torsion/Lorentz-mode gap.** The ranking is derivation-first: positive-aimed first, and
same-no-go-in-a-new-class last.

1. **Bilinear (mu^2) term of the conjugate-coordinate class** (appH L1527: "Ric_ab = -mu^2 eta_ab, the massive
   case"). Linearise the forty equations about the exact de Sitter solution with mu^2 = -3, built from E_{a4} on
   SO(4,1) (appH L1527). This background has an intrinsic invariant scale, where the 071/072 dilation and
   square-completion arguments do not apply, so it is the most likely within-core source of a definite-sign
   momentum-independent term.
2. **One loop on the tilted family.** Here Q = Q|_{w=0} exactly while the forty equations carry Lambda. The
   one-loop determinant (regulated trace, appH Hanada2006 regulator) could induce a non-derivative term for the
   torsion modes. Commutators are nonzero, so the cancellation of the commuting-matrix case does not apply.
3. **A pairing / Krein form** on the family. This would decide whether the real-Lambda branches (tachyonic-sign
   constant) or the rate classes are physical or gauge-null. The structure of Q as a Maxwell-like gauge-invariant
   operator is the natural starting point.
4. **Non-constant connections** on Heisenberg (not left-invariant), or other unimodular algebras (071 survey: R^2 != 0
   on algebras with a 2-dimensional abelian derived algebra, third bracket unexamined).
5. **Nonlinear** evolution of the real-Lambda zero-frequency crossings.
6. **(Bottom)** Further constant-connection families on Heisenberg. S3 indicates that the clean solutions are of this
   null-line form, so the likely outcome is the same bounded result.

**Open step O1.** Derive the Lambda set and the root formula analytically, through an operator-level triangular
(null-filtration) decomposition of the forty equations. This would make C6 exact.

**Transfer.** The exact identity Q = Q0 - tau k F and the null-line structure transfer to Problem N: a norm on these
backgrounds would act on a nilpotent non-derivative structure. They also transfer to Problem F: the w-dependence of
the second-order operator here is nilpotent, so any E-term from w on these backgrounds is nilpotent at tree level.

## Special instructions for the gatekeeper

- **Do not let the block assert a mass or a gap.** The s != 0 term s^2 Lambda^2 is explicitly "not a mass". Check
  the three supporting facts by hand from the displayed equation:
  - the square-completion;
  - the p → 0 roots -Lambda(1 ∓ c);
  - the zero-frequency crossing p^2 + (2c Lambda + kappa l)p = s^2 Lambda^2, which has exactly one positive root
    for real Lambda != 0.
- **Re-check the exact items independently:** the symbolic family (S1 (a), (b)); the Q identity (S1 (g)); the
  operator-level check (S2); the exact divisors (S4(b), S5).
- **The Lambda formula for general parameters is a numerical fit (C6), not derived.** The block says "numerical at
  sampled points otherwise". Verify that the block does not present it as exact beyond U1.
- **Survey numbers in the block come from S3's output.** Re-run S3 and confirm the counts and tolerances.
- **Full scan.** Edit 2 changes a scope clause of the 072 paragraph, so a full scan is owed under protocol 3(c).
- No status label change. No closure language. Problems D, F and N remain open.
