# Proposal 061-g-sent-replica-obstruction-and-cut-benchmark, round 2

## Result
Round 1's bounded definitional obstruction (paragraph 1: the replica density of
Assumption~\ref{ass:Sent-density}, i.e. \(\Tr\rho_D^n\) as a cover path integral,
is undefined on bare Presentation-A data; the two named exits are exhaustive
under the ch17 replica-derivation requirement; the matrix-derived route through
ass:Sent-density depends on Problem A) is unchanged and was gatekeeper-verified
ACCEPT-quality. Round 2 replaces the failing benchmark numerics of paragraph 2
(F1, F2) with a fully recomputed quasi-free cut benchmark using a valid mass
regulator (\(\mu_{\rm reg}=10^{-5}>0\); the non-integrable \(k=0\) point of the
massless symbol is never dropped), computed on the interval \([1,N]\) of the
infinite chain (two entanglement cuts): the doubling slopes
\((s_1(2N)-s_1(N))/\ln 2 = 0.31022, 0.30788, 0.30065\) approach the
central-charge value \(c/3=1/3\) for two cuts at \(c=1\);
\(s_1(\mu)=\tfrac13\ln(1/\mu)+b(\mu)\) with \(b\to0\) along
\(\mu=0.3,0.1,0.03,0.01\) (\(b=0.01740,0.00263,0.00030,0.00004\)); the large-mass
bound \(s_1(\mu)\le(\pi/2)e^{-\mu}\) holds with a large margin (ratio falling
from \(0.1935\) at \(\mu=1\) to \(0.1154\) at \(\mu=3\), no saturation claimed);
and the two-cut slab density evaluates to \(0.048959\) (direct quadrature +
analytic IR tail) and \(0.049539\) (independent interpolation route),
\(1.183\%\) agreement, so \(\sigma\approx0.049\). Every number quoted in
insert-r2.tex appears in a shipped `.out` file (traceability table below). The
Anous2020 BibTeX author list is corrected per the live arXiv record (F3), and
the apply rule now includes the `bib/namcg.bib` append (059 precedent). My
independent values reproduce the gatekeeper's reference values (F1:
\(\sigma=0.04896\); F2: slope 1/3, \(b\)-series; F6: ratio \(0.1178\) at
\(\mu=2.5\), \(s_1(2.5)=0.015185\)). Problem G remains OPEN; nothing is closed.

## Target and status
- Problem: G (modular origin of the interpolating function; G.ent / HBEV entry),
  `chapters/appH-microscopic-proofs.tex`, Problem G ledger section.
- Current status re-read from the working-tree ledger (appH working bytes, G
  section, lines ~2823-2842 of the byte-anchored read used in r1): **OPEN /
  CRITICAL PATH / PROGRAMME-CONDITIONAL**. Chapter 17 full-GR criterion item 7
  (ch17 L723-726) requires the G-derived interpolating density; chains that
  retain Assumption~\ref{ass:dictionary} cannot discharge the matrix-derived
  criterion (ch17 L696-698). No discrepancy found between ch17 and Appendix H.
- Original target: derive the entropy-density structure
  \eqref{eq:Sent-exp} of Assumption~\ref{ass:Sent-density} (hence
  \eqref{eq:Leff}) from the matrix-model data, for the stated full-GR scope.
- Dependencies recorded: G via ass:Sent-density depends on Problem A (paragraph 1
  of the insert, ACCEPT-quality in r1); eq:Leff contains \Geff with F.coeff before
  G.2 (review F7, report-only, no action here).
- Classification of this package: PROGRAMME-CONDITIONAL evidence (bounded
  no-go + conditional free benchmark). DERIVED: the definitional obstruction
  itself (proved at the level of definitions, within its stated hypothesis
  class). Nothing on the critical path is claimed closed.

