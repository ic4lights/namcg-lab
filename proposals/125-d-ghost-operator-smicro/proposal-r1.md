# Proposal 125-d-ghost-operator-smicro, round 1

**Type: verification-and-record package. Proposed manuscript changes: NONE (zero-byte payload, reasons in "Proposed changes").**

## Result

1. **The chain-7 death-state open result is resolved: it was BOTH a bug AND a genuine finding.**
   (Bug) The two reference vectors `KILLS[1], KILLS[2]` in the predecessor script
   `ghost_linearization_125.py` are not Killing fields of the round sphere
   ((L_{K1} g)_{\theta\theta} = 2\sin\theta\sin\phi \neq 0 by hand); with the true
   rotation fields `K0 = \partial_\phi`, `K1 = -\sin\phi\,\partial_\theta - \cos\phi\cot\theta\,\partial_\phi`,
   `K2 = \cos\phi\,\partial_\theta - \sin\phi\cot\theta\,\partial_\phi`, all three controls pass:
   L_{K}g = 0, `(\Box + \mathrm{Ric})K = 0`, and `\delta_K F = 0` (out-125b.txt, C1).
   The textbook Killing reference **stands** in the manuscript conventions.
   (Genuine finding) The first variation of the **bare** harmonic/de-Donder source
   `F^\mu[g] = g^{ab}\Gamma^\mu_{ab}[g]` along a Lie direction is **not a tensorial natural
   operator**: it contains the non-tensorial term `-(\mathcal{L}_\xi g)^{ab}\bar\Gamma^\mu_{ab}`,
   which is nonzero in flat space in non-Cartesian charts (explicit counterexample below).
   The operator `M = \Box + \mathrm{Ric}` specified for the diffeomorphism ghost in the
   integrated Problem-F paragraph (appH, "specified as the Laplace-type operator", unique) is
   the linearization of the **background-subtracted / covariantized** harmonic source
   `\tilde F^\mu[g] = g^{ab}(\Gamma^\mu_{ab}[g] - \bar\Gamma^\mu_{ab})`, and coincides with the
   bare one only where `\bar\Gamma = 0` (harmonic-type coordinates on the background — the
   fixed-scaffold regime in which the integrated text actually uses it).

