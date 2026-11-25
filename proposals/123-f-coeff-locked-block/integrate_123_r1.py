# Integrator splice script, ordinal 51, proposal 123-f-coeff-locked-block.
# Byte-level only. No regex. No text-mode I/O. Never touches git.
# Pre-image must be sha1 d2af19df0f998ce150c12ea11af9ea8c0387435f (863831 B).
# Payload sha1 e0b8d6b31cad8b34fe1f3764ea151df47e1e562f (5442 B).
# Expected POST sha1 ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1 (869275 B).
import hashlib, sys

APP = r"chapters/appH-microscopic-proofs.tex"
PAY = r"proposals/123-f-coeff-locked-block/payload-123.txt"
PRE_SHA = "d2af19df0f998ce150c12ea11af9ea8c0387435f"
PAY_SHA = "e0b8d6b31cad8b34fe1f3764ea151df47e1e562f"
POST_SHA = "ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1"

def sha1(b): return hashlib.sha1(b).hexdigest()
def die(msg):
    print("FAIL:", msg); sys.exit(1)

app = open(APP, "rb").read()
pay = open(PAY, "rb").read()
if sha1(app) != PRE_SHA: die("pre-image sha mismatch %s" % sha1(app))
if len(app) != 863831: die("pre-image size %d" % len(app))
if sha1(pay) != PAY_SHA: die("payload sha mismatch %s" % sha1(pay))
if len(pay) != 5442: die("payload size %d" % len(pay))
if not pay.endswith(b"\r\n"): die("payload not CRLF-terminated")

CRLF = b"\r\n"
sec = b"\\section{Problem G: HBEV}"
n_sec = app.count(sec)
print("count('\\section{Problem G: HBEV}'):", n_sec)
if n_sec != 1: die("section marker not unique")
i = app.find(sec)
if app[i-4:i] != b"\r\n\r\n": die("no CRLFCRLF before section")
end = i - 4                      # sentence line ends at index end (exclusive)
start = app.rfind(b"\r\n", 0, end - 1) + 2
sent = app[start:end]
tail_ok = sent.endswith(b"Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.")
print("closing-sentence tail ok:", tail_ok, "| sent bytes:", len(sent))
if not tail_ok: die("anchor sentence does not end with expected close")

anchor_ctx = sent + b"\r\n\r\n"
n = app.count(anchor_ctx)
print("anchor_ctx count:", n)
if n != 1: die("anchor context not unique")

new = app.replace(anchor_ctx, anchor_ctx + pay + CRLF, 1)
print("new len:", len(new), "expected:", 863831 + 5442 + 2)
if len(new) != 869275: die("post length %d" % len(new))
if sha1(new) != POST_SHA: die("post sha %s" % sha1(new))

open(APP, "wb").write(new)
chk = open(APP, "rb").read()
print("WROTE. verify sha:", sha1(chk), "len:", len(chk))
if sha1(chk) != POST_SHA or len(chk) != 869275: die("post-write verify failed")
print("SPLICE OK")
