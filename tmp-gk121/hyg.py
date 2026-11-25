import hashlib, re
BS = chr(92)
pb = open(r'C:\Users\redgi\Projects\namcg-lab@gpu\proposals\121-n-hmassive-threshold\insert-n-hmassive-threshold.tex', 'rb').read()
s = pb.decode('ascii')
pat = BS + '(?:eq)?ref' + BS + '{([^}]*)}'
pat2 = BS + 'autoref' + BS + '{([^}]*)}'
refs = re.findall(pat, s) + re.findall(pat2, s)
print('refs:', sorted(set(refs)))
print('label count:', s.count(BS + 'label'), 'cite:', s.count(BS + 'cite'))
low = s.lower()
bad = [w for w in ['proposed', 'researcher', 'gatekeeper', 'as accepted', 'status:', 'priority', 'closes problem', 'milestone'] if w in low]
print('procwords:', bad)
t = open(r'C:\Users\redgi\Projects\namcg-lab@gpu\chapters\appH-microscopic-proofs.tex', 'rb').read()
a = b'Problems~F and~N remain open.'
join = a + b'\r\n\r\n'
assert t.count(join) == 1
new = t.replace(join, join + pb + b'\r\n', 1)
print('POST', len(new), hashlib.sha1(new).hexdigest()[:12])
