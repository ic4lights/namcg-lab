import sys, numpy as np
P='C:/Users/redgi/Projects/namcg-lab/proposals/071-d1-curved-torsion-backgrounds'; sys.path.insert(0,P)
import lin, core068 as K, tools068 as Tl, bg
KUP=np.array([-1.0,0,1.0,0]); qsq=lambda q: -q[0]**2+q[1]**2+q[2]**2+q[3]**2
rng=np.random.default_rng(99)
for name,(c,w) in [('trace-free',lin.bg_F()),('tau=1',lin.bg_F(tau=1.0))]:
    a=np.array([0,0.3,-0.5,0.7]); b=np.array([1.0,0,0,0])
    roots=Tl.char_roots(lambda t: K.M_op(c,w,K.chars(a+t*b)),30)
    al=[qsq(a+z*b)/(2*(KUP@(a+z*b))) for z in roots]
    print(name,'unrounded alpha (sorted):'); 
    for x in sorted(al,key=lambda z:(round(z.real,4),round(z.imag,4))): print('   %.10f %+.10fj'%(x.real,x.imag))
    S3=np.sqrt(3)
    cand=[S3,-S3,S3+1j,S3-1j,-S3+1j,-S3-1j,S3+2j,-S3+2j] if name=='trace-free' else [-0.5j,-1.5j,-2.5j]
    for al0 in cand:
        vals=[]
        for t in range(3):
            v=0.5*(rng.normal(size=3)+1j*rng.normal(size=3)); qt=np.array([np.sqrt(v@v),*v])
            sv=np.linalg.svd(K.M_op(c,w,K.chars(qt+al0*np.array([1.0,0,1.0,0]))),compute_uv=False); vals.append(sv[29]/sv[0])
        print('  converse exact alpha',np.round(al0,4),['%.1e'%x for x in vals])
    # also check -2i not present / control
    ctrl=[]
    for t in range(3):
        q=0.5*(rng.normal(size=4)+1j*rng.normal(size=4)); sv=np.linalg.svd(K.M_op(c,w,K.chars(q)),compute_uv=False); ctrl.append(sv[29]/sv[0])
    print('  control',['%.1e'%x for x in ctrl])
# Heisenberg + kB check with bg convention both signs
for sg in (1,-1):
    C=K.lie({(3,1):{2:1.0}}); W=sg*np.einsum('a,cd->acd',lin.KL,lin.Bg)
    B1,B2,T,R=bg.brackets(C,W,K.ETA); print('Heis + w=%+d kB: |B1| %.1e |B2| %.1e'%(sg,np.abs(B1).max(),np.abs(B2).max()))
