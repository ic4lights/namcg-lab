VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
r2 applies F1-F4 verbatim and changes nothing else. I re-derived the F1 claim (I^{(u)}[1] does not depend on u on (0,2)) and the other changed claims, and they hold. The apply_check hashes reproduce. No correction remains, so the package can be integrated. **The CLAUDE.md 3(b) full scan is incomplete** (see Source reading), and the M2 milestone is issued under that stated limitation.

## Source reading
**Mode: digest + targeted reads. This is NOT a full scan. The CLAUDE.md 3(b) full scan was attempted and not completed.**

Digest status:
- `make_digest.py --check` printed `DIGEST CURRENT`.
- Digest head is e375d9f, `dirty-chapters: no`, 30 files.
- `git status --short` is empty, and `git diff --stat HEAD -- chapters bib` is empty.
- appH is 532576 bytes, sha256 7a75554e…6aaa, 3203 lines.

Why the scan was not completed:
- The manifest is 947,210 bytes; appH alone is 532,576 bytes.
- I read appH L1-298 in full, then stopped. Completing the scan in one context would very likely have exhausted it and lost the review.

What was read in full:
- `chapters/appH-microscopic-proofs.tex`:
  - L1-298 (Problems A and B, part of the B ledger);
  - L1470-1515: the end of the 052 block, L1478 (052 as re-scoped by 053), the whole of Problem E (ledger label L1485-1489, the 053 block L1495-1510, Status L1512-1513), and the Problem F heading.
- `chapters/ch04-vierbein-emergence.tex` L312-341: sec:ch4-signature, and Assumption ass:lorentzian, defined once at L322.
- `chapters/ch17-agenda.tex` L390-401 (Problem E) and L714-722 (the criterion).
- Context lines:
  - ch16 L300-310 and L355-361;
  - ch09 L190-198 and L360-367;
  - appJ L98-106;
  - ch18 L66-74.
- Folder files: review-r1.md, proposal-r2.md, both inserts, apply_r2_edits.py/.txt, apply_check.py/.txt, `MILESTONE.md`, and the tail of `reports/ledger.md`.

Targeted grep coverage of every manifest file. This is not a reading:
- Terms searched: `ass:lorentzian`, `signature`, `Wick`, `regulated`, `Definition (A)`, `\mathcal R_u`, `F_{\mathrm E}`, `characteristic function`, `Fourier mode`, `k^\mu k_\mu`, `Problem~E`.
- I read the context of every hit outside appH. In appH I read the context of every hit on `ass:lorentzian`, "regulated Lorentzian", "Lorentzian matrix integral", "non-polynomial" and "real-time reading".

Unreadable files: none.

## Claim under review
The claims are unchanged from r1. The package covers Fourier observables (products of traces of single-index exponentials e^{iκA_μ}) under Definition (A), with eps→0 first, fixed N and gamma=0:
- **Step 0:** the fixed-eps Stokes identity for u<2/3.
- **(i):** limits at complex axis momenta on the unitary rays.
- **(ii):** non-integrability at real κ at N=2.
- **(iii):** smeared limits as line integrals.
- **(iv):** at N=2, J is holomorphic on 0<arg κ<3π/4 with the stated bound, and F_E is holomorphic on |arg t|<3π/4. Real timelike κ lies on the edge ray arg t=−3π/4, reached from k·k−i0.

**Original target:** derive Lorentzian signature rather than retain Assumption ass:lorentzian.

**Appendix H (L1486-1489), verbatim:** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature." The Status paragraph (L1512-1513) reads "Remains Assumption~\ref{ass:lorentzian}."

**Chapter 17 (L395), verbatim:** "OPEN; CRITICAL PATH for the matrix-derived label." The criterion (L718-719) reads "Problem~E: Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})."

The two sources agree. The current critical-path set is A, B, C, D1, E, F, G-derived, N. No label change is proposed.

## Checks performed

**r1→r2 diff (direct).**
- `git show a31435a:…/appH_insert.tex` hashes to 4f5c1301…5bd1, which equals `appH_insert.r1.tex`. HEAD's insert is dca477de…f8e8, which equals the working `appH_insert.tex`.
- A word diff shows exactly four changed spans.
- In a Python check I extracted the F1 and F2 replacement strings from review-r1.md and used the F3/F4 strings as quoted there. Applying all four to the r1 bytes reproduces r2 exactly (`reconstructed == r2: True`). Each new string occurs once in r2 and not in r1. So F1-F4 are verbatim and nothing else changed.

