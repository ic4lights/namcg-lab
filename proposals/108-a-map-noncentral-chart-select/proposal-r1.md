# Proposal 108-a-map-noncentral-chart-select, round 1

**Recovery provenance (honest record).** The dispatched researcher for this package died from an API
context-length error ("Prompt is too long") after shipping the full mathematics and verification pack to disk
(artifact timestamps 2026-11-21 14:13-14:20 local) and before writing this proposal file. This r1 was completed
from disk by a recovery researcher. No mathematics was re-derived or added: every shipped artifact was re-run
first and all reproduce **byte-identically** (paths in "Verification scripts"). Sole script authority resolved to
`s4_noncentral_selection_v3.py` (D1 below); v1/v2 retained unmodified as inert provenance.

## Result

For the A.map chain-4 head edge `A.map.noncentral-chart-select` (the dispatch named by INTEGRATION-107,
ledger:1377) the package establishes, exactly within the hypothesis classes stated below, a positive
derivation-grade input for the named missing step (a DERIVED state/background-dependent effective bivector):

1. **Scalarity dichotomy.** For self-adjoint coordinate operators of a unital operator algebra and the
   state-induced bivector `Theta^{IJ}_omega = -i omega([X^I,X^J])`: this datum is independent of the normalized
   state iff every coordinate commutator is scalar. In finite dimension the trace forces such a scalar to vanish
   (measured `max |tr([P,Q])/3| = 2.96e-16` over 40 random Hermitian 3x3 pairs), so the
   coordinate-commutator centrality that produced the 107 chart-blindness no-go is exactly the **scalar case** of
   the dichotomy, and every finite-N matrix regularization with nonvanishing commutator lies automatically in the
   **non-scalar complement** (commutator traceless, hence non-scalar, since a traceless scalar is zero). In the
   non-scalar case the bivector has nontrivial spread over states, and its extreme values are exactly the extreme
   eigenvalues of the Hermitian `i[X^I,X^J]` (check 4: eigenvalues -4,+4, spread width 8, both attained).
2. **Lie-type class: derived leaf-dependent bivector.** If `[X^I,X^J] = i c^{IJ}{}_K X^K`, the bivector of a
   state with one-point functions `x^K = omega(X^K)` equals `c^{IJ}{}_K x^K` - a bivector field DERIVED from the
   background one-point data, not postulated. Concretely for the spin-j fuzzy sphere `X^i = l J^i`:
   `Theta^{12}_omega = l omega(X^3)` attains the ends `+/- l^2 j` (pole check at j = 2,3,4,6,8, max dev
   `8.88e-16`; values span `[-l^2 j, l^2 j]` over pure states), the exact Casimir identity
   `X.X = l^2 j(j+1) 1` holds (max rel dev `3.42e-16`; R^2 = 6,12,20,42,72 for j = 2,3,4,6,8) and identifies the
   bivector field as the Kirillov-Kostant-Souriau field of the orbit, and the bivector's coherent-state relative
   fluctuation width is **exactly 1/sqrt(j)** (j = 1:1.0000, 2:0.7071, 3:0.5774, 4:0.5000, 6:0.4082, 8:0.3536,
   50:0.1414; closed-form dev `1.11e-16`) - semiclassically sharp as j -> infinity.
3. **Chart 1-jet supply up to symplectic gauge.** Where the derived bivector is nondegenerate, the chart 1-jets
   carrying it to the constant ambient bivector form a single torsor of the symplectic group: the linearized
   frame equation `M J M^T = J` has solution-space dimension 16 - 6 = 10 = dim Sp(4) (check 10, with an explicit
   symplectic non-orthogonal element, orth dev 0.500), so there are no moduli beyond the symplectic group; an
   explicit Darboux chart for the model field `theta(x) = eps x` on a sphere of radius sqrt(12) (= the j=3 Casimir
   radius) gives `{g1,g2} = 1` at 5 points, max dev `1.11e-16` (check 14). The residual gauge is the
   bivector-automorphism group: infinitesimal automorphism dimension 3 = so(3) (check 12, rank 6 in 9 unknowns,
   so(3) generators satisfy the equations to dev 0.00e+00) and finite equivariance `Q theta(x) Q^T = theta(Qx)`
   on 24 sampled points (max dev 0.00e+00) with failure 2 for the non-automorphism diag(2,1,1) (check 15).
4. **Rank obstruction.** A leaf bivector of a 2-dimensional orbit has matrix rank 2 (sampled point rank 2; as a
   4x4 block rank 2) while the manuscript's ambient constant bivector has rank 4; rank is invariant under frame
   change `M theta M^T`, so no such background supplies the rank-4 semiclassical-chart 1-jet and
   characteristic-direction data beyond the bivector are required (check 11).
