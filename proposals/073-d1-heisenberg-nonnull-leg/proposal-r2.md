# Proposal 073-d1-heisenberg-nonnull-leg, round 2

## Result

The mathematics is unchanged from round 1. `s1_family_exact.py` was re-run under `python -I -B`, and its output is
identical to r1 apart from timings (`s1_family_exact_output_r2.txt`). This round makes the following changes.
- It applies the gatekeeper's S1-S3, F4 and F6 to the manuscript block.
- It adopts the optional F6 renaming. The tilt becomes (sin phi, cos phi), and the class shift Lambda becomes varpi.
- It corrects the S7(e) column-cut counts in the proposal text (F3).
- It re-ranks the avenues to match the review.
- It narrows one block sentence (N1). The tilted-point gauge-kernel claim is restricted to the oscillator levels
  <= 5 that S7(a) actually tests, because that check uses the column cut.

Summary of the result, which is unchanged:

On time x Heisenberg, in the first-order equivariant class with constant connection at tree level, this package
gives an exact family of solutions with non-null legs. It also gives the characteristic structure of the forty
linearised equations on that family.

1. **Exact family (symbolic).** w_a = k_a(chi B_n + th J_n) + P_a N_e + Q_a N_f, with
   - the null line n = (1, sin phi, -cos phi, 0);
   - P = zeta k + al e + (be+th) f and Q = x k + be e + ga f;
   - the constraint th^2 - 2 th be - 2 be^2 - al^2 - ga^2 + 2 chi(al+ga) = 0;
   - tau := chi + al + ga = 0 when sin phi != 0.

   Its invariants are:
   - R_abcd R^abcd = 4 kappa^2 cos^2 phi (th^2 - chi^2);
   - T_ac^c = tau k_a;
   - the third bracket holds;
   - every w_a fixes the null line n;
   - the vector leg operator eta^{ab} W_a W_b is nilpotent of order 2.
2. **Exact identity.** Q_b = Q_b|_{w=0} - tau k^a F_ab on the whole ansatz.
3. **Characteristic structure.** This is exact at rational untilted points and numerical elsewhere. Every root
   satisfies (q_par + varpi k_par)^2 + kappa p l = 0, with k_par = (1, 0, cos phi, 0). varpi lies in the six-member
   set displayed in the block, and the Landau levels are unshifted.
4. **Gap decision.** At phi = 0 there is no momentum-independent term. At sin phi != 0 the term
   varpi^2 sin^2 phi appears, but it does not give a gap. It is the term -varpi^2 k_par^2 of the square and vanishes
   with sin phi. Its p -> 0 limits are non-real for non-real varpi, and have the same sign for real varpi != 0. For
   real varpi each branch crosses zero frequency at a unique p > 0.

This is a bounded result on this family at tree level and linear order. It is not a no-go for D1, and no closure is
claimed.

## Response to review r1

| finding | action |
|---|---|
| F1 MAJOR (gap argument convention-laden; non-real Lambda; numerical root formula) | **S1 applied**, with only the F6 symbol substitutions (listed below). The new wording covers non-real varpi ("not real when varpi is not real"). It replaces "sign opposite to a mass term" by the convention-free "same sign, unlike the pair ±m of a mass". It marks the zero-crossing as "by hand from the displayed equation", and it drops "of definite sign". New exact check `s8_root_algebra_r2.py` verifies each by-hand step from the display: square identity, p = 0 roots and their product, the q0 = 0 equation and the product of its p-roots. |
| F2 minor (multiplicities only at s = 0, l <= 5) | **S2 applied**, with substitutions (below). |
| F3 minor (S7(e) counts wrong) | **Corrected in the proposal text (R3 below).** T1: 109 roots, of which 108 are in class 0 and 1 is unassigned. T2: 115 roots, of which 108 are in class 0, 1 is in class i chi (class 1), and 6 are unassigned. These are the gatekeeper's numbers, and they agree with the printed S7 output (`(e) column cut: 109 roots, per class [108, 0, 0, 0, 0, 0]` and `115 roots, per class [108, 1, 0, 0, 0, 0]`). I chose to state that the column cut is **not a valid test at s != 0**, and I did not add an N-dependence test (reason in R3). The block never relied on the cut at s != 0. |
| F4 minor | **Applied**: "positive for \(\cos\varphi\neq0\) and \(\|\vartheta\|>\|\chi\|\)". Under the rename, c != 0 becomes cos phi != 0. |
| F5 minor ("so" presents O1 as derived) | **S3 applied**, with substitutions (below). |
| F6 minor (delta_0; rename) | **Applied in full.** \(\delta_0^a=(1,0,0,0)\) is defined. The tilt (s, c) becomes (sin phi, cos phi), and Lambda becomes varpi (details below). |
| (consequence of F3) | **N1, a narrowing of one block sentence.** The kernel claim at the tilted point rests on the cut restricted to levels <= 5 (S7(a)). The sentence now reads "The kernel at generic \(q_0\) is the ten gauge directions for each level (numerical; at \(\varphi=\arcsin\tfrac35\) among the fluctuations of oscillator level at most \(5\))." This is the only block change beyond S1-S3, F4 and F6, and it narrows a claim. |
| Scope / avenues | **Re-ranked** to the review's order (Remaining open step). |
| Full scan (3(c), Edit 2) | Still owed by the gatekeeper. Edit 2 is unchanged. |

