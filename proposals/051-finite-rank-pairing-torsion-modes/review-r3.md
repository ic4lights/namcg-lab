VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
The insert is exactly the r2 bytes plus R18, the bib is unchanged, and the corrected sentence is true and reads correctly in context. This is a review verdict, not merge approval; only the author merges.

## Source reading
**Method: digest + targeted reads. No full scan.**
- **Scan ruling:** ordinal 49 requires no full scan, and none was done. The package changes no definition, assumption, scope or status passage, and no milestone verdict is issued. **The next integration after this one is ordinal 50 and requires my full scan.**
- **Digest:** `make_digest.py --check` printed DIGEST CURRENT at head 1b904ca, with `dirty-chapters: yes`. I did not independently confirm your attribution of the dirty state to 049 and 050 this round: I did not diff the working tree, and my ledger grep showed only older "Pending author commit" lines. I read working-tree files, and `git diff --stat 426f2ab HEAD -- chapters bib` is empty.
- **Read in full:** `review-r2.md`, `proposal-r3.md`, `s7_r18_kappa.py`, `compile_check_r2.py`.
- **Read in part:**
  - `s3_cutoff_pencil.py` L1-110
  - `appH_insert.tex`: the cutoff paragraph and its tail
  - appH L569-572, L1385-1390, L1405-1407, L2954-2955
  - the digest header, and the ledger by grep
- **Not read this round:** ch17 beyond a grep. The D1 and N targets are as quoted in `review-r2.md`, and no chapter text changed between 426f2ab and HEAD. No literature was consulted, as no citation changed.
- **Unreadable files:** none.
- **Process disclosure:**
  - My second tool round issued two reads together, against the serial rule. Both were read-only. All later calls were serial.
  - My first byte script stopped on a regex escape in its last line, after every byte result had printed. I ran the label check again in a corrected script.
  - No background job was started.
  - Scratch files are in the session scratchpad. `git status` is unchanged, the proposal folder is clean against HEAD, and no pycache was written.

## Claim under review
The R18 correction to the cutoff paragraph. The package is otherwise as accepted in substance in `review-r2.md`: quadratic-order statements about the flat point of the first-order class, with a bounded de Sitter extension.

**Targets (ch17), as quoted in `review-r2.md`:** D1 and N.

**Verbatim Appendix H labels, re-read this round:**
- D (L569): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- F (L1405), first three lines re-read, remainder as quoted in `review-r2.md`: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- N (L2954): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

## Checks performed

**1. Bytes (my own script, not `apply_r18.py`, which I did not run).** I parsed the old and new strings raw from `review-r2.md`.

| Item | Result |
|---|---|
| Old string | count 1 in r2, 0 in the insert |
| New string | count 0 in r2, 1 in the insert |
| r2 with R18 applied | equals `appH_insert.tex` byte for byte |
| Insert | 14205 bytes, sha256 94b4c128d5d16ffbad412d43aebb3f9566fc7de90758b600564cd9ef70b7dd2e; 0 CR, ASCII, no BOM, 39 LF |
| `appH_insert.r2.tex` | 14148 bytes, sha256 b6ccbf5f8cbd2848413c3c1fddb7a6c112e52c103262c307d593c5cb45ef86dd; equals the insert at commit 426f2ab, which is what I reviewed in r2 |
| Bib | 647 bytes, sha256 77758a19e96b69e91cc20ccf03470739603ba05f6ae7b6bfeb0933fe4a4159f1; same at 426f2ab and HEAD |

**2. R18 claim.**
- **By hand.**
  - With psi1 psi2 = (sigma/sqrt2)(phi^2)', integration by parts gives kappa = -(sigma/sqrt2) E[d_t Q2 (v.p)] / sqrt(a).
  - The part of Q2 even in t has an odd derivative, so it integrates to zero. The term p.Lambda_t p is even because p.lambda p = 0.
  - The odd part is sinh t (v.p) for the boost and sin t (v.p) for the rotation. E[cosh t] = e^{sigma^2/4} and E[cos t] = e^{-sigma^2/4} at variance sigma^2/2.
  - With a = 4P^2: kappa = -sqrt2 sigma P exp(+-sigma^2/4), upper sign for the boost. The stated (1+O(sigma^2)) factor is correct and independent of P.
