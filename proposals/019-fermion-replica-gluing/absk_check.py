from fractions import Fraction as F
for n in range(1,10):
    ks=[F(-(n-1),2)+j for j in range(n)]
    s=sum(abs(k)/n for k in ks)
    t=F(n,4) if n%2==0 else F(n*n-1,4*n)
    assert s==t,(n,s,t)
    print(n,s)
print("sum|a_k| = n/4 (even), (n^2-1)/(4n) (odd): OK")
