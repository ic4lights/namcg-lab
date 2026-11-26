import sympy as sp
n=2
xs=[sp.Symbol('x%d'%i) for i in range(4)]
Th=sp.zeros(4)
for a in range(4):
    for b in range(a+1,4):
        v=sp.Symbol('t%d%d'%(a,b),real=True); Th[a,b]=v; Th[b,a]=-v
def star(f,g,maxk=3):
    tot=f*g
    for k in range(1,maxk+1):
        t=sp.zeros(n)
        def rec(rem,fa,gb,idxs):
            if rem==0:
                c=[(sp.Rational(1,2)*sp.I)**3,(sp.Rational(1,2)*sp.I)**2,(sp.Rational(1,2)*sp.I)][0]
                return
        # explicit k-contraction
        t=sp.zeros(n)
        import itertools
        for combo in itertools.product([(a,b) for a in range(4) for b in range(4) if Th[a,b]!=0],repeat=k):
            da=[c[0] for c in combo]; db=[c[1] for c in combo]
            coef=1
            for (a,b) in combo: coef*=Th[a,b]
            ff=f; gg=g
            for a in da: ff=ff.diff(xs[a])
            for b in db: gg=gg.diff(xs[b])
            t=t+coef*ff*gg
        ck={(1):(sp.I/2),(2):sp.Rational(-1,8),(3):sp.Rational(-1,48)*sp.I}[k]
        tot=tot+ck*t
    return sp.expand(tot)
def gensym(tag,deg):
    mon=[sp.Integer(1)]+xs[:]
    if deg==2: mon+= [xs[i]*xs[j] for i in range(4) for j in range(i,4)]
    M=sp.zeros(n)
    for r in range(n):
        for c in range(n):
            M[r,c]=sum(sp.Symbol('%s_%d%d_%d'%(tag,r,c,q),complex=True)*m for q,m in enumerate(mon))
    return M
A=[gensym('A%d'%m,1) for m in range(4)]
Phi=gensym('P',2)
Xhat=[sp.eye(n)*xs[m]+sum((Th[m,r]*A[r] for r in range(4)), sp.zeros(n)) for m in range(4)]
def sc(f,g): return star(f,g)-star(g,f)
for mu in [0,2]:
    lhs=sc(Xhat[mu],Phi)
    rhs=sum((sp.I*Th[mu,nu]*(Phi.diff(xs[nu])-sp.I*sc(A[nu],Phi)) for nu in range(4)), sp.zeros(n))
    print('BRIDGE mu=%d exact:'%mu, sp.simplify(lhs-rhs)==sp.zeros(n))
    lhsact=sum((sp.I*Th[mu,nu]*(Phi.diff(xs[nu])-sp.I*star(A[nu],Phi)) for nu in range(4)), sp.zeros(n))
    d1=sp.simplify((lhsact-lhs)-sum((Th[mu,nu]*star(Phi,A[nu]) for nu in range(4)), sp.zeros(n)))
    print('mismatch left-bridge == +Th Phi A:', d1==sp.zeros(n))
c=sc(sp.eye(n),Phi)
print('u(1) const central invisible:', c==sp.zeros(n))
