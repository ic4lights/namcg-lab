# Proposal 054-055-r2 (gpu line, combined 054 + 055), round 2

Packages combined here (gpu numbering; it does not match the local `proposals/057-070`):
`proposals/local-gpu/054-nonpolynomial-observables-lorentzian-n2` and
`proposals/local-gpu/055-anti-wick-slice-nonzero-k`. Review addressed: `proposals/local-gpu/_local-review/group3-E.md`,
sections 054, 055 and "Group-wide". The 057 PRIOR-CLAIM-ERROR against 055 is included.

## Result

This round gives the full corrected text of the 054 and 055 paragraphs for the Problem E ledger. It is anchored on the
current tree and applies every required revision of group3-E.md. Where a revision is not used verbatim, the reason and
the evidence are given in the table below.

The mathematical content is unchanged except for the 057 correction:
- **054 (bounded obstruction, N=2).** The right-hand side of the limit identity of the regulated Lorentzian integral
  paragraph diverges in modulus for the exponential observables `O_k = Tr e^{i k.A}` for every nonzero real `k` and
  every `k` off the anti-Wick slice. The identity is unresolved on the slice at `k != 0`. At fixed `gamma < 0` the
  obstruction is absent.
- **New in 054: the obstruction does not mean the limit fails to exist.** By (v) of the linear-contour paragraph,
  already in the tree, the limit of `<O_k>_eps` exists. It equals `F_E(e^{i pi/4} k.k)` for every real spacelike `k`
  and for every `k` with `Lambda^T k` real on `R_{u'}`, `0 < u' < 2/3`.
- **055 now carries the 057 PRIOR-CLAIM-ERROR correction (M3) in its own paragraph.** The exponents
  `cos(3 pi u/4 - pi/4)/(16 eps)` and `sin(3 pi u/4 - pi/4)/(8|gamma|)` are labelled as frozen-coefficient-model
  values. The contour-dependent coefficient gives exponents `r0^2/(16 sqrt2 eps)` and
  `-g^2 r0^2/(8 sqrt2 |gamma|)`, both independent of `u`. Hence the predicted growth as `gamma -> 0^-` is an artefact of
  the frozen model.
- **Surrogate numerics are labelled.** This covers the 055 factorized surrogate with frozen coefficient and the 054
  large-radius `cosh` proxy.
- **One status sentence for the block.** The 054-057 block now ends with a single scoped status sentence, at the end
  of 057.

Nothing here derives a signature, discharges Assumption~\ref{ass:lorentzian}, or changes a label. Problem E remains
OPEN, CRITICAL PATH for the matrix-derived label, and PROGRAMME-CONDITIONAL.

## Target and status

- **Problem E (signature).** In `chapters/appH-microscopic-proofs.tex`, `\section{Problem E: signature}`,
  `\label{sec:status-E}`, the ledger reads: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label.
  Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of
  emergent or matrix-derived Lorentzian signature."
- **Chapter 17.** `ch17-agenda.tex` L394-399 has "\emph{OPEN; CRITICAL PATH for the matrix-derived label.}", and the
  completion list at L718-719 has "Problem~E: Lorentzian signature is derived rather than retained
  (Assumption~\ref{ass:lorentzian})". Appendix H and Chapter 17 are consistent; there is no discrepancy.
- **Original target.** Lorentzian signature derived, not retained.
- **Critical-path set.** At the full-GR / matrix-derived scope, Chapter 17 requires A, B, C, D1, E, F, G-derived and
  N; H, I and J are optional.
- **This package.**
  - Its target is a bounded sub-lemma and obstruction for the limit identity of the regulated Lorentzian integral on
    exponential observables at `N=2`. It is PROGRAMME-CONDITIONAL: `eta` is supplied in `S_b`, and so are the fermion
    content and the regulator.
  - It is DERIVED inside its hypothesis class only where marked. The rest is numerical or a model.
  - Dependencies: the 053 paragraph (regulated Lorentzian integral, in the tree), the Fourier-observables paragraph
    ((iv): `F_E`), and the linear-contour paragraph ((v)), all in the tree. 056 and 057 are gpu plain ACCEPT, deferred,
    and integrated together with this package.

## Source reading

- **Mode.** Digest + targeted reads. `python scripts/make_digest.py --check` gives `DIGEST CURRENT`.
- **Dirty chapters.** The digest has `dirty-chapters: yes`. I checked the working-tree diff against HEAD
  (`git diff HEAD -U0`). It is confined to appH Problem A (around L28-79), appH L3097 (Problem I region) and one line of
  ch14. Nothing touches Problem E or ch17. **No full scan was done**, which protocol 3(d) formally requires when
  `dirty-chapters: yes`. I flag this for the gatekeeper: the dirty hunks do not overlap the passages used here.
- **Read in full.**
  - Problem E entry of the current appH, L1509-1691: all paragraphs and the Status.
  - ch17 L390-402 and L700-730.
  - group3-E.md.
  - review-r2 of 055.
  - The gpu backup paragraphs 053-057 (backup L1608, 1610, 1612, 1614, 1617).
  - The 053 paragraph sub-blocks "The bound along the flat directions" and "Limit at finite N".
  - Fourier observables (iv) and linear contours (iii), (v) and its closer.
