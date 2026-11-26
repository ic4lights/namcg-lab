# r2_assemble.py - assembles proposal-r2.md from scratch parts + programmatic fenced insert copy.
# Re-run: python -I proposals/076-g-edge-uqstack-selrule/r2_assemble.py  (repo root)
# Expected: "ASSEMBLED <path> <bytes>" ; deletes scratch parts.
import hashlib, os

INS = "proposals/076-g-edge-uqstack-selrule/insert-r1.tex"
OUT = "proposals/076-g-edge-uqstack-selrule/proposal-r2.md"
PARTS = [f"scratch/076-r2-part{i}.md" for i in (1, 2, 3)]

ins = open(INS, "rb").read()
assert ins.endswith(b"\r\n") and ins.count(b"\r") == 1
content = ins[:-2]  # minus terminal CRLF
sha = hashlib.sha256(content).hexdigest()

head = (
    "\r\n## Insert copy (fenced; byte-identical to insert-r1.tex minus terminal CRLF)\r\n\r\n"
    "Programmatic embed of proposals/076-g-edge-uqstack-selrule/insert-r1.tex "
    f"(3,350 B incl. terminal CRLF; content {len(content)} B, sha256 {sha}). "
    "The integrator takes insert-r1.tex itself as authoritative; this block exists "
    "for review convenience and is checked for byte equality by r2_bytecheck.py.\r\n\r\n"
    "```latex\r\n"
).encode()
tail = b"\r\n```\r\n"

buf = b""
for p in PARTS:
    d = open(p, "rb").read().replace(b"\n", b"\r\n").replace(b"\r\r\n", b"\r\n")
    if not d.endswith(b"\r\n"):
        d += b"\r\n"
    buf += d + b"\r\n"
buf += head + content + tail
open(OUT, "wb").write(buf)
print(f"ASSEMBLED {OUT} {len(buf)} sha256 {hashlib.sha256(buf).hexdigest()}")
for p in PARTS:
    os.remove(p)
print("parts deleted")
