## Decisions Taken

- Adopted the review's Required-action wording for all six payload edits. Where mathematically equivalent wording was permitted: the Finding-5 closer follows the book's own variant formula at appH L1731 ("nothing in this paragraph closes ...") with the identical problem list (D, D1, A) and no status labels; the Finding-2 pointer mirrors the review's own description of the recorded lemma and claims neither overlap nor novelty.
- Finding 7 (researcher decision): delete and replace the weak-closure parenthetical with the strong bracket-retention statement per Research B step 6, because the weak form admits the central-scalar counterexample and would make the payload conclusion false on its stated premises; the alternative (rewording the parenthetical to keep weak closure) was rejected as it preserves a false claim.
- The generator reads payload-126-v2.txt from disk (pin-asserted) and applies the eight byte replacements, so v3 is provably v2 plus exactly the prescribed edits (each old string asserted unique; each new string asserted exactly-once and absent from v2); retyping the body was rejected for silent-drift risk.
- Rejected: adding a label or \eqref at appH L1931 - no label exists there, editing another part of appH is outside this single-insertion package, and the review prescribed the prose form.
- Rejected: whole-book-count defect probes - the string "over with" occurs twice in unrelated pre-existing book text (ch02 exercises note; an appendix passage); defect probes are scoped to the spliced paragraph and the two hits are recorded in the certificate so a future whole-book count cannot mis-fire.
- Certificate: fresh external tree C:/Users/redgi/AppData/Local/Temp/build126_cert_v4_12620 (new name, kept, outside the repo; repository never built, never written outside this folder).

## Milestone assessment

Routine: a round-2 revision package with no new mathematics; no MILESTONE.md trigger applies (the mathematical scope is the bounded conditional obstruction plus two exact models that review-r1 classified as non-milestone; the Chapter 17 D1 criterion is untouched).

## Status-label recommendation

Unchanged for every label. Critical-path list re-derived from the current Chapter 17 criterion and Appendix H: A, B, C, D1, E, F, G-derived and N (H, I, J optional within their stated scopes). D1 stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; no label, priority or completion-classification edit is proposed or made.

## Author decision needed

None.

## Special instructions for the gatekeeper

- Scope of this package: payload v3 + splice + certificate + this document. Do not integrate v1 or v2 objects (preserved bytes: payload-126.txt 7e6ed4cd6c83/4,361; payload-126-v2.txt b9ebeba71fe9/4,447; generators v1 d2826812c80a, v2 e996ca20baad/7,417).
- Anchor and recipe: ANCHOR = "supplied: this paragraph closes none of Problem~D, Problem~D1, or Problem~A." + CRLFCRLF, unique at appH L1740; insertion recipe live.replace(ANCHOR, ANCHOR + payload_v3 + CRLF, 1); expect POST 880,023 = 875,106 + 4,915 + 2; the canonical replace(anchor, payload+anchor) form is the wrong object (880,021). appH must still be 76d862968c31d78fffc665f72aaf60d40c90367a / 875,106 B at integration time.
- Re-checks suggested: re-run make_payload_126.v3.py (expect 19 CTRL-FIRED, 0 CTRL-DEAD, MAKE-OK) and the independent POST one-liner; confirm each of the six finding edits appears exactly once in the v3 bytes and the Finding-7 parenthetical phrase is absent; confirm the difflib segments account for all and only the eight replacements; confirm the central-scalar datum does not satisfy the qualified conclusion's premises (it fails bracket retention unless lambda = 0, since so(3,1) is perfect).
- The certificate need not be re-run unless bytes change; out-cert-126-v4.txt carries the full probe table, the scoped-resolution note for the two pre-existing whole-book "over with" hits, and the baseline citation count.
- Must not be asserted anywhere in the integrated text: any closure (of D, D1 or A), any derivation of SO(3,1) from the matrix algebra or the condensate, any novelty for the Problem E lemma, or any unqualified triviality sentence without the bracket-retention premise.
- Script B's stale docstring line 19 / R6 print labels (review-r1 Finding 4 side note) are script-internal and byte-preserved; the executable checks are correct.
