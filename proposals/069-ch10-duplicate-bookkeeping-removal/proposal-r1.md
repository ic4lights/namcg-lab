# Proposal 069-ch10-duplicate-bookkeeping-removal, round 1

## Result

The section "Provisional sector bookkeeping (frame/metric sector only)" of
Chapter 10 (`chapters/ch10-lorentz-locking.tex`, lines 331-367, label
`sec:ch10-table`) is a duplicate of Section "Provisional sector bookkeeping"
of Chapter 5 (`chapters/ch05-lorentz-decomposition.tex`, lines 324-360, label
`sec:ch5-count`): the intro paragraph and the whole tabular are
character-identical, and the closing caveat sentence is a near-paraphrase
(exact comparison below). The label `sec:ch10-table` has zero incoming
`\ref` anywhere in the manuscript, so the block is unreferenced dead
duplication. This proposal deletes the Chapter 10 copy and replaces it with
one pointer sentence attached to the paragraph in Section
`sec:ch10-vector` that already discusses the same bookkeeping and already
cites `Section~\ref{sec:ch5-count}`. The replacement keeps the
frame/metric-sector scoping, keeps the "no full-theory mode count follows"
caveat, and refers to `Section~\ref{sec:ch5-count}`. No status, priority or
completion label changes. No mathematical content is added or removed from
the manuscript's claims: every statement in the deleted block already
appears verbatim (or, for the closing caveat, in equivalent form) in the
Chapter 5 block that is kept and referenced.

## Target and status

- This is a bookkeeping/dedup package, not an Appendix H research target. It
  touches no problem's target, evidence or missing step.
- Exact current manuscript passages affected: only
  `chapters/ch10-lorentz-locking.tex`. `chapters/ch05-lorentz-decomposition.tex`
  (the canonical block, lines 324-360) is NOT modified.
- Critical-path status: unchanged. Re-derived from the current sources
  (appH ledger labels and ch17 status lines, digest lines 381-450): the
  critical-path set is A, B, C, D, E, F, G, N (all OPEN, with D/E/F etc.
  PROGRAMME-CONDITIONAL as recorded). None of these is altered by this
  package; the deletion changes no equation, no assumption, no status
  passage, no scope statement. H, I, J remain OPTIONAL within their scopes;
  unchanged.
- DERIVED or PROGRAMME-CONDITIONAL: not applicable (no problem closed,
  narrowed or touched).

## Source reading

Digest + targeted reads. `scratch/digest.md` read first; digest head
`d8585c4...` matches the current branch tip (`git log` top commit
`d8585c4`), and the digest reports `dirty-chapters: no`, so no full-scan
trigger applies; this package changes no definition, assumption, scope
statement or status passage. Files read in full over the relevant ranges:

- `chapters/ch10-lorentz-locking.tex` lines 1-40 (chapter head, learning
  outcomes, intro) and lines 200-389 (sec:ch10-vector through sec:ch10-exercises start);
- `chapters/ch05-lorentz-decomposition.tex` lines 318-387 (the canonical
  bookkeeping section and the exercise that references it);
- `chapters/ch09-ultraviolet.tex` lines 375-392 (the bridge reference to
  `sec:ch5-count`);
- `chapters/ch17-agenda.tex` lines 322-367 (Problem D passage mentioning
  "Chapter~10 generator count" and "frame/metric bookkeeping");
- every `\ref`/`\label` site of `sec:ch10-table`, `sec:ch5-count`,
  `sec:ch10-not`, `sec:ch10-exercises`, `sec:ch10-vector`, `sec:ch10-diffs`
  (whole-repo grep);
- definition sites of `thm:mT` and `ass:gap-psi` (the only cross-references
  inside the deleted tabular): both defined in
  `chapters/ch07-massless-tensor.tex:276` and `:411`, outside the deletion.

Unreadable files: none.

## Research and reasoning

This is a redundancy audit, not a derivation. Everything below was
re-verified from source (not taken on trust from the gatekeeper audit);
the script `verify_dedup.py` (saved with output in this folder) reproduces
every count.