5. **Finite-N realization.** For 't Hooft clock-shift pairs at N = 5 and N = 8 the commutator is traceless, hence
   non-scalar (normalized non-scalar deviation exactly 1 / 1), and block-local states in the K = 5 and K = 8
   blocks give distinct bivector values 0.345492 vs 0.146447 (check 13): finite-N blocks carry into the bivector.

All 16 checks pass (`TOTALS: PASS 16/16 FAIL 0`), the insert passes a 21/21 hygiene battery, and the splice
simulation contracts POST 815065 B / sha256/16 dcfa82a524551702 / 3878 CRLF. **Nothing here closes Problem A,
A.map, or the edge:** the fuzzy sphere is not a condensate of the manuscript's matrix model, the rank-4
nondegenerate instance for the 4-dimensional leaf is not constructed, and the order-Theta^2 correction on the
noncentral background is not computed. The manuscript paragraph proposed for insertion says this itself and ends
"this paragraph does not close Problem~A."

## Target and status

- **Problem A (matrix-to-modular map)**, `chapters/appH-microscopic-proofs.tex` sec:status-A (L12-20, read in
  full): current labels as printed - Status **OPEN**; Priority **CRITICAL PATH** for the matrix-derived label;
  Completion **PROGRAMME-CONDITIONAL**. `chapters/ch17-agenda.tex` L377-381 agrees ("OPEN; CRITICAL PATH for the
  matrix-derived label"); the completion item (L704-706): Assumption ass:dictionary is derived, or the chains of
  the other items are re-derived without invoking it. No discrepancy between the two sources.
- **Edge** `A.map.noncentral-chart-select` (`reports/graph/frontier.yaml` L105-125, read in full): state
  `untried`, rank 13, HEAD of chain 4 and of gap A; named the next dispatch by INTEGRATION-107 (ledger). Target
  from its `requires_symbols` / `missing_inputs`: a matrix-model condensate/background class in which the
  coordinate commutator is noncentral AND the induced effective bivector is y-dependent and DERIVED (not
  postulated), supplying semiclassical-chart 1-jet selection data.
- **Dependencies** (from the edge's `available_from`, passages read): appH L140 (106 pullback selection, affine
  rank-20 selection map, 20-of-36 embedding-2-jet reach; passage read in full), appH L142 (107 bounded no-go - pins the centrality
  mechanism `i Theta^{IJ} 1` that this route must break, and names this route verbatim as the out-of-class
  escape), appH L90-136 (058 Weyl data; cited from the edge spec, not read at recovery).
- **DERIVED vs PROGRAMME-CONDITIONAL.** Everything derived here is derived for the stated abstract hypothesis
  classes (unital operator algebras; finite-dimensional su(2) Lie-type realizations; the model bivector field
  `eps x`), i.e. conditional results with explicit class. Nothing is DERIVED for the NAMCG matrix model itself;
  the package is a PROGRAMME-CONDITIONAL input to the edge, not its closure.

## Source reading

**Digest + targeted reads.** `python scripts/make_digest.py --check` -> `DIGEST CURRENT` (head 251b9d5;
`dirty-chapters: yes` is the expected uncommitted ordinal-37 integration state; digest appH hash 698f38979140 =
live bytes, independently re-measured at recovery: 812227 B / 698f38979140770d / 3876 CRLF). Read in full: all
15 files of the package folder (three script versions and their outputs, `insert-r1.tex`, `mk_insert_108_r1.py`,
`hygiene_108_r1.py/.out`, three `simulate_apply_108_r1*.py/.out`); `frontier.yaml` edge blocks L73-126 plus the
post-37 note (L29); `reports/ledger.md` tail (last 60 lines);
`proposals/107-a-map-chart-condensate-selection/review-r2.md` "Scope of what is established" (relaxations
(i)-(vi)); appH L12-21, L138, L140, L142 (the three integrated A paragraphs), L144-151 (Missing step);
ch17 L377-381 and L700-712. No full `chapters/` scan performed (none required: this proposal adds a labelled
conditional paragraph; it changes no definition, assumption, scope statement or status passage; the mandatory
full scan remains due at the ordinal-40 gatekeeper review).

## Research and reasoning

**D1. The dichotomy and what it does to the 107 mechanism.** Let C = [X^I,X^J] with X^I, X^J self-adjoint, so C
is anti-Hermitian and iC is Hermitian (check 3: `max ||iC-(iC)^dag|| = 0.00e+00`). Then
`Theta^IJ_omega = -i omega(C)` is real. If C = c 1, every normalized state gives `Theta = -i c`: state-
independent. Conversely, if `-i <psi|C|psi>` is the same for all normalized vectors, the quadratic form of the
Hermitian iC is constant on the unit sphere, so by the polarization identity iC = (const) 1, i.e. C is scalar. In
finite dimension `tr C = 0` forces the scalar to vanish (check 3). This is exactly the hypothesis that 107's
centrality argument used - `[X^I,X^J] = i Theta^{IJ} 1` central, "every normalized state of the fixed Heisenberg
algebra has the same constant effective bivector" (appH L142) - and it shows the mechanism is the scalar case,
not a general fact about states: the check-2 control (commuting diagonal pair, biv = 0 on all 6 test states)
reproduces 107's rigidity, while check 1 (A = sigma_x, B = 2 sigma_y, C = 4i sigma_z, non-scalar deviation 5.657
= 4 sqrt(2), bivector +4 on |0> and -4 on |1>) realizes the complement. Check 4 adds that the attainable spread
of the bivector over states equals the full spectrum width of iC (eigenvalues -4, +4 attained at eigenvectors).
So a noncentral background is precisely where 107's chart-blindness stops applying: the effective bivector
becomes a function on the state space (hence, for a condensate, on the background).

