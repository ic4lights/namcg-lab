# Proposal 095-g-gram-moment-identification, round 2

Complete standalone round-2 record. Round-1 verdict (`review-r1.md`, 13,538 B / sha8 04fb1009):
ACCEPT WITH REQUIRED REVISIONS, FLAGS none, PROGRESS first. The two required revisions are
mechanical record repairs; the integration artifact is hash-locked and untouched. This file
re-states the full accepted claim set and derivations (it is self-contained; no need to consult
`proposal-r1.md` to evaluate or integrate), with exactly two changes vs r1:
- **R1** (finding 1): derivation step 3's closing inference and the corresponding claim-classification
  row are replaced by the gatekeeper's unitary-invariance / conditional-Haar / nonatomic-conditional
  argument; the invalid r1 support-equality clause is deleted (its failure mode stated in step 3).
- **R2** (finding 2): open avenue 2 is annotated: the r1 candidate fibre density is wrong for the
  named conditioning; the exact D=2 constant-variance conditional laws are put on record and the
  pushforward density is re-derived here (steps 2b and the verification script).
No change to the insert bytes or the byte contract.

## Result

**Negative result delivered: a proved non-bridge lemma.** Within the named constant-variance
gaussian edge-block subclass at D=2, the moment-type diagonal coordinate
\(\hat\rho_{2}=\sum_i (G_{ii}/\tau)^2\) (the second power sum of the normalized Gram diagonal,
equal to the integrated moment-map coordinate \(\rho_2 = 1+s_2/W^2\) evaluated at the diagonal
profile, up to the constant shift one) is **not** an almost-everywhere-measurable,
relabelling-equivariant — or even arbitrary — function of the Gram-spectrum coordinate
\(p=(\lambda_1,\lambda_2)/\tau\), under any constant-variance gaussian edge-block law at D=2.
The Schur–Horn fibre of the spectrum map at a fixed nondegenerate spectrum is computed exactly:
\(G_{11}\) ranges over the whole interval \([\lambda_2,\lambda_1]\) with
\(|G_{12}|^2 = G_{11}G_{22}-\lambda_1\lambda_2\), every value realized inside the subclass, and
\(\hat\rho_2\) ranges over an interval of width \((\lambda_1-\lambda_2)^2/(2\tau^2) > 0\) on each
fibre. Explicit counterexample pair with identical spectrum: \(G=\mathrm{diag}(3,1)\) vs
\(G=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\) (spectrum both \(\{3,1\}\)), with
\(\hat\rho_2 = 5/8\) vs \(1/2\). The rank-one atomic-Gram datum of the frontier is the degenerate
extreme: the spectrum is the single vertex atom for every configuration while \(\hat\rho_2\)
ranges over the full interval from \(1/2\) to \(1\). The only collapse case is the fully degenerate
spectrum \(\lambda_1=\lambda_2\), where the fibre is the single point \(G=(\tau/2)I\).

**Round-2 strengthening of the a.e. clause (R1).** The a.e. nonexistence of any recovery map is
established measure-theoretically, not by support-equality: the constant-variance complex gaussian
Gram law is invariant under \(G\mapsto UGU^{\dagger}\), so conditional on the spectrum the
eigenvectors are Haar, \(G_{11}=\lambda_2+(\lambda_1-\lambda_2)u\) with \(u\sim\mathrm{Beta}(1,1)\)
uniform on \([0,1]\) (gatekeeper numerics quoted in step 3), the conditional law of
\(\hat\rho_2\) given \(p\) is nonatomic on a positive-width interval, and therefore
\(P(\hat\rho_2=F(p))=0\) for **every** map \(F\), measurable or not (step 3; review-r1.md
finding 1). Additionally the exact fibre conditional laws are now on record: \(a=G_{11}\mid p\) is
uniform on \([\lambda_2,\lambda_1]\), and \(\hat\rho_2\mid p\) has density
\(\tau/((\lambda_1-\lambda_2)\sqrt{2\rho-1})\) on
\(\rho\in(1/2,(\lambda_1^2+\lambda_2^2)/\tau^2]\), normalizing to 1 (step 2b).

This converts the recorded "identification ... is not supplied" disclaimer (appH L3195, 091
paragraph) into a bounded, proved nonexistence for these two named coordinates within the named
subclass at D=2 — a proved constraint on the exactness route. It closes nothing.

## Target and status

- Problem G. appH ledger header (L3026-3029, verbatim as read in round 1): "Status: OPEN. Priority:
  CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and G-external
  support at most a scope-limited model; G remains OPEN and neither satisfies the matrix-derived
  criterion." Labels frozen; this package changes none and asserts no closure.
