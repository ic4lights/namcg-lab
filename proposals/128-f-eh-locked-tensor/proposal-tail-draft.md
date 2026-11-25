## Research and reasoning

### The question, exactly

The integrated item-123 Alternate-scope paragraph (live appH line 3224, one line) fixes a
truncation of the Problem-F heat-kernel evaluation in which the tensor sector is "an input
Laplace-type block of ten symmetric-tensor components with fibre-traced endomorphism
`tr E_ten = e_h R_E`" - a SUPPLIED parameter. The frontier edge asks for `e_h` to become a
derived quantity: computed from the tensor-block endomorphism of the LOCKED ACTION for a
named class of locked backgrounds and fibre data, under the TOTAL-trace convention (the
convention fixed by review-123-r1 finding 1; the per-component reading of appH L2093-2114
would give `10/6 - 10 e_h` instead of `10/6 - e_h`, and the record uses the total-trace
reading - script 1 verifies the bookkeeping identity `(10/6 - e_h) R` from
`tr E_ten = e_h R_E`, and every intermediate below is total-trace unless stated).

The locked action itself does not supply the answer: the manuscript records at appH
L2039-2041 that the displayed quadratic action "also does not exhibit the Fierz-Pauli
structure used as hypothesis 5 of Theorem thm:mT, so any tensor-block terms beyond it are
an additional input". So the derivation must name a completion of the tensor block. The
natural one - and the one the Alternate-scope paragraph itself gestures at by gauge-fixing
with `F^mu = g^{ab} Gamma^mu_{ab}` - is the Einstein-Hilbert completion.

### Hypothesis H1

**H1.** The ten-component tensor block of the locked action is the quadratic
Einstein-Hilbert action of the metric sector about the fixed background of
Assumption ass:aux-metric, gauge-fixed by the harmonic functional
`F^mu = g^{ab} Gamma^mu_{ab}` with `S_gf = (1/2) int sqrt(g) g^{mn} F_m F_n`, in the
curvature conventions eq:christoffel/eq:riemann of ch02 (metric signature (-,+,+,+)), with
the unit-sphere calibration `R = +2` (script 1, `SPHERE_R = 2`).

H1 is a hypothesis, not a claim about `eq:Smicro`: it names the unique standard completion
whose flat limit is the massless Fierz-Pauli block eq:FP - the operator class that
Section sec:ch1-checklist item 3 requires of `T_{mu nu}` - and it is exactly the operator
the ghost sector of the item-123 paragraph is built over. Defending satisfiability in
F-scope is by construction: under H1 every object the Alternate-scope paragraph specifies
(principal symbol, endomorphism Laplace-type form, ghost operator `M xi = g^{ab}
nabla_a nabla_b xi + R^mu_nu xi^nu`, ghost weight -2 via eq:appA-sector-sum) exists and is
computable; what remains unproved is that the locked action IMPLIES H1.

### Method (script 2, exact symbolic)

Background `gbar = e^{2w} delta`, `w = (1/2) C_{mu nu} x^mu x^nu`, `C` constant symmetric
(10 independent symbols). This conformal family is the standard point-source normal form:
at `x = 0`, `g = delta`, `dg = 0`, `Gamma = 0`, while `Ric_{mu nu}(0) = -(1/2)(d_a d_b
C_{mu nu} ...)`-type linear functions of `C` give 10 independent curvature components
(script 2 prints `R0` and uses `Ric0` as a general matrix). A natural fibre endomorphism
coefficient is a scalar invariant, so if it is background-independent it can be read off
ANY background in the family; independence is then verified by differentiating against all
10 components of `C` (`EH_SCALAR_OK`).

