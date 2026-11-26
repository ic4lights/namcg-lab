# Chain 119 stage-3 working notes (proposal assembly)
Started 2026-11-23. Folder: proposals/119-d1-selection-underdetermination/.

## Baseline (re-verified 2026-11-23, stage 3)
chapters/appH-microscopic-proofs.tex: sha1[:12] 2ed53c7778c1, size 843649 B.
Anchor `\section{Problem E: signature}`: count 1, byte offset 290106. MATCHES dispatch pin.
Canonical splice: replace(anchor, payload+CRLF+anchor, 1); POST = 843649 + len(payload) + 2.
Payload: insert-overdetermination-r1.tex, 4704 B, sha1[:12] 3b4c2d0794a9.
POST: 848355 B, full sha1 eaea0964e7f50c27c24540b9ac523c443af873d7.

## Live reads done (targeted)
- appH L765 `\section{Problem D: local Lorentz}`, ledger label para: Status OPEN / CRITICAL PATH /
  PROGRAMME-CONDITIONAL, D2 reduced-scope note.
- appH tail before anchor: 116-era composite para (L1708), vacuum-nondegacy para, state-route para
  ("...remains the missing input of Section~\ref{sec:ch3-relate}..."), 117 Gibbs para ("...remains the
  upstream input that gates what any Presentation-B measure can be cited as..."), 118 constraint para
  (L1718, ends "...nothing in this paragraph closes Problem~D, Problem~D1, or Problem~A.").
  Payload lands between the 118 para and the anchor. Purely additive `\emph{...}` paragraph, 118 register.
- ch17 L329-360: Problem D paragraph (D1 closure requires omega/A_mu/B/ghost operators + field content
  specified; frame existence/non-degeneracy derived from microscopic data).
- ch03: eq:Smatrix L142-157 (three terms, S_matter symbolic, no Phi); eq:V L240-245; eq:Smicro L220-228;
  ass:dictionary L345-363 ("matching condition, not an established result"), "most important unproved bridge".
- Labels verified defined exactly once in chapters/ch03-matrix-action.tex: eq:Smatrix(143), eq:Smicro(221),
  eq:V(241), eq:Phi-eom(310), sec:ch3-relate(335), ass:dictionary(346). No Problem D1 section exists in
  appH; D1 referenced via Chapter agenda (L754, 918, 1071, 1232, 1708). Payload refers "Problem~D1" as text,
  matching the 118 paragraph's usage.

## Stage-2 record discrepancies FOUND (report, do not fix)
1. Repo-root stray `out-q4.txt` (176 B) is a failed-run traceback (python can't open q4_su4.py),
   NOT the stage output; real output is scratch/119/out-q4.txt (51 B). Root file left untouched.
2. scratch/119/out-s7-m1.txt crashed at the su(3) orthonormal assert; the current s7_m1.py does NOT
   crash there (fast path out-s7-m1b.txt passes it), so out-s7-m1.txt is stale w.r.t. the current
   script. su(3)=(7/3,1/9) comes from out-s7-m1b.txt. verify_r119.py re-derives all of it from scratch.
3. notes.md S7.1 line "disc/1024 = ..." mixes b and b/4 normalizations; the correct exact statement
   (re-derived in verify_r119): real fixed rays iff (w - v4 - 8(n+4))^2 > 32*96*(n-1/2) *? see verifier;
   n=4 form (w-v4-64)^2 > 10752 confirmed numerically there.
4. Dispatch said the .bbl is "tracked"; live check: namcg-book7.bbl EXISTS in the working tree but is
   git-IGNORED (not in git ls-files). cert-r119p.py copies the working .bbl explicitly; the temp tree
   is tracked-files minus root PDF minus reports/ plus that .bbl (2945 files).
5. Stage-2 blanket "no fixed ray for any N" is only exact for n>=4: w*(2)~115.9 and w*(3)~143.6 lie
   BELOW 16 pi^2 ~ 157.91, so a window-internal strong-coupling fixed ray is not excluded at n=2,3 by
   the discriminant alone. Payload states the exact iff and the n=4 window corollary only; D9 prints
   w*(n) for n=2..6 as informational.

## Plan
1. verify_r119.py -> out-r119.txt (fresh): re-derive tensor/gauge/beta/cutoff/Moyal teeth across full
   ranges n=2..6 + OFF-DEFAULT two-root tooth w=200,v4=0 -> r=3/14,1 (predicted exactly).
2. gen_payload_119.py (join guard r'\\[A-Za-z]+$' + positive control FIRES + negative control passes +
   hygiene asserts) -> insert-overdetermination-r1.tex; rerun byte-identical.
3. cert-r119p.py: fresh out-of-repo temp tree, HARD asserts (pin/anchor/hash/POST), 2x pdflatex, CERT PASS.
4. proposal-r1.md, manifest.md.
5. 118 record fixes: copy proposal-r1.md -> proposal-r1-superseded-F1F2.md, then F1 (x=(1/sqrt(2eps),0,0,0)),
   F2 (sigma^2=w^2=...), record old/new sha1/size in 118 manifest.

## Payload numbers -> sources (rule 7)
256/96/3-8: scratch out-q3/out-s7-m1 + out-r119; 0 vs 1/56: out-q2/out-q4 + out-r119 (orthonormality
asserted); P quadratic, P(0)=96+B_G w: out-s7-m1b + out-r119; threshold 10752, w*=64+16 sqrt(42),
w=200 -> r=3/14,1: out-r119 (new); K3=64,K2=136, C_u(n)=n, C_su=(n^2-1)/n: out-s7-m2 + out-r119;
Moyal collapse 0: out-s7-m3 + out-r119; 16 pi^2 ~ 157.9: universal constant computed in out-r119.

## Status log (updated 2026-11-23, late session)
[x] baseline verified  [x] live reads  [x] notes written
[x] payload+generator (gen rerun byte-identical; GEN OK 119)
[x] cert (CERT PASS, CERT-EXIT=0, out-cert-r119p.txt raw)
[x] 118 record fixes (superseded copy 4a6fa455daa2/48887; F1+F2 applied; r1 now b6c55d51a73f/48902;
    118 manifest section 10 appended, manifest 8df4f47c7d19/13057)
[~] verify: fresh background run b9lr1490k writing out-r119.txt; all lines PASS through B1 n=5 so far
[x] proposal-r1.md written (TOTAL count + D9 values to be filled from final out-r119.txt)
[ ] manifest.md (after out-r119.txt finalizes; excludes __pycache__ - stale dir from an early
    pre-`-B` run, removal denied by permission hook; repro commands all use -I -B so no new cache)

## Verifier run-1 (out-r119-run1-fail.txt): 59/61, two CHECK-SIDE bugs, fixed, rerun bg2lr6ygl
- D4 FAIL: grid point (0,60) is OUTSIDE the window ((0-60-64)^2 = 15376 > 10752), so the interior
  antecedent was false at that point and the conjunction failed. Mathematics unaffected: the claim
  "(w-v4-64)^2 < 10752 (interior) => disc<0, LC>0 => no real fixed ray" is exact (D3, BG=0).
  Fix: grid -> (0,30) interior ((0-30-64)^2 = 8836 < 10752); message now states all 8 points interior.
- G3 FAIL: Wst = dstar(...).trace() is a SCALAR; the check compared it to sp.zeros(2,2), always False.
  Standalone recheck (this session, sympy): theta^2 coeff of W_star at zero gradients == 0 EXACTLY,
  and the theta^1 zero-grad part == 0 EXACTLY too (new companion check G3b). G1 collapse re-confirmed
  scalar diff == 0. No payload change (line 8 claim "O(theta) total derivative, O(theta^2) pure
  derivative operator" is exactly what G1/G2/G3/G3b support at constant Phi).
- D9 line (run-1, values unaffected by fixes): w*(n): n=2:115.88, n=3:143.64, n=4:167.69, n=5:189.58,
  n=6:209.98; 16 pi^2 = 157.91 (matches proposal text).
- Failed raw capture kept as out-r119-run1-fail.txt (never hand-edited); fresh capture goes to
  out-r119.txt from the patched verify_r119.py.
- Run 2 result (fresh out-r119.txt, raw): TOTAL 62/62 PASS, ALL CHECKS DONE 119 (61 + G3b).
- proposal-r1.md finalized (TOTAL 62/62, fix history in Verification scripts + Decisions);
  manifest.md written (self-hash token rule documented and self-checked).

## Round 2 (2026-11-23, required revisions after review-r1 ACCEPT WITH REQUIRED REVISIONS)
Baseline re-verified live before byte work: appH sha1[:12] 2ed53c7778c1, 843649 B; anchor count 1 @ 290106. MATCH.

### Supersession (byte-for-byte copies made BEFORE editing; pins old -> new)
- insert-overdetermination-r1-superseded-r1.tex = old payload 3b4c2d0794a9/4704; new payload c085c19cba68/5191.
- proposal-r1-superseded-r1.md = old 23535 a9316eba486e (superseded by proposal-r2.md).
- gen_payload_119-superseded-r1.py = old 7804 15cbff8eb70f; patched gen 8291 2242d21eacc5.
- Stale insert-overdetermination-r1.tex (old bytes, preserved in superseded copy) deleted before the
  first regeneration run so the generator's byte-identity assert compares the NEW round's runs.

### Actions applied (exact review-r1 required actions; option (a))
- F-1: rays iff `>=` with single marginal double ray at equality; window clause `0<=w<64+16sqrt42`.
  Re-derived independently (scratch, sympy): disc(w*)=0 exact; P(r*)=P'(r*)=0 with r*=sqrt(42)/14 and
  exactly one distinct root at w*; disc<0 at w=160,167.69; disc>0 at w=168.
- F-2 option (a): displayed beta system labeled u(4) instance (A_G,B_G)=(4,0); su(4) channel data
  A_G=N-2/N=7/2 with B_G=1/16 stated OUTSIDE the displayed pairing; "both give thresholds above 16pi^2".
  Independent re-derivation: generalized system beta_c3 with +A_G w gives
  P=448r^2+(256+4v4-A_G w)r+96+B_G w and disc=16[(64+v4-(A_G/4)w)^2-10752-112B_G w] (exact sympy).
  su(4) threshold: solve((7/8 w-64)^2-10752-7w=0) -> w = 544/7 + 32 sqrt(705)/7 = 199.0941...;
  RIGOROUS bound: for 0<=w<=158, |(7/8)w-64| <= 297/4 and (297/4)^2 = 88209/16 = 5513.0625 < 10752,
  so no rays on [0,158] and 16pi^2 < 158  =>  w*(su4) > 16pi^2 with no floating point.
  u(4): 64+16sqrt42 > 16pi^2 exact. Printed-form (A_G=4,B_G=1/16) instance: 173.3879 > 16pi^2 (D3b family).
  Verify pack UNCHANGED per dispatch (option (a)); raw recapture to out-r119-r2.txt (new file).
- F-3: shift clause scoped to commutators-only lifts; eq:Smicro lift (D_mu Phi = partial_mu Phi - i A_mu Phi,
  left mult on the I index; live ch03 L214-227 verified) and the dictionary bridge stated NOT shift-covariant;
  scope sentence "minimal shift-symmetric lift" -> "commutator-type lift". Re-derived: left-mult lift defect
  D(Phi+kI) - D Phi = -kappa A != 0 (exact); commutator lift [A,Phi+kI]=[A,Phi] (exact); bridge LHS [X,Phi]
  invariant, RHS i Theta D Phi shifts by +kappa Theta_{mu nu} A^nu (ass:dictionary L352-356 read live).
  Bridge named via Assumption~\ref{ass:dictionary} (label unique; keeps the reference set inside the
  dispatch-enumerated list; eq:dictionary is the equation inside that assumption, also unique).

### Trace macro decision
namcg-book7.tex L104 defines 
ewcommand{\Tr}{\operatorname{Tr}}, so gatekeeper-snippet \Tr compiles, but
appH uses \operatorname{Tr} 88x vs \Tr 2x (\mathrm{Tr} 22x, incl. the adjacent 118 para) and the 119 payload
uses \operatorname{Tr}; kept \operatorname{Tr}X^2 in the new sentence (manuscript + payload-internal match).

### Artifacts (round 2)
- payload insert-overdetermination-r1.tex 5191 B c085c19cba68 (full c085c19cba683ff3aa832ac36a1c6b7075ba8d63);
  gen x2 byte-identical, GEN OK 119; join guard regex literal re-extracted from patched gen and proven to
  FIRE on injected dangling \secti (positive control) and pass on the payload (negative control).
- POST 848842 = 843649 + 5191 + 2, full sha1 9e0b198af2c3c7f11454980ec6df2e875fbb80ef.
- cert-r119p.py re-pinned (2de50b85d266/4555, POST sha1 now printed full); output out-cert-r119p-r2.txt.
- Labels re-verified unique book-wide: eq:Smatrix, eq:Smicro, eq:V, eq:LUV-def, sec:ch3-relate,
  ass:dictionary, eq:dictionary (last defined but NOT referenced by the payload).

## Round 2 addendum (2026-11-23, final)

- Verify recapture: verify_r119.py (PID 18412) exited 0. out-r119-r2.txt final: 6476 B,
  sha1 009de59d50acc04af0247dc057e94277f13a72d4, cmp exit 0 (byte-identical to out-r119.txt),
  ends TOTAL 62/62 PASS / ALL CHECKS DONE 119. The run wrapper's appended 14-byte
  VERIFY-EXIT=0 status line (file then 6490 B; the exit line is preserved in the job wrapper
  log) was removed by head -c 6476 truncation ONLY after cmp -n 6476 proved the verifier
  prefix byte-identical to out-r119.txt; no verifier byte was added, changed, or deleted.
  The 0-byte err-verify-r2.log was removed.
- Byte repair: the pre-append notes.md (fe9147ac6e45/10677) contained one 0x0D byte at offset
  9452 - the documented stray CR was in fact a backslash eaten as a CR escape by a prior
  python-string append, corrupting Assumption~REF-of-ass:dictionary into Assumption~<CR>ef.
  Restored to a literal backslash-r-e-f (byte-level replace, asserted count 1); file now
  zero CR bytes. This affects notes.md prose only; no artifact or manuscript byte involved.
- proposal-r2.md finalized: 28037 B sha1[:12] 824ba35e90f6 (guarded edits: beta-clause
  renderings v4 -> v_4 to match the payload; capture procedure documented; identity statement
  set to confirmed). Earlier draft 27569 B 8aa711e2232f superseded before first manifest pin.
- review-r1-addendum.md (c8621a1e0549/2190) read and confirmed spec-neutral: restates
  F-1/F-2/F-3 exactly as implemented, retracts its own appended-line determinism artifact,
  verdict ACCEPT WITH REQUIRED REVISIONS stands.


## Addendum 2026-11-23 (chain 120 stage 2)

Record-only disclosures from the chain-120 audit of this folder. Nothing above this line
was altered; this section was appended by byte write.

(1) Second undisclosed escape artifact in this file, line 123: the trace-macro note
begins "ewcommand{...}" because a prior python-string append turned "\newcommand" into
LF + "ewcommand" (backslash eaten as an escape). Same failure class as the documented
0x0D byte repair recorded in manifest.md line 52. Documentation-only: no number, claim
or pin in this folder depends on the mangled line.

(2) Corrected trace-macro census for appH, superseding the "88x vs 2x" figures of
proposal-r2.md line 54 and line 237 and manifest.md line 85. Verified 2026-11-23 with
proposals/120-commutator-lift-bridge/census_trace120.py on live appH bytes
9e0b198af2c3/848842 (post-119 integration) and on the pre-integration reconstruction
(live minus the 119 payload block, exact removal asserted in the script):
pre-integration \operatorname{Tr} 138, \mathrm{Tr} 25, standalone \Tr 2 (both
"\Tr\rho_D^n", appH lines 3235 and 3250, Problem N replica subsection);
live post-integration 156 / 25 / 2 (the 119 payload adds 18 \operatorname{Tr}).
The 119 figures were wrong on the operatorname count (138, not 88) and omitted the
\mathrm{Tr} category (25); the "\Tr 2x" count is confirmed. The register decision
(payload uses \operatorname{Tr}) is unaffected and strengthened: dominance 138 : 25 : 2.

(3) scratch/119/out-s7-m1.txt (pin ccfc557ff99d / 808 B) is stale relative to its
script, per the chain-120 stage-1 audit; record-only, no integrated 119 content derives
from it.
