# Proposal 107-a-map-chart-condensate-selection, round 2

Round 1: ACCEPT WITH REQUIRED REVISIONS, flags none (`review-r1.md`, read in full). Round 2 carries the
gatekeeper's corrected paragraph **byte-adopted** (no retyping), retargets hygiene/simulation, applies F3–F5
document fixes, and re-records the corrected claims. No new computations were run this round; no new
mathematics is claimed beyond what review-r1 verified.

## Result

The package's headline claim is corrected as directed by F8: at a fixed closed 1-jet the reachable model
tables form the **quadratic image of the 20-dim fiber** of the embedding 2-jet (the C11 = N·N channel makes
the table map quadratic in B) — not an affine 20-plane. The true first-variation (tangent) statement is: its
first variation along the fiber spans a 20-dim subspace of the 36-dim ker(M2r) freedom, and the complementary
16 kernel directions are invisible to **every first variation** of the order-Θ² datum along the fiber
(non-vacuously verified, researcher v5 + gatekeeper gk_lean, different A0/seeds). Gatekeeper sampling at its
seed 1072 (`scratch/gk107/gk_span.py`, cited as gatekeeper-verified, not re-run here): tangent span exactly
20; diff(2v₁) = 2·diff(v₁); mixed terms of 4 sampled pairs add 3 new directions; span of 71 sampled fiber
displacements = **30 of 36** (sampling not saturated ⇒ full-image span ∈ [30, 36], complement ≤ 6 at the
sampled point, possibly 0). The bounded no-go (no matrix-side object of class (H1)–(H3)+(C) resolves the
semiclassic­al-chart selection at order Θ²) is **unaffected in quality**: chart resolution still requires
out-of-class input (noncentral/condensate backgrounds or the Presentation-B vacuum correspondence). F1: the
centrality used by the state-independence argument is the coordinate commutator [X̂^I,X̂^J] = iΘ^{IJ}𝟙 of
(H1)/(C), expectation state-independent for normalized states — the mode commutator is ∝ Ŵ_{u+v}, not ∝ id;
the adopted text re-attributes correctly. F2: sign convention now matches the integrated 058 paragraph
(e^{−iΘmn/2} gauge phase, +2i sin(Θσ/2)). F6: σ((m,n),(p,q)) = mq − np is now defined at the insert site.
Problem A remains OPEN / CRITICAL PATH for the matrix-derived label / PROGRAMME-CONDITIONAL — unchanged;
A.map not closed.

## Target and status

Unchanged from r1: Problem A edge A.map (semiclassic­al-chart/condensate selection residual of the item-106
paragraph), `sec:status-A` ledger lines 12–20 (Status: OPEN. Priority: CRITICAL PATH for the matrix-derived
label. Completion: PROGRAMME-CONDITIONAL.), re-read this round; ch17 Weyl-map clause unchanged. Everything
this package claims remains class-conditional at checked data; no closure, no label touched.

## Source reading

digest + targeted reads. Read in full this round: `review-r1.md`; `scratch/gk107/insert-corrected-gk.tex`
(byte authority, verified 2249 / d5eef9bbed7785d0 / 1 CRLF line before adoption, and content-sanity checked:
contains `D>4` (no HTML entity), both "first variation" uses, `mq-np`, `e^{-i\Theta m n/2}`,
`2i\sin`, `normalized state`, `\mathrm i`, pure ASCII); `scratch/gk107/gk_span.out` (numbers quoted above);
live appH anchor region (PIN context unchanged); all r1 artifacts and `proposal-r1.md`.

## Disposition of every finding

- **F8 (blocking)** — carried by the gatekeeper's corrected paragraph (byte-adopted as `insert-r2.tex`);
  proposal wording restated above; r1's false sentences ("affine 20-dimensional … invisible to every
  order-Θ² datum") are withdrawn from the record in this document (r1 files kept as provenance).
- **F1 (major)** — carried by adopted text (coordinate commutator, "normalized state"). My r1 mode-commutator
  sentence is corrected: [Ŵ_u,Ŵ_v] ∝ sin(Θσ/2)Ŵ_{u+v} (gatekeeper direct check), not ∝ id.
- **F2 (major)** — carried: appH 058 convention adopted.
- **F3 (minor, here)** — corrected Q4 Sp element for the record: S = [[1,2,0,0],[0,1,0,0],[0,0,1,0],
  [0,0,3,1]] (4×4, third row [0,0,1,0]), S Θ S^T = Θ at THstd; r1's 3-row print was a transcription error of
  my own; the v5 script (unchanged code) uses the correct 4×4.