Perturbation `g = gbar + eps H`, `H` CONSTANT symmetric (this is the fibre-coordinate
choice: `H` IS the fibre vector; the constant-fibre restriction is what isolates the
endomorphism from the Laplace-Beltrami kinetic part, whose density contribution is
quadratic in `x`-derivatives of `H` and vanishes for constant `H` at `x = 0` after the
`Gamma(0) = 0` simplification). Because `dg = dgbar` is eps-independent, `Gamma(g)` is
EXACTLY polynomial of degree 2 in `eps` (the inverse is a geometric series terminating at
`eps^2`: `g^{-1} = gbar^{-1} - eps gbar^{-1} H gbar^{-1} + eps^2 gbar^{-1} H gbar^{-1} H
gbar^{-1}` with `gbar^{-1} = e^{-2w} I`), so the `eps^2` coefficient of the density
`sqrt(det g) (g^{mu nu}(d_lam Gamma^lam_{mu nu} - d_nu Gamma^lam_{mu lam}) +
g^{mu nu}(Gamma^lam_{mu nu} Gamma^kap_{lam kap} - Gamma^kap_{mu lam} Gamma^lam_{nu kap}))`
plus `S_gf` is exact polynomial algebra (no series expansions); `sqrt(det g) = e^{4w}
sqrt(det(1 + eps e^{-2w} H))` is truncated exactly at `eps^2`.

The `eps^2` density coefficient at `x = 0` is `(1/2) H (N + E) H` in fibre coordinates with
`(N H)|_0 = delta^{ab} d_b Gamma^rho_{a mu} H_{rho nu} + (mu <-> nu)` (the symmetrized
covariant-Hessian piece `-g^{ab} nabla_a nabla_b H`, exact at `x = 0` since `Gamma(0) = 0`),
so `E = Hess_{fib}(density)/2 - sym N` is extracted by fibre differentiation:
`M0 = (1/2) d^2/dy_p dy_q`, `E = M0 - (NM + NM^T)/2`.

Results (script 2, out-e_h-128.txt):
- `GF_SHIFT = 0`: the harmonic gauge-fixing density contributes NO `H`-bilinear
  `eps^2` term at `x = 0` - the endomorphism read from constant fibre directions is the
  gauge-fixing-independent one (the gauge fixing only affects the longitudinal kinetic
  part).
- `E_SYMM = True`: the extracted `E` is symmetric (required for a self-adjoint block and
  for `a_1` hermiticity bookkeeping, appH Hermitian-block paragraph).
- `EH_LICH = __EH__` and `EH_SCALAR_OK = 0`: `tr E / R` is the constant __EH__, independent
  of all ten `C` components - this is the derived `e_h^{(H1)}` (total-trace reading).
- `E_TT_TRACE_over_R = __TT__`: trace of `E` restricted to the 9-dimensional traceless
  fibre (6 off-diagonal + 3 diagonal traceless combinations), which in general differs
  from `e_h^{(H1)}` - the two readings (total trace vs traceless-fibre trace) must not be
  conflated.
- `STRUCT_TR = __STRUCT__`: total fibre trace / `R` of each natural curvature-linear
  structure `riem (R_{mu r nu s} h^{rs})`, `ric1 (Ric_{mu r} h^r_nu)`,
  `ric2 (Ric_{r nu} h^r_mu)`, `gric (g_{mu nu} Ric_{rs} h^{rs})`,
  `ricg (Ric_{mu nu} tr h)`, `ggr (R g_{mu nu} tr h)`.
- `E_DECOMP = __DECOMP__`: exact linear solve of `E = sum_k a_k SM[k]` at two random
  integer `C`-points (seed 128) in the six structures, residual check.
- `GHOST_RESID_M = __GHOST__`: `-(d_xi F)^mu` linearized at the family point equals
  `(g^{ab} nabla_a nabla_b xi + Ric xi)^mu` at `x = 0`. The linearization uses the exact
  `x = 0` formula `dF_1 = delta^{ab} (1/2) delta^{mu lam} (d_a Lg_{b lam} + d_b Lg_{a lam}
  - d_lam Lg_{ab})` with `Lg = nabla xi + (nabla xi)^T` (valid because `Gamma(gbar)|_0 = 0`
  kills the `g^{-1}`-variation term `-Lg^{ab} Gamma^mu_{ab}`); `xi = q + B x` so `d Lg` is
  general at the point. This derives the item-123 ghost operator (closing the
  "standard-textbook status, not independently re-derived end-to-end" note of
  review-123-r1) rather than assuming it.

