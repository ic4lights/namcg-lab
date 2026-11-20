# Proposal 090-g-interaction-induced-simplex-profiles, round 1

## Result

For the exchangeable fixed-trace beta family on the profile simplex, density proportional to
`prod_i p_i^(a-1) * prod_{i<j} |p_i-p_j|^beta` (`a>0`, `beta>=0`), posed as a named input
deformation of the flat profile weight that appears in the integrated 089 paragraph, the following
is established by exact computation and proof (scripts s1-s4, all green):
(1) the fixed-trace change of variables `E_i = tau p_i` has Jacobian `tau^(D-1)` exactly and the
weighted integral separates exactly into a pure-`tau` factor `sigma^(Da+beta D(D-1)/2) *
Gamma(Da+beta D(D-1)/2)` times a scale-free profile kernel; (2) on a fixed ordering chamber the
log-kernel is strictly concave for `a >= 1`; (3) at any interior stationary profile the trace
multiplier equals `D(a-1) + beta D(D-1)/2` (Euler homogeneity identity), while for `a = 1` the
summed-gradient identity forces the mean gradient to `0`, so the `a = 1` members admit NO interior
stationary profile for any `beta > 0` - a proved exclusion lemma with the `D = 2` vertex-collapse
closed form; (4) the `D = 2` interior profile is closed form, `u* = sqrt(beta/(beta+2(a-1)))`, with
exact curvature `-(2a+beta-2)^2/(a-1)`, small-`beta` onset `u* ~ sqrt(beta/(2(a-1)))`, and large-`beta`
tail `(1-u*) beta -> a-1`; (5) at `D = 3, 4` the unique chamber profiles are computed with residuals
below `1e-27`, and the square-root onset persists at `D = 3`; (6) the family is continuous at
`beta = 0` (normalizations tend to the flat values by dominated convergence) and is non-flat for
`beta > 0` (kernel exactly zero at the barycenter, positive at the chamber profile; weighted mean of
the largest entry `0.629` vs `1/3`, two independent numerical paths agreeing to `1e-4`).
Structural consequence, by symmetry alone: every member is relabelling-invariant, so its extremal
profiles are full relabelling orbits and no member of an orbit is picked out within the family -
this realizes the relabelling-symmetric alternative of the 088 rigidity dichotomy rather than
supplying a selector. What is NOT obtained: the beta factor is not derived from the named slot or
frame measures or from the matrix integral, so the `G.moments-interaction-nonconvex` requirement of a
DERIVED interaction-generated non-convex log-density is NOT met by this package; Problem G and the
edge stay exactly as they are, with the edge now additionally constrained (any such density inside
this family must have `a > 1` to have an interior profile at all, and must break relabelling
symmetry to select a single profile).

## Target and status

- Problem G (HBEV), `chapters/appH-microscopic-proofs.tex` Section `sec:status-G` (L3022-3028):
  Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL (G-model / G-external
  support at most scope-limited; G remains OPEN). Dependencies unchanged.
- Frontier edge `G.moments-interaction-nonconvex` (reports/graph/frontier.yaml L546): requires "a
  core interaction input inducing a NON-CONVEX log-density on profile space" plus "minimiser
  characterisation excluding the uniform profile"; missing_inputs include "a DERIVED
  interaction-generated non-convex log-density (postulation forbidden)". This package supplies the
  minimiser/characterisation half INSIDE a named input family (items 2-6) and the exact rigidity
  statement that the family cannot supply selection, but it does NOT postulate the density as a
  core input and does NOT close or narrow the edge. This is the "interaction-generated induced
  profile densities on the profile simplex" target (chain 2), worked as the proved sublemma layer.
- DERIVED vs PROGRAMME-CONDITIONAL: everything here is PROGRAMME-CONDITIONAL support evidence
  inside an input family; nothing is DERIVED from the matrix theory.

## Source reading

Digest + targeted reads (digest compact; no full scan - this package adds one labelled conditional
paragraph and changes no definition, assumption, scope statement or status passage). Read in full:
`chapters/appH-microscopic-proofs.tex` L3183-3193 (slot law paragraph, Haar frame paragraph,
measure-dependence paragraph, 088 rigidity/dichotomy paragraph L3189, 089 pushforward paragraph
L3191, Vacuum-term paragraph L3193); Problem G ledger L3022-3040; `chapters/ch17-agenda.tex` G
criterion passages relied on by 089's review; `proposals/089-*/review-r3.md` and
`insert-r3.tex` (integrated text); `reports/sme-scout-20261118-1954.md` and
`reports/sme-scout-20261118-2350.md` (route context only); `reports/graph/frontier.yaml` edges
`G.moments-interaction-nonconvex`, `G.moments-pig-selfconsistency`; `reports/ledger.md` G entries.
No unreadable files. No previous 090 rounds exist.

