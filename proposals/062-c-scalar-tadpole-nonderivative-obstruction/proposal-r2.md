# Proposal 062-c-scalar-tadpole-nonderivative-obstruction, round 2

Supersedes proposal-r1.md (retained for audit; its three magnitude formulas and its post-state hash
573261 B / 4ad691c1… are SUPERSEDED and must not be used). **insert-r1.tex is VOID for integration**
(retained for audit only). **insert-r2.tex is the text to apply.**

## r1 verdict and findings disposition

Gatekeeper review (`review-r1.md`): **ACCEPT WITH REQUIRED REVISIONS**, MILESTONE none, FLAGS none,
PROGRESS first, OPEN 1/0. The core — determinant-profile identity, bounded no-go for
\(\sqrt{|g|}\)-alone terms at \(q=0\), \(\mathcal M=T/4\), \(q_*^2=\tfrac12L\sum_iT_i\), the C-R2
definability/obstruction block, and the worked-example recheck (NO PRIOR-CLAIM-ERROR) — was
independently re-derived and verified; no further re-derivation of the core is expected in r2.

- **F1 (blocking) — addressed.** The F-block magnitude trio used \(L=32\pi^2m^6/A\) with
  \(A=(\hat V+2\hat T)/24\), dropping the recorded \(F\chi^2\). I verified the finding from the source
  bytes myself before changing anything: appH L2750 records \(A=\tfrac1{24}(V+2T)\) (unhatted), L2779
  records \(V=F\hat V\chi^2\), \(T=F\hat T\chi^2\), L2809 records \(L=32\pi^2m^6/A\), hence recorded
  \(L=768\pi^2m^6/(F(\hat V+2\hat T)\chi^2)\). The vacuum chain \(q_b^2=-16\pi^2V_0/(Am^2)\) with
  \(V_0=-F\hat U\chi^4/32\pi^2\) (L2811) then equals the recorded
  \(q_b^2=12\hat U\chi^2/(m^2(\hat V+2\hat T))\) **identically** (script §4, `.out` line 15: `equals
  recorded: True`; with the r1 A it gives \(12F\hat U\chi^4/(m^2(\hat V+2\hat T))\), contradicting L2811
  and the recorded large-\(N\) limit \(\chi^2/m^2\)). The gatekeeper's Corrected snippet was applied
  VERBATIM to block 2 (see Proposed changes). \(\vartheta\) dropped from the conventions sentence, per F1.
- **F2 (minor) — addressed.** `tadpole_minderivative.py` docstring rewritten: §4 now states the division
  reading \(q_b^2=12\hat U\chi^2/(m^2(\hat V+2\hat T))\) and \(q_*^2[U_4]=+6\sqrt{|g|}\hat U\chi^2m^6/
  (\hat V+2\hat T)\) (positive for \(\hat U>0\)); §3 now states the Euclidean-sign relation
  (\(T_t=-\sqrt{|g|}W/2\), \(\mathcal M=-\sqrt{|g|}W/8\)) matching the code; §6 states the corrected
  threshold. Self-consistent with the shipped `.out`.
- **F3 (informational) — recorded, carried to the orchestrator.** The item-60 mandatory full
  `chapters/**/*.tex` literal scan was not completed by the r1 review (context budget); its coverage
  statement (whole-tree structural/symbol scans over all 30 files; IN FULL reads as listed) is carried
  forward. This r2 round performs no additional full scan (revision of an accepted-core package; r2
  changes are confined to three formulas in one block of already-reviewed text plus scripts). The
  compensating full read has not been performed; the orchestrator carries the shortfall.
- **F4 (informational) — no action needed.** Closing-status conventions and non-duplication were
  verified by the review; r2 changes nothing there (block 1 byte-identical; F-block closing status line
  unchanged).

## Result (r2 state, unchanged core, corrected magnitudes)

