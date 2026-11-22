# R111-P payload note (manuscript-bound text for ordinal-41 slot)

Payload: proposals/111-g-relative-entropy-density/insert-g-srel.tex
sha1 c3d119f6c00931f6bd5843a99c80cec0f445e030, 2452 bytes, pure CRLF, UTF-8 no BOM, one \paragraph block, no \label, no \ref/\cite, one unnumbered display.

Anchor strings (live tree appH sha1 882de86864d9e9b2e14219bf223a3a0c0dd7d11f, verified by count this pass):
- BEFORE (must stay above insert): "Closing the matrix-derived criterion for Problem~G requires" — count 1; its block ends "schematic." — count 1.
- AFTER (insert immediately before this line): "\paragraph{Edge entropy of a matrix block" — count 1.
This matches r2's landing note (L289-291): after "Missing step." paragraph, before "Edge entropy of a matrix block ..." paragraph (sec:status-G).

Claim crosswalk (payload clause -> certifying r2 section, sha1 f3d9ee751e1a1114c75de19d4e680acde2027191):
1. sigma0, A0 closed form, c0 = -ln Z0 = sum ln(2 sinh(h(nu_j)/2)), h(nu) — r2 Result 1, C2-C4.
2. (star) identity for ANY rho1, uncentered G1 — r2 C6 (established derivation); exact-algebra tag — review-r2 "Scope of what is established".
3. Centered covariance off by exactly 1/2 m^T A0 m (mean m) — r2 C6 clause (F5) + review-r2 F5 probe (err 1.8e-15 uncentered; centered fails by 1/2 m^T A0 m to 1e-15).
4. Gaussian rho1 -> closed two-covariance functional — r2 C7.
5. "verified algebraically and supported numerically", 18-check battery no failures, Fock anchor on chain-cut ground states — r2 Result 2 + Battery table totals line; wording per dispatch convention.
6. Resolution limit mu=0.01 and N>=12 sampled near-pure sectors excluded, h unresolvable in double precision, fixed-input limit not a failure — r2 Battery "Resolution limit carried honestly" paragraph; required by r2 landing note L293.
7. Two-state anchor discrepancy 3.4e-3..1.45e-2, whole gap on entropy side (3.7e-3, 6.2e-3), quadratic term to 1e-6, tolerance <= 3e-2, proof independent of Fock anchor, named gap G-R with named fix route (clean symbolic two-state anchor cross-checked against the Gaussian closed form of two-Gaussian relative entropy) — r2 Result 4, gap G-R, Decisions Taken item 2 (r2.1).
8. Feeds (i)-(ii) input tier only, does not feed (iii)-(iv), closes nothing, Problem G record unchanged — r2 "Contribution to the missing steps (tiered)", "What this does NOT establish", landing note L294-295; final scoped status sentence per landing note.
9. Citation: none introduced — grep of chapters/ and bib/ for 1512.06431/Jafferis returned zero matches, so per dispatch no citation mechanism exists and the paragraph cites nothing.

F4 compliance: NO QUOTATION USED. The payload quotes no appH "Missing step." text; items (i)-(ii) are referenced by number only. The r2 gloss "and the boundary" appears nowhere in the payload.

Certificate: python -I proposals/111-g-relative-entropy-density/cert-r111p.py (run from repo root; copies tracked tree minus scratch/reports/proposals plus untracked namcg-book7.bbl into scratch/r111p/tree, splices payload with anchor-uniqueness asserts, two pdflatex passes).
Result this pass: PAGES 434 ERRORS 0 UNDEF_CITS 0 UNDEF_REFS 0 MULTIPLY 0 PASS; spliced appH sha1 60a8eb47bb32184d60d0165483a635f9a331c2b3. First attempt FAILed (196 undefined citations) because the untracked .bbl is not in git ls-files; fixed by copying namcg-book7.bbl (the untracked artifact build_check relies on); payload byte-identical both runs (c3d119f6c0).

Reproduction: run the cert command above; expect the same payload sha1 and SUMMARY ... PASS. Gatekeeper must additionally confirm every number above traces to r2/review-r2 (rule 7) and that tier wording in the payload is not above review-r2's "Scope of what is established".
