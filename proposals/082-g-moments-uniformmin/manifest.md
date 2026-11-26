# Manifest 082-g-moments-uniformmin (round 2, 2026-11-18; rewritten per review-r1 F3)

## Integration target (the only integrable insert)
- `insert-r2.tex` 2,029 B sha256 `9342a7be34ea588defdaf6efd465c6617f5e4d1bebe4f45e00c8f9218f37414e`
  (single content line + terminal CRLF; F1-corrected display `D^{-p}\prod_{k=0}^{p-1}(D+k)`;
  2,027 B body sha8 `2d69d745` = proposal-r2.md fence body, byte-checked PASS).
- `insert-r1.tex` 2,029 B sha8 `edec101f`...0690: SUPERSEDED FOR INTEGRATION (carries the F1
  display error), byte-frozen lineage only, never integrate.
- Anchor contract (unchanged from r1): the unique line-start `\emph{Charge-to-edge moment
  identification...` (PRE L3177); insert the paragraph plus one blank line, blank-CRLF-separated,
  immediately before the FIRST line-start `\emph{Vacuum term.}` after it (L3179; NOT L3006).

## Byte pins (round 2)
- PRE (live, re-measured read-only by `simulate_apply_082_r2.py` PRE block, no drift): appH
  729,152 B / sha256 `5d52b67252b152751709dd2f7d22ccdd29e77df131d60fd43432d7583463a303` /
  CRLF 3,828 / bareLF 0; HEAD 384dfc1 with the expected uncommitted 081.
- POST (computed in memory, no write): 731,183 B / sha256
  `956070afcd26fc1c8ffd040ca2d8bb8340467de79117bd0a10d782b6dd062c52` / CRLF 3,830 / bareLF 0 /
  insert lands line 3179. Integrator must re-pin against the live tree at apply time.
- Lineage pin (stale, do not integrate with): r1 POST 731,183 B / sha8 `192b8f9a` - correct for
  the pre-F1 insert only.

## VOID (do-not-integrate)
- VOID insert 2,026 B sha8 `ee51a36c`; VOID POST 731,180 B / sha8 `6414cbbe`;
  dead-pass partial `s1_uniform_min_certificate.py` 3,200 B / sha8 `4d3a10f7`.

## Repair lineage (reworded per F3; the r1 "verified byte-exact reverse collapse" claim is WITHDRAWN)
Checkable now: in the repaired r1 body the escape sites are the unique backslashes at offsets
1404 (`\rfloor}`), 1412 (`\binom`), 1682 (`g\mapsto\rho_{p}(g)`); under the documented 1-byte
collapses they land at exactly the r1-manifest void coordinates 1404/1411/1680, and a collapsed
artifact has the recorded size 2,026 B. NOT checkable: the VOID bytes are nowhere on disk; no
shipped evidence reproduces sha8 `ee51a36c` byte-exactly; the gatekeeper's independent
reconstruction (125 single-site replacement variants x 3 tail conventions, none matching) is
2,026 B with sha8 `121b4c8e`. So the coordinates and size are confirmed; the bytes are not.
Manuscript safety is independent of this: the shipped insert-r2 body is byte-checked equal to the
proposal-r2.md fence and its mathematics was re-proved by the gatekeeper.

## Artifacts (name / size B / sha8)
- Integrable: `insert-r2.tex` 2029 `9342a7be`. Proposal statement: `proposal-r2.md` 26,157 `ed8a1573`.
- Round-2 read-only checks: `simulate_apply_082_r2.py` 3,412 `861dfd2d` + `simulate_apply_082_r2.out`
  193 `9aaa7028`; `post_pin_full_r2.py` 1,339 `85461f22` + `post_pin_full_r2.out` 153 `cc61dd93`;
  `check_r2_consistency.py` 1,022 `39a36f28` + `check_r2_consistency.out` 79 `682dc8cf`;
  `verify_gen_lineage_r2.py` 997 `94a819c3` (prints `LINEAGE OK equal`, 3,412 B / `861dfd2d` both sides).
- Write-once generators (do not re-run; each rewrites its own pinned artifact): `make_insert_r2.py`
  1,458 `9de6289a` (-> `insert-r2.tex`); `gen_simulate_r2.py` 1,879 `8ba2f793` (->
  `simulate_apply_082_r2.py`; lineage re-proved without running it); `build_proposal_r2_v2.py` 2,251
  `be0529a7` (-> `proposal-r2.md`); fragments as built: `_p1.md` 1,453 `66b87744`, `_p2.md` 1,083
  `61772663`, `_q3.md` 3,406 `4f35c936`, `_p4.md` 3,060 `54746797`, `_p5.md` 963 `895cad61`,
  `_p6.md` 492 `e1634147`.
- Round-1 evidence (kept, lineage; not for integration): `proposal-r1.md` 19,059 `17873b95`;
  `review-r1.md` 16,772 `922240fe`; `insert-r1.tex` 2,029 `edec101f`; `simulate_apply_082.py` 3,385
  `3d5e1c62` + `.out` 193 `3be44bbd`; `s1_uniform_min_certificate_v2.py` 6,543 `ee684915` + `.out`
  539 `09866383` (not re-run in r2; byte-reproduced by the gatekeeper).
- Superseded dead-pass WIP (lineage; never run): `build_proposal_r2.py` 1,899 `0d96f33e` (assertion
  on L26 inverted; fence written at wrong offset L38; drops the final r1 line L46; died before
  producing `proposal-r2.md`); `_p3.md` 2,500 `aed2213e` (contains the forbidden pre-F1 literal
  `(D+k)` display string; superseded by `_q3.md`); `_p*` fragments above that were superseded: none
  other. `__pycache__/` directory: interpreter cache created by the `verify_gen_lineage_r2.py`
  import of `gen_simulate_r2`; incidental cache, not evidence, not run.
- `manifest.md`: this file; its own hash is printed by the round-2 final validation output.
