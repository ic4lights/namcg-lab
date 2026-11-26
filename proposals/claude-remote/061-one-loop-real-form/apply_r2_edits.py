"""061 r2 edits: F1 (option a), F2, F3, F4 verbatim from review-r1, F5 (Spin(5)) adopted.
Checks the r1 hash and that each old and new string occurs exactly once. Backslashes via chr(92).
Writes only appH_insert.tex in this folder."""
import hashlib, os
BS=chr(92); HERE=os.path.dirname(os.path.abspath(__file__))
p=os.path.join(HERE,'appH_insert.tex')
b=open(p,'rb').read()
assert hashlib.sha256(b).hexdigest()=='a5039fc349eff965bfa144a3ec4d634d7f5e738d6b9e7c7f079ae5747c41f493','r1 hash mismatch'
s=b.decode('ascii')
L=lambda x: x.replace('@',BS)
edits=[
('F1',L("These include the conjugate-coordinate member, whose kinetic tensor is Lorentzian on @(m@neq0@), and the base-coordinate member, whose fibre-averaged tensor is positive definite for @(0<m^2<2@ell^2@). If their fermion forms are non-degenerate, the supplied fermion content, and not the bosonic action, separates the compact real form from the non-compact ones at one loop, and it does not by itself select a Lorentzian kinetic tensor."),
 L("At fixed @(@gamma>0@) and @(h_0@) of signature @((9,1)@) the identity of the preceding paragraph admits, besides @(@mathfrak{so}(5)@), only the five-index algebra @(@mathfrak{so}(4,1)@) with @(W@) timelike, among them the conjugate-coordinate member, whose kinetic tensor is Lorentzian on @(m@neq0@); the base-coordinate member requires @(@gamma<0@) there. If the fermion forms of these members are non-degenerate, the supplied fermion content, and not the bosonic action, separates them from the compact members at one loop; the Lorentzian kinetic tensor is then fixed by the supplied sign of @(@gamma@), @(h_0@) and fermion content, not derived, and is not identified with the emergent metric.")),
('F2a',L("For a kinetic form @(K=k^{@mathrm T}@mathsf Kk@) of signature @((3,1)@) on flat momenta"),L("For @(K=-k_0^2+|@vec k|^2@) on flat momenta")),
('F2b',L("for a positive definite @(K@) over the same region"),L("for @(K=k_0^2+|@vec k|^2@) over the same region")),
('F3',"so the sign of the fluctuation spectrum does not distinguish the members","so the sign of the fluctuation spectrum does not distinguish the moduli of the members' contributions"),
('F4',L("@(34@), @(120@) and @(340@) negative eigenvalues on the four directions of @(W@)"),
 L("@(34@), @(120@) and @(340@) negative eigenvalues on the traceless fluctuations along the four directions of @(W@) (the compact check of Section~@ref{sec:status-F} counts four more from the trace)")),
('F5',L("every non-trivial unitary representation of @(@mathfrak{so}(5)@)"),L("every non-trivial unitary representation of @(@mathrm{Spin}(5)@)")),
]
for name,old,new in edits:
    assert s.count(old)==1,(name,'old',s.count(old))
    assert s.count(new)==0,(name,'new pre',s.count(new))
    s=s.replace(old,new)
    assert s.count(new)==1 and s.count(old)==0,(name,'post')
    print(name,'applied')
out=s.encode('ascii')
open(p,'wb').write(out)
print('r2 insert LF',len(out),hashlib.sha256(out).hexdigest())
