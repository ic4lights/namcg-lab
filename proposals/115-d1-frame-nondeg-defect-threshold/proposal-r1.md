# Proposal 115-d1-frame-nondeg-defect-threshold, round 1

## Result

Within the stated hypothesis class — Presentation B, i.e. the microscopic action
`eq:Smicro` with the displayed matrix Mexican-hat potential `eq:V`, the Repair-II
frame identification `eq:vev-is-frame`, and classical pointwise configuration
data — three statements about the locked frame of Problem D1 are derived:

1. **Vacuum-manifold non-degeneracy (corollary of `eq:vacuum-manifold`).** The
   vacuum manifold `{Phi : Phi^dagger Phi = v^2 I}` is exactly `v·U(4)`: every
   point has all singular values `sigma_i = v`, hence `|det Phi| = v^4 ≠ 0` and
   `Phi Phi^dagger = v^2 I`. Every Repair-II frame `e = Phi/v` built on an exact
   minimum of `eq:V` therefore has `|det e| = 1`. Assumption `ass:nondeg` holds
   automatically on the vacuum manifold of the displayed potential.
2. **Sharp defect threshold.** `inf{ V(Phi) : det Phi = 0 } = lambda v^4 / 4`,
   attained exactly at singular values `(0, v, v, v)` (proof: with `sigma_1 = 0`,
   `4 V/lambda − v^4 = sum_{i>=2} (sigma_i^2 − v^2)^2`, a sum of squares).
   Contrapositive: at every point where the function `eq:V` takes value below
   `lambda v^4/4` the Repair-II frame is non-degenerate; quantitatively,
   `V <= eps < lambda v^4/4` forces `sigma_i^2 >= v^2 − sqrt(4 eps/lambda)` for
   every `i` and `|det e| >= (1 − sqrt(4 eps/lambda)/v^2)^2`. For configurations
   of `eq:Smicro`, `ass:nondeg` is therefore *implied by a pointwise upper bound
   on the potential value* — a sharper, falsifiable state/configuration
   hypothesis than the blanket non-vanishing assumption — and the condensate
   defects recorded in Chapter `ch:vierbein-emergence` are finite-cost events
   (cost at least `lambda v^4/4` in units of the function `eq:V`), not flat
   directions.
3. **Exact internal-orbit stability.** Along the internal Lorentz orbit
   `Phi = v Omega`, `Omega in SO(3,1)`: `V(v Omega) = (lambda v^4/4)
   Tr(Omega^T Omega − I)^2 = 2 lambda v^4 cosh(2t) sinh^2(t)` for a boost of
   rapidity `t`; it vanishes exactly on `SO(3)`, grows without bound along the
   boosts, and its quadratic coefficient reproduces the recorded lift
   `V^(2)(d = vB) = 2 lambda v^4` (appH L2158). So `eq:VEV` is a strict global
   minimum along the non-compact orbit `SO(3,1)/SO(3)`: the displayed potential
   energetically selects the locked orientation along the boost directions (the
   three spatial rotations remain flat, matching the recorded split).

This does **not** close D1 or discharge `ass:frame-lock` or `ass:nondeg`: the
matrix-integral selection of `eq:Smicro`/`eq:V` (Presentation A, ch03 L337-343
records this as not supplied), the realization of the pointwise bound by the
physical state or by the bilocal composite of the Elitzur paragraph
(appH L1707-1708), and quantum/finite-`N` stability remain open. The D1 frame
clause moves from "assumed" to "conditionally derived with an exactly derived
sufficient condition" on the named hypothesis class. No status, priority or
completion label is changed; Problem D remains OPEN, CRITICAL PATH,
PROGRAMME-CONDITIONAL.

## Target and status

- Problem: **D1 / Problem D frame clause** — "The locked frame and its
  non-degeneracy must also be derived rather than assumed
  (Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg})"
  (`chapters/appH-microscopic-proofs.tex` L801-802).
- Appendix H ledger (Problem D, L769-772), verbatim: "Status: OPEN. Priority:
  CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2,
  imposed local Lorentz symmetry, supports only a scope-limited
  Presentation-B model; D remains OPEN and the matrix-derived criterion is
  unmet."
