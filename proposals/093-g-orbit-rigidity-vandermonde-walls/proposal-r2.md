# Proposal 093-g-orbit-rigidity-vandermonde-walls, round 2

Revision record for review-r1.md (VERDICT: ACCEPT WITH REQUIRED REVISIONS; review file 16,194 B, sha8 66c3922c). No mathematical claim, classification, or manuscript text changed; insert-r1.tex bytes accepted unchanged and untouched.

## Finding 1 (BLOCKING) - addressed
The r1 simulate spliced b[:pos] + insert + b[pos:], whose terminal CRLF leaves a single newline before the line-initial `\emph{Vacuum term.}`, merging the two LaTeX paragraphs against the manuscript-wide blank-line convention. Correction adopted exactly as directed by the gatekeeper: the integration splice is b[:pos] + insert bytes + ONE additional CRLF + b[pos:] at the same unique compound PIN (pos = the cut immediately before the line-initial `\emph{Vacuum term.}`, which follows the 092 tail and its CRLFCRLF). The new simulate script is simulate_apply_093_r3.py (the first corrected draft shipped as simulate_apply_093_r2.py failed only on its own blank-line check-line slice, never on the contract, and was superseded before its first PASS; both r2 files deleted). My run of r3 from the live tree reproduces the gatekeeper-corrected POST exactly: PRE 765,074 B / sha256 b1b62410229383c112d3a50e7c47f0beccdb3835001858d01628b31736b3fd0e / CRLF 3,848 / bareLF 0 (tree unmoved - assertion live, no silent re-pin); compound PIN count 1; gap CRLFCRLF; POST 769,120 B / sha256 5f62af10bbcfc0507c852e127bbad53a6829fce572c97e69f7a9b0e1e0e0d4e3 / CRLF 3,850 / bareLF 0 / noun idiom "close nothing in Problem~G." 19 (was 18) / verb "closes nothing" 1 / `\emph{Vacuum term.}` 2 / new header 1; prefix/suffix identity byte-exact; exactly one blank line between the new paragraph and the Vacuum header; "no write performed". The r1 Expected-POST paragraph (769,118 / 9dba1723... / CRLF 3,849) is superseded and must not be used; the r1 simulate pair is superseded-retained.

## Finding 2 (minor) - recorded, no math change
Confirmed: the s1 third D=4 trial (1,1,1,1,12) yields profile (1,1,1,9), on the triple-coincidence wall where V = 0, so that trial verifies 0 = 0 and does not constrain the constant 288. Effective shipped evidence at D=4: the two generic rational trials (1,3,5,11; W=20) and (2,1,6,21; W=30). Together with the gatekeeper's independent general symbolic D=4 factorization (ratio exactly -1), the constant prod k! = 288 and W-exponent 9 at D=4 are established. The r1 wording "at three rational profiles at D=4" in Result 1 and the claim classification slightly overstates which trials constrain; the accurate reading is "two constraining generic rational trials, the third degenerate on a wall". The insert text itself does not enumerate the trials, so no insert change is required; this paragraph is the corrected evidence record.

## Finding 3 (minor) - recorded, no math change
Confirmed: the s2 print reports branch-resolution booleans ("chain %s, recursion %s, sweep %s"), not which internal branch (symbolic simplify vs 1e-12 quarter-point numeric) was taken; the manifest and r1 special-instruction wording "branch printed" is imprecise. The underlying identity (Gamma recursion chain) is independently verified by the gatekeeper (value 3/2 at a=1 directly), so there is no mathematical impact; recorded here for transparency. No script changed - the shipped s2 .outs remain the record.

## What is unchanged
insert-r1.tex: 4,044 B, sha256 2f7a5320d295c8415c2a17621fa847e7e8758e423b68b9b97eca3dd0ea17b7f1 - bytes untouched since round 1, accepted unchanged by the gatekeeper ("the smallest accurate record"). s1_wall_jacobian_v8.py/.out, s2_integrability_v7.py/.out, hygiene_093.py/.out, simulate_apply_093.py/.out (superseded) all untouched; their shipped .outs remain byte-reproducible (gatekeeper re-ran all four, stdout byte-identical, rc 0). No claim, classification, status, priority, scope or label changed; Problem G stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL, and this package still closes nothing in Problem G.

## Integration contract for the gatekeeper/integrator (round 2)
Single pure insertion at the unique compound PIN; splice appH_bytes[:pos] + insert-r1.tex bytes + CRLF + appH_bytes[pos:]; assert POST per Finding 1 above; then `python scripts/build_check.py` expecting a clean two-pass build (no labels or citations added).

## Milestone assessment
Routine, as in round 1: no M1-M5 trigger; no critical-path step derived; no label change.

## Decisions Taken
- Adopted the gatekeeper's corrected splice contract verbatim (one extra CRLF; do not alter insert bytes).
- Chose to fix the failed blank-line check by regenerating the simulate under a new filename (r3) per the no-edit-WIP rule, deleting the never-passed r2 files, rather than patching r2 in place.
- Recorded findings 2-3 as evidence-wording corrections only; rejected touching insert text or scripts, since neither finding requires a mathematical change.

## Author decision needed
None.

## Remaining open step
Unchanged from round 1: the Missing step items (i)-(iv) of Problem G; selection of profile, group element and state; no closure claimed.
