# Proposal 061-g-sent-replica-obstruction-and-cut-benchmark, round 3

## Result
Single mechanical fix per review-r2 (F9). The analytic infrared tail in the
shipped script `halfline_r2.py` used the wrong primitive: the log part must be
\(\int_0^{u} t\ln(1/t)\,dt = \tfrac{u^2}{4}(1-2\ln u)\), not
\(\tfrac{u^2}{2}(1-2\ln u)\) (the \(b_{\rm tail}\) part \(\tfrac{u^2}{2}b\) was
correct). I verified the correction independently (see Research) and patched
the shipped script in place; the regenerated `halfline_r2.out` gives tail
\(0.000232\) (was 0.000464), route-A total \(0.048728\) (was 0.048959), route
agreement \(1.665\) percent (was 1.183; the gatekeeper's predicted 1.664
differs only in the printed last digit — my shipped `.out` is authoritative).
Route B (0.049539), the direct sum (0.048496), the doubling slopes, the
\(b\)-series, the ratios, and every other quoted value are byte-identical in
the regenerated output (diff over the whole file shows only the three tail
lines). `insert-r3.tex` = `insert-r2.tex` with exactly the two affected numeric
tokens changed (diff: lines 65 and 68); paragraph 1 and paragraph 3 are
byte-identical to r2 (block hashes below). The shipped script reproduces the
shipped `.out` byte-identically under `python -I` (verified by a full rerun +
`cmp`). F1-F8 remain CLOSED per the gatekeeper. Problem G remains OPEN; labels
unchanged.

## F9 closure (analysis + disclosure record)
- Gatekeeper's analytic correction: \(\int_0^u t\ln(1/t)\,dt
  = -\left[\tfrac{t^2}{2}\ln t-\tfrac{t^2}{4}\right]_0^u
  = \tfrac{u^2}{4}(1-2\ln u)\). Independently re-derived here. The measure
  prefactor \(1/(2\pi)\) in the tail is also re-checked here:
  \(\mu^2=4\sin^2(p_1/2)+4\sin^2(p_2/2)\approx |p|^2\) near the zone center, so
  \(d^2p = 2\pi\mu\,d\mu\) and \(\int d^2p/(2\pi)^2 = (1/2\pi)\int \mu\,d\mu\) —
  the script's prefactor is correct; only the log coefficient was wrong.
  Corrected tail at \(u=0.05\), \(b_{\rm tail}=0.00077\):
  \((1/2\pi)[(1/3)(u^2/4)(1-2\ln u) + b_{\rm tail}u^2/2] = 0.000232\).
- Disclosure (gatekeeper, recorded verbatim in `review-r2.md`): the gatekeeper's
  own r1 `gk_sigma.py` tail used the same wrong form; its direct sum 0.048496
  stands and matches my direct sum exactly. The r1/gk σ totals
  (0.048959/0.04896) are superseded by 0.048728.
- Patch: `halfline_r2.py` line 108 coefficient `0.5*ut**2 -> 0.25*ut**2` on the
  log part only, with the primitive noted in an inline comment. Reproducibility:
  rerun + `cmp` -> BYTE-IDENTICAL.
- Decision: the optional bracketed range [0.0487, 0.0496] is NOT added to the
  insert: those rounded numbers appear in no shipped `.out`, so quoting them
  would violate the numbers-only-from-output rule. The two exact route values
  already bracket σ.

## F10 closure (traceability line references)
Corrected against the line numbers of the regenerated SHIPPED
`halfline_r2.out` (the file in this folder):
| insert number | line in shipped halfline_r2.out |
|---|---|
| mu_reg = 1e-5 | L1 |
| 0.31022 / 0.30788 / 0.30065 | L3 / L4 / L5 |
| 1/3 reference (two cuts, c=1) | L7 |
| 0.01740 / 0.00263 / 0.00030 / 0.00004 | L9 / L10 / L11 / L12 |
| 0.1935 (mu=1) / 0.1154 (mu=3) | L14 / L18 |
| 0.048496 direct + 0.000232 tail | L21 |
| 0.048728 route-A total | L22 |
| 0.049539 route B | L24 |
| 1.665 percent agreement | L25 |
| b_tail = 0.00077 (tail-integral input, not in text) | L20 |
Note flagged instead of adopted: the review-r2 suggestion "slopes at L4-L6,
1/3 reference at L12" does not match the layout of the shipped file (which has
no extra header lines); per rule, the table cites the verified line numbers of
the shipped `.out` itself. The b-series does end at L12 (the "L12" reference
corresponds to the b-series line, not the 1/3 reference, in the shipped file).

