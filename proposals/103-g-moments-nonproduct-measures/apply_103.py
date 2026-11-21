# apply_103.py -- proposal 103 r1: integration splice (ordinal 34).
# Applies insert-r1.tex to chapters/appH-microscopic-proofs.tex at the G-block cut
# immediately AFTER the "Exact conditional diagonal law at D=3" paragraph (L3217) and
# BEFORE the "Vacuum term" paragraph, in binary mode, as a pure insertion.
# Modeled on simulate_apply_103.py (same folder) with PRE/POST assertions and the write.
# Run from repo root:
#   python -I proposals/103-g-moments-nonproduct-measures/apply_103.py
# Regional idiom (verified on live bytes, 2026-11-20): paragraphs in this block are
# separated by exactly ONE blank CRLF line; insert-r1.tex is one CRLF-terminated line
# (4205 B, sha8 1bd7af30), so the payload is the insert line plus one blank-CRLF separator.
# PIN (complete full preceding line + its CRLF + the blank-CRLF separator line) is BUILT
# PROGRAMMATICALLY from the live bytes by locating the line-initial header prefix; only the
# prefix and offsets are printed. PIN occurrence is asserted to be exactly 1.
# Gatekeeper ACCEPT spec (review-r1.md): PRE 801632 B / sha256-16 e37ca5385996df34 /
# CRLF 3868 / bareLF 0 / no BOM; POST 805839 B / sha256-16 21163962e4f7f514 / CRLF 3870 /
# bareLF 0 / PIN count 1 / byte-identical to scratch/103_sim_post.tex.
import hashlib
import os
import sys

APP = os.path.join("chapters", "appH-microscopic-proofs.tex")
FOLDER = os.path.join("proposals", "103-g-moments-nonproduct-measures")
INSERT = os.path.join(FOLDER, "insert-r1.tex")
SIM_POST = os.path.join("scratch", "103_sim_post.tex")

HEADER = rb"\emph{Exact conditional diagonal law at D=3.}"
NEXT_HEAD = rb"\emph{Vacuum term.}"

def sha16(data):
    return hashlib.sha256(data).hexdigest()[:16]

def fail(msg):
    print("STOP - no write performed:", msg)
    sys.exit(1)

def report(name, value):
    print(name, "=", value)

pre = open(APP, "rb").read()

report("PRE bytes", len(pre))
report("PRE sha256-16", sha16(pre))
report("PRE CRLF", pre.count(b"\r\n"))
report("PRE bareLF", pre.count(b"\n") - pre.count(b"\r\n"))
report("PRE BOM present", pre[:3] == b"\xef\xbb\xbf")

ok = (
    len(pre) == 801632
    and sha16(pre) == "e37ca5385996df34"
    and pre.count(b"\r\n") == 3868
    and pre.count(b"\n") - pre.count(b"\r\n") == 0
    and pre[:3] != b"\xef\xbb\xbf"
)
if not ok:
    fail("PRE contract mismatch")

# Build PIN from live bytes; print prefix + offsets only (context discipline).
report("header prefix occurrences in PRE", pre.count(HEADER))
if pre.count(HEADER) != 1:
    fail("header prefix not unique in live bytes")
idx = pre.find(HEADER)
line_start = pre.rfind(b"\r\n", 0, idx) + 2
report("header offset", idx)
report("line start offset", line_start)
if line_start != idx:
    fail("header is not line-initial")
line_end = pre.find(b"\r\n", idx)
report("line end offset (CRLF at)", line_end)
report("PIN line length bytes", line_end - line_start)
if line_end - line_start != 2846:
    fail("PIN line length != 2846")
PIN = pre[line_start:line_end + 2] + b"\r\n"  # complete line + CRLF + blank-CRLF separator
report("PIN bytes", len(PIN))
pin_count = pre.count(PIN)
report("PIN count in appH bytes", pin_count)
if pin_count != 1:
    fail("PIN not unique in live bytes")
report("PIN head 80 bytes", PIN[:80])
report("PIN tail 10 bytes", PIN[-10:])

cut = line_start + len(PIN)
head = pre[cut:cut + len(NEXT_HEAD)]
report("bytes at cut (expected Vacuum-term paragraph head)", head)
if not head.startswith(NEXT_HEAD):
    fail("wrong paragraph at cut")

ins = open(INSERT, "rb").read()
report("insert-r1.tex bytes", len(ins))
report("insert-r1.tex sha8", hashlib.sha256(ins).hexdigest()[:8])
report("insert-r1.tex sha256-16", sha16(ins))
if len(ins) != 4205 or hashlib.sha256(ins).hexdigest()[:16] != "1bd7af302d0e301e":
    fail("insert payload contract mismatch")
if ins.count(b"\r\n") != 1 or ins.count(b"\n") != 1:
    fail("insert is not a single CRLF-terminated line")
if ins[:3] == b"\xef\xbb\xbf" or not all(c < 128 for c in ins):
    fail("insert BOM or non-ASCII")

payload = ins + b"\r\n"  # insert line (CRLF-terminated) + one blank-CRLF separator
report("payload bytes (insert + blank-CRLF separator)", len(payload))
if len(payload) != 4207:
    fail("payload length != 4207")

post = pre[:cut] + payload + pre[cut:]

with open(APP, "wb") as f:
    f.write(post)
report("written", APP)

chk = open(APP, "rb").read()
report("POST bytes", len(chk))
report("POST sha256-16", sha16(chk))
report("POST CRLF", chk.count(b"\r\n"))
report("POST bareLF", chk.count(b"\n") - chk.count(b"\r\n"))
report("POST PIN count (expect 1)", chk.count(PIN))
report("POST == PRE + payload bytes", len(chk) == len(pre) + len(payload))
report("POST CRLF == PRE CRLF + 2", chk.count(b"\r\n") == pre.count(b"\r\n") + 2)
sim = open(SIM_POST, "rb").read()
report("sim_post bytes", len(sim))
report("sim_post sha256-16", sha16(sim))
report("POST byte-identical to scratch/103_sim_post.tex", chk == sim)

if (
    len(chk) == 805839
    and sha16(chk) == "21163962e4f7f514"
    and chk.count(b"\r\n") == 3870
    and chk.count(b"\n") - chk.count(b"\r\n") == 0
    and chk.count(PIN) == 1
    and chk == sim
):
    print("APPLY PASS")
    sys.exit(0)
fail("POST contract mismatch after write (restore from scratch/integrator-backup/034-103-g-moments-nonproduct-measures/)")
