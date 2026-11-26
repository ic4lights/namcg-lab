# Manifest — proposals/102-g-profile-selection-output (round 2, updated in place)

All bytes/sha8/lines computed from live disk bytes (python hashlib, sha256, hex prefix 8; lines =
LF-byte count) at 2026-11-20 by the r2 finisher, after the r2 writes and before rewriting this
file. Rows added/refreshed in r2 are marked (r2).

| file | bytes | sha8 | lines | role |
|---|---|---|---|---|
| findings.md | 9958 | 1babba2e | 55 | (r2, corrected in place) authoritative route/results/classification/OPEN list; three `[r2 correction per review-r1 Finding N]` marked sites (centred-L2 phrasing; s3b record) |
| insert-r1.tex | 3155 | 654284b4 | 1 | retained-superseded (r2); never integrated; round-1 manuscript text |
| insert-r2.tex | 3173 | 86d4b849 | 1 | (r2) NEW manuscript text: insert-r1 with the single review-r1 Finding 1 clause replacement (centred L2 rate); one CRLF line, ASCII, no BOM |
| _mk_r2_102.py | 1497 | dba2c4e4 | 29 | (r2) transient r2 generator RETAINED as provenance (agent deaths #38/#39; 18-byte correction applied as orchestrator byte surgery; do not delete) |
| review-r1.md | 13343 | 8ebbdf7e | 59 | (r2) gatekeeper verdict ACCEPT WITH REQUIRED REVISIONS, milestone NONE, ordinal 33 |
| proposal-r1.md | 11832 | eb35b9f4 | 164 | round-1 write-up (its s3b "negative variance" evidentiary sentence is superseded by review-r1 Finding 2 / corrected findings.md; r1 files are never rewritten) |
| proposal-r2.md | 5533 | a61b6e8e | 94 | (r2) revision-round proposal |
| hygiene_102.py | 5264 | 076f9503 | 125 | (r2) hygiene gate retargeted to insert-r2.tex (3173/86d4b849 asserted) with r2 notes incl. 13->18 byte correction |
| hygiene_102.out | 1147 | 6a467d35 | 37 | (r2) hygiene run output, final line HYGIENE PASS, exit 0 |
| simulate_apply_102.py | 7849 | e0218a14 | 97 | (r2) splice simulation retargeted to insert-r2.tex; PIN = eigenvalue-reduction paragraph line + CRLF + blank-CRLF; POST computed not hardcoded |
| simulate_apply_102.out | 4538 | ea081e1f | 23 | (r2) PRE 798457 / cfb6af516017367f / CRLF 3866 / bareLF 0; PIN count 1; payload 3175; POST 801632 / sha16 e37ca5385996df34 / CRLF 3868 / bareLF 0; POST==PRE+payload True; SIMULATION PASS, exit 0 |
| s1_frame_identities.py | 5645 | 721278b4 | 112 | frame-identity corroboration script (no Dirichlet content cited); unchanged r1 |
| s1_frame_identities.out | 4569 | 7e65e893 | 56 | its output; inf rows at lines 39, 49 (lc=8, N=32) - flag when citing |
| s2_uniform_rho.py | 2455 | 44052e21 | 56 | superseded r1 floor script (never cited) |
| s2_uniform_rho.out | 1660 | 6e0b2dff | 20 | superseded r1 output (never cited) |
| s2_uniform_rho_r2.py | 2423 | 427415da | 56 | floor-equality script (D=2..5, p=1..6); unchanged r1 |
| s2_uniform_rho_r2.out | 1833 | 6c89b7dd | 25 | ALL EXACT CHECKS PASS; floor rho_p = prod_{k=1}^{p-1}(1+k/D); cited for the floor equality |
| s3_dirichlet_rho_stats.py | 6668 | c61c3b8c | 162 | crashed attempt (no .out); superseded, never cited |
| s3b_dirichlet_rho_stats.py | 7653 | d73bc216 | 175 | buggy-path script; Check-I/II numbers superseded; pin and MC blocks sound; in-file FIX 2 note identifies the defect |
| s3b_dirichlet_rho_stats.out | 1585 | 710fb2e8 | 22 | superseded wrong numbers (never cited as results); per review-r1 Finding 2 its Var line is nonnegative for all D>=1 and its expectations are the true values / D, gap line sign-flipped |
| s4_dirichlet_rho_direct.py | 9452 | 69a04377 | 213 | THE DELIVERABLE: exact flat-Dirichlet statistics of rho_p, D symbolic; unchanged r1, gatekeeper-reproduced |
| s4_dirichlet_rho_direct.out | 2757 | 7b293544 | 41 | 41 lines, exit 0, final line ALL CHECKS PASS (live bytes govern) |
| manifest.md | (self) | (self) | (self) | this file; a file cannot hash its own final bytes, so the self row is marked (self); all other rows are live |
| __pycache__/s1_frame_identities.cpython-311.pyc | 9870 | 082ecc4a | 60 | leftover compiled artifact from an earlier agent's s1 import (08:55, predates the r2 finisher); NOT evidence; no NEW .pyc was created by the r2 runs |

## Provenance notes

- Agent deaths: tool-echo deaths #34-#37 occurred on this item in round 1 (see hygiene_102.py
  in-file notes); deaths #38/#39 occurred in round 2 mid-round (the `_mk_r2_102.py` byte-fix was
  applied verbatim by the orchestrator as byte surgery, and findings.md's three r2 corrections
  plus the hygiene/simulate retargeting and their `.out` regeneration were completed by the
  orchestrator).
