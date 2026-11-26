# Proposal 054-lorentzian-fourier-observables, round 2

## Changes r1 -> r2

| # | Review item | Change |
|---|---|---|
| 1 | F1 | Insert (iv), first sentence: the review's replacement applied verbatim. J is now defined as the R_u integral divided by `I^{(u)}[1]`. The u-independence of `I^{(u)}[1]` on (0,2) is justified by 053's Stokes argument, with the phase of the auxiliary factor on `Tr A_0^2` chosen separately for each interval of u. |
| 2 | F1, citation | In the proposal's Step 4 bound, the r1 citation "`\|I^{(u)}[1]\| = \|Z_E\|` (053)" is corrected (see "Correction to proposal-r1 Step 4" below). The insert carries no citation for this. |
| 3 | F2 | The two closing sentences that repeated the 053 block are replaced verbatim by: "Assumption~\ref{ass:lorentzian} is not discharged by this either, and Problem~E keeps its ledger label." |
| 4 | F3 | Insert (i), last sentence: the review's replacement applied verbatim. The u = 1 statement is now an identity of integrands, not a limit of `I_eps`. |
| 5 | F4 | Insert (iv): "With \(k^\mu k_\mu=\mp\kappa^2\) for the two cases," replaced verbatim by "With \(k^\mu=\kappa\delta^\mu_0\) and \(k^\mu=\kappa\delta^\mu_j\), so that \(k^\mu k_\mu=\mp\kappa^2\),". |
| 6 | Note | Hashes, byte counts and the scratch build are refreshed. |

**Mechanics of the edits.**
- `apply_r2_edits.py` applied the four edits. It requires the r1 insert hash (`4f5c1301...5bd1`) and each old string to occur exactly once.
- It keeps the r1 bytes as `appH_insert.r1.tex`.
- A second run was refused with "appH_insert.r1.tex already exists; nothing written".
- Word-level diff of r1 against r2: only the four spans above changed.

No mathematics, numerics or other wording changed. Every claim, script and output of proposal-r1.md stands except where this file amends it.

## Result

Unchanged from proposal-r1.md: statements (i)-(iv) with their stated hypotheses.

- **Bounded no-go extension.** For the observable class stated, with eps -> 0 first at finite N and Definition (A), the regulated Lorentzian integral yields only continuations of Euclidean data. At N = 2 these are values and line integrals of the continued Euclidean characteristic function F_E. Real timelike momentum lies on the edge ray arg t = -3 pi/4 of the sector where the continuation is established.
- **What is not established.** Pointwise values at real timelike kappa, continuation across that ray, boosted momenta, holomorphy for N >= 3, N -> infinity first, gamma != 0 and Definitions (B) and (C) are all open.
- **Problem E.** No signature is derived, and Problem E keeps its label.

## Target and status

Unchanged from r1.
- **Problem E** (appH `sec:status-E`): OPEN; CRITICAL PATH for the matrix-derived label; PROGRAMME-CONDITIONAL. Chapter 17 L394-399 agrees.
- **Original target:** derive Lorentzian signature rather than retain Assumption ass:lorentzian.
- **Classification:** PROGRAMME-CONDITIONAL sharpening.

## Source reading

**Digest + targeted reads. Not a full scan.**

This round I read:
- review-r1.md in full;
- the r1 insert;
- proposal-r1.md Step 4.

Baseline checks:
- `git diff --stat HEAD -- chapters bib` is empty (HEAD c19bf49).
- The working appH is 532576 bytes, sha256 `7a75554e...6aaa`, unchanged since r1, so no re-anchoring was needed.

The review's scan ruling applies. Under CLAUDE.md 3(b), if r2 is a plain ACCEPT carrying M2, the r2 gatekeeper does the full scan.

## Research and reasoning

### Correction to proposal-r1 Step 4 (F1)

r1 wrote "Since `|I^{(u)}[1]| = |Z_E|` (053)". 053 establishes the equality only for 0 < u <= 1. Its auxiliary factor `exp(-delta[e^{3 pi i/8} Tr A_0^2 + e^{-pi i/8} sum Tr A_i^2])` keeps a positive real part on R_u only for u < 7/6.

