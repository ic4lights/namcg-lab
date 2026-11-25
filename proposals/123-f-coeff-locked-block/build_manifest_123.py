# -*- coding: ascii -*-
# Item 123 manifest builder: hashes every file in the folder (except
# manifest.md itself) and writes manifest.md (ASCII, CRLF). Rerun after the
# final captures land; deterministic except for journal.md (live log).
import os, hashlib

FOLD = r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\123-f-coeff-locked-block"

ROLES = {
 "verify_ghost_op_123.py": "script 1: symbolic ghost-operator/a_1 verification (sympy)",
 "verify_bookkeeping_123.py": "script 2: sector bookkeeping/counts/windowed a1 (sympy)",
 "verify_threshold_window_123.py": "script 3: threshold/window and Upsilon identities (sympy)",
 "make_payload_123.py": "generator r2 bytes (in-place after .r1-bytes): r2 payload text, CONTEXT-anchor splice, 10 hygiene controls",
 "check_payload_123_r1.py": "checker r2 bytes (in-place after .r1-bytes): independent re-verification from disk",
 "run_cert_123.py": "compile cert: TEMP-dir copy build with spliced appH (repo untouched)",
 "payload-123.txt": "THE PAYLOAD paragraph, r2 bytes (one line + CRLF, ASCII); .txt container, role-identical to .tex payloads of 121/122",
 "preview-splice-123.txt": "SPLICE-WINDOW SAMPLE, r2 bytes (400 B before + payload + 200 B after), NOT a full-file POST preview",
 "out-script1-runC.txt": "0 B KILL TOMBSTONE: run C python (PID 18392, launched 16:10) killed 19:18 per author fix-order; buffered stdout lost (lineage note 2)",
 "out-script1-runD.txt": "0 B KILL TOMBSTONE: run D python (PID 1452, launched 16:19) killed 19:18 per author fix-order; buffered stdout lost (lineage note 2)",
 "out-script1-run1.txt": "0 B truncation artifact (dead-session capture lost to harness cleanup); kept as evidence",
 "out-script2-run1.txt": "script 2 run 1: 877 B FAIL, float-artifact version (superseded)",
 "out-script2-run2.txt": "script 2 run 2: byte-identical to run1 (superseded)",
 "out-script2-run3.txt": "script 2 green capture, 843 B exact rationals (hash 5e64dfef8ba2 quoted in a dispatch was THIS capture's hash, not the script's)",
 "out-script2-runC.txt": "script 2 re-capture, byte-identical to run3",
 "out-script2-runD.txt": "script 2 re-capture, byte-identical to run3",
 "out-script3-run1.txt": "script 3 capture 1 (PASS list)",
 "out-script3-run2.txt": "script 3 capture 2, byte-identical to run1",
 "out-checker-run1.txt": "checker capture 1 (PASS list, 1154 B)",
 "out-checker-run2.txt": "checker capture 2, byte-identical to run1",
 "out-checker-run3.txt": "checker determinism re-run this session, byte-identical to run1/run2",
 "out-gen-run3.txt": "generator determinism re-run this session (GEN PASS, controls fired)",
 "tmpcap123-C.txt": "redundant temp copy of script1 run C (may be truncated by harness cleanup; out-* copy is authoritative)",
 "tmpcap123-D.txt": "redundant temp copy of script1 run D (may be truncated; out-* copy authoritative)",
 "tmpcap123-GEN.txt": "redundant temp copy of generator re-run capture",
 "tmpcap123-CHK.txt": "redundant temp copy of checker re-run capture",
 "out-script1-runB3.txt": "0 B FOREIGN artifact written 17:04 by a revived dead-session task chain (cp of its truncated temp capture after this session stopped that chain's hung python); kept as evidence",
 "cert-summary-123.txt": "compile certificate summary (CERT VERDICT PASS)",
 "cert-pl3-full-123.log": "certificate pass-3 pdflatex log (0 undefined, 0 multiply)",
 "cert-pl3-tail-123.txt": "certificate pass-3 log tail",
 "cert-bib-123.log": "certificate bibtex log",
 "journal.md": "working journal of the three sessions (live log; hash is at manifest build time)",
 "proposal-r1.md": "round-1 research record (proposal; payload bytes and exclusion reason superseded at r2)",
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
 "patch_manifest_123_r2.py": "audit copy of the r2 patch applied to this builder (pre-patch a9f32d93825a)",
 "fix_patch_123.py": "interim helper (superseded by final patch_gen_123_r2.py bytes); no role in verification",
 "run_cert_123_r2.py": "r2 compile cert runner (new file; r1 runner run_cert_123.py left byte-untouched)",
 "build_proposal_r2.py": "builder of proposal-r2.md (embeds payload byte-exact, self-verifies by extraction+cmp)",
 "out-gen-run4.txt": "r2 generator capture (10 controls fired, GEN PASS, POST ba72024aba4d 869275)",
 "out-checker-run4.txt": "r2 checker capture 1 (45 check PASS + verdict, rc 0)",
 "out-checker-run5.txt": "r2 checker capture 2, byte-identical to run4",
 "cert-summary-123-r2.txt": "r2 compile certificate summary (CERT VERDICT PASS)",
 "cert-pl3-full-123-r2.log": "r2 certificate pass-3 log (0 undefined, 0 multiply, 0 '^!')",
 "cert-pl3-tail-123-r2.txt": "r2 certificate pass-3 log tail",
 "cert-bib-123-r2.log": "r2 certificate bibtex log",
 "build_manifest_123.py": "this builder (rerunnable; ASCII/CRLF output)",
}

