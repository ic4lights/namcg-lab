# Round-2 report, proposal 116-d1-state-nondeg-realization

Addresses `review-r1.md` (ACCEPT WITH REQUIRED REVISIONS: one blocking finding, five
minors, one riding phrasing fix). The geometric core (Procrustes identity, sharp
two-sided estimate, `delta_*`, Markov bound + saturation) was not changed.

## What changed, byte-wise

1. **Payload `insert-d1-state-nondeg.tex`** regenerated ONLY through
   `gen_payload_116.py` (byte discipline: no hand-typed backslash text).
   - OLD (SUPERSEDED): sha1 `daa9d33f29414c0aa856af37314fe8981f2d8bc7`, 3473 bytes.
   - NEW: sha1 `d99b67be680f3b727ab16367ea283680cd2d6269`, 3782 bytes (+309 B).
   - Delta: the clause from "; consequently every configuration of finite potential
     energy" through "...with an explicit bound on the measure of the complement." is
     replaced by the gatekeeper's Corrected-snippet clause (upper-bound measure
     statement, "which is null when \(E_{\mathcal V}=0\) and cannot in general be
     improved, saturation being attained on a region where the singular values are
     \((0,v,v,v)\)"); "an identity for a set of singular values" -> "attained as an
     identity on any region where the singular values are \((0,v,v,v)\)" (Finding 6);
     the scope clause "-> almost-everywhere non-degeneracy is not the pointwise
     statement ..." -> "the small-measure exception obtained when \(E_{\mathcal V}>0\)
     is a fortiori not the pointwise statement of Assumption~\ref{ass:nondeg} and does
     not discharge it" (Finding 1 scope adjustment). Nothing else in the line changed.
   - Verbatim evidence: the corrected clause and the scope clause were extracted BY
     SUBSTRING from `review-r1.md` (not retyped) and each found present byte-for-byte
     in the new payload bytes; "almost every point" absent from the payload (count 0).
   - Control-byte scan of the NEW bytes (recorded in `out-gen-r116p.txt`, sha1
     `1f27ace4824c311035c1131093364683348364d0`, 118 B): `bytes 3782 CR 1 LF 1 CRLF 1
     loneCR 0 loneLF 0 badC0 0 tab 0 backslash+ws 0 nonascii 0 endsCRLF True` then
     `PAYLOAD SCAN OK`.
2. **`gen_payload_116.py`** -> `54b64f4c7d7b25438c35a0d31440e229a605fa5a`, 6101 B
   (single-source LINE with the corrected clause; scan asserts unchanged).
3. **`cert-r116p.py`** (Finding 5) -> `ea4eef9764ae62c5eee22a11eae9423cbae97cf7`,
   3484 B: the two reference counters are HARD ASSERTIONS
   (`assert len(undef) == 0`, `assert len(mine) == 0`) executed BEFORE the temp tree is
   removed and before `CERT PASS` is printed. Re-run fresh (two pdflatex passes,
   spliced out-of-repo copy): `out-cert-r116p.txt` re-recorded, sha1
   `bb6d6c7fbeaf80e4db145716e00ab15ecbeb7850`, 158 B: `rc1=0 rc2=0 errlines=0
   outw=True undefrefs_pass2=0`, `undefrefs-touching-package-labels=0`, `CERT PASS`.
4. **`verify_r116.py` / `out-r116.txt`** UNCHANGED (procedure condition met: grep
   showed no check text echoed the false quantifier); fresh rerun tail `PASS 29
   FAIL 0` / `ALL CHECKS DONE 116`, rc 0.
5. **`proposal-r2.md`** (50152 B, sha1 `803042498231e79dcabfd4e5651e472a2aac596c`)
   built from the `proposal-r1.md` bytes by `patch_r2.py` (each replacement asserted
   count==1): header round 2; Finding 1 echoes rewritten to the bound wording (Result
   item 3, bottom line, conversion statement, D5 claim/proof/unconditional paragraph,
   C7 row, comparison paragraph, stale-passages note, milestone note, remaining-open
   step, gatekeeper-instruction bullets); the gatekeeper's constant
   `sigma = (0,v,v,v)` exact-`eq:Phi-eom` counterexample adopted into the
   honest-limitations record (D5 "Optimality / honest limit" paragraph and Result item
   3) - it proves the bound is optimal and the state-construction reduction
   `E_mu[V] <= f lambda v^4/4 => mu{det e = 0} <= f`; Finding 2 two-line `d > v`
   exclusion inserted in D3a; Finding 3 non-verbatim quote replaced by the live appH
   wording; Finding 4 pointers -> live L57-59 and L698-701; all r1 pins updated; the
   quoted payload block swapped to the new bytes; appended "Response to review-r1
   (round 2)" and "Decisions Taken (round 2)".
   Post-patch grep: "almost every" x1 and "a.e." x6 remain in proposal-r2.md, each
   inspected: the only "almost every" instance is the review-response sentence stating
   the string is ABSENT from the payload; the "a.e." instances are (i) the correct
   `mu_E`-a.e.-history Markov statement for the Euclidean weighted measure (a
   correct a.e. statement: infinite-action histories form a `mu_E`-null set when the
   weighted potential is integrable), (ii) explicit negations/explanations ("a.e. only
   when `E_V = 0`", "no a.e. statement can replace it when `E_V > 0`", the rejected
   alternative), and (iii) the response/decision text itself. No derivation claim uses
   the false quantifier.
6. **Round-1 record preserved:** `proposal-r1.md` (`cf65e7f20c158a2aa0f1185748dba013d80e8c71`,
   42845 B) and `_old_payload_line.txt` (`297e5e3dcfb1ca016108e19301faedf1b9ede6f6`,
   3471 B, the superseded payload line without CRLF) are kept unchanged as the round-1
   audit record; per the round protocol earlier rounds are never overwritten, so the
   revisions live in `proposal-r2.md` (review-r1 line pointers refer to r1 bytes).

## Self-corrections logged (honest record)

- r1 helper slip: a verbatim cross-check regex had been hand-transcribed from the
  review and failed; corrected to substring extraction from `review-r1.md`.
- First patch pass missed three anchors whose real bytes carried a 3-space list
  indent / extra sentence; re-read the exact regions and rebuilt (all replacements now
  assert count==1 at run time).
- Two residual section labels ("Volume/a.e. realization", "a.e./volume realization")
  renamed to "small-measure" after the first grep audit.
- `cert-r116p.py` Finding-5 assertions were inserted before the rmtree/CERT-PASS write
  and exercised in the fresh run above (they cannot pass silently: nonzero counters
  abort with nonzero exit before the out file is written).

## Baseline and closure evidence

- appH baseline at r2 start AND close: sha1 `f7a415d4707241ea6829b607afbf207697b50409`,
  830881 bytes (values recorded in the close-out verification below); digest gate
  `DIGEST CURRENT`. `chapters/` untouched by this run.
- Canonical POST arithmetic pointer only (NOT pinned; integrator recomputes from the
  CURRENT tree): 830881 + 3782 = 834663 if unchanged.
