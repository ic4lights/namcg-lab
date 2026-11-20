# simulate_apply_101.py -- item 101: apply the insert to a TEMPORARY COPY of chapters/appH (outside
# the repository; chapters/ is never written). Verifies the POST contract and prints the full POST
# sha256 so the gatekeeper can reproduce the splice independently. Ends with "no write performed".
import hashlib, os, sys, tempfile
src = os.path.abspath("../../chapters/appH-microscopic-proofs.tex")
pre = open(src, "rb").read()
ins = open("insert-r1.tex", "rb").read()
if len(pre) != 795607 or not hashlib.sha256(pre).hexdigest().startswith("3f1b030c"):
    print("PRE contract mismatch -- refusing"); sys.exit(1)
anch = b"close nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}"
assert pre.count(anch) == 1, "anchor not unique"
pos = pre.find(anch) + len(b"close nothing in Problem~G.\r\n")
post = pre[:pos] + ins + pre[pos:]
tmp = os.path.join(tempfile.gettempdir(), "appH_sim_101_post.tex")
open(tmp, "wb").write(post)
back = open(tmp, "rb").read(); os.remove(tmp)
ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name); ok = ok and cond
chk("POST size 798293", len(post) == 798293)
chk("POST round-trips temp copy", back == post)
chk("POST idiom 27", post.count(b"close nothing in Problem~G.") == 27)
chk("POST Vacuum 2", post.count(b"\\emph{Vacuum term.}") == 2)
chk("POST anchor 1", post.count(anch) == 1)
chk("POST oldseam 0", post.count(b"and they close nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}") == 0)
chk("POST CRLF 3865, bareLF 0", post.count(b"\r\n") == 3865 and post.count(b"\n") == post.count(b"\r\n"))
i = post.find(b"\\emph{Exact conditional diagonal law at D=3.}")
chk("POST insert followed by blank line then Vacuum", post[i+len(ins):i+len(ins)+22] == b"\r\n\\emph{Vacuum term.}" and post[i-2:i] == b"\r\n\r\n")
chk("POST unchanged outside splice", post[:pos] == pre[:pos] and post[pos+2686+28-28:] == pre[pos-0:])
print("POST size:", len(post), "POST sha256:", hashlib.sha256(post).hexdigest())
print("no write performed" if ok else "SIMULATION FAILURES")
sys.exit(0 if ok else 1)
