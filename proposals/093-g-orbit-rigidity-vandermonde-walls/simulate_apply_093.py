# simulate_apply_093.py -- proposal 093, round 1. Run from repo root:
#   python -I proposals/093-g-orbit-rigidity-vandermonde-walls/simulate_apply_093.py
# Reads the live appH, verifies the PRE byte contract, computes the POST bytes in
# memory only, and prints the POST contract. Performs NO writes anywhere.
import hashlib

APP = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/093-g-orbit-rigidity-vandermonde-walls/insert-r1.tex"
pre = open(APP, "rb").read()
insert = open(INS, "rb").read()

print("PRE size:", len(pre), "sha256:", hashlib.sha256(pre).hexdigest())
assert len(pre) == 765074, "PRE size mismatch"
assert hashlib.sha256(pre).hexdigest().startswith("b1b62410229383c1"), "PRE sha mismatch"
crlf_pre = pre.count(b"\r\n")
bare_pre = sum(1 for i, b in enumerate(pre) if b == 0x0A and (i == 0 or pre[i - 1] != 0x0D))
print("PRE CRLF:", crlf_pre, "bareLF:", bare_pre)
assert crlf_pre == 3848 and bare_pre == 0

PIN = (b"they do not fix the state that sets \\(W\\), \\(g\\), \\(s\\) or the frame, "
       b"they leave the missing steps (i)-(iv) of the Missing step paragraph unchanged, "
       b"and they close nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}")
n_pin = pre.count(PIN)
print("compound PIN count:", n_pin)
assert n_pin == 1, "PIN must occur exactly once"
gap = pre[pre.index(PIN) + len(PIN) - len(b"\\emph{Vacuum term.}") - 4:
          pre.index(PIN) + len(PIN) - len(b"\\emph{Vacuum term.}")]
print("gap between 092 tail and Vacuum header == CRLFCRLF:", gap == b"\r\n\r\n")
cut = pre.index(b"\\emph{Vacuum term.}", pre.index(PIN))
assert pre[cut - 4:cut] == b"\r\n\r\n"

post = pre[:cut] + insert + pre[cut:]
print("POST size:", len(post), "sha256:", hashlib.sha256(post).hexdigest())
print("POST CRLF:", post.count(b"\r\n"), "bareLF:",
      sum(1 for i, b in enumerate(post) if b == 0x0A and (i == 0 or post[i - 1] != 0x0D)))
print("POST noun-idiom count (close nothing in Problem~G.):", post.count(b"close nothing in Problem~G."))
print("POST verb-idiom count (closes nothing):", post.count(b"closes nothing"))
print("POST \\emph{Vacuum term.} count:", post.count(b"\\emph{Vacuum term.}"))
print("POST new-header count:", post.count(b"Quantitative orbit rigidity"))
assert post[:cut] == pre[:cut] and post[cut + len(insert):] == pre[cut:]
assert post[cut - 4:cut] == b"\r\n\r\n" and post[cut:cut + len(insert)] == insert
print("SIMULATE OVERALL: PASS")
print("no write performed")
