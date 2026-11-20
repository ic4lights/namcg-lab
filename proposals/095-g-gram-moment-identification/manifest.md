# Manifest 095-g-gram-moment-identification (round 2, 2026-11-19)

Round-2 status: round 1 verdict ACCEPT WITH REQUIRED REVISIONS (review-r1.md); both required
revisions (R1, R2) implemented in `proposal-r2.md` as record-only repairs. **`insert-r1h.tex` is
unchanged (3,480 B / sha8 b9b75e8f, hash re-asserted by `r2_checks_095.py`) and remains the SOLE
integration artifact.** Superseded drafts unchanged and still never-integrate.

Live-tree reference at round-1 integration time (integrator must re-measure PRE and STOP if it
moved): `chapters/appH-microscopic-proofs.tex` PRE = 772,537 B / sha256
3f81a3a9627ce491726a108a10153c657cb4dc6c6274dc9a3a3e4dc117aa5a86 / CRLF 3,852 / bareLF 0; cut byte
735,720; expected POST 776,019 B / sha256
600588c1d1087232ace2cea1cdecf13fb38885cf7a2126a72eedfdc1234bfa0d / CRLF 3,854 / bareLF 0.

## Integration artifact (the ONLY file to integrate, as bytes)

| file | bytes | sha8 |
|---|---|---|
| insert-r1h.tex | 3,480 | b9b75e8f |

## Documents

| file | bytes | sha8 | note |
|---|---|---|---|
| proposal-r1.md | 25,055 | a2756f04 | round-1 proposal (superseded by r2 as the record of record) |
| proposal-r2.md | 32,509 | 6dc042e2 | round-2 record (standalone; implements R1 and R2) |
| review-r1.md | 13,538 | 04fb1009 | gatekeeper round-1 verdict |
| manifest.md | (this file) | — | — |

## Verification scripts + captured outputs

| file | bytes | sha8 | note |
|---|---|---|---|
| gram_moment_nonbridge_095.py | 6,000 | 30f869ae | r1, unchanged; SUMMARY ALL PASS |
| gram_moment_nonbridge_095.out | 775 | cdc2a167 | r1, unchanged |
| simulate_apply_095.py | 2,849 | 8f9b6414 | r1, unchanged; SUMMARY ALL PASS |
| simulate_apply_095.out | 610 | 6720e230 | r1, unchanged |
| hygiene_095.py | 2,586 | faaa845b | r1, unchanged; SUMMARY ALL PASS |
| hygiene_095.out | 739 | 2dad8832 | r1, unchanged |
| r2_checks_095.py | 4,240 | bf1de606 | r2; artifact hashes, pushforward-density re-derivation, record-change asserts |
| r2_checks_095.out | 640 | b55ca8c5 | r2; all 28 chk lines PASS, final line `R2 CHECKS 095: PASS` |

## Superseded artifacts — NEVER INTEGRATE / NEVER USE

| file | bytes | sha8 | defect |
|---|---|---|---|
| insert-r1.tex | 3,400 | 4ad7f7d9 | LF-terminated; definition/range shift inconsistency (rho-hat defined with +1 shift but shift-free ranges stated) |
| insert-r1f.tex | 3,473 | 5c28b084 | transit-escape corruption: 2x TAB instead of \tau, 2x CR instead of \rho |
| insert-r1g.tex | 3,477 | 5fad2334 | same corruption repaired, but rank-one clause imprecise ("slot-power profile statistic") |
| r2_checks_095-broken1.py | 4,109 | 55bd2e2b | first r2 check script; crashed on `sorted()` of sympy branch expressions (TypeError); superseded by r2_checks_095.py |
| r2_checks_095-broken1.out | 130 | 377dca18 | partial output of the broken first script run |
