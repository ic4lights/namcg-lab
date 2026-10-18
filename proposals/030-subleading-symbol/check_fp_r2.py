"""Check phase-averaged FP/6 + dilaton = A, with FP/6 = (1/24)[v^2((q.a)^2-q^2 a^2)+q^2 (a.v)^2], dilaton = -(1/8) q^2 (a.v)^2 (factor-1/8 phase-averaged FP convention)."""
import numpy as np
rng=np.random.default_rng(1); eta=np.diag([-1.,1,1,1])
d=lambda x,y:x@eta@y
for _ in range(6):
    q,a,v=rng.normal(size=(3,4)); v=v-q*d(v,q)/d(q,q)
    A=(1/24)*(d(v,v)*(d(q,a)**2-d(q,q)*d(a,a))-2*d(q,q)*d(a,v)**2)
    fp=(1/24)*(d(v,v)*(d(q,a)**2-d(q,q)*d(a,a))+d(q,q)*d(a,v)**2)
    print(abs(fp-(1/8)*d(q,q)*d(a,v)**2-A))
