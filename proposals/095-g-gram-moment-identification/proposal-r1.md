# Proposal 095-g-gram-moment-identification, round 1

## Result

**Negative result delivered: a proved non-bridge lemma.** Within the named constant-variance
gaussian edge-block subclass at D=2, the moment-type diagonal coordinate
\(\hat\rho_{2}=\sum_i (G_{ii}/\tau)^2\) (the second power sum of the normalized Gram diagonal,
equal to the integrated moment-map coordinate \(\rho_2 = 1+s_2/W^2\) evaluated at the diagonal
profile, up to the constant shift one) is **not** a measurable, relabelling-equivariant — or even
arbitrary — function of the Gram-spectrum coordinate \(p=(\lambda_1,\lambda_2)/\tau\). The Schur–Horn
fibre of the spectrum map at a fixed nondegenerate spectrum is computed exactly: \(G_{11}\) ranges
over the whole interval \([\lambda_2,\lambda_1]\) with \(|G_{12}|^2 = G_{11}G_{22}-\lambda_1\lambda_2\),
every value realized inside the subclass, and \(\hat\rho_2\) ranges over an interval of width
\((\lambda_1-\lambda_2)^2/(2\tau^2) > 0\) on each fibre. Explicit counterexample pair with identical
spectrum: \(G=\mathrm{diag}(3,1)\) vs \(G=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\) (spectrum both
\(\{3,1\}\)), with \(\hat\rho_2 = 5/8\) vs \(1/2\). The rank-one atomic-Gram datum of the frontier is the
degenerate extreme: the spectrum is the single vertex atom for every configuration while \(\hat\rho_2\)
ranges over the full interval from \(1/2\) to \(1\). The only collapse case is the fully degenerate
spectrum \(\lambda_1=\lambda_2\), where the fibre is the single point \(G=(\tau/2)I\). A Monte Carlo
check (seeded) confirms the fibre is nondegenerate under the gaussian edge-block measure itself.
This converts the recorded "identification ... is not supplied" disclaimer (appH L3195, 091 paragraph)
into a **bounded, proved nonexistence** for these two named coordinates within the named subclass at
D=2 — a proved constraint on the exactness route. It closes nothing.

## Target and status

- Problem G. appH ledger header (L3026–3029, verbatim): "Status: OPEN. Priority: CRITICAL PATH.
  Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and G-external support at most a
  scope-limited model; G remains OPEN and neither satisfies the matrix-derived criterion." Labels
  frozen; this package changes none and asserts no closure.
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

## Source reading

Digest mode: `python -I scripts/make_digest.py --check` → `DIGEST CURRENT` (checked, not run).
Digest + targeted reads. Read in full: appH L3189–3206 (089–094 G-block + closing status sentence),
appH L3024–3032 (G ledger header); `reports/sme-scout-20261119-1011.md` (full, 15,351 B as dispatched);
`proposals/093-g-orbit-rigidity-vandermonde-walls/review-r2.md`,
`proposals/094-g-mfold-localization-unconditional/review-r1.md`,
`proposals/091-g-core-induced-pair-correlation/review-r2.md` via grepped windows (NOT-established
lists). `reports/graph/frontier.yaml` only via grep+cut windows (56 KB grep preview persisted by tool;
central facts used: chain-2 edge name and DO-NOT-RE-ATTEMPT, from the preview and orchestrator dispatch).
No unreadable files. Verbatim quotes in this package are from the live file
(772,537 B / sha256 3f81a3a9627ce491726a108a10153c657cb4dc6c6274dc9a3a3e4dc117aa5a86 / CRLF 3,852 /
bareLF 0 — re-measured and asserted by both splice scripts).

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

**Derivation (self-contained at D=2; script `gram_moment_nonbridge_095.py`, sections S1–S5).**