**D2. Lie-type class: the bivector is derived, not postulated.** If the commutator closes linearly,
`[X^I,X^J] = i c^{IJ}{}_K X^K`, then applying any state omega gives `Theta^IJ_omega = c^{IJ}{}_K x^K` with
`x^K = omega(X^K)` - an immediate consequence of linearity of states (no dynamics used). Identifying the
one-point-function space with the (coadjoint) orbit of the structure constants, `theta^{IJ}(x) = c^{IJ}{}_K x^K`
is the standard Kirillov-Kostant-Souriau Poisson bivector of the orbit; its dependence on x is the
y-dependence the edge asks for, and it is a derived function of the background state, satisfying the edge's
"DERIVED, not postulated (rule 3)" requirement inside its class. The fuzzy sphere is the spin-j irreducible
su(2) instance, fully represented and checked: commutator `[X_1,X_2] = i X_3` (cyclic) exact at j = 2,3 (rel dev
`6.05e-16`, check 5); at the pole (leaf point x_3 = j) `Theta^{12} = <X_3> = j` for j = 2,3,4,6,8 (check 6),
over states spanning `[-j,+j]` (l = 1 units; l-scaling exact, see insert); Casimir `X.X = j(j+1) 1` exact
(check 7) fixing the leaf-algebra radius `l sqrt(j(j+1))`; bivector 1-jet datum nonzero O(1): the symmetrized
structure-constant contraction `sum_pairs (C^{ab} X_m + X_m C^{ab}) = 2 X.X = 24 * 1` at j = 3 (rel dev
`5.34e-16`, check 9), i.e. the germ of the bivector field at the leaf point carries nonzero derivative data
(the linear field theta(x) = eps x has constant nonzero Jacobian).

**D3. Semiclassical sharpness.** At the spin coherent (pole) state: Var(X_3) = 0, Var(X_1) = Var(X_2) = j/2
(max dev `4.44e-16`, check 8), so with the explicit relative-width definition
`sqrt(2 (Var_1+Var_2+Var_3)) / sqrt(2 j^2)` (commutator-fluctuation norm over bivector norm; script line 216)
the width is `sqrt(2j)/sqrt(2 j^2) = 1/sqrt(j)` exactly (closed-form dev `1.11e-16`, check 16; table j =
1:1.0000 ... 50:0.1414, check 8). A large-j condensate background is therefore bivector-sharp: the effective
bivector concentrates on its classical value, which is what a semiclassical chart selection needs. This is an
established su(2) identity with the stated explicit measure; the measure choice is a definition (see claim
table).

**D4. What the bivector fixes: chart 1-jets modulo symplectic gauge.** For a constant nondegenerate model J at
leaf dimension 4, the linearization of `M J M^T = J` at M = 1, `K -> K J + J K^T`, has rank 6 in the 16
components of K (script builds the full 16x16), so the Lie algebra of the frame group has dimension 16 - 6 = 10
= dim Sp(4) (check 10); the explicit symplectic non-orthogonal element (orth dev 0.500) shows the frame group is
the symplectic group, not a rotation subgroup. The solution set of the frame equation for a nondegenerate target
is a single torsor under the symplectic group (standard transitivity of Sp on nondegenerate 2-forms; the package
verifies the dimension count and, for the model bivector field, constructs an explicit Darboux chart:
g1 = y1, g2 = asin(y2/sqrt(R^2-y1^2)), s^2 - y2^2 = x_3^2, so `{g1,g2} = (1/x_3) x_3 = 1` identically on the
north-polar chart - 5 points, max dev `1.11e-16`, check 14, with R^2 = 12 = j(j+1) at j = 3, the Casimir radius
of check 7). Conclusion of the chain D2+D4: in the nondegenerate regime the derived bivector field supplies
exactly the gauge-invariant content of the semiclassical-chart 1-jet - the chart is fixed up to the symplectic
group - and the residual gauge is the bivector-automorphism group, computed two ways for `theta = eps x`:
infinitesimally (9-parameter linear-field ansatz, rank 6, automorphism dimension 3, the three so(3) generators
satisfying the equations to dev 0.00e+00, check 12) and finitely (`Q theta(x) Q^T = theta(Qx)` for two integer
SO(3) samples on 24 points at dev 0.00e+00, and failure of size 2 for diag(2,1,1), check 15). This is the
positive statement the edge wants in the class where it is true: bivector datum -> chart 1-jet up to gauge, with
a computed gauge group.

