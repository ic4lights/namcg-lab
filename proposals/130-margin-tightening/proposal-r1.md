# Proposal 130-margin-tightening, round 1

## Result

Two byte-minimal typographic edits reduce the right-margin `Overfull \hbox`
count of the book from 14 to 1 (max breach 17.02pt -> 1.215pt), measured in a
reproducible scratch harness against the current tree:

- (A) one preamble line, `\setlength{\emergencystretch}{2em}`, absorbs 12
  paragraph overfulls (the 17.02, 16.29, 12.27, 11.18, 8.51, 7.82, 7.72,
  6.01, 3.00, 1.69, 1.33, 0.32 pt boxes) by letting TeX add up to 2em of
  emergency glue to otherwise-impossible line fits;
- (B) a local `\tabcolsep` wrapper on the ch03 scales table (L802-813,
  5.04942pt) clears that tabular box by shrinking only inter-column spacing
  12pt -> 6pt; all cell bytes are untouched;
- (C) the residual 1.215pt box (appH L3437-3438) is recommended to be LEFT
  as accepted: below the 2pt guard threshold, unchanged by 2em of emergency
  stretch (hence an unbreakable math atom), and fixable only by editing math
  content, which is out of bounds for this package.

No mathematical or status-bearing token changes; no page-count change in the
staged-aux passes (448 -> 448; the final 3-pass number is for the
orchestrator's normal build to record).

## Target and status

Orchestrator dispatch item 130 (author-reported inline/display math breaching
the right margin). This is NOT an Appendix H problem: it carries no status,
priority or completion label, opens or closes nothing, and is neither
DERIVED nor PROGRAMME-CONDITIONAL in the MILESTONE.md sense - it is a
layout-quality fix in the shared preamble and one table wrapper. Critical-path
set re-derived from ch17-agenda / appH at this task: A, B, C, D1, E, F,
G-derived, N remain as recorded; unchanged by this package. No dependency of
any problem changes.

## Source reading

digest + targeted reads. scratch/digest.md CURRENT (digest itself flags
`dirty-chapters: yes`, so I read in full every file my payload touches):
namcg-book7.tex L1-157 (whole preamble incl. geometry/microtype/setspace and
the `\include` list; file ends without a trailing newline - untouched by my
insert), chapters/ch03-matrix-action.tex L780-830, chapters/appH-microscopic
-proofs.tex L3425-3450 (residual site paragraph only; the author hold
L3192-3236 never opened or referenced). No unreadable files.

## Research and reasoning

1. Baseline reproduction (rule 7). The task cited scratch/margincheck/namcg
   -book7.log as the baseline; provenance audit shows that log is the PILOT
   (header `**./scratch/emerg-test/namcg-book7.tex`, 2 boxes {5.04942,
   1.215}, 448 pages). The 14-box baseline is the tracked root namcg-book7.log
   (built 10:30 pre-session; 14 boxes, max 17.0237pt, 448 pages, 3297556 B),
   independently parsed: sizes 17.0237 16.28656 12.27011 11.1815 8.50606
   7.81596 7.72087 6.0066 5.04942 2.9962 1.68848 1.33446 1.215 0.32002 - the
   audit list exactly. My own baseline mirror run (unpatched) reproduces all
   14 with the audit's per-file attribution and a PDF byte-size identical to
   the tracked root PDF (journal sec 3-4).

2. Why (A) works and what it costs. microtype's protrusion/expansion cannot
   remove these boxes because they are bad-fit cases whose interword glue
   cannot supply the needed stretch within the line (Mittelbach's standard
   remedy is exactly an emergency stretch; measured default
   `\emergencystretch = 0.0pt` on this toolchain by probe_default_ec.py, so
   the line is an effective, standard, layout-only global change). It acts on
   EVERY paragraph of the book: paragraphs that previously failed now fit with
   looser glue - observed effect: 12 overfulls vanish, 2 new Underfull \hbox
   badness notices appear (appH L3514, L4033; badness 2005/4132, cosmetic
   looseness, no margin breach), a handful of Underfull \vbox badness counts
   shift by +-1, line/page breaks reflow slightly; staged-pass page count
   stays 448. The task statement's "450 -> 448" was not reproducible from any
   clean baseline (all clean runs 448); the 450 figure matches a run whose
   preamble line was malformed (journal sec 1) - recorded, not hidden.

3. Why (B) and why this wrapper. The 5.04942pt box (ch03 L802-813) is the
   `center`+`tabular{@{}ll@{}}` scales table; its width is col1+col2+2*
   `\tabcolsep` and it exceeds the 5.65in text block by 5.04942pt. Locally
   halving `\tabcolsep` (6pt -> 3pt) shrinks the table exactly 6pt (0.95pt
   clearance) with zero content, font or alignment change; cells stay
   byte-identical. Verified: candidate log shows 0 boxes in the ch03 region.
   Rejected `{\small}` (changes table font size) and `p{}` columns (reflow +
   alignment change of cells) as larger visible changes.

4. Residual (C). The 1.215pt box at appH L3437-3438 persists with byte-ident
   size under 2em emergency stretch, so the breaching list item is an
   unbreakable inline math atom (that paragraph carries several long
   `\det`/`\int`/`\frac` inlines). Emergency stretch cannot shrink an
   unbreakable atom; manual fixes (math edit, paragraph `\small`, `\!`
   insertions) all change math bytes or create visible inconsistency, and a
   hand-tuned break risks a new box elsewhere (reflow whack-a-mole).
   1.215pt = 0.43mm into a 0.45in margin, under the 2pt guard. Decision:
   leave, explicitly recorded.

5. Classification of key statements: (1),(3) and all counts are reproduced
   derivations/measured outputs; (2) "these 12 boxes are glue-insufficient
   fits" is the standard TeX mechanism consistent with the measurement
   (boxes vanish precisely when glue becomes stretchable) - conditional/
   mechanism; (4) unbreakable-atom attribution is standard TeX behaviour plus
   the invariance measurement - conditional; nothing here is a claim about
   physics content.

## Claim classification

- Reproduced identity/derivation: baseline 14-box scan and sizes; candidate
  1-box scan (1.215pt, appH); ch03 region 0; default emergencystretch 0.0pt;
  anchor uniqueness counts; tabcolsep width arithmetic (6pt reduction);
  tracked-tree hash equality before/after; page counts 448/448 (staged).
- Conditional result: "12 of the 14 are glue-insufficiency fits" (evidenced
  by absorption at 2em; mechanism per TeX).
- Mechanism/attribution: residual box is an unbreakable math atom (invariance
  argument above).
- Input: 2pt guard threshold (orchestrator convention, adopted).
- Conjecture: none. Unresolved microscopic step: none (typographic package).

## Proposed changes

### File 1: namcg-book7.tex (preamble)

Anchor (exists exactly once, verified byte count 1; boundary quotes):
start `\setstretch{1.12}`  end (same line). Everything else kept byte-identical.

```latex
\setstretch{1.12}
\setlength{\emergencystretch}{2em}
```

(Second line is the insertion: payloadA-preamble.tex, 36 bytes, CRLF-terminated,
sha256[:12] f4aa60aa4099.)

### File 2: chapters/ch03-matrix-action.tex

Anchor 1 (unique in file, byte count 1): `\begin{tabular}{@{}ll@{}}` - insert
one line immediately before it. Anchor 2 (unique in file, byte count 1):
`\end{tabular}` - insert one line immediately after it. All existing lines,
including every cell of the table, kept byte-identical; the center environment
and booktabs rules unchanged.

```latex
{\setlength{\tabcolsep}{3pt}
\begin{tabular}{@{}ll@{}}
\toprule
Quantity & Role \\
\midrule
\(\LUV\) & kinematic cutoff from \(\Theta^{\mu\nu}\) \\
\(v\) & condensate scale; appears in the working conditional \(\Geff\) parameterization \\
\(\lambda\) & controls the radial Higgs mass \(m_\sigma\sim\sqrt{\lambda}\,v\) \\
\(g_{\mathrm{YM}}\) & internal gauge coupling; enters the connection
                     that eats Goldstones \\
\bottomrule
\end{tabular}
}
```

(The only added bytes are the two wrapper lines: `{\setlength{\tabcolsep}
{3pt}} + CRLF` (30 bytes, 717a15da8b92) before anchor 1 and `} + CRLF`
(3 bytes, e22faa535bd2) after anchor 2; full context diff in
payloadB-ch03.diff, 1026 bytes, 8b2f0ffa435a.)

### File 3: chapters/appH-microscopic-proofs.tex

NO CHANGE - explicit disposition: the residual 1.215pt box (L3437-3438) is
left as accepted (below the 2pt guard; unbreakable atom; see residual
decision above). The author-hold range L3192-3236 is not touched.

No stale passages arise elsewhere: no labels, refs, citations, math tokens or
status text change; TOC/aux regenerate normally in the next build.

## Verification scripts

All under proposals/130-margin-tightening/; pure ASCII; run with `python -I`.

- cert_130.py (9107 B, sha256[:12] 2054773e2663). Run from repo root:
  `python -I proposals/130-margin-tightening/cert_130.py` (~20 s; 3 pdflatex
  passes via -output-directory into scratch/margin-typo/cert/ only).
  Expected invariant final line:
  `CERT130 PASS BASE14 CAND1 CH03SITE0 MAX1.215`
  Sub-assertions: parser positive control fires (canned fake log -> exactly 1
  box at 9.99; malformed-token guard live); region-scanner positive control
  fires (1 in / 1 out); baseline mirror reproduces 14 boxes incl. 5.04942 in
  the ch03 region (site-existence + non-vacuous attribution); candidate:
  rc 0, no `!` lines, total <= 2, max <= 1.25pt, ch03-region 0, no box in
  [5.00,5.10], candidate really read the mirrored ch03 (log trace asserted);
  tracked hashes (book tex, ch03, root pdf/log/aux/bbl/toc/out) unchanged.
- probe_default_ec.py: prints `DEFAULT_EMERGECYSTRETCH EC=0.0pt` (the
  measured default; run inside any writable dir).
- payloadA-preamble.tex / payloadB-ch03.diff: the exact payload bytes
  (hashes above).
Reproduction pack (invariants for the gatekeeper): the CERT130 line; BASE
size list in journal sec 4; `ch03-region: []` in the CAND scan; anchor
byte-counts 1/1/1.

## Decisions Taken

- (B) = local `\tabcolsep{3pt}` wrapper, not `{\small}` not `p{}` columns:
  smallest visible change, cells byte-identical, clears with 0.95pt margin
  and a measured zero-box site. Rejected alternatives listed above with
  reasons.
- Residual 1.215pt: LEAVE with evidence (below guard; stretch-invariant, so
  an unbreakable atom; any one-token fix edits math bytes or introduces
  visible font inconsistency / reflow risk). Fixing it is not required by the
  2pt guard and not worth a new-box gamble - this maximizes the margin quality
  available without any content change.
- Corrected the dispatch's baseline-log pointer (margincheck = pilot; root
  log = baseline) and the "450" baseline page figure with provenance, rather
  than repeating them.
