# Proposal 107-a-map-chart-condensate-selection, round 1

**Date:** 2026-11-21. **Branch:** local/gpu (no git writes performed). **Target:** Problem A, edge A.map —
the semiclassical-chart / condensate selection residual stated verbatim in the integrated item-106 paragraph
of `chapters/appH-microscopic-proofs.tex`, `sec:status-A`. **One insert**, one paragraph, anchored at the
unique PIN at the end of the item-106 paragraph.

## Result

The exact selection question — *within the pullback class B2(B) of item 106, which element does the model's
Weyl / trace-quadratic symbol map select, and with what data does it act* — is answered completely, and the
answer is a bounded no-go plus an exactly located missing input:

1. **The symbol map is chart-blind (exact).** Within the constant-Θ Abelian class the datum of the Weyl symbol
   map is the constant bivector Θ plus an ordering convention, and the ordering convention is an exact gauge:
   the Weyl-ordered finite-N mode product differs from the left-ordered one by the coboundary of the quadratic
   phase e^{iΘmn/2}; the commutator coefficient is the exact −2i sin(Θσ/2) in the symplectic pairing σ
   (Moyal bracket; first differs from Poisson at order Θ³); and the structure constants depend on the mode
   labels and Θ only — no chart symbol occurs (free-symbol check). Because the commutator is central, every
   state of the fixed Heisenberg algebra induces the same constant effective bivector: **states and
   condensates of the fixed algebra cannot induce leaf (chart) dependence.**
2. **The reach of matrix selection at order Θ² is exactly 20-of-36 (exact, at checked data).** At a fixed
   closed bivector 1-jet, the solutions of the coboundary equation reachable from the model product form
   exactly the image of the embedding 2-jet: an affine 20-dimensional subspace of the 36-dimensional kernel
   freedom of item 106 (span dimension 20 verified at two rational seeds; the selection map B(40) ↦ dθ(0)(24)
   has rank 20, kernel 20). The pairing of the chart-2-jet image with the 36-dim ker(M2r) has rank 20, so
   **exactly 16 kernel directions are invisible to every order-Θ² datum of the class**; the 16 invisible basis
   vectors were verified non-vacuously to lie in ker(M2r) and to be orthogonal to the whole reachable span
   (v5, left nullspace of the 36×20 pairing matrix).
3. **Bounded no-go.** Combining (1) and (2): within hypotheses (H1)–(H3) + central commutator (below), **no
   matrix-side object — symbol map, ordering convention, trace pairing, state, or condensate of the fixed
   Heisenberg algebra — resolves the semiclassical-chart selection.** The chart-resolving input is
   out-of-class: noncentral commutator (condensate) backgrounds, or the Presentation-B vacuum correspondence.
   The residual sentence of item 106 ("...requires semiclassical-chart (embedding) data beyond the 1-jet")
   is thereby made precise: within the class the beyond-1-jet data enter only through the 20-dim 2-jet image,
   and the 16-dimensional invisible complement cannot be read by any Θ² observable of the class.
4. Sp-covariance (item 106 P8) re-verified on the current tree: the rational Sp(Θstd) transvection
   S = [[1,2,0,0],[0,1,0,0],[0,0,3,1]] (S Θ S^T = Θ) leaves the θ-jet and the selected B₂ table invariant.

This does **not** close Problem A: the chart/condensate selection remains unresolved, now with the missing
input pinned exactly (noncentral/condensate data or the Presentation-B correspondence, both unspecified in the
manuscript). No status label is touched by the insert.

## Target and status

Problem: **A (matrix-to-modular map)**, edge A.map (the chart/condensate selection residual of the item-106
matrix-selection paragraph). Current ledger text (`appH-microscopic-proofs.tex` lines 12–20, read in full):

> `\section{Problem A: matrix-to-modular map}` / `\label{sec:status-A}`
> `\paragraph{Ledger label.}`
> `Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label.`
> `Completion: PROGRAMME-CONDITIONAL. The general matrix-to-modular map remains unproved. A scope-limited
> Presentation-B model may retain Assumption~\ref{ass:dictionary} and claims no derivation from the matrix model.`

Verbatim residual (occurs exactly once, re-verified by search): "so pinning down a single correction within
the pointwise freedom requires semiclassical-chart (embedding) data beyond the 1-jet".