1. *Fibre computation (established derivation).* Fix a Hermitian \(2\times2\) \(G\succeq0\) with
   spectrum \(\lambda_1\ge\lambda_2\ge0\) and \(\tau=\lambda_1+\lambda_2\). Writing \(a=G_{11}\),
   \(G_{22}=\tau-a\) and \(|G_{12}|^2 = G_{11}G_{22}-\det G = a(\tau-a)-\lambda_1\lambda_2
   = -\,(a-\lambda_1)(a-\lambda_2)\) (S1 exact identity `S1.psd_iff_interval`). A \(2\times2\)
   Hermitian matrix is PSD iff diagonal entries are nonnegative and the determinant is
   nonnegative; with \(\det G=\lambda_1\lambda_2\ge0\) fixed and trace fixed, PSD on the fibre is
   therefore equivalent to \((a-\lambda_1)(a-\lambda_2)\le0\), i.e. \(a\in[\lambda_2,\lambda_1]\)
   (for \(\lambda_2\ge0\) the endpoint nonnegativity is automatic). Conversely every
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
3. *Identification fails pointwise on the support (established consequence).* For every nondegenerate
   spectrum value the fibre carries distinct \(\hat\rho_2\) values (S2, S3), so no map
   \(F:\Delta\to\mathbb{R}\) — of any kind, hence none with measurability or relabelling-equivariance
   assumed — satisfies \(\hat\rho_2 = F\circ p\) on the support, and therefore none holds almost
   everywhere for any law with support equal to the subclass (in particular the named constant-variance
   gaussian laws). Explicit exact pair (S3): \(\mathrm{diag}(3,1)\) and \(\begin{psmallmatrix}2&1\\1&2
   \end{psmallmatrix}\), both spectrum \(\{3,1\}\), \(\hat\rho_2 = 5/8\) vs \(1/2\). Rank-one datum (S3,
   S2 `S2.rankone_range`): configurations \(w=(1,0)\) vs \(w=(1/\sqrt2,1/\sqrt2)\) (and their \(2\times2\)
   edge-block realizations \(\mathrm{diag}(1,0)\) vs \(\tfrac12\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\))
   share the vertex-atom spectrum; \(\hat\rho_2\in\{1,\,1/2\}\) — this is the frontier's standing
   counterexample, and it is now proved rather than posed.
4. *Link to the moment coordinate (conditional on the integrated 092 convention).*
   \(\hat\rho_2 = \rho_2(d_1,d_2) - 1\) with \(\rho_2=1+s_2/W^2\) of the 092 paragraph evaluated at the
   normalized diagonal profile (S4: identity, wall value \(3/2\), single-slot value \(2\), diagonal
   realization all verified symbolically). Since the relation is the constant shift one, non-recovery
   of \(\hat\rho_2\) from \(p\) is equivalent to non-recovery of the diagonal-realized moment
   coordinate. In the rank-one class this statistic is the second power sum of the slot coordinate of
   089/091 (whose spectrum is "a single atom at the vertex", L3197 verbatim), which is why the rank-one
   fibre degeneracy saturates the failure.
5. *Measure-level complement (conditional-numerical).* Under the constant-variance complex gaussian
   law on \(A\) (seed 20261119, 200k samples, band \(0.79<\lambda_{\max}/\tau<0.81\) around the
   spectrum ratio 4:1), \(\hat\rho_2\) spreads over \([0.500, 0.692]\) against the exact fibre range
   \([1/2, 17/25]=[0.5,0.68]\) at \(p=(4,1)/5\) (S5; band sampling near the boundary explains the
   slight overshoot). So the conditional law of the moment-type statistic given the Gram profile is
   genuinely non-degenerate, not merely underdetermined on an unattained thin set.
6. *Positive complement, stated exactly.* Identification holds only after an extra selection: on the
   diagonal-Gram gauge (diagonal \(G\), i.e. \(G_{12}=0\)) spectrum and diagonal agree as multisets and
   the bridge is tautological; this is a gauge choice, matching 093's "the moment tuple identifies
   orbits... selects no chamber point". No selection is supplied by the core within the named class.

