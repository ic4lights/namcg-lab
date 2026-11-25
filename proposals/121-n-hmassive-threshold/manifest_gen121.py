# manifest_gen121.py - writes manifest.md (sha1[:12], size) for every folder file.
# Run: python -I manifest_gen121.py    (from the folder or repo root)
import os, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
NOTES = {
 'proposal-r1.md': 'round 1 proposal (final this round; payload spliced verbatim)',
 'insert-n-hmassive-threshold.tex': 'PAYLOAD as proposed; unchanged since gen r2 (702a60d1e5dc)',
 'gen_payload_121.py': 'generator r2 (e431049cf73c); r1 crash lineage in out-gen121-r1.txt',
 'verify121.py': 'FINAL verify pack = scratch v11 (d04bf3101e0c); supersedes 655227e3b3f3 (archived scratch/121/verify121_folder_pre_v8.py)',
 'appH-spliced-preview.tex': 'gen r2 whole-file preview at anchor (fd23c0d737b0; POST 857778)',
 'out-gen121-r1.txt': 'gen r1 traceback: single-backslash guard regex (lineage)',
 'out-gen121-r2.txt': 'gen r2 GEN121 OK, 5 controls fired, PRE 854131 POST 857778',
 'out-verify121-r1.txt': 'old verify (pre-v8), S11 SKIP payload-absent (lineage)',
 'out-verify121-r2.txt': 'v8 in-folder run: S11 dead-guard crash (lineage)',
 'out-verify121-r3.txt': 'v9 run: S11 FAIL scanner-token bug (lineage)',
 'out-verify121-r4.txt': 'v10 run: S11 FAIL wrong CRLF control (lineage)',
 'out-verify121-r5.txt': 'FINAL v11 run: TOTAL 12/12 PASS, S11 ACTIVE',
 'manifest_gen121.py': 'this script',
 'manifest.md': 'output of this script',
}
L = ['# Manifest 121-n-hmassive-threshold', '',
     'Live-tree pins at assembly: appH sha1[:12] f5a761c55396 / 854131; anchor'
     ' Problems~F and~N remain open. count 1 (appH line 4064, sec:status-N).'
     ' Cert capture scratch/121/out-cert-r121p-r1.txt: CERT PASS (2 passes rc 0,'
     ' exclam 0 undefrefs 0 multidef 0).', '',
     '| file | sha1[:12] | bytes | note |', '|---|---|---|---|']
for f in sorted(os.listdir(HERE)):
    p = os.path.join(HERE, f)
    if not os.path.isfile(p) or f in ('manifest.md',):
        continue
    b = open(p, 'rb').read()
    L.append('| %s | %s | %d | %s |' % (f, hashlib.sha1(b).hexdigest()[:12], len(b),
                                        NOTES.get(f, '')))
open(os.path.join(HERE, 'manifest.md'), 'wb').write(('\r\n'.join(L)).encode('ascii') + '\r\n'.encode())
print('manifest written; entries:', len(L) - 6)
