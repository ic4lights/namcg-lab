VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1

## Verdict
The central result holds within its stated class (Hilbert–Schmidt operators, Spin(4,1)-smooth vectors): there is no normalisable kernel. I re-derived the algebra, the two-condition step, the principal-series preimage and the regular-representation embedding, and they check out. Four corrections to the insert are still needed:
- the "every n" conclusion must be conditioned on the n>0 doubleton/ladder identification, which has not been verified (major);
- two sign conventions in the insert are wrong;
- the closing sentence nearly duplicates 061's;
- the unitary-dual input in Route 2 needs a citation.

## Source reading
- **Mode.** Digest plus targeted reads. `make_digest.py --check` printed DIGEST CURRENT. `dirty-chapters: yes` is expected: appH and bib hold 061, integrated and uncommitted.
- **Full scan.** Not performed. Per the orchestrator's ruling, the CLAUDE.md 3(a) full scan for ordinal 60 runs separately, in split passes, before integration. This review does not claim one.
- **Read in full, appH:**
  - Problem E ledger label (L1483–1488);
  - the 059 (P1)/(P2) paragraph end (L1586);
  - the 060 block (L1588–1607) and the 061 block (L1609–1620);
  - the Status anchor (L1622–1623);
  - the D ledger label (L597–603);
  - the doubleton passage (L1088–1096);
  - the fibre-cutoff and admissible-cone passage (L2505–2512).
- **Read in full, other chapters:** ch17 Problem E (L394–399), D1 (L333–343) and the completion list items D1/E (L708–722); ch04 ass:lorentzian (L322–328).
- **Also read:** reports/ledger.md (061 entry, tail) and MILESTONE.md. No file was unreadable.

## Claim under review
- **Claim.** Setting:
  - Definition (A), h₀ of signature (9,1), supplied IKKT fermions, supplied γ=3c>0;
  - the 060 member T̄^a=√c M^{a4} on a doubleton H_n, with W timelike;
  - order N→∞ first.

  In the class HS(H_n)⊗16 with inner product Tr ψ†ψ, taken on Spin(4,1)-smooth vectors, Γ^a[T̄_a,·] has trivial kernel for every n. Stated limits:
  - In B(H_n) the kernel contains 1⊗χ.
  - There is no bounded inverse.
  - The N=∞ Pfaffian is undefined.
  - No one-loop separation is established.
- **Original target.** Problem E: Lorentzian signature derived, not retained. D1 is touched only as a bearing.
- **Appendix H E, verbatim:** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- **Appendix H D, verbatim:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- **Ch17 E:** "OPEN; CRITICAL PATH for the matrix-derived label."
- **Consistency.** Ch17 and Appendix H agree, and the current critical-path set is A, B, C, D1, E, F, G-derived, N. No discrepancy.

## Checks performed

**Scripts.** I re-ran both scripts; their outputs are byte-identical to the saved .out.txt files. This is a check on finite-dimensional non-unitary representations, not a proof.
- s1: n=1,2; all identities at ≤4e−15; control signs fail; kernels 12/40.
- s2: (i) to (iv) as reported.
- apply_check.py reproduces every hash:
  - appH baseline 599923 B, 82ab2364…279c, which matches the working tree;
  - anchor count 1, at L1622, preceded by a blank line;
  - result 606285 B, 6a8c811d…86d6, CRLF 3324, bare LF 0;
  - bib 28049 B, 582f09d5…1f22 → 29360 B, 1d280848…856d, CRLF 980, bare LF 0;
  - no duplicate keys; the four new keys are absent from the current bib and chapters;
  - ass:lorentzian is defined once (ch04 L322).
- I could not reproduce build_r1.txt here (read-only); the integrator's build_check.py remains required.

