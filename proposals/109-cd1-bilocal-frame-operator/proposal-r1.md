# Proposal 109-cd1-bilocal-frame-operator, round 1

## Header

- Source-reading protocol: **digest + targeted reads**. `scratch/digest.md` was CURRENT with
  `dirty-chapters: no` at start. Files read in full for the passages relied on:
  `chapters/appH-microscopic-proofs.tex` Sec. "Problem C" (L529-695) and Sec. "Problem D"
  (L696-1587, including the closing paragraph "The locked frame as a gauge-invariant composite"
  L1585-1587); `chapters/ch17-agenda.tex` L139-163 (Problem C), L329-368 (Problem D), L647-691
  (work order, sec:ch17-order), L693-749 (sec:ch17-done); `chapters/ch04-vierbein-emergence.tex`
  L55-199 (eq:polar, eq:vev-is-frame, def:vierbein, def:composite-metric, eq:g-from-e, ass:nondeg,
  eq:llts); `chapters/ch03-matrix-action.tex` L139-164 (eq:Smatrix), L205-294 (eq:Smicro, eq:V,
  eq:VEV, ass:frame-lock, eq:Phi-transform); `chapters/ch10-lorentz-locking.tex` L120-200
  (eq:dressed-omega, thm:locking). Scout report `reports/sme-scout-20261121-faster-routes.md`
  read in full (its section 3, entries C and D1, and the section 4 ranking/trap paragraph).
  Date: 2026-11-21.
- Surviving scripts (previous pass, recovered; none overwritten): `bilocal_reps_core.py`,
  `check_reps.py` + `check_reps.out`, `check_connectors.py` + `check_connectors.out`.
  **Re-run status: both match the saved outputs exactly** (REPS_MATCH, CONN_MATCH). Note: plain
  `python -I check_reps.py` fails with `ModuleNotFoundError: bilocal_reps_core` because isolated
  mode removes the script directory from `sys.path`; the correct re-run command inserts the folder
  on `sys.path` (Reproduction pack). The saved `.out` files were produced by the non-isolated
  command in the script headers; the isolated re-run reproduces them byte-for-byte.
- New script added by this round: `check_bilocal.py` (new filename; depends only on `sympy`
  and `numpy` - no intra-folder import - so it runs with plain `python -I check_bilocal.py`).
  Final version passes with deterministic output (saved `check_bilocal.out`). Getting there
  corrected three initial claims of this draft, now fixed in place throughout: the endpoint
  invariance check is a FACTORED residual (the kernel does not form a closed loop
  `U(x,y) U(y,x)`), the right-stabilizer statement is the right `O(G0)` action (not right
  unitary, which holds instead for the `X X^H` model composite, K3b), and the plaquette
  commutator enters with the transport-convention sign `sigma = -1` for `U' = +w U` on
  columns (d-part sign checked Abelian-first).

## Result

A candidate **bilocal frame composite** is defined on the manuscript's own condensate data
(eq:Smicro fields, eq:Phi-transform law, dressed connection eq:dressed-omega):
`G_{mu nu}(x,y) = v^{-2} eta_{AC} Phi^A{}_mu(x) [U_omega(x,y)]^C{}_B Phi^B{}_nu(y)`, exactly
invariant under the internal/tangent gauge transformations eq:Phi-transform and Elitzur-safe.
Its coincidence reduction is the Repair-II composite metric eq:g-from-e of the frame
eq:vev-is-frame, and its short-distance connector is the Wilson line whose expansion is verified
in `check_connectors.py` (K1). Three results are established at the level each is claimed:

1. **(Established, CAS-checked.)** The Repair-I obstruction recorded in Sec. "Problem C"
   (sec:status-C) is a *linear* statement: `Hom_G(dOmega, V (x) V) = 0` and
   `Hom_G(dOmega, Sym^2 V) = 0` (checks H1, H2, reproducing the manuscript's decompositions D1-D4).
   At the bilinear order to which any bilocal two-point composite of locked data reduces,
   the obstruction is evaded: `Hom_G(W (x) W, V (x) V) = 42` and
   `Hom_G(W (x) W, Sym^2 V) = 22` (checks E1-E4, two independent code paths), and the group-level
   counterpart holds: the connector's linear term is eta-antisymmetric (pure gauge, no soldering;
   K1d) while an eta-symmetric soldering-type part appears at quadratic order (K1e). Moreover the
   locked-phase vacuum soldering is forced to be `c * eta` (check H10), so the composite cannot
   produce a non-Lorentzian vacuum frame, and the bilocalization itself adds no new linear
   soldering channel (check H7).
2. **(Established, CAS-checked.)** The non-degeneracy candidate: for `G = Phi Phi^H`,
   `Det G = |Det Phi|^2`, with positivity of the leading coefficient equivalent to invertibility
   (K3a), and the metric composite fixes the frame only up to a right unitary stabilizer (K3b).
   This converts ass:nondeg into the two-point statement anticipated at appH L1586, at the
   algebraic level.
