# Proposal 101-g-p2-conditional-density-d3, round 2

## Result

Round 2 implements the gatekeeper's three required text corrections and nothing else. The new
insert insert-r2.tex (2848 B, sha256 1b2fa7f8...) states (i) the Laplace-transform/HCIZ identity
with the correct type-A normalization, the factor 2=(D-1)! in the NUMERATOR, with the Vandermonde
Delta explicitly defined; (ii) Lambda defined as the ordered spectrum of the normalized fibre
Gram block G/tau (resolving the collision with the adjacent 099/100 Wishart-rate Lambda and
matching 098's d_i=G_ii/tau convention); (iii) the HCIZ source vector renamed a -> t, killing the
a/s overloads. A machine check (verify101_r2.py) PROVES insert-r2 equals insert-r1 under exactly
the two mandated substitutions -- no other character of the verified r1 text changed. The
mathematics is unchanged from r1 and was independently re-derived by the gatekeeper (own
Fractions arrangement, closed-form plateau/breakpoints, theta-quadrature integrating to 1.000000,
own complex-Haar MC); no numeric claim was altered, so no numeric script needed re-running
except hciz101b.py, whose header comment is now corrected while its code body is byte-identical
to hciz101.py and reproduces the same invariants (max rel 1.65e-16). Fresh byte-locked POST:
798,457 B, sha256 cfb6af516017367f6a22a9b0846df068c07e43e25d9ac8fad67c1d6497f5d438, CRLF 3866,
bareLF 0, idiom 26->27, Vacuum 2, header unique, outside-splice bytes identical.

## Target and status

- Problem G (HBEV), `chapters/appH-microscopic-proofs.tex`, `\label{sec:status-G}`. Live ledger
  re-read this round (file unchanged, 795607 B / 3f1b030c): "Status: OPEN. Priority: CRITICAL
  PATH. Completion: PROGRAMME-CONDITIONAL." Unchanged by this package; nothing closed.
- Package target (round 1, revised to integrable form per review): exact conditional density of
  P2 under the uniform fibre law at D=3, fibre-side sharpening of G.moments. PROGRAMME-
  CONDITIONAL; presents no status claim.

## Source reading

digest + targeted reads. Read fully this round: `review-r1.md` (verdict ACCEPT WITH REQUIRED
REVISIONS, 1 blocking + 2 major + minors); live appH anchor seam and Problem G ledger opening
(re-measured: 795607 B, sha 3f1b030c, anchor count 1, idiom 26, CRLF 3864, bareLF 0);
`\operatorname` usage count in appH (206, so the snippet's `\operatorname{diag}` is idiomatic and
safe; amsmath loaded at namcg-book7.tex line 15). No chapters/ file modified.

## Research and reasoning

- **Finding 1 (blocking, HCIZ factor).** Accepted verbatim. Genuine defect confirmed
  independently: the insert's printed det/(2*Delta(a)Delta(lambda)) is 4x wrong because the
  script's own values match 2*det/(Delta(t)Delta(lambda)) (hciz101b.py line 55 already computes
  `2*dt/(D(a)*D(Lam))  # (N-1)! = 2 for U(3)`; the r1 text inverted the factor). New clause
  matches the review snippet character-for-character. hciz101b.py header comment fixed
  (a=(-s1,-s2,0) -> t=(s1,s2,0) with numerator-2 note); code body asserted byte-identical to
  hciz101.py and output invariants reproduced exactly (Z rel 2.3e-16; max rel 1.65e-16).
- **Finding 2 (major, Lambda).** Accepted verbatim. New opening defines lambda as the ordered
  spectrum of G/tau and puts Lambda=diag(lambda); downstream mentions ("given $\Lambda$",
  "diagonal of $U\Lambda U^{\dagger}$") are now anchored to a defined object.
- **Finding 3 (major, Delta + t-rename).** Accepted verbatim; Delta defined inline as the
  Vandermonde product at first use; source vector renamed t. The eigen-coordinate a=(u1+u2)/sqrt2
  keeps its name (it is the plane coordinate, not the source vector).
- **No other text changes.** Enforced mechanically: verify101_r2.py asserts
  `r1.replace(o1,n1).replace(o2,n2) == r2` with each old/new pattern unique in its file.
- **Minors.** "|z|<=2" and "2*10^-16" kept (conservative; gatekeeper ruled acceptable). The
  num104b.out tail print label ("f(0.4599)") is a print label only; no manuscript claim depends
  on it; left as-is per "do not touch unflagged text".
- **Gatekeeper's general-moment remark** (Ed_i=1/3 and EP2=(1+Sum lam^2)/4 hold for ALL lambda
  via the Dirichlet(1,1,1) row-moduli argument): the insert keeps the conservative
  "exactly at both spectra" wording; adopting the general statement would import a proof not
  yet written in this package. Recorded as a cheap follow-up below.

## Claim classification