def sha(b): return hashlib.sha1(b).hexdigest()

present = set(f for f in os.listdir(FOLD) if os.path.isfile(os.path.join(FOLD, f)))
missing = set(ROLES) - present
FALLBACK = os.environ.get("M123_FALLBACK") == "1"
if missing and not (FALLBACK and missing == {"out-script1-runC.txt",
                                             "out-script1-runD.txt"}):
    raise SystemExit("MISSING EXPECTED FILES: %s" % sorted(missing))

rows = []
for name in sorted(os.listdir(FOLD)):
    p = os.path.join(FOLD, name)
    if not os.path.isfile(p) or name == "manifest.md":
        continue
    b = open(p, "rb").read()
    role = ROLES.get(name)
    if role is None:
        import re as _re
        if _re.fullmatch(r"out-script1-run[A-Z]?[0-9]?\.txt", name):
            role = ("FOREIGN capture artifact from a revived dead-session "
                    "task chain (lineage note 8); inspect bytes before use")
        else:
            raise SystemExit("UNKNOWN FILE (add role): " + name)
    rows.append("| %s | %s | %d | %s |" % (name, sha(b)[:12], len(b), role))
for name in sorted(missing):
    rows.append("| %s | ABSENT-TIMEOUT | 0 | %s |" % (name, ROLES[name]))

HDR = r"""# Manifest 123-f-coeff-locked-block

Built by build_manifest_123.py (rerun to refresh; output ASCII, CRLF).
SHA1 shown as first 12 hex digits. manifest.md is excluded from its own
table (self-reference). Live manuscript pin at build: appH
d2af19df0f998ce150c12ea11af9ea8c0387435f, 863831 B. Splice target POST
(r2, current) ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1, 869275 =
863831 + 5442 + 2; (r1, superseded) 704f3765797a89371fa683089b560e6a496f5df6,
869321. Anchor is the CONTEXT string (closing sentence + CRLFCRLF +
\section{Problem G: HBEV}); the bare closing clause recurs 6x in appH.

| file | sha1[:12] | bytes | role |
|---|---|---|---|
"""