- Target (frontier chain-2 rank 1, edge `G.moments-interaction-nonconvex`, per orchestrator dispatch
  of 2026-11-19 and `reports/sme-scout-20261119-1011.md` route 2): the Gram<->moment-profile
  coordinate identification-or-counterexample lemma, constant-variance gaussian edge-block class,
  D=2 first, rank-one atomic-Gram datum as standing counterexample.
- Dependencies: built on the integrated 091 (Gram-spectrum Jacobian, rank-one boundary, constant-
  variance scoping), 092 (moment coordinates \(\rho_p=p!\,h_p(g)/W^p\), slot coordinate as normalized
  diagonal), 093 (orbit rigidity; "the moment tuple identifies orbits... selects no chamber point").
  Does not touch the 094 integrability line (DO-NOT-RE-ATTEMPT respected).
- DERIVED vs PROGRAMME-CONDITIONAL: this is a sub-lemma (negative) for the exactness route; G remains
  OPEN and PROGRAMME-CONDITIONAL.
- What round 2 changes vs round 1 (mechanical record repair per review-r1.md, nothing else):
  * R1 (finding 1, major): step 3's closing inference and the "Nonexistence of any ... established
    consequence" classification row are replaced by the unitary-invariance / conditional-Haar /
    uniform-\(G_{11}\) / nonatomic-conditional-law / any-map a.e.-failure argument; the r1 clause
    deriving a.e. failure from pointwise-on-support failure plus support equality is deleted (its
    failure mode is stated in step 3).
  * R2 (finding 2, minor): open avenue 2 is annotated - the r1 candidate fibre density is wrong for
    the named conditioning, the exact D=2 constant-variance conditional laws are recorded (step 2b,
    re-derived in `r2_checks_095.py`), and the avenue is re-scoped.
  * The integration artifact `insert-r1h.tex` is unchanged (3,480 B / sha8 b9b75e8f; asserted by
    `r2_checks_095.py`) and remains the sole integration artifact. Superseded drafts `insert-r1.tex`,
    `insert-r1f.tex`, `insert-r1g.tex` remain registered never-integrate.

## Source reading

Digest mode: `DIGEST CURRENT` was confirmed at round 1 (checked, not run); no integration occurred
since (working tree unchanged since the round-1 measurement per the round-1 record and the
unchanged live-tree sha asserted by the round-1 splice simulation at that time), so the digest state
carries over; this round re-read the proposal-folder record in full rather than re-running the
digest. Digest + targeted reads. Read IN FULL this round: `review-r1.md` (13,538 B / sha8 04fb1009),
`proposal-r1.md`, `manifest.md`. From round 1 (record carried over verbatim where unchanged): appH
L3189-3206 (089-094 G-block + closing status sentence), appH L3024-3032 (G ledger header),
`reports/sme-scout-20261119-1011.md` (full, 15,351 B as dispatched), `proposals/093-g-orbit-rigidity-
vandermonde-walls/review-r2.md`, `proposals/094-g-mfold-localization-unconditional/review-r1.md`,
`proposals/091-g-core-induced-pair-correlation/review-r2.md` via grepped windows (NOT-established
lists), `reports/graph/frontier.yaml` only via grep+cut windows (chain-2 edge name and
DO-NOT-RE-ATTEMPT). No unreadable files. Verbatim quotes are from the live file measured in round 1
(772,537 B / sha256 3f81a3a9627ce491726a108a10153c657cb4dc6c6274dc9a3a3e4dc117aa5a86 / CRLF 3,852 /
bareLF 0); the integrator re-measures PRE against these values and STOPS if it moved, per the
review's Final integration instructions.

## Research and reasoning

Setting (all items quoted from the integrated paragraphs, appH L3191/3195/3197/3199):
the constant-variance gaussian edge-block subclass (091): \(A\) an \(M\times(N-M)\) edge block with
iid complex gaussian entries, Gram \(G=AA^{\dagger}\), \(D=\min(M,N-M)\), Gram-spectrum coordinate
\(p_i=\lambda_i/\operatorname{Tr}G\). Moment coordinates (092): \(\rho_p=p!\,h_p(g)/W^p=2^{p-1}m_{2p}/m_2^p\);
at \(p=2\), \(\rho_2 = 1+s_2(g)/W^2\) (verified symbolically, script S4). The canonical profile-space
coordinate built from a configuration (089, L3191) is the normalized diagonal of the slot Gram,
\(d_i=G_{ii}/\tau\); 092 records that within the rank-one class "the only nondegenerate Gram-type
coordinate on configurations is this diagonal one", and 091 records that the identification of the
Gram-spectrum coordinate with "the profile coordinate of the moment map is not supplied by the
repository" (L3195, verbatim).

