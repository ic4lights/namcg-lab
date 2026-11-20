# simulate_apply_091.py - read-only rehearsal of the integration: verifies the PRE contract of
# chapters/appH-microscopic-proofs.tex, splices insert-r1.tex between the 090 paragraph and
# \emph{Vacuum term.} IN MEMORY only, and reports POST invariants. Writes nothing.
# Run: python -I proposals/091-g-core-induced-pair-correlation/simulate_apply_091.py
import hashlib
A = "chapters/appH-microscopic-proofs.tex"
P = "proposals/091-g-core-induced-pair-correlation/insert-r1.tex"
raw = open(A, "rb").read()
ins = open(P, "rb").read()
print("PRE size:", len(raw), "CRLF:", raw.count(b"\r\n"), "bareLF:", raw.count(b"\n") - raw.count(b"\r\n"))
print("PRE sha256:", hashlib.sha256(raw).hexdigest())
pin = b"closes nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}"
k = raw.count(pin)
print("compound PIN count (expect 1):", k)
idx = raw.index(pin)
vt = idx + len(b"closes nothing in Problem~G.\r\n\r\n")
ls = raw.rfind(b"\n", 0, vt) + 1
print("'\\emph{Vacuum term.}' at line start:", raw[ls:vt] == b"")
pre_ok = (len(raw) == 756686 and raw.count(b"\r\n") == 3844 and raw.count(b"\n") == 3844
          and hashlib.sha256(raw).hexdigest() ==
          "068ce3f21139911ee7beccd6086b85a4ad18b19df683918ee4beb67b2963df38" and k == 1
          and raw[ls:vt] == b"")
print("insert bytes:", len(ins), "sha8:", hashlib.sha256(ins).hexdigest()[:8])
cut = idx + len(b"closes nothing in Problem~G.\r\n\r\n")
post = raw[:cut] + ins + b"\r\n" + raw[cut:]
print("POST size:", len(post), "expect", 756686 + len(ins) + 2)
print("POST CRLF:", post.count(b"\r\n"), "bareLF:", post.count(b"\n") - post.count(b"\r\n"))
print("POST sha256:", hashlib.sha256(post).hexdigest())
print("POST counts: verb-form", post.count(b"closes nothing in Problem~G."),
      "noun-form", post.count(b"close nothing in Problem~G."),
      "Vacuum-term", post.count(b"\\emph{Vacuum term.}"),
      "new-header", post.count(b"Eigenvalue reduction of the edge Gram"))
ok = pre_ok and len(post) == 756686 + len(ins) + 2 and post.count(b"\\emph{Vacuum term.}") == 2 \
     and post.count(b"Eigenvalue reduction of the edge Gram") == 1
print("SIMULATE 091:", "PASS" if ok else "FAIL")
