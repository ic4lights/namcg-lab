# Proposal 106-slug, round 2 — mechanical revision: gatekeeper findings F1/F2 applied byte-exactly

Date 2026-11-21. Branch local/gpu (unchanged, no git write commands run). This round adds
NO new mathematics. It applies the two byte-exact clause fixes F1 and F2 prescribed in
`proposals/106-a-map-matrix-selection-b2/review-r1.md` (verdict ACCEPT WITH REQUIRED
REVISIONS) to the manuscript-bound insert, and retargets the package's verification
scripts from `insert-r1.tex` to `insert-r2.tex`. No status, priority or completion label
touched (rule 2); nothing under `chapters/` or `bib/` edited.

## Result

`insert-r2.tex` (2003 B, sha256/16 74adec3f30063f4a, full sha256
74adec3f30063f4a17d6d668acb929de7e2a02b4a9d7135cb31c545326a60ee3) is produced
PROGRAMMATICALLY from `insert-r1.tex` (1950 B, sha256/16 e10d4960e7777f54, full sha256
e10d4960e7777f54fd642f17c007c6d53c76603726f0d91c564dae402c493afc) by
`r2_106_apply.py`, which parses the two replacement pairs (old1/new1 for F1, old2/new2
for F2) out of the review's ```latex fence at runtime — the gatekeeper's replacement
text is never retyped into any script — asserts each old string occurs exactly once in
`insert-r1.tex` and that the source hash matches, applies both replacements, checks the
result is still exactly one ASCII CRLF-terminated line with both new clauses present
once, and writes the result byte-exactly. Byte-equality with the gatekeeper's byte-staged
candidate `scratch/gk106/insert-r2-candidate.tex` holds: CANDIDATE MATCH: True.

F1 (MAJOR): the FINDING clause's out-of-class reason now reads
"...because it contains \(\partial\theta\,\partial\theta\) channels absent from that
class." (the theta-delta-theta channel removed from the reason, per the integrated 105
ansatz definition which includes theta-partial-theta contraction types).
F2 (REQUIRED): the non-locality sentence now carries the name-level framing clause
"..., the standard coordinate freedom of equivalent star products, ..." before
"so pinning down a single correction within the pointwise freedom requires".
No number, label, status word, citation, or other sentence was changed: the two edits
are exactly the fence-specified old->new pairs (delta −8 B for F1, +61 B for F2,
1950 -> 2003 B).

## Target and status

Problem A, edge A.map (semiclassical construction's selection of the order-Θ² correction
B2), `chapters/appH-microscopic-proofs.tex` sec:status-A. Current status unchanged from
r1 and from the gatekeeper's review: OPEN, CRITICAL PATH (full-GR / matrix-derived
scope), PROGRAMME-CONDITIONAL contribution; closes nothing ("does not close Problem~A."
retained, hygiene-checked). Residual open step unchanged: the actual chart/condensate
selection of a unique B2 (and the 16 kernel dims invisible to embedding 2-jets). No
status-label change proposed.

## Source reading

Digest + targeted reads. At dispatch, `python -I scripts/make_digest.py --check` printed
DIGEST STALE (head changed) (anomaly noted; digest used for navigation only). All
anchors were re-verified against the LIVE tree instead: `chapters/appH-microscopic-proofs.tex`
= 807971 B / sha256/16 53c1c478ae1a79ff / 3872 CRLF, PIN
`b"does not close Problem~A.\r\n\r\n\paragraph{Missing step.}"` count 1 — identical to
the state the gatekeeper's r2 preview was computed against. Read in full:
`review-r1.md`, `proposal-r1.md`, `insert-r1.tex` (bytes), `hygiene_106.py`,
`simulate_apply_106.py`, `manifest_106.py`, `scratch/gk106/insert-r2-candidate.tex`
(bytes), `scratch/gk106/appH_after_106_gk_r2preview.tex` (bytes).

## Research and reasoning

No new research content in r2. The mathematical content and its rule-6 classification
are exactly those of `proposal-r1.md` §3-§5 as independently confirmed by the
gatekeeper's review (its independent sympy re-derivation: CORE A2 = delta-B2 on all 544
rows, rank 160, ker 36/384, P2/P5/P6/P7 at its own rational point). The two corrections
change wording only:
- F1 correctness: the 105 ansatz is built from Theta-Theta AND Theta-partial-Theta
  contraction types (appH, integrated 105 paragraph), so citing theta-partial-theta as
  the omitted channel was false against the manuscript text; the omitted channel that
  the class (linear in partial-theta) cannot produce is the (partial-theta)(partial-theta)
  channel. Out-of-class membership itself is unchanged (model-specific rank jump 5 -> 6
  at the checked points, confirmed by the gatekeeper).