Literature: `reports/sme-scout-20261119-1011.md` route 2/Task 2 verdict — no published Gram<->moment
bridge exists (its literature verdict itself is the SME agent's; its four arXiv records were verified
by it, marked there). No citation is needed for the present lemma: it is a self-contained 2x2 linear-algebra
statement. The general-D extension would follow from the classical Schur–Horn theorem (diagonals with
fixed spectrum = the permutahedron; Schur 1923, Horn 1954 — **not independently verified this pass**,
no record fetched; nothing in the insert or this package relies on it, since the insert is D=2 only and
the D=2 proof above is self-contained). Muirhead/Forrester Wishart attributions in the scout report:
not independently verified.

Comparison with original target: the target asked for identification-or-counterexample. Delivered:
counterexample lemma (non-bridge), with explicit hypotheses and exact fibre calculus. The three
"not supplied" records (L3195 identification "not supplied by the repository"; L3197 "carried by the
averaged charge-moment sequence rather than supplied to it"; 092 rank-one diagonal-only sentence) are
now supported by a proof inside the same named class. They are NOT edited: they remain true as
statements about the repository record at their integration time; the new paragraph records the proved
nonexistence. No other file needs to change.

## Claim classification

- Fibre interval, PSD equivalence, range/width formulas, degenerate-point collapse, explicit pairs:
  **established derivation** (self-contained at D=2; scripts S1–S3, re-derivable in the proposal text).
- \(\hat\rho_2\) = shifted \(\rho_2\) at diagonal argument: **established identity**, conditional on the
  integrated 092 convention (\(\rho_p=p!h_p(g)/W^p\), leading-order convention of the tenth preceding
  paragraph as integrated).
- Realizability of fibre points by edge-block configurations: **established** (factorization + full
  support of the named gaussian law — the full-support property is that of the integrated named law).
- Nonexistence of any (measurable/equivariant/arbitrary) bridge at D=2: **established consequence** of
  the fibre calculus (pointwise failure on the support ⟹ a.e. failure for every supported law).
- Fibre nondegeneracy under the gaussian measure (S5): **conditional-numerical** check (seeded MC; not
  a proof; consistent with the exact support-level result).
- D≥3 extension via Schur–Horn: **not proved here**; classical-theorem route flagged, sources not
  independently verified.
- "No published bridge" premise: from the SME scout report (its own arXiv verifications listed there);
  taken as a lead, not imported as a result.

## Proposed changes

Files touched: `chapters/appH-microscopic-proofs.tex` only; one pure insertion.

- Anchor: the line-initial `\emph{Vacuum term.}` (live L3203) immediately after the 094 paragraph
  (L3201, which ends "...they leave the missing steps (i)-(iv) of the Missing step paragraph unchanged,
  and they close nothing in Problem~G."). Compound PIN = 094 tail (last 96 bytes of L3201, read
  verbatim from disk by the scripts) + `CRLFCRLF` + line-initial `\emph{Vacuum term.}` — count exactly
  1 (asserted; cut byte 735,720).
- Insertion text: `insert-r1h.tex` (3,480 B, sha8 b9b75e8f, one content line + terminal CRLF, pure
  ASCII) — reproduced here in full as the fenced block (note: the fenced copy is for review; the
  integrator must take the bytes from insert-r1h.tex, since backslash escapes are unsafe in transit —
  see "Special instructions"):

```latex
\emph{Non-identifiability of the moment-type diagonal coordinate from the Gram spectrum.} Within the named constant-variance gaussian edge-block subclass of the fourth preceding paragraph, at \(D=2\), write \(G=AA^{\dagger}\), \(\tau=\operatorname{Tr}G\), the Gram-spectrum coordinate \(p=(\lambda_{1},\lambda_{2})/\tau\) of that paragraph, and the diagonal statistic \(\hat\rho_{2}=\sum_{i}(G_{ii}/\tau)^{2}\), the second power-sum of the normalized diagonal profile \(d_{i}=G_{ii}/\tau\), which differs by the constant shift one from the moment-map coordinate \(\rho_{2}=1+s_{2}/W^{2}\) of the third preceding paragraph evaluated at \(d\), and which in the rank-one edge-datum class of the fourth preceding paragraph is the second power sum of the slot coordinate of that paragraph. The Schur--Horn fibre of the spectrum map is explicit: for a fixed spectrum \(\lambda_{1}\ge\lambda_{2}>0\) the entry \(G_{11}\) ranges exactly over the interval from \(\lambda_{2}\) to \(\lambda_{1}\), with \(G_{22}=\tau-G_{11}\) and \(\lvert G_{12}\rvert^{2}=G_{11}G_{22}-\lambda_{1}\lambda_{2}\), and every value in the interval is realized by an edge-block configuration of the subclass; consequently \(\hat\rho_{2}\) takes, on the fibre over any single nondegenerate spectrum value, exactly the interval from \(1/2\) to \((\lambda_{1}^{2}+\lambda_{2}^{2})/\tau^{2}\), of width \((\lambda_{1}-\lambda_{2})^{2}/(2\tau^{2})\), while at the fully degenerate spectrum \(\lambda_{1}=\lambda_{2}\) the fibre collapses to the scalar multiple of the identity and \(\hat\rho_{2}\) is forced to \(1/2\). Two configurations of trace \(4\) exhibit the failure: the diagonal Gram \(\operatorname{diag}(3,1)\) and the Gram with diagonal \((2,2)\) and \(\lvert G_{12}\rvert=1\) share the spectrum \((3,1)\) while \(\hat\rho_{2}\) takes the distinct values \(5/8\) and \(1/2\). In the rank-one edge-datum class of the fourth preceding paragraph the spectrum coordinate is the single atom at the vertex, identical for every configuration, while \(\hat\rho_{2}\) ranges over the interval from \(1/2\) to \(1\), the endpoints realized by the configurations of squared norm sequence \((1,0)\) and \((1/2,1/2)\). There therefore exists no map from the profile simplex to the real line -- measurable, relabelling-equivariant, or otherwise -- that recovers \(\hat\rho_{2}\) from the Gram-spectrum coordinate almost everywhere on the support of the law of any constant-variance gaussian edge-block datum at \(D=2\): the spectrum map forgets the diagonal completely off the fully degenerate spectrum, and this is a proved nonexistence on the support for these two named coordinates within the named subclass, not an unproved absence of a supplied formula; the identification holds only after an extra selection, for instance on diagonal Gram matrices, where spectrum and diagonal agree as multisets. The normalized-diagonal coordinate of the sixth preceding paragraph remains the carrier of the profile information within these named classes. These statements are exact linear-algebraic identifiability statements on the support of the named subclass at \(D=2\), they bound nonexistence between the two named coordinates only, they evaluate no matrix integral of the core action, they supply no state and no selection mechanism, they do not fix the state that sets \(W\), \(g\), \(s\) or the frame, they leave the missing steps (i)-(iv) of the Missing step paragraph unchanged, and they close nothing in Problem~G.
```

- Splice rule: `appH[:cut] + insert_bytes + ONE CRLF + appH[cut:]`, cut = 735,720 (byte index of the
  line-initial `\emph{Vacuum term.}` following the pin; the preceding blank line L3202 is preserved,
  so the insert becomes a new standalone paragraph). Everything stays; no existing equation, sentence
  or label is modified. Expected POST (printed by simulate_apply_095.py): size 776,019 =
  772,537 + 3,480 + 2; sha256 600588c1d1087232ace2cea1cdecf13fb38885cf7a2126a72eedfdc1234bfa0d;
  CRLF 3,854; bareLF 0; close-idiom noun count 20→21; verb idiom count 1; `\emph{Vacuum term.}` 2;
  header count of the new paragraph 1.
- No new labels, refs, or bib entries; nothing else in the repository references this paragraph.
- Stale passages elsewhere: none created. The 091 "not supplied by the repository" sentence and the
  092 coordinate sentences stay as-is (see Research and reasoning, last paragraph).

## Verification scripts

All under this folder; run from repo root with `python -I`; deterministic (fixed sympy expressions;
numpy seed 20261119). `.out` files are the captured outputs.

- `gram_moment_nonbridge_095.py` → `gram_moment_nonbridge_095.out` — S1 fibre/PSD equivalence and
  numeric charpoly anchor; S2 range/width/monotonicity/collapse/rank-one endpoints; S3 exact
  counterexamples (5/8 vs 1/2; rank-one 1 vs 1/2); S4 moment-convention identities (ρ₂=1+s₂/W²,
  wall 3/2, single 2, diagonal realization); S5 seeded gaussian MC fibre spread.
  **Expected invariant outputs:** all 21 `chk` lines `PASS`; `S5.band_count 8735`;
  `S5.rho_min_max` min within 1e-7 of 0.5, max in (0.68, 0.70); final line `SUMMARY ALL PASS`.
- `simulate_apply_095.py` → `simulate_apply_095.out` — read-only splice simulation. Re-measures and
  asserts live PRE (772,537 / sha256 3f81a3a9...5a86 / CRLF 3,852 / bareLF 0), PIN count 1, cut byte
  line-initiality; prints full POST sha256/CRLF/bareLF/idiom/Vacuum counts and prefix/suffix identity.
  **Expected:** `PRE_SIZE 772537`, `POST_SIZE 776019`, `POST_SHA256 600588c1d1087232ace2cea1cdecf13f
  b38885cf7a2126a72eedfdc1234bfa0d`, `POST_CRLF 3854`, `POST_bareLF 0`, `IDIOM_pre_post 20 21`,
  `VACUUM_POST 2`, `CUT_BYTE 735720`, `SUMMARY ALL PASS`. No writes performed.
- `hygiene_095.py` → `hygiene_095.out` — insert hygiene: ASCII, no control bytes except the terminal
  CRLF (this check is load-bearing — see Special instructions), exactly one line + terminal CRLF, no
  `$`/`[`/`]`/`\cite`/`\ref`/`\eqref`/`\label`, single `\emph{...}` header ending with a period, banned
  status/closure vocabulary by word boundary, idiom at end, math-delimiter balance, header uniqueness
  across `chapters/*.tex`, POST idiom counts (21 noun / 1 verb).
  **Expected:** `INSERT_SIZE 3480 INSERT_SHA8 b9b75e8f`, `HEADER_HITS_IN_CHAPTERS []`, `SUMMARY ALL PASS`.

Reproduction pack (order): (1) `python -I proposals/095-g-gram-moment-identification/gram_moment_nonbridge_095.py`;
(2) `python -I proposals/095-g-gram-moment-identification/simulate_apply_095.py`;
(3) `python -I proposals/095-g-gram-moment-identification/hygiene_095.py`. All three must end `ALL PASS`.

## Decisions Taken

1. **Negative over positive route.** Both deliverables were open; the fibre calculus immediately gives a
   pointwise counterexample on the support, which is the strictly stronger and cleaner statement. An
   identification lemma would have required smuggling a gauge/selection, which the integrated 090/093
   paragraphs prove is not available in the class. Chosen: non-bridge lemma (favours the programme by
   converting a disclaimer into a proved constraint without new inputs).
2. **Which quantity counts as "the moment coordinate" on configurations.** The law-level ρ₂(g) is not a
   function of a single configuration at all, so the only honest configuration-level carrier in the
   named class is the diagonal-realized moment coordinate, i.e. ρ₂ evaluated at the 089 normalized
   diagonal — reduced by the constant shift one to \(\hat\rho_2=\sum(G_{ii}/\tau)^2\). Rejected:
   (a) inventing a configuration-level moment from the edge-block spectrum (would be an assumed target
   inserted into a calculation); (b) law-level "no bridge" phrasing (would mix the slot-law parameter g
   with edge-block configurations, a category error).
3. **Scope D=2 only.** The counterexample needs only D=2; extending to D≥3 via classical Schur–Horn is
   left unproved rather than cited blind. Rejected: claiming general D on the strength of a theorem not
   verified this pass.
4. **Do not edit the three "not supplied" sentences.** They remain accurate records; the new paragraph
   proves the nonexistence. Rejected: rewriting correct text (proposal rule 1).
5. **Rank-one clause phrasing** "second power sum of the slot coordinate" (089/091 terminology) after an
   initial draft said "slot-power profile statistic"; corrected by byte surgery (see below).

## Milestone assessment

Routine. A bounded proved sub-lemma/negative constraint on the exactness route (chain 2, edge
G.moments-interaction-nonconvex); no milestone trigger applies; no critical-path step is closed.

## Status-label recommendation

Re-derived from agenda/ledger as quoted above: critical path at full-GR scope = A, B, C, D1, E, F,
G-derived, N (G itself OPEN/CRITICAL PATH/PROGRAMME-CONDITIONAL). **All labels unchanged** by this
package.

## Author decision needed

None.

## Remaining open step

For Problem G's exactness route the state-side demand of the Missing step paragraph (missing steps
(i)-(iv)) is unchanged; this package bounds what coordinate bridges cannot do. Open avenues, ranked:
1. D≥3 extension of the non-bridge lemma (self-contained Schur–Horn proof for the braid permutahedron,
   plus the ρ-tuple rather than ρ̂₂ — the 093 Jacobian already gives the off-wall coordinate structure).
