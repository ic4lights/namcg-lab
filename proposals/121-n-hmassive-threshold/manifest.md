# Manifest 121-n-hmassive-threshold (round 2, 2026-11-24)

Round-2 live-tree pins at assembly: appH sha1[:12] f5a761c55396 / 854131;
anchor "Problems~F and~N remain open." count 1 @ byte 853660 (line 4064) - no
drift since round 1. Round-1 verdict: ACCEPT WITH REQUIRED REVISIONS
(review-r1.md). Round 2 applies the three Corrected-snippet replacements only.

Artifact table (sha1[:12] / bytes; "supersedes" = old bytes retained by copy):

| file | sha1[:12] | bytes | note |
|---|---|---|---|
| insert-n-hmassive-threshold.tex | 84dcba179198 | 3754 | PAYLOAD r2; supersedes 702a60d1e5dc/3645; = old + 3 gatekeeper replacements (diffcheck EXACT-THREE-REPLACEMENTS True) |
| insert-n-hmassive-threshold-r1-superseded.tex | 702a60d1e5dc | 3645 | r1 payload bytes, superseded-by-copy evidence |
| appH-spliced-preview-r2.tex | cf3139fbedb0 | 857887 | r2 ARTIFACT-convention splice at 853660 (independent recompute; wrong-zone guard: bad-zone hash differs, byte count equal; wrong-zone r1 prefix f45e6e73ec04 guard True) |
| appH-spliced-preview.tex | cf3139fbedb0 | 857887 | same bytes, written by generator r3 |
| appH-spliced-preview-r1-superseded.tex | fd23c0d737b0 | 857778 | r1 preview bytes, evidence |
| gen_payload_121.py | 7e6456d40e74 | 6783 | generator r3 (3 payload-string replacements via byte patch, CRLF/ASCII preserved); supersedes e431049cf73c/6674 |
| gen_payload_121-r1-superseded.py | e431049cf73c | 6674 | r1 generator bytes, evidence |
| verify121.py | d04bf3101e0c | 10728 | r1 verifier, UNMODIFIED (no payload pins) |
| verify121-r2.py | f6e5b08d3f89 | 10754 | = verify121.py + ONE S11 selection filter ("'superseded' not in f") so the check cannot silently read the superseded copy (glob sorted[0] picks '-' < '.'); all check logic and controls byte-identical otherwise |
| out-gen121-r3.txt | fed697b48379 | 458 | generator r3 x2: hygiene OK, controls [True x5] both runs, payload 3754/84dcba179198, PRE 854131 POST 857887 delta-check True, sha1 spliced cf3139fbedb0, GEN121 OK |
| out-verify121-r6.txt | e5afce883cea | 1520 | verify121-r2.py x2: TOTAL 12/12 PASS, ALL CHECKS DONE 121, S11 ACTIVE |
| proposal-r2.md | (this round) | - | round-2 proposal: 3 before/after diffs, tiers-unchanged statement, attribution, deviation note |
| proposal-r1.md | a237b756fffd | 26236 | r1 proposal (lineage) |
| review-r1.md | - | - | gatekeeper r1: ACCEPT WITH REQUIRED REVISIONS; Corrected snippet = the 3 applied replacements |
| manifest_gen121.py | 0aef8a27545e | 2234 | r1 manifest generator (lineage; r2 manifest written directly) |
| out-gen121-r1.txt | ab53b5bc6ece | 1368 | lineage | out-gen121-r2.txt | 01f282955457 | 229 | lineage |
| out-verify121-r1..r5.txt | d6456dbf5f0d / a95dfa3d1a16 / a8e18093c73f / a8e18093c73f / f59d9b30ca8d | 649/2393/760/760/760 | lineage (r5 = FINAL r1 run 12/12) |

scratch/121/ artifacts (S:):

| file | sha1[:12] | bytes | note |
|---|---|---|---|
| S:cert-r121p.py | 36ed12edb9cc | 2405 | r1 cert, UNMODIFIED (pinned pin constant 3647) |
| S:cert-r121q.py | 55cadb3833e1 | 2405 | = cert-r121p.py with the single POST-delta pin constant 3647 -> 3756 (only change) |
| S:out-cert-r121q-r1.txt | a3bb2d681fba | 159 | CERT PASS: PRE 854131 f5a761c55396 POST 857887 cf3139fbedb0; pass 1 rc 0; pass 2 rc 0; exclam 0 undefrefs 0 multidef 0 undefcites(info) 48; temp removed True |
| S:patch_gen121.py | (scratch) | 1861 | byte-level 3-replacement patch of generator; fails closed on non-unique anchors |
| S:patch_verify121.py | (scratch) | 1062 | creates verify121-r2.py (selection filter only) |
| S:splice121r2.py | (scratch) | 1436 | independent artifact splice + independent sha1 + wrong-zone guard |
| S:diffcheck121.py | (scratch) | 1893 | proves payload delta = exactly the 3 replacements modulo CRLF wrapping |

Reproduce: `python -I gen_payload_121.py` (x2) -> out-gen121-r3.txt invariants;
`python -I splice121r2.py` -> SPLICE2 OK cf3139fbedb0/857887;
`python -I verify121-r2.py` (x2) -> 12/12 PASS / ALL CHECKS DONE 121;
`python -I scratch/121/diffcheck121.py` -> EXACT-THREE-REPLACEMENTS True;
`python -I scratch/121/cert-r121q.py` -> CERT PASS.
Labels: none changed. Integration target per review-r1 disposition: splice at
anchor (payload AFTER anchor blank line) once r2 ACCEPT issues.
