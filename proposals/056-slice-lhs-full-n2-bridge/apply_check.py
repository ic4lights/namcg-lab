# r2 apply check, REPORT MODE: computes the applied-file metrics in memory only.
# Never writes outside this folder. Run: python -I apply_check.py
import hashlib
SRC = 'C:/Users/redgi/Projects/namcg-lab@gpu/chapters/appH-microscopic-proofs.tex'
INS = 'C:/Users/redgi/Projects/namcg-lab@gpu/proposals/056-slice-lhs-full-n2-bridge/appH_insert.tex'
CRLF = b'\r\n'

def barelf(b):
    return sum(1 for x in b.replace(CRLF, b'') if x == 0x0A)

d = open(SRC, 'rb').read()
ins = open(INS, 'rb').read()
A = CRLF*4 + b'\x5cparagraph{Status.}' + CRLF + b'Remains Assumption~\x5cref{ass:lorentzian}.'
print('source size', len(d), 'sha256', hashlib.sha256(d).hexdigest())
print('source CRLF', d.count(CRLF), 'bare-LF', barelf(d))
print('anchor count', d.count(A), 'offset', d.find(A))
print('insert bytes', len(ins), 'sha256', hashlib.sha256(ins).hexdigest())
assert ins.endswith(b'\n') and b'\r' not in ins
t = ins.replace(b'\n', CRLF)
print('insert CRLF-normalized length', len(t))
out = d.replace(A, CRLF + CRLF + t + A, 1)
print('applied size', len(out), '(expected 542851:', len(out) == 542851, ')')
sha = hashlib.sha256(out).hexdigest()
print('applied sha256', sha)
print('matches gatekeeper 185bdcee...:', sha == '185bdcee9ae824e9c7fa7211c4280f56beb7f7210392f336592877f33112e73b')
print('applied CRLF', out.count(CRLF), '(3209+3 = 3212:', out.count(CRLF) == 3212, ')')
print('applied bare-LF', barelf(out), '(0:', barelf(out) == 0, ')')
print('delta', len(out) - len(d), '(6 + len(line) = 2502:', len(out) - len(d) == 2502, ')')
i = out.find(b'Slice bridge band')
print('200 bytes before new paragraph:', out[i-92:i-12])