**Derivation (self-contained at D=2; scripts `gram_moment_nonbridge_095.py` sections S1-S5 for the
fibre calculus, `r2_checks_095.py` for the round-2 density identities).**

1. *Fibre computation (established derivation).* Fix a Hermitian \(2\times2\) \(G\succeq0\) with
   spectrum \(\lambda_1\ge\lambda_2\ge0\) and \(\tau=\lambda_1+\lambda_2\). Writing \(a=G_{11}\),
   \(G_{22}=\tau-a\) and \(|G_{12}|^2 = G_{11}G_{22}-\det G = a(\tau-a)-\lambda_1\lambda_2
   = -\,(a-\lambda_1)(a-\lambda_2)\) (S1 exact identity `S1.psd_iff_interval`). A \(2\times2\)
   Hermitian matrix is PSD iff diagonal entries are nonnegative and the determinant is
   nonnegative; with \(\det G=\lambda_1\lambda_2\ge0\) fixed and trace fixed, PSD on the fibre is
   equivalent to \((a-\lambda_1)(a-\lambda_2)\le0\), i.e. \(a\in[\lambda_2,\lambda_1]\) (for
   \(\lambda_2\ge0\) the endpoint nonnegativity is automatic). Conversely every
   \(a\in(\lambda_2,\lambda_1)\) with any phase of \(G_{12}\) gives \(G\succ0\) with the fixed
   spectrum (trace and determinant fix the characteristic polynomial of a \(2\times2\) matrix;
   anchored numerically at \(\{l_1,l_2,a,\varphi\}=\{3,1,5/2,\pi/7\}\), S1
   `S1.numeric_fibre_spectrum_3_1`). Every fibre point is realized inside the edge-block subclass:
   any \(G\succeq0\) of rank \(\le \min(M,N-M)\) factors as \(AA^{\dagger}\) (Cholesky for
   \(G\succ0\); a rank-one factor for \(\lambda_2=0\)), and the gaussian law of \(A\) has full
   support on such \(A\).
2. *Statistic range on the fibre (established derivation).* \(\hat\rho_2 := \sum_i (G_{ii}/\tau)^2
   = (a^2+(\tau-a)^2)/\tau^2\) is strictly monotone in \(a\) on each half-interval (S2
   `S2.monotone_below_mid`), minimum \(1/2\) at \(a=\tau/2\) (always inside the fibre), maximum
   \((\lambda_1^2+\lambda_2^2)/\tau^2\) at the endpoints \(a\in\{\lambda_1,\lambda_2\}\), width
   exactly \((\lambda_1-\lambda_2)^2/(2\tau^2)\) (S2 `S2.width_formula`). At the fully degenerate
   spectrum \(\lambda_1=\lambda_2=\tau/2\) the interval \([\lambda_2,\lambda_1]\) collapses to
   \(a=\tau/2\): the fibre is the single matrix \((\tau/2)I\) (S2 `S2.degenerate_fibre_point`),
   and \(\hat\rho_2\equiv 1/2\) there.