Unchanged from round 1 except as noted: Kostant-sum density rho-hat and the arrangement lemma
-- established (self-contained derivation, exact rational check at both spectra); Z = Delta/2 at
the two spectra -- established (exact; a third-spectrum corroboration Z=3/1000 at
lambda=(0.5,0.3,0.2) came from the gatekeeper, NOT imported as proof); general-lambda Z=Delta/2 --
conjecture; E d_i = 1/3, E P2 = (1+Sum lam^2)/4 at both spectra -- established (insert wording
stays "both spectra"; the gatekeeper's general-lambda Dirichlet argument is conditional-until-written
here); coarea Jacobian factor sqrt(3)/6 -- established (symbolic, jac101b.py); density
plateau 40*pi/(3*sqrt(3)) on [1/3,67/200], breakpoints, endpoint 23/50 -- established at the
displayed spectra; MC agreement -- conditional numerical check; HCIZ/Laplace identity as now
printed (2 in numerator, Delta defined, source t) -- established numerically to 1.65e-16 at the
two spectra; general literature HCIZ statement -- NOT independently verified (no external source
imported; the printed identity is checked against the package's own exact Z).

## Proposed changes

One file: `chapters/appH-microscopic-proofs.tex`, splice at the unique anchor
`close nothing in Problem~G.\r\n\r\n\emph{Vacuum term.}` (count 1). Rule:
post = pre[:p] + insert-r2.tex bytes + pre[p:], p = find(anchor) + len("close nothing in
Problem~G.\r\n\r\n"). insert-r2.tex body is enclosed in fenced latex in proposal-r1.md's
Proposed changes section, r1 body; the ONLY differences are the two review snippets (prove by
diff). Keep all r1 text otherwise. Stale passages elsewhere: none (no other file references
this insert). POST contract (round 2, byte-locked against live PRE 795,607 / 3f1b030c...):
size 798,457; sha256 cfb6af516017367f6a22a9b0846df068c07e43e25d9ac8fad67c1d6497f5d438; CRLF 3866;
bareLF 0; idiom 26->27; `\emph{Vacuum term.}` stays 2; header line unique; bytes outside the
splice window identical. The r1 POST (798,295 / 000dbd83...) is superseded lineage.

## Verification scripts

All in this folder. Reproduction pack (run `python -I <script>` from this folder; python 3.13):
- gen_insert_101_r2.py -> "2848 bytes" and sha 1b2fa7f8... (regenerates insert-r2.tex).
- ..\..\scratch\verify101_r2.py -> "EXACT two-region substitution confirmed" (r2 = r1 + the two
  review snippets, nothing else).
- hygiene_101_r2.py -> ALL PASS (insert-r2 structure; live appH PRE contract 795607/3f1b030c/
  idiom 26/Vacuum 2/CRLF 3864/anchor 1; r2 markers present; stale r1 HCIZ/a=(s1,s2,0) patterns
  absent). Output: hygiene_101_r2.out.
- simulate_apply_101_r2.py -> all PASS + "POST size: 798457" + "POST sha256: cfb6af51...d438" +
  "no write performed". Output: simulate_apply_101_r2.out.
- hciz101b.py -> Z rel 2.3e-16; max rel 1.65e-16 (identical numbers to hciz101.out; header
  comment fixed only). Output: hciz101b.out.
- r1 pack unchanged and re-validated by the gatekeeper: exact103.py (Z=3/200, 73/200),
  exact103b.py (Z=117/4000, 311/800), exact101b.py, jac101b.py (PASS, ratio sqrt(3)/6),
  num104b.py (max|z| 1.83), mc101b.py (max z 1.43), mc101d.py (corr 0.9902, trapz 1.00000,
  E[P2] 0.388732), sym101.py (mode0 corr 0.9967). manifest.md lists size+sha256 of every file.

## Decisions Taken

Used all three review snippets verbatim (deviations: none). Rejected alternatives: (a) keeping
the r1 HCIZ denominator form with a rephrased definition of Delta -- rejected, mathematically
wrong by 4x; (b) renaming Lambda to M instead of defining Lambda:=spectrum(G/tau) -- rejected,
the review snippet's route matches 098's d=G/tau convention and was mandated verbatim;
(c) upgrading the moment identities to all-lambda wording -- rejected this round (would import an
unwritten proof; the conservative statement is true either way). Kept r1 artifacts as lineage
on disk, marked superseded in manifest.md. New filenames used for every touched file per the
echo-mitigation directive.

## Milestone assessment

Routine. No milestone trigger: no critical-path step derived, no missing link closed.

## Status-label recommendation

Derived from current ch17-agenda + Appendix H (A, B, C, D1, E, F, G-derived, N critical path):
unchanged. No labels proposed for change.

## Author decision needed

none

## Remaining open step

Unchanged from r1: (i) prove Z(lambda)=Delta(lambda)/2 for general lambda at D=3; (ii) extend
beyond D=3; (iii) exact tilted (interaction-induced) P2 density; (iv) derive the DH measure
from the 096 Jacobian rather than postulating it. New cheap step: write the general-lambda moment
proof (Dirichlet(1,1,1) row-moduli) in-package, which would let the insert drop "both spectra".

## Special instructions for the gatekeeper

Re-derive the POST sha by splicing insert-r2.tex into the live appH bytes; the expected value
is cfb6af51...d438 at 798,457 B. Verify the two review snippets appear verbatim in insert-r2.tex
and that insert-r2 differs from insert-r1 only there (verify101_r2.py). Do NOT assert the HCIZ
identity as proven from literature -- it is checked against package-internal exact Z only.
Do NOT treat the third-spectrum Z corroboration (gatekeeper's own) as part of this package.
r1 files in this folder are lineage; manifest.md marks every superseded file.
