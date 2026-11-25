# Journal 127-n-dict-kinetic-sign

## T0 (2026-11-25) - pins
- Asserted proposals/127-n-dict-kinetic-sign ABSENT, created folder.
- sha1 pins (live bytes):
  - chapters/appH-microscopic-proofs.tex = 123108d4a94723be1dbad752883125baac940fe4 (4144 lines)
  - chapters/ch17-agenda.tex = 23bd98d96532c2e20939aced3c107c052c10be45 (793 lines)
  - reports/graph/frontier.yaml = 256c37c88162e74acb04fc1eeb5c4159c6f82f32
  - scratch/digest.md = c7fe588c0d0e0c6fb9c7706c883b065ba5a41f89
  - 121-n-hmassive-threshold r1 = a237b756fffd..., r2 = d6324d428eb9...
  - 124-n-mqm-pos r1 = 601a08139360..., r2 = 92d23ed21ed4...
- Dispatch pins agree for appH and frontier.

## T1 (2026-11-25) - source reads
- digest: scratch/digest.md c7fe588c (stale-freshness caveat noted; live bytes re-hashed).
- READ IN FULL (live): appH L3872-4144 (Problem N complete ledger entry incl. 067 sublemma L3987-4023, 124 paragraph L4025, completion-class L4027-4055, deferral L4058-4072, 121 paragraph L4074-4132); ch17 L497-516 (N target), L650-676 (order, A/E premise note), L693-740 (DERIVED criterion + item 8); ch03 L120-364 (eq:NC/LUV, eq:Smatrix L142-157 with -1/(4g_YM^2), S_matter unnamed L155+L166-170, def:matrix-coords-ext L172-205 incl. K^{mu nu}=theta^{alpha mu} g_{alpha beta} theta^{beta nu} L192 and explicit non-identification L199-204, eq:Smicro L220-228, sign note L233-237, eq:V, ass:frame-lock, eq:Phi-transform L279-289 "puts in by hand", sec:ch3-relate, ass:dictionary L345-363); ch04 L140-199 (def:composite-metric/eq:g-from-e, ass:nondeg) and L300-334 (ass:lorentzian); ch05 L55-99 (eq:convert, ass:locked-block); ch09 L40-167 (eq:W4, thm:ostro, eq:stelle, ass:EFT-a2 + compositeness para L147-151, UV list L156-167); ch01 L170-212 (item 6 = "Ultraviolet control"); appA L55-159 (eq:appA-a0/a1/a2, sector sums, eq:appA-Wexp).
- READ IN FULL: proposals/124-n-mqm-pos/review-r2.md (ACCEPT r2, avenues ranking (1) ass:dictionary kinetic-sign = unique transfer step); review-r1.md L25-40 (unresolved list keeps ass:dictionary kinetic-sign open; lift no-go scoped to "that lift"); frontier.yaml L1430-1542 (N gap, N.dict-kinetic-sign edge verbatim rows, routing flag STRUCTURAL->fundamentality); 121 proposal-r2 Result; 121 folder listing.
- BY POINTER only: proposals/124 proposal-r1/r2 bodies (review-r2 summarizes), proposal/manifest of 067 (ledger status quoted in frontier + integrated text read in appH directly).
- Live convention sanity check (quick, pre-script): K = Theta^T eta Theta = diag(th_p^2, th^2, th^2, -th_p^2) symmetric; K = lam*eta solvable iff th = +/- i th_p (non-real); det Theta = th^2 th_p^2.

## T1b - CRITICAL finding: partial integration of the core obstruction
- appH L1735 (120-commutator-lift-bridge, integrated; D1 section): recorded lift
  -(kappa/2)\int g^{mu nu}Tr([X_mu,Phi]_star[X_nu,Phi]_star) has kinetic tensor proportional to
  K^{mu nu} of def:matrix-coords-ext; "K = c g admits no real solution with Theta != 0" (recorded
  statement); "for purely spatial Theta the tensor K is degenerate, so Phi carries no time-derivative term."
- appH L2711-2744 (Problem F section, conjugate-coordinate class): recorded theorems - G=K^{-1} is
  not g, pointwise, ANY real Lorentzian g, D>=4, any fibre/average; K != c eta^{-1} for every c!=0;
  for any nondegenerate real Lorentzian g_L on leaf dim 2m>=4, (theta^T g_L theta)^{-1} not proportional
  to g_L (Pfaffian/determinant + totally-null-eigenspace proof). 2D exception K=-4g^{-1} for 2-metric.
