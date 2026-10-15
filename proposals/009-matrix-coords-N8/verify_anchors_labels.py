import re, os
root='C:/Users/redgi/Projects/namcg-lab/chapters/'
def rd(f): return open(root+f,encoding='utf-8',newline='').read().replace('\r\n','\n')
ch3=rd('ch03-matrix-action.tex'); h=rd('appH-microscopic-proofs.tex')
BS=chr(92)
a3=("in Chapter~14. The existence of such a map is enough for now."+chr(10)+chr(10)+BS+"section{Presentation B: the covariant condensate action}")
print("ch03 anchor count:",ch3.count(a3))
print("ch03 eq:Smatrix precedes anchor:",ch3.index(BS+"label{eq:Smatrix}")<ch3.index(a3))
aH=("Problem~F, and Problems~A, B, C and~D, remain open.\n\n"+BS+"section{Problem G: HBEV}")
print("appH anchor count:",h.count(aH))
alltex=''.join(rd(f) for f in os.listdir(root) if f.endswith('.tex'))
for l in ['def:matrix-coords','def:matrix-coords-ext','eq:Smatrix','eq:NC','eq:g-from-e','ass:emergent-op','ass:lorentzian','ass:locked-block','ass:dictionary','ass:frame-lock','rem:ch3-moyal-check','thm:Geff','def:composite-metric','sec:status-D','sec:status-E','eq:vev-is-frame','ass:EE','eq:Geff-structure','sec:ch3-two-presentations']:
    print(l, alltex.count(BS+'label{'+l+'}'))
bib=open('C:/Users/redgi/Projects/namcg-lab/bib/namcg.bib',encoding='utf-8').read()
for k in ['Steinacker2023','KumarSteinacker2023','Steinacker2026','Steinacker2016Gravity','IKKT1997','Steinacker2010']:
    print('bib',k,bib.count('{'+k+','))
