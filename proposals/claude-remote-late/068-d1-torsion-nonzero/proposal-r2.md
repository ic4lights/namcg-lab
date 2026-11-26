# Proposal 068-d1-torsion-nonzero, round 2

## Result

The substance is unchanged from r1. Review-r1 verified all the mathematics and returned ACCEPT WITH REQUIRED
REVISIONS on minor findings only. The class is the first-order equivariant class of appH `sec:status-D`. The
backgrounds are left-invariant backgrounds with torsion: base a four-dimensional Lie group `G`, vanishing background
connection, `D_a = u_a^b E_b`, so `R = 0`, `F = 0` and `T = -c`. On them:

* **(R1)** `E^(2)_b^{de} = Q_b[omega^{de}]`; no frame field enters.
* **(R2)** `E^(1)_b^e |_{omega=0} = Q_b[f^I] (L^{-1})_I^e`, with `f_b^I = -h_b^c L_c^I` and `E_c = L_c^I rho_I`.
  The matrix called `\mathsf A` in r1 is `\mathsf L` in r2 (finding o2).

Here `Q_b[A] = E^a F_ab + c_ab^c F^a_c` is the gauge-invariant linearised third bracket. The forty equations are
block-triangular and consist of ten copies of `Q`.

* **Null-rotation background.** The roots lie on the real cones `(q + j vartheta k)^2 = 0`. The parameter is
  renamed from kappa to vartheta (m3). It is now also checked at `vartheta = -1/2`, the value that carries the
  left-invariant torsion. Cone membership is read off without rounding, with exact rational ranks at points on the
  cones.
* **Heisenberg background.** `[E_3,E_1] = kappa E_2` with `kappa > 0` (m2). There is an exact non-gauge mode with
  `Q[A] = (q0^2 - p^2 + kappa p) A`. It gives real solutions growing like `exp(Gamma y0)`, with
  `Gamma = sqrt(p(kappa - p)) <= kappa/2`. So the background is linearly unstable at tree level within the class.

The Euler–Lagrange sentence now uses the gatekeeper's wording (m4). The last sentence of appH L1581, which left the
mass question open, is replaced by a pointer to the new paragraph (m5). The insert moves to the end of
`sec:status-D`, immediately before `\section{Problem E: signature}` (m1).

**What this is and is not.** As in r1, this is positive, derivation-grade data on the torsion and connection
dynamics at `T != 0`. That is part of the D1 Missing step "Generator counting alone does not settle its torsion or
propagating modes". It holds within a supplied background class, at tree level and linear order. It does not derive
the class, its algebra, the frame or its non-degeneracy. It gives no norm, no nonlinear fate for the instability and
no loops. It closes nothing.

## Diffs from r1 (exact)

### Insert (`appH_insert_r1.tex` -> `appH_insert_r2.tex`)

`make_insert_r2.py` applies these replacements to the r1 file. Each old string occurs exactly once, except o2,
which occurs exactly four times; the script asserts this.

| id | old (r1) | new (r2) |
|---|---|---|
| m2 | `The Heisenberg algebra \([E_3,E_1]=\kappa E_2\), with \(E_0\) and \(E_2\) central,` | `The Heisenberg algebra \([E_3,E_1]=\kappa E_2\), with \(\kappa>0\) and with \(E_0\) and \(E_2\) central,` |
| m3a | `\omega_a{}^{12}=\kappa k_a` | `\omega_a{}^{12}=\vartheta k_a` |
| m3b | `for \(\kappa=-\tfrac12\)` | `for \(\vartheta=-\tfrac12\)` |
| m3c | `\((q+j\kappa k)^2=0\)` | `\((q+j\vartheta k)^2=0\)` |
| m3d | `roots numerical at \(\kappa=\tfrac12,1,2\)` | `roots numerical at \(\vartheta=-\tfrac12,\tfrac12,1,2\)` |
| m3e | `for \(\kappa=1\)` | `for \(\vartheta=1\)` |
| m4 | `On flat space and on the null-rotation background, moreover, every constant matrix ... with constant coefficients.` | the review's sentence verbatim: `On flat space and on the null-rotation background in the gauge with constant frame below, moreover, every constant matrix \(G\) for which \(G\) times the forty linearised equations is formally self-adjoint vanishes on the frame equations (numerical), so no constant recombination of these equations is the Euler--Lagrange system of a quadratic Lagrangian in \(h\) and \(\omega\) with constant coefficients; the ten Maxwell equations of the paragraph on the pairing of the action are in variables that contain \(y\) explicitly.` |
| o1 | `acquire no term beyond those of a gauge field that keeps its gauge parameter, and at generic characters the kernel` | `obey the gauge-invariant equation \(\mathcal Q\); no term breaking \(A_b\to A_b+E_b\Lambda\) appears. At generic characters the kernel` |
| o2 | `\mathsf A` (4 occurrences: `E_c=\mathsf A_c{}^I\rho_I`, `\(\mathsf A\) an invertible`, `(\mathsf A^{-1})_I{}^e`, `h_b{}^c\mathsf A_c{}^I`) | `\mathsf L` |