- F2 correctness: the bare non-locality statement is the published equivalence-class /
  gauge-Schwartz-Wolff (star-coordinate) freedom of equivalent star products (scout,
  name-level: Domański-Błaszak arXiv:1305.4026; Bertelson-Cahen-Guediri CQG 14 (1997)
  DOI 10.1088/0264-9381/14/1a/008; Bursztyn-Waldmann arXiv:0909.4259 — NOT
  independently re-fetched by me; marked "not independently verified", same status the
  review gives them). The insert makes no novelty claim; the added clause frames the
  bare fact as an instance of that standard freedom and confines novelty to the
  model-specific counts. No \cite added (separate author decision per review).

## Claim classification

Unchanged from `proposal-r1.md` §4 (established identities at the stated test data;
delta-B2 = A2 ESTABLISHED at 3 points + gatekeeper's point, CONDITIONAL-BY-ARGUMENT
class-wide; "reduces to chart selection" = analysis statement). The F2 framing clause is
a literature-framing statement verified only at name level by the scout — not
independently verified by me; it asserts no new mathematical fact about NAMCG.

## Proposed changes

Manuscript-bound payload: `insert-r2.tex` REPLACES `insert-r1.tex` as the integration
payload. No other manuscript-bound text changes. Integration spec is the gatekeeper's
(review-r1.md "Integration spec"): live `chapters/appH-microscopic-proofs.tex` at
807971 / 53c1c478ae1a79ff / 3872 (re-verified today, unchanged), PIN asserted count 1,
splice payload = head + `\r\n\r\n` + insert-r2.tex bytes + `\r\n` + tail between the
PIN's blank line and `\paragraph{Missing step.}`; expected POST 809976 B / sha256/16
8fa53c956445bb49 / 3874 CRLF — valid ONLY against those live bytes; the integrator must
re-anchor. `insert-r1.tex` is RETAINED in the folder as provenance; `proposal-r1.md` is
left UNTOUCHED (FYI per review F1: the same erroneous out-of-class wording remains in
`proposal-r1.md` §3 P5 — a non-manuscript-bound findings file, not corrected by design).

Package-file changes this round (proposal folder only):
- `hygiene_106.py`, `simulate_apply_106.py`: only the F / INS target-path constants
  retargeted r1 -> r2 (verified by printing the new constants and re-reading the files;
  the F-constant-change lesson from item 105 is honored: every .out self-records the
  checked filename, size and hash).
- `manifest_106.py`: printed hash width 8 -> 16 (record format only).
- Added: `insert-r2.tex`, `hygiene_106_r2.out`, `simulate_apply_106_r2.out`,
  `r2_106_apply.py`, `retarget_106.py` (copies of the scratch drivers), `manifest.md`.
  The r1 evidence files (`insert-r1.tex`, `hygiene_106.out`, `simulate_apply_106.out`,
  `manifest_106.out`) are retained unchanged as provenance.

## Verification scripts

Run from the repo root with `python -I` (all paths repo-root-relative):
1. `python -I proposals/106-a-map-matrix-selection-b2/r2_106_apply.py` — parses the F1/F2
   pairs from `review-r1.md`'s fence, rewrites `insert-r2.tex`, compares to the
   gatekeeper candidate. Expected invariants: insert-r1 sha256/16 e10d4960e7777f54;
   fence parsed old1/new1/old2/new2 = 160/152/127/188 B; insert-r2 2003 B sha256/16
   74adec3f30063f4a; candidate 2003 B sha256/16 74adec3f30063f4a; final line
   `CANDIDATE MATCH: True`; exit 0.
2. `python -I proposals/106-a-map-matrix-selection-b2/retarget_106.py` — idempotence
   note: now that the constants are r2 the asserts on `insert-r1.tex` inside it fail by
   design (guard against double application); run once per retarget only. Its printed
   new constants are recorded here.
3. `python -I proposals/106-a-map-matrix-selection-b2/hygiene_106.py > proposals/106-a-map-matrix-selection-b2/hygiene_106_r2.out`
   — expected self-record: `checked insert: ...\insert-r2.tex 2003 bytes, sha256/16
   74adec3f30063f4a`; macros `['\Theta','\delta','\le','\paragraph','\partial','\tfrac','\theta']`;
   `appH size 807971 sha256/8 53c1c478 CRLF 3872 PIN count 1`; `HYGIENE: PASS`; exit 0.
   Observed (hygiene_106_r2.out): exactly that.
