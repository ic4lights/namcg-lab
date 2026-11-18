# Proposal 080-g-selrule-mixedmult, round 2

Revision round. No new mathematics, no script change beyond the new byte-contract scripts,
no scope change. This note records the revision and the re-issued byte pins.

## Result

Gatekeeper verdict on r1 (review-r1.md L1):
"VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2"
and (Recommended disposition, L47): "On receipt of r2 with these exact corrections and matching
pins, the verdict should be ACCEPT without further mathematical re-review (the corrected clause
is the one I prove in check 6)."
r2 applies exactly the three insert-text corrections F1 (major, false embedded justification in
the D-diagnostic sentence), F2 (major, dropped numeral making a true depth-2 value a false
general claim), F3 (minor, ambiguous positional referent), and re-issues the PRE/POST byte pins
against the unchanged live tree. `insert-r2.tex` is `insert-r1.tex` with exactly three substring
substitutions (applied by `make_insert_r2.py`, which asserts each old string occurs exactly once
and that the byte delta equals the sum of the three string-length differences, +157 total);
no other byte changed. The r1 package's mathematics, scripts, lineage and scope statements are
unchanged and all r1 claims and classifications (rule 6) stand verbatim: the r1 central results
(factorization, per-factor spectrum, realizability, q=2 criterion, moment identities, D/U2
diagnostics, escape of the 076 negation at its exact hypothesis) are untouched by the edits.
The corrected D-sentence justification is the sign-separation argument the gatekeeper proved in
their independent re-derivation check 6, so no unsound lemma is being imported.

## Target and status

Unchanged from round 1. Frontier edge: `G.selrule-mixedmult` (chain 2, reports/graph/frontier.yaml).
Manuscript target: Problem G (appH sec:status-G): Status OPEN, Priority CRITICAL PATH,
Completion PROGRAMME-CONDITIONAL, missing steps (i)-(iv) at appH L3119-3130; Chapter 17
criterion at ch17-agenda.tex L474-495. All PROGRAMME-CONDITIONAL, inside the rank-one
edge-datum family; nothing here is DERIVED and no label is touched (rule 2).

## Source reading

digest + targeted reads. For this round read in full: proposals/080-g-selrule-mixedmult/
review-r1.md (all 61 lines, Findings 1-5 and the Corrected snippet), proposal-r1.md,
insert-r1.tex, manifest.md, simulate_apply_080.py. Live tree re-verified read-only by
`simulate_apply_080_r2.py`: no drift since r1 - appH PRE pins identical (720,144 B,
sha a10eca51...08028012f, CRLF 3824, bare LF 0, anchor unique line-start L3175, header
collision 0 in appH and 0 across all chapters/**/*.tex).

## Research and reasoning

No new derivation. The three substitutions, quoted exactly (old -> new), all inside
`insert-r2.tex` (the only manuscript-bound file):

- F1 (D-diagnostic sentence). Old (count 1, now 0):
  `- for sorted nonzero eigenvalues the multiplicity of each extreme value is strictly below \(q\) at genuine mismatch, so one of its two defining gaps is then strictly positive -`
  New (count 1):
  `- each pair contributes one negative and one positive element, their product being \(-4n_f<0\), so the \(q\) smallest sorted eigenvalues are exactly the lower pair elements and the two defining gaps are the spreads of the lower and upper elements, which vanish together only when all pairs \((h_f,n_f)\) coincide -`
  Why the new clause is correct: for n_f > 0 the factor quadratic lambda^2 + 4 h_f lambda - 4 n_f
  has negative constant term -4 n_f < 0, so its two real roots have opposite signs (one negative,
  one positive); with s such pairs the q = q_1 + ... + q_s smallest sorted eigenvalues are
  exactly the lower (negative) elements and the upper q are the upper (positive) elements, so
  the two defining gaps of D are the spreads of the lower and upper elements, and both vanish
  iff all lower elements coincide iff all pairs (L_f, U_f) coincide iff all (h_f, n_f) coincide
  (injectivity: L + U = -4h, U - L = 4(h^2 + n)^{1/2}). This uses only n_f > 0, already in the
  hypotheses. The old clause was false by the gatekeeper's counterexample (q = 2, pairs
  (0,1), (0.2, 0.6): value -2 with multiplicity exactly q at genuine mismatch); the D-iff
  *headline* it justified is true and is kept.
- F2 (moment sentence). Old: `and \(1\) at equal depths (exact rational arithmetic)` ->
  New: `and \(1\) at equal depths \(2\) (exact rational arithmetic)`.
  The addend 1 of 1 + sum_f (q_f - 1) n_f^p / sum_f n_f^p is the equal-depth value only at
  common depth 2 (at common depth q the excess sum_f(q_f-1)n^p/sum_f n^p = q - 1); the s3
  script checked (2,2) and the integrated 076 sentence states the value at equal depths 2,
  so the numeral is restored.
