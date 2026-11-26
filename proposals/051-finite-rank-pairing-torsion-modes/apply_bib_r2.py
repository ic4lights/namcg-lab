"""051 round 2: delete the Kibble1961 entry from new_bib_entries.bib, keep Hehl2017, and append the Sakai2019 entry read
verbatim from the fenced block of review-r1.md.  The r1 bytes are kept as new_bib_entries.r1.bib.  A second run is refused."""
import hashlib
import os
import re
import sys

here = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(here, 'new_bib_entries.bib')
KEEP = os.path.join(here, 'new_bib_entries.r1.bib')
R1_SHA = '7119f251b3bfc37efa0b18c4a9e03c5d0b7259972e7762e996a10de2910cec60'


def refuse(msg):
    print('REFUSED, nothing written:', msg)
    sys.exit(2)


if os.path.exists(KEEP):
    refuse('new_bib_entries.r1.bib exists: already applied')
cur = open(BIB, 'rb').read()
if hashlib.sha256(cur).hexdigest() != R1_SHA:
    refuse('new_bib_entries.bib is not the r1 bytes')
review = open(os.path.join(here, 'review-r1.md'), 'rb').read().replace(b'\r\n', b'\n')
fences = re.findall(rb'```\n(@article\{Sakai2019,.*?\n\}\n)```', review, re.S)
if len(fences) != 1:
    refuse('Sakai2019 fenced block found %d times' % len(fences))
head, sep, tail = cur.partition(b'@article{Hehl2017,')
if not sep or not head.startswith(b'@article{Kibble1961,') or head.count(b'@article') != 1:
    refuse('r1 layout unexpected')
out = sep + tail + b'\n' + fences[0]
with open(KEEP, 'xb') as f:
    f.write(cur)
with open(BIB, 'wb') as f:
    f.write(out)
keys = re.findall(rb'@\w+\{([^,\s]+),', out)
print('keys', [k.decode() for k in keys], '; bytes', len(out), '; sha256', hashlib.sha256(out).hexdigest())
print('ascii', all(b < 128 for b in out), '; CR', out.count(b'\r'))
print('DONE')