2b. *Exact fibre conditional laws under the gaussian law (established derivation; new in r2, R2).*
   Under the constant-variance law on \(A\), the Gram matrix \(G\) has a unitarily invariant
   (complex Wishart) density \(\propto(\det G)^{n-2}e^{-\operatorname{Tr}G/\sigma^{2}}\)
   (\(n=\max(M,N-M)\ge2\)) depending only on the eigenvalues, so conditional on the spectrum the
   unitary in \(G=U\,\mathrm{diag}(\lambda_1,\lambda_2)U^{\dagger}\) is Haar and independent of the
   spectrum. Hence \(G_{11}=\lambda_1 q+\lambda_2(1-q)\) with \(q=|U_{11}|^{2}\sim\mathrm{Beta}(1,1)\)
   uniform on \([0,1]\): \(a=G_{11}\mid p\) is uniform on \([\lambda_2,\lambda_1]\). Pushforward
   through the two-to-one quadratic \(\rho(a)=(a^2+(\tau-a)^2)/\tau^2\): with
   \(t=\sqrt{2\rho-1}\in[0,(\lambda_1-\lambda_2)/\tau]\) the two inverse branches are
   \(a=(\tau\pm\tau t)/2\) with \(d\rho/da=\pm 2t/\tau\), so
   \(f_\rho(\rho)=\sum_\pm f_a(a_\pm)/\lvert d\rho/da\rvert_\pm
   =2\cdot\frac{1}{\lambda_1-\lambda_2}\cdot\frac{\tau}{2\sqrt{2\rho-1}}
   =\frac{\tau}{(\lambda_1-\lambda_2)\sqrt{2\rho-1}}\) on
   \(\rho\in(1/2,(\lambda_1^2+\lambda_2^2)/\tau^2]\); it normalizes to \(1\) because
   \(\sqrt{2\rho_{\max}-1}=(\lambda_1-\lambda_2)/\tau\). Verified symbolically
   (`r2_checks_095.py`: branch identity, slope identity, CDF match, normalization \(\equiv 1\), and
   mean-form agreement all simplify to \(0\)) and numerically (quadrature to \(1\pm10^{-6}\);
   seeded MC of the uniformity of \(a\) against variance \((\lambda_1-\lambda_2)^2/12\)). The r1
   candidate fibre density \(\propto\sqrt{a(\tau-a)-\lambda_1\lambda_2}\,\lvert\tau-2a\rvert/2\) is
   wrong for the named conditioning: it vanishes at \(a=\tau/2\) (gatekeeper values at
   \(\{3,1\},\tau=4\): \(0.480,0.000,0.392\) for \(a=1.2,2.0,2.9\), review-r1.md finding 2) where
   the true conditional density is uniform and maximal.

3. *Identification fails pointwise on the support, and almost everywhere under every named law
   (established; a.e. argument repaired in r2 per review-r1.md finding 1).* For every nondegenerate
   spectrum value the fibre carries distinct \(\hat\rho_2\) values (S2, S3), so no map
   \(F:\Delta\to\mathbb{R}\) of any kind satisfies \(\hat\rho_2 = F\circ p\) pointwise on the
   support. Explicit exact pair (S3): \(\mathrm{diag}(3,1)\) and
   \(\begin{psmallmatrix}2&1\1&2\end{psmallmatrix}\), both spectrum \(\{3,1\}\), \(\hat\rho_2=5/8\)
   vs \(1/2\). Rank-one datum (S3, S2 `S2.rankone_range`): configurations \(w=(1,0)\) vs
   \(w=(1/\sqrt2,1/\sqrt2)\) (edge-block realizations \(\mathrm{diag}(1,0)\) vs
   \(\tfrac12\begin{psmallmatrix}1&1\1&1\end{psmallmatrix}\)) share the vertex-atom spectrum;
   \(\hat\rho_2\in\{1,\,1/2\}\) - the frontier's standing counterexample, now proved rather than
   posed.
   *a.e. upgrade (repaired argument, replacing the r1 inference).* Pointwise failure on the support
   alone does **not** imply a.e. failure for a full-support law: a law concentrated on the graph of
   a measurable section of the spectrum map (with interval-full-support marginals) satisfies
   \(\hat\rho_2 = F\circ p\) everywhere for \(F := \hat\rho_2\circ\mathrm{section}\) - this is the
   counterexample logic that invalidated the r1 route (review-r1.md finding 1). The valid argument
   is measure-theoretic: the constant-variance complex gaussian edge-block Gram law is invariant
   under \(G\mapsto UGU^{\dagger}\) (left-unitary mixing of the rows of \(A\) preserves iid
   \(\mathrm{CN}(0,\sigma^2)\) entries), so conditional on the spectrum the eigenvectors are Haar
   (step 2b), \(G_{11}=\lambda_2+(\lambda_1-\lambda_2)u\) with \(u\) uniform on \([0,1]\), i.e.
   \(\mathrm{Beta}(1,1)\), and the conditional law of \(\hat\rho_2\) given \(p\) is nonatomic on the
   positive-width interval \([1/2,(\lambda_1^2+\lambda_2^2)/\tau^2]\) (the degenerate spectrum is a
   null set under the named law). Since \(F(p)\) is \(p\)-measurable as a value, conditioning gives
   \(P(\hat\rho_2=F(p))=\mathbb{E}\bigl[P(\hat\rho_2=F(p)\mid p)\bigr]=0\) for **every** map \(F\),
   measurable or not (for non-measurable \(F\) read the probability as outer probability; the
   conditional-measure integral is unchanged). Gatekeeper Monte Carlo confirms the conditional
   uniformity of the normalized \(G_{11}\) on the fibre under the named law directly (attributed to
   review-r1.md, Checks performed: bands \(p_1\approx0.75\): mean \(-0.006\), variance \(0.0838\);
   bands \(p_1\approx0.65\): mean \(-0.004\), variance \(0.0823\); both against \(1/12\approx
   0.0833\); \(\max\lvert\cdot\rvert\approx0.4998\) - the Haar \(\mathrm{Beta}(1,1)\) prediction).
