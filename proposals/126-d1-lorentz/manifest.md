# manifest 126-d1-lorentz (post-resume, 2026-11-25, resume1 final state)

Baseline manuscript (NOT touched by this chain; UNCOMMITTED, never restored):
chapters/appH-microscopic-proofs.tex sha1 76d862968c31d78fffc665f72aaf60d40c90367a,
875106 B, 4142 lines. HEAD stale for appH; live bytes are authority.

## Proposed integration object

- payload-126-v2.txt (PROPOSED TEXT): b9ebeba71fe933b1048dbcd2a0ec4f46d89c54dd, 4447 B
- appH-spliced-126-v2.tex (certified splice against the pinned baseline):
  13341a8b6fb7f99ff7a005a5ad4ad1d0cf3d5f93, 879555 B
- generator: make_payload_126.v2.py e996ca20baadcdf0a7b90df70616bc072a3a14d9
- compile certificate: out-cert-126-v3.txt (c1d578cb15e16d9adc3e2d0fd0c9215848610bd3),
  temp tree C:/Users/redgi/AppData/Local/Temp/build126_cert_v3_41207 (kept; outside repo)
- proposal: proposal-r1.md 728b651487e65f7b6eea46d40d0d16b46c29cfe5, 43408 B
  (embedded fenced payload byte-identical to payload-126-v2.txt: EMBED-MATCHES-PAYLOAD
  True via assemble_r1.resume.py)

## Byte accounting (splice recipe spliced = base.replace(ANCHOR, ANCHOR+PAYLOAD+b"\r\n"))

- payload v1: PRE 875106 + 4361 + 2 = POST 879469 (certified, out-cert-126.txt);
  canonical replace(anchor, payload+anchor) would be 879467 (NOT the recipe).
- payload v2: PRE 875106 + 4447 + 2 = POST 879555 (certified, out-cert-126-v3.txt);
  canonical alternative 879553.
- Anchor: "supplied: this paragraph closes none of Problem~D, Problem~D1, or
  Problem~A." + CRLFCRLF, count 1 at end of appH L1740 (before \section{Problem E}),
  asserted by both generators at splice time.

## Lineage

- journal.dead-bytes 23011583d2ee... 6579 B = predecessor agent's final journal bytes,
  preserved; journal.md b47bf1195f2e... 11655 B = same + resume rows R1-R4.
- make_payload_126.py d2826812c80a... 6486 B = pinned v1 generator (dispatch pin);
  byte-preserved copy make_payload_126.v1.py (identical hash). Kept on disk; do not
  re-run (would rewrite payload-126.txt / appH-spliced-126.tex; deterministic).
- payload v1 payload-126.txt 7e6ed4cd6c83... 4361 B (finding F1: ghost-sign clause)
  and its spliced file appH-spliced-126.tex 7534c424b969... 879469 B: SUPERSEDED, kept
  as evidence; certificate v2 out-cert-126.txt 58e57b109ddb... 1100 B points at them
  (temp tree build126_cert_v2_31476, kept).
- v2 derived from v1 source bytes by build_v2_generator_126.resume.py
  543511f423ce... (auditable diff; runtime count==1 asserts on both F1 clause anchors;
  the join guard demonstrably fires: it fired on a buggy intermediate insert).