- **My own numerics, independent of s3 and s7.** These use different k and planes: k = (1,0,0,1) as a vector, boost(0,1), rotation(1,3). Gaussian p-moments are by Wick contraction and t by 25-digit quadrature, at sigma = 0.1, 0.05, 0.01 with P = 1, and sigma = 0.1 with P = 3.
  - |v|^2 = 4 in both cases.
  - H12 agrees with the closed form to all 10 printed digits in every case.
  - The relative correction is +0.00250313 for the boost and -0.00249688 for the rotation at sigma = 0.1.
  - All three entries are computable exactly. H11 and H22 scale as sigma^2 with P-dependent coefficients.
  - H22 is exactly zero in my boost case, because the trace of (1-Lambda)^T eta (1-Lambda) vanishes there. This is consistent with the O(sigma^2) in the display.
- **"The entries ... are evaluated exactly".** This is true of what s3 does. L92-94 give H11, H22 and H12 in closed form through the characteristic function. This confirms the wording covers all three entries, not only kappa.
- **Reading in context.** "The entries of this compression" now refers unambiguously to the displayed matrix, and no longer to the spectral-measure sentence before it. The sentence keeps "with a seeded Monte Carlo agreeing" and "smearing over the other five fibre directions is not treated". The stale "This is exact" has count 0. F13 parts 1 and 2 are both closed.
- **`s7_r18_kappa.py`,** run on a copy outside the repository: exit 0, output identical to `s7_r18_kappa.r3.out.txt`. It is a check, not a proof; the hand argument above is the proof. Its reproduction of the six printed s3 values holds.
- **`proposal-r3.md`** records F13 and adds no claim. `git diff --stat 426f2ab HEAD` over the folder shows only `appH_insert.tex` (one line), the kept r2 bytes, r3 outputs, `apply_r18.py`, s7, `proposal-r3.md` and `review-r2.md`. `proposal-r2.md` and s1-s6 are untouched.
  - The "DIGEST STALE" it reports was true of its moment, at head 2249df2, and the digest has since been regenerated.
  - Its disclosure of the `.rewrite(sp.erf)` change weakens no check: erf + erfc = 1, and the assertions still compare with the predicted closed form.

**3. Compile and mechanics on a copy outside the repository.**
- `compile_check_r2.py`, output identical to `compile_check.r3.out.txt`:

| Build | Exit codes | Pages | Undefined refs / citations / multiply defined | Bibtex warnings | Bibitems |
|---|---|---|---|---|---|
| Baseline | [0,0,0,0] | 344 | 0 / 0 / 0 | 0 | 68 |
| With insert and bib | [0,0,0,0] | 348 | 0 / 0 / 0 | 0 | 70 |

  The bbl has Hehl2017 and Sakai2019, and not Kibble1961.
- `s5_insert_mechanics.py`: output identical to the r3 output. All refs are defined, there are no new labels, no unused new keys, and 0 process words.
- **Anchor, my own byte check:** `\section{Problem E: signature}` + CRLF occurs once; + bare LF zero times; the bare string once in total. Bare LF in appH is 0 before and after insertion.
- **Bytes added:** appH 14244 after CRLF conversion. Bib: 670 bytes of entries plus a separating CRLF, so 672 in total.

**4. Scope and status.**
- No labels are added, and no status, priority or completion text is in the insert ("Status:" count 0).
- There is one closing status sentence: "Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL."
- D, F and N are open and unchanged in the working tree.
- Spacetime stays emergent.

## Findings
**Blocking: none. Major: none. Minor: none. PRIOR-CLAIM-ERROR: none.**
- **F13:** closed by R18, applied byte for byte. F1-F12 stay closed; nothing was reopened, since the bytes match.

## Scope of what is established
Carried unchanged from `review-r2.md`, with one precision: kappa is -sqrt2 sigma P exp(+-sigma^2/4) on the Gaussian, printed as -sqrt2 sigma P (1+O(sigma^2)).

