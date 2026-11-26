# Journal 130-margin-tightening (researcher, round 1, 2026-11-26)

Typographic package only. No physics/mathematics content change; no status,
priority or completion text touched; appH L3192-3236 (author hold) and the
ordinal-55 payload lines never touched. Source reading: digest + targeted
reads (digest CURRENT; I additionally read in full: namcg-book7.tex preamble
L1-60 and L60-157 (to end), ch03-matrix-action.tex L780-830,
appH-microscopic-proofs.tex L3425-3450).

## 1. Provenance audit of the orchestrator's logs (rule 7)

- scratch/margincheck/namcg-book7.log is NOT the 14-box baseline: its header
  command line is `**./scratch/emerg-test/namcg-book7.tex` (a temp copy), it
  has 2 Overfull \hbox (5.04942pt @802-813, 1.215pt @3437-3438), 448 pages,
  3297731 bytes. It is the PILOT run with the preamble line inserted.
  (emergencystretch not mentioned in log - a transcript never echoes an
  error-free preamble line.)
- The 14-box baseline is the tracked root namcg-book7.log (regenerated
  2026-11-26 10:30, before my session; I did not run it). My parse: 14 boxes,
  sizes 17.0237, 16.28656, 12.27011, 11.1815, 8.50606, 7.81596, 7.72087,
  6.0066, 5.04942, 2.9962, 1.68848, 1.33446, 1.215, 0.32002; max 17.0237pt;
  448 pages, 3297556 bytes. Matches the audit list and sizes exactly.
- Audit per-file attribution reproduced independently in my own harness
  (section 3): ch13 17.02 (L52-55), ch02 16.29 (L71-75), appH x9
  (L2803/138/2950/4033/1600/3514/4038/2900/3437), ch03 5.05 (L802-813,
  tabular), ch17 1.33 (L475-481), ch06 0.32 (L42-49).
- "Page count 450 -> 448" was NOT reproduced from a clean baseline: every
  clean staged-aux run I measured is 448 (root baseline log 448; margincheck
  pilot 448; my base mirror 448; my candidate 448). I did observe exactly
  450 pages once, in a deliberately-perturbed debugging run whose preamble
  line was malformed (TeX error changed the layout); the orchestrator's "450"
  most plausibly has the same origin, not the baseline. The final authoritative
  page count belongs to the orchestrator's normal 3-pass build; my staged-pass
  evidence shows NO page-count shift (448 -> 448) from A+B.

## 2. Measured facts

- Preamble: geometry paperwidth 7in, inner 0.9in, outer 0.45in => text block
  5.65in; microtype loaded (L14); setspace L21; `\setstretch{1.12}` L22,
  byte-count 1 in namcg-book7.tex; no `\emergencystretch` anywhere tracked.
- Default `\emergencystretch` measured on this toolchain (MiKTeX pdfTeX
  3.141592653-2.6-1.40.29, book class): 0.0pt (probe_default_ec.py ->
  `DEFAULT_EMERGECYSTRETCH EC=0.0pt`). The payload A line is therefore an
  effective change, not a no-op.
- ch03 table: `center` env + `tabular{@{}ll@{}}`, 1 occurrence each of
  `\begin{tabular}{@{}ll@{}}` and `\end{tabular}` in ch03 (byte counts).
  Width = col1 + col2 + 2*tabsolsep(6pt); local tabcolsep 6pt->3pt shrinks
  the tabular 6pt > 5.04942pt overrun => 0.95pt clearance. No font or column
  alignment change (rejected alternatives: `{\small}` changes the table font;
  `p{}` columns reflow cells and change alignment - both larger changes).
- ch03 (916 CRLF, 0 bare LF), appH (4154 CRLF, 0 LF), namcg-book7.tex
  (156 CRLF, 0 LF, NO trailing newline; my insert does not touch EOF).

## 3. Harness (scratch/margin-typo/, all output -output-directory confined)

Mirror route: scratch/margin-typo/{base,cand}/ hold copies of
namcg-book7.tex + chapters/ + frontmatter/ with root aux/.bbl/.toc/.out
staged; run FROM REPO ROOT with
TEXINPUTS='<mirror>/;;' pdflatex -interaction=nonstopmode -file-line-error
-output-directory scratch/margin-typo/out-<x> <mirror>/namcg-book7.tex.
Trailing `;;` keeps repo-root fallback for figs/ inputs. Proof the mirror is
read: log file-open trace `.../scratch/margin-typo/{base,cand}/chapters/
ch03-matrix-action.tex`; cert asserts this trace for the candidate.
Per-box file attribution: newline-unwrapped log, region between the
`ch03-matrix-action.tex` open trace and the `ch04-vierbein-emergence.tex`
trace; owner = last chapter .tex trace before the box. Region scanner proved
non-vacuous on the base log (finds the 5.04942 ch03 box) and by a canned
positive control in the cert.

