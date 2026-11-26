# Proposal 053-lorentzian-integral-limit-order, round 3

Mechanical revision round. No new derivation is presented or requested; the gatekeeper's
review-r2 ("Recommended disposition": "Round 3 needs only a byte check against the hashes
below and the record updates. No new derivation is requested.") is followed literally.

## Result

The Result section of proposal-r2.md stands unchanged and is kept by reference; it is not
re-derived or rewritten here. In one line: at finite N, in the limit eps -> 0+ taken first,
for polynomial observables of degree k < 14, the regulated Lorentzian matrix integral
equals the Euclidean one up to phases — proved at N = 2, conditional for N >= 3 (extension
of the Austing-Wheater proof, and Z_E != 0 for ratios); the fixed-eps contour identity
holds for u < 2/3 at any N with no absolute integrability on R_1; Definition (C) equality
is proved at N = 2, gamma <= 0, for invariant observables with the convergence factor
removed last. **Proved: N = 2. Conditional: N >= 3. Untreated: fixed gamma > 0, N -> infinity
first. Problem E remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; no label is touched and
no signature is derived.** The only content change since r2 is the gatekeeper's own
replacement S7 (its review-r2, "Corrected snippet"), applied to the insert as instructed;
it changes the wording of the Definition (C) identification only, adds no mathematics and
no assumption.

## Round 3 changes

1. **S7 applied to `appH_insert.tex` only**, by `apply_s7_r3.py`, which parses the S7
   Old/New strings from `review-r2.md`, verifies their sha256
   (old `5c217b675886d1ff5cd0a1f81b14d8308e61fde336bbea8c14c246ac49d6ec76`, 195 B;
   new `4dd695f93cada41514bb4c086d142717da4d1f8e8061e62401370f9f7c6aef2c`, 316 B),
   refuses unless `appH_insert.r2.tex` is the recorded r2 bytes (10645,
   `5d0d4538...3aef`) and refuses a second run. Net +121 bytes (316 - 195).
   The insert is now byte-identical to the gatekeeper's expected object:
   LF 10766 B `e5562f7670046d486f9855703190b04d78a08994aee9f661b124f930f6d15009`,
   CRLF 10783 B `bab65e9595a2b2c2f7dad231e1427cfeae0de0ff0ac4e262b33dd8d95b504285`
   (`apply_check_r3b.out` lines 4-5, stored file re-hashed after the round:
   10766 `e5562f76...5009`). No other chapter-bound byte changed: `E1 old` (337 B,
   `145590c5...255c`) and `E1 new` (653 B, `7f9d628d...73fe`) are unchanged from r2,
   `bib_additions.bib` is unchanged (1672 B LF `29602647...8ea3`; 1716 B CRLF
   `981eb00f...f458`).
2. **Re-verification against the current working tree** (`apply_check_r3b.out`):
   E1 old occurs exactly once; E2 anchor occurs exactly once; the four new keys
   `AustingWheater2001`, `Anagnostopoulos2026`, `AsanoNishimuraPiensukYamamori2025`,
   `ChouNishimuraTripathi2025` are absent from `bib/namcg.bib` and present in the
   additions; `IKKT1997` and `Steinacker2026Invitation` are in the bib and not in the
   additions; `ass:lorentzian`, `eq:Smatrix` and `sec:status-E` are each defined
   **exactly once** in `chapters/` (the second definition seen at
   `apply_check_r3.out` line 24 came from `chapters/appH-microscopic-proofs-compact.tex`,
   which the author has since deleted; the digest's Duplicate-labels section is now empty).
3. **Supersession of the r2 hash table.** Since review-r2 was written, the tree changed
   for reasons independent of 053: the integrated blocks 048-052 were committed into
   `chapters/`, and `chapters/appH-detailed.tex` and
   `chapters/appH-microscopic-proofs-compact.tex` (CR-CR-LF corrupted, author commits
   `1de50f3`) were deleted together with their `\include` in `namcg-book7.tex`. The
   appH input is now 521477 B `c0f9462fd2c6daf7e1b085250ea9f4bc7d45f605b93afc21857950bb796ba777`,
   not the 519811 `f3d20921...1285` the r2 table assumed. **The r2 "Expected results of
   integration" appH row is void; the values in the table below hold only from the input
   hashes stated there.** `bib/namcg.bib` is unchanged at 24258 `09ac48a5...a3aa`, so the
   bib row and its output are unchanged.
4. **Build on a fresh applied copy outside the repository** re-run on the current tree;
   the failure recorded in `build_check_r3.out` was caused solely by the CR-CR-LF
   `appH-detailed.tex` (a clean copy failed identically) and does not reproduce now that
   the file is deleted. Details under "Build on a copy outside the repository".
5. **Record line requested by review-r2 on the digest:** the digest has since been
   regenerated and `make_digest --check` reports CURRENT; the r2 "DIGEST STALE (head
   changed)" entries are resolved, and `chapters/bib` are clean at HEAD
   (`git status --porcelain -- chapters bib namcg-book7.tex` empty).

## Target and status

Unchanged from r2 and re-read again this round. Appendix H, Problem E (now
`chapters/appH-microscopic-proofs.tex` L1482-1496): "Status: OPEN. Priority: CRITICAL PATH
for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining
Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived
Lorentzian signature." Status paragraph: "Remains Assumption~\ref{ass:lorentzian}."
Chapter 17 L394-399: "OPEN; CRITICAL PATH for the matrix-derived label." No discrepancy.
Original target: derive Lorentzian signature rather than retain it. This package does not
derive it: PROGRAMME-CONDITIONAL sharpening plus the E1 correction of the 052 sentence
(PRIOR-CLAIM-ERROR, narrow, as ruled).

## Source reading

**Digest + targeted reads. Not a full scan.** `scratch/digest.md` is CURRENT
(head `30a1e07`, chapters-hash `060976c0e8e7218c`, `dirty-chapters: no`), so CLAUDE.md
3(d) does not fire; this round changes no definition, assumption, scope statement or
status passage in existing manuscript text (S7 edits only the new insert), so 3(c) does
not fire either. The scan ruling of review-r1/r2 (reliance on the recorded ordinal-50
full scan of 052) lapses by its own terms because chapter bytes changed beyond the 052
block when the author committed and deleted files; nothing in this round relies on it:
every byte the integration touches was re-checked against the current files this round,
and the only manuscript passages relied on were read in full at the current baseline:
the E1 host paragraph (`chapters/appH-microscopic-proofs.tex` L1478, the 052 paragraph
"\paragraph{Bearing on Section~\ref{sec:status-E}, and the relaxations.}"), the whole
Problem E section (L1482-1496), and `chapters/ch17-agenda.tex` L377-405. `reports/ledger.md`
entries 050-052 read. **Out-of-scope observation, flagged not fixed (writes forbidden
outside the proposal folder): `reports/ledger.md` contains residual merge-conflict
markers at lines 279 (`<<<<<<< HEAD`), 286 (`=======`) and 420 (`>>>>>>> 6aa44906...`).**

## Research and reasoning

No new mathematics. Mechanics, all re-run this round:

1. Byte-level anchor check, report half of `apply_check.py` (output
   `apply_check_r3b.out` lines 1-24): E1 old 1 occurrence; E2 anchor (`\paragraph{Status.}`
   CRLF `Remains Assumption~\ref{ass:lorentzian}.`) 1 occurrence, at L1495-1496; E1 host
   paragraph at L1478 (r2 reported L1447; positions shifted by the merged 048-052 blocks,
   content of both anchors unchanged, hashes equal). Insert and E1/E1-new/bib-additions
   hashes as in "Round 3 changes" item 1. Cite and label checks as there.
2. Application to a fresh out-of-repo copy (`make_copy_r3.py`, 250 tracked files except
   `proposals/`, `reports/`, `.claude/`, `agents/`, to
   `C:/Users/redgi/tmp/p053r3_copy_b`), then `apply_check.py --copy` (the script refuses a
   destination inside the repository and a second run). After application: appH 532576 B,
   CRLF 3203, bare LF 0; bib 25976 B, CRLF 867, bare LF 0. Arithmetic:
   521477 + (653 - 337) + 10783 = 521477 + 316 + 10783 = 532576;
   24258 + 2 + 1716 = 25976.
3. Build in the copy: `pdflatex` pass 1 exit 0; `bibtex` exit 0 with no warnings and no
   missing entries; `pdflatex` pass 2 exit 0; `pdflatex` pass 3 exit 0 (357 pages, but
   the log still carried "Label(s) may have changed. Rerun..."); a fourth `pdflatex` pass
   exit 0, after which `rerunfilecheck` reports `namcg-book7.out` not changed and the log
   has no Rerun warning. Final log: **357 pages, 0 undefined references or citations,
   0 multiply-defined labels.** For orientation, the current un-applied repository
   baseline passes `scripts/build_check.py` at 355 pages (orchestrator, after the
   author's deletions); the applied copy's +2 pages is the insert.
   Citation keys: all four new keys land in `namcg-book7.bbl` (natbib labels wrap, so
   `\bibitem[...]...{key}` matches on the second line; direct key grep confirms each
   once) and each appears once as `\bibcite{...}` in the final `.aux`.
4. Repository after all runs: `chapters/appH-microscopic-proofs.tex` 521477 `c0f9462f...`,
   `bib/namcg.bib` 24258 `09ac48a5...`, insert 10766 `e5562f76...` — unchanged; `git
   status --porcelain -- chapters bib namcg-book7.tex` empty.

## Claim classification

Unchanged from proposal-r2.md (kept by reference). S7 adds no claim: it scopes the
Definition (C) identification of the Euclidean model to p = 0 and records that the p = 4
model carries the Pfaffian — the wording of a classification already made in r2, corrected
by the gatekeeper's own replacement. E1's classification (first clause of the 052 sentence
overbroad: established false in the limit at N = 2, conditional for N >= 3; second clause
unsupported, not proved false) is unchanged.

## Proposed changes

Structurally identical to r2; only the byte values and the input hashes change.

### `chapters/appH-microscopic-proofs.tex`

**E1.** In-place replacement inside the 052 paragraph `\paragraph{Bearing on
Section~\ref{sec:status-E}, and the relaxations.}` (current file L1478). The old string
occurs exactly once, contains no line break, so EOL does not touch it.
Old (337 B, sha256 `145590c5b443c6342e694b9b62bd86693b35aa7db7fb9fa84998926095cb255c`)
and new (653 B, sha256 `7f9d628dddf1d4d4df94adfe47e1658bff54649dd4db9d8263340041002f73fe`)
are exactly the two `latex` blocks in proposal-r2.md, "E1. Correction to the 052 block",
unchanged; `apply_check_r3b.out` lines 6-7 confirm the sizes and hashes. Kept: everything
else in the paragraph, and the closing status sentence of the 052 block.

**E2.** Insert the CRLF form of `appH_insert.tex` (10783 B,
sha256 `bab65e9595a2b2c2f7dad231e1427cfeae0de0ff0ac4e262b33dd8d95b504285`) immediately
before the anchor

    \paragraph{Status.}
    Remains Assumption~\ref{ass:lorentzian}.

(CRLF between the two lines; occurs once, at current L1495-1496, in the Problem E
section). Kept: the Ledger label, the sentences "Euclidean positivity ...", the Status
paragraph. Pure insertion with one closing scoped status sentence. The insert is ASCII;
stored in the proposal folder with LF, 10766 B, sha256 `e5562f...5009`; it contains S7,
so it is no longer the r2 insert `5d0d4538...` (that byte form is preserved as
`appH_insert.r2.tex`).

Labels: `ass:lorentzian`, `eq:Smatrix`, `sec:status-E` each defined once in `chapters/`
at the current tree. Cites already in the bib: `IKKT1997`, `Steinacker2026Invitation`.
New keys, not yet in the bib: `AustingWheater2001`, `Anagnostopoulos2026`,
`AsanoNishimuraPiensukYamamori2025`, `ChouNishimuraTripathi2025`.

**Stale passages elsewhere:** none (as ruled in r1/r2; re-checked that the E1 host
paragraph and the Problem E section read as quoted).

### `bib/namcg.bib`

Append, **CRLF**: one blank line (`\r\n`), then `bib_additions.bib` converted to CRLF
(1716 B, sha256 `981eb00f360048973286f86084fb11b5949231309404c416302c37882327f458`).
Unchanged from r2. Do not re-normalise anything else; 0 bare LF after application.

### Expected results of integration

These hold **only from the input hashes shown**; if either input differs, stop and
recheck. The r2 table is superseded: its appH input `f3d20921...1285` / 519811 B no
longer exists in the tree.

| File | Input size, sha256 | Output size, sha256 |
|---|---|---|
| `chapters/appH-microscopic-proofs.tex` | 521477, `c0f9462fd2c6daf7e1b085250ea9f4bc7d45f605b93afc21857950bb796ba777` | 532576, `7a75554ef8cb7efe0e4c5cd3c53d6a9c4ffd2a9149e6ff29c7e8e067bb7f6aaa` |
| `bib/namcg.bib` | 24258, `09ac48a5a1157723a766f1aa118081b1c3f5ec4c928158ba3d0c43a80a90a3aa` | 25976, `a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b` (unchanged from r2) |

The outputs were produced by `apply_check.py --copy` on the current tree
(`apply_check_r3b.out` lines 26-28); the bib output hash equals the value the gatekeeper
computed in review-r2, as expected since neither the input nor the additions changed.
Arithmetic: 521477 + 316 + 10783 = 532576; 24258 + 2 + 1716 = 25976.

### Build on a copy outside the repository

Copy `C:/Users/redgi/tmp/p053r3_copy_b` (250 tracked files, excluding `proposals/`,
`reports/`, `.claude/`, `agents/`), E1 + E2 + bib applied, then pdflatex, bibtex,
pdflatex, pdflatex, +1 stabilising pdflatex: all exit 0; **357 pages; 0 undefined
references or citations; 0 multiply-defined labels**; bare LF after application: appH 0,
bib 0; all four new keys in the `.bbl` and one `\bibcite` each in the final `.aux`.
The extra pass was needed because the log kept "Label(s) may have changed" through pass
3; pass 4 shows `rerunfilecheck` unchanged and no warning. Full record:
`build_check_r3b.out`. The copy was left in place (outside the repository) so the
gatekeeper can re-hash it; the repository's tracked files are unchanged
(`c0f9462f`/`09ac48a5` re-confirmed after the runs).

## Verification scripts

All under `proposals/053-lorentzian-integral-limit-order/`.

New in r3:
- `apply_s7_r3.py` — applies S7 (parsed from `review-r2.md`) to `appH_insert.r2.tex`,
  writes `appH_insert.tex`; refuses on any hash or byte mismatch and on a second run.
- `make_copy_r3.py` — copies tracked files to an out-of-repo destination; refuses inside
  the repository.
- `apply_check_r3b.out` — current-tree anchor/hash/label/cite report plus the applied-copy
  hashes and bare-LF counts.
- `build_check_r3b.out` — the build record described above.

Earlier-round files kept and not overwritten: `appH_insert.r1.tex`, `appH_insert.r2.tex`,
`apply_check.r1.py`, `apply_s_r2.py`, `apply_check_r2.out`, `apply_check_r3.out`,
`build_check_r3.out`, `s2_s4_check_r2.py`, the `n2_*.py` and `pf_su2_identity.py` numerics
with their `.out` files. `apply_check.py` and `bib_additions.bib` unchanged since r2.
`apply_s7_r3.py` cannot be re-run now (it refuses: S7 already applied); to verify the
insert, compare `appH_insert.r2.tex` with `appH_insert.tex` — they differ exactly by S7,
and the result hashes to `e5562f76...`/`bab65e95...`.

## Decisions Taken

No RESEARCHER-DECISION finding was open. Routine decisions (author directive, autonomous
mode):
1. Kept the applied build copy at `C:/Users/redgi/tmp/p053r3_copy_b` instead of deleting
   it, so the gatekeeper can re-hash inputs and outputs; it is outside the repository and
   the author may delete it. Rejected: immediate deletion (loses the re-verification
   artifact; the gatekeeper's own r2 copy was likewise kept).
2. Ran one extra pdflatex pass beyond the four-command protocol to silence the persistent
   "Label(s) may have changed" warning and prove the cross-references are at a fixed
   point. Rejected: reporting pass 3 with the warning unresolved.
3. New record names `apply_check_r3b.out` / `build_check_r3b.out` so the pre-deletion r3
   records (`apply_check_r3.out`, `build_check_r3.out`) remain as evidence that the old
   build failure predates and is independent of 053.
4. Flagged but did not touch the residual conflict markers in `reports/ledger.md`
   (L279/L286/L420): outside the write permission.
5. Digest treated as CURRENT per the regenerated `scratch/digest.md`; the scan ruling is
   reported as lapsed by its own terms and replaced, for this round, by direct byte
   re-verification against the current files.

## Milestone assessment

M3 stands as ruled in review-r2 (the corrected 052 sentence: an accepted claim overbroad
to the point of being false in a limit). Round 3 itself is routine mechanics and triggers
nothing new. Not a breakthrough.

## Status-label recommendation

Critical-path set re-derived from Chapter 17 at this scope: A, B, C, D1, E, F, G-derived,
N (ch17 L378, L395, L404, L475, L498 and the appH ledger labels; ledger entries 050-052
agree). Affected labels: none. Problem E stays OPEN, CRITICAL PATH for the matrix-derived
label, PROGRAMME-CONDITIONAL.

## Author decision needed

None. (The Round 1 process item remains with the orchestrator/author as recorded in r2.)

## Remaining open step

Unchanged from r2. To close the original target: a derivation of a Lorentzian contraction
or real-time reading from the matrix integral with no retained premise. Next ranked
avenue: non-polynomial observables at N = 2. For this package's N >= 3 statement: an
independent proof of Lemma D, and Z_E != 0.

## Special instructions for the gatekeeper

- **Verify the input hashes before integration**: appH 521477 `c0f9462f...` and bib 24258
  `09ac48a5...`. The r2 appH input `f3d20921...1285` is gone from the tree; any table
  built from it is void. The outputs in the r3 table above were produced from the stated
  inputs by `apply_check.py --copy`; the bib output hash is identical to the gatekeeper's
  r2 value.
- The insert must equal `e5562f76...` (LF, 10766) / `bab65e95...` (CRLF, 10783): byte-
  identical to the gatekeeper's "Expected after S7" rows. Do not compare against
  `appH_insert.r2.tex`.
- Anchor positions moved with the merged 048-052 blocks: E1 host paragraph at current
  L1478, E2 anchor at L1495-1496; both occur once (byte content unchanged).
- `sec:status-E` is now defined once (compact/detailed appendix files deleted by the
  author at commit `1de50f3` together with their `\include`); the old "defined 2 times"
  line in `apply_check_r3.out` is stale for the current tree.
- Must not be asserted (unchanged from r2): a derivation of signature; any large-N
  statement; that 2501.17798 is wrong or has a systematic; novelty. Proved/conditional
  scoping is unchanged.
- The build used four pdflatex passes (exit 0 each, plus bibtex exit 0); report the 357
  pages, 0 undefined, 0 multiply defined from the final pass; re-verify on the kept copy
  `C:/Users/redgi/tmp/p053r3_copy_b` if wanted.
- No new derivation was produced this round; re-checking r2's mathematics is governed by
  the r2 verdict (accepted). Nothing outside the assigned proposal folder was written;
  the residual conflict markers in `reports/ledger.md` (L279/286/420) are reported for
  the orchestrator, not fixed.
