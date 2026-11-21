#!/usr/bin/env python3
"""Proposal 055 r2: summarize the two pdflatex pass logs of the build copy and hash the
applied appH + PDF. Usage: python -I build_summary_r2.py DIR_OF_BUILD_COPY"""
import re, hashlib, sys

d = sys.argv[1].rstrip('/')
for p in ('pass1.log', 'pass2.log'):
    b = open(d + '/' + p, 'rb').read().decode('latin1')
    pages = re.findall(r'Output written on .*?\((\d+) pages', b)
    undef = len(re.findall(r'^LaTeX Warning: Reference .* undefined', b, re.M))
    mult = len(re.findall(r'LaTeX Warning: Citation .* multiply defined|LaTeX Warning: Label .* multiply', b, re.M))
    warn = len(re.findall(r'^LaTeX Warning:', b, re.M))
    err = len(re.findall(r'^!', b, re.M))
    print('%s: pages=%s undefined_refs=%d multiply_defined=%d latex_warnings=%d excl_errors=%d'
          % (p, ','.join(pages), undef, mult, warn, err))
pdf = open(d + '/namcg-book7.pdf', 'rb').read()
print('pdf: %d B sha256 %s' % (len(pdf), hashlib.sha256(pdf).hexdigest()))
apph = open(d + '/chapters/appH-microscopic-proofs.tex', 'rb').read()
print('applied appH in copy: %d B CRLF %d bare-LF %d sha256 %s'
      % (len(apph), apph.count(b'\r\n'), apph.count(b'\n') - apph.count(b'\r\n'), hashlib.sha256(apph).hexdigest()))