The script also asserts that no `\kappa` remains in the null-rotation sentences and that they contain
`\vartheta` exactly five times. Nothing else in the block changed. r1 was 7277
bytes; r2 is 7503 bytes, sha256 `b80bc4e350d0794db4f2eb8c49b5c249ef9369b0fdd22b2fd31422f46c056dc8`, CRLF, no BOM.

### Placement (m1)

* **r1.** Immediately before `\paragraph{The locked frame as a gauge-invariant composite (conditional; not
  closure).}`.
* **r2.** Immediately before the unique line `\section{Problem E: signature}` (pre-image line 1607). The block is
  followed by one blank CRLF line, so the result reads: composite paragraph (L1605), blank line, block, blank line,
  `\section{Problem E: signature}`.

### New anchored edit in the live appH (m5)

* Anchor: the sentence `Whether the remaining modes acquire a mass term of definite sign is not computed.` It
  occurs exactly once in the file. It is the last sentence of pre-image line 1581, the paragraph "First-order
  equivariant class: one loop about commuting matrices, ...", followed directly by CRLF. `apply_and_build_r2.py`
  asserts the count, the line number and the line end.
* Replacement, from the review verbatim: `Whether the remaining modes acquire a mass term of definite sign is not
  computed in this part; for left-invariant backgrounds with vanishing connection their linearised equations are
  given in the paragraph on left-invariant backgrounds with torsion later in this section.`
* The rest of L1581 is kept. The edit changes no line count.

### Hashes

* Pre-image: `8d1eb5dccd6c808feb0bfbc935b5d5d0444dbfd8a46ac9c56c56519d07cfd41e`, 712252 bytes. This is the live
  file, verified this round.
* r1 post-image: `08bc659e...` (withdrawn).
* r2 post-image: `6a72a3268302d46b9b5d3ede69f8b15e838a0a3c14bfddc2e1b4e8ab58b39a7c`, 719947 bytes, no bare LF. That
  is 712252 - 81 + 271 + 7503 + 2 bytes.

### Closers (task item 3)

* The block has exactly one status sentence, its final clause `Problems~D, F and~N remain open and
  PROGRAMME-CONDITIONAL.`, on line 21 of 21. The script asserts this.
* The preceding composite paragraph (L1605) ends with `Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.`
  It is now followed by a blank line and the block's `\paragraph` heading. The block's first paragraph contains no
  status clause, which the script also asserts.
* So the two closers are not on consecutive lines. They are separated by the whole 21-line block, which is its own
  contiguous unit with its own single closer. This matches the pattern already in the section, where the 052
  paragraph L1597 closes with "Problems~D, E, F and~N remain open ...".
* The r1 position split the 059 unit (compact toy at L1599-1602 + composite at L1604-1605). That split is removed:
  the 059 unit is contiguous again.

### Cross-references after the move

* "the convention of the compact toy above": the toy is still above, at L1599.
* "the paragraph on the pairing of the action" (L1533) and "the paragraph on one loop about commuting matrices"
  (L1572) are both above.
* "the Heisenberg algebra below" and "in the gauge with constant frame below" both point to the block's own second
  paragraph.
* The m5 pointer "later in this section" is correct: L1581 < L1607, and the block is inside `sec:status-D`.