- F3 (closing scope sentence). Old: `exactly as the two paragraphs above` ->
  New: `exactly as the second and third paragraphs above`. Post-apply, second above = 078
  and third above = 077 (1st = 079), which is the intended pair carrying the typicality and
  general-(H,K)-criterion open items; the nearest-two reading was ambiguous.

## Claim classification

Unchanged from round 1: the full r1 list (proposal-r1.md, "Claim classification") is adopted
verbatim and every r1 claim keeps its r1 classification (rule 6: no r1 claim is weakened or
strengthened by this round). Two clarifications specific to r2:
- The replaced D-sentence justification is a derivation, classified established: for n_f > 0 the
  factor quadratic lambda^2 + 4 h_f lambda - 4 n_f has root product -4 n_f < 0, so each pair has
  one negative and one positive element; ordering then identifies the q smallest eigenvalues with
  the lower pair elements, and the two defining gaps of D are the spreads of the lower and upper
  elements, vanishing together iff all pairs (h_f, n_f) coincide. It uses only n_f > 0, already
  in the class hypotheses. The gatekeeper independently re-derived exactly this argument in
  review-r1 check 6.
- F2 (numeral "2" in the equal-depth moment value) and F3 (positional referent) are corrections
  of wording of claims already classified in r1 (established / exact rational arithmetic); they
  change no classification.

## Proposed changes

File: chapters/appH-microscopic-proofs.tex - one paragraph inserted, nothing else.
`insert-r2.tex` REPLACES `insert-r1.tex` as the manuscript-bound artifact: r1 must NOT be
integrated, and the r1 POST pins (725384 B / sha e6a0335e...) in proposal-r1.md and manifest.md
are lineage-only and void for integration.
- Anchor: the unique line-start passage
  `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023} states that the vacuum energy there`
  (live tree L3175; line-start occurrence count 1, asserted by simulate_apply_080_r2.py). The new
  paragraph lands blank-separated immediately before it, i.e. after the 079 paragraph (L3173),
  following the same stacking convention as paragraphs 072-079.
- Exact text: proposals/080-g-selrule-mixedmult/insert-r2.tex, 5395 B, a single content line with
  terminal CRLF, one \emph header, zero occurrences of $, [, ], \cite, \ref, \label, \eqref, and
  zero occurrences of the words status, priority, completion, open, critical, programme, derived
  (case-insensitive, as substrings) except the closing idiom "... they close nothing in
  Problem~G." (independently re-checked this round, see Verification scripts).
- Kept: every existing line of appH unchanged; no deletions, no rewording. The paragraphs the
  insert refers to positionally (first/second/third above after apply = 079/078/077) are
  physically before the insertion point, so their own positional references are unaffected.
- Stale passages elsewhere: none identified; no other file changes; no bib entries added.
- Byte contract (simulated, read-only; re-run 2026-11-17 against the live tree, pins match):
  PRE appH size 720144, sha256
  a10eca5184d853b8baa0ffac185c67265e6414672e93025dad05a4e08028012f, CRLF 3824, bare LF 0, anchor
  at L3175, headerCount 0. POST: size 725541, sha256
  f8797f82be8d590929388ea9eeb48b1988c4ce164445a2be362c51242df63ea1, CRLF 3826, bare LF 0, anchor
  at L3177, header line at L3175 (post-apply numbering), headerCount 1.

## Verification scripts

All under proposals/080-g-selrule-mixedmult/, run from the repository root with `python -I`,
stdout byte-reproducible. Re-run this round (2026-11-17): every shipped .out reproduced
byte-identically, and insert-r2.tex regenerated sha-stable (a74841c2...) on two consecutive runs.
- `python -I proposals/080-g-selrule-mixedmult/make_insert_r2.py` -> key lines:
  "insert-r2 size=5395 sha256=a74841c2916dc1ed438ec3d46b30129cea688ff0d2f9a41906cf7f34750487ee",
  "size delta=157 (expected 157)", "banned-word count=0 closing-idiom count=1 emph=1
  content-lines=1 terminalCRLF=True". It rebuilds insert-r2.tex from insert-r1.tex by the three
  Corrected-snippet substitutions, asserting each old string occurs exactly once and each new
  string exactly once afterwards, with byte delta exactly 157.
- `python -I proposals/080-g-selrule-mixedmult/simulate_apply_080_r2.py` -> byte-identical to the
  shipped simulate_apply_080_r2.out (367 B): PRE 720144 / sha a10eca51...08028012f / CRLF 3824 /
  bareLF 0 / anchorLine 3175 / headerCount 0; POST 725541 / sha f8797f82...42df63ea1 / CRLF 3826
  / bareLF 0 / anchorLine 3177 / headerLine 3175 / headerCount 1; "OK: no write performed; appH
  unchanged after simulation" (the script re-reads appH and re-checks its sha afterwards).