## 4. Scans (real numbers)

- BASE mirror pass (staged aux, 1 pass): rc=0; 14 boxes, sizes identical to
  the root baseline; region ch03: 1 box 5.04942; 448 pages; PDF 3297556 bytes
  (byte-size-identical to tracked root PDF => harness fidelity).
- CAND mirror (A+B) 2 passes: rc=0; no `!` error lines; 1 box: 1.215pt,
  appH L3437--3438; ch03 region: 0; 448 pages; 3297740 bytes.
- Log warning profile base->cand: 13 Overfull \hbox removed (12 absorbed by
  emergencystretch, 1 by the tabcolsep wrapper). New: 2 Underfull \hbox
  badness notices in appH (2005 @L3514-..., 4132 @L4033-...) - loose lines,
  not margin violations; Underfull \vbox badness-10000 46 -> 47, 7397 2 -> 1,
  3977 0 -> 1, 2384 1 -> 0 (cosmetic vertical glue). No new Overfull anywhere.
- Residual 1.215pt (appH L3437-3438): unchanged size and line range despite
  2em emergency stretch => the offending line is an unbreakable inline math
  atom (the paragraph holds long \det/\int/\frac display-style inlines);
  stretch cannot fix an over-wide unbreakable list item. Decision: LEAVE.
  A one-token fix would require editing math tokens (out of bounds) or
  paragraph-level \small (visible); 1.215pt = 0.017in = 0.43mm protrusion
  into the 0.45in outer margin, below the 2pt guard threshold.

## 5. cert_130.py (final, run 2026-11-26: PASS; total runtime 19.9 s)

`python -I proposals/130-margin-tightening/cert_130.py` from repo root.
Output: CTL-PARSER fires (1 box @9.99), CTL-REGION fires (1 in / 1 out),
BASE rc 0 total 14 ch03-region [5.04942], CAND rc 0 total 1 max 1.215,
owners [appH], ch03-region 0, mirror trace True, 448 pages, TRACKED hashes
unchanged (8 files incl. root pdf/log/aux/bbl/toc/out), final line:
`CERT130 PASS BASE14 CAND1 CH03SITE0 MAX1.215`.

## 6. Bug log (honest)

1. The Bash tool squashes `\\` in heredocs; my first mirror build lost the
   `\emergencystretch` backslash -> "Missing \begin{document}" at L23, rc=1,
   a 450-page PDF, 13 boxes (ch03 fix worked, A did not). Fixed by building
   all backslash strings with chr(92); cert_130.py is written backslash-free.
2. First cert run FAILED on its own positive control: the decoy contained a
   truncated overfull token and the parser (correctly) flagged it malformed.
   Replaced with a non-token decoy. The malformed-token guard itself fired
   as designed.
3. First probe used `\type` (typo) then hit the same `\\` squash; final probe
   uses chr(92) and prints EC=0.0pt.

## 7. Artifact inventory (sha256[:12], bytes)

- cert_130.py 2054773e2663 9107  (CRLF-normalized; was 2be6656cf0f1 8902 LF)
- payloadA-preamble.tex f4aa60aa4099 36  (34 content + CRLF)
- payloadB-ch03.diff 8b2f0ffa435a 1026  (CRLF-only, ASCII)
  insert1 bytes 30 (717a15da8b92), insert2 bytes 3 (e22faa535bd2)
- probe_default_ec.py -> DEFAULT_EMERGECYSTRETCH EC=0.0pt
- Tracked hashes identical before/after all runs: namcg-book7.tex bf3e291ffb15;
  chapters/ch03-matrix-action.tex 1e3e37b31a1e (== digest value); pdf
  255c0fbf08cc; root log 5a5907f6d5a9; aux 12cd5d99ae14; bbl 3b7d1f8fb3f4;
  toc 274dc9dc1530; out ec9c638e19a6.

## 8. Decisions

- B implemented as local `{\setlength{\tabcolsep}{3pt} ... }` wrapper (smallest
  change, cells byte-identical) over `{\small}` / `p{}` - evidence: section 2.
- Residual 1.215pt LEAVE (evidence: section 4).
- Page count reported as "no change in staged passes (448/448)"; final number
  deferred to orchestrator 3-pass build; the 450 baseline claim corrected with
  provenance (section 1).