Chapter 17 requirement relied on (Problem A, verified by search): "A derivation must specify the Hilbert
space, Weyl map, continuum limit, and error at each order in \(\Theta\)." This package addresses the **Weyl
map** clause for the constant-Θ Abelian class at order Θ²: it identifies the map's datum and shows it carries
no chart data.

Dependencies: item 106 (integrated) supplies the pullback class B2(B), the Hochschild-delta matrix M2r
(rank 160 / ker 36 / kerᵀ 384) and the selection map; this package re-derives those quantities itself rather
than importing them (framework check PASS, 0.8 s). ch03 `def:matrix-coords-ext`, `rem:ch3-trace-quadratic`
read. **DERIVED vs PROGRAMME-CONDITIONAL:** everything claimed here is conditional-class (proved within
(H1)–(H3)+central, at the enumerated checked data); Problem A stays OPEN / PROGRAMME-CONDITIONAL, unchanged.

## Source reading

**digest + targeted reads.** Compact digest of this run used for navigation (digest current at dispatch).
Read in full: `chapters/appH-microscopic-proofs.tex` `sec:status-A` lines 12–23 and the item-106 paragraph +
`\paragraph{Missing step.}` (byte-exact re-quote below); `chapters/ch17-agenda.tex` Problem A passage;
`chapters/ch03-*` `def:matrix-coords-ext`, `rem:ch3-trace-quadratic`; `proposals/106-a-map-matrix-selection-b2/s2_matrix_selection.py`
(framework source of truth), `proposal-r2.md`, `review-r2.md`, `simulate_apply_106.py`; `reports/ledger.md`
Problem A and item-106 entries; `reports/sme-scout-20261121-0416.md`; `reports/graph/frontier.yaml` chain 4;
all round-1 artifacts of this folder. No unreadable files. Live appH triple re-verified immediately before
writing this document: **809976 / sha256-16 8fa53c956445bb49 / 3874 CRLF**, PIN count 1 — matches the
dispatch value, digest not stale.

## Research and reasoning

**Class hypotheses (what everything below is conditional on).**
(H1) constant-Θ Abelian model pair: 't Hooft torus generators U, V with U V = e^{iΘ} V U, Θ = const bivector
(THstd: Θ01 = Θ23 = 1, others 0); (H2) polynomial test data of degree ≤ 2 in the embedding coordinates,
order Θ² truncation, 4-dimensional ambient with the fixed A0 = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[0,0,0,1]] and
embedding x^I = A^I_a y^a + ½ B^I_ab y^a y^b (item-106 presentation); (H3) semiclassical-chart data enter the
pullback class only through the embedding 1-jet A and 2-jet B; plus **(C)** the commutator of the model
product is central (a scalar multiple of the identity).

**Q1 — symbol map datum and chart-blindness.**
(a) Left-ordered phase d(u,v) = e^{iΘ np} is a 2-cocycle: associativity exponents agree exactly over all 729
label triples. (b) Weyl-ordered phase c(u,v) = e^{−iΘ σ(u,v)/2}, σ(u,v) = mq − np, is also a cocycle (729
triples, 0 failures); c(u,v) − c(v,u) = −2i sin(Θσ/2) exactly (625 pairs, 0 failures) whose Taylor series is
−iΘσ + i(Θσ)³/24 + O(Θ⁵) (so the bracket is the constant-Θ Moyal bracket, first correction to Poisson at
Θ³); the ordering is an exact coboundary gauge c = d·δφ with φ(u) = e^{iΘ mn/2} (625 pairs, 0 failures);
and the structure constants are free of any symbol other than the mode labels and Θ (free-symbol check).
(c) 5×5 't Hooft numerics confirm the exact laws: Tr(W_u W_v) = N δ_{u+v,0} e^{−2iΘ mn} maxerr 9.93e-16;
Tr(B_u B_v) = N δ_{u+v,0} e^{iΘ np} maxerr 1.42e-15; |Tr| ordering-independent maxerr 0.00e+00.
**Consequence (derivation):** the commutator [ , ] = −2i sin(Θσ/2)·id is central in (H1); the effective
bivector read off from any state ρ (the state-averaged commutator) is the same constant Θ for all ρ; hence
no state or condensate of the fixed Heisenberg algebra produces leaf dependence. This is the precise sense in
which "condensate selection" is empty within (H1)+(C).