## Source reading
digest + targeted reads. Digest status: relied on the run digest from the
current cycle; targeted reads IN FULL: Problem G and Problem H ledger passages
of `chapters/appH-microscopic-proofs.tex`; `chapters/ch17-agenda.tex` L696-698
and L723-726; `chapters/ch06-entanglement-equilibrium.tex` L118-139
(sec:ch6-modular label L123, spectral-projection prose L125-130 "after the
dictionary of Assumption~\ref{ass:dictionary}", def:rhoD L132-138) and
L176-181 (sec:ch6-replica, eq:replica); `chapters/ch12-*.tex` passages for
ass:Sent-density L139, eq:Sent-exp L147, ass:bdy-EE L185, eq:bdy-EE L190,
eq:Leff L215, ch:hbev L2; `chapters/ch03-*.tex` ass:dictionary L346,
eq:LUV-def L119, eq:Smatrix L143, eq:NC L106; `proposals/061-*/review-r1.md`
(read IN FULL, all findings F1-F8 and the Corrected snippet); `bib/namcg.bib`
tail (no Anous2020 entry present). Unreadable files: none. arXiv record for
1911.11145 fetched and verified 2026-11-09 (title, authors, SciPost Phys. 8,
057 (2020), DOI 10.21468/SciPostPhys.8.4.057).

## Research and reasoning

### F1/F2 re-computation (valid IR regulator; own scripts)
Object (stated in `halfline_r2.py` docstring): per transverse mode \(p_\perp\),
the infinite 1D chain in lattice units \(a=1\) with \(\Lambda_{\rm UV}=\pi\)
(eq:LUV-def with \(\Theta^{1/2}=a\) up to \(O(1)\)); region = contiguous
interval of sites \([1,N]\), which has TWO entanglement cuts and Toeplitz
correlators. Covariance blocks from the full-BZ symbols
\(C_{ij}=\mathrm{ifft}(1/(2\omega))_{i-j}\), \(D_{ij}=\mathrm{ifft}(\omega/2)_{i-j}\),
\(\omega(k)=\sqrt{\mu^2+4\sin^2(k/2)}\), restricted to \([1,N]\). Restricted
symplectic spectrum \(\nu_k^2=\mathrm{eig}(D^{1/2}CD^{1/2})\) with diagnostic
count of eigenvalues below \(1/4\) (0 at every point in the shipped output),
entropy \(s_1=\sum_k[(\nu+\tfrac12)\ln(\nu+\tfrac12)-(\nu-\tfrac12)\ln(\nu-\tfrac12)]\).
The massless regime is approached only through \(\mu_{\rm reg}=10^{-5}>0\); the
\(k=0\) point of the massless symbol \(1/(2|\sin(k/2)|)\) is non-integrable and
is never dropped (the r1 script's treatment — dropping it — is invalid and its
output is superseded).

Geometry correction (F2): the computed object is the two-cut interval, so the
CFT slope is \(c/3=1/3\) at \(c=1\), not \(1/6\); \(c/6\) is the single-cut
value. Doubling slopes at \(\mu_{\rm reg}=10^{-5}\): \(0.31022\) (256\(\to\)512),
\(0.30788\) (512\(\to\)1024), \(0.30065\) (1024\(\to\)2048); the 2048\(\to\)4096
slope \(0.27337\) drifts as the finite regulator saturates the interval
(\(N\sim10^4 \ll 1/\mu_{\rm reg}\) is no longer asymptotic), so the fourth value
and the additive constant \(s_1-\tfrac13\ln N\) (which drifts
\(1.424\to1.327\)) are NOT quoted. The r1 "constant" \(0.2315=(\ln 2)/3\) is
indeed the doubling increment at slope \(1/3\), not a constant (F2).

Small mass (F2): at \(N=20/\mu\) (capped 4096),
\(s_1(\mu)-\tfrac13\ln(1/\mu)=0.01740,0.00263,0.00030,0.00004\) for
\(\mu=0.3,0.1,0.03,0.01\): the additive constant in this normalization tends to
0 (matches gatekeeper's \(0.0174,0.0026,0.0003,4\times10^{-5}\)).

Large mass (F6): \(s_1(\mu)/((\pi/2)e^{-\mu})=0.1935,0.1505,0.1282,0.1178,0.1154\)
for \(\mu=1,1.5,2,2.5,3\): the inequality holds with large margin; no saturation
claimed; the r1 "0.9775" is deleted.

Slab density: \(\sigma_{\rm 2cut}=(2\pi)^{-2}\int_{\rm BZ^2}d^2p_\perp\,
s_1(\mu(p_\perp))\), \(\mu^2=4\sin^2(p_1/2)+4\sin^2(p_2/2)\). Route A: direct
\(s_1(\cdot,512)\) on a \(64^2\) offset BZ grid for \(\mu\ge0.05\)
(= \(0.048496\), identical to the gatekeeper's direct sum) plus the analytic
tail over \(\mu<0.05\) with \(s_1\sim\tfrac13\ln(1/\mu)+b_{\rm tail}\),
\(b_{\rm tail}=0.00077\) computed from the check-(2) form at \(\mu=0.05\)
(gatekeeper used \(b\sim0.01\), tail \(0.000466\) vs my \(0.000464\)): total
\(0.048959\). Route B: 16-point interpolation table of directly computed
\(s_1\) values evaluated on a \(512^2\) offset grid with the same tail:
\(0.049539\). Route agreement \(1.183\%\). Quote \(\sigma\approx0.049\).
Since the interval carries two cuts, the single-cut surface coefficient is one
half of the logarithmic term (stated symbolically; no halved decimal is quoted,
as no script prints it).

### F3 (BibTeX)
Live arXiv record for 1911.11145 (fetched 2026-11-09) confirms: Tarek Anous,
Joanna L. Karczmarek, Eric Mintun, Mark Van Raamsdonk, Benson Way; "Areas and
entropies in BFSS/gravity duality"; SciPost Phys. 8, 057 (2020); DOI
10.21468/SciPostPhys.8.4.057. The corrected entry below is what the apply rule
appends. The paper supports the manuscript sentence's claim (non-factorization
of region algebras in the BFSS setting) as cited in r1; citation practice
unchanged.

### F4
The r1 evidence-body numbers \(c0\_ref=0.144345\) and the continuum reference
\(0.008398\) matched no shipped output and are DELETED; they appear nowhere in
r2 or in insert-r2.tex. The r2 evidence chain consists only of
`halfline_r2.out` and `continuum_check.out`, whose printed values are
reproduced above and tabulated below.

### F5
ch06 L125-130 states that in Presentation A the algebra \(\mathcal A_D\) is
generated by spectral projections of \(\hat X^\mu\) restricted to \(D\) "after
the dictionary of Assumption~\ref{ass:dictionary}" (label
`sec:ch6-modular`, ch06 L123, verified unique; `def:rhoD` defines \(\rho_D\)
from a supplied algebra, so the r1 reference to it was the wrong anchor).
Exit (i) is reworded to the gatekeeper's corrected-snippet wording ("spectral
projections of the coordinate operators (Section~\ref{sec:ch6-modular}), with
the cut by the half-spectrum of a single coordinate operator as their
non-geometric variant") plus a parenthetical recording that the projection
algebra itself is stated in that section only after the dictionary — a
faithful paraphrase of ch06 L129-130, no mathematical change.

### Cross-check table (mine vs gatekeeper, independent codes)
| quantity | mine (halfline_r2.out) | gatekeeper (gk_truth/gk_sigma) |
|---|---|---|
| doubling slopes -> slope | 0.31022, 0.30788, 0.30065 -> 1/3 | "-> 1/3" (review F2) |
| b-series at mu=0.3/0.1/0.03/0.01 | 0.01740, 0.00263, 0.00030, 0.00004 | 0.0174, 0.0026, 0.0003, 4e-5 |
| ratio at mu=2.5 | 0.1178 (s1=0.015185) | 0.1178, s1(2.5)=0.015185 |
| sigma direct (64^2, mu>=0.05) | 0.048496 | 0.048496 |
| sigma total | 0.048959 (tail 0.000464) | 0.04896 (tail 0.000466) |
| second route | 0.049539 (interp table) | (not run) |

### Comparison with original target
The package does not derive \eqref{eq:Sent-exp} from matrix data. It (a) proves
a bounded definitional obstruction to the replica realization on bare A-data
and records the dependency G \(\leftarrow\) A; (b) supplies a conditional free
benchmark of the exit-(i) cut functional (quasi-free cut entropy, valid IR
regulation, \(\sigma\approx0.049\) two-cut / half that per cut at log level) and
the dimensional bookkeeping \(\alpha_0=\sigma/(\Lambda w)\), forced
\(w=\Theta^{1/2}\), thin-tube divergence \(\sigma\Lambda^2/w\). Missing-step
(i)-(iv) remain exactly as stated in the insert.

## Claim classification
- Bounded obstruction paragraph (incl. exits, \(\alpha_0=\sigma/(\Lambda w)\),
  forced tube width, thin-tube divergence): established definitional
  derivation within the stated hypothesis class (replica/cover realization on
  Presentation-A data without the dictionary); gatekeeper independently
  verified in r1. Does NOT rule out non-geometric entropy functionals on
  A-data (that is exit (i)).
- Quasi-free cut-entropy formula, \(\nu_k\ge\tfrac12\), decoupled-kernel
  identity \(s=0\): established identities (re-derived in continuum_check (iii)
  and by the gatekeeper).
- Two-cut slope \(1/3\): conditional/numerical (standard CFT value applied to
  the explicitly computed two-cut interval; numerics confirm).
- \(s_1(\mu)=\tfrac13\ln(1/\mu)+b\), \(b\to0\): numerical (conditional),
  finite-\(N\) sequences.
- \(s_1(\mu)\le(\pi/2)e^{-\mu}\) with large margin: numerical inequality at
  sampled \(\mu\); not an analytic bound proof.
- \(\sigma=0.048959 / 0.049539\), \(\sigma\approx0.049\): conditional numerical
  benchmark (quadratic truncation of \eqref{eq:Smatrix}, finite regulator,
  \(1.183\%\) route agreement bounds truncation error).
- \(\alpha_0\) fixed to the single-cut coefficient only under the tube
  identification \(w=\Theta^{1/2}=\Lambda_{\rm UV}^{-1}\): conditional
  bookkeeping; \(\alpha_1,\alpha_2\) not computed.
- Anous2020 support for region-algebra non-factorization in BFSS: established
  literature fact (record verified 2026-11-09); its application as NAMCG
  evidence is conditional on the cited claim only.
- Any massless additive constant: deliberately NOT claimed (regulator drift).

## Proposed changes

### File 1: `chapters/appH-microscopic-proofs.tex` (insert only)
Location: end of the Problem G ledger section, before the Problem H section
header. Anchors (verified in `simulate_apply_r2.out`, working tree UNCHANGED
since r1): `scope-limited model.` unique at byte offset 540076, followed by
`\r\n\r\n`; `\section{Problem H: modular origin of the interpolating function}`
unique at byte offset 540100. Insert at offset 540100 (before the header). No
existing sentence is replaced; nothing in appH is deleted. Stale passages
elsewhere: none (r1 was never integrated, so no manuscript text carries the
failing numbers). Review F8 (hard-coded "Chapter~12" in the G intro) is in the
untouched region — no action by this proposal.

Insert (file `proposals/061-g-sent-replica-obstruction-and-cut-benchmark/insert-r2.tex`,
LF, 6120 B, raw sha256 c5ca9bca2f4874f30bf436b7e3db6f95f1d98276f620d6335ac3cadf3077421d;
identical byte content also reproduced here):

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
\(\mu^2=4\sin^2(p_1/2)+4\sin^2(p_2/2)\) evaluates to \(0.048959\) (direct
quadrature on a \(64^2\) offset Brillouin-zone grid for \(\mu\ge0.05\) plus the
analytic infrared tail) and to \(0.049539\) by an independent interpolation
route, a \(1.183\) percent agreement. Since the interval carries two cuts, the
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

### File 2: `bib/namcg.bib` (append only, gatekeeper-mandated by the \cite)
Pre-state (re-verified in `simulate_apply_r2.out`): 26936 bytes, sha256
6b4612d18c2884e9ff486053f80b9769aad26c71006b1fd034d2d7eb7303b3d2, CRLF 896,
bare LF 0, ends with `}\r\n`, zero occurrences of `Anous2020`. Append the
following entry verbatim as CRLF text (414 bytes) at offset 26936:

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

Record verified against the live arXiv abs page 2026-11-09 (title, author
list, SciPost Phys. 8, 057 (2020), DOI 10.21468/SciPostPhys.8.4.057).

### APPLY RULE (single pass; supersedes the withheld r1 rule)
1. Assert appH pre-state: `chapters/appH-microscopic-proofs.tex` size 560743,
   sha256 `fe02de8970b7dee8b0df8cad9a84ca557b1ecf41bc9d2b4984135a50b8faab8d`,
   CRLF 3326, bare LF 0. Assert `scope-limited model.` occurs exactly once, at
   offset 540076, followed by bytes `\r\n\r\n`. Assert
   `\section{Problem H: modular origin of the interpolating function}` occurs
   exactly once, at offset X = 540100.
2. Read `proposals/061-g-sent-replica-obstruction-and-cut-benchmark/insert-r2.tex`
   (raw: 6120 B, sha256 `c5ca9bca2f4874f30bf436b7e3db6f95f1d98276f620d6335ac3cadf3077421d`).
   Right-strip trailing whitespace, convert every LF to CRLF, terminate with
   `\r\n\r\n`: 6210 B, CRLF 89, bare LF 0, sha256
   `7cab921f31d419d3f2803dd82e4283284d235ce318b98ca09f470c8d7570a5d9`.
3. appH := bytes[:540100] + converted-insert + bytes[540100:]. Predicted
   post-state: size 566953, sha256
   `0cef7077c2f2dea22b9cf07345542d8f76fb100d7a3fde0d17616985884834f4`,
   CRLF 3415, bare LF 0.
4. Assert bib pre-state (above) and append the File-2 entry as CRLF at offset
   26936. Predicted post-state: size 27350, sha256
   `40d6ea09915dd4b8220f30c466821118492ee5560f66930b7c5d9a2dd8b95b90`,
   CRLF 908, bare LF 0.
5. `insert-r1.tex` must NOT be integrated (its paragraph 2 carries the failing
   numbers; gatekeeper withheld its splice).

### Verified labels used by the insert
`ass:Sent-density` (ch12:139), `sec:ch6-replica` (ch06:176), `eq:replica`
(ch06:181), `eq:LUV-def` (ch03:119), `eq:NC` (ch03:106), `ass:dictionary`
(ch03:346), `sec:ch6-modular` (ch06:123), `eq:Sent-exp` (ch12:147),
`eq:Leff` (ch12:215), `eq:bdy-EE` (ch12:190), `ass:bdy-EE` (ch12:185),
`ch:hbev` (ch12:2), `eq:Smatrix` (ch03:143). `\Tr` defined in namcg-book7.tex:104.
No duplicate labels introduced (no labels are defined by the insert). New cite
key `Anous2020` unique in the current bib.

## Number traceability (every manuscript number -> shipped output)
| insert number | source line in halfline_r2.out |
|---|---|
| mu = 1e-5 | L1 header |
| 0.31022, 0.30788, 0.30065 | L3, L4, L5 |
| 1/3, two cuts c=1 | L7 |
| 0.01740, 0.00263, 0.00030, 0.00004 | L9-L12 |
| 0.1935, 0.1154 | L14, L18 |
| 0.048959 (0.048496 + 0.000464) | L21-L22 |
| 0.049539 | L24 |
| 1.183 percent | L25 |
| b_tail 0.00077 (not in text, tail integral input) | L20 |
Continuum identities C(r)=K0(mu r)/(2pi), -C''+mu^2C = -mu K1/(2 pi r),
CD=I/4 => nu=1/2 => s=0, alpha_0 = sigma/(Lambda w): continuum_check.out (i)-(iv).
No other numbers appear in insert-r2.tex except exact fractions and the
\(64^2/512^2/\mu\ge0.05/N\)-sequence parameters, which are stated in
halfline_r2.py itself.

## Verification scripts (proposal folder; run with `python -I`)
- `halfline_r2.py` + `halfline_r2.out` — authoritative free-benchmark
  computation (checks (1)-(4)); every quoted value above appears verbatim.
- `continuum_check.py` + `continuum_check.out` — continuum/identity checks
  (i)-(iv); docstring corrected for r2 (two-cut slope 1/3) and output
  regenerated this round.
- `simulate_apply_r2.py` + `simulate_apply_r2.out` — pre-state assertions,
  anchor uniqueness, splice simulation (no writes), predicted post-hashes for
  both files, bib append simulation.
- `anchor_check.out` (r1) — retained for audit only.
- `halfline_ee.py`, `halfline_ee.out`, `insert-r1.tex` (r1) — INVALID for
  citation (F1: crashed stale `.out`, massless handling not a valid
  regularization); retained for audit only.

## Decisions Taken
- Quoted slopes only through N=2048 and NO massless additive constant: at
  fixed \(\mu_{\rm reg}=10^{-5}\) the constant drifts as \(N\) approaches the
  regulator scale; quoting it would re-introduce the F1 failure class.
  Rejected: quoting \(s_1-\tfrac13\ln N\) (drift) or \(\mu_{\rm reg}\to0\)
  limits (no valid massless correlator exists).
- Kept the two-cut interval as the computed object and stated the single-cut
  coefficient symbolically ("one half of the logarithmic term") instead of
  reformulating a single-cut boundary-CFT setup (the F2 alternative): the
  Toeplitz numerics are for the interval, and the half-line single-cut object
  would need a different computation (open step noted below).
- Route B (16-point interpolation table) kept as the independent second route
  after the r1 exponential-fit route overestimated (\(\sigma=0.200794\),
  superseded); agreement quoted exactly as printed (1.183 percent).
- Exit (i) wording: adopted the gatekeeper Corrected-snippet phrase nearly
  verbatim and added only the parenthetical mirroring ch06 L129-130 ("after
  the dictionary"); rejected dropping that caveat (would repeat the F5 error).
- F4: deleted rather than re-derived the orphan numbers (they support no claim
  in the insert).
- F3: corrected authors per live arXiv record (re-fetched, not copied from the
  review without verification).
- No build_check run (building inside the repository is prohibited for this
  role); the insert was kept to constructs already present in the manuscript
  (\paragraph, \ref/\eqref/\cite, standard math).

## Milestone assessment
Routine. No milestone trigger: the bounded obstruction (already gatekeeper
PROVED in r1) plus conditional benchmark values close no critical-path step;
Problem G stays open on all four missing steps.

## Status-label recommendation
Derived current critical-path list from ch17 (items A, B, C, D1, E, F,
G-derived, N) and the ledger snapshot: unchanged. Problem G remains
OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; no label change is proposed.

## Author decision needed
None. (All r2 choices are route/notation/recording choices within my remit;
spacetime remains emergent throughout — exit (ii) explicitly retains the
dictionary rather than assuming geometry.)

## Remaining open step
To close the original target: (i) a derivation of the cut \(\leftrightarrow\)
\(\partial M\) identification (Problem A output) turning the exit-(i) cut
functional into the local density \eqref{eq:Sent-exp}; (ii) interacting sector
(\(\alpha_1,\alpha_2\)); (iii) derivation of \eqref{eq:bdy-EE}
stationarity; (iv) the dimension-1 boundary-to-bulk conversion making
\eqref{eq:Leff} non-schematic. Benchmark-side open items: a genuine single-cut
(one-boundary) computation; \(\mu_{\rm reg}\to0\) and \(N\to\infty\)
continuum-limit control; analytic proof of the \((\pi/2)e^{-\mu}\) bound.
F7 (attack-plan G.ent depends_on) stays report-only.

## Special instructions for the gatekeeper
- Re-run `halfline_r2.py` (expect `halfline_r2.out` reproduced; runtime ~
  minutes) and check that EVERY number in insert-r2.tex paragraph 2 traces to
  its output (table above); re-derive the slope bookkeeping (interval = two
  cuts => c/3, per-cut half) and \(\alpha_0=\sigma/(\Lambda w)\).
- My direct-sum sigma (0.048496) matches your `gk_sigma.py` exactly; tail uses
  my computed \(b_{\rm tail}=0.00077\) instead of your \(b\sim0.01\): check the
  tail formula \(\int_{\mu<0.05}\) in `halfline_r2.py` L108 against
  \(\tfrac13\ln(1/\mu)+b_{\rm tail}\).
- Do NOT integrate `insert-r1.tex`; the certified r1 splice is void.
- Verify insert bytes against raw sha c5ca9bca... (6120 B) before conversion;
  predicted appH post sha 0cef7077... (566953 B) and bib post sha 40d6ea09...
  (27350 B).
- Confirm the Anous2020 BibTeX author list against the arXiv 1911.11145 record.
- Must not be asserted beyond scope: closure of G; the obstruction beyond the
  replica/cover realization on A-data without the dictionary; saturation of the
  large-mass bound; any massless additive constant; the halved single-cut
  decimal (never computed).
