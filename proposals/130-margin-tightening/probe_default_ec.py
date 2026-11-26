import subprocess, os, sys
# probe_default_ec.py - prints the default emergencystretch of the local
# toolchain. Run from anywhere inside a writable dir: python -I probe_default_ec.py
BS = chr(92)
doc = (BS + 'documentclass{book}' + chr(10) + BS + 'begin{document}' + chr(10)
       + BS + 'typeout{EC=' + BS + 'the' + BS + 'emergencystretch}' + chr(10)
       + BS + 'end{document}' + chr(10))
open('probe.tex', 'w', encoding='ascii').write(doc)
subprocess.run(['pdflatex', '-interaction=nonstopmode', 'probe.tex'],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
s = open('probe.log', encoding='utf-8', errors='replace').read()
i = s.find('EC=')
print('DEFAULT_EMERGECYSTRETCH', s[i:i+18].split(chr(10))[0].split('(')[0].strip())
