# simulate_apply_091_r2.py - read-only r2 rehearsal: re-pins the LIVE appH bytes fresh, splices
# insert-r2.tex in memory, prints NEW POST contract. r1's POST sha is void. Writes nothing.
# Run: python -I proposals/091-g-core-induced-pair-correlation/simulate_apply_091_r2.py
import hashlib
A = "chapters/appH-microscopic-proofs.tex"
P = "proposals/091-g-core-induced-pair-correlation/insert-r2.tex"
raw = open(A, "rb").read()
ins = open(P, "rb").read()
print("PRE live size:", len(raw), "CRLF:", raw.count(b"\r\n"), "bareLF:", raw.count(b"\n") - raw.count(b"\r\n"))
print("PRE live sha256:", hashlib.sha256(raw).hexdigest())
print("PRE matches r1-pinned 068ce3f2.../756686:",
      len(raw) == 756686 and hashlib.sha256(raw).hexdigest().startswith("068ce3f2"))
pin = b"closes nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}"
k = raw.count(pin)
print("compound PIN count (expect 1):", k)
idx = raw.index(pin)
vt = idx + len(b"closes nothing in Problem~G.\r\n\r\n")
ls = raw.rfind(b"\n", 0, vt) + 1
print("'\\emph{Vacuum term.}' at line start:", raw[ls:vt] == b"")
print("insert-r2 bytes:", len(ins), "sha256:", hashlib.sha256(ins).hexdigest())
cut = idx + len(b"closes nothing in Problem~G.\r\n\r\n")
post = raw[:cut] + ins + b"\r\n" + raw[cut:]
print("POST size:", len(post), "expect", len(raw) + len(ins) + 2)
print("POST CRLF:", post.count(b"\r\n"), "bareLF:", post.count(b"\n") - post.count(b"\r\n"))
print("POST sha256:", hashlib.sha256(post).hexdigest())
print("POST counts: verb-form", post.count(b"closes nothing in Problem~G."),
      "noun-form", post.count(b"close nothing in Problem~G."),
      "Vacuum-term", post.count(b"\\emph{Vacuum term.}"),
      "new-header", post.count(b"Eigenvalue reduction of the edge Gram"))
ok = (k == 1 and raw[ls:vt] == b"" and len(ins) == 3749 and len(post) == len(raw) + 3751
      and post.count(b"\\emph{Vacuum term.}") == 2 and post.count(b"Eigenvalue reduction of the edge Gram") == 1)
print("SIMULATE 091 R2:", "PASS" if ok else "FAIL")
