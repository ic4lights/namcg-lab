# manifest_gen120.py - writes manifest.md: pins table for every file in this folder.
# Self cell per the 119 documented rule: "self: see run report". CRLF, ASCII, no BOM.
import hashlib
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))

DEBRIS = {"vpart2a.txt", "vpart2b.txt", "vpart3a.txt", "vpart3b.txt", "vpart3btail.txt",
          "vpart3c.txt", "vtest.txt"}
NOTES = {
    "insert-commutator-lift-r1.tex": "PAYLOAD (fixed input this round; P1-pinned)",
    "verify_r120.py": "verify pack, final post-R3 (see verify_repair_log.txt)",
    "verify_r120-preR1.py": "superseded verify bytes (54ec6b20233b/34530), preserved",
    "verify_r120-preR2.py": "superseded verify bytes after R1 (610a2c6c7a32/36376), preserved",
    "patch_r1_t5c.py": "repair R1 applier + controls (idempotent; intermediate step)",
    "patch_r2_simplify.py": "combined repair-chain re-deriver R1+R2 + controls (idempotent)",
    "out-patchR1.txt": "repair R1 capture (CONTROL OK 120R1)",
    "out-patchR2.txt": "repair R2 capture (CONTROL OK 120R2)",
    "out-r120-fail3.txt": "RAW failed capture: post-R1 stall at simplify_sym, killed (R2)",
    "out-r120-fail4.txt": "RAW failed capture: post-R1+R2 stall, probe localized (R3)",
    "probe_t5c.py": "timing probe localizing the T5c full-lift cost (diagnostic)",
    "out-probe-t5c.txt": "probe capture (lift_from_B ~50 min/call; mats_eq 1 s)",
    "patch_r3_liftcongruence.py": "repair R3 applier + controls (idempotent)",
    "out-patchR3.txt": "repair R3 capture (CONTROL OK 120R3, APPLIED+VERIFY)",
    "verify_r120-preR3.py": "superseded verify bytes after R2 (b71430a6ebf3/36449), preserved",
    "repair_chain120.py": "combined audit re-deriver R1+R2+R3 + chk-name census (temp dir)",
    "out-chain120.txt": "chain audit capture (CHAIN OK 120)",
    "out-probe1.txt": "assembly debris (chain-120 S2b deaths)",
    "out-r120.txt": "canonical clean verify capture (TOTAL/ALL CHECKS DONE 120)",
    "out-r120-fail1.txt": "RAW failed capture: orphan buffered run killed at 0 B (R0)",
    "out-r120-fail2.txt": "RAW failed capture: stall localized at T5c, killed (R0/R1)",
    "out-r120-rerun1.txt": "clean run copied to out-r120.txt",
    "verify_repair_log.txt": "repair log R0/R1 (check-side only; claims unchanged)",
    "assemble_pr1.py": "proposal-r1.md assembler (guards placeholders/FAILs; CRLF)",
    "proposal-r1.md": "FINAL proposal text (r1)",
    "pr1_partA.md": "drafted head (input to assembler; LF in source, CRLF in output)",
    "pr1_partB.md": "drafted continuation (input to assembler)",
    "manifest_gen120.py": "this generator",
    "gen_payload_120.py": "payload generator (run twice byte-identical)",
    "out-gen120-a.txt": "GEN OK 120 capture a",
    "out-gen120-b.txt": "GEN OK 120 capture b (== a)",
    "cert-r120p.py": "compile certificate (CERT PASS)",
    "out-cert-r120p.txt": "CERT PASS capture",
    "check_labels120.py": "label census (LABELS OK 120)",
    "out-labels120.txt": "label census capture",
    "out-s2b-bridge-r1.txt": "stage-1 s2b re-run (byte-identical to stage-1 pin)",
    "out-s2c-lift-r1.txt": "stage-1 s2c re-run (byte-identical to stage-1 pin)",
    "out-s3a-quartic-r1.txt": "stage-1 s3a re-run (byte-identical to stage-1 pin)",
    "out-s3b-frame-r1.txt": "stage-1 s3b re-run (byte-identical to stage-1 pin)",
    "addendum119_notes.txt": "119 notes.md addendum payload text (applied)",
    "addendum119_manifest.txt": "119 manifest.md addendum payload text (applied)",
    "apply_trims120.py": "payload trim tool (earlier S2 round)",
    "trims.json": "trim table consumed by apply_trims120.py (earlier S2 round)",
    "census_trace120.py": "trace/operatorname census helper (earlier S2 round)",
    "find_Tr120.py": "census helper a", "find_Tr120b.py": "census helper b",
    "find_Tr120c.py": "census helper c", "find_Tr120d.py": "census helper d",
}