1. **Exact duplication.** With 1-based line numbers in the current files:
   - ch10 heading (line 331): `\section{Provisional sector bookkeeping (frame/metric sector only)}`;
     ch05 heading (line 324): `\section{Provisional sector bookkeeping}` — different wording.
   - Intro paragraph: ch10 334-337 vs ch05 327-330 — character-identical
     (`Component counts in the algebraic split are distinct from on-shell
     polarization counts. ... counted separately.`).
   - Tabular: ch10 339-364 vs ch05 332-357 — character-identical, including
     the internal refs `Assumption~\ref{ass:gap-psi}` and
     `Theorem~\ref{thm:mT}` and the internal hardcoded
     `(Ch.~10)` in the \(F_{\mu\nu}\) row (which stays in the ch05 copy;
     this proposal neither adds nor removes hardcoded chapter numbers).
   - Closing caveat: ch10 366-367 `No total mode count of the full theory
     follows from this bookkeeping; the “2” is a metric-sector target,
     not a full-spectrum result.` vs ch05 359-360 `No full-theory mode count
     follows from this bookkeeping. The final “2” is only a
     metric-sector target.` — NOT character-identical (paraphrase).
   **Discrepancy flag against the briefing:** the audit called the whole
   block "character-identical"; precisely, the intro paragraph and the
   tabular are character-identical while the section headings and the
   closing sentences differ in wording (semantically equivalent caveats).
   This does not change the conclusion; the scoping and caveat content must
   and do survive via the pointer sentence.
2. **Reference audit.** `\ref{sec:ch10-table}`: zero occurrences in all of
   `chapters/` (label site ch10:332 is the only occurrence of the string).
   `\ref{sec:ch5-count}`: three sites — `ch05:379` (exercise), `ch09:386`
   (bridge to Ch. 10), `ch10:229` (sec:ch10-vector paragraph). All three
   point at the kept ch05 section and are unaffected.
