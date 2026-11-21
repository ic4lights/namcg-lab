# apply_102.py -- integrator apply for proposal 102 r2, integration ordinal 33.
# Pure binary splice of insert-r2.tex into chapters/appH-microscopic-proofs.tex at the
# PIN anchor, per review-r2 "Integration spec (final)". Writes ONLY that one file.
# Extracts the PIN constant from simulate_apply_102.py by AST parse (no execution).
# All PRE/PIN/POST assertions are checked BEFORE the single write; nothing is written
# unless every assertion passes. Run from repo root:
#   python -I proposals/102-g-profile-selection-output/apply_102.py
import ast
import hashlib
import os
import sys

ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
APP = os.path.join(ROOT, "chapters", "appH-microscopic-proofs.tex")
FOLDER = os.path.join(ROOT, "proposals", "102-g-profile-selection-output")
INSERT = os.path.join(FOLDER, "insert-r2.tex")
SIM = os.path.join(FOLDER, "simulate_apply_102.py")
SIMPOST = os.path.join(ROOT, "scratch", "102_sim_post.tex")

def sha16(data):
    return hashlib.sha256(data).hexdigest()[:16]

def report(name, value):
    print(name, "=", value)

def fail(msg):
    print("APPLY ABORT:", msg)
    sys.exit(1)

# --- extract PIN from the sim script without executing it ---
tree = ast.parse(open(SIM, "r", encoding="ascii").read(), filename=SIM)
pin = None
for node in tree.body:
    if isinstance(node, ast.Assign) and any(
        isinstance(t, ast.Name) and t.id == "PIN" for t in node.targets
    ):
        pin = ast.literal_eval(node.value)
if not isinstance(pin, bytes):
    fail("PIN not found in simulate_apply_102.py")
report("PIN extracted from simulate_apply_102.py (bytes)", len(pin))

# --- live appH PRE assertions ---
pre = open(APP, "rb").read()
report("PRE bytes", len(pre))
report("PRE sha256-16", sha16(pre))
report("PRE CRLF", pre.count(b"\r\n"))
report("PRE bareLF", pre.count(b"\n") - pre.count(b"\r\n"))
report("PRE BOM present", pre[:3] == b"\xef\xbb\xbf")
if len(pre) != 798457:
    fail("PRE size mismatch")
if sha16(pre) != "cfb6af516017367f6a22a9b0846df068c07e43e25d9ac8fad67c1d6497f5d438"[:16]:
    fail("PRE sha mismatch")
if pre.count(b"\r\n") != 3866:
    fail("PRE CRLF mismatch")
if pre.count(b"\n") - pre.count(b"\r\n") != 0:
    fail("PRE bareLF mismatch")
if pre[:3] == b"\xef\xbb\xbf":
    fail("PRE has BOM")

# --- PIN anchor ---
pin_count = pre.count(pin)
report("PIN count in appH bytes", pin_count)
if pin_count != 1:
    fail("PIN not unique")
cut = pre.find(pin) + len(pin)
head47 = pre[cut:cut + 47]
report("47 bytes after pin", head47)
if not head47.startswith(b"\\emph{Transport of the profile coordinate"):
    fail("wrong paragraph after pin")

# --- insert payload assertions ---
ins = open(INSERT, "rb").read()
report("insert-r2.tex bytes", len(ins))
report("insert-r2.tex sha8", hashlib.sha256(ins).hexdigest()[:8])
if len(ins) != 3173:
    fail("insert size mismatch")
if hashlib.sha256(ins).hexdigest()[:8] != "86d4b849":
    fail("insert sha8 mismatch")
if ins[:3] == b"\xef\xbb\xbf":
    fail("insert has BOM")
if any(b > 127 for b in ins):
    fail("insert not ASCII-only")
if ins.count(b"\n") != 1 or not ins.endswith(b"\r\n"):
    fail("insert not a single CRLF-terminated line")
if ins.count(b"\r\n") != 1:
    fail("insert CRLF count mismatch")

payload = ins + b"\r\n"  # insert line (CRLF-terminated) + one blank-CRLF separator
report("payload bytes (insert + blank-CRLF separator)", len(payload))
if len(payload) != 3175:
    fail("payload size mismatch")

# --- compute POST and assert everything BEFORE writing ---
post = pre[:cut] + payload + pre[cut:]
report("POST bytes (computed)", len(post))
report("POST sha256-16 (computed)", sha16(post))
report("POST CRLF (computed)", post.count(b"\r\n"))
report("POST bareLF (computed)", post.count(b"\n") - post.count(b"\r\n"))
report("POST == PRE + payload bytes", len(post) == len(pre) + len(payload))
report("PIN still count 1 in POST", post.count(pin))
if len(post) != 801632:
    fail("POST size mismatch")
if sha16(post) != "e37ca5385996df34166295642b9dd0ee2132cda2cc2c32f315f03d1c83b794d7"[:16]:
    fail("POST sha mismatch")
if post.count(b"\r\n") != 3868:
    fail("POST CRLF mismatch")
if post.count(b"\n") - post.count(b"\r\n") != 0:
    fail("POST bareLF mismatch")
if post.count(pin) != 1:
    fail("POST PIN count mismatch")
simpost = open(SIMPOST, "rb").read()
report("POST identical to scratch/102_sim_post.tex", post == simpost)
if post != simpost:
    fail("POST differs from simulated POST")

# --- guard: nothing changed on disk since PRE read (re-read once) ---
if open(APP, "rb").read() != pre:
    fail("appH changed on disk between read and write")

# --- the single binary write ---
with open(APP, "wb") as f:
    f.write(post)
report("WROTE", APP)

# --- verify live bytes ---
live = open(APP, "rb").read()
report("LIVE bytes after write", len(live))
report("LIVE sha256-16 after write", sha16(live))
report("LIVE == computed POST", live == post)
if live != post:
    fail("live bytes differ from computed POST")
print("APPLY PASS")
sys.exit(0)
