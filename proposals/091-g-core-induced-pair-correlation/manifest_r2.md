# Manifest, proposal 091-g-core-induced-pair-correlation, round 2

Round 2 per review-r1.md (ACCEPT WITH REQUIRED REVISIONS, sha8 807544fc). Finding 1 adopted:
insert-r2.tex = insert-r1.tex with the 24-byte phrase `identically distributed ` deleted from
the rank-one sentence (`independent identically distributed complex entries` ->
`independent complex entries`; the sentence's `gaussian` modifier is upstream in
`a gaussian column contraction`). All other bytes identical; made ONLY by fix_insert_091_r2.py.
r1 files are frozen and were re-hashed: all match manifest.md (r1) exactly.

## Manuscript payload (r2 ACTIVE insert)
| file | bytes | sha8 |
|---|---|---|
| insert-r2.tex | 3749 | ecc2b239 (full sha256 ecc2b239fb95b07c46bc23b49781e9c955d55480b88ccd8577e9a69426d64b07) |

r2 integration contract (simulate_apply_091_r2.py, LIVE tree re-pinned at r2 time):
PRE appH 756,686 B, sha256 068ce3f21139911ee7beccd6086b85a4ad18b19df683918ee4beb67b2963df38,
CRLF 3844, bareLF 0 (unchanged from r1 pin; PIN count 1, Vacuum-term at line start).
Splice: after `closes nothing in Problem~G.\r\n\r\n` insert insert-r2.tex + one CRLF.
POST: 760,437 B, CRLF 3846, bareLF 0, sha256
6b0b2914f251a977b8bdeabc4e82a91a3a2d2890333fe0b3516c68d5aefa6c1e.
POST counts: noun-form 17, verb-form 1, Vacuum-term 2, new header 1. r1's POST sha 784cb0a8...
is VOID for r2 (different insert bytes).

## r2 contract scripts
| file | bytes | sha8 | result |
|---|---|---|---|
| fix_insert_091_r2.py / .out | 1385/109 | a7066c28/93a4e3b3 | surgery + all asserts pass |
| hygiene_091_r2.py / .out | 1887/609 | 0700dd26/eb6b53c0 | PASS (r1 24 checks + 2 r2 checks: F1 phrase deleted, A-block iid kept) |
| smoke_compile_091_r2.py / .out | 1556/110 | 834a03f9/21d83e2a | PASS (POS rc0, NEG rc1 undefined control sequence) |
| simulate_apply_091_r2.py / .out | 1990/576 | b206d9f0/7ce728c8 | PASS (read-only, live re-pin, NEW POST above) |

## Frozen r1 artifacts (unchanged; re-hashed this round)
insert-r1.tex 3773/3e471d12; proposal-r1.md 24899/0bf9784c; manifest.md 5647/21a162d7;
review-r1.md 19199/807544fc; hygiene_091.py/.out 1693/bdcf1a56, 559/fb623710;
smoke_compile_091.py/.out 1671/c7bf62ab, 107/04063dfb; simulate_apply_091.py/.out 2138/ec5cf934,
454/c5bd2eaa. Derivation scripts unchanged and reusable: s2_exact_d2 2138/ec4d62ca (.out 141/
6f7c2448); s2b_exact_d2_stats_v2 1637/13297eb9 (.out 536/d6ac0eb3); s2c_chart_check 1507/
84a4fbb6 (.out 185/a2141613); s2d_numeric_id_v2 1712/a013c95b (.out 282/33ed1be3);
s2e_d3_jacobian_num 2166/c6750b9c (.out 158/fc669557); s2f_dirichlet_var 783/b3061f3c
(.out 96/312ec0d0); s3_mc_checks_v3 2407/b3733746 (.out 508/65822d0d); s3b_tau_exponent
1210/01e93d33 (output shipped as s3b_tau_exponent_v2.out 207/5d0382ec); s3c_tau_exponent_exact
1303/a9b13ea4 (.out 320/b2109e3e).

## Quarantine table (cumulative, r2 notes included)
| file | bytes | sha8 | status |
|---|---|---|---|
| s1_jacobian_v4.py / .out | 3318/735 | a3ea74ff/1a133e86 | dead-pass WIP; check (2) ratio-1 assertion wrong (true 2^(1-2a)); not relied upon |
| s2b_exact_d2_stats.py | 2743 | 7f830193 | superseded first attempt (check 4d substitution) |
| s2d_numeric_id.out | 320 | ae75eabc | crash output of v1 (BooleanAtom); fixed in v2 |
| s3_mc_checks.py | 3133 | c7efd5ad | superseded (garbled 1b/1c; shape crash) |
| s3_mc_checks_v2.py / .out | 2245/961 | 696c894c/fe3c9d34 | superseded (histogram-window artifacts) |
| s3b_tau_exponent.out | 742 | bfdfb69e | stdin-echo artifact of a harness-flattened backgrounded heredoc; NOT the output of s3b_tau_exponent.py, whose shipped output is s3b_tau_exponent_v2.out [REVIEW-091 F3 naming note: future readers must diff against s3b_tau_exponent_v2.out; rename deferred] |
| gkF.py (gatekeeper scratch, scratch/gk091b/) | - | - | [REVIEW-091 F2 registration] D=3 pushforward MC predictor invalid (predicts 3.39732 vs true 1.32274 at x=0.3, g=(1,2.5,0.7): a D=2-form plug against a D=3 histogram); quarantined by the gatekeeper; no accepted claim relies on it |