**Independent re-derivations (direct).**
1. *su(2) relations of J_L.* With the Lorentz relations ([J,J]=iεJ, [J,K]=iεK, [K,K]=−iεJ), I computed [J−iK, J−iK] = 2iε(J−iK), and the same holds for J+iK. So J_L = ½(J±iK) is su(2)-normalised. Since [J_i,K_i]=0, (J±iK)² = J²−K² ± 2iJ·K = C4 ± 2iP.
   - Note: the ± in J_L must match the ± in 4J_L². See F2.
2. *X identity.* (J_L+σ/2)² = J_L²+σ·J_L+3/4. With C4 = 2(J_L²+J_R²), this gives C4^tot = C4+2X+3/2. Then D²=C5−C4^tot+3/2 gives C5−C4−2X. Also (σ·J_L)² = J_L²+iσ·(J_L×J_L) = J_L²−X. Confirmed.
3. *Two conditions.* D₊ψ=0 gives (A−2X)ψ=0. Since [A,X]=0 (C5 and C4 commute with J,K), 4X²ψ=A²ψ. Hence 4J_L²ψ=(A²+2A)ψ, i.e. Bψ = ∓2iPψ with B=1+C4−(A+1)². B and P are symmetric, commute and preserve HS^∞, so ⟨Bψ,Pψ⟩ is real and ‖Bψ‖² = ∓2i·(real). Hence Bψ=Pψ=0. Confirmed.
   - The conclusion is independent of the sign conventions: with A=−2X instead, one gets B'=1+C4−(A−1)², with the same consequences, P=0 and 1+C4≥0.
   - ad M is symmetric for Tr ψ†ψ, by Tr([M,ψ]†φ)=Tr ψ†[M,φ].
4. *Principal series.* C4=k²−p²−1, P=kp. Both pk=0 and k²−p²≥0 hold only at p=0, and k=0 forces −p²≥0. So within the principal series the set is {D(0,k)}, a countable set.
   - Complementary series (1+C4=r²>0, P=0) and the trivial representation (C4=0) satisfy the algebraic condition and are excluded only by the Plancherel support, as the proposal states.
   - Route 2 check: C4≤−1 excludes D(0,k≥½) (C4≥−3/4), the complementary series and the trivial representation, leaving D(p,0).
5. *Spectral step.* C5's spectral projections are central for Spin(4,1); those of C4 and P are central for Spin(3,1) ⊂ Spin(4,1). So the three operators strongly commute, and Bψ=0 puts ψ in E({b=0}) ⊂ {1+c4≥0}.
   - The agreement of the algebraic Casimirs on smooth vectors with the decomposable scalars is standard. One argues via Dixmier–Malliavin (ψ=ΣU(f_i)φ_i) rather than the proposal's "iterated Stone"; that wording is loose but does not change the conclusion, and it stays in the proposal, not the insert.
6. *Regular-representation embedding.* You asked whether this is proved or only plausible. It is **proved**, given standard Wigner and Mackey theory:
   - H_n|SL(2,C) is the Lorentz part of a massless Wigner representation: L² sections over C₊ with d³p/|p|. HS ≅ H⊗H̄ gives sections over C₊×C₊.
   - Collinear pairs form a 4-dimensional subset of a 6-dimensional space, so they are null.
   - For future null p, q that are not collinear, p·q<0. Their stabiliser fixes the timelike plane span(p,q) and is SO(2) on its spacelike complement; the preimage in SL(2,C) is U(1), which is compact.
   - The stabiliser of p (dimension 3) acts transitively on the connected 2-dimensional level set {q: q²=0, p·q=−s}, so each orbit is G/U(1) (dimension 5 = 6−1).
   - The invariant product measure disintegrates as ν(ds)⊗μ_{G/U(1)}, using only uniqueness of the invariant measure on each orbit; ν need not be computed.
   - Ind_{U(1)}^G χ ⊂ L²(G), because U(1) is compact.
   - Hence HS(H_n)|Spin(3,1) ⊂ ∞λ, and invariant subspaces reduce central projections.
   - I verified the stabiliser and orbit claims analytically as well as by s2(iv).
   - Caveat: Route 1 needs H_n to be a ladder (massless) representation. See F1.
