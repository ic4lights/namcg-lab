# Proposal 114-d1-locked-ghost-sector-spec, round 1

Target: Problem D1 (operator-specification deliverable) within the Problem D host
entry of Appendix H. Dispatch: R114, single target, derivation-first directive.

## Result

For the Presentation-B locked block (the only domain where D1's operator content
is presently definable, imposed local Lorentz symmetry under
Assumption `ass:local-lorentz`), package 114 derives the Faddeev--Popov (FP)
ghost operator of the local-Lorentz sector exactly:

1. **Pointwise-gauge lemma (derived).** The transformation law `eq:Phi-transform`
   (ch03 L279-284: `\Phi^I{}_A(x) |-> \Omega^I{}_J(x)\Phi^J{}_B(x)\Lambda^B{}_A(x)`)
   contains no derivative of `\Omega(x)` or `\Lambda(x)`. Hence the gauge actions
   on `\Phi` (internal, local Lorentz, and the locked diagonal combination) are
   pointwise on field space, and the FP operator of any gauge fixing of these
   groups has derivative order equal to that of the fixing functional: a
   zeroth-order fixing yields a ghost operator that is a **field endomorphism**,
   not a kinetic operator.
2. **Exact FP determinant for the antisymmetric Lorentz gauge (derived).** Fixing
   `F := antisym(eta Phi) = 0` about the vacuum `eq:VEV`, the ghost map
   `a |-> antisym(eta Phi eta a)` on the 6-dim space of `\eta`-antisymmetric
   `a := eta lambda` has, for `\Phi` with characteristic roots `r_i`,
   `det M(Phi) = (1/64) prod_{i<j} (r_i + r_j)`, and this equals the
   class-function polynomial
   `-(E1^2 E4 - E1 E2 E3 + E3^2)/64` in the characteristic-polynomial
   coefficients `E_i` of `\Phi` (so `det M` depends on all of `E_1..E_4`, and is
   **not** a function of `det Phi` alone: witness `\Phi = diag(2,1/2,1,1)` gives
   `405/256` at `det Phi = 1`). Vacuum value `det M(v I) = v^6 != 0`: the chosen
   slice is transverse to the gauge orbit at the vacuum. Logarithmic linear
   response at the vacuum: `delta ln det M = (3/(2v)) tr delta Phi`, a tadpole
   for the locking potential. Degeneracy locus: `det M = 0` iff `r_i + r_j = 0`
   for some pair; in particular the `eta`-orthogonal frame `v.Rot(pi/2)` obtained
   from the vacuum by a `\pi/2` spatial rotation is a zero, so the fixing is
   admissible only on a field-space patch free of such frames (Gribov-type
   copies inside the compact `SO(3)` subgroup).
3. **Sector-sum consequence (conditional corollary of 1-2).** Because these FP
   operators are endomorphism fields, the corresponding ghost integrals are
   pointwise and exact (no momentum integration, no regulator), contribute only
   derivative-free local functionals `\int d^4x ln det M(Phi(x))` to the
   path-integral exponent, and **do not enter the weighted sector sum of
   `thm:Geff` as kinetic operators**. Combined with two recorded facts of the
   same section - the quadratic action has no linearised diffeomorphism
   invariance (appH L1191-1192) and, with `g^(0)` fixed, the invariance of
   `eq:Smicro` under diffeomorphisms is exhibited only for those that preserve
   `g^(0)`, such as its isometries, which does not exclude other symmetries
   (appH L1201-1209) - among the symmetries exhibited for the displayed action
   at the orders recorded above, no kinetic ghost operator other than that of
   the diffeomorphism sector arises, and that ghost is a supplied input of the
   infrared sector, not a consequence of `eq:Smicro`.