Established within the stated recorded hypotheses (equal weights, \(V=T\), frozen symbol, product
background, static channel \(q\cdot v=0\), one loop, formal continuation \(S_E=-S_L\), pure-trace
channel): the profile identity \(\sqrt{|g+h|}=\sqrt{|g|}(1+t/2+t^2/16+O(t^3))\);
\(T_i=-\sqrt{|g|}W_i/2\), \(\mathcal M_i=-\sqrt{|g|}W_i/8\), \(\mathcal M=T/4\),
\(q_*^2=\tfrac12L\sum_iT_i\); the bounded no-go that no supplied set of \(\sqrt{|g|}\)-alone terms
(including a cosmological-type counterterm) cancels the \(q=0\) tadpole while leaving
\(\mathcal M\ne0\) (flat \(\Rightarrow q_*^2=0 \Rightarrow\) pole at \(q^2=q_b^2\), tachyonic-signed for
\(\hat U>0\)); candidate localization of the missing \(\mathcal M\) to the (recorded, not computed)
fibre-level response to \(\bar h\) in \(v^M-2\sigma^M\). Corrected conditional magnitudes in the
**recorded** convention: threshold tadpole \(|T|=F\hat U\chi^4/(32\pi^2m^8)\);
\(q_*^2[U_4]=6\sqrt{|g|}\hat U\chi^2m^6/(\hat V+2\hat T)\) (positive for \(\hat U>0\));
\(q_*^2[U_4]/q_b^2=\sqrt{|g|}m^8/2\) — the ratio is independent of \(F,\hat U,\chi\); the magnitude
comparison turns on the conventions for \(m\) and \(\sqrt{|g|}\) and is not settled. Nothing closed;
Problems C, F, N remain OPEN and PROGRAMME-CONDITIONAL. No label change.

## Block-1 (C-block) byte-stability proof

`make_insert_r2.py` asserts `b1_old == b1_new` between `insert-r1.tex` and `insert-r2.tex` and prints:
- block 1: len 2415, **sha256 c8985520d679dcf19a4fa4655a159092aa6c94bfa98cf2df1d9a34461b2d8671**
  (r1) → identical in r2; `simulate_apply_r2.out` echoes prefix `c8985520d679dcf1` for both raw and
  CRLF-converted block C (single line; conversion is a no-op).
- block 1 contains no magnitude formula, so the F1 fix did not touch it. The only other C-block-bearing
  file pair, `example_recheck.py/.out`, is unchanged and reproduces byte-identically on re-run this round
  (`all recorded values reproduced: True`).

## insert-r1 → insert-r2 diff (exactly the gatekeeper's sentence)

`insert-r1-to-r2.diff` (CRLF text in the folder) records the proof. Summary:
- File diff is a single contiguous replacement inside block 2 at byte offset 1665 (bytes 1665..2148 of
  block 2); block 1 and the `%---SPLIT---%` marker line unchanged; both files LF-only.
- Invariants asserted in `make_insert_r2.py`: `insert-r1.tex.count(OLD)==1`; `insert-r2.tex` contains
  OLD 0 times; NEW exactly once; `b2_old == b2_new.replace(NEW, OLD)` round-trip.
- OLD (283 bytes) = the r1 sentence beginning "Conversely the Yukawa threshold ...
  \(|T|=\hat U\chi^2/(32\pi^2m^8)\) ... \(q_*^2=6F\sqrt{|g|}\hat U\chi^4m^6/(\hat V+2\hat T)\); its ratio
  to \(q_b^2\) is \(F\sqrt{|g|}\chi^2m^8/2\), and the comparison of magnitudes turns on the conventions
  for \(m\), \(\vartheta\) and \(\sqrt{|g|}\) and is not settled here."
- NEW (261 bytes) = the gatekeeper's Corrected snippet verbatim:
  "Conversely the Yukawa threshold \(q_*^2=q_b^2\) at \(\hat U>0\) requires an uncancelled tadpole of
  size \(|T|=F\hat U\chi^4/(32\pi^2m^8)\) in the same convention. Second, taken alone and not cancelled,
  \(U_4\) contributes \(\mathcal M=F\sqrt{|g|}\hat U\chi^4/256\pi^2\), of the sign that pulls \(q_*^2\)
  positive for \(\hat U>0\), and \(q_*^2=6\sqrt{|g|}\hat U\chi^2m^6/(\hat V+2\hat T)\); its ratio to
  \(q_b^2\) is \(\sqrt{|g|}m^8/2\), and the comparison of magnitudes turns on the conventions for \(m\)
  and \(\sqrt{|g|}\) and is not settled here."
- Block 2: 3886 → 3864 bytes (rstripped 3863); sha256 55d18e40e5431354… → 84fdd1fa26b7576c…
  (rstripped 1e04cf3bcabbbe53…). `insert-r2.tex`: 6294 bytes, sha256
  db1b3489042db86003bb7fca722175596f398ed1794feddefe0440c22f47d1d9.

## Target and status

