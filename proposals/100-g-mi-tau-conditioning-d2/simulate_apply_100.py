# simulate_apply_100.py -- READ-ONLY simulation of the integration byte contract for item 100
# r1. Prints the full POST invariants; writes nothing. Run:
# python -I proposals/100-g-mi-tau-conditioning-d2/simulate_apply_100.py
import hashlib
D = "C:/Users/redgi/Projects/namcg-lab@gpu/"
A = D + "chapters/appH-microscopic-proofs.tex"
INS = D + "proposals/100-g-mi-tau-conditioning-d2/insert-r1.tex"
d = open(A, "rb").read()
ins = open(INS, "rb").read()
post = d[:756799] + ins + b"\r\n" + d[756799:]
hdr = ins[: ins.index(b"}") + 1].decode()
print("PRE bytes=%d crlf=%d bareLF=%d sha256=%s"
      % (len(d), d.count(b"\r\n"), d.replace(b"\r\n", b"").count(b"\n"), hashlib.sha256(d).hexdigest()))
print("ins bytes=%d sha256=%s" % (len(ins), hashlib.sha256(ins).hexdigest()))
print("POST bytes=%d crlf=%d bareLF=%d sha256=%s"
      % (len(post), post.count(b"\r\n"), post.replace(b"\r\n", b"").count(b"\n"), hashlib.sha256(post).hexdigest()))
print("POST checks: idiom=%d closesverb=%d vacuum=%d hdr=%d adjacency=%d oldseam=%d"
      % (post.count(b"close nothing in Problem~G."), post.count(b"closes nothing"),
         post.count(b"\\emph{Vacuum term.}"), post.decode("latin-1").count(hdr),
         post.count(b"Problem~G.\r\n\r\n" + ins[:12]),
         post.count(b"and they close nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}")))
print("expected POST bytes 793616+%d+2, crlf 3864, idiom 26, closesverb 1, vacuum 2, hdr 1, adjacency 1, oldseam 0" % len(ins))
print("no write performed")