**D5. The rank obstruction (where the supply fails).** Under any frame change the rank of the bivector matrix is
invariant (congruence). The leaf bivector of the 2-dimensionally-orbiting fuzzy sphere, `theta = eps x`, has
matrix rank 2 (checked at the sampled axis point: rank 2 as a 3x3 and 2 as a 4x4 block) while the manuscript's
constant ambient bivector is rank 4 (Jst, rank 4): check 11. Hence a 2-orbit condensate can never supply the
rank-4 chart 1-jet of the book's 4-dimensional semiclassical coordinate construction at ANY point (the insert
names poles and 4-coordinate embeddings as the representative loci; see claim table for the exact extent), and
rank-2 degeneration is an obstruction the bivector alone cannot overcome: characteristic-direction data beyond
the bivector are required. The positive supply of D4 therefore requires a 4-dimensional orbit (e.g. product or
higher fuzzy orbits), which this package does not construct.

**D6. Finite-N realization and block dependence.** Any finite-N matrix regularization of noncommuting
coordinates has traceless commutator, hence if the commutator is nonzero it is non-scalar automatically (no
exceptional central case can occur at finite N): this is the structural half of why the 107 rigidity is a
large-N/Heisenberg-algebra artifact of the CENTRAL background. The explicit clock-shift ('t Hooft) pairs at
N = 5, 8 have normalized non-scalar deviation exactly 1 (scalar part zero by trace), and the same local
two-site state in the K = 5 block gives bivector 0.345492 while the K = 8 block gives 0.146447 (check 13): at
finite N the bivector remembers the block, i.e. condensate/block data can select bivector values - the mechanism
whose absence 107 proved in the central case.

**D7. Comparison with the original edge target.** The edge asks for "a matrix-model condensate/background class
with noncentral coordinate commutator AND an induced effective bivector that is y-dependent and DERIVED" feeding
the chart 1-jet selection. What this package gives: the exact dichotomy (which hypothesis is broken and why the
107 no-go does not extend to it); a fully derived, checked and semiclassically sharp instance of the y-dependent
derived bivector (Lie-type class); the precise positive supply result (bivector -> chart 1-jet up to Sp, gauge =
automorphism group) where nondegenerate; the precise obstruction (rank) where degenerate; and the structural
finite-N fact that noncentrality is generic. What it does not give: a condensate OF THE NAMCG MATRIX MODEL of
this class; a rank-4 nondegenerate orbit instance; the order-Theta^2 pullback correction B2 recomputed on the
derived x-dependent background; or the embedding-2-jet fiber question (whether the derived bivector 1-jet pins
the embedding 2-jet inside the 20-dimensional fiber of appH L140). These are listed in "Remaining open step".

**D8. Script version provenance (v1 -> v2 -> v3).** Diff analysis plus reproduction of every recorded failure
signature:
- `s4_noncentral_selection.py` (v1): CHECK 5 FAIL (rel dev 2.00e+00: the spin-ladder construction was inverted -
  `Jp[k+1][k]` populated, `Jm = adj(Jp)` - so the realized algebra had `[X_1,X_2] = -i X_3`, a sign error);
  CHECK 6 FAIL (bivector -j at the poles - same root cause); CHECK 9 FAIL (dev 5.29e+00 - same root cause);
  CHECK 12 FAIL (rank 9 in 9 unknowns -> autdim 0: wrong row indexing `row[a*3+i]` with a spurious inner m-loop
  in the automorphism-equation assembly); and the run CRASHED at check 13 - reproduced NameError
  `name 'k' is not defined` in the 't Hooft U diagonal (v1 line 306; stderr re-captured at recovery:
  `scratch/s4_v1_rerun_r1.err`), which is why the shipped v1 stdout ends after CHECK 12 with no TOTALS line and
  exactly 4 FAIL lines.