- findings.md was persisted by the orchestrator verbatim from the FIX-102 dispatch's completion
  handback (the agent's own Write was blocked by the harness); the provenance note is at the head
  of findings.md.
- The handback's "sha8 17544b9f" for `s4_dirichlet_rho_direct.out` was a pipe/EOL artifact; the
  live file hashes to 7b293544 (41 lines), and live bytes govern every citation in this package.
- FIX 2: the identification of s3b's `E_of_power_sum_monomial` defects (wrong falling factorial
  (D-1)!/(D-b)!; missing unit-trace substitution) is recorded in an in-file note in
  s3b_dirichlet_rho_stats.py and in findings.md; per review-r1 Finding 2 the correct defect record
  is: s3b's Check-I/II expectations equal the true values divided by D and its gap line is
  floor - E_true (sign-flipped); the earlier "Var negative at small D - impossible" claim is
  struck (s3b's Var line is nonnegative for all integer D >= 1). No s3b Check-I/Check-II number
  is cited anywhere in the insert or the proposals as a result.
- FIX H102 / FIX H102b: orchestrator in-file plumbing fixes to hygiene_102.py applied after death
  #37 (macro-loop key mapping; lenient UTF-8 decode of appH, which contains one non-ASCII byte
  0xe2 at offset 711159 from an integrated character - the ASCII-only assertion is on the insert).
- r2 byte-count correction: review-r1 stated the mandated clause pair differs by 13 bytes
  (expected insert 3168 B); byte measurement gives 18 bytes (`-\mathbb{E}\,s_{2}`), so
  insert-r2.tex is 3173 B, payload 3175 (3173 + blank CRLF), and the measured POST is 801632 /
  sha16 e37ca5385996df34 (the earlier r1-round handback figures "3170 / 801629" were superseded
  miscounts; measured values govern; the scripts compute and print POST, they do not hardcode it).
- PRE pins for the splice are live and unchanged: chapters/appH-microscopic-proofs.tex,
  798457 bytes, sha256 prefix cfb6af516017367f, 3866 CRLF, 0 bare LF, no BOM; the live manuscript
  is untouched by the simulations (POST written only to git-ignored scratch/102_sim_post.tex).
- _gen_sim_102.py (r1 transient generator) was used and deleted by the r1 finisher;
  _mk_r2_102.py (r2 transient generator) is RETAINED as provenance per orchestrator instruction.

MANIFEST r1 self-registered
MANIFEST r2 self-registered