3. **Numbering impact.** Deleting the ch10 `\section` shifts only later
   ch10 section numbers (`sec:ch10-not`, `sec:ch10-exercises`). Incoming
   refs: `sec:ch10-not` 0, `sec:ch10-exercises` 0. The one incoming ref to
   an adjacent label, `appH:1113 → \ref{sec:ch10-diffs}`, points to a
   section BEFORE the deletion, so its number is unchanged. No `cleveref`,
   no `autoref`, no literal `Section~10.` hard-coded references exist
   anywhere (scanned). No duplicate labels exist (digest "Duplicate labels:
   none"), so removing `sec:ch10-table` cannot change any resolved number.
4. **Placement of the pointer.** The deleted section sits between
   "Diffeomorphisms" (`sec:ch10-diffs`) and "What locking does not do"
   (`sec:ch10-not`). A headingless paragraph left at that position would
   read as part of the Diffeomorphisms section, which is topically wrong
   (the bookkeeping is not about diffeomorphisms). The paragraph ending at
   ch10:235 already (i) cites `Section~\ref{sec:ch5-count}` at line 229,
   (ii) contains the sentence "This identifies the conditional vector row of
   the provisional sector bookkeeping; it does not establish the dynamics of
   the diagonal connection (Problem~D)." whose phrase "the provisional
   sector bookkeeping" was ambiguous between the ch10 and ch05 tables. After
   deletion the only referent is ch05's, and the proposal makes that
   explicit with the added `of Section~\ref{sec:ch5-count}` and appends the
   pointer sentence. This is the placement that keeps the chapter readable
   and carries all three required elements (scoping, caveat, reference).
5. **Cross-file staleness check.** Grep of "bookkeeping" across
   `chapters/`: the only ch10 occurrences outside the deleted block are the
   learning outcome (line 14-15, see below), the vector paragraph (230,
   233), and the deletion itself. `ch17:345-346` "The Chapter~10 generator
   count identifies six Goldstone orbit variables removable in unitary
   gauge" refers to the broken-generator/Stueckelberg counting in
   `sec:ch10-groups`-`sec:ch10-vector`, not to the deleted table, and
   remains true after the deletion. `ch09:385-386` already routes through
   `sec:ch5-count`. Learning outcome item 4 (ch10:14-15, "state the
   provisional sector bookkeeping through the Goldstone and vector lines")
   is a capability statement that stays satisfiable: the chapter's
   `sec:ch10-vector` paragraph and the explicit pointer to
   `Section~\ref{sec:ch5-count}` still deliver the Goldstone and vector
   lines. It is kept unchanged (minimal-text rule; see Decisions Taken).

## Claim classification

- Intro paragraph and tabular of ch10 334-364 are character-identical to
  ch05 327-357; headings and closing sentences are rewordings: **established
  identity** (byte-level comparison, script saved).
- `sec:ch10-table` has zero incoming `\ref`; `sec:ch5-count` has exactly
  three: **established fact** (whole-repo scan, script saved).
- Section-number shift is invisible to every cross-reference: **established
  fact** (no cleveref/autoref/hardcoded numbers; 0 incoming refs to the
  shifted labels).
- The replacement preserves every caveat of the deleted block:
  **established by direct textual comparison** (frame/metric scoping from
  the deleted heading; "no full-theory mode count" and "not a full-spectrum
  result" carried by the appended sentence, which matches the ch05 caveat
  wording "No full-theory mode count follows from this bookkeeping").
- No status/priority/completion label is touched: **established** (the diff
  contains no status text).

## Proposed changes

One file only: `chapters/ch10-lorentz-locking.tex`. Two edits. CRLF
endings and UTF-8 (no BOM) must be preserved; the replacement text uses no
hard-coded chapter numbers, no process language, and no new macros.

### Edit E1 — attach the pointer to the `sec:ch10-vector` paragraph (replace lines 232-235)

Anchor (occurs exactly once in the file, ch10 lines 232-235):

    gauge field is massless (conditional). This identifies the
    conditional vector row of the provisional sector bookkeeping; it
    does not establish the dynamics of the diagonal connection
    (Problem~D).

What is kept: everything before "This identifies the" in the paragraph, the
clause "it does not establish the dynamics of the diagonal connection
(Problem~D)." and everything after the paragraph. Replaced text (verbatim,
final):

```latex
gauge field is massless (conditional). This identifies the
conditional vector row of the provisional sector bookkeeping of
Section~\ref{sec:ch5-count}; it does not establish the dynamics of
the diagonal connection (Problem~D). That bookkeeping covers the
frame/metric sector only, and no full-theory mode count follows
from it.
```

Labels verified to exist: `sec:ch5-count`
(`chapters/ch05-lorentz-decomposition.tex:325`). No new labels.

### Edit E2 — delete the duplicate section (delete ch10 lines 331-368)

The block to delete is delimited above by the unique heading line and below
by the unique closing line (both verified count 1 in the file):

- line 331: `\section{Provisional sector bookkeeping (frame/metric sector only)}`
- line 332: `\label{sec:ch10-table}`
- lines 334-337: intro paragraph ("Component counts ... counted
  separately.")
- lines 339-364: the `\begin{center} ... \end{tabular} \end{center}` tabular
- lines 366-367: closing caveat ("No total mode count ... not a
  full-spectrum result.")

Delete lines 331-367 together with the blank separator line 368 (or,
equivalently, lines 330-367), so that exactly one blank line separates
"the condensed phase." (line 329, end of `sec:ch10-diffs`) from
`\section{What locking does not do}` (line 369). Nothing else is kept from
the block; the scoping and caveat it carried are preserved by E1.

Stale passages elsewhere: none found that require edits (audit of
"bookkeeping" occurrences and ch17/ch09 passages in Research and reasoning
§5; learning outcome ch10:14-15 and ch17:345-346 remain accurate and are
left unchanged).

No other file is modified. In particular `chapters/ch05-lorentz-decomposition.tex`
lines 324-360 (the canonical section, incl. its hardcoded `(Ch.~10)` inside
the table cell, a pre-existing feature outside this package's scope) are
untouched.

## Verification scripts

Both under this proposal folder; re-runnable with `python -I verify_dedup.py`
from the folder (reads `chapters/` read-only):

- `verify_dedup.py` — checks: (1) intro/tabular character-identity between
  the two blocks and non-identity of headings/closings; (2) zero incoming
  `\ref{sec:ch10-table}`; (3) the three `\ref{sec:ch5-count}` sites;
  (4) anchor-string uniqueness in ch10; (5) zero incoming refs to the
  number-shifted labels, no cleveref/autoref, no `Section~10.` literals;
  (6) CRLF-only, no BOM for both files.
- `verify_output.txt` — saved output of the run (curly quotes render as
  `?` in the console dump; the files themselves are UTF-8).

Post-integration build checklist for the integrator (do NOT run builds in a
proposal round; run after applying):

1. `python scripts/build_check.py` — must report 0 undefined references and
   0 multiply-defined references, and `git diff --check` clean.
2. `grep -rn "sec:ch10-table" chapters/` must return nothing.
3. `grep -rn "ref{sec:ch5-count}" chapters/` must return exactly the three
   sites (ch05 exercise, ch09 bridge, ch10 vector paragraph).

## Decisions Taken

- **Pointer placement:** attached to the `sec:ch10-vector` paragraph
  (ending ch10:235) instead of left as a headingless paragraph where the
  section stood. Reason: that paragraph already discusses the same
  bookkeeping, already cites `sec:ch5-count`, and contains the phrase
  "the provisional sector bookkeeping" whose referent is made explicit by
  E1; a floating paragraph after `sec:ch10-diffs` would attach topically
  to diffeomorphisms. Rejected alternative: standalone one-line section
  (`\section{...}` + one sentence) — keeps a duplicate-heading near-duplicate
  and buys nothing.
- **Canonical copy:** keep the ch05 block (referenced three times), delete
  the ch10 copy (referenced zero times). Rejected: keep ch10 and repoint
  the three refs — that moves the table away from the counting chapter,
  lengthens refs from ch05's own exercises to a later chapter, and would
  also relocate the hardcoded `(Ch.~10)` problem.
- **Learning outcome ch10:14-15:** left unchanged. It states a capability
  ("state the provisional sector bookkeeping through the Goldstone and
  vector lines"), which the chapter still delivers through
  `sec:ch10-vector` plus the explicit `Section~\ref{sec:ch5-count}`
  pointer. Rejected alternative: rewording it — an unnecessary text change
  under the minimal-text rule.
- **Pointer wording:** uses "frame/metric sector only" (carrying the
  deleted ch10 heading's scoping) and "no full-theory mode count follows"
  (matching the ch05 closing's phrasing). The full-spectrum caveat of the
  deleted closing sentence is covered by the same phrase plus the kept
  "No full-spectrum claim follows." row inside the ch05 table.

## Milestone assessment

Routine. No milestone trigger in `MILESTONE.md` applies: this is a
presentation-level dedup with no new derivation and no status change.

## Status-label recommendation

Current critical-path set re-derived from the agenda/ledger (ch17 status
lines and appH ledger labels): A, B, C, D, E, F, G, N — all OPEN,
PROGRAMME-CONDITIONAL as recorded; H, I, J OPTIONAL. This package affects
none of these labels: **unchanged, no recommendation**.

## Author decision needed

None.

## Remaining open step

For this package: none — E1+E2 is complete and applicable as written. The
book's provisional-bookkeeping content remains exactly where it is (the
Chapter 5 section); nothing about any research target is closed. (Note for
a possible future package, not proposed here: the ch05 table cell contains
a hard-coded "(Ch.~10)"; it predates this proposal and is untouched.)

## Special instructions for the gatekeeper

- Scope limit: verify the duplication claim (byte comparison), the
  reference audit, the anchor uniqueness, and that E1's replacement carries
  the scoping + caveat + ref. Re-run `verify_dedup.py`.
- Must not be asserted: that any problem is closed or narrowed; that the
  deleted block was "referenced" (it was not); that the ch05 closing is
  character-identical to the ch10 closing (it is a paraphrase — the
  briefing's "character-identical block" is loose; only intro + tabular are
  byte-identical).
- Re-check: after E2, `sec:ch10-table` must appear nowhere; the three
  `sec:ch5-count` refs must be intact; `appH:1113`'s
  `\ref{sec:ch10-diffs}` must be unaffected (it precedes the deletion);
  no status word (OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL / OPTIONAL)
  occurs in the diff.
