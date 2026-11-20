# Manifest, proposal 091-g-core-induced-pair-correlation, round 3

Round 3 per review-r2.md (ACCEPT WITH REQUIRED REVISIONS, 14,111 B / sha8 cf92c775), finding 1
blocking. Option (i) of the corrected snippet adopted verbatim: the rank-one sentence is scoped
to "at constant variance on the contracted entries" with "identically distributed" restored
inside that class, and the closing sentence scoped to "the constant-profile rank-one slot
subclass of the gaussian state model;". Made ONLY by fix_insert_091_r3.py from frozen
insert-r2.tex (verified 3,749/ecc2b239 before surgery; two exact substring replacements, each
count-asserted 1 before and after). All r1/r2 files frozen and re-hashed this round: all match
manifest_r2.md / review-r2 registry exactly. Corrections register: the r1-review "a fortiori /
normalization removes slot scales" rationale is FALSE (normalization removes a common scale
only; slot-dependent variances survive; general-profile rank-one slots follow the 089
pushforward) - corrected in proposal-r3.md, never re-propagated hereafter.

## Manuscript payload (r3 ACTIVE insert)
| file | bytes | sha8 / full sha256 |
|---|---|---|
| insert-r3.tex | 3840 (+91 vs r2) | da7c500a, full sha256 da7c500a7251bc3f1bd374631533e622273156081eee147a90c35f9508742c92 |

r3 integration contract (simulate_apply_091_r3.py, LIVE tree re-pinned at r3 time):
PRE appH 756,686 B, sha256 068ce3f21139911ee7beccd6086b85a4ad18b19df683918ee4beb67b2963df38,
CRLF 3844, bareLF 0 (unchanged since ordinal 21); compound PIN count 1, Vacuum-term at line
start. Splice: after `closes nothing in Problem~G.\r\n\r\n` insert insert-r3.tex + one CRLF.
POST: 760,528 B, CRLF 3846, bareLF 0, sha256
46dbfb3f14d444b7e7046883e00e4c58d19847ab4b9ca37bd47a3f97e691811d; counts noun-17/verb-1/vac-2/
header-1. r1 POST 784cb0a8... and r2 POST 6b0b2914... are VOID for r3.

## r3 contract scripts
| file | bytes | sha8 | result |
|---|---|---|---|
| fix_insert_091_r3.py / .out | 1986/129 | 78140a0b/c5bc41f4 | surgery + all asserts; delta +91 |
| hygiene_091_r3.py / .out | 2252/709 | db6189ef/8a0781d6 | PASS (r2 battery + control-byte scan + 2 r3 scope spans + iid-count-2) |
| smoke_compile_091_r3.py / .out | 1556/110 | 0118843e/8a1901b3 | PASS (POS rc0, NEG rc1 undefined control sequence) |
| simulate_apply_091_r3.py / .out | 2190/581 | 3fea0865/fb25ce59 | PASS (read-only, live re-pin, NEW POST above) |

## Frozen artifacts (re-hashed this round; unchanged)
r1: insert-r1.tex 3773/3e471d12; proposal-r1.md 24899/0bf9784c; manifest.md 5647/21a162d7;
hygiene_091.py/.out 1693/bdcf1a56, 559/fb623710; smoke_compile_091.py/.out 1671/c7bf62ab,
107/04063dfb; simulate_apply_091.py/.out 2138/ec5cf934, 454/c5bd2eaa.
r2: insert-r2.tex 3749/ecc2b239; proposal-r2.md 5711/28f62ffc; manifest_r2.md 4004/565f97be;
fix_insert_091_r2.py/.out 1385/a7066c28, 109/93a4e3b3; hygiene_091_r2.py/.out 1887/0700dd26,
609/eb6b53c0; smoke_compile_091_r2.py/.out 1556/834a03f9, 110/21d83e2a;
simulate_apply_091_r2.py/.out 1990/b206d9f0, 576/7ce728c8.
Reviews: review-r1.md 19199/807544fc; review-r2.md 14111/cf92c775.
Derivation scripts (unchanged, reusable): s2_exact_d2 2138/ec4d62ca (.out 141/6f7c2448);
s2b_exact_d2_stats_v2 1637/13297eb9 (.out 536/d6ac0eb3); s2c_chart_check 1507/84a4fbb6
(.out 185/a2141613); s2d_numeric_id_v2 1712/a013c95b (.out 282/33ed1be3); s2e_d3_jacobian_num
2166/c6750b9c (.out 158/fc669557); s2f_dirichlet_var 783/b3061f3c (.out 96/312ec0d0);
s3_mc_checks_v3 2407/b3733746 (.out 508/65822d0d; part (3) evidences the CONSTANT-VARIANCE
rank-one subclass only - see review-r2 check 3); s3b_tau_exponent 1210/01e93d33 (output
shipped as s3b_tau_exponent_v2.out 207/5d0382ec); s3c_tau_exponent_exact 1303/a9b13ea4
(.out 320/b2109e3e). This manifest lists every folder file except itself and proposal-r3.md.

## Quarantine table (cumulative)
| file | bytes | sha8 | status |
|---|---|---|---|
| s1_jacobian_v4.py / .out | 3318/735 | a3ea74ff/1a133e86 | dead-pass WIP; FALSE ratio-1 assertion in check (2) (true constant 2^(1-2a)); not relied upon |
| s2b_exact_d2_stats.py | 2743 | 7f830193 | superseded v1 (check 4d substitution bug) |
| s2d_numeric_id.out | 320 | ae75eabc | v1 crash output (BooleanAtom); fixed in v2 |
| s3_mc_checks.py | 3133 | c7efd5ad | superseded v1 (garbled 1b/1c; shape crash) |
| s3_mc_checks_v2.py / .out | 2245/961 | 696c894c/fe3c9d34 | superseded v2 (histogram-window artifacts) |
| s3b_tau_exponent.out | 742 | bfdfb69e | orphan stdin-echo of harness-flattened backgrounded heredoc; NOT output of s3b_tau_exponent.py (shipped output: s3b_tau_exponent_v2.out) [review-091r1 F3 naming note] |
| gkF.py (gatekeeper scratch) | - | - | D=3 pushforward MC predictor invalid (3.39732 vs 1.32274); no accepted claim relies on it [review-091r1 F2] |
| r1-review a-fortiori rationale (text) | - | - | PRIOR-CLAIM-ERROR per review-r2: "normalization removes slot scales" false; superseded by "exactly the 089 pushforward at general rank-one profile; flat iff uniform profile" |