3. **(New this round, CAS-checked; `check_bilocal.py`.)** The bilocal itself: the residual of
   the endpoint gauge substitution in the kernel `Psi^T eta U Phi` factors EXACTLY as
   `Psi^T (L^T eta L - eta) U Phi` (the `y`-endpoint pair `Lambda_y^{-1} Lambda_y` cancels
   between `U` and `Phi`), and the factor vanishes through `O(th^3)` at the finite
   truncated-exponential group element (K4a/K4b, exact symbols; the six `so(3,1)` generators
   are eta-antisymmetric, K4z); `U(x,x) = 1` and `G(x,x) = v^{-2} Psi^T eta Phi` (K4i); the
   connector series of `eq:bilocal-frame-op` coincides with the exact series solution of the
   transport ODE through `O(ell^2)` - the numerical gap under `e -> e/2` scales as `e^3`
   (ratio 8.0; K4c1, scaling-certified, no hand-tuned tolerance); path dependence of the
   two-point transport begins at `O(ell^2)` and its coefficient is the curvature-type
   expression `d_1 w_2 - d_2 w_1 + sigma [w_1, w_2]` of the connector - best `(sign, sigma)`
   error scaling as `e^3` (ratio 8.1) against a loop defect scaling as `e^2` (ratio 4.0;
   K4c2; observed `sigma = -1` fixes the holonomy convention for `U' = +w U` acting on
   columns); and the coincidence composite fixes the frame only up to a right `O(G0)`
   stabilizer (exact nontrivial element, K4h) - the bilocal gives the metric and a frame
   orbit, not a fixed section.
4. **(By argument; conditional.)** The route evades, without contradicting, every recorded
   obstruction on the single-site algebra: it is quadratic on the single site, so H1/H2 and the
   Leibniz-defect paragraph of Sec. "Problem D" (single-frame coefficients on the central Moyal
   branch) do not bind; the bilocal supplies the second point the linear statement lacks.

Nothing here derives the lock, selects the vacuum, produces an action for the composite, or
computes the scalar operator of Problem C. The headline claim is classified below; the D1 lock
remains explicitly un-derived (the scout-report trap - importing a polarization as an input
collapses D1 to D2 - is honored by keeping the lock a named hypothesis throughout).

## Target and status

- **Problems.** C (Sec. "Problem C: conformal mode and Cassini", sec:status-C) and
  D1 (within Sec. "Problem D: local Lorentz", sec:status-D). Both **OPEN, CRITICAL PATH,
  PROGRAMME-CONDITIONAL** (appH ledger labels re-read; ch17 sec:ch17-done items 3 and 4;
  work order sec:ch17-order item 1 D1 then item 2 C).
- **Discrepancy flagged (not silently resolved).** The dispatch described Problem C as
  "constructed vierbein/frame". The manuscript's Problem C is titled "conformal mode and
  Cassini" and its Missing step demands the gauge-fixed quadratic scalar operator; however its
  Missing-step item (i) *is* "A frame" (appH L693), and D1 closure requires "the locked frame
  exist and be non-degenerate on the claimed domain, derived from the same microscopic data"
  (ch17 L339-342, L715-720). This package targets exactly that shared missing input - a
  candidate *constructed* frame composite - which serves item (i) of C and the frame half of D1.
  It does not touch the other C inputs ((ii) G_eff, (iii) the massless constraint structure) or
  the D1 connection-dynamics half.
- **Classification of the package:** PROGRAMME-CONDITIONAL throughout; DERIVED nothing. No
  status/priority/completion label is proposed for change anywhere.

## Source reading

digest + targeted reads (digest CURRENT, `dirty-chapters: no`). No unreadable files. Full scan
not required and not performed: the proposal **adds** one new conditional paragraph to appH and
changes no existing definition, assumption, scope statement, or status passage (the existing
paragraph appH L1585-1587, which this paragraph complements, is quoted but not edited).
`HoKawaiSteinacker2025` verified present in `bib/namcg.bib` (L666, key already cited in appH).

## Research and reasoning

### 1. What the recorded obstruction actually says, and what it does not

Sec. "Problem C" (L548-601) proves: `dOmega` transforms in `V (x) so(3,1)`, complexified to
`(3/2,1/2) + 2(1/2,1/2) + (1/2,3/2)`, while a vierbein fluctuation transforms in
`V (x) V = (0,0)+(1,0)+(0,1)+(1,1)`; no common summand, hence **no nonzero Lorentz-equivariant
linear map** from `dOmega` to a vierbein fluctuation built from the locked invariant tensors, and
the single-vector contraction `e = dOmega . n` has rank <= 3. Check D1-D5 in `check_reps.py`
reproduce both decompositions independently (exact Weyl-integral characters plus a brute-force
Clebsch-Gordan path), and H1/H2 give the equivalent intertwiner statements
`Hom_G(W, V(x)V) = Hom_G(W, Sym^2 V) = 0`. K2a-c in `check_connectors.py` reproduce the rank
bound at the group level (`n_A e^A_mu = 0`, `det e = 0` identically, some 3x3 minor nonzero).

The logical scope: the obstruction is about **linear** maps out of the single-insertion
derivative data. It says nothing about quadratic maps on it. That is the gap the bilocal route
attacks, and it is exactly the gap the manuscript itself leaves open in two places: the ch04
remark after def:vierbein ("A corrected Repair I would need additional background tensors or an
independent coframe, which is part of Problem C") and appH L1585-1587, which already proposes,
in words, "composites that are bilocal in the base ... with parallel transporters built from the
connection of the class above relating the two points" (Ho-Kawai-Steinacker pattern, arXiv:2509.06646,
key verified in the repository bib), while recording that "the construction presupposes the
connection content that the closure of Problem D1 ... requires to be specified". This package
turns that recorded mechanism into an explicit operator and computes what its representation
content is.

### 2. The candidate bilocal frame operator (manuscript notation)