### Bibliography

`bib-additions-r2.bib` is identical to r1: `NielsenOlesen1978`, verified in r1 against Crossref and INSPIRE, and
re-checked by the gatekeeper.

### Scripts

* New: `v4_null_rotation_vartheta_r2.py` and its output, `make_insert_r2.py` and its output,
  `apply_and_build_r2.py` and its output.
* r1 files are kept unchanged, including `v4_null_rotation_kappa.py` and its stored output, so r1 stays
  reproducible.

## Target and status

Unchanged from r1, and re-checked against the live file, whose hash is still the pre-image hash:

* **Problem.** Problem D (`sec:status-D`), sub-route D1.
* **Ledger label (appH L716-720).** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL".
* **Chapter 17.** Problem D is "CRITICAL PATH; OPEN".
* **Missing step.** appH L743-756, including "derive the effective dynamics of the independent diagonal connection
  or retain it as unresolved field content. Generator counting alone does not settle its torsion or propagating
  modes".
* **Dependencies.** D1 gates F, C and N.
* **Classification.** PROGRAMME-CONDITIONAL; not DERIVED for the original target.
* **Discrepancies.** None found.

## Source reading

Digest + targeted reads.

* **Digest.** `python scripts/make_digest.py --check` printed `DIGEST STALE (head changed)`. I did not regenerate
  it, because `scratch/` is outside my folder. Instead I read the live files directly. The live appH hash equals the
  r1 pre-image hash, so every appH passage read in r1 is byte-identical.
* **Re-read this round:**
  * appH paragraph headings L1494, 1511, 1533, 1572, 1599, 1604;
  * the full ends of L1581, L1595, L1597, L1600, L1602 and L1605;
  * L1607 `\section{Problem E: signature}` (unique);
  * L1555, the "ten Maxwell equations" sentence and "The redefinition contains \(y\) explicitly", which support
    the m4 clause;
  * uses of `\mathsf A`, of `\mathsf L` and `\mathsf P` (none in chapters/), and of `\vartheta` in appH. Its
    occurrences are at L102-115, L443-509, L914-974 and L2427-2982, none in `sec:status-D` (L713-1606), so the
    local parameter collides with nothing there.
* **Not a full scan.** The gatekeeper's disposition already schedules the full scan before a plain ACCEPT.

## Research and reasoning

r1 §§0-5 are carried over unchanged; the gatekeeper verified them. Briefly:

* **(R1).** Linearising the closed curvature formula of appH L1523 about `Omega = 0` gives `dR_ab^{de} =
  F_ab[w^{de}]`, independent of `h`. With `R-bar = 0`, `T-bar = -c`, this gives `dE^(2) = E^a F_ab + c_ab^c F^a_c`.
* **(R2).** The right-invariant fields commute with the background. Summing the three linear terms gives `Q_b[f]`
  plus `-c_ab^d c^a_d^e f_e`, and that extra term vanishes by the background equation. `L` is invertible, so the
  four labels exhaust the frame fluctuations.
* **Heisenberg mode.** `F_32 = p phi != 0`, so the mode is not a gauge direction. `Q` is a real operator.
  Superpositions in `p` are square-integrable on the slices.
* **Euler–Lagrange test.** `v3`.
* **Fork record.** Ranked avenues as in r1 §5 and in the gatekeeper's list; repeated under "Remaining open step".

### New in r2: the null-rotation cones at vartheta = -1/2 without rounding (m3)

For `k_a = (1,0,0,1)` and `eta = diag(-1,1,1,1)`, `k` is null. So `(q + j vartheta k)^2 = q^2 + 2 j vartheta (k.q)`,
and a root `q` lies on the weight-`j` cone if and only if `x(q) := -q^2/(2 vartheta k.q) = j`.
`v4_null_rotation_vartheta_r2.py` checks this in two ways.

