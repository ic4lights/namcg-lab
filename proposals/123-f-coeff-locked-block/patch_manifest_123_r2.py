# -*- coding: ascii -*-
# r2 patch for build_manifest_123.py (old bytes preserved as
# build_manifest_123.py.r1-bytes, a9f32d93825a): r2 roles, header POST line,
# lineage notes 9-10, note-5 hash refresh. Literals verbatim from the file.
import hashlib
P = r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\123-f-coeff-locked-block\build_manifest_123.py"
src = open(P, "rb").read()
print("pre-patch sha1", hashlib.sha1(src).hexdigest(), len(src))

def rep(old, new):
    global src
    o = old.encode("ascii"); n = new.encode("ascii")
    assert src.count(o) == 1, "count %d for %r" % (src.count(o), old[:70])
    src = src.replace(o, n, 1)

rep(r''' "make_payload_123.py": "generator: builds payload, splices live bytes, hygiene controls",''',
    r''' "make_payload_123.py": "generator r2 bytes (in-place after .r1-bytes): r2 payload text, CONTEXT-anchor splice, 10 hygiene controls",''')
rep(r''' "check_payload_123_r1.py": "checker r1: independent re-verification from disk",''',
    r''' "check_payload_123_r1.py": "checker r2 bytes (in-place after .r1-bytes): independent re-verification from disk",''')
rep(r''' "payload-123.txt": "THE PAYLOAD paragraph (one line + CRLF, ASCII); .txt container, role-identical to .tex payloads of 121/122",''',
    r''' "payload-123.txt": "THE PAYLOAD paragraph, r2 bytes (one line + CRLF, ASCII); .txt container, role-identical to .tex payloads of 121/122",''')
rep(r''' "preview-splice-123.txt": "SPLICE-WINDOW SAMPLE (400 B before + payload + 200 B after), NOT a full-file POST preview",''',
    r''' "preview-splice-123.txt": "SPLICE-WINDOW SAMPLE, r2 bytes (400 B before + payload + 200 B after), NOT a full-file POST preview",''')
rep(r''' "proposal-r1.md": "round-1 research record (proposal)",''',
    r''' "proposal-r1.md": "round-1 research record (proposal; payload bytes and exclusion reason superseded at r2)",
 "review-r1.md": "gatekeeper r1 review, ACCEPT WITH REQUIRED REVISIONS (verdict line pinned in proposal-r2.md header)",
 "proposal-r2.md": "round-2 record: finding responses, option dispositions, byte-exact r2 payload, reproduction pack",
 "embedded-r2-extract.bin": "extraction of the proposal-r2.md payload block; cmp-identical to payload-123.txt (evidence)",
 "make_payload_123.py.r1-bytes": "byte snapshot of the generator before the r2 in-place patch (r1 bytes 25063ff68713...)",
 "check_payload_123_r1.py.r1-bytes": "byte snapshot of the checker before the r2 in-place patch (r1 bytes 462ed5b332ac...)",
 "build_manifest_123.py.r1-bytes": "byte snapshot of this builder before the r2 in-place patch (r1 bytes a9f32d93825a...)",
 "inspect_anchor_123.py": "r2 helper: anchor-variant and context-anchor counts in live appH (read-only)",
 "recom_post_123_r2.py": "r2 INDEPENDENT POST recompute from live bytes (does not call the generator)",
 "patch_gen_123_r2.py": "audit copy of the r2 patch applied to make_payload_123.py",
 "patch_chk_123_r2.py": "audit copy of the r2 patch applied to check_payload_123_r1.py",
 "fix_patch_123.py": "interim helper (superseded by final patch_gen_123_r2.py bytes); no role in verification",
 "run_cert_123_r2.py": "r2 compile cert runner (new file; r1 runner run_cert_123.py left byte-untouched)",
 "build_proposal_r2.py": "builder of proposal-r2.md (embeds payload byte-exact, self-verifies by extraction+cmp)",
 "out-gen-run4.txt": "r2 generator capture (10 controls fired, GEN PASS, POST ba72024aba4d 869275)",
 "out-checker-run4.txt": "r2 checker capture 1 (45 check PASS + verdict, rc 0)",
 "out-checker-run5.txt": "r2 checker capture 2, byte-identical to run4",
 "cert-summary-123-r2.txt": "r2 compile certificate summary (CERT VERDICT PASS)",
 "cert-pl3-full-123-r2.log": "r2 certificate pass-3 log (0 undefined, 0 multiply, 0 '^!')",
 "cert-pl3-tail-123-r2.txt": "r2 certificate pass-3 log tail",
 "cert-bib-123-r2.log": "r2 certificate bibtex log",''')