4. *Link to the moment coordinate (conditional on the integrated 092 convention).*
   \(\hat\rho_2 = \rho_2(d_1,d_2) - 1\) with \(\rho_2=1+s_2/W^2\) of the 092 paragraph evaluated at
   the normalized diagonal profile (S4: identity, wall value \(3/2\), single-slot value \(2\),
   diagonal realization all verified symbolically). Since the relation is the constant shift one,
   non-recovery of \(\hat\rho_2\) from \(p\) is equivalent to non-recovery of the diagonal-realized
   moment coordinate. In the rank-one class this statistic is the second power sum of the slot
   coordinate of 089/091 (whose spectrum is "a single atom at the vertex", L3197 verbatim), which is
   why the rank-one fibre degeneracy saturates the failure.
5. *Measure-level complement (conditional-numerical).* Under the constant-variance complex gaussian
   law on \(A\) (seed 20261119, 200k samples, band \(0.79<\lambda_{\max}/\tau<0.81\) around the
   spectrum ratio 4:1), \(\hat\rho_2\) spreads over \([0.500, 0.692]\) against the exact fibre range
   \([1/2, 17/25]=[0.5,0.68]\) at \(p=(4,1)/5\) (S5; band sampling near the boundary explains the
   slight overshoot). Combined with step 2b the conditional law of the moment-type statistic given
   the Gram profile is now exactly known (density of step 2b), not merely non-degenerate.
6. *Positive complement, stated exactly.* Identification holds only after an extra selection: on
   the diagonal-Gram gauge (diagonal \(G\), i.e. \(G_{12}=0\)) spectrum and diagonal agree as
   multisets and the bridge is tautological; this is a gauge choice, matching 093's "the moment
   tuple identifies orbits... selects no chamber point". No selection is supplied by the core within
   the named class.

Literature: `reports/sme-scout-20261119-1011.md` route 2/Task 2 verdict - no published
Gram<->moment bridge exists (its literature verdict itself is the SME agent's; its four arXiv
records were verified by it, marked there). No citation is needed for the present lemma: it is a
self-contained 2x2 linear-algebra and Haar-Beta statement. The general-D extension would follow
from the classical Schur-Horn theorem (diagonals with fixed spectrum = the permutahedron; Schur
1923, Horn 1954 - **not independently verified this pass**, no record fetched; nothing in the
insert or this package relies on it, since the insert is D=2 only and the D=2 proof above is
self-contained). Muirhead/Forrester Wishart attributions in the scout report: not independently
verified; the conditional-Haar property used in step 2b is derived above from unitary invariance of
the Wishart density rather than cited.