Let `Phi^I{}_A` be the condensate of Presentation B with transformation law eq:Phi-transform,
`v` the scale of eq:V/eq:VEV, `eta = diag(-1,1,1,1)` (signature (-,+,+,+)), and let
`U_omega(x,y)` be the path-ordered parallel transporter in the vector representation of
`SO(3,1)` of the dressed connection `Lambda^{-1} omega Lambda + Lambda^{-1} dLambda`
(eq:dressed-omega), with `U_omega(x,x) = 1`; `U_A(x,y)` likewise for the internal connection
`A_mu` of eq:Dmu-Phi. Define the **bilocal frame composite**

    G_{mu nu}(x,y) := v^{-2} delta_{II'} (U_A(x,y))^{I'}{}_J Phi^{I A}(x)
                     [U_omega(x,y)]_{AB} Phi^{J B'}(y) (U_omega(y,x))_{B'} ...

- the precise index placement is awkward to typeset in prose; the formula actually used, and the
  one in the LaTeX block below and in `check_bilocal.py`, is the manifestly invariant one

    G_{mu nu}(x,y) := v^{-2} eta_{AC} Phi^{A}{}_{mu}(x)
                      [U_{tot}(x,y)]^{C}{}_{B} Phi^{B}{}_{nu}(y),      (blframe)

with `U_tot` the transporter of the combined internal-plus-tangent connection (`U_A` on `I`,
`U_omega` on the tangent index), written with the tangent index of `Phi^A{}_mu` as an upper
frame index acting under `eq:llts`-type transformations, `Phi^A{}_mu -> Lambda^A{}_B Phi^B{}_mu`,
so that `eta_{AC} U^C{}_B Phi^B` contracts the transported frame index at `y` against the one at
`x`. After the locked identification `I <-> A` of eq:VEV and Chapter 10, the internal indices
`I, I'` are set equal by `delta` (equivalently: normalized trace over the locked block,
`d^{-1} delta_{IJ}`, with `d` the internal dimension - a normalization choice, no content);
the un-fixed `I` index of Repair I (the failure recorded at appH L580-582) is thereby contracted
between **two insertions**, not by a forbidden single-site contraction.
The **coframe candidate** and **composite connection candidate** are the two canonical pieces of
the short-distance expansion in `ell = y - x` (valid for `|ell| >> L_UV^{-1}` of eq:LUV-def; the
`ell -> 0` limit is an expansion in the cutoff scale, never a point-split coincidence below the
noncommutative length):

    G_{mu nu}(x, x+ell) = G0_{mu nu}(x) + ell^mu1 G_{mu nu, mu1} + (1/2) ell^mu1 ell^mu2 (...) ,

    G0_{mu nu} = v^{-2} eta_{AB} Phi^A_mu Phi^B_nu  ->  g_{mu nu} of eq:g-from-e
                 for the Repair-II frame e^A_mu = v^{-1} <Phi^A_mu> of eq:vev-is-frame;
    g_flat{mu nu} := G_{(mu nu)}(x,x) = g_{mu nu}            (soldering, coincidence);
    C_lambda := G0^{-1} . G_{[mu nu] lambda} |_{gauge-algebra projection}  -> w_lambda in
                 so(3,1) (eta-antisymmetric; K1a, K1d): the composite spin connection candidate;
    the eta-symmetric soldering-type contribution from the connector first appears at O(ell^2)
    (K1e); its closed form is not fixed by the checks of this round (only the order and the
    gauge/soldering split are used).

Checks K4z/K4b/K4a/K4i/K4c1/K4c2/K4h in `check_bilocal.py` (new this round) establish: endpoint
local-Lorentz invariance at finite group elements through O(th^3) - the substitution residual
factors exactly as `Psi^T (L^T eta L - eta) U Phi` and the `y`-endpoint factors cancel exactly
(K4a/K4b, exact symbols); the coincidence reduction `U(x,x) = 1`, `G(x,x) = Psi^T eta Phi`
(K4i, exact); the connector series equals the exact series solution of the transport ODE through
O(ell^2), certified by the cubic scaling of the gap under `e -> e/2` (K4c1, ratio 8.0); path
dependence of the two-point transport beginning at O(ell^2) with curvature-type coefficient
`d_1 w_2 - d_2 w_1 + sigma [w_1, w_2]` of the connector (K4c2: best `(sign, sigma)` error scales
as `e^3`, ratio 8.1, while the loop defect scales as `e^2`, ratio 4.0; observed `sigma = -1`
matches the holonomy convention of `U' = +w U` on columns, the d-part sign verified
Abelian-first) - the transport is well defined through the order used and the ambiguity that
remains is curvature-type, so a locally flat (Riemann-normal-type) frame is the natural gauge of
the operator; and an exact nontrivial right `O(G0)` element shows the composite fixes the frame
only up to the right stabilizer (K4h).

**Why built this way (manuscript structures, not ported notation).** (i) Elitzur (cited at
appH L1585, keys Elitzur1975, FradkinShenker1979 in bib) forbids the one-point `<Phi>` as a
gauge-invariant order parameter; `G` is invariant, and appH L1586 already declares this reading
("the locking ... is to be represented ... by composites that are bilocal in the base").
(ii) The two endpoints' `ell` supplies the vector index `mu` that Repair I cannot contract:
`C^infty`-coefficients of `G_{mu nu}(x,x+ell)` in `ell` are tensors at `x` by construction.
(iii) The connection used in `U_omega` is eq:dressed-omega, the manuscript's own gauge-covariant
object (Stueckelberg-dressed), so the composite is invariant under the *local* rotations whose
existence D1 must derive - and this is also the honest weakness: **the operator presupposes the
connection content**, exactly as recorded at L1586; see "Remaining open step".