This specifies the ghost-operator entry that ch17 requires D1 to supply (and
that the Problem F gap at appH L1954-1958 lists as unspecified), for the
local-Lorentz sector of the locked block, and records the endomorphism status of
all pointwise-sector ghosts. It does NOT close D1, D or F: the locked frame
existence/non-degeneracy deliverable and the derivation of `SO(3,1)` from the
matrix algebra (D1(a)/(c)) are untouched, and the manuscript's own sentence
"specifying the full operator content does not close D" (appH L803-804) is
honored.

## Target and status

- Problem **D** (Appendix H, `sec:status-D`, L765-766). Ledger label passage,
  verbatim (appH L769-772): "Status: OPEN. Priority: CRITICAL PATH. Completion:
  PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz
  symmetry, supports only a scope-limited Presentation-B model; D remains OPEN
  and the matrix-derived criterion is unmet."
- D missing step, verbatim (appH L795-808, tail): "Derive SO(3,1) from the
  matrix algebra alone, or state that Presentation A is not ontologically prior
  (the present text does the latter), and derive the effective dynamics of the
  independent diagonal connection or retain it as unresolved field content.
  Generator counting alone does not settle its torsion or propagating modes.
  The locked frame and its non-degeneracy must also be derived rather than
  assumed (Assumptions ref{ass:frame-lock} and ref{ass:nondeg}). Under D2, only
  explicitly scope-limited Presentation-B claims are available; specifying the
  full operator content does not close D or meet the matrix-derived criterion."