**Q2 — reach of the model product at a fixed closed 1-jet.** The selection map B(40 params) ↦ dθ(0)(24)
has rank 20 (24 − 4 closedness conditions) and kernel 20. At two rational seeds (1070, 1071) the 20 kernel
directions were pushed through the pullback data map: each leaves dθ fixed and changes the B₂ table by an
element of ker(M2r), nonzero, and the span of the resulting table differences has dimension exactly 20.
So the matrix-reachable set at a fixed closed 1-jet is an affine 20-dim image of the embedding 2-jet inside
the 36-dim kernel freedom — not all of the freedom.

**Q3 — the invisible 16 (the ker-invisible-inputs companion question).** Pair the chart-2-jet image with the
36-dim ker(M2r): R ∈ Q^{36×20}, R_ij = KER_i · diff_j (KER = kernel basis of M2r, diff = table differences of
Q2). rank R = 20 at both seeds ⇒ the orthogonal complement (kernel combinations invisible to all Θ² data) has
dimension 36 − 20 = **16**. The invisible basis is the **left** nullspace of R (coefficients c ∈ Q³⁶, cᵀ R = 0
— i.e. nullspace of Rᵀ, dimension 16), verified in v5: all 16 vectors are nonzero, lie in ker(M2r)
(M2r·v = 0 entrywise, all 544 rows) and are orthogonal to every reachable table difference. (Bug history,
recorded honestly: v4 used the right nullspace of the 36×20 rank-20 matrix — dimension 0 — so its
basis-membership and orthogonality conjuncts were vacuously true and `len(inv)==16` correctly failed; v5 fixes
the nullspace and all conjuncts now verify non-vacuously. v4's printed *values* (rank 20, invisible 16) were
correct; only its basis verification was empty.)

**Q4 — Sp-covariance re-verified** (item 106 P8): rational transvection S with S Θ S^T = Θ acts by
(A,B,Θ) ↦ (SA, SB, S Θ S^T) and leaves the θ-jet and the selected table invariant.

**Conclusion (bounded no-go).** Any matrix-side object built from the class data — the symbol map (chart-blind
by Q1), an ordering choice (a gauge by Q1b), trace pairings (Q1c, chart-blind functions of labels and Θ), a
state or condensate of the fixed algebra (central commutator, no leaf dependence) — cannot distinguish the
elements within the 106 pointwise freedom at order Θ², and cannot see the 16-dim invisible complement at all.
Hypotheses the obstruction depends on, and named relaxations: (H1) constant central Θ → **noncentral
commutator / condensate background** (the state then induces a y-dependent effective bivector, i.e. a chart
input); (H3) chart data enter only via 1/2-jet → **Presentation-B vacuum correspondence** (manuscript-unspecified);
order Θ² → higher orders could probe beyond the quadratic table (open, not attempted here); polynomial
degree ≤ 2 → non-polynomial data (open); 4-dim/Abelian → D>4 / non-Abelian (open). Per the 2026-11-20
directive the positive-aimed forks rank first: (i) construct a noncentral background model (condensate) whose
effective bivector reproduces a chosen 20-dim chart 2-jet — the natural next derivation; (ii) test whether any
Θ³-order invariant in the class pairs nontrivially with the invisible 16 (direct attack on the invisibility
clause); (iii) Presentation-B vacuum correspondence as chart datum (upstream gap: the correspondence itself is
not derived anywhere in the manuscript — transfers here as the named out-of-class input).

