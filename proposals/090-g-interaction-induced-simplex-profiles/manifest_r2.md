# Manifest, proposal 090, round 2

Round 2 = mechanical quantifier fix of the insert per review-r1 (F1, F2, taken F3; F4 no action).
Manuscript file touched by the proposed integration: `chapters/appH-microscopic-proofs.tex` only.
ALL round-1 files are frozen (never edited); the r2 scripts re-assert the frozen r1 insert hash.

## Integration artifact
- `insert-r2.tex` (integrator splices this, NOT insert-r1.tex): one paragraph, CRLF-terminated,
  3,894 bytes, sha256 first 8 hex 2f868a49. Built from frozen insert-r1.tex (3,735 / 3a6a69c4) by
  fix_insert_090_r2.py; delta +159 = F1 +114, F2 +12, F3 +33; extracted clauses unescaped from
  review-r1.md bytes (no retyping); changed regions (gap-merged character opcodes): bytes
  1336-1524, 1820-1946, 2281-2440 of r1; tail incl. closer byte-equal to r1.

## Splice contract (re-verified this round by simulate_apply_090_r2.py against the live tree)
- PRE appH: 752,790 B, sha256 4b5213160fab6154dbefcdaaf5795501eebed9add432b910660ef2b4e62068d6,
  CRLF 3,842, PIN count 1 (re-derive live before splicing; working tree is dirty).
- POST appH (insert-r2): 756,686 B (= PRE + 3,894 + 2, matching the review's delta rule),
  sha256 068ce3f21139911ee7beccd6086b85a4ad18b19df683918ee4beb67b2963df38, CRLF 3,844,
  lone-LF 0; outside-window byte identity asserted; layout L3191 089 / L3193 new / L3195 Vacuum.

## Audits (re-run from the repository root with `python -I`; .out files shipped)
- fix_insert_090_r2.py: pre/post asserts as above; prints size/sha8/delta; FIX R2 OK.
  History (disclosed): v1 wrong F1 end-marker; v5/v6/v7 F3 anchoring errors caught by asserts; a
  transient broken insert-r2.tex from the v7 run was overwritten by the passing final run; the
  shipped script is the final content and downstream scripts hash-verify the output.
- hygiene_090_r2.py: HYGIENE PASS (banned map empty; no macros/$/brackets/accents/control bytes;
  single CRLF line; \( \) 58/58; closer 1; header 1 in insert, 0 in PRE appH; frozen r1 checked).
- smoke_compile_090_r2.py: SMOKE GATE OK (POS insert-r2 rc=0; NEG \lvert->\lvertz in memory rc=1,
  Undefined control sequence; build dir in-folder scratch_latex/; frozen r1 checked).
- simulate_apply_090_r2.py: SIMULATE OK (read-only; contract above; frozen r1 checked).
- s1, s2, s2b, s2c, s3, s4 and all r1 audit artifacts: unchanged math and outputs; see manifest.md
  (round 1) for their descriptions and known shipped-fix history.

## Inventory (all files except this manifest, which self-references)
| file | bytes | sha256[0:8] |
|---|---|---|
| fix_insert_090_r2.out | 112 | 92ff595b |
| fix_insert_090_r2.py | 2363 | 32080cbd |
| hygiene_090.out | 268 | ffdff856 |
| hygiene_090.py | 1938 | 187617dc |
| hygiene_090_r2.out | 268 | db2823cf |
| hygiene_090_r2.py | 2103 | ec47ffb8 |
| insert-r1.tex | 3735 | 3a6a69c4 |
| insert-r2.tex | 3894 | 2f868a49 |
| manifest.md | 4834 | a11566c7 |
| proposal-r1.md | 25242 | 9090a9b9 |
| proposal-r2.md | 4837 | 38558962 |
| review-r1.md | 16138 | 29ed2d57 |
| s1_pushforward.out | 295 | c745375f |
| s1_pushforward.py | 1473 | 23a43f76 |
| s2_stationarity_D2.out | 569 | 84d81357 |
| s2_stationarity_D2.py | 1333 | bc9e9481 |
| s2b_stationarity_D3.out | 650 | f1a0e5f8 |
| s2b_stationarity_D3.py | 1731 | 08e15f60 |
| s2c_D4_and_gridmax.out | 240 | 75956a8a |
| s2c_D4_and_gridmax.py | 1772 | aeea4a3a |
| s3_limits_normalization.out | 536 | d747e30d |
| s3_limits_normalization.py | 2592 | 2424f8f4 |
| s4_mc_weighted_mean.out | 201 | 66fd6fc0 |
| s4_mc_weighted_mean.py | 1299 | 8aa33fad |
| scratch_latex/smoke090.log | 6727 | e2006d9f |
| scratch_latex/smoke090.tex | 3820 | 7f610b2f |
| scratch_latex/smoke090neg.log | 6016 | d4727355 |
| scratch_latex/smoke090neg.tex | 3821 | 06541ba9 |
| scratch_latex/smoke090r2.log | 6739 | 997db881 |
| scratch_latex/smoke090r2.tex | 3979 | 5d38960d |
| scratch_latex/smoke090r2neg.log | 6024 | b2c9f05b |
| scratch_latex/smoke090r2neg.tex | 3980 | a7cafc90 |
| simulate_apply_090.out | 404 | 86bfd2bb |
| simulate_apply_090.py | 1758 | 1c0e1de2 |
| simulate_apply_090_r2.out | 404 | 925eabe0 |
| simulate_apply_090_r2.py | 1921 | 3c09dd88 |
| smoke_compile_090.out | 99 | cbdb27ee |
| smoke_compile_090.py | 1817 | 9393d0f4 |
| smoke_compile_090_r2.out | 99 | eb18715e |
| smoke_compile_090_r2.py | 2002 | 41f64e58 |
