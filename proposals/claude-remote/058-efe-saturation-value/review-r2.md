VERDICT: ACCEPT | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/0

## Verdict
r2 applies both required r1 corrections word for word and adopts the optional "comparable to" wording, and nothing else in the edit text changed. The core correction verified in r1 therefore stands: ν_√(g_gal) = 1.348, not 1.1; the eq:nu-efe bracket sign is fixed to match the 1D QUMOND law (FM12 Eq. 60); and the false dependent claims are removed.

## Source reading
- **Mode.** Digest + targeted reads + the ordinal-55 full-scan record. I did not do a new full scan.
- **Digest.** `make_digest.py --check` printed `DIGEST CURRENT` at HEAD e24d458. The only dirty chapter file is appH (055–057).
- **Changes since r1.** Two commits since 13647fa, d24f435 (the review) and e24d458 (r2). `git diff --stat 13647fa e24d458 -- chapters/ bib/` is empty.
- **Target files.** `git diff --quiet HEAD` is clean for all four. They are byte-identical to the r1 baselines, and therefore to the versions covered by the ordinal-55 scan.
- **Passages.** The passages read in full in r1 (ch13 L190–319, ch16 L95–361, appE L20–69 and L190–309, all of appI, appH sec:status-H, ch17 Problem H, ch18 L38–56) are unchanged, so I did not re-read them.
- **Scan ruling, CLAUDE.md 3(c).** Same as r1: satisfied in substance, not by a new full scan in this session. The basis is the ordinal-55 gatekeeper full scan of all 30 files at f2d005f, the unchanged hashes of the target files, my reading of the only later chapter change (the appH 057 insert, which has no EFE content), and the r1 dependency grep over all chapter files. Since r1 no chapter file has changed and no edited passage reaches new text, the sweep still holds.

## Claim under review
- **Claim.** Unchanged from r1. The package corrects "ν_√(g_gal) ≈ 1.1" to ≈1.35 at four sites, corrects the eq:nu-efe bracket sign, and corrects the dependent compatibility and "not explained" claims (ch16, appE, appI). It also clarifies appI's 20% as a velocity excess and adds a sentence on the anisotropy of the saturated boost.
- **Target.** Problem H (appH L2788–2790): "Status: OPEN. Priority: OPTIONAL within the phenomenological scope. Completion: PROGRAMME-CONDITIONAL." ch17 L521: "OPEN; OPTIONAL research within the theory." Problem H is not on the critical path, and no label is changed.

## Checks performed
- **Edit diffs, r2 against r1** (`diff *_edits.r1.txt *_edits.txt`):
  - **ch13.** One line differs: "The saturated boost" became "The saturated boost~\eqref{eq:efe-sat}". This is F2 exactly as I specified it. Edit 1 (the sign fix) is unchanged.
  - **ch16.** One line differs: "is of the size of that" became "is comparable to that" (F3).
  - **appE.** Edit 1 NEW lines 5–7 now match the r1 Corrected snippet character for character (F1), including the explicit condition "If eq:appE-RAR holds at the Sun". Edit 2 has the single F3 wording change.
  - **appI.** No difference from r1.
- **proposal-r2.md against r1.** The only additions are the change log, decision D7, the updated hashes, the r2 scratch-build record, and the `eq:efe-sat` label in the list of labels used. No new mathematical claim was added.
- **make_r2.py.** It writes only `proposal-r2.md` inside the proposal folder.
- **apply_check.py, re-run in report mode** (output in `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\apply_r2.txt`):
  - The output is identical to apply_check.txt and ends with ALL CHECKS PASS.
  - Every OLD string occurs exactly once and every NEW string zero times in the baseline.
  - The results match the claimed values: ch13 17259 B, 66afb3c5…4eda; ch16 16832 B, 49529f71…c565; appE 13921 B, 854cc10a…6dd8; appI 4154 B, b91dc5e4…041e.
  - The CRLF counts are 409, 362, 315 and 87, with no bare LF.
  - `git status` is unchanged afterwards.
- **Re-verification of the r1 findings:**
  - **F1, resolved.** The new appE text matches ass:efe (g_ext is baryonic) and states the RAR-at-the-Sun condition. Its numbers are those already verified in r1: g_N = 1.474e-10, giving ν = 1.49.
  - **F2, resolved.** eq:efe-sat is defined exactly once (ch13 L240). The anisotropy sentence now names the limit it qualifies, so it no longer reads as an unqualified isotropic statement.
  - **F3, adopted.** "Comparable to" together with "would be a coefficient-level agreement … not a derivation" makes no claim of a match at the limit, and it does not turn Problem H into a success.
  - **F4.** Pre-existing hard-coded references and the unsourced g_gal inputs are out of scope and left for a later bookkeeping item, as recorded.
- **Central numbers.** Unchanged from r1, which I re-derived by hand: ν_√(1.8333) = 1.348, L_e = −0.236, along-field values 1.03 (corrected form) and 1.67 (old sign), 3D QUMOND transverse value 1.19, velocity excess 0.16–0.22. In r1 I checked FM12 Eqs. (60) and (63)–(64) against the arXiv text, and the Chae and Banik abstracts; none of that wording has changed.
- **Not independently verified.** I did not run a LaTeX build, because that would write in the repository. The researcher reports a fresh r2 scratch build: 365 pages, 0 undefined or multiply-defined references, both citations resolved. The integrator's `build_check.py` must confirm this.
- **LaTeX.** The `\eqref`, `\ref` and `\cite` keys all exist, there is no process language, and the line endings are CRLF.

## Findings
None blocking, major or minor in r2. The r1 findings F1 and F2 are resolved and F3 is adopted. F4 is out of scope by design.

## Scope of what is established
The scope is the same as in r1.
- **Established:**
  - ν_√(2.2e-10) = 1.348, and "1.1" is false under every reading the manuscript supports.
  - The eq:nu-efe bracket sign was reversed relative to the 1D QUMOND law, and the correction is established.
  - The anisotropy values (corrected algebraic form, ν_e transverse and ν_e(1+L_e) ≈ 1.03 along; 3D QUMOND, ν_e along and ν_e(1+L_e/2) ≈ 1.19 transverse) and the 20% velocity-excess reading are established.
- **Conditional:**
  - The baryonic g_ext ≈ 1.5e-10, which requires the RAR to hold at the Sun.
  - The statement that ass:efe is disfavoured by the controlled Gaia analyses, which rests on premises (i)–(vi) of the proposal.
- **Problem H.** It remains OPEN, OPTIONAL and PROGRAMME-CONDITIONAL. This package corrects the record and is not progress on H.
- **Open avenues, ranked as in r1:**
  1. An external-field modular response, U_ent with an external Newtonian source.
  2. An orbit-averaged 3D boost for the corrected eq:nu-efe or full QUMOND with ν_√.
  3. A cited value of g_ext at the Sun.

## Recommended disposition
Integrate as-is using the r2 edit files (`ch13_edits.txt`, `ch16_edits.txt`, `appE_edits.txt`, `appI_edits.txt` in `C:\Users\redgi\Projects\namcg-lab\proposals\058-efe-saturation-value\`). Run `scripts/build_check.py` after integrating.

Milestone M3 applies because an error in merged text was found and corrected: a false numerical value with false implications in the falsifier list, and a sign error inside an assumption. The loop stops for the author under the M3 rule. This is not a breakthrough.

## Corrected snippet
None needed.

VERDICT: ACCEPT | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/0