### Exact F6 renaming and the adapted snippets

**Rename rule.**
- s → \(\sin\varphi\), c → \(\cos\varphi\), \(\Lambda\) → \(\varpi\).
- "For \(s^2+c^2=1\)" → "For an angle \(\varphi\)", and \(\delta_0^a=(1,0,0,0)\) is added to the definitions.

**Why varpi.**
- In this appendix \(\Lambda\) is the gauge parameter of the class paragraph, which the forty equations' gauge
  directions use.
- \(\sigma\) is an index elsewhere in appH, and \(\Xi\) and \(\Upsilon\) are used in the Problem D and N sections.
- \(\varpi\) occurs nowhere in appH L1500-1663. Its only appH use is a different constant in Problem F (L2967-2979).
- \(\rho\) is kept. Its only nearby use is the spinor representation \(\rho(u)\) in the class paragraph, which
  always carries its argument. The gatekeeper did not flag it.

**Where sin phi = 0 became phi = 0.** In r1, "s = 0" was always the point c = +1, since the scripts take
c = sqrt(1-s^2) >= 0. The symbolic statements cover c = ±1, but the sampled and comparison statements do not. So:
- statements that are exact for all angles keep \(\sin\varphi=0\) / \(\sin\varphi\neq0\) (the tau condition, and
  "at \(\sin\varphi\neq0\) generic \(\tau\neq0\)");
- statements made at sampled points, or by comparison with the preceding (phi = 0) paragraph, use \(\varphi=0\);
- the sampled tilt s = 3/5, c = 4/5 becomes \(\varphi=\arcsin\tfrac35\).

The renaming therefore does not widen any claim.

**S1 as inserted.** This is the gatekeeper's text with only the substitutions Lambda → varpi, c → cos phi,
s → sin phi. "(2c\Lambda+\kappa l)p=s^2\Lambda^2" becomes "(2\varpi\cos\varphi+\kappa l)p=\varpi^2\sin^2\varphi",
and "-\Lambda^2k_\parallel^2" becomes "-\varpi^2k_\parallel^2".

> This term does not give a gap. It is the term \(-\varpi^2k_\parallel^2\) of the square \((q_\parallel+\varpi k_\parallel)^2\), fixed by the coefficient \(\varpi\) of the first-order term \(2\varpi(q_0-p\cos\varphi)\), and it vanishes with \(\sin\varphi\). Given the displayed equation, as \(p\to0\) the roots of a class tend to \(q_0=-\varpi(1\mp\cos\varphi)\), which are not real when \(\varpi\) is not real; for real \(\varpi\neq0\), as at \(\chi=0\), these two limits have the same sign, unlike the pair \(\pm m\) of a mass, and for each \(l\) one of the two roots vanishes at the unique \(p>0\) with \(p^2+(2\varpi\cos\varphi+\kappa l)p=\varpi^2\sin^2\varphi\) (by hand from the displayed equation). So no gauge-invariant gap or mass appears for the Lorentz or torsion modes on this family at this order.

The sentence "No norm is used, so no statement on stability is made." is kept after it.

A note on S1 wording, which is applied verbatim. The constant in the "that is" form, \(\varpi^2\sin^2\varphi\), equals
\(-\varpi^2k_\parallel^2\). In the square itself the constant enters as \(+\varpi^2k_\parallel^2\), and the "that is"
form is minus the square. So "the term \(-\varpi^2k_\parallel^2\) of the square" means "of the square as it enters
the displayed second form". S8(a) checks this identity. I left the wording unchanged because it is the gatekeeper's
snippet.

