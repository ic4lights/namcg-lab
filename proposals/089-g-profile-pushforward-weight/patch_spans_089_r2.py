import hashlib,os
F='proposals/089-g-profile-pushforward-weight'
S='proposals/089-g-profile-pushforward-weight'
b=open(F+'/insert-body.txt','rb').read()
assert hashlib.sha256(b).hexdigest()[:8]=='bde45e06'
assert b[-1:]==b'\n' and b[-2:-1]!=b'\r'
c=b[:-1]
def rd(n):return open(os.path.join(S,n),'rb').read().rstrip(b'\r\n')
n1=rd('frag-n1a.txt')+b' '+rd('frag-n1b.txt');n2=rd('frag-n2.txt');n3=rd('frag-n3.txt')
a1=b'For the wider class of product slot laws';e1=b'indexing the law.'
assert c.count(a1)==1 and c.count(e1)==1
p1=c.find(a1);p1e=c.find(e1)+len(e1);o1=c[p1:p1e]
o2=b'and has its unique minimum at the vertex of the largest slot variance:'
o3=b'this weight selects the single-slot profile'
assert c.count(o2)==1 and c.count(o3)==1 and c.count(o1)==1
p2=c.find(o2);p3=c.find(o3)
sp=sorted([(p1,p1e,o1,n1),(p2,p2+len(o2),o2,n2),(p3,p3+len(o3),o3,n3)])
for i in range(2):assert sp[i][1]<=sp[i+1][0]
d=c[:sp[0][0]]
for i,(s,e,o,n) in enumerate(sp):d+=n+(c[e:sp[i+1][0]] if i<2 else c[e:])
assert d==c.replace(o1,n1,1).replace(o2,n2,1).replace(o3,n3,1)
import difflib
ops=[op[:5] for op in difflib.SequenceMatcher(None,c,d,autojunk=False).get_opcodes() if op[0]!='equal']
oldw=[(s,e) for s,e,_,_ in sp];neww=[];cur=0
for (s,e,o,n) in sp:
    ns=s+cur;neww.append((ns,ns+len(n)));cur+=len(n)-(e-s)
def ins(a,w):return any(x[0]<=a<=x[1] for x in w)
for op in ops:assert ins(op[1],oldw) and ins(op[2],oldw) and ins(op[3],neww) and ins(op[4],neww)
assert len(d)-len(c)==sum(len(x[3])-len(x[2]) for x in sp)
open(F+'/insert-body-r2.txt','wb').write(d+b'\n')
h=hashlib.sha256(d+b'\n').hexdigest()
print('oldspans',[(s,e) for s,e,_,_ in sp]);print('newspans',neww)
print('lens',[(len(x[2]),len(x[3])) for x in sp],'delta',len(d)-len(c))
print('body-r2 size',len(d)+1,'sha8',h[:8])
print('o1h',o1[:50].decode());print('o1t',o1[-30:].decode())