- `s4_noncentral_selection_v2.py`: fixed the ladder construction (`Jm[k+1][k]` = lowering, `Jp = adj(Jm)`), the
  check-12 row indexing (`row[i*3+a] -= eps(a,c,j)`, `row[j*3+a] -= eps(i,a,c)`), and the NameError (`k` -> `i`)
  -> 15/16 PASS, with CHECK 12 still FAIL: the dimension became right (rank 6, autdim 3) but the so(3) generators
  failed the equations (dev 2.00e+00) - a residual sign error in the first equation block.
- `s4_noncentral_selection_v3.py`: one further sign fix `row[i*3+a] += eps(a,c,j)` (since -eps^{ajc} = +eps^{acj}
  in the contracted slot convention) -> **16/16 PASS**, reproduced byte-identically at recovery. v3 is the SOLE
  SCRIPT AUTHORITY; v1/v2 retained unmodified as inert provenance.
- `simulate_apply_108_r1.py` / `r1b` / `r1c`: measured PRE/PIN/POST triples identical across all three (all the
  measurements above); the succession only corrected the printed expectation labels (r1: `expect +2836 / +1` and
  `POST PIN count expect 2`; r1b fixed the PIN expectation; r1c fixed both to the actual +2838 / +2 and 1).
  `r1c` is the authority simulate; r1/r1b inert provenance.

**D9. Recovery verification pass (this round, all from repo root with `python -I`).** Re-ran and compared
byte-for-byte against the shipped outputs: v3 battery -> `scratch/s4_v3_rerun_r1.out` byte-identical (2576 B /
sha256/16 6fb8631fcecda151 / 18 CRLF; `TOTALS: PASS 16/16 FAIL 0`, exit 0; deterministic - `random.seed(108)`
set before the only random draw); hygiene on insert-r1.tex -> `scratch/hygiene_108_rerun_r1.out` byte-identical
(21/21, self-recording H21 line `file=insert-r1.tex sha256/16=7657be68c8ffa5b4`); simulate r1c ->
`scratch/simulate_108_r1c_rerun_r1.out` byte-identical (PRE 812227 / 698f38979140770d / 3876; PIN count 1, short
count 3, offset 14892; POST 815065 / dcfa82a524551702 / 3878; undo True; `live appH unchanged after run: True`);
preview re-written by the rerun re-measured 815065 / dcfa82a524551702 / 3878; v1/v2 reruns reproduce their
recorded failure signatures (scratch/s4_v1_rerun_r1.out/.err, scratch/s4_v2_rerun_r1.out). Live appH measured
independently: 812227 B / sha256/16 698f38979140770d / 3876 CRLF, equal to the digest-recorded appH hash and to
the simulate PRE. The simulate scripts re-confirmed read-only on chapters/ (live-bytes re-check printed True).
`insert-r1.tex` measured 2836 B / sha256/16 7657be68c8ffa5b4 / exactly 1 CRLF - equal to the values in hygiene
H21 and the mk_insert generator's contract; `mk_insert_108_r1.py` was NOT re-run at recovery (it would rewrite
the insert byte-identically; left untouched to keep the shipped bytes the audited ones).

## Claim classification

| # | Claim | Classification |
|---|-------|----------------|
| 1 | Dichotomy: bivector state-independent iff all commutators scalar (normalized vector states) | Established derivation (polarization identity on the Hermitian iC); instances verified numerically (checks 1, 2, 4) |
| 2 | In finite dimension the scalar is forced to vanish | Established identity (tr [X,Y] = 0; check 3) |
| 3 | "Every finite-N matrix regularization with noncommuting coordinates realizes the complement" | Established conditional result - exact hypothesis: finite dimension AND commutator nonzero (traceless + nonzero implies non-scalar); "noncommuting coordinates" in the insert supplies the nonzero |
| 4 | Lie-type bivector equals c x (insert clause "possibly with scalar terms") | Established derivation for Lie-type WITHOUT scalar terms (checks 5-6); with scalar terms exact when read affinely - the scalar term contributes c^{IJ}{}_0 omega(1), i.e. the identity is adjoined to the generating set (Decisions Taken, D2); in finite dimension with traceless generators scalar terms cannot occur (check 3) |
| 5 | Fuzzy-sphere instance: [X_1,X_2] = iX_3, Theta^{12} = l omega(X^3) attaining +/- l^2 j, Casimir = l^2 j(j+1) 1, Var values, 1-jet identity = 2 X.X | Established su(2) representation identities (l-scaling exact algebra); verified at j = 2,3 (commutator), j = 2,3,4,6,8 (pole values, Casimir), j = 1,2,3,4,6,8,50 (variances, widths), deviations <= 8.88e-16 (checks 5-9, 16) |
| 6 | Relative width exactly 1/sqrt(j) | Established identity UNDER the explicit relative-width definition of script line 216 (commutator-fluctuation norm / bivector norm); the definition is a choice, the identity for it is exact (check 16) |
| 7 | Bivector field is the KKS field of the orbit | Established standard identification (orbit method); used as a label for the computed field, not imported as evidence |
| 8 | Nondegenerate case: chart 1-jets form a single torsor of Sp(4), dim 10, no moduli | Established linear algebra for the dimension count (16 - rank 6 = 10, check 10) plus standard transitivity of Sp on nondegenerate 2-forms; Darboux existence verified explicitly for the model field (check 14); exact hypothesis: bivector nondegenerate at the leaf point, leaf dimension 4 |
| 9 | Residual gauge = bivector automorphism group = so(3) for theta = eps x | Established for the model field: infinitesimal dim 3 + generator satisfaction (check 12), finite equivariance + non-automorphism failure (check 15) |
| 10 | Rank obstruction: rank-2 leaf bivector cannot be gauged to rank-4 ambient; characteristic data needed | Established (rank invariant under congruence); verified at sampled point (check 11); exact extent: for 2-dimensional orbits rank 2 at EVERY point (the insert names poles and 4-coordinate embeddings as representative loci, not the only ones) |
| 11 | Finite-N 't Hooft block values 0.345492 vs 0.146447 distinct | Established numerical fact for the two sampled instances K = 5, 8 (check 13); no genericity claim made |
| 12 | Relevance to NAMCG: the matrix model admits/realizes such a condensate class; the leaf is a spacetime chart | UNRESOLVED - not claimed; emergent-reading discipline kept (nothing proposed makes the leaf or metric fundamental) |
| 13 | Whether the bivector 1-jet fixes the embedding 2-jet in the 20-dim fiber of appH L140 | UNRESOLVED (stated as open in the insert) |
| 14 | Generic (non-Lie-type) noncentral condensates | UNRESOLVED for the bivector-field derivation; the dichotomy itself (claim 1) holds with no class restriction beyond unital algebra and states |

