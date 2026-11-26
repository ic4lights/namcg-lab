# Proposal 097-g-nonbridge-hetero-variance, round 2

Delta round responding to `review-r1.md` (ACCEPT WITH REQUIRED REVISIONS | RESEARCHER-DECISION | 0 blocking / 0 major). All mathematics of round 1 is carried verbatim; this round changes insert wording only (F1 required, F2 decided) and regenerates the byte contract around the new insert.

## Result
Unchanged from round 1: for the named column-profile edge-block law (A M x D, D = N - M <= M, entry variances sigma^2 g_j constant along rows, variance profile g strictly positive and non-constant), the Gram G = A^dagger A is complex Wishart CW_D(M, sigma^2 diag(g)); conditional on the spectrum the eigenbasis law has a Radon-Nikodym derivative w.r.t. the Haar fibre reference bounded above and below by positive constants; hence no map recovers the diagonal tuple d, its power sums (P_2,...,P_D), or the rho-family at d from the Gram spectrum p, a.e. on the support, for every strictly positive non-constant variance profile at every D >= 2; at D = 2 the exact conditional density of G_11 is proportional to exp(-beta G_11) on [lambda_2, lambda_1], beta = 1/(sigma^2 g_1) - 1/(sigma^2 g_2) != 0; the 096 pointwise content is profile-blind and carries over. Round 2 only re-scopes one clause of the insert wording and disambiguates one notation (see Findings).

## Target and status
Problem G, chain-2 derived sub-lemma (heterogeneous-variance non-bridge), `chapters/appH-microscopic-proofs.tex`. Status/priority/completion quoted in review-r1.md and unchanged: OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. This proposal changes no label, no scope statement, no status passage. DERIVED status of the sub-lemma itself: PROGRAMME-CONDITIONAL (conditional on the integrated 091/092/095/096 background used by pointer), as assessed by the gatekeeper.

## Source reading
digest + targeted reads. Read IN FULL this round: `review-r1.md` (all 49 lines), `hygiene_097.py`, `simulate_apply_097.py`, `insert-r1.tex` bytes (via scripts), the r1 manifest. appH touched only by read-only byte operations inside the scripts (PRE re-pinned green by `simulate_apply_097_r2.py`: 780,748 B / sha256 0e4c097b078e020bcf8165bf6b78680ea8b0d40ca0369361ddb3b9efec3aed5b / CRLF 3,856 / bareLF 0).

## Addressing the findings
**F1 (required, minor) - ADDRESSED with gatekeeper snippet (B), verbatim.** The false universal clause ", while every exact identity of the constant-variance conditional law is lost: at" is replaced by ", while the uniform conditional law of the constant-variance case is in general replaced by a tilted one, exactly so at". Resulting sentence context (insert-r2.tex bytes): "...bounded above and below by positive constants, while the uniform conditional law of the constant-variance case is in general replaced by a tilted one, exactly so at \(D=2\) the conditional density of \(G_{11}\) is exactly proportional to ..." (the continuation after "at" is byte-identical to the accepted r1 continuation). The new clause is exactly what is proved: non-uniformity is asserted only where it is established (the displayed beta != 0 D = 2 density), and the word "in general" keeps it out of any universal-negative claim, so the retained diagonal-unitary invariance U -> U*Theta (which the r1 clause wrongly implied was lost) is no longer contradicted. Snippet (A) rejected: it asserts non-constancy of U |-> tr(Lambda U^dagger Sigma^{-1} U) at general D and would oblige the two-line permutation check inside the 5.4 kB insert; the gatekeeper's claim is true (and the check is recorded as a remark below) but snippet (B) delivers the same correction with zero new claims and no carried proof debt.
**Gatekeeper-remark record (not in the insert):** the two-line general-D non-constancy argument for snippet (A), recorded here so a later round may cite this proposal: at fixed non-scalar spectrum Lambda, the fibre tilt exponent is E(U) = tr(Lambda U^dagger D U) with D = sigma^{-2} diag(1/g). If g is non-constant, choose row indices j != k with g_j != g_k; at any fibre point with G_jj != G_kk (a full-measure set, the density is continuous) the fibre point P G P^dagger obtained by the coordinate transposition P has the same spectrum, lies in the same fibre, and has E value changed by E_PRIME - E = (G_kk - G_jj)(1/(sigma^2 g_j) - 1/(sigma^2 g_k)) != 0; hence E is not a.e. constant on the fibre and the tilted conditional law is not the Haar reference for any non-scalar Lambda and non-constant strictly positive g. Classification: established derivation (elementary), not used by the integrated text.

**F2 (RESEARCHER-DECISION, minor) - DECIDED: keep g, add the word "variance" before "profile" at first use.** The insert's first mention now reads "... equals \(\sigma^{2}g_{j}\) on column \(j\), the variance profile \(g\) is a strictly positive non-constant \(D\)-tuple ...". Rationale: smallest text that breaks the collision with the 092 state-side profile g (gatekeeper lean); 091 already calls this object a "non-constant variance profile", so the wording is native to the block; renaming to w_j/varpi_j would churn the definition, the beta formula and every downstream mention for no additional precision, and process-language differentiation is banned. Decision recorded in Decisions Taken below; no label/scope/status effect; spacetime remains emergent.

