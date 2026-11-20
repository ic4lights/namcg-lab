# Proposal 099-g-mi-p-d-d2, round 2

Delta document: round 1 (ACCEPT WITH REQUIRED REVISIONS, review-r1.md, sha8 0f14dbb8)
is kept unchanged as lineage; this round fixes notation and re-issues the byte
contract only. The mathematics was fully accepted: the gatekeeper's independent exact
mpath (own mpmath path, dps 25-30, different code path) confirmed every shipped value
to <=4e-7, including the correction of the predecessor values, and nothing is
re-derived here.

## Result

Round 2 delivers the r1 result with the blocking notation defect removed: the insert
no longer contains any bare `u` token. Both occurrences named in the review's Corrected
snippet were replaced verbatim, and a third bare-u occurrence the snippet had left in
place ("joint density of \((\tau,u,x)\)") was eliminated by the pure renaming
\((\tau,p_{2},x)\) (u=p_{2} identically under the block's own convention p=lambda/tau).
No numerical value, claim, assumption, or scope statement changed. New bytes:
insert-r2.tex, 1,656 B, sha8 aa19ac66 (full sha256 aa19ac668cc8a59c... in the gen and
hygiene outputs). New POST contract (simulate_apply_099_r2.out, authoritative for r2):
POST 793,616 B, sha256 7cd6e2084c065f69045e82216439bcb5feee71468b4b84fb7caaae71b9305885,
CRLF 3,862, bareLF 0, idiom 25, verb 1, Vacuum 2, new header 1, adjacency 1/1,
old-seam probe 0. The round-1 contract (793,516 B / fae8dcd2...) is VOID: it described
the superseded not-to-integrate insert-r1.tex bytes.

## Target and status

Unchanged from round 1: Problem G ledger OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL
(appH L3026-3029); item 099 is evidence for the named D=2 subclasses only, DERIVED
for those subclasses, closes nothing; dependencies 096/097/098 unchanged.

## Review-response record (every finding)

- BLOCKING (bare `u`, 093 collision at appH L3199): FIXED. Snippet adopted verbatim:
  "combining this independence with the exact density \(6(1-2p_{2})^{2}\),
  \(0<p_{2}<1/2\), of the smaller entry \(p_{2}\) of the spectrum coordinate and the
  affine fibre map gives" and "\(\rho=\beta\tau(p_{1}-p_{2})\)". Third occurrence
  \((\tau,u,x)\)->\((\tau,p_{2},x)\) (one-line deviation, disclosed below). Enforced
  by a new machine check `ins.nobareu` (regex for standalone u; PASS in
  hygiene_099_r2.out). Ordering p1>=p2 inherited from p=(lambda1,lambda2)/tau of the
  preceding paragraphs, as the review notes.
- MINOR (Coordinates sentence, proposal file only): REWORDED; corrected authoritative
  wording given in the next section.
- MINOR (coordinator-transcript artifact, sha8 mixup): no action required, noted.
- NANO (7-decimal targets in Decisions vs 6-decimal insert): acknowledged; insert
  rounds correctly from the gatekeeper's exact values (0.267989031/0.475265655).

## Coordinates wording (corrected, authoritative for this item)

The r1 sentence misstated the convention. Correct statement: under the manuscript's
block convention p=lambda/tau (so p=(p1,p2), p1+p2=1, p1>=p2), the map p<->u is
bijective with u=lambda2/tau=p2; tau is NOT part of p. The quantity computed and
reported is I(u;.)=I(p;.), the mutual information between the (normalized) spectrum
coordinate and the fibre coordinate. Conditioning on the full unnormalised spectrum
(lambda1,lambda2)=(tau,u) is strictly richer than conditioning on u alone: the
conditional law of x given (tau,u) genuinely depends on tau (rho=beta*tau*(p1-p2)),
so I((tau,u);x)>I(u;x) by strict concavity of entropy under mixtures. The numerical
scripts marginalize tau exactly and compute I(u;.), which is the correct reported
target.

## Decisions Taken

- **u-elimination over inline define (RESEARCHER-DECISION).** Adopted the
  gatekeeper's elimination recommendation. Reason: an inline "where u=lambda2/tau"
  would leave a bare-u token whose block-adjacent meaning is 093's u=|p1-p2|
  (appH L3199); the collision persists for any later reader of the ledger block, and
  p2/p1-p2 notation is native to the preceding 089-098 paragraphs. Rejected: inline
  define (leaves collision); rejected: redefining 093's u (out of scope, edits prior
  integrated text).
- **Deviation from the verbatim snippet (one occurrence).** The snippet kept
  "\((\tau,u,x)\)", a third bare-u token. Since the r2 brief requires bare u
  eliminated ENTIRELY, it became "\((\tau,p_{2},x)\)". This is a renaming of a
  dummy coordinate (u=p2 by the block convention); the joint density is the same
  object; ASCII kept. Alternative rejected: deleting the coordinate triple (loses
  specificity). Recorded here because the insert bytes differ from the literal
  snippet in this clause only.
- **r2 file convention.** insert-r1.tex and the hygiene_099b pair retained as
  lineage (SUPERSEDED, not-to-integrate); gen_insert_099_r2.py is the sole byte
  authority for insert-r2.tex; simulate_apply_099_r2.out is the sole POST contract
  authority for r2. Nothing deleted; verify_099 evidence rows unchanged.

## Proposed changes