Unchanged from r1: Problem C, `chapters/appH-microscopic-proofs.tex` L482-486 verbatim:

    \paragraph{Ledger label.}
    Status: OPEN. Priority: CRITICAL PATH. Completion:
    PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope
    outcome only when its operator, coupling and phenomenological test
    are supplied; it does not by itself meet the matrix-derived criterion.

Chapter 17 criterion (L142-157) unchanged. Nothing in r2 alters any status/priority/completion label.
PROGRAMME-CONDITIONAL.

## Source reading

digest + targeted reads. New targeted reads this round (bytes verified in the current working tree):
appH L2744-2756 (recorded \(A=\tfrac1{24}(V+2T)\) at L2750), L2773-2782 (recorded
\(V=F\hat V\chi^2\), \(T=F\hat T\chi^2\) at L2779), L2805-2814 (recorded \(L=32\pi^2m^6/A\),
\(q_*^2=2\mathcal ML\) at L2809; vacuum term and \(q_b^2\) at L2811; display L2813);
`review-r1.md` IN FULL. appH byte state re-asserted by `simulate_apply_r2.py`: 566953 B, sha256
21737625769589a64090c8b7f93842b1eaa5d12cff3e4877f70f2db8e5947999, CRLF 3415, bare LF 0. bib untouched:
27350 B, sha256 40d6ea09915dd4b8220f30c466821118492ee5560f66930b7c5d9a2dd8b95b90. r1 source list stands.

## Research and reasoning (r2 delta)

The F1 correction is a convention fix, not new physics. With the recorded
\(A=F(\hat V+2\hat T)\chi^2/24\):

1. \(L=32\pi^2m^6/A=768\pi^2m^6/(F(\hat V+2\hat T)\chi^2)\) (`.out` line 13).
2. \(q_b^2\) chain: \(-16\pi^2V_0/(Am^2)\), \(V_0=-F\hat U\chi^4/32\pi^2\)
   \(\Rightarrow F\hat U\chi^4/(2Am^2)=12\hat U\chi^2/(m^2(\hat V+2\hat T))\) — the recorded L2811
   value, identically (line 15); r1's \(A\) gives \(12F\hat U\chi^4/(m^2(\hat V+2\hat T))\to F\chi^4/m^2\)
   at large \(N\), contradicting the recorded \(\chi^2/m^2\) (line 19 reproduces \(\chi^2/m^2\) in the
   recorded convention).
3. \(q_*^2[U_4]=2\mathcal M_E[U_4]L=2\cdot\frac{F\sqrt{|g|\hat U\chi^4}}{256\pi^2}\cdot
   \frac{768\pi^2m^6}{F(\hat V+2\hat T)\chi^2}=\frac{6\sqrt{|g|}\hat U\chi^2m^6}{\hat V+2\hat T}\)
   (line 17); the \(F\) cancels, so the \(\mathcal M\) sign statement is unchanged and positive for
   \(\hat U>0\).
4. Ratio: \(\frac{6\sqrt{|g|}\hat U\chi^2m^6}{\hat V+2\hat T}\cdot
   \frac{m^2(\hat V+2\hat T)}{12\hat U\chi^2}=\frac{\sqrt{|g|}m^8}{2}\) (line 18) — independent of
   \(F,\hat U,\chi\); hence \(\vartheta\) also drops from the conventions sentence.
5. Threshold: \(|T|=2q_b^2/L=q_b^2A/(16\pi^2m^6)=F\hat U\chi^4/(32\pi^2m^8)\) (line 28);
   \(|T_{\rm need}/T[U_4]|=2/(\sqrt{|g|}m^8)\) (line 29), the same condition
   \(\sqrt{|g|}m^8\gtrless2\) as the ratio test.
All other r1 derivations are untouched (lines 1-11, 21-27 unchanged in content from the r1 .out).

## Claim classification (delta)

- Recorded \(A,V,T,L,q_b^2,V_0\) data: **input** (quoted manuscript data; verified in bytes this round).
- Corrected trio (\(|T|=F\hat U\chi^4/32\pi^2m^8\); \(q_*^2[U_4]=6\sqrt{|g|}\hat U\chi^2m^6/
  (\hat V+2\hat T)\); ratio \(\sqrt{|g|}m^8/2\)): **conditional result** (established algebra in the
  recorded convention; convention-bound magnitudes).
