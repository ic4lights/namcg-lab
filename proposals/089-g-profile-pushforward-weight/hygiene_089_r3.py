import hashlib,re
P='proposals/089-g-profile-pushforward-weight/'
raw=open(P+'insert-r3.tex','rb').read()
assert len(raw)==3974 and hashlib.sha256(raw).hexdigest()[:8]=='ccb89c9e'
B=bytes([92])
assert raw.endswith(b'\r\n')
body=raw[:-2]
assert b'\r' not in body and not [c for c in body if c<32] and body+b'\r\n'==raw
txt=raw.decode('utf-8'); low=txt.lower()
c=dict(bytes=len(raw),CRLF=raw.count(b'\r\n'),bareLF=raw.count(b'\n')-1,emph=txt.count('emph'),dollar=txt.count('$'),brack=txt.count('[')+txt.count(']'))
for k in ('cite','ref','eqref','label'): c[k]=raw.count(B+k.encode())
c['bs_eq']=raw.count(B+b'=')
c['lp']=raw.count(B+b'('); c['rp']=raw.count(B+b')')
c['accInMath']=sum(sp.count(B+bytes([q])) for sp in re.findall(B+b'\((.*?)'+B+b'\)',raw,re.S) for q in b"=^`'~.")
c['close']=txt.count('they close nothing in Problem~G.')
c['banned']={w:low.count(w) for w in 'status priority completion open critical programme derived'.split() if w in low}
c['nonascii']=sorted(set(hex(ord(ch)) for ch in txt if ord(ch)>127))
print(c)
ok=(c['dollar']==0 and c['brack']==0 and c['cite']==0 and c['ref']==0 and c['eqref']==0 and c['label']==0
 and c['emph']==1 and c['lp']==c['rp'] and c['close']==1 and c['bareLF']==0 and c['CRLF']==1
 and not c['banned'] and c['bs_eq']==0 and c['accInMath']==0)
for fn,hs in [('insert-r1.tex','602e63d9'),('insert-r2.tex','bba6adc4'),('insert-body.txt','bde45e06'),('insert-body-r2.txt','4f13d17f')]:
    assert hashlib.sha256(open(P+fn,'rb').read()).hexdigest()[:8]==hs,fn
print('frozen r1+r2 OK; HYGIENE','PASS' if ok else 'FAIL')