Single paragraph, same splice point as r1: between the live 098 paragraph (tail ends
"...they close nothing in Problem~G.") and the line-initial `\emph{Vacuum term.}` of
the next paragraph in chapters/appH-microscopic-proofs.tex; byte cut 755141; POST =
d[:755141] + insert-r2.tex + CRLF + d[755141:]. No bib entries, no labels/refs, no
ch17 edits, no status text. The full insert (byte authority gen_insert_099_r2.py,
1656 B = paragraph + terminal CRLF):

```latex
\emph{Mutual information between the Gram spectrum and the diagonal fibre coordinate at \(D=2\).} In the constant-variance \(D=2\) class the fibre coordinate \(x=(G_{11}-\lambda_{2})/(\lambda_{1}-\lambda_{2})\) is exactly uniform on the unit interval and exactly independent of the spectrum for every \(M\), by right-unitary invariance, so the mutual information between the spectrum and the fibre coordinate vanishes identically; at \(M=2\), combining this independence with the exact density \(6(1-2p_{2})^{2}\), \(0<p_{2}<1/2\), of the smaller entry \(p_{2}\) of the spectrum coordinate and the affine fibre map gives in closed form \(I(p;d_{1})=I(p;t)=I(p;P_{2})=2-\ln 6=0.2082405308\) nats for the ordered-diagonal, pair and quadratic-statistic channels, where \(t=|2d_{1}-1|\). In the column-profile class with \(g_{1}\neq g_{2}\) the conditional density of the fibre coordinate given the spectrum is the truncated exponential \(e^{-\rho x}\) on the unit interval with \(\rho=\beta\tau(p_{1}-p_{2})\) and \(\beta=1/(\sigma^{2}g_{1})-1/(\sigma^{2}g_{2})\), and nested quadrature on the exact joint density of \((\tau,p_{2},x)\), cross-checked by direct Wishart sampling, gives \(I(p;x)=0.0108991\) at \(M=2\) and \(0.0327074\) at \(M=4\) and \(I(p;P_{2})=0.267988\) at \(M=2\) and \(0.475266\) at \(M=4\) nats for \(g=(1,2)\); these values are exactly independent of \(\sigma\), invariant under \(g_{1}\leftrightarrow g_{2}\), and tend to the constant-variance values as \(\beta\to 0\). These are spectrum-side numbers about a fibre coordinate: they bound no state-side profile weight, identify no simplex fibre, and they close nothing in Problem~G.
```

Stale passages elsewhere: none introduced by r2; r1's Proposed-changes block is
superseded by this one (lineage retained in proposal-r1.md).

## Verification scripts and reproduction pack (r2)

From repo root with `python -I`; r1 pack (proposal-r1.md) remains valid for the
mathematics (rederive_099.py etc. unchanged and still passing).

1. `python -I proposals/099-g-mi-p-d-d2/gen_insert_099_r2.py` -> must print
   `bytes=1656 sha256=aa19ac668cc8a59c4473f69f829b739507d07f3f3da1b8a3274876b5a4ed2525`
   and `bare_u=0`; regenerates insert-r2.tex byte-identically (re-verified with cmp).
2. `python -I proposals/099-g-mi-p-d-d2/hygiene_099_r2.py` (hygiene_099_r2.out) ->
   19 PASS + `SUMMARY ALL PASS`, including the new `ins.nobareu` check and unchanged
   live-appH pins (791958 B / 711ed76d..., CRLF 3860, bareLF 0, idiom 24, verb 1,
   vac 2, 620-B tail == d[754517:755137], compound probe 1, cut 755141).
3. `python -I proposals/099-g-mi-p-d-d2/simulate_apply_099_r2.py`
   (simulate_apply_099_r2.out, ends `no write performed`) -> POST contract above:
   `POST bytes=793616 sha256=7cd6e208...5885`, CRLF 3862, bareLF 0, idiom 25, verb 1,
   vac 2, hdr 1, adj 1/1, old-seam 0; expected line printed by the script matches.

## Milestone assessment

Routine (same as r1): notation repair plus re-issued byte contract; no critical-path
step closed; no milestone trigger.

## Status-label recommendation

Unchanged. G remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; critical-path set
(A, B, C, D1, E, F, G-derived, N per ch17) unaffected. No label changes proposed.

## Author decision needed

none

## Remaining open step

Unchanged from r1: Problem G missing steps (i)-(iv) untouched; to move G itself a
core-action derivation of the state-side profile weight remains the next required
calculation.

## Special instructions for the gatekeeper (r2)

1. Verify only the delta: (a) insert-r2.tex bytes vs gen_insert_099_r2.py (byte
   authority), (b) zero bare-u tokens (regex `(?<![A-Za-z])u(?![A-Za-z])`), (c) the
   two snippet replacements are verbatim as in review-r1 "Corrected snippet",
   (d) the one disclosed deviation \((\tau,p_{2},x)\) is a legitimate renaming
   (u=p2), (e) hygiene_099_r2.out and simulate_apply_099_r2.out reproduce,
   (f) POST sha 7cd6e208... from live bytes.
2. Do NOT re-derive the numerics (accepted r1, confirmed <=4e-7 by your exact path);
   no live file cites the VOID r1 POST (793516/fae8dcd2) except lineage docs
   (proposal-r1.md, review-r1.md) and the manifest, which marks it VOID.
3. Do not integrate insert-r1.tex bytes or use hygiene_099b.py/simulate_apply_099.py
   outputs as the r2 contract; the integrator must re-verify anchors against the live
   tree at integration time.