## Void declarations
`insert-r1.tex` and `insert-r2.tex` are VOID for integration (their σ/agreement
tokens carry the pre-F9 values). They are retained for audit only; not deleted.
`halfline_ee.py`/`halfline_ee.out` remain superseded r1 audit artifacts.

## Target and status
Unchanged from r2: Problem G ledger entry OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL; ch17 criterion item 7; chains retaining
Assumption~\ref{ass:dictionary} disqualified; G via ass:Sent-density depends on
Problem A. This package changes no status; it corrects benchmark numerics.

## Source reading
digest + targeted reads. r3 targeted reads: `review-r2.md` (saved verbatim this
round from the gatekeeper hand-back), Problem G/H passages of
`chapters/appH-microscopic-proofs.tex` (unchanged working tree, verified via
pre-state hash), ch06 L118-139, ch12/ch03 label passages as listed in
proposal-r2.md (unchanged). arXiv 1911.11145 record verified in r2 (2026-11-09).
No unreadable files.

## Proposed changes

### File 1: `chapters/appH-microscopic-proofs.tex` (insert only)
Same anchor and offset as r2 (re-verified in `simulate_apply_r3.out`):
`scope-limited model.` unique at 540076 + `\r\n\r\n`;
`\section{Problem H: modular origin of the interpolating function}` unique at
X = 540100; insert before the header. Only paragraph 2 of the insert differs
from r2 (two numeric tokens); P1/P3 unchanged.

insert-r3.tex (LF, 6120 B, sha256
7348ff056016b62ebf94ecfeeae7bf35ac8b819bf1bcbe7c1f888a4cbd9cb7fc):