### 3. Central representation-theoretic claim (evasion) and its evidence

**Claim.** The bilocal two-point composite at coincident order is quadratic in the locked
condensate data, and quadratic equivariant maps into the soldering target `Sym^2 V` (and into
`V (x) V`) are not obstructed: the no-shared-summand statement binds only `Hom_G(W, .)`.

**CAS evidence** (`check_reps.py`, all PASS, re-run matches saved output):
- Decompositions of the manuscript passage reproduced: D1-D5 (`V(x)ADJ`, `V(x)V`, `Sym^2 V`,
  `wedge^2 V`), dimensions D6-D11.
- Obstruction reproduced: H1 `Hom(W, V(x)V) = 0`, H2 `Hom(W, Sym^2 V) = 0`; refinement H3-H5
  (all of the 2-dimensional image of the full 1-jet `J1 = ADJ + V + W` into `V(x)V` lands in the
  gauge block `wedge^2 V`), H4 (zero soldering at linear order even with the full 1-jet),
  H8/H9 (no singlet in the source data), H10 `dim (Sym^2 V)^G = 1` (any locked vacuum soldering
  is `c * eta`), H11.
- Evasion at bilinear order: E1 `Hom(W(x)W, Sym^2 V) = 22 = m_(0,0) + m_(1,1)`, E2/E3
  `Hom(W(x)W, V(x)V) = 42` (character and brute-force CG agree), E4
  `Hom(Sym^2 W, Sym^2 V) = 15`, E5 six invariant bilinear structures on `W` (the number of
  independent `<OO>` structures), E6 (the effect is not bifundamental-specific: adjoint sources
  give 4 soldering structures too).
- Stability of the *linear* obstruction under bilocalization multiplicity: H7
  `Hom(2ADJ+3V+5W, Sym^2V) = 0` - adding more single-insertion channels never creates a linear
  soldering map; only genuine bilinearity does.
- Normalization freedom: U1-U4 (`V(x)V` multiplicity-free; trace and TT pieces of `Sym^2 V`
  rescale independently): the 22 structures include genuine scheme freedom, so the claim is
  "the sector admits 22 soldering structures", never "the theory selects one".

**Established by argument (not CAS):** that the coincidence/bilinear reduction of the operator
of section 2 lands in the `W (x) W` source sector whose multiplicities E1-E4 count (each
endpoint supplies one `dOmega`-type factor at leading fluctuation order: the frame enters through
`Phi`, whose derivative content is `dOmega` at linear order in the Stueckelberg gauge where
`sigma = 0`); that the linear term of the connector is gauge-type while soldering begins at
quadratic order, at group level (this is K1d/K1e, so it is actually CAS-checked too); and that
the obstruction of the Leibniz-defect paragraph (appH L788-807) is a single-site statement about
left-multiplication actions with central coefficients and does not bind bilinears of two
endpoints (the defect is computed per frame coefficient, not per bilocal kernel).

**Conjecture / mechanism (explicitly):** that the matrix dynamics of eq:Smatrix (or its
Presentation-B completion) selects, in the locked phase, a vacuum at which the composite `G` has
an invertible leading coefficient and small fluctuations, and that the 22 structures are reduced
by the dynamics (loops, the cubic term, the measure) to a definite linear combination whose
fluctuation sector is the one Problem C needs. No claim here is made about which combination:
the one-loop-about-commuting-matrices no-go recorded at appH L1555-1562 (vanishing quadratic
induced term about commuting backgrounds at the stated content and regulator) is compatible with
this (it concerns induced terms for the *label* modes about commuting matrices; here the bilocal
is a tree-defined composite whose expectation value is the datum), and no use is made of any
induced kinetic term.

### 4. Non-degeneracy and selection

The ass:nondeg-type property for the composite: `G0_{mu nu} = v^{-2} eta_{AB} Phi^A_mu Phi^B_nu`
is non-degenerate iff the frame matrix is invertible. K3a verifies the exact algebraic content on
the Hermitian composite model used in the manuscript's contraction (eq:Smicro is positive
definite on `Phi`, hence the K3 model is the right algebraic proxy at the locked block):
`G = Phi Phi^H` Hermitian, `Det G = |Det Phi|^2`, positive definite iff `Phi` invertible (8 exact
rational trials). Stabilizer structure - two distinct statements: K3b, the Hermitian model
composite `X X^H` is blind to right UNITARY recombination (`(XV)(XV)^H = X X^H`); K4h, the
bilocal coincidence composite `G0 = Phi^T eta Phi` is invariant under LEFT local Lorentz (the
gauge invariance of K4a/K4b), while a right recombination `Phi -> Phi C` sends
`G0 -> C^T G0 C`, so given `G0` the frame is fixed only up to the right action of `O(G0)`
(exact nontrivial element checked). So **the bilocal determines the metric and a frame orbit,
not a canonical section** - a frame-orbit (metric-plus-connection) datum. This
matches the recorded structure (the metric eq:g-from-e is tangent-rotation invariant; the frame
requires a gauge choice). Selection: H10 forces the locked vacuum value of the soldering block to
`c * eta` (no dynamically frame-generated Lorentzian anomaly at the level of symmetry); the
vacuum scale `c` and the fluctuation coefficients are dynamics, not symmetry.