- **F4/F5 (minor)** — fixed on the script authority by `retarget_r2_107b.py` →
  `s3_symbol_selection_v6.py` (21982 / 6901ae1bb6916d77): only the two header comment lines differ from v5
  (correct path `proposals/106-a-map-matrix-selection-b2/s2_matrix_selection.py`; "copied byte-for-byte" →
  "reused verbatim (shared blocks)"), asserted via line-level diff ⊆ {comment lines 16–17} and identical
  `ast.dump` — **code body unchanged, so the v5 run `.out` remains the valid evidence; v6 was NOT re-run**
  (battery unchanged; manifest states this).
- **F6 (minor, pre-existing)** — carried: σ defined in the adopted paragraph.
- **F7 (optional, not added)** — I did not add a genericity claim: the adopted text ("its first variation …
  spans a 20-dimensional subspace") is point-verified only, and no point-independent claim is needed for the
  no-go. Noted here per instruction.

## Corrected claim classification (rule 6)

| # | claim (round-2 wording) | classification |
|---|--------------------------|----------------|
| 1 | M2r 160/36/384; selection map affine, rank 20, kernel 20 | established identity (researcher v5 + gatekeeper gk_lean, independent A0/seeds) |
| 2 | cocycles; ordering = exact coboundary gauge (φ = e^{−iΘmn/2}, appH convention); commutator coefficient exact 2i sin(Θσ/2), Moyal bracket, first deviation from Poisson at Θ³; structure constants label+Θ only | established identity/derivation (exact, both A0 conventions) |
| 3 | N=5 't Hooft trace laws | numerical verification (≤1.5e-15) of exact laws |
| 4 | tangent (first-variation) reachable span exactly 20; 16-dim tangent-invisible basis, nonzero, in ker(M2r), orthogonal, direct-sum 36 | established at checked points (two A0, ≥4 seeds), bounded; NOT a genericity statement (F7) |
| 5 | full fiber image is quadratic (C11 = N·N); sampled span 30 of 36 at seed 1072, complement ≤6 (possibly 0) | gatekeeper-verified (gk_span), recorded not re-derived here |
| 6 | coordinate-commutator centrality ⇒ every normalized state of the fixed algebra has the same constant effective bivector; no state/condensate leaf dependence | established derivation within (H1)+(C) |
| 7 | bounded no-go at order Θ² within (H1)–(H3)+(C), degree ≤2, 4-dim Abelian | bounded-no-go-with-class (unaffected by F8; "cannot see the invisible 16 at all" withdrawn — replaced by: first variations cannot see them; full-image complement ≤6 at sampled point) |
| 8 | chart-resolving input out-of-class (noncentral/condensate backgrounds or Presentation-B vacuum correspondence) | unresolved-step identification (named; sufficiency not derived) |
| 9 | Q4 Sp-covariance at the correct 4×4 rational transvection | established at checked data |

## Proposed changes

Single insert, same PIN as r1 (end of item-106 paragraph before `\paragraph{Missing step.}`; PIN count 1
re-verified this round by `hygiene_107_r2.out` and `simulate_apply_107_r2.out` — "PIN occurrences: 1",
context before PIN unchanged). Candidate file `insert-r2.tex` (2249 B / sha256-16 d5eef9bbed7785d0) is
byte-identical to the gatekeeper's `scratch/gk107/insert-corrected-gk.tex`; it is not reprinted here (read it
from the file — the driver asserts byte identity, `mk_insert_107_r2.py` prints CANDIDATE MATCH). No other
manuscript passage changes; r1's stale passages statement stands (none). **POST triple is researcher-computed
this round: 812227 B / sha256-16 698f38979140770d / 3876 CRLF — not yet certified by the gatekeeper** (the
812085 / ba22f8b8fc56d094 certification applied to the withdrawn 2107 B insert).

## Verification scripts (round 2) and reproduction pack

- `retarget_r2_107.py` (3605 B / d0eb9b0294e87c58) — retarget driver (steps 1–2 OK; its step-3
  pattern missed the leading "# and", kept as provenance of the failure); `retarget_r2_107b.py` — step-3
  driver, asserts unique header match, changed lines ⊆ comments {16,17}, identical ast.dump.
- `mk_insert_107_r2.py` (1118 B) — byte-adopts the gatekeeper snippet; asserts 2249 / d5eef9bbed7785d0 /
  CRLF 1; prints `CANDIDATE MATCH` (run: printed CANDIDATE MATCH).
