# Review r2 - item 129 (gatekeeper, confirmation pass)

Source: gatekeeper agent (same instance as r1), 2026-11-26. Saved verbatim by the orchestrator.

---

VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
Round-2 confirmation passes on every item: the payload changed by exactly the three mandated finding strings and nothing else (r1 bytes exactly recovered by inverting the edit-script strings), anchors and POST arithmetic re-verified independently, and the cert reproduces.

## Confirmation log
1. **Byte-diff.** Live `payload-F.tex`: 3,147 B, sha256[:12] `87a7c2568f72`, sha1[:12] `0cf326eb3457` (claims match), 3 CRLF / 0 bare LF / ASCII / ends CRLF. Inverting the three new strings from `edit_payload_r2_129.py` yields exactly 3,113 B, sha256[:12] `bcace605a53b`, sha1[:12] `af564f3bf0b9` - **matches the claimed r1 bytes**, so r2 = r1 + exactly three edits. Opcode diff r1-recon vs r2 shows exactly three contiguous changed regions (bytes 141-227 = the finding-3 clause incl. `supplied there as`->`specialised there to` and `+ on the flux directions`; byte 997 = `1.5\times` insertion; byte 2451 = deleted `5` of `5.345`). **No fourth region.** (My first two inversion attempts failed on my own heredoc escaping, not on the file - resolved by using the edit script's raw-byte strings.)
2. **Anchors / POST.** Live appH unchanged at 883,075 B; `On this evidence the sign of \(\hat U\) depends on \(K\).` count 1 (L3194), `\emph{Scale dependence.}` count 1 (L3196). POST independently recomputed: 883,075 + 3,147 + 2 = **886,224 B** = claim.
3. **Cert.** `cert_129.py` re-run with `python -I`: `CERT129 PASS (exit 0, undefined refs/citations = 0)`; pdflatex exit 0/0, pages = 450, multiply-defined = 0; spliced post 886,224 B.
4. **Finding closure.** F1: `\beta_K\simeq2\cdot5.34/10.68\simeq1.000` exactly once; `5.345` zero times in payload. F2: `below \(1.5\times10^{-13}\)` exactly once (bound now covers the checked 1.421e-13 point at N=4). F3: `specialised there to \(C_{ijk}=\mathrm i c_3\epsilon_{ijk}/g^2\) on the flux directions` once; `supplied there as` zero times. F4/F5 correctly untouched: `spinor and ghost parts being unchanged` once, byte-identical to r1 (survives inversion).
5. **Residue.** `5.345` absent from `payload-F.tex`, all four verify scripts and `proposal-r1.md` (L41 note now "tree-slope size 5.34"); remaining occurrences are only legitimate provenance/control sites: `check_payload_129.py` (guard list + re-injection control), `edit_payload_r2_129.py` (old string), `journal-129.md`/`proposal-r2.md` (change record), `review-r1.md` (my finding text).
6. **Pack re-run.** `CHK129 PASS` with **4/4 positive controls fired** (bare-LF, 5.345 re-injection, non-ASCII, stripped trailing CRLF - guards proven non-vacuous per the generator-join-guard lesson); `HESSIAN_129 PASS`, `TREECURVE_129 PASS`, `EXAMPLE_129 PASS`, `WEIGHTS_129 PASS` unchanged. No unexplained change => no re-derivation performed (r1 derivations stand; nothing mathematical moved).

## Integrate-ready statement
- Payload: `proposals/129-rc-held-recheck/payload-F.tex`, **3,147 B**, sha256[:12] `87a7c2568f72`, sha1[:12] `0cf326eb3457`, pure CRLF, ASCII, trailing CRLF.
- Insert between the two unique anchors in `chapters/appH-microscopic-proofs.tex`: after `On this evidence the sign of \(\hat U\) depends on \(K\).` (**L3194**, unique) and before `\emph{Scale dependence.}` (**L3196**, unique); file is byte-identical to the reviewed pin (883,075 B). Expected spliced size **886,224 B** (join CRLF + payload, preserving the anchor's blank-line accounting).
- Compile cert: 450 pp, exit 0/0, 0 undefined refs/citations, 0 multiply-defined.
- No status/priority/completion-label change; Problem F remains **Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL.** No new labels/refs/cites; `eq:Smatrix` resolves.

Integrate as-is.