- Route choices (TEXINPUTS mirror, chr(92) construction, region attribution)
  were mine, layout-only, status-neutral.

## Milestone assessment

Routine. No MILESTONE.md trigger: this is a typographic package; no critical-
path step advances, no physics claim changes.

## Status-label recommendation

None. Critical-path list re-derived from the agenda/ledger (A, B, C, D1, E, F,
G-derived, N at full-GR scope) - all labels unchanged by this package.

## Author decision needed

None.

## Remaining open step

- The 1.215pt appH L3437-3438 residual: accepted (decision above). If the
  author later wants it gone, the only clean fixes are a re-typeset of that
  paragraph's display-style inlines (content change) or a scoped `\small` -
  neither is within a typographic-only package.
- Final page count / TOC entries: recorded by the orchestrator's normal
  3-pass build after integration (staged-pass evidence: 448 -> 448).

## Special instructions for the gatekeeper

- This is typography: assert no math token, label, citation, or status text
  changed anywhere; the diff for ch03 must show exactly two added lines and
  zero modified lines; the preamble insertion is one line.
- Re-run: `python -I proposals/130-margin-tightening/cert_130.py` from repo
  root; expect `CERT130 PASS BASE14 CAND1 CH03SITE0 MAX1.215`. It writes only
  under scratch/margin-typo/cert/ and hash-checks the tracked tree itself.
- Verify anchor uniqueness yourself (counts: `\setstretch{1.12}` 1 in
  namcg-book7.tex; `\begin{tabular}{@{}ll@{}}` 1 and `\end{tabular}` 1 in
  ch03). Verify payload byte sizes/hashes (36/f4aa60aa4099; 30/717a15da8b92
  + 3/e22faa535bd2; diff 1026/8b2f0ffa435a).
- Must not be asserted in integrated text: any physics meaning, any
  "overfull-free book" claim (the 1.215pt residual remains), any page-count
  claim beyond "may shift; recorded by the final build". The 2 new Underfull
  \hbox notices (appH L3514/L4033) are the honest cost and should be
  acknowledged if asked, not hidden.
- Re-check specifically: the emergencystretch line acts book-wide (standard
  practice, but it is the one global effect; the reviewer should see no
  change in any math token). Do NOT expect 450 baseline pages; clean runs are
  448 (provenance in journal sec 1).
