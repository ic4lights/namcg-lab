# Review r2 (confirmation pass) - proposal 109-cd1-bilocal-frame-operator
# Reviewer: gatekeeper (fresh instance, 2026-11-21). Subject: proposal-r2.md
# (sha1 251e5196a01c8b6762a0e1c49a41aabf60b44764). Verdict verbatim.

CONFIRM VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

Step 1 — PASS. sha1s: r1 `4467405488dda142235c44c8e4afd4af6ead1eac`, r2 `251e5196a01c8b6762a0e1c49a41aabf60b44764`, diff `7c4a69f0e6f830184f4ccdd6259a0878268faac9` — all match pins.

Step 2 — PASS. `patch --fuzz=0 proposal-r1.md &lt; r1_to_r2.diff` applied with exact context and produced sha1 `251e5196…` = r2 byte-for-byte. This proves the diff is the complete r1→r2 transformation with no other hunks. Contents are exactly findings 1–4: (1) `$\mathcal G^{+}_{\mu\nu}$` → `$g^{+}_{\mu\nu}$`; (2) determinant sentence now reads, as joined text, verbatim the review L56 replacement ("…differs from the squared frame determinant only by the constant factor $\det\eta$, and the composite determines the frame only modulo the right action of the orthogonal group of $g^{+}$,"); (3) all four `\operatorname{Hom}_{G}` → `\operatorname{Hom}_{\mathrm{SO}(3,1)}` (dΩ pair line + two W⊗W lines); (4) L375 clause "and small compared with the scale on which $w_{\rho}$ varies," appended per review L52. Det sentence keeps r1's wrap positions (compared joined, as instructed). Advisories 5–6 correctly not applied. Note: prompt said the diff is 27 lines; `wc -l` gives 33 — immaterial, since the pinned sha1 plus exact roundtrip establish completeness.

Step 3 — PASS. `check_reps.py` output sha1 `a71bc3da9872fa509a50b6a61539c77ce325a70d` = `check_reps.out`; `check_connectors.py` output sha1 `5664fd85f65001bd0b5d5f57d983ecd78e9e79cc` = `check_connectors.out`; `check_bilocal.py` exits 0; `gk_indep_reps.py` ends `ALL CHECKS PASS`. Independent read of `gk_indep_reps.py` L121-122,145: the (h) check literally evaluates `(drep(J1), hom(J1,W2), hom(V,W2))` with `W2 = tprod(V,V)` and `J1 = plus(ADJ, V, W)`, so the tuple is (dim J1, Hom(J1,W2), Hom(V,W2)) as specified; 34 = 6+4+24 is arithmetically consistent with ADJ⊕V⊕W and the enumeration yields it (not just trusted from the pin).

Step 4 — PASS. proposal-r2.md L370-412: zero occurrences of `Hom}_{G}` and of `\mathcal G^{` in the file; L375 expansion-domain clause present; L399/401/402 use `\operatorname{Hom}_{\mathrm{SO}(3,1)}`; L405-407 non-degeneracy sentence with `$\det\eta$` factor and `$g^{+}_{\mu\nu}$`. Remaining `\mathcal G_{\mu\nu}` (no superscript, L390) is the bilocal composite defined immediately above (untouched by the diff; not flagged in r1). Undefined symbols from findings 1/3 are gone from manuscript text.

Step 5 — PASS. Diff hunks contain no status/priority/completion labels and no bib changes.

Residual caveats: (a) anchor re-verification against the live `chapters/appH-microscopic-proofs.tex` (Problem C, before `\paragraph{Missing step.}`) and CRLF preservation remain the integrator's serialization duty, per standing protocol — the diff does not touch the anchor region; (b) the r1 acceptance scope stands unchanged: this is a correctly scoped conditional candidate input to C Missing-step (i) / D1 frame half; nothing becomes DERIVED and no labels change on integration.

Recommendation: integrate the drafted LaTeX paragraph of proposal-r2.md as the single appH Problem-C paragraph before `\paragraph{Missing step.}`; no further revision needed.