```latex
\paragraph{Bounded obstruction: the replica density on Presentation-A data.}
The entropy density of Assumption~\ref{ass:Sent-density} is evaluated in
Section~\ref{sec:ch6-replica} through the replica formula~\eqref{eq:replica}:
\(\Tr\rho_D^n\) as a path integral on an \(n\)-sheeted cover of \(M\) branched
over the edge \(B\) of \(\partial M\). Restricted to Presentation~A, the
regularized trace over \(\mathcal H\) with cutoff~\eqref{eq:LUV-def} and matrix
coordinates~\eqref{eq:NC}, this object is undefined: the data supply neither a
manifold \(M\), nor a hypersurface \(\partial M\), nor a tubular neighbourhood,
nor a branched cover, nor a factorization of the trace over a region. The
boundary \(\partial M\) of the emergent spacetime is available only through the
infrared dictionary of Assumption~\ref{ass:dictionary}; the non-factorization
of region algebras in matrix models is established independently in the BFSS
setting in~\cite{Anous2020}. Two exits remain. (i) A Presentation-A cut:
spectral projections of the coordinate operators (Section~\ref{sec:ch6-modular}),
with the cut by the half-spectrum of a single coordinate operator as their
non-geometric variant, define a one-particle cut (the algebra of these
projections is itself stated in that section only after the dictionary of
Assumption~\ref{ass:dictionary}), and for quadratic fluctuations
\(\Tr\rho_D^n\) is defined by Fock factorization over the restricted
one-particle space; the
output is a functional of the quadratic kernel of the action and of the cut
projector, not a cover path integral and not a diffeomorphism scalar, and
reducing it to the local form~\eqref{eq:Sent-exp} requires a dictionary-type
identification of the cut with \(\partial M\), which is not derived.
(ii) Presentation~B with the dictionary, in which case any use of
\eqref{eq:Sent-exp} in \eqref{eq:Leff} inherits Assumption~\ref{ass:dictionary}
and cannot discharge the matrix-derived completion criterion while that
assumption is retained. The matrix-derived route through
Assumption~\ref{ass:Sent-density} therefore depends on Problem~A, and a
derivation chain recorded without this dependency is incomplete. A sharp
spectral cut of a quadratic kernel gives a strict area law
\(S=\sigma\Lambda_{\mathrm{UV}}^2 A_{\mathrm{cut}}\) of mass dimension two;
the density form \(\alpha_0\Lambda_{\mathrm{UV}}^3\) of \eqref{eq:Sent-exp} is
recovered from it only for a tube of width \(w=\Theta^{1/2}=\Lambda_{\mathrm{UV}}^{-1}\)
in the convention of \eqref{eq:LUV-def}, so the localization scale of
Assumption~\ref{ass:Sent-density} is forced by the cut rather than derived, and
in the thin-tube limit \(w\to0\) the density diverges as
\(\sigma\Lambda_{\mathrm{UV}}^2/w\).

\paragraph{Free benchmark in the constant-\(\Theta\) sector.}
For quadratic fluctuations about a constant \(\Theta\) background, with the
cubic term and the matter action in \eqref{eq:Smatrix} dropped, each transverse
Fourier mode \(p_\perp\) gives a one-dimensional quadratic problem whose cut,
in the sense of exit (i), is the half-spectrum of a single coordinate operator.
The computable form of this cut restricts the infinite one-dimensional chain to
a contiguous interval of \(N\) sites, which carries two entanglement cuts and
Toeplitz correlators; the restricted ground-state covariance \((C,D)\) has a
restricted symplectic spectrum \(\nu_k\ge\tfrac12\) (a kernel that does not
couple across the cut contributes only \(\nu_k=\tfrac12\) and no entropy), and
\(S_{\mathrm{cut}}=\sum_k[(\nu_k+\tfrac12)\ln(\nu_k+\tfrac12)-(\nu_k-\tfrac12)\ln(\nu_k-\tfrac12)]\).
The massless regime is approached through a mass regulator \(\mu=10^{-5}>0\) in
the correlator symbols; the \(k=0\) point of the massless symbol is not
integrable and is not dropped. Numerically, in lattice units with
\(\Lambda_{\mathrm{UV}}=\pi\): the interval entropy has doubling slopes
\((s_1(2N)-s_1(N))/\ln 2=0.31022,0.30788,0.30065\) approaching the
central-charge value \(c/3=\tfrac13\) for the two cuts of the interval at
\(c=1\); a mode of small mass \(\mu\) contributes
\(s_1(\mu)=\tfrac13\ln(1/\mu)+b(\mu)\) with \(b(\mu)\to0\) along the sequence
\(\mu=0.3,0.1,0.03,0.01\) giving \(b=0.01740,0.00263,0.00030,0.00004\); a mode
of large mass satisfies \(s_1(\mu)\le\tfrac\pi2 e^{-\mu}\) with a large margin
(the ratio \(s_1(\mu)/(\tfrac\pi2 e^{-\mu})\) falling from \(0.1935\) at
\(\mu=1\) to \(0.1154\) at \(\mu=3\); no saturation of the bound is claimed);
and the two-cut slab density
\((2\pi)^{-2}\int_{\mathrm{BZ}^2}d^2p_\perp\,s_1(\mu(p_\perp))\) with
\(\mu^2=4\sin^2(p_1/2)+4\sin^2(p_2/2)\) evaluates to \(0.048728\) (direct
quadrature on a \(64^2\) offset Brillouin-zone grid for \(\mu\ge0.05\) plus the
analytic infrared tail) and to \(0.049539\) by an independent interpolation
route, a \(1.665\) percent agreement. Since the interval carries two cuts, the
single-cut surface coefficient is one half of the logarithmic term. With
\(w=\Theta^{1/2}=\Lambda_{\mathrm{UV}}^{-1}\) the tube identification above
fixes \(\alpha_0\) in \eqref{eq:Sent-exp} to the single-cut coefficient at the
free level; \(\alpha_1\) and \(\alpha_2\) are not computed. These are
conditional benchmark values in a quadratic truncation of \eqref{eq:Smatrix} at
finite regulator; they do not derive Assumption~\ref{ass:Sent-density}, and
Problem~G remains open.

\paragraph{Missing step.}
Closing the matrix-derived criterion for Problem~G requires, beyond the
present note: (i) a derivation, not a retained dictionary, of the
identification between a Presentation-A boundary cut and \(\partial M\) under
which the cut entropy becomes the local density \eqref{eq:Sent-exp}; (ii) the
interacting condensate sector of \eqref{eq:Smatrix}, the cubic term, matter
and non-Gaussian ground-state correlations, which carry the \(\alpha_1\) and
\(\alpha_2\) structures; (iii) a derivation of the stationarity
condition~\eqref{eq:bdy-EE} of Assumption~\ref{ass:bdy-EE}; and (iv) the
mass-dimension-one boundary-to-bulk conversion recorded in the dimensional
status remark of Chapter~\ref{ch:hbev}, without which \eqref{eq:Leff} stays
schematic.
```