rep(r'''d2af19df0f998ce150c12ea11af9ea8c0387435f, 863831 B. Splice target POST
704f3765797a89371fa683089b560e6a496f5df6, 869321 = 863831 + 5488 + 2.''',
    r'''d2af19df0f998ce150c12ea11af9ea8c0387435f, 863831 B. Splice target POST
(r2, current) ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1, 869275 =
863831 + 5442 + 2; (r1, superseded) 704f3765797a89371fa683089b560e6a496f5df6,
869321. Anchor is the CONTEXT string (closing sentence + CRLFCRLF +
\section{Problem G: HBEV}); the bare closing clause recurs 6x in appH.''')

rep(r'''   preview-splice-123.txt (5f45bad05587, 6132 B) is a splice-WINDOW sample''',
    r'''   preview-splice-123.txt (r2 bytes afbf4f9c81b3, 6086 B; r1 was
   5f45bad05587, 6132 B) is a splice-WINDOW sample''')
rep(r'''   checker recompute); it is verified by the checker POST_SHA1 check
   (704f3765797a89371fa683089b560e6a496f5df6) and must be RECOMPUTED''',
    r'''   checker recompute); it is verified by the checker POST_SHA1 check
   (r1 704f3765797a89371fa683089b560e6a496f5df6; r2
   ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1) and must be RECOMPUTED''')

rep(r'''proposal-r1.md record the full artifact chain so the
   gatekeeper can re-run every check from the scripts (reproduction pack in
   proposal-r1.md). journal.md is the live working log (all three sessions).''',
    r'''proposal-r1.md record the full artifact chain so the
   gatekeeper can re-run every check from the scripts (reproduction pack in
   proposal-r1.md). journal.md is the live working log (all rounds).
9. Round 2 (revision round, review-r1 finding 1): payload definition clause
   changed to "with fibre-traced endomorphism \(\mathrm{tr}\,E_{\mathrm{ten}}=e_h R_E\)"
   (gatekeeper Corrected snippet, verbatim); ghost-operator clause rephrased as
   a SPECIFIED Laplace-type operator per the review addendum (optional A
   adopted; first-variation derivation claim deleted; no consumed equation
   changed); r1 DELRHO exclusion reason corrected in proposal-r2.md (finding
   2; verified 64\pi line numbers); remainder alignment declined (finding 3).
   Supersession discipline observed: generator and checker edited in place
   ONLY after byte snapshots (.r1-bytes) were taken; run_cert_123.py was NOT
   edited (new file run_cert_123_r2.py). Generator adds two content guards
   (fibre-trace token present; first-variation token absent), each with an
   injected positive control; run4 capture shows 10 controls fired. Script 1
   stayed frozen per author fix-order and was not run this round.
10. r2 certificate (run_cert_123_r2.py, fresh %TEMP% copy cert123r2build):
    substituted appH ba72024aba4d / 869275 == POST; pdflatex1/bibtex/
    pdflatex2/pdflatex3 all rc=0; pl3.log 0 '^!', 0 undefined, 0 multiply;
    STABLE True; PDF 3272661 B (aux-state dependent size); repo untouched,
    build_check.py never run by this package.''')

open(P, "wb").write(src)
print("post-patch sha1", hashlib.sha1(src).hexdigest(), len(src))
print("PATCH VERDICT: PASS")
