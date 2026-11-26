# Proposal 040-zeeman-vector-mass, round 2

## Result
Revision of r1 after review-r1 (ACCEPT WITH REQUIRED REVISIONS, PRIOR-CLAIM-ERROR). Physics of r1 unchanged: Zeeman-dressed log coefficients (4A - F1 vector, 4A - F1/2 Dirac block, supertrace cancellation), spin-block growth, regulated one-orbit-point Fin data, no restoration of proportionality to A; bounded no-go, Problem F stays OPEN. New in r2: the Fin sign error is corrected IN PLACE in the merged 032 and 034 text (file `merged_edits.md`), with the 032 values verified by an actual rerun of the 032 routine with the corrected sign.

## Target and status
Unchanged from r1: Problem F, OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL (appH sec:status-F; Chapter 17 "CRITICAL PATH; OPEN"). No label affected.

## Source reading
Digest + targeted reads (chapters dirty from 038/039, case 3(d) handled by direct reads): review-r1 in full; appH paragraphs 2235-2293 (supertrace through the 034 block) and the Landau-model paragraph at the line of "Einstein--Hilbert sector in a four-dimensional Landau model"; 032 `s7_resummed_sector_mp.py` and its stored output. Not a full scan.

## Research and reasoning
Finding 1 verification. `s7_corrected_sign.py` is `032/s7_resummed_sector_mp.py` with the single change `tot += -c*mp.log(rho1*PH)` -> `+c*...` (diff in the log of this folder's shell history; the file differs on line 35 only). Rerun, all three (a,b) cases, three frames each (~49 s/frame):
- (0.7,1.3): Fin/c = 1.0507-1.4343i, 1.5762-0.9997i, 0.2726-1.5214i.
- (1.919,1.0): 0.3135+0.0814i, -1.3956-0.1486i, 0.0314+0.0649i.
- (0.4696,1.0) (not quoted in the manuscript): 1.2375-1.4915i, 0.5978-1.6837i, 1.3091-1.5277i.
Each equals the original `s7` value plus 2 ln s1 (s1 = 0.05 e^{-0.6i}/max(a,b)): shifts -6.516-1.2i, -7.295-1.2i, -5.991-1.2i. The Maxwell integrals are bit-identical (c = 0). The gatekeeper's numbers (1.05/1.58/0.27, Im -1.52..-1.00; 0.31/-1.40/0.03, Im -0.15..0.08) are CONFIRMED. The 034 item (iii) numbers (0.63/0.82, 0.49/0.99, 0.011/0.94) are confirmed by `t7_correct_034_forms.py` (0.634/0.815, 0.492/0.994, 0.011/0.943). One wording change relative to the gatekeeper: "varies between frames by an amount of the order of its mean" is replaced by "of the order of, or larger than, its mean", because at (1.92,1.0) the spread (about 1.7) exceeds the mean (-0.35). Other occurrences of the old numbers in the repository: grep of chapters for 7.6, 0.54 and "roughly 20%" shows only the three merged locations; ch17 has no Fin values.

## Claim classification
As in r1, plus: corrected 032 Fin/c values: established numerically (rerun, 9 frames, plus exact additive identity); corrected 034 residuals: established numerically (t7). The orientation dependence of the Landau-model finite remainder is unchanged qualitatively and larger in relative size.

## Proposed changes
1. `merged_edits.md`: three old->new replacements in `chapters/appH-microscopic-proofs.tex` (one in the 034 block item (iii); two in the 032 Landau-model paragraph). Each old string occurs exactly once (Python count, `merged_edits_check.out.txt`: 1, 1, 1). No new labels.
2. `appH_insert.tex` (r2; r1 version kept as `appH_insert_r1.tex`): same anchor (before `\section{Problem G: HBEV}`, occurs once); first four subparagraphs of r1 with the wording edits below; the last subparagraph replaced by the gatekeeper's text, extended by two clauses (definition of the normalised residual; statement that the corrected imaginary part at the strongly electric sample vanishes to quadrature accuracy: before correction Im Q/|A| = 7.6e-3 equals the shift, after correction lambda = 3e-8).
3. Byte check of the r2 insert: 9236 bytes, 0 TAB, 0 CR, 0 non-ASCII, 0 control other than LF; braces balanced, `\(` and `\)` both 157; one `\ref{ch:vierbein-emergence}` (label exists once). Scratch compile outside the repo with the three merged edits AND the insert applied (`compile_check_r2.py`, `.out.txt`): 309 pages, 0 errors, 0 undefined, 0 multiply defined, 0 duplicate labels.

Findings:
- F1 (major): applied: in-place edits (merged_edits.md), rerun verification above, correction subparagraph reduced to the error statement and invariant defects, PRIOR-CLAIM-ERROR for 032 and 034.
- F2 (major): applied: "No ray of the closed fourth quadrant gives..." and "the rays of the first quadrant," added to the final scope sentence.
- F3: applied: "of the tetrad part, real and imaginary parts" (in the replacement text).
- F4: no wording required; the strongly electric entry is reported only as a defect and the clause on quadrature accuracy is added.
- F5: applied: "(iii) for the real and imaginary parts of the forms Fin of T_2, on the quotient by kappa, ...".
- F6: applied: s1 and the normalised residual are defined in the correction subparagraph.

## Verification scripts
r1 list plus: `s7_corrected_sign.py` + `s7_corrected_sign.out.txt` (rerun), `s7_original_sign.out.txt` (copy of the merged 032 output), `merged_edits.md`, `merged_edits_check.out.txt`, `compile_check_r2.py` + `.out.txt`.

## Decisions Taken
- Rerun rather than additive identity for 032 (both agree). 
- Wording "of the order of, or larger than, its mean" replaces the gatekeeper's (spread exceeds mean at the second (a,b)).
- Edit the merged text in place (all inconsistent numbers) rather than append a superseding note.

## Milestone assessment
Routine (bounded no-go plus correction of two merged numerical statements).

## Status-label recommendation
None.

## Author decision needed
none

## Remaining open step
As in r1 (ranked): window average of the full corrected Fin with the shift-invariant defect and the logarithm-free supertrace form; exact u-integration for a regulator-free branch-wise continuation; more orbit points; weight-one terms; the covariance gap (y^mu dependence), which the Zeeman term does not touch.

## Special instructions for the gatekeeper
- Verify merged_edits.md old strings against the file (counts 1,1,1) and that nothing else in chapters quotes the replaced numbers.
- The 032 rerun takes ~25 min (`s7_corrected_sign.py 3`); the additive identity (original + 2 ln s1) reproduces it to the printed digits.
- Do not read the Fin sign data of the Zeeman-dressed forms as anything beyond the one-orbit-point regulated family.