Derived vs named-hypothesis vs remaining D1 burden:
- Derived here: representation content of the obstruction and its evasion (with CAS); connector
  expansion and gauge/soldering split; exact bilocal invariance and curvature/path properties;
  determinant/stabilizer algebra of the composite.
- Named hypotheses (unchanged, restated): existence of the locked phase (ass:frame-lock) - used
  as a sector condition, NOT imported as a vacuum value substituted into the operator; the
  connection content feeding `U_omega` (eq:dressed-omega is gauge-covariant by construction, but
  `omega` and `Lambda` are the D1 objects whose existence and dynamics D1 must derive); that the
  connector `w` entering the transport series is the smooth-background value of eq:dressed-omega
  in the operator's domain `|ell| >> L_UV^{-1}`.
- Remaining D1 burden (unaffected): deriving local `SO(3,1)` from the matrix algebra; the
  `omega, A_mu, B` and ghost operators and field content; frame non-degeneracy *from dynamics*;
  torsion and diagonal-connection dynamics (ch17 L337-342, L715-720). Remaining C burden: all of
  the Missing-step list except that input (i) now has a candidate operator.

### 5. Comparison with the original target

The original targets (C scalar operator; D1 derived local Lorentz plus derived frame) are not
met. What is delivered is the object the named missing inputs demand - a gauge-invariant
candidate frame/connection composite whose obstruction profile is computed and evades the
recorded Repair-I no-go - plus the explicit statement of what it still presupposes. Per the
author directive, this is a positive derivation-grade input for a named missing step
(C Missing-step (i); D1 frame half), not another no-go.

### Literature

- Ho-Kawai-Steinacker, arXiv:2509.06646 (bib key HoKawaiSteinacker2025, present in
  `bib/namcg.bib` L666 and cited in appH): bilocal-field technology about a Lorentz-invariant
  vacuum. Verified as recorded in the scout report: the vacuum/polarization is imposed there,
  which under the NAMCG criterion is D2-style; we import only the operator pattern and keep the
  lock a named hypothesis. The scout's arXiv IDs 2509.06646 for the abstract contents were not
  re-fetched this round: the specific claims used (bilocal fields; positivity of bilocals; no
  Einstein equations to an order) are the ones already recorded and cited in the integrated
  manuscript text (appH L1586, L1512, L1522, L1542) - **not independently re-verified beyond the
  manuscript's own citations**.
- Viennot arXiv:2106.01913 (Berry-connection Lorentz connection) and Gielen-Mickel
  arXiv:2312.10016 (metric-from-condensate precedent) are recorded in the scout report as cover
  citations for the route; **neither is in `bib/namcg.bib` and neither is relied on for any
  statement in this proposal** - no new bib entries are requested. Nothing was imported from
  them without derivation; they are cited in the proposal text only as precedent for the
  mechanism existing in the literature (not independently verified).

## Claim classification

- established identity/derivation: all PASS lines of `check_reps.py`, `check_connectors.py`,
  `check_bilocal.py` (exact finite computations: characters, CG, word-algebra series identity,
  determinant identities, factored endpoint-invariance residual, right-O(G0) stabilizer element);
  the order-scaling of the transport-series gap and of the plaquette curvature coefficient
  (K4c1/K4c2: numerical e-scaling ratios 8.0/8.1/4.0 - scaling evidence for the O(ell^2)
  curvature-type path dependence, with the exact word-algebra identity K1b carrying the
  symbolic content); the invariance of (blframe) under eq:Phi-transform and eq:llts (by
  construction, verified symbolically K4a/K4b); the linear-only scope of the recorded
  Repair-I obstruction.
- conditional result: coincidence reduction of (blframe) to eq:g-from-e of the Repair-II frame
  (conditional on identifying the composite's leading coefficient with the frame datum, which is
  a definition within the locked sector); that the curvature-type plaquette coefficient of
  K4c2 extends to the full curvature of eq:dressed-omega once its dynamics is derived (the
  check fixes the connector-level expression and its transport convention, nothing more);
  "evasion" of the obstruction in the sense of nonvanishing intertwiner space for
  the source sector the composite occupies.
- phenomenological input / fit: none.
- conjecture/mechanism: that eq:Smatrix dynamics selects a phase with invertible `G0` and small
  fluctuations; that the 22 soldering structures reduce to a unique dynamical combination; that
  `C_lambda` is the spin connection whose dynamics D1 must supply; extension of Elitzur/Fradkin-
  Shenker statements to the noncompact frame group (recorded as not established at appH L1585).
- unresolved step: everything in the D1 list and the rest of the C list (section 4 above); the
  normalization `d^{-1}` of the internal contraction; the operator-domain/regularization issues
  of point-split composites at `|ell| ~ L_UV^{-1}`; loop renormalization of `G`.

## Proposed changes

### File `chapters/appH-microscopic-proofs.tex` (one added paragraph; nothing else edited)

Anchor: end of the "Off-shell trace-tensor mixing" paragraph of Sec. "Problem C", immediately
before `\paragraph{Missing step.}`. Boundary sentence (occurs once; verified by search):
"The displayed microscopic action on the fixed scaffold does not specify the full coupled,
gauge-fixed tensor operator or the remaining scalar couplings." (last sentence of L689-691).
Everything before it and the entire `\paragraph{Missing step.}` paragraph stay as they are.
The new paragraph keeps all existing equations and claims. Proposed labels verified absent from
the whole tree (`eq:bilocal-frame-op`, `eq:bilocal-frame-expansion`; no duplicates found by
grep). Labels referenced and verified to exist: `eq:Smicro`, `eq:VEV`, `eq:Phi-transform`,
`eq:dressed-omega`, `eq:vev-is-frame`, `eq:g-from-e`, `eq:LUV-def`, `ass:frame-lock`,
`ass:nondeg`, `sec:status-D`, `ch:vierbein-emergence`, `HoKawaiSteinacker2025`.

