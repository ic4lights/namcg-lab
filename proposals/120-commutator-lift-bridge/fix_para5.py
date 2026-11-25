import hashlib, shutil
def pin(f):
    b = open(f, 'rb').read(); return hashlib.sha1(b).hexdigest()[:12], len(b)
shutil.copyfile('insert-commutator-lift-r1.tex', 'insert-commutator-lift-r1-superseded-r1.tex')
shutil.copyfile('gen_payload_120.py', 'gen_payload_120-superseded-r1.py')
print('OLD payload (copy shares old hash)', pin('insert-commutator-lift-r1-superseded-r1.tex'))
print('OLD gen   (copy shares old hash)', pin('gen_payload_120-superseded-r1.py'))
src = open('gen_payload_120.py', 'rb').read()
reps = [
    (rb"no quadratic shift-invariant term exists",
     rb"no shift-invariant term is a function of \(X\) at quadratic order, \(X\) itself being shift-variant"),
    (rb"at quartic order the \(X\)-free shift-invariant sector is one-dimensional, spanned by \(W_1=\operatorname{Tr}([\Phi,\Phi^\dagger])^2\) (checked at matrix sizes \(2,3\) over the conjugation-invariant families)",
     rb"at quartic order the shift-invariant sector of the checked conjugation-invariant family is four-dimensional, spanned by \(W_1=\operatorname{Tr}([\Phi,\Phi^\dagger])^2\) and three invariants of the traceless part \(\widetilde\Phi=\Phi-(\operatorname{Tr}\Phi/2)\,\mathbb I\) (checked at matrix size \(2\))"),
    (rb"so this lone quartic locks nothing",
     rb"so this quartic locks nothing"),
]
for old, new in reps:
    assert src.count(old) == 1, (old[:40], src.count(old))
    src = src.replace(old, new)
open('gen_payload_120.py', 'wb').write(src)
print('NEW gen', pin('gen_payload_120.py'))
