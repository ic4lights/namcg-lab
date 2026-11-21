# Manifest 087-g-derivedprofile-selection, round 3 (2026-11-18)
Closes review-r2 F5 (comment-only fix of the s4 header). No manuscript bytes touched;
insert-r2.tex and the POST contract 744,476/e7736a56... are unchanged and remain the
integration target. The r2 artifact set is byte-frozen and carried forward; nothing was
edited in place (prior-round files never mutated, per folder convention).

## r3 change (F5)
- s4_selection_content_r3.py 4843 19e90e60 — NEW live script. Header comment lines 3-7
  (byte span [146,545), old span 399 B) replaced by 687 B stating: (a) the tie
  E_pi Gamma >= lam+ * ||g - gbar||^2 = lam+ * W^2 (1/D_eff - 1/D) with D_eff = W^2/sum g^2 <= D
  (corrected sign, matching the code at line 95 and printed output); (b) lam+ = least
  eigenvalue of Sigma_pi restricted to mean-zero profiles (= least nonzero eigenvalue;
  > 0 iff the slot graph G_pi is connected); (c) the numerical checks exercise the
  connected case only (lam_plus() takes the least eigenvalue > 1e-9) and the
  general-measure case follows from the psd certificate Sigma_pi >= lam+ (I - D^-1 J),
  established in review-r2, not checked by this script. CODE bytes outside the comment
  span verified byte-identical (prefix/suffix equality at span bounds; first differing
  byte at offset 272, inside span; Hamming distance outside span = 0). ASCII-only.
- s4_selection_content.py 4555 d0981d8e — SUPERSEDED-BY-COMMENT-ONLY (kept; carries the
  F5 sign-flip defect in its header comment; code always correct). Do not re-run as live.
- stdout check: `python -I proposals/087-g-derivedprofile-selection/s4_selection_content_r3.py`
  from repo root → stdout 483 B / sha256 53fcf550…, byte-identical to the shipped
  s4_selection_content.out (483 53fcf550). rc 0.

## Full folder hash sweep at r3 (30 files; manifest_r3.md self-referential, not hashed)
build_insert_087.py 5460 4f02d531 | build_insert_r2.py 5558 8f25bc1c | build_proposal_r2.py 15058 941e663b
hygiene_087.out 1336 f8a7016a | hygiene_087.py 1921 ffd08b6c | hygiene_087_r2.out 1336 b79a7a48 | hygiene_087_r2.py 1921 470ede77
insert-r1.tex 5280 3fc233c9 (superseded) | insert-r2.tex 5378 5e692fbc (LIVE insert)
manifest.md 5003 247e8eeb | manifest_r2.md 5699 9feaf624 (frozen; does not quote the s4 header wording — verified, no amendment needed)
proposal-r1.md 28875 2ae709c0 | proposal-r2.md 36413 ec95617d (proposal text unchanged; F5 was folder-local)
review-r1.md 17057 3a5d4486 | review-r2.md 14937 634a3ba7
s1_variance_graph.out 397 dba73a0c | s1_variance_graph.py 5854 92f019ae
s2_haar_stiffness.out 652 70abf974 | s2_haar_stiffness.py 4359 a389d3d8
s3_proxy_closedforms.out 1261 e5a483ee | s3_proxy_closedforms.py 5501 4f203f52
s4_selection_content.out 483 53fcf550 (shipped stdout contract; unchanged) | s4_selection_content.py 4555 d0981d8e (superseded, F5)
s4_selection_content_r3.py 4843 19e90e60 (LIVE s4 script)
simulate_apply_087.out 382 b1e2855a | simulate_apply_087.py 1796 93d77efb (dead, declared r2)
simulate_apply_087_fix.out 589 fb1359a2 | simulate_apply_087_fix.py 3096 62cb48c9 (dead, declared r2)
simulate_apply_087_r2.out 589 0c616886 | simulate_apply_087_r2.py 3143 44171c42 (LIVE simulator; matches gatekeeper independent splice)
All r2-set sizes/sha8 identical to the pre-r3 sweep: zero drift outside this folder-local addition.

## Unchanged contracts (do not re-verify)
- Live appH pin: 739,096 B / sha256 31b345ed…679d / CRLF 3,836 / bareLF 0; PIN = full 085 closer (count 1).
- Splice insert-r2.tex + one CRLF at next `\emph{Vacuum term.}` line-start → POST 744,476 /
  e7736a56230f80eff3c3325c519eda797d2f3b7a1a77c4f785451d51b79df75b / CRLF 3,838 / bareLF 0.
- Never splice against 744,376/d65eb64f or 744,378/38db6497 (superseded r1-era contracts).