```latex
\paragraph{A bilocal candidate frame composite (conditional; not closure).}
Assume a locked sector in the sense of Assumption~\ref{ass:frame-lock}, without assigning its
vacuum value, and let $\mathcal U(x,y)$ denote the path-ordered transporter from $y$ to $x$ of
the combined connection, equal to $U_A(x,y)$ on the internal index and to the vector-representation
transporter of the dressed connection~\eqref{eq:dressed-omega} on the frame index, with
$\mathcal U(x,x)=\mathbb I$. On the condensate data of Equation~\eqref{eq:Smicro}, with
$\eta=\operatorname{diag}(-1,1,1,1)$, define
\begin{equation}
  \label{eq:bilocal-frame-op}
  \mathcal G_{\mu\nu}(x,y)
  =
  \frac{1}{v^{2}}\,\eta_{AC}\,\Phi^{A}{}_{\mu}(x)\,
  \bigl[\mathcal U(x,y)\bigr]^{C}{}_{B}\,\Phi^{B}{}_{\nu}(y),
\end{equation}
with the internal indices of the two insertions contracted after the locked identification of
Equation~\eqref{eq:VEV}; by the transformation law~\eqref{eq:Phi-transform} the object is
invariant under independent internal and local frame transformations at $x$ and $y$. Its
expansion in $\ell=y-x$, valid for separations large compared with $\LUV^{-1}$, begins
\begin{equation}
  \label{eq:bilocal-frame-expansion}
  \mathcal U(x,x+\ell)
  =
  \mathbb I+\ell^{\rho}w_{\rho}
  +\tfrac{1}{2}\,\ell^{\rho}\ell^{\sigma}
   \bigl(\partial_{\sigma}w_{\rho}+w_{\rho}w_{\sigma}\bigr)
  +\mathcal O(|\ell|^{3}),
\end{equation}
the short-distance transport series of the kernel, in which $w_{\rho}$ is the connection in the
frame representation (the dressed connection~\eqref{eq:dressed-omega} in the vector
representation). Equation~\eqref{eq:bilocal-frame-expansion} is an exact identity of the
truncated series through $\mathcal O(\ell^{2})$ (word-algebra check; coincidence with the exact
series solution of the transport equation through the same order checked numerically at cubic
scaling). In the induced expansion of $\mathcal G_{\mu\nu}(x,x+\ell)$ the coincidence term is
$g^{+}_{\mu\nu}=v^{-2}\eta_{AB}\Phi^{A}{}_{\mu}\Phi^{B}{}_{\nu}$, the composite
metric~\eqref{eq:g-from-e} of the Repair~II frame~\eqref{eq:vev-is-frame}; the
$\mathcal O(\ell)$ connector contribution is of pure-gauge type, proportional to the
$\eta$-antisymmetric $w_{\rho}$; an $\eta$-symmetric (soldering-type) connector contribution
first appears at $\mathcal O(\ell^{2})$; and the dependence of the kernel on the transport path
between $x$ and $y$ first appears at $\mathcal O(\ell^{2})$ with a curvature-type coefficient
(antisymmetric derivative of $w$ plus commutator, sign fixed by the transport convention). The representation content is admissible where the linear Repair~I
prescription is obstructed (Section~\ref{sec:status-C}): the linear intertwiner spaces vanish,
$\operatorname{Hom}_{G}(\mathrm{d}\Omega,V\otimes V)=\operatorname{Hom}_{G}(\mathrm{d}\Omega,\operatorname{Sym}^{2}V)=0$,
while the bilinear ones do not,
$\dim\operatorname{Hom}_{G}(W\otimes W,\operatorname{Sym}^{2}V)=22$ and
$\dim\operatorname{Hom}_{G}(W\otimes W,V\otimes V)=42$ with $V\otimes\mathfrak{so}(3,1)$ the
source of $\mathrm{d}\Omega$, and the locked vacuum soldering is forced to a multiple of $\eta$;
these multiplicities were checked with exact $\mathfrak{so}(3,1)$ characters and independently
by Clebsch--Gordan enumeration. Non-degeneracy of $\mathcal G^{+}_{\mu\nu}$ is equivalent to
invertibility of the frame matrix, since the composite determinant is the squared frame
determinant, and the composite determines the frame only modulo the right action of the
orthogonal group of $g^{+}$, so on this reading Assumption~\ref{ass:nondeg} becomes a
non-degeneracy statement about the two-point composite. The construction is the bilocal mechanism anticipated in
Section~\ref{sec:status-D}; it presupposes the connection content that the closure of
Problem~D1 requires to be specified, does not derive the locking of
Assumption~\ref{ass:frame-lock}, and defines no action, selection rule, or fluctuation operator
for $\mathcal G$. It is a candidate constructed frame composite with derived transformation
properties under the stated hypotheses; it neither constructs the Repair~I linear map nor closes
Problem~C or Problem~D, and the frame of Equation~\eqref{eq:bilocal-frame-op} is not identified
with the emergent metric of Chapter~\ref{ch:vierbein-emergence}. Problems~B, C, D, F and~G
remain open.
```