1. **Numerical check.** For each root cluster on the s2 line, at `vartheta = -1/2, 1/2, 1, 2`, the script prints
   three things: `x` itself, complex and unrounded; `|x - j|` for the nearest integer `j`; and the direct residual
   `|(q + j vartheta k)^2| / |q|^2`. A root counts as on a cone only if `|x - j| < 1e-8`.
   * Results: 40 roots at each value; max `|Im t|` 1.8e-13 at `vartheta = -1/2`; max `|x - j|` 1.4e-11 at
     `-1/2` and 1.5e-9 at `vartheta = 2`; max cone residual 1.5e-12 at `-1/2`.
   * At every value the multiplicities per crossing are `{-2:[2,2], -1:[6,6], 0:[4,4], 1:[6,6], 2:[2,2]}`.
   * At `vartheta = -1/2` the root values `t` coincide with those at `+1/2`, with `j -> -j`. This is as expected,
     since only `j vartheta` enters.
2. **Exact check, independent of root finding.**
   * At `vartheta = -1/2`, with the coefficient matrices recognised as rationals (asserted to 1e-12), the exact
     rank of `M(q)` is 30 at a generic rational point. That equals 40 minus the 10 gauge directions, and agrees
     with the floating rank.
   * At the exact rational points `q = nvec - j vartheta k` with `nvec = (13,3,4,12)` null, the rank is 28, 26,
     26, 26, 28 for `j = -2..2`. These points lie on the cones exactly (`x = j` in `Fraction` arithmetic). The
     same ranks are found at `vartheta = 1` (s2).

So the roots at `vartheta = -1/2` lie on the cones `(q + j vartheta k)^2 = 0` to numerical precision with `j`
determined without rounding, and the rank drop on the cones is exact.

The inserted text is unchanged in its claim class: "roots numerical at `vartheta = -1/2, 1/2, 1, 2`". The exact
ranks at `-1/2` are extra evidence and are not added to the text, so the gatekeeper's m3 wording is used verbatim.

## Claim classification

As in r1, with these updates:

| Claim | Class |
|---|---|
| (R1), (R2) for arbitrary `h`, `w` on left-invariant backgrounds with vanishing connection that solve the equation | established (derivation; exact symbolic check on four backgrounds, `v1`) |
| block-triangular; ten copies of `Q`; the non-commutant Lorentz modes obey the gauge-invariant `Q` with no term breaking `A -> A + E Lambda` (o1 wording) | established (corollary) |
| kernel at generic characters = ten gauge directions | numerical |
| no constant EL recombination (flat; null rotation in the constant-frame gauge); the flat Maxwell variables contain `y` (L1555) | numerical; the second part is integrated text |
| null rotation: roots on `(q + j vartheta k)^2 = 0` at `vartheta = -1/2, 1/2, 1, 2`, `j` read off unrounded | numerical (residuals at most 1.5e-9) |
| null rotation: exact rank drop on the cones at `vartheta = -1/2` and `1` | exact rational arithmetic at sampled points (coefficients rationalised; assertion 1e-12) |
| Heisenberg (`kappa > 0`): exact mode, growth, normalisable superpositions, frame-label lifts with `dT != 0` | established |
| Landau spectrum; forty-field multiplicity ten times that of `Q` | numerical |
| Nielsen–Olesen comparison | analogy; literature verified at abstract level |
| class, algebra, frame, non-degeneracy, selection; norm; nonlinear fate; loops | unresolved |

## Proposed changes

### File `chapters/appH-microscopic-proofs.tex` (the only file changed; two edits)

* **Pre-image.** sha256 `8d1eb5dccd6c808feb0bfbc935b5d5d0444dbfd8a46ac9c56c56519d07cfd41e`, 712252 bytes. This is
  the live file, verified.
* **Edit 1 (m5).** At L1581, replace the last sentence:

  ```latex
  Whether the remaining modes acquire a mass term of definite sign is not computed.
  ```

  with

  ```latex
  Whether the remaining modes acquire a mass term of definite sign is not computed in this part; for left-invariant backgrounds with vanishing connection their linearised equations are given in the paragraph on left-invariant backgrounds with torsion later in this section.
  ```

  The anchor occurs once in the file and is the last sentence of its line. Everything else on L1581 is kept.
* **Edit 2 (m1).** Insert the block `appH_insert_r2.tex`, followed by one blank CRLF line, immediately before the
  unique line `\section{Problem E: signature}`. That puts it directly after the paragraph `\paragraph{The locked
  frame as a gauge-invariant composite (conditional; not closure).}`, whose last sentence is "Problems~D, F and~N
  remain open and PROGRAMME-CONDITIONAL." Nothing is removed.
