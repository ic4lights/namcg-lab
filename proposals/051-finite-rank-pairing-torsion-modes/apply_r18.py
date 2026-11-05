"""051 apply_r18: applies R18 of review-r2.md to appH_insert.tex, once.

Reads the old and new strings raw from review-r2.md.  Requires the current insert to have the r2 size and sha256, the old string
exactly once in it, and the result to have the expected size and sha256, LF, ASCII, no BOM.  Nothing is written on any mismatch.
On success keeps the r2 bytes as appH_insert.r2.tex, then writes appH_insert.tex.  A second run is refused, exit 2.
A mismatch exits 1.  Runs a self-test on a mutated old string before anything else."""
import hashlib
import os
import re
import sys

here = os.path.dirname(os.path.abspath(__file__))
REVIEW = os.path.join(here, 'review-r2.md')
INSERT = os.path.join(here, 'appH_insert.tex')
KEEP = os.path.join(here, 'appH_insert.r2.tex')
R2_SIZE, R2_SHA = 14148, 'b6ccbf5f8cbd2848413c3c1fddb7a6c112e52c103262c307d593c5cb45ef86dd'
R3_SIZE, R3_SHA = 14205, '94b4c128d5d16ffbad412d43aebb3f9566fc7de90758b600564cd9ef70b7dd2e'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fail(msg):
    print('REFUSED, nothing written:', msg)
    sys.exit(1)


def apply_once(data, old, new):
    n = data.count(old)
    if n != 1:
        return None, n
    return data.replace(old, new), n


if os.path.exists(KEEP):
    print('REFUSED: appH_insert.r2.tex already exists, R18 has been applied')
    sys.exit(2)

review = open(REVIEW, 'rb').read()
m = re.search(rb'\*\*R18\.\*\* Old[^\n]*\r?\n`([^`\r\n]+)`\r?\n\s*\r?\nNew:\r?\n`([^`\r\n]+)`', review)
if m is None:
    fail('R18 strings not found in review-r2.md')
old, new = m.group(1), m.group(2)
print('review-r2.md: old', len(old), 'bytes, new', len(new), 'bytes, delta', len(new) - len(old))
print('old:', old.decode('ascii'))
print('new:', new.decode('ascii'))

data = open(INSERT, 'rb').read()
print('current insert', len(data), 'bytes sha256', sha(data), 'CR', data.count(b'\r'))
if data.count(b'\r'):
    fail('current insert has CR bytes; line endings need review')
if len(data) != R2_SIZE or sha(data) != R2_SHA:
    fail('current insert is not the r2 bytes')

mutated, n = apply_once(data, old + b'X', new)
print('self-test, mutated old string: count', n, ', refused', mutated is None)
if mutated is not None:
    fail('self-test failed')

result, n = apply_once(data, old, new)
print('old string count in insert:', n)
if result is None:
    fail('old string must occur exactly once')
print('new string count in result:', result.count(new))
print('result', len(result), 'bytes sha256', sha(result))
print('ascii', all(b < 128 for b in result), 'CR', result.count(b'\r'), 'BOM', result[:3] == b'\xef\xbb\xbf')
if len(result) != R3_SIZE or sha(result) != R3_SHA:
    fail('result differs from the expected size or sha256')
if result.count(b'\r') or not all(b < 128 for b in result):
    fail('result is not LF ASCII')

with open(KEEP, 'xb') as f:
    f.write(data)
with open(INSERT, 'wb') as f:
    f.write(result)
print('kept', os.path.basename(KEEP), 'sha256', sha(open(KEEP, 'rb').read()))
print('wrote', os.path.basename(INSERT), 'sha256', sha(open(INSERT, 'rb').read()))