**S2 as inserted** (s = 0 → phi = 0 and s = 3/5 → phi = arcsin 3/5, both at the sampled points):
"(at \(\varphi=0\) and \(l\le5\); at \(\varphi=\arcsin\tfrac35\) only the presence of the predicted roots with
\(l\le3\) is checked)", placed after "and half of these at \(l=\pm1\)".

**S3 as inserted:** "At \(\sin\varphi\neq0\) the null leg has a component along \(E_1\), on which the Landau sectors
act by oscillators, \(k_\parallel^2=-\sin^2\varphi\), and the characteristic equation found above contains" (the
r1 text "s^2\Lambda^2" continues as "\varpi^2\sin^2\varphi").

The complete r1 → r2 sentence diff is in `insert_r1_to_r2_sentdiff.txt`. Every changed sentence is one of:
- S1, S2, S3 or F4;
- the F6 definition sentence;
- the N1 narrowing of the kernel sentence;
- a pure rename (s, c, Lambda → sin phi / phi = 0 / phi = arcsin 3/5, cos phi, varpi).

`make_insert_r2.py` asserts the following:
- no `\Lambda` remains;
- no free `s` or `c` symbol remains in math mode (index positions `^c`, `_{ac}` are excluded);
- each of the S1, S2, S3, F4 and F6 strings occurs exactly once;
- the r1 phrases "This term is not a mass" and "so the characteristic equation contains" are gone.

## Target and status

The target and status are unchanged from r1 (re-read for r2).
- **Problem D (local Lorentz)**, `sec:status-D` (appH L715-722): "Status: OPEN. Priority: CRITICAL PATH. Completion:
  PROGRAMME-CONDITIONAL."
- **Chapter 17, D1** (ch17 L329-345, L650-653, L712-716): the omega, A_mu, B and ghost operators and their field
  content must be specified. The locked frame must exist and be non-degenerate, derived from microscopic data.
- **Missing step** (appH L745-748): "derive the effective dynamics of the independent diagonal connection or retain
  it as unresolved field content". This package addresses the propagating-mode / gap content of the torsion and
  Lorentz sector of the first-order equivariant class (appH L1513-1533) on Heisenberg backgrounds. It continues
  068, 071 and 072 (L1609-1661).
- **Retained dependencies:** the class and its selection by the matrix integral, and Assumptions `ass:frame-lock`,
  `ass:nondeg`, `ass:lorentzian`, `ass:local-lorentz` and `ass:EFT-a2`.
- **Critical-path set** (ch17 + appH): A, B, C, D1, E, F, G-derived, N. No ch17/appH discrepancy for D.
- **Classification:** PROGRAMME-CONDITIONAL.

## Source reading

Digest + targeted reads.
- `python scripts/make_digest.py --check` printed `DIGEST CURRENT`, and the digest has `dirty-chapters: yes`.
- The digest's appH hash `c8c07938df99` matches the live sha256
  `c8c07938df995ac1e6ebedc4e80bcc4ce43eaec9ec99c45696aad6474554ab52`, re-verified this round with `sha256sum` and by
  `apply_and_build_r2.py`.
- Read this round: review-r1, the gatekeeper scripts `gk_cut_r1.py` and `gk_op_r1.py` (read, not re-run), appH
  L1513-1533 and L1606-1663 (symbol collisions), and the appH-wide occurrences of `\Lambda`, `\varphi`, `\varpi`,
  `\sigma`, `\Xi`, `\Upsilon`, `\varrho`.
- Not done: a full scan. Edit 2 still triggers the gatekeeper full scan under 3(c).

## Research and reasoning

R1 (exact family), R2 (Q identity) and the hypotheses table are as in r1 (proposal-r1.md, sections R1, R2), with
the notation of this round: s = sin phi, c = cos phi, Lambda = varpi. Only the changed parts follow.

### R3. Characteristic structure, s != 0 Landau sectors (corrected F3 text)

The solutions at s != 0 are not polynomial × Gaussian. The column cut keeps all forty components but only the
oscillator columns n <= Lc of a level-N matrix. At s != 0 it is therefore **not a valid test**. It gives:
- **T1:** 109 roots. 108 are in class 0 and 1 is unassigned.
- **T2:** 115 roots. 108 are in class 0, 1 is in class i chi (class 1), and 6 are unassigned.

These counts are from S7(e): `per class [108, 0, 0, 0, 0, 0]` and `[108, 1, 0, 0, 0, 0]`.