2. **Verified identities** (established derivations, re-derived here from the manuscript's
   own conventions eq:christoffel, eq:riemann, signature (-,+,+,+); `(\nabla_m,\nabla_n)v^r =
   R^r{}_{smn}v^s`; sphere `R=+2`; `\Box = g^{ab}\nabla_a\nabla_b` connection Laplacian).
   For any smooth background (\bar g, \bar\nabla) and vector field \xi, variation
   `g_t = \bar g + t\,\mathcal{L}_\xi \bar g` at fixed chart:

   (1) `d_\xi F^\mu = \bar\nabla_\nu(\mathcal{L}_\xi\bar g)^{\mu\nu}
        - \tfrac12\bar\nabla^\mu \mathrm{tr}(\mathcal{L}_\xi\bar g)
        - (\mathcal{L}_\xi\bar g)^{ab}\bar\Gamma^\mu_{ab}`
       (equivalently `= \bar g^{ab}\delta\Gamma^\mu_{ab}(\mathcal{L}_\xi\bar g) - (\mathcal{L}_\xi\bar g)^{ab}\bar\Gamma^\mu_{ab}`,
       `\delta\Gamma` the tensorial variation);
   (2) the covariant part collapses **exactly** (grad-div terms cancel):
       `\bar\nabla_\nu(\mathcal{L}_\xi\bar g)^{\mu\nu} - \tfrac12\bar\nabla^\mu\mathrm{tr}
        = (\Box\xi)^\mu + \bar R^\mu{}_\nu\xi^\nu`;
   (3) hence `d_\xi \tilde F^\mu = (\Box\xi)^\mu + \bar R^\mu{}_\nu\xi^\nu` exactly (tensorial),
       and every Killing field is in the kernel: `(\Box + \bar{\mathrm{Ric}})\xi = 0`
       (verified for all three S^2 rotations, the hyperbolic-plane rotation, and the
       Schwarzschild static and axial Killing fields);
   (4) flat counterexample to any tensorial reading of the bare source: on `\mathbb{R}^2` with
       the **flat** metric in polar coordinates and the (flat-Cartesian-constant) field
       `\xi = x\,\partial_x`, every tensorial candidate vanishes,
       `\Box\xi = \mathrm{Ric}\,\xi = \mathrm{grad\,div}\,\xi = 0` (each verified symbolically),
       yet `d_\xi F = [\,2\sin^2\phi/r,\; 2\sin(2\phi)/r^2\,] \neq 0`, while for the same
       geometric data in Cartesian coordinates `d_\xi F = 0`. So no natural tensorial
       differential operator `a\Box + b\,\mathrm{Ric} + c\,\mathrm{grad\,div} + \ldots` equals the
       bare linearization on general charts, and the bare `d_\xi F` is itself chart-dependent.

   Verification coverage: three independent symbolic routes for `d_\xi F` (t-route on
   `F^\mu = -|g|^{-1/2}\partial_\nu(|g|^{1/2}g^{\mu\nu})`, t-route on `g^{ab}\Gamma^\mu_{ab}`,
   direct tensor route) agree; the full identity `d_\xi F = \Box\xi + \bar{\mathrm{Ric}}\,\xi
   - (\mathcal{L}_\xi\bar g)^{ab}\bar\Gamma^\mu_{ab}` holds on seven background families:
   S^2 rotational, S^2 general `(u(\theta,\phi), v(\theta,\phi))`, S^2 all three Killing fields,
   H^2 (`R=-2` convention check passes), 4D Lorentzian static-spherically-symmetric family with
   **free functions** `A(r), B(r), C(r)`, for all affine vector fields:
   the map `\xi \mapsto d_\xi F - (\Box\xi + \bar{\mathrm{Ric}}\,\xi) - (\mathcal{L}_\xi\bar g)^{ab}\bar\Gamma^\mu_{ab}`
   is linear in `\xi`, so this is tested as one Poly-coefficient vanishing per vector component
   (each: all coefficients in its 4 affine constants vanish identically; the combined
   16-constant call left 7 coefficients that `simplify` could not reduce syntactically —
   journal resume6, `out-dbg-d5*.txt`), and Schwarzschild Killing fields.

3. **Consistency of the integrated Problem-F data (re-checked, not edited).** With
   `M = \Box + \mathrm{Ric}` one has `-M = (-\nabla^2 + E)`-form with `E_{gh} = -\mathrm{Ric}`,
   so `a_1 = \mathrm{tr}(R/6 - E_{gh}) = \tfrac{4}{6}R + R = \tfrac53 R` (4-dimensional fibre,
   weight `-2`, ghost contribution `-\tfrac{10}{3}`) — exactly the values recorded in the
   integrated paragraph. The identity confirmed here supplies, for the first time in the
   repository end-to-end, the geometric derivation behind the operator that paragraph
   specifies as input; review-123-r1 had flagged its linearization as
   "standard-textbook status, not independently re-derived end-to-end". That verification gap
   is closed **in this proposal folder** (no manuscript change is needed or proposed).

