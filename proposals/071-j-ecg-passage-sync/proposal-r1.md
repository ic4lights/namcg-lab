# Proposal 071-j-ecg-passage-sync, round 1

## Result

This package syncs the two manuscript passages that still present the Problem J reduced
Euler--Lagrange identities as validated, to the already-accepted 068 reduction-consistency
audit (integrated 2026-11-15, appH `sec:status-J`, review-r3.md ACCEPT | none | none, binding on
scope). It introduces no new mathematics and closes nothing: it replaces the stale claims
(1) ch17-agenda.tex L602-604 "Section~\ref{sec:status-J} records checked reduced
Euler--Lagrange identities, the resulting first integral including" and
(2) ch09-ultraviolet.tex L234-239 "the Euler--Lagrange equations have been checked
symbolically: \(N=1\) is a consistent vacuum branch and the lapse equation yields the displayed
first integral ... This check uses the static spherical reduction;"
with the smallest text that accurately records, at both passages, the bounded 068 outcome: under
the literal bivector-map index reading of \eqref{eq:ECG} plus the displayed \((N,f)\) reduction,
a symbolic re-evaluation of the same reduced action does NOT reproduce the recorded identities,
\(N=1\) is not an exact consistent truncation for a general profile on that reading, while the
recorded first-integral arithmetic of the displayed one-dimensional system (including
\(\Lambda_{\mathrm{eff}}\)) is internally consistent. The existing symmetric-criticality hedge is
kept verbatim at both sites. No label, priority or completion-classification text is inside any
anchor or replacement; the ch17 status sentence (L597 "OPEN; OPTIONAL research within the stated
model scope.") and the appH ledger block are byte-unchanged (appH is not touched at all).

## Target and status

- Target: frontier edge `J.ecg-sync` (reports/graph/frontier.yaml chain 1, rank 1): "ledger
  2026-11-15 gatekeeper-endorsed plan: ch17-agenda.tex L602-605 is an ACTIVE stale passage (HIGH
  priority, next targeted round; made stale by E1/E1b/E3 landing) and ch09 L234-238 pre-existing
  stale - both recorded as the next small targeted package (stale ECG passage sync)".
- Problem J, current status (appH L3431-3434, verbatim, untouched): "Status: OPEN. Priority:
  OPTIONAL within the stated ECG model. Completion: PROGRAMME-CONDITIONAL. The reduced results
  do not derive singularity resolution from the matrix theory." ch17 L596-597 (untouched):
  "\paragraph{Problem J: spherical ECG solutions.} \emph{OPEN; OPTIONAL research within the
  stated model scope.}" Consistent between the two sources; no discrepancy to flag.
- Dependencies: none new. This package carries only content already accepted in 068 (r3 ACCEPT),
  i.e. the appH audit block at appH L3510-3547 and the updated Status paragraph L3577-3590.
- DERIVED or PROGRAMME-CONDITIONAL: unchanged, PROGRAMME-CONDITIONAL. Nothing is derived or
  closed here; the package is a truth-sync of two stale passages to a bounded accepted result.

## Source reading

digest + targeted reads (full scan not performed and not claimed; no 3(a)-3(d) trigger: no
definition, assumption, scope statement or status passage is edited - the edits are evidentiary
wording inside an agenda item and inside an enumerate item, and the status sentences are outside
every anchor). Digest state: `scratch/digest.md` read IN FULL (head f7c7b034, tree-hash
f8142847baea9aa0, `dirty-chapters: yes` = the accepted 068 integration awaiting author commit;
the two target files are listed as UNCHANGED with hashes 73e7dc112186 (ch17) and 9d1d831f6281
(ch09), both matching my measured live hashes below). Read IN FULL this round:
`reports/graph/frontier.yaml`; `proposals/068-j-spherical-reduction-consistency/review-r3.md`
(esp. "Scope of what is established", "Recommended disposition" steps 1-7);
`chapters/appH-microscopic-proofs.tex` L3429-3591 (current accepted Problem J section incl. the
+39-line audit block at L3510-3547); `chapters/ch17-agenda.tex` L580-624;
`chapters/ch09-ultraviolet.tex` L195-293; `reports/ledger.md` tail (068 integration entry,
2026-11-15, incl. the "FOR THE LOOP" instruction for this package; 066/069/070 for house style);
`reports/sme-scout-20261114-0154.md` skimmed for J/ECG leads - none exists, and this package
needs no new literature (no citation is added or removed). No unreadable files.