**apply_check.py (report mode), re-run with output to the session scratchpad.** Output is identical to apply_check.txt apart from the "wrote" line:
- baseline 532576 bytes, 7a75554ef8cb…6aaa, CRLF 3203, bare LF 0;
- anchor 61 bytes, a7c77412…26cc, count 1, line 1512;
- insert LF 8011 bytes, dca477de…f8e8; CRLF form 8027 bytes, ef4b69e9…eab7;
- result 540605 bytes, e67297cd3066…e134d7, CRLF 3220, bare LF 0.

These match the stated hashes. The anchor `\paragraph{Status.}` / `Remains Assumption~\ref{ass:lorentzian}.` exists exactly once.

**exact_checks.py** re-run: output identical to exact_checks.txt. The script is unchanged since r1, so this is a regression check only.

**F1: I^{(u)}[1] does not depend on u on (0,2) at N=2. Re-derived by hand.**
1. *Auxiliary factor.* Use exp(−δ[e^{iψ0} Tr A_0² + e^{iψs} Σ Tr A_i²]). On R_u, Tr A_0² = e^{−3πiu/4} Tr Ã_0² and Tr A_i² = e^{πiu/4} Tr Ã_i². The real parts are −δ cos(ψ0 − 3πu/4) Tr Ã_0² and −δ cos(ψs + πu/4) Σ Tr Ã_i².
2. *Where 053's choice works.* 053's ψ0 = 3π/8 gives positivity iff u < 7/6, which confirms the r1 gap. ψs = −π/8 gives positivity for u < 5/2, so the spatial phase needs no change on (0,2).
3. *Re-chosen phase.* On [1, u1] with u1 < 2, take ψ0 = 3π(1+u1)/8. Then |ψ0 − 3πu/4| ≤ 3π(u1−1)/8 < 3π/8 < π/2, so the real part is positive throughout. Equivalently, the A_0 angle span 3π(u1−1)/4 < π.
4. *Stokes at δ>0, ε=0.* The integrand is holomorphic (Pf is polynomial). On [0,2], Re iS_b = −sin(πu/2) S_E ≤ 0. The boundary term on a ball of radius R is therefore bounded by poly(R)·e^{−δcR²} → 0. This gives I_δ^{(u)} = I_δ^{(u')} on each interval.
5. *Removing δ.* On each end contour, δ → 0 follows by dominated convergence. The domination uses |Pf| e^{−sin(πu/2) S_E}, which is integrable at N=2 for every u ∈ (0,2): the Cauchy-Binet bound holds for any phase, and k=0 < 14. The modulus of the auxiliary factor is ≤ 1.
6. *Covering (0,2).* Chaining with 053's range (0,1] covers (0,2).
7. *Non-vanishing.* I^{(1)}[1] equals a phase times c_P ∫ (det G̃)⁴ e^{−S_E}, using G = e^{iπ/4} G̃ on R_1. This is nonzero.

Hence J = I^{(u)}[Tr e^{iκA_0}]/I^{(u)}[1] is well defined. The bound follows:
- the numerator is at most 2|c_P| s^{−27/2} ∫ (det G̃)⁴ e^{−S_E}, with s = sin(πu/2) = sin(4 arg κ/3), using |Tr e^{iKÃ_0}| ≤ 2 and the scaling Ã → s^{−1/4}Ã (30 + 24 = 54, giving exponent −54/4);
- the denominator equals |c_P| ∫ (det G̃)⁴ e^{−S_E} exactly;
- so |J| ≤ 2[sin(4 arg κ/3)]^{−27/2} is confirmed.

The unitary condition κA_0 = |κ|Ã_0 holds iff arg κ = 3πu/8, i.e. u = 8 arg κ/(3π) ∈ (0,2). F1's added sentence is correct, and it adds no assumption.

**F1 citation in the proposal.** proposal-r2's "Correction to proposal-r1 Step 4" now attributes |I^{(u)}[1]| = |Z_E| to 053 only for u ≤ 1, and to the re-phased Stokes argument for 1 < u < 2. This is correct, and the insert carries no citation for it.

**F3.** At u=1 with κ = Ke^{3πi/8} (μ=0) and Ke^{−πi/8} (μ≥1), each factor equals e^{iKÃ_μ}. The integral on R_1 at ε=0 is then the 053 Euclidean integrand (Pf(−iÃ_0, Ã_i) e^{−S_E}) with that O. It is an identity of integrands, and the new text says it is not a limit of I_ε. Correct.

**F4.**
- k^μ = κδ^μ_0 gives k·k = η_00κ² = −κ²; k^μ = κδ^μ_j gives +κ². This matches "∓" in timelike-first order.
- e^{iπ/4}(−κ²) = e^{−3πi/4}κ² matches the A_0 statement, and the A_j statement matches F_E(e^{iπ/4}κ²). Signature (−,+,…) is consistent.
- The clash with 053's degree k is removed, because k^μ is now defined.

**F2.** The closing sentence "Assumption~\ref{ass:lorentzian} is not discharged by this either, and Problem~E keeps its ledger label." is one scoped closing sentence. It no longer repeats L1510 on the consecutive paragraph and changes no label.

**Earlier r1 checks** (Step 0, (i)-(iv), the scripts and the numerics against n2_runs.txt) concern text that r2 does not change. I re-checked the bound and F_E steps above wherever F1/F4 touch them. n2_runs.py was not re-run (about 3 h), and no numerical sentence changed.

**LaTeX (direct).**
- Braces, `\(`/`\)` and `\[`/`\]` are balanced.
- The only reference is `\ref{ass:lorentzian}`, which exists once (ch04 L322). There are no labels and no citations.
- There is no process language: no hits for propos/researcher/review.
- The insert is ASCII, LF in the proposal file, and CRLF on application.
- No build was run (read-only). The researcher's scratch build (359 pages, 0 undefined, 0 multiply defined) is not independently verified.

**Cross-file consistency** (from the reads and greps listed above, not from a full scan):
- **Assumption ass:lorentzian and signature.** ch04 L321-333, ch03 L196, ch10 L372-373, ch16 L89/131/305/359, ch17 L100/394-399/670/697/718-719, ch18 L72 and appJ L102-104 all retain ass:lorentzian. The insert keeps it retained, so there is no conflict.
- **Problem E.** The label is unchanged in appH and ch17.
- **The 053 caveat (appH L1510).** The 053 sentence "no statement … about non-polynomial observables such as Tr e^{ik^μA_μ} … It does not exclude a real-time reading obtained by continuation" stays a correct scope statement of its own paragraph. The 054 paragraph follows directly and treats an axis-momentum subclass while leaving off-axis momenta open. It is not stale.
- **052 as re-scoped (L1478).** "Polynomial moments of low degree … up to phases" is consistent with the insert.
- **Definition (A).** "Definition~(A)" and "Definitions~(B) and~(C)" follow the (A)/(B)/(C) list at L1496 and the "Definition (C)" heading at L1508, so there is no clash.
- **Notation.** `\mathcal J` is defined locally and is also used in Problem B (L279-283) for a normal-plane rotation. This was accepted in r1 and is unchanged.

**Literature.** No new citations. No SME consultation needed.

## Findings
**r1 findings, re-verified:**
- **F1:** closed. Verbatim, and mathematically verified above.
- **F1-citation:** closed.
- **F2:** closed. Verbatim.
- **F3:** closed. Verbatim.
- **F4:** closed. Verbatim.

**New findings:** none blocking, major or minor.

**Observations (not findings; no change required):**
1. *Range of R_u.* 053 introduces R_u "for 0≤u≤1" (L1498). The insert (iv) uses the same explicit parametrisation for 0<u<2 ("holds on R_u for 0<u<2"). The formula fixes the extension unambiguously, so no edit is needed.
2. *Placement of "with u = 8 arg κ/(3π)".* After F1, this clause follows "chosen for each interval of u,". Its meaning (the u used to define J at κ) is clear from (i). This is the review's own F1 text, and I do not require a change.
3. *Pre-existing appJ wording (not caused by this package; for the author).* appJ L103-104 says Problem E "remains under the assumption stated in Chapter 3". Assumption ass:lorentzian is stated in ch04; ch03 L196 only retains it.

No PRIOR-CLAIM-ERROR.

## Scope of what is established
As in review-r1, now with F1 in place.

**Established (exact):**
- Step 0, at any N;
- the unitary-phase identity;
- the smearing identity and its bound;
- the u=1 integrand identity (not a limit);
- at N=2, the u-independence of I^{(u)}[1] on (0,2).

**Proved at N=2; conditional for N≥3** (053's flat-direction bound at k=0, and Z_E ≠ 0):
- (i), for 0<u<2/3;
- (iii).

**Proved at N=2 only:**
- (ii);
- (iv): holomorphy of J on 0<arg κ<3π/4 with |J| ≤ 2[sin(4 arg κ/3)]^{−27/2}, and holomorphy of F_E on |arg t|<3π/4;
- the spacelike smeared limit ∫φ F_E(e^{iπ/4}κ²);
- real timelike κ on the edge arg t = −3π/4, reached from k·k − i0.

**Hypothesis class of the bounded no-go:**
- IKKT content supplied, C=0, gamma=0;
- Definition (A) with a δ_{μν} Gaussian regulator;
- fixed N, eps→0 first;
- axis momenta, products of single-index exponentials;
- complex momenta on the unitary rays, or Gaussian smearing in κ.

Within this class, the regulated Lorentzian integral yields only continuations of Euclidean data.

**Not established:**
- the pointwise limit at real timelike κ;
- continuation across arg t = −3π/4;
- boosted or off-axis momenta;
- N≥3 holomorphy;
- N→∞ first;
- gamma≠0;
- Definitions (B) and (C);
- any signature, background, frame or fermion content.

**Classification:** PROGRAMME-CONDITIONAL. Problem E stays OPEN, CRITICAL PATH for the matrix-derived label, PROGRAMME-CONDITIONAL. ass:lorentzian is retained.

**Open avenues** (ranking unchanged from r1):
1. Edge behaviour of F_E at arg t = −3π/4 at N=2, via a one-variable representation, together with the pointwise eps→0 limit at real timelike κ. This is the one place a non-Euclidean light-cone datum could enter in this class.
2. Contours that mix indices, beyond the per-index phase family that caps the sector at 3π/4. These could also reach boosted momenta.
3. N→∞ taken first (the constants are not uniform in N).
4. Osterwalder-Schrader reflection positivity of the N=2 Euclidean characteristic functions, giving a real-time Hilbert-space reading. Spacetime stays emergent.
5. Holomorphy for N≥3, and an independent proof of 053's bound.
6. gamma>0, and Definitions (B) and (C).

**Milestone.** M2: a bounded no-go extension that answers, for the stated class, the exception 053 named explicitly. It is not M3 (no merged claim is wrong), not M4 or M5, and not a BREAKTHROUGH (no step of a signature derivation).

## Recommended disposition
Integrate as-is: the CRLF form of `appH_insert.tex` (r2, dca477de…f8e8), followed by one CRLF, immediately before the unique anchor at appH L1512. The resulting appH must be 540605 bytes, sha256 e67297cd3066e3f4795ed81875d5075dfec3fe98ba5a8d8feb0bfcb733e134d7. Run `scripts/build_check.py` after integration.

**Scan limitation.** The CLAUDE.md 3(b) full scan for this milestone verdict was not completed: only appH L1-298 and L1470-1515 were read in full, and every other file was covered by targeted grep. The orchestrator should arrange a complete full scan, for example split across passes by file, before or alongside the milestone digest, and record in the digest that this M2 verdict was issued with the scan incomplete. Nothing found in the targeted reads conflicts with the insert.

## Corrected snippet
None required.

Files:
- C:\Users\redgi\Projects\namcg-lab\proposals\054-lorentzian-fourier-observables\proposal-r2.md
- C:\Users\redgi\Projects\namcg-lab\proposals\054-lorentzian-fourier-observables\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\054-lorentzian-fourier-observables\appH_insert.r1.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\054-lorentzian-fourier-observables\apply_check.txt
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (anchor L1512; Problem E L1482-1513)

VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0