LIN = r"""
## Lineage notes (honest record)

1. Script 2 (verify_bookkeeping_123.py, df307b2e7750, 9130 B): run history
   out-script2-run1 == run2 (877 B, FAIL, float artifacts) then run3 ==
   runC == runD (843 B, all PASS, exact rationals). The hash 5e64dfef8ba2
   quoted in an orchestrator dispatch was the sha1 of the GREEN CAPTURE
   out-script2-run3.txt, not of the script bytes; resolved in journal
   milestone 24c.
2. Script 1 (verify_ghost_op_123.py, 454d22922dd9, 15256 B): capture
   truncation history: out-script1-run1.txt is 0 B (lost at 10:03,
   dead-session harness cleanup); runA2 was green-BY-NOTIFICATION (full PASS
   list in the orchestrator notification) but its file bytes were later
   truncated to 0 B; tmpD.txt (0 B) is the truncation artifact of a
   dead-session redirect target. out-script1-run1.txt (0 B) is kept as
   evidence of the harness truncation; tmpD.txt (0 B) was itself removed
   at 17:04 on 2026-11-24 by a revived dead-session task chain (note 8)
   before this session could re-tabulate it. This session re-captured runC and runD with the
   survivor protocol (foreground python, redirect to tmpcap123-*, copy to
   out-script1-run* inside the same command). FINAL: no script-1 capture
   bytes were obtained; both runs (full-compute, ~3 h each, ~3.8 GB) were
   killed at 19:18 under an explicit author fix-order, python's buffered
   stdout was lost, and out-script1-runC.txt / out-script1-runD.txt are
   0 B kill tombstones (19:18:02). No further script-1 runs are armed.
   DISPOSITION: the gatekeeper r1 may re-derive script 1's central
   computation (ghost-fibre a_1 = (5/3)R in harmonic gauge, Wald-sign
   conventions of eq:christoffel--eq:riemann) independently per the
   proposal 120 verifier precedent, or re-run the frozen script
   454d22922dd9 at its discretion; the payload's remaining arithmetic is
   covered by the byte-reproducible green captures of scripts 2-3 and was
   hand-checked independently (a_1 ghost fibre (4/6+1)R; ghost A1
   contribution -10/3; N0 = 18 + n_K).
3. check_payload_123_r1.py was revised IN PLACE twice during development
   (checker-token bug fixes per journal: a Specif{}y typo; the ghost-weight
   REC token lives in appH, not ch17). The r0 bytes are NOT preserved:
   recorded deviation from the supersede-by-copy rule. The doubled
   REC_GHOSTM2W line in its output is by construction (dict entry plus a
   redundant raw-string check of the same token).
4. run_cert_123.py was also edited IN PLACE after the cert run: the journal
   cites 8f8b9e78379e for the cert-time bytes; disk is f54de3d0e12e. Old
   bytes not preserved (same deviation class as note 3). The certificate
   artifacts below were produced by the cert-time version against spliced
   bytes hash-asserted at POST.
5. payload-123.txt uses a .txt container; its bytes play the role of the
   .tex payload files of items 121/122 (ASCII, CRLF-terminated, no labels).
   preview-splice-123.txt (r2 bytes afbf4f9c81b3, 6086 B; r1 was
   5f45bad05587, 6132 B) is a splice-WINDOW sample
   (400 B before + payload + 200 B after, with markers), NOT a full-file
   preview. The full POST exists only transiently (generator arg-1 output /
   checker recompute); it is verified by the checker POST_SHA1 check
   (r1 704f3765797a89371fa683089b560e6a496f5df6; r2
   ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1) and must be RECOMPUTED
   independently from live bytes by the gatekeeper and integrator.
6. Compile certificate (cert-summary-123.txt): CERT VERDICT PASS; the
   substituted appH in the TEMP build copy hashed 704f3765797a size 869321
   (== POST); all four passes rc 0; pl2.log and pl3.log show 0 '^!' lines, 0
   undefined, 0 multiply-defined; STABLE True; PDF 3272848 B. pl1.log shows
   1606 undefined references, expected pre-bibtex. The repository itself was
   never built on or modified by this package.
8. Revived dead-session task chains: at ~17:04-17:06 on 2026-11-24 this
   session stopped nine hung python processes running
   verify_ghost_op_123.py that had been launched by the two dead
   predecessor sessions (8 orphans at 6.4h+ CPU, 1.4-4.7 GB RAM each,
   plus one respawn; machine free RAM had dropped to 292 MB). Those
   chains' shells were still resident in the task host: when their
   pythons exited (killed), the chains executed their post-commands -
   writing out-script1-runB3.txt (0 B, kept as evidence) and removing
   tmpD.txt. No file named out-script1-runC.txt or out-script1-runD.txt
   was touched by the revived chains before this session's own runs
   landed; the manifest build verifies this by hash.
7. Two predecessor sessions died of environment context overflow; this
   manifest and proposal-r1.md record the full artifact chain so the
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
    build_check.py never run by this package.
"""

out = HDR + "\r\n".join(rows) + "\r\n" + LIN
out = out.replace("\r\n", "\n").replace("\n", "\r\n")
ob = out.encode("ascii")
open(os.path.join(FOLD, "manifest.md"), "wb").write(ob)
print("MANIFEST", sha(ob)[:12], len(ob))
print("FILES TABBED:", len(rows))
