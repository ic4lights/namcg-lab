# Proposal 068-d1-torsion-nonzero, round 1

## Result

Within the first-order equivariant class of appH `sec:status-D`, about **left-invariant backgrounds with torsion**
(base a four-dimensional Lie group G, vanishing background connection, `D_a = u_a^b E_b`, so `R = 0`, `F = 0`,
`T = -c`), the linearised dynamics of the full frame-plus-connection content (16 + 24 = 40 section fields) is
derived in closed form:

* **(R1)** the linearised second bracket is `E^(2)_b^{de} = Q_b[omega^{de}]`, with no frame field in it;
* **(R2)** the linearised first bracket at zero connection fluctuation is `E^(1)_b^e = Q_b[f^I] (A^{-1})_I^e`,
  `f_b^I = -h_b^c A_c^I`, where `E_c = A_c^I rho_I` relates left- and right-invariant fields;

with `Q_b[A] = E^a F_ab + c_ab^c F^a_c`, `F_ab[A] = E_a A_b - E_b A_a - c_ab^d A_d`, the linearised third bracket,
i.e. the equation of the class's order-zero gauge field `A_a`. Both identities are exact for arbitrary
fluctuation functions (sympy, four backgrounds). So the forty equations are block-triangular (connection sources
frame), and all ten components (six Lorentz components of omega, four right-invariant frame labels) obey the
**same** gauge-invariant operator `Q`. This answers the question that the integrated 052 text leaves open ("Whether
the remaining modes acquire a mass term of definite sign is not computed", appH L1581) for this class of
backgrounds: the Lorentz modes that stop being commutant at `c != 0` acquire no term beyond those of a gauge field
that keeps its gauge parameter.

Two derived spectral consequences on unimodular examples:

1. **Null-rotation background** (Lorentzian only): characteristic roots on the real shifted cones
   `(q + j kappa k)^2 = 0`, `j = 0, ±1, ±2`, multiplicities 4, 6, 2 (twenty in all, as at the flat point), Jordan
   chains of length at most three. No gap, no complex root (numerical; exact rational ranks at sampled points).
2. **Heisenberg background** `[E_3, E_1] = kappa E_2` (solves the equation for both contractions; torsion with
   nonzero totally antisymmetric part, the part read as a B-field strength in FHKK 2007): an **exact** solution
   `A = (0, phi, 0, i phi)`, `phi = exp(i q0 y0 + i p y2 - kappa p (y1^2 + y3^2)/4)`, of `Q[A] = (q0^2 - p^2 + kappa p) A`,
   so for `0 < p < kappa` the linearised equations have real solutions growing like `exp(Gamma y0)`,
   `Gamma = sqrt(p (kappa - p)) <= kappa/2`, normalisable on constant-`y0` slices after superposition in `p`; via (R2)
   the frame-label lifts of this mode solve the linearised first two brackets with nonzero linearised torsion
   (exact). The full sector spectrum of `Q` is `q0^2 = p^2 + kappa p (2n + 1 ∓ 2)` (numerical), the Landau-level
   form of a charged vector in a homogeneous magnetic field (cf. Nielsen–Olesen 1978). The Heisenberg torsion
   background is therefore **linearly unstable at tree level** within the class; no norm is used for this.

Also: on flat space and the null-rotation background no constant recombination of the forty linearised equations
is the Euler–Lagrange system of a constant-coefficient quadratic Lagrangian in `(h, omega)` (numerical).

What this is and is not. It is a positive, derivation-grade statement of the **torsion and connection dynamics at
T != 0** (part of the D1 Missing step: "Generator counting alone does not settle its torsion or propagating
modes"), within a stated background class, at tree level and linear order. It removes the hypothesis "background
torsion zero" from the masslessness statement of appH L1557 for this class, and supplies dynamical data relevant to
the selection edge (one torsion background is linearly unstable). It does **not** derive the class, its algebra,
the frame, non-degeneracy, a norm, the nonlinear fate of the instability or loops, and it closes nothing.

## Target and status

* Problem D (`sec:status-D`), sub-route D1. Ledger label (appH L716-720): "Status: OPEN. Priority: CRITICAL PATH.
  Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2 ... D remains OPEN and the matrix-derived criterion
  is unmet." Chapter 17 (ch17 L329-370): "CRITICAL PATH; OPEN"; D1 closure requires the omega, A_mu, B and ghost
  operators and resulting field content, and a derived locked frame; "it does not determine the dynamics of the
  independent diagonal connection B or whether torsion vanishes, propagates, or is massive."
* Missing step (appH L743-756): derive SO(3,1) from the matrix algebra ..., "derive the effective dynamics of the
  independent diagonal connection or retain it as unresolved field content. Generator counting alone does not
  settle its torsion or propagating modes. The locked frame and its non-degeneracy must also be derived ...".
* Target of this package: the torsion / connection propagating-mode dynamics on backgrounds with T != 0, in the
  first-order equivariant class (frontier edge `D1.torsion-T-nonzero`, rank 2; pathfinder plan 2026-11-21 item 2).
* Dependencies: D1 gates F, C and N (ch17 L650-660; appH L1804-1806); E supplies eta (not touched; E paused).
* Classification: **PROGRAMME-CONDITIONAL** (conditional on the supplied class and backgrounds). Not DERIVED for
  the original target.
* Discrepancies: none found between the appH ledger label and the ch17 D passage. The frontier record says
  "Serialize after the 059 edge" and "059 convention fixed first": 059 is integrated (appH L1599-1602); this
  package uses the class torsion of the vanishing connection, not the anholonomy of horizontal lifts, and says so,
  so it is consistent with the 059 convention (`T = 0` for equivariant lifts of a torsion-free connection).

## Source reading

Digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT` (digest marks
`dirty-chapters: yes`; appH is the only file changed relative to HEAD, live sha256 `8d1eb5dc...cfd41e`). Read in
full: appH L713-772 (ledger, Missing step, opening of the symmetries paragraph) and L1494-1606 (conjugate-coordinate
frame-index obstruction; the four first-order equivariant class paragraphs including the newly integrated 059
compact-toy block; the locked-frame composite paragraph); ch17 L320-370 (Problem D); ch10 in full (lines read
with long lines truncated at 400 characters; all of the chapter's statements on B and torsion, Proposition
`prop:B-torsion-free`, Theorem `thm:locking` and the bookkeeping table were read). Also read: `reports/graph/frontier.yaml`
(edge record), `reports/pathfinder/plan-2026-11-21.md`, `reports/ledger.md` 068 entry, adversary report
`reports/adversary/adversary-P-20261114-1705.md` findings F3-F5. Not a full scan; the proposal adds a conditional
paragraph and changes no definition, assumption, scope statement or status passage.

## Research and reasoning

### 0. What the stalled 068 round had computed (reconstruction)

`core.py`: numerical linearisation of the first two brackets (closed formulas of appH L1523) about
constant-coefficient backgrounds, on mode spaces where the frame acts by matrices (characters `E_a = i q_a`, or the
Schrödinger representation of the Heisenberg algebra); gauge directions; backgrounds flat, null rotation in two
gauges, Heisenberg, second algebra. `tools.py`: characteristic roots via two random compressions; partial
multiplicities. `t0`-`t6` are drafts superseded by `s1`-`s4`. Re-run under `python -I` (via `rerun.py`): `s1`-`s4`
outputs are byte-identical to the stored ones.

* s1: all backgrounds solve the equation (eta); null rotation and the second algebra fail for delta, Heisenberg
  solves for both; at generic characters kernel = the ten gauge directions (rank 30 + 10) on all of them (adversary
  F3 test passed: the non-derivative coefficients are not a lifting of modes modulo gauge).
* s2: roots and partial multiplicities (flat 8 simple + 6 double; null rotation cones `(q + jk)^2 = 0`; Heisenberg
  q_2 = 0 sector; second algebra complex roots `(q - i tau)^2 = 0`, tau the trace of T); exact rational ranks.
* s3: Heisenberg sectors of central momentum p: forty fields and order-zero field have levels
  `(q0^2 - p^2)/(kappa p) = 2n + 1 ∓ 2`, with forty-field multiplicities ten times those of A.
* s4: constant forms making M formally symmetric (only the w-block).

The stall point was the absence of an explanation of the factor ten and of the shifted cones. The new analytic step
below explains it.

### 1. The reduction (R1), (R2)

Background: `D_a = u_a^b E_b`, E_a left-invariant on G, `[E_a,E_b] = c_ab^d E_d`, vanishing connection. Then in
section values `T = -c`, `R = 0`, `F = 0` (appH L1581 already records `R = 0` and T built from c). Background
equation: `eta^{ac} c_ab^d c_cd^e = 0` (= `eta^{ac} ad_a ad_c = 0`, appH L1581).

(R1). Linearising `R_ab^f_c = e_a Om_bc^f - e_b Om_ac^f + Om Om - Om Om - C_ab^d Om_dc^f` about `Om = 0` gives
`dR_ab^{de} = E_a w_b^{de} - E_b w_a^{de} - c_ab^g w_g^{de} = F_ab[w^{de}]`, independent of h (the `C Om` term is
`c dOm` since `Om-bar = 0`). With `R-bar = 0`, `dE^(2) = E^a dR_ab - T-bar_ab^c dR^a_c = E^a F_ab + c_ab^c F^a_c =
Q_b[w^{de}]`.

(R2). Let rho_I be the right-invariant fields; `[rho_I, E_a] = 0`, and they do not act on u, so they commute with
all D_a and S_cd. If `delta D_b = f_b^I rho_I` (first order, no S part), then using only that rho_I commutes with
the background: `[E_a, f rho] = (E_a f) rho`, `[f rho, E_b] = -(E_b f) rho`,
`[f^a rho, [E_a, E_b]] = [f^a rho, c_ab^d E_d] = -c_ab^d (E_d f^a) rho`. Summing the three linear terms of
`[D^a,[D_a,D_b]]`: `(E^aE_a f_b - E^aE_b f_a - c_ab^d E_d f^a) rho`. Expanding `Q_b[f] = E^a F_ab + c_ab^c F^a_c` gives
the same expression plus `-c_ab^d c^a_d^e f_e`, which vanishes by the background equation. Hence the linearised
operator equation is `Q_b[f^I] rho_I`; writing `rho_I = (A^{-1})_I^e E_e` and `delta D_b = -h_b^c E_c` gives (R2).
This is the adjoint compatibility of appH L1541/L1581 applied to `C = rho_I`; the new point is that, since A is
invertible, the four right-invariant labels exhaust the frame fluctuations, and (R1) covers the six non-commutant
Lorentz components. Order-zero pieces (Hermitisation `½{f, rho}`, the term t, the field A) do not enter the first two
brackets (appH L1557), so they do not affect (R1)-(R2).

Verification: `v1_reduction_symbolic.py` re-implements the closed linearised formulas independently of `core.py` and
checks (R1), (R2) exactly with sympy undefined functions `h_b^c(y)`, `w_b^{cd}(y)` on flat space, Heisenberg, the
null-rotation group (explicit E(2) x R realisation) and the second algebra.

Consequences: block-triangular system; ten copies of the gauge-invariant `Q` (`Q[E Lambda] = 0` since
`F[E Lambda] = 0`); the gauge parameter of each w-copy is the omega-part of the local rotation. The characteristic
data of the forty equations are those of Q, up to Jordan chains created by the w -> h source when the two diagonal
blocks share roots (which is generic, since both are Q). This explains s3's factor ten and the flat-point count.

### 2. Null-rotation background

Same torsion in the left-invariant gauge and in the gauge with constant frame and `omega_a^{12} = kappa k_a`,
`kappa = -1/2` (s1, exact equality of T arrays). In the latter, roots on `(q + j kappa k)^2 = 0`, `j = 0, ±1, ±2`,
multiplicities 4, 6, 2, total 20 per crossing (s2 at kappa = 1; `v4` at kappa = 1/2, 1, 2);
partial multiplicities `[4,4,4,4]` (j = 0), `[4,5,6,6]` (j = ±1, one chain of length 3), `[2,2,2,2]` (j = ±2);
exact rational ranks 26, 26, 26, 28, 28 at sampled rational points. All roots real along real lines: no gap and no
complex root. (Reading the integer j as the J_12 weight of the components is an interpretation, not claimed.)

### 3. Heisenberg background: exact unstable mode

Coordinates: `E_0 = d0`, `E_1 = d1 + (kappa/2) y3 d2`, `E_2 = d2`, `E_3 = d3 - (kappa/2) y1 d2`; then
`[E_3, E_1] = kappa E_2`. In the sector `E_2 = i p`, `E_1 + i E_3` annihilates `exp(-kappa p (y1^2+y3^2)/4)`
(lowest Landau level). With `A = (0, phi, 0, i phi)`, by hand: `F_31 = 0`, `F_32 = p phi`, `F_12 = -i p phi`,
`F_01 = i q0 phi`, `F_03 = -q0 phi`, `F_02 = 0`; then `Q_1 = (q0^2 - p^2 + kappa p) phi`,
`Q_3 = i (q0^2 - p^2 + kappa p) phi`, `Q_0 = Q_2 = 0`. Checked exactly by `v2`. Since `F_32 != 0`, A is not a gauge
direction. At `q0^2 = p(p - kappa) < 0` (0 < p < kappa), `q0 = -i Gamma` gives growth `e^{Gamma y0}`; Q is a real
operator so the real part is a real solution; superpositions over p in a compact subinterval of (0, kappa) are
square-integrable on each `y0` slice (Fourier in y2, Gaussian of width bounded by the smallest p in y1, y3); Haar
measure is `d^4y` (unimodular). Max growth rate `kappa/2` at `p = kappa/2` (v2 U3). By (R2), `h = -f A^{-1}` with
`f_b^I = A_b delta^I_J` solves `dE^(1) = dE^(2) = 0` at the root for each J = 0..3, with nonzero linearised torsion
(v2 U2, exact). For delta: `Q[A] = -(q0^2 + p^2 - kappa p) A` (v2 U4).

Remaining Landau levels: s3 Part B gives `(q0^2 - p^2)/(kappa p) = -1, 1, 3, 5, ...` with counts 2, 2, 4, 4, ...
(both signs of q0), i.e. `q0^2 = p^2 + kappa p (2n + 1 ∓ 2)`; numerical (rows on all oscillator levels, columns cut,
so no truncation defect). s3 Part A: forty-field multiplicities ten times those of A on the levels below the cut.

Literature. Nielsen and Olesen, Nucl. Phys. B 144 (1978) 376-396, DOI 10.1016/0550-3213(78)90377-2: record verified
via Crossref; abstract (INSPIRE) verified to state an unstable mode of a charged vector field in an external
homogeneous magnetic field. The Landau-level formula with gyromagnetic ratio two is the standard reading of that
paper and is **not independently verified** beyond the abstract; the insert only says "has the form of the Landau
levels ... for that field an unstable mode is found in". FurutaHanadaKawaiKimura2007 is already in the bib and
the B-field reading of the antisymmetric torsion is already attributed to it in appH L1527; reused, not re-verified.

### 4. Euler–Lagrange test (bears on adversary F5)

`v3_forms_EL.py`: constant 40 x 40 G with `G M` formally self-adjoint (`(G M0)^T = G M0`, `(G M1)^T = -G M1`,
`(G M2)^T = G M2`). Solution spaces of dimension 21 (flat), 7 (null rotation), 42 (Heisenberg, characters in
directions 0,1,3 only); every member vanishes on the 16 frame-equation columns (max 1.6e-15) and has rank at most 24.
So no constant recombination of the forty equations is an Euler–Lagrange system of a constant-coefficient local
quadratic Lagrangian in (h, omega) on flat and null-rotation backgrounds. This explains why the published ghost
conditions for local Lagrangians quadratic in T and R (adversary F5's hypothesis class) do not apply directly; the
insert states only the numerical fact. (s4 tested the different condition `G M = M^T G`; same conclusion.)

### 5. Fork record (author directive 2026-10-15)

The no-mass part is a bounded statement: hypotheses (a) tree level, (b) linear order, (c) left-invariant
backgrounds with vanishing connection, (d) first-order equivariant fluctuations, (e) first two brackets, (f) no
matter term, `C = 0`. Avenues:

1. (positive-aimed, rank 1) **Nonlinear/selection use of the Heisenberg instability**: follow the unstable Landau
   mode to second order (Nielsen–Olesen-type condensate) and test whether the matrix equation has a lower-action or
   stable endpoint with torsion; this feeds `D1.selection-of-class` with derived data. Transfers: the exact mode and
   the reduction.
2. (positive-aimed, rank 2) **Backgrounds with curvature and torsion** (`R != 0`, e.g. de Sitter `SO(4,1)` with the
   bilinear term, appH L1525/L1555, deformed by torsion): (R1) fails there because `R-bar` enters; compute the
   analogue of Q. This is where a derived mass or gap could first appear.
3. (positive-aimed, rank 3) **One loop at T != 0**: the commuting-background vanishing (appH L1577) does not apply
   since the Heisenberg and null-rotation backgrounds have nonzero commutators; the supertrace second-order term on
   these backgrounds is computable with (R1)-(R2) reducing it to ten copies of Q.
4. (bottom; same-no-go class) further unimodular left-invariant backgrounds with R = 0: by (R1)-(R2) every one gives
   ten copies of its Q, so only the spectrum of Q changes; no mass term can appear in this class. Not proposed.

## Claim classification

| Claim | Class |
|---|---|
| (R1) `dE^(2) = Q[omega^{de}]`, (R2) `dE^(1)|_{w=0} = Q[-hA] A^{-1}` for arbitrary h, w, on any left-invariant background with vanishing connection solving the equation | established (derivation in §1; exact symbolic check on four backgrounds) |
| block-triangular structure; ten copies of Q; non-commutant Lorentz modes acquire no term beyond the gauge field's | established (corollary) |
| kernel at generic characters = ten gauge directions on the three algebras with c != 0 | numerical |
| no constant EL recombination (flat, null rotation) | numerical |
| null-rotation: same torsion in the two gauges | numerical (exact equality of arrays) |
| null-rotation roots on `(q + j kappa k)^2 = 0`, multiplicities, chain lengths | numerical (exact rational ranks at sampled points, kappa = 1) |
| Heisenberg solves for eta and delta (`ad_a ad_c = 0`) | established |
| Heisenberg torsion data `T^2 = 2 kappa^2`, trace 0, axial part nonzero (`-kappa/3` for T_[123]) | established (by hand; numerical check) |
| exact mode `Q[A] = (q0^2 - p^2 + kappa p) A`, `F_32 = p phi` | established (by hand; sympy) |
| growth `e^{Gamma y0}`, `Gamma <= kappa/2`; normalisable superpositions | established |
| frame-label lifts solve the linearised first two brackets with `dT != 0` | established (sympy, exact) |
| full Landau spectrum `q0^2 = p^2 + kappa p (2n+1 ∓ 2)`; forty-field multiplicity ten times | numerical |
| Nielsen–Olesen comparison | conjecture-level analogy, literature verified at abstract level |
| the class, its algebra, frame, non-degeneracy, selection; norm; nonlinear fate; loops | unresolved |

## Proposed changes

### File `chapters/appH-microscopic-proofs.tex` (only file changed)

* Live pre-image sha256: `8d1eb5dccd6c808feb0bfbc935b5d5d0444dbfd8a46ac9c56c56519d07cfd41e` (712252 bytes).
* Anchor (verified unique, line 1604, preceded by a blank CRLF line):
  `\paragraph{The locked frame as a gauge-invariant composite (conditional; not closure).}`
* Action: insert the block `appH_insert_r1.tex` (7277 bytes, CRLF, UTF-8 without BOM, sha256
  `4f64732b250d1cfe0884996757eadd112e6d712a7f3dd2b911b5e336867ed92f`) followed by one blank CRLF line immediately
  before the anchor, i.e. directly after the 059 paragraph "First-order equivariant class on a compact toy ...",
  whose last sentence ends "... so Assumptions~\ref{ass:frame-lock}, \ref{ass:nondeg} and~\ref{ass:local-lorentz}
  are not discharged." Nothing is removed or replaced; all existing text is kept.
* Post-image sha256: `08bc659e6f37446c700d2ef9757aca76dfe96ae84688d40e0d5b756e4791b543` (719531 bytes, no bare LF).
* Labels referenced (each defined once in `chapters/*.tex`): `eq:Smatrix`, `ass:frame-lock`, `ass:nondeg`,
  `ass:lorentzian`, `ass:local-lorentz`, `ass:EFT-a2`. No new labels.
* Citations: `FurutaHanadaKawaiKimura2007` (in bib), `NielsenOlesen1978` (new; `bib-additions-r1.bib`).

```latex
\paragraph{First-order equivariant class on left-invariant backgrounds with torsion: the linearised frame and connection equations (conditional; not closure).}
Take the class with base a four-dimensional Lie group \(G\), vanishing background connection and \(\mathbb D_a=u_a{}^bE_b\), where the \(E_a\) are left-invariant fields with \([E_a,E_b]=\mathsf c_{ab}{}^dE_d\), as in the part on commutant labels at nonzero torsion of the paragraph on one loop about commuting matrices. In section values \(\mathsf R=0\), \(\mathsf F=0\) and \(\mathsf T=-\mathsf c\). This is the torsion of the vanishing connection of the class, not of the Levi-Civita connection of the frame; the convention of the compact toy above, in which the equivariant lifts of a torsion-free connection have \(\mathsf T=0\), is unchanged. The background solves the matrix equation when \(\eta^{ac}\mathsf c_{ab}{}^d\mathsf c_{cd}{}^e=0\). Let
\[
\mathsf F_{ab}[A]=E_aA_b-E_bA_a-\mathsf c_{ab}{}^dA_d,\qquad
\mathcal Q_b[A]=E^a\mathsf F_{ab}[A]+\mathsf c_{ab}{}^c\mathsf F^a{}_c[A],
\]
the linearised third bracket, that is the equation of the order-zero field \(A_a\) of the class on this background, which is invariant under \(A_b\to A_b+E_b\Lambda\). Let \(\rho_I\) be the right-invariant fields on \(G\), which commute with all \(\mathbb D_a\) and \(\mathcal S_{cd}\), and write \(E_c=\mathsf A_c{}^I\rho_I\), with \(\mathsf A\) an invertible matrix of functions. For \(\mathbb D_a\to\mathbb D_a-h_a{}^c\mathbb D_c+\tfrac12\omega_a{}^{cd}\mathcal S_{cd}\) with arbitrary functions \(h\) and \(\omega\) on \(G\), the linearised first two brackets of the matrix equation are
\[
\mathcal E^{(2)}{}_b{}^{de}=\mathcal Q_b[\omega^{de}],\qquad
\mathcal E^{(1)}{}_b{}^e\big|_{\omega=0}=\mathcal Q_b[f^I]\,(\mathsf A^{-1})_I{}^e,\qquad
f_b{}^I=-h_b{}^c\mathsf A_c{}^I,
\]
with \(\omega^{de}\) the one-form with components \(\omega_a{}^{de}\). The first holds because, about this background, the linearised curvature is \(\mathsf R_{ab}{}^{de}=\mathsf F_{ab}[\omega^{de}]\) and contains no \(h\); the second is the adjoint compatibility of the paragraph on the pairing of the action, for \(\mathcal C=\rho_I\). Both were checked symbolically for arbitrary \(h\) and \(\omega\) on flat space, on the null-rotation algebra and the second algebra of the paragraph on one loop about commuting matrices, and on the Heisenberg algebra below. So on every such background the forty equations are block-triangular, the connection sourcing the frame, and each of the six components \(\omega^{de}\) and each of the four frame labels \(f^I\) obeys the equation \(\mathcal Q\) of the order-zero field. In particular the Lorentz modes that stop being commutant at \(\mathsf c\neq0\) acquire no term beyond those of a gauge field that keeps its gauge parameter, and at generic characters the kernel of the forty equations is the ten gauge directions (numerical, on the three algebras with \(\mathsf c\neq0\)). Whether such a background gaps the torsion modes is therefore the question whether it gaps \(\mathcal Q\). On flat space and on the null-rotation background, moreover, every constant matrix \(G\) for which \(G\) times the forty linearised equations is formally self-adjoint vanishes on the frame equations (numerical), so no constant recombination of these equations is the Euler--Lagrange system of a quadratic Lagrangian in \(h\) and \(\omega\) with constant coefficients.

The null-rotation algebra solves the equation for \(\eta\) and not for the Euclidean contraction. The gauge with constant frame and \(\omega_a{}^{12}=\kappa k_a\), \(k_a=(1,0,0,1)\), has the same torsion for \(\kappa=-\tfrac12\), with \(\mathsf T_{abc}\mathsf T^{abc}=0\). There the characteristic roots of the forty equations in the character sectors lie on the real cones \((q+j\kappa k)^2=0\), with multiplicities \(4\), \(6\) and \(2\) for \(j=0\), \(j=\pm1\) and \(j=\pm2\), twenty in all as at the flat point, and with chains of length at most three (roots numerical at \(\kappa=\tfrac12,1,2\); chains numerical and ranks exact in rational arithmetic at sampled points for \(\kappa=1\)). So these sectors have neither a gap nor a complex root. The Heisenberg algebra \([E_3,E_1]=\kappa E_2\), with \(E_0\) and \(E_2\) central, solves the equation for both contractions, since \(\mathrm{ad}_a\mathrm{ad}_c=0\) for all \(a,c\). Its frame metric is that of time times the Heisenberg group, and its torsion has \(\mathsf T_{abc}\mathsf T^{abc}=2\kappa^2\), vanishing trace and a nonzero totally antisymmetric part, the part read as the field strength of a \(B\)-field in~\cite{FurutaHanadaKawaiKimura2007}. In coordinates with \(E_0=\partial_0\), \(E_1=\partial_1+\tfrac12\kappa y^3\partial_2\), \(E_2=\partial_2\) and \(E_3=\partial_3-\tfrac12\kappa y^1\partial_2\), let \(p>0\), \(\phi=\exp\bigl(\mathrm iq_0y^0+\mathrm ipy^2-\tfrac14\kappa p((y^1)^2+(y^3)^2)\bigr)\) and \(A=(0,\phi,0,\mathrm i\phi)\). Then, exactly and for \(\eta\),
\[
\mathcal Q_b[A]=(q_0^2-p^2+\kappa p)\,A_b,\qquad\mathsf F_{32}[A]=p\,\phi,
\]
so \(A\), which is not a gauge direction, solves \(\mathcal Q[A]=0\) at \(q_0^2=p(p-\kappa)\), which is negative for \(0<p<\kappa\). At \(q_0=-\mathrm i\Gamma\), \(\Gamma=\sqrt{p(\kappa-p)}\le\kappa/2\) with equality at \(p=\kappa/2\), the real part of \(A\) is a real solution growing like \(\mathrm e^{\Gamma y^0}\); it is Gaussian in \(y^1,y^3\), and its superpositions over \(p\) in a closed subinterval of \((0,\kappa)\) are square-integrable on each slice of constant \(y^0\). By the reduction, for each right-invariant label \(J\) the frame fluctuation with \(f_b{}^I=A_b\delta^I{}_J\) solves the linearised first two brackets with nonzero linearised torsion (exact), and in the sector of fixed \(p\) the lowest level of the forty equations has ten times the multiplicity of that of \(\mathcal Q\) (numerical). In that sector the roots of \(\mathcal Q\) are \(q_0^2=p^2+\kappa p(2n+1\mp2)\), \(n\ge0\) (numerical), which has the form of the Landau levels of a charged vector field in a homogeneous magnetic field, with \(\kappa p\) in the place of the field; for that field an unstable mode is found in~\cite{NielsenOlesen1978}. For the Euclidean contraction the same \(A\) gives \(\mathcal Q[A]=-(q_0^2+p^2-\kappa p)A\), which vanishes at real \(q_0\) for \(0<p<\kappa\); no form is used, so no sign is attached to this.

These statements are for Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and no matter term, tree level, linear order in the fluctuation, left-invariant backgrounds with vanishing connection on a four-dimensional group and the contractions named, with the spectra stated only for the two unimodular examples. The growing modes are solutions of the linear equations; their nonlinear evolution, the regulated trace, the domains of the unbounded operators, loops and a norm are not treated. Nothing here shows that the matrix integral excludes the Heisenberg background, selects this class or its algebra \(\mathcal A\), or yields the frame and its non-degeneracy, so Assumptions~\ref{ass:frame-lock}, \ref{ass:nondeg}, \ref{ass:lorentzian}, \ref{ass:local-lorentz} and~\ref{ass:EFT-a2} are not discharged; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.
```

(The fenced block is the content of `appH_insert_r1.tex`; the file is authoritative for bytes.)

### Bibliography (integrator adds to `bib/namcg.bib`)

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

* appH L1581 ("Whether the remaining modes acquire a mass term of definite sign is not computed.") is now answered
  for left-invariant backgrounds with vanishing connection by the new paragraph, which refers back to it. The
  sentence remains true as a statement about that paragraph's content and is **kept**; no replacement proposed
  (smallest change).
* appH L1557 ("That is a bounded statement: quadratic order, background torsion zero, ...") remains true; the new
  paragraph extends it to the stated T != 0 class without editing it.
* ch10, ch17: no stale statement (both say torsion dynamics open; still open in general).

## Verification scripts

All in `proposals/068-d1-torsion-nonzero/`. Under `python -I` the script folder is not on `sys.path`; `v2`, `v3`
and `apply_and_build_r1.py` insert it themselves, the older scripts are run through `rerun.py`.

| Command | Checks | Expected invariant output |
|---|---|---|
| `python -I v1_reduction_symbolic.py` | (R1), (R2) exactly for arbitrary h, w on flat, Heisenberg, null rotation, second algebra; constancy of c; `[rho, E] = 0`; background equation | each background: `(R1) ... True`, `(R2) ... True`; negative controls on Heisenberg and null rotation print `False ; ... False` (identity fails with A replaced by 1; the frame bracket does depend on w); last line `ALL REDUCTION IDENTITIES EXACT: True` (stored: `v1_reduction_symbolic_output.txt`; about 40 s) |
| `python -I v5_crosscheck_core.py` | v1's independent symbolic linearisation agrees with `core.M_of_q` on characters (flat, Heisenberg) | `max |v1 - core|` below 1e-14 for both |
| `python -I v2_heisenberg_unstable_mode.py` | exact mode, frame-label lifts, growth rate, delta contraction | `(U1) ... True ; F_32 / phi = p`; four `(U2) label J = j: ... True ; linearised torsion nonzero: True`; `(U3) ... p = [kappa/2] ; Gamma there = kappa/2`; `(U4) ... True` |
| `python -I v3_forms_EL.py` | EL recombination test | dims 21, 7, 42; rank of generic member 24; max on frame-equation columns < 1e-14 |
| `python -I rerun.py s1_backgrounds.py` | backgrounds, gauge kernel | identical to `s1_backgrounds_output.txt` (rank 30 + gauge 10, `True`, on all; delta residual 0.5 for null rotation, 0 for Heisenberg) |
| `python -I rerun.py s2_spectrum.py` | roots, partial multiplicities, exact ranks | identical to `s2_spectrum_output.txt` (null rotation multiplicities 2,6,4,6,2 at j = 2,1,0,-1,-2 per crossing; `[4, 5, 6, 6]` at j = ±1; exact ranks 28,26,26,26,28) |
| `python -I rerun.py s3_heisenberg_landau.py` | Landau levels for forty fields and A | identical to `s3_heisenberg_landau_output.txt` (levels -1, 1, 3, ...; A counts 2,2,4,4; forty-field counts 20,20,40) |
| `python -I rerun.py s4_forms.py` | forms with `G M = M^T G` | identical to `s4_forms_output.txt` |
| `python -I apply_and_build_r1.py --build` | pre/post hashes, labels, citations; build on a temporary copy outside the repo with bibtex | pre `8d1eb5dc...`, post `08bc659e...`, labels defined 1, `BUILD CLEAN`, `temp copy removed: True` (stored: `apply_and_build_r1_output.txt`; 406 pages) |

| `python -I v4_null_rotation_kappa.py` | null-rotation roots for kappa = 1/2, 1, 2 on the line of s2 | each kappa: `total roots 40; all real: True; j -> multiplicities per crossing {-2: [2, 2], -1: [6, 6], 0: [4, 4], 1: [6, 6], 2: [2, 2]}` (stored: `v4_null_rotation_kappa_output.txt`) |

## Decisions Taken

* **Package or not.** Decided to submit: the headline is a closed-form derivation of the linearised torsion and
  connection dynamics on T != 0 backgrounds (R1-R2) and an exact dynamical instability of one torsion background,
  i.e. positive data on the D1 Missing step's "torsion or propagating modes" and input for the selection edge. The
  no-mass part is reported as a consequence, not the headline. Rejected: holding the computation as a
  bounded-no-go extension only (it is not only that), and the 059-recommended Krein-form de Sitter realisation
  (different edge; not started here).
* **Placement.** After the 059 compact-toy paragraph and before the locked-frame composite paragraph, so that the
  first-order equivariant class paragraphs stay contiguous and the 059 convention is stated before it is used.
  Rejected: inserting between the 052 and 059 paragraphs (would split 059 from its convention context).
* **Notation.** `\mathcal Q` for the order-zero operator (unused in `sec:status-D`; `\mathcal M` is used at L1568
  for a different operator). Linearised brackets named `\mathcal E^{(1)}`, `\mathcal E^{(2)}` as at L1549.
* **Second algebra.** Reductions stated for it; spectra not (non-unimodular: Ad(g) carries exponentials, which
  explains the complex roots `(q - i tau)^2 = 0` of s2 as a sector shift, not a mass; not put in the text).
* **No norm.** The instability is stated as growth of solutions; no sign of a form is quoted (adversary F4).

## Milestone assessment

Routine. A derived sub-lemma of the D1 Missing step within a supplied class; it does not derive the class, the
frame or a norm, so no critical-path step is derived from the matrix theory without unsupported inputs.

## Status-label recommendation

Current critical-path set at the full-GR / matrix-derived scope (ch17; appH ledger labels L16, L158, L552, L717,
L1611, L1803, L2988, L3430): A, B, C, D (D1), E, F, G-derived, N, all OPEN. Optional: H, I, J, all OPEN. No label
change is recommended. OPEN counts: 8 critical-path OPEN, 3 optional OPEN, 11 OPEN in total.

## Author decision needed

None.

## Remaining open step

For the D1 target: derive from the matrix integral that the class (algebra, frame, non-degeneracy) is selected; a
norm or regulated trace for the torsion modes; their fate beyond linear order (in particular the endpoint of the
Heisenberg instability); backgrounds with both curvature and torsion, where (R1) acquires `R-bar` terms and a gap
could appear; one loop on these non-commuting backgrounds (the commuting-background vanishing does not apply);
the dynamics of the diagonal elements. Ranked avenues in §5.

## Special instructions for the gatekeeper

* Re-derive (R1) from the R formula of appH L1523 and (R2) from the adjoint-compatibility argument of §1; check the
  use of the background equation to drop `c_ab^d c^a_d^e f_e`.
* Check the 059 consistency: the torsion here is that of the vanishing connection of the class (equivariant lift
  `u E` with omega = 0), not the anholonomy of horizontal lifts of a torsion-free connection.
* Check the exact mode by hand (§3) and that "not a gauge direction" rests on `F_32 = p phi != 0`.
* Must not be asserted: that background torsion never gaps torsion modes (only this class, R = 0); that the
  Heisenberg background is excluded by the matrix integral; any norm/ghost statement; that the Nielsen–Olesen
  analogy is an identification; any closure.
* The second algebra spectra are deliberately not stated.