## Proposed changes

**One file, one insertion, nothing else.** `chapters/appH-microscopic-proofs.tex`: splice the single-paragraph
payload `insert-r1.tex` (2836 B / sha256/16 7657be68c8ffa5b4 / exactly 1 CRLF) at the Problem-A ledger PIN, i.e.
replace the unique pattern

    "does not close Problem~A.\r\n\r\n\paragraph{Missing step.}"   (count 1, rebuilt from CURRENT live bytes; measured offset 14892)

by the same head + payload + CRLF (one blank line) + tail. Anchor boundaries (verified to occur exactly as
quoted at the end of the integrated 107 paragraph, appH L142, and at L144): last original sentence before the
insert: "... do not derive the dictionary assumption, and this paragraph does not close Problem~A." (end of the
L142 paragraph); first original line after the insert: `\paragraph{Missing step.}` (L144). Both stay; every
existing sentence, equation, status passage and label stays; no stale passage elsewhere needs updating (the new
paragraph is the out-of-class complement of L142 and contradicts nothing: L142's sentence "chart-resolving data
must come from outside the class, namely from noncentral commutator (condensate) backgrounds ..." stays true and
is the passage this paragraph begins to cash out). Payload contains no `\ref`/`\eqref`/`\cite`/`\label`, no new
labels, no bib entries (hygiene H11); the CRLF layout and blank-line placement follow the 105/106/107 integrated
layout (payload line + exactly one blank line before `\paragraph{Missing step.}`).

The paragraph content is exactly the scope of Result items 1-5, and it CLOSES ITSELF with the explicit
non-closure list: "they do not compute the order-Theta^2 correction selected in the Lie-type class, they do not
determine whether a derived bivector germ fixes the embedding 2-jet within the 20-dimensional fiber of embedding
2-jets at fixed bivector 1-jet, they do not cover generic non-Lie-type condensates, and this paragraph does not
close Problem~A." Status labels are untouched anywhere; the paragraph asserts no status.

