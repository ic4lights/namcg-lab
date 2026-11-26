# -*- coding: ascii -*-
# Builds proposal-r2.md (ASCII, CRLF) with the payload embedded BYTE-EXACTLY
# from payload-123.txt, then verifies the embedding by byte comparison.
import hashlib, io, os
F = r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\123-f-coeff-locked-block"
pay = open(os.path.join(F, "payload-123.txt"), "rb").read()
PAY_SHA = hashlib.sha1(pay).hexdigest()
assert PAY_SHA == "e0b8d6b31cad8b34fe1f3764ea151df47e1e562f" and len(pay) == 5442
CRLF = b"\r\n"

BEGIN = b">>> BEGIN PAYLOAD-123.TXT BYTE-EXACT (r2, sha1 e0b8d6b31cad8b34fe1f3764ea151df47e1e562f, 5442 B) <<<"
END = b">>> END PAYLOAD-123.TXT <<<"

T = r'''# Proposal 123-f-coeff-locked-block, round 2

## Header and pins (r2)
- r1 verdict (review-r1.md, sha1 e6707eca0ebfe8b8fcd3cc879f43f988c412655a, 13,043 B):
  "ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1"
  (addendum re-issued the same verdict).
- Manuscript pin (unchanged this round): chapters/appH-microscopic-proofs.tex
  sha1 d2af19df0f998ce150c12ea11af9ea8c0387435f, 863,831 B, 4,138 lines, UNCOMMITTED.
- Payload lineage: r1 payload 5548ee218f2c3b0720054801f20a8590f6fd9a75 / 5,488 B
  -> r2 payload e0b8d6b31cad8b34fe1f3764ea151df47e1e562f / 5,442 B (net -46 B).
- Splice target POST (context anchor, live bytes): r1 704f3765797a.../869,321
  -> r2 ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1 / 869,275 = 863,831 + 5,442 + 2.
- proposal-r1.md 3758b167c4880fb9774f265da4e195eb9ce24138 / 31,169 B stays as the
  round-1 research record; this round supersedes its payload bytes, its exclusion
  record (finding 2) and the two record passages quoting the old E_ten clause
  (r1 L98-100 and L135-137); it supersedes nothing else.

## Result
Round 2 applies the single required revision of review-r1 (finding 1): the tensor
block definition now reads "with fibre-traced endomorphism
\(\mathrm{tr}\,E_{\mathrm{ten}}=e_h R_E\)", matching the result clause
"the tensor block contributes 10/6 - e_h" under appH's per-component endomorphism
convention (the total fibre trace is what e_h denotes; script 2's e_h = tr E/R).
The r1 package's arithmetic, windows and status scoping are unchanged and were
independently re-derived by the gatekeeper at r1. Optional items disposed below.
Nothing new is claimed: the paragraph remains a conditional Alternate-scope record;
Problems F, D, D1 and N remain OPEN and PROGRAMME-CONDITIONAL; no label changes.

## Target and status
Problem F (chapters/appH-microscopic-proofs.tex, section "Problem F", ledger
opening L1995-2015): "Status: OPEN. Priority: CRITICAL PATH. Completion:
PROGRAMME-CONDITIONAL." Original target: the per-sector heat-kernel data of
G_eff with matrix-derived content and derived gauge fixing; reduced-scope result
treats G_eff as an input, which leaves F OPEN. This package is PROGRAMME-CONDITIONAL
supply (Alternate-scope weighted sector data for a named truncation); it closes
nothing and discharges none of the missing-step items. Gating dependencies per the
review's ranked avenues (derivation of the kinetic diffeo-ghost operator from
eq:Smicro gates F; determination of e_h) remain OPEN upstream.

## Gatekeeper findings and how addressed
- Finding 1 (major, REQUIRED): payload defined E_ten = e_h R_E while the per-
  component convention (appH L2093-2107: "otherwise 1/6-Q replaced by its trace";
  eq:appA-a1 fibre trace over the 10 components) makes the contribution
  10/6 - 10 e_h; with e_h := tr E_ten/R_E (script 2's definition) the contribution
  is 10/6 - e_h. APPLIED VERBATIM per the review's Corrected snippet: definition
  clause changed to "with fibre-traced endomorphism \(\mathrm{tr}\,E_{\mathrm{ten}}=e_h R_E\)";
  result clause unchanged (already correct); the record passages r1 L98-100/L135-137
  are restated below. Payload bytes, POST and all pins recomputed (reproduction
  pack below). Internal consistency re-verified: sum over 10 components of
  (1/6 - E_ii/R) with total trace e_h R gives 10/6 - e_h exactly.
- Finding 2 (minor): DELRHO exclusion reason in r1 L189-194 was false
  ("no 64 pi^2 convention occurs anywhere in chapters/"). CORRECTED here with
  self-verified line numbers: 64\pi^2 occurs in appA-seeley-dewitt.tex at
  L148, L160, L166, L167, L168, L194, L196 (grep of 64\pi; the review cited
  L148/160/166/168), and also 6 times in appH-microscopic-proofs.tex, 3 times in
  ch08-heat-kernel.tex, 1 time in ch12-hbev.tex, 1 time in ch17-agenda.tex. The
  corrected reason is scope: DELRHO = +8 (Lambda_UV^4 - mu^4)/(64 pi^2) is
  rho_Lambda vacuum-energy bookkeeping of the eq:appA-Wexp conventions, outside
  this paragraph's a_1 / windowed-a_1 scope; it stays excluded from the payload
  for that reason only.
- Finding 3 (minor, optional alignment O(m^4 ln m^2) vs recorded O(m^4 s_max),
  appH L2150-2157): DECLINED. The review states both bounds are valid in their
  regimes and the payload's is "weaker but true"; introducing s_max notation
  inside this paragraph would require importing that paragraph's definitions for
  no gain. Payload claim (iii) keeps O(m^4 ln m^2); the recorded O(m^4 s_max)
  passage is untouched.
- Finding 4 (minor, no action): "-M positive" stands (non-negative modulo the
  Killing kernel; BEREZIN_DET covers zero-mode counts). No change.
- Finding 5 / lineage adjudication: deviations accepted at r1; r2 additionally
  eliminates future in-place-edit risk by keeping run_cert_123.py untouched and
  adding run_cert_123_r2.py as a new file, and by preserving .r1-bytes snapshots
  of every script edited this round (see Verification scripts).

## Optional-item dispositions (decisions taken)
- Addendum wording note (optional A): ADOPTED. Clause (i) now specifies the ghost
  operator as the Laplace-type operator \(M\xi^\mu:=g^{ab}\nabla_a\nabla_b\xi^\mu+
  R^\mu{}_\nu\xi^\nu\) with endomorphism \(E_{\mathrm{gh}}{}^\mu{}_\nu=-R^\mu{}_\nu\);
  the first-variation definition \(M\xi^\mu:=\frac{\mathrm d}{\mathrm d\varepsilon}
  \big|_0 F^\mu[g+\varepsilon\mathcal L_\xi g]\) and the "equals" derivation claim are
  deleted, removing the only clause whose derivation no runnable artifact in this
  package reproduces (author order froze script 1; gatekeeper attempts at the full
  linearization identity did not complete). This is exactly the rephrasing the
  Alternate-scope paragraph permits (ch17 L678-686: the operator is a specified
  input), it changes NO equation that the paragraph consumes (M's displayed form,
  E_gh = -R, a_1 = (4/6+1)R = 5/3 R, the weight -2, all counts and windows are
  byte-identical to r1), and it aligns the payload with the review's own Rule-6
  classification ("specified conditional input"). Two grammar consequences with no
  equation content: "...hence the positive Euclidean operator \(-M\) is
  Laplace-type with endomorphism..." became "...the positive Euclidean operator
  \(-M\) has endomorphism...", and the status list "the ghost operator, weight,
  endomorphism and \(a_1\) contribution ... are derivations" became "the ghost
  weight, endomorphism and \(a_1\) contribution ... are derivations" (the operator
  itself is now listed where it was always classified: among the supplied premises,
  "the ghost as an infrared input"). The Scheme clause naming "harmonic (de Donder)
  gauge \(F^\mu=g^{ab}\Gamma^\mu_{ab}\) for the diffeomorphism sector" is kept
  byte-identical: it names the gauge of the scheme, and after deletion of the
  first-variation clause the paragraph no longer asserts any identity between that
  functional and M. Rejected alternative: keeping the attribution (the review
  records that no artifact in this chain reproduces its derivation end-to-end);
  re-arming script 1 is barred by the author fix-order and was not attempted.
- Remainder alignment (optional B): DECLINED, see finding 3.

## r1 -> r2 payload diff summary (4 textual changes, net -46 B)
1. Premises: "components with \(E_{\mathrm{ten}}=e_h R_E\)" -> "components with
   fibre-traced endomorphism \(\mathrm{tr}\,E_{\mathrm{ten}}=e_h R_E\)".
2. Clause (i): "\(M\xi^\mu:=\frac{\mathrm d}{\mathrm d\varepsilon}\big|_0 F^\mu[
   g+\varepsilon\mathcal L_\xi g]\) equals \(g^{ab}\nabla_a\nabla_b\xi^\mu+
   R^\mu{}_\nu\xi^\nu\)" -> "the ghost operator is specified as the Laplace-type
   operator \(M\xi^\mu:=g^{ab}\nabla_a\nabla_b\xi^\mu+R^\mu{}_\nu\xi^\nu\)".
3. "hence the positive Euclidean operator \(-M\) is Laplace-type with endomorphism"
   -> "the positive Euclidean operator \(-M\) has endomorphism".
4. Status list: "the ghost operator, weight, endomorphism" -> "the ghost weight,
   endomorphism".
All other payload bytes, all 12 ref/eqref targets (whitelist unchanged: thm:Geff,
ass:aux-metric, sec:status-D, eq:Geff-structure, eq:V, eq:appA-a1, eq:appA-a2,
eq:appA-sector-sum, eq:appA-Wexp, eq:christoffel, eq:riemann, ch:agenda; used
count 12), the exclusions (no DELRHO, no W_C/delta_W, no ghost a_2, no closure or
label language) and all numerals are unchanged from r1.

## Revised record passages (replace r1 L98-100 and L135-137 wording)
- Premises list (r1 L98-100, restated): tensor block supplied as a Laplace-type
  input (10 symmetric-tensor components, FIBRE-TRACED endomorphism
  tr E_ten = e_h R_E, i.e. e_h is the total fibre trace tr E_ten/R_E per script 2),
  and the diffeomorphism ghost supplied as an infrared input, its kinetic operator
  SPECIFIED as the Laplace-type operator M = g^{ab} nabla_a nabla_b + Ric.
- A1_trunk record (r1 L135-137, restated): tensor 10/6 - e_h with e_h the TOTAL
  fibre trace; under the per-component convention the sum of 1/6 - E_ii/R_E over
  the 10 components equals 10/6 - tr E/R_E; ghost weight -2 x (4/6) = -4/3 from
  the R/6 term and -2 x (+1) = -2 from tr E, total -10/3;
  A1_trunk = 16(1/6 - Q) + n_K(1/6 - Q_K) + (10/6 - e_h) - 10/3
           = 16(1/6 - Q) + n_K(1/6 - Q_K) - 5/3 - e_h.

## Splice plan (unchanged geometry, r2 bytes)
Single-line insertion into chapters/appH-microscopic-proofs.tex between the last
paragraph of the Problem F section and "\section{Problem G: HBEV}". The anchor is
the SECTION-CONTEXT string: the closing sentence "These statements are for the
hypotheses and the channel convention stated here; ... PROGRAMME-CONDITIONAL."
followed by CRLFCRLF followed by "\section{Problem G: HBEV}". The bare closing
clause "These statements are for the hypotheses" occurs 6 times in appH
(verified this round by inspect_anchor_123.py), so uniqueness is counted ONLY on
the context string; the generator and checker both assert count == 1 on the
context string and splice via it. The integrator must re-anchor against the live
tree at integration time and recompute POST from the live bytes. Payload: one
ASCII line, CRLF-terminated, no labels, no citations, braces balanced.

## Revised payload (for integration; single line)

__BEGIN_BLOCK__

## Verification scripts / reproduction pack (all in this folder, ASCII/CRLF-safe)
Run from this folder; interpreter: python (plain -I is fine; scripts only read
the repo). Expected invariant outputs in brackets.
1. python -I make_payload_123.py [OUTFILE]   [10 lines "CTRL ...: fires OK"
   (8 r1 hygiene controls + 2 new r2 token guards with positive controls),
   PIN OK d2af19df0f99 863831, R2 TOKENS OK, REFS OK used=12, ANCHOR unique on
   CONTEXT string (count 1), PAY e0b8d6b31cad 5442, POST ba72024aba4d 869275,
   GEN VERDICT: PASS; OUTFILE = spliced appH bytes]  (sha1 403507c033fedccd...,
   11,689 B; r1 bytes preserved as make_payload_123.py.r1-bytes, 25063ff68713,
   10,858 B)
2. python -I recom_post_123_r2.py OUTFILE   [POST
   ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1 869275; length arithmetic assert;
   "matches generator spliced file: True"; RECOM POST VERDICT: PASS]
   (392c324973bc71d8ebd4306365361106941506b0) - INDEPENDENT of the generator.
3. python -I check_payload_123_r1.py        [45 check lines all PASS incl.
   PAY_FIBRETRACE, PAY_GHOST_SPEC, PAY_NO_FIRSTVAR, ANCHOR_UNIQUE_CTX and the
   CTRL control rows; CHECKER VERDICT: PASS; exit 0]  (e2deeee5a9728ea1...,
   5,843 B; r1 bytes preserved as check_payload_123_r1.py.r1-bytes, 462ed5b332ac).
   Captures: out-checker-run4.txt == out-checker-run5.txt byte-identical
   (fd99bb68d547..., 1,328 B). Generator capture out-gen-run4.txt
   (cc6459457636..., 681 B).
4. python -I inspect_anchor_123.py          [full anchor count 1, context anchor
   count 1, short clause count 6, INSPECT VERDICT: PASS]  (e64a06334b68...)
5. python -I run_cert_123_r2.py             [needs step 1 with OUTFILE =
   %TEMP%/cert123r2/appH-spliced-r2.tex; CERT VERDICT: PASS; all 4 rc=0; final
   pass 0 '^!', 0 undefined, 0 multiply; STABLE True; artifacts
   cert-summary-123-r2.txt etc.]  (new file; run_cert_123.py r1 left untouched).
6. Unchanged from r1 and NOT re-run this round: verify_bookkeeping_123.py
   (df307b2e7750; green capture out-script2-run3.txt 5e64dfef8ba2/843) and
   verify_threshold_window_123.py (c0a811a2eb38; capture 7867134b879b/380) -
   their checked algebra does not touch the two changed clauses. The gatekeeper
   should re-run both from the captures' reproduction commands.
7. verify_ghost_op_123.py: FROZEN by author order 2026-11-24 (19:18); must not
   be re-run or re-armed in any form (author fix-order, journal 24d).
Patches kept for audit: patch_gen_123_r2.py (df236bff30da), patch_chk_123_r2.py
(3a1ed7e3cd01), fix_patch_123.py (interim, superseded by final
patch_gen_123_r2.py bytes).

## Certificate (r2, independent artifact set)
Fresh %TEMP% copy of the build tree with the spliced appH substituted
(hash-asserted ba72024aba4d / 869,275): pdflatex1 rc=0, bibtex rc=0,
pdflatex2 rc=0, pdflatex3 rc=0; pl3.log: 0 '^!' lines, 0 undefined,
0 multiply-defined; pl1.log 1,606 undefined pre-bibtex (expected); STABLE True;
PDF 3,272,661 B. Repo never built on or modified. Artifacts:
cert-summary-123-r2.txt, cert-pl3-full-123-r2.log, cert-pl3-tail-123-r2.txt,
cert-bib-123-r2.log. (Item-108 rule: this payload ships with its own cert.)

## Claim classification (r2; changes from r1 in bold)
- Ghost operator M (displayed Laplace-type form with E_gh = -Ric): SPECIFIED
  CONDITIONAL INPUT under Alternate-scope (ch17 L678-686); sign calibration
  (S^2, R=+2, Killing-field kernel) per r1 evidence; NO derivation claim.
- e_h = total fibre trace tr E_ten/R_E: EXPLICIT STATED DEFINITION (r2 fix); its
  VALUE remains an unspecified input parameter.
- Ghost fibre a_1 = (5/3)R, weight -2, N0 ghost shift -8: established derivation
  from the specified M and eq:appA-a1/eq:appA-sector-sum conventions (r1,
  re-derived by gatekeeper).
- N0 = 18 + n_K; A1_trunk = 16(1/6-Q) + n_K(1/6-Q_K) - 5/3 - e_h; vanish at
  Q=1/6, n_K=0 iff e_h = -5/3; windowed coefficient: established conditional
  algebra (script 2; gatekeeper re-derivation).
- J-window identities, small-mass expansion, Upsilon -> 10 (remainder form
  O(m^4 ln m^2) in the windowed regime): established derivation (script 3).
- DELRHO rho_Lambda shift: computed in script 2, NOT asserted in the payload
  (scope exclusion; corrected reason above).
- Not claimed (unchanged from r1): W_C, delta_W, ghost a_2, A/B/C comparison of
  eq:Geff-structure, any G_eff value, any closure, any label change; Problems
  D, D1, F, N remain OPEN and PROGRAMME-CONDITIONAL.

## Source reading
Digest + targeted reads. This round: live appH pins and anchor regions
(inspect_anchor_123.py), the four edited generator regions, review-r1.md in
full, r1 exclusion passage L186-196 and record passages L96-100/L133-139,
64\pi grep across appA/appH/ch08/ch12-hbev/ch17, ch17 Alternate-scope L678-686
(r1-verified passage relied on unchanged). No full scan (protocol 3 conditions
not met; digest-current conditions per manifest).

## Milestone assessment
Routine: a revision round executing a gatekeeper-specified wording fix plus two
dispositions. No milestone trigger.

## Status-label recommendation
Re-derived from the current agenda/ledger: critical path at the full-GR scope
includes A, B, C, D1, E, F, G-derived, N; none of their labels is touched by this
package. All labels unchanged (F remains OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL).

## Author decision needed
None.

## Remaining open step
Unchanged from r1/review: F's original target needs (i) the kinetic diffeo-ghost
operator derived from eq:Smicro (upstream, gates F), (ii) e_h fixed by the
tensor-block endomorphism of the locked action, (iii) removal of the supplied
truncation inputs (field content, Q, Q_K, n_K, window scheme) - each outside this
package's scope; F's missing-step paragraph items stay OPEN.

## Special instructions for the gatekeeper
- Verify the four-diff payload against r1 bytes (payload r1 bytes live in
  proposal-r1.md; r2 bytes in payload-123.txt and the block above - verify the
  block is byte-exact by extraction + cmp, and that extraction markers do not
  appear elsewhere).
- Verify internal consistency of the fix: 10 components, per-component
  contribution 1/6 - E_ii/R_E, total trace e_h R_E => block contributes
  10/6 - e_h; and that no OTHER clause now conflicts with e_h = total trace.
- Re-run items 1-4 of the reproduction pack and re-derive POST independently;
  confirm the context anchor (not the bare sentence) is what the generator and
  checker use, and confirm 64\pi line numbers for the corrected exclusion record.
- The cert log pl1.log's 1,606 undefined references are pre-bibtex state; the
  operative log is pl3.log (0/0/0). Do not read the PDF size delta vs r1 as
  signal (aux-state dependent).
- Do not re-arm script 1 (author fix-order). Do not assert any derivation of the
  ghost operator from the gauge functional; the payload no longer does.
'''

