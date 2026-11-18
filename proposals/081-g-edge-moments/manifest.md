# Manifest 081-g-edge-moments, round 1

## Shipped files (size bytes, sha256)

- proposal-r1.md — 28788 B, 9560e16d7d11f35d251f59b0ced0ceeb291a80c66bbae599780b5e9c5628d5f4
  (manifest hashes exclude itself, the file whose own hash cannot be embedded)
- insert-r1.tex — 3609 B, 06e34e715a77c285f10337c55602cbd7e608e154dd5966424c611b1cea32fdd5
  (single content line + terminal CRLF; zero occurrences of $, [, ], \cite,
  \ref, \label, \eqref; banned-word scan clean except the closing idiom)
- s1_spectrum_wick_r2.py — 6021 B, 78d2faf77a5f1a6d3a034f87d4830c65fce83d253b8540aceea62dbd17ade78c
- s1_spectrum_wick_r2.out — 426 B, ec880f4e105bcaf5fc4d9de14482ddb2a9b26fa992a9610b637fcb1762718abc
- s2_eq_moment_identity.py — 7356 B, 8688366af6d3c372c70e291a54f1ed841242506713d4c146e274818ab755cedf
- s2_eq_moment_identity.out — 1204 B, 3b8fffcc243be5abed198e1da2bf2a9935c0d9add3d623e17f4456697577ce48
- s3_profile_concentration_r2.py — 7860 B, 7e04643d3b2d64c5c4b74d0f5a7db1ceb2295789ac39f792a394a2d72d61b8b9
- s3_profile_concentration_r2.out — 926 B, 90a8ad96341ed32a7ce42bb22adaee659d4ed9c7b65d3a8ce2779c656d496e16
- simulate_apply_081.py — 2812 B, 5908d9df5cd8150a8468820bdab0bbabbef1aef3b49207b0851a8dc6c0d19ccf
- simulate_apply_081.out — 437 B, 8dbbc60b846bcc9631e1ae9cea6b7b15ecee424c3e6097ce6e88cab3a8094754

All four .out files verified byte-reproducible across two `python -I` runs
from the repository root (`cmp` clean).

## Superseded untrusted WIP lineage (retained unmodified; NOT run to any
## result relied on by this package)

- s1_spectrum_wick.py — 5026 B, a81b490ca9a37d3cb3ed18f184aa3be9567ad2cf4e209557dd035ba57787fbef
  (sha8 a81b490c). j-DEPENDENT factor 2**(2*p+1-j) at lines 41, 102, 114;
  its docstring "verified" claims were never achieved.
- s1_spectrum_wick.out — 459 B, 0207ecc609a2d1469090355df42e94b5a6cce83ca9e9493509288c6022f6eaaf
  (sha8 0207ecc6). Stale: the recorded AssertionError traceback at line 87 of
  the draft, i.e. the draft never passed.
- s3_profile_concentration.py — 4656 B, 5a5efa006af3a3c44ca39e37defe72324cbcd7a9f686af3a37d65c6a733b5184
  (sha8 5a5efa00). Its bound (4) rho_p <= prod(1+i/D_eff) is FALSE (see
  s3_r2 audit: counterexample and reproduced own-list failure count 384).
  Disclosure: the draft s3 was executed read-only once during the audit, to
  reproduce its failure mode; no draft file was modified. Nothing in the
  shipped package relies on any draft output.

The three *_r2 / s2 scripts carry every numerical claim of the proposal and
the insert.

## Live-file pins (chapters/appH-microscopic-proofs.tex, read-only)

- PRE: size 725541 B; sha256
  f8797f82be8d590929388ea9eeb48b1988c4ce164445a2be362c51242df63ea1;
  CRLF count 3826; bare LF 0. These match the orchestrator pins; no drift.
- Anchor coordinates: insertion point = offset 688724, live line 3177, the
  line-start `\emph{Vacuum term.}` occurrence pinned by the unique preceding
  080-paragraph tail ("per-factor depths only ... close nothing in
  Problem~G."). The same string also begins live line 3006 (Problem F
  section) — a second occurrence that is NOT the anchor; the simulate script
  asserts total count 2. Header collision count 0.
- POST (simulated, never written): size 729152 B; sha256
  5d52b67252b152751709dd2f7d22ccdd29e77df131d60fd43432d7583463a303; CRLF 3828;
  bare LF 0; equals PRE with insert-r1.tex bytes + one separator CRLF spliced
  at the anchor offset.

## Honesty one-liner

Every number in the proposal and the insert traces to the shipped scripts
(rerun-verified) or to quoted live manuscript text; nothing closed; Problem G
remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