2. Exact conditional law of \(\hat\rho_2\) given p under the complex Wishart law at D=2 (fiber density
   ∝ \(\sqrt{a(\tau-a)-\lambda_1\lambda_2}\,\lvert\tau-2a\rvert/2\) — derived candidate, not yet proved
   with Jacobian bookkeeping); would upgrade S5 from numerical to exact.
3. Quantitative profile-information gap: mutual information between p and d under the named law
   (relates the "zero profile content" of the spectrum coordinate to a number).
4. State-side profile weight (the actual missing ingredient per 090/091; untouched here).

## Special instructions for the gatekeeper

- **Transit-safety:** during drafting, tool-transit corrupted four backslash escapes in the insert
  (`\tau`→TAB+'au', `\rho`→CR+'ho'). `insert-r1h.tex` is verified byte-clean by hygiene_095.py
  (`ascii_only`, `no_ctrl_except_eol`, math-delimiter balance). Integrate **only the bytes of
  insert-r1h.tex**; do not retype the insert from the fenced block in this file. Superseded artifacts
  `insert-r1.tex` (LF-terminated, shifted-definition defect), `insert-r1f.tex` and `insert-r1g.tex`
  (escape-corrupted) are registered in manifest.md as **never-integrate**.
- Verify scope limits in the insert wording: it claims nonexistence only for the two named coordinates
  (Gram-spectrum coordinate vs \(\hat\rho_2\)) within the constant-variance subclass at D=2, and does
  not assert that no other coordinate of any kind can carry the moment data, nor anything at D≥3.
- Re-check that the insert asserts no closure and ends with the noun idiom; confirm the close-idiom
  counts (20→21) and that "closes nothing in Problem~G." (verb form) is unchanged at 1.
- Re-derive the fibre identity \(|G_{12}|^2 = -\,(a-\lambda_1)(a-\lambda_2)\) and the width formula;
  they are the mathematical core. The MC band overshoot (0.692 vs 0.68) is a band-edge sampling
  artifact of the ±0.01 spectrum window, not a contradiction — the exact range statement is S2.
- appH contains non-ASCII UTF-8 (at least one 0xe2 sequence, byte offset ~711,159); splice scripts
  compare bytes, not decodes.
