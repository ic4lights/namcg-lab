manifest.md - proposals/120-commutator-lift-bridge/ - S2-final (round 1)

Baseline manuscript pin: chapters/appH-microscopic-proofs.tex 9e0b198af2c3 / 848842 B.
Integration anchor: '\section{Problem E: signature}', count 1 at byte 295299.
Payload: insert-commutator-lift-r1.tex sha1[:12] 343226e27ebf / 5138 B (P1-pinned in verify pack).
POST: 853982 B = 848842 + 5138 + 2 (blank-line join), full sha1 d5e2e67c0a63ad3b0bce6034f2985ea94b9f3274.
Rerun identity: the four stage-1 re-run captures out-s2b-bridge-r1.txt, out-s2c-lift-r1.txt,
out-s3a-quartic-r1.txt, out-s3b-frame-r1.txt are byte-identical to the stage-1 pins recorded in
reports/ledger.md (CHAIN-120-S2-DEATH-RESUME): 9c14be97058a/828, b27a498ec4b2/1645,
1b01e527846c/1362, 0bc923bb8d5e/451; gen_payload_120.py ran twice byte-identical
(out-gen120-a.txt == out-gen120-b.txt, d1e03210a7f7/199); cert-r120p.py CERT PASS on the live tree.
119 doc-only addendum pins (applied previous round): scratch/120/notes.md 6fbc2d9b88f7/12257 ->
d81b9d34e5c3/13937; scratch/120/manifest.md 5e3e09090733/8999 -> 494242828797/10489.
verify pack: verify_r120.py final pin dac3381f5dc8/39762 (chain 54ec6b20233b/34530 -> 610a2c6c7a32/36376 (preR2) ->
b71430a6ebf3/36449 (preR3) -> final; re-derive with repair_chain120.py -> CHAIN OK 120;
repairs check-side only (verify_repair_log.txt); all pre-repair chk claim strings kept verbatim.

| file | sha1[:12] | bytes | notes |
|---|---|---|---|
| STATUS120.txt | 2420d85edae4 | 1069 |  |
| addendum119_manifest.txt | 5a0f5c809f84 | 1461 | 119 manifest.md addendum payload text (applied) |
| addendum119_notes.txt | 8d9f2cefe37b | 1650 | 119 notes.md addendum payload text (applied) |
| append_partB_r2.py | 447c8f7a9559 | 2732 |  |
| apply_trims120.py | 2ffbef78f10f | 775 | payload trim tool (earlier S2 round) |
| assemble_pr1.py | 4eb619312b8c | 2583 | proposal-r1.md assembler (guards placeholders/FAILs; CRLF) |
| census_trace120.py | fac1fc436daf | 1652 | trace/operatorname census helper (earlier S2 round) |
| cert-r120p-preR5.py | 1bf4a61b1597 | 4781 |  |
| cert-r120p.py | c633cbdc2288 | 4781 | compile certificate (CERT PASS) |
| check_labels120.py | b63bada1af1a | 1377 | label census (LABELS OK 120) |
| find_Tr120.py | 76ab813847c7 | 427 | census helper a |
| find_Tr120b.py | dda91f6178e6 | 460 | census helper b |
| find_Tr120c.py | a94e4c7dd13d | 441 | census helper c |
| find_Tr120d.py | 82eb06404851 | 441 | census helper d |
| fix_para5.py | 0a90e7bd536d | 1502 |  |
| fix_r5.py | c42a8957c7e4 | 2385 |  |
| gen_payload_120-superseded-r1.py | 3eab305230b3 | 10229 |  |
| gen_payload_120.py | 67cee1fbc771 | 10378 | payload generator (run twice byte-identical) |
| insert-commutator-lift-r1-superseded-r1.tex | 343226e27ebf | 5138 |  |
| insert-commutator-lift-r1.tex | a5aa77dc90a3 | 5287 | PAYLOAD (fixed input this round; P1-pinned) |
| manifest_gen120.py | c96a093658f2 | 6767 | this generator |
| out-assemble-r2.txt | 90b09755faa9 | 455 |  |
| out-assemble-r3.txt | 2b7cd5f38aa9 | 124 |  |
| out-cert-r120p-r2.txt | 53787eb3cf34 | 418 |  |
| out-cert-r120p.txt | 857fb96cda26 | 423 | CERT PASS capture |
| out-chain120.txt | 92546f3fa0ae | 305 | chain audit capture (CHAIN OK 120) |
| out-fix-para5.txt | 64bc94ba8213 | 150 |  |
| out-fix-r5.txt | eace1c893cdb | 152 |  |
| out-gen120-a.txt | d1e03210a7f7 | 199 | GEN OK 120 capture a |
| out-gen120-b.txt | d1e03210a7f7 | 199 | GEN OK 120 capture b (== a) |
| out-gen120-c.txt | 8990b3db0b43 | 199 |  |
| out-gen120-d.txt | 8990b3db0b43 | 199 |  |
| out-labels120.txt | 364326fc75b9 | 441 | label census capture |
| out-patchR1.txt | 785e25b72451 | 134 | repair R1 capture (CONTROL OK 120R1) |
| out-patchR2.txt | 782249320087 | 97 | repair R2 capture (CONTROL OK 120R2) |
| out-patchR3.txt | ce6a83f0a1c2 | 155 | repair R3 capture (CONTROL OK 120R3, APPLIED+VERIFY) |
| out-probe-t5c.txt | f708a5daa6fa | 6799 | probe capture (lift_from_B ~50 min/call; mats_eq 1 s) |
| out-probe1.txt | 415334b785ed | 1008 | assembly debris (chain-120 S2b deaths) |
| out-r120-fail1.txt | da39a3ee5e6b | 0 | RAW failed capture: orphan buffered run killed at 0 B (R0) |
| out-r120-fail2.txt | 8fcd9bad4289 | 2507 | RAW failed capture: stall localized at T5c, killed (R0/R1) |
| out-r120-fail3.txt | cfd7d16e2d31 | 2502 | RAW failed capture: post-R1 stall at simplify_sym, killed (R2) |
| out-r120-fail4.txt | 8fcd9bad4289 | 2507 | RAW failed capture: post-R1+R2 stall, probe localized (R3) |
| out-r120-rerun1.txt | 5452003fa8cd | 4474 | clean run copied to out-r120.txt |
| out-r120-rerun2.txt | b9a936c5b5fc | 4593 |  |
| out-r120-rerun3.txt | 0950831e672d | 4610 |  |
| out-r120.txt | da39a3ee5e6b | 0 | canonical clean verify capture (TOTAL/ALL CHECKS DONE 120) |
| out-s2b-bridge-r1.txt | 9c14be97058a | 828 | stage-1 s2b re-run (byte-identical to stage-1 pin) |
| out-s2c-lift-r1.txt | b27a498ec4b2 | 1645 | stage-1 s2c re-run (byte-identical to stage-1 pin) |
| out-s3a-quartic-r1.txt | 1b01e527846c | 1362 | stage-1 s3a re-run (byte-identical to stage-1 pin) |
| out-s3b-frame-r1.txt | 0bc923bb8d5e | 451 | stage-1 s3b re-run (byte-identical to stage-1 pin) |
| patch_r1_t5c.py | eea728c8b473 | 4546 | repair R1 applier + controls (idempotent; intermediate step) |
| patch_r2_simplify.py | 1999fe405b1f | 3036 | combined repair-chain re-deriver R1+R2 + controls (idempotent) |
| patch_r3_liftcongruence.py | e5b0848850c6 | 4682 | repair R3 applier + controls (idempotent) |
| patch_r4_verify.py | 3d449165b0fb | 5934 |  |
| pr1_partA.md | 001eca92495c | 4549 | drafted head (input to assembler; LF in source, CRLF in output) |
| pr1_partB.md | f38abdfd42df | 23643 | drafted continuation (input to assembler) |
| probe-r4-fast.txt | 34c386b9400c | 1130 |  |
| probe-r4-heavy.txt | 5b897e4edae4 | 2823292 |  |
| probe-r4-heavy2.txt | b8716c7f3d08 | 537 |  |
| probe_r4_triage.py | 1e6c7413212f | 6553 |  |
| probe_r4_triage2.py | 2f83640b6568 | 1478 |  |
| probe_t5c.py | 2fd89dd8b367 | 2311 | timing probe localizing the T5c full-lift cost (diagnostic) |
| proposal-r1.md | 52902a6bcfcc | 28621 | FINAL proposal text (r1) |
| repair_chain120.py | cab490414f9f | 2696 | combined audit re-deriver R1+R2+R3 + chk-name census (temp dir) |
| trims.json | 61f0170df7ac | 3071 | trim table consumed by apply_trims120.py (earlier S2 round) |
| verify_r120-preR1.py | 54ec6b20233b | 34530 | superseded verify bytes (54ec6b20233b/34530), preserved |
| verify_r120-preR2.py | 610a2c6c7a32 | 36376 | superseded verify bytes after R1 (610a2c6c7a32/36376), preserved |
| verify_r120-preR3.py | b71430a6ebf3 | 36449 | superseded verify bytes after R2 (b71430a6ebf3/36449), preserved |
| verify_r120-preR4.py | 6d72f26fbfd7 | 37603 |  |
| verify_r120-preR5.py | 4d751ac4afb8 | 39745 |  |
| verify_r120.py | dac3381f5dc8 | 39762 | verify pack, final post-R3 (see verify_repair_log.txt) |
| verify_repair-log-preR4.txt | 2812029591fa | 6729 |  |
| verify_repair_log.txt | 1924b768cedf | 11780 | repair log R0/R1 (check-side only; claims unchanged) |
| vpart2a.txt | 7188f28b8e59 | 2998 | assembly debris (chain-120 S2b deaths) |
| vpart2b.txt | 8b87648a224c | 5911 | assembly debris (chain-120 S2b deaths) |
| vpart3a.txt | eeed15add9aa | 5544 | assembly debris (chain-120 S2b deaths) |
| vpart3b.txt | 2070f9dcb725 | 6795 | assembly debris (chain-120 S2b deaths) |
| vpart3btail.txt | dd152fcd735b | 716 | assembly debris (chain-120 S2b deaths) |
| vpart3c.txt | e4d06a954d51 | 1898 | assembly debris (chain-120 S2b deaths) |
| vtest.txt | a6b2c3ebfeb1 | 27 | assembly debris (chain-120 S2b deaths) |
| write_r4_logs.py | 920b84a26816 | 7140 |  |
| manifest.md | self: see run report | - | this file (self-hash cell per the 119 documented rule) |