- F1 fix diff: three difflib opcodes in one clause (delete "ghost "; insert operator
  form [\mathbb D^a,[\mathbb D_a,\cdot\,]]; insert " up to the sign of
  \(\hat X_a=\mathrm i\mathbb D_a\)"); all other bytes identical; PDF confirms new
  clause x1, old clause x0.

## File table (sha1, size)

    appH-spliced-126-v2.tex                 879555  13341a8b6fb7f99ff7a005a5ad4ad1d0cf3d5f93
    appH-spliced-126.tex                    879469  7534c424b9696c3596dc40e4d5ceac256408359b
    assemble_r1.resume.py                      1169  bf0ada6365949a97f4b8bc9ead10bb9341a78e1c
    build_v2_generator_126.resume.py           2639  543511f423ce26013d6071f38bb7a99c90fbbcf1
    check_payload_killing_126.resume.py        2333  20f9637200fe05b529f66bae17d11b615390d34e
    journal.dead-bytes                         6579  23011583d2ee8b9c22656498737404e3b6d6b23e
    journal.md                                11655  b47bf1195f2ef8492a126cc444180bcb7d1009e6
    make_payload_126.py                         6486  d2826812c80a1f465d584d427f11b19e1570bb29
    make_payload_126.v1.py                      6486  d2826812c80a1f465d584d427f11b19e1570bb29
    make_payload_126.v2.py                      7417  e996ca20baadcdf0a7b90df70616bc072a3a14d9
    out-A-run1.txt                               820  1815234621be72bb2713399124342d4f1d62a0a0
    out-A-run2.txt                               994  b75bb07c1f65802691d75f6d3795a51c2f33d6d6
    out-A-run3.txt                               994  b75bb07c1f65802691d75f6d3795a51c2f33d6d6
    out-A-run4.resume.txt                        994  b75bb07c1f65802691d75f6d3795a51c2f33d6d6
    out-B-run1.txt                               698  983414dd977661ba3b3175177aacc981208e5c06
    out-B-run2.txt                               897  46396df66b2c6ad875b26aff42c3833af34bdefd
    out-B-run3.txt                               897  46396df66b2c6ad875b26aff42c3833af34bdefd
    out-B-run4.resume.txt                        897  46396df66b2c6ad875b26aff42c3833af34bdefd
    out-C-run1.txt                              1859  8a58011ca9759d56389065f04d65ed45dfb10b3b
    out-C-run2.txt                              1859  8a58011ca9759d56389065f04d65ed45dfb10b3b
    out-C-run3.resume.txt                       1859  8a58011ca9759d56389065f04d65ed45dfb10b3b
    out-cert-126-v3.txt                         1763  c1d578cb15e16d9adc3e2d0fd0c9215848610bd3
    out-cert-126.txt                            1100  58e57b109ddba483794ed905b63e7fcf12b1ef05
    out-killing-check.resume.txt                 199  838e0bfa2f1be192070c994335f82a95ae02bf36
    out-payload-v2.txt                           119  716f3ef109c4c5e09dcfa0c23a9f7c66b8b4b646
    out-payload.txt                              119  929f594ac11525766bcbd203c0b34f843e97589e
    payload-126-v2.txt                          4447  b9ebeba71fe933b1048dbcd2a0ec4f46d89c54dd
    payload-126.txt                             4361  7e6ed4cd6c838d14bb017961740bd0bbf71c7691
    proposal-r1.md                             43408  728b651487e65f7b6eea46d40d0d16b46c29cfe5
    verify_126_A_nogo.py                        7068  aa8135e0299f7ed1801e9c49dc214136b84c21a2
    verify_126_B_flat5.py                       7913  b87f28eeedc38d0798bf09ec6d74494ae52505d9
    verify_126_C_spinor.py                     12328  52f7204c5443ad4308fe58309243931987a010c8

Re-run equality: A run4 = run3 = run2 (b75bb07c1f65); B run4 = run3 = run2
(46396df66b2c); C run3.resume = run2 = run1 (8a58011ca975). Generator v1 re-run
(temp C:/Users/redgi/AppData/Local/Temp/check126_resume, kept) reproduced
7e6ed4cd6c83/4361 and 7534c424b969/879469 byte-identically.

Frozen: proposals/123-f-coeff-locked-block/verify_ghost_op_123.py never run.
Repo never built; no git write commands; chapters/ untouched; no status labels touched.

## Round 2 (2026-11-25, review-r1 disposition) -- payload v3 lineage
    make_payload_126.v3.py     8207  432496798bed9c4c45394ec1d5d3141814d434ae  (19 CTRL-FIRED / 0 CTRL-DEAD; run capture out-payload-v3.txt)
    payload-126-v3.txt         4915  fb89da16df60f08b595e3fb0df71ce577e05fb61  (v2 4447 + 468; 8 byte-replacements = review-r1 Findings 1a/1b/1c/2/3/4/5/6, no other bytes)
    appH-spliced-126-v3.tex  880023  123108d4a94723be1dbad752883125baac940fe4  (POST 880023 = 875106 + 4915 + 2; generator POST + independent recompute agree; v2 POST 879555 VOID for integration)
    out-payload-v3.txt          688  c717deea514f5f730de5eae0e17333493761fb1f  (generator stdout)
    out-diff-v2v3.txt          4294  98f848fdb129d6e91c0703e9e652a188ca8864a7  (difflib char-opcodes, 16 segments, v2 -> v3)
    cert_stage_126.r2.py       1491  d0c036e4e0f234717b231b52106d550a9732df95  (external tree build126_cert_v4_12620, kept, hash-asserted staging)
    out-cert-126-v4.txt        3814  563e7c25b578a2ade0317af94447fcbeac2f26d0  (item-108 certificate on v3 bytes: PASS1/2 exit 0, ^! 0, undef refs 0, undef cites 196 = baseline, multiply 0, pdf 3197586 B; clause probes PRESENT x1 / defects x0 in spliced region; PROBE-RESULT-SCOPED ALL-OK; 2 whole-book 'over with' hits = pre-existing unrelated text, recorded)
    r2part1.md              8819  3b941b8bd5ca4d101fa7bb5329d0dbbd2cc38342  (assembly part, kept for assembler re-run)
    r2part2.md              8799  5614409664cf6ce12ddd5a66c2a06e0ca1448721
    r2part3.md              4396  f649c3556d2b7a95eaaa1d5f83642a978cb3281d
    assemble_r2.py             1497  7d024f23529530c43962bf10e465dd2d78a06dde  (emits proposal-r2.md; PAYLOAD-EMBEDDED-SHA1 guard fb89da16df60, EMBED-MATCHES True)
    proposal-r2.md            31528  7e4f1cf6b96f6466bd8e9937e5bf39ab369c96a1  (round-2 record; Finding 7 corrected here, never in payload)

Preserved unmodified at round-2 close: payload-126-v2.txt b9ebeba71fe9/4447; make_payload_126.v2.py e996ca20baad/7417; appH-spliced-126-v2.tex 13341a8b6fb7/879555 (VOID for integration); proposal-r1.md 728b651487e6/43408; verify_126_A/B/C aa8135e0299f/7068, b87f28eeedc3/7913, 52f7204c5443/12328. Non-blocking (review-r1 F4 side note): verify_126_B_flat5.py docstring line 19 and R6 print labels stale vs the corrected centralizer claim (span{1,D}); executable checks correct; bytes intentionally untouched. Live appH at round-2 close: 76d862968c31/875106 (unchanged; must match at integration).