- **Labels.** `ass:lorentzian` is defined once, in ch04 L322.
- **Citation keys.** `ChouNishimuraTripathi2025` and `AsanoNishimuraPiensukYamamori2025` are in `bib/namcg.bib` and
  already cited in the 053 paragraph.
- No unreadable files.

## Research and reasoning

### Placement (discrepancy with gpu, resolved)

In the gpu tree, 054-057 (and 060) sit right after the 053 paragraph, before "Fourier observables". The task asks for
an anchor before `\paragraph{Status.}`, which is the end of the Problem E ledger. I chose the end of the ledger, for
two reasons:
- 054's corrected text uses `F_E`, defined in (iv) of the Fourier-observables paragraph.
- 054 also uses (v) of the linear-contour paragraph.

Both sit between 053 and the end of the ledger, so at the gpu position 054 would use them before they appear. At the
end of the ledger every object 054-057 uses is already defined.

The cost is distance from 053. Three changes handle it:
1. 054 gets its own `\paragraph{...}` heading, so it is not read as a continuation of the doubleton-determinant
   paragraph that precedes Status.
2. 054 gets an opening sentence that recalls Definition (A), the contours `R_u` and "the displayed limit identity"
   of the 053 paragraph.
3. The sentence appended to 053 refers to "the paragraph on exponential observables at N=2 below" instead of "the
   next paragraph".

The order 053 < 054 < 055 < 056 < 057 < Status holds.

### Re-derivations

All of these are checked in `check_r2.py`.

1. **N=2 eigenvalues.** With `A_mu = sum_a A^a_mu sigma^a/2` (manuscript convention, 053 bound paragraph),
   `k^mu A_mu = sum_a w_a sigma^a/2` with `w_a = k^mu A^a_mu`. Its characteristic polynomial is
   `lam^2 - sum w_a^2/4`, so `rho_X^2 = sum_{a=1}^3 w_a^2 = -4 det(k.A)`, and `Tr e^{i k.A} = 2 cos(rho_X/2)`.
   - The gpu formula `rho_X^2 = k^mu k^nu G_{mu nu}` is ill-typed: `G_{ab} = eta^{mu nu} A^a_mu A^b_nu` carries colour
     indices. This confirms 054/5.
   - The relation is the su(2) determinant identity, not Cauchy-Binet. In this ledger Cauchy-Binet names the bound
     `|det G| <= det G~` of the 053 paragraph. This is why 055's "Cauchy-Binet identity" is renamed.
2. **Rank-one lower bound.** `|2cos(w/2)|^2 = 4(cos^2(Re w/2) + sinh^2(Im w/2))`. On `A~_mu = rho_mu H` with
   `Tr H^2 = 1`, the eigenvalues of `H` are `+-1/sqrt2`. So `|O_k| >= 2 sinh(b rho/sqrt2) >= 2 sinh(b rho/2)`: the
   stated bound is valid but not sharp. No change is needed; it is recorded so that nobody "corrects" it to a
   stronger, unproved form.
3. **Rank-one corner maximisation.** `max_rho [b rho/2 - A rho^2] = b^2/(16 A)`. With `b = sin(3 pi(1-u)/8)|r0|` and
   `A = eps cos(3 pi u/4)` this gives the `c0(u)` of 056. For real `k` at `u in (0,2/3)` the same argument runs along a
   ray with `b_u(rho^; k) != 0`. Such a ray exists for every nonzero real `k`, since the functional is nonzero (054,
   strip_symmetry (2c)-(2e)), and the regulator damping on that ray is at most `eps rho^2`. This supports the wording
   of 054/3 with the added "applied along a ray with `b_u != 0`".
4. **The 057 correction, from the one-dimensional branch model.**
   - Setup: `Q = e^{-3 pi i u/4}(eps - i gamma/(2 g^2))`, the branch integral is `2 sqrt(pi/Q) e^{-gc^2/(4Q)}`, and
     `gc = e^{i phi} r0/2`.
   - Frozen model, `phi = 3 pi/8`:
     - `Re(-gc^2/(4Q)) = r0^2 cos(3 pi u/4 - pi/4)/(16 eps)` at `gamma = 0`;
     - it tends to `r0^2 sin(3 pi u/4 - pi/4)/(8|gamma|)` at fixed `gamma < 0` with `g = 1`.
     - These are 055's numbers, correct inside the frozen model.
   - Contour-dependent model, `phi = 3 pi(1-u)/8`. On `R_u`, `k^0 A_0 = e^{3 pi i/8} r0 e^{-3 pi i u/8} A~_0`, check
     (2e). Then:
     - the exponent is `r0^2/(16 sqrt2 eps)` at `gamma = 0`;
     - it is `-g^2 r0^2/(8 sqrt2 |gamma|)` at fixed `gamma < 0`;
     - both are independent of `u`.
   - So the dependence on the sign of `3 pi u/4 - pi/4` and the divergence as `gamma -> 0^-` are frozen-model
     artefacts. With the true coefficient, the exponential factor of the signed 1D integral is
     `e^{-g^2 r0^2/(8 sqrt2|gamma|)} < 1` at fixed `gamma < 0`.
   - `Re Q = eps cos(3 pi u/4) + |gamma| sin(3 pi u/4)/(2g^2) > 0` on `(0, 2/3)`, so the Gaussian formula applies.
   - At `u = 0` the two coefficients coincide (2f). The `u = 0` ladder evidence of 055 is therefore not affected by the
     frozen-coefficient error. Only the `u = 0.6` rows use a coefficient that differs from the contour one.
   - This is a signed-integral statement. It does not contradict 057's modulus lower bound `e^{Gamma0(u)/|gamma|}`,
     which concerns absolute values.