Expected POST (contract of `simulate_apply_108_r1c.py`, re-verified byte-identical at recovery): 815065 B /
sha256/16 dcfa82a524551702 / 3878 CRLF, delta +2838 B / +2 CRLF; undo verified True; **valid only against live
bytes 812227 B / 698f38979140770d / 3876 CRLF** (independently re-measured at recovery and equal to the digest
hash). Integrator must re-anchor the PIN from current bytes at integration time (the short string "does not
close Problem~A." occurs 3x post-107; the full-pattern PIN count is 1). Preview:
`scratch/sim/appH_after_108_r1_preview.tex` (815065 / dcfa82a524551702 / 3878).

## Verification scripts

All in this proposal folder; run from repo root with `python -I` (per memory: interpreter isolation). Reproduction
pack - exact commands and expected invariant outputs:

1. `python -I proposals/108-a-map-noncentral-chart-select/s4_noncentral_selection_v3.py`
   (SOLE SCRIPT AUTHORITY; deterministic, seed fixed). Expected: 16 lines `CHECK n ... PASS` and
   `TOTALS: PASS 16/16 FAIL 0`, exit 0. Invariants: C1 non-scalar dev 5.657, biv +/-4; C2 max |biv| 0.00e+00;
   C3 tr dev 2.96e-16, iC-Hermiticity dev 0.00e+00; C4 spread 8; C5 rel dev 6.05e-16; C6 dev 8.88e-16, values
   j = 2,3,4,6,8; C7 R^2 = 6,12,20,42,72, dev 3.42e-16; C8 var dev 4.44e-16, widths
   1.0000/0.7071/0.5774/0.5000/0.4082/0.3536/0.1414; C9 target 24, dev 5.34e-16; C10 dim 10, orth dev 0.500;
   C11 ranks 2/2/4; C12 rank 6 -> autdim 3, dev 0.00e+00; C13 devs 1/1, biv 0.345492 vs 0.146447; C14 dev
   1.11e-16; C15 24 points dev 0.00e+00, failure dev 2; C16 dev 1.11e-16.
   Recovery rerun: `scratch/s4_v3_rerun_r1.out` byte-identical to shipped `s4_noncentral_selection_v3.out`
   (2576 B / sha256/16 6fb8631fcecda151 / 18 CRLF).
2. `python -I proposals/108-a-map-noncentral-chart-select/hygiene_108_r1.py proposals/108-a-map-noncentral-chart-select/insert-r1.tex`
   (reads only the checked file; writes nothing). Expected: 21 `H.. PASS` + `HYGIENE TOTALS: PASS 21/21 FAIL 0`,
   exit 0; H21 self-record `file=insert-r1.tex sha256/16=7657be68c8ffa5b4`; H20 `bytes=2836`. Recovery rerun:
   `scratch/hygiene_108_rerun_r1.out` byte-identical to shipped `hygiene_108_r1.out`.
3. `python -I proposals/108-a-map-noncentral-chart-select/simulate_apply_108_r1c.py`
   (read-only on chapters/ - self-asserts `live appH unchanged after run: True`; writes only
   `scratch/sim/appH_after_108_r1_preview.tex`). Expected: PRE 812227/698f38979140770d/3876; PIN count 1 (short
   count 3, offset 14892); POST 815065/dcfa82a524551702/3878; delta +2838/+2; undo True; POST PIN count 1; live
   unchanged True. Recovery rerun: `scratch/simulate_108_r1c_rerun_r1.out` byte-identical to shipped
   `simulate_apply_108_r1c.out`; preview re-measured 815065/dcfa82a524551702/3878.
4. Provenance reruns (not part of the contract): v1 battery reproduces its recorded failure signature - 4 FAIL
   lines (checks 5, 6, 9, 12), no TOTALS, and stderr NameError `name 'k' is not defined` at line 306
   (`scratch/s4_v1_rerun_r1.out`, `scratch/s4_v1_rerun_r1.err`); v2 battery reproduces `TOTALS: PASS 15/16
   FAIL 0` with CHECK 12 the sole FAIL (`scratch/s4_v2_rerun_r1.out`). `mk_insert_108_r1.py` is the insert
   generator (not re-run at recovery; re-run regenerates byte-identically). `simulate_apply_108_r1.py`,
   `simulate_apply_108_r1b.py` are superseded label variants with identical measurements (inert).

Tool output is a check, not a proof: the derivations behind each invariant are in D1-D6; the scripts verify the
algebra, conventions and constants.

## Decisions Taken

- **D1 (script authority).** `s4_noncentral_selection_v3.py` declared SOLE SCRIPT AUTHORITY: diff analysis (D8)
  shows v1/v2 differ from v3 only by the three bug fixes, and the reruns reproduce each recorded failure
  signature; v3 is the corrected successor. v1/v2 retained unmodified as inert provenance. Rejected: deleting
  v1/v2 (provenance value), editing them (would falsify the record).
- **D2 (scalar-terms clause).** The insert's Lie-type clause "possibly with scalar terms ... equals
  c^{IJ}{}_K x^K" is exact when read affinely (adjoin the identity to the generating set: a scalar term s 1
  contributes c^{IJ}{}_0 omega(1) = c^{IJ}{}_0); in the finite-dimensional traceless setting checked here scalar
  terms cannot occur (check 3). Chose recording the exact hypothesis class over editing the insert: an edit would
  move the insert hash and invalidate the certified hygiene/simulate contract for zero mathematical gain, and the
  affine reading is the standard one. Gatekeeper may re-rule; the classification table states this explicitly.
- **D3 (insert kept as shipped).** `insert-r1.tex` not regenerated, not retyped, not edited; verified by triple
  (2836 / 7657be68c8ffa5b4 / 1 CRLF) + hygiene rerun + simulate rerun. This follows the tool-echo-death
  mitigation (byte-authority discipline) and the 107 salvage convention.
