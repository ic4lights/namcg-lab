# Review r1 - item 131 (gatekeeper)

Source: gatekeeper agent, 2026-11-26. Saved by the orchestrator; HTML entities restored to plain characters
(`<`, `>`), content otherwise unaltered.

---

VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/0

## Verdict
The package is exactly what it claims: a pure permutation of two `\include` lines in `namcg-book7.tex` that moves the problem-ledger appendix to last position, verified byte-exact and build-identical (448 pp, single 1.215 pt overfull box) with zero content change, zero hardcoded appendix-letter breakage, and zero position-dependent prose; ACCEPT.

## Source reading
`scratch/digest.md` was not relied on (permanently-dirty tree; task specified targeted reads). **Targeted reads**, not a full scan (none required: no definition, assumption, scope or status text changes). Read in full: `proposals/131-appendix-reorder/proposal-r1.md`, `proposals/131-appendix-reorder/cert_131.py`, `namcg-book7.tex` (all 158 lines), `chapters/ch17-agenda.tex` L683-692 and L775-794, `chapters/appJ-summary.tex` L1-14 and L90-124, `chapters/appK-endomorphism.tex` L84-95, `chapters/appH-microscopic-proofs.tex` L1-8 and L3555-3572, `chapters/ch04-vierbein-emergence.tex` L141-149, `chapters/ch06-entanglement-equilibrium.tex` L64-71. Plus scripted scans over all of `chapters/**/*.tex` and `frontmatter/`. Unreadable files: none.

## Claim under review
Moving one `\include` line makes the ledger appendix print as the final appendix (letter L), shifting appI-appL to H-K, with every prose reference following automatically; no manuscript content changes. Not a critical-path problem; no Appendix H problem involved; no status/priority/completion label touched (confirmed: `git status --porcelain -- chapters bib namcg-book7.tex` empty - package not yet applied, and appH/bib untouched by design).

