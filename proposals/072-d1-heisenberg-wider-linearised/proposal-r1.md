# Proposal 072-d1-heisenberg-wider-linearised, round 1

## Result

On the wider Heisenberg family of 071, w_a^{cd} = k_a(chi B + zeta N + x N')^{cd} on time x Heisenberg
([E_3,E_1] = kappa E_2), linearised in the Landau sectors (E_0 = i q0, E_2 = i p, E_1, E_3 oscillator):

1. **Order-zero operator, exact.** For a constant connection F_ab[A] = E_aA_b - E_bA_a - c_ab^d A_d has no w, and on
   this family Q_b[A] = Q_b[A]|_{w=0} - chi k^a F_ab[A] for all zeta, x and every A (sympy, arbitrary functions).
   So Q does not depend on zeta, x. The connection adds only a gauge-invariant first-order term along the null k.
   On the 068 mode A = (0, phi, 0, i phi): Q_b[A] = (q0^2 - p^2 + kappa p + i chi (q0 - p)) A_b (exact).
   Q agrees with the linearised third bracket of the literal bundle operators, order-zero part included (exact
   rational evaluation at a sample point, two parameter sets).
2. **Spectrum of the forty equations.** Every characteristic root lies on
       (q_par + (i/2) c chi k)^2 + kappa p l = 0,  i.e.  q0^2 - p^2 + i c chi (q0 - p) = kappa p l,
   with c in {-1, 1, 3} and l in {-1, 1, 3, ...}. Per level l >= 3 there are 10, 6 and 4 quadratic factors for
   c = 1, 3, -1 (20 in all, as at chi = 0); at l = +-1 there are half as many. Q has c = 1, and the c = 1 class has
   five times Q's multiplicities.
   - Exact over QQ(i) in all J-blocks J = -2..3 at zeta = x = 0, at (kappa,p,chi) = (1,1/2,1/2) and (2,1/4,-1/3).
   - Numerical at zeta, x != 0, and in the p = 0 sector, where the roots lie on the cones (q + (i/2) c chi k)^2 = 0.
   - The kernel at generic q0 is exactly the gauge directions.
3. **No gauge-invariant gap or mass, and no sign.** chi, zeta and x shift no Landau level: kappa p l are the 068
   values. chi enters only as the imaginary null shift (i/2) c chi k of the longitudinal momentum, a term linear in
   k^a q_a. This holds although the background has the scale kappa and R_abcd R^abcd = -4 chi^2 kappa^2 != 0.
4. **The 068 growing mode persists, modified.** The roots are q0 = -(i/2)c chi +- ((p + (i/2)c chi)^2 + kappa p l)^{1/2}.
   - For chi != 0 no root is real at p > 0, and both signs of Im q0 occur.
   - For l >= 1, |Im q0| < |c chi|, and |c chi| is approached as p -> infinity.
   - For l = -1, max |Im q0| = |c chi|/2 + sigma_c with sigma_c = kappa/4 + sqrt(kappa^2/16 + c^2 chi^2/4), attained
     at p = sigma_c (by hand).
   - For the 068 mode (c = 1) the bound Gamma <= kappa/2 is replaced by |chi|/2 + sigma_1 > kappa/2, and growth is
     no longer confined to 0 < p < kappa. The overall largest rate is 3|chi|/2 + sigma_3.
   - These are section values without a norm, so no stability claim is made.
5. **Where a gap could come from (avenue indicator, numerical survey).** On the Heisenberg algebra, constant
   connections with eta^{ab} w_a^{cd} w_b^{ef} != 0 also solve all three brackets: 116 of 120 norm-constrained
   starts, 94 of them with R^2 > 0. This w^2 form vanishes identically on the wider family because k is null.

This is a bounded negative result for a gap on this family at tree level and linear order. Problem D stays OPEN.

## Target and status

- Problem D, `\section{Problem D: local Lorentz}` (appH L715). Ledger: Status OPEN; Priority CRITICAL PATH;
  Completion PROGRAMME-CONDITIONAL; reduced-scope D2 does not close D (appH L718-722).
- ch17 D1 (L330-342, L650-653, L712-717): derive local SO(3,1) from the matrix algebra and condensate, specify the
  omega, A_mu, B and ghost operators and the field content, and derive the locked frame and its non-degeneracy.
- Missing step (appH L745-756): among other things, "derive the effective dynamics of the independent diagonal
  connection or retain it as unresolved field content. Generator counting alone does not settle its torsion or
  propagating modes."
- This package addresses the torsion/propagating-mode content of the first-order equivariant class on the first
  background in the class that has a scale and no known boost-dilation symmetry.
- Dependencies: 068 (L1609-1629), 071 (L1631-1646), the class definition (L1513-1533) and the pairing paragraph
  (L1535-1572).
- Classification: PROGRAMME-CONDITIONAL; the result is conditional on the class and backgrounds. No discrepancy found
  between appH and ch17 for D1.

## Source reading

Digest + targeted reads. `make_digest.py --check` printed DIGEST CURRENT (dirty-chapters: yes, but the digest is
current with the working tree). Read in full:
- appH L715-760 (D ledger label and missing step);
- appH L1513-1646: class definition, flat-space pairing, one loop and reflected form, compact toy, locked-frame
  composite, the 068 paragraph and the 071 paragraph;
- ch17 L330-345, L645-655, L708-718.

The rest of Section D (L760-1495) was not re-read in full; it is not cited or edited here. Also read: 071
review-r2.md and review-r4-final.md, the 071 code (bg.py, lin.py, core068.py, x2, x3, s2_linearised_r2) and the
068 code (core.py, tools.py, s3_heisenberg_landau.py). No full scan is claimed.

## Research and reasoning

**Set-up.** Normalisation and code follow 071, imported read-only with no bytecode written (`common.py`):
- first-order part E_a + 1/2 w S at u = 1, with the literal L1519 omega = -w;
- the fluctuation D_a -> D_a - h_a^c D_c + 1/2 omega_a^{cd} S_cd;
- M_op from core068, Q from lin.Qop, and the gauge vectors (with the curvature term) from lin.gauge_vectors_R.

Landau sectors: E_0 = i q0, E_2 = i p with p > 0; E_1 = s(a - a^dag) and E_3 = -i s(a + a^dag) with s^2 = kappa p/2.
Roots are values of q0 where the rank drops below generic. The 068 device (columns at levels <= L, rows on all
levels) means no truncation defect enters the columns used. The equations have real coefficients, so sector -p is
the complex conjugate (q0 -> -conj q0), with the same |Im q0|.

**(a) Q, by hand and exact.** With nabla_a A_b = E_a A_b + Om_ab^c A_c and T = -c - Om + Om^T, the Om terms cancel in
F_ab = nabla_a A_b - nabla_b A_a + T_ab^c A_c, which leaves E_aA_b - E_bA_a - c_ab^c A_c. So Q = nabla^a F_ab - T F
is affine in Om. The exact form of the w-part, -chi k^a F_ab[A], is verified symbolically for arbitrary functions
A_b(y) (s1 part D). It is gauge invariant, since F is. Contracting with the ground mode, where k^a A_a = 0 and
k^a E_a = i(p - q0), gives the eigenvalue q0^2 - p^2 + kappa p + i chi(q0 - p) (s1 part A, symbolic in all four
parameters). Part B builds the literal bundle vector fields (L1519 form, t_a = half the divergence, order-zero
fluctuation -i eps u_a^b A_b). It finds the O(eps) multiplication part of sum_a eta^{aa}[D_a,[D_a,D_b]] equal to
-i eps Q_b[A], with residual 0 in rational arithmetic. So lin.Qop is the linearised third bracket on this family.

**(b) Forty equations.**
- *J-conservation (ζ = x = 0).* J = n + (helicity in the 1-3 plane), with the helicity read from i rho(R_13) on the
  40 components (s3; [M, J] = 0 checked).
- *Exact recipe in each J-block.* Rescale the oscillator basis (|n>' = sqrt(n!)|n>) to obtain Gaussian-rational
  entries. Reconstruct rationals with an asserted residual below 1e-10. Compress twice with random integer matrices
  to the generic rank r, take the determinants by exact interpolation, and take the gcd. Every r x r minor is
  divisible by the determinantal divisor D_r, so the gcd is a multiple of D_r. Hence every characteristic root (a
  zero of D_r) is a zero of the gcd.
- *Exact result.* The gcd factors completely into the P_{c,l}, with remainder degree 0 in every block J = -2..3 at
  both rational points. So in these blocks there are no other roots, exactly. The leak of each block into other
  rows is 0.
- *Multiplicities.* The totals over J for l <= 5 are (c=1: 5,5,10,10), (c=3: 3,3,6,6), (c=-1: 2,2,4,4) at
  l = -1, 1, 3, 5. They match the numerical root counts (s2 (c)). At chi = 0 they give 10, 10, 20, 20, the 068
  counts.
- *Numerical at ζ, x ≠ 0 (s2 (c)).* Three points: the roots fit c to integers within 1e-4. The only unclassified
  roots sit at l = 11, at the column cut. At chi = 0 with zeta, x != 0 (family (ii)) the 068 levels are recovered;
  the roots split by ~1e-3 there, which is consistent with chains.
- *Sector p = 0 (s5).* Characters q = (q0, q1, 0, q3): alpha/(-i chi/2) = c in {-1, 1, 3} with 8/20/12 of 40
  roots, and Q at c = 1.
- *Kernel (s2 (a)).* At generic complex q0 the kernel is exactly the span of the gauge directions, 10 per parameter
  level (50 for L = 5).
- *Labels (s2 (b)).* The central frame labels I = 0, 2 map to Q: h = -f delta_I, omega = -f w_I gives
  (Qf delta_I, -Qf w_I), with residual 2e-15.

**(c) Gap question (F3).** A gap would be an isolated q^2 in the gauge-invariant characteristic spectrum, or a
gauge-invariant discrete Landau-level shift. Neither occurs:
- the levels kappa p l are exactly those of chi = 0;
- the only chi-dependence is i c chi k^a q_a, linear in the momentum and purely imaginary for real q;
- in the p = 0 sector the cones (q + (i/2)c chi k)^2 = 0 carry no isolated q^2, since k^a q_a ranges over C.

In the order-zero sector gauge invariance of Q forbids a mass term outright. The only possible change is through F,
and on this family it is -chi k^a F_ab.

**(d) Growth, by hand.** With gamma = c chi/2 and Z = (p + i gamma)^2 + kappa p l, let sqrt Z = X + iS. Then
X S = gamma p and X^2 - S^2 = p^2 - gamma^2 + kappa p l, and Im q0 = -gamma +- S.
- *l >= 1.* If S >= |gamma|, then gamma^2 p^2/S^2 - S^2 <= p^2 - gamma^2 < p^2 - gamma^2 + kappa p l, a
  contradiction. So S < |gamma| and |Im q0| < 2|gamma| = |c chi|. Both roots have Im q0 of sign -c chi, and S ->
  |gamma| as p -> infinity.
- *l = -1.* Maximise S on f = gamma^2 p^2/S^2 - S^2 - p^2 + gamma^2 + kappa p = 0. Setting df/dp = 0 gives
  p = kappa S^2/(2(S^2 - gamma^2)). Substitution gives (S^2 - gamma^2)^2 = kappa^2 S^2/4, so
  S = kappa/4 + sqrt(kappa^2/16 + gamma^2) = sigma_c, attained at p = S (s1 C symbolic; s6 grid). At the boundaries
  p -> 0 and p -> infinity, S -> |gamma| < sigma_c.
- *No real root at p > 0.* A real root needs S = |gamma|. For l >= 1 that is excluded above. For l = -1 the
  constraint gives kappa p = 0.
- *Bounds.* max |Im q0| = |gamma| + sigma_c. At chi = 0 this is kappa/2 at p = kappa/2, the 068 bound. The overall
  maximum is c = 3: 3|chi|/2 + sigma_3, which exceeds 3|chi| (the l >= 1 supremum). Both signs of Im q0 occur
  (classes c = 1, 3 versus c = -1).

**(e) Why the wider family cannot gap at this order (structural pointer).**
- *Where w enters.* With w_a = k_a M, k null and k^a only along the central E_0, E_2, the w^2 part
  eta^{ab} w_a w_b of nabla^a nabla_a vanishes. In Q, w enters only linearly (exact).
- *The forty equations.* They are not affine in w: the second difference is nonzero. It squares to zero at sampled
  points, which is an observation only. Their roots are nonetheless shifted only linearly (b).
- *Survey on the Heisenberg algebra (s4).* With w free and the norm |w|^2 constrained to 1/4, 1 or 4, the survey
  finds solutions of all three brackets with eta^{ab} w_a^{cd} w_b^{ef} != 0: 116 of 120 starts, 94 with R^2 > 0,
  4 with R^2 < 0, 18 with |R^2| <= 1e-8, and 29 with a trace of T. G != 0 is invariant under constant Lorentz
  rotations, so these are not in the orbit of any null-leg connection. They are the only backgrounds found in the
  class where a real w^2 term enters the second-order operator.

**Literature.** No new citation. Reference is made only to merged statements: the Nielsen-Olesen comparison and
Furuta-Hanada-Kawai-Kimura are already in L1627 and L1529 and are not repeated.

**Comparison with the original target.** D1 requires the dynamics or field content of the connection, including
torsion and propagating modes. Here, on one more background family, the torsion and Lorentz modes stay gapless at
tree level and linear order, and the growing mode persists. Nothing derives SO(3,1), the frame, or its
non-degeneracy.

## Claim classification

| # | Claim | Class |
|---|---|---|
| 1 | F_ab[A] contains no w for constant connections; Q affine in w | established (by hand) |
| 2 | Q_b = Q_b w=0 - chi k^a F_ab, independent of zeta, x, for all A | established (exact symbolic) |
| 3 | Ground-mode eigenvalue q0^2 - p^2 + kappa p + i chi(q0-p) | established (exact symbolic) |
| 4 | lin.Qop equals the literal linearised third bracket on this family | established at sampled point (exact rational evaluation, polynomial A) |
| 5 | Roots of the forty equations on P_{c,l}, c in {-1,1,3}; counts 10/6/4 (5/3/2 at l=+-1) | exact in J-blocks J=-2..3 at two rational points (zeta=x=0); numerical otherwise |
| 6 | Same values/counts at zeta, x != 0; p = 0 cones; family (ii) recovers 068 levels | numerical |
| 7 | Kernel at generic q0 = gauge directions; central labels reduce to Q | numerical |
| 8 | No gauge-invariant gap/mass on this family at tree level, linear order | conditional (follows from 2, 5, 6 within the stated hypotheses) |
| 9 | Root formula, no real root at p>0, |Im q0| bounds, sigma_c and its location | established (by hand) given 5; checked numerically |
| 10 | Growth in section values; no stability claim | conditional; no norm |
| 11 | Heisenberg constant connections with eta w w != 0 solve all three brackets | numerical survey, not a classification |
| 12 | Selection of the class/background by the matrix integral, frame, non-degeneracy | unresolved |

## Proposed changes

### File `chapters/appH-microscopic-proofs.tex`

**Edit 1 (insert).**
- Placement: a new paragraph immediately before the unique line `\section{Problem E: signature}` (currently L1648).
  It follows the closing paragraph of the 071 paragraph, which begins `These statements are for
  Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and no matter term, tree level, the Lorentzian
  contraction, left-invariant backgrounds with constant connection` and ends `Problems~D, F and~N remain open and
  PROGRAMME-CONDITIONAL.`
- The block is followed by one blank CRLF line.
- Nothing is removed.
- The block, byte for byte, is `appH_insert_r1.tex`: CRLF, UTF-8 without BOM, 6106 bytes, sha256
  3dbdc81ddd65079a970cd516da5fef294f10356bcee764a0ababaa1edeb69a98. It is generated by `make_insert_r1.py`.

```latex
\paragraph{First-order equivariant class on the Heisenberg background with curvature: Landau sectors of the linearised equations (conditional; not closure).}
Take the wider ansatz \(w_a{}^{cd}=k_a(\chi B^{cd}+\zeta N^{cd}+xN'^{cd})\) of the preceding paragraph on time times the Heisenberg group, with its normalisation and the fluctuation \(\mathbb D_a\to\mathbb D_a-h_a{}^c\mathbb D_c+\tfrac12\omega_a{}^{cd}\mathcal S_{cd}\), in the sectors of the paragraph on left-invariant backgrounds with torsion: \(E_0=\mathrm iq_0\), \(E_2=\mathrm ip\) with \(p>0\), and \(E_1\), \(E_3\) acting on oscillator levels. The linearised equations have real coefficients, so the sectors with \(p<0\) follow by complex conjugation. For a constant connection \(\mathsf F_{ab}[A]=E_aA_b-E_bA_a-\mathsf c_{ab}{}^dA_d\) contains no \(w\), and on this family
\[
\mathcal Q_b[A]=\mathcal Q_b[A]\big|_{w=0}-\chi\,k^a\mathsf F_{ab}[A]
\]
for all \(\zeta,x\) and all \(A\) (exact), so the connection adds only a gauge-invariant term of first order along the null \(k\). On \(A=(0,\phi,0,\mathrm i\phi)\), with \(\phi\) as in that paragraph, this gives \(\mathcal Q_b[A]=\bigl(q_0^2-p^2+\kappa p+\mathrm i\chi(q_0-p)\bigr)A_b\) (exact). The operator \(\mathcal Q\) agrees with the linearised third bracket of the operators on the bundle, order-zero part included (exact at a sampled point for polynomial \(A\), at two parameter sets). With \(q_\parallel=(q_0,0,p,0)\), every characteristic root of the forty equations in these sectors, a value of \(q_0\) at which their rank drops below its generic value, satisfies
\[
\bigl(q_\parallel+\tfrac{\mathrm i}2c\chi k\bigr)^2+\kappa p\,l=0,\quad\text{that is}\quad q_0^2-p^2+\mathrm ic\chi(q_0-p)=\kappa p\,l,\qquad c\in\{-1,1,3\},\ l\in\{-1,1,3,\dots\}.
\]
For \(l\ge3\) the numbers of these quadratic factors are \(10\), \(6\) and \(4\) for \(c=1,3,-1\), twenty in all as at \(\chi=0\), and half of these at \(l=\pm1\); \(\mathcal Q\) has \(c=1\), and the class \(c=1\) has five times its multiplicities (numerical, at sampled \(\kappa,\chi,p\)). At \(\zeta=x=0\) a rotation of the \(1\)-\(3\) plane combined with the oscillator level is conserved, and in each of its blocks \(J=-2,\dots,3\), which contain all factors with \(l\le5\), the greatest common divisor of two random compressions of the maximal minors, which every characteristic root annuls, is exactly the product of these factors at \((\kappa,p,\chi)=(1,\tfrac12,\tfrac12)\) and \((2,\tfrac14,-\tfrac13)\) (exact in rational arithmetic). For \(\zeta,x\neq0\) the same values and counts appear for \(l\le5\), and in the sector \(p=0\), where \(E_1\) and \(E_3\) commute, the roots lie on the complex cones \((q+\tfrac{\mathrm i}2c\chi k)^2=0\) with the same \(c\) (numerical, at sampled points). The kernel at generic \(q_0\) is the ten gauge directions for each level of the parameter, and the frame labels along \(E_0\) and \(E_2\) reduce to \(\mathcal Q\) as on family~(i) (numerical). At \(\chi=0\) this gives the levels \(q_0^2=p^2+\kappa p\,l\) of the paragraph on left-invariant backgrounds with torsion for every \(\zeta,x\) (numerical).

So \(\chi\), \(\zeta\) and \(x\) shift no level: the values \(\kappa p\,l\) are those at \(\chi=0\), and \(\chi\) enters only through the imaginary null vector \(\tfrac{\mathrm i}2c\chi k\) added to \(q_\parallel\), whose contribution \(\mathrm ic\chi\,k^aq_a\) is linear in the momentum. No gauge-invariant gap or mass therefore appears for the Lorentz or torsion modes at this order, although the background carries the scale \(\kappa\) and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4\chi^2\kappa^2\neq0\), and no sign of a mass arises. The roots are \(q_0=-\tfrac{\mathrm i}2c\chi\pm\bigl((p+\tfrac{\mathrm i}2c\chi)^2+\kappa p\,l\bigr)^{1/2}\). For \(\chi\neq0\) none is real at \(p>0\), and their imaginary parts have both signs; for \(l\ge1\), \(|\operatorname{Im}q_0|<|c\chi|\), with supremum \(|c\chi|\) as \(p\to\infty\); for \(l=-1\) the largest value of \(|\operatorname{Im}q_0|\) is \(\tfrac12|c\chi|+\sigma_c\) with \(\sigma_c=\tfrac\kappa4+(\tfrac{\kappa^2}{16}+\tfrac14c^2\chi^2)^{1/2}\), attained at \(p=\sigma_c\) (by hand, checked numerically). For \(c=1\) this is the mode \(A\) above: the growing mode of the paragraph on left-invariant backgrounds with torsion persists at \(\chi\neq0\), its largest rate rises from \(\kappa/2\) to \(\tfrac12|\chi|+\sigma_1>\kappa/2\), and the growth is no longer confined to \(0<p<\kappa\). Over all modes the largest rate is \(\tfrac32|\chi|+\sigma_3\). These are section values and no norm is used, so, as for family~(i), no statement on stability is made.

These statements are for Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and no matter term, tree level, linear order in the fluctuation, the Lorentzian contraction and the wider family on time times the Heisenberg group with constant connection, in the sectors named. A norm, the nonlinear evolution of the growing modes, loops, for which the cancellation at second order about commuting matrices does not apply since the commutators of this background are nonzero, the solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) of the survey of the preceding paragraph, the regulated trace and the domains of the unbounded operators are not treated. On the Heisenberg algebra, constant connections with \(\eta^{ab}w_a{}^{cd}w_b{}^{ef}\neq0\), a form that vanishes on the wider family since \(k\) is null, also solve all three brackets, most of them with \(\mathsf R_{abcd}\mathsf R^{abcd}>0\) (numerical survey, not a classification); they are not linearised here. Nothing here shows that the matrix integral selects this class, these backgrounds or the algebra \(\mathcal A\), or yields the frame and its non-degeneracy, so Assumptions~\ref{ass:frame-lock}, \ref{ass:nondeg}, \ref{ass:lorentzian}, \ref{ass:local-lorentz} and~\ref{ass:EFT-a2} are not discharged, and the frame of these backgrounds is not identified with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
```

**Edit 2 (stale passage in the 071 closing paragraph, currently L1646).**
- Context: after Edit 1 the sentence "Family (ii), its extension with \(\chi\neq0\) and the survey solutions ... are
  not linearised here" is stale for family (ii) and its extension.
- Replace the unique string (it occurs once):
  `Family (ii), its extension with \(\chi\neq0\) and the survey solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\), for which no scaling symmetry is shown, are not linearised here, and`
- with:
  `Family (ii) and its extension with \(\chi\neq0\) are linearised in the following paragraph; the survey solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\), for which no scaling symmetry is shown, are not linearised here, and`
- The rest of that paragraph is unchanged.

**Hashes and labels.**
- Pre-hash of the live appH: b98a3a34d2ac71800ceae7369db90d373d8bcdc139fe7fb81e7bad3e552df1c0.
- Post-hash after both edits: ae6c95cdb240188807e403fc23ed5240a7cf8fdfef853ba3be6830974f844fa3 (759245 bytes, bare LF 0).
- Labels referenced in the block, each defined exactly once: eq:Smatrix, ass:frame-lock, ass:nondeg,
  ass:lorentzian, ass:local-lorentz, ass:EFT-a2, ch:vierbein-emergence.
- No new labels and no citations, so no bibliography change.
- The block contains one status sentence ("remain open"), in its last paragraph.

No other stale passage was found:
- L1627 (the 068 Q levels) is a chi = 0 statement and remains correct.
- L1644, the family (i) no-mass result, is unaffected.

## Verification scripts

All scripts are in `proposals/072-d1-heisenberg-wider-linearised/`. Run them from that folder with `python -I -B`;
`-B` and `sys.dont_write_bytecode` keep the read-only 071/068 folders free of bytecode.

| Script | Checks | Expected invariant output |
|---|---|---|
| `common.py` | set-up; imports 071 `core068`, `tools068`, `bg`, `lin` read-only | n/a |
| `s1_Q_exact.py` (~30 s) | A: ground-mode eigenvalue, symbolic; B: literal bundle operators vs Q; C: sigma_c stationary point and grid; D: Q - Q_{w=0} + chi k^a F_ab = 0 for arbitrary A | `[0, 0, 0, 0]`; `F_32[A] / phi = p`; both B lines `0.0e+00 ; ... 0.0e+00`; C `0 0` and grid = closed form (0.853553 at kappa=1, chi=+-0.5; 1.240388 at kappa=1.3, chi=0.8; 0.500000 at chi=0); D `[0, 0, 0, 0]`, `F_ab[A] contains no w: True` |
| `s2_numeric_spectrum.py` (~2.5 min) | (a) background brackets, kernel = gauge; (b) central labels; (c) root classes; (d) Q; (e) w-second difference | (a) kernel dim 50 = gauge 50, rank 50; (b) residuals ~2e-15; (c) every chi != 0 case gives `{(-1,-1):4,(-1,1):4,(-1,3):8,(-1,5):8,(1,-1):10,(1,1):10,(1,3):20,(1,5):20,(3,-1):6,(3,1):6,(3,3):12,(3,5):12}` (roots counted, two per factor), with unclassified roots only at l ~ 11 and the family (ii) case giving `{(0,-1):20,(0,1):20,(0,3):40,(0,5):40}`; (d) `|Q(zeta,x) - Q(0,0)| = 0e+00` and counts at c = 1 |
| `jblocks.py` | exact helpers: helicity basis, rescaled oscillator, rational reconstruction, compressions, interpolation, gcd | n/a |
| `s3_exact_jblocks.py` (~7 min) | exact D_r factorisation per J-block at three rational points | every line `remainder degree 0` and `leak 0e+00`; forty totals `{(-1,-1):2,(-1,1):2,(-1,3):4,(-1,5):4,(1,-1):5,(1,1):5,(1,3):10,(1,5):10,(3,-1):3,(3,1):3,(3,3):6,(3,5):6}` at both chi != 0 points; at chi = 0 `{(0,-1):10,(0,1):10,(0,3):20,(0,5):20}`; Q totals `{(1,-1):1,(1,1):1,(1,3):2,(1,5):2}` |
| `s4_heisenberg_survey.py` (~4 min) | non-null-leg solutions on the Heisenberg algebra | `converged 120 of 120`; `non-null leg ... 116`; `RR > 1e-8: 94, RR < -1e-8: 4, ... 18; |trace T| > 1e-8: 29; max |third bracket| 2.5e-14` (seeded) |
| `s5_p0_sector.py` (~20 s) | p = 0 cones | forty: `-1 x8, 1 x20, 3 x12`; Q: `1 x4` at every line |
| `s6_growth.py` (~10 s) | growth bounds for all c, l | l=-1 maxima = closed form at p = sigma_c; l >= 1 `True`; overall max = `3|chi|/2 + sigma_3` (1.790569 at kappa=1, chi=+-0.5); signs `[-1, 1]` |
| `make_insert_r1.py` | writes the CRLF block | `bytes 6106 sha256 3dbdc81d... bare LF 0` |
| `apply_and_build_r1.py [--build]` | pre/post hash, anchors, labels; build on a temporary copy outside the repository | pre match True; post `ae6c95cd...`; `BUILD CLEAN`, 416 pages, 0 undefined/multiply-defined; temp copy removed |

Saved outputs are the `*_output.txt` files.

## Decisions Taken

- **Target variant.** Two other options were considered: a symbolic J-block determinant, which was too slow, and
  numerics only. I used exact J-block factorisation at rational points plus numerics. This gives exact control of
  "no other roots" at ζ = x = 0, which is the claim that bears on a gap.
- **Classification of the ζ, x ≠ 0 case.** It is kept numerical. An exact argument (gauge equivalence or a
  triangular boost-weight grading) was not established. The constant null rotations do not preserve the Heisenberg
  structure constants, so they are not an available gauge map.
- **The non-null-leg survey goes into the insert as one bounded sentence.** It points to the only place a real
  w^2 term can enter. That is the derivation-first lead for a gap, and a scope sentence without it would hide the
  avenue. It is marked as a numerical survey, not a classification.
- **No χ-sign statement on time direction beyond "both signs".** Without a norm a preferred time orientation is
  not meaningful here.
- **Stale sentence (Edit 2).** I chose the minimal replacement over rewriting the 071 paragraph.

## Milestone assessment

Routine. This is a bounded result: no gap or mass on one more background family, the growing mode modified, and a
survey lead. No critical-path step is derived from the matrix theory.

## Status-label recommendation

From ch17 L645-718 and the appH ledger, the critical path is A, B, C, D1, E, F, G-derived and N. The appH ledger has
11 problems, all OPEN: 8 CRITICAL PATH (A, B, C, D, E, F, G, N) and 3 OPTIONAL (H, I, J). The affected labels are
D, F and N. Unchanged: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No label change is proposed.

## Author decision needed

None.

## Remaining open step

D1 closure still requires:
- deriving local SO(3,1) and the class from the matrix integral;
- deriving the locked frame and its non-degeneracy;
- the effective dynamics of the connection, including whether its torsion modes are massive.

This package bounds the last item on one more family.

**Forked avenues, ranked derivation-first.**

1. **Linearise the Heisenberg backgrounds with eta^{ab} w_a w_b != 0 (s4) in Landau sectors.** Positive-aimed:
   this is the only background class found where a real w^2 term enters the second-order operator, so a real,
   gauge-invariant shift of the Landau levels, that is a gap with a sign, is not excluded.
   - Method: the connection components along E_1 and E_3 displace the oscillator, so the column-cut device misses
     roots. Use a displaced (coherent) basis or a symmetric truncation with convergence in N.
   - Pick survey points with R^2 > 0 and trace T = 0 first.
2. **One loop about the Heisenberg family.** The second-order cancellation of L1577-1581 needs commuting
   backgrounds; here the commutators are nonzero, so an induced mass term on the labels is not excluded. It is
   positive-aimed but heavy, and needs the supplied content and a regulator.
3. **A pairing or norm on these modes.** Use the trace form or the reflected form of L1585-1595. The question is
   whether the imaginary null shift is growth in a norm or a non-unitary similarity. This matters for N (ghosts)
   and for the stability reading.
4. **Nonlinear evolution and condensation of the growing modes.** This is the Nielsen-Olesen analogy, already cited
   at L1627. It could select a different background, possibly one in avenue 1. It needs an energy or regulated
   trace, which is upstream (the regulated trace and the action at L1523).
5. **Non-constant connections and non-left-invariant backgrounds.**
6. **Bottom of the list.** Other families with a null connection leg along central directions (e.g. other
   unimodular algebras with w_a = k_a M). The expected outcome is the same imaginary null shift, so this is not
   proposed next.

**What transfers.**
- Problem F: the torsion and Lorentz modes stay gapless at tree level on this family, so the truncation question of
  Section ch17-bearing is unchanged.
- Problem N: the growing modes are first-order-in-time growth in section values, not an Ostrogradsky statement.

## Special instructions for the gatekeeper

- Do not let the text assert a gap, a mass, stability or instability. Growth is in section values without a norm.
- "Every characteristic root" is exact only in the J-blocks J = -2..3 at the two rational points with ζ = x = 0. It
  is numerical elsewhere, including ζ, x ≠ 0 and p = 0. Check that the insert's parentheticals say so.
- Re-check the exactness logic of s3. The gcd of two compressions is a multiple of D_r, so "all roots are on the
  P_{c,l}" is exact. Equality with D_r, and hence the multiplicities, is supported by agreement with the numerical
  counts.
- Re-check the by-hand growth derivation (Research (d)) and the claim that no root is real at p > 0.
- Re-check that Q = Q|_{w=0} - chi k^a F_ab is gauge invariant and contains no mass term (s1 D).
- The survey (s4) is seeded and numerical; the third bracket uses F = -c t for constant section values (071 by
  hand). It must stay "not a classification".
- Hashes: pre b98a3a34..., post ae6c95cd...; the build was on a copy outside the repository.