5. **The commuting-ray form at u=0.**
   - `B = (1/sqrt2)[[r0^2, -r0 R], [-r0 R, -R^2]]` on `span{e0, r^}`.
   - The stated `lambda_max` is an eigenvalue, and `det B = -r0^2 R^2`.
   - So `lambda_max > 0` iff `r0 != 0`, and `lambda_max = 0` at `r0 = 0` (3a-3c).
6. **Support for the 054/1 inserted sentence.**
   - (v) of the linear-contour paragraph (current tree L1574) gives `lim <Tr e^{ik.A}>_eps = F_E(e^{i pi/4} k.k)` for
     every path with `Lambda(0)` real, `h(tau)` in the closure of the class, `Re Lambda^T Lambda > 0`,
     `h(1) in C_0` and `Lambda(1)^T k` real. It also states the result for every real spacelike `k`.
   - For `R_{u'}`, the path `tau -> R_{tau u'}` has `Re Lambda^T Lambda = diag(cos(3 pi u' tau/4), cos(pi u' tau/4),
     ...) > 0` iff `u' < 2/3` (5a, 5b). The `R_u` lie in the class adjacent to the Hermitian contour, as stated in that
     paragraph ("They contain the `R_u`") and in Fourier (i).
   - So the sentence is supported as written.
7. **Numerics re-run.** All scripts re-run, outputs in this folder:
   - **055 exact insertion at `u = 0`, `eps >= 0.1`.** Ratios are 3.459, 4.034, 2.052 (`r0 = 1`) and 3.305, 3.959,
     2.041 (`r0 = 2`). The range [2.041, 4.034] lies in "between 2.0 and 4.1".
   - **Factorized surrogate.**
     - The ladder goes down to `eps = 0.003`; the fitted slope is 0.0000.
     - At `u = 0.6`: `gamma = -0.2` gives [0.74696, 1.2550] and `gamma = -0.05` gives [1.5708, 1.7788]. Both lie in
       [0.74, 1.78].
   - **054 `n2_exp_mech`.** It samples `eps = 1, 0.3, 0.1, 0.03, 0.01` (so `eps in [0.01,1]`, as in 054/3). It uses a
     "masked large-radius cosh proxy (cb=0.4)", a surrogate. The proxy label is therefore added to 054/3.

### Finding-by-finding

| Finding | Action |
|---|---|
| 054/1 MAJOR | Both edits verbatim (E2.1a, E2.1b). |
| 054/2 minor | Applied with two changes, in E1. (a) "The next paragraph" becomes "The paragraph on exponential observables at \(N=2\) below", forced by the placement. (b) "it is unresolved on that slice" becomes "the identity is unresolved on that slice at \(k\ne0\)": on the slice the right-hand side converges, so "it" (the right-hand side) would be false. |
| 054/3 minor | Applied with additions: the proxy label ("for a large-radius \(\cosh\) proxy of \(\|O_k\|\) in a reduced chart"), the range \(\epsilon\in[0.01,1]\) and the verbatim corner-estimate clause, plus "applied along a ray with \(b_u(\hat\rho;k)\ne0\)" because the 056 estimate is stated for slice momenta. The leading comma is dropped for grammar. |
| 054/4 minor | Verbatim; only the first "(numerical)" is replaced. The second, for \(\gamma>0\) at \(k=0\), stays numerical. |
| 054/5 minor | Verbatim. |
| 055/1 MAJOR | Both replacements verbatim (E2.9, E2.11). Added: the 057 correction sentence, moved here from 057 (E2.10); "(it coincides with the contour-dependent one at \(u=0\))"; "of the frozen-coefficient model" after "pointwise saturation factor" (E2.12). |
| 055/2 minor | Verbatim (E2.13). |
| Group-wide closers | One status sentence for 054-057, at the end of 057 (E2.7, E2.13, E3, E4). |
| Group-wide L3766 / 060 | Outside this package; 060 is a separate item. |

## Claim classification

- **Established identities.**
  - `rho_X^2 = sum_{a=1}^3 (k^mu A^a_mu)^2 = -4 det(k.A)` and `O_k = 2cos(rho_X/2)`.
  - The `|2cos|^2` identity.
  - The `lambda_max(B)` formula and its sign lemma.
  - The 1D Gaussian branch formula and both sets of exponents (frozen and contour-dependent).
  - The corner maximisation `b^2/(16A)`.
  - That `R_{u'}`, `u' < 2/3`, satisfies the hypotheses of (v).