Editorial note for the integrator (not manuscript text): equation
\eqref{eq:bilocal-frame-expansion} is the verified transport-series identity (exact word-algebra
identity K1b plus numerical cubic scaling of the gap against the exact series solution of the
transport equation, K4c1); the remainder $\mathcal O(|\ell|^{3})$ is the standard statement and
no unsupported higher-order term appears in the text (earlier drafts carried an unfounded
mixed-curvature bracket; it has been removed here). All claims in the paragraph are supported
by this proposal; the soldering statement is an order-and-split statement (K1d/K1e), not a
closed form.

### Stale passages elsewhere

None. The paragraph at `sec:status-D` L1585-1587 remains accurate and is referenced by the new
text ("anticipated in Section~\ref{sec:status-D}"). No chapter asserts anything contradicted by
the new paragraph; `def:vierbein`, its remark, and `thm:locking` are untouched.

## Verification scripts

All in `proposals/109-cd1-bilocal-frame-operator/`. Symbolic output is a check, not a proof.

1. `bilocal_reps_core.py` - exact `(j_L, j_R)` character engine for
   `so(3,1)_C = sl(2,C) + sl(2,C)` (Laurent polynomials, Weyl-integral Haar pairing, Frobenius
   `Sym^2`/`wedge^2` via Adams operation, CG tensor products). Self-test: orthonormality of
   irreducible characters, exact dimensions.
2. `check_reps.py` - decomposition/obstruction/evasion battery D1-D11, H1-H11, E1-E6, U1-U4.
   Cross-checks: character inner product vs brute-force CG (E1/E3), `V(x)V = Sym^2 V + wedge^2 V`
   (D5).
3. `check_connectors.py` - K1 Wilson-line short-distance expansion as an exact word-algebra
   identity of the truncated transport ODE; K1d/K1e gauge-vs-soldering split; K2 rank bound of
   the Repair-I contraction; K3 composite determinant and right-stabilizer tests (exact
   rationals).
4. `check_bilocal.py` (new this round; needs `sympy` and `numpy`) - the bilocal of
   Equation~\eqref{eq:bilocal-frame-op}: K4z eta-antisymmetry of the six `so(3,1)` generators;
   K4b the finite truncated-exponential group element preserves `eta` through `O(th^4)` exactly;
   K4a the endpoint substitution residual of `Psi^T eta U Phi` factors through
   `L^T eta L - eta` (y endpoint cancels exactly) and the factor vanishes through `O(th^3)`;
   K4i coincidence reduction `U(x,x) = 1`, `G(x,x) = Psi^T eta Phi`; K4c1 connector series vs
   the exact series solution of the transport ODE (numerical gap scales as `e^3` under
   `e -> e/2`, ratio window [5.5, 10.5]); K4c2 plaquette - two L-path transporters between the
   same endpoints: loop defect scales as `e^2` (window [3, 5]) while the residual against
   `1 -/+ e^2 (d1 w2 - d2 w1 + sigma [w1, w2])` scales as `e^3` (window [5.5, 10.5]) over the
   sign/sigma choice (observed sigma = -1, convention `U' = +w U` on columns, d-part sign
   verified Abelian-first); K4h an exact nontrivial right `O(G0)` element exhibits the
   right-stabilizer ambiguity (frame orbit, not section). All assertions are made by
   scaling-ratio windows - no hand-tuned tolerances.

Reproduction pack (exact commands, from the proposal folder; PowerShell-safe form first):

```
powershell: python -I -c "import sys; sys.path.insert(0,'.');exec(open('check_reps.py').read())"
  -> last line: ALL CHECKS PASS (full output must equal check_reps.out)
powershell: python -I -c "import sys; sys.path.insert(0,'.');exec(open('check_connectors.py').read())"
  -> last line: ALL CHECKS PASS (full output must equal check_connectors.out)
powershell: python -I check_bilocal.py
  -> last line: ALL CHECKS PASS (output equals check_bilocal.out; deterministic across runs)
bash:       the same three commands (check_bilocal.py needs no sys.path insert - it has no
            intra-folder import; the other two do, because `python -I` removes the script
            directory from `sys.path` and they import `bilocal_reps_core`).
```
Key invariants if diffing is inconvenient: `Hom(dOmega,V(x)V) = 0`; `Hom(W(x)W,Sym^2V) = 22`;
`Hom(W(x)W,V(x)V) = 42`; `dim(Sym^2V)^G = 1`; `K1b ... exactly through O(ell^2) = PASS`;
`K3a/K3b PASS`; `K4b ... = O(th^4) exactly PASS`; `K4c1 ... ratio 8.0 PASS`;
`K4c2 ... ratio 8.1 ... ratio 4.0 PASS`; `K4h ... right O(g)-orbit PASS`. Dependencies:
CPython 3; `sympy` and `numpy` for scripts 3-4 (plus stdlib `fractions`, `itertools`,
`random`, `functools`). Verified with the repository interpreter on 2026-11-21.

## Decisions Taken

- **Frame vs metric headline.** The deliverable leads with the bilocal *metric-soldering*
  composite (the object whose invariance, non-degeneracy and obstruction evasion are provable)
  and records the frame as a right-stabilizer orbit (K4h). Alternative rejected: asserting a
  bilocal with a free frame index whose VEV equals `e^A_mu` - such an object is gauge-covariant,
  not invariant, and its VEV is exactly the Elitzur-excluded datum appH L1585 replaces by
  bilocals; asserting it would silently import the lock and collapse D1 to D2 (scout trap).
