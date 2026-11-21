VERDICT: NEEDS EVIDENCE | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 1/0

(Gatekeeper review r3, remote/claude, 2026-11-19. Saved here by the orchestrator. The gatekeeper is read-only.)

## Source reading
- Digest + targeted reads + a PARTIAL full scan. Digest CURRENT, dirty-chapters: yes. Protocol 3(d) applies (orchestrator ruling).
- Read in full: chapters/appH-microscopic-proofs.tex L1-2401, which covers A-D, all of E (L1509-1691) and F up to L2401.
- NOT read: appH L2402-3419 and the other 29 chapter files.
- Tree: appH sha256 6a83d79e... (same as at r2).

## Checks
- check_r3.py: 22 PASS, and its output matches the stored file.
- convert_r3.py: 8 PASS, with the unique map {eps_A=2 eps_c, gamma_A=gamma_c, g^2=1/2}.
- gk_normcheck_r2.py: |I| = 7.41732077747273, as predicted.
- build_r3.py reproduced exactly. Anchors A1 and A2 are unique in the tree.
- Applied copy (sha fa3e3181...) built with pdflatex/bibtex/pdflatex x2: 0 undefined, 0 multiply defined, 386 pp.
- Q and the four exponents were re-derived by hand.
- The Pauli-component reading of the reduced code was confirmed directly (055 n2_slice_r1.py L55, L107-109; 054 n2_exp_mech.py L43, L73-75). The insertion eigenvalue fixes the reading. The conversions were checked against the code's eps ladder and lists.
- The 8 disclosed differences against the original 057 tail are accurate and complete.
- Token diff r2 -> r3: only the listed changes.

## Findings
- r2 findings 1-6: all CLOSED.
- New finding 1 (blocking, procedural): the mandatory full scan was not completed (context exhausted).
  - Required: a scan-only gatekeeper pass over appH L2402-3419 and the 29 other chapter files.
  - The proposal text needs no change.
  - If the pass is clean, the verdict on these exact r3 texts becomes ACCEPT.
- Optional style point: the (f) sentence has two colons in a row. Not required.

## Disposition
Integrate E1-E4 (.r3.tex) jointly once the scan-only pass is clean. Re-verify that the anchors are unique at integration time.
No label change. Problem E stays OPEN / CRITICAL PATH for the matrix-derived label / PROGRAMME-CONDITIONAL.