## Checks performed
1. **Byte verification (direct, independent of the pack).** Live root = 4293 B `43031b9414e0` (matches PRE); `\include{chapters/appH-microscopic-proofs}` count 1 at L144, `\include{chapters/appL-coupling}` count 1 at L148. Constructed the candidate myself: 4293 B `1b45f1d475ec` (matches POST), pure line permutation (CRLF-line multiset equal, file differs), size constant; diff is exactly the 5-line shift moving appH from 144 to 148. Integrator block (12 lines anchored on unique `\include{chapters/appA-seeley-dewitt}`): PRE 443 B `4aa7b99378e8` -> POST 443 B `040c20252ad2`, POST order A,B,C,D,E,F,G,I,J,K,L,H - all match the proposal.
2. **Reproduction pack.** `python -I proposals/131-appendix-reorder/cert_131.py` from repo root: exit 0, `CERT131 PASS PRE12=43031b9414e0 POST12=1b45f1d475ec BASE=448,1,1.215 CAND=448,1,1.215 CONTROLS=FIRED`. BASE and CAND both 448 pages (no verso-parity change); CAND 0 undefined refs, 0 undefined citations, 0 error lines, overfull total 1 max 1.215 pt (< 2.0 pt build_check threshold, the known appH L3437 box). Controls audited for teeth, not just output: perm-guard rejects an appended-character edit and discriminates identity (both guards backed by hard asserts, so vacuity aborts the run); block-anchor control is backed by the in-code `count(APP_A)==1` uniqueness assert; the overfull parser fires on the injected 9.99 pt box via the literal `\hbox` string split. `ucit=0` on CAND also proves the tracked `.bbl` was genuinely consumed. Post-run `git status` confirms the pack wrote nothing tracked (all under `scratch/reorder131/cert/`).
3. **Auto-renumber claim (direct).** `book` class with `openright`; `\appendix` at root L136 immediately before the include block; no `\thechapter`/`\theappendix`/`\thesection` redefinitions anywhere in `chapters/` (the root's `\thechapter` use is only the `\chaptermark` page header, display-only). Hardcoded letters in prose exist only for **A-D** (`ch01` B; `ch02` A,B; `ch16` D; `ch17` bridge L785-790 A-D) and all name files whose positions 1-4 are unchanged by the move, so they remain correct. Zero "Appendix H" (or E-L) hardcoded strings with or without tilde, case-insensitive; `frontmatter/` has no appendix mentions.
4. **Position-dependent prose hunt (main semantic risk - clear).** Word-boundary proximity scan (±3 lines) of all `chapters/**/*.tex` for order vocabulary around any "append"/`app:` mention, plus full reads of every candidate: appJ summary (references ledger only via `\ref`; contains no order claim), ch17 bridge (names only A-D; the only order-sensitive sentence, "None of the appendices introduces a new physical hypothesis", is order-invariant), ch17 L686 "sequence above" refers to ch17's own list; appK "far below laboratory interest" and ch04 "at first order" are mathematical; ch06 L68 `\ref{sec:status-A}--\ref{sec:status-B}` is an intra-ledger range, internally unchanged. Note the only genuine relative-position flip: the ledger moves from before to after appI-appL, but no sentence in appI, appJ, appK, appL or appH asserts relative reading order - all say "Appendix~\ref{app:status}" or "open-problem ledger of Appendix~\ref{app:status}" (appK L92, appL L62, appD L14, ch18 L92, etc.). No sentence becomes false.
5. **Cross-file integrity.** Repo-wide grep: only `namcg-book7.tex` includes `chapters/appH-microscopic-proofs`. `previewA(no blank).tex` and `previewB(blank).tex` exist at root but do not include it and are outside the namcg-book7 build - noted, not blocking. appH file and `bib/` unmodified; working tree clean in `chapters/`, `bib/`, root.
6. **Ledger self-letter.** appH opens with `\chapter{Status of the Open Problems}`, no literal letter; "Problems A--J and N" are problem labels, not appendix letters, and are unaffected.
7. **Right margin (directive 2026-11-26).** Zero prose or formula changes; CAND build introduces no Overfull \hbox versus the recorded baseline (identical single 1.215 pt box, threshold 2 pt).

## Findings
- **none** (blocking or major). One minor observation, no action required for this package: `ch06` L68 writes "Appendix~\ref{sec:status-A}--\ref{sec:status-B}", printing "Appendix L.1-L.2" (section labels rendered under an "Appendix" noun). This looseness is pre-existing and unchanged in kind by the move; if the author ever wants it tightened, "Section~..." would do - outside this package's scope.

## Scope of what is established
- **Proved/verified:** the exact byte edit (PRE/POST/block hashes, permutation property); CAND compiles at 448 pp with 0 undefined refs/citations, 0 errors, overfull identical to baseline; all manuscript appendix cross-references are label-based or point to position-stable letters A-D; no order-asserting prose exists; no other tracked file or build consumes appH.
- **Conditional:** nothing beyond the above; the change carries no mathematical content, so no derivation status (DERIVED/PROGRAMME-CONDITIONAL) is asserted, altered, or implied.
- **Still OPEN:** unchanged - every Appendix H problem keeps its current status; nothing here closes, supports, or touches any critical-path problem. Spacetime remains emergent: zero content changes. The proposal's "Aftercare" (process-doc rewording) is author-sanctioned, outside this review, and does not rewrite historical records.

## Recommended disposition
**Integrate as-is.** Exact splice instructions for the integrator:
1. Re-hash the live `namcg-book7.tex`; require 4293 B `43031b9414e0`. If it differs (another chain integrated first), recompute PRE/POST/block hashes and re-derive the candidate as the pure line permutation moving the single appH include line to immediately after the appL line before applying.
2. Anchor: the unique line `\include{chapters/appA-seeley-dewitt}` (block start); block = that line plus the following 11 include lines, each CRLF-terminated (12 lines, 443 B). Replace the block (443 B `4aa7b99378e8`) with the same 12 lines ordered appA, appB, appC, appD, appE, appF, appG, appI, appJ, appK, appL, appH (443 B `040c20252ad2`). Preserve CRLF; UTF-8 no BOM.
3. Confirm whole-file POST = 4293 B `1b45f1d475ec`.
4. Run `python scripts/build_check.py` exclusively; expect PASS, 448 pp, 0 undefined refs/citations, overfull total 1 / max ≈1.215 pt / 0 boxes >=2 pt, tracked PDF restored, `git diff --check` clean. Then refresh the digest.

## Corrected snippet
Not needed.
