# simulate_apply_101_r2.py -- item 101 round 2: splice insert-r2.tex (+ one added CRLF) into a
# TEMPORARY COPY of the LIVE chapters/appH bytes (chapters/ is never written). Anchor: after the
# unique b"close nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}". Prints the full POST sha256;
# reproduction: post = pre[:pos] + ins + b"\r\n" + pre[pos:] with pos = find(anchor)+len("...G.\r\n\r\n").
import hashlib, os, sys, tempfile
src = os.path.abspath("../../chapters/appH-microscopic-proofs.tex")
pre = open(src, "rb").read()
ins = open("insert-r2.tex", "rb").read()
if len(pre) != 795607 or not hashlib.sha256(pre).hexdigest().startswith("3f1b030c"):
    print("PRE contract mismatch -- STOP and report"); sys.exit(1)
anch = b"close nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}"
assert pre.count(anch) == 1, "anchor not unique"
pos = pre.find(anch) + len(b"close nothing in Problem~G.\r\n\r\n")
post = pre[:pos] + ins + b"\r\n" + pre[pos:]
tmp = os.path.join(tempfile.gettempdir(), "appH_sim_101_r2_post.tex")
open(tmp, "wb").write(post)
back = open(tmp, "rb").read(); os.remove(tmp)
ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name); ok = ok and cond
L = len(ins)
chk("POST size 798457", len(post) == 795607 + L + 2)
chk("POST round-trips temp copy", back == post)
chk("POST idiom 27", post.count(b"close nothing in Problem~G.") == 27)
chk("POST Vacuum 2", post.count(b"\\emph{Vacuum term.}") == 2)
chk("POST oldseam 0", post.count(b"and they close nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}") == 0)
chk("POST CRLF 3866, bareLF 0", post.count(b"\r\n") == 3866 and post.count(b"\n") == post.count(b"\r\n"))
i = post.find(b"\\emph{Exact conditional diagonal law at D=3.}")
chk("blank line before insert", post[i-4:i] == b"\r\n\r\n")
chk("blank line after insert then Vacuum", post[i+L:i+L+21] == b"\r\n\\emph{Vacuum term.}")
chk("insert header unique", post.count(b"\\emph{Exact conditional diagonal law at D=3.}") == 1)
chk("unchanged outside splice", post[:pos] == pre[:pos] and post[pos+L+2:] == pre[pos:])
print("POST size:", len(post), "POST sha256:", hashlib.sha256(post).hexdigest())
print("no write performed" if ok else "SIMULATION FAILURES")
sys.exit(0 if ok else 1)
