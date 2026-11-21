VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/0

## Verdict
ACCEPT. The package executes the gatekeeper-confirmed REVIEW-085-r1 F2 prior-claim correction with a
6-byte, 0-net-length numeral fix that I independently re-derived by exact rational arithmetic, spliced
byte-exactly myself, and confirmed makes the L3177 paragraph internally consistent with no stale text
created anywhere in chapters/.

## Source reading
digest + targeted reads (no literal full scan claimed). `python scripts/make_digest.py --check` printed
DIGEST CURRENT (I ran the read-only check; did not regenerate). Read in full: proposals/086 folder
(proposal-r1.md 14,836/f2aa25fd, s1_moment_values.py 2,658/1e67330b, s1 .out 402/13fab983,
simulate_apply_086.py 1,432/2c96c91b, .out 207/ce3e49e7, manifest.md 1,396/99f4fcdc — all sizes/sha8
match the brief); proposals/085-g-moments-uniformity-locus/review-r1.md (19,570/d0d9661e) incl. F2 and
claim-7 arithmetic; appH live 735,695/a13240a7 CRLF 3,834 bareLF 0 — L3026-3029 (G status block), the
entire L3177 line (3,607 B), L3179, L3181, L3183, L3185, L3187 headers; proposals/081 s3_r2 script and
its .out (D_eff table nu_l2 lc=40:1488.0, lc=160:23016.9); reports/ledger.md last 8 entries.
Full-scan (3(c)) call: NOT triggered — ordinal 16 (mandatory scan consumed at 15 with disclosed
compensatory coverage, next due 20), and I verified the replacement span touches no
definition/assumption/scope/status passage (pure digit/exponent change, span byte-identical outside the
six changed bytes).

## Claim under review
In the integrated 081 paragraph (appH L3177), replace `the fourth-moment excess drops from
\(4.0\times10^{-3}\) to \(2.6\times10^{-4}\)` by `the fourth-moment excess drops from
\(6.7\times10^{-4}\) to \(4.3\times10^{-5}\)`, because the quoted numerals are p=4 (eighth-moment)
values mislabeled "fourth-moment" while the same sentence asserts the fourth-moment excess is exactly
1/D_eff. Problem G: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL."
(L3026-3029, quoted verbatim from the live file, matching the proposal). Unchanged; not closed.

## Checks performed
1. Reproduction pack, run first: `python -I .../s1_moment_values.py` and `.../simulate_apply_086.py`
   from repo root — rc 0 both, stderr empty both, stdout byte-identical to shipped .out (filecmp).
