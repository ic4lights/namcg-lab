# Manifest 108-a-map-noncentral-chart-select (round 3)

Regenerated 2026-11-21 at round-3 close. Live appH 812227 B / sha256/16 698f38979140770d / 3876 CRLF (107 state;
r2 integration REVERTED after a fatal pdflatex error in the accepted r2 payload). All triples regenerated from
disk at the end of round 3; the manifest excludes itself by necessity.

**History:** r1 review = ACCEPT WITH REQUIRED REVISIONS (math verified; four wording substitutions staged as gatekeeper
byte authority; review-r1.md). r2 adopted that authority byte-for-byte; r2 review = ACCEPT ("integrate insert-r2.tex
as-is", review-r2.md). At integration the r2 splice compiled FATAL: `! Package amsmath Error: \hat allowed only in
math mode.` at l.144 (paragraph opening `Let \hat X^I be`) — LaTeX syntax defect missed by every prior check because
no compile test existed (scratch/apply_108.out, scratch/build_check_108.out). Integration cleanly reverted. Round 3 =
delimiter-only fix + compile certificate; NO claim, scope, gap or status changed.

**Round-3 integration contract:** payload `insert-r3.tex` (3076 B / `356f6ba97912775c` / 1 CRLF) = insert-r2.tex +
ONE `\( \)` pair around the single text-mode island `\hat X^I` (parser authority mk_insert_r3_108d.py; normalization
assert: r3 minus all delimiters == r2 minus all delimiters, byte-for-byte, PASS). Splice at the unique PIN
"does not close Problem~A.\r\n\r\n\paragraph{Missing step.}" (count 1, rebuilt from CURRENT live bytes; offset 14892),
PRE 812227/698f38979140770d/3876 -> POST computed **815305/4b3e836d29b3efa5/3878** (= r2-certified POST + 4 bytes),
undo True, live unchanged (simulate_apply_108_r3.out). Preview authority:
`scratch/sim/appH_after_108_r3_preview.tex` (815305/4b3e836d29b3efa5/3878).

**Compile certificate:** compile_cert_108_r3b.py built a sandbox copy of the manuscript inputs in scratch/compile108/,
spliced the r3 payload into the COPIED appH (triple 815305/4b3e836d29b3efa5/3878, equal to the simulate POST), ran one
`pdflatex -interaction=nonstopmode -halt-on-error namcg-book7.tex` pass: exit 0, zero `! ` lines,
"Output written on namcg-book7.pdf (426 pages, 2707904 bytes)", live appH untouched. Evidence compile_cert_108_r3.out.
(compile_cert_108_r3.py — superseded first attempt whose sandbox filter dropped figure PDFs; provenance only.)

**Sole battery authority:** `s4_noncentral_selection_v3.py` (16/16 PASS; v1/v2 inert provenance: v1 = 4 FAIL +
NameError, v2 = 15/16 check-12 sign error).

## Proposal-folder files (name | size B | sha256/16 | CRLF)

Active (round 3):
- insert-r3.tex | 3076 | 356f6ba97912775c | 1   <-- SOLE INTEGRATION PAYLOAD
- proposal-r3.md | 5390 | 725459679e5c3604 | 0
- mk_insert_r3_108d.py | 2738 | 9d904208090b01f9 | 0   (r3 generator authority)
- mk_insert_r3_108.py | 3097 | 3eb274d1f1b51da4 | 0   (inert: failed own asserts, never wrote payload)
- mk_insert_r3_108b.py | 2519 | 0395c107e9e739f1 | 0   (inert: same)
- mk_insert_r3_108c.py | 2809 | e8a6703152c6da13 | 0   (inert: same)
- compile_cert_108_r3b.py | 3355 | 95779cdc3956521c | 0   (compile certificate authority)
- compile_cert_108_r3.py | 3362 | ca10356e450413c9 | 0   (superseded sandbox filter, provenance)
- compile_cert_108_r3.out | 321 | ad7aebfb2830b670 | 7   (COMPILE CERT PASS, 426 pages)
- hygiene_108_r3.py | 2581 | f480ec27f0d093be | 0
- hygiene_108_r3.out | 773 | 27b3dc113e04e1b3 | 22   (21/21 PASS, file=insert-r3.tex, folder cwd)
- simulate_apply_108_r3.py | 2177 | 9a416f3c670747e4 | 0
- simulate_apply_108_r3.out | 550 | f7d25afc46cffbb5 | 9
- review-r2.md | 7166 | d2ad9db948ff91d5 | 0   (ACCEPT of r2; compile gap noted here)
- review-r1.md | 17788 | e1dd88b79f8be127 | 0

Superseded but valid provenance (retained, never delete):
- insert-r2.tex | 3072 | 180b005188c8268a | 1   (SUPERSEDED BY COMPILE FAILURE — DO NOT INTEGRATE; accepted
  text/math; gatekeeper byte authority of round 1; sole content source of r3 modulo one delimiter pair)
- proposal-r2.md | 5753 | 2a84a51c3a188e61 | 0
- adopt_r2_108.py | 1272 | 866515592836b007 | 0   (byte adoption of gatekeeper authority, CANDIDATE MATCH True)
- mk_hygiene_r2_108.py | 792 | 9fb664782dcc3300 | 0
- hygiene_108_r2.py | 2581 | 331d09c283b65742 | 0 ; hygiene_108_r2.out | 773 | e02de1598c85cf51 | 22
- simulate_apply_108_r2.py | 2349 | b049afea2a03b399 | 0 ; simulate_apply_108_r2.out | 607 | b3a78ba2531432e3 | 10

Round-1 authorities and inert provenance (unchanged on disk):
- proposal-r1.md | 35560 | 9a298f7eacf3b589 | 0   (claim table unchanged; still matches r3 payload)
- s4_noncentral_selection_v3.py | 15595 | ffa671abb3a6e4d6 | 0 ; s4_noncentral_selection_v3.out | 2576 | 6fb8631fcecda151 | 18
- s4_noncentral_selection.py | 15515 | c0104aced9dab9d9 | 0 (INERT) ; s4_noncentral_selection.out | 1872 | ff8e938b4a57fcca | 13
- s4_noncentral_selection_v2.py | 15579 | 4b7b7a680efae27a | 0 (INERT) ; s4_noncentral_selection_v2.out | 2576 | 72e561ae42b86805 | 18
- insert-r1.tex | 2836 | 7657be68c8ffa5b4 | 1   (SUPERSEDED — rejected at r1 for the four substitutions)
- mk_insert_108_r1.py | 3470 | af6146cb06efd1f2 | 0 ; hygiene_108_r1.py | 2581 | 06c64a989861bb1b | 0 ; hygiene_108_r1.out | 773 | dd68b9bcb2871efe | 22
- simulate_apply_108_r1.py | 2024 | 1f238c6a20f0e31a | 0 ; simulate_apply_108_r1.out | 497 | 67d0ba03fd457543 | 9
- simulate_apply_108_r1b.py | 2077 | 50cb46a831c48049 | 0 ; simulate_apply_108_r1b.out | 550 | a7b893f521e099e9 | 9
- simulate_apply_108_r1c.py | 2113 | b7a5885c39c2373f | 0 ; simulate_apply_108_r1c.out | 584 | 83d06599fc24c1d1 | 9

## Evidence in scratch/

Round 3:
- scratch/sim/appH_after_108_r3_preview.tex | 815305 | 4b3e836d29b3efa5 | 3878 CRLF   (round-3 preview authority)
- scratch/compile108/   (sandbox build: namcg-book7.pdf 426 pp, log with zero error lines; rebuildable by compile_cert_108_r3b.py)
- scratch/apply_108.out | 273 | (integrator r2 splice log, PRE/POST certified); scratch/build_check_108.out | 22899 (r2 compile failure log)

Round 1 recovery evidence and previews (unchanged):
- scratch/s4_v3_rerun_r1.out | 2576 | 6fb8631fcecda151 ; scratch/s4_v1_rerun_r1.out | 1872 | ff8e938b4a57fcca
- scratch/s4_v1_rerun_r1.err | 1412 | 6c9ae68aa923b599 ; scratch/s4_v2_rerun_r1.out | 2576 | 72e561ae42b86805
- scratch/hygiene_108_rerun_r1.out | 773 | dd68b9bcb2871efe ; scratch/simulate_108_r1c_rerun_r1.out | 584 | 83d06599fc24c1d1
- scratch/sim/appH_after_108_r1_preview.tex | 815065 | dcfa82a524551702 (SUPERSEDED)
- scratch/gk108/insert-corrected-gk.tex | 3072 | 180b005188c8268a | 1 (gatekeeper byte authority; == insert-r2.tex)
- scratch/gk108/gk_post_preview_r1_corrected.tex | 815301 (gatekeeper r2 splice certification; superseded by r3)
