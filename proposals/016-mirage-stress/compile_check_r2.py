import shutil, os, subprocess, re
R = r'C:\Users\redgi\Projects\namcg-lab'
S = r'C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\4d0177a0-6b3d-45ad-bb6d-645d2be99f00\scratchpad\bk'
if os.path.exists(S):
    shutil.rmtree(S)
shutil.copytree(R, S, ignore=shutil.ignore_patterns('.git', 'proposals', 'reports', 'scratch'))
p = os.path.join(S, 'chapters', 'appH-microscopic-proofs.tex')
s = open(p, 'rb').read().decode('utf8')
blk = open(R + r'\proposals\016-mirage-stress\block-r2.tex', encoding='utf8').read().replace('\r\n', '\n').replace('\n', '\r\n')
a = '\\section{Problem G: HBEV}'
assert s.count(a) == 1
open(p, 'wb').write(s.replace(a, blk + a).encode('utf8'))
for i in range(2):
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'], cwd=S, capture_output=True)
    print('pass', i, r.returncode)
log = open(os.path.join(S, 'namcg-book7.log'), encoding='latin1').read()
print('undefined/multiply:', len(re.findall(r'undefined|multiply', log, re.I)))
print([l for l in log.splitlines() if l.startswith('!')][:5])
print('Output written' in log, re.findall(r'Output written.*', log))