**Why the cut is invalid here.** The cut computes the roots of a rectangular truncation, which keeps every equation
row up to level N but only the trial columns up to level Lc. A root of the full system is a root of this
truncation only if its eigenfunction lies in the span of the kept columns. At s = 0 the eigenfunctions are
polynomial × Gaussian, so the span is exact (S5). At s != 0 they are not (S7, D-3). The cut then returns a subset of
the class-0 roots together with spurious roots: the unassigned ones at T1 and T2.

**Why no N-dependence test.** The gatekeeper's `gk_cut_r1.py` varies (N, Lc). It was not re-run here. Whatever it
gives, the cut cannot certify roots at s != 0, for the reason above. Adding it would sharpen a diagnostic on which
no claim rests.

No statement in the block or in C6 uses the cut at s != 0. The s != 0 claims rest on the square truncations
N = 18, 24 (S7(b), (c)), as in r1:
- every converged eigenvalue is assigned: 147 at T1 and 191 at T2, with 0 unassigned;
- the predicted roots with l = -1, 1, 3 are found within 8e-9 (T1) and 1.5e-7 (T2);
- the gauge-kernel statement is the one exception that does use the cut. S7(a) computes the kernel of the cut
  (N = 14, columns at oscillator levels <= 5) at generic q0 and prints `kernel dim 50, gauge 50, rank[ker|G] 50,
  |M G| 2e-15`. This is a valid one-sided statement, not a root count: the gauge vectors of levels <= 4 are exact
  null vectors (|M G| ~ 1e-15), and every kernel vector of the operator supported in the kept columns lies in their
  span. It says nothing about kernel vectors with components at higher levels. The block's kernel sentence is
  therefore narrowed at the tilted point (change N1).

The p = 0 and s = 0 parts of R3 are unchanged from r1.

### R4. Gap decision (rewritten per S1; exact check S8)

From the display q0^2 - p^2 + 2 varpi(q0 - p cos phi) + varpi^2 sin^2 phi = kappa p l:
- (a) The left side is -(q_par + varpi k_par)^2 with k_par = (1, 0, cos phi, 0), and its constant is
  -varpi^2 k_par^2 = varpi^2 sin^2 phi. So the constant is fixed by the coefficient varpi of the first-order term,
  and it vanishes with sin phi. [S8(a), exact]
- (b) At p = 0 the roots are q0 = -varpi(1 ∓ cos phi), with product varpi^2 sin^2 phi.
  - For non-real varpi the roots are not real.
  - For real varpi != 0 and sin phi != 0 the product is > 0, so the roots have the same sign. A mass gives ±m.
  [S8(b), exact]

  This replaces r1's "imaginary for imaginary Lambda" and "sign opposite to a mass term". The first covered only a
  subset of the classes. The second depended on a convention. This addresses F1.
- (c) At q0 = 0 the equation is p^2 + (2 varpi cos phi + kappa l)p - varpi^2 sin^2 phi = 0. The product of its
  p-roots is -varpi^2 sin^2 phi < 0 for real varpi != 0, so there is exactly one root p > 0. [S8(c), exact]
- (d) Scope. These are statements about the displayed equation. The display itself is numerical at
  phi = arcsin 3/5 (C6), so the gap decision there is conditional on C6. The block says "Given the displayed
  equation" and "(by hand from the displayed equation)".

## Claim classification

These are as in r1, with these changes:
- C6 now records that the multiplicities are verified at phi = 0, l <= 5. At phi = arcsin 3/5 only the presence of
  the l <= 3 predicted roots is verified (S2).
- C7 is now "established from the displayed equation (exact S8), conditional on C6 at phi != 0".
- New C9 (established, exact): the r1 → r2 notation map sends the r1 display to the r2 display (S8(d)).

Summary of the classes:
- established: C1, C2, C3, C5, C9;
- numerical: C4, C6;
- conditional on C6: C7;
- unresolved: C8, which includes O1.

## Proposed changes

### File `chapters/appH-microscopic-proofs.tex`

**Edit 1 (insert).** This uses the same anchor as r1. Insert the block `appH_insert_r2.tex` (CRLF, UTF-8 without
BOM, 7312 bytes, sha256 `0a56538d601cbdb17de3727b1f6074fea73116faa49d3da0e20d53c48562969c`), followed by one blank
CRLF line, immediately before the unique line

```
\section{Problem E: signature}
```

The insert follows the 072 closing paragraph, which begins "These statements are for Equation~\eqref{eq:Smatrix}
with \(C_{\mu\nu\lambda}=0\) and no matter term, tree level, linear order in the fluctuation, the Lorentzian
contraction and the wider family" (unique; checked by the script). Nothing is removed.
- Labels used: `eq:Smatrix` and `ch:vierbein-emergence`, each defined once.
- No new labels and no citations.
- One status sentence, at the end of the block.

