#!/bin/bash

python code/namcg_inspiral.py
python code/generate_uvlf.py
latexmk -C
latexmk -pdf -interaction=nonstopmode namcg-book7.tex
pdfinfo namcg-book7.pdf
pdffonts namcg-book7.pdf