The invariant-theory lemma behind `EH_SCALAR_OK`: the fibre trace of any natural,
curvature-linear fibre endomorphism of a natural bundle is a natural scalar that is linear
in the curvature tensor; the only such scalar (contracting the curvature to a scalar with
the metric) is a constant multiple of `R`. Hence `tr E = c R` for a single number `c`
independent of the background - verified numerically-symbolically rather than quoted.

### The sigma bookkeeping (unconditional structural part)

Curvature-linear endomorphism additions that vanish on the 9-dimensional traceless fibre
are exactly those of the form `(b Ric_{mu nu} + c R g_{mu nu}) g^{rho sigma} h_{rho sigma}`
(the map factors through the fibre trace; symmetry under `(mu nu) <-> (rho sigma)` - formal
self-adjointness of the block - forces the same combination in both slots). Script 2
derives their total fibre traces: `ricg -> R`, `ggr -> 4 R` (STRUCT_TR), so
`e_h -> e_h + (b + 4 c)`, i.e. a single unrestricted real parameter `sigma = b + 4c`,
invisible to traceless-fibre (TT) propagation:

    e_h = e_h^{(H1)} + sigma,  sigma in R unknown unless the pure-trace completion is fixed.

(Transversality cannot constrain this: it constrains derivative terms, and `sigma` lives in
the zero-order part.) The iff-reduction: `e_h` is determined by tensor-block data that
cannot see the trace fibre (e.g. TT graviton propagation, or `eq:FP`-class flat data) if
and only if the pure-trace zero-order completion is determined - and no flat datum can
determine it, since all these completions share the flat limit (massless FP block eq:FP).
This is a sharpened restatement of the appH L2039-2041 obstruction localized to `e_h`, not
a new no-go beyond it; it transfers to any attempt to derive `e_h` from the quadratic
Hessian paragraph alone.

### Consumption by the item-123 record (script 3, self-contained)

Script 3 re-derives the Alternate-scope algebra WITHOUT running any item-123 script (the
author kill-order on `verify_ghost_op_123.py` is honored; no 123 script executed):
`a1_sc16 = 16(1/6 - Q)`, `a1_ten = 10/6 - e_h`, `a1_gh = 4/6 + 1` with ghost weight `-2`
give `A1 = 16(1/6 - Q) + n_K (1/6 - Q_K) - 5/3 - e_h` (`A1_MATCH_123 = True`),
`N0 = 18 + n_K` (`N0_MATCH_123 = True`), and the windowed bracket matches
(`WINDOW_MATCH = True`). `COND_IV_EH = [-5/3]`: the record's condition (iv) vanishing at
`Q = 1/6, n_K = 0` holds iff `e_h = -5/3`. Substituting the derived value (`e_h = e_h^{(H1)}`)
the trunk coefficient is `A1_derived_Q16nK0 = -5/3 - e_h^{(H1)}` and condition (iv) becomes
the explicit, falsifiable requirement on the completion coefficient:

    sigma = -5/3 - e_h^{(H1)}   (script 3: SIGMA_for_cond_iv = __SIGMA__)

With `e_h^{(H1)} = __EH__` this is `sigma = __SIGMA__` - in particular NOT automatically
satisfied, so the derived value does not manufacture the record's condition (iv): it states
precisely which pure-trace completion would realize it. (Control run with `e_h = 0`
confirms `COND_IV_HOLDS = False`, out-ehsum-0.txt; symbolic run gives `COND_IV_EH = -5/3`,
out-ehsum-iv.txt.)

### Comparison with the original target

Original edge target: derive `e_h` so the item-123 evaluation consumes a DERIVED input.
Given: an explicit derived value under H1, an unconditional iff-reduction localizing the
residual freedom to one number `sigma`, a proof that flat locked data cannot fix it, and
the ghost-operator derivation. NOT given: H1 itself as a theorem about `eq:Smicro` (the
gating missing step of the section), and any `sigma` value. The a1 evaluation and the
windowed coefficient now consume `e_h^{(H1)} + sigma` with a derived `e_h^{(H1)}` instead
of a free parameter: the supplied input is downgraded to an explicitly characterized
one-parameter ambiguity plus a derived constant.