```latex
\paragraph{First-order equivariant class on the Heisenberg background: connections with legs off the null direction (conditional; not closure).}
Keep time times the Heisenberg group with the normalisation and the fluctuation of the preceding paragraph. For an angle \(\varphi\) let \(\delta_0^a=(1,0,0,0)\), \(n^a=(1,\sin\varphi,-\cos\varphi,0)\), \(\hat n^a=(0,\sin\varphi,-\cos\varphi,0)\), \(e^a=(0,\cos\varphi,\sin\varphi,0)\), \(f^a=(0,0,0,1)\) and \(k_a=-\eta_{ab}n^b\), write \(X(u,v)^{cd}=u^cv^d-u^dv^c\), and let \(B_n=X(\delta_0,-\hat n)\), \(J_n=X(e,f)\), \(N_e=X(n,e)\) and \(N_f=X(n,f)\); at \(\varphi=0\) these are \(k\), \(B\), \(N\) and \(N'\) of the preceding paragraphs and the rotation of the \(1\)-\(3\) plane. Take
\[
w_a{}^{cd}=k_a(\chi B_n+\vartheta J_n)^{cd}+P_aN_e^{cd}+Q_aN_f^{cd},\qquad P_a=\zeta k_a+\alpha e_a+(\beta+\vartheta)f_a,\quad Q_a=xk_a+\beta e_a+\gamma f_a,
\]
which is the wider family at \(\varphi=\vartheta=\alpha=\beta=\gamma=0\). For all real \(\kappa,\chi,\vartheta,\zeta,x\) the first two brackets hold when
\[
\vartheta^2-2\vartheta\beta-2\beta^2-\alpha^2-\gamma^2+2\chi(\alpha+\gamma)=0
\]
and, if \(\sin\varphi\neq0\), \(\tau:=\chi+\alpha+\gamma=0\); at \(\sin\varphi\neq0\) and generic \(\tau\neq0\) the constraint alone does not suffice. Then \(\mathsf T_{ac}{}^c=\tau k_a\), the third bracket holds, \(\mathsf R_{abcd}\mathsf R^{abcd}=4\kappa^2\cos^2\varphi\,(\vartheta^2-\chi^2)\), which is positive for \(\cos\varphi\neq0\) and \(|\vartheta|>|\chi|\), and every \(w_a\) fixes the null line of \(n\) (exact for symbolic parameters; for the operators on the bundle at a rational Lorentz \(u\), order-zero part included, exact at one point with \(\varphi=0\), \(\tau\neq0\) and one with \(\varphi=\arcsin\tfrac35\)). The form \(\eta^{ab}w_a{}^{cd}w_b{}^{ef}\) is nonzero when one of \(\alpha\), \(\beta\), \(\beta+\vartheta\), \(\gamma\) is, but on vectors \(\eta^{ab}w_aw_b=-\eta^{ab}(P_aP_b+Q_aQ_b)\,n\otimes n^\flat\), whose square is zero (exact). Of the 107 solutions of the survey of the preceding paragraph that converge to residual \(10^{-13}\), 80 pass the tests for this form at tolerances \(10^{-10}\) to \(10^{-9}\), 25 more at \(10^{-8}\) to \(10^{-6}\), and two do not; for all of them \((\eta^{ab}w_aw_b)^2\) vanishes on vectors to \(2\cdot10^{-11}\) (numerical, not a classification).

On this family \(\mathcal Q_b[A]=\mathcal Q_b[A]|_{w=0}-\tau\,k^a\mathsf F_{ab}[A]\) for all \(A\) (exact), so at \(\varphi=0\) the order-zero operator is that of the preceding paragraph with \(\chi\) replaced by \(\tau\), and at \(\sin\varphi\neq0\) it is the operator of the paragraph on left-invariant backgrounds with torsion. For the forty equations, in the sectors \(p=0\), where \(E_1\) and \(E_3\) commute, every characteristic root lies on a cone \((q+\varpi k)^2=0\), and in the Landau sectors every root satisfies
\[
(q_\parallel+\varpi k_\parallel)^2+\kappa p\,l=0,\quad\text{that is}\quad q_0^2-p^2+2\varpi(q_0-p\cos\varphi)+\varpi^2\sin^2\varphi=\kappa p\,l,\qquad k_\parallel=(1,0,\cos\varphi,0),\ l\in\{-1,1,3,\dots\},
\]
with \(\varpi\) in the set
\[
\bigl\{\tfrac{\mathrm i}2\tau,\ \mathrm i(\tfrac\tau2+\chi),\ \mathrm i(\tfrac\tau2+\chi)\pm\vartheta,\ \mathrm i(\tau-\tfrac32\chi)\pm\rho\bigr\},\qquad\rho^2=\tfrac32\vartheta^2-\chi^2+\tfrac14(\tau-3\chi)^2,
\]
whose members carry \(10\), \(2\), \(2\), \(2\), \(2\) and \(2\) of the twenty quadratic factors at \(l\ge3\), and half of these at \(l=\pm1\) (at \(\varphi=0\) and \(l\le5\); at \(\varphi=\arcsin\tfrac35\) only the presence of the predicted roots with \(l\le3\) is checked). So \(\zeta\), \(x\), \(\alpha\), \(\beta\) and \(\gamma\) enter only through \(\tau\) and the constraint, and the levels \(\kappa p\,l\) are not shifted. At \(\varphi=0\), \(\chi=\tfrac14\), \(\vartheta=\tfrac12\), \(\alpha=\gamma=\tfrac34\), \(\beta=-\tfrac14\), where the rotation of the \(1\)-\(3\) plane combined with the oscillator level is conserved, this is exact in rational arithmetic after rational reconstruction, in the sector \(p=0\) at a sampled \(q\), also with \(\zeta,x\neq0\), and in the blocks that on the observed pattern contain all factors with \(l\le5\), at \((\kappa,p)=(1,\tfrac12)\) and \((2,\tfrac14)\). Otherwise it is numerical at sampled points: at \(\varphi=0\) for \(l\le5\) as in the preceding paragraph, and at \(\varphi=\arcsin\tfrac35\), where the solutions are not polynomials times the Landau Gaussian, for the eigenvalues of truncations to \(18\) and \(24\) oscillator levels that agree, all of which are assigned. The kernel at generic \(q_0\) is the ten gauge directions for each level (numerical; at \(\varphi=\arcsin\tfrac35\) among the fluctuations of oscillator level at most \(5\)).

At \(\varphi=0\) the vector \(k_\parallel=k\) is null and no term independent of the momentum enters, as for the wider family, now on backgrounds with \(\mathsf R_{abcd}\mathsf R^{abcd}>0\) and a nonzero leg form; the real parts \(\pm\vartheta\) and \(\pm\operatorname{Re}\rho\) of \(\varpi\) shift the cones along \(k\), as on the null-rotation background of the paragraph on left-invariant backgrounds with torsion, and the imaginary parts are rates. At \(\sin\varphi\neq0\) the null leg has a component along \(E_1\), on which the Landau sectors act by oscillators, \(k_\parallel^2=-\sin^2\varphi\), and the characteristic equation found above contains the momentum-independent term \(\varpi^2\sin^2\varphi\) for every class with \(\varpi\neq0\); the class \(\varpi=\tfrac{\mathrm i}2\tau=0\), which contains \(\mathcal Q\), has none. This term does not give a gap. It is the term \(-\varpi^2k_\parallel^2\) of the square \((q_\parallel+\varpi k_\parallel)^2\), fixed by the coefficient \(\varpi\) of the first-order term \(2\varpi(q_0-p\cos\varphi)\), and it vanishes with \(\sin\varphi\). Given the displayed equation, as \(p\to0\) the roots of a class tend to \(q_0=-\varpi(1\mp\cos\varphi)\), which are not real when \(\varpi\) is not real; for real \(\varpi\neq0\), as at \(\chi=0\), these two limits have the same sign, unlike the pair \(\pm m\) of a mass, and for each \(l\) one of the two roots vanishes at the unique \(p>0\) with \(p^2+(2\varpi\cos\varphi+\kappa l)p=\varpi^2\sin^2\varphi\) (by hand from the displayed equation). So no gauge-invariant gap or mass appears for the Lorentz or torsion modes on this family at this order. No norm is used, so no statement on stability is made.

These statements are for Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and no matter term, tree level, linear order in the fluctuation, the Lorentzian contraction and this family on time times the Heisenberg group with constant connection, in the sectors named. The survey solutions outside the family, a norm, loops, the nonlinear evolution, the regulated trace and the domains of the unbounded operators are not treated. Nothing here shows that the matrix integral selects this class, these backgrounds or the algebra \(\mathcal A\), so the assumptions listed in the paragraph on left-invariant backgrounds with curvature and torsion are not discharged, and the frame of these backgrounds is not identified with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
```

