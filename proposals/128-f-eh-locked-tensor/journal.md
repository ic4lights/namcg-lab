journal 128-f-eh-locked-tensor (2026-11-25)
- live pins: appH 6839a5cab30e 883075B 4146 lines; ch03 9b1de0928d53 37978B (hashed this pass). digest stale for appH (dee9a4174b81, dirty tree) -> live targeted reads used.
- read live: appH 1997-2265 (Problem F entry), L3224 (123 paragraph), L2485-2530 (EH-not-generated paragraph); ch17 395-430; ch07 1-90,130-175 + label scan; ch01 140-200 (Lichnerowicz requirement); ch02 38-70 (eq:christoffel/eq:riemann conventions); appA 55-150 (eq:appA-a1, eq:appA-sector-sum, eq:appA-Wexp); review-123 r1 L25-45, r2 L30-48; proposal-r2 e_h lines; verify_bookkeeping_123.py e_h lines; frontier.yaml F.eh-locked-tensor + F.a2-windowed.
- never ran verify_ghost_op_123.py (kill-order).

## Journal 2026-11-25 (item 128, cont.)
- Script 1 verify_conventions_128.py run (python -I, repo root); output out-conventions-128.txt:
  SPHERE_R = 2; SPHERE_Ric_11 - sin^2 = 0 (Ric = g on unit S2 under eq:christoffel/eq:riemann);
  GAUGE_a1_S2 = 8/3, ratio_to_R = 4/3 (dim-shrunk 123 ghost a1 = (d/6+1)R with E_gh=-Ric);
  A1_TENSOR_R identity (10/6-e_h)*R = tr(R/6 - E) total-trace reading: True.
  One patch: line 66 contraction fixed from sum(Ric[i,i]) to g^{ij}Ric_{ij} (= Rscal) before green run.
- Next: rewrite verify_eh_128.py (draft had dead code), run, capture out-e_h-128.txt.

## Journal 2026-11-25 (item 128, cont. 2)
- Script 3 verify_ehsum_128.py: self-contained re-derivation of the 123 sector algebra
  with e_h symbolic. Runs: e_h=-5/3 -> out-ehsum-iv.txt (A1_MATCH_123/N0_MATCH_123/WINDOW_MATCH
  True, COND_IV_EH=[-5/3], A1_derived_Q16nK0=0, COND_IV_HOLDS True); e_h=0 control ->
  out-ehsum-0.txt (A1=-5/3, COND_IV_HOLDS False). Item-123 scripts NOT run.
- Anchor check on LIVE appH (re-hashed 6839a5cab30e, 883,075 B, unchanged):
  Problem F section = lines 1997..3225; the item-123 Alternate-scope paragraph is line 3224
  (ONE line, substring count 1); anchor string '\paragraph{Alternate-scope weighted sector data'
  count = 1. '\paragraph{The assumed group ...' count = 1 (unused fallback).
  Payload P1 plan: insert new conditional paragraph immediately BEFORE the Alternate-scope
  paragraph (anchor = unique short string above).
- Script 2 verify_eh_128.py (main conformal-family derivation) running in background
  (task bqj6m4uix, timeout 580 s); capture file out-e_h-128.txt.