4. **Tier accounting for the dispatched target (F.gate-ghost).**
   Tier A (derive the kinetic diffeomorphism-ghost operator from eq:Smicro): **not achieved**,
   with the obstruction located precisely and upstream: eq:Smicro's diffeomorphism invariance
   is exhibited only for diffeomorphisms preserving g^{(0)} (live bytes appH L1241-1243), hence
   the action furnishes **no** diffeomorphism gauge symmetry from which an FP ghost could be
   derived; the live text says so ("a supplied input of the infrared sector and not a
   consequence of~\eqref{eq:Smicro}", unique occurrence, appH L1244). Geometry of the specified
   operator cannot substitute for that missing gauge principle; nothing here changes that status.
   Tier B (establish the geometric half end-to-end): **achieved** (items 1-2).
   Tier C (dependency map): recorded in "Research and reasoning" s.6 with ranked open avenues.

## Target and status

- Target: frontier edge F.gate-ghost — "derive the kinetic diffeomorphism-ghost operator from
  eq:Smicro, or establish the geometric half end-to-end (Tier B) plus dependency map (Tier C)".
- Problem D (local Lorentz), appH `\label{sec:status-D}` (L766): verbatim ledger —
  "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope
  result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B
  model; D remains OPEN and the matrix-derived criterion is unmet." Unchanged by this package.
- Problem D1 (ch17): completion requires "the quadratic operators and local-Lorentz and ghost
  operators specified and the field content stated" (ch17 L715-717; see also L338). The
  Alternate-scope paragraph (ch17 L678-686) permits specification; the Alternate-scope
  weighted-sector paragraph in appH exercises that permission for the diffeomorphism ghost.
- Classification of this package: the geometric identities are **derived** (established,
  re-derived here); **no critical-path problem is closed or advanced in status**. The result is
  a verified-geometry record plus an honest Tier-A obstruction location. DERIVED (the lemma) /
  nothing promoted (the programme items).
- Dependencies: none consumed are unresolved; the package creates no new dependency and removes
  none from the critical path (the eq:Smicro ghost gate remains open for the reason in item 4).

## Source reading

digest + targeted reads. Read in full: appH Problem-D ledger section (L765-808), the
Faddeev--Popov paragraph (L1201-1253, incl. the unique "supplied input" sentence at L1244),
the diffeomorphism-symmetry and linearised-diffeo paragraphs (L1254-1305), the integrated
Alternate-scope weighted-sector paragraph (L3220ff, live bytes, this session), ch17 Problem-D
passage (L329-361), Alternate-scope paragraph (L678-686), full-GR completion items (L703-719),
ch02 eq:christoffel / eq:riemann (unique labels), ch03 eq:Smicro and ass:aux-metric labels,
proposals/123 payload and reviews r1-r2, `reports/ledger.md` and `reports/graph/frontier.yaml`
entries for F.gate-ghost, and all prior rounds/artifacts in this folder. No manuscript
definition, assumption, scope statement or status passage is edited, so no full scan was
triggered by this package; `chapters/` was not modified (verifiable: `git status` shows no new
changes under `chapters/` attributable to this chain beyond pre-existing ones).

## Research and reasoning

1. **Death-state resolution.** Predecessor state (journal + out-ghost-linearization-part1.txt):
   first variation along `f(\theta)\partial_\phi` gives `f'' + \cot\theta f'`, matching none of
   the candidate operators, and controls `(\Box+\mathrm{Ric})\xi = 0` passed for `K0` but failed
   for `K1, K2`. Hand computation showed `K1, K2` were not Killing fields; regenerating them as
   true rotations made every control fire in the correct direction (C1 all-PASS, C1t teeth:
   a generic rotational field has `d_\xi F \neq 0`).
2. **Hand lemmas.** L1 (source variation): `\delta g^{ab} = -(\mathcal{L}_\xi g)^{ab}` at fixed
   chart and `\delta\Gamma^\mu_{ab}(h)` tensorial, giving (1). L2 (trace of `\delta\Gamma`):
   `\bar g^{ab}\delta\Gamma^\mu_{ab}(h) = \bar\nabla_\nu h^{\mu\nu} - \tfrac12\bar\nabla^\mu
   h^\alpha{}_\alpha` (standard, re-derived symbolically on all families). L3 (Lie
   specialization): with `h = \mathcal{L}_\xi\bar g`, `\nabla_\nu(\mathcal{L}_\xi g)^{\mu\nu}
   = \nabla^\mu(\mathrm{div}\,\xi) + \Box\xi^\mu + C^\mu`, `C^\mu = [\nabla_\nu, \nabla^\mu]\xi^\nu`,
   and `\mathrm{tr}(\mathcal{L}_\xi g) = 2\,\mathrm{div}\,\xi`, so the grad-div terms cancel
   exactly in (2) and the endomorphism is `C = \bar R^\mu{}_\nu\xi^\nu` with a **+** sign in the
   eq:riemann convention. The sign is not imported: it is pinned numerically by S^2 (`R=+2`),
   H^2 (`R=-2`, D4a), the free-function 4D Lorentzian family (D5) and is consistent with the
   Schwarzschild kernel check (D6, Ricci-flat).
3. **Non-tensoriality.** Item 1.4 above is a proof of the non-existence of any tensorial
   natural operator equal to the bare linearization on general charts: all tensorial candidates
   vanish on the displayed flat-family datum while the bare `d_\xi F` does not (and changes
   under chart change). The residual in the S^2 rotational family, `d_\xi F - (\Box\xi + \mathrm{Ric}\,\xi)
   = -2\cot\theta f'`, is exactly `-(\mathcal{L}_\xi g)^{ab}\Gamma^\phi_{ab}` (C0c; hand-checked).
4. **Background-subtracted source.** `\tilde F^\mu[g] = g^{ab}(\Gamma^\mu_{ab}[g]-\bar\Gamma^\mu_{ab})`
   at fixed background: the `\delta g^{ab}` term multiplies `\Gamma - \bar\Gamma`, which vanishes
   at `g = \bar g`, so `\delta_\xi\tilde F` is tensorial; by (1)-(2) it equals
   `\Box\xi + \bar{\mathrm{Ric}}\,\xi` with no chart term. On flat `\bar g = \eta` in Cartesian
   coordinates `\bar\Gamma = 0` and `\tilde F = F`: this is exactly the usage regime of the
   integrated Problem-F paragraph (fixed scaffold + named harmonic scheme + supplied ghost),
   so that text and this geometry are consistent.
5. **Relation to the integrated text (live bytes).** The Alternate-scope paragraph says
   "Scheme (named, not derived): harmonic (de Donder) gauge F^\mu=g^{ab}\Gamma^\mu_{ab}" and
   "(i) the ghost operator is specified as the Laplace-type operator
   M\xi^\mu := g^{ab}\nabla_a\nabla_b\xi^\mu + R^\mu{}_\nu\xi^\nu"; it asserts **no** identity
   between the two (review-123-r2 removed the attribution, keeping the gauge naming as scheme
   naming only). Re-checked consistency: `E_{gh} = -R^\mu{}_\nu`,
   `a_1^{\mathrm{gh}} = (4/6 + 1)R = \tfrac53 R`, weight `-2`, contribution `-\tfrac{10}{3}`.
6. **Tier C dependency map and ranked avenues (derivation-first).**
   Gate structure: `ghost operator from eq:Smicro` requires (G1) a diffeomorphism gauge
   symmetry of the action, which requires (G2) a covariant completion identifying the composite
   metric as gauge-variable-covariant (appH records both as absent: L1241-1245 and the
   Presentation-B linearised-diffeo paragraph). Given a completion, the ghost kinetic operator
   is forced to the tensorial object verified here (its symbol `g^{ab}\delta^\mu_\nu` and
   endomorphism `+\bar R^\mu{}_\nu` are now pinned, and the chart term must cancel by using the
   tensor-difference gauge source) — a **design constraint any completion candidate must
   reproduce**. Ranked avenues, positive-derivation first:
   1. (matrix-side positive data for D1's "ghost operators specified" item) Compare the
      background-gauge matrix ghost (live bytes: "the background-gauge ghost operator on End
      of the Hilbert space is \([\hat X^a,[\hat X_a,\cdot\,]]\)", appH L1624) on vector-type fluctuations in the fuzzy-sphere background with the spectrum of
      `\Box + \mathrm{Ric}` on the emergent sphere (the recorded fuzzy-sphere ad-Laplacian data
      there is scalar-type; the vector-type lift is the check). Positive outcome derives a
      named missing-step input; a mismatch would redirect the specification.
   2. (upstream G2, gating) Use the pinned operator as the verification target for candidate
      covariant completions of the quadratic structure (Problem B/D boundary): a completion
      earns the ghost only if its h–\xi mixing reproduces `\Box + \mathrm{Ric}` on the emergent
      metric with the chart term cancelled.
   3. (Problem F positive input) Evaluate the vector-ghost curvature-squared coefficient
      (connection-curvature terms of Equation~\eqref{eq:appA-a2}, appA-seeley-dewitt, label unique, on the tangent bundle) with the connection
      now pinned — explicitly left open by the integrated paragraph.
   4. (bottom, negative-class) Extending the bare-source non-tensoriality to other named gauge
      schemes: no new data for the target beyond the recorded family; record only.
7. **Defects found by guards in this chain (all fixed; guard-firing evidence retained).**
   (i) predecessor `KILLS[1,2]` non-Killing (Lie-half guard fired); (ii) `divxi` treated
   contravariant components with a covariant-divergence \Gamma-slot (fixed; C4a textbook
   cross-check + C4b teeth added); (iii) `div_grad` applied `-\\Gamma` on the raised second
   index (flat-polar tensorial-zero control C2' fired; fixed); (iv) `addl()` **concatenated**
   vectors instead of adding, so the D battery silently compared `d_\xi F` against `\Box\xi + GT`
   with the Ric term dropped — D1 S2-rot FAIL with residual `[0, +f] = +\mathrm{Ric}\,\xi`
   is the fire (retained byte-exact as `out-125c-bugtrace.txt`); `addl` fixed elementwise with a
   firing length-guard and unit control (C4c). Audit: `addl` was used only in the D battery and
   the D5 block; the C0/C1/C2' certificates do not call it and remain valid. The out-125b.txt
   timeline (C0 through C3 route agreement, then the recorded 580 s timeout inside the C3
   coefficient solve) was produced by the pre-`addl`-patch script, whose D-battery path was
   never reached; supersession bytes are pinned (`ghost_linearization_125c.py.prefix-addl-bug`,
   `ghost_linearization_125.py.dead-bytes`).
   **Honesty record:** one intermediate turn of this chain narrated artifacts ("125d/125e",
   "SUMMARY 15/15 PASS") that did not exist on disk; they are retracted (journal, resume5), are
   not cited anywhere in this proposal, and every number quoted here was re-read from a file
   that exists (manifest.md hashes).
8. **Literature.** The de-Donder-gauge linearization / Lichnerowicz-operator form and the
   Killing identity are textbook-standard. Per the no-import rule no external result is used:
   every statement above is re-derived from eq:christoffel/eq:riemann conventions and re-checked
   on the seven families; correspondingly **no BibTeX entries are proposed** and no citation is
   relied on. (What was not verified: the printed textbook statements themselves were not
   re-fetched; they are corroborative only.)

## Claim classification

- Identities (1)-(3), the grad-div cancellation, the Killing-kernel checks, the D5 affine-family
  per-component affine coefficient vanishing (linearity in \xi proved in-comment),
  the H^2/S^2 convention checks: **established identity/derivation**
  (re-derived here; three independent routes for `d_\xi F`).
- The flat polar/Cartesian counterexample and the resulting **non-existence** of a tensorial
  natural operator for the bare source: **established derivation** (explicit values).
- "The 123-specified `M` is the linearization of the covariantized harmonic source (and of the
  bare one only where `\bar\Gamma = 0`)": **established derivation** given item (1)-(3), applied
  to the live text's scheme naming.
- "`E_{gh} = -\mathrm{Ric}`, `a_1 = \tfrac53 R`, contribution `-\tfrac{10}{3}` are the
  `a_1`-data of the specified `M`": **established derivation within the named scheme** (same
  classification the integrated text gives its own items).
- "Any covariant completion must reproduce `\Box + \mathrm{Ric}` as the ghost operator":
  **conditional result** — conditional on the completion making the composite metric a gauge
  variable with the standard FP construction; the statement is a design constraint, not a
  derivation from eq:Smicro.
- "The matrix ghost `\mathrm{ad}_X\mathrm{ad}_X` reproduces `M` in a geometric background":
  **conjecture/mechanism** (avenue 1; not tested here).
- eq:Smicro \Rightarrow ghost operator: **unresolved step** (gates G1/G2 above); Tier A open.

## Proposed changes

**None.** `chapters/`, `bib/` untouched by this package; no payload file ships. Reasons:
1. No live sentence is false. The FP paragraph records the ghost as supplied input (unique
   anchor "a supplied input of the infrared sector and not a consequence", verified this
   session); the Alternate-scope paragraph "specifies" `M`, names the gauge "(named, not
   derived)", and asserts no linearization identity (review-123-r2 removed it; re-confirmed on
   live bytes). The smallest text that accurately records "geometry verified, status unchanged"
   is the zero change.
