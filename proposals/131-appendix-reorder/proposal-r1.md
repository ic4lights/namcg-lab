# Proposal 131 - move the problem-ledger appendix to the last appendix position

Originator: orchestrator, under explicit author directive 2026-11-26 ("Reorder only", author-selected option:
"Just move the ledger appendix to the end so the reading flow ends with it; book stays 448 pp everywhere").
This is a **structural/editorial manuscript change with zero content change**: no mathematics is originated, no
definition, assumption, scope statement or status passage is altered, and no Appendix H problem is involved.
The gatekeeper reviews exact text; the integrator applies it on ACCEPT.

## Claim

Interchanging two `\include` lines in `namcg-book7.tex` moves the problem-ledger appendix
(`chapters/appH-microscopic-proofs.tex`, label `app:status`) from the 8th to the last appendix position, so the
printed appendix order becomes A, B, C, D, E, F, G, I, J, K, L, then the ledger. Because the book class
auto-generates appendix letters from `\appendix` + chapter order, and because every manuscript cross-reference to
the ledger is a `\ref`-based label reference (a current `chapters/**/*.tex` scan finds zero hardcoded
"Appendix H" strings), the printed letter of the ledger becomes **Appendix L** and appI-appL shift to H-K, with all
prose references following automatically. Reading order now ends with the ledger; page content of every file is
byte-identical.

## Exact change

File `namcg-book7.tex`, live tree at integration time: PRE 4293 B `43031b9414e0` (ordinal 56 / author commit
0e39eb6 lineage). One line moved; file size unchanged, POST 4293 B.

Bytes: MOVE = `\include{chapters/appH-microscopic-proofs}` + CRLF (47 B, count 1); ANCHOR =
`\include{chapters/appL-coupling}` + CRLF (35 B, count 1). Operation: delete MOVE (with its CRLF), re-insert the
identical 47 B immediately after the ANCHOR line's CRLF. Equivalent integrator view: replace the 12-line appendix
include block (appA..appL, anchored on the unique `\include{chapters/appA-seeley-dewitt}` line, block start =
that line) with the same 12 lines in order A,B,C,D,E,F,G,I,J,K,L,H-block-last; the block is a pure line
permutation of equal length.

Expected POST and block hashes (measured by the reproduction pack on the live tree): POST 4293 B `1b45f1d475ec`;
integrator block replacement 443 B `4aa7b99378e8` -> 443 B `040c20252ad2`. The integrator must see POST file hash
equal to the CERT131 POST12 value, size 4293 B.

## Verification (reproduction pack)

    python -I proposals/131-appendix-reorder/cert_131.py    # from repo root; writes only scratch/reorder131/cert/

Checks: (1) candidate is a pure line permutation of the live root file (multiset equality + not-equal), with fired
positive controls (a perturbed line and the identity edit are both rejected); (2) include anchors unique;
(3) block-anchor strictness control fires; (4) BASE (live) and CAND (moved) mirror compiles, three pdflatex passes
each with the tracked `.bbl` copied in, parsed by the proven string-split overfull scanner (parser positive control
fires on an injected 9.99pt box). Required: CAND 0 undefined references, 0 undefined citations, 0 error lines,
Overfull \hbox total <= 1 with max < 2.0 pt (same single 1.215 pt appH L3437 box is expected; the ledger file is
untouched), BASE comparable. Measured run (2026-11-26, live tree): `CERT131 PASS PRE12=43031b9414e0
POST12=1b45f1d475ec BASE=448,1,1.215 CAND=448,1,1.215 CONTROLS=FIRED` - 448 pages on both mirrors (no verso-parity
page change occurred).

## Integration and build

Integrator applies the block replacement (anchors re-verified live), then `python scripts/build_check.py`: expect
PASS, 0 undefined refs/citations, overfull line unchanged from baseline (`total 1, >=2pt 0, max 1.22pt`), PDF
restored, `git diff --check` clean. TOC will show the ledger as the final appendix.

## Aftercare (outside this proposal, author-sanctioned by the same 2026-11-26 decision "Generic reword")

Process documents naming "Appendix H" as the ledger will be reworded generically to "the problem-ledger appendix
(last)" by the orchestrator after integration: CLAUDE.md, MILESTONE.md, .claude/commands/run-cycle.md, agent
definitions, README, and two scripts. No historical record (ledger, reviews, reports, proposals) is rewritten.
No status, priority or completion label is touched anywhere. The `appH-...` file name and `app:status` label are
deliberately unchanged.