* **Post-image.** sha256 `6a72a3268302d46b9b5d3ede69f8b15e838a0a3c14bfddc2e1b4e8ab58b39a7c`, 719947 bytes, CRLF
  throughout.
* **Labels referenced.** Each is defined once: `eq:Smatrix`, `ass:frame-lock`, `ass:nondeg`, `ass:lorentzian`,
  `ass:local-lorentz`, `ass:EFT-a2`. No new labels.
* **Citations.** `FurutaHanadaKawaiKimura2007` (in the bib) and `NielsenOlesen1978` (new).

The block below is the content of `appH_insert_r2.tex`; the file is authoritative for bytes.

```latex
\paragraph{First-order equivariant class on left-invariant backgrounds with torsion: the linearised frame and connection equations (conditional; not closure).}
Take the class with base a four-dimensional Lie group \(G\), vanishing background connection and \(\mathbb D_a=u_a{}^bE_b\), where the \(E_a\) are left-invariant fields with \([E_a,E_b]=\mathsf c_{ab}{}^dE_d\), as in the part on commutant labels at nonzero torsion of the paragraph on one loop about commuting matrices. In section values \(\mathsf R=0\), \(\mathsf F=0\) and \(\mathsf T=-\mathsf c\). This is the torsion of the vanishing connection of the class, not of the Levi-Civita connection of the frame; the convention of the compact toy above, in which the equivariant lifts of a torsion-free connection have \(\mathsf T=0\), is unchanged. The background solves the matrix equation when \(\eta^{ac}\mathsf c_{ab}{}^d\mathsf c_{cd}{}^e=0\). Let
\[
\mathsf F_{ab}[A]=E_aA_b-E_bA_a-\mathsf c_{ab}{}^dA_d,\qquad
\mathcal Q_b[A]=E^a\mathsf F_{ab}[A]+\mathsf c_{ab}{}^c\mathsf F^a{}_c[A],
\]
the linearised third bracket, that is the equation of the order-zero field \(A_a\) of the class on this background, which is invariant under \(A_b\to A_b+E_b\Lambda\). Let \(\rho_I\) be the right-invariant fields on \(G\), which commute with all \(\mathbb D_a\) and \(\mathcal S_{cd}\), and write \(E_c=\mathsf L_c{}^I\rho_I\), with \(\mathsf L\) an invertible matrix of functions. For \(\mathbb D_a\to\mathbb D_a-h_a{}^c\mathbb D_c+\tfrac12\omega_a{}^{cd}\mathcal S_{cd}\) with arbitrary functions \(h\) and \(\omega\) on \(G\), the linearised first two brackets of the matrix equation are
\[
\mathcal E^{(2)}{}_b{}^{de}=\mathcal Q_b[\omega^{de}],\qquad
\mathcal E^{(1)}{}_b{}^e\big|_{\omega=0}=\mathcal Q_b[f^I]\,(\mathsf L^{-1})_I{}^e,\qquad
f_b{}^I=-h_b{}^c\mathsf L_c{}^I,
\]
with \(\omega^{de}\) the one-form with components \(\omega_a{}^{de}\). The first holds because, about this background, the linearised curvature is \(\mathsf R_{ab}{}^{de}=\mathsf F_{ab}[\omega^{de}]\) and contains no \(h\); the second is the adjoint compatibility of the paragraph on the pairing of the action, for \(\mathcal C=\rho_I\). Both were checked symbolically for arbitrary \(h\) and \(\omega\) on flat space, on the null-rotation algebra and the second algebra of the paragraph on one loop about commuting matrices, and on the Heisenberg algebra below. So on every such background the forty equations are block-triangular, the connection sourcing the frame, and each of the six components \(\omega^{de}\) and each of the four frame labels \(f^I\) obeys the equation \(\mathcal Q\) of the order-zero field. In particular the Lorentz modes that stop being commutant at \(\mathsf c\neq0\) obey the gauge-invariant equation \(\mathcal Q\); no term breaking \(A_b\to A_b+E_b\Lambda\) appears. At generic characters the kernel of the forty equations is the ten gauge directions (numerical, on the three algebras with \(\mathsf c\neq0\)). Whether such a background gaps the torsion modes is therefore the question whether it gaps \(\mathcal Q\). On flat space and on the null-rotation background in the gauge with constant frame below, moreover, every constant matrix \(G\) for which \(G\) times the forty linearised equations is formally self-adjoint vanishes on the frame equations (numerical), so no constant recombination of these equations is the Euler--Lagrange system of a quadratic Lagrangian in \(h\) and \(\omega\) with constant coefficients; the ten Maxwell equations of the paragraph on the pairing of the action are in variables that contain \(y\) explicitly.

The null-rotation algebra solves the equation for \(\eta\) and not for the Euclidean contraction. The gauge with constant frame and \(\omega_a{}^{12}=\vartheta k_a\), \(k_a=(1,0,0,1)\), has the same torsion for \(\vartheta=-\tfrac12\), with \(\mathsf T_{abc}\mathsf T^{abc}=0\). There the characteristic roots of the forty equations in the character sectors lie on the real cones \((q+j\vartheta k)^2=0\), with multiplicities \(4\), \(6\) and \(2\) for \(j=0\), \(j=\pm1\) and \(j=\pm2\), twenty in all as at the flat point, and with chains of length at most three (roots numerical at \(\vartheta=-\tfrac12,\tfrac12,1,2\); chains numerical and ranks exact in rational arithmetic at sampled points for \(\vartheta=1\)). So these sectors have neither a gap nor a complex root. The Heisenberg algebra \([E_3,E_1]=\kappa E_2\), with \(\kappa>0\) and with \(E_0\) and \(E_2\) central, solves the equation for both contractions, since \(\mathrm{ad}_a\mathrm{ad}_c=0\) for all \(a,c\). Its frame metric is that of time times the Heisenberg group, and its torsion has \(\mathsf T_{abc}\mathsf T^{abc}=2\kappa^2\), vanishing trace and a nonzero totally antisymmetric part, the part read as the field strength of a \(B\)-field in~\cite{FurutaHanadaKawaiKimura2007}. In coordinates with \(E_0=\partial_0\), \(E_1=\partial_1+\tfrac12\kappa y^3\partial_2\), \(E_2=\partial_2\) and \(E_3=\partial_3-\tfrac12\kappa y^1\partial_2\), let \(p>0\), \(\phi=\exp\bigl(\mathrm iq_0y^0+\mathrm ipy^2-\tfrac14\kappa p((y^1)^2+(y^3)^2)\bigr)\) and \(A=(0,\phi,0,\mathrm i\phi)\). Then, exactly and for \(\eta\),
\[
\mathcal Q_b[A]=(q_0^2-p^2+\kappa p)\,A_b,\qquad\mathsf F_{32}[A]=p\,\phi,
\]
so \(A\), which is not a gauge direction, solves \(\mathcal Q[A]=0\) at \(q_0^2=p(p-\kappa)\), which is negative for \(0<p<\kappa\). At \(q_0=-\mathrm i\Gamma\), \(\Gamma=\sqrt{p(\kappa-p)}\le\kappa/2\) with equality at \(p=\kappa/2\), the real part of \(A\) is a real solution growing like \(\mathrm e^{\Gamma y^0}\); it is Gaussian in \(y^1,y^3\), and its superpositions over \(p\) in a closed subinterval of \((0,\kappa)\) are square-integrable on each slice of constant \(y^0\). By the reduction, for each right-invariant label \(J\) the frame fluctuation with \(f_b{}^I=A_b\delta^I{}_J\) solves the linearised first two brackets with nonzero linearised torsion (exact), and in the sector of fixed \(p\) the lowest level of the forty equations has ten times the multiplicity of that of \(\mathcal Q\) (numerical). In that sector the roots of \(\mathcal Q\) are \(q_0^2=p^2+\kappa p(2n+1\mp2)\), \(n\ge0\) (numerical), which has the form of the Landau levels of a charged vector field in a homogeneous magnetic field, with \(\kappa p\) in the place of the field; for that field an unstable mode is found in~\cite{NielsenOlesen1978}. For the Euclidean contraction the same \(A\) gives \(\mathcal Q[A]=-(q_0^2+p^2-\kappa p)A\), which vanishes at real \(q_0\) for \(0<p<\kappa\); no form is used, so no sign is attached to this.

These statements are for Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and no matter term, tree level, linear order in the fluctuation, left-invariant backgrounds with vanishing connection on a four-dimensional group and the contractions named, with the spectra stated only for the two unimodular examples. The growing modes are solutions of the linear equations; their nonlinear evolution, the regulated trace, the domains of the unbounded operators, loops and a norm are not treated. Nothing here shows that the matrix integral excludes the Heisenberg background, selects this class or its algebra \(\mathcal A\), or yields the frame and its non-degeneracy, so Assumptions~\ref{ass:frame-lock}, \ref{ass:nondeg}, \ref{ass:lorentzian}, \ref{ass:local-lorentz} and~\ref{ass:EFT-a2} are not discharged; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
```

