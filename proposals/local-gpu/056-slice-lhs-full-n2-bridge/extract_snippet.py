# Extract the gatekeeper's Corrected snippet from review-r1.md byte-exactly and
# write it as appH_insert.tex (single line, LF, trailing newline). ASCII check.
import hashlib
rev = open('review-r1.md', 'rb').read()
start = rev.find(b'```latex')
assert start != -1
nl = rev.find(b'\n', start)
body_start = nl + 1
end = rev.find(b'```', body_start)
assert end != -1
line = rev[body_start:end]
if line.endswith(b'\r'):
    line = line[:-1]
if line.endswith(b'\n'):
    line = line[:-1]
assert b'\n' not in line and b'\r' not in line, 'snippet must be one line'
assert all(b < 128 for b in line), 'snippet must be ASCII'
out = line + b'\n'
open('appH_insert.tex', 'wb').write(out)
print('len(line) =', len(line), ' (gatekeeper predicts delta 2502 = 6 + len(line))')
print('sha256(line LF) =', hashlib.sha256(out).hexdigest())
print('CRLF-normalized insert length =', len(line) + 2)