- Chapter 17, verbatim (L330): "CRITICAL PATH; OPEN."; (L339-342): "D1 closure
  also requires that the locked frame exist and be non-degenerate on the claimed
  domain, derived from the same microscopic data rather than taken from
  Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg}." Done-criterion item 4
  (L715-720) and order item 1 (L653-656) are unchanged. The DERIVED definition
  (L696-701) states that a chain using `ass:frame-lock`/`ass:nondeg` "does not
  qualify" — the package below respects this.
- Gating (with src): both prior gatekeeper rounds on this target routed the next
  attack to frame existence/non-degeneracy and `omega_mu`/`A_mu` kinetic-term
  generation; Problem E's packages rank their escape #1 upstream at D/D1
  (`reports/ledger.md` L1546: "upstream D/D1 per the 2026-11-20 derivation-first
  directive (both E packages rank their escape #1 there)"). The
  vacuum/state-route escape asks for a state hypothesis implying frame
  non-degeneracy; Result 2 above is exactly such a derived sufficient condition
  (an implication only — Problem E is untouched). The `omega`/`A_mu` ghost clause
  is separately handled by the pending item 114 package; the frame clause was
  the more movable target with a positive (not negative) outcome, so it is the
  fallback-not-taken: the fallback (`omega_mu` kinetic generation) is gated, per
  appH L801-802, by the same D1 clause list but its positive output (a derived
  kinetic term) is blocked by the recorded conjugate-coordinate obstruction
  (appH L1599-1614) at tree level, whereas the frame clause yielded Results
  1-3.
- Classification of this package: **conditional sub-lemma within Presentation B
  with exactly derived sufficient conditions**; the broader D1 target
  (Presentation A selection) remains OPEN. DERIVED vs PROGRAMME-CONDITIONAL:
  nothing here is DERIVED for the full-GR criterion; it narrows what remains
  PROGRAMME-CONDITIONAL.

## Source reading

digest + targeted reads. `python scripts/make_digest.py --check` printed
`DIGEST CURRENT` (head `8b9ff3932501c116c6784c74338159ad1c03eb8b`).
`chapters/appH-microscopic-proofs.tex` sha1 `94968e3ad43c4e7696367455996869ae88857e0b`,
828029 bytes — matches baseline. Read in full: appH Problem D section (L765-1709)
and Problem E head; targeted: appH Problem F head L1963-2092, Hessian paragraph
L1985-2011, G_int paragraph L2149-2176; ch17 L329-345, L650-658, L696-701,
L713-721; ch03 L180-294 and L306-361; ch04 L85-182, L400-406; ch10 L40-124,
L140-148; item 114 proposal "Setting" and review-r2 "Scope"; item 113 review
"Scope" (the equivariance-breaking falsifiability check was consulted; it does
not bear on this package, since no equivariant class is imported here — stated
rather than forced). No unreadable files.

## Research and reasoning

Setting. `Phi` is a complex `4 x 4` matrix (mixed index `Phi^I_A`), `v > 0`,
`lambda > 0`. Equation `eq:V` defines the scalar function
`V(Phi) = (lambda/4) Tr (Phi^dagger Phi − v^2 I)^2` (ch03 L240-245). Via the
singular value decomposition `Phi = U diag(sigma) W^dagger` (valid for every
complex square matrix), `Phi^dagger Phi = W diag(sigma^2) W^dagger`, so

    V(Phi) = (lambda/4) sum_{i=1}^4 (sigma_i^2 − v^2)^2,   sigma_i >= 0.   (*)

This identity is exact algebra; it is the only input to Results 1-3.
Convention note: `eq:Smicro` (ch03 L221-228) places `−V` under an outer `Tr`
and the measure `sqrt(−g^(0))`; both are positive overall factors of the action
density, and all bounds below are stated for the *function* `eq:V` itself,
which is convention-independent.

**Lemma A (Result 1).** `V = 0` iff every term in (*) vanishes iff
`sigma_i = v` for all `i` iff `Phi^dagger Phi = v^2 I`, i.e. `Phi = v U`,
`U` unitary — the manifold recorded at `eq:vacuum-manifold` ("up to unitary
rotations"); its content that every point is invertible with `|det Phi| = v^4`
and `Phi Phi^dagger = v^2 I` follows because `Phi (Phi^dagger Phi) Phi^dagger =
v^2 Phi Phi^dagger` with `Phi = v U` invertible. Determinant of the frame: with
`eq:vev-is-frame` (`e = <Phi>/v`, ch04 L91), `|det e| = |det Phi|/v^4 = 1`.
Established identity + conditional frame reading. Novelty: grep over `chapters/`
finds `invertible` never applied to `Phi` and no statement of
`|det Phi| = v^4` on the vacuum manifold; the manifold itself is recorded, the
corollary is not.

**Lemma B (Result 2).** With `sigma_1 = 0` (`det Phi = 0` iff some `sigma_i = 0`),
(*) gives `4 V/lambda = v^4 + sum_{i>=2} (sigma_i^2 − v^2)^2 >= v^4`, equality
iff `sigma_2 = sigma_3 = sigma_4 = v`. Hence
`inf{V : det Phi = 0} = lambda v^4/4` uniquely at `(0, v, v, v)` up to
`U(4) x U(4)` and phase. Contrapositive gives pointwise non-degeneracy under
`V < lambda v^4/4`. Quantitative bound: each square in (*) is at most
`4 eps/lambda` when `V <= eps`, so `sigma_i^2 >= v^2 − sqrt(4 eps/lambda)` and
`|det Phi| = prod sigma_i >= (v^2 − sqrt(4 eps/lambda))^2`, i.e.
`|det e| >= (1 − sqrt(4 eps/lambda)/v^2)^2`. Established (elementary but
load-bearing). Novelty: `lambda v^4` occurs in the manuscript only at appH
L1166, L1353 (the `eta`-contracted mass form `lambda v^4 K(M_s)`) and L2158
(the boost quadratic value); no defect threshold, no contrapositive bound
anywhere (grep: "energy density" absent from appH; no `det`-non-vanishing bound
on potential value).

**Lemma C (Result 3).** `Phi = v Omega`, real `Omega`: (*) applies with
`Phi^dagger Phi = v^2 Omega^T Omega`, so
`V = (lambda v^4/4) Tr(Omega^T Omega − I)^2 >= 0` (Frobenius norm of a real
symmetric matrix). `det(Omega^T Omega) = (det Omega)^2 = 1`; with `s_i > 0` the
eigenvalues of `Omega^T Omega`, `Tr(Omega^T Omega − I)^2 = sum (s_i − 1)^2 = 0`
iff all `s_i = 1` iff `Omega^T Omega = I` iff `Omega` orthogonal; together with
`Omega^T eta Omega = eta` this forces `Omega in SO(3)`. For the standard boost
of rapidity `t`, `Omega^T Omega` has `01`-block `[[cosh 2t, sinh 2t],[sinh 2t,
cosh 2t]]` with eigenvalues `e^{±2t}`, so `V(v Omega) = 2 lambda v^4
cosh(2t) sinh^2(t)` (exact; sympy identity in check C1), quadratic coefficient
`2 lambda v^4`, matching the recorded `V^(2) = lambda v^2 Tr H^2 = 2 lambda v^4`
at `d = vB` (appH L2158), and `m^2 = lambda v^2` with the `eq:Smicro` kinetic
normalization. So the orbit is lifted, stable, and has no runaway; the three
`SO(3)` directions are exactly flat. Established identities; the sentence "the
displayed potential selects the locked orientation along boosts" is a
conditional statement at the classical-potential level.

**Relation to recorded material (cited, not re-derived).** The quadratic boost
lift and the three-of-six Goldstone-massive statement are recorded at appH
L2149-2176 ("For the displayed potential, three of the six broken directions of
Proposition~\ref{prop:goldstone-count} carry mass \(\lambda v^2\) ... This
dependence is recorded, not resolved.") — Lemma C reproduces its coefficient and
extends it from quadratic to exact order along the orbit. The boost-invariant
`eta`-contracted completion is a saddle with `(7,3)` kinetic signature (appH
L1151-1199); its potential has `det`-zero flat access, so Results 1-2 do NOT
transfer to it (they are conditional on `eq:V`). The Hessian paragraph (appH
L1985-2011), the boost non-invariance of `eq:V` (L1102-1120, L1461-1463) and the
`U(4)`/`so(3,1)` tension (L2013-2027) are consistent with and unrebutted by
this package. The Elitzur composite paragraph (L1707-1708) is the place where
`ass:nondeg` "becomes a non-degeneracy statement about the two-point composite":
Results 1-2 are statements about the one-point `Phi`; their transfer to the
bilocal composite is stated as open (the bound is pointwise; a composite needs
an analogous norm bound, not established).

**Comparison with the original target.** The D1 clause asks that frame existence
and non-degeneracy be derived from the same microscopic data (Presentation A).
This package derives them from the Presentation-B potential `eq:V` plus the
Repair-II map, and converts the residual content into a single sharp hypothesis:
that the state/configurations obey the pointwise bound `V < lambda v^4/4` (and
that Presentation A selects `eq:V`). It is a genuine sub-lemma plus a precise
relocation of the gap, not the clause.

Literature: no new citations; none introduced; the Elitzur and Fradkin-Shenker
references already in the paragraph at appH L1707 are not relied on. Nothing in
this package is imported from a paper without derivation.

## Claim classification

- V(Phi) = (lambda/4) sum (sigma_i^2 − v^2)^2: **established identity** (SVD).
- Lemma A (manifold = v U(4), |det Phi| = v^4, Phi Phi^dagger = v^2 I):
  **established identity**; frame corollary |det e| = 1: **conditional** on
  `eq:vev-is-frame` (the book's definition).
- Lemma B (threshold, uniqueness, contrapositive, quantitative bound):
  **established** (sum-of-squares proof).
- "defects are finite-cost events, not flat directions": **established for
  configurations of `eq:V`**; its reading for the quantum theory: **unresolved**.
- Lemma C identities and equality cases: **established**; "energetically
  selects the locked orientation": **conditional** (classical potential only).
- `m^2 = lambda v^2` for the three boost modes: **recorded conditional**
  (appH L2149-2176), reproduced (C2), not novel here.
- State realizes `V < lambda v^4/4` pointwise (or in expectation with
  concentration): **unresolved** state hypothesis (sharper replacement of
  `ass:nondeg` on the configuration route).
- Presentation A selects `eq:Smicro`/`eq:V`: **unresolved** (recorded, ch03
  L337-343).
- Transfer to the bilocal composite (Elitzur reading): **unresolved**.

## Proposed changes

**File `chapters/appH-microscopic-proofs.tex`.** One insertion: the paragraph
held in `proposals/115-d1-frame-nondeg-defect-threshold/insert-d1-frame-threshold.tex`
(the manuscript-bound text; not duplicated here per dispatch), spliced
immediately BEFORE the unique line

    \section{Problem E: signature}

(L1710; anchor occurrence count verified `1` in the live tree; verified against
appH sha1 `94968e3ad43c4e7696367455996869ae88857e0b`). All existing text is
kept; nothing is removed or reworded. The paragraph sits at the end of the
Problem D ledger section, immediately after "The locked frame as a
gauge-invariant composite." (ends L1708 "...with no change to the status of
Problem~D above.") and closes with one scoped status sentence ("Problem~D
remains OPEN and PROGRAMME-CONDITIONAL.").

`\ref` targets used by the insert and their verified live labels: `eq:V`
(ch03 L241), `eq:vacuum-manifold` (ch03 L248), `eq:VEV` (ch03 L254),
`eq:Smicro` (ch03 L221), `ass:frame-lock` (ch03 L265), `eq:vev-is-frame`
(ch04 L91), `eq:g-from-e` not used, `ass:nondeg` (ch04 L171),
`ch:vierbein-emergence` (ch04 L2), `sec:status-F` (appH L1964). No new labels
are introduced (no duplicates possible).

Stale passages elsewhere: none. ch04 L177-182 ("Vanishing of \(\det e\) is a
physical possibility---a condensate defect, a region where the frame-locking
vacuum has not formed---not a gauge artifact.") remains true and is sharpened,
not contradicted, by Result 2 (the defect now has a computed minimum cost); no
text change proposed there. ch04 L400-406 (open question interpreting a limit as
a condensate defect) likewise unchanged.

Compilation certificate for the spliced paragraph: `cert-r115p.py` (below).

## Verification scripts

Folder: `C:\Users\redgi\Projects\namcg-lab@gpu\proposals\115-d1-frame-nondeg-defect-threshold\`

1. `verify_r115.py` — reproduction command:
   `python -I verify_r115.py` (cwd = folder; numpy + sympy, seed 115, no
   network). Expected invariants: nine `PASS` lines;
   `threshold lambda v^4/4 = 0.7309713741`;
   `sqrt(4 eps/lam) = 1.028020468`; final line `ALL CHECKS PASSED (seed 115)`;
   exit code 0. A1/A2 (Lemma A), B1 symbolic sum-of-squares + B2 rank-3 minimum
   search (Lemma B, v = 1.37, lambda = 0.83), B3 quantitative bound with 24139
   retained samples and zero violations, C1/C2 symbolic boost identity and
   quadratic coefficient, C3 3000 random Lorentz orbit points (identity error
   < 1e-9, `Omega^T eta Omega − eta` < 1e-9, `V = 0` exactly on rotations),
   C4 `SO(3)` flatness. Full recorded output (`out-r115.txt`):

   ```
   PASS A1 V=0 and |det Phi|=v^4 on v*U(4)*phase  maxV=2.705e-30 max|det|dev=3.997e-15
   PASS A2 Phi^dag Phi=v^2 I => Phi Phi^dag=v^2 I  max=1.554e-15
   PASS B1 symbolic: 4V/lambda|(s1=0) - v^4 = sum (s_i^2-v^2)^2 (squares >= 0)
   PASS B2 min V over det Phi=0 >= lambda v^4/4 (= 0.730971), sampled min close  min=0.739089 th=0.730971
   PASS B3 V<=eps => sigma_i^2>=v^2-sqrt(4eps/lam) and |det e|>=(1-sqrt(4eps/lam)/v^2)^2  n=24139 viol=0 worst det e margin=4.067e-01
   PASS C1 symbolic: V(v Om(t)) = 2 lambda v^4 cosh(2t) sinh^2(t); det(Om^T Om)=1
   PASS C2 quadratic term 2 t^2 matches recorded V^(2)(d=vB)=2 lambda v^4
   PASS C3 V(v Om)=(lambda v^4/4)||Om^T Om-I||^2 >=0, zero iff pure rotation, Om^T eta Om=eta  idmax=4.66e-10 etapremax=1.07e-11 minV=8.78e-27 pureRotMaxV=8.78e-27
   PASS C4 SO(3) subgroup: V(v Om)=0 exactly (3 flat directions)  max=7.715e-27
   threshold lambda v^4/4 = 0.7309713741 ; sqrt(4 eps/lam) = 1.028020468
   ALL CHECKS PASSED (seed 115)
   ```

   B2's sampled minimum (0.739089) sits 1.1% above the exact infimum because a
   uniform draw rarely hits `sigma = (0,v,v,v)`; exactness is the B1 symbolic
   identity, the search only certifies "never below" and approximate attainment.
   Tool output is a check, not a proof; the proofs are the sum-of-squares and
   eigenvalue arguments above.
2. `insert-d1-frame-threshold.tex` byte scan (gate for the .tex payload): no
   bytes `0x00-0x08/0x0B/0x0C/0x0E-0x1F`, zero TAB, `CR == LF == CRLF` counts
   (2/2/2), no BOM, ends CRLF — recorded: `BYTE-SCAN PASS`
   (`bytes=2850 bad=0 tab=0 cr=2 lf=2 crlf=2 bom=False endsCRLF=True`).
3. `cert-r115p.py` — reproduction command: `python -I cert-r115p.py` (copies the
   working tree minus `.git`, `scratch/`, `proposals/`, `reports/` and build junk,
   includes the untracked `namcg-book7.bbl`, splices the insert before the unique
   anchor line, one `pdflatex -interaction=nonstopmode -halt-on-error
   namcg-book7.tex` pass in a temp dir outside the repo). Expected: `rc=0
   errlines=0 outw=True` then `CERT PASS`, exit 0. Recorded result: CERT PASS,
   rc=0, 0 error lines, "Output written" (see out-cert-r115p.txt). Honest log:
   the first run FAILED (`! Package pdftex.def Error: File
   figs/namcg_gr_simulation_corrected.pdf not found`) because the copy filter
   skipped all `.pdf` files including `figs/` inputs; the filter was patched to
   skip only the tracked root `namcg-book7.pdf`, and the re-run passed as
   recorded. The gatekeeper should re-run and confirm CERT PASS.

## Decisions Taken

- **Primary vs fallback.** Attacked the frame existence/non-degeneracy clause
  (both gatekeeper routes; positive output found). The fallback
  (`omega_mu`/`A_mu` kinetic generation) was checked for movability first: its
  tree-level route is blocked by the recorded conjugate-coordinate obstruction
  (appH L1599-1614) and the frame clause strictly contains the D1 missing-step
  text L801-802; the ghost-operator clause is item 114's (pending) target.
  Rejected: attacking E directly (its escape #1 is routed upstream here by the
  ledger).
- **Novelty demotion.** The three-boost-mode mass `lambda v^2` (my original
  finding (d)) is recorded at appH L2149-2176; found in the final novelty grep
  before writing. It is cited and reproduced (check C2), not claimed. The novel
  content is narrowed to: Lemma A corollary, Lemma B (threshold + contrapositive
  + quantitative bound), Lemma C exact orbit identity and equality cases.
- **Threshold stated for the scalar function `eq:V`** (not the action density),
  to avoid the outer-`Tr` factor convention of `eq:Smicro`; the insert flags
  "up to the overall positive measure and trace factors". Rejected: resolving
  the outer-Tr question (a ch03 typo-level question, out of scope for D1).
- **No potential redesign proposed.** The `eq:V`-vs-`SO(3,1)` tension (recorded
  L2149-2176, L1151-1199) could only be removed by changing the core potential;
  that is STRUCTURAL (author only) and the recorded saddle of the naive
  `eta`-completion is evidence against the obvious repair; not recommended, not
  sketched further. Emergence of spacetime is untouched throughout.
- **Landing note = one paragraph** in the Problem D ledger section before the
  Problem E section (anchor unique, verified); rejected: edits to ch03/ch04
  (their text stays true) and edits to the ch17 agenda (label-adjacent).

## Milestone assessment

Routine. No milestone trigger: Results 1-3 are a conditional sub-lemma inside
Presentation B; D1's original target (derivation from the matrix data of
Presentation A) is untouched and remains OPEN; nothing is discharged, no
assumption removed.

## Status-label recommendation

Derived from ch17 (current full-GR criterion): critical path A, B, C, D1, E, F,
G-derived, N — all OPEN. Affected labels: none. No change proposed to any
status, priority or completion label (Problem D stays OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL).

## Author decision needed

None. (A core potential change that would make the boost directions flat is a
core change and structurally disfavored by the recorded saddle no-go; out of
scope, not pursued.)

## Remaining open step

To close the D1 frame clause as originally targeted one still needs:
(1) a derivation from `eq:Smatrix` (Presentation A) that the effective potential
is `eq:V` (or has the form (*) with positive `lambda`) — recorded not supplied
(ch03 L337-343); (2) a state/phase argument that the physical locked-phase state
satisfies the pointwise bound `V < lambda v^4/4` (or its bilocal-composite
analogue of appH L1707-1708); (3) quantum/finite-`N` stability of the strict
orbit minimum of Lemma C; (4) the remaining D1 clauses (omega, `A_mu`, `B`,
ghost operator content and weights) — item 114 addresses the ghost part. Result
2 relocates, and sharply narrows, step (2): on the state route, `ass:nondeg` may
be replaced by the single quantitative hypothesis "potential value below
`lambda v^4/4`", nothing else.

## Special instructions for the gatekeeper

- Re-derive by hand: the sum-of-squares threshold (Lemma B) and the boost
  identity `V(v Omega(t)) = 2 lambda v^4 cosh 2t sinh^2 t` (Lemma C); then re-run
  `python -I verify_r115.py` (expect the recorded block, rc 0).
- Re-run `python -I cert-r115p.py` for the spliced paragraph; confirm the anchor
  line `\section{Problem E: signature}` is unique in the current tree before
  splicing (the cert asserts it) and re-verify the `\ref` label list against the
  live tree (it may have moved since sha1 `94968e3a...`).
- Scope limits to enforce on the insert: it must not be read as deriving frame
  non-degeneracy from Presentation A, as discharging `ass:frame-lock` or
  `ass:nondeg`, as forbidding defects (they are allowed, at cost
  `lambda v^4/4`+), or as claiming anything about the `eta`-contracted completion
  (Results 1-2 fail there: its potential has `det = 0` access at zero cost).
- Check the package does not duplicate appH L2149-2176: novelty is exactly the
  determinant corollary, the threshold + contrapositive + quantitative bound,
  and the exact (not quadratic) orbit identity; the quadratic boost coefficient
  is cited from L2158 and matched by check C2.
- Confirm no status/priority/completion passage is edited anywhere and that the
  insert's closing sentence keeps Problem D OPEN.
- Out-of-scope for this review: whether `eq:Smicro`'s outer `Tr` over a scalar
  is a typo (factor 4 in the action density only; the insert and all bounds are
  phrased on the function `eq:V`).