**Edit 2.** Unchanged from r1, with the same anchor, in the 072 closing paragraph (L1661). Replace the unique string

```
(numerical survey, not a classification); they are not linearised here.
```

with

```
(numerical survey, not a classification); those of the form of the following paragraph are linearised there.
```

**Hashes.**
- appH pre sha256: `c8c07938df995ac1e6ebedc4e80bcc4ce43eaec9ec99c45696aad6474554ab52`. It is live: checked by
  `sha256sum` and by the script, and it equals the digest.
- appH post sha256 (r2): **`29ac2a634bb819df7ecb29e138f97ae014656d4c0bb812b86f3573759a872046`**, 766977 bytes, no
  bare LF.
- This replaces the r1 post hash `69ab958a…`.

No other file changes. No bibliography change.

## Verification scripts

All scripts are in `proposals/073-d1-heisenberg-nonnull-leg/`. The r1 scripts are unchanged. New this round:

| script | checks |
|---|---|
| `make_insert_r2.py` | Writes `appH_insert_r2.tex` (CRLF). Fills the survey counts from S3 output. Asserts no `\Lambda` or free s/c survives, that each S1/S2/S3/F4/F6 string occurs once, and that the r1 phrases are removed. |
| `s8_root_algebra_r2.py` | Exact sympy checks of the by-hand gap statements (S1) in the r2 notation, plus the r1 → r2 notation map. |
| `apply_and_build_r2.py` | Uses the r1 anchors, including Edit 2. Checks the pre and post hashes and the labels. `--build` builds in a temp copy outside the repo and removes it. |
| `insert_r1_to_r2_sentdiff.txt` | Sentence-level unified diff of the r1 and r2 blocks. |
| `s1_family_exact_output_r2.txt` | r2 re-run of S1 under `python -I -B`. |