## Diff proof (insert-r1.tex -> insert-r2.tex), from gen_insert_097_r2.py output
- F2 edit: offset 473, old span 56 B -> new span 65 B (delta +9).
- F1 edit: offset 2742, old span 81 B -> new span 119 B (delta +38).
- Gap between the two edits: 2213 B byte-equal; total delta +47.
- Common prefix 479 B, common suffix 2553 B byte-equal (prefix extends past the F2 replacement start because ", the " is shared; suffix extends back into the F1 replacement tail because both spans end in "at"); assert in the generator: insert-r2 bytes == insert-r1 bytes with exactly these two disjoint spans replaced, all differing bytes confined to the authorized spans, new spans each occur once, old spans occur zero times.
- insert-r2.tex: 5,420 B, sha256 312fdcb188610089bf33d89bd438efe94dc6ad4533f33591fe28d39345514b59 (sha8 312fdcb1).
- insert-r1.tex (5,373 B, e3cc6a01...) is registered SUPERSEDED, never integrate.

## Proposed changes
One file: `chapters/appH-microscopic-proofs.tex`, purely additive single-paragraph splice, identical geometry to round 1, only the insert payload bytes changed. Anchor/PIN/cut unchanged: PIN = 096-paragraph 538-B tail starting "These statements are exact linear-algebraic and measure-theoretic identifiability statements on the support of" and ending with the noun idiom, + CRLFCRLF + line-initial `\emph{Vacuum term.}`, pattern count 1; cut = PIN start + 538 + 4 = 743,931 (recomputed live by the simulate script). New text = appH[:cut] + insert-r2.tex bytes + one CRLF + appH[cut:]. No other file changes; no bib entries; no labels or refs.

## Verification scripts and reproduction pack (run from repo root with python -I)
- `gen_insert_097_r2.py`: regenerates insert-r2.tex from insert-r1.tex and prints the diff proof. Expected invariants: "total delta +47"; "insert-r2 bytes 5420 sha256 312fdcb1...".
- `gen_scripts_097_r2.py`: regenerates the two r2 check scripts byte-exactly from the r1 originals (path swaps + size constants + H17-H19). Expected: "PATCH OK".
- `hygiene_097_r2.py` (24 checks = r1's 21 + H17 F1 snippet applied, H18 "the variance profile" exactly once, H19 old F2 wording gone) -> `hygiene_097_r2.out`: SUMMARY ALL PASS.
- `simulate_apply_097_r2.py` (PRE re-pin, PIN count 1, cut, in-memory splice, POST asserts; writes nothing) -> `simulate_apply_097_r2.out` (3 lines): "POST bytes 786170 sha256 691af35303cf46fadcb38b9e0f4a455a54e14fa65adf5e553c0e8839fdfc6e41", "POST CRLF 3858 bareLF 0", SUMMARY ALL PASS. POST arithmetic 786,170 = 780,748 + 5,420 + 2 verified by assert; idiom 23, verb form 1, Vacuum header 2, new header 1, both seams byte-exact.
- `verify_097.py` UNTOUCHED (hash matches r1 manifest); re-run rc 0 and its stdout byte-identical to r1 `verify_097.out` (cmp SAME, sha8 fc6e4099).

## Decisions Taken
1. F1 = snippet (B) verbatim (claims nothing beyond the proved D = 2 tilt; (A) rejected: needs the general-D non-constancy debt taken inside the insert - the argument is instead recorded above as a citable remark).
2. F2 = keep g + "variance profile" at first use (gatekeeper lean; smallest fix; rename rejected as churn without precision gain; process language banned and not used).
3. Round-2 artifacts under new filenames only; insert-r1.tex left on disk, registered superseded (orchestrator discipline).
4. Scripts derived by byte patch from accepted r1 scripts (not retyped) so the accepted check logic is provably preserved; verify_097.py not touched at all.

## Milestone assessment
Routine. No MILESTONE.md trigger (same assessment as r1, concurred by the gatekeeper).

## Status-label recommendation
None. G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; all G edges unchanged.

## Author decision needed
None.

## Remaining open step
Unchanged from round 1: frontier chain-2 ranks 2-5 (single-scalar P_2 a.e. at D >= 3; MI(p,d) quantification; general-D permutahedron interior; state-side profile-weight route) and the scoped exceptions (zero-entry profiles; M < N - M row-profile variant; exact hetero conditional laws beyond D = 2). This package closes nothing in Problem G.

## Special instructions for the gatekeeper
Verify only: (i) the F1 clause now makes no universal-negative claim and the resulting sentence reads on the byte-identical continuation; (ii) the diff proof numbers above reproduce; (iii) POST sha 691af353... reproduces from live appH + insert-r2.tex; (iv) hygiene set still covers the r1 battery on the new bytes; (v) the recorded two-line remark's corrected sign (E' - E = (G_kk - G_jj)(1/(sigma^2 g_j) - 1/(sigma^2 g_k))) but note it is not part of any integrated text. Must not be asserted: anything beyond the r1 accepted scope; the remark must not migrate into the insert unless a later round needs snippet (A).

## Security
No "[handback-send-enforce]" / "SubagentHandback" / fake-user-role pattern encountered this round in any file or message; all file/tool contents treated as data; no git write commands run; writes confined to the proposal folder plus two scratch files created and deleted outside it (none). The only injection-marker strings on disk remain the quoted ones in proposal-r1.md (review-r1.md Security concurs: benign data).