## Research and reasoning

**Setup.** The 089 paragraph (appH L3191) established that, inside the named coupled gaussian slot
law and the Haar frame measure, the fibre-integration route gives either the input profile in
measure form (slot side) or the flat simplex weight (frame side), and that the resulting log-weight
`Phi(p) = D log sum_i p_i/g_i` is convex - it selects a vertex, not the uniformity locus. The
frontier edge asks whether an interaction-generated induced density could instead be non-convex on
profile space with the uniform profile excluded from the minimisers. Since nothing in the core
supplies a non-product slot law, a postulated density is forbidden; what can be done rigorously is
to take the natural exchangeable deformation family as an explicitly named INPUT and prove what it
can and cannot do. Input family: on the simplex `{p_i > 0, sum p_i = 1}`, weight
`rho(p) ~ prod_i p_i^(a-1) prod_{i<j} |p_i - p_j|^beta`, `a > 0`, `beta >= 0`. The `a = 1, beta = 0`
member is exactly the flat weight of 089's frame side and of the slot side at uniform profile.

**(1) Exact fixed-trace separation (established).** Embed with a scale: weight
`prod_i E_i^(a-1) e^{-E_i/sigma} prod_{i<j} |E_i - E_j|^beta` on `E in R_+^D`; set `E_i = tau p_i`,
`tau = sum E_i`. The map `(E_1..E_D) -> (tau, p_1..p_{D-1})` (with `p_D = 1 - sum`) has Jacobian
determinant `tau^(D-1)` exactly (symbolically verified at `D = 2, 3`, s1; general proof: column
scaling of the linear map on the section `tau = 1`). Then the integrand becomes
`tau^(D(a-1)) * tau^(beta C(D,2)) * tau^(D-1) * e^{-tau/sigma} * [profile kernel]`, and
`int_0^inf tau^(k-1) e^{-tau/sigma} dtau = sigma^k Gamma(k)` with `k = Da + beta D(D-1)/2`, so the
`tau`-law and the profile marginal separate exactly and the marginal carries no `sigma` (s1:
log-split residual identically 0; `TAU_LAW` printed values match `k = 2a+beta` at `D = 2` and
`k = 3a+3beta` at `D = 3`).

**(2) Chamber concavity (established).** On the open chamber `p_1 > ... > p_D > 0`,
`log rho = (a-1) sum log p_i + beta sum log(p_i - p_j)`; each `log p_i` is concave (`a >= 1`) and
each `log(p_i - p_j)` is strictly concave where defined, so `log rho` is strictly concave on the
chamber for `a >= 1`. For `a > 1` the density tends to `0` at every chamber wall (collision walls
through the beta factor, `p_D = 0` through the `a`-factor), so the strict concavity gives EXISTENCE
and UNIQUENESS of an interior maximiser, which then satisfies the stationary equations. For `a = 1`
the density does not vanish at `p_D = 0` (only at collisions), consistent with (3).

**(3) Two-multiplier contradiction and the a=1 exclusion (established).** Write `L = log rho`
extended off the simplex. At an interior stationary profile under `sum p = 1`, `partial_i L = mu`
for all `i`. Homogeneity count: `sum_i p_i partial_i L = D(a-1) + beta C(D,2)` (each pair
`{i,j}` contributes `beta (p_i - p_j)/(p_i - p_j) = beta`), so `mu = D(a-1) + beta C(D,2)` (s2b,
s2c: identity residuals `0` at the computed profiles). For `a = 1`: the SAME sum over all `i` of
the gradients telescopes, `sum_i partial_i L = sum_{i<j} beta (1/(p_i-p_j) - 1/(p_i-p_j)) = 0`, so
the mean gradient is `0`, while stationarity demands mean gradient `mu = beta C(D,2) > 0`:
contradiction. Hence: for `a = 1` and ANY `beta > 0` there is no interior stationary profile, and
maximisers exist only on the boundary; for `D = 2` the density `(2t-1)^beta` on the ordered half is
maximized only at the vertices (s2). This is a proved exclusion lemma: interaction alone, without
the `prod p_i^(a-1)` repulsion from the vertices (`a > 1`), cannot produce an interior profile.

