# simulate_apply_091_r3.py - read-only r3 rehearsal: re-pins LIVE appH fresh (STOP-flag if not
# 756686/068ce3f2.../CRLF3844/bareLF0), splices insert-r3.tex in memory, prints NEW POST
# contract. r1/r2 POST hashes are VOID. Writes nothing.
# Run: python -I proposals/091-g-core-induced-pair-correlation/simulate_apply_091_r3.py
import hashlib
A = "chapters/appH-microscopic-proofs.tex"
P = "proposals/091-g-core-induced-pair-correlation/insert-r3.tex"
raw = open(A, "rb").read()
ins = open(P, "rb").read()
print("PRE live size:", len(raw), "CRLF:", raw.count(b"\r\n"), "bareLF:", raw.count(b"\n") - raw.count(b"\r\n"))
print("PRE live sha256:", hashlib.sha256(raw).hexdigest())
pre_ok = (len(raw) == 756686 and hashlib.sha256(raw).hexdigest() ==
          "068ce3f21139911ee7beccd6086b85a4ad18b19df683918ee4beb67b2963df38"
          and raw.count(b"\r\n") == 3844 and raw.count(b"\n") == 3844)
print("PRE matches pinned 756686/068ce3f2.../CRLF3844/bareLF0:", pre_ok)
pin = b"closes nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}"
k = raw.count(pin)
idx = raw.index(pin)
vt = idx + len(b"closes nothing in Problem~G.\r\n\r\n")
ls = raw.rfind(b"\n", 0, vt) + 1
print("compound PIN count (expect 1):", k, "| Vacuum-term at line start:", raw[ls:vt] == b"")
print("insert-r3 bytes:", len(ins), "sha256:", hashlib.sha256(ins).hexdigest())
cut = idx + len(b"closes nothing in Problem~G.\r\n\r\n")
post = raw[:cut] + ins + b"\r\n" + raw[cut:]
print("POST size:", len(post), "expect", len(raw) + len(ins) + 2)
print("POST CRLF:", post.count(b"\r\n"), "bareLF:", post.count(b"\n") - post.count(b"\r\n"))
print("POST sha256:", hashlib.sha256(post).hexdigest())
print("POST counts: verb-form", post.count(b"closes nothing in Problem~G."),
      "noun-form", post.count(b"close nothing in Problem~G."),
      "Vacuum-term", post.count(b"\\emph{Vacuum term.}"),
      "new-header", post.count(b"Eigenvalue reduction of the edge Gram"))
ok = pre_ok and k == 1 and raw[ls:vt] == b"" and len(ins) == 3840 and len(post) == len(raw) + 3842 \
     and post.count(b"\\emph{Vacuum term.}") == 2 and post.count(b"Eigenvalue reduction of the edge Gram") == 1
print("SIMULATE 091 R3:", "PASS" if ok else "FAIL")
