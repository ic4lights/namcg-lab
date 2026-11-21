# Local re-review r1 (remote/claude, 2026-11-18): 066-bw-diamond-scope-correction (gpu r5 text)

VERDICT: ACCEPT | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/0

Source reading: digest + targeted reads + pattern scans over all 30 chapter files (Bisognano, Hislop, K_0, H_quad, half-sided, double cone, sqrt||dTheta||, modular, ...). This is not a literal line-by-line full scan; the author should decide whether that meets protocol 3(c).

Checks:
- appH L1-146 matches the accepted r5 result (gpu a19a30f), with CRLF preserved. moyal_K0_symbol_066.py re-run with matching output.
- Bisognano-Wichmann = wedge theorem; Hislop-Longo = geometric diamond flow, free massless scalar only. HislopLongo1982 verified via Crossref (DOI 10.1007/BF01208372).
- Labels are defined once. Build log: 414 pp, 0 undefined.
- No other passage keeps the old Bisognano-Wichmann diamond claim or the old O(R sqrt||dTheta||) bound.

Optional findings:
- appH L22: the heading could say "(conditional lemma)".
- appH L81-83: "at most identifiable" would be more exact.

Report-only (pre-existing, not in the import):
- ch06 L149-153 and ch02 L443-447 attribute H_D to Bisognano-Wichmann "in Rindler space", and give an unsourced leading-order small-diamond identification.
- ch17 calls A the "IR dictionary"; appH calls it the "matrix-to-modular map".

Disposition: keep the text as integrated. Problem A OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; no label change.
