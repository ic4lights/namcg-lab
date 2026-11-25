# 114-d1-locked-ghost-sector-spec, round 2: byte-revision report

Scope: BYTE REVISION ONLY per review-r1.md (ACCEPT WITH REQUIRED REVISIONS).
No new mathematics; wording changed only in the mandated fixes (findings 1, 2, 3
insert; findings 1 tail, 2/5 proposal) and the cert-record number. Findings 4
(optional) NOT applied. Anchor and landing unchanged.

## 1. Byte diffs applied

### insert-d1-locked-ghosts.tex

Finding 1 (blocking). At old byte offset 2127-2178 the sequence was
`the vacuum is \\(` + 0x09 (literal TAB) + `frac{3}{2v}\\mathrm{tr}\\,\\delta\\Phi\\)`
(review reported offset 2143 for the TAB byte itself; same sequence).
Replaced per the corrected snippet with
`the vacuum is \\(\\frac{3}{2v}\\mathrm{tr}\\,\\delta\\Phi\\)`
(backslash, open-paren, backslash + "frac" - frac, not tfrac, exactly as the
review snippet has it).

Findings 2+3 (major). Replaced the 383-byte fragment running from
`and the only` (after `... as kinetic operators, `) through
`not a consequence of~\eqref{eq:Smicro}.` with the review's corrected-sentence
block VERBATIM, internal newlines as CRLF:

    and, among the symmetries exhibited
    for the displayed action at the orders recorded above, no
    kinetic ghost operator other than that of the diffeomorphism
    sector arises; and with \(g^{(0)}_{\mu\nu}\) held fixed
    (Assumption~\ref{ass:aux-metric}) the invariance
    of~\eqref{eq:Smicro} under diffeomorphisms is exhibited only
    for those that preserve \(g^{(0)}\), such as its isometries,
    which does not exclude other symmetries and derives no
    diffeomorphism gauge symmetry, so the diffeomorphism ghost is
    a supplied input of the infrared sector and not a consequence
    of~\eqref{eq:Smicro}.

Joins preserved: the prefix `...weighted sector sum of Theorem~\ref{thm:Geff} as
kinetic operators, ` and the suffix CRLF + `These statements concern ...` are
untouched; everything else in the insert is unchanged.

Process note (honest record): the first r2 edit pass applied by this agent
introduced three further control-byte corruptions (0x0C from an escaped \f, one
lone LF from \n, one lone CR from \r) which the mandated scan caught and the
same round repaired before finalization; the final-state proofs below are for
the shipped bytes.

### proposal-r1.md

- LaTeX quote block replaced byte-for-byte by the new insert (LF-normalized),
  carrying both the frac fix (finding 1 tail) and the corrected two-consequence
  passage; verified programmatically: block == insert modulo EOL = True.
- L44-49 (finding 2/5): "the invariance of `eq:Smicro` is restricted to the
  isometries of `g^(0)` ... the only kinetic ghost operator available to a
  locked-block calculation is the diffeomorphism ghost" replaced with the
  recorded-hedge characterization: "the invariance of `eq:Smicro` under
  diffeomorphisms is exhibited only for those that preserve `g^(0)`, such as its
  isometries, which does not exclude other symmetries (appH L1201-1209) - among
  the symmetries exhibited for the displayed action at the orders recorded
  above, no kinetic ghost operator other than that of the diffeomorphism sector
  arises, and that ghost is a supplied input of the infrared sector, not a
  consequence of `eq:Smicro`."
- Same mischaracterization corrected at its second occurrence in the Research
  and reasoning passage (finding 2 required both insert and proposal body; this
  is the second proposal-body instance of the identical sentence).
- Cert record line updated to the r2 rerun numbers.
- Stale artifact size record in 'Proposed changes' updated 3438 B -> 3647 B
  (pin propagation only, per re-pin task; no wording change).
No other proposal changes. verify_ghost_fp_114.py, run-r114.txt,
cert-r114p.py untouched (hashes unchanged below).

## 2. Proof-by-inspection of the final insert (shipped bytes)

Full scan of all 3647 bytes:

- bytes in {0x00-0x08, 0x0B, 0x0C, 0x0E-0x1F, 0x7F+}: NONE (empty set).
- 0x09 TAB: count 0 (forbidden everywhere; none present).
- CR count 52, LF count 52, CRLF count 52 -> every line terminator is CRLF,
  no lone CR, no lone LF.
- No BOM (first bytes not EF BB BF). File ends CRLF. ASCII-only.
- LaTeX structural counts: 6 backslash-ref{ and 5 backslash-eqref{ (all nine
  live labels, none corrupted); backslash-frac x2 (tadpole + 1/64 display),
  backslash-tfrac x1 (the genuine witness 1/2 at the review-checked spot).

## 3. Certificate rerun on the final insert (r2)

`python -I -B cert-r114p.py`:

    spliced bytes: 828027 rc: 0 exclam-lines: 0 Output written: True
    CERT OK

## 4. Live-tree pins

- appH sha1 unchanged: `60a8eb47bb32184d60d0165483a635f9a331c2b3` (verified
  this round).
- Anchor paragraph `\paragraph{Diffeomorphism symmetry of the displayed action
  (conditional; not closure).}` grep -c in live appH = 1.
- Integrator note (per review): recompute POST from these pinned bytes; the
  review's POST value `68a2b471...` was for the pre-fix insert and is superseded
  by the re-pinned bytes above.

## 5. File table at r2 finalization (sha1, bytes)

    d512e4ab88989b6531633e39e417f683bfcc74a0  29389  proposal-r1.md
    a813eb9cf97f7f6c7ad57ca12f4595e75c53ef33   3647  insert-d1-locked-ghosts.tex
    595212189dfb57c56f8be5a22b321178c6c3b3b9   6585  verify_ghost_fp_114.py
    6b8832bd1dc199c17c24fedda8e6d3fced8a4d92    822  run-r114.txt
    d0cc7251ca8ba06fd742282b93d4dc823e88c3e3   1866  cert-r114p.py
    163c0d62f22d8e279a210734ff0db315bf2fd058  13565  review-r1.md
    (this file and manifest.md are hashed in manifest.md)

Reproduction unchanged: `python -I -B verify_ghost_fp_114.py` ->
`ALL CHECKS DONE`; `python -I -B cert-r114p.py` -> `CERT OK` (numbers in
section 3; the math verification was untouched this round).