Paragraph-block byte-identity vs r2 (verified): P1 (2723 B) sha256
883eba64c81a3751385a339130255648ea91389e79080bd74011a7e418ffef84 identical;
P3 (772 B) sha256 c7e24bf9bb410a6b65eb28e9f80f01396f35d8c809fe8aeeb5df5f6588d501b1
identical. Diff `insert-r2.tex` vs `insert-r3.tex`: exactly two lines, both in
paragraph 2 (saved as `insert_diff_r2_r3.txt`):
- `\(...\) evaluates to \(0.048959\) (direct` -> `... \(0.048728\) (direct`
- `route, a \(1.183\) percent agreement. ...` -> `route, a \(1.665\) percent agreement. ...`

### File 2: `bib/namcg.bib` (append only) — UNCHANGED from r2
Corrected Anous2020 entry (414 B, entry sha256
200c81f80f715133d0e29b688fb5b900945e0ed1b469c4b2355edf244524a9ee; bytes
re-verified this round to be identical to the fenced block in proposal-r2.md and
to the appended bytes in `simulate_apply_r3.py`):

```bibtex
@article{Anous2020,
  author  = {Anous, Tarek and Karczmarek, Joanna L. and Mintun, Eric and Van Raamsdonk, Mark and Way, Benson},
  title   = {{Areas and entropies in BFSS/gravity duality}},
  journal = {SciPost Phys.},
  volume  = {8},
  pages   = {057},
  year    = {2020},
  doi     = {10.21468/SciPostPhys.8.4.057},
  eprint  = {1911.11145},
  archivePrefix = {arXiv},
  primaryClass = {hep-th}
}
```

### APPLY RULE r3 (single pass; supersedes r1 and r2 rules)
1. Assert appH pre-state: `chapters/appH-microscopic-proofs.tex` size 560743,
   sha256 `fe02de8970b7dee8b0df8cad9a84ca557b1ecf41bc9d2b4984135a50b8faab8d`,
   CRLF 3326, bare LF 0. Assert `scope-limited model.` exactly once at offset
   540076, followed by `\r\n\r\n`; assert
   `\section{Problem H: modular origin of the interpolating function}` exactly
   once at offset X = 540100.
2. Read `proposals/061-g-sent-replica-obstruction-and-cut-benchmark/insert-r3.tex`
   (raw 6120 B, sha256 `7348ff056016b62ebf94ecfeeae7bf35ac8b819bf1bcbe7c1f888a4cbd9cb7fc`).
   Right-strip trailing whitespace, convert every LF to CRLF, terminate with
   `\r\n\r\n`: 6210 B, CRLF 89, bare LF 0, sha256
   `90f279b8fd57519791205b92c1c1d04f61557939c62b5ec5451053b41c9b2d92`.
3. appH := bytes[:540100] + converted-insert + bytes[540100:]. Predicted
   post-state: size 566953, sha256
   `21737625769589a64090c8b7f93842b1eaa5d12cff3e4877f70f2db8e5947999`,
   CRLF 3415, bare LF 0.
4. Assert bib pre-state: 26936 B, sha256
   `6b4612d18c2884e9ff486053f80b9769aad26c71006b1fd034d2d7eb7303b3d2`, CRLF 896,
   bare LF 0, ends `}\r\n`, zero occurrences of `Anous2020`. Append the 414 B
   entry above (sha256 `200c81f80f715133d0e29b688fb5b900945e0ed1b469c4b2355edf244524a9ee`)
   as CRLF at offset 26936. Predicted post-state: size 27350, sha256
   `40d6ea09915dd4b8220f30c466821118492ee5560f66930b7c5d9a2dd8b95b90`, CRLF 908,
   bare LF 0.
5. `insert-r1.tex` and `insert-r2.tex` must NOT be integrated.