### Bibliography (the integrator adds this to `bib/namcg.bib`; unchanged from r1)

```bibtex
@article{NielsenOlesen1978,
  author  = {Nielsen, N. K. and Olesen, P.},
  title   = {An Unstable {Yang--Mills} Field Mode},
  journal = {Nucl. Phys. B},
  volume  = {144},
  number  = {2-3},
  pages   = {376--396},
  year    = {1978},
  doi     = {10.1016/0550-3213(78)90377-2}
}
```

### Stale passages elsewhere

* **appH L1581.** Handled by edit 1 (m5).
* **appH L1557** ("background torsion zero ..."). Remains true as a bounded statement; the new paragraph extends it
  to the class with `T != 0` without editing it.
* **ch10 and ch17.** No stale statement.

## Verification scripts

All are in `proposals/068-d1-torsion-nonzero/` and run from that folder with `python -I`. Re-run this round: every
stored output is reproduced byte for byte.

| Command | Checks | Expected invariant output |
|---|---|---|
| `python -I v1_reduction_symbolic.py` | (R1), (R2) exact; negative controls | last line `ALL REDUCTION IDENTITIES EXACT: True` (identical to stored) |
| `python -I v2_heisenberg_unstable_mode.py` | exact mode, lifts, growth, delta | `(U1) ... True ; F_32 / phi = p`, four `(U2) ... True`, `(U3) ... Gamma there = kappa/2`, `(U4) ... True` (identical) |
| `python -I v3_forms_EL.py` | EL recombination | dims 21, 7, 42; generic rank 24; frame-column max < 1e-14 (identical) |
| `python -I v4_null_rotation_kappa.py` | r1 version (kappa = 1/2, 1, 2) | identical to stored r1 output |
| `python -I v5_crosscheck_core.py` | v1 against core | `max abs(v1 - core)` < 1e-14 (identical) |
| `python -I v4_null_rotation_vartheta_r2.py` | **new (m3)**: vartheta = -1/2, 1/2, 1, 2, `j` unrounded; exact ranks at -1/2 | four summary lines `total roots 40; ... all on cones: True; j -> multiplicities per crossing {-2: [2, 2], -1: [6, 6], 0: [4, 4], 1: [6, 6], 2: [2, 2]}`; at -1/2 `max abs(x - j) 1.4e-11`; exact ranks `30` generic and `28, 26, 26, 26, 28`; last line `ALL ROOTS ON CONES WITHOUT ROUNDING: True` |
| `python -I make_insert_r2.py` | builds `appH_insert_r2.tex` from r1 by the listed replacements | occurrence counts `1` (m2, m3a-e, m4, o1) and `4` (o2); `status sentences ('remain open'): 1`; block sha256 `b80bc4e3...6dc8`, bare LF 0 |
| `python -I -W error apply_and_build_r2.py --build` | pre hash, m5 anchor (unique, L1581, end of line), m1 anchor (unique, L1607, preceded by the composite paragraph), post hash, closers, labels, citations, build on a temporary copy outside the repo with bibtex | pre `8d1eb5dc...` True; post `6a72a326...9a7c`; labels defined 1; `pdflatex rc 0 pages 406` (twice); `undefined/multiply-defined warnings: 0`; `BUILD CLEAN`; `temp copy removed: True` (stored: `apply_and_build_r2_output.txt`) |
| `python -I gk_chk_v4_r1.py` | gatekeeper's check at vartheta = -1/2 | `-0.5 40 [...]` with `x` = -2, -1, 0, 1, 2 (twice), multiplicities 2, 6, 4, 6, 2, imaginary parts 0.0 |
| `python -I rerun.py s1_backgrounds.py` (and `s2`-`s4`) | unchanged from r1 | identical to stored |