- ch03 L199-204 records non-identification + cites app:status for K^{-1} nowhere proportional to g.
- DELTA of 127 over recorded: (1) K is ALWAYS Lorentzian (det K = det(eta) det(Theta)^2 < 0) - K is not
  a failed metric, it is a competing one; (2) SPACELIKE LEMMA: (K^{-1})(d x^0,d x^0) = det(K_sp)/det K
  = |b|^2 (E.b)^2 / det(Theta)^2 > 0 for every real nondegenerate Theta (det K_sp = -|b|^2(E.b)^2 via
  K_sp = |b|^2 I - EE^T - bb^T, determinant lemma), nondegenerate <=> E.b = pf != 0; hence g0-time is
  strictly K-spacelike => K-type energy unbounded below relative to ass:lorentzian time for EVERY
  normalization kappa and sign; (3) full real solution set of the 2-parameter transfer family
  alpha*K + beta*S2*g0^{-1} = c*g0^{-1}: none with Theta nondegenerate (scalar-mixed-square no-go);
  complex solutions = (anti-)self-dual class only (unique escape, contradicts def:matrix-coords Hermitian
  + ass:lorentzian); (4) light-cone corollary (matching even the causal structure = proportionality);
  (5) CONSEQUENCE: ass:dictionary's "including its sign" clause is unsatisfiable on core data for
  eta/g0-contraction transfers => datum, not open derivation; N input chain resolved.
- Decision: N-mode negation package + structural redaction/extension of the ass:dictionary sign clause
  (ch03 L358-361) + appH N-section record paragraph before "\paragraph{The named completion class...}".
  No-go hypothesis class H1-H6 incl. exclusion of C-inserted transfers (open data escape).

## T2 - verification scripts (all green)
- verify_dict_sign_127.py: 30 checks (S0 sanity, S1 Lorentzian+non-proportional,
  S2 spacelike lemma with exact identities detKsp=-|b|^2 pf^2, (K^-1)_00=|b|^2/pf^2,
  S3 trace-insertion extension = s*eta shift only, S4 cone/positivity criterion,
  S5 plain vs dagger contractions = +/- eta-K-eta (raised +/- K); 8 POS-CONTROLs.
  Run python -I: ALL PASS (30). Capture capture-verify-r1.txt.
  Bug found while developing: tool transfer collapses backslash-backslash to one
  backslash; "\ref" in python source -> CR escape. Anchors script rebuilt with
  chr(92) needles.
- verify_anchors_127.py: A1-A7, ALL PASS. Unique anchors: ch03 matching-condition
  sentence; ch03 "including its sign in the signature"; appH paragraph head
  "The named completion class and the remainder bound."; appH kinetic-sign input
  sentence (124 paragraph, L4025). CRLF confirmed in both target files.
- Key derivations (hand, symbolic-checked): K = Theta^T g0 Theta congruent to g0 =>
  Lorentzian; K = lam g0-impossible: A:=Theta eta, A^2 = -K eta, if K = lam eta
  then A^2 = -lam I => det A = lam^2 >= 0 but det A = det(eta) det Theta = -pf^2
  => pf = 0; complex escape = (anti-)self-dual q = +/- i p (S1h witness);
  (K^-1)_00 = det Ksp / det K = (-|b|^2 pf^2)/(-pf^4) = |b|^2/pf^2 > 0 strict
  (pf = E.b != 0 => b != 0); positivity criterion: energy of K-type kinetic term
  bounded below iff time direction inside cone of K; cone(C_g subset C_K => equal
  => proportional) = Lorentzian-cone maximality (standard).
- Dependency resolution found: 124 paragraph (appH L4025) lists the kinetic-sign
  content of ass:dictionary as the FIRST of three pinned inputs of the N sublemma
  hypotheses; the Presentation-B MQM class realizes the sublemma WITHOUT any
  transfer, so the transfer no-go does not weaken the 124 realization; it only
  bars the Presentation-A supply route named by frontier edge N.dict-kinetic-sign.

## T3 - payload + proposal assembly
- P1: ch03-matrix-action.tex, insert one sentence after the unique anchor
  "this is a matching condition, not an established result." (same paragraph).
- P2: appH-microscopic-proofs.tex, new ledger paragraph inserted immediately
  before unique head "\paragraph{The named completion class and the remainder
  bound.}" (L4027).