## Claim classification

- `SPHERE_R = 2`, `A1_TENSOR_R` bookkeeping identity, `A1/N0/WINDOW_MATCH_123`,
  `COND_IV_EH = -5/3`, `GF_SHIFT = 0`, `E_SYMM`, `EH_SCALAR_OK = 0`, `GHOST_RESID_M = 0`,
  STRUCT_TR traces, E_DECOMP residual: **established derivations** (exact symbolic,
  scripts 1-3 reproducible).
- `e_h^{(H1)} = __EH__`: **conditional result** (theorem under H1; H1 is stated and its
  satisfiability in F-scope is by construction, but H1-as-consequence-of-`eq:Smicro` is
  unresolved).
- H1 as the actual locked-action tensor block: **conjecture/mechanism** (named operator
  class of sec:ch1-checklist item 3; NOT derived from `eq:Smicro`).
- `sigma = b + 4c` parametrization of trace-fibre completions and TT-invisibility:
  **established** (structural, curvature-linear class); "the locked completion's sigma is
  unknown": **unresolved step**.
- `Q = 1/6`, `Q_K`, `n_K`: phenomenological **inputs** of the record, untouched.
- "No flat datum fixes sigma or H1": **established conditional argument** (all
  completions in the class share the flat limit; consistent with and localizing appH
  L2039-2041).
- Everything else in the payload: restatements of integrated text (checked line by line)
  or explicit non-claims.

## Proposed changes

### chapters/appH-microscopic-proofs.tex - one inserted paragraph (P1)

Insert ONE new paragraph immediately BEFORE the Alternate-scope truncation paragraph of the
Problem F ledger section (so "the Alternate-scope truncation below" reads correctly).

- Anchor (exact bytes, occurs exactly ONCE in live file - verified against live bytes
  6839a5cab30e, count = 1): line-initial text
  `\paragraph{Alternate-scope weighted sector data`
- Kept: everything; nothing is reworded or removed. The paragraph is additive.
- Payload = file `payload-P1.txt` (pin: __PAYSIZE__ bytes, sha1_12 __PAYSHA__), CRLF line
  endings, ASCII, no new `\label`, no `\cite`, no status/priority/completion wording, one
  scoped closing sentence; spliced copy for gatekeeper inspection:
  `appH-spliced-P1.tex` (PRE __PRESIZE__ B 6839a5cab30e -> POST __POSTSIZE__ B, POST =
  PRE + payload exactly; hygiene guards with positive controls in
  `out-make-payload-128.txt`).

latex
__PAYLOAD_ESCAPED__

- Stale-passage check elsewhere: the Alternate-scope paragraph keeps "with fibre-traced
  endomorphism ... e_h R_E" (it is the record of the truncation and stays valid verbatim:
  P1 does not redefine `e_h`, it derives the H1 value and states `e_h = e_h^{(H1)} +
  sigma`); no other passage in appH/ch17 quotes `e_h` numerically (grep of live bytes for
  `e_h`: only the Alternate-scope line and its condition (iv) clause) - no other edits
  needed. ch17 untouched.
- No bib changes.

## Verification scripts

All run from the repo root as `python -I <path>`; captures live next to the scripts.

1. `verify_conventions_128.py` -> `out-conventions-128.txt`. Conventions: eq:christoffel
   / eq:riemann on the unit 2-sphere give `SPHERE_R = 2`, `Ric_11 = sin^2(theta)` printed
   with `SPHERE_Ric11_minus_g11 = 0`; gauge-field calibration on S^2 gives
   `GAUGE_a1_S2 = 8/3`, ratio `4/3` (sanity on `a_1 = tr(R/6 - E)`); total-trace
   bookkeeping `10/6 - e_h` from `tr E = e_h R` confirmed symbolically
   (`A1_TENSOR_R holds: True`). Expected invariants: `SPHERE_R = 2`, ratio `4/3`, `True`.