## Decisions Taken

* **o1 adopted.** It replaces the informal phrase "acquire no term beyond those of a gauge field that keeps its gauge
  parameter" with the checkable statement that the modes obey the gauge-invariant `Q` and that no term breaking
  `A_b -> A_b + E_b Lambda` appears. `Lambda` is already introduced in the same paragraph. The resulting
  run-on sentence is split, so "At generic characters ..." starts a new sentence. No reason not to adopt.
* **o2: cheap relabel done.** In r1 three A's were in use:
  * the order-zero field `A_a`, of which the Heisenberg mode `A = (0, phi, 0, i phi)` is a value;
  * the left/right matrix `\mathsf A`;
  * the class algebra `\mathcal A`.

  The matrix is now `\mathsf L`, which is unused anywhere in `chapters/`. `\mathcal A` is the manuscript's notation
  for the algebra and is kept. The field and the mode are the same object, a solution of `Q[A] = 0`, so they share a
  letter. Rejected: renaming the field, because the integrated text calls it `A_a` (appH L1557, L1581).
* **v4 kept as r1 plus a new r2 script.** The r1 v4 file and its output are not modified, so the r1 record stays
  reproducible. `v4_null_rotation_vartheta_r2.py` adds `vartheta = -1/2`, the unrounded `j`, and the exact ranks.