**Reproduction pack** (run from the proposal folder):
- `python -I -B s1_family_exact.py` should print:
  - (a) and (b) `residual set {0}`;
  - (c) `True ; distinct remainders 13`;
  - (d) `... = 0` and `T_ac^c - tau k_a = [0, 0, 0, 0]`;
  - (e) third bracket `[0, 0, 0, 0]`;
  - (f) `True`, `True`, `L^2 == 0: True`, leg form `True`;
  - (g) `[0, 0, 0, 0]`.

  The r2 output is identical to r1 modulo timings. Check with `diff` after `sed 's/ *\[[0-9]*s\]//'`.
- `python -I -B s8_root_algebra_r2.py` should print:
  - (a) `= 0` twice;
  - (b) `expected -varpi(1-+cos): True` and product `= 0`;
  - (c) `= 0` and `product of p-roots = -varpi**2*sin(phi)**2`;
  - (d) `= 0`.
- `python -I -B make_insert_r2.py` should print: `survey: clean 107, strict 80, loose 25, outside 2`; the symbol
  checks `True`; `bytes 7312 CRLF lines 24 bare LF 0`.
- `python -I -B apply_and_build_r2.py --build` should print:
  - `pre-hash matches expected: True`;
  - both anchors unique, at lines 1663 and 1661;
  - block 7312 bytes, sha256 `0a56538d…`;
  - post `29ac2a634bb819df7ecb29e138f97ae014656d4c0bb812b86f3573759a872046`, `post-hash matches expected: True`;
  - labels defined `1`;
  - pdflatex `418` pages, `undefined/multiply-defined warnings: 0`, `BUILD CLEAN`, `temp copy removed: True`.

  The r2 output is recorded in `apply_and_build_r2_output.txt`.
- The other r1 commands (S2-S7) are unchanged. Their outputs are the r1 files.

## Decisions Taken

- **D-1 to D-6:** as in r1.
- **D-7 (F6 rename adopted).** The tilt becomes (sin phi, cos phi) and Lambda becomes varpi.
  - Reasons: c collides with a Lorentz index (`T_{ac}^c`, `X^{cd}` in the same block) and with 072's class label;
    Lambda collides with the class gauge parameter of L1521; and varpi is unused in this section.
  - Rejected: sigma (an index elsewhere in appH) and Xi / Upsilon (used in the D and N sections).
- **D-8 (phi = 0 vs sin phi = 0).** Sampled and comparison statements use phi = 0 and phi = arcsin 3/5. Symbolic
  statements use sin phi = 0 / != 0. The sample points have cos phi >= 0, so a literal s → sin phi substitution
  would have implicitly extended the numerical claims to cos phi = -1.