2. `verify_eh_128.py` -> `out-e_h-128.txt`. Main derivation (see Research and reasoning).
   Expected invariants (reproduction pack): `GF_SHIFT = 0`; `E_SYMM = True`;
   `EH_SCALAR_OK = 0`; `EH_LICH = __EH__`; `E_TT_TRACE_over_R = __TT__`;
   `STRUCT_TR = __STRUCT__`; `E_DECOMP` entries with residual `True`;
   `GHOST_RESID_M = [0, 0, 0, 0]`; `Q16_TRUNK = 8/3 - __EH__`
   (`= 16*(1/6) + (10/6 - e_h) - 5/3`: an independent recomputation inside script 2 of the
   sector sum with the scalar piece kept at `16*(1/6)`; subtracting `16*(1/6)` gives the
   tensor+ghost trunk, so this must equal `16*(1/6) + A1_derived_Q16nK0` of script 3,
   both reducing to `8/3 - __EH__` / `-5/3 - __EH__` respectively); `SCRIPT2_DONE`.
3. `verify_ehsum_128.py` (no arguments) -> `out-ehsum-iv.txt`:
   `A1_MATCH_123 = True`, `N0_MATCH_123 = True`, `WINDOW_MATCH = True`,
   `COND_IV_EH = [-5/3]`, `PASS3`.
   `verify_ehsum_128.py __EH__` -> `out-ehsum-derived.txt`:
   `E_H_INPUT = __EH__`, `A1_derived_Q16nK0 = __A1D__`, `SIGMA_for_cond_iv = __SIGMA__`,
   `COND_IV_HOLDS = False` (for `__EH__ != -5/3`), `PASS3`.
   `verify_ehsum_128.py 0` -> `out-ehsum-0.txt`: control run, `COND_IV_HOLDS = False`.
   No item-123 script is run (author kill-order on `verify_ghost_op_123.py` honored).
4. `make_payload_128.py __EH__` -> `out-make-payload-128.txt`: rebuilds `payload-P1.txt`,
   asserts live anchor count 1, splices into `appH-spliced-P1.tex`, asserts POST = PRE +
   payload bytes, hygiene guards fire on injected positive controls (label token, bare LF,
   brace imbalance) - `CTRL_FIRES = (True, True, True)`, `ANCHOR_COUNT = 1`, `GEN PASS`,
   prints PAY/PRE/POST pins. Re-running the generator must reproduce the pinned payload
   bytes (deterministic template + argv value).

## Decisions Taken

- **Completion named = H1 (harmonic-gauge-fixed quadratic Einstein-Hilbert).** Rejected:
  (i) Lichnerowicz-on-flat-scaffold toy (outside the locked-action class - dispatch
  explicitly excludes it); (ii) minimal `nabla^* nabla` completion alone (not a
  completion of the diffeo-invariant quadratic action; differs from H1 by exactly the
  curvature-linear structures, so it is covered by the sigma bookkeeping anyway);
  (iii) adding higher-derivative terms (changes the Laplace-type class the record
  assumes). H1 is derivation-first: it produces an explicit number AND the iff-reduction.
- **Background family = conformal point-normal family.** Rejected Riemann-normal and
  product families: the conformal family already delivers 10 independent curvature
  components at a Gamma-normal point with the cheapest exact polynomial algebra (constant
  `dg`, terminating geometric series for `g^{-1}`); scalar-ness of `tr E / R` then makes
  the value family-independent once `EH_SCALAR_OK = 0` is verified.
- **Convention tier = TOTAL fibre trace** everywhere (dispatch convention trap): script 1
  pins the bookkeeping identity, script 2 computes the total trace of the 10x10 fibre
  matrix, script 3 consumes the record algebra; `E_TT_TRACE_over_R` is reported separately
  and never mixed with `e_h`.