- **Derived within the hypothesis class.**
  - 054: the right-hand side diverges in modulus off the slice, and the commuting-ray growth `e^{c2/eps}` (model
    level, as stated).
  - 054: the mass-damped extension for every `k` at fixed `gamma < 0` (derived in 057).
  - 054: existence of the limit for real spacelike `k` and for `R_{u'}`-real `k`, via (v), already in the tree.
- **Numerical.**
  - The bounded corner factor `e^{-S_E}` and the polynomial factors in a reduced chart.
  - The `e^{c/sqrt eps}` behaviour of the `cosh` proxy. It is now only labelled as a proxy, and the rate is no longer
    asserted in the text.
  - Divergence at `gamma > 0`, `k = 0`.
  - All 055 reduced-model ratios: factorized surrogate with frozen coefficient; exact insertion at `u = 0`,
    `eps >= 0.1` only.
- **Conjecture or mechanism.** Phase-space suppression by Vandermonde and measure powers. This is hedged, with "no
  domination lemma is claimed".
- **Unresolved.**
  - Control of the left-hand side on the slice at `k != 0`, `r0 != 0`, at full `N=2`.
  - The `gamma -> 0^-` bridge.
  - `N -> infinity` first.
  - Assumption~\ref{ass:lorentzian}.

## Proposed changes

All edits are in `chapters/appH-microscopic-proofs.tex`. The text comes from `build_r2.py`, which asserts that each
old string occurs once. The CRLF files are `E1_053_sentence.r2.tex`, `E2_insert_054_055.r2.tex`,
`E3_056_adjusted.r2.tex` and `E4_057_adjusted.r2.tex`.

### E1: one sentence in the closing paragraph of the 053 paragraph

