# Proposal 045-cp12-times-K, round 2

This round answers `review-r1.md` (ACCEPT WITH REQUIRED REVISIONS; MILESTONE none; no BREAKTHROUGH; no PRIOR-CLAIM-ERROR).

**Changes from r1:**
- The r1 block is saved unchanged as `appH_insert_r1.tex` (7691 bytes).
- `appH_insert.tex` is now the r2 block, produced by `apply_r2.py`. That script applies exactly the review's verbatim replacements R1–R8, with R6 in three parts (a), (b), (c).
- Before each replacement the script checked that the old string occurs exactly once; the log is in `apply_r2.out.txt`.
- No other edit was made to the insert.
- No calculation changed, so all r1 scripts and outputs stand.

All sections of `proposal-r1.md` not amended below stand as written.

## Findings and how they were applied

1. **Finding 1 (major, scope: the averaged-frame c_T and c_A = c_T are stated before the reading is qualified).** Applied with R1 and R2.
   - R1: the "Hence ..." sentence now opens "Hence, in this averaged-frame reading, which is not the fibre trace treated below, and in the units c ...".
   - R2: the equality is now stated to inherit the non-derived equality of the Dirac cone value with the Einstein-term coefficient of the index density.
2. **Finding 2 (major, scope: index density carried over from the four-coordinate class).** Applied with R3. The insert now states that the index density is the torsion invariant of the four-coordinate class, evaluated on the frame at the fibre point, and that this identification is carried over and not recomputed for the leaf CP^{1,2}.
   - In the proposal's claim classification, claim 5 (the averaged-frame coefficient −2) and claim 8 (the trace-reading forms) are therefore conditional on this identification, in addition to their r1 classification.
3. **Finding 3 (major, scope: restriction of the no-go).** Applied with R4, R5 and R6(a)–(c).
   - (a) The no-go and the eigenvalues hold with the inert amplitudes set to zero, not eliminated. This is stated in R4 and R6a, and the elimination is added to the not-computed list in R6c.
   - (b) "Covariant" now means "under the Lorentz group of the frozen point". Forms that depend on the background vector y^μ/ℓ are stated as not tested (R5).
   - (c) "vanishes on no traceless polarisation" is replaced by "vanishes on no generalised eigendirection of the traceless polarisations" (R6b).
   - The proposal's hypothesis list gains two entries: inert = 0, and covariance without the background vector.
   - Open avenues 2 (eliminate the inert and higher-harmonic amplitudes) and 3 (test forms depending on y/ℓ) are ranked as in the review.
4. **Finding 4 (minor).**
   - R7 adds "units R = 1" after m = M^{45}.
   - R8 corrects the count to "five wave vectors including two time-like ones": cases 3 and 4 both have q² < 0.
5. **Finding 5 (minor; proposal wording only).** The r1 proposal attributed the trace-polarisation mismatch to the dilaton/conformal direction and to Problem C. That attribution is withdrawn. The corrected wording, which replaces r1 avenue 3, r1 Decisions Taken 3 and the "touches C" dependency note, is:
   - "The sixth polarisation is the trace polarisation of h̄, i.e. the sixth transverse polarisation of the rank-6 response, whose trace merged L2151 notes is not removed by gauge. Its relation to the Problem C scalar is not established."
   - With the cone values, the gap on it is nonzero: 3W_R/8 − 3W_X fixed-state, 3W_R/8 − W_X periodic, W_R/8 − W_X smooth.

   The insert never attributed it and is unchanged on this point.

## Ranked open avenues (r2, following the review)

1. Regime interpolation: derive the loop fibre spectrum and compute the second-order Duhamel weights, together with the first-term fibre-flux (S²–M) part in the same regime.
2. Eliminate the inert and higher-harmonic amplitudes with the tree Maxwell forms in the induced-dominated window.
3. Test forms that depend on the background vector y^μ/ℓ. The target is still an Einstein form.
4. Replica selection and the Λ²/log first-term excess (Problem A).
5. The sixth (trace) polarisation of h̄; its relation to the Problem C scalar is an open question, not an attribution.
6. The subleading symbol and the finite-fibre trace beyond the hybrid treatment.
7. Non-product backgrounds, an explicit K, and the sign of W_R.

## Checks

- **r2 insert bytes** (`apply_r2.out.txt`): 8485 bytes; 0 TAB, 0 CR, 0 non-ASCII, 0 control characters other than LF.
- **Balance:** braces net 0; `\(`/`\)` and `\[`/`\]` balanced.
- **Structure:** one `\paragraph`, no `\label`.
- **Mechanics** (`s5_insert_mechanics.out.txt`):
  - refs `sec:status-B`, `ch:vierbein-emergence` and `ass:lorentzian` are each defined once;
  - cite `Steinacker2023` is present once;
  - the anchor `\section{Problem G: HBEV}` is unique, and the line before it ends with the 044 closing sentence;
  - the title is not duplicated;
  - no process language.
- **Scratch compile of the CURRENT working tree** (`compile_check.out.txt`, outside the repository):
  - baseline 321 pages, with the r2 insert 323 pages;
  - exit codes all 0;
  - 0 undefined references, 0 undefined citations, 0 multiply defined labels;
  - CRLF preserved; scratch removed.

## Insert (r2, authoritative copy `appH_insert.tex`)

Placement as in r1: one paragraph immediately before `\section{Problem G: HBEV}`, after the 044 paragraph, with one blank line before the anchor; the integrator converts it to CRLF.

## Milestone assessment
None. No BREAKTHROUGH, as the review agrees.

## Status-label recommendation
None. B and F remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Author decision needed
None.

## Special instructions for the gatekeeper
- A diff check of `appH_insert.tex` against `appH_insert_r1.tex` should show exactly R1–R8.
- No physics changed.
