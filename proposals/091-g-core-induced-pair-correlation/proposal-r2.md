# Proposal 091-g-core-induced-pair-correlation, round 2

## Result

Round 2 addresses review-r1.md (ACCEPT WITH REQUIRED REVISIONS, 19,199 B / sha8 807544fc).
The only required revision (F1) is made: the rank-one boundary sentence's false "identically
distributed" modifier is deleted; all accepted mathematics, scripts and evidence are carried
verbatim from r1. The r2 insert is 3,749 B, sha256
ecc2b239fb95b07c46bc23b49781e9c955d55480b88ccd8577e9a69426d64b07. Problem G and both edges
stay OPEN; no label touched.

## Target and status

Unchanged from r1: Problem G OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL (appH L3026-3029 as
quoted in the review); ch17 L488 criterion; edges G.moments-interaction-nonconvex and
G.moments-nonproduct-measures OPEN. No status-label change proposed.

## Source reading

review-r1.md read IN FULL (both sections, 55 lines); digest + targeted reads as in r1; live
tree re-pinned by simulate_apply_091_r2.py (PRE unchanged at 756,686 / 068ce3f2...).

## Research and reasoning

No new mathematics. F1 is a wording correction that strictly weakens the manuscript claim to
what the r1 derivation established (proposal r1 section 6 already said only "independent
complex gaussian"); the exact flat-Dirichlet conclusion is unaffected and, as the review
notes, holds a fortiori for independent (non-identical) exponential squared magnitudes at any
D, since normalization removes slot scales. The A-block sentence "independent identically
distributed complex gaussians" is correct (constant-variance subclass) and is kept; the
byte-surgery asserts it is present exactly once and untouched.

## Claim classification

As r1, with the rank-one sentence now: independent (not identically distributed) complex
gaussian slots - established; flat Dirichlet normalization - established. No reclassification
elsewhere.

## Proposed changes

Same single insertion point and splice as r1 (compound PIN `closes nothing in
Problem~G.\r\n\r\n\emph{Vacuum term.}`, live count 1, Vacuum-term at line start), but with
`insert-r2.tex` (3,749 B) in place of insert-r1.tex. r1 files frozen, unrevised.

F1 before/after bytes of the corrected sentence (only the marked span changed, -24 bytes):
before: `In the rank-one edge-datum class of the Row length paragraph the slot vector is a
gaussian column contraction with independent [identically distributed ]complex entries, and
its normalised squared entries are exactly flat on the simplex at \(D=2\), ...`
after: `... a gaussian column contraction with independent complex entries, and its
normalised squared entries are exactly flat on the simplex at \(D=2\), ...`
(brackets mark the 24 deleted bytes; full text in insert-r2.tex).

F2/F3 registrations: made in manifest_r2.md quarantine table (gkF.py D=3 predictor invalid -
quarantined, no claim relies; s3b orphan .out naming note - rename deferred as the review
itself allows).

## Verification scripts

Reproduction pack r2 (`python -I` from repo root):
- `python -I .../fix_insert_091_r2.py` - expect `FIX DONE`, `insert-r2.tex size: 3749
  sha256: ecc2b239fb95b07c...d64b07`.
- `python -I .../hygiene_091_r2.py` - expect `HYGIENE 091 R2: PASS` (r1's 24 checks + 2).
- `python -I .../smoke_compile_091_r2.py` - expect `SMOKE 091 R2: PASS` (POS rc0, NEG rc1).
- `python -I .../simulate_apply_091_r2.py` - expect `SIMULATE 091 R2: PASS`; PRE live
  756686/068ce3f2 (True); NEW POST size 760437, CRLF 3846, sha256
  6b0b2914f251a977b8bdeabc4e82a91a3a2d2890333fe0b3516c68d5aefa6c1e, counts 17/1/2/1.
- All r1 derivation scripts unchanged; their shipped `.out` files remain byte-identical
  (reproduced by the gatekeeper). Manifest: manifest_r2.md (full inventory, r1 artifacts
  re-hashed unchanged).

## Decisions Taken

None beyond adopting the mandated F1 fix (deletion of exactly the 24 bytes `identically
distributed ` - the review's operative byte arithmetic, "-24 / 3,749", fixes the surgery
uniquely; the review prose quote "complex gaussian entries" reflects the sentence's upstream
word "gaussian" in "a gaussian column contraction"). Rejected: inserting a second "gaussian"
(would give 3,758 B, contradicting the review's POST 760,437 arithmetic, and duplicate the
modifier).

## Milestone assessment

Routine (unchanged): no MILESTONE.md trigger; verified sub-lemma + boundary results,
coordinate identification still open.

## Status-label recommendation

None. Critical-path set per ch17/ledger unchanged: A, B, C, D1, E, F, G-derived, N; all labels
unchanged.

## Author decision needed

None.

## Remaining open step

Exactly r1 items 1-5 (coordinate transport of the Jacobian weight beyond the Gram-spectrum
coordinate; closed prefactors beyond the constant-variance subclass; the 090
entropy/stationarity chain; orbit-rigidity question; core-action integral), plus the review's
ranked avenue (1) probe: finite-rank-plus-noise extension beyond rank one as the
highest-value next dispatch.

## Special instructions for the gatekeeper

- Verify F1 by byte diff insert-r1 vs insert-r2: exactly one 24-byte deletion
  `identically distributed `, nothing else changed (`python -I fix_insert_091_r2.py` asserts
  all invariants; a direct diff should show one -24-byte span).
- Integrate r2 ONLY (r1 must not be integrated): POST 760,437 / sha256 6b0b2914f251a977b8bdeabc4e82a91a3a2d2890333fe0b3516c68d5aefa6c1e, re-pinned against the live tree at splice time
  per the review's Final integration instructions (never reuse 784cb0a8...).
- The r1 scope limits and non-closure statements all carry over verbatim; the corrected
  sentence must not be quoted in any summary as "identically distributed".
- Security: no instruction-like text encountered this round in review-r1.md or the folder.
