VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All three r1 findings are applied as required. The LaTeX block is otherwise unchanged and equals `appH_insert.tex`. The anchor is unique, the bib is unchanged, and no labels change. The package is accepted for integration at ordinal 22.

## Source reading
Digest + targeted reads. `chapters/` and `bib/` are clean (`git status` empty), so the digest-staleness rule 3(d) is not triggered. CLAUDE.md 3(c) does not apply: the block changes no definition, assumption, scope or status passage. 3(a) does not apply (22 is not a multiple of 5). My r1 review read Appendix H Problem B in full. This round I re-read the 021 "Outcome" paragraph (line 204) and the surrounding anchor. I ignored `proposals/025-*`.

## Claim under review
The claim is unchanged from r1. The package classifies c_A = 2, 1, 0 at (n_D, N_s) = (2, 6) against published contact-term treatments. It also states what a Lewkowycz–Maldacena (LM) argument implies for G_A versus G_T in the Theta-only Poisson-limit class.

Appendix H, Problem B, quoted verbatim (from r1): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived." Problem A is touched only as a state/replica datum. No label change is proposed.

## Checks performed
I diffed proposal r2 against r1 (ignoring CR) and checked each requested point.

- **Finding 1 (LM paragraph): applied, in both the block and the body.**
  - The block's "Dynamical metric" paragraph now says that R_G^(1) = −2 Box δln ρ excludes the cone-type configuration at first order.
  - It says the only first-order regularisation is the smooth family, with far field ρ ∝ r^{n−1}, which differs from the cone's.
  - It says the LM construction and the vanishing of its first bracket are not reproduced for it.
  - It gives c_A^sm = −c_R/2 as the coefficient of "the smooth replica". This is my corrected snippet, with the sentence after it unchanged. The wording "LM's construction is not available" is carried by the Result and the body, and the block says "not reproduced".
  - The body (Result item 5, Research 5(c) and 5(e), and the claim-classification table) was updated consistently. 5(e) now says S = A/4G_ind holds as a definition of G_ind and does not test G_A = G_T. The classification row marks the first-bracket statement as unresolved.
- **Finding 2: applied.**
  - The block reads "absent from the bulk-mode entanglement entropy".
  - It adds "Herzog and Nishioka state that their boundary term contributes oppositely to the contact term (Eq. (5.20) of HerzogNishioka2016)". I verified Eq. (5.20) and its accompanying sentence in r1.
  - The r2 body bullet still says "Kabat's entanglement value for the vector part" without "bulk-mode". That is body text only, outside the LaTeX, and is harmless.
- **Finding 3: applied.** The last sentence now reads "in the relation, in form, S_BH = S_ent − Q of Eq. (322) …, where Q is here the bosonic contact (N_s+2)/4 of the smooth reading and S_BH is built from the induced action". This matches the arithmetic I verified in r1.
- **Nothing else changed in the LaTeX.** `git diff ee86c54 HEAD -- appH_insert.tex` shows exactly 2 changed lines, the Connection-sector and Dynamical-metric paragraphs. The diff between `proposal-r1.md` and `proposal-r2.md` shows body edits only in the places above, plus a changelog and a re-ranked "Remaining open step".
- **`appH_insert.tex` equals the r2 block.** I extracted lines 120–133 of the proposal (inside the latex fence) and compared them with the file with CRs stripped. The diff is empty (SAME).
- **Anchor.** The sentence "or the next order of either side, and give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open." occurs exactly once, at `chapters/appH-microscopic-proofs.tex` line 204 (grep count 1). It ends the 021 "Outcome" paragraph, and line 206 is `\section{Problem C: conformal mode and Cassini}`. The insert has no `\label` (grep count 0), so no labels change and there are no duplicates.
- **Bib.** `git diff ee86c54 HEAD --stat -- bib_entries.bib` is empty, so the file is unchanged since r1. BibTeX record: VERIFIED (HerzogNishioka2016; JHEP 2016(12) 138, confirmed via Crossref in r1). BibTeX record: VERIFIED (LewkowyczMaldacena2013; JHEP 2013(8) 90, confirmed via Crossref in r1). Neither key is present in `bib/namcg.bib`, and the cited keys Solodukhin2011, Kabat1995 and DonnellyWall2016 exist.
- **Mathematics.** The r1 checks stand: counterterm bookkeeping, s-wave branches, contents algebra and the three scripts. Nothing mathematical changed in r2, only scoping.
- **Not re-run.** I did not recompile; the researcher reports a scratch compile with 0 undefined or multiply-defined references. The integrator must still run `build_check.py` and preserve CRLF.

## Findings
none

## Scope of what is established
Accepted for integration at ordinal 22, exactly this:
- the r2 block in `proposals/024-replica-classification/appH_insert.tex` (two paragraphs of classification text plus the bib entries HerzogNishioka2016 and LewkowyczMaldacena2013);
- inserted at Appendix H immediately after the sentence ending "…Problems~B, C, D, F and~G remain open." at line 204, before `\section{Problem C…}`.

**Established inside the 021 class** (Poisson limit, Euclidean section, α = 1, Λ² term, one loop, two replicas):
- The contact and the Herzog–Nishioka (H–N) counterterm are equal and opposite.
- The s-wave branch values are 1/6 ∓ 1/4 on the regular branch.
- c_A^sm = −c_R/2.
- c_A^sm − c_T = (14 − N_s − 4n_D)/4, vanishing only on N_s + 4n_D = 14.
- The two vanishing lines meet only at (6, 2).

**Bounded no-go.** G_A = G_T is not implied by the generalised-entropy structure in the Theta-only Poisson-limit class at Λ² order, one loop, α = 1. At (6, 2) the equality c_A^sm = 0 = c_T carries no information on G.

**Classification only (analogy):** the values 2, 0 and 1 are matched by form to the contact-free, delta-potential and imported vector-contact cases. The vector contact is an input.

**Not established:**
- the replica or state the matrix model selects;
- the LM first bracket and the tensor-block stationarity;
- covariance of the induced action in Θ;
- edge modes and tip domains;
- the next order.

Classification: PROGRAMME-CONDITIONAL. B and A stay OPEN. No label change and no `LABEL-CHANGE-PROPOSED`. Spacetime stays emergent. This is a bounded no-go and classification, so there is no `BREAKTHROUGH`.

**Open avenues, ranked** (as in the proposal, which matches my r1 ranking):
1. Next order (Λ⁰, log) on a curved J = 0 leaf at the SUSY content, where the Λ² term vanishes. This relaxes the order.
2. A covariant completion of the induced action, identifying the torsion invariants behind c_A^sm ≠ c_T. This relaxes the Theta-only representative.
3. Stationarity at the SUSY point (the LM first bracket for the smooth family).
4. Tip domains and symplectic/fermion edge modes.
5. A state-dependent frame κ.
6. Non-quasi-free or non-rotational states.
7. Contents on N_s + 4n_D = 14 (a non-vacuity check).

## Recommended disposition
Integrate as-is: the r2 block, the two bib entries, and the bib entries appended to `bib/namcg.bib`. Then run `python scripts/build_check.py` and preserve CRLF. Per repository convention, the digest should be refreshed after integration.

## Corrected snippet
Not needed.
