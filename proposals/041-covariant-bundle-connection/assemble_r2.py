import os, shutil
base = 'C:/Users/redgi/AppData/Local/Temp/claude/C--Users-redgi-Projects-namcg-lab/4d0177a0-6b3d-45ad-bb6d-645d2be99f00/scratchpad/'
for d in ('build041c', 'build041d'):
    if os.path.isdir(base + d):
        shutil.rmtree(base + d)
t = open('proposal-r2.template.md', encoding='utf-8').read()
ins = open('appH_insert.tex', encoding='utf-8').read().rstrip('\n')
b = open('appH_insert.tex', 'rb').read()
cc = open('compile_check.out.txt').read().strip().replace('\n', '; ')
t = t.replace('{{INSERT}}', ins).replace('{{BYTES}}', str(len(b))).replace('{{COMPILE}}', cc)
open('proposal-r2.md', 'w', encoding='utf-8', newline='\n').write(t)
os.remove('proposal-r2.template.md')
os.remove('compile_check.run.txt')
print(len(b), cc)