Comparison with original target: the target asked for identification-or-counterexample. Delivered:
counterexample lemma (non-bridge), with explicit hypotheses and exact fibre calculus. The three
"not supplied" records (L3195 identification "not supplied by the repository"; L3197 "carried by the
averaged charge-moment sequence rather than supplied to it"; 092 rank-one diagonal-only sentence) are
now supported by a proof inside the same named class. They are NOT edited: they remain true as
statements about the repository record at their integration time; the new paragraph records the proved
nonexistence. No other file needs to change.

## Claim classification

- Fibre interval, PSD equivalence, range/width formulas, degenerate-point collapse, explicit pairs:
  **established derivation** (self-contained at D=2; scripts S1-S3, re-derivable in the proposal text).
- \(\hat\rho_2\) = shifted \(\rho_2\) at diagonal argument: **established identity**, conditional on
  the integrated 092 convention (\(\rho_p=p!h_p(g)/W^p\), leading-order convention of the tenth
  preceding paragraph as integrated).
- Realizability of fibre points by edge-block configurations: **established** (factorization + full
  support of the named gaussian law - the full-support property is that of the integrated named law).
- Nonexistence of any (measurable/equivariant/arbitrary) recovery map at D=2 under the named
  constant-variance gaussian edge-block laws: **established derivation** - unitary invariance ⟹
  conditional Haar ⟹ uniform \(G_{11}\) ⟹ nonatomic conditional law of \(\hat\rho_2\mid p\) ⟹
  zero-probability coincidence with any \(p\)-measurable value, for every \(F\) (step 3; repaired
  route per review-r1.md finding 1). The pointwise-on-support failure in step 3's first paragraph
  stands on its own, but pointwise failure plus full support alone would NOT establish the a.e.
  claim: a full-support law can concentrate on the graph of a measurable section, on which an exact
  pointwise bridge exists (this is why the r1 row was repaired rather than kept).
- Exact fibre conditional laws (step 2b: \(a\mid p\) uniform on \([\lambda_2,\lambda_1]\);
  \(\hat\rho_2\mid p\) density \(\tau/((\lambda_1-\lambda_2)\sqrt{2\rho-1})\)): **established
  derivation** (change-of-variables computation; verified symbolically and numerically by
  `r2_checks_095.py`), conditional on the integrated named constant-variance gaussian law. The
  Wishart exponent \((\det G)^{n-2}\) states the square/nonsquare case for \(A\) of size
  \(M\times(N-M)\) with \(D=\min(M,N-M)=2\), \(n=\max(M,N-M)\ge2\); the derivation uses only the
  unitary invariance and not the exponent.
- Fibre nondegeneracy under the gaussian measure (S5): **conditional-numerical** check (seeded MC;
  not a proof; consistent with the exact support-level and step 2b results).
- D>=3 extension via Schur-Horn: **not proved here**; classical-theorem route flagged, sources not
  independently verified.
- "No published bridge" premise: from the SME scout report (its own arXiv verifications listed
  there); taken as a lead, not imported as a result.

## Proposed changes

Byte-identical with round 1. Files touched: `chapters/appH-microscopic-proofs.tex` only; one pure
insertion. The artifact is the bytes of `insert-r1h.tex` (3,480 B / sha8 b9b75e8f; hash-locked by
the gatekeeper and unchanged in r2 - asserted by `r2_checks_095.py`); the fenced copy in
`proposal-r1.md` is review text only. **Do not retype or re-emit the insert; integrate from the file
bytes only.**

- Anchor: the line-initial `\emph{Vacuum term.}` (live L3203) immediately after the 094 paragraph
  (L3201, which ends "... they leave the missing steps (i)-(iv) of the Missing step paragraph
  unchanged, and they close nothing in Problem~G."). Compound PIN = 094 tail (last 96 bytes of
  L3201) + `CRLFCRLF` + line-initial `\emph{Vacuum term.}` - count exactly 1 (asserted; cut byte
  735,720).
- Splice rule: `appH[:cut] + insert_bytes + ONE CRLF + appH[cut:]`, cut = 735,720 (byte index of the
  line-initial `\emph{Vacuum term.}`; the preceding blank line L3202 is preserved, so the insert
  becomes a new standalone paragraph). Everything stays; no existing equation, sentence or label is
  modified.
- Expected POST (printed by `simulate_apply_095.py`): size 776,019 = 772,537 + 3,480 + 2; sha256
  600588c1d1087232ace2cea1cdecf13fb38885cf7a2126a72eedfdc1234bfa0d; CRLF 3,854; bareLF 0;
  close-idiom noun count 20→21; verb idiom count 1; `\emph{Vacuum term.}` 2; header count of the
  new paragraph 1. (Independently reproduced by the gatekeeper in r1, review-r1.md "Checks
  performed".)
- No new labels, refs, or bib entries; nothing else in the repository references this paragraph.
- Stale passages elsewhere: none created. The 091 "not supplied by the repository" sentence and the
  092 coordinate sentences stay as-is (see Research and reasoning, last paragraph).
- Gatekeeper r1 finding 3 (wording, "no change required") carries unchanged: "the spectrum map
  forgets the diagonal completely" stays as written (determinacy sense, controlled by the exact
  surrounding sentences; byte contract hash-locked).

## Verification scripts

All under this folder; run from repo root with `python -I`; deterministic (fixed sympy expressions;
numpy seed 20261119). `.out` files are the captured outputs. The three round-1 scripts and their
outputs are unchanged and remain part of the reproduction pack.

- `gram_moment_nonbridge_095.py` → `gram_moment_nonbridge_095.out` — S1 fibre/PSD equivalence and
  numeric charpoly anchor; S2 range/width/monotonicity/collapse/rank-one endpoints; S3 exact
  counterexamples (5/8 vs 1/2; rank-one 1 vs 1/2); S4 moment-convention identities; S5 seeded
  gaussian MC fibre spread. **Expected:** all 21 `chk` lines `PASS`; `S5.band_count 8735`;
  `S5.rho_min_max` min within 1e-7 of 0.5, max in (0.68, 0.70); final line `SUMMARY ALL PASS`.
- `simulate_apply_095.py` → `simulate_apply_095.out` — read-only splice simulation; re-measures and
  asserts live PRE (772,537 / sha256 3f81a3a9...5a86 / CRLF 3,852 / bareLF 0), PIN count 1, cut byte
  line-initiality; prints full POST sha256/CRLF/bareLF/idiom/Vacuum counts and prefix/suffix
  identity. **Expected:** `PRE_SIZE 772537`, `POST_SIZE 776019`, `POST_SHA256 600588c1...fa0d`,
  `POST_CRLF 3854`, `POST_bareLF 0`, `IDIOM_pre_post 20 21`, `VACUUM_POST 2`, `CUT_BYTE 735720`,
  `SUMMARY ALL PASS`. No writes performed.
- `hygiene_095.py` → `hygiene_095.out` — insert hygiene (ASCII, control bytes, one line + terminal
  CRLF, delimiter balance, banned status/closure vocabulary, idiom at end, header uniqueness across
  `chapters/*.tex`, POST idiom counts). **Expected:** `INSERT_SIZE 3480 INSERT_SHA8 b9b75e8f`,
  `HEADER_HITS_IN_CHAPTERS []`, `SUMMARY ALL PASS`.
- **New in r2:** `r2_checks_095.py` → `r2_checks_095.out` — (a) sha256/size assertions that
  `insert-r1h.tex` is unchanged (3,480 B / sha8 b9b75e8f) and that `review-r1.md` matches its
  registered identity (13,538 B / sha8 04fb1009); (b) re-derivation of the corrected conditional
  density: the `rho2hat|p` density tau/((lambda1-lambda2)*sqrt(2r-1)) as the pushforward of the
  `a|p` uniform law on [lambda2, lambda1] - branch-inverse identity, branch-slope identity,
  two-branch Jacobian sum identical to the target density (sympy simplify == 0), symbolic
  normalization == 1 (simplify == 0), CDF match (simplify == 0), equality of the two mean forms
  (simplify == 0), uniform-fibre variance == (lambda1-lambda2)^2/12, and the r1 candidate density
  vanishing at a=tau/2; plus quadrature within 1e-6 of 1 and a seeded MC uniformity check.
  (c) record-change assertions on `proposal-r2.md`: the deleted r1 support-equality phrase (the clause whose deletion R1
  requires, as quoted in review-r1.md finding 1) occurs 0 times; the repaired-argument markers
  ("unitary invariance", "Haar", "Beta(1,1)", "nonatomic", "graph of a measurable section") and the
  R2 markers ("tau/((lambda1-lambda2)*sqrt(2r-1))", "uniform on [lambda2, lambda1]", "essentially
  settled at D=2", "heterogeneous variances") are present.
  **Expected:** all `chk` lines `PASS`; final line `R2 CHECKS 095: PASS`.

Reproduction pack (order, all from repo root, all `python -I`): (1)
`proposals/095-g-gram-moment-identification/gram_moment_nonbridge_095.py`; (2)
`proposals/095-g-gram-moment-identification/simulate_apply_095.py`; (3)
`proposals/095-g-gram-moment-identification/hygiene_095.py` - all three must end `SUMMARY ALL PASS`;
(4) `proposals/095-g-gram-moment-identification/r2_checks_095.py` - must end `R2 CHECKS 095: PASS`.

## Decisions Taken

Carried unchanged from round 1 (1: negative non-bridge route over positive route; 2: the
diagonal-realized moment coordinate as the only honest configuration-level carrier in the named
class, rejecting an assumed-target configuration-level moment and a category-mixing law-level
phrasing; 3: scope D=2 only, general-D left unproved rather than cited blind; 4: do not edit the
three "not supplied" sentences; 5: rank-one clause phrasing fixed by byte surgery).

**Round-2 decisions taken.** No scope, label, route, or completion decisions were needed beyond
adopting the gatekeeper repair. R1: adopted the unitary-invariance / conditional-Haar /
uniform-G11 / nonatomic-conditional argument of review-r1.md finding 1, adopting its numeric
confirmations (band means/variances vs 1/12) with attribution to review-r1.md; deleted the invalid
clause instead of weakening the insert's claim (the claim as written is true, so the hash-locked
insert stays as-is). Rejected alternatives: (i) narrowing the r1 inference by re-quantifying the
law class - the r1 clause was an invalid inference, not a scope choice; (ii) any edit of the insert
bytes - hash-locked and unnecessary. R2: recorded the exact D=2 densities with a fresh
change-of-variables re-derivation (step 2b) rather than only citing the review, so every identity
is verified inside the package, not imported.

## Milestone assessment

Routine. A bounded proved sub-lemma/negative constraint on the exactness route (chain 2, edge
G.moments-interaction-nonconvex); round 2 is a mechanical record repair; no milestone trigger
applies; no critical-path step is closed.

## Status-label recommendation

Re-derived from agenda/ledger as quoted above: critical path at full-GR scope = A, B, C, D1, E, F,
G-derived, N (G itself OPEN/CRITICAL PATH/PROGRAMME-CONDITIONAL). **All labels unchanged** by this
package.

## Author decision needed

None.

## Remaining open step

For Problem G's exactness route the state-side demand of the Missing step paragraph (missing steps
(i)-(iv)) is unchanged; this package bounds what coordinate bridges cannot do. Open avenues,
re-ranked after the r1 negative result (review-r1.md ranking adopted):
1. D>=3 extension of the non-bridge lemma: a self-contained Schur-Horn/permutahedron proof for the
   full rho-tuple - the rank-one datum already realizes the obstruction at every D>=2.
