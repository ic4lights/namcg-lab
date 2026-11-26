"""Static check of appH_insert.tex (no build): brace balance, \( \) pairing, ASCII, no tabs/CR, macros used."""
import re
BS=chr(92)
t=open('appH_insert.tex','rb').read().decode('ascii')
depth=0; bad=False
for i,ch in enumerate(t):
    if ch=='{' and (i==0 or t[i-1]!=BS): depth+=1
    if ch=='}' and (i==0 or t[i-1]!=BS): depth-=1
    if depth<0: bad=True
print('brace depth at end',depth,'negative seen',bad)
print('inline math opens',t.count(BS+'('),'closes',t.count(BS+')'))
print('display opens',t.count(BS+'['),'closes',t.count(BS+']'))
macros=sorted(set(re.findall(BS*2+'([A-Za-z]+)',t)))
print('macros:',macros)
print('paragraphs (blank-line separated):',len([p for p in t.split('\n\n') if p.strip()]))
print('words:',len(t.split()))