* **Closer wording not changed.** The m1 move already separates the two identical status clauses by the whole
  block. Rewording the block's closer would depart from the gatekeeper-checked text and from the section's
  pattern.

## Milestone assessment

Routine. This is a derived sub-lemma of the D1 Missing step within a supplied class. It does not derive the class,
the frame or a norm.

## Status-label recommendation

* **Critical-path set** at the full-GR / matrix-derived scope (ch17; appH ledger labels): A, B, C, D (D1), E, F,
  G-derived and N, all OPEN.
* **Optional:** H, I and J, all OPEN.
* **Recommendation:** no label change. The edits touch no label; edit 1 changes a sentence inside a conditional
  paragraph, not a status passage.

## Author decision needed

None.

## Remaining open step

For the D1 target, the following must still be derived or supplied:

* from the matrix integral, that the class (algebra, frame, non-degeneracy) is selected;
* a norm or regulated trace for the torsion modes;
* the nonlinear fate of the Heisenberg instability, which is avenue 1 and positive-aimed: the second-order /
  Nielsen–Olesen-type endpoint;
* the analogue of `Q` on backgrounds with `R != 0` and `T != 0`, where (R1) acquires `R-bar` terms and a gap could
  first appear (avenue 2);
* one loop on these non-commuting backgrounds (avenue 3);
* the dynamics of the diagonal elements.

Further unimodular backgrounds with `R = 0` stay at the bottom of the list, because by (R1)-(R2) they only change
the spectrum of `Q`.

## Special instructions for the gatekeeper

* Check that m2-m4 and m5 are byte-verbatim against review-r1; `make_insert_r2.py` and `apply_and_build_r2.py`
  hold the strings.
* Check that o1 and o2 change no claim. o1 restates the corollary of (R1)-(R2). o2 is a pure relabel, four
  occurrences.
* Check that the m5 pointer is accurate: L1581 concerns commutant labels at nonzero torsion on left-invariant
  backgrounds, and the new paragraph treats exactly the backgrounds with vanishing connection.
* Must not be asserted: that background torsion never gaps the torsion modes (this holds only for this class, with
  `R = 0`); that the matrix integral excludes the Heisenberg background; any norm or ghost statement; any closure.
* The full scan is still owed under your disposition.