## Journal 2026-11-25 (item 128, cont. 3)
- Label verification (plain-string scan, all chapters/*.tex): eq:christoffel, eq:riemann, eq:appA-a1,
  eq:appA-sector-sum, eq:appA-Wexp, eq:FP, eq:FP-eom, eq:Smicro, thm:Geff, ass:aux-metric, ch:agenda,
  eq:V, eq:Geff-structure, sec:status-D, sec:status-F, thm:mT, ch:geometrogenesis, sec:ch1-checklist
  all present exactly once (single-file hit). Payload will use only these.
== cont.3 (2026-11-25) ==
- Payload generator staged: proposals/128-f-eh-locked-tensor/make_payload_128.py.
  Takes derived e_h value as argv[1]; builds payload-P1.txt (CRLF-terminated
  paragraph + blank line, ASCII, no label/cite/status tokens), hygiene guards
  WITH injected positive controls (label token, bare LF, brace imbalance) per
  memory rule generator-join-guard-selftest; asserts live anchor count==1;
  splices into appH-spliced-P1.tex INSIDE the proposal folder only; POST
  accounting assert len(post)==pre+len(pay); prints PAY/PRE/POST sha1_12 pins
  to out-make-payload-128.txt. NOT yet run - waiting on EH_LICH from script 2.
- Anchor for P1 = the unique line-start string
  backslash-paragraph{Alternate-scope weighted sector data
  (count 1 in live appH 6839a5cab30e; payload inserts immediately BEFORE it).
- Script 2 (verify_eh_128.py) relaunched optimized: background task bbortv5dt,
  capture -> out-e_h-128.txt with rc line. Do not rerun; do not poll per
  dispatch. Old slow run died rc=124 (4x4 symbolic inverse blowup); fix was
  exact eps-polynomial truncation (Gamma is degree 2 in eps exactly for
  constant H) - documented in script header.
- Payload EOL decision: container payload-P1.txt holds the paragraph with
  trailing CRLF CRLF so the replace(anchor, payload+anchor) splice keeps the
  blank-line join and POST = PRE + len(payload) exactly (memory
  splice-post-accounting). Recorded in Decisions Taken.

== cont.4 (2026-11-25) ==
- Re-verified live bytes: appH sha1_12 6839a5cab30e / 883075 B (unchanged), ch03
  9b1de0928d53 / 37978 B (unchanged). Payload anchor 'backslash-paragraph{Alternate-
  scope weighted sector data' count = 1; fallback '...assumed group' count = 1.
- Drafted all remaining proposal-r1.md sections in proposal-tail-draft.md with
  value placeholders __EH__/__TT__/__STRUCT__/__DECOMP__/__GHOST__/__SIGMA__/__A1D__
  (+ payload pins). Tail uses LF (Write tool); final merge to proposal-r1.md will
  normalize CRLF. Cross-identities derived for the merge pass: Q16_TRUNK = 8/3 - e_h;
  A1_derived_Q16nK0 = -5/3 - e_h; SIGMA_for_cond_iv = -5/3 - e_h.
- Corrected tail draft: Q16_TRUNK keeps scalar piece 16*(1/6) (equals 8/3 - e_h);
  it is the sum with scalar at 16*(1/6), NOT the Q=1/6 trunk; tensor+ghost trunk
  (-5/3 - e_h) is script 3's A1_derived_Q16nK0. Sentence patched accordingly.
- Pending on script 2 (task bbortv5dt): fill placeholders, run make_payload with
  derived value, run script 3 with derived value (out-ehsum-derived.txt), merge
  tail into proposal-r1.md, final return.

== cont.5 (2026-11-25) ==
- BUG FOUND in verify_eh_128.py structure-base datum: old Rm0 used
  dG0[(r,s,mu)][nu] - dG0[(r,mu,s)][nu] = d_nu G^r_{s mu} - d_nu G^r_{mu s} = 0
  identically (Christoffel symmetric in lower indices); it missed the correct
  slot permutation for R^r_{s mu nu} = d_mu G^r_{nu s} - d_nu G^r_{mu s}.
  Impact scope: ONLY STRUCT_TR['riem'] and E_DECOMP (they alone consume Rm0).
  EH_LICH, EH_SCALAR_OK, GF_SHIFT, E_SYMM, E_TT_TRACE_over_R, GHOST_RESID_M,
  Q16_TRUNK use Ric0/R0/M0 built from Ri()/dG, unaffected.
  Fix applied: Rm0[(r,s,mu,nu)] = subs0(dG0[(r,nu,s)][mu] - dG0[(r,mu,s)][nu]);
  Gamma-Gamma terms drop at x=0 since Gamma(0)=0. File now 13719 B,
  sha1_12 82d7fa0e088b. The STILL-RUNNING task bbortv5dt executes the PRE-FIX
  code: its EH-family outputs remain a valid early read, but its STRUCT_TR/
  E_DECOMP must be DISCARDED and the script re-run once (patched) for the
  capture file out-e_h-128.txt that the proposal pins.
- Waiting: bbortv5dt completion -> read out -> re-run patched script -> then
  make_payload + script3(derived) + merge proposal tail -> final return.


== cont.6 (2026-11-25) ==
- Script 2 FINAL (v4.1, 11401 B, sha1_12 86e8f227ceb1), out-e_h-128.txt rc=0 all
  green: EH_LICH=29/6; GF_SHIFT=0; E_SYMM=True; EH_SCALAR_OK=0; E_TTQF/R=9/2;
  STRUCT_TR {riem -1/2, ric1 5/2, ric2 5/2, gric 1, ricg 1, ggr 4} (hand-verified
  independently); E_DECOMP exact at 2 random C-points (free ric1/ric2 split =
  rank-5 kernel ric1-ric2, zero bilinear form on symmetric fibres);
  EH_COMBO_CHECK=0 x2; TT_PAIRING_INVARIANT True True; FIBRE_TRACE DELTA=0;
  GHOST_A1_COEFF=5/3; Q16_TRUNK=-13/6. Bug log: apply_structure mult-count,
  Gram-Schmidt orthonormal fibre basis, E_DECOMP via linsolve (rank 5).
- Script 3 with e_h=29/6 -> out-ehsum-29-6.txt: A1/N0/WINDOW MATCH True;
  A1_derived_Q16nK0=-13/2; SIGMA_for_cond_iv=-13/2; COND_IV_HOLDS False.
  Controls out-ehsum-0.txt, out-ehsum-iv.txt (COND_IV_HOLDS True at -5/3).
- FINAL RESULT FRAMING: e_h(total-trace) = 29/6 + sigma_gf + sigma_pt under H1;
  record condition (iv) <=> sigma_gf+sigma_pt = -13/2; under strict H1 sigma_pt=0,
  open step = sigma_gf (zero-order remainder of harmonic-gauge-fixing Laplace
  reduction at Gamma=0 points). Old story (pure-trace sigma only, GF-contributes-
  nothing-to-E, ghost identity asserted) RETIRED: GF_SHIFT=0 constrains only the
  constant-fibre density kernel, not the Laplace E_gf piece.
- make_payload_128.py rewritten (artifacts removed; pure-trace span = 3
  structures incl. Ric (x) tr, trivially vanishing) and RUN with 29/6:
  GEN PASS; ANCHOR_COUNT=1; CTRL_FIRES (True,True,True);
  PAY_PIN 18a641ad797e / 4195; PRE_PIN 6839a5cab30e / 883075;
  POST_PIN aa611bc78a35 / 887270 = PRE+PAY. Splice written to
  appH-spliced-P1.tex (proposal folder only).
- cert_payload_128.py: standalone amsmath wrapper compile OUTSIDE repo (temp dir,
  deleted): CERT PASS rc=0, ERR_LINES=0, 5 undefined-ref warnings = exactly the
  5 ef/\eqref in the payload. out-cert-128.txt.

== cont.7 (2026-11-25) ==
- TAB TRAP FOUND+FIXED: first generator emitted EHS/SIG with single-backslash
  	frac -> literal TAB before "rac" (compile cert passes, output WRONG:
  prints "frac{29}{6}" as text). Regenerated with doubled backslashes; hygiene
  now has raw-TAB check + 4th positive control (tab injection) + occurrence
  counts 	frac{29}{6}=3, 	frac{13}{2}=2. NEW PINS: PAY 54f62d402998 / 4200;
  POST fa04730cc359 / 887275; PRE unchanged 6839a5cab30e / 883075; GEN PASS.
  Cert re-run on new bytes: CERT PASS rc=0 ERR=0, 5 undef-ref warnings = the
  payload's 5 refs. cont.6 pins (18a641ad797e/4195) SUPERSEDED.

== cont.8 (2026-11-25) ==
- proposal-r1.md written complete (all mandated sections), payload embedded
  byte-exact from container (marker replace; verified 3x29/6 + 1 mention,
  2x13/2 + 1 mention, exact tr K line, zero raw tabs). FINAL PIN
  proposal-r1.md a32a2e7fc025 / 26886. Round 1 submitted to gatekeeper.
