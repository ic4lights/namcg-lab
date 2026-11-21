# Proposal 081-088-r2, round 4

## Result
Minimal round. It addresses review-r3 finding 1 and nothing else. The mathematical content, scope and status are
unchanged from r3.

## Target and status
Problem G (HBEV): OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL, unchanged. This round proposes no label change.

## Source reading
Digest + targeted reads. I read scratch/digest.md (head bc78424; recorded appH file hash 779bfcac0950). I also read
review-r3.md, rowlen_r3.txt and apply_build_r3.py(.out). The live appH sha256 matches the recorded pre-hash
779bfcac09504722912302eb74299f4ba045dca64c65c166799b7bc3f70f723f.

## Research and reasoning
None new. The sentence edited is a wording clarification. The re-derived identity 1/2<Tr Q^2> = 4 s^2 W_block
(review-r3, Checks) is exactly what the new wording states: W_block is the full sum over the boundary row inside
the block.

## Claim classification
Unchanged from r3.

## Proposed changes
### Diff from r3 (S3 only)
Only line 2 of the Row length replacement changes: `rowlen_r3.txt` becomes `rowlen_r4.txt`. Line 1 (the text
being replaced in the live file) is unchanged. The file is CRLF, like r3.

```diff
- with \(W\) the sum over the boundary row inside the block without its entry at \(u\), while \(\tfrac12\langle\operatorname{Tr}Q^{2}\rangle\) is \(4s^{2}\) times the full sum (exact).
+ with \(W\) the sum over the boundary row inside the block without its entry at \(u\), while \(\tfrac12\langle\operatorname{Tr}Q^{2}\rangle\) is \(4s^{2}\) times the full sum over the boundary row inside the block (exact).
```

The new line 2 is the replacement text from review-r3 finding 1, byte for byte; the creation step asserts this
equality. The net change is +39 bytes (" over the boundary row inside the block").

### Unchanged parts
| item | file | sha256 | status vs r3 |
|---|---|---|---|
| S1 | insert_r3.tex | 8dfc3ac0e98f6505fa21220a546a66ce284a43cd918fd05deb5b5d14db9200b6 (5236 B) | unchanged |
| S2 | closing_r2.tex | 44f1695d0b403fbc513439d0c55aab2fee4dd345d3c2b2c66772ba73b706ea08 (1135 B) | unchanged |
| S2 | clause_r2.txt | 06b5de4cb36316a02b0343fa39e1e6679643c6d6f97b97c9ad5a9722e33a4e7a | unchanged |
| S3 old | rowlen_r3.txt | 24d15670950d6ae7ac478000afdb6fa21aa01a0db87de732c29d4a02120a6428 | superseded |
| S3 new | rowlen_r4.txt | 161e7ff4934a2e3746a12a9cd3f9558a30b4dec42d546968aabc158f3f193fd0 | new |

The insertion rule (S1, S2, S3 anchors and positions) is the same as in r3.

### Anchor uniqueness (live appH, from apply_build_r4.out)
- S1 anchor `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}`: line-start count 1. It immediately
  follows the Coincident copies paragraph (asserted).
- S2 anchor `These statements are for a compact factor ...`: count 1; the clause occurs once in the file and once in that line.
- S3 anchor `\emph{Row length.} If `: count 1. Line 1 of rowlen_r4 occurs once in the file and once in that line.
  After the edit, the full new line 2 occurs exactly once (asserted).

Note for the reviewer: the phrase "times the full sum over the boundary row inside the block (exact)" now appears
twice in the applied file. One is at L2922, the S3 edit. The other is at L2936, the existing `8s^{2}` sentence in
insert_r3.tex. That sentence was accepted in r3 and is not changed here. The two sentences now use the same wording.

### Hashes
- PRE appH: 676585 B, sha256 779bfcac09504722912302eb74299f4ba045dca64c65c166799b7bc3f70f723f, CRLF 3463, bare LF 0.
- POST appH (r4): 682047 B, sha256 **fc0884aa8c24e414020520f979a356b07374e2d58e8cdedf55910344a16510c6**,
  CRLF 3467, bare LF 0. This replaces the r3 post-hash b71bb0ac... (682008 B); the difference is +39 B.

No labels are added, removed or changed. bib/ is not touched.

## Verification scripts
- `apply_build_r4.py` is apply_build_r3.py with `rowlen_r3.txt` replaced by `rowlen_r4.txt` (plus the r4 tag in the
  docstring). All byte-contract assertions are the same as in r3. Output: `apply_build_r4.out`.
- Re-run from the repository root:
  `python -I proposals/local-gpu/081-088-r2/apply_build_r4.py <OUTDIR outside repo> --build`
- Expected output:
  - PRE sha matches: True;
  - POST sha256 fc0884aa...10c6, 682047 B;
  - pdflatex rc=0 ×3, bibtex rc=0, 394 pages;
  - undefined/multiply-defined warnings: 0;
  - BUILD PASS.
- The build actually ran in the session scratchpad (outside the repository), and the build directory was removed.
- v1, v2 and v3_r3 are unaffected and not re-run.

## Decisions Taken
None.

## Milestone assessment
Routine.

## Status-label recommendation
None. Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed
None.

## Remaining open step
As in r3. The gatekeeper full scan is still pending (review-r3 finding 4).

## Special instructions for the gatekeeper
- Check that rowlen_r4 line 2 equals the finding 1 text byte for byte.
- Check that S1/S2 hashes are unchanged and that the POST hash is fc0884aa....
- Do not treat any part of this package as closing Problem G.