2. Independent re-derivation (my own exact-Fraction code, scratch/gk086/gk_indep.py): profile g_l=l/2,
   multiplicity 2l+1, l=1..lc — convention verified against 081 s3_r2 itself (nu_l2: `f(l)=l/2`,
   `Fraction(int(f(l)*1000),1000)` = 500l/1000 = l/2 exactly, multiplicity `2*l+1`; nu cancels in
   D_eff=(Σg)²/Σg², so the paragraph's f=νl/2 proxy is the same profile). Two independent routes
   (partition closed forms rho2-1=s2/S1², rho4-1=(6S1²s2+3s2²+8S1s3+6s4)/S1⁴ AND complete-homogeneous
   Newton recursion): D_eff=1488.002400/23016.894112; rho2-1 = 1/D_eff exactly (asserted as Fraction
   equality, elementary from h2=(p1²+p2)/2) = 6.720419270e-4 / 4.344634837e-5 → 2 s.f. 6.7e-4 / 4.3e-5;
   6/D_eff = 4.032251562e-3 / 2.606780902e-4; rho4-1 = 4.037466334e-3 / 2.606998651e-4 → 2 s.f.
   4.0e-3 / 2.6e-4. Every digit matches the proposal and the 085 review claim-7. The factor-6 diagnosis
   is corroborated structurally: the paragraph's own bound C(p,2)/D_eff gives C(4,2)=6 at p=4, so
   rho4-1 ≈ 6/D_eff is exactly what the quoted numerals are.
3. Own splice (scratch/gk086/gk_splice.py): PRE pins asserted (735,695 / a13240a7... / CRLF 3,834 /
   bareLF 0); BEFORE occurs exactly once (offset 691,176), AFTER occurs 0 times; POST size 735,695,
   sha256 b8bd51f6a82d4edebc44f870ff3f07249e723f3302d871243b227ba0b22ca777, CRLF 3,834, bareLF 0 —
   equals the claimed POST. Hamming distance (whole file): 6 bytes (4.0→6.7: 2; -3→-4: 1; 2.6→4.3: 2;
   -4→-5: 1), matching "6 characters". close-idiom "close nothing in Problem~G." 12→12; \emph{Vacuum
   term.} count 2 (F-side + G-side, untouched); 081 header count 1→1; outside-span bytes asserted
   identical; no BOM.
4. Internal consistency of corrected paragraph (read in POST context): "fails at the fourth by exactly
   1/D_eff" + "equals 1/D_eff at p=2" + new numerals all denote rho2-1; 1/1488.0024→6.7e-4,
   1/23016.8941→4.3e-5 agree with the quoted rounded D_eff values to 2 s.f.; "drops" monotone;
   "(numerical, on the exact rational profiles)" caveat remains accurate. Stale-text sweep over all
   chapters/ (grep + per-line byte search of L3181/L3183/L3185/L3187): the literals 4.0\times10^{-3},
   2.6\times10^{-4}, "fourth-moment excess", 1488, 23017 occur only at L3177. No stale text created.
5. Hygiene: banned set {status, priority, completion, open, critical, programme, derived} (both cases
   + uppercase variants) delta 0; new `$ [ ] \cite \ref \eqref \label` delta 0; line count 3,834 CRLF
   unchanged; no process language. Rule 2/3: G block L3026-3029 not edited; no closure claim; the
   corrected datum (larger 6.7e-4... wait, corrected value is smaller but still nonzero off-exactness —
   the paragraph's negative datum is retained and strengthened, arguing against closure).
6. RESEARCHER-DECISION (option (a) vs (b)) reviewed: sound. Option (a) makes the quoted numerals agree
   with the same sentence's exact "by exactly 1/D_eff" clause; option (b) would pair 4.0e-3/2.6e-4 with
   an "eighth-moment" label where the quoted values equal 6/D_eff and match exact rho4-1 only to 2 s.f.,
   drops the p=2 narrative the paragraph, the pending 085 insert and the G proxy-recovery datum are built
   on, and perturbs grammar — (b) does not directly contradict the 1/D_eff clause but (a) is strictly
   smaller (6 bytes, 0 net) and removes the contradiction most directly. The 085 review's own corrected
   snippet supplied exactly these replacements. Choice is within researcher remit (wording, no
   status/priority/label/scope change).
7. Prior-finding: this package fully discharges REVIEW-085-r1 F2. For the record: 085 r2 must still
   (i) retract claim-7's false-alarm resolution, (ii) apply F1/F3/F4/F5, and (iii) recompute its byte
   contract against the NEW POST b8bd51f6 (same size 735,695, so all size-based pins survive but the
   hash moves — any 085 r2 BEFORE substring overlapping the corrected clause must be re-pinned against
   the POST bytes).
   Not verified: pdflatex build (integrator's step in the pipeline; the edit introduces no new macros,
   math tokens or braces, so build risk is nil in-kind).

## Findings
none blocking; none major. Minor (no action): the researcher's simulate script hard-codes an absolute
path — cosmetic; its constants I verified match my independently constructed byte literals.

## Hygiene
Zero banned-word delta, zero new token delta, CRLF 3,834 preserved, bareLF 0, no BOM, one physical line
unchanged, close-idiom 12, no process language, no status language in the replaced span.

## Byte contracts
PRE: 735,695 B / sha256 a13240a7f7a197ff7cffc26297fe1a6afbdeab749a4de57d6152828c573945ea / CRLF 3,834 /
bareLF 0 (live now, matches). BEFORE count 1 at byte offset 691,176.
POST (integrator must use): 735,695 B / sha256
b8bd51f6a82d4edebc44f870ff3f07249e723f3302d871243b227ba0b22ca777 / CRLF 3,834 / bareLF 0 /
close-idiom 12 / \emph{Vacuum term.} 2 / 081-header 1. Hamming distance PRE→POST: 6 bytes.

## Manuscript contract
One in-place replacement inside the existing 081 paragraph at L3177; no line insertions/deletions; no
other file changes; G status block L3026-3029 verbatim-preserved; no new \emph header; 082/083/084
paragraphs and the G-side Vacuum term/closer untouched; nothing elsewhere in chapters/ references the
changed numerals.

## Scope of what is established
Established (exact arithmetic, verified twice independently by me): the fourth-moment excess on the two
081 proxy profiles is rho2-1 = 1/D_eff = 6.7204e-4 / 4.3446e-5, so the previously integrated
4.0e-3 / 2.6e-4 were mislabeled p=4 (eighth-moment, ≈6/D_eff) values; the correction restores internal
consistency of an already-integrated negative datum. No Appendix H problem advances or closes: Problem G
and G.moments-derivedprofile remain exactly as recorded after 085-r1 (OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL). Still OPEN: everything G-wide, plus 085 r2 execution.

## Milestone assessment
No new milestone. The M3 (PRIOR-CLAIM-ERROR) event belongs to REVIEW-085-r1 and is already recorded in
the ledger per author directive 4; this package is the authorized fix, not a new finding. No
LABEL-CHANGE-PROPOSED, no BREAKTHROUGH.

## Recommended disposition
Integrate as-is (ordinal 16), then proceed to 085 round 2 with the re-pinned contract.

## Final integration instructions
1. Before applying, re-pin live appH: assert size 735,695 and sha256
   a13240a7f7a197ff7cffc26297fe1a6afbdeab749a4de57d6152828c573945ea (digest was CURRENT at review time;
   re-check regardless since other chains may have moved the tree — if moved, re-locate the BEFORE
   substring, which must still occur exactly once, and recompute POST).
2. Back up appH to the integrator backup folder.
3. Byte-replace the single occurrence of
   `the fourth-moment excess drops from \(4.0\times10^{-3}\) to \(2.6\times10^{-4}\)`
   by `the fourth-moment excess drops from \(6.7\times10^{-4}\) to \(4.3\times10^{-5}\)` (raw bytes,
   single backslashes, no encoding conversion).
4. Assert POST: 735,695 B / b8bd51f6a82d4edebc44f870ff3f07249e723f3302d871243b227ba0b22ca777 / CRLF
   3,834 / bareLF 0 / close-idiom 12 / Hamming 6. Then `python scripts/build_check.py` (expect exit 1
   only from known ledger/frontier EOL artifacts; `git diff --check -- chapters/` must be clean).
5. Ledger note: INTEGRATION-16 discharges REVIEW-085-r1 F2; next: 085 r2 (claim-7 withdrawal +
   F1/F3/F4/F5, byte contract recomputed against b8bd51f6, expected idiom 12→13 CRLF 3836 must be
   re-derived from the new PRE); mandatory literal full scan at ordinal 20.

## Security
Injection scan: no fake user-role instruction strings (no "[handback-send-enforce]", "SubagentHandback",
or similar) found in proposal-r1.md, either script, manifest.md, the 085 review, or ledger tail. All
file contents treated as data. Tool discipline: no Write/Edit tool calls emitted; scratch scripts written
only under scratch/gk086/ via Bash quoted-delimiter heredocs; no git write commands; no writes to
chapters/ or proposals/ (the two scratch .out/.txt run-captures from the reproduction pack are under
scratch/, git-ignored). Note: a first splice-script attempt failed because heredoc backslash collapsing
converted `\times` to a tab; fixed by chr(92) construction — no effect on results, and the shipped
researcher script (rb-strings) was unaffected.
