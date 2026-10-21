# Integrator Report: 037-comparator-first-law

## Precondition checks

- **Branch**: `local/gpu` -- confirmed.
- **Review verdict**: `ACCEPT WITH REQUIRED REVISIONS`, FLAGS: none, PROGRESS: improving.
- **Digest**: `DIGEST CURRENT`.
- **Git status**: only `.claude/agents/*.md`, `shroud.ps1`, and `proposals/037-comparator-first-law/proposal-r2.md` modified outside `chapters/` and `bib/`. No uncommitted changes in `chapters/` or `bib/` from other agents.
- **Anchor**: `\section{Problem C: conformal mode and Cassini}` occurs exactly once in the target file.
- **BibTeX keys**: `JacobsonMohd2015` and `FrolovFursaev1997` were absent from `bib/namcg.bib` at time of check; both added.

## Files changed

1. **`chapters/appH-microscopic-proofs.tex`** -- 11 lines inserted (the 037 block from `appH_insert.tex`, converted to CRLF).
2. **`bib/namcg.bib`** -- 24 lines added (two new BibTeX entries: `JacobsonMohd2015` and `FrolovFursaev1997`).

## Insertion details

- The 037 block was inserted immediately before `\section{Problem C: conformal mode and Cassini}` (line 295), after the 036 block ending "Problem~B stays open and PROGRAMME-CONDITIONAL." (line 293).
- No existing text was replaced or modified; only new lines were added.
- No new `\label` or `\ref` entries were added.
- The two new `\cite{JacobsonMohd2015}` and `\cite{FrolovFursaev1997}` citations are present in the insert.
- File encoding: UTF-8 without BOM, CRLF line endings preserved throughout.

## Status labels

No status labels were changed. The existing `Problem~B stays open and PROGRAMME-CONDITIONAL.` in the 036 block (line 293) is untouched. The 037 block ends with its own "Problem~B stays open and PROGRAMME-CONDITIONAL." (line 304). All other status labels in the file remain byte-identical.

## Build result

- **Pass 1**: OK, 303 pages
- **Pass 2**: OK, 303 pages
- **Undefined/multiply-defined references**: 0
- **PDF**: restored (tracked PDF unchanged)
- **git diff --check**: clean
- **BUILD_CHECK**: PASS (pages=303)

## Backup

- **Path**: `scratch/integrator-backup/037-comparator-first-law/`
  - `chapters/appH-microscopic-proofs.tex`
  - `bib/namcg.bib`

## Page count

303 pages (unchanged from pre-integration; the insert is bounded text that fits within existing pagination).

## Commit status

**Nothing was committed.** Both `chapters/appH-microscopic-proofs.tex` and `bib/namcg.bib` remain uncommitted in the working tree for the author to review.
