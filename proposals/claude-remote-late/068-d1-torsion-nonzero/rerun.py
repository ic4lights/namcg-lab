"""Run a script of this folder under python -I (which does not put the script folder on sys.path).
Usage: python -I rerun.py s1_backgrounds.py > out.txt
"""
import os
import runpy
import sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
target = os.path.join(here, os.path.basename(sys.argv[1]))
sys.argv = [target] + sys.argv[2:]
runpy.run_path(target, run_name='__main__')