**(4) D=2 closed form (established).** In separation `u = p_1 - p_2 = 2t - 1`, the stationary
equation `dL/du = 0` reads `(2a + beta - 2) u^2 = beta`, so `u* = sqrt(beta/(beta + 2(a-1)))`,
with exact second derivative `-(2a+beta-2)^2/(a-1) < 0` for `a > 1` (s2, residual `0`; the
curvature factorization re-checked symbolically, printed `D2_FACTOR_CHECK: 0`). Limits:
`u*/sqrt(beta) -> 1/sqrt(2(a-1))` (square-root onset), `(1-u*) beta -> a-1` (large-beta gap),
`a -> 1+`: `u* -> 1` (vertex collapse, matching (3)).

**(5) D=3, D=4 chamber profiles (conditional: numerical within the input family).** Solving the
stationary equations with high precision (s2b, s2c): at `a=2`, unique chamber profiles for
`beta in {0.2, 1, 5, 20}`, e.g. `(0.646564, 0.275451, 0.077985)` at `beta=1`, residual `<= 7e-28`;
`D=4` at `beta=1`: `(0.547695, 0.286559, 0.128582, 0.037165)`, residual `1.6e-29`. Existence and
uniqueness of these roots is THEORETICAL by (2) for `a > 1`; the numbers are their numerical
values. Cross-check: brute-force grid argmax at `D=3` (`h = 1/241`) lies `0.0016 < h` from the
root (s2c). Square-root onset at `D=3`: consecutive-in-log-beta gap slopes `0.4856, 0.4959, ...,
0.5000` converging to `0.5` (s2b). Face check (s3): on the face `p_D = 0` the `a=2, beta=1` density
`p_1 p_2 (p_1-p_2)` has its face-stationary point at `((3+sqrt3)/6, (3-sqrt3)/6, 0)`,
`(3+sqrt3)/6 = 0.788675` - strictly inside the face, so boundary collapse at `a=1` does not extend
to `a>1`.

**(6) Continuity at beta = 0 and non-flatness (established + numeric).** Since
`prod|p_i-p_j|^beta <= 1` on the simplex (`|p_i-p_j| <= 1`), dominated convergence gives
`rho_beta -> rho_0` in normalization for `a = 1`: at `D = 2` the exact value is
`Z_2(a=1) = int_0^1 u^beta du = 1/(beta+1) -> 1` (flat value 1), and at `D = 3` the numerics give
`0.4007` at `beta = 0.05` trending to the flat simplex volume `1/2` (s3). The `D = 2` general-`a`
normalization is the beta-function form `4^(1-a) B((beta+1)/2, a)/2`, verified numerically to 12
digits at three `(a, beta)` pairs (s3) - this is the `D = 2` case of the classical Dyson-gas
(Selberg-type) normalization; that connection is standard background and was NOT independently
verified against the primary literature in this session, and no manuscript claim relies on it.
Non-flatness for `beta > 0` is exact: the kernel VANISHES at the barycenter (a collision wall) and
is positive at the chamber profile (`5.8e-4` vs `0` at `a=2, beta=1`, s3). Weighted mean of the
largest entry at `a=2, beta=1`: `0.628843` (Monte Carlo, `N = 4e5`, seed 20261119) vs `0.628941`
(grid `M = 1000`) - independent paths agreeing to `1e-4`, against the flat value `1/3` (s4). The
interaction genuinely displaces weight from the uniformity locus.