## Research and reasoning

**What 068 established (bounded).** Under the literal bivector-map reading of \eqref{eq:ECG}
(ch09 L213-217, coefficients 12, 1, -12, +8) plus the displayed \((N,f)\) reduced action
\(L[N,f]=Nr^2(R-2\Lambda_{\mathrm{eff}}+\kappa\mathcal P)\), appH L3510-3547 (accepted):
(i) \(\left.\mathcal E_f\right|_{N=1}\) vanishes identically for \(\kappa=0\) but not for
\(\kappa\ne0\) - on this reading \(N=1\) is not an exact consistent truncation for a general
profile, while on the slice \(f=1-kr^2\) it vanishes for every \(k\);
(ii) the displayed identity for \(\left.\mathcal E_N\right|_{N=1}\) is not reproduced: already at
\(\kappa=\Lambda_{\mathrm{eff}}=0\) the reduced operator is \(2-2f-4rf'-r^2f''\), differing from
\(\mathrm d[2r(1-f)]/\mathrm dr\) by \(-\mathrm d[r^2f']/\mathrm dr\), and the residual is not a
total \(\mathrm d/\mathrm dr\) of any local functional of \(f\) (Helmholtz criterion), for any
overall normalisation of \(\mathcal P\);
(iii) the displayed first-integral passage is internally consistent (\(\mathcal B[1-kr^2] =
(16/3)k^3r^3\) reproduces the recorded \(k-8\alpha k^3=\Lambda_{\mathrm{eff}}/3\) and the recorded
tail coefficients); the slice \(N=1\), \(f=1-kr^2\) is not constant curvature there
(Ric\({}_{\theta\theta}-(R/4)g_{\theta\theta}=kr^2/2\)); on it \(R=6k\) and the invariant is
\(216k^3\), against the recorded \(48\kappa k^3\), while on the constant-curvature slice
\(N=\sqrt{1-kr^2}\) the invariant is \(192k^3\);
(iv) not established: whether the intended density differs from \eqref{eq:ECG} as written, or
whether a different static-spherical parametrisation was used.

**Why the two passages are stale.** Both assert, without the 068 qualification, that the reduced
equations "have been checked" and that "\(N=1\) is a consistent vacuum branch":
- ch17 L603 "records checked reduced Euler--Lagrange identities" - actively stale: made false as
  stated by the 068 edits E1/E1b/E3 (the identities are now recorded together with the finding
  that they are not reproduced under the literal reading).
- ch09 L235-238 "have been checked symbolically: \(N=1\) is a consistent vacuum branch and the
  lapse equation yields the displayed first integral ... This check uses the static spherical
  reduction;" - the first clause is contradicted (on the literal reading \(N=1\) is not an exact
  consistent truncation for a general profile, and the recorded \(\mathcal E_N\) identity is not
  reproduced); the first-integral clause survives only as a statement of the displayed
  one-dimensional system, and "This check" no longer refers to anything that passed.

**The sync text.** Each replacement states exactly the accepted bounded outcome, with the reading
hedge ("under the literal bivector-map index reading of \eqref{eq:ECG}") so that neither passage
asserts a book-wide error or settles the density question, and re-attributes the surviving
first-integral/regular-centre/MS-relation/tail list to "the displayed one-dimensional system",
matching the accepted appH Status sentence (L3577-3582 "... are internally consistent for the
displayed one-dimensional system, and a symbolic re-evaluation ... does not reproduce them.").
The ch17 replacement keeps the sentence's second half (first integral including
\(\Lambda_{\mathrm{eff}}\), conditional regular-centre constraint, maximally symmetric curvature
relation, large-radius tail) and the existing hedge sentence L607-610 verbatim; the ch09
replacement keeps the symmetric-criticality hedge, the reduced-coupling sentence and the whole
regular-core-profile discussion verbatim. No new cross-references are added: both passages
already carry `\ref{sec:status-J}` (verified unique, appH L3429) and ch09 already sits at the
definition of `\eqref{eq:ECG}` (L213) with `\eqref{eq:S-ECG}` (L222); the digest label index
confirms no duplicates, so the optional one-line forward pointer is not needed.

**What must NOT be asserted (preserved from review-r3 "Must-NOT-be-asserted boundaries").** No
book error beyond the literal reading + \((N,f)\) reduction; no closure or narrowing of Problem J;
nothing load-bearing from 068 stage2; the density question (intended density vs \eqref{eq:ECG} as
written) stays open. Neither replacement asserts any of these.

## Claim classification

- The two OLD passages misstate the current record: established (byte-verified quotes below vs
  the accepted appH audit).
- The sync content (identities not reproduced under the literal bivector-map reading; \(N=1\) not
  an exact consistent truncation for a general profile; first-integral arithmetic internally
  consistent for the displayed 1D system): established, as accepted bounded derivations of 068
  (r1/r2/r3 gatekeeper re-derivations + CAS; carried here by chain of custody from the integrated
  appH text, which this package quotes and does not re-derive).
- Reading hedge (bounded to the literal bivector-map reading; density question open): input
  scoping inherited from 068, restated verbatim in spirit.
- No new mathematical claim is made in this package.

## Proposed changes

Two files, one edit each. The binding contract is the byte sequence in
`proposals/071-j-ecg-passage-sync/simulate_apply.py` (CRLF bytes); the fenced blocks below render
the same text with the line breaks shown explicitly. No other file is touched; appH, bib, ledger
are collateral.

### File 1: `chapters/ch17-agenda.tex` (E1)

PRE pin (current working tree): **39,519 bytes, sha256
`73e7dc11218677d164dd3766f91fbdcbacab339fd77d116c9cff760e69612de8`, CRLF 790, bare-LF 0**.

Anchor: starts at the beginning of L602 ("the action~...") and ends at the end of L604 with the word "including"; the CRLF ending original L604 and all of
L605-617 are OUTSIDE the anchor and are kept verbatim. The OLD fragment is exactly original lines
602+603+604 joined by 2 CRLF (148 B, 2 CRLF). Count in file: 1 (verified; the string "checked
reduced Euler--Lagrange" occurs nowhere else in `chapters/`).

OLD (byte-exact, 3 lines, 2 CRLF):

```latex
the action~\eqref{eq:S-ECG}, Section~\ref{sec:status-J} records
checked reduced Euler--Lagrange
identities, the resulting first integral including
```

NEW (392 B, 5 CRLF; replaces the 3 lines with 6; the untouched continuation line
`\(\Lambda_{\mathrm{eff}}\), its conditional regular-centre constraint` follows unchanged):

```latex
the action~\eqref{eq:S-ECG}, Section~\ref{sec:status-J} records the
reduced Euler--Lagrange identities together with the audit finding
that, under the literal bivector-map index reading of \eqref{eq:ECG},
a symbolic re-evaluation of the same reduced action does not
reproduce them; the section also records the resulting first integral
of that displayed one-dimensional system, including
```

Kept verbatim: L596-601 (paragraph header, status sentence, singularity-resolution sentence,
"For the explicit invariant~\(\mathcal P\) in~\eqref{eq:ECG}, used in"), L605-617 (first-integral
list continuation, the conditional hedge "These results are conditional on the static spherical
reduction capturing the full field equations; that symmetric-criticality step is not established
here.", the cited-spectrum sentence, and the "Problem~J remains open: ..." list). Delta +244 B,
+3 CRLF (790 -> 793); file 39,519 -> 39,763 B; POST sha256
`20ba622bd27e9c250f6422eb11fdc6052c2b0fcfc2f7be292761c007f9b66621`.

### File 2: `chapters/ch09-ultraviolet.tex` (E2)

PRE pin (current working tree): **16,338 bytes, sha256
`9d1d831f62816753f5d56032be9a5bdfa927a40e14b0334113f70abbd616292e`, CRLF 391, bare-LF 0**.

Anchor: exactly original lines 234-238 (full) plus the beginning of L239 through
"spherical reduction;" (352 B, 5 CRLF). Count in file: 1 (verified; "have been checked
symbolically" occurs nowhere else in `chapters/`). The remainder of original L239 ("
its relation to the unrestricted field") and everything after are OUTSIDE the anchor and kept
verbatim.

OLD (byte-exact; the 8-space continuation indentation is part of the bytes):

```latex
  \item For the reduced action in Section~\ref{sec:status-J}, the
        Euler--Lagrange equations have been checked symbolically:
        \(N=1\) is a consistent vacuum branch and the lapse equation
        yields the displayed first integral, including
        \(\Lambda_{\mathrm{eff}}\). This check uses the static
        spherical reduction;
```

NEW (552 B, 8 CRLF; replaces with 8 lines; the untouched remainder "
its relation to the unrestricted field" continues the new last line):

```latex
  \item For the reduced action in Section~\ref{sec:status-J}, a
        symbolic re-evaluation under the literal bivector-map index
        reading of \eqref{eq:ECG} does not reproduce the recorded
        Euler--Lagrange identities: on that reading \(N=1\) is not
        an exact consistent truncation for a general profile, while
        the displayed one-dimensional system has the recorded first
        integral, including
        \(\Lambda_{\mathrm{eff}}\), internally consistent. This reduction uses
        the static spherical ansatz;
```

Kept verbatim: the enumerate item's remainder (symmetric-criticality hedge, "The reduced coupling
is \(\alpha=-16\pi G_{\mathrm{eff}}\beta_{\mathrm{ECG}}\).", the regular-core profile
`eq:fr-ECG` and its residual sentence), items 2-3, `ass:ECG`, and the `eq:ECG`/`eq:S-ECG`
display equations themselves (L211-229 untouched - the density is NOT amended here; that is
edge `J.density`). Delta +200 B, +3 CRLF (391 -> 394); file 16,338 -> 16,538 B; POST sha256
`dfd116e68012821d3bde045d73819ffcf06485ad54ac3c38b24e6a83161b9213`.

Byte arithmetic check: (+244)+(+200) = +444, matching the script's total delta.

### Stale-passage check elsewhere

Grep of `chapters/` for "checked symbolically" and "checked reduced": the only hits bearing on
the Problem J reduced identities are the two anchors themselves (ch09 L235, ch17 L603), each the
sole hit of its string in its file. The three remaining "checked symbolically" hits (appH L308,
L2766, L2860) concern the Problem B cone-coefficient and Problem F operator identities, not the
Problem J identities, and are untouched by this package. The words "consistent vacuum branch" occur
only at ch09 L236 (inside E2). No other passage presents the Problem J identities as validated:
the appH Problem J section is the 068-updated text, and ch13 (regular-core profile usage) defers
to `eq:fr-ECG`/`ass:ECG` wording, which this package does not touch.

## Verification scripts

Folder: `proposals/071-j-ecg-passage-sync/`

- `simulate_apply.py` (4,022 B, sha256
  `636d624f1e88041bfdde74766bb3bbe917d21d0db0e439fbce0e670f356ae467`): read-only simulator. For
  each file: prints PRE bytes/sha256/CRLF/bare-LF, asserts anchor count == 1, applies the
  replacement in memory, asserts the post-anchor continuation sentence survives with unchanged
  occurrence count, prints POST bytes/sha256/CRLF/bare-LF. Writes nothing. Exits 0 iff all
  asserts hold.
- `simulate_apply.out` (674 B, sha256
  `ffcfe00ff9baf01915d52f2947985b07749697f77d3b93d6885d72f86c07102e`): captured stdout.

Reproduction pack (run from the repo root):

```
python -I proposals/071-j-ecg-passage-sync/simulate_apply.py
```

Expected invariant output (byte-identical stdout on re-run - verified):

```
PRE   chapters\ch17-agenda.tex
PRE  : bytes 39519 sha256 73e7dc11218677d164dd3766f91fbdcbacab339fd77d116c9cff760e69612de8 CRLF 790 bareLF 0
anchor count: 1 (must be 1)
POST  chapters\ch17-agenda.tex
POST : bytes 39763 sha256 20ba622bd27e9c250f6422eb11fdc6052c2b0fcfc2f7be292761c007f9b66621 CRLF 793 bareLF 0
PRE   chapters\ch09-ultraviolet.tex
PRE  : bytes 16338 sha256 9d1d831f62816753f5d56032be9a5bdfa927a40e14b0334113f70abbd616292e CRLF 391 bareLF 0
anchor count: 1 (must be 1)
POST  chapters\ch09-ultraviolet.tex
POST : bytes 16538 sha256 dfd116e68012821d3bde045d73819ffcf06485ad54ac3c38b24e6a83161b9213 CRLF 394 bareLF 0
total byte delta: 444
SIMULATION OK
```

If the tree moved (e.g. the author commits and reflows nothing - a plain commit does not change
file bytes, so PRE pins should survive; any actual file change will trip the anchor or PRE-pin
asserts), STOP and re-pin.

## Anchor line numbers in the current tree

- `chapters/ch17-agenda.tex`: OLD spans L602-L604 (inclusive, whole lines); the replaced text
  ends at "including" at the end of L604; continuation `\(\Lambda_{\mathrm{eff}}\), its
  conditional regular-centre constraint` at L605 is kept. Section context: Problem J item L596-617.
- `chapters/ch09-ultraviolet.tex`: OLD spans L234-L239 (through "spherical reduction;" mid-L239);
  enumerate item starts L233; `eq:ECG` L211-218; `eq:S-ECG` L221-229; the kept remainder of L239
  (" its relation to the unrestricted field") continues the final NEW line.

## Decisions Taken

- Anchor granularity: chose minimal byte spans that keep each replacement grammatically closed and
  leave every hedge sentence byte-unchanged outside the anchors, rather than rewriting whole
  paragraphs (rejected: wider rewrites enlarge the diff and risk re-touching status-adjacent text).
- Wording "together with the audit finding" (ch17): chosen because the appH section itself now
  contains a paragraph titled "Reduction-consistency audit of the displayed identities", so the
  word names an existing manuscript object; rejected "disproved" / "shown to be wrong" as
  overstepping the bounded reading.
- ch09: kept the item's surviving claims (first integral with \(\Lambda_{\mathrm{eff}}\),
  symmetric-criticality hedge) and changed "This check uses the static spherical reduction" to
  "This reduction uses the static spherical ansatz" because no check passed; the referent of the
  hedge must be the reduction, not a defunct check. Rejected deleting the sentence (weaker hedge).
- Did not add a new forward-pointer line: both passages already carry an explicit
  `Section~\ref{sec:status-J}` reference, so the allowed extra pointer would be redundant.
- Read-only simulator (no in-tree patched copies, no build in-tree), matching the 068 house style.

## Milestone assessment

Routine. No milestone trigger: this records an accepted bounded result at two stale passages; no
critical-path step is derived and no missing link is closed.

## Status-label recommendation

Derived from ch17 (criterion section) + appH + ledger: the current critical-path set is A, B, C,
D1, E, F, G-derived, N (H, I, J OPTIONAL within stated scopes). Affected labels for this package:
**none, unchanged.** Problem J stays OPEN / OPTIONAL within the stated ECG model /
PROGRAMME-CONDITIONAL in both appH and ch17; no LABEL-CHANGE-PROPOSED content is included.

## Author decision needed

None.

## Remaining open step

After integration, the Problem J edges stay open as ranked in frontier.yaml: (1) `J.density` -
settle whether the intended density differs from \eqref{eq:ECG} as written or a different
static-spherical parametrisation was used (the slot-shifted reading is a cheap within-core test,
appH L3514-3516); (2) `J.rederive` - re-derive the MS branch / tail / rational profile /
regular-centre obstruction from the corrected operators (gated on 1); (3) `J.symcrit` -
symmetric-criticality justification for the written density; (4) `J.stage2` - complete the 068
stage2 computation. None of these is touched here.

## Special instructions for the gatekeeper

1. Scope limits: this package must be checked for (a) byte-exactness of anchors/replacements and
   the PRE/POST pins, (b) that no asserted sentence exceeds the 068 bounded scope (literal
   bivector-map reading + displayed \((N,f)\) reduction), (c) that the status sentences and the
   appH file are untouched, (d) anchor uniqueness in the live tree. The mathematics inside the
   replacement text is a restatement of 068 content already accepted by review-r3 (which
   re-derived it independently, including its own numeric contraction test); re-checking the CAS
   is not required - re-check instead that the two replacement sentences faithfully paraphrase the
   accepted appH audit wording at L3510-3547 and L3577-3582 without strengthening it.
2. Must NOT be asserted after integration: a book-wide error; closure or narrowing of Problem J;
   resolution of the density question; that the audit applies under any reading other than the
   literal bivector-map one.
3. Re-run `python -I proposals/071-j-ecg-passage-sync/simulate_apply.py` from the repo root before
   applying; gate on the PRE pins; then build (`python scripts/build_check.py`) - the two edits
   add no labels and no citations, so no undefined-reference risk beyond the existing
   `\eqref{eq:ECG}` usage already present in ch17 L601.
4. Digest is dirty (accepted 068 integration, appH only, uncommitted); ch17 and ch09 hashes match
   the digest's "unchanged" rows exactly, so no re-pin against appH churn is involved.
