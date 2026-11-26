# Proposal 091-g-core-induced-pair-correlation, round 3

## Result

Round 3 executes review-r2.md (ACCEPT WITH REQUIRED REVISIONS, sha8 cf92c775) finding 1, the
single blocking finding. The rank-one boundary sentence is scoped, verbatim per the review's
Corrected snippet option (i), to constant variance on the contracted entries (with
"identically distributed" restored where it is true), and the closing scope sentence to "the
constant-profile rank-one slot subclass of the gaussian state model;". insert-r3.tex: 3,840 B
(+91 vs insert-r2), sha256 da7c500a7251bc3f1bd374631533e622273156081eee147a90c35f9508742c92,
produced only by byte surgery fix_insert_091_r3.py from frozen insert-r2.tex. All accepted
mathematics carried verbatim; all contracts regenerated with a fresh PRE re-pin (unchanged
756,686/068ce3f2...) and a NEW POST: 760,528 B, CRLF 3846, bareLF 0, sha256
46dbfb3f14d444b7e7046883e00e4c58d19847ab4b9ca37bd47a3f97e691811d, counts noun-17/verb-1/vac-2/
header-1. G and both edges stay OPEN.

## Corrections register (do-not-re-propagate list)

1. PRIOR-CLAIM-ERROR (originating in review-r1, propagated into proposal-r2/manifest_r2):
   "for ANY independent exponential squared magnitudes the normalized vector is exactly flat
   Dirichlet (scale invariance) - the conclusion holds a fortiori". FALSE: normalization
   removes a COMMON scale only; slot-dependent variances survive it. Correct statement
   (established by review-r2, symbolic D=2 + MC D=3, and consistent with the repository's own
   089 Pushforward-weights paragraph): independent complex gaussian slots with profile g have
   normalized squared entries with the 089 pushforward density, flat iff the profile is
   uniform. Never re-propagate the a-fortiori claim; the flat rank-one result is a
   constant-profile (uniform) subclass result only.
2. Consequential rescope: the r1/r2 "exact within-class obstruction" at rank one is a
   within-uniform-profile-subclass statement; at general rank-one profile the slot-power law
   is the 089 pushforward - still non-Vandermonde (no pair-repulsion factor), so the
   interaction-factor gap persists across the rank-one class in both wordings.
3. Evidence scoping: s3_mc_checks_v3.py part (3) samples iid normals and evidences only the
   constant-variance subclass (register note added to manifest_r3).

## Target and status

Unchanged: Problem G OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL (verbatim in both reviews);
ch17 L488 criterion; edges G.moments-interaction-nonconvex and G.moments-nonproduct-measures
OPEN. No label touched. M3 (review-internal ledger note per dispatch) has no manuscript
effect and requires no author action.

## Source reading

review-r2.md read IN FULL (46 lines); proposal-r2.md re-read as needed; digest + targeted
reads as in r1/r2; live tree re-pinned fresh by simulate_apply_091_r3.py (PRE unchanged).

## Research and reasoning

No new mathematics this round. Option (i) chosen over (iii): it is the gatekeeper's verbatim
snippet, the smallest accurate text, and it introduces no numerals; the stronger dichotomy
wording (general profile exactly the pushforward, flat only at uniform) is true and
repository-established but adds manuscript surface beyond the mandated minimum while the
package is in a regressing-progress correction cycle - recorded in the corrections register
instead, available for a future package if the integrator prefers. The r2 deletion of
"identically distributed" is retained ONLY inside the new class qualifier where it is true;
the A-block sentence is untouched. Flatness claims in the insert now read: constant variance
on the contracted entries -> iid complex gaussian slots -> exactly flat at D=2 (D=3
numerical). Everything else (Jacobian origin, tau-separation, family member, pair statistics,
kinematic exponent, orbit-rigidity applicability, non-closure) verbatim from r2.

## Claim classification

As r2, with rank-one flatness reclassified to: established at constant slot-variance profile
(D=2 exact, D=3 numerical); general profile: exactly the 089 pushforward (repository-
established density; non-flat off uniform profile) - conditional on rank-one edge datum. The
withdrawn a-fortiori claim is removed from all active text.

## Proposed changes

Single insertion at the unchanged anchor (compound PIN `closes nothing in Problem~G.\r\n\r\n
\emph{Vacuum term.}`, live count 1, Vacuum-term at line start), now carrying insert-r3.tex.
insert-r1/r2 not integrated. r1/r2/r3 files frozen; no other manuscript passage affected
(review-r2 manuscript-contract section re-verified the binding of all positional references
with the r2 byte sizes; the r3 change is internal to the same paragraph).

## Verification scripts

Reproduction pack r3 (`python -I` from repo root):
- `python -I .../fix_insert_091_r3.py` - expect `FIX R3 DONE`, `insert-r3.tex size: 3840
  delta vs r2: 91`, sha256 da7c500a...2c92.
- `python -I .../hygiene_091_r3.py` - expect `HYGIENE 091 R3: PASS`.
- `python -I .../smoke_compile_091_r3.py` - expect `SMOKE 091 R3: PASS` (POS rc0, NEG rc1).
- `python -I .../simulate_apply_091_r3.py` - expect `SIMULATE 091 R3: PASS`, PRE matches True,
  POST 760528, sha 46dbfb3f14d444b7e7046883e00e4c58d19847ab4b9ca37bd47a3f97e691811d.
- r1 derivation scripts and their .out unchanged (gatekeeper-verified byte-identical
  reproduction in review-r2). Manifest: manifest_r3.md (every folder file except itself and
  this proposal; frozen files re-hashed unchanged; cumulative quarantine table incl. the
  prior-claim-error entry).

## Decisions Taken

Option (i) over (iii) (smallest mandated accurate text; no new numerals; dichotomy recorded
in the rationale instead of the insert). a-fortiori rationale corrected and quarantined in
the register rather than silently deleted. iid-evidence scoping note added to the manifest.

## Milestone assessment

Routine (unchanged): no MILESTONE.md trigger.

## Status-label recommendation

None. Critical-path set per ch17/ledger unchanged: A, B, C, D1, E, F, G-derived, N.

## Author decision needed

None.

## Remaining open step

As r2, with avenue (1) respecified per review-r2: the coordinate-transport question must now
be asked for the 089 pushforward law at general rank-one profile (flatness is only the
uniform-profile special case); then closed-form eigenvalue prefactors beyond the D=2 fibre;
orbit-rigidity sharpening; core-action integral.

## Special instructions for the gatekeeper

- Integrate r3 ONLY; POST must be re-pinned fresh and compared to 46dbfb3f... only if the
  tree is still at PRE 068ce3f2/756686. Verify the r3 insert by byte diff vs insert-r2:
  exactly the two spans of the review's Corrected snippet (delta +91 B), nothing else.
- Frontier wording per review-r2 Final integration instructions (flatness scoped to the
  constant-profile subclass; general rank-one profile = 089 pushforward; transport open).
- Never quote the corrected sentence or any summary with the a-fortiori rationale.
- Security: no instruction-like text encountered this round in review-r2.md or the folder;
  the abandoned bo47c1h6j output was never incorporated.