2. (Re-scoped in r2 per R2) Quantitative profile-information gap: mutual information between p and
   the diagonal d under the named law. The "exact conditional law" content that r1 listed as a
   separate avenue is now essentially settled at D=2 by step 2b (review-r1.md finding 4 concurs):
   the exact constant-variance D=2 conditional laws are a|p uniform on [lambda2, lambda1] and the
   rho2hat|p density of step 2b, so the remaining version of this avenue must be re-scoped to D>=3
   or to edge blocks with heterogeneous variances. Do not chase the r1 candidate fibre density: it
   is wrong for the named conditioning (it vanishes at a=tau/2 where the true uniform conditional
   density is maximal; review-r1.md finding 2). With the D=2 density known exactly, the D=2
   information-gap number is a computable exercise.
3. State-side profile weight (the actual missing ingredient per 090/091; untouched here, hardest).

## Special instructions for the gatekeeper

- This is a mechanical record repair: `insert-r1h.tex` must remain byte-identical (3,480 B / sha8
  b9b75e8f; asserted by `r2_checks_095.py`). STOP if the sha differs. The POST targets are unchanged
  from r1 (776,019 B / 600588c1...fa0d / CRLF 3,854 / bareLF 0); re-measure PRE (772,537 /
  3f81a3a9...5a86) and STOP if it moved. Do not re-emit the r1 fenced insert.