- **D4 (no new mathematics).** All reruns reproduced, so no new mathematics was added by the recovery agent; the
  proposal text is a faithful account of the shipped artifacts. Rejected: "completing" the package with fresh
  computations (would break the shipped-by-the-dead-agent provenance separation).
- **D5 (target).** Stayed on the dispatched edge (chain-4 head, derivation-first directive 2026-11-20), which
  the package serves with positive derivation-grade data; rejected: pivoting to relaxation (iii)/(iv) edges.

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step derived for the programme (Problem A remains
PROGRAMME-CONDITIONAL), no missing link closed without new unsupported inputs - the Lie-type class is an
additional hypothesis, not the NAMCG model. Same-chain precedent: 105/106/107 all `MILESTONE: none`.

## Status-label recommendation

Critical-path list re-derived from ch17 L700-712 and the appH ledger entries: A, B, C, D1, E, F, G-derived, N
(H, I, J optional within their scopes). All affected labels **unchanged**: Problem A stays OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL (appH L15-20, ch17 L377-378); A.map and every chain-4 edge keep their frontier state. No
label change is proposed or implied by the insert.

## Author decision needed

None. All choices taken here (D1-D5) change no status/priority/completion label, no Chapter 17 scope, no
critical-path set, no core assumption, and preserve emergent spacetime.

## Remaining open step

For the edge `A.map.noncentral-chart-select` and its consumer A.map:

1. **Matrix-model realization.** Exhibit a condensate/background class OF THE NAMCG MATRIX MODEL (ch03 action,
   locked-vacuum sector, or a named sector thereof) whose coordinate commutator is noncentral - currently the
   instance is the abstract spin-j fuzzy sphere, not an object of the manuscript's model. Whether the model's
   vacuum algebra admits a Lie-type class at all is unexamined.
2. **Rank-4 nondegenerate instance.** Construct a 4-dimensional orbit (or product/higher fuzzy orbit) whose
   derived bivector is nondegenerate - the fuzzy S^2 instance is rank 2 everywhere as ambient matrix and so, by
   the package's own obstruction (check 11), cannot supply the book's rank-4 chart 1-jet.
3. **Selection on the derived background.** Recompute the order-Theta^2 pullback selection (appH L140) with the
   x-dependent bivector produced by a noncentral condensate, and decide whether the derived bivector 1-jet fixes
   the embedding 2-jet inside the 20-dimensional fiber (this is the actual chart-selection question of the edge;
   the package supplies the datum and the gauge structure, not the B2 computation).
4. **Emergent reading.** Settle, within the book's emergent-spacetime discipline, whether a condensate leaf of
   this kind is a spacetime chart or an internal leaf; nothing in this package presupposes a fundamental
   spacetime, and any such presupposition must be excluded before integration-level claims are made.
5. Generic non-Lie-type noncentral condensates (dichotomy covers them for scalarity; the derived-field
   mechanism used Lie-type closure).

## Special instructions for the gatekeeper

- Script authority is `s4_noncentral_selection_v3.py` ONLY; v1/v2 outputs are historical failure signatures
  (reproduced at recovery, see D8) - do not treat them as current evidence.
- Test the insert clause-by-clause against the claim table's hypothesis classes. Specifically: claim 3's
  "noncommuting coordinates" condition (a traceless commutator that is zero IS scalar - the insert's
  noncommuting hypothesis is what rules that out); claim 4's scalar-terms reading (D2); claim 10's extent (rank 2
  holds at EVERY point of a 2-dim orbit, the insert's "poles ... every four-coordinate embedding" is a
  representative loci statement, and its 4-coordinate clause is precisely what makes rank < 4 unavoidable for a
  2-orbit).
- The package must NOT be read as: closing Problem A / A.map / the edge; the fuzzy sphere being a NAMCG
  condensate; a derived bivector resolving the embedding-2-jet fiber; or Theta^2 selection computed in the
  noncentral class. The insert states its own non-closure; keep any accepted text at that scope.
- Re-check the byte triples: live appH 812227 / 698f38979140770d / 3876; insert-r1.tex 2836 / 7657be68c8ffa5b4
  / 1 CRLF; POST contract 815065 / dcfa82a524551702 / 3878 (valid only against those live bytes; PIN rebuilt from
  current bytes). Recovery rerun outputs already on disk (paths above) - a fresh gatekeeper run should reproduce
  them byte-for-byte before re-deriving any check.
- What to re-derive first if short on time: the dichotomy iff (one-line polarization argument), the sharpness
  closed form (j/2 variance values + 1/sqrt(j)), and the dim-10 linearization (rank of K -> KJ + JK^T).