The correct statement is that `I^{(u)}[1]` is independent of u in (0,2), so that `|I^{(u)}[1]| = |Z_E|` there:
- For 0 < u <= 1 this is 053's result.
- For [1, u_1] with u_1 < 2, rerun the same Stokes argument with the auxiliary factor's phase on Tr A_0^2 re-chosen for that interval. On [1, u_1] the A_0 angle spans 3 pi (u_1 - 1)/4 < pi and the spatial angle spans pi (u_1 - 1)/4. So a phase exists that makes the real part of the factor positive on every contour of the interval.
- The gatekeeper checked this independently (review-r1, "Gap found in (iv)").

The bound `|J(kappa)| <= 2 [sin(4 arg kappa/3)]^{-27/2}` and the holomorphy argument then hold as written in r1.

### The other edits

F2, F3 and F4 are wording only.
- **F3** makes explicit that statement (i) gives no limit at u = 1, because (i) needs u < 2/3.
- **F4** defines k^mu. It removes any clash with 053's k, which denotes the degree in (ii).

## Claim classification

Unchanged from r1, with one row amended:

| Claim | Class |
|---|---|
| `I^{(u)}[1]` independent of u in (0,2) at N = 2 | established (053 for u <= 1; for 1 < u < 2, 053's Stokes argument with the auxiliary phase re-chosen per interval) |
| u = 1 member of (i) | identity of integrands (not a limit) |

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`

**Placement.** One insertion, the same as r1. It goes immediately before the anchor below, which occurs once, at line 1512 (61 bytes, sha256 `a7c77412...26cc`, CRLF between the lines). Insert the CRLF form of `appH_insert.tex` followed by one CRLF. No existing text changes.

```latex
\paragraph{Status.}
Remains Assumption~\ref{ass:lorentzian}.
```

**Hashes** (`apply_check.txt`):

| Item | Bytes | sha256 | Line endings |
|---|---|---|---|
| Baseline appH | 532576 | `7a75554ef8cb7efe0e4c5cd3c53d6a9c4ffd2a9149e6ff29c7e8e067bb7f6aaa` | CRLF 3203, bare LF 0 |
| Insert, LF | 8011 | `dca477de7f98a866ba8bf14419b7791cc3ba7f61cdace5425c6a109241f9f8e8` | |
| Insert, CRLF form | 8027 | `ef4b69e905a924f57a2433f0a32ca19d83b3cb9c8f8aa83c81d79103e307eab7` | |
| Result appH | 540605 | `e67297cd3066e3f4795ed81875d5075dfec3fe98ba5a8d8feb0bfcb733e134d7` | CRLF 3220, bare LF 0 |

**Labels and citations.** Only `\ref{ass:lorentzian}`, which is defined once (ch04 L322). No new labels or citations, and no bib change.

**Stale passages.** None, as in r1.

Full text of `appH_insert.tex` (r2):

```latex
\paragraph{Fourier observables of the regulated integral (conditional for \(N\ge3\)).}
Keep the setting, Definition~(A) and the contours \(\mathcal R_u\) of the preceding paragraph, and let \(O\) be a product of \(n_{\mathrm{tr}}\) traces, each of a product of factors \(\mathrm e^{\mathrm i\kappa A_\mu}\) with a single index \(\mu\) and a constant \(\kappa\in\mathbb C\). For real \(\kappa\), \(\operatorname{Tr}\mathrm e^{\mathrm i\kappa A_0}\) is the Fourier mode of \(A_0\) with timelike momentum along the time axis that the regulator fixes. On \(\mathcal R_u\) such an \(O\) is bounded by \(N^{n_{\mathrm{tr}}}\mathrm e^{c\|\tilde A\|}\), with \(c\) the sum of the \(|\kappa|\), so for fixed \(\epsilon\) the Stokes argument above still gives \(I_\epsilon[O]\) on \(\mathcal R_u\) for every \(u<2/3\) (exact).

(i) \emph{Complex momenta.} Let \(0<u<2/3\), with \(\kappa=K\mathrm e^{3\pi\mathrm iu/8}\) in each factor with \(\mu=0\) and \(\kappa=K\mathrm e^{-\pi\mathrm iu/8}\) in each factor with \(\mu\ge1\), each \(K\) real. On \(\mathcal R_u\) every factor is then \(\mathrm e^{\mathrm iK\tilde A_\mu}\), which is unitary, so that \(|O|\le N^{n_{\mathrm{tr}}}\) there. The bound along the flat directions without the polynomial factor and dominated convergence give \(\lim_{\epsilon\to0^+}I_\epsilon[O]=I^{(u)}[O]\), the integral on \(\mathcal R_u\) at \(\epsilon=0\), and the ratios converge where the Euclidean partition function does not vanish. At \(u=1\) the same choice of \(\kappa\) makes the integral on \(\mathcal R_1\) at \(\epsilon=0\) the Euclidean expectation value of \(O\) with every factor replaced by \(\mathrm e^{\mathrm iK\tilde A_\mu}\); this is an identity of integrands, not a limit of \(I_\epsilon\).

(ii) \emph{Real momenta.} For real \(\kappa\neq0\) the integrand on the right-hand side of the limit display above, with \(O=\operatorname{Tr}\mathrm e^{\mathrm i\kappa A_0}\), is not integrable at \(N=2\). There \(|\operatorname{Tr}\mathrm e^{\mathrm iz\tilde A_0}|=2|\cos(z\|\tilde A_0\|_{\mathrm{op}})|\ge2|\sinh(\operatorname{Im}z\,\|\tilde A_0\|_{\mathrm{op}})|\), which grows exponentially for \(z=\kappa\mathrm e^{-3\pi\mathrm i/8}\), while the modulus of the Euclidean weight is the integrand of the bound along the flat directions at \(u=1\), so that, since that integral converges exactly for \(k<14\), and by \(\mathrm{SO}(10)\) invariance, it has no moment of degree \(14\) in \(\|\tilde A_0\|_{\mathrm{op}}\). The polynomial result does not extend to these observables in that form.

(iii) \emph{Smearing in the momentum.} For \(\varphi(\kappa)=\mathrm e^{-(\kappa-\kappa_0)^2/\ell^2}\), with \(\kappa_0\) real and \(\ell>0\), one has \(\int_{\mathbb R}\varphi(\kappa)\operatorname{Tr}\mathrm e^{\mathrm i\kappa A_0}\mathrm d\kappa=\sqrt\pi\,\ell\operatorname{Tr}\mathrm e^{\mathrm i\kappa_0A_0-\ell^2A_0^2/4}\), which on \(\mathcal R_u\) is bounded by \(\sqrt\pi\,\ell N\exp\bigl(\kappa_0^2\sin^2(3\pi u/8)/(\ell^2\cos(3\pi u/4))\bigr)\) for \(u<2/3\). Write \(\mathcal J(\kappa)\) for the limit of \(\langle\operatorname{Tr}\mathrm e^{\mathrm i\kappa A_0}\rangle_\epsilon\) given by (i) for \(\kappa\in\mathrm e^{3\pi\mathrm iu/8}\mathbb R\). Dominated convergence on \(\mathcal R_u\), followed by turning the line of integration in \(\kappa\) for fixed \(\tilde A\) onto \(\mathrm e^{3\pi\mathrm iu/8}\mathbb R\), where the trace is bounded by \(N\) and \(\varphi\) still decays like a Gaussian, gives
\[
\lim_{\epsilon\to0^+}\int_{\mathbb R}\varphi(\kappa)\,\langle\operatorname{Tr}\mathrm e^{\mathrm i\kappa A_0}\rangle_\epsilon\,\mathrm d\kappa=\int_{\mathrm e^{\mathrm i\theta}\mathbb R}\varphi(\kappa)\,\mathcal J(\kappa)\,\mathrm d\kappa\qquad(0<\theta<\pi/4),
\]
and the same holds for \(A_j\), \(j\ge1\), with the lines \(\mathrm e^{-\mathrm i\theta}\mathbb R\), \(0<\theta<\pi/12\).

(iv) \emph{Analytic structure at \(N=2\).} At \(N=2\) the Cauchy--Binet bound of the preceding paragraph holds for every phase and \(\operatorname{Re}\mathrm iS_{\mathrm b}=-\sin(\pi u/2)\,S_{\mathrm E}\) holds on \(\mathcal R_u\) for \(0<u<2\), so the integral of (i) on \(\mathcal R_u\), divided by \(I^{(u)}[1]\), defines \(\mathcal J(\kappa)\) for \(0<\arg\kappa<3\pi/4\), where \(I^{(u)}[1]\) is independent of \(u\in(0,2)\) by the Stokes argument of the preceding paragraph with the phase of the auxiliary factor on \(\operatorname{Tr}A_0^2\) chosen for each interval of \(u\), with \(u=8\arg\kappa/(3\pi)\), and \(|\mathcal J(\kappa)|\le2[\sin(4\arg\kappa/3)]^{-27/2}\). This function is holomorphic. The integrand is even in \(\tilde A_0\), so in polar coordinates for \(\tilde A_0\) the cosine may be replaced by one exponential along full radial lines, and the two halves of each line can be turned to phases slightly below and slightly above \(\arg\kappa\) with the phase of the \(\tilde A_i\) fixed; the integrand is then dominated uniformly for \(\kappa\) near a given point. Hence \(F_{\mathrm E}(t)=\mathcal J(\sqrt t\,\mathrm e^{3\pi\mathrm i/8})\) is holomorphic for \(|\arg t|<3\pi/4\), and for \(t>0\) it is the Euclidean characteristic function \(\langle\operatorname{Tr}\mathrm e^{\mathrm i\sqrt t\,\tilde A_0}\rangle_{\mathrm E}\), which by \(\mathrm{SO}(10)\) invariance is the same for every \(\tilde A_\mu\). For \(A_j\) the same steps give \(F_{\mathrm E}(\mathrm e^{\pi\mathrm i/4}\kappa^2)\) for \(-\pi/4<\arg\kappa<0\). Since \(\arg t=\pi/4\) lies inside the sector, the smeared limit for \(A_j\) in (iii) is \(\int_{\mathbb R}\varphi(\kappa)F_{\mathrm E}(\mathrm e^{\pi\mathrm i/4}\kappa^2)\,\mathrm d\kappa\). For \(A_0\) the line integrals in (iii) are integrals of \(F_{\mathrm E}(\mathrm e^{-3\pi\mathrm i/4}\kappa^2)\), and real \(\kappa\) corresponds to the boundary ray \(\arg t=-3\pi/4\). With \(k^\mu=\kappa\delta^\mu_0\) and \(k^\mu=\kappa\delta^\mu_j\), so that \(k^\mu k_\mu=\mp\kappa^2\), both read \(F_{\mathrm E}(\mathrm e^{\pi\mathrm i/4}k^\mu k_\mu)\), the timelike case being reached from \(k^\mu k_\mu-\mathrm i0\). At \(N=2\) the reduction of the preceding paragraph, extended by the angular integral over \(\tilde A_0\), gives the following (numerical). On \(\mathcal R_u\) with \(u=0.6\) and \(u=0.8\) the ratios to \(I^{(u)}[1]\) of the integrals of \(\|\tilde A_0\|_{\mathrm{op}}^{2n}\), \(n=1,2,3\), are the Euclidean moments times \(\mathrm e^{3\pi\mathrm in(u-1)/4}\) to within \(5\times10^{-7}\) relative, and \(\mathcal J\) agrees with the polynomial of degree six in \(\kappa\) built from them to the size of the first omitted term for \(|\kappa|\le1\). For \(u=0.8\) two phases of the \(\tilde A_i\) give the same \(\mathcal J\) to \(5\times10^{-11}\). On \(\mathcal R_{0.6}\) the limits in (i) and (iii) are approached linearly in \(\epsilon\), the ratio of the difference to \(\epsilon\) changing by at most \(2\%\) between \(\epsilon=0.03\) and \(\epsilon=0.003\). The smeared limit at \(\epsilon=0\) is the same on \(\mathcal R_{0.5}\) and \(\mathcal R_{0.6}\) to \(3\times10^{-6}\).

For these observables, this order of limits and \(\gamma=0\), the regulated integral therefore gives at finite \(N\), conditionally for \(N\ge3\), the integrals at \(\epsilon=0\) on the contours \(\mathcal R_u\), and at \(N=2\) values of the continuation \(F_{\mathrm E}\) of the Euclidean characteristic function, or line integrals of them, which \(F_{\mathrm E}\) on \(t>0\) determines. The Euclidean value at phases is not available for real timelike \(\kappa\). This is no statement about \(\langle\operatorname{Tr}\mathrm e^{\mathrm i\kappa A_0}\rangle_\epsilon\) pointwise at real \(\kappa\) as \(\epsilon\to0\); about whether \(F_{\mathrm E}\) continues beyond \(\arg t=-3\pi/4\); about momenta off the coordinate axes, which combine matrices with different phases on \(\mathcal R_u\); about holomorphy for \(N\ge3\); about \(N\to\infty\) taken first; or about \(\gamma\neq0\) and Definitions~(B) and~(C). Assumption~\ref{ass:lorentzian} is not discharged by this either, and Problem~E keeps its ledger label.
```

## Verification scripts

Unchanged from r1, plus:
- `apply_r2_edits.py` -> `apply_r2_edits.txt`. It applies F1-F4, keeps the r1 bytes as `appH_insert.r1.tex`, and refuses a second run.
- `apply_check.py`, re-run -> `apply_check.txt`, with the values above.

**Scratch build** (outside the repository; tree from `git archive HEAD`, without proposals/ and reports/, appH replaced by the apply_check output `e67297cd...34d7`):
- pdflatex, bibtex, pdflatex and pdflatex all exited 0.
- 359 pages.
- 0 "undefined" lines and 0 "multiply defined" lines in the log, no rerun warning.
- No BibTeX warnings.

`n2_runs.py` was not re-run, since no numerical claim changed.

## Decisions Taken

1. **F1-F4 applied verbatim, as required.** No alternative wording was considered.
2. **The F1 justification is placed in the insert's own sentence, not in a separate lemma.** The review supplied that sentence, and it keeps the block minimal.

All r1 decisions stand.

## Milestone assessment

M2 (bounded no-go extension), as the review judged. It is not a breakthrough, and not M3, M4 or M5.

## Status-label recommendation

- Critical-path set: A, B, C, D1, E, F, G-derived, N.
- E is unchanged.
- No label change.

## Author decision needed

None.

## Remaining open step

Unchanged from r1.

**For the original target:** a derivation of Lorentzian signature. Nothing here supplies it.

**Ranked open avenues:**
1. Edge behaviour of F_E at arg t = -3 pi/4 at N = 2, through a one-variable representation, together with the pointwise limit at real timelike kappa.
2. Contours that mix indices, which the review notes are not excluded by the 3 pi/4 cap of the per-index phase family.
3. N -> infinity first.
4. Reflection positivity (Osterwalder-Schrader type) of the N = 2 Euclidean characteristic functions.
5. N >= 3 holomorphy, and the 053 bound.
6. gamma > 0, and Definitions (B) and (C).
7. The scout's R2, which stays queued.

## Special instructions for the gatekeeper

- Check that the four replaced spans match review-r1 F1-F4 byte for byte and that nothing else in the insert changed. `appH_insert.r1.tex` holds the r1 bytes for the diff.
- Check the corrected Step 4 citation.
- If you issue a plain ACCEPT with M2, the full scan of CLAUDE.md 3(b) is due in this round.
- Process: tool calls were serial. No file outside the proposal folder was written, apart from the session scratchpad. No git write command was run, and nothing was denied this round.