- r1 lineage scripts, byte-frozen and re-run this round with byte-identical stdout against their
  shipped .out files: s1_spectrum_mixed.py, s2_q2_criterion.py, s3_mixed_moments.py,
  simulate_apply_080.py. The r1 repro pack stands unchanged (expected invariant lines as listed
  in proposal-r1.md, "Verification scripts"); the POST line printed by simulate_apply_080.py
  pertains to insert-r1.tex and is lineage-only, void for integration.

## Decisions Taken

- Adopted the gatekeeper's Corrected-snippet wording (review-r1 L50-54) verbatim for F1/F2/F3,
  because the Recommended disposition pre-commits ACCEPT precisely for "these exact corrections
  and matching pins". Rejected alternatives: rephrasing the F1 sign-separation clause myself
  (needless deviation from the pre-approved text), or deleting the false clause without
  replacement (would drop a genuine derivation the gatekeeper proved in check 6).
- Byte-froze every r1 artifact and put the new contract in new filenames (insert-r2.tex,
  make_insert_r2.py, simulate_apply_080_r2.py/.out), keeping the r1 lineage auditable and making
  it impossible to integrate the void insert-r1.tex by filename collision.
- Generated insert-r2.tex mechanically (make_insert_r2.py, three asserted-unique substitutions +
  delta check) rather than editing by hand, so the exactly-three-substring diff against
  insert-r1.tex holds by construction; independently confirmed this round by full reconstruction
  of insert-r2.tex from insert-r1.tex + the three substitutions (byte-equality check passed).
- r1 RESEARCHER-DECISION items (route; n_f > 0 restriction of the q=2 reduction; fixed-depth
  proviso wording; "block-equalized" header) stand unchanged; no mathematics was altered.

## Milestone assessment

Routine; MILESTONE: none. No critical-path step is closed. The gatekeeper assessed the underlying
result as firing none of MILESTONE.md triggers 1-5 (review-r1, milestone section); this round
changes only three text substrings and re-issues pins.

## Status-label recommendation

Critical-path list derived from ch17-agenda.tex L474-495 and the Appendix H ledger: A, B, C, D1,
E, F, G-derived, N (H, I, J optional within their stated scopes). Affected labels: none. Problem
G remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; no label change is proposed here or made
in any file.

## Author decision needed

None.

## Remaining open step

Unchanged from r1. For the frontier target G.selrule-mixedmult itself: (a) the two-sided +/-
reading of the selection rule is untouched; (b) the double-pair criterion at q > 2 for general
(H, K) beyond the block-scalar subclass is open; (c) a relaxation to K with zero modes (some
n_f = 0) is open as a question but is not a free relaxation here: n_f > 0 does real work both in
the corrected D sign-separation clause (root product -4 n_f < 0) and in the AM-GM step of the
q = 2 criterion, so the n_f = 0 case needs its own case analysis; (d) typicality - whether any
natural state or ensemble yields block-scalar data with unequal blocks at leading semiclassical
order - is unresolved (077 showed iid does not); (e) any statement for depths growing with N is
forbidden by the 076 avenue-(3) fixed-q constraint, which the insert's proviso respects. For
Problem G proper, none of the missing steps (i)-(iv) (appH L3119-3130) is addressed.

## Special instructions for the gatekeeper

Per your Recommended disposition (review-r1 L47), this round should need no mathematical
re-review; verify exactly three things:
1. Three-substring diff: insert-r2.tex = insert-r1.tex with the Corrected-snippet F1/F2/F3
   substitutions, each old string count 1 before and 0 after, each new string count exactly 1
   (make_insert_r2.py asserts this; I also confirmed by full byte-reconstruction this round).
2. Hygiene of the new bytes: 5395 B, single content line + terminal CRLF, ASCII, one \emph, zero
   $ [ ] \cite \ref \label \eqref, zero banned words (status, priority, completion, open,
   critical, programme, derived; case-insensitive substrings), closing idiom exactly once.
3. PRE/POST pins against the live tree via simulate_apply_080_r2.py; if another chain has landed
   in appH since, re-derive rather than trusting the shipped pins.
Do NOT integrate insert-r1.tex (void). Its POST pins (725384 B / e6a0335e...) are lineage-only.
Nothing outside this proposal folder was written; no bib changes; no other manuscript passages
touched.

## Closing statements

Rule 3 (no closure by scope): this round closes, solves, completes or narrows nothing in Problem
G and adds no DERIVED claim; it is the same bounded class-level statement as r1, with three
corrections. Rule 2 (labels): no status, priority or completion label is changed or proposed to
be changed anywhere. The closing idiom "they close nothing in Problem~G." appears exactly once in
insert-r2.tex.
