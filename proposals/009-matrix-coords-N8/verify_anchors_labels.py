import re, os
root='C:/Users/redgi/Projects/namcg-lab/chapters/'
def rd(f): return open(root+f,encoding='utf-8',newline='').read().replace('\r\n','\n')
ch3=rd('ch03-matrix-action.tex'); h=rd('appH-microscopic-proofs.tex')
BS=chr(92)
a3=("  analysis with a "+BS+"(c"+BS+")-number "+BS+"("+BS+"Theta^{"+BS+"mu"+BS+"nu}"+BS+")."+"\n"+BS+"end{definition}")
print("ch03 anchor count:",ch3.count(a3))
aH=("Problem~F, and Problems~A, B, C and~D, remain open.\n\n"+BS+"section{Problem G: HBEV}")
print("appH anchor count:",h.count(aH))
alltex=''.join(rd(f) for f in os.listdir(root) if f.endswith('.tex'))
for l in ['def:matrix-coords','def:matrix-coords-ext','eq:Smatrix','eq:NC','eq:g-from-e','ass:emergent-op','ass:lorentzian','ass:locked-block','ass:dictionary','ass:frame-lock','rem:ch3-moyal-check','thm:Geff','def:composite-metric','sec:status-D','sec:status-E','eq:vev-is-frame','ass:EE','eq:Geff-structure','sec:ch3-two-presentations']:
    print(l, alltex.count(BS+'label{'+l+'}'))
bib=open('C:/Users/redgi/Projects/namcg-lab/bib/namcg.bib',encoding='utf-8').read()
for k in ['Steinacker2023','KumarSteinacker2023','Steinacker2026','Steinacker2016Gravity','IKKT1997','Steinacker2010']:
    print('bib',k,bib.count('{'+k+','))