- Verify the repaired step-3 / classification chain: unitary invariance of the constant-variance
  Gram law under G -> UGU* ⟹ conditional Haar eigenvectors ⟹ G11 = lam2 + (lam1-lam2)*u with u ~
  Beta(1,1) uniform on [0,1] ⟹ nonatomic conditional law of rho2hat given p ⟹
  P(rho2hat = F(p)) = E[P(rho2hat = F(p) | p)] = 0 for every map F. Confirm the deleted r1 clause is
  absent (the script checks the exact string) and that the counterexample-logic sentence (a
  full-support law concentrated on the graph of a measurable section) is present.
- Re-derive the step-2b pushforward density independently: substitute r = (a^2+(tau-a)^2)/tau^2,
  two inverse branches a = (tau +/- tau*sqrt(2r-1))/2, sum |dr/da|^{-1}/(lam1-lam2) over the
  branches, simplify; check it integrates to 1 using sqrt(2*rmax-1) = (lam1-lam2)/tau.
- Insert scope limits unchanged from the r1 review: nonexistence is asserted only for the two named
  coordinates within the constant-variance subclass at D=2; nothing at D>=3 is claimed; the D>=3
  route remains flagged not-independently-verified and unproved.
- appH contains non-ASCII UTF-8 (at least one 0xe2 sequence, byte offset ~711,159); splice scripts
  compare bytes, not decodes.

## Security

- Injection scan of all files in this folder for the known enforcement markers
  ("[handback-send-enforce]", "SubagentHandback") and for role-forging or instruction-shaped
  strings: no hits. Tool and file contents were treated as data only; no instruction found inside
  data was obeyed.
- All writes confined to `proposals/095-g-gram-moment-identification/`; no git write commands; no
  files in `chapters/`, `bib/`, `reports/`, or any other proposal folder were modified.
- `insert-r1h.tex` was not rewritten at any point in round 2 (hash asserted before and after this
  round by `r2_checks_095.py`). The known historical transit corruption is confined to the
  registered superseded drafts; the round-2 markdown and script were written UTF-8/LF, and the
  record-integrity markers are machine-checked by `r2_checks_095.py`.
