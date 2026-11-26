# manifest 094-g-mfold-localization-unconditional (round 1, resume pass, 2026-11-19)

Lineage: the first pass on this package died on an API context limit with no verdict, mid-assembly of proposal-r1.md. This resume pass re-ran and re-verified every survivor script, independently re-derived the central math (spot_094_v2), found and fixed one false clause in the survivor insert, and completed the package. Re-verified byte-identical on re-run (stdout, EOL-normalized): s1_localization_094_v6.py, simulate_apply_094_v2.py (vs its .out), hygiene_094.py (vs its .out). Survivor sizes/sha8 on disk matched the orchestrator inventory exactly (all 21 files).

Final integration artifacts: insert-r1f2.tex (3415 B / 3cf45c6a) + simulate_apply_094_v5.py contract (PRE 769120/5f62af10 CRLF3850 bareLF0 -> POST 772537/3f81a3a9627ce491 CRLF3852 bareLF0, noun 20 verb 1 Vacuum 2 header 1) + hygiene_094_v4.py (28 checks PASS). proposal-r1.md uses bare LF endings to match proposals/093-*/proposal-r1.md (92 LF / 0 CRLF).

Registered files (name, bytes, sha256/8, status):
- _p1.md | 3523 | 38c5e92d | SUPERSEDED (dead-pass draft of proposal part 1; superseded by _q1-_q4)
- _q1.md | 5145 | cab0a0e5 | part 1 of proposal assembly
- _q2.md | 5726 | bab5a80d | part 2
- _q3.md | 4023 | a3933163 | part 3
- _q4.md | 6602 | 58614b5c | part 4
- byte_surgery_094.py | 3035 | 67dcab60 | SUPERSEDED (v1 NEW contained banned literal "[" but is the unique producer of insert-r1f.tex; kept as lineage)
- byte_surgery_094_v2.py | 3118 | 64919025 | SUPERSEDED (ran with a stale-filename assert and crashed after writing insert-r1f2.tex; no .out; superseded by v3)
- byte_surgery_094_v3.py | 3206 | b52ac8b1 | ACTIVE (canonical re-generator of insert-r1f2.tex from insert-r1.tex; its derived hygiene_v3/simulate_v4 pins are stale, do not use)
- hygiene_094.out | 1761 | 373a3c4f | record (superseded contract PASS vs insert-r1.tex)
- hygiene_094.py | 1852 | b5b59f21 | SUPERSEDED (pins insert-r1.tex; re-run byte-identical)
- hygiene_094_v2.out | 1761 | 43cdb4b8 | record (2 FAIL lines, HYGIENE OVERALL: FAIL vs insert-r1f.tex)
- hygiene_094_v2.py | 1854 | 6e38e0ce | SUPERSEDED (pins insert-r1f.tex; FAILs on banned bracket pair - evidence)
- hygiene_094_v3.out | 1761 | 43cdb4b8 | record (FAIL, mis-pinned run)
- hygiene_094_v3.py | 1854 | 6e38e0ce | SUPERSEDED (mis-pinned to insert-r1f.tex by surgery-v2 collateral; do not use)
- hygiene_094_v4.out | 1761 | 8e8036c2 | record (FINAL PASS)
- hygiene_094_v4.py | 1856 | a8d5d5da | ACTIVE FINAL contract vs insert-r1f2.tex (28 checks PASS)
- insert-r1.tex | 2968 | d7bf1889 | SUPERSEDED (false pointwise comparability clause; never integrate)
- insert-r1f.tex | 3415 | dc1cf8be | SUPERSEDED (contains banned literal bracket pair; failed hygiene_v2; never integrate)
- insert-r1f2.tex | 3415 | 3cf45c6a | FINAL INSERT (3415 B / 3cf45c6a; single use of the closing idiom)
- proposal-r1.md | 21496 | 56e5dd64 | FINAL proposal (round 1)
- s1_localization_094.out | 600 | 9426ec61 | record
- s1_localization_094.py | 3678 | 9403efa9 | SUPERSEDED (initial; see v-series history)
- s1_localization_094_v2.out | 2883 | dcd70ca1 | record
- s1_localization_094_v2.py | 3239 | 58d640f7 | SUPERSEDED (mpmath import fix)
- s1_localization_094_v3.out | 2036 | 324b417b | record
- s1_localization_094_v3.py | 3252 | c75ccc27 | SUPERSEDED (mpmath quad endpoint fix)
- s1_localization_094_v4.out | 469 | bd03d93d | record
- s1_localization_094_v4.py | 3273 | b59b4d3a | SUPERSEDED (quad accuracy)
- s1_localization_094_v5.out | 579 | b9bc3b65 | record (FAIL, evidence)
- s1_localization_094_v5.py | 3875 | 8cc4f3c8 | SUPERSEDED (FAIL: D1 slope window too early; D2 witness degenerate at E=0)
- s1_localization_094_v6.out | 578 | 2b2c057d | record (FINAL PASS)
- s1_localization_094_v6.py | 3682 | 3d50b398 | ACTIVE FINAL math
- simulate_apply_094.out | 507 | 0faac1ea | record
- simulate_apply_094.py | 2358 | 770d0d57 | SUPERSEDED (v1 wrongly required zero triple-CRLF globally)
- simulate_apply_094_v2.out | 365 | fa7e2035 | record (superseded contract PASS)
- simulate_apply_094_v2.py | 2446 | f0d4db02 | SUPERSEDED contract (pins insert-r1.tex; re-run byte-identical)
- simulate_apply_094_v3.out | 365 | 91b62742 | record (mis-pinned PASS)
- simulate_apply_094_v3.py | 2447 | 27bd9c39 | SUPERSEDED (mis-pinned to insert-r1f.tex; PASS there is not the final contract)
- simulate_apply_094_v4.out | 365 | 91b62742 | record (mis-pinned PASS)
- simulate_apply_094_v4.py | 2447 | 27bd9c39 | SUPERSEDED (same mis-pin as v3; do not use)
- simulate_apply_094_v5.out | 365 | 9a9be43f | record (FINAL PASS)
- simulate_apply_094_v5.py | 2448 | 131b4e93 | ACTIVE FINAL contract vs insert-r1f2.tex
- spot_094.out | 357 | 305106e8 | record (FAIL, evidence)
- spot_094.py | 3216 | f5344f8d | SUPERSEDED (my own v1 bugs: run-sum accumulation, 3D log-grid resolution, early window; FAIL is a script artifact, not a math negative)
- spot_094_v2.out | 337 | 06e14b44 | record (FINAL PASS)
- spot_094_v2.py | 3229 | ca58835d | ACTIVE independent verification