**Proved within hypotheses (formal adjoints, domains untreated)**, for eq:Smatrix with C = 0, no matter, quadratic order about commuting matrices:
- on-shell signature on Q-perp/Q at null Q != 0, modulo gauge directions of either sign;
- no Hilbert-Schmidt eigenvector or Jordan block in background gauge;
- the fibre-less content is HKS's, and the spectrum and right action are Hanada's in the Euclidean form.

**Established identities:**
- T = F + yF, E1 + yE2 = -Mx, E2 = Mx, 2E3 = dE1 - eta E2;
- commutant ad-compatibility;
- pairing and half value;
- G semi-definite and never a nonzero multiple of eta;
- the dS labels and Maxwell equation, with no pairing or spectrum there.

**Compression:**
- The 2 x 2 matrix is a compression. Its entries are evaluated exactly on a Gaussian w for one boost and one rotation on its covering line.
- Its resolvent has two simple poles with residues of one sign.
- These are not poles of the probes' two-point function, whose spectral measure under the full operator is positive and continuous.

**Conditional or unresolved:**
- which form governs effective fields, and the sign of h_i^0 for them;
- full fibre smearing;
- selection of the class, frame and non-degeneracy, and Assumptions frame-lock, nondeg, lorentzian, local-lorentz;
- the B operator, masses, loops, diagonal dynamics, G_eff, the graviton two-point function, EFT-a2.

**Classification:** PROGRAMME-CONDITIONAL. Nothing is DERIVED for a critical-path target. D, F and N remain OPEN.

**Obstruction classes (bounded, not no-gos on the route):**
1. Masslessness: quadratic order; T = 0 background; first-order operators; commutant labels; Theta, order-zero and K-singlet additions; the bilinear term on dS. Within this class the torsion labels stay massless and are not removed.
2. Sign: the positive value holds in this pairing only, off the hyperplane for h_i^0 and for h along q. It is not a statement about effective fields.
3. Cutoff: one-parameter fibre smearing at sigma -> 0 before the momentum cutoff is removed.

**Milestone ruling, unchanged.** M1: no, the class is supplied and this is quadratic order. M2: no, the statement is bounded and lists its relaxations. M3, M4, M5: none. No BREAKTHROUGH.

**Open avenues, ranked (each keeps spacetime emergent):**
1. **T != 0 backgrounds** (Lie-algebra or left-invariant with torsion): the first place a label can get a non-derivative term, because F is first order there. Relaxes "background torsion zero". Read 0911.1769 first.
2. **Diagonal-element dynamics and which labels are Nambu-Goldstone** (HKS mass gap): relaxes the commuting vacuum and connects to selection.
3. **One-loop induced form on labels with IKKT content:** decides the tension. Sakai reports no mass induced at one loop, which lowers expectations for the mass branch unless independent torsion modes change it. A renormalised form may differ in sign from any positive truncation.
4. **Constraint branch for the fibre class:** HKS-type or supermatrix constraint removing excess labels. It must be derived, not imposed.
5. **Curved backgrounds with few automorphisms:** complex pairs on actual solutions, neutral chains.
6. **Full fibre smearing and Plancherel treatment;** full Hilbert-space construction per label, with domains.

## Recommended disposition
Integrate as-is:
- `appH_insert.tex`, converted to CRLF, immediately before `\section{Problem E: signature}` + CRLF: 14244 bytes added.
- `new_bib_entries.bib`, converted to CRLF, appended after a separating CRLF: 672 bytes added.

The next integration after this one is ordinal 50 and requires my full scan.

## Corrected snippet
None. No byte needs to change.

**Files:**
- C:\Users\redgi\Projects\namcg-lab\proposals\051-finite-rank-pairing-torsion-modes\proposal-r3.md
- C:\Users\redgi\Projects\namcg-lab\proposals\051-finite-rank-pairing-torsion-modes\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\051-finite-rank-pairing-torsion-modes\new_bib_entries.bib
- C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g51r3\bytes.py (byte check)
- C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g51r3\mine.py (own entries check)
- C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g51r3\final.py (anchor, labels, closing sentence)