**Literature.** No external result was imported; no citation is used in the insert. The algebra used (group
2-cocycles, 't Hooft clock-and-shift algebra, Moyal bracket) is textbook-level and re-derived in full in the
script, so no literature verification obligation arises. The sme-scout report of 2026-11-21 was read; none of
its ranked routes addresses the symbol-map datum question, and no scout claim was relied on.

## Claim classification (rule 6)

| # | claim | classification |
|---|-------|----------------|
| 1 | M2r rank 160, ker 36, kerᵀ 384; selection map rank 20, kernel 20 | established identity (re-derived, exact) |
| 2 | Q1a/Q1b cocycle laws, exact sine commutator, Taylor to Θ³, ordering = exact coboundary gauge, structure constants chart-blind | established identity/derivation (exact; all 729/625 checks) |
| 3 | Q1c trace identities at N=5 | numerical verification (maxerr ≤ 1.5e-15) of the exact laws of #2 |
| 4 | Q2: reachable set = affine image of embedding 2-jet, span dim 20 of 36 | established at the two checked rational points, within (H1)–(H3); bounded, not general |
| 5 | Q3: pairing rank 20 ⇒ exactly 16 invisible kernel directions; 16-vector basis in ker(M2r), orthogonal to span | established at the two checked points, non-vacuous (v5); bounded |
| 6 | centrality of commutator ⇒ states/condensates of fixed algebra carry no leaf dependence | established derivation within (H1)+(C) |
| 7 | bounded no-go: no matrix-side object of the class resolves chart selection at order Θ² | bounded-no-go-with-class: (H1)–(H3) + central (C), degree ≤ 2, orders Θ², 4-dim Abelian, checked data |
| 8 | chart-resolving input = noncentral condensate backgrounds or Presentation-B vacuum correspondence | unresolved-step identification (named, manuscript-unspecified; conjecture that these suffice — not derived) |
| 9 | Q4 Sp-invariance | established at checked data (re-verification of 106 P8) |

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex` (the only manuscript file touched).
**Location:** `sec:status-A`, immediately after the item-106 matrix-selection paragraph and before
`\paragraph{Missing step.}`.
**Anchor (PIN, verified count 1 on the live tree, built programmatically in all scripts):** the end of the
item-106 paragraph

> `...do not derive the dictionary assumption and does not close Problem~A.` \r\n \r\n `\paragraph{Missing step.}`

Exact boundary quote (end of preceding paragraph, occurs once as the PIN head):
"and this paragraph does not derive the dictionary assumption and does not close Problem~A."
Following block kept unchanged: `\paragraph{Missing step.}` and its text (unmodified).
**Everything else in the file is kept.** No existing sentence is removed or altered; the paragraph adds a new
labelled observation consistent with (sharpening, not contradicting) the residual sentence of item 106.

Insert file `insert-r1.tex` (2107 B, sha256-16 7aed01d22e4a6806, one CRLF-terminated ASCII line), verbatim:

```latex
\paragraph{Chart-blindness of the constant-\(\Theta\) symbol map and the reach of matrix selection at order \(\Theta^2\).} Within the constant-\(\Theta\) Abelian class the Weyl symbol map and its finite-\(N\) Weyl-ordered realization carry no semiclassical-chart datum: the map's own datum is the constant bivector plus an ordering convention, and the ordering is a gauge. Concretely, the Weyl-ordered mode product of the finite-\(N\) torus pair differs from the left-ordered mode product by the coboundary of the quadratic mode phase \(e^{i\Theta m n/2}\), its commutator coefficient is the exact \(-2i\sin(\Theta\sigma/2)\) in the symplectic pairing \(\sigma\), equal to the constant-\(\Theta\) Moyal bracket and differing from the Poisson bracket first at order \(\Theta^3\), and its structure constants depend on the mode labels and \(\Theta\) only. Since the commutator is central, every state of the fixed Heisenberg algebra has the same constant effective bivector, so states and condensates of the fixed algebra induce no leaf dependence. Combining with the pullback selection: at a fixed closed bivector 1-jet the solutions of the coboundary equation reachable from the model product form exactly the image of the embedding 2-jet, an affine 20-dimensional subspace of the 36-dimensional kernel freedom, and the remaining 16 kernel directions are invisible to every order-\(\Theta^2\) datum of the class. Hence within the stated class no matrix-side object -- symbol map, ordering convention, trace pairing, state, or condensate -- resolves the semiclassical-chart selection; chart-resolving data must come from outside the class, namely from noncentral commutator (condensate) backgrounds or the Presentation-B vacuum correspondence. These are exact algebraic facts for polynomial test data of degree \(\le 2\) at order \(\Theta^2\) within the class stated here; they do not cover noncentral commutator backgrounds, \(D>4\) submanifold embeddings, non-Abelian configurations, or orders \(\Theta^3\) and higher, do not derive the dictionary assumption, and this paragraph does not close Problem~A.
```

No `\ref`/`\label`/`\cite` added (so no label verification needed; hygiene enforces absence). Hyphenation
"Presentation-B" matches the adjectival usage in appH. Stale passages elsewhere: **none found** — no other
text asserts or implies that the symbol map or a condensate selects the chart; the ch17 Weyl-map clause and
the 106 paragraph remain accurate as written (the 106 residual sentence is retained deliberately; the new
paragraph records what its exact content is).

## Verification scripts

All in `proposals/107-a-map-chart-condensate-selection/`; every `.out` self-records the checked script's
name/size/sha256-16. Run from the repo root with `python -I` (scripts use repo-root-relative paths).

- `s3_symbol_selection_v5.py` — **sole script authority.** Central computation (framework + Q1a/Q1b/Q1c +
  Q2/Q3 at seeds 1070/1071 + Q4). Supersedes v4/v3/v2/s3 (retained as provenance; s3/v2 have no `.out`
  because neither completed a clean full run).
- `s3_symbol_selection_v5.out` — run log: python 3.11.9; framework `rank = 160, dim ker = 36, dim kerᵀ = 384,
  0.8s`; all claim lines PASS; summary dict `{'Q1a': 'PASS', 'Q1b': 'PASS', 'Q1c': 'PASS', 'Q2map': 'PASS',
  'Q2pt1070': 'PASS', 'Q2pt1071': 'PASS', 'Q3pt1070': 'PASS', 'Q3pt1071': 'PASS', 'Q4': 'PASS', 'framework': 'PASS'}`;
  total 185.4s.
- `fix_s3_v3.py`, `fix_s3_v4.py`, `fix_s3_v5.py` — byte-surgery drivers (v2→v3→v4→v5), each asserted single
  exact byte replacements + `ast.parse` of the result (the fix v3→v4 corrected a wrong Taylor series order and
  a scalar×nested-list crash; v4→v5 corrected the Q3 nullspace side).
- `s3_symbol_selection_v4.out` — honest record of the run in which all printed values matched but the Q3
  basis conjunct was vacuous (right-nullspace bug; `len(inv)==16` caught it, Q3pt marked FAIL).
- `s3_symbol_selection_v3.out` — crash record (TypeError at Q1c, Taylor FAIL); provenance.
- `mk_insert_107.py` — writes `insert-r1.tex` byte-exactly (raw string + b"\r\n").
- `insert-r1.tex` — the single insertion line (see above).
- `hygiene_107.py` / `hygiene_107.out` — 21 PASS checks + `HYGIENE: PASS` (single CRLF line, ASCII, 2107 B,
  ends with period, no `\label`/`\ref{`/`\eqref`/`\cite`, no hard-coded Chapter/Section numbers, no status
  words, braces balanced, "does not close Problem~A" ×1, derive-disclaimer ×1, all macros present in appH,
  live appH 809976/8fa53c956445bb49/3874, PIN count 1).
- `simulate_apply_107.py` / `simulate_apply_107.out` — PIN-based splice simulation writing **only**
  `scratch/sim/appH_after_107.tex`; BEFORE 809976/8fa53c956445bb49/3874; predicted **POST triple:
  812085 / sha256-16 ba22f8b8fc56d094 / 3876 CRLF**; live untouched.
- `undo_check_107.out` — removing the insert from the preview reproduces the live bytes exactly (`UNDO True`).
- `manifest_107.py` / `manifest.md` — per-file size + sha256-16 for the whole folder + live appH triple
  (manifest.md generated last, after this proposal document exists).

**Reproduction pack (exact commands from repo root, expected invariants):**
```
python -I proposals/107-a-map-chart-condensate-selection/s3_symbol_selection_v5.py
  # expect within ~4 min: "M2r rank = 160, dim ker(M2r) = 36, dim ker(M2r^T) = 384";
  # Q1b "0 failures" x2 (cocycle 729, gauge 625), Taylor PASS, maxerrs 9.93e-16 / 1.42e-15 / 0.00e+00;
  # "Q2: rank(B -> dtheta(0)) = 20 ... kernel dim 20"; "span dim 20 (expect 20)" x2;
  # "pairing rank 20 ... invisible dim 16 ... True ; ... True" x2; summary dict ALL PASS (10 keys); exit 0.
python -I proposals/107-a-map-chart-condensate-selection/hygiene_107.py     # expect "HYGIENE: PASS", exit 0
python -I proposals/107-a-map-chart-condensate-selection/simulate_apply_107.py
  # expect BEFORE 809976/8fa53c956445bb49/3874; "PIN occurrences: 1";
  # AFTER(simulated) 812085/ba22f8b8fc56d094/3876; live sha unchanged; exit 0
```
Tool output is a check, not a proof; the derivations are the reasoning in the section above (each identity
verified exactly over all enumerated label pairs/triples, not sampled).

## Decisions Taken

- **v5 as sole authority, superseded versions retained.** Coordinator directive (post tool-death): no Edit
  tool; version-by-byte-surgery; superseded files kept as provenance, declared here and in the manifest.
  Rejected alternatives: deleting v2–v4 (loses honest bug history the gatekeeper should see); silently
  overwriting (breaks the .out↔script sha pairing).
- **Q3 fixed via left nullspace** (`R.T.nullspace()`), the mathematically correct object for "kernel
  combinations invisible to the reachable span" (c ∈ R³⁶, cᵀR = 0). Right nullspace is 0-dim at rank 20;
  keeping v4's vacuous PASS was rejected as misreporting.
- **Seeds 1070/1071, rational arithmetic:** two generic rational points at each stage, no floating point in
  the exact-algebra checks. One seed rejected as insufficient evidence for a "at checked data" claim.
- **Insert placed after the 106 paragraph, before `Missing step.`** (keeps the selection-evidence chain in
  reading order; the Missing-step paragraph's content is unaffected). Anchor PIN is program-built, unique.
- **"Presentation-B" adjectival hyphenation** to match appH usage; en-dash avoided (ASCII-only insert).
- **Scope wording** records class (H1)–(H3)+central and the checked-data bound in the paragraph itself —
  chosen over a longer paragraph with a formal hypothesis list, to stay within the 1500–2500 B single-line
  convention (actual 2107 B).
- **No new bibliography entries; no web claims imported.**

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step derived to closure; the package supplies a bounded
class-internal no-go + an exactly located missing input for edge A.map.

## Status-label recommendation

Derived current critical-path list from the agenda + ledger (full-GR / matrix-derived scope): A, B, C, D1, E,
F, G-derived, N — all OPEN. **Affected labels: none — all unchanged.** Problem A remains OPEN / CRITICAL PATH
for the matrix-derived label / PROGRAMME-CONDITIONAL. No status wording appears in the insert (hygiene-checked).

## Author decision needed

None.

## Remaining open step

To close the A.map residual (and any use of it toward Problem A): exhibit, **outside** class (H1)–(H3)+central,
a matrix-side construction whose data resolve the semiclassical chart — concretely either (i) a noncentral
commutator (condensate) background on the matrix side, with the derived y-dependent effective bivector shown
to select a chart 1-jet consistently with the 106 coboundary equation, or (ii) a derivation of the
Presentation-B vacuum-to-Chart-data correspondence (currently absent from the manuscript; Assumption
`ass:dictionary` untouched here). Additionally open within-class: whether any order-Θ³ invariant of the class
pairs nontrivially with the 16-dim invisible complement (not examined at any order ≥ 3 in this package), and
the same questions for D>4 submanifolds and non-Abelian configurations. Problem A's completion per ch17 still
requires the full four-clause specification (Hilbert space, Weyl map, continuum limit, error at each order in
Θ) with the dictionary assumption not retained as a premise — untouched.

## Special instructions for the gatekeeper

1. **Must NOT be asserted:** closure of Problem A or of A.map; any out-of-class statement (noncentral
   backgrounds, Θ³+, D>4, non-Abelian) as established; that the 16 invisible directions carry no data at
   *higher* order (the invisibility is proven only for Θ² data of the class at the checked points); that a
   condensate background *would* select the chart (named as the candidate out-of-class input only).
2. **Re-check especially:** Q3pt non-vacuity in v5 (the v4 `.out` is kept to show the vacuity bug and why v4
   cannot be cited for the basis claim — only v5 may be cited); Q1b "ordering is a gauge" (the coboundary
   identity c = d·δφ with φ = e^{iΘmn/2} is the whole content — verify the phase bookkeeping); the centrality
   ⇒ no-leaf-dependence step (it is a two-line argument from [ , ] ∝ id; confirm no smuggled state-selection).
3. **Scope of the evidence:** exact algebra at all 729/625 enumerated pairs/triples (not sampled), rational
   arithmetic, two seeds for the pointwise reach/invisibility claims; the insert's own limitation sentence
   enumerates the bounds — the gatekeeper should confirm the insert text matches `insert-r1.tex` bytes and
   that the limitation sentence covers every class qualifier used in the reasoning.
4. Hygiene/PIN/simulation already green; the integrator must re-anchor to the live tree (PIN built from
   bytes) and expect POST 812085 / ba22f8b8fc56d094 / 3876 CRLF, then `git diff --check`/build per convention.
5. No files outside `proposals/107-a-map-chart-condensate-selection/` were written (simulation preview lives
   in `scratch/sim/`, git-ignored scratch area, as in item 106).
