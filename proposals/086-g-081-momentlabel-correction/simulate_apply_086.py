"""086 simulate: read-only splice simulation for the L3177 clause fix.
Run: python -I proposals/086-g-081-momentlabel-correction/simulate_apply_086.py
Never writes to chapters/. Prints the new byte contract for integration.
"""
import hashlib

P = 'C:/Users/redgi/Projects/namcg-lab@gpu/chapters/appH-microscopic-proofs.tex'
BEFORE = rb'the fourth-moment excess drops from \(4.0\times10^{-3}\) to \(2.6\times10^{-4}\)'
AFTER = rb'the fourth-moment excess drops from \(6.7\times10^{-4}\) to \(4.3\times10^{-5}\)'

data = open(P, 'rb').read()
assert len(data) == 735695, len(data)
assert hashlib.sha256(data).hexdigest() == 'a13240a7f7a197ff7cffc26297fe1a6afbdeab749a4de57d6152828c573945ea'
crlf = data.count(b'\r\n')
assert crlf == 3834, crlf
assert data.count(b'\n') == crlf  # bareLF == 0
n = data.count(BEFORE)
assert n == 1, n
post = data.replace(BEFORE, AFTER, 1)
delta = len(AFTER) - len(BEFORE)
assert len(post) == len(data) + delta, (len(post), len(data), delta)
assert post.count(b'close nothing in Problem~G.') == 12, post.count(b'close nothing in Problem~G.')
pcrlf = post.count(b'\r\n')
assert pcrlf == 3834, pcrlf
assert post.count(b'\n') == pcrlf  # bareLF == 0
assert post != data
print(f"BEFORE occurrences: {n}; byte delta: {delta}")
print(f"POST size: {len(post)}")
print(f"POST sha256: {hashlib.sha256(post).hexdigest()}")
print(f"POST CRLF: {pcrlf}; bareLF: 0; close-idiom count: 12")
print("no write performed")