- **Payload EOL:** `payload-P1.txt` carries the paragraph plus trailing CRLF CRLF so the
  canonical `replace(anchor, payload + anchor)` splice costs exactly `len(payload)` bytes
  and keeps the blank-line join between paragraphs (memory rules splice-post-accounting,
  payload-compile-cert); the generator asserts `POST = PRE + len(payload)`.
- **Anchor = `\paragraph{Alternate-scope weighted sector data`** (count 1 in live bytes)
  rather than the fallback `\paragraph{The assumed group ` (also count 1): P1 must sit
  directly above the paragraph it consumes and below all text it references as "above".
- **Ghost linearization formula at x=0:** used the exact point formula (valid since
  `Gamma(gbar)|_0 = 0`) instead of a generic series expansion, after the naive
  eps-series `Gamma` path was found to be wrong for the x-linear ghost perturbation;
  documented at the patch site in script 2.

## Milestone assessment

Routine: no MILESTONE.md trigger. This is a conditional derivation plus a structural
localization for one supplied input of an OPEN critical-path problem; no critical-path step
is closed and no missing link is closed without residual inputs (`sigma`, H1-theorem).

## Status-label recommendation

Derived from ch17 + appH: critical-path OPEN set unchanged (A, B, C, D1, E, F, G-derived,
N). Affected labels: NONE. Problem F stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL;
the item-123 Alternate-scope paragraph's inputs stay as recorded except that `e_h` acquires
a conditionally derived value and an explicit residual parameter. No label edit is proposed
in the payload (guards assert absence).

## Author decision needed

None. (Route, hypotheses naming, payload wording, EOL and anchor choices are routine.)

## Remaining open step

To convert the payload paragraph's hypothesis into a derivation of `e_h` for the programme:
prove (or replace) H1 from the locked action - i.e. derive from `eq:Smicro` / the quadratic
Hessian paragraph that the tensor block's zero-order curvature coupling is the harmonic
Einstein-Hilbert one (fixing the completion AND its trace sector, `sigma = 0` or otherwise);
this is the recorded gating step (appH L2039-2041: tensor-block terms beyond the displayed
action are an additional input) and it is upstream of F's closure. Independently, closing
the record's condition (iv) requires the explicit `sigma = __SIGMA__`. F remains OPEN;
a1/a2 evaluations remain conditional on `Q`, `Q_K`, `n_K`, threshold data and the operator
identification.

## Special instructions for the gatekeeper

- Do NOT run any script under `proposals/123-f-coeff-locked-block/` (author kill-order on
  `verify_ghost_op_123.py`; scripts 1-3 here are self-contained substitutes). Run only the
  commands in "Verification scripts" from the repo root with `python -I`.
- Convention: every `e_h`-type number here is the TOTAL fibre trace `tr E_ten / R_E`; the
  per-component convention of appH L2093-2114 is NOT used for it (dispatch trap; script 1
  demonstrates the `10/6 - e_h` bookkeeping under the total-trace reading).
- What must NOT be asserted from this package: that the locked action satisfies H1; that
  `sigma` has any particular value; that condition (iv) is satisfied; any `a1`/`a2`
  evaluation for the programme; any change to Problem F's status. The payload is a labelled
  conditional paragraph; its non-claim clause is load-bearing.
- Re-check first: (1) `EH_LICH` scalar-ness (`EH_SCALAR_OK`) - if the trace were
  background-dependent the lemma fails; (2) the `sigma` span (trace-fibre-vanishing
  endomorphisms factor through the fibre trace - verify against E_DECOMP and STRUCT_TR);
  (3) `GHOST_RESID_M` sign convention against eq:christoffel/eq:riemann; (4) payload
  hygiene report and POST byte accounting; (5) anchor uniqueness against the CURRENT tree
  (live bytes at draft time: appH 6839a5cab30e / 883,075 B - re-anchor if another chain
  integrated in between).
- Splices and drafts outside the payload are in this folder only (`appH-spliced-P1.tex`,
  `proposal-tail-draft.md`); nothing outside `proposals/128-f-eh-locked-tensor/` was
  touched.