4. `python -I proposals/106-a-map-matrix-selection-b2/simulate_apply_106.py > proposals/106-a-map-matrix-selection-b2/simulate_apply_106_r2.out`
   — SIMULATION into `scratch/sim/` only; `chapters/` never written. Expected self-record
   (observed in simulate_apply_106_r2.out): BEFORE 807971 / 53c1c478ae1a79ff / 3872;
   PIN occurrences 1; AFTER(simulated) 809976 / sha256/16 8fa53c956445bb49 / 3874; live
   appH untouched 53c1c478ae1a79ff.
5. Preview equality (one-off, run in this round): `scratch/sim/appH_after_106.tex` is
   BYTE-EQUAL to `scratch/gk106/appH_after_106_gk_r2preview.tex` (both 809976 B /
   sha256/16 8fa53c956445bb49 / 3874 CRLF) — PREVIEW BYTE-EQUAL: True.
6. `python -I proposals/106-a-map-matrix-selection-b2/manifest_106.py > proposals/106-a-map-matrix-selection-b2/manifest.md`
   — lists every folder file (size, sha256/16; manifest.md itself excluded) plus live
   appH 807971 / 53c1c478ae1a79ff / 3872.

## Decisions Taken

- Applied both fixes verbatim from the fence (never retyped), per review; rejected
  authoring my own paraphrase of the gatekeeper's clauses.
- Kept r1 evidence files under their r1 names and added r2-named .out files, so no r1
  evidence is silently reused and nothing overwrote r1 records.
- Bumped manifest hash width to 16 (record format; no content effect) so the manifest
  meets the r2 recording spec.
- Recorded the DIGEST STALE condition and re-verified anchors live instead of relying on
  the digest; did not run `make_digest.py` (single-writer rule for digests).
- `scratch/` driver scripts copied into the proposal folder for durability (scratch is
  git-ignored).

## Milestone assessment

Routine. No milestone trigger; the r1 mathematics and its non-closure stand unchanged;
this round only makes the manuscript-bound payload match the gatekeeper-accepted wording.

## Status-label recommendation

Current critical-path list re-derived from Chapter 17 / Appendix H via the gatekeeper
r1 review and the live sec:status-A passage: A, B, C, D1, E, F, G-derived, N (OPEN; H,
I, J optional within their scopes). A remains OPEN, CRITICAL PATH. No label changes
proposed or made.

## Author decision needed

None new. (Unchanged from r1/review: any \cite for the equivalence-class framing would
be a separate author decision; none added.)

## Remaining open step

Unchanged: the chart/condensate selection of a unique B2 from the matrix-model dynamics
within (H1)-(H3) (and identifying the data source that sees the 16 kernel dimensions
invisible to embedding 2-jets); D > 4, non-Abelian, Θ³+ outside scope as stated.

## Special instructions for the gatekeeper

- Verify `insert-r2.tex` byte-equals `scratch/gk106/insert-r2-candidate.tex`
  (2003 B / sha256/16 74adec3f30063f4a) — re-run r2_106_apply.py (invariants above).
- Verify the two changes vs insert-r1.tex are EXACTLY the review's fence pairs
  (byte-diff or re-run the apply script's parse) and that no other byte changed.
- This round originates no mathematics; r1's rule-6 classification and its
  MUST-NOT-assert list carry over unchanged: no closure of Problem A; no derivation of
  ass:dictionary / half-sided inclusion; no 1-jet-locality or universality; no
  non-emergence of spacetime; no claims beyond (H1)-(H3); no D>4 / non-Abelian / Θ³+
  content. F1's corrected clause must be asserted only as "the (partial-theta)(partial-theta)
  channel is absent from the 105 class" (model-specific out-of-class membership), and
  F2's clause only as name-level framing (the cited sources were not independently
  re-fetched by me or by the r1 reviewer).
- Integration must use `insert-r2.tex`; the POST triple 809976 / 8fa53c956445bb49 / 3874
  is valid only if live appH is still 807971 / 53c1c478ae1a79ff / 3872 — re-anchor.
- Live `chapters/` was not touched by this round (simulation output went to scratch/sim/
  only; post-simulation live hash re-printed unchanged).
