# Integration journal - item 129, integrator ordinal 55 (2026-11-26)

Branch: local/gpu (verified with `git branch --show-current`; no switch/commit/stash performed).
Guard flag `.claude/state/allow_chapters` present (kept by author; not created or deleted here).
Review: `review-r2.md` line 7 `VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0`;
no `LABEL-CHANGE-PROPOSED`. Same round (r2) and same item (129) as `proposal-r2.md`.

## Pre pins (measured on disk before edit)

- `chapters/appH-microscopic-proofs.tex`: 883,075 B, 4,146 lines, sha256 `dee9a4174b8113e36850f17b82bba413f7f80da8955a370f5affd072bc7b64df`, sha1 `6839a5cab30e4d95e14eb6950ee978a51c3557cf`.
- `proposals/129-rc-held-recheck/payload-F.tex`: 3,147 B, sha256[:12] `87a7c2568f72`, sha1[:12] `0cf326eb3457` - exact match to the accepted pins; pure CRLF (0 lone CR, 0 lone LF), ASCII, single trailing CRLF, 3 CRLFs, no internal trailing blank line.

## Pre-checks

- Anchor 1 `On this evidence the sign of \(\hat U\) depends on \(K\).`: count 1 (L3194).
- Anchor 2 `\emph{Scale dependence.}`: count 1 (L3196).
- Join region `\r\n\r\n\emph{Scale dependence.}`: count 1.
- Payload not already present (count 0); `eq:Smatrix` already used/defined in appH (34 occurrences pre-edit).
- Byte hygiene deviation from the dispatch (recorded, not a blocker): appH pre-image is NOT pure ASCII - it carries
  one pre-existing UTF-8 em dash (E2 80 94) at offset 775756 / L3401. Payload is pure ASCII, so the splice adds zero
  non-ASCII bytes; post-check asserts the whole-file non-ASCII byte string is exactly that em dash (passed).
- Tree state pre-edit: only ` M reports/ledger.md` (pre-existing, orchestrator's ledger; known EOL artifact) plus
  untracked `proposals/129-rc-held-recheck/` and `proposals/claude-remote-late/`. NOTE: the dispatch expected
  pending edits in `chapters/ch01` and `namcg-book7.tex`; none were present in the working tree (presumably since
  committed - HEAD shows recent commits). Nothing in `chapters/` or `bib/` was dirty before my splice. No bib entry
  (accepted proposal adds none).

## Splice math (recomputed independently)

Canonical replace of the unique join region `X = CRLF CRLF \emph{Scale dependence.}` with
`CRLF CRLF + payload + CRLF + \emph{Scale dependence.}`: added bytes = 3,147 + 2 (join CRLFs) = 3,149.
New size = 883,075 + 3,149 = 886,224 B = accepted POST figure. New line count = 4,146 + 3 (payload CRLFs) + 1
(blank-line join) = 4,150.

First splice attempt used pre-insertion instead of replace and added 3,153 B (kept the original blank line AND the
new join); the size guard aborted before any write and the on-disk file was re-measured at 883,075 B (unchanged).
Second attempt used the replace form. Guards had injected positive controls (item 117 rule): the guard function was
fired on an absent-anchor pattern and correctly failed; the adjacency and size guards each fired in live use.

Removal round-trip check: `new.replace(payload + CRLF, '', 1) == pre` (byte-for-byte restoration of the pre-image).

## Post verification (re-read from disk)

- Size 886,224 B; lines 4,150; sha256[:12] `beed36d60b8c`, sha1[:12] `27bf197bd548`.
- Anchor 1 count 1 (L3194); anchor 2 count 1 (L3200); payload count 1, offset 679996, order anchor1 < payload < anchor2.
- Payload occupies L3196 (para 1), L3197 blank, L3198 (para 2); exactly one blank line (L3199) before
  `\emph{Scale dependence.}` (L3200). No doubled or missing blank line.
- Pure CRLF (0 lone CR, 0 lone LF), ends CRLF; whole-file non-ASCII bytes == the single pre-existing em dash.

## Build (`python -I scripts/build_check.py`, exclusive)

```
pass 1 OK, 450 pages
bibtex OK, 0 warnings
pass 2 OK, 450 pages
pass 3 OK, 450 pages
undefined citations: 0, undefined references: 0
undefined/multiply-defined warnings: 0
pdf restored
git diff --check: clean
BUILD_CHECK PASS pages=450
```

450 pp matches the gatekeeper compile cert (review-r2 line 23). Tracked PDF restored by the script (no diff).

## Final state

- `git diff --stat -- chapters bib`: `chapters/appH-microscopic-proofs.tex | 4 ++++` (pure insertion: 2 paragraphs +
  2 blank lines); no bib changes.
- `git status --porcelain`: ` M chapters/appH-microscopic-proofs.tex` (this package), ` M reports/ledger.md`
  (pre-existing), untracked proposal folders. Nothing staged, nothing committed, no branch operations.
- No status/priority/completion label touched; Problem F ledger text unchanged (payload is inserted narrative only).
- Backups: `scratch/integrator-backup/55-129-rc-held-f-cubic/payload-F.tex.bak-of-appH` (appH pre-image, 883,075 B),
  `payload-F.tex.orig`, `hashes.txt` (pre-image sha256+sha1 of both files).
