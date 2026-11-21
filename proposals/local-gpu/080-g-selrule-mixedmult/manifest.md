# Manifest 080-g-selrule-mixedmult, round 2 (r1 lineage preserved below)

## Shipped files, round 2 (live sizes and sha256 as of 2026-11-17)

| file | bytes | sha256 |
|---|---|---|
| proposal-r2.md | 14355 | 3fd2ee641c3d1142b8f32a8d371d11ca05c1073e4bd97c45eaa14ead11e83409 |
| insert-r2.tex | 5395 | a74841c2916dc1ed438ec3d46b30129cea688ff0d2f9a41906cf7f34750487ee |
| make_insert_r2.py | 2869 | 50309cac259883a4907bace979375fb1326661d3928bfb166e9593dc25b8f629 |
| simulate_apply_080_r2.py | 2797 | f31aa4a6da1953cd24a89de50a6d85f474b9ae80c39f382b6329cdf1f8b3604b |
| simulate_apply_080_r2.out | 367 | ea1e189b288b99149dde580943864cdfcbdf80e701480a58d2e2e83cdb0bfca9 |

insert-r2.tex = insert-r1.tex with exactly the three review-r1 Corrected-snippet substitutions
(F1 sign-separation clause, F2 numeral "2", F3 "second and third paragraphs above"); byte delta
+157; generated mechanically by make_insert_r2.py and regenerated sha-stable on re-run.
manifest.md self-sha is not recorded (self-reference).

## Live tree pins, round 2 (read-only; appH on local/gpu working tree, digest head d8b29f8,
dirty-chapters: yes - 078/079 integrated, uncommitted; re-verified by re-run this round)

- PRE chapters/appH-microscopic-proofs.tex: 720144 B, sha256
  a10eca5184d853b8baa0ffac185c67265e6414672e93025dad05a4e08028012f, CRLF 3824, bare LF 0,
  headerCount 0 (appH and across all chapters/**/*.tex).
- Anchor: line-start of the unique line
  `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023} states that the vacuum energy there`
  at line 3175 (1-based). Insert lands at this offset with content "<insert-r2.tex bytes>\r\n":
  header at line 3175 and anchor at line 3177 after apply.
- POST (computed, never written): 725541 B, sha256
  f8797f82be8d590929388ea9eeb48b1988c4ce164445a2be362c51242df63ea1, CRLF 3826, bare LF 0.
- simulate_apply_080_r2.py asserts all PRE pins, computes POST, and re-checks the on-disk sha
  after the simulation ("no write performed"); shipped stdout re-run byte-identical this round.

## Void for integration (r1 artifacts)

- insert-r1.tex (5238 B / 79a3c29d...): superseded by insert-r2.tex; must NOT be integrated.
- r1 POST pins in proposal-r1.md / the r1 manifest section below (725384 B / e6a0335e...) and
  the POST line in simulate_apply_080.out: lineage-only, void for integration.

## r1 lineage (files kept byte-frozen in this folder; originals shipped 2026-11-17 round 1)

| file | bytes | sha256 |
|---|---|---|
| proposal-r1.md | 22836 | 32eec5c86ceb63b9ecbe9c6f2fa1baf8339419a242787f1fca6ed09557ce9bbb |
| insert-r1.tex | 5238 | 79a3c29d4c0329805bbfb79321e8cdcc1a9912d897db9e0767ad994e6e98bcf6 |
| s1_spectrum_mixed.py | 4053 | 76454bd3f5a8779d51e904b47659f967a7703d6e55a31b723f1fbf6025cec785 |
| s1_spectrum_mixed.out | 239 | ea16a9228bfd9cfd20ccca325712a8712171466c39502452be43809ec8d2f142 |
| s2_q2_criterion.py | 4385 | bd902b463d449772f56b8c5916b1e82cd4e47969b58cc11fc90bb95d6e428e80 |
| s2_q2_criterion.out | 636 | 50223927ec5adcf5d961fba96384f6eccfa1c0f5ac4cb36acf82c2d8df49cdb2 |
| s3_mixed_moments.py | 3997 | 79ab3e0603ad79dbf1399d43427890de263f70b458582b4f1fbd2841f5fee2b2 |
| s3_mixed_moments.out | 500 | 5de098ed642119fa548cdbed84610dc0a9d4feffe471c0b8004789f64db13c71 |
| simulate_apply_080.py | 2267 | d2326d70f3922e6248381f44fdc0655c1f1801e0a139cf61181bb134ac0b0308 |
| simulate_apply_080.out | 249 | 014aca1faf3cb2efeb48e09a4c98afa8f2dc1031ab04193b06ef00f7bb9e5738 |

Script seeds: 20261117 (all three numeric scripts); stdout byte-reproducible under
`python -I <script>` from the repository root, stderr empty; re-run this round: all four shipped
.out reproduced byte-identically (r1 repro pack stands; its POST line void, see above).
r1 PRE pins were identical to the r2 PRE pins above (tree unchanged since r1).

## Lineage of inherited inputs (from round 1, unchanged)

- 078 pencil identity det(lambda I - T) = det(lambda^2 I + 4 lambda H - 4 K), K >= 0, Re C0
  invisible, involution lambda -> -4n/lambda, double-root-vs-double-pair example (3,7)/(5,11):
  proposals/078-g-selrule-imalpha (review-r1 ACCEPT); reused as a lemma, reproved only in s1-A
  for the block-scalar instances.
- 076 rho_p signature-excess formula and the per-copy-invariance negation; fixed-q validity
  constraint: proposals/076-g-edge-uqstack-selrule (review-r1 L45 avenue (3); constraint
  re-confirmed in review-r2 L32).
- 077 D and U2 diagnostics, rank-one edge-datum family definition (U, R, C0, Z0), q=2 exact
  criterion statement: proposals/077-g-selrule-copyinv (review-r2; mixed-multiplicity target
  named at L47).
- 079 byte-contract convention and appH pins: proposals/079-g-frameavg-residual (review-r1).

## Honesty statements

Round 2: this round applies three gatekeeper-specified text corrections to the r1 insert and
re-issues byte pins; it derives nothing new, closes nothing, narrows nothing, and changes no
label in Problem G or elsewhere.

Round 1 (unchanged): this package realizes and characterizes mixed-multiplicity spectra for
block-scalar edge data at fixed depths, and does NOT: derive or test the selection rule, produce
or analyze any state or ensemble, treat depths growing with N, address the two-sided +/- reading,
the general (H, K) q > 2 criterion, or any missing step (i)-(iv) of Problem G; it closes nothing
in Problem G.