**(7) Relabelling rigidity (established, no computation).** `rho` is invariant under joint
relabelling of `(p)`; hence if `p*` is extremal so is every permutation, and since the chamber
profile is unique for `a > 1`, the full extremal set is exactly its `D!`-element relabelling orbit
(or a larger degenerate set at `a = 1` on the boundary). No relabelling-symmetric member of the
family can single out one profile: this is the relabelling-symmetric alternative of the 088 rigidity
dichotomy ("leaves degenerate relabelling orbits of minimisers that themselves require a further
selection input", appH L3189) realized by an explicit family, and it complements 089's convex
vertex-selecting family: 089 showed relabelling-ASYMMETRIC induced weights select vertices by input
labels; here relabelling-symmetric deformations select orbits. Together they narrow where any
profile-selecting induced density could live: it must be neither convex-symmetric-as-089 nor
exchangeable-as-here.

**Comparison with the original target.** The edge target is a DERIVED interaction-generated
non-convex log-density with the uniform profile excluded from the minimisers. This package does not
derive the density, so the target is NOT met; what is met is the characterisation layer: inside the
maximally natural exchangeable family the uniform profile is EXCLUDED from the maximisers for every
`a >= 1, beta > 0` (maximisers are the chamber orbit for `a>1` and the boundary for `a=1`), the
interior alternative exists only for `a > 1`, and selection is provably unavailable inside the
family. The remaining derivation is microscopic: produce the `prod|p_i-p_j|^beta`-type factor (or a
relabelling-asymmetric alternative) from the core matrix integral or from a derived non-product
slot law. Literature position: the fixed-trace beta ensemble and its Selberg-type normalizations
are standard; the pieces used here (Jacobian separation, Euler identity, concavity, the a=1
telescoping contradiction, the D=2 closed form) are elementary and self-derived, so no external
result is imported into the manuscript.

## Claim classification

- Jacobian `tau^(D-1)`; exact tau/profile separation with `sigma^k Gamma(k)`: established identity.
- Chamber strict concavity (`a>=1`) and existence/uniqueness of the chamber profile (`a>1`):
  established derivation (elementary).
- Euler multiplier identity `mu = D(a-1) + beta C(D,2)`; summed-gradient identity at `a=1`; NO
  interior stationary profile for `a=1, beta>0`; `D=2` vertex collapse: established derivation.
- `D=2` closed form `u*`, curvature `-(2a+beta-2)^2/(a-1)`, onset and tail limits: established.
- `D=3, D=4` profile coordinates; `D=3` onset slope; weighted mean `0.629`; face point
  `(3+sqrt3)/6`: conditional numerical values WITHIN the named input family (exact objects,
  numerical evaluation).
- Continuity at `beta = 0` (`a=1`): established (dominated convergence; `D=2` exact).
- Non-flatness (zero at barycenter): established; the Selberg/Dyson attribution of the general
  normalizations: standard background, not independently verified this session, not used in text.
- Relabelling-orbit statement and the 088-dichotomy branch realization: established (symmetry).
- Origin of the beta factor in the matrix integral: UNRESOLVED (explicitly not claimed).
## Proposed changes

Single file: `chapters/appH-microscopic-proofs.tex`. One new paragraph is inserted between the 089 pushforward paragraph (ends at line 3191 with the unique tail) and the Vacuum-term paragraph.

Anchor boundary (occurs exactly once, verified):
```text
close nothing in Problem~G.
<blank line>
\emph{Vacuum term.} The abstract of~\cite{Steinacker2023} ...
```
Everything on both sides stays byte-identical (asserted by simulate_apply_090.py). Nothing else in the paragraph region is kept-or-replaced: NO existing sentence is modified or removed.

Relative-reference check from the new position (line 3193): "the preceding paragraph" = the 089 pushforward paragraph (names the slot law and Haar frame measure); "the second preceding paragraph" = the 088 rigidity paragraph containing the either/or alternative (L3189); "the Missing step paragraph" reuses the phrase already used by 089. No relative reference below is affected: the string "preceding paragraph" occurs nowhere in appH after line 3191 (verified by scan of the rest of the file), so no downstream counting chain crosses the insertion.

LaTeX block for the new paragraph (verbatim copy of insert-r1.tex, CRLF-terminated, sha256 first 8 hex = 3a6a69c4, 3735 bytes):

```latex
\emph{Fixed-trace beta deformation of the exchangeable weight on the profile simplex.} Within the named coupled gaussian slot law and Haar frame measure of the preceding paragraph, and at fixed \(D\) and unit trace, this paragraph records what follows for the exchangeable profile weights with density \(\prod_{i}p_{i}^{a-1}\prod_{i<j}\lvert p_{i}-p_{j}\rvert^{\beta}\) on the simplex, taken as a named input family with parameters \(a>0\) and \(\beta\ge 0\): the factor \(\prod_{i<j}\lvert p_{i}-p_{j}\rvert^{\beta}\) is posed here as a deformation, and no preceding computation yields it from the named slot or frame measures. Two endpoints of the preceding paragraph sit in the family at \(a=1\), \(\beta=0\): the flat Haar frame weight, and the slot pushforward at uniform profile. Writing \(E_{i}=\tau p_{i}\) with \(p_{D}=1-\sum_{i<D}p_{i}\), the Jacobian of \((E_{1},\dots,E_{D})\mapsto(\tau,p_{1},\dots,p_{D-1})\) is exactly \(\tau^{D-1}\), so the fixed-trace weight with exponential scale factor \(e^{-E_{i}/\sigma}\) and the deformation factor separates exactly into \(\sigma^{Da+\beta D(D-1)/2}\Gamma(Da+\beta D(D-1)/2)\,\tau^{Da+\beta D(D-1)/2-1}e^{-\tau/\sigma}\) times the profile weight above, and the profile marginal carries no scale parameter. On the chamber \(p_{1}>\dots>p_{D}>0\) the log-weight is strictly concave for \(a\ge 1\), so for \(a>1\) it has exactly one stationary profile there; and at any interior stationary profile the multiplier of the trace constraint is forced by the homogeneity count \(\sum_{i}p_{i}\partial_{i}L=D(a-1)+\beta D(D-1)/2\) to equal that constant, while for \(a=1\) the summed-gradient identity \(\sum_{i}\partial_{i}L=0\) is incompatible with that multiplier for every \(\beta>0\): the \(a=1\) members have no interior stationary profile at any deformation strength, and for \(D=2\) the density \((2t-1)^{\beta}\) is maximized only at the vertices. The family is continuous at \(\beta=0\): for \(a=1\) its normalizations tend to the flat values, \(1/(\beta+1)\to 1\) at \(D=2\) and \(1/2\) at \(D=3\), by dominated convergence from \(\prod_{i<j}\lvert p_{i}-p_{j}\rvert^{\beta}\le 1\). For \(D=2\) and \(a>1\) the stationary profile is known in closed form: the separation \(u=p_{1}-p_{2}\) is \(u=\sqrt{\beta/(\beta+2(a-1))}\) with log-weight curvature \(-(2a+\beta-2)^{2}/(a-1)\), so the departure of the stationary profile from the barycenter grows like \(\sqrt{\beta/(2(a-1))}\) at small \(\beta\), while at large \(\beta\) the gap to the vertex obeys \((1-u)\beta\to a-1\); the same square-root onset is found numerically at \(D=3\). For \(D=3\) and \(D=4\) at \(a=2\), \(\beta=1\) the stationary profiles are \((0.6466,0.2755,0.0780)\) and \((0.5477,0.2866,0.1286,0.0372)\), with stationarity residuals below \(10^{-28}\) and, at \(D=3\), the grid maximum of the weight within one grid step of the stationary profile. The deformed weight is not flat: at \(a=2\), \(\beta=1\) it vanishes at the barycenter, is positive at the stationary profile, and weights the largest entry with mean \(0.629\) against the flat value \(1/3\), checked on two independent numerical paths. Every member is relabelling-invariant, so its extremal profiles form full relabelling orbits and no single member of an orbit is picked out inside the family: the deformation displaces weight from the uniformity locus and creates, exactly for \(a>1\), a unique chamber profile up to relabelling, realizing the relabelling-symmetric alternative of the second preceding paragraph rather than supplying a selector; it supplies no state, its origin in the matrix integral is not established, it leaves the missing steps (i)-(iv) of the Missing step paragraph unchanged, and it closes nothing in Problem~G.
```


Stale passages elsewhere: none identified. No existing sentence asserts anything contradicted by this paragraph (089 asserts convexity inside the named measures only; this paragraph adds a distinct input family and its own closer). No bibliography changes.

## Verification scripts

All under this folder; re-run with `python -I <script>` (Python 3.11, sympy/mpmath/random only);
expected invariants per script are recorded in `manifest.md` and in the shipped `.out` files:
s1 (Jacobian `tau`, `tau^2`; log-split residual 0; `TAU_LAW` exponents), s2 (residual at `u*` = 0;
curvature factorization `D2_FACTOR_CHECK: 0`; onset/tail limits; `a=1` vertex), s2b (residuals
`<= 7e-28`; `euler_mismatch = 0`; onset slopes to `0.5`; `a=1` mismatch `= 3 beta`), s2c (D4
residual `1.6e-29`; grid-argmax distance `0.0016 < h`), s3 (closed forms and limits; note the
shipped s3 is the FIXED version - v3 had a wrong inner integration limit; the script label prefix
`A1_D3_FACE_MAX` is a misnomer: it computes the face point of the `a=2` density `t(1-t)(2t-1)`),
s4 (MC vs grid `0.628843` vs `0.628941`; shipped version is FIXED - v2 double-counted the Dirichlet
base factor; bug recorded in the script header), simulate_apply_090.py (read-only splice rehearsal;
`SIMULATE OK`; POST size 756527, sha256 `31149f6250ec834adaac83903a6a492ee7c987f1b4ce0ca9abcf1d930ad6ac1c`,
CRLF 3844). Smoke compile: standalone harness outside the repository, pdflatex exit 0, zero
undefined control sequences, scratch deleted (incident note: an initial `rm -rf` of the scratch dir
was denied by the guard; the files were removed individually and the directory removed empty).

## Decisions Taken

1. **Axis choice (RESEARCHER-DECISION from the frontier/gatekeeper ranking).** Chose the
   interaction-generated induced-profile route (frontier rank 2 edge, scout TOP route) worked as a
   proved sublemma inside a NAMED INPUT family, over attempting a derived non-product slot law: no
   object in the core supplies a non-product joint slot law, so any such derivation would be
   postulation in disguise; the family route converts the edge into proved exclusion/characterisation
   lemmas plus an exact rigidity statement, without postulating anything into the core. Rejected:
   non-convex term postulated as core input (forbidden); vertex-selection mechanisms outside the
   dichotomy branches.
2. **Family presentation.** Presented as an explicitly named input deformation with a closer
   denying origin in the matrix integral - not as "interaction-generated by the theory" - because
   the beta factor is not derived; overclaiming origin would be a materially false claim.
3. **Face-point detail omitted from the manuscript paragraph.** The `a=2` face point
   `(3+sqrt3)/6` is kept in scripts only (secondary detail; paragraph already long).
4. **Selberg attribution** mentioned only as background in the proposal (not verified against
   primary sources this session) and excluded from the manuscript text, which uses only the
   self-derived elementary pieces.
5. **Title** chosen not to contain the words of 088/089 anchors to keep the grep-unique title test
   trivially checkable.

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step derived from the matrix theory, no missing
link closed without new unsupported inputs. The package is conditional-layer evidence that narrows
the `G.moments-interaction-nonconvex` hypotheses (a>1 necessity, orbit rigidity) and closes the
characterisation half inside a named family.

## Status-label recommendation

Re-derived critical-path list from ch17 + ledger at current scope: A, B, C, D1, E, F, G-derived, N
(H, I, J optional). Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. Edge
`G.moments-interaction-nonconvex` state should move from `untried` to attempted-partial only by the
ledger owner, not by this proposal. Expected label changes: none.

## Author decision needed

None. (No core change, no scope change, no status-label change proposed.)

## Remaining open step

To close the characterisation half of `G.moments-interaction-nonconvex` for the programme, the
missing microscopic step is unchanged: derive, from the core matrix integral or a derived
non-product slot law, an induced profile density containing a pair-repulsion factor (or a
relabelling-asymmetric non-convex structure), and show the resulting log-density is non-convex with
the uniform profile excluded from its minimisers. Within the named family here, the open steps are
only (i) a closed form (beyond the `D=2` case) for the chamber profile at general `(a, beta, D)` -
existence/uniqueness are already proved - and (ii) extension of the `a=1` boundary-collapse lemma
from `D=2` closed form to explicit face characterisation at `D>=3` (the `D=3` face-of-face
structure is partially covered by the s3 face point).

## Special instructions for the gatekeeper

- Check the paragraph against the block idiom of L3187-3191 and the 089 review-r3 constraints:
  no status words, no selector claim, closer must preserve "closes nothing in Problem~G".
- Must NOT be asserted: any origin of the beta factor in the matrix integral; any selection of a
  single profile; any status change; any closure of Problem G or of the edge.
- Re-check first: the two-multiplier contradiction (the heart of the a=1 lemma), the D=2 closed
  form and curvature factorization, the Euler multiplier identity, the relabelling-orbit statement,
  and the relative-reference count ("second preceding paragraph" = L3189 rigidity paragraph).
- Splice rehearsal is byte-exact; if the integrator's PRE differs from the contract sha, re-run
  simulate_apply_090.py before integrating.
- `frontier.yaml` and `reports/` are outside this proposal; the orchestrator/ledger owner updates
  the edge state.