- **D-9 (F3).** I chose to state that the column cut is not valid at s != 0, rather than add an N-dependence test. No
  claim rests on the cut there, and an N-dependence study could not turn it into a certificate.
- **D-11 (N1).** Narrowed the tilted-point kernel sentence to the tested span, and did not extend S7(a) to a
  larger cut. That claim is not on the gap path, and the narrowing is the smallest accurate text.
- **D-10 (S1 wording).** S1 is applied verbatim, with only the symbol substitution, even though "the term
  -varpi^2 k_par^2 of the square" reads most naturally with the sign of the displayed second form (noted above).

## Milestone assessment

Routine. No critical-path step is derived.

## Status-label recommendation

Critical-path set (ch17 + appH): A, B, C, D1, E, F, G-derived, N. All labels are unchanged. D, F and N remain
OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

None. Adopting a mu^2 term as core would be STRUCTURAL (fundamentality agent). It is not proposed here. It is
listed only as a scoped hypothesis class (avenue 5).

## Remaining open step

**To close D1 (unchanged).** Derive local SO(3,1) and the locked frame from the matrix data, select the class, and
specify omega, A, B and the ghost operators with their field content and propagating modes (including norms).

**Ranked avenues for the torsion/Lorentz-mode gap (re-ranked to review r1).** These are derivation-first.
1. **C_{μνλ} != 0, within the core.** Linearise the forty equations on the Heisenberg family with the cubic term of
   Equation~\eqref{eq:Smatrix} switched on. Eq:Smatrix already contains C_{μνλ}, so this needs no new core input. A
   cubic term is the natural within-core source (conjecture, not derived) of a momentum-independent, non-square-completion term, because it
   gives an intrinsic scale that the dilation and square-completion arguments of 071, 072 and 073 do not remove.
   First task: find the constant-connection solutions with C != 0 (they shift the brackets). Then compute the
   characteristic equation.
2. **One loop on the tilted family.** Q = Q|_{w=0} exactly, while the forty equations carry varpi. The regulated
   one-loop determinant could induce a non-derivative torsion-mode term. The commutators are nonzero, so the
   cancellation of the commuting case does not apply.
3. **A pairing / Krein form** on the family. It would decide whether the real-varpi branches and the rate classes
   are physical or gauge-null. The Maxwell-like Q is the starting point.
4. **Non-constant connections** on Heisenberg, **or other algebras.** Examples are the 071 survey algebras with
   R^2 != 0 and a 2-dimensional abelian derived algebra, where the third bracket has not been examined.
5. **mu^2 (bilinear) term.** It is not in eq:Smatrix, so adopting it as core is STRUCTURAL. It may be studied as a
   scoped hypothesis class, for example on the de Sitter solution built from E_{a4} on SO(4,1) (appH L1527).
6. **Nonlinear** evolution of the real-varpi zero-frequency crossings.
7. **O1:** derive the varpi set and the root formula analytically, by a null-filtration triangular decomposition.
   This would make C6, and so C7 at phi != 0, exact. It is ranked last because it would not change the gap verdict.

At the bottom of the record, as in r1: further constant-connection families on Heisenberg. S3 indicates that the
clean solutions are of this null-line form, so the likely outcome is the same bounded result.

**Hypotheses table, avenue column, updated:**
- H5 (constant connection) → avenue 4;
- H6 (tree level) → avenue 2;
- H7 (no pairing) → avenue 3;
- H8 (C = 0, no mu^2) → avenues 1 and 5;
- H9 (linear order) → avenue 6.

**Transfer (unchanged).** Q = Q0 - tau k F and the nilpotent leg structure transfer to Problem N, where a norm on
these backgrounds acts on a nilpotent non-derivative structure. They also transfer to Problem F, where the
w-dependence of the second-order operator is nilpotent at tree level.

## Special instructions for the gatekeeper

- Check that S1-S3 and F4 occur verbatim modulo the declared substitutions. `make_insert_r2.py` asserts each string,
  and `insert_r1_to_r2_sentdiff.txt` shows every changed sentence.
- Check D-8: no numerical claim was extended to cos phi < 0.
- Check N1, the tilted-point kernel sentence, against S7(a) (`N, L = 14, 5`).
- Re-run `s8_root_algebra_r2.py`, a new exact check of S1's by-hand content.
- Re-run `apply_and_build_r2.py --build` and confirm the new post hash `29ac2a63…`.
- The full scan under 3(c) is still owed (Edit 2).
- No mass or gap may be asserted. No label change. D, F and N remain open.