7. *Smoothness.* It is needed: the step uses symmetric, commuting B and P and D₊ψ in the domain of D₋. It is stated as a premise in the insert. Non-smooth closure vectors are recorded as not treated.
8. *n-dependence.* Route 2 settles n=0 independently of Mack–Todorov, using MS (11)–(12), the unitary dual and MD (308). For n>0 the conclusion rests on H_n being a ladder representation, which is unverified (F1).
9. *Explicit σ convention in the insert (new).* With σ^a=(1,σ⃗) and σ̄^a=(1,−σ⃗), σ̄^aσ^b+σ̄^bσ^a = −2η^{ab} for η=(−,+,+,+). Hence ½tr_{C²}(D₋D₊) = −η^{ab}ad T̄_a ad T̄_b = −c(C5−C4), whereas ½tr(c(C5−C4−2X)) = +c(C5−C4). So the displayed identity holds only up to an overall sign with the σ's as defined. This does not affect any kernel. s1 uses {γ,γ}=2η and is correct. See F3.

**Literature (fetched; read from PDF text).**
- *Martin-Dussaud 1902.08439v3.* Eq. (297), "(K²−J²)|…⟩=(p²−k²+1)|…⟩, K·J|…⟩=pk|…⟩", is confirmed. Eq. (308), D(p₁,k₁)⊗D(p₂,k₂) = ∫_R dp ⊕_k D(p,k), is confirmed. The unitary-dual classification is in §7 ("Nota Bene", Gel'fand–Naimark). The title page confirms GRG 51, 110 (2019), DOI 10.1007/s10714-019-2583-5.
- *Fioresi–Yuncken 2403.17180v1.* Theorem 7.1 is "Plancherel Theorem for SL(2,C)", for the **classical** group (§7.1; the q-deformed version is Thm 7.4), with dm=½|μ+iλ|². The arXiv page shows no journal reference, so @misc is correct.
- *Manta–Steinacker 2502.02498v1.* The following are confirmed:
  - Eq. (1), with η=diag(−1,1,1,1,1,−1);
  - Eq. (11), ½M_{μν}M^{μν} = −1−r^{−2}X₄²;
  - Eq. (12), the second Casimir vanishes;
  - "minimal series … Hn … known as 'doubletons' or 'minireps' [15]";
  - "Like all doubleton irreps … remains irreducible as a representation of SO(4,1)";
  - H₀ := F_{N̂=−2}, i.e. N_a=N_b (Eq. 28).

  MS does not state, in what I read, that H_n for n>0 is the ladder representation of helicity n/2.
- *Todorov 1905.13009.* Confirmed: after (1.14)–(1.15), "For fixed (twice) helicity h … the ladder representation of U(2,2) is irreducible and remains irreducible when restricted to the Poincaré subgroup (see [MT] and Appendix A)", with p²=0 and p⁰≥0. The appendix gives a self-contained exposition. The arXiv journal reference is "Bulg. J. Phys. 46 (2019) 117-133", which matches the bib entry.
- *Mack–Todorov 1969.* Crossref confirms the title, JMP 10, 2078–2085, 1969, and the authors. The text is not independently verified, and it is cited "as stated in" Todorov2019, which is acceptable.
- No bib entry invents a journal reference.

**Insert hygiene.**
- No process language; refs and cites resolve; no new labels; no label or status change.
- Nothing claims a one-loop selection, a derived signature, a non-zero Pfaffian or a trivial B(H) kernel.
- The class premise (HS, smooth) and the B(H) ambiguity are both in the insert.

## Findings

- **F1. Severity: major.**
  - *Location:* insert, "Restriction to Spin(3,1)" and the final paragraph ("So, for every \(n\), …").
  - *Finding:* Route 1 needs H_n to be a ladder (massless) representation of U(2,2). The insert never states this step. The proposal itself lists the n>0 identification as not independently verified, and the sources I read do not establish it for n>0. For n=0, Route 2 is independent.
  - *Reason:* an unverified input is carried into an unconditional "for every n".
  - *Required action:* condition the n>0 claim explicitly (replacements R1 and R2).
- **F2. Severity: minor.**
  - *Location:* "Algebra", \(\vec J_{\mathrm L}=\tfrac12(\vec J\mp\mathrm i\vec K)\) together with \(4\vec J_{\mathrm L}^2=C_4\pm2\mathrm iP\).
  - *Finding:* the sign pairing is inconsistent, since (J∓iK)² = C4∓2iP.
  - *Required action:* replacement R3.
- **F3. Severity: minor.**
  - *Location:* first paragraph, "with \(\sigma^a=(1,\vec\sigma)\) and \(\bar\sigma^a=(1,-\vec\sigma)\)".
  - *Finding:* with these σ's, D₋D₊ = −c(C5−C4−2X) (check 9), so the stated identity has the wrong overall sign. The kernel is unaffected.
  - *Required action:* define D_± through the chiral blocks of Γ^a (replacement R4).
- **F4. Severity: minor.**
  - *Location:* closing sentence.
  - *Finding:* it is near-verbatim the 061 closing sentence on the immediately preceding paragraph ("Nothing here derives the family, the mass or the fermion content, so Assumption~\ref{ass:lorentzian} is not discharged, and Problem~E remains open and PROGRAMME-CONDITIONAL."). That repeats a closing status line on consecutive paragraphs.
  - *Required action:* replacement R5.
- **F5. Severity: minor.**
  - *Location:* Route 2, "so \(\mathcal H_0\) restricts to principal series with \(k=0\)".
  - *Finding:* this uses the classification of the unitary dual, which is uncited at that point.
  - *Required action:* replacement R6.
- **Process note (not a finding).** The denied command was a deletion (`rm -rf` of a scratchpad directory). It was not retried. The substitute (mkdir plus tar of tracked files into the session scratchpad) deletes nothing and writes nothing in the repository, so it does not circumvent the intent of the denial. I do not count it as working around a denial.
- **Prior claims.** None wrong. 061's "the square of Γ^a[T̄_a,·] is c(C5−C4^tot+3/2)" is consistent with s1's {Γ,Γ}=2η convention.

## Scope of what is established
- **Established identities:**
  - c⁻¹D₋D₊ = C5−C4−2X (with Clifford-normalised chiral blocks);
  - X²+X = J_L²;
  - 4J_L² = C4±2iP.
- **Established within the hypotheses:** a smooth HS kernel vector satisfies P=0 and 1+C4=(A+1)² ≥ 0. On HS(H_n)|Spin(3,1) ⊂ ∞λ this forces ψ=0.
- **Class of the positive result:**
  - (P-class) HS(H_n)⊗16;
  - (P-dom) Spin(4,1)-smooth vectors;
  - the 060 doubleton member, with no transverse factor K;
  - Definition (A), h₀ (9,1), supplied fermions, supplied γ>0, N→∞ first;
  - n=0 unconditionally within this class; n>0 conditional on H_n being a ladder representation.
- **Classification:** PROGRAMME-CONDITIONAL. It is not DERIVED, and E and D1 stay OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.
- **Milestone ruling: none, and no BREAKTHROUGH.**
  - The package does settle, within a class and in the favourable direction, the sub-question 061 ranked decisive.
  - But the 061 consequent (one-loop separation) still needs a defined, non-zero N=∞ Pfaffian. The family, h₀, γ and the fermions are supplied, so no E step is derived (not M1).
  - It is not a no-go (not M2). No merged claim is wrong (not M3). No label or structural change (not M4/M5).
  - It is a significant, coherent package, but not a milestone.
- **Open relaxations, ranked (useful for the IR / full-GR route):**
  1. Whether 0 lies in σ_cont(D_±), and a definition of the N=∞ Pfaffian. One option is finite-N truncations; another is a ζ/heat-kernel definition with Definition (A)'s iε extended to fermions. Either must also show the Pfaffian is non-zero against the compact members' exact zero. Decisive.
  2. Smallest singular values of truncated so(4,1) fermion operators against N.
  3. Products with K: Lorentzian D_W² is not positive, so ker D ≠ ker D_W ∩ ker D_K a priori.
  4. The n>0 ladder identification (closes F1 as a hypothesis).
  5. Complementary and discrete-series Spin(4,1) members. The principal-series case is sketched in the proposal only.
  6. The non-smooth closure kernel (a core statement for the Casimir polynomials).
  7. The bounded-operator kernel beyond 1⊗χ.

## Recommended disposition
Revise: apply R1 to R6 verbatim in round 2, then re-review. Integrate only after a plain ACCEPT and after the separate ordinal-60 full scan. Bib entries and anchor need no change; hashes will change with the revisions and must be re-reported.

## Corrected snippet
None of these needs new physics. R1 and R2 add an explicitly marked unverified hypothesis.

- **R1.** Replace:
  `as irreducible massless representations of fixed helicity~\cite{MackTodorov1969}, as stated in~\cite{Todorov2019}.`
  with:
  `as irreducible massless representations of fixed helicity~\cite{MackTodorov1969}, as stated in~\cite{Todorov2019}; for \(n>0\) this uses the identification of the doubleton \(\mathcal H_n\) with a ladder representation, which is taken from the literature on doubletons and not independently verified here.`
- **R2.** Replace:
  `So, for every \(n\), the fermion form of the doubleton member has no normalisable kernel in this class.`
  with:
  `So the fermion form of the doubleton member has no normalisable kernel in this class, for \(n=0\) and, given that identification, for every \(n\).`
- **R3.** Replace:
  `\(\vec J_{\mathrm L}=\tfrac12(\vec J\mp\mathrm i\vec K)\)`
  with:
  `\(\vec J_{\mathrm L}=\tfrac12(\vec J\pm\mathrm i\vec K)\)`
- **R4.** Replace:
  `the Weyl operators \(\mathcal D_+\psi=\sigma^a[\bar T_a,\psi]\) and \(\mathcal D_-\psi=\bar\sigma^a[\bar T_a,\psi]\), with \(\sigma^a=(1,\vec\sigma)\) and \(\bar\sigma^a=(1,-\vec\sigma)\), have trivial kernels.`
  with:
  `the Weyl operators \(\mathcal D_\pm\psi=\sigma_\pm^a[\bar T_a,\psi]\) have trivial kernels, where \(\sigma_\pm^a\) are the blocks of \(\Gamma^a\) between the two chiralities of \(\mathfrak{so}(3,1)\), so that \(\sigma_\mp^a\sigma_\pm^b+\sigma_\mp^b\sigma_\pm^a=2\eta^{ab}\).`
- **R5.** Replace:
  `Nothing here derives the family, \(h_0\), the mass or the fermion content, so Assumption~\ref{ass:lorentzian} is not discharged, and Problem~E remains open and PROGRAMME-CONDITIONAL.`
  with:
  `The family, \(h_0\), the mass and the fermion content remain supplied, so this removes one obstruction to the conditional route of the preceding paragraph without deriving the signature, and Problem~E stays open with Assumption~\ref{ass:lorentzian} retained.`
- **R6.** Replace:
  `so \(\mathcal H_0\) restricts to principal series with \(k=0\),`
  with:
  `so, by the classification of the unitary dual in~\cite{MartinDussaud2019}, \(\mathcal H_0\) restricts to principal series with \(k=0\),`

**Files:**
- `C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\proposal-r1.md`
- `C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\appH_insert.tex`
- `C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\bib_entries.bib`
- `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex` (anchor at L1622)

**Housekeeping.** I wrote the script re-run outputs to /tmp and the fetched PDFs and their text to the session scratchpad, all outside the repository. Nothing in the repository was modified.

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1