- `insert-r2.tex` — the candidate insertion line.
- `hygiene_107_r2.py` / `hygiene_107_r2.out` — HYGIENE: PASS 21/21; records insert-r2 2249/d5eef9bbed7785d0,
  live appH 809976/8fa53c956445bb49/3874, PIN count 1.
- `simulate_apply_107_r2.py` / `simulate_apply_107_r2.out` — PRE 809976/8fa53c956445bb49/3874;
  **POST 812227 / 698f38979140770d / 3876** (= 809976+2249+2, as predicted); preview
  `scratch/sim/appH_after_107_r2.tex` (r1 preview `appH_after_107.tex` preserved); live untouched.
- `undo_check_107_r2.out` — UNDO True (preview minus insert == live bytes).
- `s3_symbol_selection_v6.py` 21982 / 6901ae1bb6916d77 — header-only variant of the verified v5 (AST
  identical; NOT re-run — see F4/F5). All r1 scripts/outs retained; `s3_symbol_selection_v5.out` remains the
  run evidence.

Reproduction (repo root, `python -I`):
```
python -I proposals/107-a-map-chart-condensate-selection/mk_insert_107_r2.py      # CANDIDATE MATCH
python -I proposals/107-a-map-chart-condensate-selection/hygiene_107_r2.py        # HYGIENE: PASS, exit 0
python -I proposals/107-a-map-chart-condensate-selection/simulate_apply_107_r2.py
# PRE 809976/8fa53c956445bb49/3874 ; AFTER 812227/698f38979140770d/3876 ; live unchanged
```
The v5 battery (unchanged code) reproduces per the r1 pack.

## Decisions Taken

- **Byte-adoption without retyping** of the gatekeeper paragraph (source `scratch/gk107/insert-corrected-gk.tex`,
  verified 2249/d5eef9bbed7785d0 before and after copy). Rejected: retyping from the review's fenced block
  (the review block contains an HTML-escaped `&gt;` artifact; retyping risked importing it).
- **New preview filename** `appH_after_107_r2.tex` so r1's certified preview survives (routine, no status effect).
- **v6 = header-only** with AST-equality proof instead of a fresh 3-min battery run (code identical ⇒ same
  evidence); rejected: silent re-run under a new name (no new information) and in-place editing of v5
  (would orphan v5.out's checked-file pairing).
- **F7 not adopted** (no genericity wording) — point-verified claims suffice for the no-go; adopted wording
  stays within sampled evidence.
- r1 artifacts (insert-r1.tex, its outs, proposal-r1.md incl. the false sentences) kept unedited as the audit
  trail; this document is the record of withdrawal.

## Milestone assessment

Routine for this round. (The review notes the corrected package is a strong Trigger-2 (no-go) milestone
candidate once ACCEPTed — that verdict is the gatekeeper's, not claimed here.)

## Status-label recommendation

Critical-path list derived from current agenda + ledger: A, B, C, D1, E, F, G-derived, N — all OPEN.
**No label changes.** Problem A unchanged (OPEN / CRITICAL PATH for the matrix-derived label /
PROGRAMME-CONDITIONAL).

## Author decision needed

None.

## Remaining open step

To close A.map: same as r1, with the F8 sharpening — the complement to attack for any Θ²-class observable is
now the **≤6-dimensional orthogonal complement of the full quadratic fiber image** at a sampled point (not the
tangent 16); named forks ranked: (i) noncentral commutator / condensate background model with derived
y-dependent effective bivector selecting a chart 1-jet; (ii) order-Θ³+ invariants (the F8 correction applies
only to Θ² first variations and to the sampled full image); (iii) Presentation-B vacuum correspondence
(upstream: not derived in the manuscript); (iv) D>4 / non-Abelian; (v) non-polynomial data. Problem A's
full ch17 four-clause derivation untouched.

## Special instructions for the gatekeeper

1. `insert-r2.tex` must be byte-checked against `scratch/gk107/insert-corrected-gk.tex` (the driver certifies
   it; re-check independently). Do not re-flow the review's fenced copy (contains the `&gt;` artifact).
2. Re-certify the POST triple 812227 / 698f38979140770d / 3876 (researcher-computed; r1 certification void).
3. Must NOT be asserted: closure of A/ A.map; genericity of rank-20/span-20 across all closed 1-jets (F7);
   invisibility of the 16 to non-first-order data (full-image complement ≤6 at the gatekeeper's sampled
   point); sufficiency of condensate backgrounds; any out-of-class or Θ³+ claim.
4. v6: verify header-only via ast.dump yourself; v5.out is the run evidence; v6 not re-run by design.
5. Integrator must re-anchor to the live tree at integration time (PIN built from bytes).