- **Base notation.** Drafted (blframe) on the Presentation-B condensate fields with
  eq:dressed-omega, not on the first-order-class operators `(X_a, S_ab)`. Alternative rejected:
  building on the class - the class already *contains* a frame by construction (appH L1500), so
  a frame there is a class datum, not a composite; the Presentation-B bilocal is the candidate
  that could later be realized as a class composite without assuming it. Noted in-text: the
  class paragraph L1586 is where the mechanism is anticipated.
- **`python -I` re-run form.** Chose the `sys.path.insert` one-liner (byte-identical outputs)
  over rewriting the surviving scripts (instruction: do not overwrite; new files only for
  revisions). Both the isolated and the saved non-isolated commands reproduce `check_reps.out`.
- **Discrepancy on Problem C's identity** (dispatch: "constructed vierbein/frame"; manuscript:
  "conformal mode and Cassini" whose Missing-step (i) is "A frame"): treated as targeting
  Missing-step (i) and the D1 frame half; flagged rather than resolved.
- **Laundry**: kept the surviving scripts' normalization `d^{-1}`-free internal contraction,
  flagged as a choice; no new bib entries requested (only `HoKawaiSteinacker2025`, already in
  the repository bib, is cited by the drafted paragraph; Viennot/Gielen-Mickel are proposal-text
  mentions only, so the integrator adds no bib entries).

## Milestone assessment

Routine. No MILESTONE.md trigger is claimed: no critical-path step is derived, no problem closes.
If accepted and integrated, the package records a candidate constructed operator for one named
missing input (C Missing-step (i) / D1 frame half) - a conditional sub-lemma-grade input, not a
milestone.

## Status-label recommendation

Re-derived from ch17 sec:ch17-order and sec:ch17-done and the appH ledger passages (not from any
frontier record): critical path at the full-GR scope = A, B, C, D1, E, F, G-derived, N; H, I, J
optional; D1 gates C in the stated work order. **All labels unchanged.** No problem is solved,
closed, or complete; C and D stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

To close the original targets: (a) Problem C additionally requires the gauge-fixed quadratic
scalar operator on the locked vacuum *in a constructed frame* - now including a derivation that
the fluctuation sector of `eq:bilocal-frame-op` supplies the frame data of its Missing-step (i),
plus the other two inputs (G_eff of Problem F; the massless-sector constraint structure);
(b) Problem D1 additionally requires: deriving local `SO(3,1)` from the matrix algebra (the
bilinear route evades the linear single-site obstructions but supplies no gauge transformation
law from eq:Smatrix yet), specifying the `omega, A_mu, B` and ghost operators, deriving the
connection content that `\mathcal U(x,y)` presupposes, deriving the vacuum selection (the lock)
from dynamics, and deriving non-degeneracy of `G0` from dynamics rather than as a sector
condition; (c) the dynamical selection of the 22 bilinear soldering structures (which linear
combination, with which normalization) is untouched. Ranked open avenues (derivation-first):
(1) derive the transformation law of `eq:bilocal-frame-op` fluctuations against eq:Smatrix and
show the soldering block transforms as a tensor under matrix gauge conjugation (positive
derivation-grade output for D1's matrix-to-frame map); (2) compute the quadratic fluctuation
kernel of `G` about a commuting/locked background in the bilocal (End-of-Hilbert-space modes,
recorded as untreated at appH L1514) to test invertibility of `G0` dynamically for C(i);
(3) realize `\mathcal U` as a genuine path-ordered matrix Wilson line in the adjoint-kernel
representation and verify K1c's zero-curvature triviality only for flat connectors (isolating
what the connection content must supply for D1); (4) Berry/adiabatic-transport candidate for
`omega` (Viennot pattern, proposal-level mention only). Bottom of list (recorded, not proposed
next): extending the linear Hom-vanishing (H7-type) to further source multiplicity classes -
same no-go, no new data for the target.

## Special instructions for the gatekeeper

- Scope limits: verify (i) the two decomposition/evasion claims against the appH sec:status-C
  passage (D1-D4 vs manuscript display; H1/H2 vs the "no common irreducible summand" sentence);
  (ii) the invariance of (blframe) directly from eq:Phi-transform and eq:llts conventions
  (upper frame index on `Phi^A{}_mu`; metric signature (-,+,+,+); `SO(3,1)`); (iii) that the
  drafted paragraph changes no existing sentence, assumption or label; (iv) re-run all four
  scripts (Reproduction pack) including the `sys.path` form and confirm the saved-output match;
  (v) confirm `eq:bilocal-frame-op` / `eq:bilocal-frame-expansion` are new labels and that the
  anchor sentence occurs exactly once in the current tree.
- Must NOT be asserted on integration: any closure or narrowing of C or D; that the lock is
  derived or that a vacuum value of `G` is computed; that the bilocal *is* the emergent frame or
  metric of Chapter 4; that the 22/42 multiplicities are selected by the dynamics; any use of
  Viennot or Gielen-Mickel as support (not in bib, not re-verified); that Elitzur applies to the
  noncompact frame group (recorded at appH L1585 as not established).
- Known conditionalities to keep visible: the curvature-path statement is connector-level at
  O(ell^2) with transport convention sigma = -1 (`U' = +w U` on columns) and numerical
  scaling-ratio evidence; nothing beyond that order is computed; the O(ell^2) soldering block
  is claimed as order-and-split only, not in closed form; the internal-index contraction
  normalization is a choice; point-splitting below `L_UV^{-1}` is outside the operator's domain.