# Build: replace placeholder with marker-wrapped payload line.
block = BEGIN + CRLF + pay.rstrip(CRLF) + CRLF + END + CRLF
data = T.encode("ascii")
# insert block at placeholder position (bytes)
ph = b"__BEGIN_BLOCK__"
i = data.find(ph)
assert i >= 0
data = data[:i] + block + data[i + len(ph):]
data = data.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")  # normalize CRLF
open(os.path.join(F, "proposal-r2.md"), "wb").write(data)

# verify: ASCII, CRLF-only, single CR/LF classes, embedded payload exact
b = open(os.path.join(F, "proposal-r2.md"), "rb").read()
assert all(c < 128 for c in b)
assert b.count(b"\n") == b.count(b"\r\n") and b"\r\r" not in b
i0 = b.find(BEGIN); i1 = b.find(END)
emb = b[i0 + len(BEGIN) + 2:i1]
assert emb == pay, "embedded payload != payload-123.txt"
assert b.count(BEGIN) == 1 and b.count(END) == 1
open(os.path.join(F, "embedded-r2-extract.bin"), "wb").write(emb)
print("embedded extraction written; cmp with payload-123.txt should be silent")
print("proposal-r2.md bytes", len(b), "sha1", hashlib.sha1(b).hexdigest())
