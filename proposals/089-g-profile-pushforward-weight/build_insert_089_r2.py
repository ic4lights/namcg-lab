import hashlib
F='proposals/089-g-profile-pushforward-weight/'
b2=open(F+'insert-body-r2.txt','rb').read()
assert b2[-1:]==b'\n' and b2[-2:-1]!=b'\r'
c=b2[:-1]
assert b'\n' not in c and b'\r' not in c and not any(x<0x20 for x in c)
t2=c+b'\r\n'
open(F+'insert-r2.tex','wb').write(t2)
r1=open(F+'insert-r1.tex','rb').read()
assert len(r1)==3823 and hashlib.sha256(r1).hexdigest()[:8]=='602e63d9'
a=[(2027,2097,2179),(2175,2218,2319),(2862,3272,3424)]
assert t2[:2027]==r1[:2027]
assert t2[2179:2257]==r1[2097:2175] and t2[2319:2963]==r1[2218:2862]
assert t2[3424:-2]==r1[3272:-2]
assert len(t2)==len(r1)+152
rv=open(F+'review-r1.md','rb').read()
n2=t2[2027:2179];n3=t2[2257:2319];n1=t2[2963:3424]
for nm,n in [('F1',n1),('F2a',n2),('F2b',n3)]:
    assert n in rv,nm
    print(nm,'verbatim-in-review OK len',len(n))
print('insert-r2.tex size',len(t2),'sha8',hashlib.sha256(t2).hexdigest()[:8])
print('changed spans (old,new) lens',[(x[1]-x[0]) for x in a],[2179-2027,2319-2257,3424-2963])
