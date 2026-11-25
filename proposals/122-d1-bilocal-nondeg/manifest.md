# Item 122 manifest (round 2; round-1 record retained below)

All hashes sha1[:12]; sizes in bytes. Live-manuscript pin unchanged through
round 2: `chapters/appH-microscopic-proofs.tex` = cf3139fbedb0 / 857887
(round-2 start and round-2 end verified; item 122 writes nothing outside this
folder). Round-2 scope: review 122 r1 findings 1-4 (mechanical: single-CRLF
terminator + generator detector/control fix; two accepted wording fixes in
payload (ii); proposal-record numeric relabel). No mathematics, tier or scope
change.

## Round-2 artifacts (current)

| sha1[:12] | bytes | file | role |
|---|---|---|---|
| affd17c6f13d | 5942 | payload-122.tex | r2 manuscript-bound paragraph: single CRLF terminator; (ii) unitary **carrier transport operator** clause (finding 2, gatekeeper wording verbatim); fibre-wise/operator equality scope (finding 3, gatekeeper wording verbatim) |
| 4f7eb6a0afdc | 10957 | make_payload_122.py | r2 generator: terminator appended once (rstrip of CR/LF + single CRLF after LF->CRLF pass), `det_eol` flags any CR not followed by LF (regex built via chr(92)), named controls with new CR-CR-LF positive control, four terminator guard checks |
| d2af19df0f99 | 863831 | preview-appH-spliced.tex | live appH + r2 payload via canonical splice replace(anchor+CRLFCRLF, anchor+CRLFCRLF+payload+CRLF, 1) (PREVIEW ONLY, not integrated) |
| 17dc357362f8 | 4697 | check_payload_122_r2.py | r2 independent verifier: payload byte invariants, verbatim new wordings present, old wordings absent, POST recomputed from live appH, wrong-zone variant same size / different hash, exact heat-kernel spectrum values (finding 4) |
| 5cab45b3dd9d | 977 | out-gen122-r2-run1.txt | generator stdout run 1 |
| 5cab45b3dd9d | 977 | out-gen122-r2-run2.txt | generator stdout run 2 (byte-identical: determinism) |
| bffb7cc5198e | 1190 | out-check122-r2.txt | verifier stdout, CHECK-FAILURES: 0 (none) |
| 96f19a3d6b92 | 26182 | proposal-r1.md | unchanged round-1 proposal (never overwritten) |

proposal-r2.md: 84b1a85f06b7 22229 (round-2 proposal; embeds the payload body verbatim, and the body plus one CRLF
reproduces pin affd17c6f13d / 5942.

## Supersession pairs (both hashes recorded; author directive 2026-11-24 r2)

| superseded (r1) | pin / bytes | superseded by (r2) | pin / bytes |
|---|---|---|---|
| payload-122-r1-superseded.tex | 33165816b9fd / 5783 | payload-122.tex | affd17c6f13d / 5942 |
| make_payload_122-r1-superseded.py | 8c29318d3995 / 9902 | make_payload_122.py | 4f7eb6a0afdc / 10957 |
| preview-appH-spliced-r1-superseded.tex | c577442aab35 / 863672 | preview-appH-spliced.tex | d2af19df0f99 / 863831 |

The three r1 bytes above are also the round-1 pins recorded in the round-1
table below (unchanged). Full 40-hex, r2 central pins: payload
affd17c6f13d99ab0e8bbda2253950ee1cc2f1cf; spliced POST
d2af19df0f998ce150c12ea11af9ea8c0387435f. Payload-body delta old->new:
exactly the two accepted word substitutions, +160 bytes (verified in
proposal-r2.md difflog and re-derivable from the embedded bodies). POST
accounting r2: POST(863831) = PRE(857887) + PAY(5942) + 2, asserted inside the
generator AND recomputed independently by check_payload_122_r2.py from the
live appH bytes (recomputed POST equals the preview file byte-for-byte;
wrong-zone variant same size, different sha1). The review-r1 line "expect PAY
5782, POST 863671" was the finding-1-only arithmetic; the mandatory
findings 2-3 add the +160 body delta.

Reproduction commands (run from repository root):

    python -I proposals/122-d1-bilocal-nondeg/bilocal_nondeg_s1.py
    python -I proposals/122-d1-bilocal-nondeg/bilocal_nondeg_s2.py
    python -I proposals/122-d1-bilocal-nondeg/make_payload_122.py
    python -I proposals/122-d1-bilocal-nondeg/check_payload_122_r2.py

Expected invariants (r2): s1 and s2 end "FAILURES: 0 (none)" (unchanged from
r1; they do not consume the payload); the generator ends "GEN-FAILURES: 0
(none)", prints "controls fired: 7/7" with "FIRED CR-CR-LF-terminator" among
the seven, PRE 857887 PAY 5942 POST 863831 and POST-SHA1 d2af19df0f99...;
the verifier ends "CHECK-FAILURES: 0 (none)" and prints the exact spectrum
values exp(-s^2 n^2/4), s=0.15: 3.15e-03 (n=32), 9.86e-11 (n=64), 9.45e-41
(n=128), 7.97e-161 (n=256).

---
# Round-1 record (historical; superseded where noted above)

All hashes are sha1[:12]; sizes in bytes. Live-manuscript pin at dispatch and at
payload generation: `chapters/appH-microscopic-proofs.tex` = cf3139fbedb0 / 857887
(UNCHANGED; item 122 writes nothing outside this folder).

| sha1[:12] | bytes | file | role |
|---|---|---|---|
| df1d198e305b | 8211 | bilocal_nondeg_s1.py | fiber/operator algebra R0-R6, teeth |
| f57402f6ca0e | 6268 | bilocal_nondeg_s2.py | transport classes/state reading T1-T5, teeth |
| 62ea7c6e5b25 | 1012 | out-s1-run1.txt | s1 output, run 1 |
| 62ea7c6e5b25 | 1012 | out-s1-run2.txt | s1 output, run 2 (byte-identical) |
| 2ab6fb1050ee | 1169 | out-s2-run1.txt | s2 output, run 1 |
| 2ab6fb1050ee | 1169 | out-s2-run2.txt | s2 output, run 2 (byte-identical) |
| 8c29318d3995 | 9902 | make_payload_122-r1-superseded.py | r1 generator (superseded by 4f7eb6a0afdc; copy under r1 name) |
| 33165816b9fd | 5783 | payload-122-r1-superseded.tex | r1 paragraph (superseded by affd17c6f13d; copy under r1 name; carries the stray lone CR, finding 1) |
| c577442aab35 | 863672 | preview-appH-spliced-r1-superseded.tex | r1 splice (superseded by d2af19df0f99; copy under r1 name) |

Full 40-hex for the two central r1 pins: payload
33165816b9fd404bf77899ed4eaf8efa84e6368b; spliced POST
c577442aab35c7d4a736557c32cc17ae91079736. POST accounting (r1):
POST(863672) = PRE(857887) + PAY(5783) + 2. Generator was deterministic in r1
too. The r1 "7/7 controls" are superseded: the lone-CR control was a dead
branch (review 122 r1 finding 1); r2 replaces it with the CR-CR-LF control.

proposal-r1.md: 96f19a3d6b92 26182 (round-1 proposal; embeds r1 payload bytes;
its Carrier-topology record at ~L146-147 is amended by proposal-r2.md finding 4).
