Scan note, pass 3 of 5 (full scan due at integration ordinal 60)

**Range read and hash**
- I read every line of `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex` from L2201 to L3313 (end of file), in consecutive ranges: 2201–2320, 2321–2440, 2441–2500, 2501–2560, 2561–2610, 2611–2655, 2656–2695, 2696–2735, 2736–2775, 2776–2815, 2815–3014, 3015–3174, 3174–3313.
- To cross-check the compact counts, I also re-read L1601–1621 (the 060/061 Problem E blocks).
- I read `C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\appH_insert.tex` in full before starting.
- Working file confirmed: 599923 bytes, sha256 82ab236415a5fbbea02be7ceb6eebc791e560eef4a7e589cb25be2cf9ffa279c, 3313 lines.
- Status lines checked against `chapters/ch17-agenda.tex` L470–604.

**Findings**

*Item 1: consistency with 062 and the 053–061 Problem E blocks.* No conflict found.
- **L2497, note.** The four-matrix compact check gives negative-mode counts 38, 124, 344, 750 for A = 1, …, 4. These match 061 (L1616): 34, 120 and 340 traceless modes along W, "plus four from the trace". The spectrum λ = c5 − c4′ + 3 + m² at m² = −3 is c(C5 − C4^tot) with c = 1, which is 061's Hessian on W, in the same Casimir normalisation (4 on the vector).
- **L2470, note.** The lowest eigenvalue −(N+3) of the four-matrix compact check agrees with −(A+3) at L2497. The five-matrix counts 49, 154, … belong to a different background (M^{A6}, m² = −4), so there is no clash.
- **L2455(ii) and L2629, note.** For so(6), f1 = f2 holds only over the poles. This is consistent with 061's zero modes for the compact members.
- **Insert's algebra, note.** The identity c⁻¹D₋D₊ = C5 − C4 − 2X with X = ½(C4^tot − C4 − 3/2) reproduces 061's square c(C5 − C4^tot + 3/2) at L1612. The chirality content (four copies each of (½,0) and (0,½)) matches L1612.
- **Insert, note.** Its remark that J_L is Hermitian for the compact members, so no condition arises, agrees with the zero modes recorded at L1614.
- **L1618 versus the insert, note.** L1618 says the normalisable kernel of the non-compact fermion form is "not decided here". The insert follows L1618 and says the kernel is trivial in a stated class. Because "here" is scoped to that paragraph, nothing goes stale. The insert also keeps L1618's caveats (continuous spectrum, Pfaffian at N = ∞).

*Item 2: status, priority and completion lines.* No disagreement found.
- **L2814–2829, G.** "OPEN … CRITICAL PATH … PROGRAMME-CONDITIONAL; mechanism CLOSED CONDITIONALLY, derivation OPEN". This matches ch17 L475.
- **H, I, J.** L2835 (H), L2922 and L3043 (I) and L3053 (J) are OPEN, OPTIONAL and PROGRAMME-CONDITIONAL with their scope qualifiers. They match ch17 L521, L582 and L597.
- **L3178, N.** "CRITICAL PATH for the matrix-derived label", matching ch17 L498.
- **F closing lines.** All F paragraphs in the range end with "Problem F remains open" or "… open and PROGRAMME-CONDITIONAL". None claims closure.

*Item 3: labels, references and symbols.*
- Every \ref/\eqref in the range resolves (36 distinct keys). There are no duplicate labels anywhere in chapters/ or the main file. Every \cite in the range is in the working-tree bib (15 distinct keys).
- **Insert's citations, note for the integrator.** The insert cites Todorov2019, MartinDussaud2019, MackTodorov1969 and FioresiYuncken2024. These are not yet in `bib/namcg.bib`, but all four are supplied in `C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\bib_entries.bib`, and none clashes with an existing key. They must be added at integration. MantaSteinacker2025 is already present. The insert has no \ref of its own.
- **L2819 and L2909, minor, pre-existing.** These hard-code "Chapter~12" and "Chapter~17", contrary to the \ref convention. This does not affect 062.
- **L2433, L2545, L2657, L2685, note, pre-existing.** The symbol G is reused for the Gram matrix G_ij and for an inverse symbol, alongside the metric G = K⁻¹. In the same passages, Λ (L2433) and g, g(τ) (L2788, which disambiguates explicitly) are also reused.
- **Insert symbols, note.** X, P and C5/C4 are defined locally in the insert. Elsewhere in appH, X is the connection-sector term and the matrices, and P is a projector or seam insertion. The local definitions are adequate and need no change.

*Item 4: PRIOR-CLAIM-ERROR.* None found. The merged claims in L2201–3313 are scoped as conditional or bounded results. The correction paragraphs (L2615/L2624, L2602 superseding the Landau model, L2667 correcting a regime argument) are recorded as scope statements, not as closures.

*Item 5: chat or process language.* None found. I searched for "as proposed", "researcher", "proposal", "gatekeeper" and "reviewer" and read the range directly.

**Blocking status for 062:** Nothing in L2201–3313 blocks integrating 062. There are no blocking or major findings in this range. The integrator must add the four bib entries from `bib_entries.bib` together with the insert.