lines = []
lines.append("manifest.md - proposals/120-commutator-lift-bridge/ - S2-final (round 1)")
lines.append("")
lines.append("Baseline manuscript pin: chapters/appH-microscopic-proofs.tex 9e0b198af2c3 / 848842 B.")
lines.append("Integration anchor: '\\section{Problem E: signature}', count 1 at byte 295299.")
lines.append("Payload: insert-commutator-lift-r1.tex sha1[:12] 343226e27ebf / 5138 B (P1-pinned in verify pack).")
lines.append("POST: 853982 B = 848842 + 5138 + 2 (blank-line join), full sha1 d5e2e67c0a63ad3b0bce6034f2985ea94b9f3274.")
lines.append("Rerun identity: the four stage-1 re-run captures out-s2b-bridge-r1.txt, out-s2c-lift-r1.txt,")
lines.append("out-s3a-quartic-r1.txt, out-s3b-frame-r1.txt are byte-identical to the stage-1 pins recorded in")
lines.append("reports/ledger.md (CHAIN-120-S2-DEATH-RESUME): 9c14be97058a/828, b27a498ec4b2/1645,")
lines.append("1b01e527846c/1362, 0bc923bb8d5e/451; gen_payload_120.py ran twice byte-identical")
lines.append("(out-gen120-a.txt == out-gen120-b.txt, d1e03210a7f7/199); cert-r120p.py CERT PASS on the live tree.")
lines.append("119 doc-only addendum pins (applied previous round): scratch/120/notes.md 6fbc2d9b88f7/12257 ->")
lines.append("d81b9d34e5c3/13937; scratch/120/manifest.md 5e3e09090733/8999 -> 494242828797/10489.")
vb = io.open(os.path.join(HERE, "verify_r120.py"), "rb").read()
v2 = io.open(os.path.join(HERE, "verify_r120-preR2.py"), "rb").read()
v3 = io.open(os.path.join(HERE, "verify_r120-preR3.py"), "rb").read()
lines.append("verify pack: verify_r120.py final pin %s/%d (chain 54ec6b20233b/34530 -> %s/%d (preR2) ->" %
             (hashlib.sha1(vb).hexdigest()[:12], len(vb), hashlib.sha1(v2).hexdigest()[:12], len(v2)))
lines.append("%s/%d (preR3) -> final; re-derive with repair_chain120.py -> CHAIN OK 120;" %
             (hashlib.sha1(v3).hexdigest()[:12], len(v3)))
lines.append("repairs check-side only (verify_repair_log.txt); all pre-repair chk claim strings kept verbatim.")
lines.append("")
lines.append("| file | sha1[:12] | bytes | notes |")
lines.append("|---|---|---|---|")

rows = []
for fn in sorted(os.listdir(HERE)):
    p = os.path.join(HERE, fn)
    if not os.path.isfile(p) or fn == "manifest.md":
        continue
    b = io.open(p, "rb").read()
    note = NOTES.get(fn, "")
    if fn in DEBRIS:
        note = "assembly debris (chain-120 S2b deaths)"
    if fn == "manifest_gen120.py":
        note = NOTES["manifest_gen120.py"]
    rows.append((fn, hashlib.sha1(b).hexdigest()[:12], len(b), note))
for fn, h, n, note in rows:
    lines.append("| %s | %s | %d | %s |" % (fn, h, n, note))
lines.append("| manifest.md | self: see run report | - | this file (self-hash cell per the 119 documented rule) |")
lines.append("")
txt = "\r\n".join(lines) + "\r\n"
io.open(os.path.join(HERE, "manifest.md"), "wb").write(txt.encode("ascii"))
print("MANIFEST OK 120: %d files tabled" % len(rows))
