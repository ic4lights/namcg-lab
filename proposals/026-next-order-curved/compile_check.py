"""Scratch compile of the proposed block OUTSIDE the repository: copies the manuscript to a temporary directory, inserts appH_insert.tex after the unique anchor
sentence (end of the 024 paragraph in sec:status-B), runs pdflatex twice and scans the log for undefined/multiply-defined references and errors."""
import shutil, subprocess, sys, os, re, tempfile
repo = r'C:\Users\redgi\Projects\namcg-lab'
tmp = sys.argv[1] if len(sys.argv) > 1 else tempfile.mkdtemp(prefix='build026_')
os.makedirs(tmp, exist_ok=True)
for name in ('chapters', 'frontmatter', 'bib', 'figs'):
    dst = os.path.join(tmp, name)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(os.path.join(repo, name), dst)
shutil.copy(os.path.join(repo, 'namcg-book7.tex'), tmp)
app = os.path.join(tmp, 'chapters', 'appH-microscopic-proofs.tex')
txt = open(app, 'rb').read().decode('utf-8')
anchor = "they treat neither edge modes of the symplectic gauge sector nor fermion edge modes, and they give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open."
assert txt.count(anchor) == 1, txt.count(anchor)
block = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'appH_insert.tex'), 'rb').read().decode('utf-8').replace('\r\n', '\n').strip('\n')
nl = '\r\n' if '\r\n' in txt else '\n'
block = block.replace('\n', nl)
txt = txt.replace(anchor, anchor + nl + nl + block, 1)
open(app, 'wb').write(txt.encode('utf-8'))
for p in (1, 2):
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'], cwd=tmp, capture_output=True, text=True)
    print('pass', p, 'returncode', r.returncode)
    if r.returncode != 0:
        print(r.stdout[-3000:])
        break
log = open(os.path.join(tmp, 'namcg-book7.log'), 'r', errors='ignore').read()
und = re.findall(r'(Reference `[^\']*\' on page \d+ undefined|Citation `[^\']*\' on page \d+ undefined)', log)
mult = re.findall(r'Label `[^\']*\' multiply defined', log)
print('undefined refs/cites:', len(und), und[:5])
print('multiply defined:', len(mult), mult[:5])
m = re.search(r'Output written on .*? \((\d+) pages', log)
print('pages:', m.group(1) if m else None)
print('build dir:', tmp)