- **Anchor (current tree; occurs once, verified).** Inside the paragraph that begins "For these observables, this
  order of limits, and \(\gamma\le0\) or \(\gamma\) as above, the regulated integral therefore carries at finite
  \(N\)": `so that the domination above fails for them. It does not exclude a real-time reading obtained by
  continuation.`
- **Rule.** Insert the sentence below between "fails for them." and " It does not exclude". Every other sentence stays.

```latex
The paragraph on exponential observables at \(N=2\) below sharpens this at \(N=2\), \(\gamma=0\), regulator (A) and the contours \(\mathcal R_u\): the right-hand side diverges in modulus for every nonzero real \(k\) and every \(k\) off one slice, the identity is unresolved on that slice at \(k\ne0\), and the failure is absent at fixed \(\gamma<0\).
```

### E2: the corrected 054 + 055 paragraph, inserted at the end of the Problem E ledger

- **Anchor (current tree; the CRLF byte string occurs once, verified):**
  `Problem~E stays open with Assumption~\ref{ass:lorentzian} retained.` CRLF CRLF `\paragraph{Status.}` CRLF
  `Remains Assumption~\ref{ass:lorentzian}.` CRLF. The first line is the last sentence of the paragraph "A relative
  fermion determinant for the doubleton member at fixed \(\gamma>0\) ...".
- **Insertion rule.** Keep the anchor text. After the blank line that follows "retained.", insert in this order:
  1. the E2 text;
  2. a blank line, then 056 as adjusted by E3;
  3. a blank line, then 057 as adjusted by E4;
  4. a blank line, then `\paragraph{Status.}`.
- **Joint integration.** E2 refers forward to 056 ("the paragraph on the slice bridge band") and to 057 ("the
  paragraph on the \(\gamma\to0^-\) link below"). E2, E3 and E4 must therefore be integrated in one step. If 056/057
  are not integrated in the same step, E2 must not be integrated.
- **Application.** `build_r2.py --apply-to DIR` performs exactly this application. On the current tree (appH 631366 B,
  sha256 6a83d79ec7adce2b8f67bfaf7db7710b69129a62970c36311cc19a73324d4a4a, CRLF 3419, bare-LF 0) it gives
  647608 B, sha256 a9045bb35fcd50590ad4e727df04f1023ee42c6a5b34e34375f1691ae44dc311, CRLF 3428, bare-LF 0.

```latex
\paragraph{Exponential observables \(\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\) at \(N=2\) (bounded obstruction, partly numerical).}
Keep Definition~(A), the contours \(\mathcal R_u\) and the displayed limit identity of the paragraph on the regulated Lorentzian integral at finite \(N\). Let \(O_k(A)=\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\) with \(k\in\mathbb C^{10}\), at \(\gamma=0\), regulator (A), contours \(\mathcal R_u\) and \(\epsilon\to0^+\) last. For each fixed \(\epsilon>0\) and \(u<2/3\) the integral converges absolutely and is entire in \(k\), because on \(\mathcal R_u\) the growth of \(O_k\) is at most \(\mathrm e^{c(u,k)\|\tilde A\|}\) against a Gaussian regulator, and the fixed-\(\epsilon\) Stokes identity extends to it. At \(N=2\) the matrix \(k^\mu A_\mu\) has eigenvalues \(\pm\rho_X/2\) with \(\rho_X^2=\sum_{a=1}^{3}(k^\mu A^a_\mu)^2\), so \(O_k=2\cos(\rho_X/2)\) is branch-independent, and \(|2\cos(\omega/2)|^2=4(\cos^2(\operatorname{Re}\omega/2)+\sinh^2(\operatorname{Im}\omega/2))\). Along rank-one rays \(\tilde A_\mu=\rho_\mu H\), \(\operatorname{Tr}H^2=1\), the Euclidean weight \(\mathrm e^{-S_{\mathrm E}}\) is not exponentially damped and tends to a bounded factor along the corner (\(S_{\mathrm E}\) vanishes on the exact rank-one rays), the Pfaffian vanishes on the ray and is polynomial in the coordinates nearby, and the remaining factors are polynomial (numerical, in a reduced chart), while \(|O_k|\ge 2\sinh\!\bigl(b_u(\hat\rho;k)\rho/2\bigr)\) with \(b_u(\hat\rho;k)=|\operatorname{Im}(k^0\mathrm e^{-3\pi\mathrm iu/8}\hat\rho_0+k^i\mathrm e^{\pi\mathrm iu/8}\hat\rho_i)|\). At every \(u\in(0,1]\) the functional \(\hat\rho\mapsto\operatorname{Im}(k^0\mathrm e^{-3\pi\mathrm iu/8}\hat\rho_0+k^i\mathrm e^{\pi\mathrm iu/8}\hat\rho_i)\) is nonzero for every nonzero real \(k\) (at \(u=1\) its coefficients are \(-\sin(3\pi/8)k^0\) and \(\sin(\pi/8)\vec k\)), so the Euclidean side of the displayed limit identity diverges in modulus for every nonzero real \(k\); more generally it diverges for every \(k\) outside the slice on which \(k^0\mathrm e^{-3\pi\mathrm i/8}\) and all \(k^i\mathrm e^{\pi\mathrm i/8}\) are real, where \(|O_k|\le2\) and that side converges by the bound along the flat directions with polynomial degree \(0\). For \(\operatorname{Im}k\ne0\) such that some commuting unit \(\hat\rho\) has \(|\operatorname{Im}(k\cdot\hat\rho)|>|\operatorname{Re}(k\cdot\hat\rho)|\), the commuting-ray contribution to the \(u=0\) integral has \(S_{\mathrm b}=0\) and grows along a sequence \(\epsilon\to0^+\) like \(\mathrm e^{c_2(k)/\epsilon}\) with \(c_2(k)>0\) (commuting-ray model; no transverse stationary-phase bound is claimed), and for real \(k\ne0\) the integrand at \(u=0\) carries \(|O_k|\le2\) pointwise, but no fixed-\(u\) domination in \(\epsilon\) is available at any \(u\in(0,2/3)\): the fixed-\(\epsilon\) modulus on \(\mathcal R_u\) grows without bound as \(\epsilon\to0\) (numerical, for a large-radius \(\cosh\) proxy of \(|O_k|\) in a reduced chart, on the sampled range \(\epsilon\in[0.01,1]\); the rank-one corner estimate of the paragraph on the slice bridge band, applied along a ray with \(b_u(\hat\rho;k)\ne0\), gives growth at least like \(\mathrm e^{c/\epsilon}\) up to polynomial factors). Hence within the class stated the displayed limit identity fails for every nonzero real \(k\) and for every non-real \(k\) outside the slice on which \(k^0\mathrm e^{-3\pi\mathrm i/8}\) and all \(k^i\mathrm e^{\pi\mathrm i/8}\) are real, holds at \(k=0\), and is unresolved on that slice at \(k\ne0\): the displayed identity has no analyticity strip in \(k\) and no non-polynomial extension at \(\gamma=0\) off that slice, within the hypothesis class \(N=2\), regulator (A), contours \(\mathcal R_u\), \(\epsilon\to0^+\) last. This concerns the right-hand side of the displayed identity and the modulus route, not the existence of the limit: by (v) of the paragraph on linear contours that mix the indices, at \(N=2\) the limit of \(\langle O_k\rangle_\epsilon\) exists and equals \(F_{\mathrm E}(\mathrm e^{\mathrm i\pi/4}k^\mu k_\mu)\) for every real spacelike \(k\) and for every \(k\) with \(\Lambda^{\mathrm T}k\) real on \(\mathcal R_{u'}\), \(0<u'<2/3\), although for some of these \(k\) the commuting-ray contribution grows. The obstruction is the massless flat direction, and at fixed \(\gamma<0\) it is absent: the mass contributes on \(\mathcal R_u\) the real exponent \((\gamma/2g_{\mathrm{YM}}^2)[\sin(3\pi u/4)\operatorname{Tr}\tilde A_0^2+\sin(\pi u/4)\sum_{i=1}^{9}\operatorname{Tr}\tilde A_i^2]\), a Gaussian damping on every component that dominates \(\mathrm e^{c(k)\|\tilde A\|}\) uniformly for \(\epsilon\le\epsilon_0<|\gamma|/(2g_{\mathrm{YM}}^2)\), and the displayed limit identity then extends to \(O_k\) for every \(k\in\mathbb C^{10}\) (derived in the paragraph on the \(\gamma\to0^-\) link below). At fixed \(\gamma>0\) the \(u=1\) integral diverges in modulus even at \(k=0\) (numerical), so the contour family and the thimbles of~\cite{ChouNishimuraTripathi2025} act on different contour integrals and produce no competing value; the classicalization of~\cite{AsanoNishimuraPiensukYamamori2025} is tied there to a Lorentz-breaking infrared cutoff and bears neither on this paragraph nor on the statements above. Everything in this paragraph is for the hypothesis class stated in it, does not address \(N\to\infty\) taken first, and derives no signature, real-time response, background or continuation; Assumption~\ref{ass:lorentzian} is not discharged.

\emph{The slice at \(k\ne0\): refinement of the window and model-level growth control.} On the slice \(k^0\mathrm e^{-3\pi\mathrm i/8}=r^0\in\mathbb R\), \(k^i\mathrm e^{\pi\mathrm i/8}=r^i\in\mathbb R\) the identity \(\rho_X^2=\sum_{a=1}^{3}{(k^\mu A^a_\mu)}^2=-4\det(k^\mu A_\mu)\) is exact at \(N=2\), and on \(\mathcal R_1\) the contraction \(k^\mu A_\mu\) reduces to the Hermitian real-linear form \(r^\mu\tilde A_\mu\), so \(\rho_X\) is real and \(|O_k|\le2\) pointwise there; right-hand-side boundedness on the slice is structural. The commuting-ray alternative also refines inside the slice: at \(u=0\), writing the growth functional as \(B=\mathbf v\mathbf v^{\mathrm T}-\mathbf u\mathbf u^{\mathrm T}\) with \(\mathbf u=(\cos(3\pi/8)r^0,\cos(\pi/8)\vec r\,)\), \(\mathbf v=(\sin(3\pi/8)r^0,-\sin(\pi/8)\vec r\,)\), the matrix \(B\) is supported on \(\operatorname{span}\{\mathbf e_0,\hat{\mathbf r}\}\), has rank at most two, and \(\lambda_{\max}(B)=[{(r^0)}^2-r^2+\sqrt{{(r^0)}^4+6{(r^0)}^2r^2+r^4}]/(2\sqrt2)\), which is positive iff \(r^0\ne0\); for pure spatial slice momenta (\(r^0=0\)) there is no commuting ray with growth, the neutral set is \(\hat{\mathbf r}\cdot\hat\rho=0\), and \(B\) is negative off it. For \(r^0\ne0\) the one-dimensional branch integral \(\int_{\mathbb R}\mathrm e^{-Qa^2}\,2\cos(\gamma_{\mathrm c}|a|)\,\mathrm da=2\sqrt{\pi/Q}\,\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\), \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\) frozen at its value on the Hermitian contour, gives in that frozen-coefficient model (with \(g_{\mathrm{YM}}=1\)) pointwise modulus growth \(\mathrm e^{{(r^0)}^2\cos(3\pi u/4-\pi/4)/(16\epsilon)}\) for the soft temporal mode at \(\gamma=0\), saturating as \(\epsilon\to0^+\) at fixed \(\gamma<0\) to a constant of order \(\mathrm e^{{(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)}\), which diverges as \(\gamma\to0^-\) when \(3\pi u/4-\pi/4>0\) and decays when it is negative. In the one-dimensional branch model the coefficient of \(\tilde A_0\) in \(k^\mu A_\mu\) on \(\mathcal R_u\) at pure temporal slice momentum is \(\mathrm e^{3\pi\mathrm i(1-u)/8}r^0\), not its value at \(u=0\); with this contour-dependent coefficient in \(\gamma_{\mathrm c}\) the soft-mode growth exponent at \(\gamma=0\) is \({(r^0)}^2/(16\sqrt2\,\epsilon)\) and the fixed-\(\gamma\) saturation exponent is \(-g_{\mathrm{YM}}^2{(r^0)}^2/(8\sqrt2|\gamma|)\), both independent of \(u\), so the saturation factor above and its growth as \(\gamma\to0^-\) for \(3\pi u/4-\pi/4>0\) are properties of the frozen-coefficient model, not of the contour family; with the contour-dependent coefficient the exponential factor of the signed one-dimensional integral tends at fixed \(\gamma<0\) to a constant below one for every \(u\in(0,2/3)\). In the reduced \(N=2\) integral (regulator (A), contours \(\mathcal R_u\), \(\epsilon\to0^+\) last) with the factorized surrogate of this insertion along the soft temporal mode, coefficient frozen as above (it coincides with the contour-dependent one at \(u=0\)), at pure temporal slice momenta (the exact insertion, evaluated at \(u=0\) for \(\epsilon\ge0.1\) only, gives ratios between \(2.0\) and \(4.1\)), the modulus ratio \(|Z_\epsilon[O_k]|/|Z_\epsilon[1]|\) stays of order one and tends to \(2\) along the ladder down to \(\epsilon=3\cdot10^{-3}\) (fit slope \(0.0000\) of \(\ln\)-ratio against \(1/\epsilon\), against the pointwise corner value \(0.044/\epsilon\) at \(r^0=1\)), and at \(u=0.6\) with \(\gamma=-0.2,-0.05\) it stays between \(0.74\) and \(1.78\): in the reduction neither the commuting-ray growth \(\mathrm e^{c_2(k)/\epsilon}\) nor the pointwise saturation factor of the frozen-coefficient model materialises, consistent with phase-space suppression of the corner branch growth near the soft corner by Vandermonde and measure powers, though no domination lemma is claimed. These are reduced-model computations with oscillation-limited resolution at \(\gamma=0\); whether the left-hand side is controlled on the slice at \(k\ne0\) with \(r^0\ne0\) remains open at full \(N=2\), the \(\gamma\to0^-\) bridge from fixed-\(\gamma<0\) success remains open, and the pure-spatial half of the slice has no commuting ray with growth.
```

### E3: closing sentence of 056 (gpu plain-ACCEPT text; closer change only, for joint integration)

- **Old (end of 056):** `... or an independent mechanism. Problem~E remains open and PROGRAMME-CONDITIONAL.`
- **New:** `... or an independent mechanism.` That is, delete the final sentence "Problem~E remains open and
  PROGRAMME-CONDITIONAL."
- Nothing else in 056 changes. The full text is in `E3_056_adjusted.r2.tex`.

### E4: last two sentences of 057 (gpu plain-ACCEPT text; for joint integration)

- **Old (end of 057).** Delete from "In the one-dimensional branch model the coefficient of \(\tilde A_0\) ..." to the
  end ("... not of the contour family. Problem~E remains open and PROGRAMME-CONDITIONAL."). That correction sentence
  now stands, with the same formulas, in 055 (E2.10).
- **New (replacing it):**

```latex
The statements of this paragraph and of the two preceding ones hold in the hypothesis classes stated there, at \(N=2\) with \(\epsilon\to0^+\) taken last, and derive no signature, real-time response, background or continuation; Assumption~\ref{ass:lorentzian} is not discharged, and Problem~E remains open and PROGRAMME-CONDITIONAL.
```

- Nothing else in 057 changes. The full text is in `E4_057_adjusted.r2.tex`.
- "The two preceding ones" are the 054 paragraph (which contains 055) and 056.

### What this means for the 054-057 closers

| Paragraph | Status sentence |
|---|---|
| 054 | None; its scope sentence stays. |
| 055 | None; it ends at "...no commuting ray with growth." |
| 056 | None. |
| 057 | The single scoped status sentence above. |

The 053 closing paragraph keeps its own existing status sentence: it is current text, separated from the block by the
rest of the ledger. If 060 (reflection positivity) is later placed after 057, its "Problem~E remains open and
PROGRAMME-CONDITIONAL." should be handled the same way in 060's own round.

No stale passages elsewhere: grep finds no other text that cites the 054/055 wording.

## Verification scripts

All are in `proposals/local-gpu/054-055-r2/` unless noted. Re-run from the repository root.

1. `python -I proposals/local-gpu/054-055-r2/check_r2.py` produces `check_r2.out`. Expected: 18 PASS lines and the
   last line `OVERALL: ALL CHECKS PASS`. Key invariants:
   - (1b) `-4 det(k.A) = sum_{a=1}^3 w_a^2`;
   - (2c) `r0^2/(16 sqrt2 eps)` and (2d) `-g^2 r0^2/(8 sqrt2|gamma|)`, both u-independent;
   - (2a)/(2b) the frozen values;
   - (2f) the corner value 0.0441942;
   - (3c) `det B = -r0^2 R^2`;
   - (4a) `b^2/(16A)`;
   - the frozen saturation factors 1.4439 and 4.3469 at `u = 0.6`, `gamma = -0.2, -0.05`.
2. `python -I proposals/local-gpu/054-055-r2/build_r2.py [--apply-to DIR_OUTSIDE_REPO]` produces `build_r2.out`.
   Expected:
   - `status closers in 054-057 block: 1`;
   - anchors A1 and A2 each have count 1;
   - insert sha256 values: E1 810e8e99..., E2 f8fdd3ce..., E3 1cbaafa3..., E4 05d430d1...;
   - the applied copy is 647608 B, sha256 a9045bb35fcd5059...;
   - `BUILD_R2 OK`.
   The script needs the scratch backup or the frozen `gpu_source_053_057.txt` (sha256 891af036...).
3. Package scripts, re-run unchanged with `python -I <path>`. The outputs are in this folder as `rerun_*.out`. These
   scripts write no files.
   - `../054-nonpolynomial-observables-lorentzian-n2/laplace_model_r2.py`: `OVERALL: ALL CHECKS PASS`.
   - `../054-nonpolynomial-observables-lorentzian-n2/strip_symmetry.py`: `ALL PASS`.
   - `../054-nonpolynomial-observables-lorentzian-n2/n2_exp_mech.py`: about 5 minutes. **Proxy, labelled.** The sampled
     `eps` are 1, 0.3, 0.1, 0.03, 0.01. The `u = 0.6` fit is `0.6526 eps^{-1/2}`.
   - `../055-anti-wick-slice-nonzero-k/slice_ray_r1.py`: section (1) max relative deviation 4.596e-51; section (3)
     `0.0441941738/eps`.
   - `../055-anti-wick-slice-nonzero-k/n2_slice_r1.py`: about 45 s. **Factorized surrogate with frozen coefficient,
     labelled.**
     - E1 exact ratios fall in [2.041, 4.034] at `eps >= 0.1`.
     - The factor ladder fit slope is 0.0000, down to `eps = 0.003`.
     - E2 rows: `gamma = -0.2` min 0.74696; `gamma = -0.05` max 1.7788.
4. Build: `build_check_r2.out`. The copy was built in the session scratchpad outside the repository, with two
   pdflatex passes. Both exit 0, with 0 undefined references, 0 multiply defined, 386 pages.

## Decisions Taken

1. **Placement: end of the Problem E ledger, not after 053 as in gpu.** This placement keeps every object used
   (`F_E`, (v) of linear contours) defined before use. The order 053 < 054 < 055 < 056 < 057 < Status is kept.
   Rejected: the gpu placement, because of forward use of `F_E` and (v).
2. **054 becomes a `\paragraph`, with one opening "Keep ..." sentence; 055 stays an `\emph` sub-block inside it.**
   Rejected: leaving 054 as `\emph`, which would attach it to the doubleton paragraph.
3. **The 054/2 and 054/3 wording deviations,** with the reasons given in the table. In each case the replacement as
   given would be false or unlabelled in the new placement or in substance: the wrong "next paragraph"; the
   ambiguous "it"; the missing proxy label.
4. **"\(k<14\) Pfaffian window" in 054 becomes "the bound along the flat directions with polynomial degree \(0\)".**
   The symbol `k` is both the 053 polynomial degree and the momentum in the same sentence. Rejected: keeping it. 056
   keeps its own phrase, because 056 is not edited beyond its closer.
5. **"Cauchy-Binet identity" in 055 becomes "the identity ... \(=-4\det(k^\mu A_\mu)\)".** It is a determinant
   identity, and Cauchy-Binet names a different bound in the same ledger.
6. **The 057 correction moves into 055, and 057's tail becomes the block closer.** This satisfies 055/1 ("fix in 055's
   own paragraph") without duplicating the formulas. Rejected: duplicating them in both paragraphs, or leaving only a
   pointer in 055.
7. **The single status sentence sits at the end of 057.** Rejected: placing it after 055, which would be in the middle
   of the block.

## Milestone assessment

M3 (an accepted claim found wrong) applies to the 055 frozen-coefficient exponents. That PRIOR-CLAIM-ERROR comes from
057 and is now corrected in 055's own paragraph. Otherwise this is routine: no critical-path step is derived and there
is no new no-go beyond the stated classes. No breakthrough is claimed.

## Status-label recommendation

Current critical-path set (Chapter 17 and the ledger): A, B, C, D1, E, F, G-derived, N. Affected label: Problem E. It
stays unchanged: OPEN, CRITICAL PATH for the matrix-derived label, PROGRAMME-CONDITIONAL. No label change is proposed.

## Author decision needed

None.

## Remaining open step

To close the original target, Lorentzian signature must be derived rather than retained
(Assumption~\ref{ass:lorentzian}). Within this line, ranked:
1. **Signed (oscillation-based) control of the slice left-hand side at full \(N=2\), uniform in \(\epsilon\), for
   \(r^0\ne0\).** The reduced-model ratio O(1) with slope 0 is the lead. A transverse domination lemma would extend the
   identity to the slice.
2. **The \(\gamma\to0^-\) bridge at fixed \(u\).** With the contour-dependent coefficient, the 1D soft-mode factor
   is now damped for every \(u\in(0,2/3)\) at fixed \(\gamma<0\). The frozen-model obstruction for \(u>1/3\) is gone at
   branch level. Only the modulus obstruction of 057 remains, so the route needs signed estimates.
3. **The pure-spatial half of the slice (\(r^0=0\)) as a sub-window,** since it has no commuting ray with growth.

None of these selects a signature: \(\eta\) is supplied in \(S_{\mathrm b}\) throughout.

## Special instructions for the gatekeeper

- **Joint integration.** E2-E4 must be integrated together, with 056/057 in the same step. E2 refers forward to both.
- **Placement.** It deviates from gpu by design (Decision 1). Check that nothing in 054/055 uses an object defined
  only later, apart from those two forward references.
- **Verbatim check.** Every replacement is listed with a tag (E2.0-E2.13, E3, E4) in `build_r2.py`.
- **Re-check these points.**
  - Point 4 (contour-dependent exponents and the "constant below one" consequence).
  - Point 6 (that \(\mathcal R_{u'}\), \(u'<2/3\), meets (v)'s path hypotheses).
  - That the 055 numbers are within the re-run ranges.
- **Do not assert:**
  - that the limit identity holds on the slice at \(k\ne0\);
  - that the \(\gamma\to0^-\) bridge exists;
  - any domination lemma;
  - any signature derivation;
  - any label change.
- **Full scan.** The digest has `dirty-chapters: yes`, but the dirty hunks (appH Problem A and the I region, ch14) do
  not overlap Problem E. Decide whether a full scan is required before ACCEPT.
- **Outside this package.** L3766 and 060 (OS framing) belong to 060's own round.