- Everything else: unchanged from r1 (core: established/conditional as listed there and endorsed by the
  r1 review's "Scope of what is established").

## Proposed changes

Same two insertions as r1 into `chapters/appH-microscopic-proofs.tex`, now with **insert-r2.tex** as the
byte content (block 1 as in r1, unchanged; block 2 with the gatekeeper-corrected sentence). No bib
changes; no new labels; all cross-references verified in r1 and unchanged. Anchors, offsets and apply
rule per the review's Apply rule: appH pre-state as above; anchorC
`tensor operator or the remaining scalar couplings.` unique at X_C=144554 (following bytes asserted);
anchorF `\r\n\r\n\section{Problem G: HBEV}` unique at X_F=539217 (preceding bytes end
`PROGRAMME-CONDITIONAL.`); single ascending pass `out = app[:144554] + b"\r\n\r\n" + pc +
app[144554:539217] + b"\r\n\r\n" + pf + app[539217:]`, `pc, pf` CRLF-converted, `pf` from rstripped
block; LF→CRLF. **Predicted post-state (r2, authoritative): size 573239, sha256
08a61b890e33dedf9c3122912c8e4ea6c113fe95396fa4220136d3417b49b9eb, CRLF 3419, bare LF 0.** The r1
post-state (573261 B / 4ad691c1…) certified the uncorrected insert and is void. Stale passages: none;
r1's superseded numbers appear only in superseded process files (proposal-r1.md, insert-r1.tex,
simulate_apply.py/.out — all retained for audit, not for integration).

## Verification scripts

All in the proposal folder (`python -I` from it):
- `tadpole_minderivative.py` / `.out` (r2, regenerated): §§1-6 as in r1 with the recorded
  \(A\)-convention; new §4 cross-derivation `equals recorded: True` (line 15) and the r1-A counterexample
  printed as `wrong`; line map: 3-4 profile; 5 rank-one; 7 U2 match; 9-11 \(T,\mathcal M,q_*^2=\tfrac12LT\);
  13 \(A,L\); 14 \(q_b^2\); 15 chain; 16 \(\mathcal M_E[U_4]\); 17 \(q_*^2[U_4]\); 18 ratio
  \(\sqrt{|g|}m^8/2\); 19 large-\(N\) \(\chi^2/m^2\); 22-23 saddles; 26 \(\Lambda_{\rm ct}^*\);
  27 flatness \(q_*^2=0\); 28 threshold; 29 ratio-to-\(T[U_4]\).
- `make_insert_r2.py`: builds insert-r2.tex from insert-r1.tex by the single asserted replacement;
  writes `insert-r1-to-r2.diff`; prints block hashes.
- `insert-r1-to-r2.diff`: the diff record (offset, invariants, OLD/NEW sentences).
- `example_recheck.py` / `.out`: unchanged; re-run this round reproduces byte-identically.
- `simulate_apply_r2.py` / `.out`: apply simulation against the current appH pre-state; prints block
  hashes (C block prefix c8985520d679dcf1, identical to r1; F rstripped 3863 B prefix 1e04cf3bcabbbe53),
  anchor uniqueness/offsets/following-preceding bytes, junction checks, content checks (corrected
  threshold at 543411, corrected \(q_*^2[U_4]\) at 543642, corrected ratio at 543695 — all present;
  stale r1 threshold formula absent; F end junction at 545445), post-state 573239 B / 08a61b89… /
  CRLF 3419 / bare LF 0; bib echoed unchanged.
- `simulate_apply.py` / `simulate_apply.out`: VOID (r1, superseded), retained for audit.

Numbers traceability for insert-r2 (each value → `tadpole_minderivative.out` line):
\(1+t/2+t^2/16\) → 3-4; \(-\lambda^2/8\) → 5; \(T_i,\mathcal M_i\) → 9; \(q_*^2=\tfrac12L\sum T_i\) → 11;
\(|T|=F\hat U\chi^4/(32\pi^2m^8)\) → 28; \(\mathcal M=F\sqrt{|g|}\hat U\chi^4/256\pi^2\) → 16;
\(q_*^2=6\sqrt{|g|}\hat U\chi^2m^6/(\hat V+2\hat T)\) → 17; ratio \(\sqrt{|g|}m^8/2\) → 18;
\(q_*^2=0\) at flatness / \(\Lambda_{\rm ct}^*\) → 26-27; \(q_*^2=2\mathcal ML\), display denominator,
\(A,L,q_b^2,V_0\) → quoted from appH L2809/L2813/L2750/L2779/L2811 (cross-checked at lines 13-15, 19).

## Decisions Taken

