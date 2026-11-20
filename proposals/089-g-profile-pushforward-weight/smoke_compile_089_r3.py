import hashlib,os,subprocess,re
P='proposals/089-g-profile-pushforward-weight/'
D='scratch/latex'
os.makedirs(D,exist_ok=True)
B=bytes([92])
def m(s): return B+s.encode()
PRE=(m('documentclass{article}')+b'\n'+m('usepackage{amsmath,amssymb}')+b'\n'
 +m('providecommand')+b'{'+m('dd')+b'}{{'+m('mathrm')+b'{d}}}'+b'\n'
 +m('begin{document}')+b'\n')
POST=m('end{document}')+b'\n'
for W in (PRE,POST):
    assert not [c for c in W if c<32 and c not in (10,13)], 'ctrl byte wrapper'
i3=open(P+'insert-r3.tex','rb').read()
i2=open(P+'insert-r2.tex','rb').read()
assert len(i3)==3974 and hashlib.sha256(i3).hexdigest()[:8]=='ccb89c9e'
assert len(i2)==3975 and hashlib.sha256(i2).hexdigest()[:8]=='bba6adc4'
def comp(name,ins):
    t=name+'.tex'
    buf=PRE+ins+POST
    assert not [c for c in buf if c<32 and c not in (10,13)], 'ctrl byte buffer'
    open(os.path.join(D,t),'wb').write(buf)
    p=os.path.join(D,name+'.log')
    if os.path.exists(p): os.remove(p)
    r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',t],cwd=D,capture_output=True)
    log=open(p,'rb').read() if os.path.exists(p) else b''
    return r.returncode, bool(re.search(rb'(?m)^! ',log)), log
rc,err,log=comp('smoke089',i3)
p1=(rc==0 and not err and b'invalid in math' not in log and b'undefined control' not in log)
rc2,err2,log2=comp('smoke089neg',i2)
p2=(rc2!=0 and err2 and (b'invalid in math' in log2 or b'mathaccent' in log2))
print('GATE insert-r3: rc=%d PASS=%s'%(rc,p1))
print('NEG-CONTROL insert-r2: rc=%d EXPECTED-FAIL=%s'%(rc2,p2))
print('SMOKE GATE','OK' if (p1 and p2) else 'PROBLEM')