## Claim classification (changed items only; all others as in r2)
- \(\int_0^u t\ln(1/t)dt = (u^2/4)(1-2\ln u)\): established identity
  (elementary antiderivative; re-derived this round).
- \(\sigma_{\rm 2cut}\) route A = 0.048728: conditional numerical benchmark
  (supersedes 0.048959).
- Route agreement 1.665 percent: numerical (supersedes 1.183).
- \(\sigma\approx0.049\): unchanged conclusion.
- All other r2 classifications (bounded obstruction = established definitional
  within hypothesis class; slope 1/3 conditional/numerical; b→0 numerical;
  exponential-bound margin numerical; α₀ bookkeeping conditional; Anous2020
  established literature) unchanged.

## Verification scripts (proposal folder; `python -I`)
- `halfline_r2.py` (patched F9) + `halfline_r2.out` (regenerated): the shipped
  pair; rerun reproduces the `.out` BYTE-IDENTICALLY (verified with `cmp`).
- `insert_diff_r2_r3.txt`: `diff insert-r2.tex insert-r3.tex` (exactly two
  lines, both in paragraph 2).
- `simulate_apply_r3.py` + `simulate_apply_r3.out`: pre-state assertions (appH
  560743/fe02de89.../CRLF 3326/bare LF 0 still current), anchors 540076/540100,
  insert hashes, predicted appH post sha 21737625..., bib 414 B append,
  predicted bib post 27350 B / 40d6ea09....
- `continuum_check.py` + `continuum_check.out`: unchanged from r2 (no σ
  numbers used).
- Audit-only: `insert-r1.tex`, `insert-r2.tex` (VOID), `halfline_ee.*`,
  `anchor_check.out`, r1/r2 proposal and simulate files, `review-r1.md`,
  `review-r2.md`.

## Decisions Taken
- Patched `halfline_r2.py` in place rather than shipping `halfline_r3.py`:
  keeps the script/.out name pair the gatekeeper already verified; the shipped
  pair now reproduces byte-identically.
- Kept all non-tail computations untouched; whole-file diff confirms only the
  three tail-related output lines changed (no drift flag raised).
- Did not adopt the gatekeeper's suggested traceability line numbers (L4-L6,
  L12) verbatim: they do not match the shipped `.out` layout; the table cites
  verified line numbers instead, with the discrepancy flagged.
- Did not add the optional range [0.0487, 0.0496] (unsourced rounding; the two
  exact route values already appear).
- Quoted 1.665 (printed value) rather than the gatekeeper's predicted 1.664;
  difference is last-digit rounding of the full-precision ratio; shipped `.out`
  authoritative.

## Milestone assessment
Routine (numeric correction; no status change, no closure).

## Status-label recommendation
Unchanged. Critical-path list re-derived from ch17 (A, B, C, D1, E, F,
G-derived, N); Problem G remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed
None.

## Remaining open step
Unchanged from r2: Missing-step (i)-(iv); single-cut (one-boundary) computation;
\(\mu_{\rm reg}\to0\), \(N\to\infty\) continuum-limit control; analytic proof
of the \((\pi/2)e^{-\mu}\) bound. F7 report-only.

## Special instructions for the gatekeeper
- Rerun `halfline_r2.py`; expect BYTE-IDENTICAL `halfline_r2.out` (verified
  here by `cmp`). Only L21, L22, L25 differ from the r2 output.
- Verify the two changed insert tokens (0.048728 at L22, 1.665 at L25 of the
  `.out`) and the `insert_diff_r2_r3.txt` two-line diff; verify P1/P3 block
  hashes (883eba64..., c7e24bf9...) match the r2 blocks you already checked.
- Apply-rule hashes: insert-r3 raw sha 7348ff05..., converted sha 90f279b8...
  (6210 B, CRLF 89), appH post sha 21737625769589a64090c8b7f93842b1eaa5d12cff3e4877f70f2db8e5947999
  (566953 B, CRLF 3415), bib entry sha 200c81f8..., bib post 40d6ea09...
  (27350 B).
- Do not integrate insert-r1.tex / insert-r2.tex.
- Must not be asserted: closure of G; obstruction beyond the replica/cover
  realization on A-data without the dictionary; saturation of the large-mass
  bound; any massless additive constant; any rounded σ range.