1. Adopted the recorded \(A=(V+2T)/24\), \(V=F\hat V\chi^2\) convention everywhere after independently
   verifying the three source lines (L2750, L2779, L2809); rejected keeping the r1 hats-only \(A\)
   (it contradicts the recorded \(q_b^2\) and its large-\(N\) limit — F1).
2. Applied the gatekeeper's Corrected snippet **verbatim**, including \(\sqrt{|g|}\) LaTeX and the
   \(\vartheta\) removal; rejected paraphrase.
3. Kept `insert-r2.tex` clean (no VOID comment inside the .tex); VOID is recorded in this file and in
   `insert-r1-to-r2.diff`, so the shipped diff contains only the mandated sentence change.
4. Replaced the failing slice-based diff assertions in `make_insert_r2.py` with exact count/round-trip
   invariants (OLD once in r1, zero in r2; NEW once in r2, zero in r1; round-trip replace) — the
   slice form was wrong because OLD and NEW share a long common prefix and suffix; the shipped invariants
   are the rigorous statement that the only change is the sentence.
5. Fixed one stale printed line in the r2 script (`|T_need/T_t[U4]|` substitution silently failed on the
   pre-simplified W); now computed directly as \(-U_4/2\), giving \(2/(\sqrt{|g|}m^8)\), consistent with
   line 18.

## Milestone assessment

**Routine** (unchanged): no trigger in MILESTONE.md; bounded computed obstruction + missing-step record;
060/061 precedent. The r1 review confirmed MILESTONE: none.

## Status-label recommendation

Critical-path set re-derived from ch17/Appendix H: {A, B, C, D1, E, F, G-derived, N}. **No label
changes.** C remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; F, N unchanged.

## Author decision needed

None.

## Remaining open step

Unchanged from r1: closure of C needs the full gauge-fixed quadratic scalar operator on a constructed
frame (kinetic coefficient incl. induced EH, mixing, non-minimal and matter couplings, pole mass,
comparison-grade coupling) with `ass:gap-psi` discharged and \(G_{\rm eff}\) derived (F). Within the
trace-channel thread the ranked open avenues are those of review-r1: (1) fibre-level response to
\(\bar h\) in \(v^M-2\sigma^M\); (2) tree non-derivative terms at \(q=0\) incl. \(\chi^2\lesssim\vartheta\)
second-order terms; (3) C-R3 operator-class/basis-invariance analysis of the trace–tensor mixing;
(4) classes outside the recorded hypotheses (rotating class, higher loops, non-equal weights, unfrozen
symbol) where the no-go does not bind; (5) the Problem-F route to \(G_{\rm eff}\).

## Special instructions for the gatekeeper (r2)

- No re-derivation of the r1 core is requested (r1 review verified it). r2 must check: (a) the three
  corrected formulas against the recorded convention — two-line algebra:
  \(2\cdot\frac{F\sqrt{|g|}\hat U\chi^4}{256\pi^2}\cdot\frac{768\pi^2m^6}{F(\hat V+2\hat T)\chi^2}
  =\frac{6\sqrt{|g|}\hat U\chi^2m^6}{\hat V+2\hat T}\); \(\frac{2q_b^2}{L}=\frac{F\hat U\chi^4}{32\pi^2m^8}\);
  ratio \(=\sqrt{|g|}m^8/2\) — and that the recorded \(q_b^2\) chain (L2750/L2779/L2811) forces this
  convention; (b) block-1 byte identity (sha256 c8985520d679dcf19a4fa4655a159092aa6c94bfa98cf2df1d9a34461b2d8671
  in both rounds) and that insert-r1→insert-r2 differs only by the mandated sentence (count/round-trip
  invariants printed by `make_insert_r2.py`, record in `insert-r1-to-r2.diff`); (c) re-run
  `simulate_apply_r2.py` and match post-state 573239 B / sha256
  08a61b890e33dedf9c3122912c8e4ea6c113fe95396fa4220136d3417b49b9eb / CRLF 3419 / bare LF 0 (if appH
  moved, re-anchor via the same assert-once anchors and re-simulate); (d) F3 full-scan shortfall stands
  and is carried by the orchestrator, not cured by this round.
- Must not be asserted: closure or narrowing of Problem C; extension of the no-go beyond the stated
  hypothesis class; that any magnitude comparison was settled (ratio \(\sqrt{|g|}m^8/2\) is
  convention-bound); that \(t\) is an emergent-metric quantity; any label change.
- insert-r1.tex and simulate_apply.py/.out and the magnitude trio in proposal-r1.md are VOID/superseded;
  do not integrate them.
