# simulate_apply_103.py -- proposal 103 r1: simulation of the integration splice.
# Applies insert-r1.tex to an IN-MEMORY copy of chapters/appH-microscopic-proofs.tex at the
# G-block cut immediately AFTER the "Exact conditional diagonal law at D=3" paragraph (item
# 101, L3217) and BEFORE the "Vacuum term" paragraph, and writes the simulated POST ONLY to
# scratch/103_sim_post.tex (git-ignored). Never writes under chapters/. Run from repo root:
#   python -I proposals/103-g-moments-nonproduct-measures/simulate_apply_103.py
# Regional idiom (verified on live bytes, 2026-11-20): paragraphs in this block are
# separated by exactly ONE blank CRLF line; insert-r1.tex is one CRLF-terminated line
# (4205 B, sha8 1bd7af30), so the payload is the insert line plus one blank-CRLF separator.
# Anchor rationale (see findings.md section 6.8): pure insertion after L3191 or L3197 would
# silently re-point downstream "Nth preceding paragraph" ordinals (L3193, L3199, L3203,
# L3205, L3207, L3209, L3211, L3215); the only pure-insertion slots that break no ordinal
# are after L3217 and after L3219. Chosen: after L3217, inside the orchestrator-approved
# span "after the integrated 102 paragraph and before the block closer".
# PIN (complete full preceding line + its CRLF + the blank-CRLF separator line) is BUILT
# PROGRAMMATICALLY from the live bytes by locating the line-initial header prefix; only the
# prefix and offsets are printed. PIN occurrence is asserted to be exactly 1.
import hashlib
import os
import sys

APP = os.path.join("chapters", "appH-microscopic-proofs.tex")
FOLDER = os.path.join("proposals", "103-g-moments-nonproduct-measures")
INSERT = os.path.join(FOLDER, "insert-r1.tex")

HEADER = rb"\emph{Exact conditional diagonal law at D=3.}"
NEXT_HEAD = rb"\emph{Vacuum term.}"

def sha16(data):
    return hashlib.sha256(data).hexdigest()[:16]

pre = open(APP, "rb").read()

def report(name, value):
    print(name, "=", value)

report("PRE bytes", len(pre))
report("PRE sha256-16", sha16(pre))
report("PRE CRLF", pre.count(b"\r\n"))
report("PRE bareLF", pre.count(b"\n") - pre.count(b"\r\n"))
report("PRE BOM present", pre[:3] == b"\xef\xbb\xbf")

ok = (
    len(pre) == 801632
    and sha16(pre).startswith("e37ca5385996df34")
    and pre.count(b"\r\n") == 3868
    and pre.count(b"\n") - pre.count(b"\r\n") == 0
    and pre[:3] != b"\xef\xbb\xbf"
)
if not ok:
    print("PRE MISMATCH")
    sys.exit(1)

# Build PIN from live bytes; print prefix + offsets only (context discipline).
idx = pre.find(HEADER)
report("header prefix occurrences in PRE", pre.count(HEADER))
if pre.count(HEADER) != 1:
    print("PRE MISMATCH (header prefix not unique)")
    sys.exit(1)
line_start = pre.rfind(b"\r\n", 0, idx) + 2
report("header offset", idx)
report("line start offset", line_start)
if line_start != idx:
    print("PRE MISMATCH (header is not line-initial)")
    sys.exit(1)
line_end = pre.find(b"\r\n", idx)
report("line end offset (CRLF at)", line_end)
report("PIN line length bytes", line_end - line_start)
PIN = pre[line_start:line_end + 2] + b"\r\n"  # complete line + CRLF + blank-CRLF separator
report("PIN bytes", len(PIN))
pin_count = pre.count(PIN)
report("PIN count in appH bytes", pin_count)
if pin_count != 1:
    print("PRE MISMATCH (PIN not unique)")
    sys.exit(1)
report("PIN head 80 bytes", PIN[:80])
report("PIN tail 10 bytes", PIN[-10:])

cut = line_start + len(PIN)
head = pre[cut:cut + len(NEXT_HEAD)]
report("bytes at cut (expected Vacuum-term paragraph head)", head)
if not head.startswith(NEXT_HEAD):
    print("PRE MISMATCH (wrong paragraph at cut)")
    sys.exit(1)

ins = open(INSERT, "rb").read()
report("insert-r1.tex bytes", len(ins))
report("insert-r1.tex sha8", hashlib.sha256(ins).hexdigest()[:8])
if len(ins) != 4205 or hashlib.sha256(ins).hexdigest()[:8] != "1bd7af30":
    print("PRE MISMATCH (insert payload)")
    sys.exit(1)
if ins.count(b"\r\n") != 1 or ins.count(b"\n") != 1:
    print("PRE MISMATCH (insert not a single CRLF-terminated line)")
    sys.exit(1)

payload = ins + b"\r\n"  # insert line (CRLF-terminated) + one blank-CRLF separator
report("payload bytes (insert + blank-CRLF separator)", len(payload))
post = pre[:cut] + payload + pre[cut:]
report("POST bytes", len(post))
report("POST sha256-16", sha16(post))
report("POST CRLF", post.count(b"\r\n"))
report("POST bareLF", post.count(b"\n") - post.count(b"\r\n"))
report("POST == PRE + payload bytes", len(post) == len(pre) + len(payload))
report("POST CRLF == PRE CRLF + 2", post.count(b"\r\n") == pre.count(b"\r\n") + 2)
report("PIN still count 1 in POST", post.count(PIN))

os.makedirs("scratch", exist_ok=True)
out = os.path.join("scratch", "103_sim_post.tex")
with open(out, "wb") as f:
    f.write(post)
report("simulated POST written to", out)

if (
    len(post) == len(pre) + len(payload)
    and post.count(b"\n") - post.count(b"\r\n") == 0
    and post.count(PIN) == 1
):
    print("SIMULATION PASS")
    sys.exit(0)
print("SIMULATION FAIL")
sys.exit(1)