- D1 deliverable, verbatim (ch17 L337-341): "D1 closure requires the
  \(\omega\), \(A_\mu\), \(B\), and ghost operators and the resulting field
  content to be specified. D1 closure also requires that the locked frame exist
  and be non-degenerate on the claimed domain, derived from the same microscopic
  data rather than taken from Assumptions ref{ass:frame-lock} and
  ref{ass:nondeg}." Order-of-work item (ch17 L653-656) and completion item 4
  (ch17 L715-719) mirror this ("specify the \(\omega,A_\mu,B\) and ghost
  operators needed by Problem F"; "the \(\omega,A_\mu,B\) and ghost operators
  specified and the field content stated").
- D1 has no separate Appendix H status block; D1 is referenced inside the
  Problem D section at appH L754, L918, L1071, L1655. L1655 records that the
  gauge-invariant-composite reading "presupposes the connection content that the
  closure of Problem D1 in Chapter ch:agenda requires to be specified".
- Dependencies consumed: `eq:Phi-transform`, `eq:VEV`, `ass:local-lorentz`,
  `prop:goldstone-count` (six broken generators matched by the 6-component
  fixing), the recorded quadratic-order facts of the completed-action test
  paragraph (appH L1151-1199), the diffeomorphism paragraph (appH L1201ff),
  `ass:aux-metric`, `eq:Smicro`, `thm:Geff`. Problem F gap statement: appH
  L1954-1958 ("The gauge-fixed sector list, Goldstone and ghost operators,
  measure, curvature couplings and weights are not specified by this
  calculation, so it does not fix the sector sum of Theorem ref{thm:Geff}, does
  not close F or D, and leaves the missing step above unchanged.")
- Classification of this package: **conditional derivation inside the
  Presentation-B locked block** supplying one named D1 deliverable entry (ghost
  operators) and a sector-sum non-contribution statement consumed by F. D/D1
  remain OPEN, PROGRAMME-CONDITIONAL; nothing here is DERIVED at the
  matrix-derived criterion.

## Source reading

digest + targeted reads. Digest CURRENT (head
`8b9ff3932501c116c6784c74338159ad1c03eb8b`, `dirty-chapters: no`). appH sha1
`60a8eb47bb32184d60d0165483a635f9a331c2b3` re-verified at the start of this
round and unchanged since the dispatch pin. Read in full: appH L765-808 (D
ledger + missing step), L1118-1217 (ghost-free paragraph, completed-action test,
diffeomorphism paragraph), L1650-1656 (Elitzur paragraph, D1 references),
L1910-1991 (F ledger + gap); ch17 L329-345, L650-658, L713-721; ch03 L254-291
(`eq:Phi-transform`, `eq:VEV`); ch10 L56-81 (`eq:D-both`),
`ass:local-lorentz`; ch08 `thm:Geff` heading; `prop:goldstone-count` statement;
`ass:frame-lock`, `ass:nondeg`, `ass:aux-metric` statements. Prior-proposal
dispositions 112/113 re-read (record, do not re-farm class-K; next target
upstream D/D1). No unreadable files.

## Research and reasoning

**Setting.** Presentation B under imposed local Lorentz symmetry
(`ass:local-lorentz`, explicitly "not derived from Presentation A"). The
frame/order-parameter field `\Phi^I{}_A(x)` transforms per `eq:Phi-transform`.
No derivative of the transformation parameter appears in that law; this is
literal in the displayed equation (ch03 L279-284) and is the whole content of
the pointwise-gauge lemma.

**Ghost operator.** For `\Lambda = I + \lambda`, `\lambda^T\eta + \eta\lambda = 0`
(`\lambda \in so(3,1)`), `\delta\Phi = \Phi\lambda`. Put `a := \eta\lambda`
(antisymmetric). Gauge fixing `F(\Phi) := antisym(\eta\Phi)` (6 components; it
removes exactly the six `\eta`-antisymmetric tangent components counted by
`prop:goldstone-count`). Then
`dF_\Phi(\Phi\lambda) = antisym(\eta\Phi\lambda) = antisym(\eta\Phi\eta\, a)`
(using `\eta^2 = I`), so the FP operator is the 6x6 endomorphism field
`M(\Phi): a |-> antisym((\eta\Phi\eta)\,a)`. It is a map between fibres at the
same `x`: order zero, no derivatives of `\Phi`.

**Spectrum and determinant.** For `\Phi = diag(r_0,r_1,r_2,r_3)`,
`\eta\Phi\eta = \Phi`, and on the antisymmetric basis element `e_i ^ e_j`
(`i<j`), `M` acts by `(r_i + r_j)/2`; hence
`det M = prod_{i<j} (r_i + r_j) / 64` (six factors of `1/2`). Verified exactly
(S2). `det M(\Phi)` is a polynomial of total degree 6 in the 16 entries of
`\Phi` (S1, exact). Being symmetric of weighted degree 6 in the roots it
reduces uniquely (S3a) to the characteristic-coefficient polynomial
`-(E1^2 E4 - E1 E2 E3 + E3^2)/64` (S3b; the identity
`prod_{i<j}(r_i+r_j) = E1 E2 E3 - E3^2 - E1^2 E4` is the classical factorization,
here verified by exact linear algebra over the weighted-degree-6 monomial basis).
`det M` is therefore a class function of `\Phi`; equality with the endomorphism
determinant for general (non-diagonal) `\Phi` was verified by exact integer
polynomial-identity sampling on 300 random integer matrices, mismatches 0 (S3c),
both sides being polynomials of total degree <= 6.
- Vacuum: `det M(v I) = v^6` exactly (S4); nonzero for `v != 0`, so the slice is
  transverse at the vacuum and the FP logarithm is regular there.
- Not a function of `det\Phi`: exact rational witness `diag(2,1/2,1,1)` gives
  `405/256` at `det\Phi = 1` (S7). This matters for the F sector bookkeeping:
  the ghost factor cannot be absorbed into a determinant-only measure weight.
- Degeneracy locus: `det M = 0` iff some `r_i + r_j = 0`. The frame
  `v.Rot(\pi/2)` (spatial `xy` rotation, `eta`-orthogonal, in `SO(3) < SO(3,1)`)
  has roots `(v, iv, -iv, v)` with `r + \bar r = 0` pair: `det M = 0` exactly
  (S6a/S6b). These are gauge-transformed vacua in the same orbit, so the chosen
  slice is not global even along compact directions: admissibility is a
  patch statement (Gribov-type obstruction, standard in content).
- Linear response: since `det M` is degree-6 polynomial, its first variation at
  `vI` is linear in the perturbation; verified on all 16 matrix units
  `E_ij`: `d/dt|_0 det M(vI + t E_ij) = (3/2) v^5 (E_ij)_{tr}` (S8), i.e.
  `d det M|_{vI} = (3/2) v^5 tr H`, equivalently
  `\delta ln det M|_{vI} = (3/(2v)) tr \delta\Phi`: a derivative-free tadpole
  for the locking potential that the vacuum/stationarity conditions of any
  locked-block expansion must absorb.
- Float spot check of the product formula on 200 random real matrices (not
  assumed diagonalizable), max relative error `1.542e-13` (S9, seed 114).

**Order-zero consistency check.** `F(\Phi (I + eps w_0))` with
`w_0 \in so(3,1)` (S5a) is exactly linear in `eps` with `\Phi`-only
coefficients (S5b): the transformed gauge-fixing functional involves no
derivative of the (infinitesimal) parameter, confirming the FP operator is an
endomorphism for the orbit direction itself, not just for the chosen `F`.

**Consequences for the D1/F operator inventory (conditional corollaries).**
(i) The internal `\Omega(x)`, local-Lorentz `\Lambda(x)` and locked-diagonal FP
determinants, in zeroth-order gauges, are pointwise nonlocal-in-momentum-free
factors `exp(+- \int d^4x ln det M(Phi(x)))`; they contribute no kinetic
operator and hence no heat-kernel sector of the type weighted in `thm:Geff`.
(ii) The recorded quadratic analysis already showed no linearised
diffeomorphism invariance at quadratic order (appH L1191-1192, bounded no-go for
that candidate at that order, L1196-1199), and with `g^(0)` held fixed the
`eq:Smicro` under diffeomorphisms is exhibited only for those that preserve
`g^(0)`, such as its isometries, and this does not exclude other symmetries
(appH L1201-1209). So within the locked block as displayed, **among the
exhibited symmetries at the recorded orders no kinetic ghost other than that
of the diffeomorphism sector is seen, and it is a supplied infrared input,
not derived from `eq:Smicro`**. This is exactly the kind of inventory entry the
F gap statement (L1954-1958, "Goldstone and ghost operators ... are not
specified") requires; it narrows what remains unspecified (measure, weights,
Goldstone list at quadratic-plus order) to named items.

**What is new vs recorded.** Grepped before writing: the only ghost entries in
the D section are (a) the class-3 ghost operator on the `End(C^N)` toy
(appH L1653 paragraph, a Laplace-Beltrami realisation on a compact torsion-free
toy, unrelated to the locked block), (b) the U(4)-model linearized K=0 Jacobian
with field-independent determinant (appH L1986-1987, a different model), and
(c) "not specified" statements (L1954-1958). The endomorphism FP structure of
the locked block and its exact determinant are recorded nowhere; the
Gribov-type patch statement for this slice appears nowhere.

**Novelty/derivation caution.** The FP procedure is textbook (Faddeev-Popov
1967; copies: Gribov 1977). Neither is cited in the inserted text (no `\cite`
there), and neither record was fetched this round: treated as background, not
imported results. No external result is imported; everything in the insert is
derived from `eq:Phi-transform` plus linear algebra, with the manuscript-recorded
facts quoted at the exact places they are used.

**Rejected test (recorded for the record).** The 113-donated
`\Lambda_w`-equivariance test was NOT applied: D1's open deliverable here is
operator specification and (separately) frame selection; the equivariance test
addresses signature/background selection, which is the closed E route. Using it
would farm a closed direction. The Elitzur sentence at appH L1655 was read; it
concerns D1(a)/(c) (order-parameter/selection), not the operator inventory, and
is unchanged.

## Claim classification

- Pointwise-gauge lemma (no derivatives of parameters in `eq:Phi-transform`;
  FP order = fixing order): **established derivation** (read off the displayed
  equation; order-zero orbit check S5b).
- `M` is a 6x6 endomorphism field for `F = antisym(eta Phi)`: **established
  derivation**.
- `det M = prod(r_i+r_j)/64` for diagonal `\Phi`; total degree 6; class-function
  reduction `-(E1^2E4 - E1E2E3 + E3^2)/64` (unique): **established derivation**
  (exact, S1-S3a/S3b).
- Equality for general `\Phi`: **derivation via randomized exact polynomial
  identity testing** (degree <= 6 both sides; 300 exact integer samples, 0
  mismatches, seed 114; plus float check 1.5e-13 on 200 matrices). Not a
  hand proof on the general fibre; gatekeeper may re-derive by noting both sides
  are conjugation-covariant constructions - stated as such, not assumed.
- Vacuum value `v^6`; log-tadpole `(3/(2v)) tr delta Phi`; witness `405/256`;
  `det M(v.Rot(pi/2)) = 0`: **established derivation** (exact, S4/S8/S7/S6).
- "Ghost determinants of zeroth-order gauges do not enter the `thm:Geff` sector
  sum as kinetic operators": **conditional derivation** (given the endomorphism
  status and the pointwise path integral).
- "Only kinetic ghost is the diffeomorphism ghost; it is a supplied input":
  **conditional** on the recorded quadratic-order no-linearised-diffeo fact and
  the recorded isometry restriction, at the orders those records state.
- Tadpole as a physical effect of the vacuum: **unresolved** (it shifts
  stationarity conditions of the locking potential; not evaluated here).
- Gribov-copy statement: exact at the exhibited frame; global admissibility of
  any Lorentz gauge on the full locked-field space: **unresolved** (patch-level
  statement only).

## Proposed changes

### chapters/appH-microscopic-proofs.tex (one insertion, conditional paragraph)

Insertion point: inside the Problem D section, immediately BEFORE the unique
line (verified `grep -c` = 1; also asserted at splice time by the certificate):

    \paragraph{Diffeomorphism symmetry of the displayed action (conditional; not closure).}

The anchor paragraph and everything after it stay. No existing sentence is
modified or deleted. The inserted paragraph (file
`insert-d1-locked-ghosts.tex`, 3647 B, CRLF, UTF-8 no BOM, no new labels, no
`\cite`):

```latex
\paragraph{Faddeev--Popov determinants of the pointwise gauge sectors of the locked block (conditional; Presentation-B scope; not closure).}
Under~\eqref{eq:Phi-transform} both gauge actions on \(\Phi\) are pointwise: an
internal transformation \(\Omega(x)\) acts by left multiplication and a local
Lorentz transformation \(\Lambda(x)=\mathbb{I}+\lambda(x)\),
\(\lambda\in\mathfrak{so}(3,1)\), by right multiplication, and neither contains
a derivative of the transformation parameter. The Faddeev--Popov operator of a
gauge fixing of either group therefore has order equal to the derivative order
of the gauge-fixing functional, and a zeroth-order fixing yields a ghost
operator that is a field endomorphism rather than a differential operator; the
locked diagonal combination shares this property. For the
\(\mathrm{SO}(3,1)\) sector, fix about the vacuum~\eqref{eq:VEV} the
antisymmetric gauge \(F:=\mathrm{antisym}(\eta\Phi)=0\), which removes the six
\(\eta\)-antisymmetric components of Proposition~\ref{prop:goldstone-count}.
With \(a:=\eta\lambda\) antisymmetric, the ghost map
\(a\mapsto\mathrm{antisym}(\eta\Phi\eta\,a)\) gives
\[
  \det M(\Phi)=\frac{1}{64}\prod_{i<j}\bigl(r_i(\Phi)+r_j(\Phi)\bigr),
\]
where \(r_i(\Phi)\) are the roots of the characteristic polynomial of \(\Phi\);
the identity is polynomial in the entries of \(\Phi\). It equals \(v^{6}\) at
\(\Phi=v\mathbb{I}\), is not a function of \(\det\Phi\) (the spectral datum
\((2,\tfrac12,1,1)\) gives \(405/256\) at \(\det\Phi=1\)), and vanishes whenever
\(r_i+r_j=0\); in particular the \(\eta\)-orthogonal frame obtained from the
vacuum by a \(\pi/2\) spatial rotation is a zero, so this fixing is admissible
only on the field-space patch containing the vacuum and free of such frames.
Because \(M\) is an endomorphism field, the ghost integral is pointwise and
exact, with no momentum integration and no regulator: it contributes the
derivative-free local functional \(\int d^{4}x\,\ln\det M(\Phi(x))\) to the path-integral exponent (entering
the effective action with sign \(-1\)), whose logarithmic linear response at
the vacuum is \(\frac{3}{2v}\mathrm{tr}\,\delta\Phi\), a tadpole for the locking
potential, and it contributes no kinetic operator. Two
consequences for the operator content that Problem~D1 must specify: in a
zeroth-order gauge the internal, Lorentz, and locked-diagonal
Faddeev--Popov determinants are pointwise factors, so they do not enter the
weighted sector sum of Theorem~\ref{thm:Geff} as kinetic operators, and, among the symmetries exhibited
for the displayed action at the orders recorded above, no
kinetic ghost operator other than that of the diffeomorphism
sector arises; and with \(g^{(0)}_{\mu\nu}\) held fixed
(Assumption~\ref{ass:aux-metric}) the invariance
of~\eqref{eq:Smicro} under diffeomorphisms is exhibited only
for those that preserve \(g^{(0)}\), such as its isometries,
which does not exclude other symmetries and derives no
diffeomorphism gauge symmetry, so the diffeomorphism ghost is
a supplied input of the infrared sector and not a consequence
of~\eqref{eq:Smicro}.
These statements concern the gauge-fixing structure of the Presentation-B locked
block under Assumption~\ref{ass:local-lorentz}, the
transformation law~\eqref{eq:Phi-transform}, and the stated gauge choice and
patch; they derive no local symmetry, derive no frame locking or
non-degeneracy (Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg}), leave
the kinetic term for \(\omega_\mu\) and the diagonal-connection dynamics
untouched, and say nothing about Presentation~A. Problem~D remains open.
```

Labels referenced and verified to exist (no new labels added, no duplicates):
`eq:Phi-transform`, `eq:VEV` (ch03); `prop:goldstone-count`, `ass:local-lorentz`
(ch10); `thm:Geff` (ch08); `ass:aux-metric`, `eq:Smicro`, `ass:frame-lock`
(ch03); `ass:nondeg` (ch04). Digest duplicate-label index: none.

### Stale-passage check (no edits proposed)

- appH L1954-1958 (F gap) says the ghost operators "are not specified **by this
  calculation**" - scoped to the completed-action calculation; remains true
  after this insert (a different, pointwise calculation) and is not edited.
- appH L803-804 "specifying the full operator content does not close D": kept;
  the insert closes nothing and says so.
- No other passage asserts the locked-block ghosts are kinetic or already
  specified.

### Compile certificate

`cert-r114p.py` copies `namcg-book7.tex`, the untracked `namcg-book7.bbl`,
`chapters/`, `figs/`, `bib/` to a temp dir OUTSIDE the repository, asserts the
anchor is unique in the spliced copy, inserts the paragraph, runs ONE
`pdflatex -interaction=nonstopmode -halt-on-error namcg-book7.tex` pass,
requires rc 0, no `! ` log lines, `Output written`, then deletes the temp dir.
Result on the final insert text:
`spliced bytes: 828027 rc: 0 exclam-lines: 0 Output written: True (r2 re-pin rerun)` -> `CERT OK`.

## Verification scripts

All in this folder; seed 114; deterministic.

- `verify_ghost_fp_114.py` - sympy/numpy checks S1-S9 of the FP operator.
  Re-run: `python -I -B verify_ghost_fp_114.py` (cwd this folder). Expected
  invariant outputs (full recorded output in `run-r114.txt`):
  `S1 ... True`; `S2 ... True`; `S3a ... True`; `S3b prod(r_i+r_j)/64 =
  -(E1**2*E4 - E1*E2*E3 + E3**2)/64`; `S3c ... mismatches: 0`; `S4 ... True`;
  `S5a ... True`; `S5b ... True`; `S6a Rot eta-orthogonal: True | S6b detM(Rot)
  == 0: True`; `S7 detM(diag(2,1/2,1,1)) = 405/256 | det Phi = 1 | val != 1:
  True`; `S8 ... True`; `S9 max rel err, 200 random Phi (seed 114): 1.542e-13`;
  final line `ALL CHECKS DONE`. Recorded output (verbatim):

```
R114 local-Lorentz FP-operator checks (sympy 1.14.0, numpy 2.4.6, seed 114)
S1 detM(Phi) polynomial, total degree 6 (expect 6): True
S2 exact diag identity detM == prod(r_i+r_j)/64: True
S3a unique weighted-degree-6 reduction: True
S3b prod(r_i+r_j)/64 = -(E1**2*E4 - E1*E2*E3 + E3**2)/64 (in E_i = char-poly coefficients of Phi)
S3c exact integer sampling, 300 general 4x4 Phi (seed 114), mismatches: 0
S4 detM(v*I) == v**6: True
S5a w0 in so(3,1): True
S5b F(Phi*Lambda) is linear in eps with Phi-only coefficients (order 0): True
S6a Rot eta-orthogonal: True | S6b detM(Rot) == 0: True
S7 detM(diag(2,1/2,1,1)) = 405/256 | det Phi = 1 | val != 1: True
S8 linear response d/dt detM(v*I+t*E_ij)|0 == (3/2) v^5 (E_ij) for all 16 i,j: True
S9 max rel err, 200 random Phi (seed 114): 1.542e-13
ALL CHECKS DONE
```

  Note (honest scope): S3c/S8 establish the general-`\Phi` identity by exact
  randomized polynomial-identity testing (degree <= 6) and by matrix units
  justified by the degree-6 polynomiality of S1; the diagonal case (S2) is an
  exact hand-verified computation. S8's matrix-unit reduction is exactly valid
  because `det M` is polynomial of degree 6 in the entries, so the first
  variation at `vI` is linear; this was re-stated in the script comment.
- `cert-r114p.py` - compile certificate above. Re-run:
  `python -I -B cert-r114p.py`; expect final line `CERT OK`.
- `insert-d1-locked-ghosts.tex` - the manuscript-bound paragraph (CRLF verified;
  no bare LF).
- `run-r114.txt` - recorded output of the verification run.
- `manifest.md` - sha1 + byte sizes.

Tool output is a check, not a proof; the reasoning is in the sections above.

## Decisions Taken

- **Route**: ghost-operator deliverable of D1 (the only D1 clause not covered by
  the three recorded class results or the Elitzur/composite paragraph), attacked
  by a new exact FP computation on the locked block rather than another
  representation-class edge. Positive-derivation target per the 2026-11-20
  directive; expected output is derivation-grade data for a named missing step
  (ghost operators unspecified, appH L1956).
- **Declined the 113-donated `\Lambda_w`-equivariance test**: it addresses
  signature/background selection (closed E route); applying it would farm a
  closed direction without touching D1's operator-specification clause.
- **Gauge choice** `F = antisym(eta Phi)`: routine choice (changes no label);
  chosen because it is zeroth order, matched one-to-one to the six components of
  `prop:goldstone-count`, and gives the closed-form determinant. Other
  zeroth-order fixings are covered by the general pointwise lemma.
- **Landing**: one conditional paragraph in the D section before the diffeo
  paragraph (gatekeeper decides integration). No chapter-17 text change, no F
  edit (the F gap statement stays accurate as scoped).
- **Class-function status reported** (S3) even though the insert keeps the
  root-product form; the stronger "polynomial in char-poly coefficients" form
  is recorded here so F bookkeeping can use it later without a new package.
- **Tadpole sentence corrected** mid-round (response of `det M` vs of
  `ln det M`; correct log-response `(3/(2v)) tr delta Phi`) before certification;
  certificate re-run after the fix (`CERT OK`).

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path problem is closed, no
missing step is fully derived at the matrix-derived criterion, no label moves,
no false claim in the manuscript is corrected. The package supplies one named
D1 inventory entry and one sector-sum non-contribution statement.

## Status-label recommendation

Derived from ch17 (criterion: A, B, C, D1, E, F, G-derived, N) and the current
Appendix H ledger: all remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL as
recorded. Affected labels: **none** (unchanged; no label edit is proposed or
made).

## Author decision needed

None.

## Remaining open step

To close D1 as stated: (a) derive local `SO(3,1)` from the matrix algebra and
condensate (or the manuscript's D2 re-reading stands); (c) derive the locked
frame's existence and non-degeneracy on the claimed domain from microscopic
data (the `ass:frame-lock`/`ass:nondeg` pair); and complete the D1 inventory:
the `omega`-kinetic operator and diagonal-connection dynamics (recorded
unresolved: "the diagonal combination does not enter at quadratic order",
appH L1180-1181; "Whether higher-order terms, a kinetic term for `\omega_\mu`,
or an induced action change this is not examined", L1193-1196), the `B`-sector
and Goldstone operator list at the order used by F, the measure, the curvature
couplings and the sector weights (appH L1956-1957), plus the `A_mu` kinetic
term. For F specifically: the ghost entries supplied here remove "ghost
operators" from the unspecified list only for the pointwise sectors and only at
the zeroth-order-gauge level; the diffeomorphism-ghost kinetic operator remains
a supplied input, so the sector sum of `thm:Geff` is still not fixed. Within
this target the transferable finding for the gating problem (D1(a), Presentation
A selection) is negative-adjacent but explicit: the locked-block ghost
structure is entirely an `ass:local-lorentz`-level (Presentation-B) input and
carries no data that could derive the gauge symmetry from the matrix algebra.

## Special instructions for the gatekeeper

- Scope: the inserted claims are for the Presentation-B locked block under
  `ass:local-lorentz`, the gauge `F = antisym(eta Phi)` and the stated patch.
  They must not be read as deriving any local symmetry, the locked frame,
  `ass:nondeg`, the `omega` kinetic term, or anything about Presentation A, and
  must not be used to close D1, D or F. The insert says "Problem D remains
  open."
- Re-derive first: the 6x6 ghost matrix entries `M_{(ij),(kl)}` from
  `antisym(eta Phi eta a)` (one line by hand), the diagonal eigenvalues
  `(r_i + r_j)/2`, and `det M(v I) = v^6`; then check S4/S6b/S7 exactly by
  sympy. The general-`\Phi` step is randomized exact PIT (S3c) - grade it as
  such, not as a hand proof on the general fibre.
- Confirm the tadpole coefficient two ways: `d/dt det M(vI + tH) = (3/2) v^5
  tr H` and `delta ln det M = (3/(2v)) tr delta Phi` (they must be consistent
  with S4/S8).
- Verify the pointwise lemma against `eq:Phi-transform` as displayed (no
  parameter derivatives), and that `prop:goldstone-count` counts six broken
  generators (the 6-component matching of the fixing).
- Anchor: the `\paragraph{Diffeomorphism symmetry...}` line is unique in the
  current appH (`grep -c` = 1, sha1 `60a8eb47...`); re-anchor at integration.
  Re-run `cert-r114p.py` (must print `CERT OK`, rc 0, `exclam-lines: 0`).
- What must NOT be asserted from this package: closure or narrowing of any
  status label; that the FP determinant fixes the `thm:Geff` sector sum (it
  shows pointwise ghosts do NOT enter it as kinetic operators); that the gauge
  is globally admissible; that the diffeomorphism ghost is derived.
