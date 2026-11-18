# Manifest 087-g-derivedprofile-selection, round 2 (2026-11-18)

Round 2 addresses review-r1 (ACCEPT WITH REQUIRED REVISIONS, 17,057 B /
sha8 3a5d4486): blocking F1 (false stiffness-tie clause in the insert)
plus minors F2/F3/F4. Finding-by-finding actions are registered in
proposal-r2.md, section "Round 2 corrections". This round adds the
clause-corrected insert (insert-r2.tex) and the r2 verification chain;
r1 artifacts are kept unmodified as audit trail except two assert-guarded
comment-only script fixes (s1, s4), each re-run with stdout
byte-identical to its unchanged shipped .out.

## File table (size B / sha256 first 8)

Round-2 generated (AUTHORITATIVE chain marked):
- build_insert_r2.py 5,558 / 8f25bc1c (byte-surgery copy of
  build_insert_087.py: F1 clause span at source offset 2244 plus the
  output-filename span; round-trip assert proves the two spans are the
  whole diff)
- insert-r2.tex 5,378 / 5e692fbc, full sha256
  5e692fbca8984cd552047b38ba52a35df63409f4df4333795ffbbe4af31fc3a6
  (AUTHORITATIVE insert: single content line + terminal CRLF; vs
  insert-r1.tex a single changed span, common prefix 2,233 B, common
  suffix 3,008 B, 39 B replaced by 137 B, +98 B)
- hygiene_087_r2.py 1,921 / 470ede77 ; hygiene_087_r2.out 1,336 /
  b79a7a48 (overall PASS, 5,378 B; numeral set identical to r1 - the
  corrected clause adds no numerals)
- simulate_apply_087_r2.py 3,143 / 44171c42 ;
  simulate_apply_087_r2.out 589 / 0c616886 (AUTHORITATIVE round-2
  splice: PRE 739,096 / 31b345ed...; POST 744,476 B / sha256
  e7736a56230f80eff3c3325c519eda797d2f3b7a1a77c4f785451d51b79df75b /
  CRLF 3,838 / bareLF 0 / close-idiom 14 / header 1 / Vacuum-term 2)
- build_proposal_r2.py 15,058 / 941e663b (deterministic driver:
  regenerates proposal-r2.md from proposal-r1.md (pin 2ae709c0) and
  review-r1.md (pin 3a5d4486) with per-anchor count asserts; refuses to
  write on any mismatch)
- proposal-r2.md 36,413 / ec95617d, full sha256
  ec95617d029bfb5b76e76ca857b573bba3d250879b34cc3b8a2659439aa425e8
  (supersedes proposal-r1.md, which is kept)

Carried from round 1, re-hashed this round:
- proposal-r1.md 28,875 / 2ae709c0 (unchanged)
- review-r1.md 17,057 / 3a5d4486 (gatekeeper input, unchanged)
- insert-r1.tex 5,280 / 3fc233c9 (SUPERSEDED by insert-r2.tex; kept)
- build_insert_087.py 5,460 / 4f02d531 (superseded generator; kept;
  still regenerates insert-r1.tex byte-identically)
- hygiene_087.py 1,921 / ffd08b6c ; hygiene_087.out 1,336 / f8a7016a
  (r1-pair hygiene record; kept)
- simulate_apply_087_fix.py 3,096 / 62cb48c9 ;
  simulate_apply_087_fix.out 589 / fb1359a2 (encodes the VOID r1
  contract for insert-r1.tex bytes only; audit trail)
- s2_haar_stiffness.py 4,359 / a389d3d8 ; s2_haar_stiffness.out 652 /
  70abf974 (unchanged)
- s3_proxy_closedforms.py 5,501 / 4f203f52 ; s3_proxy_closedforms.out
  1,261 / e5a483ee (unchanged)
- s1_variance_graph.py 5,854 / 92f019ae (ROUND-2 comment-only fix, was
  5,769 / fbfc512a: header phase-provenance corrected per review F2;
  stdout re-run byte-identical to s1_variance_graph.out 397 / dba73a0c)
- s4_selection_content.py 4,555 / d0981d8e (ROUND-2 comment-only fix,
  was 4,456 / 584e64ec: lam+ definition corrected per review F1; stdout
  re-run byte-identical to s4_selection_content.out 483 / 53fcf550)
- simulate_apply_087.py 1,796 / 93d77efb ; simulate_apply_087.out 382 /
  b1e2855a (dead; audit)
- manifest.md 5,003 / 247e8eeb (r1 manifest, unchanged)

## Dead / void artifacts (registered; do not integrate against either)
1. simulate_apply_087.py: POST 744,376 / d65eb64f - same-line splice
   defect (r1 finding; unchanged).
2. simulate_apply_087_fix.py: POST 744,378 /
   38db6497530b15663f6d206912dfce0e59662941eb1dc3d46912ae7d43d640bd -
   void once the F1 clause fix is applied: valid only for the superseded
   insert-r1.tex bytes.
Integrate only against simulate_apply_087_r2.py (POST 744,476 /
e7736a56230f80eff3c3325c519eda797d2f3b7a1a77c4f785451d51b79df75b).

## Reproduction pack (round 2; from the repository root; expect exit 0)
1. python -I proposals/087-g-derivedprofile-selection/build_insert_r2.py
   -> stdout "insert bytes 5378"; insert-r2.tex stays 5,378 / 5e692fbc.
2. python -I proposals/087-g-derivedprofile-selection/hygiene_087_r2.py
   -> stdout == hygiene_087_r2.out (b79a7a48); "overall PASS".
3. python -I proposals/087-g-derivedprofile-selection/simulate_apply_087_r2.py
   -> stdout == simulate_apply_087_r2.out (0c616886); POST pins above;
   three CRLFCRLF boundary probes; "no write performed".
4. python -I .../s1_variance_graph.py and .../s4_selection_content.py
   (comment-fixed sources) -> stdout byte-identical to the UNCHANGED
   .out files (dba73a0c / 53fcf550).
5. s2 / s3 -> unchanged .out (70abf974 / e5a483ee), as round 1.
6. python -I .../build_proposal_r2.py -> regenerates proposal-r2.md
   byte-identically (36,413 / ec95617d) from pinned inputs.
7. python -I .../build_insert_087.py -> "insert bytes 5280";
   insert-r1.tex stays 5,280 / 3fc233c9 (audit pair).

Live-repo pins at this round (read-only; re-verified before AND after
every run; unchanged): chapters/appH-microscopic-proofs.tex 739,096 B /
sha256 31b345ed5e957910bacd3c02ebae87edfbeb5f0effa77c98149f6eafc2a2679d
/ CRLF 3,836 / bareLF 0. Forward-pin note (F3, for the integrator and
the frontier row): after this integration the full-085-closer PIN
counts 2; re-anchor any later chain-2 edit to the 087 closer unique
tail ("they classify the locus over frame laws rather than selecting
the profile"). No git write commands were run; no file outside this
proposal folder was created or modified; appH was never opened for
write. Self-hash line intentionally omitted (review-r1 F4 pattern).
