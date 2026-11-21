# Proposal 108-a-map-noncentral-chart-select, round 3 (math-delimiter-only fix + compile certificate)

## Result
The round-2 payload `insert-r2.tex` (accepted text, byte-perfect splice) FAILED `pdflatex` with
`! Package amsmath Error: \hat allowed only in math mode.` (fatal, l.144 of the spliced appH — inside the new
paragraph) and the integration was cleanly reverted (live appH back to 812227/698f38979140770d/3876; see
scratch/apply_108.out and scratch/build_check_108.out). Root cause: a LaTeX syntax defect in the accepted payload —
the opening sentence `Let \hat X^I be self-adjoint coordinate operators` places `\hat X^I` (and its `^I`) in TEXT
mode — and the pipeline gap that let it through: byte/splice/hygiene verification covered everything EXCEPT math
mode; no compile test existed for the payload. Round 3 supplies `insert-r3.tex` (3076 B / sha256/16
`356f6ba97912775c` / 1 CRLF): insert-r2.tex with math delimiters ADDED ONLY, and a compile certificate.

## Delimiter-only construction and normalization test
`mk_insert_r3_108d.py` parses insert-r2.tex by char-level `\( \)` mode toggling and wraps, in each TEXT region, the
maximal whitespace-joined runs of mathy tokens (token starts with a backslash command or contains `^`/`_`/`$`;
`\paragraph` whitelisted). It found EXACTLY ONE text-mode math island in the whole payload:
`\hat X^I` (the paragraph's first sentence); all 16 other `\hat` occurrences and every other `^`/`_` are already
inside `\( ... \)` — consistent with a full manual read of the payload. Delimiters added: 1 pair (4 bytes).
MANDATORY normalization test asserted PASS: `insert-r3.tex` with all `\(`/`\)` removed == `insert-r2.tex` with all
`\(`/`\)` removed, byte-for-byte; `len(r3) == len(r2) + 4`, `\(` and `\)` counts 26/26, 1 CRLF preserved, no
control bytes. No occurrence required grouping beyond delimiter insertion (the `\hat` grabs `X`, `^I` attaches to
the same atom inside `\( \)` — no `{\hat X}^I` regrouping needed). Provenance note: generator revisions a-d are on
disk; a-c failed their own asserts (regex/backslash-literal mangling in the transfer path; dropped-delimiter and
bytes-per-pair accounting bugs) and never wrote an accepted payload — 108d is the authority and asserts before
writing. Hygiene r3 (folder cwd): 21/21 PASS, `file=insert-r3.tex sha256/16=356f6ba97912775c`.

## Compile certificate
`compile_cert_108_r3b.py` copied the manuscript inputs (root .tex/.bbl + chapters/, frontmatter/, bib/, figs/) to
`scratch/compile108/` (never writing into chapters/ or .git/), spliced insert-r3.tex at the unique PIN of the
COPY (PRE asserted == live 812227/698f38979140770d/3876; spliced copy 815305/`4b3e836d29b3efa5`/3878 — byte-equal
geometry to the simulate POST), ran one `pdflatex -interaction=nonstopmode -halt-on-error namcg-book7.tex` pass
and certified: **COMPILE CERT: PASS=True exit=0 errlines=0 output_written=True — `Output written on
namcg-book7.pdf (426 pages, 2707904 bytes)`**; live appH unchanged after the run (sha 698f38979140770d). The
first attempt (compile_cert_108_r3.py) failed only because its file filter dropped the figure PDFs (a sandbox
copy defect, not the payload) — kept on disk as provenance.

## Simulate (POST recomputed, never hard-coded)
`simulate_apply_108_r3.out`: PRE 812227/698f38979140770d/3876 (asserted from live bytes); PIN count 1, offset
14892; POST computed **815305/`4b3e836d29b3efa5`/3878** = r2-certified 815301/316c7b6f549ed660 + 4 bytes (the one
added delimiter pair) — geometry asserted as PRE + payload + 2 CRLF, delta CRLF +2; undo True; live appH
unchanged True; preview `scratch/sim/appH_after_108_r3_preview.tex`.

## No content change
This round alters NO claim, NO scope, NO gap and NO status of the accepted round-1/r2 result: the r2 text
(gatekeeper-staged wording, all four F1-F4 substitutions intact — verified via the normalization equality to r2)
is unchanged except the inserted `\( \)` around `\hat X^I`. Problem A stays OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL; the round-1 Remaining-open-steps list (1)-(5) is unchanged.

## Status-label recommendation
Unchanged (A: OPEN/CRITICAL PATH/PROGRAMME-CONDITIONAL; edge A.map.noncentral-chart-select: untried -> attempted
at integration).

## Milestone assessment
Routine correction round (fixes a materially false-on-compile payload); no MILESTONE.md trigger.

## Author decision needed
None. Process observation for the author (advisory, no action required by this package): the pipeline lacked a
payload compile test; the compile-certificate method used here (sandboxed copy + splice + one halt-on-error pass)
can become a standing integration step.

## Remaining open step
Unchanged from round 1/2 (items 1-5), plus integration of insert-r3.tex (the integrator should re-certify the
splice from live bytes: expected POST 815305/4b3e836d29b3efa5/3878 against live 812227/698f38979140770d/3876).

## Special instructions for the gatekeeper
Payload is `insert-r3.tex` ONLY; `insert-r2.tex` is SUPERSEDED BY COMPILE FAILURE — do not integrate. Verify: (a)
normalization equality r3 <-> r2 modulo delimiters; (b) the single wrap location is the paragraph's first
sentence; (c) compile_cert_108_r3.out page count and zero error lines; (d) hygiene_108_r3.out 21/21 on the r3
triple; (e) simulate r3 POST geometry. Re-run compile in a scratch sandbox if desired (r3b script, ~1-2 min).