2. Inserting the verified identity into appH would attach new mathematics to a paragraph whose
   own scope sentence says it "derives no local symmetry" and would invite the reading that the
   ghost operator is now derived from the named scheme toward eq:Smicro — an overclaim of the
   eq:Smicro relation (mission rule: an assumed target inserted into a calculation is not a
   microscopic derivation).
3. Stale passages created or perpetuated by this package: none.
The theorem statement in this file plus the pinned scripts are the record; a future package
that attacks gate G1/G2 can cite them if a text change then becomes warranted.

## Verification scripts

All in this folder. Reproduction pack (run from this folder; `python -I` guards against
cwd-import hijack; expected outputs are the invariants, not timings):

| file | role |
|---|---|
| `ghost_linearization_125.py` | predecessor artifact (dead; contains KILLS/divxi/div_grad bugs) |
| `ghost_linearization_125.py.dead-bytes` | byte-pinned pre-supersession copy (same sha1 as above) |
| `ghost_linearization_125b.py` | main C-certifier: C0 three-route agreement, C0b sqrt-det identity, C0c/d Gamma-term residual, C0f wrong-sign control, C1 Killing trio, C1t teeth, C2' flat counterexample (both halves), C3 4D route agreement; then the recorded 580 s timeout inside the (abandoned, non-decisive) C3 coefficient solve; note: latent `tan`-import gap would fire at C4 (never reached) and its D-battery path contains the pre-fix `addl` (never executed) |
| `out-125b.txt` | its certificate (sha1 in manifest; ends `EXIT=124` = wrapper timeout, expected) |
| `ghost_linearization_125c.py.prefix-addl-bug` | pre-fix D-battery bytes (supersession pin) |
| `out-125c-bugtrace.txt` | the `addl` bug **firing**: D1 FAIL residual `[0, f]` = `+\mathrm{Ric}\,\xi` (counterexample tooth; do not delete) |
| `ghost_linearization_125c.py` | fixed C4 + D battery: C4a/C4b/C4c controls, D1 S2-rot, D2 S2-general, D3 S2-Killing trio, D4a H^2 `R=-2` convention, D4 H2-rot, D5 4D Lorentzian free `A,B,C` x affine fields, per-component (direct route; Poly coefficients in each component's 4 constants), D6 Schwarzschild two Killing fields; t-route skipped only on the two heavy families (agreement certified at C0a/C3/D-r2 elsewhere) |
| `out-125c.txt` | its certificate (post-fix run) |
| `dbg_c2b.py`, `out-dbg-d1.txt` | bug-localization probes (tensorial-zero isolation; per-term D1 table showing `dC = box+ricv+GT` with the pre-fix `addl` residual) |
| `kill125b.ps1` | process hygiene helper (kills stale 125b runs) |
| `journal.md` | contemporaneous research journal incl. bug log and the honesty retraction (resume5) |

Re-run commands and expected invariant outputs:
1. `python -I ghost_linearization_125c.py` (allow up to ~10 min)
   expect: `C4a/C4b/C4c PASS`; every `dF==cov+GT PASS`; D4a `R = -2`;
   four `D5 ... xi^{t,r,th,ph} affine: ... PASS` lines; final line `SUMMARY 125c: 13/13 PASS` and exit 0.
2. `timeout 400 python -I ghost_linearization_125b.py`
   expect: `C0a PASS`, `C0c dF-(box+Ric) = [0, -2*Derivative(f(x0), x0)/tan(x0)]`,
   `C1 K0/K1/K2: Killing PASS | (box+Ric)xi=0 PASS | dF=0 PASS`,
   `C2' ... PASS` with `dF polar = [2*sin(x1)**2/x0, 2*sin(2*x1)/x0**2]`,
   `C3 ... PASS`, then timeout before C4 (by design of the wrapper).
3. Negative controls that must fail-if-broken (already in-run): C1t (Killing-kernel teeth),
   C0f (wrong-sign candidate), C4b (div teeth), C4c (length guard raises), and the retained
   D1 FAIL in `out-125c-bugtrace.txt` reproducing the silent-drop signature `[0, +f]`.

## Decisions Taken

- **Resolve the dispatch's (i)/(ii) as "both", not one** — chosen because each half is
  independently evidenced (C1 all-PASS vs C0c/C2' residual), and the "both" resolution is the
  one that preserves the Killing reference (protecting the integrated text) while recording the
  non-tensoriality finding (protecting future ghost-derivation attempts from a mis-specified
  target). Rejected: "bug only" (contradicted by the nonzero chart term on flat polar) and
  "convention finding about (\Box+\mathrm{Ric})" (contradicted by true-Killing C1).
- **Abandon the C3 coefficient solve** after its 334 s route-agreement half: the full-metric
  version hung >10 min and C2' is already decisive for non-existence of a tensorial identity;
  re-running it adds no information for the target. Rejected: unbounded compute.
- **Supersession by new script (125c) rather than in-place edit of 125b**; pre-fix bytes of
  both pinned alongside their firing logs (pinned-file supersession rule). Rejected: editing
  125b in place would orphan its issued certificate.
- **Skip t-route on D2/D5 only** (route agreement independently certified at C0a 3-way, C3,
  and per-\xi inside the battery on the cheap families); the identity check itself uses the
  direct tensor route on all seven families. Rejected: 300 s-class t-route recomputation per
  family for no new information.
- **Payload = NOTHING** (vs the one-clause convention-clarification alternative): no live
  sentence is false; the clause would add unneeded mathematics to a scope-limited paragraph and
  could be read as an eq:Smicro derivation claim. Reasons in "Proposed changes".
- **Do not force Tier A**: the gate is upstream (gauge symmetry of eq:Smicro); proposing a
  background or regulator relabeling that "derives" the ghost would manufacture the overclaim
  the FP paragraph exists to prevent. The positive-aimed avenues 1-3 are recorded ranked.
- **Retraction handling**: phantom narration retracted in journal and manifest; all proposal
  numbers re-read from files on disk before submission.

## Milestone assessment

Routine (no MILESTONE.md trigger). The package closes no critical-path step and corrects no
false manuscript claim; it (a) closes the review-123-r1 verification gap ("linearization
identity ... not independently re-derived end-to-end") inside the proposal folder, (b) records
a structural fact (non-tensoriality of the bare scheme's linearization) that constrains every
future ghost-operator derivation, and (c) maps the Tier-A gate with ranked positive avenues.

## Status-label recommendation

Unchanged for every problem. Current critical-path list re-derived from ch17 L703-719 and the
appH ledger labels (8 occurrences of "Status: OPEN. Priority: CRITICAL PATH" in appH, matching
the snapshot set A, B, C, D1, E, F, G-derived, N); this package moves none of them. D stays
OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; the ghost remains "a supplied input of the
infrared sector and not a consequence of~\eqref{eq:Smicro}".

## Author decision needed

None. (No label, scope or core change is proposed; spacetime remains emergent throughout —
no route in this package touches the fundamentality of the background beyond using `\bar g` as
the standard auxiliary scaffold `ass:aux-metric`.)

## Remaining open step

Tier A ("ghost operator derived from eq:Smicro") requires, in order:
1. **G1/G2 (upstream, gating):** a covariant completion of eq:Smicro under which the composite
   metric transforms as a gauge-variable-covariant object, yielding a diffeomorphism gauge
   symmetry (the live text exhibits invariance only for `g^{(0)}`-preserving diffeomorphisms).
   No choice within this target substitutes for it.
2. Given G2: identify the FP ghost of the resulting gauge orbit with the tensorial operator
   verified here (`\Box + \bar{\mathrm{Ric}}` on the emergent metric; chart term cancels iff
   the tensor-difference source is used) and show the emergent `\bar g` entering `M` is the
   emergent metric (not the auxiliary scaffold) — the auxiliary-vs-emergent distinction is
   exactly what the target's "from eq:Smicro" demands.
3. **Matrix-side match (avenue 1):** derive `\mathrm{ad}_X\mathrm{ad}_X`-on-vector-fluctuations
   = `M`-spectrum in a geometric background, converting the present "specified" operator into
   a matrix-derived one (D1's stated sense of "specified" would already be met by the
   integrated paragraph; this step is what F.gate-ghost-Tier-A additionally requires).
This package completes none of these; it pins the unique geometric target they must hit.

## Special instructions for the gatekeeper

- Scope limits: assert only what "Claim classification" tags as established; in particular
  NEVER that the ghost operator was derived from eq:Smicro, or that this package advances D,
  D1 or F. The identity is geometry of the named scheme.
- Re-derive by hand (cheap and decisive): the S^2 rotational family — `d_\xi F^\phi = f'' + \cot\theta f'`
  (three routes agree in-script), `\Box\xi^\phi = f'' + 3\cot\theta f' - f`,
  `\mathrm{Ric}\,\xi^\phi = f`, `-(\mathcal{L}_\xi g)^{ab}\Gamma^\phi_{ab} = -2\cot\theta f'`;
  their sum reproduces `d_\xi F^\phi` and the `C0c` residual is exactly the chart term.
- Re-run: `python -I ghost_linearization_125c.py` (expect all PASS, `SUMMARY 125c: 13/13 PASS`,
  exit 0) and the `125b` pack above (expect the C-line invariants and the wrapper timeout).
- Controls-firing check: confirm each guard has a fired positive control — C1t, C0f, C4b, C4c
  in-run, plus the retained `out-125c-bugtrace.txt` D1 failure (silent-drop signature `[0, +f]`)
  proving the battery can and did catch its own wiring bug.
- D5 combined-mode history: an intermediate run (pinned `out-125c-9of10.txt`) records D5 as
  FAIL with "7 coef eqs". That is a `simplify` artifact at 16 simultaneous affine constants,
  not a counterexample: the per-component runs (`out-dbg-d5b.txt`, `out-dbg-d5c.txt`: t 6 s,
  r 37 s, th 31 s, ph 15 s, each exact 0) plus 2D Lorentz (`out-dbg-d5.txt`) settle the family,
  and the final script tests per component. If you re-derive, use the component form or any
  numeric substitution of the 16 constants - not `simplify` at 16 constants.
- Anchor uniqueness verified this session: "a supplied input of the infrared sector and not a
  consequence" (appH, 1 occurrence), "specified as the Laplace-type operator" (appH, 1),
  "\label{sec:status-D}" (1); ledger quote cross-checked against live L769-772.
- Verify this chain wrote nothing outside its folder (`git status` read-only) and that
  `manifest.md` hashes match; note the honesty retraction (journal resume5) and confirm no
  retracted number appears in the proposal text.
- Do not read "no payload" as incompleteness: the dispatch explicitly allowed payload
  "a one-clause convention clarification or NOTHING" and required reasons; see "Decisions Taken".