- proposal-r1.md assembled from chunks; backslash bytes verified by grep after
  write; sha1s recorded below.

## T4 - deliverables assembled
- proposal-r1.md written (sections in mandated order); LaTeX bytes verified
  programmatically (no CR/TAB/double-backslash; single-backslash payload intact);
  broken LUV commentary sentence fixed.
- core-aspect-register.md written (label definition files + use-file counts from
  live grep; stale-flag list).
- Hashes and sizes recorded in T5.

## T5 - payload artifacts, patches, final state
- payload-P1.txt (871 B, 1 line), payload-P2.txt (3043 B, 2 lines) extracted from
  the proposal fenced blocks (leading-fence-newline bug found and fixed); ASCII,
  no CR; each matches its fence block verbatim (count 1).
- Proposal Verification section patched to ship the payload files and the
  POST = PRE + 1 / + 2 line accounting (splice-as-insertion model; no anchor
  bytes replaced, so no double-count of the anchor).
- Splice model settled: insert payload as new source line(s) AFTER the anchor
  line (ch03 anchor line ends at "result."; the next source line is the LUV
  sentence inside the assumption environment) - P2 likewise inserts new
  paragraph lines before its anchor paragraph head.
- Gatekeeper-style gatecheck drafts created during a misdispatch inside this
  session were deleted; this folder ships proposer artifacts only (role rule 4).
- Final hashes (live at close): see orchestrator message; re-hash before any
  anchor-critical dispatch (dirty-tree caveat, per memory).

## T6 - close hashes (live bytes at dispatch of gatekeeper round)
- proposal-r1.md            4f6853dbb5385010deba82ef58b243f10f559d7c  (33885 B)
- journal.md                (this file; appended below by no one else)
- core-aspect-register.md   2e3d14a40097012f932bf2279e5076d99ee590d7
- verify_dict_sign_127.py   19af147f499c1ea19fc2f8a96da4b37b88998ea9  (ALL PASS 30)
- verify_anchors_127.py     574b460be50269c730af7323e5f0d4de7c685a0c  (ALL PASS 7)
- capture-verify-r1.txt     1901293f1aa32fa412a6adc6fbc2246fe2c6b800
- capture-anchors-r1.txt    b6791076b16519d5eea2da03fe3f559667487d2f
- payload-P1.txt            8df7a7f42a971892dec26c4e80ad9d18884b1786  (871 B, 1 line)
- payload-P2.txt            e30a1cd68ed607c1d6f51782039464697225b2e3  (3043 B, 2 lines)
- No files outside proposals/127-n-dict-kinetic-sign/ were modified.

R2-REVISION r2 (2026-11-25)
- Applied review-r1.md REQUIRED REVISIONS R1/R2 byte-mechanically to the frozen
  r1 payload bytes; no other changes, no new mathematics, no manuscript/status
  edits.
- R1 (payload-P1.txt): attribution clause rewrite per F2a; replacement grows
  the file by +139 B (871 -> 1,010 B).
- R2 (payload-P2.txt): 'self-dual' -> '(anti-)self-dual' per F2b; replacement
  grows the file by +7 B (3,043 -> 3,050 B).
- Generator: make_payload_127.r2.py, run 'python -I'. Old-string uniqueness
  asserted (count == 1) before each replace; r1 base hashes re-verified inside
  the generator (P1 8df7a7f42a97/871, P2 e30a1cd68ed6/3043, both MATCH).
- Pins matched: YES. Revised P1 sha1_12 6dd693e2cf0b / 1,010 B (expected
  6dd693e2cf0b/1,010); revised P2 sha1_12 73aca8c862ec / 3,050 B (expected
  73aca8c862ec/3,050). Output files payload-P1-r2.txt, payload-P2-r2.txt (new
  names; r1 files never overwritten, re-hashed unchanged after the run).
- Controls fired: YES. Absent-probe uniqueness control raised AssertionError
  as expected (printed by the generator run).
- Hygiene on r2 outputs: bare LF (matching r1 convention; integrator does the
  LF -> CRLF conversion at splice per review-r1 integrator notes), no CR,
  ASCII, trailing LF present; P1 1 line, P2 2 lines (per review pins).
- r2 expected POST numbers as recorded by review-r1 (gatekeeper to recompute
  independently; NOT claimed here): ch03 37,978 B / 917 lines; appH 883,075 B /
  4,146 lines.
- Journal hash before append (sha1_12): 4344487e4468
