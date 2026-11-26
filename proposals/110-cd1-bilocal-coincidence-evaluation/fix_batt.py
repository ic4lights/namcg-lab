import shutil, hashlib
NL = chr(10)
shutil.copyfile('run_induced.out', 'run_induced_r1_outdated.out')
def fix(f, old, new):
    t = open(f, 'rb').read().decode('utf-8')
    assert t.count(old) == 1, (f, t.count(old))
    open(f, 'wb').write(t.replace(old, new).encode('utf-8'))
old1 = '        + Fd0*eta*(Ud1[r]*Ed1[s] + Ud1[s]*Ed1[r])' + NL + '        + Fd0*eta*Ed2[(r, s)])'
new1 = '        + Fd0*eta*(Ud1[r]*Ed1[s] + Ud1[s]*Ed1[r])' + NL + '        + Fd1[r]*eta*Ed1[s] + Fd1[s]*eta*Ed1[r]' + NL + '        + Fd0*eta*Ed2[(r, s)])'
fix('check_induced_expansion.py', old1, new1)
old3 = '            + Fd0*sp.Rational(1, 2)*sp.simplify(' + NL + '                  sym(eta*(w[r-1]*w[s-1] + w[s-1]*w[r-1]))))'
new3 = '            + Fd0*sp.Rational(1, 2)*sp.simplify(' + NL + '                  sym(eta*(w[r-1]*w[s-1] + w[s-1]*w[r-1])))' + NL + '            + sp.simplify(sym(Fd1[r]*eta*Ed1[s] + Fd1[s]*eta*Ed1[r])))'
fix('check_induced_expansion_part3.py', old3, new3)
for f in ['check_induced_expansion.py','check_induced_expansion_part3.py','run_induced_r1_outdated.out']:
    print(hashlib.sha1(open(f,'rb').read()).hexdigest()[:12], f)
print('FIX OK')
